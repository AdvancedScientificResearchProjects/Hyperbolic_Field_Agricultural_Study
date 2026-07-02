#!/usr/bin/env python3
"""Lightweight CV texture/sharpness metrics inside the eyepiece field-of-view.
Group-agnostic; label mapping applied only at aggregation (see blind_key.tsv).
Dedup: byte-identical frames (same MD5) counted once. Usage: python cv_texture.py images/ blind_key.tsv"""
import sys,os,glob,csv,hashlib,collections,numpy as np
from PIL import Image
def fov(path):
    a=np.asarray(Image.open(path).convert("L"),dtype=float)
    thr=max(a.mean()+0.2*a.std(), a.max()*0.25); m=a>thr
    ys,xs=np.where(m)
    if len(xs)<100: return None,None
    a=a[ys.min():ys.max()+1, xs.min():xs.max()+1]; m=m[ys.min():ys.max()+1, xs.min():xs.max()+1]
    return a,m
def metrics(path):
    a,m=fov(path)
    if a is None: return None
    v=a[m]; gy,gx=np.gradient(a); g=np.hypot(gx,gy)[m]
    # Laplacian variance = focus/sharpness proxy
    lap=np.gradient(np.gradient(a,axis=0),axis=0)+np.gradient(np.gradient(a,axis=1),axis=1)
    return dict(edge_density=float((g>g.mean()+g.std()).mean()),
                contrast=float(v.std()/(v.mean()+1e-6)), std=float(v.std()),
                sharpness_lapvar=float(lap[m].var()))
def main(imgdir,keyf):
    md5=lambda p:hashlib.md5(open(p,'rb').read()).hexdigest()
    seen={}; rows=[]
    key={r['blind']:r['label'] for r in csv.DictReader(open(keyf),delimiter='\t')}
    # map label by msg-id embedded in filename
    for f in sorted(glob.glob(f"{imgdir}/*.jpg")):
        h=md5(f)
        if h in seen: print("DUP skip",os.path.basename(f),"==",seen[h]); continue
        seen[h]=os.path.basename(f)
        lab="control" if os.path.basename(f).startswith("control") else "treated"
        mt=metrics(f); rows.append((lab,os.path.basename(f),mt))
    g=collections.defaultdict(lambda:collections.defaultdict(list))
    for lab,f,mt in rows:
        for k,v in mt.items(): g[lab][k].append(v)
    print(f"\nunique frames: control={len(g['control']['edge_density'])} treated={len(g['treated']['edge_density'])}")
    for k in ["edge_density","contrast","std","sharpness_lapvar"]:
        c=float(np.median(g['control'][k])); t=float(np.median(g['treated'][k]))
        print(f"  {k:18s} control={c:.4f} treated={t:.4f} Δ={100*(t-c)/(c+1e-9):+.1f}%")
if __name__=="__main__": main(sys.argv[1] if len(sys.argv)>1 else "images", sys.argv[2] if len(sys.argv)>2 else "blind_key.tsv")
