"""Directed normalized block arithmetic. Analytic theorem audit is separate."""
from flint import arb,ctx
from fractions import Fraction
from pathlib import Path
import json,hashlib
ctx.prec=192
HERE=Path(__file__).resolve().parent

def B(v):
 q=Fraction(v);return arb(q.numerator)/q.denominator
pi=arb.pi()
def AB(k,eta,h):
 l=1/(1/eta+32*eta.sqrt()*h/(15*pi.sqrt()))
 d=(B('1/2')+(1+3*pi.sqrt()*eta**B('3/2')/8).sqrt()/2).sqrt()
 A=(1/(eta*h)+32/(15*pi.sqrt())*(eta+l).sqrt()+(eta+l)*l/3).sqrt()*d
 C=32**B('1/2')/(B(3).sqrt()*pi**B('1/4')*eta**B('1/4'))*d
 for j in range(3,k):
  J=2**(j-1);d=(1+2/B(2337)**B(Fraction(J-2,J))*(9*pi*eta/1024)**B(Fraction(1,J))).sqrt()
  A=d*(h**B(Fraction(-1,J))+B(2)**B('19/12')*(J-1)/B((2*J-1)*(4*J-3)).sqrt()*A.sqrt())
  C=d*B(2)**B('3/2')*(J-1)/B((2*J-3)*(4*J-5)).sqrt()*C.sqrt()
 return A,C

def ceil_upper(x):
 n=int(x.ceil().unique_fmpz());assert B(n)>=x;return n

def bound(lo,hi,p):
 x=B(lo);y=B(hi);h1,h2,eta1,eta2,theta1,theta2,theta3=map(B,p)
 K=ceil_upper((3*y/34-(theta2*(2*pi).sqrt()).log())/h1.log())
 R=ceil_upper((115*y/1394-(theta3/theta2).log())/h2.log())
 assert K>0 and R>0
 assert theta2/h1*(115*x/1394).exp()-(-27*x/82).exp()>theta3
 h=h1/(1-h1/theta2*(-7*x/17).exp())
 h3=h2/(1-h2/theta3*(-27*x/82).exp())
 assert h>1 and h<2 and h3>1 and h3<2
 A5,B5=AB(5,eta1,B(76545)*B(2).sqrt()/107264*h**9)
 b1=(B(53632)*B(2).sqrt()*pi**4/729)**B('1/30')*(B(76545)*B(2).sqrt()/107264)**B('1/8')/pi
 b2=pi**B('-7/8')*(B(729)/(53632*B(2).sqrt()*pi**4))**B('1/30')
 c3=b1*pi.sqrt()*A5*h**B('21/8')*(h-1)
 c4=b2*pi.sqrt()*B5*h**B('3/2')*(h-1)**B('7/8')
 E4=B('5.686')*pi.sqrt()*h**B('3/2');E5=6/pi*h**3*(h-1)
 S3=B(0);qmin=None;ratio_max=B(0)
 for k in range(1,K+1):
  Ah=h1**(-k)/(2*pi).sqrt();Al=Ah-(-x/2).exp();assert Al>0
  Qh=theta1*Ah**B('36/41');Ql=theta1*Al**B('36/41')-(-7*x/41).exp();assert Ql>0
  qlower=Ql*(7*x/41).exp();qr=Qh/Al*(-27*x/82).exp();assert qr<1
  if qmin is None or qlower<qmin:qmin=qlower
  if qr>ratio_max:ratio_max=qr
  terms=(h-1)*Ah/Ql+B('1800/2911')*c3*Al**B('-1/5')*Qh**B('11/30')
  terms+=B('28800/54481')*c4*Al**B('-11/20')*Qh**B('61/120')*(-3*x/328).exp()
  terms+=B('8/3')*E4*Ah**B('3/2')*Ql**B('-1/2')*(-27*x/164).exp()
  terms+=B('9/14')*E5*Al**B('-1/3')*Qh**B('1/3')*(-13*x/123).exp()
  terms+=(6+5/pi*(2+(h-1)*Qh/Al**2*(7*x/41).exp()/pi).log())*(-27*x/82).exp()
  S3+=((h-1+qr)*terms).sqrt()
 A4,B4=AB(4,eta2,h3**4)
 D1=(3/pi)**B('1/14')*A4*h3**B('5/7')*(h3-1)
 D2=(pi/3)**B('1/14')*B4*h3**B('2/7')*(h3-1)**B('3/4')
 S2=D1*theta2**B('3/14')*(1-h2**B(Fraction(-3*R,14)))/(h2**B('3/14')-1)*((B('19/119')-B('27/164'))*x).exp()
 S2+=D2*theta2**B('15/28')*(1-h2**B(Fraction(-15*R,28)))/(h2**B('15/28')-1)*((B('71/476')-B('27/164'))*x).exp()
 S1=2*(theta3+(-27*x/82).exp()/2).sqrt()
 total=2*(S1+S2+S3)+B('1.48')*((-B('1/4')-B('27/164'))*x).exp()+B('.127')*((-B('3/4')-B('27/164'))*x).exp()
 n=ceil_upper(total*100);upper=f'{n//100}.{n%100:02d}'
 assert total<B(upper)
 return {'log_lo':str(lo),'log_hi':str(hi),'A':str(upper),'total_ball':str(total),'S1_ball':str(S1),'S2_ball':str(S2),'S3_ball':str(S3),'K_upper':K,'R_upper':R,'q_lower':str(qmin),'q_over_a_upper':str(ratio_max),'parameters':p}

if __name__=='__main__':
 rows=[]
 for line in (HERE/'parameters.txt').read_text().splitlines():
  p=line.split();lo=int(p[0]);v=bound(lo,lo+5,p[1:]);rows.append(v);print(lo,v['A'],flush=True)
 out={'status':'ARITHMETIC_PASS','precision_bits':192,'scope':'32 closed intervals covering log t in [60,220]','rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'parameters_sha256':hashlib.sha256((HERE/'parameters.txt').read_bytes()).hexdigest()}
 (HERE/'unsplit_py_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
