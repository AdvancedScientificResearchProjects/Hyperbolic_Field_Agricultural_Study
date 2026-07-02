#!/usr/bin/env python3
"""Parse LeafNet statistic.txt outputs → zoom-invariant cell/stomata metrics, control vs treated.
LeafNet = plant-specific model (stomata + pavement cells). Method 5 of the triangulation.
Key metrics are DIMENSIONLESS (zoom-invariant): stomatal index, stoma aspect ratio, cell-size CV.
Usage: python leafnet_parse.py <leafnet_out_dir>"""
import sys,os,glob,ast,collections,statistics as st
def parse(fp):
    d={}
    for line in open(fp):
        if ':' not in line: continue
        k,v=line.split(':',1); v=v.strip()
        try: d[k]=ast.literal_eval(v)
        except Exception: d[k]=v
    return d
def cv(xs):
    xs=[x for x in xs if x>0]
    return (st.pstdev(xs)/st.mean(xs)) if len(xs)>1 and st.mean(xs)>0 else float('nan')
def main(outdir):
    g=collections.defaultdict(lambda:collections.defaultdict(list)); rows=[]
    for fp in sorted(glob.glob(f"{outdir}/*_statistic.txt")):
        d=parse(fp); name=os.path.basename(fp).replace('.jpg_statistic.txt','')
        lab="control" if name.startswith("control") else "treated"
        sc=float(d.get('stoma_count',0)); cc=float(d.get('cell_count',0))
        si=sc/(sc+cc) if (sc+cc)>0 else float('nan')      # stomatal index (dimensionless)
        asp=d.get('stoma_aspects',[]); asp=[a for a in asp if isinstance(a,(int,float))]
        cs=d.get('cell_sizes',[]); cs=[c for c in cs if isinstance(c,(int,float))]
        r=dict(stom_index=si, stoma_aspect=(st.median(asp) if asp else float('nan')),
               cell_count=cc, cell_size_cv=cv(cs), stoma_count=sc)
        rows.append((lab,name,r))
        print(f"{lab:8s} {name[:34]:34s} stomIdx={si:.3f} stomaAsp={r['stoma_aspect']:.3f} cells={cc:.0f} stomata={sc:.0f} cellCV={r['cell_size_cv']:.3f}")
        for k,v in r.items():
            if v==v: g[lab][k].append(v)
    print("\n=== group medians (control vs treated) — LeafNet plant-specific ===")
    for k in ['stom_index','stoma_aspect','cell_count','cell_size_cv']:
        if g['control'][k] and g['treated'][k]:
            c=st.median(g['control'][k]); t=st.median(g['treated'][k])
            inv="(zoom-invariant)" if k in('stom_index','stoma_aspect','cell_size_cv') else "(scale-dep)"
            print(f"  {k:14s} control={c:.4f} treated={t:.4f} Δ={100*(t-c)/(c+1e-9):+.1f}% {inv}")
if __name__=="__main__": main(sys.argv[1] if len(sys.argv)>1 else ".")
