#!/usr/bin/env python3
"""Exact constants and algebraic countercheck for EXACT_BASE_DECOUPLING.md.

Only Python standard-library rational arithmetic is used. These finite checks
are not a verification of the theta identity, the operator domains, or RH.
Output files are created exclusively, never replaced.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

Matrix = list[list[F]]


def zeros(n: int, m: int) -> Matrix:
    return [[F(0) for _ in range(m)] for _ in range(n)]


def diag(v: list[F]) -> Matrix:
    a = zeros(len(v), len(v))
    for i, x in enumerate(v):
        a[i][i] = x
    return a


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def add(a: Matrix, b: Matrix, factor: F = F(1)) -> Matrix:
    return [[x+factor*y for x, y in zip(row, other)]
            for row, other in zip(a, b)]


def scale(a: Matrix, factor: F) -> Matrix:
    return [[factor*x for x in row] for row in a]


def mul(a: Matrix, b: Matrix) -> Matrix:
    assert len(a[0]) == len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a: Matrix) -> int:
    a = [row[:] for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][j]
        a[r] = [x/v for x in a[r]]
        for i in range(r+1, len(a)):
            a[i] = [x-a[i][j]*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def pinch(a: Matrix, p: Matrix) -> Matrix:
    one = diag([F(1)]*len(a))
    q = add(one, p, F(-1))
    return add(mul(mul(p, a), p), mul(mul(q, a), q))


def det2(a: Matrix) -> F:
    assert len(a) == len(a[0]) == 2
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def inv2(a: Matrix) -> Matrix:
    d = det2(a)
    assert d
    return [[a[1][1]/d, -a[0][1]/d], [-a[1][0]/d, a[0][0]/d]]


def constant_checks() -> dict:
    q = F(27, 512)
    v_bound = 8*128*q + 256*(q*(1+q)/(1-q)**3-q)
    assert v_bound == F(13055795757, 228168250) and v_bound < 64
    ratio = F(81, 1024)
    assert 1/(1-ratio) == F(1024, 943) < F(12, 11)
    assert F(24, 11)*F(129, 2) == F(1548, 11) < 144
    assert 15**2 < 2**8
    # At M>=8, the next polynomial-factor ratio is at most (16/15)^2<2.
    assert F(16, 15)**2 < 2
    beta = F(1, 2**20)
    assert (1+beta)/(1-beta) < F(5, 4)
    assert F(15, 31) < F(1, 2)
    rows = []
    for k in (3, 10, 20, 100):
        epsilon = F(1, 2**k)
        for power in (0, 1, 2):
            eta = epsilon**power / 4
            m = 8
            while F(8)**m * eta * epsilon**2 < 144:
                m += 1
            d = F((m+7)**2, 16**m)
            rho = F(12, 11)*d
            exact_bound = 2*rho*(epsilon+64)/epsilon**2
            assert exact_bound <= eta
            assert F((m+7)**2) <= F(2)**m
            rows.append({'epsilon': str(epsilon), 'eta': str(eta),
                         'mode_count': m, 'correction_rank_at_most': 2*m,
                         'trace_error_bound': str(exact_bound)})
    return {'V_upper': str(v_bound), 'V_upper_less_than': '64',
            'geometric_trace_factor': str(1/(1-ratio)),
            'conservative_trace_factor': '12/11',
            'BS_constant': '144', 'interleaved_gram_off_row': '15/31',
            'residual_frame_lower': '1/2', 'residual_frame_upper': '33/32',
            'parameter_cases': rows}


def matrix_countercheck() -> dict:
    l = [[F(x) for x in row] for row in
         [[1, 0, 0, 0, 0], [1, 2, 0, 0, 0], [2, -1, 1, 0, 0],
          [1, 1, 1, 2, 0], [-1, 2, 0, 1, 3]]]
    one = diag([F(1)]*5)
    b = add(one, scale(mul(l, transpose(l)), F(1, 16)))
    h = diag([F(0), F(0), F(-1, 2), F(-1, 16), F(1, 3)])
    v = add(b, h, F(-1))
    p = diag([F(1), F(1), F(0), F(0), F(0)])
    pm = diag([F(1), F(0), F(0), F(0), F(0)])
    assert mul(p, p) == p and mul(pm, pm) == pm
    assert mul(h, p) == zeros(5, 5)
    assert mul(b, p) == mul(v, p)
    bf, vf = pinch(b, p), pinch(v, p)
    bm, vm = pinch(b, pm), pinch(v, pm)
    assert add(bf, vf, F(-1)) == h
    assert add(bm, vm, F(-1)) == h
    assert add(bf, b, F(-1)) == add(vf, v, F(-1))
    assert mul(bf, p) == mul(p, bf)
    assert mul(vf, p) == mul(p, vf)
    r = add(p, pm, F(-1))
    j = add(one, scale(p, F(2)), F(-1))
    jm = add(one, scale(pm, F(2)), F(-1))
    diff_rhs = scale(add(mul(mul(r, b), j), mul(mul(jm, b), r)), F(-1))
    assert add(bf, bm, F(-1)) == diff_rhs
    rank_full = rank(add(bf, b, F(-1)))
    rank_one = rank(add(bm, b, F(-1)))
    assert rank_full <= 4 and rank_one <= 2
    eps = F(1, 128)
    c = [row[:2] for row in bf[:2]]
    assert c[0][0] > 0 and det2(c) > 0
    ce = add(c, diag([eps, eps]))
    known_complement = scale(inv2(ce), eps)
    assert known_complement[0][0] > 0 and det2(known_complement) > 0
    # C commutes with C+eps and its inverse; this matrix is I-C/(C+eps).
    assert add(diag([F(1), F(1)]), mul(c, inv2(ce)), F(-1)) == known_complement
    full_diag = [h[i][i]+eps for i in range(5)]
    negative_count = sum(x < 0 for x in full_diag)
    assert negative_count == 2
    return {'exact_H_preserved': True,
            'infinite_style_two_mode_correction_rank': rank_full,
            'one_mode_correction_rank': rank_one,
            'epsilon': str(eps),
            'known_block_I_minus_BS_positive': True,
            'known_block_determinant': str(det2(known_complement)),
            'full_H_plus_epsilon_diagonal': [str(x) for x in full_diag],
            'full_negative_count': negative_count,
            'purpose': 'Known-kernel safety does not certify the orthogonal complement.'}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    result = {'status': 'PASS_EXACT_RATIONAL_CONSTANTS_AND_ALGEBRA_ONLY',
              'python': platform.python_version(), 'third_party_packages': [],
              'constants': constant_checks(), 'countercheck': matrix_countercheck(),
              'rh_proved': False,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    with a.output.open('x', encoding='utf-8') as w:
        json.dump(result, w, indent=2, ensure_ascii=False)
        w.write('\n')
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
