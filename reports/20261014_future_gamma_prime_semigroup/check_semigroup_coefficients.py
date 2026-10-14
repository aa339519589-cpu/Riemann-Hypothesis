#!/usr/bin/env python3
"""Exact arithmetic and polynomial checks; no RH sign is tested."""
from fractions import Fraction as F
from math import comb


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def j(t, n):
    ans = F(1)
    for p in prime_factors(n):
        ans *= 1 - F(1, p**t)
    return ans


for n in range(1, 101):
    ds = divisors(n)
    for t in (1, 2, 3):
        assert sum(F(1, d**t) * j(t, n // d) for d in ds) == 1
        for s in (1, 2, 3):
            assert sum(F(1, d**t) * j(s, d) * j(t, n // d) for d in ds) == j(s+t, n)
            for e in ds:
                lhs = sum(F(1, d**t) * j(t, n//d) * F(1, e**s) * j(s, d//e)
                          for d in ds if d % e == 0)
                assert lhs == F(1, e**(s+t)) * j(s+t, n//e)


def rising(a, k):
    out = F(1)
    for j0 in range(k):
        out *= a+j0
    return out


def gamma_polynomial(coeffs, t):
    # E[(z+Gamma(t/2,1))^k], coefficient order ascending.
    out = [F(0)] * len(coeffs)
    for k, ck in enumerate(coeffs):
        for l in range(k+1):
            out[l] += ck * comb(k, l) * rising(t/2, k-l)
    return out


for t in (F(1, 3), F(1), F(2), F(5, 2)):
    assert gamma_polynomial([0, -6, 4], t) == [t*t-t, 4*t-6, F(4)]
    assert gamma_polynomial([0, 15, -30, 8], t) == [t/2-F(3,2)*t*t+t**3, 15-18*t+6*t*t, -30+12*t, F(8)]

print('Exact divisor normalization and composition: n <= 100, s,t in {1,2,3}, passed.')
print('Exact hidden integer-chain Chapman-Kolmogorov identities: all divisors, passed.')
print('Exact gamma q/c ladder at four rational times: passed.')
