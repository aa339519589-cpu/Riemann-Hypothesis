"""Exact objective/capacity checks and outward energy-floor check."""
import json,pathlib
from fractions import Fraction
from flint import arb,ctx
ctx.prec=192
D=pathlib.Path(__file__).resolve().parent;d=json.loads((D/'certified_window_data.json').read_text())
P=d['pressure'];W=d['weights'];pairs=d['pairs'];den=d['weight_denominator']
assert len(P)==8 and len(W)==len(pairs)==36 and den==10**8
assert pairs==[[i,j] for i in range(9) for j in range(i+1,9)]
assert all(x>=0 for x in W) and min(P)>0 and P==P[::-1]
wd=dict(zip(map(tuple,pairs),W))
assert all(wd[(i,j)]==wd[(8-j,8-i)] for i,j in wd)
assert all(sum(w for (i,j),w in wd.items() if j-i==s)<=2*den for s in range(1,9))
assert sum(P)==437542 and d['candidate_reward']==[867000,10**8]
cc=[arb(c)/d['coefficient_denominator'] for c in d['cosine_coefficients']]
pi=arb.pi();r=arb(2).sqrt();m=r*(1/r).sin()
H=arb(3)/2-(1/r).cos()/m-sum(c*c*(arb(1)/2-1/(4*pi*pi*j*j)) for j,c in enumerate(cc,1))/(m*m)
lo=Fraction(67212547684242257756837921426708,10**32)
assert H>arb(lo.numerator)/lo.denominator
c=Fraction(867000,10**8);B=Fraction(sum(P),den);p=(lo-B)/(1-c)
assert p==Fraction(16693751421060564439209480356677,24783250000000000000000000000000)
old=Fraction(34191001116882886388531117129201664,50760020691785094633026544189453125)
assert p>old
print('CONSTANTS_PASS',str(p),'positive_exact_gap',str(p-old))
