#!/usr/bin/env python3
"""Rigorous interval certificate for H_kappa psi + (1/2)F_r psi > sinh(x/2)/2.

This file certifies ONLY 0 <= x <= 6. The separate analytic tail theorem
starts at log(349)<6. Each retained Mangoldt term is a genuine prime power;
all omitted terms are positive. mpmath interval arithmetic encloses pi, exp,
log and all rational operations. No floating-point point samples are used.
"""
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80
mp.iv.dps = 60
iv = mp.iv

def lower(a):
    return mp.mpf(a._mpi_[0])

def upper(a):
    return mp.mpf(a._mpi_[1])

def text_endpoint(a):
    return mp.nstr(a, 45)

def exact_ratio(a, b=1):
    return iv.mpf(a) / b

# V_psi = int exp(-y/2)psi(y)dy >= exp(-1/4)[Phi(0)-Phi(1/2)].
# Phi(0) is bounded below by its first, positive eta term.
# For Phi(1/2), z=pi*e>8 and consecutive m^4 exp(-m^2 z) tail terms
# have ratio <= (3/2)^4 exp(-5z) < 1/2, starting at m=2.
z = iv.pi * iv.exp(1)
ratio = exact_ratio(81,16) * iv.exp(-5*z)
assert lower(z) > 8
assert upper(2*ratio) < 1
phi0_lower = (4*iv.pi**2 - 6*iv.pi)*iv.exp(-iv.pi)
phi_half_upper = iv.exp(exact_ratio(1,4)) * (
    (4*z**2-6*z)*iv.exp(-z) + 128*z**2*iv.exp(-4*z))
v_lower = iv.exp(-exact_ratio(1,4)) * (phi0_lower - phi_half_upper)
assert lower(v_lower-exact_ratio(3,5)) > 0

# Exact integer sieve. Lambda(n) is log p precisely when n=p^k.
N = 1024
is_prime = [True]*(N+1)
is_prime[0] = is_prime[1] = False
prime_powers = {}
for p in range(2,N+1):
    if not is_prime[p]:
        continue
    for m in range(p*p,N+1,p):
        is_prime[m] = False
    n = p
    while n <= N:
        assert n not in prime_powers
        prime_powers[n] = p
        n *= p
terms = [(n,iv.ln(n),iv.ln(p)/iv.sqrt(n))
         for n,p in sorted(prime_powers.items())]

# psi(y) >= max(0, xi_1(y)) for y>=0: the complete psi is positive,
# while every xi_m, m>=2, is positive since m^2*pi*exp(2y)>=4*pi>12.
# xi_1(y)=exp(y/2)c(pi*exp(2y))*exp(-pi*exp(2y)).
def first_xi(Y):
    w = iv.pi * iv.exp(2*Y)
    return iv.exp(Y/2) * w*(8*w*w-30*w+15)*iv.exp(-w)

step_den = 100
num_cells = 6*step_den
minimum = None
minimum_cell = None
minimum_terms = None
for j in range(num_cells):
    X = iv.mpf([j,j+1])/step_den
    # Strictly reflected: terms crossing the moving boundary are omitted.
    L_lower = iv.mpf(0)
    retained = 0
    for n,d,alpha in terms:
        Y = d-X
        if lower(Y) <= 0:
            continue
        xi = first_xi(Y)
        if lower(xi) <= 0:
            continue
        L_lower += alpha*xi
        retained += 1
    H_lower = exact_ratio(3,5)*iv.exp(-X/2)
    pole_upper = (iv.exp(X/2)-iv.exp(-X/2))/4
    margin = H_lower+L_lower/2-pole_upper
    m = lower(margin)
    if minimum is None or m < minimum:
        minimum,minimum_cell,minimum_terms=m,j,retained
    assert lower(margin-exact_ratio(1,16)) > 0, ('unproved cell',j, str(margin))

assert upper(iv.ln(349)) < 6
# Exact rational arithmetic for the separately proved analytic tail.
assert 91*100-13*293 == 5291
assert 5291-5000 == 291
assert 18**2 < 349
assert 291*18*16 > 20000
result = {
    'status':'PASS: half-reflected storage row on [0,6]',
    'interval_decimal_precision':60,
    'cells':num_cells,
    'cell_width':'1/100',
    'prime_power_cutoff':N,
    'prime_powers_available':len(terms),
    'V_psi_lower_enclosure':text_endpoint(lower(v_lower)),
    'V_psi_used':'3/5',
    'certified_margin_target':'1/16',
    'minimum_certified_margin':text_endpoint(minimum),
    'minimum_cell_index':minimum_cell,
    'minimum_cell_left':str(mp.mpf(minimum_cell)/step_den),
    'minimum_cell_right':str(mp.mpf(minimum_cell+1)/step_den),
    'retained_terms_in_minimum_cell':minimum_terms,
    'analytic_tail_overlap':'log(349) < 6',
    'scope':'No omitted prime or theta term is subtracted; no RH or full-form sign claim.'
}
print(json.dumps(result,indent=2))
Path(__file__).with_name('half_reflected_storage_row_certificate.json').write_text(
    json.dumps(result,indent=2)+'\n')
