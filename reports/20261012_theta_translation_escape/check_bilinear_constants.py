#!/usr/bin/env python3
"""Exact algebraic checks of mixed critical-mode Mellin constants, NOT RH."""
import json
import sympy as S

th = S.symbols('theta', positive=True)
pi = S.pi
Gam = S.gamma
r0 = S.Rational(3,128)
A = 4*pi**2*2**(-S.Rational(9,2))
for sval in [-3,-1,0,1,2]:
    shape=S.Rational(sval+5,2)
    original = A/r0*Gam(shape) * (pi*(1+th))**(-shape) * th**(shape/2)
    expected = (2*pi)**(-S.Rational(sval,2))*Gam(shape)/Gam(S.Rational(5,2)) * (2*S.sqrt(th)/(1+th))**shape
    assert S.simplify(original-expected)==0, sval

G = S.simplify(S.Rational(1,2)*A*Gam(2)/(r0*pi**2)*th**S.Rational(5,4)/(1+th)**2)
assert S.simplify(G-(8*S.sqrt(2)/3)*th**S.Rational(5,4)/(1+th)**2)==0
assert S.simplify(G.subs(th,1)-2*S.sqrt(2)/3)==0
xi5=S.Rational(15,2)*S.zeta(5)/pi**2
coef=S.simplify(A/r0*xi5)
assert S.simplify(coef-40*S.sqrt(2)*S.zeta(5))==0
print(json.dumps({'status':'PASS_EXACT_ALGEBRA_ONLY','sympy':S.__version__,
  'mixed_power_tests':[-3,-1,0,1,2],
  'gamma_cross_coefficient':str(G),
  'gamma_equal_scale':str(S.simplify(G.subs(th,1))),
  's_minus_5_log_coefficient':str(coef),
  'rh_proved':False},indent=2))
