#!/usr/bin/env python3
"""Finite algebra and pointwise checks for the band-core superoscillation.

The mathematical full-form convergence proof is in ANALYTIC_BAND_FORM_CORE.md.
This checker is NOT a rigorous interval certificate, RH proof, or check of
infinite Gamma / full-prime bounds.
"""
import json
import mpmath as mp

mp.mp.dps = 90
carrier, width, target = mp.mpf(4), mp.mpf(1), mp.j/2
A = (target - carrier)/width
x_values = [mp.mpf('0.1'), mp.mpf('0.4'), mp.mpf('1')]

def f_n(n, x):
    z = width*x/n
    return (mp.cos(z) + mp.j*A*mp.sin(z))**n

def envelope(n, x):
    return (mp.exp(mp.j*carrier*x)*f_n(n,x) +
            mp.exp(-mp.j*carrier*x)*f_n(n,-x))/2

def finite_cosine(n, x):
    return mp.fsum(mp.binomial(n,k) * ((1+A)/2)**k *
                   ((1-A)/2)**(n-k) *
                   mp.cos((carrier+(2*k-n)*width/n)*x)
                   for k in range(n+1))

algebra = []
for x in x_values:
    difference = abs(envelope(8,x)-finite_cosine(8,x))
    algebra.append(dict(x=str(x),N=8,absolute_error=mp.nstr(difference,20)))
    assert difference < mp.mpf('1e-75')

convergence=[]
for x in x_values:
    errs=[]
    for n in [4,16,64,256]:
        er=abs(envelope(n,x)-mp.cosh(x/2))
        errs.append(er)
        convergence.append(dict(x=str(x),N=n,pointwise_error=mp.nstr(er,20)))
    assert errs[0]>errs[1]>errs[2]>errs[3]
    assert errs[-1] < mp.mpf('0.04')

result = {
    'status':'PASS_FINITE_IDENTITY_AND_POINTWISE_SANITY',
    'precision_digits':mp.mp.dps,
    'carrier':'4','band_half_width':'1','target':'i/2',
    'algebra':algebra,
    'pointwise_convergence':convergence,
    'rigorous_scope':'Exact finite binomial identity is proved analytically in the manuscript; the numerical computations here are not interval-certified.',
    'not_verified':['full original form convergence','zero location','RH'],
    'rh_proved':False
}
print(json.dumps(result, indent=2))
