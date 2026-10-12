"""Directed scalar tables for the 373-dimensional actual finite Gram experiment.
This is a component check, NOT a completed continuous residual or inertia proof.
"""
import json, math, time, sys
from pathlib import Path
import numpy as np
import mpmath as mp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=400;iv=mp.iv;iv.dps=360;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
R=I(209)/100;T=65;win=14;rank=373;L=20;ngrid=5120
K=827;maxfreq=int(sys.argv[1]) if len(sys.argv)>1 else K
assert hi(iv.pi*K/L)<2*T and lo(iv.pi*(K+1)/L)>2*T
start=time.time();out=np.zeros((maxfreq+1,rank));maxerr=mp.mpf(0);maxwidth=mp.mpf(0)
NN=2*rank+20
factor_cache={n:(I(2)**n*I(math.factorial(n))/I(math.factorial(2*n+1))) for n in [NN,NN+1]}

def anchor(n,x):
 term=I(1);su=I(1);j=0
 while True:
  nex=term*(-x*x)/(2*(j+1)*(2*n+2*j+3))
  if j>50 and hi(abs(nex))<mp.mpf(2)**-1100:
   su+=I([-hi(abs(nex)),hi(abs(nex))]);break
  su+=nex;term=nex;j+=1
  if j>2000:raise RuntimeError('anchor did not converge')
 return x**n*factor_cache[n]*su

def rho(t):
 if hi(abs(t))<=T:return I(1)
 if lo(abs(t))>=2*T:return I(0)
 z=win*(abs(t)/T-1)
 flo=int(mp.floor(lo(z)))
 # No integer boundary is hit in the finite nonzero-frequency table.
 assert flo==int(mp.floor(hi(z)))
 cdf=sum((I((-1)**j*math.comb(win,j))*(z-j)**win for j in range(flo+1)),I(0))/math.factorial(win)
 return 1-cdf

for q in range(maxfreq+1):
 t=iv.pi*q/L;x=R*t;ro=rho(t)
 if q==0: vals=[I(1)]+[I(0)]*(rank-1)
 else:
  current=anchor(NN,x);following=anchor(NN+1,x);vals=[None]*rank
  for nn in range(NN,0,-1):
   previous=I(2*nn+1)/x*current-following
   if (nn-1)%2==0 and nn-1<2*rank:vals[(nn-1)//2]=previous
   following,current=current,previous
 for j,v in enumerate(vals):
  value=ro*iv.sqrt(2*R*(4*j+1))*((-1)**j)*v
  center=float((lo(value)+hi(value))/2)
  er=hi(abs(value-I(center)));wi=hi(value)-lo(value)
  maxerr=max(maxerr,er);maxwidth=max(maxwidth,wi)
  out[q,j]=center
 if q%100==0:print(f'Bessel row {q}/{maxfreq}',flush=True)
assert maxerr<mp.mpf(2)**-44
np.save(ROOT/f'verified_rho_ehat_rows_{maxfreq}.npy',out)
report={'status':'Verified scalar component only; no continuous residual or spectral certificate','rows':maxfreq+1,'columns':rank,'iv_decimal_digits':360,'max_scalar_conversion_error':mp.nstr(maxerr,30),'max_interval_width':mp.nstr(maxwidth,30),'uniform_scalar_error_rational':'1/17592186044416','elapsed_seconds':time.time()-start}
(ROOT/f'verified_rho_ehat_rows_{maxfreq}.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
