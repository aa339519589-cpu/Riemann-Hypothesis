'''Exact rational positivity certificates for a new degree-six BTY packet.
No zero-free-region assertion is made here.'''
import sympy as s,json
from pathlib import Path
x=s.Symbol('x');Y=s.Symbol('Y')
old=[s.Rational(n,859) for n in [859,-851,780,-525,171,28,-29]]
raw=list(map(s.Rational,['1','-.9993544650035157','.9865335396552144','-.9045345971859327','.6665553909357624','-.31899129155848827','.06984571251379879']))
# A 1% exact convex blend provides strict positivity before rational rounding.
D=10**12
ks=[s.Rational(round((99*u+v)*D/100),D) for u,v in zip(raw,old)]
assert ks[0]==1
p=sum(ks[j]*x**j for j in range(7))
assert s.count_roots(p,0,1)==0 and p.subs(x,0)>0 and p.subs(x,1)>0
assert s.count_roots(s.diff(p,x),0,1)==0 and s.diff(p,x).subs(x,0)<0 and s.diff(p,x).subs(x,1)<0
bs=[ks[0]]+[ks[j]+ks[j-1] for j in range(1,7)]+[ks[6]]
eps=s.Rational(1,2000)
R=sum((bs[j]*j-abs(bs[j])*eps/j)/(j*j+Y) for j in range(1,8))
num,den=s.fraction(s.cancel(R));N=s.Poly(num,Y);DD=s.Poly(den,Y)
assert all(v>0 for v in DD.all_coeffs())
assert s.count_roots(N,0,s.oo)==0 and N.eval(0)>0 and N.LC()>0
pairleading=sum(ks)+2*sum(j*ks[j] for j in range(7))
assert pairleading>0
result={'theta':'1.1338','kappa':[str(k) for k in ks],'sum':str(sum(ks)),'l1':str(sum(abs(k) for k in ks)),'pair_leading':str(pairleading),'epsilon':'1/2000','B_numerator_coefficients':[str(a) for a in N.all_coeffs()],'B_denominator_coefficients':[str(a) for a in DD.all_coeffs()],'status':'EXACT_STURM_PASS'}
path=Path(__file__).with_name('rescaled_packet.json');path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
