"""Directed binary64 interval elementary arithmetic and analytic trig/exp.
Every arithmetic endpoint is widened with nextafter. No libm trig or exp
is used in an enclosure. Integer range reduction is verified afterward.
"""
import numpy as np,math
from mpmath import iv
iv.dps=60
NINF=-np.inf;PINF=np.inf
def dn(x):return np.nextafter(x,NINF)
def up(x):return np.nextafter(x,PINF)
def I(x):
 a=np.asarray(x,dtype=float);return (a,a)
def A(x):return (np.asarray(x[0],dtype=float),np.asarray(x[1],dtype=float))
def ivpair(x):return (np.asarray(math.nextafter(float(x.a),-math.inf)),np.asarray(math.nextafter(float(x.b),math.inf)))
def add(x,y):return (dn(x[0]+y[0]),up(x[1]+y[1]))
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 p=[x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1]]
 return (dn(np.minimum.reduce(p)),up(np.maximum.reduce(p)))
def div(x,y):
 assert np.all(y[0]>0)
 return mul(x,(dn(1/y[1]),up(1/y[0])))
def ab(x):return up(np.maximum(abs(x[0]),abs(x[1])))
def inflate(x,e):return (dn(x[0]-e),up(x[1]+e))
def square(x):
 lo=np.where((x[0]<=0)&(x[1]>=0),0,np.minimum(x[0]*x[0],x[1]*x[1]))
 return (np.maximum(0,dn(lo)),up(np.maximum(x[0]*x[0],x[1]*x[1])))
PI=ivpair(iv.pi);LN2=ivpair(iv.log(2))
COEF_S=[ivpair(iv.mpf((-1)**j)/math.factorial(2*j+1)) for j in range(11)]
COEF_C=[ivpair(iv.mpf((-1)**j)/math.factorial(2*j)) for j in range(12)]
COEF_E=[ivpair(iv.mpf(1)/math.factorial(j)) for j in range(26)]
def trig(theta):
 midpoint=(theta[0]+theta[1])/2
 n=np.rint(midpoint/(math.pi/2)).astype(np.int64)
 r=sub(theta,mul(I(n),div(PI,I(2))))
 assert np.all(ab(r)<.8)
 r2=square(r);s=COEF_S[-1];c=COEF_C[-1]
 for a in COEF_S[-2::-1]:s=add(a,mul(r2,s))
 for a in COEF_C[-2::-1]:c=add(a,mul(r2,c))
 s=inflate(mul(r,s),1e-23);c=inflate(c,1e-23)
 q=n%4;sl=np.choose(q,[s[0],c[0],-s[1],-c[1]]);sh=np.choose(q,[s[1],c[1],-s[0],-c[0]])
 cl=np.choose(q,[c[0],-s[1],-c[1],s[0]]);ch=np.choose(q,[c[1],-s[0],-c[0],s[1]])
 return (cl,ch),(sl,sh)
def exp(x):
 mid=(x[0]+x[1])/2;n=np.floor(mid/math.log(2)).astype(np.int64)
 r=sub(x,mul(I(n),LN2));assert np.all(r[0]>-.01) and np.all(r[1]<.71)
 y=COEF_E[-1]
 for a in COEF_E[-2::-1]:y=add(a,mul(r,y))
 y=inflate(y,1e-28)
 assert np.all(n>-1000) and np.all(n<1000)
 return (dn(np.ldexp(y[0],n)),up(np.ldexp(y[1],n)))
def log(x):return ivpair(iv.log(iv.mpf([float(x[0]),float(x[1])])))
def cmul(x,y):return (sub(mul(x[0],y[0]),mul(x[1],y[1])),add(mul(x[0],y[1]),mul(x[1],y[0])))
def cadd(x,y):return add(x[0],y[0]),add(x[1],y[1])
def cabs(x):return up(ab(x[0])+ab(x[1]))
