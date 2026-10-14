"""Outward coefficients for an infinite-dimensional original-head Schur test.
This generator alone is NOT a sign certificate. It retains the complete Gamma
multiplier, reflections 2,3 and full pole. The pending neutral load is separate.
"""
from mpmath import iv
import math,json,os,argparse
iv.dps=35
b=iv.log(2);pi=iv.pi;d=iv.log(3);l=d-b
alpha2=b/iv.sqrt(2);alpha3=d/iv.sqrt(3)
def enc(v,side):
 x=float(v.a if side==0 else v.b)
 for _ in range(100):
  x=math.nextafter(x,-math.inf if side==0 else math.inf)
  n,d=x.as_integer_ratio();z=iv.mpf(n)/d
  if bool(z.a<=v.a) if side==0 else bool(z.b>=v.b):return x
 raise RuntimeError('outward float conversion')
def pair(v):return [enc(v,0),enc(v,1)]
def psi_complex(om):
 # DLMF5.9.15, expanded three times at z+8. The remainder satisfies
 # |R| <=1/(480 Re(z+8) Im(z) |z+8|^6); see companion derivation.
 z=iv.mpc(iv.mpf(1)/4,om/2);w=z+8
 p=iv.log(w)-1/(2*w)-1/(12*w**2)+1/(120*w**4)-1/(252*w**6)
 for r in range(8):p-=1/(z+r)
 er=1/(480*w.real*w.imag*abs(w)**6)
 err=iv.mpf([-er.b,er.b])
 return p.real+err,p.imag+err

def generate(N=48,M=4096):
 omega=[None]+[k*pi/b for k in range(1,M+2)]
 aval=[None];S=[None]
 for k in range(1,M+2):
  re,im=psi_complex(omega[k]);aval.append(re-iv.log(pi));S.append(im/(2*omega[k]))
 sign=[(-1)**k for k in range(M+2)]
 sinl=[None]+[iv.sin(omega[k]*l) for k in range(1,M+2)]
 ell=[None]+[-iv.sqrt(2/b)*omega[k]*sign[k]*(iv.exp(b/2)-iv.exp(-b/2))/2/(omega[k]**2+iv.mpf(1)/4) for k in range(1,M+2)]
 uu=[None]+[iv.sqrt(2/b)*omega[k]*(1-iv.sqrt(2)*sign[k])/(omega[k]**2+iv.mpf(1)/4) for k in range(1,N+1)]
 assert bool((iv.sqrt(2*b)/pi*(1+iv.sqrt(2))).b<1)
 la=[iv.mpf(2*r)+iv.mpf(1)/2 for r in range(12)]
 ew=[iv.exp(-2*b*t) for t in la]
 V=[[None]]+[ [omega[k]*sign[k]/(t*t+omega[k]**2) for t in la] for k in range(1,M+2)]
 # All omitted exp-weighted Gram entries are <10^-16: lambda_12=24.5,
 # omega/(lambda²+omega²)<=1/(2lambda), with geometric factor1/16.
 LR=iv.mpf('24.5')
 assert bool((iv.exp(-2*b*LR)/(b*LR**2)/(1-iv.exp(-4*b))).b<iv.mpf('1e-16'))
 diag=[]
 for k in range(1,N+1):
  om=omega[k];s=iv.mpf(0);R=1000
  for r in range(R):
   t=iv.mpf(2*r)+iv.mpf(1)/2;s+=1/(t*t+om*om)**2
  t=iv.mpf(2*R)+iv.mpf(1)/2
  integ=iv.atan2(om,t)/(2*om**3)-t/(2*om**2*(t*t+om*om))
  tail=integ/2+iv.mpf([0,(1/(t*t+om*om)**2).b])
  diag.append(s+tail)
 C=pi+4*b/(pi*pi*N)+2*(alpha2+alpha3)+4*((iv.exp(b)-iv.exp(-b))/2-b)
 gap=[None]*(M+2)
 for j in range(N+1,M+2):gap[j]=2*aval[j]-C-iv.mpf(20)/N-iv.mpf(1)/100
 assert bool(gap[N+1].a>1)
 Ci=[1+4*alpha3/(pi*(1-iv.mpf(N)/(M+1)))+6*b/(pi*pi*i) for i in range(1,N+1)]
 tail_schur=sum(t*t for t in Ci)/(M*gap[M+1])
 low=[[None]*N for _ in range(N)];cross=[]
 for i in range(1,N+1):
  row=[]
  for j in range(1,M+1):
   A=omega[i];B=omega[j]
   if i==j:raw=diag[i-1]
   else:raw=(S[i]-S[j])/(B*B-A*A)
   E=4/b*A*B*sign[i]*sign[j]*raw
   E-=4/b*sum(ew[r]*V[i][r]*V[j][r] for r in range(12))
   E+=iv.mpf(['-1e-16','1e-16'])
   q=-E
   if i==j:
    q+=2*aval[i]+2*alpha2*(-sign[i])
    cc=2*b-d
    rr=(iv.sin(A*cc)/A-cc*iv.cos(A*d))/b
   else:rr=2/b*(A*sign[i]*sinl[j]-B*sign[j]*sinl[i])/(B*B-A*A)
   q+=2*alpha3*rr-8*ell[i]*ell[j]
   pp=pair(q)
   if j<=N:low[i-1][j-1]=pp
   else:row.append(pp)
  cross.append(row)
  print('row',i,'of',N,flush=True)
 return {'N':N,'M':M,'q_low':low,'q_cross':cross,'u':[pair(x) for x in uu[1:]],'high_diagonal':[pair(gap[j]) for j in range(N+1,M+1)],'schur_tail':pair(tail_schur),'first_gap':pair(gap[N+1])}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--N',type=int,default=48);ap.add_argument('--M',type=int,default=4096);ap.add_argument('--out',default='original_head_kernel_intervals.json');a=ap.parse_args()
 data=generate(a.N,a.M);out=os.path.join(os.path.dirname(__file__),a.out)
 with open(out,'w') as f:json.dump(data,f)
 print('Generated complete coefficient enclosures:',out,flush=True)
 print('High gap:',data['first_gap'],'omitted Schur tail:',data['schur_tail'],flush=True)
