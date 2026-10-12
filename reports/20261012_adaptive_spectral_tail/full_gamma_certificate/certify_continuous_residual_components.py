"""Candidate continuous residual accounting for exact Gaussian-cosine trials.
Uses already outward-verified scalar tables and explicit analytic error terms.
Must be independently reviewed together with the companion proof before use.
"""
import json,math,time
from pathlib import Path
import numpy as np
import mpmath as mp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=100;iv=mp.iv;iv.dps=80;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
UP=lambda z:float(np.nextafter(float(hi(z)),np.inf))
U=I(2)**-53;MIN=I(2)**-1074;PI=iv.pi
start=time.time();r=373;h=1/128;H=I(1)/128
A=4*PI**2*125/121;delta=20*A/9*16*iv.exp(-4*PI);e=I(1)/8-delta
cN=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI)+2*iv.ln(2)/iv.sqrt(2)+2*iv.ln(3)/iv.sqrt(3)
T=65;win=14;R=I(209)/100
base=np.load(ROOT/'verified_elementary_tables.npz');src=np.load(ROOT/'verified_elementary_tables_box24.npz')
TR=np.load(ROOT/'trial_cosine_dyadic.npz')
assert int(TR['denominator_exponent'])==42 and np.max(abs(TR['numerators']))<2**53
P=TR['numerators'].astype(float)/2**42
EH=np.load(ROOT/'verified_rho_ehat_rows_827.npy')
assert P.shape==(1274,r) and EH.shape==(828,r)
# Exact trial frequencies are pi*j/20; all stored coefficients are binary rationals.

def gamma(n):return I(n)*U/(1-I(n)*U)
def normup(X):
 s=float(np.sum(X*X));g=gamma(2*X.size+4)
 return UP(iv.sqrt((I(s)+I(4*X.size)*MIN)/(1-g)))
def mul(A,B,ea=0.,eb=0.):
 C=A@B;na=normup(A);nb=normup(B);g=gamma(4*A.shape[1]+8)
 err=I(ea)*nb+I(eb)*na+I(ea)*I(eb)+g*I(na)*I(nb)+I(4*A.shape[1]*C.size)*MIN
 return C,UP(err)
def diagmul(v,B,ev=0.,eb=0.):
 C=v[:,None]*B;mx=float(np.max(abs(v)));nb=normup(B)
 err=I(mx)*eb+I(ev)*(nb+I(eb))+2*U*I(mx)*nb+I(4*C.size)*MIN
 return C,UP(err)
def scale(A,ea,q):
 C=A/q;return C,UP(I(ea)/q+2*U*normup(C)+I(4*C.size)*MIN)
def rownorms(X):
 ss=np.sum(X*X,axis=1);g=gamma(2*X.shape[1]+4)
 return [iv.sqrt((I(float(s))+I(4*X.shape[1])*MIN)/(1-g)) for s in ss]
def coeffnorm(X,period_half,a):
 rr=rownorms(X)
 return sum((v*iv.exp(I(a)*PI*j/period_half) for j,v in enumerate(rr)),I(0))

jj=np.arange(-512,513,dtype=np.int64)
def costable(root,N,K):return root[(jj[:,None]*np.arange(K,dtype=np.int64)[None,:])%N]
C40=costable(base['cosroot'],5120,1274)
C48=costable(src['cosroot'],6144,3073)
coserr=float(2.**-52)
errC40=UP(I(coserr)*iv.sqrt(C40.size));errC48=UP(I(coserr)*iv.sqrt(C48.size))
PP,errPP=mul(C40,P,errC40,0.)
YY,errYY=diagmul(base['gaussian'],PP,2.**-52,errPP)
ff,errff=diagmul(base['m'],YY,2.**-50,errYY)
af,erraf=mul(C48.T,ff,errC48,errff);af,erraf=scale(af,erraf,6144)
mult=np.full(3073,2.);mult[0]=mult[-1]=1.
sc,errsc=diagmul(src['d'],af,2.**-44,erraf)
sc*=mult[:,None];errsc=UP(2*I(errsc)) # multiplication by two is exact
# Source samples outside |x|<=4 and their periodic copies have total <10^-1000.
errsc=UP(I(errsc)+I(10)**-500)
gc=EH.copy();gc[1:]*=2;gc,errgc=scale(gc,UP(2*I(2)**-44*iv.sqrt(EH.size)),40)
# gc and sc now define exact binary-rational finite cosine sums for a residual.
gv,errgv=mul(C40[:,:828],gc,UP(I(coserr)*iv.sqrt(1025*828)),0.)
sv,errsv=mul(C48,sc,errC48,0.)
uv=gv-sv;erruv=UP(I(errgv)+I(errsv)+2*U*(normup(gv)+normup(sv)))
rv,errrv=diagmul(base['m'],uv,2.**-50,erruv)
e0=float(src['e']);rv-=e0*YY
errrv=UP(I(errrv)+abs(I(e0))*I(errYY)+4*U*(normup(rv)+abs(I(e0))*normup(YY)))
# Real coefficient norms, directed outward (no floating scalar sum is trusted).
S0=coeffnorm(P,20,0);S1=sum((a*PI*j/20 for j,a in enumerate(rownorms(P))),I(0))
Cph=coeffnorm(P,20,I(1)/2)
Cpa=coeffnorm(P,20,I(1)/4);Cga=coeffnorm(gc,20,I(1)/4);Csa=coeffnorm(sc,24,I(1)/4)
Cg0=coeffnorm(gc,20,0);Cs0=coeffnorm(sc,24,0)
assert hi(Cg0+Cs0+S0)<10**6 and hi(S0)<14 and hi(S1)<637
# Analytic strip .25 and the proved m^2 strip integral <=25.
stripR=50*(Cga+Csa)**2+2*I(e0)**2*iv.exp(I(1)/8)*Cpa**2*iv.sqrt(PI/2)
quadR=2*stripR/(iv.exp(2*PI*(I(1)/4)/H)-1)
# All omitted Gaussian samples, with the double-exponential m terms negligible.
outR=2*abs(I(e0))*S0*iv.exp(-16)/iv.sqrt(8)+I(10)**-500
rhoSynth=iv.sqrt(H*(I(normup(rv))+I(errrv))**2+outR**2+quadR)
# True b periodization: a separately proved whole-line bound.
Cf=389*S0+24*S1
bPeriod=I(12)/5*Cf*iv.exp(-24)/(1-iv.exp(-24))
# Fourier alias and high-mode omission for d=b-(1-rho^2)C_N.
# f=m*Y: ||fhat(t)|| <= (160/9) C_P(.5) exp(-|t|/2).
FourC=I(160)/9*Cph;dt=PI/24;t0=128*PI;rat=iv.exp(-dt/2)
sum0=iv.exp(-t0/2)/(1-rat)
sum2=iv.exp(-t0/2)*(t0*t0/(1-rat)+2*t0*dt*rat/(1-rat)**2+dt*dt*rat*(1+rat)/(1-rat)**3)
aliasD=FourC/48*(72*sum2+4*cN*sum0) # ||m||_2<1
# Window-kernel periodizations. K has L1 norm <4; K*K has the displayed tail.
def tail_kernel(D,power_numerator,constant):
 return I(constant)/(PI*D)*(I(power_numerator)/(T*D))**win*(1+I(1)/win)
# Q^2 C_N f: inner |f| support paid at 2; shifts at most log 3.
Dq=48-2-2-iv.ln(3)
q2Period=cN*S0*tail_kernel(Dq,4*win,32)
# Exterior in x and the input |y|>2 have actual theta L1/L2 envelopes.
mtail2=iv.sqrt(A)*iv.exp(4-PI*iv.exp(4)/2)
ftail2=S0*iv.exp(-4)*2*iv.sqrt(A)/PI*iv.exp(-PI*iv.exp(4)/2)
q2Period+=cN*S0*tail_kernel(24-2-iv.ln(3),4*win,32)*mtail2+4*T*cN*ftail2
# Input m Q e_j: period 40, source support [-R,R]. Pay sqrt(rank) for HS.
inputPeriod=iv.sqrt(r)*iv.sqrt(2*R)*(tail_kernel(40-2-R,2*win,2)+mtail2*tail_kernel(20-R,2*win,2))
# All scalar/finite arithmetic perturbations enter as exact cosine coefficient errors.
coefError=iv.sqrt(len(sc))*I(errsc)+iv.sqrt(len(gc))*I(errgc)
eError=abs(e-I(e0))*2*S0
rho=rhoSynth+bPeriod+aliasD+q2Period+inputPeriod+coefError+eError+I(10)**-100
# Actual cross Gram: F_actual^*Y. Use Hermitian part after enclosure.
fv,errfv=diagmul(base['m'],gv,2.**-50,errgv)
cross,errcross=mul(fv.T,YY,errfv,errYY);cross*=h;errcross=UP(H*I(errcross)+2*U*normup(cross))
stripCross=I(40)/3*Cga*Cpa*iv.exp(I(1)/16)
quadCross=2*stripCross/(iv.exp(2*PI*(I(1)/4)/H)-1)
inputError=inputPeriod+iv.sqrt(len(gc))*I(errgc)
crossError=I(errcross)+quadCross+inputError*2*S0+I(10)**-100
Gmid=(cross+cross.T)/2
# Enclose the final rounded symmetrization as well as the earlier cross product.
symError=2*U*I(normup(Gmid))+I(4*Gmid.size)*MIN
crossError+=symError
Gerror=(I(3)/2)/e*rho+crossError
assert hi(rho)<mp.mpf(1)/100000
assert hi(Gerror)<mp.mpf(1)/30000
np.save(ROOT/'verified_cross_gram_midpoint.npy',Gmid)
np.savez_compressed(ROOT/'residual_cosine_coefficients.npz',P=P,g=gc,s=sc)
rep={'status':'Candidate complete continuous residual ledger, pending independent review','rank':r,'trial_cosine_period':40,'source_FFT_period':48,'mesh':'1/128','S0_upper':mp.nstr(hi(S0),30),'S1_upper':mp.nstr(hi(S1),30),'real_coefficient_sum_upper':mp.nstr(hi(Cg0+Cs0+S0),30),'final_symmetrization_error_upper':mp.nstr(hi(symError),30),'synth_residual_upper':mp.nstr(hi(rhoSynth),30),'b_periodization_upper':mp.nstr(hi(bPeriod),30),'Fourier_alias_upper':mp.nstr(hi(aliasD),30),'Q2_periodization_upper':mp.nstr(hi(q2Period),30),'input_periodization_upper':mp.nstr(hi(inputPeriod),30),'finite_coefficient_error_upper':mp.nstr(hi(coefError),30),'total_true_residual_upper':mp.nstr(hi(rho),30),'cross_Gram_error_upper':mp.nstr(hi(crossError),30),'true_Gram_upper_ridge_needed':mp.nstr(hi(Gerror),30),'chosen_Gram_upper_ridge_rational':'1/10000','elapsed_seconds':time.time()-start,'diagnostics':{'synth_grid_residual_Frobenius':normup(rv),'grid_evaluation_error_Frobenius':errrv,'source_coefficient_error_Frobenius':errsc,'input_coefficient_error_Frobenius':errgc}}
(ROOT/'continuous_residual_component_result.json').write_text(json.dumps(rep,indent=2));print(json.dumps(rep,indent=2))
