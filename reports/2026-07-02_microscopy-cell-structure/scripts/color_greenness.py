#!/usr/bin/env python3
"""Greenness / color analysis inside the eyepiece FOV, control vs treated (method 6).
Added after Denis noted a naked-eye green difference the grayscale methods (1-5) discarded.
g_chroma = G/(R+G+B) is brightness-invariant; ExG = 2G-R-B is brightness-sensitive.
Usage: python color_greenness.py images/"""
import sys,os,glob,hashlib,collections,numpy as np,statistics as st
from PIL import Image
def metrics(path):
    a=np.asarray(Image.open(path).convert("RGB"),float); L=np.asarray(Image.open(path).convert("L"),float)
    thr=max(L.mean()+0.2*L.std(), L.max()*0.25); m=L>thr
    R,G,B=a[...,0][m],a[...,1][m],a[...,2][m]; S=R+G+B+1e-6
    mx=np.maximum(np.maximum(R,G),B); mn=np.minimum(np.minimum(R,G),B); df=mx-mn+1e-6
    hue=np.where(mx==R,(60*((G-B)/df))%360,np.where(mx==G,60*((B-R)/df)+120,60*((R-G)/df)+240))
    return dict(g_chroma=float(np.mean(G/S)), ExG=float(np.mean(2*G-R-B)),
                green_hue_frac=float(np.mean((hue>=70)&(hue<=170))))
def main(d):
    seen={}; g=collections.defaultdict(lambda:collections.defaultdict(list))
    for f in sorted(glob.glob(f"{d}/*.jpg")):
        h=hashlib.md5(open(f,'rb').read()).hexdigest()
        if h in seen: continue
        seen[h]=1; lab="control" if os.path.basename(f).startswith("control") else "treated"
        mt=metrics(f); print(f"{lab:8s} {os.path.basename(f)[:34]:34s} gchroma={mt['g_chroma']:.3f} ExG={mt['ExG']:+5.1f} ghue={mt['green_hue_frac']:.3f}")
        for k,v in mt.items(): g[lab][k].append(v)
    print("\n=== group medians ===")
    for k in ['g_chroma','ExG','green_hue_frac']:
        c=st.median(g['control'][k]); t=st.median(g['treated'][k]); print(f"  {k:14s} control={c:.3f} treated={t:.3f} Δ={t-c:+.3f}")
if __name__=="__main__": main(sys.argv[1] if len(sys.argv)>1 else "images")
