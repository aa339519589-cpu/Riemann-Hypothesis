"""Independent exact check of the actual displayed +B lambda-ray labels."""
from fractions import Fraction as F
from itertools import product

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def scale(x,n): return (n*x[0],n*x[1])
def tr(x): return 2*x[0]-x[1]
def mod1(x): return x % 1
def mod9(x): return (x[0]%9,x[1]%9)
lam=(1,2); l2=mul(lam,lam); l3=mul(l2,lam)
cs=[(a2,a3,add((1,0),add(scale(l2,a2),scale(l3,a3))))
    for a2,a3 in product(range(3),repeat=2)]
assert len({mod9(c) for _,_,c in cs})==9
labels=set()
for A,B in product(range(3),repeat=2):
    T=(A,B); labels.add((B%3,(2*A-B)%3))
    def ray(c): return mod1(F(tr(mul(mul(T,lam),sub(c,(1,0)))),27))
    for a2,a3,c in cs:
        assert ray(c)==mod1(F(B*a2+(2*A-B)*a3,3))
        assert mod1(3*ray(c))==0
        for _,_,d in cs:
            assert ray(mul(c,d))==mod1(ray(c)+ray(d))
            f3=mul(mul(d,d),d)
            assert mod9(f3)==(1,0)
            # t*lambda^(-3)=T*lambda/27 exactly.
            phase=mod1(F(tr(mul(mul(T,lam),mul(c,f3))),27))
            zeta=mod1(F(tr(mul(T,lam)),27))
            assert phase==mod1(zeta+ray(c))
assert len(labels)==9
# Actual matrix-word parameters, without importing the user's coset permutations.
omega=(0,1); omega2=(-1,-1)
assert add((2,3),omega2)==lam
assert add((-1,-3),omega)==scale(lam,-1)
print('ALL_PASS: actual +B trace labels, 81 evaluations, 729 multiplicativity')
print('and source phase identities; primary cube congruence; two exact lower words.')
