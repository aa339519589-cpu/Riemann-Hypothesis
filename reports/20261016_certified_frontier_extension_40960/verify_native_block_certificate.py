"""Replay rigorous disjoint zero-ball/count certificates using official FLINT.
The batch API contract, not numerical root suggestions, supplies root existence.
Replay requires full returned count and strict containment in each recorded bracket.
The separate all-zero multiplicity count supplies completeness and simplicity.
This own wrapper uses opaque FLINT allocations, without C structure layouts.
"""
import argparse,ctypes as C,hashlib,json,pathlib,time
from fractions import Fraction
import flint
from flint import arb,acb,ctx


def native_roots(start,count,bits,threads):
    files=list((pathlib.Path(flint.__file__).resolve().parent.parent/'python_flint.libs').glob('libflint-*.so.*'))
    if len(files)!=1:raise RuntimeError('Expected exactly one official bundled Linux FLINT shared library')
    lib=C.CDLL(str(files[0]));L=C.c_long;P=C.c_void_p
    signatures=[('_fmpz_vec_init',[L],P),('_fmpz_vec_clear',[P,L],None),('fmpz_set_str',[P,C.c_char_p,C.c_int],C.c_int),('_arb_vec_init',[L],P),('_arb_vec_clear',[P,L],None),('_arb_vec_entry_ptr',[P,L],P),('flint_set_num_threads',[C.c_int],None),('acb_dirichlet_platt_hardy_z_zeros',[P,P,L,L],L),('arb_get_str',[P,L,L],P),('flint_free',[P],None)]
    for name,args,ret in signatures:
        f=getattr(lib,name);f.argtypes=args;f.restype=ret
    n=lib._fmpz_vec_init(1);v=lib._arb_vec_init(count)
    try:
        if lib.fmpz_set_str(n,str(start).encode('ascii'),10):raise RuntimeError('Invalid starting index')
        lib.flint_set_num_threads(threads)
        found=lib.acb_dirichlet_platt_hardy_z_zeros(v,n,count,bits)
        if found!=count:raise RuntimeError(f'Incomplete native result: {found}/{count}')
        strings=[]
        for i in range(found):
            ptr=lib.arb_get_str(lib._arb_vec_entry_ptr(v,i),60,0)
            try:strings.append(C.string_at(ptr).decode('ascii'))
            finally:lib.flint_free(ptr)
        return strings
    finally:
        lib._arb_vec_clear(v,count);lib._fmpz_vec_clear(n,1)


def ball(t):return arb(t.numerator)/t.denominator

def count_at(t):
    value=ball(t).zeta_nzeros()
    if not value.is_exact():raise RuntimeError('Indeterminate total zero count')
    n=value.unique_fmpz()
    if n is None:raise RuntimeError('Nonintegral total zero count')
    return int(n)

def sign_at(t):
    x=ball(t);G=acb(arb(1)/4,x/2).gamma()
    Z=G/abs(G)*acb(0,-x*arb.pi().log()/2).exp()*acb(arb(1)/2,x).zeta()
    if not Z.imag.contains(0):raise RuntimeError('Hardy reality enclosure failure')
    if Z.real>0:return 1
    if Z.real<0:return -1
    raise RuntimeError('Indeterminate endpoint sign')


def main():
    p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('--bits',type=int,default=256);p.add_argument('--threads',type=int,default=4);a=p.parse_args()
    if not __debug__:raise RuntimeError('Run without Python optimization: assertions are validation checks')
    if not(192<=a.bits<=1024 and 1<=a.threads<=4):raise ValueError('Outside bounded replay settings')
    path=pathlib.Path(a.certificate);d=json.loads(path.read_text())
    ctx.prec=a.bits;ctx.threads=1;start=time.perf_counter()
    lower=Fraction(*d['T0']);upper=Fraction(*d['T1'])
    assert 0<lower<upper and 1<=d['zero_count']<=65536
    assert a.bits>d['generation_bits'],'Replay precision must exceed generation precision'
    assert d['start_index']==d['counts'][0]+1
    assert len(d['brackets'])==d['zero_count']==d['counts'][1]-d['counts'][0]
    assert [count_at(lower),count_at(upper)]==d['counts']
    assert [sign_at(lower),sign_at(upper)]==d['outer_signs']
    previous=lower
    for i,entry in enumerate(d['brackets']):
        lo=Fraction(*entry['lower']);hi=Fraction(*entry['upper'])
        assert previous<lo<hi<upper,('strict bracket order',i,str(previous),str(lo),str(hi),str(upper))
        previous=hi
    # Fresh full-return calls; stored textual native enclosures are never trusted.
    for offset in range(0,d['zero_count'],4096):
        size=min(4096,d['zero_count']-offset)
        fresh=native_roots(d['start_index']+offset,size,a.bits,a.threads)
        assert len(fresh)==size
        for j,text in enumerate(fresh):
            r=arb(text);entry=d['brackets'][offset+j]
            assert r.is_finite()
            assert ball(Fraction(*entry['lower']))<r and r<ball(Fraction(*entry['upper'])),('strict containment',offset+j,text)
        print(json.dumps({'verified':offset+size,'total':d['zero_count'],'seconds':time.perf_counter()-start}),flush=True)
    print(json.dumps({'result':'PASS','zeros':d['zero_count'],'interval':[str(lower),str(upper)],'counts':d['counts'],'bits':a.bits,'threads':a.threads,'native_block_size':4096,'library':f'python-flint {flint.__version__} / FLINT {flint.__FLINT_VERSION__}','seconds':time.perf_counter()-start,'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'verifier_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}),flush=True)

if __name__=='__main__':main()
