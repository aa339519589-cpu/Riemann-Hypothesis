"""Outward scalar component for new epsilon=1/1024 hard-band residual.
No complete residual/Gram/inertia assertion is made by this component.
"""
from pathlib import Path
import math,json,time,numpy as np,mpmath as mp
mp.mp.dps=100;iv=mp.iv;iv.dps=80;I=iv.mpf;PI=iv.pi
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
PTH=Path(__file__).resolve().parent
par=json.loads((PTH/'hardband_parameters.json').read_text());bands=par['bands']
AST=4*PI**2*125/121;C0=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI);e=I(1)/1024-20*AST/9*25*iv.exp(-5*PI)
terms=[(iv.ln(2)/iv.sqrt(2),iv.ln(2)),(iv.ln(3)/iv.sqrt(3),iv.ln(3)),(iv.ln(2)/2,iv.ln(4))]
BER=[(1,6),(-1,30),(1,42),(-1,30),(5,66),(-691,2730),(7,6),(-3617,510)];ERR=I(43867)/(798*18*I(64)**18)
thtail=I(5)**4*iv.exp(-24*PI)/(1-(I(6)/5)**4*iv.exp(-11*PI));errors={};start=time.time()
def conv(z,key):
 v=float((lo(z)+hi(z))/2);er=hi(abs(z-I(v)));errors[key]=max(errors.get(key,mp.mpf(0)),er);return v

def msq(x):
 x=abs(x);u=iv.exp(2*x);s=sum((I(n)**4*(1-3/(2*PI*n*n*u))*iv.exp(-PI*(n*n-1)*u) for n in range(1,5)),I(0))+I([0,hi(thtail)])
 return 4*PI**2*iv.exp(I(9)*x/2-PI*u)*s/(iv.exp(x/2)+iv.exp(-x/2))
def bgamma(t):
 if hi(abs(t))==0:return I(0)
 z=iv.mpc(I(257)/4,t/2);v=iv.log(z)-1/(2*z)
 for j,(num,den) in enumerate(BER,1):v-=I(num)/den/(2*j*z**(2*j))
 for j in range(64):v-=1/iv.mpc(I(j)+I(1)/4,t/2)
 return v.real+iv.euler+PI/2+3*iv.ln(2)+I([-hi(ERR),hi(ERR)])
cosroot=np.array([conv(iv.cos(2*PI*j/20480),'cosroot') for j in range(20480)])
mvals=np.array([conv(iv.sqrt(msq(I(j)/256)),'m') for j in range(-1024,1025)])
gauss=np.array([conv(iv.exp(-(I(j)/256)**2),'gaussian') for j in range(-1024,1025)])
bc=[]
for j in range(5121):
 t=PI*j/40;cc=C0+sum((2*a*iv.cos(d*t) for a,d in terms),I(0));bc.append(conv(bgamma(t)-cc,'bc'))
 if j%1000==0:print('complete Gamma',j,flush=True)
phi=np.empty((2049,127));at=0
for rec in bands:
 a=I(rec['left_over_8'])/8;b=I(rec['right_over_8'])/8;n=rec['Taylor_remainder_order'];nu=I(0) if rec['left_over_8']==0 else (a+b)/2
 powers=list(range(0,n,2)) if rec['left_over_8']==0 else list(range(n))
 for jj in range(1025):
  x=I(jj)/256;cs=iv.cos(nu*x);sn=iv.sin(nu*x)
  for kk,k in enumerate(powers):
   trig=[cs,-sn,-cs,sn][k%4];val=conv((2*x)**k/math.factorial(k)*trig,'phi')
   phi[1024+jj,at+kk]=phi[1024-jj,at+kk]=val
 at+=len(powers)
assert errors['cosroot']<mp.mpf(2)**-52 and errors['gaussian']<mp.mpf(2)**-52
assert errors['m']<mp.mpf(2)**-50 and errors['bc']<mp.mpf(2)**-44 and errors['phi']<mp.mpf(2)**-42
np.savez_compressed(PTH/'verified_hardband_elementary_scaled.npz',cosroot=cosroot,m=mvals,gaussian=gauss,bc=np.array(bc),phi=phi,e=conv(e,'e'))
r={'status':'Component scalar enclosures only','max_conversion_errors':{k:mp.nstr(v,30) for k,v in errors.items()},'Gamma_remainder_upper':mp.nstr(hi(ERR),30),'iv_digits':80,'elapsed_seconds':time.time()-start};(PTH/'verified_hardband_elementary_scaled.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
