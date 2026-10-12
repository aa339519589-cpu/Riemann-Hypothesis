"""Directed-interval scalar certificate for a bounded positive factor.
This certifies only explicitly printed inequalities when they pass. It does NOT
certify Arem>=B, original H positivity, or any new zero exclusion.
"""
import os,json,time,hashlib,math
from pathlib import Path
from fractions import Fraction
from mpmath import iv
iv.dps=int(os.getenv('CERT_DPS','35'))
D=int(os.getenv('CERT_BOX_DENOM','4096'));scale=10**12
err=iv.mpf(2)**-40
pi=iv.pi

def frac_tuple(t):
 sign,man,exp,bc=t
 return Fraction((-1 if sign else 1)*man)*(Fraction(2)**exp)
def endpoints(x):return tuple(frac_tuple(t) for t in x._mpi_)
def lo(x):return endpoints(x)[0]
def hi(x):return endpoints(x)[1]
def ivq(q):return iv.mpf(q.numerator)/q.denominator
def iabs(x):
 a,b=endpoints(x)
 if a>=0:return x
 if b<=0:return -x
 z=ivq(max(-a,b));return iv.mpf([0,z.b])
def phi3(x):
 e=iv.exp(2*x);r=iv.mpf(0)
 for n in (1,2,3):
  z=pi*n*n*e;r+=(4*z*z-6*z)*iv.exp(x/2-z)
 return r+iv.mpf([0,err.b])
def theta3(x):
 return iv.exp(x/2)*sum(iv.exp(-pi*n*n*iv.exp(2*x)) for n in (1,2,3))+iv.mpf([0,err.b])
def prime_power(n):
 for p in range(2,math.isqrt(n)+1):
  if n%p==0:
   v=n
   while v%p==0:v//=p
   return p if v==1 else 0
 return n
rows=[]
for n in range(2,128):
 p=prime_power(n)
 if p:rows.append((n,iv.log(p)/iv.sqrt(n),iv.log(n)))
def box(j):
 x=iv.mpf([iv.mpf(j)/D,iv.mpf(j+1)/D]);den=iv.exp(x/2)+iv.exp(-x/2)
 pp=sum(a*(phi3(x+d)+phi3(iabs(x-d))) for n,a,d in rows)+iv.mpf([0,(iv.mpf(2)**-100).b])
 jp=iv.mpf('.5')*iv.exp(-x/2)-theta3(x)
 db=iv.mpf('.5')-(pp+jp)/den
 if lo(db)<=0:raise ArithmeticError(('nonpositive box lower',j,str(db)))
 w2=phi3(x)/(den*db)
 # Integer outward enclosures, hence all cached bounds are exact rationals.
 low=(lo(db)*scale).__floor__();upp=(hi(w2)*scale).__ceil__()
 return low,upp
if os.getenv('CERT_TEST_ONLY'):
 print([(j,box(j)) for j in [0,int(.35*D),int(.55*D),int(.7*D),D,int(1.5*D),2*D-1]])
 raise SystemExit
start=time.time();lower=[];upper=[]
for j in range(2*D):
 a,b=box(j);lower.append(a);upper.append(b)
 if j%512==0:print('box',j,'of',2*D,flush=True)
# Full [-2,2] boxes, x=j/D; even reflection preserves upper values.
full=upper[::-1]+upper
terms=[];total=iv.mpf(0)
for n,a,d in rows:
 if n>=55:continue
 dl,du=endpoints(d);k0=(dl*D).__floor__();k1=(du*D).__floor__()
 best=0
 for j,v in enumerate(full):
  for k in range(k0,k1+2):
   jj=j+k
   if 0<=jj<len(full):best=max(best,v*full[jj])
 # One argument outside [-2,2] has W<2^-80 by the analytic exterior bound;
 # compact W^2 upper is required below to be <2, so product <2^-79.
 c=2*a*(iv.sqrt(iv.mpf(best))/scale+iv.mpf(2)**-79)
 total+=c;terms.append({'n':n,'upper_decimal':str(c.b),'upper_dyadic':str(hi(c))})
# The full n>=55 prime-power sum is paid by the analytic theta/exterior bound.
total+=iv.mpf(2)**-70
checks={'exp4_below55':hi(iv.exp(4))<55,'theta_envelope_below41':hi(4*pi*pi*125/121)<41,'e3_above20':lo(iv.exp(3))>20,'all_D_boxes_positive':min(lower)>0,'compact_W2_below_2':max(upper)<2*scale,'relative_shift_sum_below_4_5':hi(total)<Fraction(4,5)}
result={'scope':'Only scalar D_B positivity and the sufficient full-prime relative bound; no Arem>=B statement','precision':iv.dps,'box_denom':D,'boxes':len(upper),'D_lower_scaled_min':min(lower),'W2_upper_scaled_max':max(upper),'scale':scale,'relative_sum_interval':str(total),'relative_sum_upper_exact':str(hi(total)),'terms':terms,'checks':checks,'all_pass':all(checks.values())}
out=Path(__file__).with_name('bounded_factor_interval_result.json');out.write_text(json.dumps(result,indent=2)+'\n')
cache=out.with_name('bounded_factor_interval_boxes.json');cache.write_text(json.dumps({'denom':D,'scale':scale,'D_lower':lower,'W2_upper':upper})+'\n')
print(json.dumps(result,indent=2),flush=True)
