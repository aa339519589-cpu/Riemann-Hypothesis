"""Outward interval certificate for exact integer-row quadrature constants.
No sampled sign inference. All theta labels n>=9 and x>=2 are enclosed
by explicit positive Gaussian tails. mpmath.iv is used only for intervals.
"""
from mpmath import iv
from fractions import Fraction
iv.dps=30

def derivative(p):
 out=[Fraction(0)]*(len(p)+1)
 for k,a in enumerate(p):
  out[k]+=(Fraction(1,2)+2*k)*a; out[k+1]-=2*a
 return out
ps=[[Fraction(0),Fraction(15),Fraction(-30),Fraction(8)]]
for j in range(3): ps.append(derivative(ps[-1]))
# On 0<=x<=2, each n>=9 tail is below 10^-65.
# The maximum of e^(x/2) w^d e^-w occurs at x=0 for w>=3*81.
# A ratio bound <1/2 gives 4 C 3^d 9^(2d)/20^81.
for pp in ps:
 d=len(pp)-1; C=sum(abs(a) for a in pp)
 assert Fraction(4)*C*3**d*9**(2*d)/20**81 < Fraction(1,10**65)
tail=iv.mpf(['-1e-65','1e-65'])

def ev(p,w):
 a=iv.mpf(0)
 for c in reversed(p):a=a*w+iv.mpf(c.numerator)/c.denominator
 return a

def jets(x):
 z=iv.pi*iv.exp(2*x); out=[iv.mpf(0) for _ in range(4)]
 for n in range(1,9):
  w=n*n*z; ew=iv.exp(-w)
  for j in range(4):out[j]+=ev(ps[j],w)*ew
 return [iv.exp(x/2)*a+tail for a in out]

# At x>=2, w>=pi e^4>160. Polynomial monomials satisfy
# w^d e^-w <= 2^d d! e^(-w/2). After the change w=n^2 pi e^(2x),
# all three weighted integrals below have tails <10^-20;
# this is checked using a deliberately larger rational constant.
import math
C=sum(sum(abs(a) for a in pp) for pp in ps)*10
D=6
assert Fraction(C)*2**D*math.factorial(D)*4/20**26 < Fraction(1,10**20)
# e^80>e^78>20^26; constants above also cover the label tail ratio.
IT=iv.mpf(['-1e-20','1e-20'])
N=2000  # step 1/1000 across [0,2]
h=iv.mpf(2)/N
I=iv.mpf(0); VF=iv.mpf(0); VG=iv.mpf(0)
for k in range(N):
 x=iv.mpf([iv.mpf(2*k)/N,iv.mpf(2*(k+1))/N]); a,b,c,d=jets(x)
 I+=h*iv.exp(-x/2)*a
 VF+=h*iv.exp(3*x/2)*abs(iv.mpf(3)/4*a+2*b+c)
 VG+=h*iv.exp(3*x/2)*abs(-iv.mpf(3)/8*a-iv.mpf(1)/4*b+iv.mpf(3)/2*c+d)
p=jets(iv.mpf(0))[1]
I+=IT;VF+=abs(p)+IT;VG+=IT
assert bool(p.b<17),p
assert bool(I.a>iv.mpf(3)/4),I
assert bool(I.b<1),I
assert bool(VF.b<80),VF
assert bool(VG.b<500),VG
print('CERTIFIED p<17, I0>3/4, Var(F prime)<80, Var(G prime)<500.')
print('p:',p)
print('I0:',I)
print('VarFprime:',VF)
print('VarGprime:',VG)
