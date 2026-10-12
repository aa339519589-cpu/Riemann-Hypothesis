"""Directed-interval scalar ledger for a finite-height/negative-depth test.

This validates the displayed elementary constants, not its mathematical hypotheses.
The original-domain second-derivative lemma and complete Weil identity must be
independently reviewed before a spectral conclusion is reported.
"""
from pathlib import Path
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
import hashlib, json
import mpmath as mp
mp.mp.dps=110
iv=mp.iv
iv.dps=90
I=iv.mpf
def endpoint(z, index):
    sign, mantissa, exponent, _ = z._mpi_[index]
    numerator = (-1 if sign else 1)*int(mantissa)
    if exponent >= 0:
        return Fraction(numerator << exponent, 1)
    return Fraction(numerator, 1 << (-exponent))
lo=lambda z:endpoint(z,0)
hi=lambda z:endpoint(z,1)
P=iv.pi
N=6
beta=I(1)/32
q=1+beta/2
height=I(3)*10**12
C0=iv.euler+P/2+3*iv.log(2)+iv.log(P)
cn=C0+2*iv.log(2)/iv.sqrt(2)+2*iv.log(3)/iv.sqrt(3)+iv.log(2)+2*iv.log(5)/iv.sqrt(5)
delta=I(980)/9*49*iv.exp(-7*P)
frequency=iv.exp(cn)
# The full-Gamma lower bound b(t)>=.5 log(1+4t²) proves this
# convenient (deliberately nonoptimal) positive-frequency cutoff.
assert lo(iv.log(1+4*frequency**2)/2-cn)>0
Gbeta=4+2**beta/beta
epsilon=beta/2
# Complete contour moments: exact polynomial integrals I0=2, I2=18,
# I4=802. Holder is applied to the positive Fourier measures, including
# the full paired-prime coefficient measure; no noninteger Gamma input.
A0=I(14)*2/P
A2=I(14)*18/P
A4=I(14)*802/P
P2=I(800)*18/P
P4=I(800)*802/P
Ap=A2**((1-epsilon)/2)*A4**((1+epsilon)/2)
P3=iv.sqrt(P2*P4)
D=16*Gbeta*2**(beta/2)*Ap**2+4*iv.sqrt(2)*P3
Lstar=2*frequency**2*A0+2*A2
W=32*height**(-3)*(iv.log(height)/3+I(1)/9)

def rounded_decimal(value, rounding):
    with localcontext() as context:
        context.prec=50
        context.rounding=rounding
        return str(Decimal(value.numerator)/Decimal(value.denominator))
def upper(z):return rounded_decimal(hi(z), ROUND_CEILING)
def lower(z):return rounded_decimal(lo(z), ROUND_FLOOR)
rows=[]
for denominator in [65536,100000]:
    kappa=I(1)/denominator
    a=kappa-delta
    assert lo(a)>0
    assert hi(delta-kappa/2)<0
    K1=iv.sqrt(2*cn/a)*Lstar
    K2=(2**q*D/a)**(1/(2-q))
    # Choose a rational integer larger than all three analytic K bounds;
    # integer upward rounding is checked again by interval comparison.
    bound=max(Fraction(1),hi(K1),hi(K2))
    Kint=(bound.numerator+bound.denominator-1)//bound.denominator+1
    K=I(Kint)
    assert lo(K-K1)>0 and lo(K-K2)>0 and Kint>=1
    eval_bound=7*K+56*iv.sqrt(K)+224
    error=eval_bound**2*W
    ratio=error/kappa
    assert hi(ratio)<1
    rows.append({
      'kappa':'1/'+str(denominator),'N':N,'beta':'1/32',
      'a_lower':lower(a),'K_second_derivative_integer_upper':str(Kint),
      'frequency_cutoff_upper':upper(frequency),
      'second_derivative_bound_branch_1_upper':upper(K1),
      'second_derivative_bound_branch_2_upper':upper(K2),
      'complex_evaluation_numerator_upper':upper(eval_bound),
      'complete_zero_tail_error_upper':upper(error),
      'error_over_kappa_upper':upper(ratio),
      'strict_scalar_test_passed':True})
report={
 'status':'Directed-interval scalar assertions passed; mathematical chain requires independent review',
 'mpmath_version':mp.__version__,'interval_decimal_precision':90,
 'complete_verified_zero_height':'3000000000000',
 'external_height_source':'https://arxiv.org/pdf/2004.09765, Theorem 1',
 'paired_prime_moment_constant':'800','theta_Fourier_L1_constant':'14',
 'weighted_derivative_L2_constant':'7','prime_tail_upper':upper(delta),
 'finite_prime_norm_upper':upper(cn),'quadratic_commutator_constant_upper':upper(D),
 'low_frequency_constant_upper':upper(Lstar),'complete_zero_tail_weight_upper':upper(W),
 'tests':rows,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out=Path(__file__).with_name('second_derivative_height_test_result.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
