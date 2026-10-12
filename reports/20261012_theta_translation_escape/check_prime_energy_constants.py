#!/usr/bin/env python3
"""Exact symbolic constants in PRIME_ENERGY_SCALING.md.

Does NOT prove PNT convergence, theta tails, or any RH statement.
"""
import json
import sympy as s

pi = s.pi
G = s.gamma
norm_constant = 4*pi**2 * 2**(-s.Rational(9,2)) * G(s.Rational(5,2)) / (2*pi)**s.Rational(5,2)
gamma_energy_constant = 2**(-s.Rational(11,2))
normalized_gamma_coeff = gamma_energy_constant / norm_constant
weighted_mass_constant = 2**(-s.Rational(9,2))
expected_weighted_rate = weighted_mass_constant / norm_constant
xi2 = pi/6
xi3 = 3*s.zeta(3)/(2*pi)
first_moment = 2*xi2 * G(3)/G(s.Rational(5,2))/(2*pi)**s.Rational(1,2)
second_moment = 2*xi3 * G(s.Rational(7,2))/G(s.Rational(5,2))/(2*pi)
checks = {
    'norm_sq_coefficient': (norm_constant, s.Rational(3,128)),
    'gamma_energy_sq_coefficient': (gamma_energy_constant, 2**(-s.Rational(11,2))),
    'normalized_gamma_sqrt_delta': (normalized_gamma_coeff, 2*s.sqrt(2)/3),
    'weighted_mass_sqrt_delta': (expected_weighted_rate, 4*s.sqrt(2)/3),
    'prime_scale_first_moment': (first_moment, 4*s.sqrt(2)/9),
    'prime_scale_second_moment': (second_moment, 15*s.zeta(3)/(4*pi**2)),
}
for label, (actual, expected) in checks.items():
    assert s.simplify(actual-expected) == 0, label
print(json.dumps({'status': 'PASS_EXACT_SYMBOLIC_CONSTANTS_ONLY',
                  'sympy':s.__version__,
                  'checks': {key:str(s.simplify(actual)) for key,(actual,_) in checks.items()},
                  'rh_proved':False},indent=2))
