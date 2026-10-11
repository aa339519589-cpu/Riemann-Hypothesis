"""Rigorous Arb certificate + rational tail constants for D_beta(2,r)>0.

Pending independent review. Not a Lean kernel verification, not RH.
Requires python-flint==0.9.0; the original run linked FLINT 3.6.0.
"""
from pathlib import Path
import json
import platform
import sys
from fractions import Fraction as F
try:
    import flint
except ImportError:
    sys.path.insert(0, "/workspace/shared/rh_low_start_20261007/vendor")
    import flint
from flint import arb, acb, acb_series, arb_mat, ctx
ctx.prec = 1024
PREFIX = 37
RADIUS = 2200
NSEG = 4096


def show(x):
    return x.str(35)


def xi(s):
    return s * (s - 1) * (-s * arb.pi().log() / 2).exp() * (s / 2).gamma() * s.zeta() / 2


# beta_0,...,beta_38; D_h(37,2) needs h_38.
ctx.cap = 2 * (PREFIX + 1) + 1
s = acb_series([acb("0.5"), acb(0, "0.5")])
E = xi(s) / 8
beta = [((-1) ** k * E[2 * k]).real for k in range(PREFIX + 2)]
assert all(b > 0 for b in beta)
beta0 = beta[0]
h = [arb(1)]
for n in range(1, PREFIX + 2):
    h.append(-sum(((-1) ** k * beta[k] * h[n - k] / beta0
                   for k in range(1, n + 1)), arb(0)))

# Total zero count with multiplicity, all real parts.
count = arb(24).zeta_nzeros()
assert count == 2
assert arb(RADIUS).sqrt() / 2 < 24
ctx.cap = 2
zeros, rho, A, derivatives = [], [], [], []
for n in (1, 2):
    zero = acb.zeta_zero(n)
    assert zero.real == arb("0.5")
    r = 4 * zero.imag ** 2
    sp = acb_series([zero, 1])
    fp = (acb(0, 1) * xi(sp)[1] / (32 * r.sqrt())).real
    assert not fp.contains(0)
    a = -beta0 / (r * fp)
    zeros.append(zero)
    rho.append(r)
    A.append(a)
    derivatives.append(fp)
assert rho[0] > 799 and rho[0] < 800
assert rho[1] > 1767 and rho[1] < 1768
assert A[0] > 50 and A[0] < 51
assert A[1] > -2665 and A[1] < -2664
C = -A[0] * A[1] * (rho[1] - rho[0]) ** 2 / (rho[0] * rho[1])
assert C > 90000

# Full-circle interval cover, not point sampling.
M = arb(0)
minimum_f = arb(1)
for j in range(NSEG):
    angle = arb.pi() * (2 * j + 1) / NSEG
    angle += arb(0, (arb.pi() / NSEG).upper())
    root = arb(RADIUS).sqrt() * acb(0, angle / 2).exp()
    s_arc = acb("0.5") - acb(0, 1) * root / 2
    f_arc = xi(s_arc) / 8
    assert not f_arc.contains(0), (j, show(f_arc))
    lo = f_arc.abs_lower()
    assert lo > arb("0.00000019")
    if lo < minimum_f:
        minimum_f = lo
    up = (beta0 / f_arc).abs_upper()
    assert up < 1284000
    if up > M:
        M = up
assert M < 1284000
assert minimum_f > arb("0.00000019")

# All following constants/decays are checked by exact rational arithmetic.
MR = 1295000
assert F(1284000) + F(51) / (F(2200, 800) - 1) + F(2665) / (F(2200, 1768) - 1) < MR
c1 = F(MR * 51, 90000) * (2 + F(800, 2200) + F(2200, 799))
c2 = F(MR * 2665, 90000) * (2 + F(1768, 2200) + F(2200, 1767))
c3 = F(2 * MR ** 2, 90000)
assert c1 < 3760
assert c2 < 155500
assert c3 < 37300000
ratios = (F(221, 275), F(4, 11), F(800 * 1768, 2200 ** 2))
assert all(0 < t < 1 for t in ratios)
tail38 = 3760 * ratios[0] ** 38 + 155500 * ratios[1] ** 38 + 37300000 * ratios[2] ** 38
assert tail38 < 1

prefix = []
for r in range(1, PREFIX + 1):
    d = h[r] ** 2 - h[r - 1] * h[r + 1]
    assert d > 0, (r, show(d))
    prefix.append({"r": r, "D_h(r,2)": show(d),
                   "D_h(r,2)_times_(rho1rho2)^r": show(d * (rho[0] * rho[1]) ** r)})

# Independent direct actual-beta Toeplitz determinants, not just reciprocal recurrence.
direct_prefix = []
for r in range(1, PREFIX + 1):
    matrix = arb_mat([[beta[2+j-i] if 2+j-i>=0 else arb(0) for j in range(r)] for i in range(r)])
    direct = matrix.det()
    assert direct > 0, (r, show(direct))
    dual = beta0 ** r * (h[r] ** 2 - h[r-1] * h[r+1])
    assert (direct-dual).contains(0), (r, show(direct-dual))
    direct_prefix.append({"r":r,"direct_actual_D_beta_2_r":show(direct)})
report = {
    "claim": "For the actual beta sequence, D_beta(2,r)>0 for every integer r>=1.",
    "verification_scope": "Arb rigorous interval certificate + analytic two-pole determinant tail argument; pending independent review; not Lean, not RH.",
    "python": platform.python_version(),
    "python_flint": flint.__version__,
    "linked_flint": flint.__FLINT_VERSION__,
    "precision_bits": ctx.prec,
    "beta0": show(beta0),
    "zeta_nzeros_24": show(count),
    "poles": [{"index": n + 1, "zeta_zero": show(zeros[n]), "rho": show(rho[n]),
               "fprime": show(derivatives[n]), "A": show(A[n])} for n in range(2)],
    "positive_main_coefficient_C": show(C),
    "circle_radius": RADIUS,
    "covering_arcs": NSEG,
    "minimum_circle_f_lower_bound": show(minimum_f),
    "maximum_circle_H_upper_bound": show(M),
    "rational_tail": {"analytic_remainder_MR": MR, "main_C_lower": 90000,
                      "relative_error_constants": [3760, 155500, 37300000],
                      "decay_ratios": [str(x) for x in ratios],
                      "tail38_exact_numerator": tail38.numerator,
                      "tail38_exact_denominator": tail38.denominator,
                      "tail38_is_strictly_less_than_one": True,
                      "tail_starts_at_r": 38},
    "finite_prefix": prefix,
    "independent_direct_beta_determinants": direct_prefix,
    "status": "ALL_INTERVAL_AND_RATIONAL_ASSERTIONS_PASSED"
}
print(json.dumps(report, ensure_ascii=False, indent=2))