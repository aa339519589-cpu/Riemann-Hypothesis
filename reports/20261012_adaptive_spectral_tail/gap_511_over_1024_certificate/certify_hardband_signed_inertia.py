"""Finite rational-matrix inertia via a verified approximate congruence.
The proposed eigenvectors are only a change of basis. All final signs follow
from strict Gershgorin separation with explicit binary64 arithmetic bounds.
"""
import json,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
import mpmath as mp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=100;iv=mp.iv;iv.dps=80;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
u=I(2)**-53;mn=I(2)**-1074
G0=np.load(ROOT/'verified_hardband_Q0_midpoint.npy');D0=np.load(ROOT/'verified_hardband_quadrature.npz')['D'];r=len(G0)
assert r==127 and np.array_equal(G0,G0.T) and np.array_equal(D0,D0.T)
def gam(k):return I(k)*u/(1-I(k)*u)
def nup(X):
 s=float(np.sum(X*X));return iv.sqrt((I(s)+I(4*X.size)*mn)/(1-gam(2*X.size+4)))
def frob_mul_err(A,B):return gam(4*A.shape[1]+8)*nup(A)*nup(B)+I(4*A.shape[1]*A.shape[0]*B.shape[1])*mn
G=G0+np.eye(r)/10000;D=D0+np.eye(r)/10000000000;c=I(4095)/4096
ge=max(hi(abs(I(float(G[j,j]))-I(float(G0[j,j]))-I(1)/10000)) for j in range(r))
de=max(hi(abs(I(float(D[j,j]))-I(float(D0[j,j]))-I(1)/10000000000)) for j in range(r))
ge=I(ge)*iv.sqrt(r);de=I(de)*iv.sqrt(r)
P=G@D;errP=frob_mul_err(G,D)
Z=P@G;errZ=frob_mul_err(P,G)+errP*nup(G)
C=float(c.a)*G-Z
errC=errZ+4*u*(nup(Z)+nup(G))+I(8*r*r)*mn
# Add perturbation from converting exact rational diagonal ridges into doubles.
errC+=c*ge+(2*nup(G)*ge+ge**2)*nup(D)+(nup(G)+ge)**2*de
C=(C+C.T)/2;errC+=2*u*nup(C)+I(4*r*r)*mn
st=time.time();vals,V=eigh(C)
Q=V.T@V;errOrth=frob_mul_err(V.T,V)
assert hi(nup(Q-np.eye(r))+errOrth)<mp.mpf(1)/1000
A=V.T@C;errA=frob_mul_err(V.T,C)
W=A@V;errW=frob_mul_err(A,V)+errA*nup(V)+errC*nup(V)**2
# A Frobenius perturbation gives row absolute error <=sqrt(r) times its bound.
rowerr=iv.sqrt(r)*errW
positive=[];negative=[]
for j in range(r):
 off=float(np.sum(abs(W[j,:]))-abs(W[j,j]))
 # Avoid subtraction cancellation in an upper bound for the off-diagonal sum.
 offdirect=float(np.sum(np.abs(np.delete(W[j,:],j))))
 offupper=I(offdirect)/(1-gam(2*r+4))+I(r)*mn
 lower=I(float(W[j,j]))-offupper-rowerr
 upper=I(float(W[j,j]))+offupper+rowerr
 if lo(lower)>0:positive.append(lo(lower))
 elif hi(upper)<0:negative.append(hi(upper))
 else:raise RuntimeError(f'Unseparated congruence row {j}')
assert len(negative)==1 and len(positive)==126
assert min(positive)>mp.mpf(6)/100000
report={'status':'Finite exact-rational Ccert inertia component; continuous Gram and prime-matrix hypotheses must independently pass','rank':r,'G_ridge':'1/10000','D_ridge':'1/10000000000','c':'4095/4096','certified_negative_directions':len(negative),'certified_positive_directions':len(positive),'minimum_positive_Gershgorin_lower':mp.nstr(min(positive),30),'negative_Gershgorin_upper':mp.nstr(max(negative),30),'congruence_row_error_upper':mp.nstr(hi(rowerr),30),'C_matrix_rounding_error_Frobenius_upper':mp.nstr(hi(errC),30),'invertibility_test_upper':mp.nstr(hi(nup(Q-np.eye(r))+errOrth),30),'elapsed_seconds':time.time()-st}
(ROOT/'hardband_signed_finite_inertia_result.json').write_text(json.dumps(report,indent=2));np.save(ROOT/'hardband_rational_congruence_matrix.npy',V)
print(json.dumps(report,indent=2))
