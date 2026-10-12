"""Interval parameter certificate for physical-first multiband kernel compression.
No true resolvent Gram entries or spectral sign are computed here.
"""
from pathlib import Path
import math,json,mpmath as mp
mp.mp.dps=80;iv=mp.iv;iv.dps=50;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
P=Path(__file__).resolve().parent;covers={z['N']:z for z in json.loads((P/'frequency_well_cover_certificate.json').read_text())['covers']}
PI=iv.pi;astar=4*PI**2*125/121;c0=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI)
def lam(n):
 for p in range(2,n+1):
  if all(p%q for q in range(2,math.isqrt(p)+1)):
   v=n
   while v%p==0:v//=p
   if v==1:return iv.ln(p)
 return I(0)
out=[]
for den,N in [(8,3),(64,3),(1024,4),(1048576,7)]:
 eps=I(1)/den;eta=eps/4
 tail=20*astar/9*(N+1)**2*iv.exp(-PI*(N+1));e=eps-tail
 assert lo(e)>lo(eps/2)
 c=c0+sum((2*lam(n)/iv.sqrt(n) for n in range(2,N+1)),I(0))
 re=max(1,int(mp.ceil(hi(iv.ln((2/PI)*iv.ln(astar/e))/2))))
 mu=int(mp.ceil(min(hi(astar*iv.exp(-PI)/e),1000*re*re)));M=iv.sqrt(mu)
 Rnum=0
 while True:
  R=I(Rnum)/100;mt=iv.sqrt(astar)*iv.exp(2*R-PI*iv.exp(2*R)/2)
  spatial=2*c*M*mt/iv.sqrt(e)
  if hi(spatial)<lo(eta/2):break
  Rnum+=1
 cover=covers[N]['positive_axis_cover_endpoints_over_8'];W=sum((I(b-a)/8 for a,b in cover),I(0))
 ztarget=eta/(6*iv.sqrt(c)*mu);assert hi(ztarget)<lo(iv.sqrt(c))
 target=ztarget/iv.sqrt(2*R/PI*c*W)
 degrees=[];zsq=I(0);rank=0
 for a,b in cover:
  width=I(b-a)/8;w=I(b)/8 if a==0 else I(b-a)/16
  n=2 if a==0 else 1;step=2 if a==0 else 1
  rem=lambda n:((R*w)**n)/math.factorial(n)
  while hi(rem(n))>=lo(target):n+=step
  rr=n//2 if a==0 else n;rank+=rr
  zsq+=2*R/PI*c*width*rem(n)**2
  degrees.append({'left_over_8':a,'right_over_8':b,'Taylor_remainder_order':n,'rank_upper':rr})
 z=iv.sqrt(zsq);freq=mu*(2*iv.sqrt(c)*z+z*z);total=spatial+freq
 assert hi(total)<lo(eta)
 out.append({'epsilon':f'1/{den}','eta':f'1/{4*den}','N':N,'sigma':'1/100','R':f'{Rnum}/100','M_squared_upper':mu,'positive_frequency_width':mp.nstr(hi(W),20),'number_of_positive_intervals':len(cover),'rank_upper':rank,'spatial_error_upper':mp.nstr(hi(spatial),30),'feature_HS_error_upper':mp.nstr(hi(z),30),'finite_kernel_error_upper':mp.nstr(hi(freq),30),'whole_operator_error_upper':mp.nstr(hi(total),30),'bands':degrees})
res={'status':'Outward full-norm parameter budgets only; no resolvent/inertia sign certificate','budgets':out};(P/'multiband_kernel_budgets.json').write_text(json.dumps(res,indent=2)+'\n')
for r in out:print(json.dumps({k:v for k,v in r.items() if k!='bands'}))
