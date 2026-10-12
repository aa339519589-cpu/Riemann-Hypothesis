#!/usr/bin/env python3
"""Exact algebra for the full-y theta growth-tail convexity theorem.
The finite checks do not prove RH or replace the analytic argument.
The output is created exclusively. No existing path is overwritten.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as s


def run() -> dict:
    a, t, z, v = s.symbols('a t z v')
    half = s.Rational(1, 2)
    def advance(A, B):
        # (1/2+a*d/da)(A*K+B*K') with
        # K''=(1+t/a**2)*K-K'/a, t=y**2.
        return (s.expand(half*A+a*s.diff(A,a)+(a+t/a)*B),
                s.expand(a*A-half*B+a*s.diff(B,a)))
    A, B = a**4+9*a**2, 6*a**3
    A1, B1 = advance(A,B)
    assert s.expand(A1-((s.Rational(21,2))*a**4+(s.Rational(45,2)+6*t)*a**2)) == 0
    assert s.expand(B1-(a**5+24*a**3)) == 0
    A2, B2 = advance(A1,B1)
    assert s.expand(A2-(a**6+(s.Rational(285,4)+t)*a**4+(s.Rational(225,4)+39*t)*a**2)) == 0
    assert s.expand(B2-(15*a**5+(s.Rational(165,2)+6*t)*a**3)) == 0
    P = s.expand(2*(a-s.Rational(1,4))*A2.subs(t,0)
                 -(2*(a-s.Rational(1,4))+3)*B2.subs(t,s.Rational(1,4)))
    R = s.expand(2*(a-s.Rational(1,4))*s.diff(A2,t)
                 -(2*(a-s.Rational(1,4))+1)*s.diff(B2,t))
    P_shift = s.Poly(P.subs(a,z+12),z)
    R_shift = s.Poly(R.subs(a,z+12),z)
    assert all(c>0 for c in P_shift.all_coeffs())
    assert all(c>0 for c in R_shift.all_coeffs())
    assert P.subs(a,12)==2323566
    assert R.subs(a,12)==365256
    # The integral lemma uses these two exact derivative identities.
    f=(1+v*v)*s.sinh(v)-v*s.cosh(v)
    assert s.simplify(s.diff(f,v)-(v*s.sinh(v)+v*v*s.cosh(v)))==0
    g=v*s.sinh(v)-2*(s.cosh(v)-1)
    assert s.simplify(s.diff(g,v)-(v*s.cosh(v)-s.sinh(v)))==0
    assert s.simplify(s.diff(v*s.cosh(v)-s.sinh(v),v)-v*s.sinh(v))==0
    # Triangle kernels have transform 2(1-cos(k*r))/k^2.
    # Evaluate the elementary half-line integral symbolically.
    x,k,r=s.symbols('x k r', positive=True)
    triangle=s.integrate(2*(r-x)*s.cos(k*x),(x,0,r))
    assert s.simplify(triangle-2*(1-s.cos(k*r))/k**2)==0
    return {'status':'PASS', 'rh_proved':False,
            'scope':'Exact finite algebra, not the analytic or RH claims',
            'python':platform.python_version(),'sympy':s.__version__,
            'A2':str(A2),'B2':str(B2),
            'P_factorized':str(s.factor(P)),'R_factorized':str(s.factor(R)),
            'P_shift_coefficients_descending':list(map(str,P_shift.all_coeffs())),
            'R_shift_coefficients_descending':list(map(str,R_shift.all_coeffs())),
            'P_at_12':str(P.subs(a,12)),'R_at_12':str(R.subs(a,12)),
            'checks':['Bessel first and second logarithmic derivatives',
                      'all shifted polynomial coefficients strictly positive',
                      'hyperbolic inequalities: derivative identities',
                      'triangle-kernel Fourier normalization'],
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    result=run()
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))
