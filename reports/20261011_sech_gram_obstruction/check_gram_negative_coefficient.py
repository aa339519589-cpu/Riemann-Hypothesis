"""Rigorous fixed-point interval certificate. Every operation rounds outwards.
No numerical sampling; pi enclosure uses Machin's formula and alternating sums.
The asymptotic/uniqueness proof is separate in REPORT.md.
"""
from fractions import Fraction as F
from math import comb
import json
DIGITS=100
S=10**DIGITS
N=24

def ceildiv(a,b):return -((-a)//b)
def atan_bounds(q,n):
    s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F())
    t=F((-1)**n,(2*n+1)*q**(2*n+1))
    return min(s,s+t),max(s,s+t)
a,b=atan_bounds(5,80)
c,d=atan_bounds(239,24)
pl,ph=16*a-4*d,16*b-4*c
assert pl>F(314159265358979323846264338327950288419716939937510,10**50)
assert ph<F(314159265358979323846264338327950288419716939937511,10**50)
class I:
    def __init__(self,lo,hi=None,scaled=False):
        if scaled:self.lo,self.hi=lo,hi
        else:
            q=F(lo);self.lo=(q.numerator*S)//q.denominator;self.hi=ceildiv(q.numerator*S,q.denominator)
    @classmethod
    def pair(cls,lo,hi):return cls(lo,hi,True)
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I.pair(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I.pair(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I(o) if not isinstance(o,I) else self+-o
    def __rsub__(self,o):return I(o)+-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        p=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I.pair(min(p)//S,ceildiv(max(p),S))
    __rmul__=__mul__
    def __truediv__(self,q):return self*F(1,q)
    def out(self,digits=18):
        T=10**digits
        return {'lo_numerator':self.lo*T//S,'hi_numerator':ceildiv(self.hi*T,S),'denominator':T}
xl,xh=1/(2*ph),1/(2*pl)
x=I.pair(xl.numerator*S//xl.denominator,ceildiv(xh.numerator*S,xh.denominator))
A=[I(1)];A2=[I(0)]
for k in range(1,N+1):
    f=F(-(2*k-1)**2,8*k)*x
    g=F(1,k)*x
    A2.append(f*A2[-1]+g*A[-1]);A.append(f*A[-1])
def nextS(a):return [a[n]+(x*F(2*n-1,2)*a[n-1] if n else 0) for n in range(N+1)]
def H(a,b):return [a[n]+(9*x*x*a[n-2] if n>=2 else 0)-(6*x*b[n-1] if n>=1 else 0) for n in range(N+1)]
hs=[];a=A
for k in range(N+1):
    b=nextS(a);hs.append(H(a,b));a=b
y=[a/4 for a in H(A2,nextS(A2))]
def basis(j):
    v=[I(0) for _ in range(N+1)]
    for p in range(N-j+1):
        c=(-1)**p*comb(j+p-1,p)
        for k in range(p+1):
            e=j+2*p-k
            if e>N:continue
            d=c*comb(p,k)*2**k
            for n in range(e,N+1):v[n]=v[n]+d*hs[k][n-e]
    return v
res=y.copy();cs=[]
for j in range(1,N+1):
    bj=res[j];cs.append(bj/(4**j));base=basis(j)
    for n in range(j,N+1):res[n]=res[n]-bj*base[n]
assert all(c.lo>0 for c in cs[:23])
assert cs[23].hi<0
# Convenient rational outer enclosure.
assert cs[23].lo > I(F(-645486,10**11)).hi
assert cs[23].hi < I(F(-645484,10**11)).lo
out={'degree':N,'precision_decimal_digits':DIGITS,
'pi_bounds_method':'pi=16 arctan(1/5)-4 arctan(1/239), 80 and 24 alternating terms, exact rational remainder bounds',
'coefficient_intervals':[{'j':j+1,**c.out()} for j,c in enumerate(cs)],
'checks':{'c1_through_c23_strictly_positive':True,'c24_strictly_negative':True,
'c24_between_minus_645486_over_10pow11_and_minus_645484_over_10pow11':True},
'scope':'Rigorous coefficient interval computation; all asymptotic and infinite-series implications require the accompanying analytic proof.'}
print(json.dumps(out,ensure_ascii=False,indent=2))
