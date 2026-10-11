#!/usr/bin/env python3
"""Exact second-order curve and Fourier checks. No frequency sampling."""
import json
import sympy as S
s,e,x,b,c,d=S.symbols('s e x b c d')
A=b*s/S.Integer(2)-s*s/S.Integer(2)
P=A-c
Q=A*A/S.Integer(2)-s**3/S.Integer(6)+c*s+d-c*A
p=1+e*P+e**2*Q
num=S.diff(p,s,2)-2*S.diff(p,s)+p
den=(p-S.diff(p,s)).subs(s,0)
f=S.series(num/den,e,0,3).removeO().expand()

def cosine_poly(poly):
    result=0
    for (n,),a in S.Poly(poly,s).terms():
        rn=sum(S.binomial(n+1,2*j)*(-1)**j*x**j
               for j in range((n+1)//2+1))
        result+=a*S.factorial(n)*rn/(1+x)**(n+1)
    return S.factor(result)

records=[]
Vs=[]
for q,bv,cv in [(0,8,S.Rational(49,8)),(1,6,S.Rational(53,8))]:
    F=S.factor(f.coeff(e,2).subs({b:bv,c:cv}))
    assert not F.has(d)
    assert cosine_poly(F).subs(x,0)==0
    V=S.factor(-(1+x)/x*cosine_poly(F))
    Vs.append(V)
    records.append({'q':q,'density_Q':str(F),'spectral_V':str(V)})
margin=S.factor(Vs[0]-49*(3-x)/(4*(1+x)**2))
expected=(15*x**3+281*x**2+189*x+19)/(2*(1+x)**4)
assert S.factor(margin-expected)==0
positive_poly=S.expand((15*x**3+281*x**2+189*x+19)-15*(1+x)**3)
assert positive_poly==236*x*x+144*x+4
out={'second_order':records,'endpoint_margin':str(margin),'margin_certificate':str(positive_poly),'status':'exact_checks_pass'}
print(json.dumps(out,indent=2))
