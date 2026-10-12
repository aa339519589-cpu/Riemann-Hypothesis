"""Interval hard-band quadrature and actual finite D component.
Sharp bands are integrated on their actual intervals, without periodizing them.
"""
from pathlib import Path
import json,math,time,numpy as np,mpmath as mp
mp.mp.dps=100;iv=mp.iv;iv.dps=80;I=iv.mpf;PI=iv.pi
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
PTH=Path(__file__).resolve().parent
par=json.loads((PTH/'hardband_parameters.json').read_text());bands=par['bands'];r=127;n=128
C0=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI);terms=[(iv.ln(2)/iv.sqrt(2),iv.ln(2)),(iv.ln(3)/iv.sqrt(3),iv.ln(3)),(iv.ln(2)/2,iv.ln(4))]
start=time.time();errors={}
def conv(z,key):
 v=float((lo(z)+hi(z))/2);er=hi(abs(z-I(v)));errors[key]=max(errors.get(key,mp.mpf(0)),er);return v
cs=[iv.cos(PI*j/n) for j in range(2*n)];weights=[]
for j in range(n+1):
 if j in [0,n]:w=I(1)/(n*n-1)
 else:w=I(2)/n*(1-sum((2*cs[(2*l*j)%(2*n)]/I(4*l*l-1) for l in range(1,n//2)),I(0))-cs[(n*j)%(2*n)]/(n*n-1))
 assert lo(w)>0;weights.append(w)
C=np.empty((2049,(n+1)*len(bands)));W=[];D=np.zeros((r,r));at=0
quadridge=I(0)
for band,rec in enumerate(bands):
 a=I(rec['left_over_8'])/8;b=I(rec['right_over_8'])/8;mid=(a+b)/2;half=(b-a)/2
 nu=I(0) if rec['left_over_8']==0 else mid
 powers=list(range(0,rec['Taylor_remainder_order'],2)) if rec['left_over_8']==0 else list(range(rec['Taylor_remainder_order']))
 moments=[I(0) for j in range(2*max(powers)+1)]
 for j in range(n+1):
  t=mid+half*cs[j];cc=C0+sum((2*al*iv.cos(sh*t) for al,sh in terms),I(0));ww=half*weights[j]*cc/PI
  W.append(conv(ww,'weighted_quadrature'))
  z=(t-nu)/2;zz=I(1)
  for k in range(len(moments)):moments[k]+=ww*zz;zz*=z
  # Binary divide-and-conquer cosine identities avoid exponentially unstable wrapping.
  ct=[I(1),iv.cos(t/256)]
  for jj in range(2,1025):
   if jj%2==0:ct.append(2*ct[jj//2]**2-1)
   else:ct.append(2*ct[jj//2]*ct[jj//2+1]-ct[1])
  col=band*(n+1)+j
  for jj,zv in enumerate(ct):C[1024+jj,col]=C[1024-jj,col]=conv(zv,'band_cosine')
 for k,pk in enumerate(powers):
  for l,pl in enumerate(powers):D[at+k,at+l]=conv(moments[pk+pl],'D_entry')
 # C0 is polynomial-exact. Expand the prime cosines to the remaining degree.
 order=n-2*max(powers)+1
 qe=2*(b-a)/PI*sum((2*al*(half*sh)**order/math.factorial(order) for al,sh in terms),I(0))
 quadridge+=len(powers)*qe;at+=len(powers)
 print('band',band,'complete',flush=True)
assert hi(quadridge)<mp.mpf(10)**-70
assert errors['band_cosine']<mp.mpf(2)**-52
assert errors['weighted_quadrature']<mp.mpf(2)**-48
assert errors['D_entry']<mp.mpf(2)**-45
Derror=r*I(2)**-45+quadridge;assert hi(Derror)<mp.mpf(1)/10**10
np.savez_compressed(PTH/'verified_hardband_quadrature.npz',cosine=C,weights=np.array(W),D=D)
report={'status':'Actual hard-band scalar quadrature and finite D components only','iv_digits':80,'quadrature_order':n,'max_conversion_errors':{k:mp.nstr(v,30) for k,v in errors.items()},'D_quadrature_operator_error_upper':mp.nstr(hi(quadridge),30),'D_total_operator_error_upper':mp.nstr(hi(Derror),30),'D_upper_ridge_rational':'1/10000000000','elapsed_seconds':time.time()-start};(PTH/'verified_hardband_quadrature.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
