#!/usr/bin/env python3
"""Exact rational certificate: exponent-pair double-Gram detector specialization.
Standard library only. Rational-function identities are checked polynomially;
interval signs use exact Bernstein coefficients, not a sample grid.
Analytic input theorems and worldwide novelty are outside this program.
"""
from fractions import Fraction as F
from math import comb

def trim(p):
    p=list(map(F,p))
    while len(p)>1 and not p[-1]:p.pop()
    return tuple(p)
def add(p,q):
    return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                 for i in range(max(len(p),len(q)))])
def neg(p):return tuple(-x for x in p)
def mul(p,q):
    z=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):z[i+j]+=x*y
    return trim(z)
def divmodp(p,q):
    p=list(trim(p));q=trim(q);z=[F(0)]*max(1,len(p)-len(q)+1)
    while len(p)>=len(q) and any(p):
        i=len(p)-len(q);v=p[-1]/q[-1];z[i]+=v
        for j,a in enumerate(q):p[i+j]-=v*a
        p=list(trim(p))
    return trim(z),trim(p)
def gcd(p,q):
    while any(q):p,q=q,divmodp(p,q)[1]
    return tuple(x/p[-1] for x in p)
def ev(p,x):
    z=F(0)
    for a in reversed(p):z=z*x+a
    return z
class R:
    def __init__(self,p=0,q=1):
        p=trim(p if isinstance(p,(list,tuple)) else [p])
        q=trim(q if isinstance(q,(list,tuple)) else [q])
        assert any(q)
        if not any(p):self.p=(F(0),);self.q=(F(1),);return
        g=gcd(p,q);p=divmodp(p,g)[0];q=divmodp(q,g)[0]
        scale=q[-1];self.p=tuple(x/scale for x in p);self.q=tuple(x/scale for x in q)
    def __add__(self,b):
        b=asr(b);return R(add(mul(self.p,b.q),mul(b.p,self.q)),mul(self.q,b.q))
    __radd__=__add__
    def __neg__(self):return R(neg(self.p),self.q)
    def __sub__(self,b):return self+-asr(b)
    def __rsub__(self,b):return asr(b)+-self
    def __mul__(self,b):
        b=asr(b);return R(mul(self.p,b.p),mul(self.q,b.q))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=asr(b);return R(mul(self.p,b.q),mul(self.q,b.p))
    def __rtruediv__(self,b):return asr(b)/self
    def __eq__(self,b):return not any((self-asr(b)).p)
    def at(self,x):return ev(self.p,x)/ev(self.q,x)
def asr(x):return x if isinstance(x,R) else R(x)
def bernstein(p,l,r):
    d=len(p)-1
    # p(l+(r-l)t), then power basis to degree-d Bernstein basis.
    a=[sum(p[j]*comb(j,i)*l**(j-i)*(r-l)**i for j in range(i,d+1))for i in range(d+1)]
    return [sum(a[i]*F(comb(k,i),comb(d,i))for i in range(k+1))for k in range(d+1)]
def sign(f,l,r,strict=False):
    f=asr(f);bp=bernstein(f.p,l,r);bq=bernstein(f.q,l,r)
    if max(bq)<0:bp=[-x for x in bp];bq=[-x for x in bq]
    assert min(bq)>0,('denominator',l,r,bq)
    assert min(bp)>0 if strict else min(bp)>=0,('numerator',l,r,bp)

s=R([0,1]);eta=1-s
A=F(543,178);Q=F(1727,89);k=F(13,84);ell=F(55,84)
yD=1629/(4*(5831*s-4104));yI=543/(2742*s-1015)
y4=89/(1282*s-908)
CD=F(13371,15098)
cells=[('D',F(873,1000),CD,yD),('I',CD,F(111,125),yI),
       ('mu4',F(229,250),F(933,1000),y4)]
assert yD.at(CD)==yI.at(CD)
sign(yD-yI,F(873,1000),CD);sign(yI-yD,CD,F(111,125))

def endpoint_rows(E,n):
    a2=E-2*eta*n
    opts=[R(0),(1+(9-12*s)*n-E)/2,
          (A+(3-4*s)*Q*n/2-(A-1)*a2-E)/2]
    base=2*k+(2+2*ell-2*k-4*s)*n
    out=[]
    for a1 in opts:
        rows=[2*eta*n+a1+a2/2,base+4*a1-2*k*a2,base+2*a1+a2]
        gap=(2*s-2*ell+2*k)*n-2*k+k*a2-2*a1
        out.append((a1,rows,gap))
    return a2,out

for name,l,r,y in cells:
    E=4*eta*y;n0=4*y/3;n1=2*y
    for f in [E,1-E,n0-E,1-n1,y]:sign(f,l,r,True)
    for n in [n0,n1]:
        a2,out=endpoint_rows(E,n)
        sign(a2,l,r);sign(1-a2,l,r,True);sign(1-n-a2,l,r,True)
        for a1,rows,gap in out:
            sign(1-a1,l,r,True)
            for j,row in enumerate(rows):
                try:sign(E-row,l,r)
                except AssertionError as exc:raise AssertionError((name,'D',j,n.p,n.q,a1.p,a1.q,exc))
            sign(gap,l,r,True)
    # The complete length window is paid by convexity/concavity, not samples.
    if name in ['D','I']:
        # TY5.1 class-II detector contributions, fixed Bv4 pair.
        for row in [1-6*(s-F(1,2))*y,A+(Q/2-Q*s)*y]:sign(E-row,l,r)
    else:
        chi,mu=F(454,641),F(89,1282)
        assert y*(s-chi)==mu
        sign(s-chi,l,r,True)
    print(name,'endpoint/whole-window certificate PASS',l,r)

# Old full-diagonal detector bound and all of its intersected pieces.
yH4=948/(11929*s-8119);yH3=111885/(1415129*s-964637)
C1=F(8751,10033);C2=F(2589,2923);C3=F(136744872,153875459)
old=[(F(433,500),C1,yD),(C1,C2,yH4),(C2,C3,yH3),(C3,F(89,100),yI)]
for name,l,r,y in cells[:2]:
    for a,b,yo in old:
        lo=max(l,a);hi=min(r,b)
        if lo<=hi:sign(yo-y,lo,hi,True)
# High interval: prior seven-piece exponent is eta/(3sigma-2), hence divide by 4eta.
for name,l,r,y in cells[2:]:sign(1/(4*(3*s-2))-y,l,r,True)

# Identified Table11.1 envelope plus the broader 3/(2sigma) comparator.
table=[(F(873,1000),F(7,8),3/(2*s)),
       (F(7,8),F(279,314),3/(10*s-7)),
       (F(279,314),F(9,10),24/(30*s-11)),
       (F(31,34),F(14,15),11/(48*s-36))]
for name,l,r,y in cells:
    sign(3/(2*s)-4*y,l,r,True)
    for a,b,coefficient in table:
        lo=max(l,a);hi=min(r,b)
        if lo<=hi:sign(coefficient-4*y,lo,hi,True)
assert (4*eta*yD).at(F(7,8))==F(1629,7985)
assert (4*eta*yD).at(F(22,25))==F(4887,25682)
assert (4*eta*y4).at(F(23,25))==F(356,3393)
print('All endpoint identities, full-window inequalities and comparator checks PASS.')
