#!/usr/bin/env python3
"""Non-rigorous finite numerical cross-check; not an interval certificate."""
import argparse, json, platform
from pathlib import Path
import mpmath as m

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--output',type=Path,required=True)
args=p.parse_args()
m.mp.dps=50

def Q2(a,c):
    # Directly applying (1/2+a*d/da) twice to P*exp(-a*c).
    P=a**4+9*a*a-6*a**3*c
    P1=4*a**3+18*a-18*a*a*c
    P2=12*a*a+18-36*a*c
    return (m.mpf('0.25')*P+2*a*(P1-c*P)+a*a*(P2-2*c*P1+c*c*P))

out=[]
for a in [m.mpf(12),4*m.pi,m.mpf(24)]:
    for y in [m.mpf('0.001'),m.mpf('0.25'),m.mpf('0.5')]:
        integ=lambda f:m.quad(lambda v:m.exp(-a*(m.cosh(v)-1))*f(v),[0,m.mpf('.5'),1,2,4])
        K=integ(lambda v:m.cosh(y*v))
        Kp=-integ(lambda v:m.cosh(v)*m.cosh(y*v))
        E=integ(lambda v:v*m.sinh(y*v))
        Ep=-integ(lambda v:m.cosh(v)*v*m.sinh(y*v))
        t=y*y
        A=a**6+(m.mpf(285)/4+t)*a**4+(m.mpf(225)/4+39*t)*a*a
        B=15*a**5+(m.mpf(165)/2+6*t)*a**3
        At=a**4+39*a*a;Bt=6*a**3
        direct=integ(lambda v:Q2(a,m.cosh(v))*v*m.sinh(y*v))
        reduced=A*E+B*Ep+2*y*(At*K+Bt*Kp)
        P=a*a*(16*a**5-244*a**4+840*a**3-1629*a*a-780*a-225)/8
        R=a*a*(4*a**3-25*a*a+150*a-39)/2
        bound=(P*E+2*y*R*K)/(2*(a-m.mpf('.25')))
        rel=abs(direct-reduced)/abs(reduced)
        assert rel<m.mpf('1e-35')
        assert 0<bound<direct
        assert -Kp/K < 1+1/(2*(a-y*y))
        assert -Ep/E < 1+3/(2*(a-y*y))
        out.append({'a':m.nstr(a,20),'y':str(y),'direct_scaled_second_derivative':m.nstr(direct,35),
                    'analytic_lower_bound_scaled':m.nstr(bound,35),'relative_dictionary_difference':m.nstr(rel,8)})
data={'status':'PASS','scope':'NUMERICAL_ONLY: finite integration checks, no tail/rounding interval certificate',
      'python':platform.python_version(),'mpmath':m.__version__,'dps':50,'points':out,'rh_proved':False}
with args.output.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
print(json.dumps(data,indent=2))
