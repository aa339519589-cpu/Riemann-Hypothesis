#!/usr/bin/env python3
"""Nonrigorous floating-point test of Hilbert and source Grams.

This is NOT an interval certificate, not an H spectral computation, and not
a proof of RH. The analytic full-Gamma/full-prime theorem is separately proved
in HIGH_ZERO_PROBE_TWO_PLANE.md.
"""
import json
import math
from scipy.integrate import quad
from scipy.linalg import eigh


def phi(x):
    x = abs(x)
    z = math.pi * math.exp(2*x)
    val = 0.0
    for n in range(1, 9):
        u = n*n*z
        val += (4*u*u - 6*u) * math.exp(x/2-u)
    return val


def m2(x):
    return phi(x)/(2*math.cosh(x/2))


def beta(eta, x):
    return math.sinh(eta*x)/eta if eta else x


def even_integral(func):
    return 2*quad(func, 0, 4, epsabs=1e-12, epsrel=1e-11, limit=2000)[0]


def matrices(eta, gamma):
    out = []
    for power in [1, 2]:
        def entry(i, j):
            def term(x):
                a = math.cosh(eta*x)
                b = beta(eta,x)
                waves = (a*math.cos(gamma*x), b*math.sin(gamma*x))
                return (m2(x)**power)*waves[i]*waves[j]
            return even_integral(term)
        out.append([[entry(0,0),entry(0,1)],
                    [entry(1,0),entry(1,1)]])
    return out


rows = []
for eta in [0,0.125,0.375,0.5]:
    a2, a4 = [], []
    for envelope in [lambda x: math.cosh(eta*x)**2,
                     lambda x: beta(eta,x)**2]:
        a2.append(even_integral(lambda x:m2(x)*envelope(x)))
        a4.append(even_integral(lambda x:m2(x)**2*envelope(x)))
    predicted = [a4[j]/a2[j] for j in range(2)]
    for gamma in [20,80,200]:
        G1,G2=matrices(eta,gamma)
        eigen=eigh(G2,G1,eigvals_only=True)
        rows.append({'eta':eta,'gamma':gamma,
            'predicted_limit_eigenvalues':predicted,
            'finite_generalized_source_to_physical_eigenvalues':[float(v) for v in eigen],
            'positive':bool(min(eigen)>0)})
assert all(r['positive'] for r in rows)
result={'type':'FLOATING_POINT_SANITY_NOT_INTERVAL_CERTIFICATE',
        'theta_modes_truncated_to':8,'integration_cutoff':4,
        'proof_dependency':'original analytic theorem, not this program',
        'rows':rows,'rh_proved':False}
print(json.dumps(result,indent=2))
