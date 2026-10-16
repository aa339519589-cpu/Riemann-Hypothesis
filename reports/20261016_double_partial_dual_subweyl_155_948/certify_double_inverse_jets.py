#!/usr/bin/env python3
"""Finite interval certificate for the two-partial-dual local lemma only."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=192
def R(x):
 x=Q(x);return arb(x.numerator)/x.denominator
def choose(a,n):
 z=Q(1)
 for j in range(n):z*=a-j
 return z/factorial(n)
def add(p,q):
 z=p.copy()
 for k,v in q.items():z[k]=z.get(k,arb(0))+v
 return z
def scale(p,c):return {k:v*c for k,v in p.items()}
def mul(p,q,n):
 z={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():
   if i+j+k+l<=n:z[i+k,j+l]=z.get((i+k,j+l),arb(0))+v*w
 return z
def compose(p,u,n):
 powers=[{(0,0):arb(1)}]
 for k in range(1,n+1):powers.append(mul(powers[-1],u,n))
 z={}
 for (i,j),v in p.items():
  if i+j>n:continue
  for (k,l),w in powers[j].items():
   if k+l+i<=n:z[k+i,l]=z.get((k+i,l),arb(0))+v*w
 return z
one={(0,0):arb(1)}
def implicit_phase(ak,au,eps,D,sgn):
 # Known-coordinate exponent ak, inverted-coordinate exponent au.
 f={(i,j):R(choose(ak,i)*choose(au,j))*arb(1,eps) for i in range(D+2) for j in range(D+2-i)}
 v={(i,j):(j+1)*f[i,j+1]/R(au) for i in range(D+1) for j in range(D+1-i)}
 u={}
 for n in range(1,D+1):
  c=compose(v,u,n)
  for i in range(n+1):
   j=n-i;target=v[0,0] if (i,j)==(0,1) else arb(0)
   u[i,j]=(target-c.get((i,j),arb(0)))/v[0,1]
 prod=mul(add(one,{(0,1):arb(1)}),add(one,u),D)
 dual=scale(add(compose(f,u,D),scale(prod,-R(au)*v[0,0])),R(sgn))
 return f,v,u,dual
f,v,u,psi=implicit_phase(Q(-1,2),Q(-3,2),'1e-25',9,-1)
first=[]
for i in range(10):
 for j in range(10-i):
  model=-R(Q(5,2)*choose(Q(-1,5),i)*choose(Q(3,5),j))
  err=psi[i,j]/model-1;assert err.abs_upper()<arb('1e-14')
  first.append({'x_order':i,'nu_order':j,'relative_error':str(err)})
# Log of the first curved endpoint b(x)=-f_y(x,y_end).
p={(i,0):v[i,0]/v[0,0] for i in range(1,10)}
lg={};pw=one
for k in range(1,10):
 pw=mul(pw,p,9);lg=add(lg,scale(pw,R(Q((-1)**(k+1),k))))
logs=[]
for i in range(1,10):
 val=lg.get((i,0),arb(0))*factorial(i)
 assert val.abs_upper()<arb(10**6)
 logs.append(str(val))
# First amplitude w1=(f_yy)^(-1/2), after substitution.
def amp_jet(f,u):
 dd={(i,j):(j+1)*(j+2)*f[i,j+2] for i in range(3) for j in range(3-i)}
 base=compose(dd,u,2);p={k:z/base[0,0] for k,z in base.items() if k!=(0,0)}
 w=one.copy();pw=one
 for n in range(1,3):
  pw=mul(pw,p,2);w=add(w,scale(pw,R(choose(Q(-1,2),n))))
 vals=[w[k] for k in [(1,0),(0,1),(1,1)]]
 assert all(z.abs_upper()<arb(100) for z in vals)
 return [str(z) for z in vals]
amp1=amp_jet(f,u)
# The first dual plus its bounded-frequency twist enters as a fresh box.
g,v2,u2,theta=implicit_phase(Q(3,5),Q(-1,5),'1e-12',8,1)
second=[]
for i in range(4):
 for j in range(6):
  if i+j>8:continue
  model=R(Q(6,5)*choose(Q(1,2),i)*choose(Q(1,6),j))
  err=theta[i,j]/model-1;assert err.abs_upper()<arb('1e-4')
  second.append({'nu_order':i,'mu_order':j,'relative_error':str(err)})
amp2=amp_jet(g,u2)
C=R(Q(5,2))*R(Q(1,8))**R(Q(2,5))*R(Q(3,2))**R(Q(-3,5))
D=6*(C/5)**R(Q(5,6));delta=arb('1e-40')
# Extended first inverse: X in[1/16,32], V in[1/64,1/4].
ylo=(R(Q(3,16))*arb(32)**R(Q(-1,2))/R(Q(1,4)))**R(Q(2,5))
yhi=(R(Q(3,16))*R(Q(1,16))**R(Q(-1,2))/R(Q(1,64)))**R(Q(2,5))
assert ylo>R(Q(1,4)) and yhi<8
# The second stationary inverse covers all U in[1/256,1/7].
mu_left=C/5*R(Q(1,16))**R(Q(-6,5))*R(Q(1,64))**R(Q(3,5))
mu_right=C/5*arb(32)**R(Q(-6,5))*R(Q(1,4))**R(Q(3,5))
assert mu_left>R(Q(1,7)) and mu_right<R(Q(1,256))
# Original second-transform strip X in[1,2].
for k in [2,3]:
 lo=C*abs(R(choose(Q(-1,5),k)))*factorial(k)*arb(2)**R(Q(-1,5)-k)*R(Q(1,64))**R(Q(3,5))
 hi=C*abs(R(choose(Q(-1,5),k)))*factorial(k)*R(Q(1,4))**R(Q(3,5))
 assert lo>arb('0.0001') and hi<1
# All first-twist derivatives are smaller than the spare relative budget.
for i in range(10):
 for j in range(10-i):
  if not i+j:continue
  lower=C*arb(32)**R(Q(-1,5))*R(Q(1,64))**R(Q(3,5))*abs(R(choose(Q(-1,5),i)))*factorial(i)*abs(R(choose(Q(3,5),j)))*factorial(j)
  assert lower>arb('0.00001')
  assert delta*10**7/lower<arb('1e-20')
# Full second amplitude on its extended inverse domain.
psixxlo=C*R(Q(6,25))*arb(32)**R(Q(-11,5))*R(Q(1,64))**R(Q(3,5))*(1-arb('1e-12'))
assert psixxlo>arb('1e-6')
# Two mu-differences: model coefficient D*(5/36)*beta^(1/6)*alpha^(1/2).
c0=D*R(Q(5,36))*R(Q(1,256))**R(Q(1,6))*R(Q(1,64))**R(Q(1,2))
err=arb('0.0003')
xx=c0*R(Q(11,6))*R(Q(17,6))*arb(3)**R(Q(-23,6))*(1-err)-delta*1000
nyy=c0/4*arb(3)**R(Q(-11,6))*arb(2)**R(Q(-3,2))*(1-err)
assert xx>arb('1e-6') and nyy>arb('1e-6') and xx*nyy>arb('1e-12')
for i in range(4):
 for j in range(4):
  hi=D*R(Q(5,36))*abs(R(choose(Q(-11,6),i)))*factorial(i)*abs(R(choose(Q(1,2),j)))*factorial(j)*2*(1+err)+delta*1000
  assert hi<10000
out={'status':'PASS','precision_bits':192,'input_relative_error':'1e-25','first_output_relative_error':'1e-14','second_input_relative_error':'1e-12','second_output_relative_error':'1e-4','cutoff_delta':'1e-40','first_inverse':first,'first_log_boundary':logs,'first_amplitude':amp1,'second_inverse':second,'second_amplitude':amp2,'stationary_y_lower':str(ylo),'stationary_y_upper':str(yhi),'second_stationary_left':str(mu_left),'second_stationary_right':str(mu_right),'second_fxx_lower':str(psixxlo),'terminal_xx_lower':str(xx),'terminal_negative_yy_lower':str(nyy),'terminal_det_lower':str(xx*nyy)}
Path(__file__).with_name('double_inverse_jets.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS: two local inverse jets, two amplitudes, stationary domains and terminal Hessian')
