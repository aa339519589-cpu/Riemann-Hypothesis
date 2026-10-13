#!/usr/bin/env python3
"""Exact SymPy consistency checks, not verification of infinite-energy estimates or RH."""
import json
import math
import sympy as S

z, z0, U, A = S.symbols('z z0 U A', nonzero=True)
J0, J1, J2, J3 = S.symbols('J0 J1 J2 J3')
counts = []
for m in range(1, 7):
    jets = S.symbols(f'j0:{m+1}')
    Taylor = sum(jets[k]*(z-z0)**k/S.factorial(k) for k in range(m+1))
    Xi = (z-z0)**m*(1+2*(z-z0)+3*(z-z0)**2)
    F = z**3*Xi
    D = -z**2*Taylor-F*U/A
    for k in range(m):
        lhs = S.diff(D,z,k).subs(z,z0)
        right = -z0*z0*jets[k]
        if k>=1: right -= 2*k*z0*jets[k-1]
        if k>=2: right -= k*(k-1)*jets[k-2]
        assert S.simplify(lhs-right)==0,(m,k)
        assert S.simplify(S.diff(F,z,k).subs(z,z0))==0
    boundary = S.factor(S.diff(D,z,m).subs(z,z0)+z0**2*jets[m]+2*m*z0*jets[m-1] + (m*(m-1)*jets[m-2] if m>=2 else 0))
    assert S.simplify(boundary+S.factorial(m)*z0**3*U/A)==0
    counts.append({'multiplicity':m,'zero_defect_jet_orders':list(range(m)),
                   'first_nonzero_defect':'-'+str(S.factorial(m))+'*z0**3*U/A'})

# At z=i/2, completed xi is 1/2, and the cutoff nonclosability pairing
# limit is -z^3*xi(z)=i/16.  This is exact arithmetic, not an RH statement.
zi=S.I/S.Integer(2)
assert S.simplify(-zi**3/S.Integer(2)-S.I/S.Integer(16))==0
print(json.dumps({'status':'PASS_EXACT_FORMAL_JET_ALGEBRA',
'multiplicity_cases':counts,
'nonzero_completed_endpoint_test':'z=i/2; Xi(z)=1/2; limit J_z(B chi_R)=i/16',
'analytic_tail_and_operator_domain_proved_by_script':False,
'rh_proved':False},ensure_ascii=False,indent=2))
