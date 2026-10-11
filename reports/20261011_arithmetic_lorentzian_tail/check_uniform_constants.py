#!/usr/bin/env python3
"""Exact algebra checks for the uniform Lorentzian manuscript.
Only SymPy rational polynomial arithmetic; no numerical frequency samples.
"""
import json
import sympy as S

z, s, x = S.symbols('z s x')
p = {0:z*z+9, 1:6*z}
L0 = S.Integer(100)
claimed = [15,30,47,66,90]

def norm_at(poly, degree):
    return sum(abs(c)*L0**(d[0]-degree)
               for d,c in S.Poly(poly,z).terms())

records=[]
first_order_coefficients={0:[],1:[]}
for m in range(5):
    Q=S.expand(sum((-1)**j*v for j,v in p.items())-(-2)**m*z**(m+2))
    vals=[]
    for q in (0,1):
        def E(j):
            return S.Rational(3,2)*j+S.Rational(3,4) if q==0 else 9*j+S.Rational(15,2)
        c=(norm_at(Q,m+1)+sum(norm_at(v,m+2)*E(j) for j,v in p.items()))/2**m
        assert c < claimed[m]
        vals.append(str(c))
        b=lambda j:S.Rational(j*(2*q+1),2)-S.Rational((2*q+1)*(2*q+3),24)
        expanded=S.expand(sum((-1)**j*v*(1+b(j)/z) for j,v in p.items()))
        gamma=expanded.coeff(z,m+1)/(-2)**m
        first_order_coefficients[q].append(gamma)
    records.append({'m':m,'exact_upper_bounds_q0_q1':vals,'rounded_claim':claimed[m]})
    p={j:S.expand(5*p.get(j,0)+2*z*S.diff(p.get(j,0),z)+2*z*p.get(j-1,0))
       for j in range(m+3)}

def cosine_poly(poly):
    result=0
    for (n,),coeff in S.Poly(poly,s).terms():
        real_numer=sum(S.binomial(n+1,2*j)*(-1)**j*x**j
                       for j in range((n+1)//2+1))
        result+=coeff*S.factorial(n)*real_numer/(1+x)**(n+1)
    return S.factor(result)

for q in (0,1):
    P=S.Integer(6-q)*s-s*s/S.Integer(2)-S.Integer(5-q)
    for j in (0,1,2):
        direct=-s*s/S.Integer(2)+S.Integer(j+6-q)*s+first_order_coefficients[q][j+2]-first_order_coefficients[q][1]
        differentiated=sum(S.binomial(j,h)*(-1)**h*S.diff(P,s,h) for h in range(j+1))
        assert S.expand(direct-differentiated)==0

corrections=[]
for q in (0,1):
    P=(6-q)*s-s*s/2-(5-q)
    # Every number must stay exact.
    P=S.Rational(6-q)*s-s*s/S.Integer(2)-S.Integer(5-q)
    expected=-x*((7-2*q)+(11-2*q)*x)/(1+x)**3
    assert S.factor(cosine_poly(P)-expected)==0
    assert cosine_poly(P).subs(x,0)==0
    corrections.append({'q':q,'P':str(P),'cosine_transform':str(expected)})

output={'constants':records,'first_order_derivative_coefficients':{str(q):[str(c) for c in cs] for q,cs in first_order_coefficients.items()},'first_corrections':corrections,'status':'exact_checks_pass'}
print(json.dumps(output,indent=2))
