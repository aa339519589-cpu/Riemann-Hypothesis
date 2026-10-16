#!/usr/bin/env python3
"""Directed scalar certificate for the complete two-partial-dual mixed-coordinate candidate.
Requires python-flint 0.9.0 / FLINT 3.6.0. The complete local analytical
appendices are part of the proof; this is not a sampled-height certificate.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
from flint import arb,ctx
ctx.prec=192
HERE=Path(__file__).resolve().parent

def B(v):
 q=Q(v);return arb(q.numerator)/q.denominator
pi=arb.pi()
def AB(k,eta,h):
 lam=1/(1/eta+32*eta.sqrt()*h/(15*pi.sqrt()))
 delta=(B('1/2')+(1+3*pi.sqrt()*eta**B('3/2')/8).sqrt()/2).sqrt()
 aa=(1/(eta*h)+32/(15*pi.sqrt())*(eta+lam).sqrt()+(eta+lam)*lam/3).sqrt()*delta
 bb=B(32).sqrt()/(B(3).sqrt()*pi**B('1/4')*eta**B('1/4'))*delta
 for j in range(3,k):
  J=2**(j-1)
  delta=(1+2/B(2337)**B(Q(J-2,J))*(9*pi*eta/1024)**B(Q(1,J))).sqrt()
  aa=delta*(h**B(Q(-1,J))+B(2)**B('19/12')*(J-1)/B((2*J-1)*(4*J-3)).sqrt()*aa.sqrt())
  bb=delta*B(2)**B('3/2')*(J-1)/B((2*J-3)*(4*J-5)).sqrt()*bb.sqrt()
 return aa,bb

x0=10000;x=B(x0);theta=Q(155,948);p=2*theta;pa=Q(12,25);lp=Q(89,158);gamma=B('1e-12');s=B('1e-30')
qamin=pa*Q(76,79)-Q(73,237);qaratio=Q(73,237)+pa*Q(3,79)
assert qamin==Q(911,5925) and qaratio==Q(1933,5925)
qmin=gamma*(B(qamin)*x).exp()/x**B('89/79');assert qmin>2
assert B(qamin)-B('89/79')/x>0
shift=8*(B(Q(145,237)-pa*Q(112,79))*x).exp();assert shift<s
assert Q(145,237)-pa*Q(112,79)==-Q(407,5925)
series=100*(-2*B(qaratio)*x).exp();assert series<B('1e-80')
assert B(2)**B('134/89')>2
rpower=pa*Q(13,10)-Q(8,15);assert rpower==Q(34,375)
assert 16*(B(rpower)*x).exp()>2
assert 2*((B(p)-B('3/7'))*x).exp()<1
assert 2*((B('3/7')-B(pa))*x).exp()<1
assert 2*(2*pi).sqrt()*((B(pa)-B('1/2'))*x).exp()<1
fmn_power=Q(85,79)-pa*Q(9,79);n_power=Q(164,237)-pa*Q(82,79)
assert 2*(-2*x).exp()+2*((B(fmn_power)-2)*x).exp()<1
assert 4*((B(n_power)-1)*x).exp()<1
raw=[('main',Q(7,10),Q(3,10),Q(1,10)),('bx',Q(3,4),Q(1,4),Q(0)),('by',Q(3,4),Q(0),Q(1,4)),('inverse2',Q(4,5),Q(-1,20),Q(3,20)),('cap',Q(7,8),Q(-1,8),Q(0)),('short',Q(0),Q(1),Q(1,2)),('constant',Q(0),Q(1),Q(0)),('derivative2',Q(5,6),Q(0),Q(0)),('log2',Q(1,2),Q(0),Q(0)),('inverse1',Q(-1,2),Q(1),Q(1)),('derivative1',Q(1,3),Q(1),Q(0))]
ledger=[];normalized=[]
for name,k0,l0,m0 in raw:
 h=7*k0/8
 k=k0/8-h*Q(7,89);l=(7+l0-k0)/8+h*Q(14,89);m=(7+m0-2*k0)/8+h*Q(23,89)
 u=k+m-Q(1,2);v=k+l+m-Q(1,2);w=Q(3,2)-k-2*m
 tt=u-Q(73,237)*v;aa=w-1+Q(76,79)*v;xx=Q(3,2)-Q(89,79)*v
 z=tt+aa*(Q(1,2) if aa>=0 else pa)
 assert k/2+m-Q(3,4)>0 and v>1 and u>0
 if name=='main':assert (tt,aa,xx)==(Q(0),Q(0),Q(0))
 else:assert z<0 and B(z)+B(xx)/x<0
 coef=3*200*B(10**16)*B(2)**B(k)*B(2).sqrt()/(1-B(2)**(-B(v)))
 assert coef<10**20
 nv=8*B(10**20)*gamma**B(v-1)*x**B(xx)*(B(z)*x).exp()
 normalized.append((name,nv))
 ledger.append({'name':name,'k':str(k),'l':str(l),'m':str(m),'c_power':str(u),'r_power':str(v),'a_power':str(w),'normalized_t_power':str(tt),'normalized_a_power':str(aa),'normalized_log_power':str(xx),'worst_t_power':str(z),'good_row_coefficient':str(coef)})
wall=3*3200*B('1/4')**B('-3/4')*(2*pi).sqrt()/(1-B(2)**B('-1/2'));assert wall<3*10**5
small=4*B(128)**B('3/2')*(2*pi)**B('3/10');assert small<20000
E4=B('5.686')*pi.sqrt()*B(2)**B('3/2');E5=48/pi;assert E4<30 and E5<16
combined=4*B(3*10**5)*B(2).sqrt()+240*B(2).sqrt();assert combined<3*10**6
assert 6+5/pi*((2+1/pi).log()+B(1-pa)*x)<10*x
assert -Q(1,2)-Q(73,474)+(Q(3,2)-Q(41,79))/2==-theta
first_deriv=Q(1,3)-Q(292,711)-pa*Q(4,79)
normalized += [('diagonal',4/gamma),('small_r',160000/gamma*(-B('3/40')*x).exp()),('cutoff_and_endpoint',B(3*10**6)/gamma.sqrt()*x**(-B(lp))*(-B(theta)*x).exp()),('first_B_derivative',64*gamma**B('1/3')*x**B('-356/237')*(B(first_deriv)*x).exp()),('first_B_log',40*x**B('-10/79')*(-B(qaratio)*x).exp())]
assert first_deriv<0
large_squared=sum((v for _,v in normalized),start=B(0));assert large_squared<10**20
large=B(10**10)*(2*pi)**B('-3/316')/(1-B(2)**B('-3/158'))
assert Q(73,474)+Q(3,316)==theta
# Middle range only up to t^(3/7). The published LOCAL 19/116 row bridges to t^.48.
A4,B4=AB(4,B(1),B(16))
D1=(3/pi)**B('1/14')*A4*B(2)**B('5/7');D2=(pi/3)**B('1/14')*B4*B(2)**B('2/7')
midp1=Q(8,49);midp2=-Q(1,14)+Q(3,7)*Q(15,28)
assert midp1<theta and midp2<theta
mid1=D1*B(2)**B('3/14')/(B(2)**B('3/14')-1)*(B(midp1-theta)*x).exp()
mid2=D2*B(2)**B('15/28')/(B(2)**B('15/28')-1)*(B(midp2-theta)*x).exp()
bridge_power=Q(9,58)+pa/58;bridge_log=Q(33,58)-lp
assert bridge_power<theta and B(bridge_power-theta)+B(bridge_log)/x<0
bridge=B(10**4)*B(2)**B('1/58')/(1-B(2)**B('-1/58'))*x**B(bridge_log)*(B(bridge_power-theta)*x).exp()
initial=2*B(2).sqrt()
rem=B('1.48')*((-B('1/4')-B(theta))*x).exp()+B('.127')*((-B('3/4')-B(theta))*x).exp()
total=2*large+2*bridge+(2*(initial+mid1+mid2)+rem)/x**B(lp)
assert total<2*10**12
assert Q(19,116)-theta==Q(2,6873)
assert Q(33,58)-lp==Q(13,2291)
# Both exponents are positive, so the whole lower-splice ratio increases.
low=B(10**7)*(2*x/6873).exp()*x**B('13/2291');assert low<2*10**12
assert B(3).log()>1
cx=B(50000)
ratio=B(2*10**5)*cx**(-B('13/2291'))*(-2*cx/6873).exp()
assert ratio<1
out={'status':'PASS','precision_bits':192,'coefficient':'2e12','exponent':'155/948','log_power':'89/158','valid_t_lower':'3','analytic_tail_log_start':str(x0),'outer_gamma':'1e-12','large_block_threshold_power':'12/25','q_unfloored_lower':str(qmin),'uniform_shift_guard':str(shift),'uniform_series_guard':str(series),'row_ledger':ledger,'large_squared_rows':{n:str(v) for n,v in normalized},'large_squared_total':str(large_squared),'large_geometric_coefficient':str(large),'small_r_coefficient':str(small),'wall_coefficient':str(wall),'combined_endpoint_coefficient':str(combined),'A4':str(A4),'B4':str(B4),'middle1':str(mid1),'middle2':str(mid2),'bridge_coefficient':str(bridge),'full_tail_coefficient':str(total),'lower_splice_coefficient':str(low),'comparison_log_start':'50000','comparison_ratio':str(ratio),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'global_double.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS: candidate global double-partial ledger; tail '+str(total)+'; low splice '+str(low)+'; comparison '+str(ratio))
