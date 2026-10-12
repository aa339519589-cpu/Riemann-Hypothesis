"""Scalar interval validation for the actual signed polynomial-overlap matrix.
Clenshaw-Curtis integrates the polynomial products exactly. Matrix roundoff and
scalar conversion radii are bounded explicitly; no resolvent is computed here.
"""
import math,json,time
from pathlib import Path
import numpy as np
import mpmath as mp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=530;iv=mp.iv;iv.dps=500;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
r=373;n=2048;R=I(209)/100
assert n>=4*r-4
st=time.time()
# Point interval constants: the very high precision prevents recurrence wrapping.
cosiv=[iv.cos(iv.pi*j/n) for j in range(2*n)]
cosc=np.array([float((lo(z)+hi(z))/2) for z in cosiv])
coserr=max(hi(abs(z-I(float(c)))) for z,c in zip(cosiv,cosc))
assert coserr<I(2)**-52
weights=np.empty(n+1);weights[0]=weights[n]=1/(n*n-1)
kk=np.arange(1,n//2);coef=2/(4*kk.astype(float)**2-1)
for j in range(1,n):weights[j]=2/n*(1-np.dot(coef,cosc[(2*kk*j)%(2*n)])-cosc[(n*j)%(2*n)]/(n*n-1))
# IEEE binary64 dot products: at most 4n operations in each weighted sum.
u=2.**-53; gamma=4*n*u/(1-4*n*u)
# Includes coefficient divisions, cos conversion, final scaling and addition.
werr=2/n*(4*gamma+4*float(coserr))+8*u/n
assert 2/I(n)*(4*(I(4*n)*I(2)**-53/(1-I(4*n)*I(2)**-53))+4*I(coserr))+8*I(2)**-53/n < I(2)**-47
assert weights.min()>werr
maxentry=mp.mpf(0);matrices=[]
scales=[iv.sqrt((4*j+1)/(2*R)) for j in range(r)]
logs=[iv.ln(2),iv.ln(3)]
for prime,shift in zip([2,3],logs):
 length=2*R-shift
 sides=[]
 for side in [0,1]:
  values=np.zeros((n+1,r))
  for q in range(n+1):
   xx=((length/2)*cosiv[q]-shift/2+side*shift)/R
   p0=I(1);p1=xx
   row=[p0]
   for degree in range(1,2*r-2):
    p2=((2*degree+1)*xx*p1-degree*p0)/(degree+1)
    if (degree+1)%2==0:row.append(p2)
    p0,p1=p1,p2
   assert len(row)==r
   for j,z in enumerate(row):
    z*=scales[j];f=float((lo(z)+hi(z))/2)
    maxentry=max(maxentry,hi(abs(z-I(f))));values[q,j]=f
   if q%500==0:print(f'prime={prime} side={side} node={q}',flush=True)
  sides.append(values)
 assert maxentry<mp.mpf(2)**-40
 lengthfloat=float((lo(length)+hi(length))/2)
 cross=sides[0].T@((weights*lengthfloat/2)[:,None]*sides[1])
 # Verified conservative norm estimate for all entry and weight conversions.
 # The exact positive weighted polynomial evaluation maps each have norm <=1.
 entryerr=2.**-40
 def nup(X):
  su=float(np.sum(X*X));gg=I(2*X.size+4)*I(2)**-53/(1-I(2*X.size+4)*I(2)**-53)
  return iv.sqrt((I(su)+I(X.size)*I(2)**-1074)/(1-gg))
 err_eval=iv.sqrt(2*R*r)*I(2)**-40
 frobprod=nup(sides[0])*nup(sides[1])
 # Includes exact weight, interval length, and formation-rounding errors.
 err_weight=(R+1)*I(2)**-47*frobprod
 weighted=(weights*lengthfloat/2)[:,None]*sides[1]
 gg=I(4*(n+1)+8)*I(2)**-53/(1-I(4*(n+1)+8)*I(2)**-53)
 err_mult=gg*nup(sides[0])*nup(weighted)+I(10)**-100
 totalerr=2*err_eval+err_eval**2+err_weight+err_mult
 assert hi(totalerr)<mp.mpf(1)/1000000
 matrices.append((prime,cross,totalerr))
C0=iv.euler+iv.pi/2+3*iv.ln(2)+iv.ln(iv.pi)
c0=float((lo(C0)+hi(C0))/2);D=c0*np.eye(r);derr=abs(C0-I(c0))
for prime,cross,err in matrices:
 al=iv.ln(prime)/iv.sqrt(prime);a=float((lo(al)+hi(al))/2)
 D+=2*a*cross
 derr+=2*al*err+2*abs(al-I(a))*(1+err)
# Symmetrization is allowed; charge a generous extra binary64 accumulation bound.
D=(D+D.T)/2;derr+=I(1)/10**10
assert hi(derr)<mp.mpf(1)/100000
np.save(ROOT/'verified_prime_matrix_midpoint.npy',D)
report={'status':'Signed finite prime matrix component only; no Gram or spectral certificate','rank':r,'quadrature':'Clenshaw-Curtis 2048, exact for all product polynomials','scalar_iv_digits':500,'basis_value_conversion_error_max':mp.nstr(maxentry,30),'weight_error_bound':werr,'Loewner_ridge_rational':'1/100000','computed_operator_error_upper_diagnostic':mp.nstr(hi(derr),30),'elapsed_seconds':time.time()-st}
(ROOT/'verified_prime_matrix_component.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
