#!/usr/bin/env python3
"""Directed scalar certificate for the complete additional partial-dual mixed-coordinate zeta bound.
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

x0=160000;x=B(x0);p=Q(53,162);theta=p/2;pa=Q(43,100);lp=Q(25,54);gamma=B('1e-8');s=B('1e-16')
qamin=pa*Q(26,27)-Q(25,81);qaratio=Q(25,81)+pa/27
assert qamin==Q(427,4050) and qaratio==Q(2629,8100)
qmin=gamma*(B(qamin)*x).exp()/x**B('25/27');assert qmin>2
assert B(qamin)-B('25/27')/x>0
shift=8*(-x/4050).exp();assert shift<s
assert Q(49,81)-pa*Q(38,27)==-Q(1,4050)
series=4*(-2*B(qaratio)*x).exp();assert series<B('1e-40')
assert B(2)**B('40/30')>2
assert 16*(B('4/225')*x).exp()>2
assert pa*Q(4,3)-Q(5,9)==Q(4,225)
assert (-B(qaratio)*x).exp()<1
# Original/dual partitions and complete logarithmic scales.
assert 2*((B(p)-B(pa))*x).exp()<1
assert 2*(2*pi).sqrt()*((B(pa)-B('1/2'))*x).exp()<1
assert Q(29,27)-pa/9==Q(2771,2700)
assert Q(56,81)-pa*Q(28,27)==Q(497,2025)
assert 2*(-2*x).exp()+2*((B('2771/2700')-2)*x).exp()<1
assert 4*((B('497/2025')-1)*x).exp()<1
rows=[('main',Q(1,30),Q(14,15),Q(53,60)),('boundary',Q(0),Q(1),Q(15,16)),('endpoint',Q(-1,30),Q(241,240),Q(491,480)),('derivative',Q(1,45),Q(359,360),Q(619,720)),('constant',Q(0),Q(1),Q(7,8))]
expected=[(Q(0),Q(0),Q(0)),(-Q(1,162),Q(1,108),-Q(35,432)),(Q(37,1296),-Q(2,27),-Q(115,864)),(-Q(85,1944),Q(7,81),-Q(35,1296)),(-Q(4,81),Q(2,27),-Q(5,216))]
worst=[Q(0),-Q(1,648),-Q(107,32400),-Q(1,1944),-Q(1,81)]
ledger=[];normalized=[]
for (name,k,l,m),want,z in zip(rows,expected,worst):
 u=k+m-Q(1,2);v=k+l+m-Q(1,2);w=Q(3,2)-k-2*m
 tt=u-Q(25,81)*v;aa=w-1+Q(26,27)*v;xx=Q(5,4)-Q(25,27)*v
 assert (tt,aa,xx)==want
 assert tt+aa*(Q(1,2) if aa>=0 else pa)==z
 assert k/2+m-Q(3,4)>0 and v>1 and u>0
 coef=3*200*B(10**7)*B(2)**B(k)*B(2)**B('1/4')/(1-B(2)**(-B(v)))
 assert coef<10**11
 nv=8*B(10**11)*gamma**B(v-1)*x**B(xx)*(B(z)*x).exp()
 normalized.append((name,nv))
 ledger.append({'name':name,'k':str(k),'l':str(l),'m':str(m),'c_power':str(u),'r_power':str(v),'a_power':str(w),'normalized_t_power':str(tt),'normalized_a_power':str(aa),'normalized_log_power':str(xx),'worst_t_power':str(z),'good_row_coefficient':str(coef)})
wall=3*3200*B('1/4')**B('-3/4')*(2*pi).sqrt()/(1-B(2)**B('-1/2'));assert wall<3*10**5
small=4*B(128)**B('3/2')*(2*pi)**B('1/3');assert small<20000
E4=B('5.686')*pi.sqrt()*B(2)**B('3/2');E5=48/pi
assert E4<30 and E5<16
combined=4*B(3*10**5)*B(2).sqrt()+240*B(2).sqrt();assert combined<3*10**6
assert 6+5/pi*((2+1/pi).log() +B(1-pa)*x)<10*x
assert -Q(1,2)-Q(25,162)+Q(53,108)==-theta
assert -Q(19,243)-pa*Q(4,81)==-Q(604,6075)
# All normalized rows are decreasing for x>=x0, except constant main/diagonal.
normalized += [('diagonal',4/gamma),('small_r',160000/gamma*(-x/12).exp()),('cutoff_and_endpoint',B(3*10**6)/gamma.sqrt()*x**(-B(lp))*(-B(theta)*x).exp()),('first_B_derivative',64*gamma**B('1/3')*x**B('-100/81')*(-B('604/6075')*x).exp()),('first_B_log',40*x**B('2/27')*(-B(qaratio)*x).exp())]
assert B('2/27')/x<B(qaratio)
large_squared=sum((v for _,v in normalized),start=B(0));assert large_squared<10**10
large=B(10**5)*(2*pi)**B('-1/108')/(1-B(2)**B('-1/54'))
assert Q(25,162)+Q(1,108)==theta
A4,B4=AB(4,B(1),B(16))
D1=(3/pi)**B('1/14')*A4*B(2)**B('5/7');D2=(pi/3)**B('1/14')*B4*B(2)**B('2/7')
midp1=Q(1,14)+pa*Q(3,14);midp2=-Q(1,14)+pa*Q(15,28)
assert midp1==Q(229,1400) and theta-midp1==Q(1,113400)
assert midp2<theta
mid1=D1*B(2)**B('3/14')/(B(2)**B('3/14')-1)*(B(midp1-theta)*x).exp()
mid2=D2*B(2)**B('15/28')/(B(2)**B('15/28')-1)*(B(midp2-theta)*x).exp()
initial=2*B(2).sqrt()
rem=B('1.48')*((-B('1/4')-B(theta))*x).exp()+B('.127')*((-B('3/4')-B(theta))*x).exp()
total=2*large+(2*(initial+mid1+mid2)+rem)/x**B(lp)
assert total<10**23
assert Q(19,116)-theta==Q(1,4698)
assert Q(33,58)-lp==Q(83,783)
low=B(10**7)*(x/4698).exp()*x**B('83/783');assert low<10**23
assert B(3).log()>1
cx=B(250000)
ratio=B(10**23)/B(10**7)*cx**(-B('83/783'))*(-cx/4698).exp()
assert ratio<1
out={'status':'PASS','precision_bits':192,'coefficient':'1e23','exponent':'53/324','log_power':'25/54','valid_t_lower':'3','analytic_tail_log_start':str(x0),'outer_gamma':'1e-8','large_block_threshold_power':'43/100','q_unfloored_lower':str(qmin),'uniform_shift_guard':str(shift),'uniform_series_guard':str(series),'row_ledger':ledger,'large_squared_rows':{n:str(v) for n,v in normalized},'large_squared_total':str(large_squared),'large_geometric_coefficient':str(large),'small_r_coefficient':str(small),'wall_coefficient':str(wall),'combined_endpoint_coefficient':str(combined),'A4':str(A4),'B4':str(B4),'middle1':str(mid1),'middle2':str(mid2),'full_tail_coefficient':str(total),'lower_splice_coefficient':str(low),'comparison_log_start':'250000','comparison_ratio':str(ratio),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'global_partial_dual.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS: global partial-dual scalar ledger; tail '+str(total)+'; low splice '+str(low)+'; comparison '+str(ratio))
