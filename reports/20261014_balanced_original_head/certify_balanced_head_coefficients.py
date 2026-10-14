"""Interval sine/variation certificate for the EXACT balanced head loads.
Uses the independently replayable calibration JSON, never its midpoints.
"""
from mpmath import iv
import math,json,time,hashlib
from pathlib import Path
iv.dps=50;I=iv.mpf;pi=iv.pi;b=iv.ln(2);root=Path(__file__).parent
cal=json.loads((root/'balanced_head_load_certificate.json').read_text())
cU=[I(v) for v in cal['coefficient_U_plus_n2_n3']]
cV=[I(v) for v in cal['coefficient_n1_plus_n2_n3']]
def lo(x):return math.nextafter(float(x.a),-math.inf)
def hi(x):return math.nextafter(float(x.b),math.inf)
def ab(x):return max(abs(lo(x)),abs(hi(x)))
def out(x):return [lo(x),hi(x)]
P=[[I(0),I(15),I(-30),I(8)]];M=[I(53)]
for j in range(28):
 old=P[-1];new=[I(0) for _ in range(len(old)+1)]
 for k,c in enumerate(old):new[k]+=(I(4*k+1)/2)*c;new[k+1]-=2*c
 P.append(new);M.append(M[-1]*(I(4*j+17)/2))
def poly(p,w):
 a=I(0)
 for c in p[::-1]:a=a*w+c
 return a
assert lo(pi*iv.exp(-I(7)/5))>.75
for j in range(29):
 w=I(3)*17**2
 assert hi((I(18)/17)**(2*j+6)*iv.exp(-3*35))<.5
 assert hi(4*M[j]*w**(j+3)*iv.exp(-w))<1e-220
for j in range(11):
 w=I(3)/4*33**2
 assert hi((I(34)/33)**(2*j+7)*iv.exp(-I(3)/4*67))<.5
 assert hi(2*M[j]*33*w**(j+3)*iv.exp(-w))<1e-260

def psis(x,J):
 zz=pi*iv.exp(2*x);p=[I(0) for _ in range(J+1)]
 for m in range(1,17):
  w=m*m*zz;ee=iv.exp(-w)
  for j in range(J+1):p[j]+=poly(P[j],w)*ee
 return [iv.exp(x/2)*v+I(['-1e-220','1e-220']) for v in p]
def mirrors(x,J):
 zz=pi*iv.exp(-2*x);p=[I(0) for _ in range(J+1)]
 for m in range(2,33):
  w=m*m*zz;ee=iv.ln(m)*iv.exp(-w)
  for j in range(J+1):p[j]+=poly(P[j],w)*ee
 return [iv.exp(-x/2)*v+I(['-1e-260','1e-260']) for v in p]
raw0=psis(I(0),27);D0=[I(0) if j%2==0 else raw0[j] for j in range(28)]
ORG=I(1)/50;rawrange=psis(I([0,1/50]),28)
REM={j:math.nextafter(ab(rawrange[j+22])/22,math.inf) for j in [0,2,4,6]}
def Hder(j,x,k):
 ans=I(0)
 for r in range(k,21):
  if r%2==0:ans+=D0[j+r+1]*x**(r-k)/((r+1)*math.factorial(r-k))
 err=I(REM[j])*x**(21-k)/math.factorial(21-k)
 return ans+I([-hi(err),hi(err)])
def quotient(A,B,J):
 v=[]
 for j in range(J+1):
  num=A[j]
  for k in range(j):num-=math.comb(j,k)*v[k]*B[j-k]
  v.append(num/B[0])
 return v

def loads(x,J):
 rr=mirrors(x,J+6)
 if hi(x)<=hi(ORG):
  den=[Hder(0,x,k) for k in range(J+1)]
  rat=[quotient([Hder(j,x,k) for k in range(J+1)],den,J) for j in [2,4,6]]
 else:
  pp=psis(x,J+6)
  rat=[quotient(pp[j:j+J+1],pp[:J+1],J) for j in [2,4,6]]
 ns=[]
 for j,R in zip([2,4,6],rat):
  row=[]
  for k in range(J+1):
   val=-(-1)**k*rr[j+k]
   for a in range(k+1):val+=math.comb(k,a)*(-1)**a*rr[a]*R[k-a]
   row.append(2*val)
  ns.append(row)
 us=[];vs=[]
 for k in range(J+1):
  us.append(iv.exp(x/2)/2**k+cU[0]*ns[1][k]+cU[1]*ns[2][k])
  vs.append(I(5)/787*(ns[0][k]+cV[0]*ns[1][k]+cV[1]*ns[2][k]))
 return us,vs

NB=1024;TV=[I(0),I(0)];bounds=[[0.]*5,[0.]*5];t0=time.time();boxes=[]
for i in range(NB):
 l=b*i/NB;r=b*(i+1)/NB
 if lo(l)<hi(ORG)<hi(r):boxes.extend([(l,ORG),(ORG,r)])
 else:boxes.append((l,r))
for i,(l,r) in enumerate(boxes):
 vals=loads(I([max(0,lo(l)),hi(r)]),4)
 mids=loads((l+r)/2,1)
 for j in range(2):
  deriv_bound=min(ab(vals[j][1]),hi(I(ab(mids[j][1]))+(r-l)/2*ab(vals[j][2])))
  TV[j]+=(r-l)*deriv_bound
  for k in range(5):bounds[j][k]=max(bounds[j][k],ab(vals[j][k]))
 if i%512==0:print('bound boxes',i,'time',time.time()-t0,flush=True)
origin=loads(I(0),0)
# Both right endpoints vanish EXACTLY by the defining calibration.
TVtot=[TV[j]+ab(origin[j][0]) for j in range(2)]
ibp=[iv.sqrt(2*b)/pi*v for v in TVtot]
print('TV',list(map(out,TVtot)),'IBP',list(map(out,ibp)),'bounds',bounds,flush=True)
assert hi(ibp[0])<2 and hi(ibp[1])<3
norm=iv.sqrt(2/b);qmax=48*pi/b
M4=[sum(math.comb(4,k)*I(bounds[j][k])*qmax**(4-k) for k in range(5)) for j in range(2)]
NS=2048
while max(hi(norm*b/180*(b/NS)**4*m) for m in M4)>4e-6:NS*=2
errors=[norm*b/180*(b/NS)**4*m for m in M4]
sums=[[I(0) for _ in range(48)] for _ in range(2)]
for i in range(NS+1):
 vals=loads(b*i/NS,0) if i<NS else ([I(0)],[I(0)])
 wt=1 if i in (0,NS) else 4 if i%2 else 2
 for k in range(1,49):
  ss=iv.sin(pi*(i*k)/NS)
  for j in range(2):sums[j][k-1]+=wt*vals[j][0]*ss
 if i%512==0:print('quad node',i,'time',time.time()-t0,flush=True)
coeff=[]
for j in range(2):
 row=[]
 for k,total in enumerate(sums[j],1):
  val=norm*(b/NS)/3*total+I([-hi(errors[j]),hi(errors[j])])
  interval=out(val);assert interval[1]-interval[0]<2e-5
  row.append({'k':k,'interval':interval})
 coeff.append(row)
result={'basis':'sqrt(2/log 2) sin(k*pi*x/log 2)','calibration_sha256':hashlib.sha256((root/'balanced_head_load_certificate.json').read_bytes()).hexdigest(),'loads':['l_U=exp(x/2)+c_U2*n2+c_U3*n3','l_V=(5/787)*(n1+c_V2*n2+c_V3*n3)'],'endpoint_zero_exact':True,'origin_intervals':[out(v[0]) for v in origin],'TV_with_left_endpoint_upper_enclosures':list(map(out,TVtot)),'ibp_constants_upper_enclosures':list(map(out,ibp)),'tail_squared_bounds':['4/48','9/48'],'derivative_bounds':bounds,'simpson_subintervals':NS,'uniform_simpson_errors':list(map(out,errors)),'coefficients_U':coeff[0],'coefficients_V':coeff[1]}
(root/'balanced_head_coefficients.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',time.time()-t0,'errors',list(map(out,errors)),flush=True)
