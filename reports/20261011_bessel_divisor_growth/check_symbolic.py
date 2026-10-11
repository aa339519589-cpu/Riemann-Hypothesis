#!/usr/bin/env python3
"""Exact algebra checks for REPORT.md; not an RH certificate.

This checks finite polynomial identities and rational sign bounds. It does
not independently prove convergence, Poisson summation, or Bessel integrals.
"""
import argparse, hashlib, json
from pathlib import Path
import sympy as s


def run():
    a,c,u,x,y,d,R=s.symbols('a c u x y d R',real=True)
    P=a**4+9*a*a-6*a**3*c
    Q=s.expand((s.Rational(1,2)-a*c)*P+a*s.diff(P,a))
    expected=6*a**4*c*c-(a**5+30*a**3)*c+s.Rational(9,2)*a**4+s.Rational(45,2)*a*a
    assert s.expand(Q-expected)==0
    assert s.factor(Q.subs(c,1)) == -a*a*(a-3)*(2*a*a-15*a+15)/2
    assert s.expand(s.diff(Q,c).subs(c,1)-a**3*(12*a-a*a-30))==0
    # After K''=(1+nu^2/a^2)K-K'/a, Q-integral gives J_nu.
    K,Kp,Kpp,nu=s.symbols('K Kp Kpp nu')
    raw=6*a**4*Kpp+(a**5+30*a**3)*Kp+(s.Rational(9,2)*a**4+s.Rational(45,2)*a*a)*K
    J=(s.Rational(21,2)*a**4+(s.Rational(45,2)+6*nu**2)*a*a)*K+(a**5+24*a**3)*Kp
    assert s.expand(raw.subs(Kpp,(1+nu**2/a**2)*K-Kp/a)-J)==0
    z=x+s.I*y
    g=lambda v:v*(v*v+d*d)
    diff=s.expand(g(z)*g(s.conjugate(z))-g(x)**2)
    assert s.expand(diff-y*y*(3*x**4+3*x*x*y*y+(y*y-d*d)**2))==0
    Pz=s.expand(-g(x-R)*g(x+R))
    C=R*R*(R*R+d*d)**2
    assert s.expand(Pz-(C-(3*R**4+d**4)*x*x+(3*R*R-2*d*d)*x**4-x**6))==0
    # Even derivatives of exp(-cosh t) divided by exp(-cosh t).
    r=s.Integer(1);derivatives=[]
    for j in range(3):
        r=s.expand((c*c-1)*s.diff(r,c,2)+(-2*c*c+c+2)*s.diff(r,c)+(c*c-c-1)*r)
        shifted=s.Poly(r.subs(c,16+u),u)
        assert all(v>0 for v in shifted.all_coeffs())
        derivatives.append(r)
    bounds=[s.Integer(1)]+[sum(abs(coef)*16**int(power[0]) for power,coef in s.Poly(p,c).terms()) for p in derivatives[1:]]
    Cv=C.subs({R:100,d:s.Rational(1,4)})
    alpha=(3*R**4+d**4).subs({R:100,d:s.Rational(1,4)})
    beta=(3*R*R-2*d*d).subs({R:100,d:s.Rational(1,4)})
    margin=Cv-alpha*bounds[0]-beta*bounds[1]-bounds[2]
    assert margin > s.Rational(99,100)*Cv
    return {'status':'PASS exact symbolic and rational checks','sympy':s.__version__,
            'Q':str(Q),'Q_at_1':str(s.factor(Q.subs(c,1))),
            'cubic_modulus_difference':str(s.factor(diff)),
            'normalized_polynomial_numerator':str(Pz),
            'Bessel_seed_even_derivative_ratios':[str(p) for p in derivatives],
            'ratio_lower_bounds':[-int(v) for v in bounds],
            'positive_source_example':{'R':100,'d':'1/4','C':str(Cv),'margin':str(margin),'lower_fraction':'99/100'},
            'scope':'finite algebra only; analytic proofs are in REPORT.md','rh_proved':False,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run()
    with a.output.open('x',encoding='utf-8') as f:json.dump(r,f,indent=2);f.write('\n')
    print(json.dumps(r,indent=2))
