#!/usr/bin/env python3
"""Cross-check the log jet using finite formal log(1+u), not differentiation.

Read an existing certificate, use its enclosed derivatives, and independently
assemble the formal logarithm. This checks the logarithm conversion only,
not an independent proof of the theta tail or pi/exp enclosures.
"""
import argparse
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import certify_theta_jet as cj


def multiply(a,b,degree):
    out=[cj.I.point(0) for _ in range(degree+1)]
    for i in range(degree+1):
        for j in range(degree+1-i):
            out[i+j]=out[i+j]+a[i]*b[j]
    return out


def run(source: Path):
    data=json.loads(source.read_text(encoding='utf-8'))
    cj.DIGITS=data['grid_digits']; cj.SCALE=10**cj.DIGITS
    derivatives={int(k):cj.I(F(v[0]),F(v[1])) for k,v in data['derivative_bounds'].items()}
    degree=6
    u=[cj.I.point(0)]+[derivatives[2*k]/(factorial(2*k)*derivatives[0]) for k in range(1,degree+1)]
    power=[cj.I.point(1)]+[cj.I.point(0) for _ in range(degree)]
    log=[cj.I.point(0) for _ in range(degree+1)]
    for j in range(1,degree+1):
        power=multiply(power,u,degree)
        for k in range(1,degree+1):
            log[k]=log[k]+F((-1)**(j+1),j)*power[k]
    p={k:((-1)**(k+1))*k*log[k] for k in (4,5,6)}
    for k in p:
        cj.strictly_inside(p[k],*data['asserted_moment_boxes'][str(k)])
        prior=data['log_jet_moments'][str(k)]
        assert max(p[k].lo,F(prior[0])) <= min(p[k].hi,F(prior[1]))
    det=p[4]*p[6]-p[5]**2
    cj.strictly_inside(det,*data['asserted_determinant_box'])
    return {'status':'PASS','grid_digits':cj.DIGITS,'method':'finite formal log(1+u) through degree 6 in x^2',
            'log_jet_moments':{str(k):v.decimal_bounds() for k,v in p.items()},
            'hankel_determinant':det.decimal_bounds(),'rh_proved':False}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path); p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); result=run(a.source)
    with a.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2); f.write('\n')
    print(json.dumps(result,indent=2))
