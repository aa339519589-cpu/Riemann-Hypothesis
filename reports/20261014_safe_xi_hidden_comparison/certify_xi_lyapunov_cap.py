"""Outward interval endpoint certificate for the safe-ray Lyapunov cap.
This checks only the cap input, not the pending bulk scalar-potential bounds.
"""
from mpmath import iv
iv.dps=50
b=iv.ln(2)
def xi(x):
 z=iv.pi*iv.exp(2*x)
 return iv.exp(x/2-z)*z*(8*z*z-30*z+15)
def gt(x,y): assert bool(x.a>y), (x,y)
S=iv.mpf(31)/100
# The n=1 positive summand alone bounds psi(S) below.
gt(xi(S),2)
gt(xi(b+S),iv.mpf(1)/10**5)
gt(xi(b+iv.mpf(3)/100),iv.mpf(3)/100)
gt(xi(b+iv.mpf(1)/10**4),iv.mpf(1)/20)
assert bool(xi(b).b<iv.mpf(1)/10)
# psi'(0), with the same explicit n>=9 derivative-tail bound as the head checker.
p1=iv.mpf(0)
for n in range(1,9):
 z=iv.pi*n*n
 p1+=z*(iv.mpf('37.5')-165*z+112*z*z-16*z*z*z)*iv.exp(-z)
p1+=iv.mpf(['-1e-70','1e-70'])
assert bool(p1.b<17)

# Exact elementary inequalities used in the complete tail estimate.
gt(iv.exp(3),20)
gt(iv.pi*iv.exp(2*S),5)
gt(iv.exp(iv.mpf(3)/5),iv.mpf(3)/2)
assert bool((iv.exp(-iv.mpf(3)/20)/(1-iv.exp(-iv.mpf(3)/5))).b<3)
print('CERTIFIED psi(.31)>2, xi(log2+.31)>10^-5,')
print('xi(log2+.03)>.03, xi(log2+.0001)>.05, and elementary cap tail constants.')
