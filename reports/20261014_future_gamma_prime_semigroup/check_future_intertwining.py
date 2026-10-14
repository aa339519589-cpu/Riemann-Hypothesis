#!/usr/bin/env python3
"""Checks constants and exact coefficient algebra, not original-form sign."""
from fractions import Fraction as Q
import mpmath as mp
mp.mp.dps=55

def primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
ps=primes(100)
for n in range(1,101):
    for p in ps:
        exponent=0
        m=n
        while m%p==0:
            exponent+=1; m//=p
        powers=0; d=p
        while d<=n:
            powers+=int(n%d==0); d*=p
        assert exponent==powers

# A finite probability identity underlying the beta part of the carre formula.
for k in range(1,10):
    p=[Q(1,k+4),Q(2,k+4),Q(k+1,k+4)]
    v=[Q(k-3,2),Q(2-k,3),Q(k+2,5)]
    b=[Q(1,2),Q(1,5),Q(1,11)]
    Ev=lambda a:sum(pi*ai for pi,ai in zip(p,a))
    cov=lambda a,c:Ev([ai*ci for ai,ci in zip(a,c)])-Ev(a)*Ev(c)
    u=Ev(v)
    assert cov(b,[a*a for a in v])-2*u*cov(b,v)==cov(b,[(a-u)**2 for a in v])

errors=[]
for z in [mp.pi,mp.mpf(7),mp.mpf(19)]:
    def base(u):
        if not u:return (z-mp.mpf(1)/4)/2
        return (mp.power(1+u,-mp.mpf(1)/4)-mp.exp(-z*u))/(2*u)
    val=mp.quad(base,[0,1,mp.inf])
    target=(mp.log(z)-mp.digamma(mp.mpf(1)/4))/2
    errors.append(abs(val-target))
    beta=(4*z-1)/(4*z*z-6*z)
    a=3/(2*z)
    def eta(u):
        if not u:return (z-mp.mpf(1)/4)/2-(2-a)/(2*(1-a))
        return base(u)-((2-a)+u)*mp.exp(-z*u)/(2*(1-a))
    errors.append(abs(mp.quad(eta,[0,1,mp.inf])-(target-beta)))
for lam in [mp.mpf(1)/7,mp.mpf(2),mp.mpf(5)]:
    val=mp.quad(lambda u:mp.exp(-u)*(-mp.expm1(-lam*u))/(2*u) if u else lam/2,[0,1,mp.inf])
    errors.append(abs(val-mp.log(1+lam)/2))
# Slowly decaying u^(-5/4) base integrand limits raw infinite-quadrature accuracy.
assert max(errors)<mp.mpf('1e-12'),max(errors)
print('Exact divisor coefficient checks: n<=100, passed.')
print('Exact rational covariance checks: 9 cases, passed.')
print('Absolute Gaussian/eta rows and Gamma generator: maximum error',mp.nstr(max(errors),8))
