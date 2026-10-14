#!/usr/bin/env python3
"""Exact coefficient and rational-certificate checks; no floating arithmetic."""
from fractions import Fraction as F
import json

def factors(n):
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def mobius(n):
    f=factors(n)
    return 0 if any(v>1 for v in f.values()) else (-1)**len(f)

count=boundaries=0
for m in range(1,501):
    mm=mobius(m); a=1-mm
    for d in range(2,129):
        fd=factors(d)
        if len(fd)!=1: continue
        p,k=next(iter(fd.items()))
        md=mobius(m*d)
        coefficient=a*(mm-md)
        expected=(-4 if k==1 and m%p else -2) if mm==-1 else 0
        assert coefficient==expected
        assert -coefficient<=(1-mm)**2
        count+=1
        for N in {m-1,m,m*d-1,m*d}:
            finite=a*(m<=N)*((1-md)*(m*d<=N)-a*(m<=N))
            defect=finite-coefficient
            assert not defect or m*d>N
            assert abs(defect)<=8
            boundaries+=1
ratio=F(2807,1600)
p1=F(400,401)
assert ratio<2
assert 4*p1/ratio>2
score_margin=F(621,200)-F(48521,16000)
assert score_margin==F(1159,16000)>0
series=F(1,65536)/(1-F(1,2**29))
assert series<F(1,60000)
assert 3*F(69,100)-F(1,60000)>2
result={
 'coefficient_cases':count,
 'finite_boundary_cases':boundaries,
 'posterior_ratio_majorant':str(ratio),
 'conditional_denominator_lower_bound':str(4*p1/ratio),
 'uniform_score_extra_margin':str(score_margin),
 'full_incidence_series_majorant':str(series),
 'spatial_gap_rational_lower_bound':str(3*F(69,100)-F(1,60000)),
 'status':'all exact checks passed'
}
print(json.dumps(result,indent=2,sort_keys=True))
