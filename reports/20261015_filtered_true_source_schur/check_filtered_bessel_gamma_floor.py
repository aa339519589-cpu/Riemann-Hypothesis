"""Final arithmetic for a complete trace-zero source Gamma LOWER bound.
Run only with the main and complete-prefix validated moment certificates.
This does not evaluate the full original Schur form.
"""
import json,os,math
from mpmath import iv
import certify_filtered_bessel_moments as q
from certify_unrepaired_head_kernel import psi_complex
iv.dps=90
base=os.path.dirname(__file__)
main=json.load(open(os.path.join(base,'filtered_bessel_main_moments.json')))
pref=json.load(open(os.path.join(base,'filtered_bessel_prefix_moments.json')))
def V(x):
 if isinstance(x,list):return iv.mpf([iv.mpf(x[0]).a,iv.mpf(x[1]).b])
 return iv.mpf(x)
pi=iv.pi;A=iv.mpf(16);nu=iv.mpf(9)/4
# Exact source trace: first two complete future labels; all n>=4 tail <1e-60.
cb=iv.mpf(0)
for n in [2,3]:
 z=4*pi*n*n;W=q.wjet(z,2*n)[0];u=q.ujet(z-A)[0];cc=8*z**3-30*z*z+15*z
 cb+=2*z*cc*iv.exp(-z)*u/W/iv.sqrt(n)
cb+=iv.mpf(['-1e-60','1e-60'])
z=4*pi
psib=iv.sqrt(2)*sum((8*(j*j*z)**3-30*(j*j*z)**2+15*(j*j*z))*iv.exp(-j*j*z) for j in range(1,13))
psib+=iv.mpf(['-1e-90','1e-90']);cb/=psib
assert bool(abs(cb).b<iv.mpf('6e-16'))
# Elementary endpoint, complete Gaussian, and neutral-gauge envelopes.
assert bool((5*27**3/iv.exp(29)).a>iv.mpf('1e-8'))
assert bool((8/pi**(iv.mpf(1)/4)*12**(iv.mpf(19)/4)*iv.exp(-12)/(1-iv.mpf(19)/48)).b<10)
assert bool((256/iv.sqrt(pi)*12**(iv.mpf(11)/2)*iv.exp(-24)/(2-iv.mpf(11)/24)).b<1)
# Main omitted onset: |F|<=.002*s^(9/4) on 0<s<.001, W>=1.
W0=q.wjet(A,2)[0];assert bool((W0-iv.mpf('.001')*q.wprime_abs(A,iv.mpf('.001'),2)).a>1)
on=8*iv.mpf('16.001')**3*iv.exp(-16)/iv.gamma(nu+1)*iv.exp(2*iv.sqrt(iv.mpf('.016')))*iv.mpf('1.001')**6*iv.mpf('.001')**(nu+1)/(nu+1)
assert bool(on.b<iv.mpf('2e-13'))
# Far tails from W>=1e-8*z^(-1/4), |u|<=64*z^nu/Gamma(nu+1).
CF=8*64*10**8/iv.gamma(nu+1)
far=CF*128**(iv.mpf(33)/4)*iv.exp(-128)/(1-iv.mpf(33)/(4*128))
assert bool(far.b<iv.mpf('1e-25'))
assert bool((iv.sqrt(2)/pi**(iv.mpf(1)/4)*far).b<iv.mpf('1e-25'))
far2=CF*CF/pi*128**13*iv.exp(-256)/(2-iv.mpf(13)/128)
assert bool(far2.b<iv.mpf('1e-58'))
z4=64*pi
assert bool(((iv.mpf(5)/4)**13*iv.exp(-36*pi)).b<iv.mpf(1)/2)
trace4=2*CF*z4**(iv.mpf(13)/2)*iv.exp(-z4)
assert bool(trace4.b<iv.mpf('1e-60'))
# Future-prefix L1 and full-odd L2 tail corrections, including z>128.
EP=V(pref['prefix_L1_upper'])+iv.mpf('1e-25')
EN=V(pref['prefix_full_L2_squared_upper'])+iv.mpf('1e-58')
R=iv.mpf(24);J=10;B=iv.mpf(0)
for j in range(J):
 mu=abs(V(main['moments'][j]))+iv.mpf('2e-13')/10**j+iv.mpf('1e-25')+EP+10*abs(cb)
 B+=2*mu*R**j/math.factorial(j)
absJ=V(main['abs_moment_J_upper'])+iv.mpf('2e-13')/10**J+iv.mpf('1e-25')+EP+10*abs(cb)
B+=2*R**J/math.factorial(J)*absJ
norm=iv.sqrt(V(main['full_mass']).a)-iv.sqrt(EN)-abs(cb)
assert bool(norm.a>0)
M=norm**2
ar=psi_complex(R)[0]-iv.log(pi)
assert bool(ar.a>0)  # Also licenses the same conservative mass lower bound for uncorrected t.
a0=-iv.euler-pi/2-3*iv.log(2)-iv.log(pi)
G=ar*M-R/pi*(ar-a0)*B*B
print('Trace gauge interval:',cb)
print('Uniform unnormalized Fourier bound |hat(T)| on [-24,24]:',B)
print('Complete full-odd source mass lower:',M.a)
print('Complete Gamma lower:',G.a)
assert bool(G.a>iv.mpf('3e-9'))
print('SUCCESS: both the trace-repaired and the UNCORRECTED true source Gamma energies >3e-9.')
