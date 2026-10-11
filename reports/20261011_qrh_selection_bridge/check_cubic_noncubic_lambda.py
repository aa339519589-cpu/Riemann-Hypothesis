"""Exact finite arithmetic for the nine primary lambda-ray cusp channels.

Checks matrices and source coset words. Automorphy, supplementary laws and
analytic continuation are mathematical inputs, not certified by this script.
"""
from fractions import Fraction as F
from itertools import product


def add(x,y): return (x[0]+y[0], x[1]+y[1])
def scale(x,n): return (x[0]*n,x[1]*n)
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def conj(x): return (x[0]-x[1],-x[1])
def norm(x):
    a,b=x
    return a*a-a*b+b*b
def mod(x,n): return (x[0]%n,x[1]%n)
def quotient(x,y):
    z=mul(x,conj(y)); q=norm(y)
    assert z[0]%q==z[1]%q==0
    return (z[0]//q,z[1]//q)
def trace(x): return 2*x[0]-x[1]

LAM=(1,2)
UNITS=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
D4=[d for d in product(range(4),repeat=2) if norm(d)%2]
assert len(D4)==12
assert mul(LAM,LAM)==(-3,0)

def psi(d):
    return 1 if norm(d)%4==1 else -1

def rho_exp(d):
    return {(1,0):0,(0,1):1,(1,1):2}[mod(d,2)]

# Exact sum psi(d)*omega^(j rho(d)); each group coefficient vanishes.
for j in range(3):
    counts=[0,0,0]
    for d in D4: counts[(j*rho_exp(d))%3]+=psi(d)
    assert counts==[0,0,0]

T9=list(product(range(3),repeat=2))
labels=set()
cases={0:0,1:0,2:0}
for T in T9:
    A,B=T
    k=(-B)%3; j=(2*A-B)%3
    labels.add((k,j))
    # trace((T/3)/lambda)=B/3, trace(T/3)=(2A-B)/3.
    assert F(-trace(mul(T,LAM)),9)==F(B,3)
    assert F(trace(T),3)==F(2*A-B,3)
    assert ((A+B)%3 != 0)==(j != 0)
    if T==(0,0):
        cases[0]+=1
        continue
    is_unit=(A+B)%3 != 0
    case=1 if is_unit else 2
    cases[case]+=1
    for shift in [-1,0,1]:
        previous_mod9=None
        for d in D4:
            a0=add(add(scale(T,4),(0,12*shift)),scale(d,-27))
            c0=(12,0)
            if not is_unit:
                a0=quotient(a0,LAM)
                c0=quotient(c0,LAM)
            choices=[u for u in UNITS if mod(mul(u,a0),3)==(1,0)]
            assert len(choices)==1
            kap=choices[0]
            a=mul(kap,a0); c=mul(kap,c0)
            # Inverse modulo 36 ensures aD-1 divisible by 3c in both cases.
            invnorm=pow(norm(a),-1,36)
            D=mod(scale(conj(a),invnorm),36)
            b=quotient(add(mul(a,D),(-1,0)),c)
            assert add(mul(a,D),scale(mul(b,c),-1))==(1,0)
            assert mod(a,3)==mod(D,3)==(1,0)
            assert mod(b,3)==(0,0)
            if is_unit:
                assert mod(c,3)==(0,0)
                assert norm(c)==144
                assert mod(a,4)==mod(mul(kap,d),4)
                if previous_mod9 is None: previous_mod9=mod(a,9)
                assert mod(a,9)==previous_mod9
            else:
                assert mod(c,3) in [(1,2),(2,1)]
                assert norm(c)==48
assert len(labels)==9 and cases=={0:1,1:6,2:2}

# Source Appendix A: k_j(E), k_j(P), k_j(T), in j=1..27 order.
KE=[1,19,10,7,23,13,4,14,22,3,12,11,6,8,24,25,17,27,2,21,20,9,5,15,16,26,18]
KP=[4,5,6,7,9,8,1,3,2,14,17,11,10,13,16,18,12,15,22,21,26,23,19,27,24,20,25]
KT=[1,2,3,6,4,5,9,7,8,11,12,10,14,15,13,17,18,16,20,21,19,23,24,22,26,27,25]

def act(j,perm,power,order):
    for _ in range(power%order): j=perm[j-1]
    return j
for j in range(1,28):
    assert act(j,KE,2,2)==j
    assert act(j,KP,3,3)==j
    assert act(j,KT,3,3)==j

def lower_lambda_index(sign):
    # L(sign*lambda)=E T^(-sign) P^2 T^(-2sign) P^(-2) E^(-1).
    j=1
    for perm,power,order in [(KE,1,2),(KT,-sign,3),(KP,2,3),
                              (KT,-2*sign,3),(KP,-2,3),(KE,-1,2)]:
        j=act(j,perm,power,order)
    return j
assert lower_lambda_index(1)==19
assert lower_lambda_index(-1)==10
print('ALL_PASS: nine ray labels; 288 exact cusp matrices; 6 unit, 2 nilpotent,')
print('and 1 zero-shift channel; primitive quadratic projections; cusp indices 19/10.')
