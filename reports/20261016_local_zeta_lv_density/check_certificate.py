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
A0,q0=F(543,178),F(1727,89)
AL,qL=F(60,17),F(386,17)
AH,qH=F(213,80),F(67,4)
k,ell=F(13,84),F(55,84)
v0,v1,v2=F(161,1110),F(131,900),F(307,2100)
join=F(696,797)
yL=45/(661*s-468);yH=639/(4*(2227*s-1557))
assert yL.at(join)==yH.at(join)
yD=1629/(4*(5831*s-4104))
cells=[('lower',F(87,100),join,yL),('upper',join,F(219,250),yH)]
checks=0
for name,lo,hi,y in cells:
 E=4*eta*y;n0,n1=4*y/3,2*y
 def check(label,f,strict=False):
  global checks
  try:sign(f,lo,hi,strict)
  except AssertionError as exc:raise AssertionError((name,label,exc))
  checks+=1
 def params(n):
  a2=E-2*eta*n;u=1-a2;h=(4*s-3)*n/(2*u)
  return a2,u,h
 def cut(v):return 2*v*(1-E)/(4*s-3-4*eta*v)
 c1,c2=cut(v1),cut(v2)
 def opts(n,A=None,q=None):
  a2,u,h=params(n)
  if A is not None:return [R(0),(u*A-q*(4*s-3)*n/2+a2-E)/2]
  return [R(0),(1+(9-12*s)*n-E)/2,(A0-q0*(4*s-3)*n/2-(A0-1)*a2-E)/2]
 def endpoint(label,n,A=None,q=None):
  a2,u,h=params(n)
  for tag,f,st in [('alpha2',a2,False),('u',u,True),('N<T0',1-n-a2,True)]:check(label+tag,f,st)
  base=2*k+(2+2*ell-2*k-4*s)*n
  for i,a1 in enumerate(opts(n,A,q)):
   check(label+'a1<1',1-a1,True)
   for row in [2*eta*n+a1+a2/2,base+4*a1-2*k*a2,base+2*a1+a2]:check(label+'count',E-row)
   check(label+'absorption',(2*s-2*ell+2*k)*n-2*k+k*a2-2*a1,True)
 for f in [y,E,1-E,n0-E,1-n1,n1-c2,(4*s-3)*(1-E)]:check('range',f,True)
 assert params(c1)[2]==v1 and params(c2)[2]==v2
 for v in [v1,v2]:check('cut denominator',4*s-3-4*eta*v,True)
 if name=='lower':
  check('local h low',params(n0)[2]-v0,True);check('c1>=n0',c1-n0);check('c2>c1',c2-c1,True)
  for n in [n0,c1]:endpoint('local L',n,AL,qL)
  for n in [c1,c2]:endpoint('local H',n,AH,qH)
 else:
  check('local h low',params(n0)[2]-v1);check('c2>n0',c2-n0,True)
  for n in [n0,c2]:endpoint('local H',n,AH,qH)
 for n in [c2,n1]:endpoint('original',n)
 for row in [1-6*(s-F(1,2))*y,A0+(q0/2-q0*s)*y]:check('class II',E-row)
 check('prior yD',yD-y,True);check('Kerr/Lewko',3/(2*s)-4*y,True)
 if hi>=F(7,8):sign(3/(10*s-7)-4*y,max(lo,F(7,8)),hi,True)
 print(name,'whole sigma/n windows PASS',lo,hi)

# Complete beta prefix: all rows join and all normalized derivatives are positive.
z=R([0,1]);b4=F(89,1282)+F(454,641)*z
bL=F(13,146)+F(47,73)*z;bH=F(11,244)+F(191,244)*z
z0,z1,z2=F(102,335),F(87,275),F(423,1295)
assert F(1424,4747)<z0<z1<z2
assert b4.at(z0)==bL.at(z0) and bL.at(z1)==bH.at(z1) and bH.at(z2)==b4.at(z2)
for a,b in [(F(89,1282),F(454,641)),(F(13,146),F(47,73)),(F(11,244),F(191,244))]:assert a+b-F(1,2)>0
nL,nM,nH=F(218,525),F(94,225),F(233,555)
for z_,n_,v_,b in [(z0,nH,v0,bL),(z1,nM,v1,bH),(z2,nL,v2,bH)]:
 assert (1-z_)/(2-3*z_+2*b.at(z_))==n_
 assert (1-n_)/4==v_
n=R([0,1]);wH=F(61,40)-F(35,16)*n;wL=(73-125*n)/34
wg=(641-1015*n)/356;wp=F(3,4)-n/4
assert wH.at(nL)==wg.at(nL) and wL.at(nM)==wH.at(nM) and wL.at(nH)==wg.at(nH)
for lo,hi,w in [(nL,nM,wH),(nM,nH,wL)]:
 for f in [w-n,wp-w,(1+n)/2-w]:sign(f,lo,hi,True)
for f in [wg-n,wp-n,(1+n)/2-wp]:sign(f,F(1,3),nL)
assert F(3,2)+F(1015,356)>0 and F(7,4)>0 and F(59,16)>0 and F(88,17)>0
v=R([0,1]);nm=1-4*v
assert F(1,2)+F(3,2)*nm-2*v-(F(61,40)-F(35,16)*nm)==AH-qH*v
assert F(1,2)+F(3,2)*nm-2*v-(73-125*nm)/34==AL-qL*v
assert A0-q0*v0==AL-qL*v0 and AL-qL*v1==AH-qH*v1 and AH-qH*v2==A0-q0*v2
for lo,hi,A,q in [(v0,v1,AL,qL),(v1,v2,AH,qH)]:
 sign(A0-q0*v-(A-q*v),lo,hi)
 sign(A-q*v-(1-6*v),lo,hi,True)
 sign(A+(24-q)*v-1,lo,hi,True)
assert min(A0,AL,AH,1)>0 and 24>max(q0,qL,qH,6) and min(q0,qL,qH,6)>2
E=4*eta*yH
assert E.at(F(7,8))==F(639,3133)
assert (4*eta*(yD-yH)).at(F(7,8))==F(1242,25017005)
print('PASS:',checks,'density interval signs, complete beta/phase ranges, continuous moment envelope and comparisons.')

# Earlier full-diagonal comparator on the part below the EP report range.
sign(948/(11929*s-8119)-yL,F(8751,10033),F(873,1000),True)
print("PASS: earlier full-diagonal comparator below .873.")
