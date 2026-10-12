"""Outward interval global-even-polynomial parameter budgets only; this does not compute a resolvent Gram.
The exact rational inputs and all asserted tail inequalities are checked in iv.
"""
import json, math
import mpmath as mp
mp.mp.dps=60
iv=mp.iv;iv.dps=45;I=iv.mpf
lo=lambda x:mp.mpf(x._mpi_[0]); hi=lambda x:mp.mpf(x._mpi_[1])
PI=iv.pi;A=4*PI**2*125/121
C0=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI)

def lam(n):
 for p in range(2,n+1):
  if all(p%q for q in range(2,math.isqrt(p)+1)):
   m=n
   while m%p==0:m//=p
   if m==1:return iv.ln(p)
 return I(0)

def b_lower(t,J=32):
 u=I(t)/2
 return sum((u*u/((I(j)+I(1)/4)*((I(j)+I(1)/4)**2+u*u)) for j in range(J)),I(0))+iv.ln(1+(u/(I(J)+I(1)/4))**2)/2

def run(den):
 eps=I(1)/den;eta=eps/4
 N=2
 while not hi(20*A/9*(N+1)**2*iv.exp(-PI*(N+1)))<=lo(eps/2):N+=1
 delta=20*A/9*(N+1)**2*iv.exp(-PI*(N+1));e=eps-delta
 c=C0+2*sum((lam(n)/iv.sqrt(n) for n in range(2,N+1)),I(0))
 candidates=[]
 for sd in [100,50,20,10,5,2]:
  sig=I(1)/sd
  re=max(1,int(mp.ceil(hi(iv.ln((2/PI)*iv.ln(A/e))/2))))
  m2a=A*iv.exp(-PI)/e;m2b=10*sd*I(re)**2
  mu=int(mp.ceil(min(hi(m2a),hi(m2b))))
  M=iv.sqrt(mu)
  k=max(1,int(mp.ceil(hi(iv.ln(12*c*mu/(PI*eta))/iv.ln(2)))))
  pp=max(1,int(mp.ceil(hi(iv.ln(6*c*mu/eta)/iv.ln(2)))))
  # Integer T, exact partial Gamma series plus its positive integral tail.
  left=max(1,4*k);right=left
  while lo(b_lower(right))<hi(c/(1-sig)):right*=2
  while left<right:
   mid=(left+right)//2
   if lo(b_lower(mid))>=hi(c/(1-sig)):right=mid
   else:left=mid+1
  T=left
  r0num=0
  while True:
   r0=I(r0num)/100
   mt=iv.sqrt(A)*iv.exp(2*r0-PI*iv.exp(2*r0)/2)
   if hi(mt)<=lo(eta*iv.sqrt(e)/(6*c*M)):break
   r0num+=1
  R=I(r0num)/100+1;n=int(mp.ceil(hi(4*R*T)))
  leak=2/(PI*k)*(I(2*k)/T)**k
  H=2*T*R
  def beta_at(q): return iv.exp(2*q*iv.ln(H)-iv.loggamma(I(2*q+1)))
  qlo=max(1,int(mp.ceil(hi(H)/2))); qhi=qlo
  while hi(beta_at(qhi))>lo(eta/(6*c*mu)): qhi*=2
  while qlo<qhi:
   qm=(qlo+qhi)//2
   if hi(beta_at(qm))<=lo(eta/(6*c*mu)): qhi=qm
   else:qlo=qm+1
  q=qlo;beta=beta_at(q);poly=beta
  tail=2*c*M*(mt/iv.sqrt(e)+leak*M+poly*M)
  assert lo(e)>=hi(eps/2)
  assert lo(b_lower(T))>=hi(c/(1-sig))
  assert T>=4*k and n>=hi(4*R*T)
  assert hi(tail)<lo(eta)
  candidates.append(dict(sigma=f'1/{sd}',N=N,e_lower=mp.nstr(lo(e),20),cN_upper=mp.nstr(hi(c),20),M2_upper_integer=mu,R0=f'{r0num}/100',T=T,window_order=k,cell_count=1,degree=2*q-2,rank=q,factorial_remainder_upper=mp.nstr(hi(beta),20),eta=f'1/{4*den}',tail_upper=mp.nstr(hi(tail),20),bT_lower=mp.nstr(lo(b_lower(T)),20)))
 best=min(candidates,key=lambda z:z['rank'])
 best['epsilon']=f'1/{den}'
 best['dense_symmetric_gram_entries']=best['rank']*(best['rank']+1)//2
 best['dense_float64_bytes_unpacked']=8*best['rank']**2
 return best
result={'status':'Certified parameter inequalities only. No Gram entries, inertia, or new spectral gap are certified.','arithmetic':'mpmath.iv, 45 decimal digits; exact rational parameters; Gamma series 32 terms plus lower integral tail','budgets':[run(d) for d in [8,64,1024,1048576]]}
print(json.dumps(result,indent=2))
