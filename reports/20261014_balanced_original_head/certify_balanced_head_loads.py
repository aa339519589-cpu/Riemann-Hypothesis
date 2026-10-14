"""Exact two-constraint head-load calibration, outward interval replay."""
from mpmath import iv
import math,json,time
from pathlib import Path
iv.dps=50;I=iv.mpf;pi=iv.pi;b=iv.ln(2)
def lo(x):return math.nextafter(float(x.a),-math.inf)
def hi(x):return math.nextafter(float(x.b),math.inf)
def ab(x):return max(abs(lo(x)),abs(hi(x)))
def out(x):return [lo(x),hi(x)]
P=[[I(0),I(15),I(-30),I(8)]];M=[I(53)]
for j in range(14):
 old=P[-1];new=[I(0) for _ in range(len(old)+1)]
 for k,c in enumerate(old):new[k]+=(I(4*k+1)/2)*c;new[k+1]-=2*c
 P.append(new);M.append(M[-1]*(I(4*j+17)/2))
def poly(p,w):
 a=I(0)
 for c in p[::-1]:a=a*w+c
 return a
# All enclosures also cover small outward x-box enlargement in [0,.7].
assert lo(pi*iv.exp(-I(7)/5))>0.75
for j in range(15):
 w=I(3)*17**2
 assert hi((I(18)/17)**(2*j+6)*iv.exp(-3*35))<.5
 assert hi(4*M[j]*w**(j+3)*iv.exp(-w))<1e-220
 w=I(3)/4*33**2
 assert hi((I(34)/33)**(2*j+7)*iv.exp(-I(3)/4*67))<.5
 assert hi(2*M[j]*33*w**(j+3)*iv.exp(-w))<1e-260

def rows(x,J=14):
 zz=pi*iv.exp(2*x);zr=pi*iv.exp(-2*x)
 ps=[I(0) for _ in range(J+1)];rr=[I(0) for _ in range(J+1)]
 for m in range(1,17):
  w=m*m*zz;e=iv.exp(-w)
  for j in range(J+1):ps[j]+=poly(P[j],w)*e
 for m in range(2,33):
  w=m*m*zr;e=iv.ln(m)*iv.exp(-w)
  for j in range(J+1):rr[j]+=poly(P[j],w)*e
 return [iv.exp(x/2)*v+I(['-1e-220','1e-220']) for v in ps],[iv.exp(-x/2)*v+I(['-1e-260','1e-260']) for v in rr]

def F_der(p,r,j,k):
 ans=I(0)
 for a in range(k+1):
  ans+=math.comb(k,a)*((-1)**a*r[a]*p[2*j+k-a]-p[a]*(-1)**(k-a)*r[2*j+k-a])
 return 2*ans

pb,rb=rows(b,6)
ends=[2*(rb[0]*pb[2*j]/pb[0]-rb[2*j]) for j in range(1,4)]
# Degree-seven midpoint Taylor integration, eighth-derivative remainder.
N=256;sums=[I(0),I(0),I(0)];err=[I(0),I(0),I(0)];t0=time.time()
for i in range(N):
 left=b*i/N;right=b*(i+1)/N;mid=(left+right)/2;length=right-left
 pp,rr=rows(mid,12)
 bb,cc=rows(I([max(0,lo(left)),hi(right)]),14)
 for jj in range(3):
  j=jj+1
  for k in [0,2,4,6]:sums[jj]+=F_der(pp,rr,j,k)*length**(k+1)/(2**k*math.factorial(k+1))
  err[jj]+=I(ab(F_der(bb,cc,j,8)))*length**9/(2**8*math.factorial(9))
 if i%64==0:print('boxes',i,'time',time.time()-t0,flush=True)
beta=[-s+I([-hi(e),hi(e)]) for s,e in zip(sums,err)]
# Exact endpoint primitive for U-tail; omitted m>=9 is analytically tiny.
u=I(0)
for m in range(1,9):
 w=4*pi*m*m;u+=2*w*(4*w-5)*iv.exp(-w)
# For w>=1, 2w(4w-5)e^-w<=8w²e^-w. w>=12m².
w=I(12)*9**2
assert hi((I(10)/9)**4*iv.exp(-12*19))<.5
assert hi(16*w*w*iv.exp(-w))<1e-300
u+=I([0,'1e-300'])
A00,A01=ends[1:];A10,A11=beta[1:];det=A00*A11-A01*A10
assert lo(det)>4e9

def solve(y0,y1):return [(A11*y0-A01*y1)/det,(-A10*y0+A00*y1)/det]
cU=solve(-iv.sqrt(2),-u);c1=solve(-ends[0],-beta[0])
result={'jet_definition':'t_j=psi^(2j)-4^(-j)psi; n_j=2W t_j','endpoint_n1_n2_n3':list(map(out,ends)),'tail_psi_moments_n1_n2_n3':list(map(out,beta)),'tail_U_psi':out(u),'determinant_n2_n3':out(det),'coefficient_U_plus_n2_n3':list(map(out,cU)),'coefficient_n1_plus_n2_n3':list(map(out,c1)),'head_moment_taylor_remainder_bounds':list(map(out,err)),'taylor_boxes':N}
Path(__file__).with_name('balanced_head_load_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));print('PASS',time.time()-t0)
