#!/usr/bin/env python3
"""Exact scalar checks for GREEN_BAND_LOG_COST.md.

Only Python's standard library is required. All decisions use Fraction, not
floating point. This checks scalar ingredients, not the infinite-dimensional
operator argument, upstream domain theorems, or Riemann-zero verification.

Usage: python verify_green_band.py
The JSON result is written next to this script.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import json


def exp_bounds(x: Q, n: int = 64) -> tuple[Q, Q]:
    """Rational lower/upper bounds for exp(x), x >= 0.

    Include terms 0,...,n. Bound the remainder by its first term times
    a geometric series whose ratio is x/(n+2).
    """
    if x < 0 or n < 0 or x >= n + 2:
        raise ValueError('Require x >= 0 and n+2 > x.')
    term = Q(1)
    total = term
    for k in range(1, n + 1):
        term *= x / k
        total += term
    first_omitted = term * x / (n + 1)
    upper = total + first_omitted / (1 - x / (n + 2))
    return total, upper


def atan_bounds(x: Q, terms: int = 20) -> tuple[Q, Q]:
    """Alternating-series rational bounds for atan(x), 0 < x < 1."""
    if not 0 < x < 1 or terms < 1:
        raise ValueError('Require 0 < x < 1 and terms >= 1.')
    total = sum(((-1) ** k * x ** (2*k + 1) / (2*k + 1)
                 for k in range(terms)), Q(0))
    next_partial = total + (-1) ** terms * x ** (2*terms + 1) / (2*terms + 1)
    return min(total, next_partial), max(total, next_partial)


def main() -> None:
    a_lo, a_hi = atan_bounds(Q(1, 5))
    b_lo, b_hi = atan_bounds(Q(1, 239))
    # Machin identity: pi = 16 atan(1/5) - 4 atan(1/239).
    pi_lo, pi_hi = 16*a_lo - 4*b_hi, 16*a_hi - 4*b_lo
    assert pi_lo > Q(314159, 100000)
    assert pi_hi < Q(22, 7)

    e_lo, _ = exp_bounds(Q(1), 8)
    e3_lo, _ = exp_bounds(Q(3), 8)
    assert e_lo > 2
    assert e3_lo > 20
    # n^6 theta-series tail: the ratio after n=2 is < 1/4,
    # and exp(9) > 20^3 = 8000.
    assert Q(3, 2)**6 / 2**15 < Q(1, 4)
    assert Q(4, 3)*64/8000 < Q(1, 64)

    # q_n' = 4u + 24u/(2u-3)^2, and u >= pi > 3.
    # E[u] <= (65/32) pi exp(2x). Thus q' < 34 exp(2x).
    q_derivative_coefficient = Q(65, 8)*Q(22, 7) + 8
    assert q_derivative_coefficient == Q(939, 28) < 34
    theta_weight_coefficient = 2*17*4
    assert theta_weight_coefficient == 136
    full_line_central_coefficient = 2*theta_weight_coefficient
    assert full_line_central_coefficient == 272

    E_lo, E_hi = exp_bounds(Q(14, 5))
    assert E_lo > Q(164446, 10000)
    assert E_hi < 17
    assert 2*pi_lo*E_lo - 12 > 84

    # Recheck the inherited tail scalar without floating-point arithmetic:
    # 2^40 exp(84/5 - pi exp(14/5)) < 1/1000.
    d0 = Q(314159, 100000)*Q(164446, 10000) - Q(84, 5)
    ed0_lo, _ = exp_bounds(d0, 128)
    assert ed0_lo > 1000 * 2**40

    # Adaptive cutoff t=32+2L, L=log(1/delta0)>=0.
    # The remaining exponent is -(29/8)L, and the scalar factor is <2^-17.
    assert 2 + Q(3, 8) - 6 == -Q(29, 8)
    assert 193 < 2**8
    assert 41 + 8 + 30 - 96 == -17
    logarithmic_constant = 272*32 + 1
    logarithmic_coefficient = 272*2
    assert logarithmic_constant == 8705
    assert logarithmic_coefficient == 544

    physical_norm_upper = Q(272*17) + Q(2*193*21**2, 1000)
    assert physical_norm_upper == Q(2397113, 500)
    assert physical_norm_upper < 5000
    exclusion_margin = Q(1, 20) - physical_norm_upper/100000
    assert exclusion_margin == Q(102887, 50000000) > 0

    result = {
        'status': 'all exact rational scalar checks passed',
        'base_commit': '1cece5ec907004c5e1693148d223cbe75eeec1b3',
        'method': 'Fraction arithmetic; positive Taylor remainders; alternating atan bounds',
        'pi_enclosure_verified': ['314159/100000', '22/7'],
        'exp_14_over_5_enclosure_verified': ['164446/10000', '17'],
        'q_derivative_coefficient_upper': str(q_derivative_coefficient),
        'theta_weight_coefficient': theta_weight_coefficient,
        'full_line_central_coefficient': full_line_central_coefficient,
        'inherited_physical_tail_scalar': '< 1/1000, independently rechecked',
        'logarithmic_source_norm_bound': '8705 + 544 log(1/delta0)',
        'physical_norm_bound_at_green_lambda_21_over_20': str(physical_norm_upper),
        'exclusion_margin': str(exclusion_margin),
        'scope': 'scalar verification only; not an operator-domain, RH, or zero-location certificate'
    }
    out = Path(__file__).with_name('verification.json')
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
