#!/usr/bin/env python3
"""Fast CLASSICAL-CV cell morphometry (skimage watershed) as method-3 triangulation.
NOT deep learning: DL (Cellpose cpsam) was attempted but CPU-impractical here (no usable GPU).
Uncalibrated (px, no µm), wavy pavement cells → approximate; reported for method-agreement only.
Usage: python cv_morphometry.py images/"""
import sys,os,glob,hashlib,collections,numpy as np
from PIL import Image
from skimage import filters, measure, segmentation, morphology, exposure
from scipy import ndimage as ndi
def fov(path,maxdim=700):
    a=np.asarray(Image.open(path).convert("L"),dtype=np.uint8)
    af=a.astype(float); thr=max(af.mean()+0.2*af.std(), af.max()*0.25); m=af>thr
    ys,xs=np.where(m)
    if len(xs)<100: return None,None
    a=a[ys.min():ys.max()+1, xs.min():xs.max()+1]; m=m[ys.min():ys.max()+1, xs.min():xs.max()+1]
    im=Image.fromarray(a)
    if max(im.size)>maxdim:
        s=maxdim/max(im.size); im=im.resize((int(im.size[0]*s),int(im.size[1]*s)))
        m=np.asarray(Image.fromarray(m.astype('uint8')*255).resize(im.size))>127
    return exposure.equalize_adapthist(np.asarray(im)), m
def seg(path):
    img,m=fov(path)
    if img is None: return None
    # cell walls = ridges (sato); interiors = low-ridge regions
    ridges=filters.sato(img, sigmas=range(1,4), black_ridges=False)
    walls=ridges>filters.threshold_otsu(ridges)
    interior=~walls & m
    interior=morphology.remove_small_objects(interior, 20)
    dist=ndi.distance_transform_edt(interior)
    coords=morphology.local_maxima(filters.gaussian(dist,1))
    markers=measure.label(coords & (dist>2))
    if markers.max()<2: return None
    lbl=segmentation.watershed(-dist, markers, mask=interior)
    props=[p for p in measure.regionprops(lbl) if 15<=p.area<=img.size*0.2]
    if not props: return None
    areas=[p.area for p in props]
    circ=[min(1,4*np.pi*p.area/(p.perimeter**2+1e-9)) for p in props if p.perimeter>0]
    return dict(n=len(props), area=float(np.median(areas)),
                circ=float(np.median(circ)), dens=len(props)/(m.sum()+1e-9)*1e4)
def main(imgdir):
    md5=lambda p:hashlib.md5(open(p,'rb').read()).hexdigest()
    seen=set(); g=collections.defaultdict(lambda:collections.defaultdict(list))
    for f in sorted(glob.glob(f"{imgdir}/*.jpg")):
        h=md5(f)
        if h in seen: print("DUP skip",os.path.basename(f)); continue
        seen.add(h); lab="control" if os.path.basename(f).startswith("control") else "treated"
        r=seg(f)
        if not r: print(os.path.basename(f),"seg-none"); continue
        print(f"{lab:8s} {os.path.basename(f)[:38]:38s} n={r['n']:4d} medArea={r['area']:6.1f} medCirc={r['circ']:.3f} dens/10kFOVpx={r['dens']:.2f}")
        for k in r: g[lab][k].append(r[k])
    print("\n=== group medians (control vs treated), classical watershed, uncalibrated ===")
    for k in ['n','area','circ','dens']:
        if g['control'][k] and g['treated'][k]:
            c=float(np.median(g['control'][k])); t=float(np.median(g['treated'][k]))
            print(f"  {k:5s} control={c:.3f} treated={t:.3f} Δ={100*(t-c)/(c+1e-9):+.1f}%")
if __name__=="__main__": main(sys.argv[1] if len(sys.argv)>1 else "images")
