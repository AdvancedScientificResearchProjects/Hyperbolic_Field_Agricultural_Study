#!/usr/bin/env python3
"""Cellpose segmentation + morphometry on eyepiece leaf microscopy, control vs treated.
Dedup by MD5; FOV-crop; downscale for CPU. Method 3 of the triangulation (see report).
Usage: python cellpose_morphometry.py images/  (run inside the report dir)
NOTE: uncalibrated (no µm scale) — areas are in pixels; pavement cells are wavy, so
segmentation is approximate. Reported as method-agreement check, not absolute morphometry."""
import sys,os,glob,hashlib,collections,numpy as np
from PIL import Image
from skimage.measure import regionprops
def fov_crop(path,maxdim=640):
    im=Image.open(path).convert("L"); a=np.asarray(im,dtype=float)
    thr=max(a.mean()+0.2*a.std(), a.max()*0.25); m=a>thr
    ys,xs=np.where(m)
    if len(xs)<100: return None
    a=a[ys.min():ys.max()+1, xs.min():xs.max()+1]
    im=Image.fromarray(a.astype('uint8'))
    if max(im.size)>maxdim:
        s=maxdim/max(im.size); im=im.resize((int(im.size[0]*s),int(im.size[1]*s)))
    return np.asarray(im)
def main(imgdir):
    from cellpose import models
    try: model=models.CellposeModel(gpu=False)
    except Exception as e: print("model init:",e); model=models.CellposeModel(gpu=False)
    md5=lambda p:hashlib.md5(open(p,'rb').read()).hexdigest()
    seen=set(); g=collections.defaultdict(lambda:collections.defaultdict(list))
    for f in sorted(glob.glob(f"{imgdir}/*.jpg")):
        h=md5(f)
        if h in seen: print("DUP skip",os.path.basename(f)); continue
        seen.add(h)
        lab="control" if os.path.basename(f).startswith("control") else "treated"
        img=fov_crop(f)
        if img is None: continue
        try:
            out=model.eval(img, flow_threshold=0.4, cellprob_threshold=0.0)
            masks=out[0]
        except Exception as e:
            print("eval fail",os.path.basename(f),e); continue
        props=regionprops(masks)
        props=[p for p in props if p.area>=15]
        if not props: print(os.path.basename(f),"0 cells"); continue
        areas=[p.area for p in props]
        circ=[min(1.0,4*np.pi*p.area/(p.perimeter**2+1e-9)) for p in props if p.perimeter>0]
        ecc=[p.eccentricity for p in props]
        dens=len(props)/(img.shape[0]*img.shape[1])*1e4  # cells per 10k px
        print(f"{lab:8s} {os.path.basename(f)[:40]:40s} n={len(props):4d} medArea={np.median(areas):7.1f} medCirc={np.median(circ):.3f} dens/10kpx={dens:.2f}")
        g[lab]['n'].append(len(props)); g[lab]['area'].append(float(np.median(areas)))
        g[lab]['circ'].append(float(np.median(circ))); g[lab]['dens'].append(dens); g[lab]['ecc'].append(float(np.median(ecc)))
    print("\n=== group medians (control vs treated) ===")
    for k in ['n','area','circ','dens','ecc']:
        if g['control'][k] and g['treated'][k]:
            c=float(np.median(g['control'][k])); t=float(np.median(g['treated'][k]))
            print(f"  {k:6s} control={c:.3f} treated={t:.3f} Δ={100*(t-c)/(c+1e-9):+.1f}%")
if __name__=="__main__": main(sys.argv[1] if len(sys.argv)>1 else "images")
