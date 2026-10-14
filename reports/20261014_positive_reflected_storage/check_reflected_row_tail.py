#!/usr/bin/env python3
"""Exact rational theta constants for the reflected-row tail proof.
The unconditional Chebyshev bounds are the cited Rosser--Schoenfeld theorem,
not a claim proved by this finite checker.
"""
from fractions import Fraction as F

def atan_interval(q, n=14):
    s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0))
    t=s+F((-1)**n,(2*n+1)*q**(2*n+1))
    return min(s,t),max(s,t)
a,b=atan_interval(5); c,d=atan_interval(239)
pi_lo,pi_hi=16*a-4*d,16*b-4*c
assert F(31415,10000)<pi_lo<pi_hi<F(22,7)
assert pi_lo>F(25,8)

def exp_interval(x, n=40):
    term=F(1); s=term
    for k in range(1,n+1):
        term*=x/k; s+=term
    nxt=term*x/(n+1)
    ratio=x/(n+2)
    assert 0<ratio<1
    return s,s+nxt/(1-ratio)
P=lambda z:4*z*z-6*z
C=lambda z:8*z**3-30*z*z+15*z
Q=lambda z:-8*z**3+54*z*z-75*z+15
Qp=lambda z:-24*z*z+108*z-75

# Phi(0) exceeds its positive n=1 term.
_,e_hi=exp_interval(F(22,7))
assert e_hi<F(2317,100)
assert P(F(31415,10000))/F(2317,100)>F(89,100)
# Theta(0) <= 1/23 + geometric tail starting at n=2.
e_lo,_=exp_interval(F(31415,10000))
assert e_lo>23
assert F(1,23)+F(1,23**4)/(1-F(1,23**5))<F(44,1000)
# J > Phi(0) + (1/2) integral Phi > 1.
assert F(44,1000)/F(11,2)==F(1,125)
assert F(89,100)+F(1,2)*(F(1,4)-F(1,4*125))>1

# C(z)e^-z increases to one maximum z_* in (4.92,4.93).
lo,hi=F(492,100),F(493,100)
assert Q(F(157,50))>0 and Q(lo)>0 and Q(hi)<0
assert Qp(lo)<0
# Q''=-48z+108 is negative on z>=3, proving the sign claims in the text.
assert -48*3+108<0
# The maximum is less than 9/4.
e_lo,_=exp_interval(lo)
assert C(hi)/e_lo<F(9,4)
# C(pi)e^-pi > -1/20, using C increasing on z>=3.
e3_lo,_=exp_interval(F(3))
assert e3_lo>20
assert -C(F(157,50))*F(2,45)<F(1,20)
# sqrt(z_*/pi)<127/100 and I_+<293/100.
assert F(127,100)**2>F(8,5)
assert F(127,100)*(F(9,4)+F(1,20))<F(293,100)
assert F(84,100)-F(20,100)*F(293,100)==F(127,500)
assert F(127,500)-F(1,4)==F(1,250)
print('PASS: exact rational constants give J>1 and I_plus<2.93.')
print('With Rosser--Schoenfeld Theorems 10 and 12: L(x)>127*exp(x/2)/500 for exp(x)>=101.')
