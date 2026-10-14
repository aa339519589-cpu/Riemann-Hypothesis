"""Outward interval certificate for V1 on [1.003,3].
Exact integer W row; all omitted theta labels bounded. No sampled sign.
All inequalities are certified for entire interval boxes, not sampled points.
"""
from mpmath import iv
from fractions import Fraction
import math,json,os,time,bisect
import numpy as np
iv.dps=25
BASE=os.path.dirname(__file__)
CACHE=os.path.join(BASE,'xi_compact_interval_cache_v2.json')
S=1000; K0=690; K1=3510
TAIL=iv.mpf(['-1e-65','1e-65'])
P=[iv.mpf(x) for x in [0,15,-30,8]]
P1=[iv.mpf(x) for x in [0,37.5,-165,112,-16]]
# P1 is generated below, avoiding handwritten coefficient assumptions.
p=[Fraction(0),Fraction(15),Fraction(-30),Fraction(8)]
p1=[Fraction(0)]*5
for k,v in enumerate(p):p1[k]+=(Fraction(1,2)+2*k)*v;p1[k+1]-=2*v
P1=[iv.mpf(c.numerator)/c.denominator for c in p1]
for pp in [p,p1]:
 d=len(pp)-1;C=sum(abs(a) for a in pp)
 assert Fraction(4)*C*3**d*9**(2*d)/20**81 < Fraction(1,10**65)
# Uniform omitted outgoing square-root tail after h=1/2.
zz=iv.pi*iv.exp(2*iv.mpf('1.003'));qq=16*iv.exp(-2*iv.mpf('1.003'))
assert bool(zz.a>23)
assert bool(((1+qq)/(1-qq/iv.e)).b<16)
assert bool((5*iv.exp(-zz*(iv.e-1)/2)*(2*iv.e/zz+4/zz**2)).b<iv.mpf('1e-7'))

def ev(p,w):
 a=iv.mpf(0)
 for c in reversed(p):a=a*w+c
 return a

def enclosed_float(v,side):
 raw=float(v.a if side==0 else v.b)
 out=raw
 for _ in range(100):
  out=math.nextafter(out,-math.inf if side==0 else math.inf)
  test=iv.mpf(str(out))
  ok=bool(test.a<=v.a) if side==0 else bool(test.b>=v.b)
  if ok:return out
 raise RuntimeError(('conversion enclosure',v,side,raw,out))

def psi_pair(lo,hi):
 if hi<=0:return iv.mpf(0),iv.mpf(0)
 cross=lo<0;lo=max(lo,0.)
 t=iv.mpf([str(lo),str(hi)]);z=iv.pi*iv.exp(2*t)
 out=iv.mpf(0);der=iv.mpf(0)
 for n in range(1,9):
  w=n*n*z;ee=iv.exp(-w);out+=ev(P,w)*ee;der+=ev(P1,w)*ee
 out=iv.exp(t/2)*out+TAIL;der=iv.exp(t/2)*der+TAIL
 ol=max(0.,enclosed_float(out,0));ou=enclosed_float(out,1)
 dl=enclosed_float(der,0);du=enclosed_float(der,1)
 if cross:ol=0.;dl=min(dl,0.);du=max(du,0.)
 return iv.mpf([str(ol),str(ou)]),iv.mpf([str(dl),str(du)])

def raw_rows(xlo,xhi,need_d=False):
 W=iv.mpf(0);D=iv.mpf(0);Lm=iv.mpf(0)
 NN=int(math.ceil(math.exp(xhi)))+1
 for n in range(2,NN+1):
  ln=iv.log(n);tt=iv.mpf([str(xlo),str(xhi)])-ln
  lo=enclosed_float(tt,0);hi=enclosed_float(tt,1)
  q,qp=psi_pair(lo,hi);q/=iv.sqrt(n);W+=q;D+=qp/iv.sqrt(n)
  fac=n;prime=None
  for k in range(2,int(math.sqrt(n))+1):
   if fac%k==0:
    while fac%k==0:fac//=k
    if fac==1:prime=k
    break
  if prime is None and all(n%k for k in range(2,int(math.sqrt(n))+1)):prime=n
  coef=iv.log(iv.mpf(n)/(prime if prime else 1))
  Lm+=coef*q
 return W,D,Lm

if os.environ.get('XI_BULK_REUSE_CACHE')=='1' and os.path.exists(CACHE):
 data=json.load(open(CACHE))
 assert data['grid']==[S,K0,K1]
 rows=np.array(data['rows'])
else:
 rows=[]
 for k in range(K0,K1):
  W,D,_=raw_rows(k/S,(k+1)/S)
  wl=enclosed_float(W,0);wu=enclosed_float(W,1)
  if wl>0:
   score=D/W;sl=enclosed_float(score,0);su=enclosed_float(score,1)
  else:sl=-1e300;su=1e300
  rows.append([wl,wu,sl,su])
  if k%200==0:print('cache',k,flush=True)
 json.dump({'grid':[S,K0,K1],'rows':rows},open(CACHE,'w'))
 rows=np.array(rows)
# Exact range minima/maxima of enclosures; sparse tables use no arithmetic.
mins=[rows[:,[0,2]]];maxs=[rows[:,[1,3]]]
j=1
while (1<<j)<=len(rows):
 h=1<<(j-1);mins.append(np.minimum(mins[-1][:-h],mins[-1][h:]));maxs.append(np.maximum(maxs[-1][:-h],maxs[-1][h:]));j+=1

def query(lo,hi,score=False):
 if hi<=math.log(2)-1e-15 and not score:return iv.mpf(0)
 l=max(K0,int(math.floor(lo*S))-1)-K0
 r=min(K1,int(math.floor(hi*S))+2)-K0
 if r<=l:return iv.mpf(0)
 j=(r-l).bit_length()-1;h=1<<j;col=1 if score else 0
 low=min(mins[j][l,col],mins[j][r-h,col]);up=max(maxs[j][l,col],maxs[j][r-h,col])
 if lo<K0/S:
  if score:raise ValueError('score below grid')
  low=0.
 return iv.mpf([str(low if score else max(0.,low)),str(up)])
# Uniform score bound for the discarded tiny Gamma interval.
assert bool(query(1.,3.01,True).a>-20) and bool(query(1.,3.01,True).b<20)

def c(w):return w*(8*w*w-30*w+15)
def rat(z,h,forward=True):
 if forward:
  zz=z*iv.exp(2*h)
  return iv.exp(h/2)*c(zz)/c(z)*iv.exp(-z*iv.expm1(2*h))
 zz=z*iv.exp(-2*h)
 return iv.exp(h/2)*c(z)/c(zz)*iv.exp(z*iv.expm1(-2*h))

def certify(lo,hi,ratio=1.04):
 y=iv.mpf([str(lo),str(hi)]);z=iv.pi*iv.exp(2*y)
 zu=enclosed_float(z,1);h0=math.nextafter(.999e-5/zu,0.)
 assert bool(100*iv.mpf(str(zu))*iv.mpf(str(h0))<=iv.mpf('.001'))
 # Each discarded grouped ratio is bounded by 100 z_upper h,
 # using |W'/W|<20 and |xi'/xi|<3z_upper locally.
 lower=iv.mpf('-.0010001')
 top=max(.5,hi-math.log(2)+1e-12)
 pts=[h0];t=h0
 while t<top:
  nt=min(top,t*ratio if t<.1 else t+.01)
  if t<.02<nt:nt=.02
  if t<.5<nt:nt=.5
  pts.append(nt);t=nt
 Wy=query(lo,hi)
 for a,b in zip(pts,pts[1:]):
  h=iv.mpf([str(a),str(b)]);kap=iv.exp(-h/2)/(-iv.expm1(-2*h))
  out=iv.mpf(0)
  if a<.5:
   Ar=rat(z,h)
   if b<=.02:
    sf=query(lo,hi+b,True)
    wf=iv.exp(-sf*h)
   else:wf=Wy/query(lo+a,hi+b)
   out=Ar-iv.sqrt(Ar*wf)
  if hi-a>math.log(2)-1e-15:
   if b<=.02:
    sb=query(lo-b,hi,True);inc=iv.exp(-sb*h)
   else:inc=query(lo-b,hi-a)/Wy
   back=rat(z,h,False)
   out+=inc-iv.sqrt(inc*back)
  val=kap*out
  lower+=(iv.mpf(str(b))-iv.mpf(str(a)))*val
 _,_,Lm=raw_rows(lo,hi)
 vg=iv.mpf(str(enclosed_float(2*lower,0))); debit=2*Lm/Wy
 # Only the lower endpoint is used: the omitted outgoing tail was bounded
 # from below, so its artificial upper endpoint is not a V_Gamma enclosure.
 rho=iv.mpf('1e-6')/(iv.sqrt(Wy*iv.exp(y/2)*c(z)*iv.exp(-z))+iv.mpf('1e-6'))
 target=rho*vg-debit
 return enclosed_float(target,0),len(pts),enclosed_float(vg-debit,0)

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--step',type=float,default=.002);args=ap.parse_args()
 if args.pilot:
  for lo in [1.003,1.05,1.1,1.25,1.4,1.8,2.5,2.998]:print('pilot',lo,certify(lo,lo+.002),flush=True)
 else:
  lo=1.003;best=(100.,0);count=0
  while lo<3:
   hi=min(3.,lo+args.step);val,n,v1=certify(lo,hi)
   if val<1e-5:raise RuntimeError(('UNRESOLVED',lo,hi,val,n))
   if val<best[0]:best=(val,lo)
   count+=1
   if count%50==0:print('passed',count,lo,'min',best,flush=True)
   lo=hi
  print('CERTIFIED rho VΓ−2(L−WΛ)/W>1e-5 on [1.003,3]',count,best,flush=True)
