"""Directed checks for the complete mixed-force remainders.
MAIN phi is represented by source cells; E=Cphi-phi is paid in L2.
"""
import json,os
from mpmath import iv
iv.dps=80
B=os.path.dirname(__file__)
p=json.load(open(os.path.join(B,'filtered_bessel_prefix_moments.json')))
# Uniform doubled-cell source envelope for tiny prime-window intersections.
for name in ['filtered_bessel_main_cells.json','filtered_bessel_onset_cells.json']:
 for cell in json.load(open(os.path.join(B,name)))['cells']:
  hh=iv.mpf(cell['h']);assert bool(hh.a>0)
  bound=sum(abs(iv.mpf(co))* (2*hh)**j for j,co in enumerate(cell['F_coefficients']))
  bound+=2**26*iv.mpf(cell['F_remainder_upper'])
  assert bool(bound.b<iv.mpf('.01'))
EN=iv.mpf(p['prefix_full_L2_squared_upper'])
CF=8*64*10**8/iv.gamma(iv.mpf(13)/4)
farweighted=2*CF*CF/iv.pi*128**14*iv.exp(-256)/(2-iv.mpf(14)/128)
assert bool(farweighted.b<iv.mpf('1e-55'))
EW=iv.sqrt(128/iv.pi*EN)+iv.sqrt(farweighted)
assert bool(EW.b<iv.mpf('5e-17'))
A=iv.log(2)/iv.sqrt(8)+2*(iv.log(2)+2)/iv.sqrt(2)
assert bool(A.b<5)
assert bool((iv.pi+iv.sqrt(2)+6*A+10).b<100)
# Complete force error from the future prefix.
force_error=100*EW
assert bool(force_error.b<iv.mpf('5e-15'))
# Remaining finite-column source omissions.
delta=iv.mpf('1e-5');onL1=iv.mpf('.004')*delta**(iv.mpf(13)/4)/(iv.mpf(13)/4)
assert bool(onL1.b<iv.mpf('1e-19'))
gap=iv.log(4/iv.pi)/2
kap=iv.exp(-gap/2)/(1-iv.exp(-2*gap))
# All prime powers on the tiny onset lie below 2 exp(x_A+delta/32)<5.
onforce=iv.sqrt(2/iv.log(2))*(2*kap+20)*onL1
assert bool(onforce.b<iv.mpf('1e-17'))
farL1=CF*128**(iv.mpf(13)/2)*iv.exp(-128)/(1-iv.mpf(13)/256)
assert bool((100*farL1).b<iv.mpf('1e-20'))
# r>=200 in the Gamma coefficient row, uniformly over every sine frequency.
Ar_tail=iv.mpf('1.2e-5')*iv.exp(-iv.mpf('400.5')*gap)/(1-iv.exp(-2*gap))
gamma_tail=iv.sqrt(2/iv.log(2))*Ar_tail/iv.mpf('400.5')
assert bool(gamma_tail.b<iv.mpf('1e-20'))
assert bool((force_error+onforce+100*farL1+gamma_tail).b<iv.mpf('1e-14'))
# Primitive analytic polynomial remainders.
assert bool((iv.mpf('.8')**23/iv.factorial(23)).b<iv.mpf('1e-23'))
assert bool((iv.exp(iv.mpf('.71'))*iv.mpf('.71')**26/iv.factorial(26)).b<iv.mpf('1e-28'))
assert bool(iv.exp(5).b<256)
print('complete weighted prefix norm upper',EW.b)
print('complete finite-column added error upper',(force_error+onforce+100*farL1+gamma_tail).b)
print('SUCCESS: each true-column inflation 1e-14 and force-error L2 norm 5e-15 are valid.')
