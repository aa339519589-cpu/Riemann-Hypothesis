"""Directed-interval scalar screen. No RH claim. mpmath.iv, 40 decimal digits."""
from mpmath import iv
import json
from fractions import Fraction
import mpmath
iv.dps=40
I=iv.mpf
pi=iv.pi

def exact_upper(v):
    sign,mantissa,exponent,_=v._mpi_[1]
    return Fraction((-1 if sign else 1)*mantissa)*(Fraction(2)**exponent)

def exact_lower(v):
    sign,mantissa,exponent,_=v._mpi_[0]
    return Fraction((-1 if sign else 1)*mantissa)*(Fraction(2)**exponent)
P=[2,3,4,5,7,8,9,11,13,16]
prime_base={2:2,3:3,4:2,5:5,7:7,8:2,9:3,11:11,13:13,16:2}
logs={n:iv.ln(I(n)) for n in P}
alphas={n:iv.ln(I(prime_base[n]))/iv.sqrt(I(n)) for n in P}

def bounds(y):
    """Complete Phi and psi=-Phi' on y>=0; n<=4 plus proved positive tails."""
    e=iv.exp(2*y)
    E=iv.exp(y/2)
    ph=I(0); ps=I(0)
    for n in range(1,5):
        u=pi*n*n*e
        v=E*iv.exp(-u)
        ph+=(4*u*u-6*u)*v
        ps+=(8*u*u*u-30*u*u+15*u)*v
    # n>=5: each term decreases in y>=0, and the n-ratio at 5 is <1/2.
    # pi in(3,4) gives total Phi tail <80000 exp(-75)<1e-26,
    # psi tail <16000000 exp(-75)<1e-24.
    return ph+I([0,'1e-26']), ps+I([0,'1e-24'])

def row_lower(x):
    out=I(0)
    for n in P:
        if bool(logs[n].a > x.b):
            _, ps=bounds(logs[n]-x)
            if bool(ps.a>0): out+=alphas[n].a*ps.a
    return out

stats={'intervals':0,'splits':0,'max_depth':0,'ratio_upper':Fraction(0),'mu2_upper':Fraction(0)}

def central(a,b,depth=0):
    x=I([a,b]); ph,ps=bounds(x); L=row_lower(x)
    if bool(ph.a>0) and bool(L.a>0):
        rat=(iv.exp(x/2)+iv.exp(-x/2))*ps/(ph*L)
        mu=ps/L
        if bool(rat.b < 128) and bool(mu.b < 16):
            stats['intervals']+=1;stats['max_depth']=max(stats['max_depth'],depth)
            stats['ratio_upper']=max(stats['ratio_upper'],exact_upper(rat))
            stats['mu2_upper']=max(stats['mu2_upper'],exact_upper(mu))
            return
    if depth>=22: raise RuntimeError(('uncertified',str(a),str(b),str(L)))
    stats['splits']+=1
    mid=(a+b)/2
    central(a,mid,depth+1);central(mid,b,depth+1)

# Rational endpoints represented by directed intervals; use exact dyadic grid.
# [0,1.4] is covered by [0, 45/32] (slightly larger), with actual max ratio<120.
central(I(0),I(45)/32)

power_stats={'intervals':0,'splits':0,'lower':Fraction(1)}
def power_lower(a,b,depth=0):
    x=I([a,b]);_,ps=bounds(x)
    c=iv.ln(I(2))*iv.exp(-x/2)*ps
    if bool(c.a>I(1)/64):
        power_stats['intervals']+=1
        power_stats['lower']=min(power_stats['lower'],exact_lower(c))
        return
    if depth>=22:raise RuntimeError(('power_uncertified',str(a),str(b),str(c)))
    power_stats['splits']+=1;mid=(a+b)/2
    power_lower(a,mid,depth+1);power_lower(mid,b,depth+1)
# Cover [1/128,1/128+log2] by a rational endpoint 90/128=.703125.
assert bool(iv.ln(I(2)).b<I(89)/128)
power_lower(I(1)/128,I(90)/128)

R=I(7)/5
M=128*iv.exp(I(7)*R/2-pi*iv.exp(2*R)/2)
physical_tail_scalar=I(2)**40*iv.exp(12*R-pi*iv.exp(2*R))
assert bool(M.b<I(1)/12)
assert bool(physical_tail_scalar.b<I(1)/1000)
# Auxiliary elementary whole-theta and tail inequalities used in the prose.
assert bool(80000*iv.exp(-75)<I('1e-26'))
assert bool(16000000*iv.exp(-75)<I('1e-24'))
assert bool(8*(I(22)/7)**3*(I(65)/64)<256)
assert bool(64*iv.exp(-9)/(1-(I(3)/2)**6*iv.exp(-15))<I(1)/64)
assert bool(294912*iv.exp(-24)<1)
print(json.dumps({'precision_decimal_digits':iv.dps,'mpmath_version':mpmath.__version__,'central':stats,'power_lower':power_stats,'mu_envelope_at_7_5_upper_fraction':str(exact_upper(M)),'physical_tail_scalar_upper_fraction':str(exact_upper(physical_tail_scalar)),'status':'all directed inequalities passed'},indent=2,default=str))
