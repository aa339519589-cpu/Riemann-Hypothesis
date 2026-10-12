"""Rigorous interval cover of all positive frequencies of C_N-(99/100)b.
No spectral sign is claimed. Every excluded dyadic cell is interval-negative.
The infinite remainder is excluded by monotonicity of the complete b multiplier.
"""
from pathlib import Path
import mpmath as mp,json,time,hashlib
mp.mp.dps=80;iv=mp.iv;iv.dps=50;I=iv.mpf
lo=lambda z:mp.mpf(z._mpi_[0]);hi=lambda z:mp.mpf(z._mpi_[1])
def lam(n):
 for p in range(2,n+1):
  if all(p%q for q in range(2,int(p**.5)+1)):
   v=n
   while v%p==0:v//=p
   if v==1:return iv.ln(p)
 return I(0)
c0=iv.euler+iv.pi/2+3*iv.ln(2)+iv.ln(iv.pi)
def blower(t):
 t=I(t);y=t*t/4;A=I(129)/4
 return sum((y/((I(j)+I(1)/4)*((I(j)+I(1)/4)**2+y)) for j in range(32)),I(0))+iv.ln(1+y/(A*A))/2
out=[]
for N,top in [(3,128),(4,256),(7,4096)]:
 start=time.time();terms=[(2*lam(n)/iv.sqrt(n),iv.ln(n)) for n in range(2,N+1) if hi(lam(n))>0]
 cN=c0+sum((a for a,d in terms),I(0));assert lo(I(99)/100*blower(top)-cN)>0
 stack=[(0,8*top)];kept=[];excluded=0;calls=0;maxneg=None
 while stack:
  a,b=stack.pop();calls+=1
  q=c0+sum((v*iv.cos(d*I([str(mp.mpf(a)/8),str(mp.mpf(b)/8)])) for v,d in terms),I(0))-I(99)/100*blower(I(a)/8)
  if hi(q)<0:
   excluded+=1;maxneg=max(maxneg,hi(q)) if maxneg is not None else hi(q)
  elif b-a<=1:kept.append((a,b))
  else:
   mid=(a+b)//2;stack.extend([(mid,b),(a,mid)])
 merged=[]
 for a,b in sorted(kept):
  if merged and a==merged[-1][1]:merged[-1][1]=b
  else:merged.append([a,b])
 rec={'N':N,'sigma':'1/100','positive_axis_cover_endpoints_over_8':merged,'covered_width_over_8':sum(b-a for a,b in merged),'number_of_intervals':len(merged),'last_covered_endpoint_over_8':merged[-1][1],'infinite_tail_start':top,'infinite_tail_margin_lower':mp.nstr(lo(I(99)/100*blower(top)-cN),30),'certified_excluded_cells':excluded,'interval_checks':calls,'largest_negative_cell_upper':mp.nstr(maxneg,30),'elapsed_seconds':time.time()-start}
 out.append(rec);print(json.dumps(rec),flush=True)
p=Path(__file__).resolve().parent;(p/'frequency_well_cover_certificate.json').write_text(json.dumps({'status':'Actual frequency cover only; no resolvent/inertia sign','covers':out},indent=2)+'\n')
