#!/usr/bin/env python3
"""Finite jet certificate for the local partial-dual lemma; not a global zeta theorem."""
from fractions import Fraction as Q
from flint import arb,ctx
from math import factorial
import json
from pathlib import Path
ctx.prec=192
D=7
A=Q(1,2);B=Q(3,2)
EPS='0.000000000001'
def R(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def choose(q,n):
 v=Q(1)
 for j in range(n):v*=q-j
 return v/factorial(n)
def add(p,q):
 o=p.copy()
 for k,v in q.items():o[k]=o.get(k,arb(0))+v
 return o
def scale(p,c):return {k:v*c for k,v in p.items()}
def mul(p,q,n=D):
 o={}
 for (a,b),v in p.items():
  for (c,d),w in q.items():
   if a+b+c+d<=n:
    k=(a+c,b+d);o[k]=o.get(k,arb(0))+v*w
 return o
def compose(p,u,n):
 powers=[{(0,0):arb(1)}]
 for j in range(1,n+1):powers.append(mul(powers[-1],u,n))
 out={}
 for (i,j),v in p.items():
  if i+j>n:continue
  for (a,b),w in powers[j].items():
   if a+b+i<=n:out[(a+i,b)]=out.get((a+i,b),arb(0))+v*w
 return out
one={(0,0):arb(1)}
eps=arb(1,EPS)
f={(i,j):R(choose(-A,i)*choose(-B,j))*eps for i in range(D+2) for j in range(D+2-i)}
v={(i,j):-(j+1)*f[i,j+1]/R(B) for i in range(D+1) for j in range(D+1-i)}
u={}
for n in range(1,D+1):
 c=compose(v,u,n)
 for i in range(n+1):
  j=n-i;tar=v[0,0] if (i,j)==(0,1) else arb(0)
  u[i,j]=(tar-c.get((i,j),arb(0)))/v[0,1]

fcomp=compose(f,u,D)
prod=mul(add(one,{(0,1):arb(1)}),add(one,u))
psi=add(scale(fcomp,-1),scale(prod,-R(B)*v[0,0]))
rows=[]
for i in range(5):
 for j in range(4):
  if i+j>D:continue
  mod=-(1+B)*choose(-A/(B+1),i)*choose(B/(B+1),j)
  rel=psi[i,j]/R(mod)-1
  assert rel.abs_upper()<arb('0.0001')
  rows.append({'i':i,'j':j,'relative_error':str(rel)})
# Logarithmic boundary derivatives through four: b(X)=-f_Y(X,Y_end).
pb={(i,0):v[i,0]/v[0,0] for i in range(1,5)}
logp={}; power=one
for n in range(1,5):
 power=mul(power,pb,4)
 logp=add(logp,scale(power,R(Q((-1)**(n+1),n))))
log_bounds=[]
for n in range(1,5):
 val=logp.get((n,0),arb(0))*factorial(n)
 assert val.abs_upper()<arb(4)
 log_bounds.append(str(val))
# Stationary amplitude and both first partial derivatives/mixed derivative.
fyy={(i,j):(j+1)*(j+2)*f[i,j+2] for i in range(3) for j in range(3-i)}
yyc=compose(fyy,u,2)
wpert={k:z/yyc[0,0] for k,z in yyc.items() if k!=(0,0)}
wjet=one.copy();power=one
for n in range(1,3):
 power=mul(power,wpert,2)
 wjet=add(wjet,scale(power,R(choose(Q(-1,2),n))))
amp_bounds=[]
for k in [(1,0),(0,1),(1,1)]:
 val=wjet.get(k,arb(0))
 assert val.abs_upper()<arb(10)
 amp_bounds.append(str(val))
# All normalized terminal derivatives and opposite Hessian diagonals.
C=R(Q(5,2))*R(Q(1,8))**R(Q(2,5))*R(Q(3,2))**R(Q(-3,5))
alpha=R(Q(1,64)); delta=arb('1e-12'); err=arb('0.0002')
xx=C*alpha**R(Q(3,5))/5*R(Q(6,5))*R(Q(11,5))*arb(3)**R(Q(-16,5))*(1-err)-delta
nyy=C*alpha**R(Q(3,5))/5*R(Q(3,5))*R(Q(2,5))*arb(3)**R(Q(-6,5))*arb(2)**R(Q(-7,5))*(1-err)
assert xx>arb('1e-5') and nyy>arb('1e-5') and xx*nyy>arb('1e-12')
for i in range(4):
 for j in range(4):
  # Absolute upper: X>=1, V<=2, alpha<=1/8; use alpha<=1.
  val=C/5*abs(R(choose(Q(-6,5),i)))*factorial(i)*abs(R(choose(Q(3,5),j)))*factorial(j)*2*(1+err)+delta
  assert val<arb(100)
# Stationary Y in[1/2,4] for X in[1,3] and V in[1/64,1/4].
assert (R(Q(3,16))*arb(3)**R(Q(-1,2))/R(Q(1,4)))**R(Q(2,5))>arb('0.6')
assert (R(Q(3,16))/R(Q(1,64)))**R(Q(2,5))<arb(3)
# f_YY lower on the extension implies w<=100 N/sqrt(F).
fyylo=R(Q(15,32))*arb(3)**R(Q(-1,2))*arb(4)**R(Q(-7,2))*(1-arb(EPS))
assert fyylo>arb('0.0001')
output={'status':'PASS','precision_bits':192,'input_relative_epsilon':EPS,'output_relative_epsilon':'0.0001','K':10**12,'cutoff_delta':'1e-12','inverse_jets':rows,'log_boundary_derivatives':log_bounds,'amplitude_relative_derivatives':amp_bounds,'terminal_xx_lower':str(xx),'terminal_negative_yy_lower':str(nyy),'terminal_determinant_lower':str(xx*nyy),'stationary_fyy_lower':str(fyylo)}
Path(__file__).with_name('partial_dual_jets.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
print('PASS: partial dual jets, boundary twists, amplitude and Hessian')
