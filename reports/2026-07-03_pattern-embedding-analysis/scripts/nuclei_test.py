import glob,os,numpy as np
from PIL import Image
from skimage.feature import blob_log
from skimage.feature import structure_tensor, structure_tensor_eigenvalues
from skimage.filters import gaussian
from scipy.stats import mannwhitneyu
D=os.path.expanduser("~/mc-work/drive_micro/conv")
def cliffs(a,b):
    a,b=np.array(a),np.array(b); gt=sum((x>y) for x in a for y in b); lt=sum((x<y) for x in a for y in b)
    return (gt-lt)/(len(a)*len(b))
def fov(path,dim=600):
    a=np.asarray(Image.open(path).convert("L"),float)
    thr=max(a.mean()+0.3*a.std(), a.max()*0.35); m=a>thr
    ys,xs=np.where(m)
    if len(xs)<200: return None,None,None
    rgb=np.asarray(Image.open(path).convert("RGB"),float)[ys.min():ys.max()+1,xs.min():xs.max()+1]
    L=a[ys.min():ys.max()+1,xs.min():xs.max()+1]; mm=m[ys.min():ys.max()+1,xs.min():xs.max()+1]
    im=Image.fromarray(L.astype('uint8')).resize((dim,dim)); L=np.asarray(im,float)
    rgbr=np.asarray(Image.fromarray(rgb.astype('uint8')).resize((dim,dim)),float)
    mr=np.asarray(Image.fromarray((mm*255).astype('uint8')).resize((dim,dim)))>127
    return L,rgbr,mr
def feats(path):
    L,rgb,m=fov(path)
    if L is None: return None
    R,G,B=rgb[...,0],rgb[...,1],rgb[...,2]
    # nuclei = dark blue-ish blobs: low green, inside FOV. detect dark spots via blob_log on inverted brightness
    inv=(255-L); inv[~m]=0; inv=gaussian(inv,1)
    blobs=blob_log(inv/inv.max(), min_sigma=2,max_sigma=8,num_sigma=6,threshold=0.12)
    fovarea=m.sum()
    nuc_area=np.sum(np.pi*(blobs[:,2]*np.sqrt(2))**2) if len(blobs) else 0
    naf=nuc_area/(fovarea+1e-9)                    # nuclear area fraction (dimensionless, zoom-inv)
    ndens=len(blobs)/(fovarea+1e-9)*1e4            # zoom-dependent (note)
    # structure tensor coherence (dimensionless, scale-robust)
    Axx,Axy,Ayy=structure_tensor(L,sigma=2,mode='reflect')
    l1,l2=structure_tensor_eigenvalues(np.stack([Axx,Axy,Ayy])) if False else (None,None)
    from skimage.feature import structure_tensor_eigenvalues as ste
    ev=ste([Axx,Axy,Ayy]); l1,l2=ev[0],ev[1]
    coh=((l1-l2)/(l1+l2+1e-9))
    coherence=float(np.mean(coh[m]))
    return dict(nuclear_area_frac=float(naf), nuclei_density=float(ndens), coherence=coherence)
g={'control':[], 'treated':[]}
for lab in ['control','treated']:
    for f in sorted(glob.glob(f"{D}/{lab}/*.png")):
        r=feats(f)
        if r: g[lab].append(r)
print(f"n control={len(g['control'])} treated={len(g['treated'])}")
print(f"{'metric':18s} {'ctrl_med':>9s} {'trt_med':>9s} {'Δ%':>7s} {'MWU-p':>7s} {'Cliff δ':>8s}")
for k in ['nuclear_area_frac','nuclei_density','coherence']:
    c=[d[k] for d in g['control']]; t=[d[k] for d in g['treated']]
    cm,tm=np.median(c),np.median(t)
    p=mannwhitneyu(c,t).pvalue; d=cliffs(t,c)
    mag='negligible' if abs(d)<0.14 else 'small' if abs(d)<0.33 else 'medium' if abs(d)<0.47 else 'LARGE'
    print(f"{k:18s} {cm:9.4f} {tm:9.4f} {100*(tm-cm)/(abs(cm)+1e-9):+7.1f} {p:7.4f} {d:+8.2f} ({mag})")
