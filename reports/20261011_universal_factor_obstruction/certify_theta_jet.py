#!/usr/bin/env python3
"""Exact rational enclosure of a theta-source logarithmic-jet obstruction.

Only Python's standard library is used. Every arithmetic interval operation
rounds outward onto a rational decimal grid. Pi uses Machin's alternating
arctangent series; exp(-x) uses an alternating Taylor series after scaling.
The omitted theta modes have an explicit rational bound proved in REPORT.md.
This certifies source derivatives, not zeros of the Fourier transform.
All output files are created exclusively, never overwritten.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path

DIGITS = 60
SCALE = 10 ** DIGITS


def floor_grid(x: F) -> F:
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def ceil_grid(x: F) -> F:
    return -floor_grid(-x)


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('Reversed interval')

    @staticmethod
    def point(x) -> 'I':
        x = F(x)
        return I(x, x)

    @staticmethod
    def rounded(lo: F, hi: F) -> 'I':
        return I(floor_grid(lo), ceil_grid(hi))

    def __add__(self, other):
        other = as_interval(other)
        return I.rounded(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) + (-self)

    def __mul__(self, other):
        other = as_interval(other)
        v = [self.lo * other.lo, self.lo * other.hi,
             self.hi * other.lo, self.hi * other.hi]
        return I.rounded(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_interval(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError('Interval contains zero')
        inv = I.rounded(1 / other.hi, 1 / other.lo)
        return self * inv

    def __pow__(self, n: int):
        if n < 0:
            return I.point(1) / (self ** (-n))
        out, base = I.point(1), self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def decimal_bounds(self):
        return [decimal_exact(floor_grid(self.lo)),
                decimal_exact(ceil_grid(self.hi))]


def as_interval(x) -> I:
    return x if isinstance(x, I) else I.point(x)


def decimal_exact(x: F) -> str:
    scaled = x * SCALE
    if scaled.denominator != 1:
        raise ValueError('Endpoint is not on the output grid')
    n = scaled.numerator
    sign = '-' if n < 0 else ''
    n = abs(n)
    return f'{sign}{n // SCALE}.{n % SCALE:0{DIGITS}d}'


def atan_rational_bounds(x: F, terms: int) -> I:
    if not 0 < x < 1:
        raise ValueError('Alternating arctan argument outside (0,1)')
    value = sum(((-1)**k * x**(2*k+1) / (2*k+1)
                 for k in range(terms)), F(0))
    next_value = value + (-1)**terms * x**(2*terms+1) / (2*terms+1)
    return I.rounded(min(value, next_value), max(value, next_value))


def exp_minus_point(x: F, terms: int) -> I:
    if not 0 <= x <= 1:
        raise ValueError('Alternating exponential argument outside [0,1]')
    term, value = F(1), F(1)
    for k in range(1, terms):
        term *= -x / k
        value += term
    next_value = value + term * (-x / terms)
    return I.rounded(min(value, next_value), max(value, next_value))


def exp_minus(x: I, terms: int) -> I:
    # exp(-x) is decreasing. x/256 is at most 49*pi/256 < 1.
    y = x / 256
    lo = exp_minus_point(y.hi, terms).lo
    hi = exp_minus_point(y.lo, terms).hi
    return I.rounded(lo, hi) ** 256


def poly_next(p: list[F]) -> list[F]:
    q = [F(0)] * (len(p) + 1)
    for k, c in enumerate(p):
        q[k] += (F(5, 2) + 2*k) * c
        q[k+1] -= 2*c
    return q


def poly_eval(p: list[F], x: I) -> I:
    out = I.point(0)
    for c in reversed(p):
        out = out * x + c
    return out


def strictly_inside(x: I, a: str, b: str):
    if not F(a) < x.lo <= x.hi < F(b):
        raise AssertionError(f'Enclosure failed for ({a},{b})')


def certificate(digits: int) -> dict:
    global DIGITS, SCALE
    DIGITS, SCALE = digits, 10**digits
    if digits < 45:
        raise ValueError('Use at least 45 decimal grid digits')
    terms = digits + 30
    pi = 16*atan_rational_bounds(F(1,5), terms) - 4*atan_rational_bounds(F(1,239), terms)
    assert F(3) < pi.lo < pi.hi < F(4)

    ps = [[F(-3), F(2)]]
    for j in range(12):
        ps.append(poly_next(ps[-1]))
    for j, p in enumerate(ps):
        assert len(p) == j+2
        assert sum(map(abs, p)) <= 5*8**j*factorial(j)

    ratio = F(9,8)**28 * F(3,8)**51
    assert ratio < F(1,2)
    C = 10 * 4**14 * 8**12 * factorial(12)
    tail = 2*C * 8**28 * F(3,8)**192
    assert tail < F(1,10**27)
    theta_terms = [(pi*(n*n), exp_minus(pi*(n*n),terms),n*n) for n in range(1,8)]
    a = [I.point(0) for _ in range(13)]
    derivative_bounds = {}
    for j in range(0,13,2):
        partial = sum((2*pi*n2*e*poly_eval(ps[j],u) for u,e,n2 in theta_terms), I.point(0))
        value = partial + I(-tail,tail)
        derivative_bounds[str(j)] = value.decimal_bounds()
        a[j] = value / factorial(j)
    assert a[0].lo > 0
    b = [I.point(0) for _ in range(13)]
    for n in range(1,13):
        # a = exp(b) up to its constant factor. Odd coefficients are exactly
        # zero by the true theta transformation, not numerical cancellation.
        if n % 2:
            continue
        previous = sum((k*b[k]*a[n-k] for k in range(1,n)),I.point(0))
        b[n] = (n*a[n]-previous)/(n*a[0])
    p = {k: ((-1)**(k+1))*k*b[2*k] for k in (4,5,6)}
    determinant = p[4]*p[6]-p[5]**2
    boxes = {4:('24.217595281065','24.217595281066'),
             5:('74.323417808078','74.323417808080'),
             6:('220.503643148115','220.503643148117')}
    for k,box in boxes.items():
        strictly_inside(p[k],*box)
    strictly_inside(determinant,'-183.902446914','-183.902446911')
    # A deliberately wide open jet neighborhood remains separated.
    neighborhood_upper = F('24.23')*F('220.52')-F('74.31')**2
    assert neighborhood_upper < -170
    return {
        'status':'PASS: exact rational outward enclosures; NOT an RH proof',
        'arithmetic':'Python fractions.Fraction, outward rational decimal grid',
        'grid_digits':digits,
        'arctan_and_exp_terms':terms,
        'included_theta_modes':[1,7],
        'highest_source_derivative':12,
        'pi_bounds':pi.decimal_bounds(),
        'common_derivative_tail_bound':str(tail),
        'tail_is_less_than':'1/10^27',
        'tail_ratio_bound':str(ratio),
        'derivative_bounds':derivative_bounds,
        'log_jet_moments':{str(k):v.decimal_bounds() for k,v in p.items()},
        'hankel_determinant':determinant.decimal_bounds(),
        'asserted_moment_boxes':{str(k):list(v) for k,v in boxes.items()},
        'asserted_determinant_box':['-183.902446914','-183.902446911'],
        'open_neighborhood':{'p4':['24.21','24.23'],'p5':['74.31','74.34'],'p6':['220.49','220.52']},
        'neighborhood_determinant_upper':str(neighborhood_upper),
        'source_polynomials':[[str(v) for v in q] for q in ps],
        'external_software_packages':[],
        'rh_proved':False,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits', type=int, default=60)
    parser.add_argument('--output', type=Path, required=True)
    args=parser.parse_args()
    result=certificate(args.digits)
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps({k:result[k] for k in ['status','grid_digits','log_jet_moments','hankel_determinant','neighborhood_determinant_upper']},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
