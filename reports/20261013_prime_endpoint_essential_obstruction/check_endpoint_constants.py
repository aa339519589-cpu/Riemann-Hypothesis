#!/usr/bin/env python3
"""Check exact Gamma Laurent coefficients and a numerical finite-theta diagnostic.

Mathematical proof: THEOREM_ENDPOINT_FINITE_PRIMES.md.
This is not an interval certificate and does not prove RH.
"""
import json
import math
import mpmath as mp
import sympy as sp

u = sp.symbols('u', positive=True)
kappa = sp.exp(-u / 2) / (1 - sp.exp(-2 * u))
assert sp.limit(u * kappa, u, 0, dir='+') == sp.Rational(1, 2)
assert sp.limit(kappa - 1 / (2 * u), u, 0, dir='+') == sp.Rational(1, 4)
assert sp.limit(-2 * u ** 2 * sp.diff(kappa, u), u, 0, dir='+') == 1

mp.mp.dps = 55
pi = mp.pi

def psi(x):
    total = mp.mpf('0')
    for j in range(1, 9):
        q = pi * j * j * mp.exp(2 * x)
        value = (4 * pi**2 * j**4 * mp.exp(mp.mpf('4.5') * x)
                 - 6 * pi * j*j * mp.exp(mp.mpf('2.5') * x))
        slope = (18 * pi**2 * j**4 * mp.exp(mp.mpf('4.5') * x)
                 - 15 * pi * j*j * mp.exp(mp.mpf('2.5') * x))
        total += (2 * q * value - slope) * mp.exp(-q)
    return total

def mangoldt(n):
    for p in range(2, n + 1):
        if all(p % q for q in range(2, math.isqrt(p) + 1)):
            x = n
            while x % p == 0:
                x //= p
            if x == 1:
                return mp.log(p)
    return mp.mpf('0')

terms = []
for n in range(2, 20):
    lam = mangoldt(n)
    if lam > 0:
        terms.append((n, lam * psi(mp.log(n)) / mp.sqrt(n)))
a2 = terms[0][1]
partial = sum((v for _, v in terms), mp.mpf('0'))
c = mp.diff(psi, mp.mpf('0'))
assert c > 0 and partial > a2 > 0
result = {
  'status':'EXACT_GAMMA_LIMITS_PASSED_FINITE_THETA_DIAGNOSTIC_ONLY',
  'rigorous_checks':{'u_kappa_limit':'1/2',
                     'kappa_regular_part':'1/4',
                     'negative_double_derivative_limit':'1'},
  'numerical_only':{
    'theta_terms':8,'max_prime_power_label':19,
    'psi_derivative_zero':mp.nstr(c,22),
    'A_2':mp.nstr(a2,22),
    'A_to_19':mp.nstr(partial,22),
    'A_to_19_over_A_2':mp.nstr(partial/a2,22)},
  'no_infinite_tail_certificate': True,
  'rh_proved':False
}
print(json.dumps(result, indent=2))
