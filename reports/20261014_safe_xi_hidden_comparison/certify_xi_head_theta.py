"""Outward interval verification of two explicit theta inequalities.
Uses mpmath.iv interval arithmetic; no sampling-based sign inference.
The omitted n>=9 derivative tail is bounded analytically below.
"""
from mpmath import iv
from fractions import Fraction
iv.dps=40
# Coefficients of ((1/2-2z)+2z*d/dz)^j c(z), j=0..3.
def deriv(poly):
 out=[Fraction(0)]*(len(poly)+1)
 for k,a in enumerate(poly):out[k]+=(Fraction(1,2)+2*k)*a;out[k+1]-=2*a
 return out
polys=[[Fraction(0),Fraction(15),Fraction(-30),Fraction(8)]]
for _ in range(3):polys.append(deriv(polys[-1]))
# For 0<=x<=31/100, 3<z<6. The n>=9 tail is at most
# 4 C_j 6^degree 9^(2degree) / 20^81, because exp(3)>20
# and consecutive n^(2degree) exp(-3n²) terms have ratio<1/2.
for pp in polys:
 deg=len(pp)-1;C=sum(abs(a) for a in pp)
 assert Fraction(4)*C*6**deg*9**(2*deg)/20**81 < Fraction(1,10**70)
tail=iv.mpf(['-1e-70','1e-70'])
def ev(poly,w):
 out=iv.mpf(0)
 for a in reversed(poly):out=out*w+iv.mpf(a.numerator)/a.denominator
 return out
def jet(x,j):
 z=iv.pi*iv.exp(2*x);q=iv.mpf(0)
 for n in range(1,9):
  w=n*n*z;q+=ev(polys[j],w)*iv.exp(-w)
 return iv.exp(x/2)*q+tail
def neg(v):return bool(v.b<0)
def pos(v):return bool(v.a>0)
# The small wall uses exact oddness psi''(0)=0 and a negative third derivative.
x=iv.mpf([0,iv.mpf(1)/1000])
assert neg(jet(x,3)),('wall third derivative',jet(x,3))
assert pos(jet(x,1)),('wall first derivative',jet(x,1))
count=0; max_second=None;min_gap=None
# Adaptive interval splitting certifies every point, including all endpoints.
def check(a,b,depth=0):
 global count,max_second,min_gap
 x=iv.mpf([iv.mpf(a.numerator)/a.denominator,iv.mpf(b.numerator)/b.denominator])
 sec=jet(x,2)
 kl=-iv.mpf(1)/2-2/iv.expm1(2*(x+iv.mpf(1)/1000))
 gap=jet(x,1)-kl*jet(x,0)
 if neg(sec) and pos(gap):
  count+=1
  return
 if depth>=30:raise RuntimeError((a,b,sec,gap))
 mid=(a+b)/2;check(a,mid,depth+1);check(mid,b,depth+1)
check(Fraction(1,1000),Fraction(31,100))
S=iv.mpf(31)/100
K=S*iv.exp(-S/2)/(1-iv.exp(-2*S))
assert bool(K.b<iv.mpf(3)/5)
def check_extra(a,b,kind,depth=0):
 x=iv.mpf([iv.mpf(a.numerator)/a.denominator,iv.mpf(b.numerator)/b.denominator])
 val=jet(x,1)+(2*jet(x,0) if kind=='minus_two' else 0)
 if neg(val):return
 if depth>=30:raise RuntimeError((a,b,kind,val))
 mid=(a+b)/2;check_extra(a,mid,kind,depth+1);check_extra(mid,b,kind,depth+1)
check_extra(Fraction(28,100),Fraction(31,100),'negative')
check_extra(Fraction(30,100),Fraction(31,100),'minus_two')
print('CERTIFIED psi concave and psi prime/psi >= kappa prime(s+1/1000)/kappa(s+1/1000).')
print('CERTIFIED psi prime<0 on [.28,.31] and psi prime/psi<-2 on [.30,.31].')
print('Verified interval leaves:',count)
print('31κ(31/100)/100 interval:',K)
print('Formal head gap lower interval 1-K:',1-K)
print('Each omitted derivative tail n>=9 is <10^-70 by exact rational check.')
