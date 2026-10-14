"""Outward certificate for V_Gamma >= -100 sqrt(W xi) on head.
All reported intervals must pass; no sampled or finite-matrix sign inference.
Uses the exact W cache of the independently maintained bulk certificate.
"""
import importlib.util,os,math,argparse
from mpmath import iv
BASE=os.path.dirname(__file__)
spec=importlib.util.spec_from_file_location('xi_bulk',os.path.join(BASE,'certify_xi_compact_bulk.py'))
bulk=importlib.util.module_from_spec(spec);spec.loader.exec_module(bulk)
iv.dps=30
b=iv.log(2)
def enc(v,side):return bulk.enclosed_float(v,side)
def xbounds(slo,shi):
 xx=b+iv.mpf([str(slo),str(shi)])
 return enc(xx,0),enc(xx,1)
def ps(slo,shi):
 if shi<=0:return iv.mpf(0)
 slo=max(0.,slo)
 val,der=bulk.psi_pair(slo,shi)
 if shi<=.01:
  _,dd=bulk.psi_pair(0.,shi)
  assert bool(dd.a>0)
  val=iv.mpf([str(slo),str(shi)])*dd
 return val

def score(slo,shi):
 assert slo>0
 val=ps(slo,shi)
 _,der=bulk.psi_pair(slo,shi)
 return der/val

def certify(slo,shi,ratio=1.08):
 ss=iv.mpf([str(slo),str(shi)]);yy=b+ss;z=4*iv.pi*iv.exp(2*ss)
 zu=enc(z,1)
 h0=math.nextafter(1e-6*min(slo,1/zu),0.)
 # Complete grouped tiny-h contribution >-.001; future h>=1 >-1e-8.
 lower=iv.mpf('-.00100001')
 pts=[h0];t=h0
 while t<1.:
  nt=min(1.,t*ratio if t<.1 else t+.01)
  for knot in [.02,slo/2,slo,shi,.5]:
   if t<knot<nt:nt=knot
  pts.append(nt);t=nt
 W=ps(slo,shi)/iv.sqrt(2)
 for aa,bb in zip(pts,pts[1:]):
  hh=iv.mpf([str(aa),str(bb)]);kap=iv.exp(-hh/2)/(-iv.expm1(-2*hh))
  Ar=bulk.rat(z,hh)
  if bb<=.02:
   sf=score(slo,shi+bb)
   wf=iv.exp(-sf*hh)
  else:
   lo,hi=xbounds(slo+aa,shi+bb)
   wf=W/bulk.query(lo,hi)
  out=Ar-iv.sqrt(Ar*wf)
  if aa<shi:
   if bb<=min(.02,slo/2):
    sb=score(slo-bb,shi)
    inc=iv.exp(-sb*hh)
   else:
    inc=ps(slo-bb,shi-aa)/(iv.sqrt(2)*W)
   back=bulk.rat(z,hh,False)
   out+=inc-iv.sqrt(inc*back)
  lower+=(iv.mpf(str(bb))-iv.mpf(str(aa)))*kap*out
 vg=2*lower
 mass=W*iv.exp(yy/2)*bulk.c(z)*iv.exp(-z)
 ans=vg+100*iv.sqrt(mass)
 return enc(ans,0),enc(vg,0),len(pts)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--ratio',type=float,default=1.08);args=ap.parse_args()
 if args.pilot:
  for lo,hi in [(5e-7,6e-7),(1e-5,1.2e-5),(.0001,.00012),(.001,.0012),(.005,.006),(.02,.022),(.06,.062),(.15,.152),(.30,.302),(.308,.31)]:
   print('pilot',lo,hi,certify(lo,hi,args.ratio),flush=True)
 else:
  count=0;best=(1e100,0.);leaves=[]
  def check(lo,hi,depth=0):
   global count,best
   v,vg,n=certify(lo,hi,args.ratio)
   if v<0:
    if depth>20:raise RuntimeError(('UNRESOLVED',lo,hi,v,vg,n))
    mid=(lo+hi)/2
    check(lo,mid,depth+1);check(mid,hi,depth+1);return
   count+=1;leaves.append([lo,hi,v,vg])
   if v<best[0]:best=(v,lo)
   if count%10==0:print('passed',count,lo,best,flush=True)
  lo=5e-7
  while lo<.31:
   hi=min(.31,lo*1.5 if lo<.005 else lo+.01)
   check(lo,hi);lo=hi
  import json
  json.dump({'range':[5e-7,.31],'ratio':args.ratio,'leaves':leaves},open(os.path.join(BASE,'xi_lyapunov_head_certificate.json'),'w'))
  print('CERTIFIED head scalar on [5e-7,.31]',count,best,flush=True)
