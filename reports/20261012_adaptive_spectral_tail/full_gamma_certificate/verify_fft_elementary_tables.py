"""Outward elementary/Gamma scalar enclosures for a finite residual candidate.
Component verification only. The Bernoulli remainder is explicitly added.
"""
import json,math,time
from pathlib import Path
import numpy as np
import mpmath as mp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=90;iv=mp.iv;iv.dps=70;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
L=20;ngrid=5120;T=65;k=14;R=I(209)/100;PI=iv.pi
BER=[(1,6),(-1,30),(1,42),(-1,30),(5,66),(-691,2730),(7,6),(-3617,510)]
ERR=I(43867)/(798*18*I(64)**18)
C0=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI)
AST=4*PI**2*125/121;delta=20*AST/9*16*iv.exp(-4*PI);e=I(1)/8-delta
thtail=I(5)**4*iv.exp(-24*PI)/(1-(I(6)/5)**4*iv.exp(-11*PI))
maxerrors={};start=time.time()
def conv(z,name):
 v=float((lo(z)+hi(z))/2);er=hi(abs(z-I(v)));maxerrors[name]=max(maxerrors.get(name,mp.mpf(0)),er);return v

def msq(x):
 x=abs(x);u=iv.exp(2*x)
 zz=sum((I(n)**4*(1-3/(2*PI*n*n*u))*iv.exp(-PI*(n*n-1)*u) for n in range(1,5)),I(0))+I([0,hi(thtail)])
 return 4*PI**2*iv.exp(I(9)*x/2-PI*u)*zz/(iv.exp(x/2)+iv.exp(-x/2))

def rho(t):
 if hi(abs(t))<=T:return I(1)
 if lo(abs(t))>=2*T:return I(0)
 z=k*(abs(t)/T-1);fl=int(mp.floor(lo(z)));assert fl==int(mp.floor(hi(z)))
 return 1-sum((I((-1)**j*math.comb(k,j))*(z-j)**k for j in range(fl+1)),I(0))/math.factorial(k)

def bgamma(t):
 if hi(abs(t))==0:return I(0)
 z=iv.mpc(I(257)/4,t/2)
 v=iv.log(z)-1/(2*z)
 for j,(num,den) in enumerate(BER,1):v-=I(num)/den/(2*j*z**(2*j))
 for j in range(64):v-=1/iv.mpc(I(j)+I(1)/4,t/2)
 return v.real+iv.euler+PI/2+3*iv.ln(2)+I([-hi(ERR),hi(ERR)])

cosroot=np.array([conv(iv.cos(2*PI*j/ngrid),'cosroot') for j in range(ngrid)])
mvals=np.array([conv(iv.sqrt(msq(I(j)/128)),'m') for j in range(-512,513)])
gauss=np.array([conv(iv.exp(-(I(j)/128)**2),'gaussian') for j in range(-512,513)])
dvals=[];bvals=[];rhovals=[]
for j in range(ngrid//2+1):
 t=PI*j/L;ro=rho(t);b=bgamma(t)
 cc=C0+2*iv.ln(2)/iv.sqrt(2)*iv.cos(t*iv.ln(2))+2*iv.ln(3)/iv.sqrt(3)*iv.cos(t*iv.ln(3))
 d=b-(1-ro**2)*cc
 dvals.append(conv(d,'d'));bvals.append(conv(b,'b'));rhovals.append(conv(ro,'rho'))
 if j%500==0:print('frequency',j,flush=True)
assert maxerrors['cosroot']<mp.mpf(2)**-52
assert maxerrors['m']<mp.mpf(2)**-50
assert maxerrors['gaussian']<mp.mpf(2)**-52
assert maxerrors['d']<mp.mpf(2)**-44
assert maxerrors['b']<mp.mpf(2)**-44
assert maxerrors['rho']<mp.mpf(2)**-52
np.savez_compressed(ROOT/'verified_elementary_tables.npz',cosroot=cosroot,m=mvals,gaussian=gauss,d=np.array(dvals),b=np.array(bvals),rho=np.array(rhovals),e=conv(e,'e'))
rep={'status':'Scalar component enclosures only; no full residual/inertia certificate','max_conversion_errors':{key:mp.nstr(v,30) for key,v in maxerrors.items()},'Gamma_Binet_remainder_upper':mp.nstr(hi(ERR),30),'iv_digits':70,'elapsed_seconds':time.time()-start}
(ROOT/'verified_elementary_tables.json').write_text(json.dumps(rep,indent=2));print(json.dumps(rep,indent=2))
