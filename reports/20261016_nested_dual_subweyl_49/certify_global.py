"""Uniform finite-block and infinite-tail arithmetic for the candidate 49 bound."""
from dual_block import B,AB,bound,pi,ctx
from pathlib import Path
from fractions import Fraction
import json,hashlib
ctx.prec=192
HERE=Path(__file__).resolve().parent
# All low heights 3<=t<=exp60: the published .618 Weyl bound.
low=B('.618')*60*((B('1/6')-B('27/164'))*60).exp()
assert low<49
# Finite range exp220 through exp1800: exact contiguous parameter cover.
rows=[]
expected=220
for line in (HERE/'parameters.txt').read_text().splitlines():
 p=line.split();assert len(p)==8 and int(p[0])==expected and int(p[1])==expected+20
 v=bound(int(p[0]),int(p[1]),p[2:]);assert B(v['A'])<49
 expected=int(p[1])
 rows.append(v);print(p[0],v['A'],flush=True)
assert expected==1800 and len(rows)==79
# Infinite tail: fixed rational parameters, not extrapolation of finite rows.
x=B(1800);h1=B('1.015');h2=B('1.03');eta1=B('1.2');eta2=B(1);theta1=B('2.7');theta2=B('1000000000000');theta3=B('.00002')
corr=1-h1/theta2*(-7*x/17).exp();h=h1/corr
h3=h2/(1-h2/theta3*(-27*x/82).exp())
beta0=theta2/h1-(-7*x/17).exp()
q0=theta1*beta0**B('36/41')*(65*x/697).exp()
p0=theta1*beta0**B('-5/41')*(-222*x/697).exp()
assert corr>0 and beta0>0 and q0>2 and p0<1 and h>1 and h<2 and h3>1 and h3<2
assert theta2/h1*(115*x/1394).exp()-(-27*x/82).exp()>theta3
alpha=h-1+p0
H5=B(76545)*B(2).sqrt()/107264*h**9
A3i,B3i=AB(3,eta1,H5)
lam0=B(53632)*B(2).sqrt()*pi**4/729;nc=(h-1)/pi;wc=pi.sqrt()*h**B('3/2')
eta=B(3);lamcut=eta**B('-15/14')
ai=1/eta+B('72/91')*A3i*H5.sqrt()*(eta+1)**B('1/6')
bi=B('72/55')*B3i*eta**B('-1/6')
aa=1/eta+B('392/435')*ai.sqrt()*(eta+1)**B('1/14')
bb=B('392/351')*bi.sqrt()*eta**B('-1/14')
cc=(ai*(eta+1)).sqrt();dd=B('49/39')*(bi*(eta+1)).sqrt()*eta**B('-1/7')
coeff=[aa.sqrt(),bb.sqrt(),cc.sqrt(),dd.sqrt(),(aa*(eta+1)).sqrt(),(bb*(eta+1)).sqrt(),(cc*(eta+1)).sqrt(),(dd*(eta+1)).sqrt()]
ps=[('1','1/30'),('7/8','-1/30'),('3/4','0'),('5/8','-1/15'),('1/2','0'),('3/8','-1/15'),('1/4','-1/30'),('1/8','-1/10')]
cr=[]
for co,(pp,ss) in zip(coeff,ps):
 pp,ss=Fraction(pp),Fraction(ss);ap=Fraction(3,2)-2*pp+9*ss;bp=-Fraction(1,2)+pp-4*ss
 assert -1<bp<=1
 cr.append((wc*co*nc**B(pp)*lam0**B(ss),ap,bp))
c3=cr[0][0];c4=cr[1][0]
ds=B('4/3')*B(2).sqrt()*wc*nc
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
extra=[]
for co,ap,bp in cr[2:]:
 uu=(ap+bp*Fraction(36,41))/2;vv=bp*Fraction(15,41)
 cf=alpha*2*co/B((1+bp)*(2+bp))*theta1**B(bp)
 if bp<0:cf*= (1-1/q0)**B(bp)
 cf=cf.sqrt()
 if uu>0:
  ex=uu/2+vv-Fraction(27,164);assert ex<0
  term=cf/(2*pi)**B(uu/2)/(h1**B(uu)-1)*(B(ex)*x).exp()
 else:
  assert uu<0
  ex=uu*Fraction(7,17)+vv-Fraction(27,164);assert ex<0
  term=cf*corr**B(uu)*(h1/theta2)**B(-uu)/(1-h1**B(uu))*(B(ex)*x).exp()
 extra.append(term)
CS=(alpha*ds/(theta1*(1-1/q0))).sqrt()
TS1=CS*(lam0/lamcut)**B('3/16')/(2*pi)**B('655/1312')/(h1**B('655/656')-1)*(-x/32).exp()
TS2=CS*corr**B('-113/164')*(h1/theta2)**B('113/164')/(1-h1**B('-113/164'))*(-179*x/2788).exp()
S3=T1+T2+T4+T5+T6+sum(extra)+TS1+TS2
A4,B4=AB(4,eta2,h3**4)
D1=(3/pi)**B('1/14')*A4*h3**B('5/7')*(h3-1);D2=(pi/3)**B('1/14')*B4*h3**B('2/7')*(h3-1)**B('3/4')
S2=D1*theta2**B('3/14')/(h2**B('3/14')-1)*((B('19/119')-B('27/164'))*x).exp()+D2*theta2**B('15/28')/(h2**B('15/28')-1)*((B('71/476')-B('27/164'))*x).exp()
S1=2*(theta3+(-27*x/82).exp()/2).sqrt()
total=2*(S1+S2+S3)+B('1.48')*((-B('1/4')-B('27/164'))*x).exp()+B('.127')*((-B('3/4')-B('27/164'))*x).exp()
assert total<49
out={'status':'ARITHMETIC_PASS','precision_bits':192,'target_global_constant':'49','low_height_bound_ball':str(low),'finite_rows':rows,'tail_log_t0':'1800','tail_parameters':['1.015','1.03','1.2','1','2.7','1000000000000','.00002'],'tail_total_ball':str(total),'tail_components':{k:str(v) for k,v in [('S1',S1),('S2',S2),('main',T1),('secondary',T2),('poisson',T4),('cubic',T5),('log',T6),('dual_extra_total',sum(extra)),('large_lambda_first',TS1),('large_lambda_second',TS2)]},'tail_extra_balls':[str(z) for z in extra],'dual_row_exponents':[[str(a),str(b)] for c,a,b in cr],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'block_script_sha256':hashlib.sha256((HERE/'dual_block.py').read_bytes()).hexdigest(),'parameters_sha256':hashlib.sha256((HERE/'parameters.txt').read_bytes()).hexdigest()}
(HERE/'global_subweyl_49.json').write_text(json.dumps(out,indent=2)+'\n')
print('TAIL',total,flush=True)
