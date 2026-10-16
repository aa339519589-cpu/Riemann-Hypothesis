"""Read-only independent replay of a rational sign-change/count certificate."""
import argparse,json,time,pathlib
from fractions import Fraction
from flint import arb,acb,ctx
p=argparse.ArgumentParser();p.add_argument('certificate',nargs='?',default=str(pathlib.Path(__file__).with_name('frontier32_certificate.json')));p.add_argument('--bits',type=int,default=128);args=p.parse_args()
d=json.loads(pathlib.Path(args.certificate).read_text());ctx.prec=args.bits;ctx.threads=1
T0=Fraction(*d['T0']);T1=Fraction(*d['T1']);assert T0<T1
rows=d['brackets'];intervals=[tuple(Fraction(v['numerator'],v['denominator']) for v in row) for row in rows]
assert all(T0<a<b<T1 for a,b in intervals);assert all(intervals[i][1]<intervals[i+1][0] for i in range(len(intervals)-1))
pi=arb.pi();lp=pi.log()
def sign(t):
    t=arb(t.numerator)/t.denominator
    th=acb(arb(1)/4,t/2).lgamma().imag-t*lp/2
    Z=acb(0,th).exp()*acb(arb(1)/2,t).zeta()
    assert Z.imag.contains(0)
    assert Z.real>0 or Z.real<0
    return 1 if Z.real>0 else -1
start=time.perf_counter()
for i,(a,b) in enumerate(intervals):
    sa,sb=sign(a),sign(b);assert sa*sb==-1
    assert [sa,sb]==[v['sign'] for v in rows[i]]
assert sign(T0) and sign(T1)
counts=[]
for t in [T0,T1]:
    count=(arb(t.numerator)/t.denominator).zeta_nzeros()
    assert count.is_exact();counts.append(int(count.unique_fmpz()))
assert counts==d['counts'];assert counts[1]-counts[0]==len(rows)==d['new_zero_count']
print(json.dumps({'result':'PASS','zeros':len(rows),'counts':counts,'bits':ctx.prec,'seconds':time.perf_counter()-start,'interval':[str(T0),str(T1)]}))
