"""Exact finite algebra only; analytic domains and positivity are proved in REPORT.md."""
import json
import sympy as s
z,h,v,L=s.symbols('z h v L', positive=True)
A=z*z+9
B=6*z

def op(A,B):
    return (s.expand(5*A+2*z*s.diff(A,z)+2*z*B+2*v*B/z),
            s.expand(3*B+2*z*A+2*z*s.diff(B,z)))
A2,B2=op(*op(A,B))
expected_A=4*z**4+285*z*z+225+(4*z*z+156)*v
expected_B=(60*z*z+330+24*v)*z
P0=s.expand(A2.subs(v,0)-B2.subs(v,0)*(1+s.Rational(1,2)/z))
P2=s.expand(A2.subs(v,0)-B2.subs(v,0)*(1+s.Rational(3,2)/z))
extra=s.expand(2*s.diff(A2,v)-2*s.diff(B2,v)*(1+s.Rational(1,2)/z))
integ0=L**2+8*L+17
integ1=(L+3)**3
checks={
 'bessel_D2_K_coefficient':s.simplify(A2-expected_A)==0,
 'bessel_D2_Kprime_coefficient':s.simplify(B2-expected_B)==0,
 'P0_shift':s.expand(P0.subs(z,12+h))==4*h**4+132*h**3+1551*h**2+7518*h+12084,
 'P2_shift':s.expand(P2.subs(z,12+h))==4*h**4+132*h**3+1491*h**2+6078*h+3114,
 'order_second_derivative_extra':s.expand(extra-8*((z-3)**2+27))==0,
 'tail_antiderivative0':s.expand(integ0-s.diff(integ0,L)-(L+3)**2)==0,
 'tail_antiderivative1':s.expand(integ1-s.diff(integ1,L)-L*(L+3)**2)==0,
}
assert all(checks.values())
output={'checks':checks,'scope':'Exact polynomial identities only. No numerical sampling and no RH claim.'}
print(json.dumps(output,ensure_ascii=False,indent=2))
