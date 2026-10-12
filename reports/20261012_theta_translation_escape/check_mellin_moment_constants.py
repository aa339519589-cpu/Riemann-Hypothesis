#!/usr/bin/env python3
"""Reproduce exact moment constants and FLOATING-POINT sanity checks.

This is not a rigorous interval certificate for the theta tails, prime-number
theorem or RH. The full proof is in PRIME_ENERGY_MELLIN_MOMENTS.md.
"""
import json
import math
from sympy import Rational as Q, sqrt, pi, gamma, zeta, simplify

xi5 = Q(15, 2)*zeta(5)/pi**2
norm = 4*pi**2*2**(-Q(9,2))*gamma(Q(5,2))/(2*pi)**Q(5,2)
log_coefficient = Q(128,3)*4*pi**2*2**(-Q(9,2))*xi5
residue = 2*xi5*(2*pi)**(Q(5,2))/gamma(Q(5,2))
assert simplify(norm-Q(3,128)) == 0
assert simplify(log_coefficient-40*sqrt(2)*zeta(5)) == 0
assert simplify(residue-80*sqrt(2)*zeta(5)) == 0

def von_mangoldt(nmax):
    flags = [True]*(nmax+1)
    flags[:2] = [False,False]
    for p in range(2, math.isqrt(nmax)+1):
        if flags[p]:
            for q in range(p*p, nmax+1, p):
                flags[q] = False
    out = [0.0]*(nmax+1)
    for p in range(2,nmax+1):
        if flags[p]:
            k = p
            while k <= nmax:
                out[k] = math.log(p)
                k *= p
    return out

def theta_phi(x):
    x = abs(x)
    if x > 13:
        return 0.0
    r = math.exp(2*x)
    return sum((4*math.pi**2*n**4*math.exp(4.5*x)
               -6*math.pi*n*n*math.exp(2.5*x))
               *math.exp(-math.pi*n*n*r) for n in range(1,7))

# Only sample positive integer prime powers up to 8 exp(x). Gaussian tails
# beyond that are NOT enclosed in this sanity calculation.
xi_values = {-3:float(3*zeta(3)/(2*pi)), 0:0.5, 1:math.pi/6}
rows = []
for x in [3.0,4.0,5.0]:
    X=math.exp(x)
    lam=von_mangoldt(int(8*X)+1)
    for s in [-3,0,1]:
        val=sum(lam[n]*(n**(s-0.5))*
                (theta_phi(x-math.log(n))+theta_phi(x+math.log(n)))
                for n in range(2,len(lam)) if lam[n])
        val /= (2*math.cosh(x/2))
        scaled=val/math.exp(s*x)
        rows.append({'x':x,'s':s,'scaled_rate':scaled,
                     'xi_1_plus_s':xi_values[s],
                     'ratio_to_limit':scaled/xi_values[s]})
assert all(abs(r['ratio_to_limit']-1)<0.05 for r in rows)
result={'status':'PASS_EXACT_CONSTANTS_AND_NUMERICAL_SANITY',
        'rigorous_scope':'only exact SymPy constant simplifications',
        'numeric_scope':'truncated theta and von Mangoldt sums; not a proof',
        'exact_norm_coefficient':str(simplify(norm)),
        'exact_borderline_coefficient':str(simplify(log_coefficient)),
        'exact_limit_mellin_pole_residue':str(simplify(residue)),
        'rows':rows,'rh_proved':False}
print(json.dumps(result,indent=2))
