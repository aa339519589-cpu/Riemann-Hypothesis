#!/usr/bin/env python3
"""Directed scalar certificate for the complete anisotropic mixed-coordinate zeta bound.
Requires python-flint 0.9.0 / FLINT 3.6.0. The three local analytical
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

x0=10000;x=B(x0);p=Q(19,58);theta=p/2;s=B('1e-12');K=10**6;gamma=B('1e-7');lp=Q(33,58)
# Exact anisotropic exponents, including all lower/upper endpoint choices.
assert Q(3,7)*Q(28,29)-Q(9,29)==Q(3,29)
assert Q(3,7)*(-Q(1,29))-Q(9,29)==-Q(66,203)
assert Q(8,11)-Q(45,319)-Q(3,7)*Q(440,319)==-Q(1,203)
assert -5+Q(90,29)+Q(3,7)*Q(242,29)==Q(341,203)
assert 1-Q(66,203)==Q(137,203)
assert Q(20,29)-Q(3,7)*Q(30,29)==Q(50,203)
assert -Q(3,11)+Q(28,29)*Q(7,22)==Q(1,29)
assert Q(9,22)-Q(9,29)*Q(7,22)==Q(9,29)
assert Q(3,2)-Q(33,29)*Q(7,22)==Q(33,29)
assert Q(1,8)+Q(3,7)*(-Q(3,8))==-Q(1,28)
assert -Q(19,29)+Q(57,116)==-theta
assert Q(20,87)-Q(9,29)-Q(3,7)*Q(4,87)==-Q(61,609)
assert Q(3,7)/29+Q(9,29)==Q(66,203)
assert Q(9,58)+Q(1,116)==theta
assert Q(229,1392)-theta==Q(1,1392)
assert Q(1,14)+Q(3,7)*Q(3,14)==Q(8,49)<theta
assert -Q(1,14)+Q(3,7)*Q(15,28)==Q(31,196)<theta
# All guards improve monotonically for x>=x0.
qmin=gamma*(B('3/29')*x).exp()/x**B('33/29');assert qmin>2
assert B('3/29')-B('33/29')/x>0
qratio=(-B('66/203')*x).exp();assert qratio<1
shift=8*(-B('1/203')*x).exp();assert shift<s
series=(2+s)**2/4*(-B('132/203')*x).exp();assert series<B('1e-30')
inverse=256*(B('341/203')*x).exp();assert inverse>2**40
assert 2**20>2**11 and 2**18>2**11
assert 16*(x/14).exp()>2
assert K*K*(-B('66/203')*x).exp()+2*(-x).exp()<1
assert 4*(-B('153/203')*x).exp()<1
assert 2*(2*pi).sqrt()*(-x/14).exp()<1
assert 2*((B(p)-B('3/7'))*x).exp()<1
assert x>B(200).log() and B(3).log()>1
# Inclusive-lattice mixed-A constant; both words are lawful, but the transposed
# anisotropic word, rather than their geometric mean, is retained in the proof.
C=B(20000)*K**4
assert B(12).sqrt()+4*B(12)**B('1/4')+8*B(12)**B('1/8')<22
assert B(4)**B('7/4')<12
assert (22+12*B(128)**B('1/8')*C**B('1/8'))*B(2).sqrt()<80*C**B('1/8')
assert 80*C**B('1/8')<10**6
main=3*200*B(10**6)*B(2)**B('1/22')/(1-B(2)**B('-29/22'))
wall=3*3200*B('1/4')**B('-3/4')*(2*pi).sqrt()/(1-B(2)**B('-1/2'))
assert main<2*10**9 and wall<3*10**5
small=4*B(2)**B('3/2')*B(64)**B('3/2');assert small<6000
E4=B('5.686')*pi.sqrt()*B(2)**B('3/2');E5=48/pi
assert E4<30 and E5<16
combined_endpoint=4*B(3*10**5)*B(2).sqrt()+240*B(2).sqrt()
assert combined_endpoint<2*10**6
assert 6+5/pi*((2+1/pi).log()+4*x/7)<10*x
# Complete squared original block divided by T_a=a^(1/29)t^(9/29)x^(33/29).
rows=[('main',B(8*10**9)*gamma**B('7/22')),('diagonal',4/gamma),
 ('small_r',48000/gamma*(-x/28).exp()),
 ('cutoff_and_endpoint',B(2*10**6)/gamma.sqrt()/x**B(lp)*(-B(theta)*x).exp()),
 ('first_B_derivative',64*gamma**B('1/3')/x**B('44/29')*(-B('61/609')*x).exp()),
 ('first_B_log',40/x**B('4/29')*(-B('66/203')*x).exp())]
large_squared=sum((v for _,v in rows),start=B(0));assert large_squared<10**8
large=10**4*(2*pi)**B('-1/116')/(1-B(2)**B('-1/58'))
a4,b4=AB(4,B(1),B(16))
D1=(3/pi)**B('1/14')*a4*B(2)**B('5/7')
D2=(pi/3)**B('1/14')*b4*B(2)**B('2/7')
middle1=D1*B(2)**B('3/14')/(B(2)**B('3/14')-1)*(B(Q(8,49)-theta)*x).exp()
middle2=D2*B(2)**B('15/28')/(B(2)**B('15/28')-1)*(B(Q(31,196)-theta)*x).exp()
initial=2*B(2).sqrt()
rem=B('1.48')*((-B('1/4')-B(theta))*x).exp()+B('.127')*((-B('3/4')-B(theta))*x).exp()
normalized_total=2*large+(2*(initial+middle1+middle2)+rem)/x**B(lp)
assert normalized_total<10**7
low_splice=110*(x/1392).exp();assert low_splice<10**7
comparison_x=B(25000)
comparison=B(10**7)/110*comparison_x**B(lp)*(-comparison_x/1392).exp()
assert comparison<1 and B(lp)/comparison_x<B('1/1392')
result={'status':'PASS','precision_bits':ctx.prec,'coefficient':'10000000','exponent':'19/116','log_power':'33/58','valid_t_lower':'3','analytic_tail_log_start':str(x0),'outer_gamma':'1/10000000',
 'uniform_shift_guard':str(shift),'uniform_series_guard':str(series),'inverse_row_guard':str(inverse),'q_unfloored_lower':str(qmin),
 'good_main_coefficient':str(main),'good_cutoff_coefficient':str(wall),'small_r_coefficient':str(small),
 'first_Poisson_endpoint_coefficient':str(E4),'first_Poisson_derivative_coefficient':str(E5),'combined_cutoff_endpoint_coefficient':str(combined_endpoint),
 'large_block_squared_normalized_rows':dict((n,str(v)) for n,v in rows),'large_block_squared_total':str(large_squared),'large_geometric_coefficient':str(large),
 'A4':str(a4),'B4':str(b4),'middle_first_normalized':str(middle1),'middle_second_normalized':str(middle2),'initial_normalized':str(initial),
 'full_tail_coefficient':str(normalized_total),'lower_splice_coefficient':str(low_splice),'comparison_log_start':'25000','comparison_ratio':str(comparison),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'anisotropic_mixed_bound.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('PASS: anisotropic mixed-coordinate bound; tail coefficient '+str(normalized_total)+'; comparison ratio '+str(comparison))
