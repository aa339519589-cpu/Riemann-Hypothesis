"""Rigorous Arb ball certificate for actual D_beta(1,r)>0, all r>=1.

Requires Python-FLINT 0.9.0 (FLINT/Arb). All acceptance tests use balls,
not mpmath point approximations. The mathematical infinite-tail argument
is in actual_n1_all_orders.md. This is not a Lean kernel verification.
"""
from pathlib import Path
import json
import platform
import sys
from fractions import Fraction

try:
    import flint
except ImportError:
    sys.path.insert(0, "/workspace/shared/rh_low_start_20261007/vendor")
    import flint
from flint import arb, acb, acb_series, ctx

ctx.prec = 512
PREFIX = 10
NSEG = 2048
RADIUS = 1200


def show(x):
    return x.str(35)


def xi(s):
    """xi(s) = s(s-1) pi^(-s/2) Gamma(s/2) zeta(s) / 2."""
    return s * (s - 1) * (-s * arb.pi().log() / 2).exp() * (s / 2).gamma() * s.zeta() / 2


# B(-z^2) = xi(1/2 + i*z/2)/8. Extract its rigorously enclosed
# Taylor coefficients. Evenness and realness justify taking real parts.
ctx.cap = 2 * PREFIX + 1
s = acb_series([acb("0.5"), acb(0, "0.5")])
E = xi(s) / 8
beta = [((-1) ** k * E[2 * k]).real for k in range(PREFIX + 1)]
assert all(b > 0 for b in beta)
beta0 = beta[0]
assert beta0 > arb("0.06214")
assert beta0 < arb("0.06215")

# This counts all nontrivial zeta zeros, not just critical-line zeros.
# In conjunction with the isolated zero and the unconditional completed-xi
# zero correspondence, it proves f(z)=B(-z) has exactly one simple zero
# inside |z|<=1200: |Im s|<=sqrt(1200)/2 <20 there.
count = arb(20).zeta_nzeros()
assert count == 1
zero = acb.zeta_zero(1)
assert zero.real == arb("0.5")
assert zero.imag > 14
assert zero.imag < 15
rho = 4 * zero.imag ** 2
assert rho > 799
assert rho < 800
assert arb(RADIUS).sqrt() / 2 < 20

# f'(rho) = i xi'(zero)/(32 sqrt(rho)); its exact value is real.
ctx.cap = 2
sp = acb_series([zero, 1])
xid = xi(sp)[1]
fprime = (acb(0, 1) * xid / (32 * rho.sqrt())).real
assert fprime < 0
A = -beta0 / (rho * fprime)
assert A > 50
assert A < 51

# Finite prefix of H(z)=beta0/B(-z)=sum h_r z^r.
h = [arb(1)]
for n in range(1, PREFIX + 1):
    h.append(-sum(((-1) ** k * beta[k] * h[n - k] / beta0
                   for k in range(1, n + 1)), arb(0)))
assert all(v > 0 for v in h)

# Cover the ENTIRE circle by interval arcs. For the j-th arc,
# theta is enclosed in [(2j)pi/NSEG,(2j+2)pi/NSEG]. There are no gaps.
# The continuous chart sqrt(R)exp(i theta/2) avoids square-root branch-cut
# inflation. xi(s)=xi(1-s) gives the sign choice used below.
M = arb(0)
minimum_f = arb(1)
for j in range(NSEG):
    angle = arb.pi() * (2 * j + 1) / NSEG
    angle += arb(0, (arb.pi() / NSEG).upper())
    root = arb(RADIUS).sqrt() * acb(0, angle / 2).exp()
    s_arc = acb("0.5") - acb(0, 1) * root / 2
    f_arc = xi(s_arc) / 8
    assert not f_arc.contains(0), (j, show(f_arc))
    lower = f_arc.abs_lower()
    assert lower > 0
    if lower < minimum_f:
        minimum_f = lower
    upper = (beta0 / f_arc).abs_upper()
    assert upper < 3040, (j, show(upper))
    assert lower > arb("0.000036"), (j, show(lower))
    if upper > M:
        M = upper
assert minimum_f > arb("0.000036")
assert M < 3040

# Since rho<800 and A<51, on |z|=1200 the pole model has
# modulus <51/(1200/800-1)=102. Thus Q=H-A/(1-z/rho) has
# modulus <3142 and, by Cauchy, |q_r| <=3142*1200^(-r).
assert rho / RADIUS < arb(2) / 3
assert Fraction(3142) * Fraction(2, 3) ** 11 < 50

report = {
    "claim": "For the actual beta sequence, D_beta(1,r)>0 for every integer r>=1.",
    "verification_scope": "Arb rigorous interval certificate + analytic Cauchy tail argument; not Lean kernel audit, not RH.",
    "python": platform.python_version(),
    "python_flint": flint.__version__,
    "linked_flint": flint.__FLINT_VERSION__,
    "precision_bits": ctx.prec,
    "zeta_nzeros_20": show(count),
    "first_zeta_zero": show(zero),
    "beta0": show(beta0),
    "rho": show(rho),
    "fprime_rho": show(fprime),
    "pole_coefficient_A": show(A),
    "circle_radius": RADIUS,
    "covering_arcs": NSEG,
    "minimum_circle_f_lower_bound": show(minimum_f),
    "maximum_circle_H_upper_bound": show(M),
    "rational_bounds": {"rho_upper": 800, "A_lower": 50, "A_upper": 51,
                        "circle_H_upper": 3040, "analytic_remainder_upper": 3142,
                        "tail_ratio_upper": "2/3", "tail_starts_at_r": 11},
    "finite_prefix": [
        {"r": k, "h_r": show(h[k]), "h_r_times_rho_to_r": show(h[k] * rho ** k)}
        for k in range(PREFIX + 1)
    ],
    "status": "ALL_INTERVAL_ASSERTIONS_PASSED"
}
print(json.dumps(report, ensure_ascii=False, indent=2))