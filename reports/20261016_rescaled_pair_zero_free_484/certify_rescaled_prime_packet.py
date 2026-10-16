from pathlib import Path
"""Rigorous strengthening of the BTY finite prime-power lower bound.
No zero-free region is claimed by this script alone.
Exact SymPy Sturm for degree6; Arb Fourier cover; outward mpmath weight intervals.
"""
import json,time
from flint import arb,ctx
ctx.prec=160
import sympy as sp
from mpmath import iv
iv.dps=60
x=sp.Symbol('x')
coeff=list(map(sp.Rational,json.load(open(Path(__file__).with_name('rescaled_packet.json')))['kappa']))
p=sum(n*x**j for j,n in enumerate(coeff))
assert sp.count_roots(p,0,1)==0 and p.subs(x,1)>0
assert sp.count_roots(sp.diff(p,x),0,1)==0 and sp.diff(p,x).subs(x,0)<0
print('Exact p positivity and decreasing certified',flush=True)
c=[4,-8,2,20,-9,-34,27,91,-27,-201,32,895,1949,2389,1896,949,239]
a=[sp.Rational(sum(v*v for v in c),14912370)]+[sp.Rational(2*sum(c[j]*c[j+k] for j in range(17-k)),14912370) for k in range(1,17)]
assert a[0]==1 and all(v>=0 for v in a)
th=iv.mpf(5669)/5000;S=1/iv.cos(th)**2;aa=th/iv.tan(th);bb=iv.tan(th);B=2/iv.tan(th)-1/iv.tan(2*th)
w0=S*(th*iv.tan(th)+3*th/iv.tan(th)-3)
eta=iv.mpf(7163)/1000000;dmin=iv.mpf(986935)/1000000
# Published admissible rectangle Amax=1/4.8594 lies inside these rational bounds.
Amax=iv.mpf(10000)/48594
assert (Amax/iv.ln(iv.mpf(3)*10**12)).b < eta.a
assert (1-2*Amax/iv.ln(iv.mpf(16)*3*10**12+10**10)).a > dmin.b

def w(u):return S*((S*aa-1)*iv.cos(bb*u)-S/2*u*iv.cos(bb*u)+B*iv.sin(bb*u)+2*aa-2-u)
lowers={2:sp.Rational(210,1000),3:sp.Rational(474,10000),5:sp.Rational(72,10000),7:sp.Rational(2,1000)}
weights={}
assert (eta*8*iv.ln(7)).b < (2*aa).a
for prime in lowers:
 wts=[]
 for m in range(1,9):
  u=m*iv.ln(prime);v=iv.exp(-dmin*u)
  z=iv.mpf(prime)**(-m)*w(eta*u)/w0*sum((iv.mpf(int(n.p))/int(n.q))*v**j for j,n in enumerate(coeff))
  # Floor decimal via exact integer from lower mpf; verify with interval order.
  n=int(float(z.a)*10**14)-2
  wt=sp.Rational(n,10**14)
  assert iv.mpf(n)/10**14 < z.a
  wts.append(wt)
 weights[str(prime)]=[str(v) for v in wts]
 poly=sp.Poly(sum(wts[m-1]*a[k]*sp.chebyshevt(m*k,x) for m in range(1,9) for k in range(17))-lowers[prime],x)
 # Fourier coefficients are exact rational sums; certify all real phases in [0,pi]
 bc=[sp.Rational(0) for _ in range(129)]
 for mm in range(1,9):
  for kk in range(17):bc[mm*kk]+=wts[mm-1]*a[kk]
 ac=[arb(int(v.p))/int(v.q) for v in bc]
 threshold=arb(int(lowers[prime].p))/int(lowers[prime].q)
 from fractions import Fraction
 stack=[(Fraction(0),Fraction(3142,1000),0)];cells=0;depthmax=0;st=time.time();lowest=None
 while stack:
  lo,hi,dep=stack.pop();mid=(lo+hi)/2;rad=(hi-lo)/2
  ph=arb(mid.numerator)/mid.denominator+arb(0,arb(rad.numerator)/rad.denominator)
  value=sum(ac[j]*(j*ph).cos() for j in range(129))
  if value>threshold:
   cells+=1;depthmax=max(depthmax,dep);continue
  assert dep<35,(prime,lo,hi,str(value))
  stack.append((lo,mid,dep+1));stack.append((mid,hi,dep+1))
 print('Prime',prime,'Arb lower',lowers[prime],'cells',cells,'maxdepth',depthmax,'seconds',round(time.time()-st,3),flush=True)
save=sum(iv.ln(pr)*iv.mpf(int(v.p))/int(v.q) for pr,v in lowers.items())
print('FOUR_PRIME_PACKET_LOWER',save,flush=True)
assert save.a>iv.mpf('.213').b
open(Path(__file__).with_name('rescaled_prime_packet_weights.json'),'w').write(json.dumps({'weights':weights,'minima':{str(k):str(v) for k,v in lowers.items()},'lower':'0.213','mmax':8,'eta_bar':'0.007163','d_bar':'0.986935'},indent=2))
print('CERTIFIED: prime sum >= 0.213 * eta * w(0) on original BTY rectangle',flush=True)
