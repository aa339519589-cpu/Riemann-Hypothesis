"""Candidate interval test of user's rank-one threshold shorting.
All assertions are directed intervals; the accompanying analytic proof and
independent review determine the theorem status.
"""
import mpmath as mp,json,sys,time
from pathlib import Path
iv=mp.iv;iv.dps=35;mp.mp.dps=50;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
ROOT=Path(__file__).resolve().parent
NC=int(sys.argv[1]) if len(sys.argv)>1 else 40000
PI=iv.pi;R=I(5)/2;DX=R/NC;EPS=I(1)/16
AST=4*PI**2*125/121;C0=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI)
LAM=[2*I(j)+I(1)/2 for j in range(6)];C=sum((1/(I(j)+I(1)/4) for j in range(6)),I(0))
DEL=20*AST/9*49*iv.exp(-7*PI)
ALS=[iv.ln(2)/iv.sqrt(2),iv.ln(3)/iv.sqrt(3),iv.ln(2)/2,iv.ln(5)/iv.sqrt(5)]
NPS=[2,3,4,5]
TH4=5**4*iv.exp(-24*PI)/(1-(I(6)/5)**4*iv.exp(-11*PI))
TH6=5**6*iv.exp(-24*PI)/(1-(I(6)/5)**6*iv.exp(-11*PI))
TH8=5**8*iv.exp(-24*PI)/(1-(I(6)/5)**8*iv.exp(-11*PI))
TH10=5**10*iv.exp(-24*PI)/(1-(I(6)/5)**10*iv.exp(-11*PI))
ZERO=I(0);tiny=I([-hi(I(10)**-45),hi(I(10)**-45)])
def cosh(t):return (iv.exp(t)+iv.exp(-t))/2
def hull(a,b):return I([lo(a),hi(b)])
def m2fun(x):
 x=abs(x);t=iv.exp(2*x)
 s=sum((n**4*(1-3/(2*PI*n*n*t))*iv.exp(-PI*(n*n-1)*t) for n in range(1,5)),ZERO)+I([0,hi(TH4)])
 return 4*PI**2*iv.exp(I(9)*x/2-PI*t)*s/(2*cosh(x/2))
def m2prime(x):
 t=iv.exp(2*x);s0=ZERO;s1=ZERO
 for n in range(1,5):
  u=PI*n*n*t;w=iv.exp(-PI*(n*n-1)*t)
  s0+=(4*u*u-6*u)*w
  s1+=u*((-8*u+30)*u-15)*w
 s0+=I([0,hi(4*PI**2*t*t*TH4)])
 tt=20*PI**3*t**3*TH6;s1+=I([-hi(tt),hi(tt)])
 th=(iv.exp(x/2)-iv.exp(-x/2))/(iv.exp(x/2)+iv.exp(-x/2))
 return iv.exp(x/2-PI*t)*(s1-th*s0/2)/(2*cosh(x/2))
def m2_taylor(x):
 x=abs(x);mid=(lo(x)+hi(x))/2;rad=(hi(x)-lo(x))/2
 er=hi(abs(m2prime(x))*I(rad))
 raw=m2fun(x);tay=m2fun(I(mid))+I([-er,er])
 return I([max(lo(raw),lo(tay)),min(hi(raw),hi(tay))])
def ffun(x):
 t=iv.exp(2*x);s=ZERO
 for n in range(1,5):
  u=PI*n*n*t
  p=4*u*(((4*u-28)*u+41)*u-9)
  s+=p*iv.exp(-PI*(n*n-1)*t)
 tt=74*PI**4*t**4*TH8
 s+=I([-hi(tt),hi(tt)])
 return iv.exp(x/2-PI*t)*s
def fprime(x):
 t=iv.exp(2*x);s=ZERO
 for n in range(1,5):
  u=PI*n*n*t;p=-2*u*((((16*u-180)*u+528)*u-405)*u+45)
  s+=p*iv.exp(-PI*(n*n-1)*t)
 tt=402*PI**5*t**5*TH10
 s+=I([-hi(tt),hi(tt)])
 return iv.exp(x/2-PI*t)*s

def f_taylor(x):
 mid=(lo(x)+hi(x))/2
 rad=(hi(x)-lo(x))/2
 er=hi(abs(fprime(x))*I(rad))
 return ffun(I(mid))+I([-er,er])

started=time.time();xs=[];ms=[];ds=[];ws=[];fs=[];aas=[];ex=[];co=[];cell=[]
DLOW=mp.inf
for j in range(NC):
 x=hull(R*j/NC,R*(j+1)/NC);m2=m2_taylor(x);m=iv.sqrt(m2)
 pn=sum((al*m*(iv.sqrt(m2_taylor(x+iv.ln(n)))+iv.sqrt(m2_taylor(x-iv.ln(n)))) for n,al in zip(NPS,ALS)),ZERO)
 d=EPS-DEL+(C-C0)*m2-pn
 DLOW=min(DLOW,lo(d));assert lo(d)>0
 f=f_taylor(x);w=f/m;aa=m/iv.sqrt(d)
 xs.append(x);ms.append(m);ds.append(d);ws.append(w);fs.append(f);aas.append(aa)
 ex.append([iv.exp(-la*x) for la in LAM]);co.append([cosh(la*x) for la in LAM])
 cell.append([DX*(I([lo(iv.exp(-la*DX)),1])+iv.exp(-2*la*x)) for la in LAM])
 if (j+1)%2000==0: print('cells',j+1,flush=True)
assert DLOW>mp.mpf(1)/50
# This tail threshold has an independent analytic proof, not empirical truncation.
mt=iv.sqrt(AST)*iv.exp(2*R-PI*iv.exp(2*R)/2)
dtail=EPS-DEL-abs(C-C0)*mt**2-2*iv.sqrt(AST)*iv.exp(-PI/2)*sum(ALS,ZERO)*mt
assert lo(dtail)>mp.mpf(1)/50

def conv(g,label):
 # Exact folded exponential convolution of a signed cell-range enclosure.
 suf=[[ZERO]*(NC+1) for k in range(6)]
 for k in range(6):
  for j in range(NC-1,-1,-1):suf[k][j]=suf[k][j+1]+DX*ex[j][k]*g[j]
 pre=[ZERO]*6;out=[]
 for j in range(NC):
  val=ZERO
  for k in range(6):
   val+=2*ex[j][k]*pre[k]+2*co[j][k]*suf[k][j+1]+cell[j][k]*g[j]
   pre[k]+=DX*co[j][k]*g[j]
  out.append(val+tiny)
 print('conv',label,'seconds',time.time()-started,flush=True)
 return out
cf=conv(fs,'Rf');bs=[ms[j]*cf[j]-(ds[j]-EPS)*ws[j] for j in range(NC)]
g=2*DX*sum((ws[j]*bs[j] for j in range(NC)),ZERO)+tiny
assert lo(g)>I(1)/1000
zs=[iv.sqrt(2)*bs[j]/iv.sqrt(ds[j]) for j in range(NC)]
# Actual T z and T a using the same complete folded R kernel.
cz=conv([aas[j]*zs[j] for j in range(NC)],'R(az)');tz=[aas[j]*cz[j] for j in range(NC)]
tau=DX*sum((z*z for z in zs),ZERO)+tiny
a1=DX*sum((zs[j]*tz[j] for j in range(NC)),ZERO)+tiny
hs=[aas[j]*(1-I(1477)/1024*xs[j]**2) for j in range(NC)]
ch=conv([aas[j]*hs[j] for j in range(NC)],'R(ah)');th=[aas[j]*ch[j] for j in range(NC)]
h2=DX*sum((h*h for h in hs),ZERO)+tiny
hTh=DX*sum((hs[j]*th[j] for j in range(NC)),ZERO)+tiny
zh=DX*sum((zs[j]*hs[j] for j in range(NC)),ZERO)+tiny
Qp=(hTh-zh**2/g)/h2
Qn=a1/tau-tau/g
# Complete positive squared trace for T, with exact cell rectangle enclosures.
pairs=[(j,k,1 if j==k else 2) for j in range(6) for k in range(j,6)]
pre=[ZERO]*len(pairs);HS=ZERO;mass=ZERO
for j in range(NC):
 a=aas[j]**2;mass+=DX*a
 for zz,(k,l,mult) in enumerate(pairs):
  ec=ex[j][k]*ex[j][l];cc=co[j][k]*co[j][l]
  HS+=mult*(8*DX*a*ec*pre[zz]+4*DX**2*a*a*ec*cc)
  pre[zz]+=DX*a*cc
mt2=AST/2*iv.exp(-PI*iv.exp(2*R))*(iv.exp(2*R)/PI+1/PI**2)
at=mt2/dtail
HS+=I([0,hi(144*(2*mass*at+at*at))])
HSc=HS-2*a1/g+(tau/g)**2
print('g',g,'tau',tau,'a1',a1,'Qp',Qp,'Qn',Qn,flush=True)
# Sign is tested only in a successful final certificate, not presumed.
rem=HS-(a1/tau)**2-Qp**2
assert lo(Qp)>hi(I(389)/100)
assert hi(Qn)<lo(-I(47)/100)
assert lo(a1)>0 and lo(tau)>0
assert lo(g)>64 and hi(g)<66
assert hi(rem)<lo(I(99)/100)
rep={'status':'ALL_WHOLE_LINE_INTERVAL_ASSERTIONS_PASS; independent review pending','cells':NC,'Dlower':str(DLOW),'g':[str(lo(g)),str(hi(g))],'Qpositive':[str(lo(Qp)),str(hi(Qp))],'Qnegative':[str(lo(Qn)),str(hi(Qn))],'Tcorrected_trace2':[str(lo(HSc)),str(hi(HSc))],'signed_HS_remainder':[str(lo(rem)),str(hi(rem))],'rational_bounds':{'d_min':'>1/50','g':'64<g<66','Qpositive':'>389/100','Qnegative':'<-47/100','signed_HS_remainder':'<99/100'}}
(ROOT/f'interval_rank1_{NC}.json').write_text(json.dumps(rep,indent=2));print(json.dumps(rep,indent=2));print('elapsed_seconds',time.time()-started)
