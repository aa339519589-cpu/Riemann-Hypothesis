"""Directed certificate for the complete extra-dual-B exponent transfer.
Requires python-flint 0.9.0 / FLINT 3.6.0. No sampled height extrapolation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from flint import arb,ctx
ctx.prec=192
HERE=Path(__file__).resolve().parent
def B(v):
 q=F(v);return arb(q.numerator)/q.denominator
pi=arb.pi()
def AB(k,eta,h):
 l=1/(1/eta+32*eta.sqrt()*h/(15*pi.sqrt()))
 d=(B('1/2')+(1+3*pi.sqrt()*eta**B('3/2')/8).sqrt()/2).sqrt()
 A=(1/(eta*h)+32/(15*pi.sqrt())*(eta+l).sqrt()+(eta+l)*l/3).sqrt()*d
 C=32**B('1/2')/(B(3).sqrt()*pi**B('1/4')*eta**B('1/4'))*d
 for j in range(3,k):
  J=2**(j-1);d=(1+2/B(2337)**B(F(J-2,J))*(9*pi*eta/1024)**B(F(1,J))).sqrt()
  A=d*(h**B(F(-1,J))+B(2)**B('19/12')*(J-1)/B((2*J-1)*(4*J-3)).sqrt()*A.sqrt())
  C=d*B(2)**B('3/2')*(J-1)/B((2*J-3)*(4*J-5)).sqrt()*C.sqrt()
 return A,C

def certify(x0=5800,h1s='1.02',h2s='1.03',theta2s='1',theta3s='.00001',eta='1.2',theta=None):
 x=B(x0);h1,h2,t2,t3=map(B,[h1s,h2s,theta2s,theta3s]);target=F(77,468)
 corr=1-h1/t2*(-B('3/7')*x).exp();h=h1/corr;hd=h*h
 qrel=B('.99');p=B('5/2');c2=B('35/4');c3=B('315/8');c4=B('3465/16')
 m4=3*qrel*qrel*c3*c3-c4*c2;M4=3*c3*c3-qrel*qrel*c4*c2
 l4=m4/c2**5;H4=M4/m4/qrel**5*hd**B('23/2')
 a4,b4=AB(4,B(eta),H4)
 dm=(hd-1)*c2;wc=qrel**B('-1/2')*c2**B('-1/2')*hd**B('9/4')
 cc1=wc*a4*H4**B('1/4')*dm*l4**B('1/14')
 cc2=wc*b4*dm**B('3/4')*l4**B('-1/14')
 cc3=B('5.686')*wc
 H2=hd**B('9/2')/qrel;H3=hd**B('11/2')/qrel
 cc4=2*B(3)**B('2/3')/pi**B('2/3')*H2*H3**B('1/3')*(hd-1)*(qrel*c3*hd**B('-11/2'))**B('1/3')
 ell=hd-1;J=ell+B('.001')
 diag=B(2).sqrt()*(J.sqrt()*ell.sqrt()+J**B('3/4')*ell**B('1/4')+J**B('7/8')*ell**B('1/8'))
 intr=[]
 for co,d,n in [(cc1,F(2,7),-F(3,7)),(cc2,F(13,28),-F(67,56)),(cc3,-F(1,2),F(9,4)),(cc4,F(1,3),-F(5,6))]:
  cp=2/B((1+d)*(2+d));coe=J**B('7/8')*(co*B('3/4')**B(d)*cp**3)**B('1/8')*B(2)**B(max(F(0),-7*d/8))
  k=d/12;l=F(7,8)+n/8+5*d/24
  intr.append([coe,k,l])
 intr[0][0]+=diag
 dl=6+5/pi*(2+B('3/4')*dm).log();el=5/(2*pi)
 intr.append([J**B('7/8')*(dl+el*x)**B('1/8'),F(0),F(7,8)])
 # first B weight, with nu lower N=tr/(2*pi*h^2*a^2), C=sqrt(tr/(2*pi)).
 rows=[]
 for co,k,l in intr:
  cf=co*pi.sqrt()*h**B('3/2')*(2*pi)**B(-k/2-l)*h**B(-2*l)
  rows.append((cf,F(3,2)-2*l,k/2+l-F(1,2)))
 lead,a,b=rows[0]
 fb=2/B((1+b)*(2+b))
 if theta is None:th=((h-1)/(B(b)*fb*lead))**B(1/(1+b))
 else:th=B(theta)
 B0=t2/h1-(-B('3/7')*x).exp();assert B0>0
 q0=th*B0**B('106/117')*(B('29/273')*x).exp();Z=1-1/q0
 p0=th*B0**B('-11/117')*(-B('88/273')*x).exp();al=h-1+p0
 assert q0>2 and p0<B('1/100')
 assert x>0 and (2*x-((2*pi)**2*h*h).log()).exp()>B(1375)**21
 # epsilon*nu <= (q/a)^2/4.
 assert p0*p0/4<B('.001')
 def geosum(co,u,v,logpower=F(0)):
  ex=(u/2+v-target) if u>0 else (F(3,7)*u+v-target)
  assert ex<=0
  if ex<0 and logpower:assert B(logpower)/x+B(ex)<0
  if u>0:return co*(2*pi)**B(-u/2)/(h1**B(u)-1)*(B(ex)*x).exp()
  return co*corr**B(u)*(h1/t2)**B(-u)/(1-h1**B(u))*(B(ex)*x).exp()
 total=geosum((al*((h-1)/(th*Z)+fb*lead*th**B(b))).sqrt(),F(11,234),F(11,78))
 out=[('main',str(total))]
 for i,(co,a,b) in enumerate(rows[1:],1):
  ff=2/B((1+b)*(2+b));u=(a+F(106,117)*b)/2;v=F(14,39)*b
  term=geosum((al*ff*co*th**B(b)*Z**B(min(b,0))).sqrt(),u,v,F(1,16) if i==4 else F(0))
  total+=term;out.append((f'second_B_{i}',str(term)))
 # original first-Poisson nonlog errors
 for name,co,a,b in [('first_pole',B('5.686')*pi.sqrt()*h**B('3/2'),F(3,2),-F(1,2)),('first_derivative',6/pi*h**3*(h-1),-F(1,3),F(1,3))]:
  ff=2/B((1+b)*(2+b));u=(a+F(106,117)*b)/2;v=F(14,39)*b
  term=geosum((al*ff*co*th**B(b)*Z**B(min(b,0))).sqrt(),u,v);total+=term;out.append((name,str(term)))
 # original first-Poisson log: tq/a^2<=t/a, q<=a
 dl1=6+5/pi*(2+(h-1)/(pi*B0)).log();el1=20/(7*pi)
 cap=1/(14*h1.log())+1/x
 tl=al.sqrt()*cap*(dl1/x+el1).sqrt()*x**B('3/2')*(-B(target)*x).exp();total+=tl;out.append(('first_log',str(tl)))
 # bad outer r: K<2, use full trivial first dual length
 dr=(2*pi)*h**B('20/9')*B(2)**B('14/3');dt=(h-1)*h**B('3/2')/pi.sqrt();ds=B('4/3')*B(2).sqrt()*dt
 for name,co,u,v in [('bad_r1',ds*dr**B('3/2'),F(451,468),-F(14,39)),('bad_r2',ds,-F(329,468),F(61,156))]:
  term=geosum((al*co/(th*Z)).sqrt(),u,v);total+=term;out.append((name,str(term)))
 h3=h2/(1-h2/t3*(-2*B(target)*x).exp());aa4,bb4=AB(4,B(1),h3**4)
 D1=(3/pi)**B('1/14')*aa4*h3**B('5/7')*(h3-1);D2=(pi/3)**B('1/14')*bb4*h3**B('2/7')*(h3-1)**B('3/4')
 S2=D1*t2**B('3/14')/(h2**B('3/14')-1)*((B('8/49')-B(target))*x).exp()
 S2+=D2*t2**B('15/28')/(h2**B('15/28')-1)*((B('31/196')-B(target))*x).exp()
 S1=2*(t3+(-2*B(target)*x).exp()/2).sqrt()
 ans=2*(S1+S2+total)+B('1.48')*((-B('1/4')-B(target))*x).exp()+B('.127')*((-B('3/4')-B(target))*x).exp()
 old=49*((B('27/164')-B(target))*x).exp()
 assert h>1 and h<2 and h3>1 and h3<2
 assert t2*(2*pi).sqrt()>1
 assert (x/14).exp()>t2*(2*pi).sqrt()
 assert B0*((B('3/7')-2*B(target))*x).exp()>t3
 assert x>B(200).log()
 assert B('3/2')/x<B(target)
 assert ans<B(90) and old<B(90)
 assert B('27/164')>B(target)
 # Exact derivative smallness and Legendre numerator signs.
 c5=B('45045/32')
 n5upper=-qrel**3*c5*c2**2+10*c3*c4*c2-15*qrel**3*c3**3
 assert n5upper<0 and m4>0 and M4>m4 and H4>1
 for k in [2,3,4,5]:
  assert B('1001/1000')**(-B('5/2')-k)*(1-1/B(1000*(2*k+3)))>qrel
 assert (-B(target)*x).exp()>0
 result={'status':'PASS','precision_bits':ctx.prec,'target_coefficient':'90',
  'target_exponent':'77/468','old_coefficient':'49','old_exponent':'27/164',
  'log_tail_start':str(x0),'h1':h1s,'h2':h2s,'theta2':theta2s,'theta3':theta3s,'eta1':eta,
  'tail_ball':str(ans),'old_splice_ball':str(old),'theta_ball':str(th),
  'q0_ball':str(q0),'q_over_a_bound':str(p0),'B0_ball':str(B0),
  'h_ball':str(h),'h_dual_ball':str(hd),'h3_ball':str(h3),
  'lambda4_coefficient':str(l4),'H4_ball':str(H4),
  'legendre_fifth_numerator_upper':str(n5upper),
  'weighted_main_rows':out,'middle_ball':str(S2),'initial_ball':str(S1),
  'phi_rows':[{'coefficient':str(co),'C_power':str(k),'N_power':str(l)} for co,k,l in intr],
  'first_dual_rows':[{'coefficient':str(co),'a_power':str(a),'tr_power':str(b)} for co,a,b in rows],
  'second_poisson_log_constant':str(dl),'second_poisson_log_slope':str(el),
  'first_poisson_log_constant':str(dl1),'first_poisson_log_slope':str(el1),
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 return result

if __name__=='__main__':
 result=certify()
 (HERE/'extra_dual_exponent_77_468.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print('PASS: global coefficient 90, exponent 77/468; analytic tail '+result['tail_ball']+'; old-bound splice '+result['old_splice_ball'])
