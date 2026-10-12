#!/usr/bin/env python3
"""Exact rational checks for the analytic all-rank theta-frame estimate.

This checks the constants used in REPORT.md, not the theta identity, kernel
membership, or the RH conclusion. No third-party packages are required.
All results are produced by this execution; existing output is never replaced.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform


def run() -> dict:
    facts: dict[str, str | bool] = {}
    # exp(1)>8/3; 3<pi<4. Tail inequalities below are entirely rational
    # consequences of these analytic facts, which are proved/cited in REPORT.
    ratio = F(3, 2)**4 * F(3, 8)**15
    norm_tail = 32 * F(3, 8)**9
    assert ratio < F(1, 2)
    assert norm_tail < F(1, 2)
    facts['successive_theta_tail_ratio_upper'] = str(ratio)
    facts['u_times_tail_bound_upper'] = str(norm_tail)

    phi_global_upper = 128 * F(3, 8)**3
    assert phi_global_upper < 8
    assert F(6, 27) > F(1, 8)  # A(c)>6 exp(-9/4)>6/27.
    facts['phi_global_upper'] = str(phi_global_upper)
    # On |x|<=1/2, m(x)>1/243 and |f_t(x)|<=48.
    core_budget = 48**2 * 243**2 * 64
    # |r_c|<=256*g0; integral U_c*g0<=4; ||g0||=1.
    cross_budget = (2*256*4 + 256**2)*64
    leading_small_interval_budget = 16
    tail_factor_budget = 29
    total = core_budget + cross_budget + leading_small_interval_budget + tail_factor_budget
    assert total < 2**36
    facts['normalized_core_budget'] = str(core_budget)
    facts['normalized_cross_budget'] = str(cross_budget)
    facts['total_raw_gram_budget'] = str(total)
    facts['raw_gram_error_constant'] = str(2**36)

    c0 = F(1, 2**128)
    beta = F(1, 2**20)
    # Relative error <=2^36 sqrt(c+d)/Gamma(5/2), and Gamma(5/2)>1.
    assert F(2**72) * 2*c0 < beta**2
    norm_correction_ratio = (1+beta)/(1-beta)
    assert norm_correction_ratio < 2
    facts['c0'] = str(c0)
    facts['uniform_relative_error_beta'] = str(beta)
    facts['normalization_ratio_upper'] = str(norm_correction_ratio)

    # For c_j=c0*256^-j, K_l <= sqrt(32)*1024^-l <6*1024^-l.
    assert 32 < 6**2
    off_row = F(24, 1023)
    assert off_row < F(1, 32)
    facts['offdiagonal_schur_row_upper'] = str(off_row)
    facts['frame_lower'] = '31/32'
    facts['frame_upper'] = '33/32'
    facts['gram_condition_upper'] = '33/31'
    facts['inverse_neumann_norm_upper'] = '32/31'
    weighted_row = F(24,63)
    weighted_inverse = 1/(1-weighted_row)
    mixed = weighted_inverse*weighted_row
    assert weighted_row == F(8,21) and weighted_inverse == F(21,13)
    assert mixed == F(8,13)
    assert 1 + mixed*F(64,63) < 2
    assert (F(32,31)**2)*F(33,32) < 4
    assert F(64,15) < 8
    facts['weighted_gram_row'] = str(weighted_row)
    facts['weighted_inverse_row'] = str(weighted_inverse)
    facts['mixed_block_row'] = str(mixed)
    facts['true_source_projection_tail'] = '2^(-147) * 16^(-M)'
    # Projection inverse Neumann tail: (33/31)*32^(-L) < 2*32^(-L).
    for ell in (1, 2, 3, 8, 16):
        z = F(1, 32)**ell
        bound = F(33,31)*z
        assert bound > 0 and bound < F(2)*z
    facts['neumann_remainder_operator_bound'] = '2 * 32^(-L)'
    full_tail_constant = F(1,2**146)+285*F(3,8)**21
    assert full_tail_constant < 1
    assert F(8,3)**3 > 16
    # 2(M+7)^2-(6M+60)=2M^2+22M+38 is positive for all M>=0.
    assert all(c>0 for c in [2,22,38])
    facts['full_gamma_prime_tail_constant'] = str(full_tail_constant)
    facts['full_operator_tail'] = '(M+7)^2 * 16^(-M)'
    facts['full_gamma_form_tail'] = '(M+7) * 4^(-M)'
    return {
        'status': 'PASS_EXACT_RATIONAL_CONSTANTS_ONLY',
        'python': platform.python_version(),
        'arithmetic': 'fractions.Fraction; integers; no floating point',
        'checks': facts,
        'rh_proved': False,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    result = run()
    with a.output.open('x', encoding='utf-8') as w:
        json.dump(result, w, indent=2, ensure_ascii=False)
        w.write('\n')
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
