#!/usr/bin/env python3
"""Directed interval compact checks; analytic all-tail reductions accompany this file."""
import json, hashlib, os
from fractions import Fraction
from pathlib import Path
import mpmath as mp
iv=mp.iv
iv.dps=int(os.environ.get("REF_DPS", "45"))
N=4096
pi=iv.pi
E=iv.exp
log=iv.ln
sqrt=iv.sqrt
sinh=lambda x:(E(x)-E(-x))/2
zero=iv.mpf(0)
d=log(2)
a=2*d/sqrt(2)

def rat(n,q=1): return iv.mpf(n)/q

def upper(v):
    s,m,e,b=v._mpi_[1]
    return Fraction((-1 if s else 1)*m)*(Fraction(2)**e)

def lower(v):
    s,m,e,b=v._mpi_[0]
    return Fraction((-1 if s else 1)*m)*(Fraction(2)**e)

def assert_lt(v,c,name):
    assert upper(v)<Fraction(c), (name, str(v), c)
    return {'name':name,'upper_fraction':str(upper(v)),'bound':str(c)}

# n >=5: every theta derivative summand is positive; its absolute upper
# bound 572*n^6*e^(13x/2-3*n^2*e^(2x)) decreases for x>=0.
theta_tail=2*572*5**6*E(-75)
assert_lt(rat(6,5)**6*E(-33),Fraction(1,2),'theta-tail successive ratio')

def psi(x):
    ans=zero
    for n in range(1,5):
        y=pi*n*n*E(2*x)
        ans+=(8*y**3-30*y**2+15*y)*E(x/2-y)
    return ans+iv.mpf([0,theta_tail.b])

def psi_pos(x):
    if upper(x)<=0: return zero
    if lower(x)<0: x=iv.mpf([0,x.b])
    return psi(x)

def power_base(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return p if m==1 else None
    return None
labels=[(n,log(power_base(n))/sqrt(n),log(n)) for n in range(2,65) if power_base(n)]
prime_tail=2*1000*65**7*E(-rat(3,55)*65**2)
checks=[]
assert Fraction(192000,997)<193
checks.append({'name':'centered reference constant','upper_fraction':'192000/997','bound':'193'})
checks.append(assert_lt(a,1,"twice prime-two alpha below one"))
checks.append(assert_lt(E(4),55,"e fourth power below 55"))
checks.append(assert_lt(1/(log(65)-2),1,"log65 minus 2 exceeds one"))
checks.append(assert_lt(1000*E(rat(13,2)-3*E(2)),3,"psi envelope above one"))
checks.append(assert_lt(64*E(-9),Fraction(1,8),"global theta normalized n2 term"))
checks.append(assert_lt(rat(3,2)**6*E(-15),Fraction(1,2),"global theta normalized successive ratio"))
checks.append(assert_lt(prime_tail,Fraction(1,2**200),'complete n>=65 row tail on 0<=x<=2'))
checks.append(assert_lt(rat(66,65)**7*E(-rat(3,55)*131),Fraction(1,2),'prime-tail successive ratio'))
# Tail envelope psi(x)<=1000 exp(13x/2-3exp(2x)), x>=1.
checks.append(assert_lt(2*1000*E(7-3*E(2)),Fraction(1,1000),'weighted integer psi-envelope tail'))
checks.append(assert_lt(E(7-3*(E(2)-1)*E(2)),Fraction(1,2),'weighted shell-envelope successive ratio'))
checks.append(assert_lt(3*E(1)*(3+rat(1,1000)),25,'global reflected row prefactor'))
checks.append(assert_lt(50/(1-E(-2)),64,'reflected diagonal ratio x>=2'))
checks.append(assert_lt(1000*2**13*E(-48),Fraction(1,10**12),'psi envelope above 2 log2'))
# psi<=3, sinh(d/2)=1/(2 sqrt2)>1/3 and sinh(d)=3/4 give beta(x)^2 <12*10^-12.
checks.append(assert_lt(12*rat(1,10**12),Fraction(1,10**6),'beta squared above log2'))

maxpsi=Fraction(0); maxbeta=Fraction(0); maxrow=Fraction(0)
for k in range(N):
    x=iv.mpf([rat(k,N).a,rat(k+1,N).b])
    val=psi(x)
    maxpsi=max(maxpsi,upper(val))
    assert upper(val)<3, ('psi',k,str(val))
for k in range(N):
    t=d*iv.mpf([rat(k,N).a,rat(k+1,N).b])
    p=psi(t); p1=psi(t+d)
    den=(sinh(t/2)+a*p1)*(sinh((t+d)/2)+a*p)
    assert lower(den)>0, ('beta denominator',k,str(den))
    val=a*a*p*p1/den
    maxbeta=max(maxbeta,upper(val))
    assert upper(val)<Fraction(4,9),('beta0',k,str(val))
for k in range(N):
    x=iv.mpf([rat(2*k,N).a,rat(2*(k+1),N).b])
    den=sinh(x/2)+a*psi(x+d)+a*psi_pos(x-d)
    assert lower(den)>0,('row denominator',k,str(den))
    L=iv.mpf([0,prime_tail.b])
    for n,alpha,ln in labels:
        L+=alpha*psi_pos(ln-x)
    val=L/den
    maxrow=max(maxrow,upper(val))
    assert upper(val)<64,('row',k,str(val))

out={'precision_decimal_digits':iv.dps,'compact_cells_each':N,'theta_labels':4,'prime_labels_through':64,
 'psi_compact_upper_fraction':str(maxpsi),'beta0_squared_upper_fraction':str(maxbeta),
 'reflected_row_compact_upper_fraction':str(maxrow),
 'readable_upper_summaries':{'psi':float(maxpsi),'beta0_squared':float(maxbeta),'row':float(maxrow)},
 'checks':checks,
 'conclusions':{'psi_global_upper':3,'beta0_upper':'2/3','beta_k_ge1_upper':'1/1000',
 'jacobi_rho_upper':'2003/3000','sup_psiL_over_D_upper':64,'centered_C_ref_upper':193}}
p=Path(__file__).with_name('green_reference_result_'+str(iv.dps)+'.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
