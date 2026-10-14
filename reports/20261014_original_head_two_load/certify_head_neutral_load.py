"""Outward interval certificate for the complete first neutral head load.
No finite Gamma/head matrix or original-form sign is asserted by this file.
All theta and Mangoldt tails are retained by exact divisor regrouping and
uniform analytic error bounds stated in HEAD_NEUTRAL_LOAD_CERTIFICATE.md.
"""
from mpmath import iv
import math,json,time
from pathlib import Path
iv.dps=50
I=iv.mpf
ZERO=I(0)
PI=iv.pi
B=iv.ln(2)
OUT=Path(__file__).with_name('head_neutral_load_certificate.json')

def ends(x):return math.nextafter(float(x.a),-math.inf),math.nextafter(float(x.b),math.inf)
def absup(x):return max(abs(ends(x)[0]),abs(ends(x)[1]))
def up(x):return math.nextafter(float(x.b),math.inf)
def down(x):return math.nextafter(float(x.a),-math.inf)
def hull_abs(x):return I([-absup(x),absup(x)])
def poladd(a,b):
 c=[0]*max(len(a),len(b))
 for j,v in enumerate(a):c[j]+=v
 for j,v in enumerate(b):c[j]+=v
 return c
# d/dx of exp(x/2) P(z) exp(-z), z'=2z.
P=[[0,15,-30,8]]
for j in range(24):
 a=P[-1];c=[I(0)]*(len(a)+1)
 for k,v in enumerate(a):
  c[k]+=I(4*k+1)/2*v;c[k+1]-=2*v
 P.append(c)

def poly(a,x):
 v=I(0)
 for c in a[::-1]:v=v*x+c
 return v

# Coefficient-l1 bounds pay every omitted integer analytically.
M=[I(53)]
for j in range(24):M.append(M[-1]*(I(4*j+17)/2))
for J,N,eps in [(6,8,I("1e-65")),(24,16,I("1e-220"))]:
 w=I(3)*(N+1)**2
 for j in range(J+1):
  ratio=(I(N+2)/(N+1))**(2*(j+3))*iv.exp(-I(3)*(2*N+3))
  assert up(ratio)<0.5
  tail=4*M[j]*w**(j+3)*iv.exp(-w)
  assert up(tail)<down(eps)
assert down(PI*iv.exp(-I(7)/5))>0.75
w=I(3)/4*33**2
for j in range(5):
 coeff=M[j+2]+M[j]/4;degree=j+5
 ratio=(I(34)/33)**(2*degree+1)*iv.exp(-(I(3)/4)*67)
 assert up(ratio)<0.5
 assert up(2*coeff*33*w**degree*iv.exp(-w))<1e-300
print("complete integer-tail bounds passed",flush=True)

def theta_derivs(x,J,labels=8):
 z=PI*iv.exp(2*x);pref=iv.exp(x/2)
 out=[I(0) for _ in range(J+1)]
 for m in range(1,labels+1):
  w=m*m*z;ga=iv.exp(-w)
  for j in range(J+1):out[j]+=poly(P[j],w)*ga
 tail=I(['-1e-65','1e-65']) if J<=6 else I(['-1e-220','1e-220'])
 return [pref*v+tail for v in out]

# At zero all even derivatives of the odd theta psi vanish exactly.
raw0=theta_derivs(I(0),23,16)
D0=[I(0) if j%2==0 else raw0[j] for j in range(24)]
ORIGIN=I(1)/50
# H_j=psi^(j)/x, j=0,2. Taylor degree20, remainder via H_j^(21).
rawrange=theta_derivs(I([0,1/50]),24,16)
REM={0:math.nextafter(absup(rawrange[22])/22,math.inf),2:math.nextafter(absup(rawrange[24])/22,math.inf)}
print('origin remainder derivative bounds',REM,flush=True)

def Hder(j,x,k):
 ans=I(0)
 for r in range(k,21):
  if r%2==0:
   ans+=D0[j+r+1]*x**(r-k)/((r+1)*math.factorial(r-k))
 err=I(REM[j])*x**(21-k)/math.factorial(21-k)
 return ans+I([-up(err),up(err)])

def quotient_derivs(A,Bd,J):
 out=[]
 for j in range(J+1):
  num=A[j]
  for k in range(j):num-=math.comb(j,k)*out[k]*Bd[j-k]
  out.append(num/Bd[0])
 return out

def ratio_derivs(x,J):
 if up(x)<=up(ORIGIN):
  den=[Hder(0,x,j) for j in range(J+1)]
  num=[Hder(2,x,j) for j in range(J+1)]
 else:
  z=theta_derivs(x,J+2)
  den=z[:J+1];num=z[2:]
 out=quotient_derivs(num,den,J)
 out[0]-=I(1)/4
 return out

def rows(x,J):
 z=PI*iv.exp(-2*x);pref=iv.exp(-x/2)
 outL=[I(0) for _ in range(J+1)]
 outS=[I(0) for _ in range(J+1)]
 for m in range(2,33):
  w=m*m*z;ga=iv.ln(m)*iv.exp(-w)
  vals=[poly(P[j],w) for j in range(J+3)]
  for j in range(J+1):
   outL[j]+=(-1)**j*vals[j]*ga
   outS[j]+=(-1)**j*(vals[j+2]-vals[j]/4)*ga
 tail=I(['-1e-300','1e-300'])
 return [pref*v+tail for v in outL],[pref*v+tail for v in outS]

def nder(x,J):
 R=ratio_derivs(x,J);L,S=rows(x,J)
 out=[]
 for j in range(J+1):
  v=-S[j]
  for k in range(j+1):v+=math.comb(j,k)*L[k]*R[j-k]
  out.append(2*v)
 return out

# Partition exactly at the origin Taylor transition.
t0=time.time(); NB=2048
bound=[0.0]*5;TV=I(0)
intervals=[]
for j in range(NB):
 l=B*j/NB;r=B*(j+1)/NB
 if down(l)<up(ORIGIN)<up(r):intervals.extend([(l,ORIGIN),(ORIGIN,r)])
 else:intervals.append((l,r))
for it,(l,r) in enumerate(intervals):
 x=I([max(0,down(l)),up(r)])
 # A tiny interval straddling the representation switch is evaluated by the
 # direct formula, valid because its left endpoint is far from zero.
 nd=nder(x,4)
 TV+=(r-l)*absup(nd[1])
 for j in range(5):bound[j]=max(bound[j],absup(nd[j]))
 if it%128==0:print('bound boxes',it,'time',time.time()-t0,flush=True)
nzero=nder(I(0),0)[0];nb=nder(B,0)[0]
TVtotal=TV+absup(nzero)+absup(nb)
print('n endpoints',ends(nzero),ends(nb),'TVtotal',ends(TVtotal),'derivative maxima',bound,flush=True)
assert up(TVtotal)<1250
# Outward upper bounds computed with interval arithmetic.
qmax=48*PI/B
M4=sum(math.comb(4,j)*I(bound[j])*qmax**(4-j) for j in range(5))
norm=5*iv.sqrt(2/B)/787
NS=2048
while up(norm*B/180*(B/NS)**4*M4)>I('0.000004').a:NS*=2
err=norm*B/180*(B/NS)**4*M4
print('Simpson N',NS,'uniform error',ends(err),flush=True)
sums=[I(0) for _ in range(48)]
for i in range(NS+1):
 x=B*i/NS
 value=nder(x,0)[0]
 weight=1 if i in (0,NS) else 4 if i%2 else 2
 for k in range(1,49):
  # x*k*pi/b simplifies EXACTLY to i*k*pi/NS.
  sine=iv.sin(PI*(i*k)/NS)
  sums[k-1]+=weight*value*sine
 if i%512==0:print('quadrature node',i,'time',time.time()-t0,flush=True)
cert=[]
for k,total in enumerate(sums,1):
 val=norm*(B/NS)/3*total
 en=I([-up(err),up(err)])
 val+=en
 lo,hi=ends(val)
 # Decimal JSON floats are expanded outwards once more.
 lo=math.nextafter(lo,-math.inf);hi=math.nextafter(hi,math.inf)
 assert hi-lo<2e-5
 cert.append({'k':k,'interval':[lo,hi],'midpoint':(lo+hi)/2,'absolute_error':(hi-lo)/2})
# The IBP coefficient estimate is sqrt(2b)/pi*(5/787)*TVtotal/k.
coefftail=iv.sqrt(2*B)/PI*5/787*TVtotal
assert up(coefftail)<3
result={'basis':'sqrt(2/log 2) sin(k*pi*x/log 2)','normalization':'5/787','n_endpoints':[ends(nzero),ends(nb)],'total_variation_with_endpoints_upper_enclosure':ends(TVtotal),'derivative_abs_bounds':bound,'simpson_subintervals':NS,'uniform_simpson_error':ends(err),'ibp_constant':ends(coefftail),'tail_l2_squared_bound':'9/48','coefficients':cert}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('PASS',str(OUT),'elapsed',time.time()-t0,flush=True)
