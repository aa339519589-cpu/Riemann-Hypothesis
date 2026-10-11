#!/usr/bin/env python3
"""Finite-precision theta/Bessel divisor dictionary checks.

No zero list or zeta evaluations enter the calculation. The analytic identity
and all-cutoff sign theorem are proved in REPORT.md. These numerical checks
are not interval certificates for quadrature or infinite tails. Outputs use
exclusive creation. Exact rational checks are separated from numerical ones.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, platform, time
import mpmath as mp


def phi(x, modes):
    x=abs(x)
    u=mp.pi*mp.exp(2*x)
    return 2*mp.pi*mp.exp(mp.mpf('2.5')*x)*sum(
        n*n*(2*n*n*u-3)*mp.exp(-n*n*u) for n in range(1,modes+1))


def divisors(k):
    return [n for n in range(1,k+1) if k%n==0]


def order_weight(k,y):
    return sum(mp.cosh(y*mp.log(mp.mpf(n*n)/k)) for n in divisors(k))


def hj(a,y):
    K=mp.besselk(y,a)
    Kprime=-(mp.besselk(y-1,a)+mp.besselk(y+1,a))/2
    H=(a**4+9*a*a)*K+6*a**3*Kprime
    J=(mp.mpf('10.5')*a**4+(mp.mpf('22.5')+6*y*y)*a*a)*K+(a**5+24*a**3)*Kprime
    return H,J


def bessel_term(k,r,y):
    a=2*mp.pi*k*mp.exp(r)
    Hy,Jy=hj(a,y); H0,J0=hj(a,0)
    d=order_weight(k,y); d0=len(divisors(k))
    return (mp.exp(r/2)*(d*Hy-d0*H0),
            mp.exp(r/2)*(d*Jy-d0*J0))


def direct_difference(r,y,modes,nodes):
    xs,ws=mp.gauss_quadrature(nodes,'legendre')
    edges=list(map(mp.mpf,['0','.125','.25','.5','1','1.5','2','3','4']))
    total=mp.mpf(0)
    for l,h in zip(edges,edges[1:]):
        mid=(l+h)/2; rad=(h-l)/2
        for x,w in zip(xs,ws):
            t=mid+rad*x
            total+=2*rad*w*phi(r/2+t,modes)*phi(r/2-t,modes)*(2*mp.sinh(y*t)**2)
    return total


def exact_constants():
    coefficient=F(2,3)-F(12,25)+F(36,175)-F(8,125)
    assert F(7,5)*coefficient > F(4,9)
    quadratic=2*F(44,7)**2-15*F(44,7)+15
    assert quadratic == -F(13,49)
    P12=-12**3+F(21,2)*12**2+12*12+F(45,2)
    Pprime12=-3*12**2+21*12+12
    assert P12 == -F(99,2) and Pprime12 == -168
    cosh1=1+F(1,2)+F(1,24)+F(1,720)/(1-F(1,56))
    assert cosh1 < F(8,5)
    return {'integral_coefficient':str(coefficient),
            'integral_lower_margin':str(F(7,5)*coefficient-F(4,9)),
            'quadratic_at_44_over_7':str(quadratic),
            'P12':str(P12),'Pprime12':str(Pprime12),
            'cosh1_upper':str(cosh1),'status':'PASS exact rational inequalities'}


def run(dps,nodes,modes,cutoff,ys_values):
    mp.mp.dps=dps
    start=time.time()
    output={'python':platform.python_version(),'mpmath':mp.__version__,
            'dps':dps,'quadrature_nodes_per_piece':nodes,'theta_modes':modes,
            'divisor_cutoff':cutoff,'exact_constants':exact_constants(),
            'scope':'exploratory high precision, not quadrature/tail certification',
            'dictionary_checks':[],'slope_checks':[],'rh_proved':False}
    def number(x):return mp.nstr(x, min(dps-8,55))
    for ys in ys_values:
        y=mp.mpf(ys)
        terms0=[bessel_term(k,mp.mpf(0),y) for k in range(1,cutoff+1)]
        for rs in ['0','.2','.7']:
            r=mp.mpf(rs)
            terms=terms0 if not r else [bessel_term(k,r,y) for k in range(1,cutoff+1)]
            bs=sum(t[0] for t in terms)
            direct=direct_difference(r,y,modes,nodes)
            output['dictionary_checks'].append({'y':ys,'r':rs,'direct':number(direct),
                                                'divisor_sum':number(bs),'absolute_difference':number(abs(direct-bs))})
        slope=mp.mpf(0)
        rows=[]
        for k,(value,derivative) in enumerate(terms0,1):
            slope+=derivative
            if k<=4 or k in [8,16,cutoff]:
                rows.append({'k':k,'term_at_zero':number(value),'derivative_at_zero':number(derivative),
                             'partial_derivative_sum':number(slope)})
        output['slope_checks'].append({'y':ys,'rows':rows})
    output['elapsed_seconds']=time.time()-start
    output['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return output

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dps',type=int,default=50)
    p.add_argument('--nodes',type=int,default=40)
    p.add_argument('--modes',type=int,default=8)
    p.add_argument('--cutoff',type=int,default=24)
    p.add_argument('--ys',nargs='+',default=['.125','.25','.49'])
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if a.dps<30 or a.nodes<16 or a.modes<2 or a.cutoff<2:raise ValueError('Insufficient test parameters')
    r=run(a.dps,a.nodes,a.modes,a.cutoff,a.ys)
    with a.output.open('x',encoding='utf-8') as f:json.dump(r,f,indent=2);f.write('\n')
    print(json.dumps({'exact_constants':r['exact_constants'],'dictionary_checks':r['dictionary_checks'],
                      'elapsed_seconds':r['elapsed_seconds']},indent=2))
