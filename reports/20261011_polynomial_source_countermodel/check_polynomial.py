"""Exact algebra only. No zero approximation or claim of an RH proof."""
import json
from pathlib import Path
import sympy as s

u, v, z = s.symbols('u v z', real=True)
P = [2*u-3]
for _ in range(4):
    P.append(s.expand((s.Rational(5,2)-2*u)*P[-1]+2*u*s.diff(P[-1],u)))
R = s.expand(P[4]+200*P[2]+10001*P[0])
SOS = v**3*(32*(v-s.Rational(3,4))**2+714)+2364*v**2+s.Rational(117689,8)*v+s.Rational(326643,16)
p = 1+(z*z-100)**2
D = s.Rational(160817,16)
assert s.expand(R.subs(u,v+3)-SOS) == 0
assert p.subs(z,s.I/2) == D
assert s.expand(p.subs(z,s.sqrt(100+s.I))) == 0
assert s.expand(p.subs(z,s.sqrt(100-s.I))) == 0
assert D == s.Rational(1,16)+200*s.Rational(1,4)+10001
# sqrt(10001)>100 gives 0<delta^2=1/[2(sqrt(10001)+100)]<1/400.
assert 10001 > 10000
out = {
  'status':'passed',
  'scope':'exact polynomial identities and elementary rational inequalities only',
  'P2':str(P[2]), 'P4':str(P[4]), 'R':str(R),
  'R_at_u_v_plus_3_positive_decomposition':str(SOS),
  'normalization':str(D), 'fourier_multiplier':str(p),
  'added_roots':'z = +/- sqrt(100 +/- i)',
  'imaginary_part_exact':'1/sqrt(2*(sqrt(10001)+100))',
  'imaginary_part_bound':'0 < abs(Im z) < 1/20 < 1/2',
  'RH_conclusion':'No RH counterexample or unconditional RH theorem is claimed.'
}
path=Path(__file__).with_name('exact_checks.json')
with path.open('x',encoding='utf-8') as f: json.dump(out,f,ensure_ascii=False,indent=2)
print(json.dumps(out,ensure_ascii=False,indent=2))
