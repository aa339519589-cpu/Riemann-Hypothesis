"""Candidate whole-line hard-band residual and quadratic least-residual Gram.
Requires independent mathematical and complete-program review before use.
"""
from pathlib import Path
import math,json,time,numpy as np,mpmath as mp
mp.mp.dps=100;iv=mp.iv;iv.dps=80;I=iv.mpf;PI=iv.pi
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1]);UP=lambda z:float(np.nextafter(float(hi(z)),np.inf))
PTH=Path(__file__).resolve().parent;start=time.time();r=127;H=I(1)/256;U=I(2)**-53;MIN=I(2)**-1074
par=json.loads((PTH/'hardband_parameters.json').read_text());bands=par['bands'];R=I(34)/25
AST=4*PI**2*125/121;delta=20*AST/9*25*iv.exp(-5*PI);e=I(1)/1024-delta
c=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI)+2*iv.ln(2)/iv.sqrt(2)+2*iv.ln(3)/iv.sqrt(3)+iv.ln(2)
base=np.load(PTH/'verified_hardband_elementary_scaled.npz');band=np.load(PTH/'verified_hardband_quadrature.npz');tr=np.load(PTH/'trial_cosine_dyadic_eps1024_scaled.npz')
assert int(tr['denominator_exponent'])==44 and np.max(abs(tr['numerators']))<2**53
P=tr['numerators'].astype(float)/2**44;assert P.shape==(1900,r)
sourceWeight=sum(((I(float(mm))+I(2)**-50)*(I(float(gg))+I(2)**-52) for mm,gg in zip(base['m'][::2],base['gaussian'][::2])),I(0))/128
assert hi(sourceWeight)<1
def gamma(n):return I(n)*U/(1-I(n)*U)
def nup(X):
 s=float(np.sum(X*X));return UP(iv.sqrt((I(s)+I(4*X.size)*MIN)/(1-gamma(2*X.size+4))))
def mul(A,B,ea=0.,eb=0.):
 C=A@B;na=nup(A);nb=nup(B);er=I(ea)*nb+I(eb)*na+I(ea)*I(eb)+gamma(4*A.shape[1]+8)*I(na)*I(nb)+I(4*A.shape[1]*C.size)*MIN
 return C,UP(er)
def diag(v,B,ev=0.,eb=0.):
 C=v[:,None]*B;mx=float(abs(v).max());er=I(mx)*I(eb)+I(ev)*(I(nup(B))+I(eb))+2*U*mx*nup(B)+I(4*C.size)*MIN
 return C,UP(er)
def scale(A,ea,q):
 C=A/q;return C,UP(I(ea)/q+2*U*nup(C)+I(4*C.size)*MIN)
def rr(X):
 ss=np.sum(X*X,axis=1);return [iv.sqrt((I(float(s))+I(4*X.shape[1])*MIN)/(1-gamma(2*X.shape[1]+4))) for s in ss]
def cn(X,half,a):return sum((v*iv.exp(I(a)*PI*j/half) for j,v in enumerate(rr(X))),I(0))
def add(A,ea,B,eb,sign=1):
 C=A+sign*B;er=I(ea)+I(eb)+2*U*(nup(A)+nup(B))+I(4*C.size)*MIN;return C,UP(er)
j=np.arange(-1024,1025,dtype=np.int64)
CT=base['cosroot'][(2*j[:,None]*np.arange(1900)[None,:])%20480]
CS=base['cosroot'][(j[:,None]*np.arange(5121)[None,:])%20480]
CB=band['cosine'];cosrad=I(2)**-52
errT=UP(cosrad*iv.sqrt(CT.size));errS=UP(cosrad*iv.sqrt(CS.size));errB=UP(cosrad*iv.sqrt(CB.size))
pp,epp=mul(CT,P,errT);Y,eY=diag(base['gaussian'],pp,2.**-52,epp)
f,ef=diag(base['m'][::2],Y[::2],2.**-50,eY)
af,eaf=mul(CS[::2].T,f,UP(cosrad*iv.sqrt(CS[::2].size)),ef);af,eaf=scale(af,eaf,10240)
mult=np.full(5121,2.);mult[0]=mult[-1]=1.;af*=mult[:,None];eaf=UP(2*I(eaf))
sc,esc=diag(base['bc'],af,2.**-44,eaf)
fh,efh=mul(CB[::2].T,f,UP(cosrad*iv.sqrt(CB[::2].size)),ef);fh,efh=scale(fh,efh,128)
hc,ehc=diag(band['weights'],fh,2.**-48,efh)
bs,ebs=mul(CS,sc,errS);hs,ehs=mul(CB,hc,errB)
s,es=add(bs,ebs,hs,ehs)
AYs,eAYs=diag(base['m'],s,2.**-50,es)
e0=float(base['e']);eYm,eeYm=diag(np.full(len(Y),e0),Y,0.,eY)
AYs,eAYs=add(AYs,eAYs,eYm,eeYm)
Ft,eFt=diag(base['m'],base['phi'],2.**-50,UP(I(2)**-42*iv.sqrt(base['phi'].size)))
rv,erv=add(Ft,eFt,AYs,eAYs,-1)
A0=cn(P,20,0);A1=sum((v*PI*j/20 for j,v in enumerate(rr(P))),I(0));Cp=cn(P,20,I(1)/4);Cph=cn(P,20,I(1)/2)
Sb=cn(sc,40,I(1)/4);Sh=iv.exp(I(873)/8/4)*sum(rr(hc),I(0));S=Sb+Sh
Bcount=len(bands);a=I(1)/4
MY=iv.exp(2*a*a)*Cp*Cp*iv.sqrt(PI/2)
Mphi=120*Bcount*iv.exp(4*a+2*I(873)/8*a)
MAY=2*(25*S*S+I(e0)**2*MY)
MR=3*(Mphi+25*S*S+I(e0)**2*MY)
poisson=iv.exp(2*PI*a/H)-1
quadR=2*MR/poisson;quadY=2*MY/poisson
outY=2*A0*iv.exp(-16)/iv.sqrt(8)
Ynorm=iv.sqrt(H*(I(nup(Y))+I(eY))**2+outY*outY+quadY)
outR=abs(I(e0))*outY+I(10)**-500
rhoSyn=iv.sqrt(H*(I(nup(rv))+I(erv))**2+outR*outR+quadR)
# Genuine input extension tail for phi=(2x)^k/k! times the exact carrier.
EFsq=I(0)
for rec in bands:
 powers=range(0,rec['Taylor_remainder_order'],2) if rec['left_over_8']==0 else range(rec['Taylor_remainder_order'])
 for k in powers:
  decay=2*PI*iv.exp(2*R)-4-I(2*k)/R;assert lo(decay)>0
  EFsq+=2*AST*(2*R)**(2*k)*iv.exp(4*R-PI*iv.exp(2*R))/(math.factorial(k)**2*decay)
EF=iv.sqrt(EFsq)
bPeriod=I(12)/5*(389*A0+24*A1)*iv.exp(-40)/(1-iv.exp(-40))
# Complete-Gamma-minus-prime sampling aliases, with the actual theta strip.
dt=PI/40;t0=128*PI;rat=iv.exp(-dt/2);sum0=iv.exp(-t0/2)/(1-rat)
sum2=iv.exp(-t0/2)*(t0*t0/(1-rat)+2*t0*dt*rat/(1-rat)**2+dt*dt*rat*(1+rat)/(1-rat)**3)
alias=(I(160)/9*Cph)/80*(72*sum2+4*c*sum0)
# CC128 error for the actual positive-frequency hard-band Fourier integral.
qerr=I(0)
for rec in bands:
 width=I(rec['right_over_8']-rec['left_over_8'])/8;w=width/2
 qerr+=2*c*A0/PI*width*(w*(8+iv.ln(4)))**128/math.factorial(128)
widthSum=sum((I(rec['right_over_8']-rec['left_over_8'])/8 for rec in bands),I(0))
# Poisson alias for the non-grid band-node Fourier integrals of f=mY.
bandAlias=2*(I(160)/9*Cph)*iv.exp(I(873)/16-128*PI)/(1-iv.exp(-128*PI))*c*widthSum/PI
coefErr=iv.sqrt(len(sc))*I(esc)+iv.sqrt(len(hc))*I(ehc)
eErr=abs(e-I(e0))*Ynorm
EA=bPeriod+alias+bandAlias+qerr+coefErr+eErr+I(10)**-100
rho=rhoSyn+EA+EF
assert hi(A0)<1000 and hi(A1)<100000 and hi(sum(rr(hc),I(0))+sum(rr(sc),I(0)))<10**8
# Whole-line cross and energy midpoints. Every final symmetrization is enclosed.
cr,ecr=mul(Ft.T,Y,eFt,eY);cr,ecr=scale(cr,ecr,256)
ag,eag=mul(Y.T,AYs,eY,eAYs);ag,eag=scale(ag,eag,256)
quadCross=2*iv.sqrt(Mphi*MY)/poisson;quadEnergy=2*iv.sqrt(MAY*MY)/poisson
crossErr=I(ecr)+quadCross+EF*Ynorm+I(10)**-100
energyErr=I(eag)+quadEnergy+EA*Ynorm+abs(I(e0))*outY*outY+I(10)**-100
cmid=(cr+cr.T)/2;amid=(ag+ag.T)/2
symErr=4*U*nup(cmid)+2*U*nup(amid)+I(12*r*r)*MIN
Q0=2*cmid-amid;symErr+=2*U*(2*nup(cmid)+nup(amid))+I(4*r*r)*MIN
centerErr=2*crossErr+energyErr+symErr
Gerror=centerErr+rho*rho/e
assert hi(rho)<mp.mpf(1)/400000
assert hi(Gerror)<mp.mpf(1)/12000
assert hi(Ynorm)<35 and hi(EF)<mp.mpf(13)/10**9
np.save(PTH/'verified_hardband_Q0_midpoint.npy',Q0)
rep={'status':'Candidate complete least-residual ledger; pending whole-chain independent review','rank':r,'epsilon':'1/1024','A0_upper':mp.nstr(hi(A0),30),'A1_upper':mp.nstr(hi(A1),30),'Y_HS_upper':mp.nstr(hi(Ynorm),30),'source_sample_weight_upper':mp.nstr(hi(sourceWeight),30),'input_extension_error_upper':mp.nstr(hi(EF),30),'synthesis_residual_upper':mp.nstr(hi(rhoSyn),30),'b_periodization_upper':mp.nstr(hi(bPeriod),30),'source_alias_upper':mp.nstr(hi(alias),30),'non_grid_band_source_alias_upper':mp.nstr(hi(bandAlias),30),'hardband_quadrature_error_upper':mp.nstr(hi(qerr),30),'finite_coefficient_error_upper':mp.nstr(hi(coefErr),30),'operator_action_error_upper':mp.nstr(hi(EA),30),'true_residual_HS_upper':mp.nstr(hi(rho),30),'least_residual_center_error_upper':mp.nstr(hi(centerErr),30),'quadratic_residual_Gram_error_upper':mp.nstr(hi(rho*rho/e),30),'true_Gram_norm_error_upper':mp.nstr(hi(Gerror),30),'elapsed_seconds':time.time()-start}
(PTH/'hardband_continuous_residual_result.json').write_text(json.dumps(rep,indent=2)+'\n');print(json.dumps(rep,indent=2))
