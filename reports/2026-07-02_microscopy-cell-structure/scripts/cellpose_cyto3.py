#!/usr/bin/env python3
"""Cellpose cyto3 (DL) segmentation + morphometry on GPU — method 4 of the triangulation.
Control vs treated broccoli leaf microscopy. Dedup by MD5; FOV-crop; uncalibrated (px).
Usage: python cellpose_cyto3.py images/   (needs GPU torch + cellpose 3.x)"""
import sys,os,glob,hashlib,collections,numpy as np
from PIL import Image
from skimage import measure
def fov(path,maxdim=700):
    a=np.asarray(Image.open(path).convert("L"),dtype=np.uint8)
    af=a.astype(float); thr=max(af.mean()+0.2*af.std(), af.max()*0.25); m=af>thr
    ys,xs=np.where(m)
    if len(xs)<100: return None
    a=a[ys.min():ys.max()+1, xs.min():xs.max()+1]
    im=Image.fromarray(a)
    if max(im.size)>maxdim:
        s=maxdim/max(im.size); im=im.resize((int(im.size[0]*s),int(im.size[1]*s)))
    return np.asarray(im)
def main(imgdir):
    from cellpose import models
    try: model=models.Cellpose(gpu=True, model_type='cyto3')
    except Exception:
        model=models.CellposeModel(gpu=True, model_type='cyto3')
    import torch; print("GPU:",torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else "-", flush=True)
    md5=lambda p:hashlib.md5(open(p,'rb').read()).hexdigest()
    seen=set(); g=collections.defaultdict(lambda:collections.defaultdict(list))
    for f in sorted(glob.glob(f"{imgdir}/*.jpg")):
        h=md5(f)
        if h in seen: print("DUP skip",os.path.basename(f),flush=True); continue
        seen.add(h); lab="control" if os.path.basename(f).startswith("control") else "treated"
        img=fov(f)
        try:
            out=model.eval(img, diameter=None, channels=[0,0])
            masks=out[0]
        except Exception as e:
            print("eval fail",os.path.basename(f),repr(e)[:120],flush=True); continue
        props=[p for p in measure.regionprops(masks) if p.area>=20]
        if not props: print(os.path.basename(f),"0 cells",flush=True); continue
        areas=[p.area for p in props]
        circ=[min(1,4*np.pi*p.area/(p.perimeter**2+1e-9)) for p in props if p.perimeter>0]
        dens=len(props)/(img.shape[0]*img.shape[1])*1e4
        print(f"{lab:8s} {os.path.basename(f)[:38]:38s} n={len(props):4d} medArea={np.median(areas):7.1f} medCirc={np.median(circ):.3f} dens/10kpx={dens:.2f}",flush=True)
        g[lab]['n'].append(len(props)); g[lab]['area'].append(float(np.median(areas)))
        g[lab]['circ'].append(float(np.median(circ))); g[lab]['dens'].append(dens)
    print("\n=== group medians (control vs treated), Cellpose cyto3 GPU ===",flush=True)
    for k in ['n','area','circ','dens']:
        if g['control'][k] and g['treated'][k]:
            c=float(np.median(g['control'][k])); t=float(np.median(g['treated'][k]))
            print(f"  {k:5s} control={c:.3f} treated={t:.3f} Δ={100*(t-c)/(c+1e-9):+.1f}%",flush=True)
if __name__=="__main__": main(sys.argv[1] if len(sys.argv)>1 else "images")
