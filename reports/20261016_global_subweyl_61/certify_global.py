"""Uniform finite-block and infinite-tail arithmetic for the candidate 61 bound."""
from unsplit_block import B,AB,bound,pi,ctx
from pathlib import Path
import json,hashlib
ctx.prec=192
HERE=Path(__file__).resolve().parent
# All low heights 3<=t<=exp60: the published .618 Weyl bound.
low=B('.618')*60*((B('1/6')-B('27/164'))*60).exp()
assert low<61
# Finite range exp220 through exp1300.
rows=[]
for line in (HERE/'parameters.txt').read_text().splitlines():
 p=line.split();v=bound(int(p[0]),int(p[1]),p[2:]);assert B(v['A'])<61
 rows.append(v);print(p[0],v['A'],flush=True)
# Infinite tail: fixed rational parameters, not extrapolation of finite rows.
x=B(1300);h1=B('1.015');h2=B('1.03');eta1=B('1.8');eta2=B(1);theta1=B('1.15');theta2=B('1000000000');theta3=B('.00002')
corr=1-h1/theta2*(-7*x/17).exp();h=h1/corr
h3=h2/(1-h2/theta3*(-27*x/82).exp())
beta0=theta2/h1-(-7*x/17).exp()
q0=theta1*beta0**B('36/41')*(65*x/697).exp()
p0=theta1*beta0**B('-5/41')*(-222*x/697).exp()
assert corr>0 and beta0>0 and q0>2 and p0<1 and h>1 and h<2 and h3>1 and h3<2
assert theta2/h1*(115*x/1394).exp()-(-27*x/82).exp()>theta3
alpha=h-1+p0
A5,B5=AB(5,eta1,B(76545)*B(2).sqrt()/107264*h**9)
b1=(B(53632)*B(2).sqrt()*pi**4/729)**B('1/30')*(B(76545)*B(2).sqrt()/107264)**B('1/8')/pi
b2=pi**B('-7/8')*(B(729)/(53632*B(2).sqrt()*pi**4))**B('1/30')
c3=b1*pi.sqrt()*A5*h**B('21/8')*(h-1);c4=b2*pi.sqrt()*B5*h**B('3/2')*(h-1)**B('7/8')
E4=B('5.686')*pi.sqrt()*h**B('3/2');E5=6/pi*h**3*(h-1)
C1=(alpha*((h-1)/theta1/(1-1/q0)+B('1800/2911')*c3*theta1**B('11/30'))).sqrt()
C2=(alpha*B('28800/54481')*c4*theta1**B('61/120')).sqrt()
C4=(alpha*B('8/3')*E4*theta1**B('-1/2')/(1-1/q0).sqrt()).sqrt()
C5=(alpha*B('9/14')*E5*theta1**B('1/3')).sqrt()
T1=C1/(2*pi)**B('5/164')/(h1**B('5/82')-1)
T2=C2*corr**B('-17/328')*(h1/theta2)**B('17/328')/(1-h1**B('-17/328'))
T4=C4/(2*pi)**B('87/328')/(h1**B('87/164')-1)*(-27*x/328).exp()
T5=C5*corr**B('-5/246')*(h1/theta2)**B('5/246')/(1-h1**B('-5/246'))*(-427*x/8364).exp()
# Entire logarithmic error, bounded without an unsupported height cutoff.
Clog=(h-1)*theta1*beta0**B('-46/41')/pi
Dlog=6+5/pi*(2+Clog).log();Elog=B('940/697')/pi
kcap=3/(34*h1.log())+1/x
assert Dlog>0 and Elog>0 and (theta2*(2*pi).sqrt()).log()>0
assert B('3/2')/x<B('27/164')
T6=alpha.sqrt()*kcap*(Dlog/x+Elog).sqrt()*x**B('3/2')*(-27*x/164).exp()
S3=T1+T2+T4+T5+T6
A4,B4=AB(4,eta2,h3**4)
D1=(3/pi)**B('1/14')*A4*h3**B('5/7')*(h3-1);D2=(pi/3)**B('1/14')*B4*h3**B('2/7')*(h3-1)**B('3/4')
S2=D1*theta2**B('3/14')/(h2**B('3/14')-1)*((B('19/119')-B('27/164'))*x).exp()+D2*theta2**B('15/28')/(h2**B('15/28')-1)*((B('71/476')-B('27/164'))*x).exp()
S1=2*(theta3+(-27*x/82).exp()/2).sqrt()
total=2*(S1+S2+S3)+B('1.48')*((-B('1/4')-B('27/164'))*x).exp()+B('.127')*((-B('3/4')-B('27/164'))*x).exp()
assert total<60 and total<61
out={'status':'ARITHMETIC_PASS','precision_bits':192,'target_global_constant':'61','low_height_bound_ball':str(low),'finite_rows':rows,'tail_log_t0':'1300','tail_parameters':['1.015','1.03','1.8','1','1.15','1000000000','.00002'],'tail_total_ball':str(total),'tail_components':{k:str(v) for k,v in [('S1',S1),('S2',S2),('main',T1),('secondary',T2),('poisson',T4),('cubic',T5),('log',T6)]},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'block_script_sha256':hashlib.sha256((HERE/'unsplit_block.py').read_bytes()).hexdigest(),'parameters_sha256':hashlib.sha256((HERE/'parameters.txt').read_bytes()).hexdigest()}
(HERE/'global_subweyl_61.json').write_text(json.dumps(out,indent=2)+'\n')
print('TAIL',total,flush=True)
