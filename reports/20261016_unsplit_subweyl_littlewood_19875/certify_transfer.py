"""Finite continuum certificate for the displayed Yang local-inequality witnesses.
No assertion of analytic transfer is made by this program alone.
"""
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import json,hashlib,time,math
from flint import arb,ctx
ctx.prec=160;ctx.threads=1

def B(q):
 q=Q(q);return arb(q.numerator)/q.denominator

def ball(l,r):return B((l+r)/2)+arb(0,B((r-l)/2))
D=B(46);bp=B('3.574410');b1p=B('1.747088');M=B(Q(1,Q('19.875')));eps=B('1e-20')
# Robust fixed-detector theta bracket, allowing far more rounding than
# the fourteen-decimal published b1 value. No new detector is introduced.
b1_source=ball(Q('1.74708'),Q('1.74710'))
tlo=B('1.1326');thi=B('1.1328')
assert tlo.sin()**2-b1_source*(1-tlo/tlo.tan())>0
assert thi.sin()**2-b1_source*(1-thi/thi.tan())<0
th=ball(Q('1.1326'),Q('1.1328'))
w0=(th*th.tan()+3*th/th.tan()-3)/th.cos()**2
c0=1/(th.sin()*th.cos()**3);c1=(th-th.sin()*th.cos())*th.tan()**4;c2=th.tan()**3*th.sin()**2;c3=(th-th.sin()*th.cos())*th.tan()**2
# For R>=100, write q=1/R. Every factor of (c(R)-1)R is
# nonnegative and increasing in q. Evaluate at q=1/100.
q=B('1/100')
c_cap=1+c0/w0*(1+q)**2/(1-th.tan()**2*q*q)**2*(c2*(q*q+q**3)*((2*th/th.tan()).exp()+1)+c1*q*q+c3)
assert c_cap<B('10.05')
def c(R):return 1+B('10.05')/R


# Exact coefficients from the independently certified unsplit-PY finite table.
table_A=['29.83', '30.90', '31.81', '32.60', '33.42', '34.08', '34.88', '35.57', '36.16', '36.75', '37.35', '37.91', '38.52', '39.02', '39.56', '40.06', '40.54', '41.03', '41.48', '41.89', '42.39', '42.79', '43.16', '43.56', '43.97', '44.35', '44.73', '45.14', '45.51', '45.83', '46.17', '46.49']
assert all(Q(a)<Q(b) for a,b in zip(table_A,table_A[1:]))
choices=[('direct_table',str(Q(i,100))) for i in range(50,28,-1)]+[('k',str(k)) for k in range(4,15)]
@lru_cache(None)
def static(mode,param):
 k=int(param) if mode=='k' else None
 eta=B(Q(k,2**k-2)) if k else B(param)
 return k,eta,(1+eta).zeta().log()

def margin(l,r,choice):
 x=ball(l,r);mode,param=choice;k,eta,zlog=static(mode,param)
 L1=x+(D+(-x).exp()).log();L2=L1.log();lam=M*L2/L1;om=(1+eps)*M*x.log()/x
 R=math.floor(float((eta/lam-1).lower()))
 if R<100:return None,False,R
 left=B('.17996')-B('.20523')*((1+eps)*(x.log()/x)/(L2/L1)-1)
 if k:
  main_bracket=(L1-B('3.377'))/(2**k-2)+L2+B('1.546').log()
  main=(bp*main_bracket+zlog)/(2*eta)
  tail_bracket=(B('23.99')/eta.sqrt()-B('40.051'))*(L1-B('3.377'))+B('1.2031')*L2-B('38.58')+(B('2.0373')*L2-B('.5322')*eta.log())/eta**2
  tail=bp*tail_bracket+B('1.8')
 else:
  assert mode=='direct_table'
  if r>215:return None,False,R
  top=B(r)+B(46).log()+B('1e-20')
  j=0
  while j<32 and not top<B(65+5*j):j+=1
  if j>=32:return None,False,R
  assert top<B(220)
  aa=(14*eta-4)/3;bb=1-aa;avg=L1-B('3.377')
  main_bracket=aa*(B('27/164')*avg+B(table_A[j]).log())+bb*(avg/14+avg.log()+B('1.546').log())+B('1e-20')
  main=(bp*main_bracket+zlog)/(2*eta)
  nu=(eta**-2+(1-eta)**-2)/2
  tail_bracket=(B('.891')+B('.6079')*nu)*(L1-B('3.377'))+(B('.7813')+B('.58')*nu)*L2+B('7.329')+B('3.898')*nu
  tail=bp*tail_bracket+B('1.8')
 valid=om<=eta/2 and lam*(R+1)<=eta and main_bracket>0 and tail_bracket>0
 rhs=lam*(B('.087')*arb.pi()**2*b1p*om/eta**2+main+c(R)*lam*tail)
 return left-rhs,valid,R

# Local finite strip: width 3/14, midpoint 17/28, horizontal half-height 1000.
# Every central integral ordinate is within 32 of its harmonic center.
a=7*arb.pi()/3
assert B(100)/arb.pi()<32
assert B(63).exp()-1000>B(60).exp()
assert B(6).log()+(1+B(46)*B(215).exp()+1000).log()<223
barrier_debit=2*B(2).sqrt()*223*(-968*a).exp()
assert barrier_debit<B('1e-1000')
# Complete integral: |u|<=100, shift 2*eta*|u|/pi<32.
# Logarithmic center error plus the COMPLETE global-Euler tail fits 1e-20.
assert B(100)/arb.pi()<1000
assert B(63).exp()-1000>B(60).exp()
assert 1+B(46)*B(215).exp()<B(220).exp()
log_debit=-(1-B(1000)*B(-63).exp()).log()
# The critical linear boundary has derivative less than one.
assert B('27/164')<1
assert log_debit<B('1e-22')
# log|zeta(.5+iy)|<=log4+log(1+|y|); tail <=4 int_100^infty e^-2u(223+u)du.
tail_debit=2*B(-200).exp()*B('323.5')
assert tail_debit<B('1e-80')
assert B('1/14')+B(60)**-1<1
assert log_debit+tail_debit+barrier_debit<B('1e-20')

# Proof splice checks in x=log(t).
assert B('4.79')*B(63).log()<B('19.875')
assert (B(10**6)/(B(10**6).log()**4))>(B('55.241')/B('19.875'))**3
# x/(log x)^4 is increasing for x>e^4.
assert B(10**6).log()>4
edges=[63,100,125,150,200,300,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000]
stack=[(Q(a),Q(b),0) for a,b in reversed(list(zip(edges,edges[1:])))];accepted=[];evals=0;fails=[];start=time.time()
while stack:
 l,r,dep=stack.pop();mid=(l+r)/2
 scores=[]
 for choice in choices:
  v,valid,R=margin(mid,mid,choice)
  if v is not None:scores.append((float(v.mid()),choice))
 choice=max(scores)[1]
 v,valid,R=margin(l,r,choice);evals+=1
 if valid and v>0:
  accepted.append({'left':str(l),'right':str(r),'mode':choice[0],'parameter':choice[1],'R':R,'margin_lower':str(v.lower())});continue
 if dep>=28:
  fails.append({'left':str(l),'right':str(r),'margin':str(v),'valid':valid});break
 stack.extend([(mid,r,dep+1),(l,mid,dep+1)])
 if evals%1000==0:print(evals,len(accepted),time.time()-start,flush=True)
out={'status':'PASS' if not fails and not stack else 'FAIL','scope':'finite scalar witnesses and splice inequalities; analytic proof separate','target':'19.875','precision_bits':160,'x_range':['63','1000000'],'near_minimum_relative_slack':'1e-20','b_upper':'3.574410','b1_upper':'1.747088','theta_enclosure':['1.1326','1.1328'],'c_bound':'c(R)<=1+10.05/R for R>=100','evaluations':evals,'cells':len(accepted),'failed':fails,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'finite_table_A':table_A}
if accepted:out['smallest_margin_lower']=min(accepted,key=lambda a:float(arb(a['margin_lower'])))['margin_lower']
Path(__file__).with_name('transfer_19.875.json').write_text(json.dumps(out,indent=2)+'\n')
Path(__file__).with_name('transfer_witnesses_19.875.json').write_text(json.dumps(accepted,separators=(',',':'))+'\n')
print(json.dumps(out,indent=2),flush=True)
if out['status']!='PASS':raise SystemExit(1)
