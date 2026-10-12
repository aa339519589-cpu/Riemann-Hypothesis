# Explicit tails covered by the full-Gamma tiny allowance

This lemma supplies the omitted-sample and remote-image inequalities used
by [certify_continuous_residual_components.py](full_gamma_certificate/certify_continuous_residual_components.py) at epsilon=1/8 in [ACTUAL_FULL_GAMMA_CERTIFICATE.md](ACTUAL_FULL_GAMMA_CERTIFICATE.md). It addresses
the omitted cross-lattice and remote-image bookkeeping qualification. It does
not change the source inputs, trial functions, or numerical error budget.

Use the actual constants T=65, rank r=373, R=209/100, and source periods
20<=L<=24. The original theta weight satisfies

    m(x)<=sqrt(Astar) exp(2|x|-(pi/2) exp(2|x|)),
    Astar=4pi^2(125/121)<81.

## Uniform theta tails

Write E=exp(2a), a>=4. Direct integration of the squared envelope gives

    ||m 1_(|x|>a)||_2^2
      <=Astar exp(-pi E)(E/pi+1/pi^2).

The right side decreases as E increases. At a=4, use 2<exp(1)<3 and
3<pi<4. Thus E>256, E<3^8, and

    Astar(E/pi+1/pi^2)<81(3^8/3+1/9)<2^18,
    exp(-pi E)<2^(-768).

Consequently every such continuous tail has norm <2^(-375). The squared
envelope decreases on x>=0, so the same bound holds for the weighted
infinite-lattice tail at mesh h=1/128 with |jh|>4, by comparison with the
integral. This includes the endpoint convention: the samples at +/-4
belong to the retained grid.

We also have

    m_env(4)<2^(-3733),     ||m||_1<2.

For this sharpened pointwise bound, exp(1)>65/24>8/3 from the
first five positive exponential-series terms. Hence E=exp(8)>(8/3)^8
>2500, while E<3^8<2^13. Thus pi*E/2>3750, and
m_env(4)<9*2^13*2^(-3750)<2^(-3733).

The second estimate follows by integrating the unsquared envelope:
||m||_1<=(2 sqrt(Astar)/pi) exp(-pi/2)<6 exp(-3/2)<2.

## Exact trial coefficient bound

The input matrix has 1274*373<2^19 coefficients, denominator 2^42,
and every absolute numerator is below 2^37. Therefore, without using
any floating coefficient norm,

    S0=sum_(q,j)|a_qj|<2^14,
    ||(Y_j(x))_j||_ell2<=S0 exp(-x^2).

All estimates below use this conservative bound rather than the smaller
computed coefficient sum.

## 1. Omitted cross-Gram samples

The code evaluates the cross lattice using the EXACT PERIODIZED input
row g_j^per=P_20 rho(D)e_j, followed by separately paid coefficient
rounding. It does not use the unperiodized Bessel row on that lattice.
Section 2's explicit Fourier-coefficient bound gives

    ||(g_j^per(x))_j||_ell2<2^13  for every real x.

The Frobenius norm of its cross integrand with the exact trial row is
therefore bounded by 2^13*S0*m(x)*exp(-x^2). Monotone right-Riemann
comparison on the mesh h=1/128 bounds the omitted |jh|>4 lattice by

    2*2^13*S0*integral_4^infinity m_env(x) exp(-x^2) dx
      <2^28*m_env(4)<2^(-3705).

The same bound pays an omitted continuous cross integral if needed.
For the actual midpoint Fourier polynomial, the script directly asserts
its coefficient-row sum Cg0<10^6<2^20. Thus even bounding that rounded
polynomial directly gives an omitted cross tail below

    2*2^20*2^14*m_env(4)<2^(-3698).

Its coefficient error is also already paid by the separate input radius;
no double-use of an unweighted image bound is needed. These tails belong
to crossError's 10^(-100) allowance, distinct from the whole-line
trapezoid alias error and the residual's own 10^(-100) allocation.

## 2. The input-period remote tail

For each input basis vector, ||e_j||_1<=sqrt(2R)<3. The exact periodized
row has Fourier coefficients rho(t_k) ehat_j(t_k)/(2L), where
t_k=pi k/L and |t_k|<=2T. For 20<=L<=24 there are fewer than 2^12
retained integer frequencies. Hence its full real-axis row norm is at most

    (2^12*3*sqrt(r))/(2L)<2^13.

The unperiodized row is bounded by 7. Their difference is therefore below
2^14 everywhere. On |x|>20 its m-weighted L2 norm is less than

    2^14 ||m 1_(|x|>20)||_2<2^(-361).

This estimate concerns the exact periodic input and the exact whole-line
input. Scalar conversion and finite-sum rounding remain covered by the
separate numerical coefficient allowances.

## 3. The Q^2 C_N remote-image tail

The source's proved absolute periodized-kernel bound for K*K is <4T,
where K is the inverse Fourier transform of rho. The sum of the absolute
nonzero images is bounded by the same constant. For N=3 the actual signed
prime multiplier has ||C_N(D)||_(L1->L1)<=c_N<8. Therefore

    ||C_N(mY)||_(L1;ell2)<=c_N*S0*||m||_1<2^18.

The row norm of its nonzero periodic images is bounded by
4T*2^18<2^27. In the remote output region |x|>24, the m-weighted norm
is accordingly less than 2^27*2^(-375)=2^(-348).

The central-region K*K image estimate, the nonzero images of the separate
local C_N term, and the source tail in the inner convolution remain the
distinct bounds already supplied by the continuous-residual program and
its analytic proof. The estimate here pays the remote-output remainder
that was placed in the generic tiny allowance.

## Combined allowance and scope

The three missing pieces have total norm/Frobenius error less than

    2^(-3698)+2^(-361)+2^(-348)<2^(-347)<10^(-100).

If both the cross integral and cross lattice tail are charged, their sum
with the other pieces is still <2^(-347). The code allocates these pieces
in separate crossError and residual tiny terms; this stronger combined
bound also suffices. Thus the existing 10^(-100)
allowance suffices with no change to the residual or Gram thresholds.
The unweighted Gaussian eY tail is much larger and is paid separately by
the program's explicit Gaussian-tail term; it is not included here.

Inputs are the complete original theta envelope, the exact dyadic trial
data and normalized basis, the rho frequency support, and the already
proved absolute K*K periodized-kernel bound. This lemma does not certify
the other analytic estimates, numerical inertia, another depth, or RH.

The final-current independent review is [REFEREE_FULL_GAMMA_TINY_TAIL.md](REFEREE_FULL_GAMMA_TINY_TAIL.md). The exact constant comparisons are reproduced by [check_full_gamma_tiny_tail.py](check_full_gamma_tiny_tail.py); that script alone is not an analytic or spectral certificate.
