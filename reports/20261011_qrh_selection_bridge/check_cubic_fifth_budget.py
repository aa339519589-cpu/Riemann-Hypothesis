"""Exact rational checks of the finite analytic budget, not of its arithmetic inputs."""
import sympy as s

a,t=s.symbols('a t', real=True)
F=s.Rational
pieces=[(F(1,8),F(1,6),F(1,6)+3*a),(F(1,6),F(1,3),F(1,3)+2*a),(F(1,3),F(1,2),s.Integer(1))]
cap=-F(133,34560)

def nonnegative_on_interval(expr,lo,hi):
    p=s.Poly(s.factor(expr).subs(a,lo+(hi-lo)*t).expand(),t)
    degree=p.degree()
    # Bernstein coefficients on [0,1] give an exact sign certificate.
    coeff=[p.nth(k) for k in range(degree+1)]
    bern=[sum(coeff[k]*s.binomial(j,k)/s.binomial(degree,k) for k in range(j+1)) for j in range(degree+1)]
    assert all(x>=0 for x in bern),(expr,lo,hi,bern)

for lo,hi,D in pieces:
    J1=7*D/8+(1-a)/2
    J2=D*(4-a)/4+(2-3*a)/4
    B=2-a+D/3
    H=J1/2-a+D/3
    nonnegative_on_interval(H,lo,hi)
    nonnegative_on_interval(-F(257,1152)-(B-F(5,2)*J1),lo,hi)
    nonnegative_on_interval(-F(95,48)-(5*a-2-F(5,2)*J1+D/3),lo,hi)
    nonnegative_on_interval(3*J1-F(175,64),lo,hi)
    nonnegative_on_interval(-F(19,8)-(6*a-2-3*J1),lo,hi)
    nonnegative_on_interval(6*B/5-2-F(1,5),lo,hi)
    nonnegative_on_interval(-F(6,5)-(-2+6*a-6*B/5),lo,hi)
    E0=-F(29,96)-F(25,48)*a+13*B/80
    for E in [E0]+[-F(29,96)-F(25,48)*a+J/3+7*B/240+(F(1,2)-D)/6 for J in (J1,J2)]:
        nonnegative_on_interval(-s.diff(E,a),lo,hi)
        assert E.subs(a,lo)<=cap,(E,lo,E.subs(a,lo))
assert (-F(29,96)-F(25,48)*a+( (F(1,6)+3*a)*(4-a)/4+(2-3*a)/4 )/3+7*(2-a+(F(1,6)+3*a)/3)/240+(F(1,2)-(F(1,6)+3*a))/6).subs(a,F(1,8))==cap
print('All exact rational interval and endpoint checks passed; maximum =',cap)
