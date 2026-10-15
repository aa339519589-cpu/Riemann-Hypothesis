"""Direct outward interval mixed columns from the complete source cells.
All polynomial/kernel operations use directed binary64 intervals.
The full prefix/onset/far row is added as an explicitly bounded error.
"""
import os,json,math,argparse,time
import numpy as np
from mpmath import iv
import interval_array_kernel as a
iv.dps=60;BASE=os.path.dirname(__file__);K=64
C=json.load(open(os.path.join(BASE,'filtered_bessel_main_cells.json')))['cells']+json.load(open(os.path.join(BASE,'filtered_bessel_onset_cells.json')))['cells']
C.sort(key=lambda c:c['lo'][0]);B=a.LN2;PI=a.PI
WW=[]
for r in range(25):
 lo=[];hi=[]
 for k in range(K+1):
  v=iv.mpf(2)/(r+k+1) if (r+k)%2==0 else iv.mpf(0)
  p=a.ivpair(v);lo.append(p[0]);hi.append(p[1])
 WW.append(a.A([lo,hi]))
def source_poly(cell,l,h):
 z=a.div(a.add(l,h),a.I(2));hh=a.div(a.sub(h,l),a.I(2));delta=a.sub(z,a.A(cell['z']))
 pp=a.I(np.zeros(25));pl=pp[0].copy();ph=pp[1].copy()
 for r in range(24,-1,-1):
  old=(pl,ph);v=a.mul(delta,old);sh=(np.r_[0,pl[:-1]],np.r_[0,ph[:-1]])
  v=a.add(v,a.mul(hh,sh));pl=v[0].copy();ph=v[1].copy()
  v0=a.add((pl[0],ph[0]),a.A(cell['F_coefficients'][r]));pl[0]=v0[0];ph[0]=v0[1]
 V=a.I(np.zeros(K+1));pabs=0.
 for r in range(25):V=a.add(V,a.mul((pl[r],ph[r]),WW[r]));pabs=a.up(pabs+a.ab((pl[r],ph[r])))
 return z,hh,V,pabs

def phase(z,kind,omega,la,n):
 y=a.div(a.sub(a.log(z),a.log(PI)),a.I(2))
 if kind=='prime':return a.trig(a.mul(omega,a.sub(y,a.ivpair(iv.log(n)))))
 if kind=='gamma':
  e=a.exp(a.neg(a.mul(la,a.sub(y,B))));r=np.arange(200)
  fac=a.sub(a.I(1),a.I(np.ldexp(np.ones(200)*.5,-4*r)))
  return a.mul(e,fac),a.I(np.zeros(200))
 return a.exp(a.mul(a.I(n),a.sub(a.log(z),a.log(PI)))),a.I(np.zeros(1))

def integral(cell,l,h,ar,ai,kind,omega,la,n=0):
 amag=a.up(a.ab(ar)+a.ab(ai));hwidth=float(h[1]-l[0]);lowsum=float(h[0]+l[0]);pieces=max(1,math.ceil(float(np.max(amag))*hwidth/lowsum/4))
 shape=np.broadcast(ar[0],ai[0]).shape;rr=a.I(np.zeros(shape));ii=a.I(np.zeros(shape))
 for p in range(pieces):
  width=a.sub(h,l);ll=a.add(l,a.mul(width,a.ivpair(iv.mpf(p)/pieces)));hh=a.add(l,a.mul(width,a.ivpair(iv.mpf(p+1)/pieces)))
  z,rad,V,ps=source_poly(cell,ll,hh)
  if float(rad[0])<=0:
   assert kind=='prime'
   assert float(rad[1])<1e-12
   err=a.up(a.up(2*float(rad[1]))*1e-2)
   rr=a.inflate(rr,err);ii=a.inflate(ii,err);continue
  beta=a.div(rad,z);cc=(a.I(np.ones(shape)),a.I(np.zeros(shape)));ss=(a.mul(cc[0],(V[0][0],V[1][0])),a.I(np.zeros(shape)))
  for j in range(1,K+1):
   fac=(a.div(a.mul(a.sub(ar,a.I(j-1)),beta),a.I(j)),a.div(a.mul(ai,beta),a.I(j)))
   cc=a.cmul(cc,fac);vv=(V[0][j],V[1][j]);ss=a.cadd(ss,(a.mul(cc[0],vv),a.mul(cc[1],vv)))
  q=a.up(a.up(a.up(amag+K+1)*beta[1])/(K+2));q=np.maximum(q,beta[1]);assert np.all(q<1)
  nxt=a.up(a.cabs(cc)*a.up(a.up(a.up(amag+K)*beta[1])/(K+1)))
  tail=a.up(a.up(a.up(2*ps)*nxt)/a.dn(1-q))
  pref=phase(z,kind,omega,la,n);value=a.cmul(pref,ss)
  klog=a.up(a.up(amag*beta[1])/a.dn(1-beta[1]));assert np.all(klog<5)
  rmult=1 if kind=='prime' else (256 if kind=='gamma' else 2)
  # The exact cell remainder in F is integrated against the real-axis kernel.
  pe=a.cabs(pref);err=a.up(rad[1]*a.up(a.up(pe*tail)+a.up(a.up(a.up(2*cell['F_remainder_upper'])*rmult)*pe)))
  rr=a.add(rr,a.inflate(a.mul(rad,value[0]),err));ii=a.add(ii,a.inflate(a.mul(rad,value[1]),err))
 return rr,ii

def lam(n):
 for p in range(2,n+1):
  if n%p==0:
   q=n
   while q%p==0:q//=p
   return a.ivpair(iv.log(p)) if q==1 else a.I(0)
 return a.I(0)

def run(N):
 om=a.div(a.mul(a.I(np.arange(1,N+1)),PI),B);la=a.I(2*np.arange(200)+.5);sg=(-1.)**np.arange(1,N+1)
 Ar=a.I(np.zeros(200));prime=a.I(np.zeros(N));ell=a.I(np.zeros(1));start=time.time()
 for ci,cell in enumerate(C):
  l=a.A(cell['lo']);h=a.A(cell['hi'])
  v,_=integral(cell,l,h,a.div(a.neg(la),a.I(2)),a.I(np.zeros(200)),'gamma',om,la);Ar=a.add(Ar,v)
  for n in range(2,13):
   al=lam(n)
   if float(al[1])==0:continue
   al=a.div(al,a.ivpair(iv.sqrt(n)))
   pLo=a.div(a.mul(PI,a.I(n*n)),a.I(4));pHi=a.mul(PI,a.I(4*n*n))
   lo=(max(float(l[0]),float(pLo[0])),max(float(l[1]),float(pLo[1])));hi=(min(float(h[0]),float(pHi[0])),min(float(h[1]),float(pHi[1])))
   if hi[1]<=lo[0]:continue
   _,v=integral(cell,a.A(lo),a.A(hi),a.I(np.zeros(N)),a.div(om,a.I(2)),'prime',om,la,n)
   fac=a.mul(a.I(-2),a.mul(a.ivpair(iv.sqrt(2/iv.log(2))),al));prime=a.add(prime,a.mul(fac,v))
  for power,factor in [(.25,.5),(-.25,-.5)]:
   v,_=integral(cell,l,h,a.I(np.array([power])),a.I(np.zeros(1)),'pole',om,la,power);ell=a.add(ell,a.mul(a.I(factor),v))
  if ci%50==0:print('outward mixed cells',ci,'/',len(C),'seconds',round(time.time()-start,1),flush=True)
 gamma=a.I(np.zeros(N))
 for r in range(200):
  den=a.add(a.square(om),a.I((2*r+.5)**2));gamma=a.add(gamma,a.div((Ar[0][r],Ar[1][r]),den))
 gamma=a.mul(a.mul(a.I(2*sg),a.ivpair(iv.sqrt(2/iv.log(2)))),a.mul(om,gamma))
 sb=a.ivpair((iv.exp(iv.log(2)/2)-iv.exp(-iv.log(2)/2))/2)
 el=a.neg(a.div(a.mul(a.mul(a.I(sg),om),a.mul(a.ivpair(iv.sqrt(2/iv.log(2))),sb)),a.add(a.square(om),a.I(.25))))
 cols=a.sub(a.add(gamma,prime),a.mul(a.I(8),a.mul(ell,el)))
 # Prefix force L2 error <1e-14; omitted onset/far/r>=200 rows fit this bound too.
 cols=a.inflate(cols,1e-14)
 out={'scope':'direct outward mixed columns for true uncorrected Cphi tail','N':N,'mixed':[[float(x),float(y)] for x,y in zip(cols[0],cols[1])],'ell_main':[[float(x),float(y)] for x,y in zip(ell[0],ell[1])],'Ar':[[float(x),float(y)] for x,y in zip(Ar[0],Ar[1])]}
 json.dump(out,open(os.path.join(BASE,'filtered_mixed_columns_intervals.json'),'w'))
 print('SUCCESS direct outward columns',N,'low width',max(cols[1][:64]-cols[0][:64]),'allwidth',max(cols[1]-cols[0]),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--N',type=int,default=4096);args=p.parse_args();run(args.N)
