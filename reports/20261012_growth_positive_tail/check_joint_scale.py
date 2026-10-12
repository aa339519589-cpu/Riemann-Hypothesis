#!/usr/bin/env python3
"""Exact finite algebra for the expanding-cutoff theta growth theorem.
Analytic error bounds and the theorem's quantifiers are proved in the report.
"""
import argparse, hashlib, json, platform
from pathlib import Path
from fractions import Fraction as F
import sympy as s

def run():
    a,z=s.symbols('a z')
    P=a*a*(16*a**5-244*a**4+840*a**3-1629*a*a-780*a-225)/8
    Q=s.expand(P-(a-s.Rational(1,4))*a**6/2)
    coefficients=s.Poly(Q.subs(a,z+24),z).all_coeffs()
    assert all(c>0 for c in coefficients)
    # For |t|<=2, the alternating sine expansion gives this coefficient.
    assert F(1,6)-F(4,120)==F(2,15)>F(1,10)
    # The convexity lower bound is weakened using e^3<27.
    assert F(1,54)>F(1,64)
    assert 2*F(1,64)*F(1,10)==F(1,320)
    # At r>=2 a geometric tail bound for r^6*exp(-2*pi*r):
    # 2*pi>6 and e>8/3.
    ratio=F(3,2)**6*F(3,8)**6
    assert ratio<F(1,2)
    # Verify the Fourier integral producing the uniform frequency factor.
    t=s.symbols('t',real=True,nonzero=True)
    u=s.symbols('u',real=True)
    assert s.simplify(s.integrate(1-s.cos(t*u),(u,0,1))-(1-s.sin(t)/t))==0
    return {'status':'PASS','rh_proved':False,
            'scope':'Finite exact algebra only; not a proof of RH',
            'python':platform.python_version(),'sympy':s.__version__,
            'P_minus_quarter_a6_factored':str(s.factor(Q)),
            'shift_24_coefficients_descending':list(map(str,coefficients)),
            'sinc_small_argument_constant':'2/15','sinc_used_constant':'1/10',
            'curvature_used_constant':'1/64','fourier_lower_constant':'1/320',
            'geometric_ratio_upper':str(ratio),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=run()
    with a.output.open('x') as f:json.dump(o,f,indent=2);f.write('\n')
    print(json.dumps(o,indent=2))
