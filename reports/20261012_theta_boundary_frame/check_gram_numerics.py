#!/usr/bin/env python3
"""Finite, non-certified sanity check of the true-theta two-parameter Gram.

Uses the exact analytic change r=exp(2|x|), u=(c+d)r to avoid overflow.
Eight theta modes and finite quadrature accuracy are used. This is NOT an
interval certificate, NOT the proof of the all-rank theorem, and NOT RH.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from math import cosh, exp, log, pi, sqrt, gamma
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import quad

MODE_COUNT = 8
A_STAR = log(2)/2
GAMMA = gamma(2.5)


def theta_normalized(r: float) -> float:
    if r < 1:
        raise ValueError('Use genuine theta reflection before evaluating S(r)')
    ans = 1-3/(2*pi*r)
    for n in range(2, MODE_COUNT+1):
        v = -pi*(n*n-1)*r
        if v > -750:
            ans += n**4*(1-3/(2*pi*n*n*r))*exp(v)
    return ans


def phi(x: float) -> float:
    y=abs(x);r=exp(2*y)
    return 4*pi*pi*exp(4.5*y-pi*r)*theta_normalized(r)


def small_v(x: float, c: float) -> float:
    t=-0.5*log(0.5+c/pi)
    m=sqrt(phi(x)/(2*cosh(x/2)))
    return (phi(x-t)+phi(x+t)-2*cosh(t/2)*phi(x))/m


def stable_factor(r: float, c: float) -> float:
    z=0.5+c/pi
    t=-0.5*log(z)
    sr=theta_normalized(r)
    main=theta_normalized(z*r)
    plus_exp=9*t-pi*(1/z-z)*r
    ground_exp=4.5*t-pi*(1-z)*r
    plus=(exp(plus_exp)*theta_normalized(r/z) if plus_exp>-750 else 0.0)
    ground=(2*cosh(t/2)*exp(ground_exp)*sr if ground_exp>-750 else 0.0)
    return sqrt((1+r**(-0.5))/sr)*(main+plus-ground)


def scaled_raw_gram(c: float,d: float) -> tuple[float,float]:
    """Return <v_c,v_d>/[A(c)A(d) Gamma(5/2) (c+d)^(-5/2)]."""
    q=c+d; umin=q*exp(1)
    cuts=sorted(set([umin]+[v for v in [.005,.05,.5,2.,8.,25.,80.] if v>umin]))
    def integrand(u):
        r=u/q
        return u**1.5*exp(-u)*stable_factor(r,c)*stable_factor(r,d)/GAMMA
    total=err=0.0
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        val,e=quad(integrand,lo,hi,epsabs=2e-13,epsrel=2e-13,limit=250)
        total+=val;err+=e
    val,e=quad(integrand,cuts[-1],np.inf,epsabs=2e-13,epsrel=2e-13,limit=250)
    total+=val;err+=e
    tc=-.5*log(.5+c/pi);td=-.5*log(.5+d/pi)
    ac=2*pi*exp(-4.5*tc);ad=2*pi*exp(-4.5*td)
    core,ce=quad(lambda x:2*small_v(x,c)*small_v(x,d),0.,.5,
                 epsabs=2e-13,epsrel=2e-13,limit=250)
    scale=q**2.5/(ac*ad*GAMMA)
    return total+core*scale,err+ce*scale


def run(c0:float,size:int):
    cs=[c0*256.0**(-j) for j in range(size)]
    raw=np.empty((size,size));err=np.empty_like(raw);model=np.empty_like(raw)
    for j in range(size):
        for k in range(j,size):
            v,e=scaled_raw_gram(cs[j],cs[k]);raw[j,k]=raw[k,j]=v;err[j,k]=err[k,j]=e
            model[j,k]=model[k,j]=(2*sqrt(cs[j]*cs[k])/(cs[j]+cs[k]))**2.5
    actual=model*raw/np.sqrt(np.outer(np.diag(raw),np.diag(raw)))
    evals=np.linalg.eigvalsh(actual)
    return {'c0':c0,'size':size,'normalized_gram':actual.tolist(),
            'model_gram':model.tolist(),'eigenvalue_range':[float(evals[0]),float(evals[-1])],
            'max_model_difference':float(np.max(np.abs(actual-model))),
            'max_reported_quadrature_error':float(err.max())}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--size',type=int,default=5)
    a=p.parse_args()
    result={'status':'NONRIGOROUS_FINITE_SANITY_ONLY','python':platform.python_version(),
            'numpy':np.__version__,'scipy':scipy.__version__,'theta_modes':MODE_COUNT,
            'runs':[run(c0,a.size) for c0 in [1e-4,1e-6,2.0**-128]],
            'rh_proved':False,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    with a.output.open('x',encoding='utf-8') as w:json.dump(result,w,indent=2);w.write('\n')
    print(json.dumps({**{k:v for k,v in result.items() if k!='runs'},
                      'runs':[{k:v for k,v in r.items() if 'gram' not in k} for r in result['runs']]},indent=2))

if __name__=='__main__':main()
