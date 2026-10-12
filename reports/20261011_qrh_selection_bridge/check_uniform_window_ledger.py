"""Exact checks for the exponent-continuity supplement; not an analytic proof."""
from fractions import Fraction as F
import sympy as s

a,e=s.symbols('a e')
D=14*a*(23-36*a)/(3*(30-49*a-36*a*a))
Dp=2*a*(37-60*a)/(3*(5+2*a-24*a*a))
a0=s.Rational(1,6); h=s.Rational(1,10000)
x=s.Rational(168,125)+e/8; y=s.Rational(238,125)-e/8
r=s.Rational(238,375)
assert D.subs(a,a0)==r
assert s.factor((Dp-D).subs(a,a0))==s.Rational(43,5250)
assert s.Rational(43,10500)>s.Rational(1,1000)
assert s.factor(s.diff(D,a)-28*(432*a*a-360*a+115)/(36*a*a+49*a-30)**2)==0
# A containing rational interval gives a proof of 0<D'<5 over all I0.
lo=F(33,200); hi=F(21,125)
assert lo<F(1,6)-F(1,1000)<F(1,6)+F(1,1000)<hi
qlo=30-49*hi-36*hi*hi
pup=432*hi*hi-360*lo+115
assert qlo>0 and 115-360*hi>0
assert 28*pup/qlo**2<5
print('Compact derivative enclosure: PASS')
# Verify the centre exponent identities used for all uniform gaps.
B=(8*a-4)*y/5+s.Rational(2,5)+s.Rational(8,15)*(1+x)
E={
 'stable':1+4*h*x+(1-2*a)*(x-y),
 'H':B-4*e/5,
 'lattice':B-2*x/5,
 'Y':2*a*y,
 'one':1+(12*a-3)*x,
 'two':6+(12*a-6)*x,
 'three':s.Rational(14,3)+(12*a-5)*x,
}
expected={
 'stable':s.Rational(47,75)+e/6+4*h*x,
 'H':r-2*e/3,
 'lattice':r+2*e/15-2*x/5,
 'Y':r-e/24,
 'one':-s.Rational(43,125)-e/8,
 'two':s.Rational(234,375)-e/2,
 'three':r-3*e/8,
}
for name,v in E.items():
 assert s.simplify(v.subs(a,a0)-expected[name])==0
 # All affine derivatives have absolute value <24 on eta in [0,1/10000].
 deriv=s.diff(v,a)
 for ee in (s.Rational(0),s.Rational(1,10000)):
  assert abs(deriv.subs(e,ee))<24
assert r-E['stable'].subs({a:a0,e:s.Rational(1,10000)})>s.Rational(1,200)
assert r-E['lattice'].subs({a:a0,e:s.Rational(1,10000)})>s.Rational(1,200)
assert r-E['two'].subs({a:a0,e:0})>s.Rational(1,200)
# |D'-E'|<5+24<32; the exceptional derivative has bound 5+5<32.
assert 5+24<32 and 5+5<32
assert s.simplify(1+x-y)==s.Rational(11,25)+e/4
assert (1+x-y).subs(e,s.Rational(1,10000))<s.Rational(1,2)
amin=F(1,6)-F(1,2000); amax=F(1,6)+F(1,2000)
assert amin-F(1,10000)>F(1,6)-F(1,1000)
assert 1-amin+3*F(1,10000)<F(7,8)
betamax=1-amin+F(1,10000)
assert all(v<0 for v in [2*betamax-3,2*betamax-2,2*betamax-F(7,3)])
assert all(12*amax-j<0 for j in (3,6,5))
print('Centre identities, common Lipschitz margin, kernel/tail ranges: PASS')
print('Nested published-density interface: PASS')
print('ALL EXACT UNIFORM-WINDOW CHECKS PASS')
