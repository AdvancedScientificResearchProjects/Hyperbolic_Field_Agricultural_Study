#!/usr/bin/env python3
"""Multi-method PATTERN analysis (control vs treated) on FOV-cropped eyepiece microscopy.
Zoom-invariant descriptors (per research): box-counting fractal dimension, lacunarity,
FFT radial slope + anisotropy, GLCM Haralick, dark-nucleus density.
Reports group medians + within-vs-between spread (null-test proxy)."""
import glob,os,sys,numpy as np,collections,statistics as st
from PIL import Image
from skimage.feature import graycomatrix, graycoprops
from skimage.filters import threshold_otsu, sato
def fov(path,dim=512):
    a=np.asarray(Image.open(path).convert("L"),float)
    thr=max(a.mean()+0.3*a.std(), a.max()*0.35); m=a>thr
    ys,xs=np.where(m)
    if len(xs)<200: return None,None,None
    a=a[ys.min():ys.max()+1,xs.min():xs.max()+1]; m=m[ys.min():ys.max()+1,xs.min():xs.max()+1]
    rgb=np.asarray(Image.open(path).convert("RGB"),float)
    R=rgb[...,0]; # (unused per-channel here)
    im=Image.fromarray(a.astype('uint8')).resize((dim,dim)); a=np.asarray(im,float)
    mm=np.asarray(Image.fromarray((m*255).astype('uint8')).resize((dim,dim)))>127
    return a,mm,path
def boxcount(binimg):
    Z=binimg>0; s=min(Z.shape); ns=[]; ks=[]
    k=2
    while k< s//2:
        S=Z[:(Z.shape[0]//k)*k,:(Z.shape[1]//k)*k].reshape(Z.shape[0]//k,k,Z.shape[1]//k,k)
        cnt=S.any(axis=(1,3)).sum(); 
        if cnt>0: ns.append(cnt); ks.append(k)
        k*=2
    if len(ks)<3: return float('nan'),0
    c=np.polyfit(np.log(1/np.array(ks)),np.log(ns),1)
    # R2
    p=np.poly1d(c); yhat=p(np.log(1/np.array(ks))); ybar=np.mean(np.log(ns))
    r2=1-np.sum((np.log(ns)-yhat)**2)/(np.sum((np.log(ns)-ybar)**2)+1e-9)
    return float(c[0]), float(r2)
def lacunarity(binimg,box=32):
    Z=binimg.astype(float); H,W=Z.shape; vals=[]
    for i in range(0,H-box,box):
        for j in range(0,W-box,box):
            vals.append(Z[i:i+box,j:j+box].sum())
    vals=np.array(vals); m=vals.mean(); 
    return float((vals.var()/(m*m+1e-9))+1) if m>0 else float('nan')
def fft_aniso(a,mask):
    A=a.copy(); A[~mask]=a[mask].mean(); A=A-A.mean()
    F=np.abs(np.fft.fftshift(np.fft.fft2(A)))**2
    H,W=F.shape; cy,cx=H//2,W//2
    y,x=np.indices(F.shape); r=np.hypot(y-cy,x-cx); th=np.arctan2(y-cy,x-cx)
    mid=(r>10)&(r<H//3)
    # radial slope
    rr=r[mid].astype(int); pw=F[mid]
    rb=np.bincount(rr,pw)/(np.bincount(rr)+1e-9); rb=rb[10:H//3]
    sl=np.polyfit(np.log(np.arange(10,10+len(rb))+1),np.log(rb+1e-9),1)[0]
    # angular anisotropy: std of energy over angle bins
    ab=np.zeros(18)
    for b in range(18):
        sel=mid&(th>=-np.pi+b*np.pi/9)&(th<-np.pi+(b+1)*np.pi/9)
        ab[b]=F[sel].sum()
    aniso=float(ab.std()/(ab.mean()+1e-9))
    return float(sl),aniso
def dark_nuclei(path,mask,dim=512):
    rgb=np.asarray(Image.open(path).convert("RGB"),float)
    im=Image.fromarray(rgb.astype('uint8')).resize((dim,dim)); rgb=np.asarray(im,float)
    R,G,B=rgb[...,0],rgb[...,1],rgb[...,2]
    # dark-blue nuclei: low overall brightness + blue>=green locally, inside FOV
    br=(R+G+B)/3
    dark=(br< (br[mask].mean()-0.6*br[mask].std())) & mask
    return float(dark.mean())
def glcm_feats(a,mask):
    q=(np.clip(a,0,255)/32).astype(np.uint8) # 8 levels
    q[~mask]=0
    g=graycomatrix(q,distances=[4,8],angles=[0,np.pi/2],levels=8,symmetric=True,normed=True)
    return {f'glcm_{p}':float(graycoprops(g,p).mean()) for p in ['contrast','homogeneity','energy','correlation']}
def analyze(path):
    a,m,_=fov(path)
    if a is None: return None
    ridges=sato(a,sigmas=range(1,4),black_ridges=False); walls=ridges>threshold_otsu(ridges)
    fd,r2=boxcount(walls&m)
    lac=lacunarity((walls&m))
    sl,aniso=fft_aniso(a,m)
    d=dict(fractal_dim=fd,fd_r2=r2,lacunarity=lac,fft_slope=sl,fft_aniso=aniso,dark_nuclei=dark_nuclei(path,m))
    d.update(glcm_feats(a,m)); return d
def main():
    g=collections.defaultdict(lambda:collections.defaultdict(list))
    for lab,dd in [('control','conv/control'),('treated','conv/treated')]:
        for f in sorted(glob.glob(f'{dd}/*.png')):
            r=analyze(f)
            if r:
                for k,v in r.items():
                    if v==v: g[lab][k].append(v)
    keys=['fractal_dim','lacunarity','fft_slope','fft_aniso','dark_nuclei','glcm_contrast','glcm_homogeneity','glcm_energy','glcm_correlation']
    print(f"n control={len(g['control']['fractal_dim'])} treated={len(g['treated']['fractal_dim'])}")
    print(f"{'metric':16s} {'control(med)':>12s} {'treated(med)':>12s} {'Δ%':>7s} {'sep':>6s}  (sep=|Δmed|/pooled_IQR, >1 = между>внутри)")
    for k in keys:
        c=np.array(g['control'][k]); t=np.array(g['treated'][k])
        cm,tm=np.median(c),np.median(t)
        iqr=(np.subtract(*np.percentile(np.concatenate([c,t]),[75,25])))+1e-9
        sep=abs(tm-cm)/iqr
        print(f"{k:16s} {cm:12.3f} {tm:12.3f} {100*(tm-cm)/(abs(cm)+1e-9):+7.1f} {sep:6.2f}")
main()
