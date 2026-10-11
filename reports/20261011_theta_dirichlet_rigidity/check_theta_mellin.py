#!/usr/bin/env python3
"""Exact finite algebra checks; not a verification of RH or distribution theory."""
import json
import platform
from pathlib import Path

import sympy as s

x = s.symbols('x', real=True)
n = s.symbols('n', positive=True, integer=True)
z, w, a, delta = s.symbols('z w a delta')
t = s.symbols('t')
u = s.pi*n**2*s.exp(2*x)
U = s.exp(x/2)*s.exp(-u)
phi = (4*s.pi**2*n**4*s.exp(s.Rational(9,2)*x)-6*s.pi*n**2*s.exp(s.Rational(5,2)*x))*s.exp(-u)
seed_residual = s.simplify(s.diff(U,x,2)-U/4-phi)

# Gamma recurrence is checked after replacing Gamma(r+2),Gamma(r+1)
# by their exact recurrence factors times Gamma(r).
r = s.symbols('r')
gamma_residual = s.expand(2*r*(r+1)-3*r - s.Rational(1,2)*(2*r)*(2*r-1))

# U(x)-U(-x)=C*sinh(x/2), and the zero Gaussian mass a0=-C.
C = s.symbols('C')
theta_reflection_residual = s.simplify(((-C)*(s.exp(x/2)-s.exp(-x/2))+2*C*s.sinh(x/2)).rewrite(s.exp))

# The Laplace transform of cos(a*x)*cosh(delta*x).
laplace_rational = sum(s.Rational(1,4)/(w-e*delta-s.I*h*a) for e in [-1,1] for h in [-1,1])
laplace_closed = s.Rational(1,2)*((w-delta)/((w-delta)**2+a*a)+(w+delta)/((w+delta)**2+a*a))
laplace_residual = s.factor(laplace_rational-laplace_closed)
example = laplace_rational.subs({a:3,delta:s.Rational(1,4)})
poles = [e*s.Rational(1,4)+s.I*h*3 for e in [-1,1] for h in [-1,1]]
residues = [s.residue(example,w,p) for p in poles]

# Correct change of Fourier variable for the fixed-Gamma quotient.
fourier_argument_residual = s.simplify(-(-s.I*(t-s.Rational(1,2)))**2-(t-s.Rational(1,2))**2)

checks = {
    'exact_seed_second_order_identity': seed_residual == 0,
    'exact_Gamma_recurrence_normalization': gamma_residual == 0,
    'zero_mass_removes_ODE_reflection_defect': theta_reflection_residual == 0,
    'four_pole_Laplace_formula': laplace_residual == 0,
    'all_four_residues_equal_one_quarter': all(v==s.Rational(1,4) for v in residues),
    'Fourier_to_Mellin_polynomial_argument': fourier_argument_residual == 0,
}
assert all(checks.values())
out = {
    'status':'EXACT_FINITE_ALGEBRA_ONLY',
    'scope':'Checks finite symbolic identities used in theta/Mellin rigidity. Does not certify the infinite distribution proof, Dirichlet convergence, spectral conclusions, or RH.',
    'python':platform.python_version(),'sympy':s.__version__,
    'checks':checks,
    'example_poles':[str(p) for p in poles],
    'example_residues':[str(r) for r in residues],
}
Path(__file__).with_name('theta_mellin_exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
