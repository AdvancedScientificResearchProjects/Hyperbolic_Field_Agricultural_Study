import glob,os,numpy as np,torch
from PIL import Image
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, permutation_test_score
from sklearn.linear_model import LinearRegression
D=os.path.expanduser("~/mc-work/drive_micro/conv")
def fov(path):
    a=np.asarray(Image.open(path).convert("L"),float)
    thr=max(a.mean()+0.3*a.std(), a.max()*0.35); m=a>thr
    ys,xs=np.where(m)
    if len(xs)<200: return None,None
    rgb=np.asarray(Image.open(path).convert("RGB"))
    crop=rgb[ys.min():ys.max()+1,xs.min():xs.max()+1]
    diam=(xs.max()-xs.min()+ys.max()-ys.min())/2.0
    return crop, (a[m].mean(), diam, (np.asarray(Image.open(path).convert("RGB"),float)[...,1][m]/ (np.asarray(Image.open(path).convert("RGB"),float).sum(2)[m]+1e-6)).mean())
dev='cuda'
model=torch.hub.load('facebookresearch/dinov2','dinov2_vits14',verbose=False).to(dev).eval()
mean=torch.tensor([0.485,0.456,0.406]).view(3,1,1); std=torch.tensor([0.229,0.224,0.225]).view(3,1,1)
X=[]; y=[]; conf=[]
for lab,dd,cls in [('control','control',0),('treated','treated',1)]:
    for f in sorted(glob.glob(f"{D}/{dd}/*.png")):
        crop,c=fov(f)
        if crop is None: continue
        im=Image.fromarray(crop).resize((224,224))
        t=torch.from_numpy(np.asarray(im,float).transpose(2,0,1)/255.).float()
        t=((t-mean)/std).unsqueeze(0).to(dev)
        with torch.no_grad(): emb=model(t).cpu().numpy()[0]
        X.append(emb); y.append(cls); conf.append(c)
X=np.array(X); y=np.array(y); conf=np.array(conf)
print(f"embeddings: {X.shape}  control={ (y==0).sum() } treated={ (y==1).sum() }")
cv=StratifiedKFold(5,shuffle=True,random_state=0)
def ptest(Xin,name):
    for clf,cn in [(make_pipeline(StandardScaler(),LogisticRegression(C=0.1,max_iter=2000,class_weight='balanced')),'LogReg'),
                   (make_pipeline(StandardScaler(),KNeighborsClassifier(5)),'kNN5')]:
        s,ps,p=permutation_test_score(clf,Xin,y,cv=cv,scoring='balanced_accuracy',n_permutations=1000,random_state=0,n_jobs=4)
        print(f"  [{name}/{cn}] balanced_acc={s:.3f}  perm_null_mean={ps.mean():.3f}  p={p:.4f}  {'*SIGNIF*' if p<0.05 else 'ns'}")
print("\n=== MAIN: DINOv2 embeddings → class ===")
ptest(X,"emb")
print("\n=== NEG-CONTROL 1: confounds (brightness,zoom,green) alone → class ===")
ptest(conf,"confound")
print("\n=== NEG-CONTROL 2: do embeddings encode brightness/zoom? (R2) ===")
for i,nm in enumerate(['brightness','zoom_diam','green_frac']):
    r2=LinearRegression().fit(StandardScaler().fit_transform(X),conf[:,i]).score(StandardScaler().fit_transform(X),conf[:,i])
    print(f"  emb→{nm}: R2(train)={r2:.2f}")
print("\n=== NEG-CONTROL 3: class signal AFTER regressing out confounds from embeddings ===")
Xr=X - LinearRegression().fit(conf, X).predict(conf)   # residualize embeddings on confounds
ptest(Xr,"emb_resid")
