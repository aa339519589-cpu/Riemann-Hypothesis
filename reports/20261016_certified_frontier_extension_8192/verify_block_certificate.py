"""Read-only rigorous replay: shared-endpoint sign chain plus total multiplicity counts.
Uses Gamma/abs(Gamma), independently of the generator's log-Gamma phase.
"""
import argparse,json,pathlib,time,concurrent.futures
from fractions import Fraction
from flint import arb,acb,ctx

def sign_job(task):
    row,bits=task;ctx.prec=bits;ctx.threads=1;t=arb(row['numerator'])/row['denominator']
    G=acb(arb(1)/4,t/2).gamma()
    Z=(G/abs(G))*acb(0,-t*arb.pi().log()/2).exp()*acb(arb(1)/2,t).zeta()
    assert Z.imag.contains(0)
    s=1 if Z.real>0 else -1 if Z.real<0 else 0
    assert s and s==row['sign'];return True

def main():
    p=argparse.ArgumentParser();p.add_argument('certificate',nargs='?',default=str(pathlib.Path(__file__).with_name('frontier8192_certificate.json')));p.add_argument('--bits',type=int,default=128);p.add_argument('--workers',type=int,default=4);args=p.parse_args()
    d=json.loads(pathlib.Path(args.certificate).read_text());T0=Fraction(*d['T0']);T1=Fraction(*d['T1']);rows=d['sign_samples'];tt=[Fraction(x['numerator'],x['denominator']) for x in rows]
    assert tt[0]==T0 and tt[-1]==T1 and all(a<b for a,b in zip(tt,tt[1:]));assert len(rows)==d['new_zero_count']+1
    assert all(x['sign'] in [-1,1] for x in rows);assert all(a['sign']*b['sign']==-1 for a,b in zip(rows,rows[1:]))
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        for i,ok in enumerate(pool.map(sign_job,((r,args.bits) for r in rows),chunksize=16)):
            assert ok
            if i and i%2048==0:print(json.dumps({'verified_signs':i+1,'seconds':time.perf_counter()-start}),flush=True)
    ctx.prec=args.bits;ctx.threads=1;counts=[]
    for t in [T0,T1]:
        n=(arb(t.numerator)/t.denominator).zeta_nzeros();assert n.is_exact();counts.append(int(n.unique_fmpz()))
    assert counts==d['counts'];assert counts[1]-counts[0]==d['new_zero_count']
    print(json.dumps({'result':'PASS','zeros':d['new_zero_count'],'counts':counts,'interval':[str(T0),str(T1)],'bits':args.bits,'workers':args.workers,'phase':'Gamma/absGamma','seconds':time.perf_counter()-start}),flush=True)
if __name__=='__main__':main()
