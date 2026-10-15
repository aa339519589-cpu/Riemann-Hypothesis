"""Validated analytic quadrature for the k=3, A=16 complement's main seed.
This is a component certificate, not a complete S0 sign certificate.
Complete future-prefix/source corrections are separate from this file.
"""
import argparse,json,math,time
from mpmath import iv
iv.dps=90
CELL_DATA=[]
P=24;J=10;A=iv.mpf(16);nu=iv.mpf(9)/4;m=6;pi=iv.pi
ZERO=iv.mpf(0);ONE=iv.mpf(1)
def upper(v):return math.nextafter(float(v.b),math.inf)
def lower(v):return math.nextafter(float(v.a),-math.inf)
def pair(v):return [math.nextafter(lower(v),-math.inf),math.nextafter(upper(v),math.inf)]
def zjet():return [iv.mpf(0) for _ in range(P+1)]
def mul(a,b):
 return [sum((a[j]*b[n-j] for j in range(n+1)),ZERO) for n in range(P+1)]
def inv(a):
 b=zjet();b[0]=1/a[0]
 for n in range(1,P+1):b[n]=-sum((a[j]*b[n-j] for j in range(1,n+1)),ZERO)/a[0]
 return b
def power(z,alpha):
 c=zjet();c[0]=z**alpha
 for n in range(1,P+1):c[n]=c[n-1]*(alpha-n+1)/(n*z)
 return c
def expjet(z,q):
 c=zjet();c[0]=iv.exp(-q*z)
 for n in range(1,P+1):c[n]=-q*c[n-1]/n
 return c
def poly(z,q=ONE):
 w=q*z;c=zjet();c[0]=8*w**3-30*w*w+15*w;c[1]=q*(24*w*w-60*w+15);c[2]=q*q*(24*w-30);c[3]=8*q**3;return c
D=[ONE,A+m]
for n in range(1,601):D.append(((A+m+n)*D[-1]-A*D[-2])/(n+1))
def ujet(s):
 term=s**nu/iv.gamma(nu+1);v=[term,term*nu/s,term*nu*(nu-1)/(2*s*s)]
 for n in range(1,601):
  term=-term*(D[n]/D[n-1])*s/(n+nu)
  v[0]+=term;v[1]+=term*(n+nu)/s;v[2]+=term*(n+nu)*(n+nu-1)/(2*s*s)
 for r in range(3):
  nxt=abs(term)*D[601]/D[600]*s/(601+nu)
  for j in range(r):nxt*=((601+nu-j)/s)/(j+1)
  q=s*(601+A+m)/((602)*(602+nu-r))
  assert upper(q)<1
  e=upper(nxt/(1-q));v[r]+=iv.mpf([-e,e])
 u=zjet();u[:3]=v
 for j in range(P-2):
  u[j+3]=-((j+2)*(j+1)*(s+j+2-nu)*u[j+2]+(j+1)*(j+m-nu+1+A)*u[j+1]+A*u[j])/(s*(j+3)*(j+2)*(j+1))
 return u
def wjet(z,nmax):
 assert lower(z)>=15.999 and upper(z)<=128.001 and 2<=nmax<=6
 out=zjet()
 for n in range(2,nmax+1):
  for k in range(1,13):
   q=iv.mpf(k*k)/(n*n);cc=poly(z,q);ee=expjet(z,q)
   for r in range(P+1):out[r]+=sum((cc[j]*ee[r-j] for j in range(min(r,3)+1)),ZERO)/n
 out=mul(power(z,iv.mpf(1)/4),out)
 for r in range(P+1):out[r]=out[r]/pi**(iv.mpf(1)/4)+iv.mpf(['-1e-90','1e-90'])
 return out
def wprime_abs(z,r,nmax):
 out=ZERO
 for n in range(2,nmax+1):
  for k in range(1,13):
   q=iv.mpf(k*k)/(n*n);v=q*(z+r)
   c=8*v**3+30*v*v+15*v;cp=24*v*v+60*v+15
   out+=iv.exp(-q*(z-r))*(q*(cp+c)+c/(4*(z-r)))/n
 return (z+r)**(iv.mpf(1)/4)/pi**(iv.mpf(1)/4)*out+iv.mpf('1e-90')
def mf_bound(z,r,W0,nmax):
 s=z-A;R=s+r;DW=wprime_abs(z,r,nmax);wl=W0-r*DW
 if lower(wl)<=0:return None
 Mu=R**nu/iv.gamma(nu+1)*iv.exp(iv.sqrt(A)*r/iv.sqrt(s-r))*(1+R/(s-r))**m
 zz=z+r;cp=8*zz**3+30*zz*zz+15*zz
 return cp*iv.exp(-(z-r))*Mu/wl

def integrate(lo,hi,nmax,tally):
 z=(lo+hi)/2;h=(hi-lo)/2;s=z-A
 W=wjet(z,nmax);r=iv.mpf(1)/2
 while upper(r)>lower(s)/2:r/=2
 MF=mf_bound(z,r,W[0],nmax)
 while MF is None or upper(r*wprime_abs(z,r,nmax))>lower(W[0])/2:
  r/=2;MF=mf_bound(z,r,W[0],nmax)
 if upper(h/r)>iv.mpf(1)/4:
  aa=integrate(lo,z,nmax,tally);bb=integrate(z,hi,nmax,tally)
  return [x+y for x,y in zip(aa,bb)]
 F=mul(mul(mul(poly(z),expjet(z,ONE)),ujet(s)),inv(W))
 rho=h/r;rem=MF*rho**(P+1)/(1-rho)
 L=zjet();L[0]=iv.log(z/pi)/2-iv.mpf(9)/10
 for j in range(1,P+1):L[j]=(-1)**(j+1)/(2*j*z**j)
 LM=abs(L[0])+r/(2*(z-r))
 def intjet(V,E):
  val=sum((2*V[j]*h**(j+1)/(j+1) for j in range(0,P+1,2)),ZERO)
  err=upper(2*h*E);return val+iv.mpf([-err,err])
 ans=[];G=F
 for j in range(J):
  ans.append(intjet(G,rem*LM**j));G=mul(G,L)
 FF=mul(F,F);mass=[4*z*v for v in FF]
 for j in range(1,P+1):mass[j]+=4*FF[j-1]
 ans.append(intjet(mass,4*(z+r)*MF*MF*rho**(P+1)/(1-rho)))
 # Absolute J-th central moment, intentionally one-sided.
 absF=sum((abs(F[j])*h**j for j in range(P+1)),ZERO)+rem
 ans.append(2*h*absF*(abs(L[0])+h/(2*(z-h)))**J)
 # Complete future-prefix L1 and full-odd L2-square comparison rows.
 if lower(lo)>=lower(16*pi):
  ans.append(iv.sqrt(2)/pi**(iv.mpf(1)/4)*(z+h)**(iv.mpf(1)/4)*2*h*absF)
  ans.append((z+h)/(4*pi)*iv.mpf([0,max(0,upper(ans[J]))]))
 else:ans.extend([ZERO,ZERO])
 CELL_DATA.append({'lo':pair(lo),'hi':pair(hi),'z':pair(z),'h':pair(h),'nmax':nmax,'F_coefficients':[pair(v) for v in F],'F_remainder_upper':upper(rem),'full_mass':pair(ans[J])})
 tally[0]+=1
 if tally[0]%100==0:print('certified cells',tally[0],'through z',float(hi.b),flush=True)
 return ans

def run(stop,start=None):
 lo=iv.mpf(16001)/1000 if start is None else 16*pi;Z=iv.mpf(stop);cuts=[lo]
 n=3
 while upper(n*n*pi)<lower(Z):
  if lower(n*n*pi)>upper(lo):cuts.append(n*n*pi)
  n+=1
 cuts.append(Z);tot=[ZERO]*(J+4);tally=[0]
 for l,h in zip(cuts[:-1],cuts[1:]):
  nm=int(math.sqrt(float(((l+h)/2/pi).a)))
  mid=(l+h)/2
  assert lower(mid)>upper(nm*nm*pi) and upper(mid)<lower((nm+1)**2*pi)
  vals=integrate(l,h,nm,tally);tot=[x+y for x,y in zip(tot,vals)]
  print('segment complete',float(h.b), 'cells',tally[0],flush=True)
 out={'scope':'main seed phi only; onset/far/future corrections not yet added','A':16,'k':3,'P':P,'J':J,'stop':stop,'cells':tally[0],'moments':[pair(v) for v in tot[:J]],'full_mass':pair(tot[J]),'abs_moment_J_upper':upper(tot[J+1]),'prefix_L1_upper':upper(tot[J+2]),'prefix_full_L2_squared_upper':upper(tot[J+3])}
 print(json.dumps(out,indent=2),flush=True)
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--stop',type=float,default=128);ap.add_argument('--out');ap.add_argument('--prefix-only',action='store_true');ap.add_argument('--cells');a=ap.parse_args();o=run(a.stop,True if a.prefix_only else None)
 if a.cells:
  with open(a.cells,'w') as f:json.dump({'scope':'validated main-seed Taylor cells; no S0 sign claim','cells':CELL_DATA},f)
 if a.out:
  with open(a.out,'w') as f:json.dump(o,f,indent=2)
