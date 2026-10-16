"""Directed full-tail certificate for the nested extra-B exponent transfer.
Requires python-flint 0.9.0 / FLINT 3.6.0.
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



def inverse_bounds(q):
 # P_n(f_2,...,f_n) / f_2^(2n-3), recurrence for a Legendre inverse.
 # Monomial maps use f_2,...,f_7.
 def addto(a,k,v):a[k]=a.get(k,F(0))+v
 def mulvar(a,j):
  z={}
  for k,v in a.items():t=list(k);t[j-2]+=1;addto(z,tuple(t),v)
  return z
 def derivative(a,j):
  z={}
  for k,v in a.items():
   if k[j-2]:t=list(k);t[j-2]-=1;addto(z,tuple(t),v*k[j-2])
  return z
 P={(0,)*6:F(-1)};p=F(5,2);out=[]
 cs=[]
 for j in range(2,8):
  c=F(1)
  for k in range(j):c*=p+k
  cs.append((-1)**j*c)
 vals=[B(c)*arb(B((1+q)/2),B((1-q)/2)) for c in cs]
 for n in range(2,8):
  exact=sum(v*__import__('functools').reduce(lambda a,bc:a*bc[0]**bc[1],zip(cs,k),F(1)) for k,v in P.items())/cs[0]**(2*n-3)
  ans=arb(0)
  for k,v in P.items():
   z=B(v)
   for a,e in zip(vals,k):z*=a**e
   ans+=z
  ans/=vals[0]**(2*n-3)*B(exact)
  power=B(n-F(5,7));lower=B(q)**power
  ans*=arb((1+lower)/2,(1-lower)/2)
  assert ans>B('.99999') and ans<B('1.00001')
  out.append((n,str(ans)))
  if n<7:
   nxt={}
   for j in range(2,n+1):
    z=mulvar(mulvar(derivative(P,j),j+1),2)
    for k,v in z.items():addto(nxt,k,v)
   for k,v in mulvar(P,3).items():addto(nxt,k,-(2*n-3)*v)
   P=nxt
 return out

def certify(x0=10000,hs='1.02',targetco=110):
 x=B(x0);h1=B(hs);h2=B('1.03');t2=B(1);t3=B('.00001');cut=F(3,7);target=F(229,1392)
 corr=1-h1/t2*(-B(cut)*x).exp();h=h1/corr;H=h*h
 q1=B('0.9999999999');s0=B('1e-12');q1f=F('0.9999999999');eg=B('.00001');s2=B('.001');q2=B('.99')
 inv=inverse_bounds(q1f)
 # Triple-difference f=D nu^-5/2, direct second-B weight/errors.
 p=B('5/2');c2=B('35/4');c3=B('315/8')
 dm=(H-1)*c2;wc=q1**B('-1/2')*c2**B('-1/2')*H**B('9/4')
 secpole=B('5.686')*wc
 secder=2*B(3)**B('2/3')/pi**B('2/3')*(H**B('9/2')/q1)*(H**B('11/2')/q1)**B('1/3')*(H-1)*(q1*c3*H**B('-11/2'))**B('1/3')
 # second dual G=-E y^(5/7) with relative derivatives 1+-eg
 e0=B('7/2')*p**B('-5/7');y0=q1*p*H**B('-7/2');HY=H**B('7/2')/q1
 pp=B('9/7');cc2=pp*(pp+1);cc3=cc2*(pp+2);cc4=cc3*(pp+3);cc5=cc4*(pp+4)
 m4=3*q2*q2*cc3*cc3-cc4*cc2;M4=3*cc3*cc3-q2*q2*cc4*cc2
 l4=m4/cc2**5;H4=M4/m4/q2**5*HY**(3*pp+4)
 a4,b4=AB(4,B('1.2'),H4)
 dm3=(HY-1)*cc2;w3=q2**B('-1/2')*cc2**B('-1/2')*HY**((pp+2)/2)
 T1=w3*a4*H4**B('1/4')*dm3*l4**B('1/14')
 T2=w3*b4*dm3**B('3/4')*l4**B('-1/14')
 T3=B('5.686')*w3
 T4=2*B(3)**B('2/3')/pi**B('2/3')*(HY**(pp+2)/q2)*(HY**(pp+3)/q2)**B('1/3')*(HY-1)*(q2*cc3*HY**(-pp-3))**B('1/3')
 assert m4>0
 n5=-q2**3*cc5*cc2**2+10*cc3*cc4*cc2-15*q2**3*cc3**3;assert n5<0
 for n in range(1,6):assert (1-eg)/(1+eg)*(1+s2)**(-pp-n)>q2
 cd=(1+eg)*B('10/49');ell2=HY-1;J2=ell2+s2
 diag2=B(2).sqrt()*((J2*ell2).sqrt()+J2**B('3/4')*ell2**B('1/4'))
 gs=[]
 for name,T,d,n in [('third_main',T1,F(2,7),-F(4,49)),('third_secondary',T2,F(13,28),-F(31,49)),('third_pole',T3,-F(1,2),F(23,14)),('third_deriv',T4,F(1,3),-F(3,7))]:
  bp=2/B((1+d)*(2+d));co=J2**B('3/4')*(T*cd**B(d)*bp**2)**B('1/4')*B(2)**B(max(F(0),-3*d/4))
  k=7*d/40;l=F(3,4)+n/4+159*d/560
  if name=='third_main':co+=diag2
  gs.append((name,co,k,l,F(0)))
 # Complete last-Poisson logarithm: M3<=dm3*cd*E^.7*Y^-1.15.
 logco=dm3*cd*e0**B('.7')*y0**B('-23/20')
 d3=6+5/pi*(2+logco).log();e3=5/pi*B('483/80')
 gs.append(('third_log',J2**B('3/4')*(d3+e3*x)**B('1/4'),F(0),F(3,4),F(1,4)))
 sf=[]
 for name,co,k,l,lp in gs:
  sf.append((name,wc*co*e0**B(k)*y0**B(l),2*k/7+l-F(1,2),F(9,4)-7*l/2,lp))
 # Both failure regions are paid by full second-dual length.
 k0=y0**B('53/140')*e0**B('-.1');fail1=(2/k0)**B('20/7');fail2=(B('3/2')*k0*k0/(s2*y0))**B('10/3')
 triv=wc*dm
 sf += [('small_second_K',triv*fail1**B('1/4'),F(1,4),-F(17,56),F(0)),('large_second_shift',triv*fail2**B('1/4'),F(1,4),-F(13,24),F(0))]
 sf += [('second_pole',secpole,-F(1,2),F(9,4),F(0)),('second_deriv',secder,F(1,3),-F(5,6),F(0))]
 d2=6+5/pi*(2+B('3/4')*dm).log();e2=5/(2*pi)
 sf.append(('second_log',d2+e2*x,F(0),F(0),F(1)))
 # Three outer-inner A-processes: K=floor N^(127/502) C^(-13/251).
 J=H-1+s0;ell=H-1
 diag=B(2).sqrt()*((J*ell).sqrt()+J**B('3/4')*ell**B('1/4')+J**B('7/8')*ell**B('1/8'))
 intr=[]
 for name,co,d,n,lp in sf:
  bp=2/B((1+d)*(2+d));cc=J**B('7/8')*(co*B('3/4')**B(d)*bp**3)**B('1/8')*B(2)**B(max(F(0),-7*d/8))
  k=d/8-F(13,251)*7*d/8;l=F(7,8)+n/8+F(127,502)*7*d/8
  if name=='third_main':cc+=diag
  intr.append((name,cc,k,l,lp/8))
 rows=[]
 for name,co,k,l,lp in intr:rows.append((name,co*pi.sqrt()*h**B('3/2')*(2*pi)**B(-k/2-l)*h**B(-2*l),F(3,2)-2*l,k/2+l-F(1,2),lp))
 _,lead,a,b,_=rows[0];fb=2/B((1+b)*(2+b));th=((h-1)/(B(b)*fb*lead))**B(1/(1+b))
 B0=t2/h1-(-B(cut)*x).exp();qa=F(313,348);qt=-F(97,348)
 q0=th*B0**B(qa)*(B(cut*qa+qt)*x).exp();Z=1-1/q0
 p0=th*B0**B(qa-1)*(B(cut*(qa-1)+qt)*x).exp();al=h-1+p0
 assert q0>2 and p0<B('.01') and p0*p0/4<s0
 # κ^4/N=(N^3/C^52)^(1/251), C^52/N^3 >= (t/(2pi))^23.
 assert (23*(x-(2*pi).log())).exp()>(B('11/8')/s0)**251
 for n in range(1,8):assert (1+s0)**(-B('5/2')-n)*(1-s0/B(2*n+3))>q1
 def geo(co,u,v,lp=F(0)):
  exponent=(u/2 if u>0 else cut*u)+v-target
  assert exponent<=0,(u,v,exponent)
  if lp:assert B(lp)/x+B(exponent)<0
  if u>0:return co*(2*pi)**B(-u/2)/(h1**B(u)-1)*(B(exponent)*x).exp()
  return co*corr**B(u)*(h1/t2)**B(-u)/(1-h1**B(u))*(B(exponent)*x).exp()
 total=geo((al*((h-1)/(th*Z)+fb*lead*th**B(b))).sqrt(),F(35,696),F(97,696));out=[('main',str(total))]
 for name,co,a,b,lp in rows[1:]:
  u=(a+qa*b)/2;v=(1+qt)*b/2;bp=2/B((1+b)*(2+b))
  term=geo((al*bp*co*th**B(b)*Z**B(min(b,0))).sqrt(),u,v,lp/2);total+=term;out.append((name,str(term)))
 for name,co,a,b in [('first_pole',B('5.686')*pi.sqrt()*h**B('3/2'),F(3,2),-F(1,2)),('first_deriv',6/pi*h**3*(h-1),-F(1,3),F(1,3))]:
  bp=2/B((1+b)*(2+b));term=geo((al*bp*co*th**B(b)*Z**B(min(b,0))).sqrt(),(a+qa*b)/2,(1+qt)*b/2);total+=term;out.append((name,str(term)))
 d1=6+5/pi*(2+(h-1)/(pi*B0)).log();e1=20/(7*pi);cap=1/(14*h1.log())+1/x
 term=al.sqrt()*cap*(d1/x+e1).sqrt()*x**B('3/2')*(-B(target)*x).exp();total+=term;out.append(('first_log',str(term)))
 dr=2*pi*h**B('127/57')*B(2)**B('251/57');ds=B('4/3')*B(2).sqrt()*(h-1)*h**B('3/2')/pi.sqrt()
 for name,co,a,b in [('bad_first_K1',ds*dr**B('3/2'),F(54,19),F(-1)),('bad_first_K2',ds,-F(1,2),F(1,2))]:
  term=geo((al*co/(th*Z)).sqrt(),(a-qa)/2,(b-qt)/2);total+=term;out.append((name,str(term)))
 h3=h2/(1-h2/t3*(-2*B(target)*x).exp());aa,bb=AB(4,B(1),h3**4)
 D1=(3/pi)**B('1/14')*aa*h3**B('5/7')*(h3-1);D2=(pi/3)**B('1/14')*bb*h3**B('2/7')*(h3-1)**B('3/4')
 mid=D1*t2**B('3/14')/(h2**B('3/14')-1)*((B('8/49')-B(target))*x).exp()+D2*t2**B('15/28')/(h2**B('15/28')-1)*((B('31/196')-B(target))*x).exp()
 init=2*(t3+(-2*B(target)*x).exp()/2).sqrt()
 ans=2*(init+mid+total)+B('1.48')*((-B('1/4')-B(target))*x).exp()+B('.127')*((-B('3/4')-B(target))*x).exp()
 old=90*((B('77/468')-B(target))*x).exp()
 assert h>1 and h<2 and h3>1 and h3<2 and B0>0
 assert t2*(2*pi).sqrt()>1 and (x/14).exp()>t2*(2*pi).sqrt()
 assert B0*((B(cut)-2*B(target))*x).exp()>t3 and x>B(200).log()
 assert B('3/2')/x<B(target)
 assert ans<B(targetco) and old<B(targetco)
 result={'status':'PASS','precision_bits':ctx.prec,'target_coefficient':str(targetco),'target_exponent':str(target),
  'old_coefficient':'90','old_exponent':'77/468','log_tail_start':str(x0),
  'h1':hs,'h2':'1.03','theta2':'1','theta3':'.00001','last_derivative_eta':'1.2',
  'original_shift_guard':'1e-12','original_derivative_lower':'0.9999999999',
  'inverse_derivative_error':'.00001','second_shift_guard':'.001','last_derivative_lower':'.99',
  'tail_ball':str(ans),'old_splice_ball':str(old),'theta_ball':str(th),'B0_ball':str(B0),
  'q0_ball':str(q0),'q_over_a_bound':str(p0),'h_ball':str(h),'first_dual_ratio':str(H),
  'second_dual_ratio':str(HY),'middle_ratio':str(h3),'inverse_derivative_ratios':inv,
  'last_legendre_fifth_numerator_upper':str(n5),'last_fourth_scale':str(l4),'last_fourth_ratio':str(H4),
  'second_dual_amplitude_factor':str(e0),'second_dual_lower_factor':str(y0),
  'second_K_factor':str(k0),'small_K_cutoff_factor':str(fail1),'large_shift_cutoff_factor':str(fail2),
  'last_log_constant':str(d3),'last_log_slope':str(e3),'second_log_constant':str(d2),'second_log_slope':str(e2),
  'first_log_constant':str(d1),'first_log_slope':str(e1),
  'second_dual_rows':[{'name':name,'coefficient':str(co),'E_power':str(k),'Y_power':str(l),'log_power':str(lp)} for name,co,k,l,lp in gs],
  'triple_difference_rows':[{'name':name,'coefficient':str(co),'D_power':str(d),'N_power':str(n),'log_power':str(lp)} for name,co,d,n,lp in sf],
  'first_dual_rows':[{'name':name,'coefficient':str(co),'C_power':str(k),'N_power':str(l),'log_power':str(lp)} for name,co,k,l,lp in intr],
  'first_correlation_rows':[{'name':name,'coefficient':str(co),'a_power':str(a),'tr_power':str(b),'log_power':str(lp)} for name,co,a,b,lp in rows],
  'weighted_block_rows':out,'middle_ball':str(mid),'initial_ball':str(init),
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 return result
if __name__=='__main__':
 result=certify()
 (HERE/'nested_extra_dual_exponent_229_1392.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print('PASS: global coefficient 110, exponent 229/1392; analytic tail '+result['tail_ball']+'; old-bound splice '+result['old_splice_ball'])
