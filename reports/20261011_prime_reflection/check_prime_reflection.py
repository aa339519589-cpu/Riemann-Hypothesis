#!/usr/bin/env python3
"""Exploratory checks only. No interval arithmetic or RH certificate."""
import json
import math
import platform
import time
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 65
started = time.time()


def seed(t):
    return (2 * mp.pi**2 * mp.exp(9*t) - 3 * mp.pi * mp.exp(5*t)) * mp.exp(-mp.pi * mp.exp(4*t))


def phi(t):
    # Exact evenness of the full theta kernel is used. The finite sum is only
    # a high-precision numerical approximation to the positive half-axis sum.
    t = abs(t)
    return mp.fsum((2*mp.pi**2*n**4*mp.exp(9*t) - 3*mp.pi*n**2*mp.exp(5*t))*mp.exp(-mp.pi*n*n*mp.exp(4*t)) for n in range(1, 11))


def xi(s):
    return mp.mpf('0.5') * s * (s-1) * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)


def cfmt(z):
    return {'real': mp.nstr(mp.re(z), 35), 'imag': mp.nstr(mp.im(z), 35)}


normalization = []
for z in [mp.mpc(0), mp.mpc(1, '0.2'), mp.mpc(2, '0.5')]:
    s = mp.mpf('0.5') + 1j*z/2
    # Finite integration windows and theta truncation: not certificates.
    full_integral = mp.quad(lambda t: phi(t)*mp.exp(1j*z*t), [-3,-1,0,1,3])
    seed_integral = mp.quad(lambda t: seed(t)*mp.exp(1j*z*t), [-16,-8,-3,-1,0,1,3])
    exact_seed = (1j*z-1)/8 * mp.pi**(-(1+1j*z)/4) * mp.gamma((5+1j*z)/4)
    normalization.append({
        'z': cfmt(z),
        'full_kernel_minus_xi_over_4_abs': mp.nstr(abs(full_integral-xi(s)/4), 8),
        'seed_integral_minus_gamma_abs': mp.nstr(abs(seed_integral-exact_seed), 8),
        'finite_integration_windows': {'full': [-3,3], 'seed': [-16,3]},
        'theta_modes': 10,
    })

# Independent finite divisor construction, not B := E*Psi-A-R.
divisors = [(1,1),(2,-1),(3,-1),(5,-1),(6,1),(10,1),(15,1),(30,-1)]
def deleted(t):
    return mp.fsum(mu/mp.sqrt(d) * phi(t+mp.log(d)/2) for d,mu in divisors)

z = mp.mpc(1, '0.2')
s = mp.mpf('0.5') + 1j*z/2
T = mp.mpf('0.3')
E = mp.fprod(1-mp.power(p,-s) for p in [2,3,5])
# Split at translated centers, where abs() is harmless analytically but
# splitting assists numerical quadrature of the even implementation.
left_breaks = sorted(set([mp.mpf(-8), -T] + [-mp.log(d)/2 for d,mu in divisors if -mp.log(d)/2 < -T]))
B = mp.quad(lambda t: deleted(t)*mp.exp(1j*z*t), left_breaks)
A = mp.quad(lambda t: seed(t)*mp.exp(1j*z*t), [-T,0,1,3])
R = mp.quad(lambda t: (deleted(t)-seed(t))*mp.exp(1j*z*t), [-T,0,1,3])
finite_reflection = {
    'z': cfmt(z), 'T': str(T), 'primes': [2,3,5],
    'A': cfmt(A), 'B': cfmt(B), 'R': cfmt(R),
    'E_Psi': cfmt(E*xi(s)/4),
    'identity_residual_abs': mp.nstr(abs(A+B+R-E*xi(s)/4), 10),
    'integration_window': [-8,3], 'status': 'NUMERICAL_ONLY',
}

# The theorem is asymptotic and does not assert that small cutoffs already
# obey the limiting signs. All values, including pre-asymptotic mismatches,
# are retained. numpy complex128 is used for this independent scale check.
limit = 4_000_000
is_prime = np.ones(limit+1, dtype=np.bool_)
is_prime[:2] = False
for p in range(2, math.isqrt(limit)+1):
    if is_prime[p]:
        is_prime[p*p::p] = False
primes = np.flatnonzero(is_prime)
sigma, tau = 0.5, 3.0
s_np = complex(sigma,tau)
theta = math.atan(tau/(1-sigma))
log_terms = np.log1p(-np.exp(-s_np*np.log(primes.astype(float))))
log_cumulative = np.cumsum(log_terms)
oscillation = []
for k in range(1, 8):
    for label, phase in [('shrink',2*math.pi*k), ('grow',(2*k+1)*math.pi)]:
        Y_real = math.exp((phase+theta)/tau)
        Y = math.floor(Y_real)
        if Y > limit:
            continue
        n = np.searchsorted(primes,Y,side='right')
        logE = log_cumulative[n-1]
        main = -complex(Y)**(1-s_np)/((1-s_np)*math.log(Y))
        r = Y**(1-sigma)/(abs(1-s_np)*math.log(Y))
        oscillation.append({
            'subsequence':label, 'k':k, 'Y':Y, 'prime_count':int(n),
            'log_abs_E':float(logE.real), 'predicted_log_abs':float(main.real),
            'scale_r':r, 'relative_complex_remainder_over_r':abs(logE-main)/r,
            'sign_matches_asymptotic':bool((logE.real<0) if label=='shrink' else (logE.real>0)),
        })
oscillation.sort(key=lambda row:row['Y'])

result = {
    'status':'NUMERICAL_ONLY',
    'scope':'Fourier normalization, one finite divisor/reflection identity, and finite Euler factor asymptotics. Not interval certified; no zero-exclusion or RH result.',
    'environment':{'python':platform.python_version(),'mpmath':mp.__version__,'numpy':np.__version__,'mp_dps':mp.mp.dps},
    'normalization':normalization,
    'finite_reflection':finite_reflection,
    'oscillation_parameters':{'sigma':sigma,'tau':tau,'max_sieve':limit},
    'oscillation':oscillation,
    'elapsed_seconds':time.time()-started,
}
out = Path(__file__).with_name('prime_reflection_checks.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
