#!/usr/bin/env python3
"""Exact rational certificate: complete nine-row CDV detector specialization.
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
LO=F(433,500);HI=F(89,100)
C1=F(8751,10033);C2=F(2589,2923);C3=F(136744872,153875459)
A4=F(543,178);Q4=F(1727,89)
A3=F(64257,20666);Q3=F(204580,10333)
yD=1629/(4*(5831*s-4104));yH4=948/(11929*s-8119)
yH3=111885/(1415129*s-964637);yI=543/(2742*s-1015)
cells=[('D4',LO,C1,yD,A4,Q4),('H4',C1,C2,yH4,A4,Q4),
       ('H3',C2,C3,yH3,A3,Q3),('I',C3,HI,yI,A3,Q3)]
assert LO<C1<C2<C3<HI
for left,right,x in [(yD,yH4,C1),(yH4,yH3,C2),(yH3,yI,C3)]:assert left.at(x)==right.at(x)
assert yH4-yH3==2349*(2923*s-2589)/((11929*s-8119)*(1415129*s-964637))

# Exact generic nine exponent rows after alpha1/alpha2 substitution.
def row_values(A,Q,E,n):
    a2=E-2*eta*n
    a1=(A+(3-4*s)*Q*n/2-(A-1)*a2-E)/2
    r=[2*eta*n+a2,1+(9-12*s)*n-2*a1,
       A+(3-4*s)*Q*n/2-2*a1-(A-1)*a2,
       2*eta*n+a1+a2/2,(3-4*s)*n+4*a1,
       (12-16*s)*n/7+F(2,7)+F(10,7)*a1+a2/7,
       (12-16*s)*n/7+F(2,7)+F(8,7)*a1+F(4,7)*a2,
       (8-16*s)*n/3+F(2,3)+F(16,3)*a1,
       (4-8*s)*n/3+F(2,3)+F(5,3)*a1+a2/6]
    return a1,a2,r

for name,l,r,y,A,Q in cells:
    E=4*eta*y;n0=4*y/3;n1=2*y
    # alpha1 = (A(1-E)+Cn)/2; C is strictly negative.
    C=(3-4*s)*Q/2+2*(A-1)*eta
    ns=-A*(1-E)/C
    a1,a2,rows=row_values(A,Q,E,n0)
    _,_,nextrows=row_values(A,Q,E,n0+1)
    _,_,starrows=row_values(A,Q,E,ns)
    sign(E,l,r,True);sign(1-E,l,r,True)
    for f in [n0-E,ns-n0,n1-ns,1-n1,a1,1-a1]:sign(f,l,r,True)
    assert a2==E/3
    assert row_values(A,Q,E,ns)[0]==0
    assert row_values(A,Q,E,n1)[1]==0
    assert rows[0]==rows[2]==E
    # Exact affine dependence on n: endpoint and slope certification covers ALL n.
    slopes=[b-a for a,b in zip(rows,nextrows)]
    assert slopes[0]==slopes[2]==0
    sign(slopes[1],l,r,True)
    for j in range(3,9):sign(-slopes[j],l,r,True)
    sign(E-starrows[1],l,r,True)
    for j in [3,4,5,6,7,8]:sign(E-rows[j],l,r)
    # For n >= n*, the direct three-row estimate uses alpha1=0.
    sign(12*s-9,l,r,True)
    sign(-C,l,r,True)
    # Thus row2 decreases and row3-E=C(n-n*) <=0; row1=E.
    assert A+(3-4*s)*Q*ns/2-(A-1)*(E-2*eta*ns)-E==0
    # Both detected class-II rows, with Bv4.
    sign(E-1+6*(s-F(1,2))*y,l,r,True)
    sign(E-A4+Q4*(s-F(1,2))*y,l,r)
    print('PASS complete sigma/n cell',name,l,r)

# Current table/Kerr envelope on the complete interval, including the jump.
J=F(279,314)
comparators=[(LO,F(7,8),3/(2*s)),(F(7,8),J,3/(10*s-7)),(J,HI,24/(30*s-11))]
# Previously published finite-pair/local-beta envelope, supplemented by Kerr
# below its left endpoint. Each expression is the coefficient E/(1-sigma).
P0=F(4282,4923);P1=F(331,380);P2=F(5902,6711);P3=F(65223,73649)
prior=[(LO,P0,3/(2*s)),(P0,P1,1629/(6009*s-4282)),
       (P1,P2,192771/(712731*s-508151)),
       (P2,P3,1995/(7449*s-5323)),
       (P3,HI,378483/(1438001*s-1031827))]
for label,comp in [('table',comparators),('prior',prior),('Kerr/Lewko',[(LO,HI,3/(2*s))])]:
    for name,l,r,y,_,_ in cells:
        for u,v,Aold in comp:
            a=max(l,u);b=min(r,v)
            if a<=b:sign(Aold-4*y,a,b,True)
    print('PASS strict complete comparison:',label)
# The frozen accepted two-branch detector is never worsened.
oldC=F(136744872,153875459)
for name,l,r,y,_,_ in cells:
    l=max(l,F(7,8))
    if l>r:continue
    old=yH3 if r<=oldC else yI
    sign(old-y,l,r)
    if name in ['D4','H4']:
        # Strict except the H4/H3 join, where equality is required.
        assert (old-y).at(l)>0
        assert (old-y).at(r)>=0
print('PASS no regression against the accepted two-branch detector.')
for x in [LO,F(87,100),F(7,8),F(22,25),F(111,125),HI]:
    y=next(y for _,l,r,y,_,_ in cells if l<=x<=r)
    print('sigma',x,'E',4*(1-x)*y.at(x))
print('PASS: polynomial identities and exact Bernstein whole-interval signs.')
