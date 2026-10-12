#!/usr/bin/env python3
"""Non-rigorous numerical sanity check of the analytic theta-translation theorem.

The proof is the analytic argument in REPORT.md. This script uses finite theta
truncations and quadrature, NOT interval arithmetic and NOT a RH certificate.
"""
import json
import sys
import mpmath as mp

mp.mp.dps = 45
A = mp.log(2) / 2
D = mp.log(2)
ALPHA = D / mp.sqrt(2)


def phi(x, cutoff=8):
    x = abs(x)  # genuine parity of the full theta kernel, not of one summand
    r = mp.exp(2 * x)
    return sum((4 * mp.pi**2 * n**4 * mp.exp(mp.mpf(9)/2 * x)
               - 6 * mp.pi * n**2 * mp.exp(mp.mpf(5)/2 * x))
               * mp.exp(-mp.pi * n*n * r) for n in range(1, cutoff+1))


def m(x):
    return mp.sqrt(phi(x)/(2*mp.cosh(x/2)))


def v(x, t):
    return (phi(x+t) + phi(x-t) - 2*mp.cosh(t/2)*phi(x))/m(x)


def unit_norm_sq(t):
    intervals = [(0, .5), (.5, 1), (1, 1.5), (1.5, 2),
                 (2, 2.5), (2.5, 3), (3, 4), (4, 5), (5, 6)]
    return 2*sum(mp.quad(lambda x: v(x,t)**2,[a,b]) for a,b in intervals)


def q_two(t):
    intervals = [(-4,-3),(-3,-2),(-2,-1),(-1,0),
                 (0,1),(1,2),(2,3),(3,4)]
    def edge(x):
        return ALPHA*m(x)*m(x+D)*(v(x+D,t)-v(x,t))**2
    return sum(mp.quad(edge,[a,b]) for a,b in intervals)


if __name__ == '__main__':
    out = []
    for raw in ['0.3400', '0.3450', '0.3465']:
        t = mp.mpf(raw)
        n2 = unit_norm_sq(t)
        edge = q_two(t)
        out.append({
            't': raw,
            'scaled_norm_sq': mp.nstr(n2*(A-t)**mp.mpf('2.5'), 17),
            'edge_energy': mp.nstr(edge, 17),
            'normalized_edge_energy': mp.nstr(edge/n2, 17)
        })
    print(json.dumps({
        'status': 'NONRIGOROUS_SANITY_ONLY',
        'python': sys.version.split()[0], 'mpmath':mp.__version__,
        'theta_modes':8, 'target_scaled_norm_sq':'3/128=0.0234375',
        'finite_integration_domains':{'norm':'|x|<=6','edge':'-4<=x<=4'},
        'runs':out
    },indent=2))
