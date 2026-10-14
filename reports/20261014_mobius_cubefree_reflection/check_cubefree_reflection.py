"""Exact integer-coefficient checks of the reflected Möbius divisor-cut law."""
import json
from pathlib import Path

def factor(n):
    f={}; p=2
    while p*p<=n:
        while n%p==0:
            f[p]=f.get(p,0)+1;n//=p
        p+=1
    if n>1:f[n]=f.get(n,0)+1
    return f

def divs(n):
    out=[1]
    for p,v in factor(n).items():
        out=[d*p**j for d in out for j in range(v+1)]
    return sorted(out)

def mu(n):
    f=factor(n)
    return 0 if any(v>1 for v in f.values()) else (-1)**len(f)

def clean(d):return {p:c for p,c in d.items() if c}

def direct(L,lo,hi,N=None):
    # The midpoint is (lo+hi)/2, kept exact throughout.
    twice_t=lo+hi; out={}
    for m in divs(L):
        for e in divs(L):
            if e%m or not(2*m<twice_t<2*e):continue
            if N is not None and (m>N or L//e>N):continue
            k=e//m; f=factor(k)
            if len(f)!=1:continue
            p=next(iter(f));out[p]=out.get(p,0)+mu(m)*mu(L//e)
    return clean(out)

def predicted(L,lo,hi):
    f=factor(L); out={}; twice_t=lo+hi
    if any(v>=3 for v in f.values()):return out
    a=1;b=1
    for p,v in f.items():
        if v==1:a*=p
        else:b*=p
    for p in factor(a):
        c=-mu(a)*sum(2*b*d<twice_t<2*b*p*d for d in divs(a//p))
        if c:out[p]=c
    return out

checks=0
for L in range(2,501):
    ds=divs(L)
    for lo,hi in zip(ds,ds[1:]):
        assert direct(L,lo,hi)==predicted(L,lo,hi),(L,lo,hi)
        assert direct(L,lo,hi,N=L)==predicted(L,lo,hi)
        checks+=1
result={'integer_labels_checked':500,'open_divisor_cells_checked':checks,
        'exact_prime_log_coefficients':True,'all_passed':True,
        'scope':'Coefficient algebra only, not positivity or RH.'}
Path(__file__).with_name('cubefree_reflection_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
