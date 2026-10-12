# An executed full-Gamma, signed-prime resolvent certificate

The complete original even theta jump form satisfies E(q) >= (3/8) Var_nu(q). This report certifies that bound at epsilon=1/8 through an actual 373-dimensional resolvent Gram retaining the complete Gamma multiplier and the finite-prime translations off diagonal. Six independently rerun programs enclose the whole-line residual, actual signed prime matrix and rational inertia: one negative and 372 positive directions. This is a new executed certificate for the exact-base framework; the already certified gap remains 3/8.

The separate [multiband theorem](MULTIBAND_COMPRESSION.md) constructs smaller finite spaces with ranks 58,77,127,853 and complete norm-error budgets. No Gram sign is supplied for those different spaces, so their ranks do not replace the 373-dimensional certificate here. The critical 1/2 bound and RH remain unproved.

## Original objects and proof dependencies

Work on full even L2(R,dx), with Phi(x)=sum_(n>=1)(4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2))exp(-pi n^2 exp(2x)), omega=2cosh(x/2), p=Phi omega, dnu=p dx, Uq=sqrt(p)q and m=sqrt(Phi/omega). The original operator satisfies U L U^(-1)=1/2+H, H=B-V, B=m b(D)m, b(t)=Re psi(1/4+it/2)-psi(1/4). Its unique ground direction sqrt(p) has H eigenvalue -1/2. V=m C_N(D)m plus the complete prime-power tail, where C0=EulerGamma+pi/2+3log2+logpi and C_N(t)=C0+2 sum_(2<=n<=N) Lambda(n)n^(-1/2)cos(t log n). These are the original closed-form realizations, not separately mean-zero compressions of B and V.

The exact operator/domain identity, full prime tail delta_N=(20Astar/9)(N+1)^2 exp[-pi(N+1)] with Astar=4pi^2(125/121), theta bounds and original even compact-smooth operator core are proved in [REPORT.md, Sections 1, 8 and 9](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261012_adaptive_spectral_tail/REPORT.md). The exact changed positive base and full-space signed comparison are proved in [POLYNOMIAL_ACCURACY_TAIL.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261012_adaptive_spectral_tail/POLYNOMIAL_ACCURACY_TAIL.md). The actual rank-373 full norm tail is the epsilon=1/8 case of [GLOBAL_POLYNOMIAL_COMPRESSION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261012_adaptive_spectral_tail/GLOBAL_POLYNOMIAL_COMPRESSION.md), with its reproducible parameter certificate. No unproved finite-matrix sign is inherited from those approximation results.

Part I supplies the continuous numerical proof. Appendices A-C contain the complete new signed-Gram counting, actual theta strip and full-line periodization arguments used by that proof. The Fourier sign convention in these even real calculations does not change any displayed symbol or Gram.

## Part I. Actual full-line residual and finite inertia

### 1. Exact operator and exact finite input space

Use the reviewed original H=B−V, B=m b(D)m on the full even L2 space. Let N=3,

 C_N(t)=C0+2(log2)/sqrt2 cos(t log2)+2(log3)/sqrt3 cos(t log3),
 delta_3=(20Astar/9)16 exp(−4pi),
 epsilon=1/8, e=epsilon−delta_3,
 T=65, k=14, R0=109/100, R=209/100, eta=1/32.

The full-prime tail ||V−V_N||<=delta_3 is unchanged. Let rho be the reviewed k-fold-box flat-top window, scaled by T, and put

 d(t)=b(t)−(1−rho(t)^2)C_N(t), A=m d(D)m+e.

The actual parameter certificate proves d>=b/100, A>=e>0, and the full original comparison

 H+epsilon >= A−m rho(D) C_N(D) rho(D)m.

The complete Gamma multiplier b is retained. No prime diagonal majorant is used.

Let r=373 and use the normalized even Legendre basis

 e_j(x)=sqrt((4j+1)/(2R)) P_(2j)(x/R) 1_[−R,R](x), 0<=j<r.

The reviewed global-polynomial theorem gives the literal full-operator approximation error <eta. Define the actual inputs f_j=m rho(D)e_j, the true Gram

 G_ij=<f_i,A^−1 f_j>,

and the actual signed finite-prime matrix D_ij=<e_i,C_N(D)e_j>. The target finite certificate is the one-sided reviewed condition

 G<=G_plus>0, D<=D_plus,
 Ccert=(31/32)G_plus−G_plus D_plus G_plus

having at most one strictly negative direction. This suffices for the original even mean-zero inequality H>=−1/8, equivalently L>=3/8 there.

### 2. Exact trial vectors, not a floating inverse

The only trial data needed are in trial_cosine_dyadic.npz. They are an integer matrix (n_(qj)) and the integer denominator exponent 42. Define, exactly,

 Y_j(x)=exp(−x^2) sum_(q=0)^1273 [n_(qj)/2^42] cos(pi q x/20).

These are real, even, whole-line functions. All coefficients are dyadic rationals; the frequencies are exact pi q/20, not the rounded frequencies of an FFT. The stored integers have modulus below 2^53, so their conversion followed by division by 2^42 is exact in binary64. Each Y_j is in the actual operator domain D(B)=D(A): mY_j has all the required Sobolev regularity and the reviewed analytic-strip envelopes.

Let F be the column map of the actual f_j, Y the column map of these exact Y_j, and Rop=F−AY. We certify the whole-line operator bound by the stronger Hilbert–Schmidt bound

 ||Rop|| <= ||Rop||_HS < 1/100000.

The actual evaluated upper bound is below 2.004e−6. The much smaller exploratory grid residual is not used as a substitute for this continuous bound.

For I=F*Y,

 G−I=F*A^−1 Rop,
 ||G−Herm(I)||<=||F|| ||Rop||/e <=(3/2)||Rop||/e.       (1)

The last inequality follows from ||rho(D)Pi_r||<=1 and the actual ||m||_infinity<3/2. Thus only the cross Gram and a continuous residual are needed; no floating inverse is certified. The fixed trial coefficients may be found in any manner because the final residual identities are checked for their exact stated values.

### 3. Directed scalar tables

All nonalgebraic scalar evaluations used in the finite arithmetic are separately enclosed.

#### 3.1 Exact input Fourier transform

For the Fourier transform convention integral exp(−itx)f(x)dx,

 ehat_j(t)=sqrt(2R(4j+1)) (−1)^j spherical_j_(2j)(Rt).

verified_scalar_tables.py encloses all rho(t_q)ehat_j(t_q), t_q=pi q/20, 0<=q<=827. The next frequency exceeds 2T. It uses 360-decimal-digit interval arithmetic, rather than trusting a special-function library's floating output.

For completeness, spherical_j_n(x) is evaluated by the exact series

 j_n(x)=x^n/(2n+1)!! sum_(l>=0) a_l,
 a_0=1, a_(l+1)/a_l=−x^2/[2(l+1)(2n+2l+3)].

Two anchors at n=766,767 are interval-summed. After l>50 the terms are decreasing for every x used here (0<=x<2TR<272); the next term bounds the alternating remainder. The recurrence j_(n−1)=(2n+1)j_n/x−j_(n+1) then gives all required even orders. At x=0 the exact values are used. Interval recurrence wrapping is explicitly retained, and every converted scalar is verified within 2^−44 of its stored binary64 value. The exact box-convolution CDF formula gives rho, also with outward arithmetic.

#### 3.2 Theta, trigonometric, and complete Gamma tables

verify_fft_elementary_tables.py and its box24 version enclose:

- the needed exact roots of unity cos(2pi j/Ngrid);
- m(j/128) and exp(−(j/128)^2) for −512<=j<=512;
- d(pi j/L), with L=20 or 24, and the other exact constants.

The real theta series retains n=1,...,4 and encloses its complete positive normalized remainder by

 5^4 exp(−24pi)/[1−(6/5)^4 exp(−11pi)].

The complete Gamma values use the recurrence to z=257/4+it/2, followed by eight Bernoulli terms. The needed formula follows by differentiation of [DLMF's Binet formula](https://dlmf.nist.gov/5.9.E10):

 psi(z)=log z−1/(2z)−2 integral_0^infinity t/[(t^2+z^2)(exp(2pi t)−1)]dt.

Expanding the last denominator through eight terms gives remainder at most

 |B18|/[18 cos(arg z)|z|^18] <= 43867/[798*18*64^18].

Indeed |t^2+z^2|>=cos(arg z)(t^2+|z|^2), and the Bernoulli moment gives the displayed bound. This remainder is explicitly added before the 64 recurrence shifts are undone. The identity psi(1/4)=−EulerGamma−pi/2−3log2 completes b. Thus no unbounded Gamma tail has been truncated without payment.

The reported uniform scalar conversion bounds are 2^−52 for cosine and Gaussian values, 2^−50 for m, and 2^−44 for b,d. The actual maximal errors are smaller. The full scalar tables are generated from exact rational parameters and interval pi/logarithms.

### 4. Explicit continuous residual ledger

Use mesh h=1/128. The exact trial cosines and the input periodization use period 40. The source f=mY is periodized independently with period 48 for applying d(D). This is legitimate: mY is a whole-line rapidly decreasing function; its trial cosine period need not equal its source periodization length.

All numerical sums in the residual evaluation are explicit real cosine matrix products. No FFT implementation error is assumed away. The verified scalar tables and elementary binary64 dot-product bounds enclose those products. The Gaussian term eY remains a whole-line Gaussian term throughout.

#### 4.1 Finite arithmetic model and outward norms

The standard binary64 round-to-nearest model is used, with unit roundoff u=2^−53. All operands are finite, no overflow occurs, and possible underflow is covered by additive multiples of 2^−1074. For an inner dimension n, the code uses the conservative gamma_(4n+8) bound. Thus

 ||fl(XY)−XY||_F <=gamma_(4n+8)||X||_F||Y||_F

with a subnormal allowance. Input radii are propagated before this multiplication bound is added. Norms are not trusted floating scalars: if s=fl(sum X_ij^2), they are bounded outward by

 sqrt[(s+4*number_of_entries*2^−1074)/(1−gamma_(2*number_of_entries+4))].

All scalar error accumulation and all final comparisons occur in mpmath.iv. The computed cosine products therefore represent interval-enclosed finite operations on exact binary-rational data and outward-enclosed scalar functions. BLAS is used only for proposed midpoint products, and its dot products are charged the displayed operation-count bound; no computed eigensolver output is used as a certificate without a subsequent residual/congruence check.

#### 4.2 The finite synthesis residual and integration

Let g0(x), s0(x) denote the exact finite cosine sums whose binary-rational coefficient matrices are produced by the enclosed operations. Define the whole-line synthesis residual

 Rsyn(x)=m(x)[g0(x)−s0(x)]−e0 exp(−x^2)P(x),

where e0 is the stored binary-rational midpoint of e, and P is the exact dyadic cosine trial matrix. Differences between these synthesis coefficients and the actual input/operator coefficients are paid separately.

For a coefficient-row matrix a_q, define C_a(s)=sum_q ||a_q||_2 exp(s|nu_q|). Their outward upper bounds are calculated from positive row-norm sums. The reviewed actual theta strip gives

 integral_R |m(x+iy)|^2 dx <25, |y|<=1/2,
 integral_R |m(x+iy)| dx <=40/3.

At strip height 1/4, a bound for the integral of the analytic squared-residual extension is

 M_R=50(C_g(1/4)+C_s(1/4))^2
           +2 e0^2 exp(1/8) C_P(1/4)^2 sqrt(pi/2).

The elementary shifted-contour/Poisson estimate bounds the whole-line trapezoidal error by

 2 M_R/[exp(2pi(1/4)/h)−1].                              (2)

This follows by summing the nonzero Fourier aliases of the analytic scalar function sum_j Rsyn,j(z)^2; its real-axis integral is the squared Hilbert–Schmidt norm. The same argument applies to each cross-Gram bilinear form, with rank-free operator bound

 M_cross=(40/3)C_g(1/4)C_P(1/4)exp(1/16).

Only the samples |x|<=4 are evaluated. The omitted Gaussian sample tail is bounded using monotonicity and integral_4^infinity exp(−2x^2)dx<=exp(−32)/16. All m-weighted omitted samples are below 10^−500 from the actual theta envelope, even after the finite coefficient sums. The code pays the conservative Gaussian tail norm 2|e0|C_P(0)exp(−16)/sqrt8. The code explicitly verifies C_g(0)+C_s(0)+C_P(0)<10^6, C_P(0)<14 and A1<637, so the fixed tiny remainder includes their actual sizes.

#### 4.3 Whole-line b periodization and Fourier alias

For A0=C_P(0), A1=sum_q |nu_q| ||a_q||_2, the separately reviewed actual Gaussian-trigonometric theorem proves

 ||m[P_L(b(mY))−b(mY)]||_2
   <=(12/5)(389A0+24A1) exp(−L)/(1−exp(−L)).              (3)

Here L=24 and the vector norm is Euclidean, hence the bound is Hilbert–Schmidt without an extra rank factor. The proof also establishes b(P_L f)=P_L(bf) and the literal Fourier coefficients b(pi k/L) fhat(pi k/L)/(2L).

The reviewed strip theorem gives

 ||fhat(t)||_2 <= C exp(−|t|/2),
 C=(160/9) C_P(1/2), f=mY.

With dt=pi/24, t0=pi/h, v=exp(−dt/2), the folded high-frequency alias plus omitted modes of d satisfy the pointwise bound

 (C/48)[72 S2+4 c_N S0],
 S0=exp(−t0/2)/(1−v),
 S2=exp(−t0/2)[t0^2/(1−v)+2t0 dt v/(1−v)^2
                         +dt^2 v(1+v)/(1−v)^3].          (4)

For each omitted frequency, compare its actual d value with its folded finite-grid value. The estimate |d(t)|<=18t^2+c_N, and the fact that the folded modulus is no larger than the original modulus, give (4). Multiplication by m costs at most ||m||_2<1. The very small difference between literal source samples and samples of P_L f, together with cutting the source samples at |x|=4, is covered separately by 10^−500. It is not assumed to vanish.

#### 4.4 The additional window and input periodizations

For the k=14 window, its kernel K has ||K||_1<4 and

 |K(x)|<=1/(pi|x|)[2k/(T|x|)]^k

where the right side is used away from zero. Splitting a convolution at |x|/2 gives

 |(K*K)(x)|<=16/(pi|x|)[4k/(T|x|)]^k.                   (5)

For a source supported in |y|<=Y and |x|<=X, sum the remote copies with period 2L. Since 2Ln−X−Y>=(2L−X−Y)n and sum n^(−k−1)<=1+1/k, (5) gives the explicit series bound used in the code. Apply it to C_N(mY), with |Y|<=2+log3 for its inner part. The actual real theta envelope gives ||m||_1<1, so ||mY||_1<=A0 and ||C_N(mY)||_1<=c_N A0. Indeed ||m||_1<=(2sqrt(Astar)/pi)exp(−pi/2)<1, by the substitution u=exp(2|x|). The true theta envelope pays the |y|>2 remainder, not a support assumption. Also ||K*K||_infinity<=2T/pi follows directly from 0<=rho^2<=1 and frequency support [−2T,2T]. Its pointwise far-image series then shows that the periodized K*K has uniformly bounded absolute sum <4T, which bounds this small outer-source contribution. The m-weighted |x|>2 part is paid with the actual theta L2 tail; the region |x|>L is smaller still and is included in the explicit tiny remainder.

There is also a local-shift image term: the decomposition is d=b−C_N+Q^2C_N, so the −C_N term is not silently included in the Q^2 estimate. For a nonzero image shift s=48l or 48l±log n, n<=3, the actual operator bound is

 ||M_m tau_s M_m||<=||m||_infinity m_tail(|s|/2).

This follows because either |x| or |x+s| is at least |s|/2. Every such shift has modulus at least 48−log3. Summing its rapidly decreasing theta envelope and using ||Y||_HS<=2A0 gives a bound below 10^−500. It is included in the explicit tiny remainder of the code. This separately covers m C_N(P_L f−f).

For mQe_j the source support is exactly [−R,R]. Use the analogous K bound and the estimate ||e_u||_1<=sqrt(2R)||u||_2. Multiply this operator bound by sqrt(r) when a Hilbert–Schmidt bound is required. The input period is 40; it is kept separate from the source period 48.

#### 4.5 Actual completed ledger

For the exact dyadic trials the outward calculation gives

 A0<13.166282, A1<636.672528,
 ||Rsyn||_HS<1.257e−7,
 b-periodization error <1.849e−6,
 frequency-alias error <1.0e−46,
 Q^2C_N periodization error <4.43e−23,
 input periodization error <9.59e−28,
 finite-coefficient error <2.902e−8,
 ||F−AY||_HS<2.004e−6.

All numerical inequalities are slack summaries; the program's final assertions use exact rational thresholds and interval-separated endpoints. The cross-Gram error is <1.286e−9. The final binary64 symmetrization I_mid=fl((cross+cross^T)/2) is charged an additional outward error 2u||I_mid||_F+4r^2*2^−1074 before the final Gram assertion; division by two is exact apart from the separately covered subnormal case. Equation (1), plus this cross error, is <1/30000. If I_mid is the stored symmetric cross-Gram midpoint, it follows that

 ||G−I_mid||<1/30000,
 G_plus=I_mid+(1/10000)I >=(1/15000)I>0.                (6)

This is an upper bound for the true whole-line resolvent Gram. It is not a Galerkin lower bound or a statement about a periodic inverse.

### 5. Actual signed prime matrix

Evenness reduces each pair of prime translations to

 D_ij=C0 delta_ij+2 sum_(n=2,3) alpha_n
           integral_(−R)^(R−log n) e_i(x)e_j(x+log n)dx.  (7)

Each integrand is a polynomial of degree at most 4r−4=1488. The code uses the 2048-order Clenshaw–Curtis rule, which integrates these products exactly in exact arithmetic. The nodes cos(pi j/2048), the logarithmic shift, and all normalized Legendre values are enclosed with 500-decimal-digit arithmetic. This high precision retains the full recurrence wrapping; it is not an assumption of stable floating Legendre recursion.

The exact Clenshaw–Curtis weights for even n are

 w0=wn=1/(n^2−1),
 wj=(2/n)[1−sum_(l=1)^(n/2−1) 2cos(2l pi j/n)/(4l^2−1)
                       −cos(pi j)/(n^2−1)].

Their midpoint error is bounded using the enclosed cosine table and a directed dot-product bound. All weights stay positive. Value-conversion, weight/interval-length conversion, matrix-product, coefficient, and symmetrization errors are included. Positive quadrature and exact polynomial integration show that each exact weighted evaluation map is a contraction, simplifying the conversion-error estimate. The final explicit upper bound is below 1/100000, hence

 D_plus=D_mid+(1/100000)I >=D.                          (8)

The indefinite signed prime matrix has not been replaced by a positive matrix.

### 6. Rational finite inertia

The midpoint matrices are stored binary-rational matrices. The ridges in (6),(8) and c=31/32 are exact rational numbers. Thus Ccert is a specified exact rational symmetric matrix.

The eigensolver is used only to propose a rational change-of-basis matrix W (its stored binary64 columns). The code verifies ||W*W−I||<1/1000, so W is invertible. It then encloses W*Ccert W by explicit matrix-product and data-conversion bounds. Strict Gershgorin separation gives exactly one negative direction and 372 positive directions. In particular,

 minimum positive Gershgorin lower bound >9/100000,
 negative Gershgorin upper bound <−9/100,
 congruence row error <4.1e−8.

Thus the sign is certified by a verified congruence and rational error margins, not by accepting floating eigenvalue signs. The true G may be singular; the separately reviewed signed one-sided Gram inertia theorem applies because G_plus is strictly positive.

Together with the full original norm tail <1/32, this gives at most one eigenvalue above one in the changed-base Birman–Schwinger operator. The actual original ground eigenvalue −1/2 supplies that unique negative direction of H+1/8. Hence the original even mean-zero space satisfies L>=3/8.

### 7. Reproduction and exact scope

Run in [full_gamma_certificate](full_gamma_certificate), with OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1:

    python verified_scalar_tables.py 827
    python verify_fft_elementary_tables.py
    python verify_fft_elementary_tables_box24.py
    python verify_prime_polynomial_matrix_v2.py
    python certify_continuous_residual_components.py
    python certify_signed_finite_inertia.py

The exact trial coefficient file is an input, not an output of a presumed-correct inverse. Scalar tables and matrix midpoints are reproducible outputs. The original exploratory eigensolver/FFT scripts are not needed to establish the certificate.

This computation certifies one actual finite Gram for the full-Gamma, signed-prime, epsilon-dependent framework. It does not certify an interval of depths, all epsilon tending to zero, a limiting second-eigenvalue inequality, or RH. Further depths require their actual parameter budgets, true residuals, and successful sign tests, or a separate uniform argument. Its new role is to demonstrate that the exact positive-base/whole-line residual/inertia chain is actually executable, rather than only a formal rank existence statement.

The independently reproduced environment was Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0. The six programs and exact dyadic input are attached unchanged. The scalar tables and matrix midpoints are regenerated in the displayed order; their recorded SHA256 values and the six actual result files are in [certificate_manifest.json](full_gamma_certificate/certificate_manifest.json). Different numerical backends need not reproduce identical midpoint bits, but all directed error and inertia assertions must pass. Component output labels are retained verbatim; approval of the whole theorem is documented in [REFEREE_ACTUAL_FULL_GAMMA_CERTIFICATE.md](REFEREE_ACTUAL_FULL_GAMMA_CERTIFICATE.md).

The only non-regenerable input is trial_cosine_dyadic.npz. No exploratory eigensolver, periodic-inverse program or hidden input is required. The final eigensolver merely proposes a binary-rational congruence; its invertibility and inertia are separately certified.

## Appendix A. One-sided upper Gram bounds with an indefinite finite matrix

### 1. Exact hypotheses

Retain any of the reviewed positive bases A>=e>0 on the original full even Hilbert space, the actual finite map F, and the signed finite prime matrix D. The reviewed full-operator estimate is

    ||K−F* D F||<=eta, 0<eta<1,
    G=F F* >=0.

Here the finite realization is exactly G^(1/2) D G^(1/2), with extra zero eigenvalues as necessary. The changed-base proof has already shown that a bound of at most one eigenvalue of K strictly above 1 gives the original mean-zero inequality H>=−epsilon, since the known original ground state accounts for the sole permitted negative direction.

Suppose actual computation provides finite symmetric matrices

    D<=D_plus,
    G<=G_plus,
    G_plus>0,                                                     (1)

in Loewner order. D and D_plus may be indefinite. The true G may be singular. In particular a Galerkin lower bound alone does not satisfy (1).

Set c=1−eta>0 and form the entirely finite symmetric matrix

    C_cert=c G_plus−G_plus D_plus G_plus.                          (2)

**Certificate.** If C_cert has at most one strictly negative eigenvalue, then the original mean-zero inequality H>=−epsilon follows from the reviewed full-operator estimate.

No square root or inverse of a numerically enclosed Gram matrix is required in (2).

### 2. Positive-eigenvalue counting with a signed D

For a selfadjoint finite matrix A, denote by n_+(A;c) the number of eigenvalues strictly greater than c>0. First,

    G^(1/2) D G^(1/2)<=G^(1/2) D_plus G^(1/2).

For the second comparison put S=G_plus^(−1/2)G^(1/2). Equation (1) gives SS*<=I and hence ||S||<=1. With

    A_plus=G_plus^(1/2)D_plus G_plus^(1/2),

one has exactly

    G^(1/2)D_plus G^(1/2)=S* A_plus S.

If a subspace E has <x,S*A_plus Sx>>c||x||² for all nonzero x in E, then S is injective on E and

    <Sx,A_plus Sx>>c||x||²>=c||Sx||².

The variational characterization of eigenvalue counts therefore gives

    n_+(G^(1/2)D G^(1/2);c)<=n_+(A_plus;c).                       (3)

This is only a statement about counts above a strictly positive threshold; it does not incorrectly assert Loewner monotonicity of the full signed spectra under changing G.

Finally,

    C_cert=G_plus^(1/2)(cI−A_plus)G_plus^(1/2).

Sylvester inertia gives

    n_+(A_plus;c)=n_-(C_cert).                                    (4)

Equations (3)–(4) show that the finite approximation has at most one eigenvalue greater than 1−eta. The full norm error then implies K has at most one eigenvalue greater than 1. The reviewed signed Birman–Schwinger form comparison and the actual ground state prove the asserted original-depth bound.

This proof also covers singular G; no inverse of the true Gram matrix has been used.

### 3. Obtaining the upper matrices honestly

For actual inputs f_i and graph-core trial vectors Y_i in D(A), let

    r_i=f_i−A Y_i,
    L_ij=<f_i,Y_j>+<Y_i,f_j>−<Y_i,A Y_j>.

The exact identity is

    G−L=(<r_i,A^(−1)r_j>),
    G<=L+e^(−1)(<r_i,r_j>).                                    (5)

Thus interval-enclosed L2 residual Gram entries yield an upper matrix. The residuals must be those of the actual A and actual inputs; the graph-core property by itself is not a numerical enclosure.

A simple rigorous entrywise-to-Loewner conversion is available. If a real symmetric matrix M has rational midpoint matrix M0 and certified entry radii r_ij=r_ji>=0, then

    ||M−M0||<=max_i sum_j r_ij=:r,
    M<=M0+rI.                                                   (6)

Apply this to the entire right side of (5), not separately to a Galerkin lower bound with unverified remainder. Add a strictly positive rational ridge if necessary to certify G_plus>0. Apply the same procedure to the actual polynomial prime-overlap matrix to obtain D_plus.

The resulting C_cert has rational entries if all displayed constants are rational. Its inertia can then be certified by exact rational symmetric elimination, including 2-by-2 pivots where required, or by a directed-interval LDL factorization with verified pivot signs. Matrix dimension, precision, and residual cost remain actual computational requirements.

### 4. Scope and convergence

For any fixed positive depth and finite compression, the reviewed actual operator core permits least-residual approximations with residual norm tending to zero. Thus the upper bound in (5) can converge to the true G. This does not assert that a chosen finite calculation has already attained that accuracy, and it does not prove that the desired inertia sign is true.

In particular, the interface removes an unnecessary square-root/inverse conditioning step and handles the signed prime matrix directly. It does not provide the missing all-depth spectral inequality, alter the original arithmetic probe, or turn a finite-depth lower bound into RH.

## Appendix B. The actual theta strip and Fourier envelopes

### 1. Exact theta and the multiplier

Use the original entire-in-strip theta kernel

    Phi(z)=sum_(n>=1) 2pi n² exp(5z/2)
              [2pi n²exp(2z)−3]exp(−pi n²exp(2z)),
    omega(z)=2cosh(z/2).

The series is locally normally convergent for |Im z|<pi/4, and its original modular identity gives Phi(−z)=Phi(z) there. Set m(x)=sqrt(Phi(x)/omega(x))>0 for real x.

**Theorem.** The actual m extends to a zero-free even holomorphic function on

    |Im z|<pi/6.                                               (1)

On the closed narrower strip |Im z|<=1/2 it obeys

    |m(x+iy)|²<=100 exp(4|x|−(3/2)exp(2|x|)).                  (2)

In particular no complex-zero exclusion for the original Xi function is being assumed. The object here is its explicit rapidly decreasing theta kernel Phi.

### 2. Dominance of the true first theta summand

Write Phi_n for its literal n-th summand. For x=Re z>=0, put t=exp(2x)>=1. The first summand is nonzero, since |2pi exp(2z)|>=2pi>3. For |Im z|<pi/6,

    pi Re(exp(2z))> (3/2)t,

and for n>=2,

    |Phi_n(z)/Phi_1(z)|
      <=n²(2pi n²t+3)/(2pi t−3)
                      exp[−(3/2)(n²−1)t]
      <=3n⁴ exp[−(3/2)(n²−1)].                              (3)

The last rational-factor inequality follows from pi>3 and t>=1. The ratio between successive terms n⁴exp[−(3/2)(n²−1)] for n>=2 is at most

    r=(3/2)^4 exp(−15/2)<1.

Therefore

    sum_(n>=2)|Phi_n/Phi_1|
       <=48 exp(−9/2)/(1−(81/16)exp(−15/2))<3/5.            (4)

The final inequality has an exact rational certificate: exp(1/2)>211/128 by its fourth Taylor polynomial. Replacing the exponentials in (4) by the corresponding powers of 128/211 increases the right side and still gives a rational number below 3/5. The attached standard-library Fraction script verifies it exactly.

Thus the complete Phi is nonzero on the right half of (1). Its true even identity gives the same conclusion on the left. Omega is nonzero there as well. The strip is simply connected, so Phi/omega has the unique holomorphic square root taking the positive value m(0). By analytic uniqueness that branch is even and agrees with the original multiplier on the real axis.

### 3. A uniform complex envelope

For x>=0 and |y|<=1/2, (4) and the first summand give

    |Phi(x+iy)|
      <=(8/5)·2pi(2pi+3)exp(9x/2−(3/2)exp(2x)).

Also

    |2cosh((x+iy)/2)|>=2cos(1/4)cosh(x/2)
                         >=(31/32)exp(x/2).

Here cos(1/4)>=1−(1/4)²/2=31/32. Combining the two estimates, the coefficient of exp(4x−(3/2)exp(2x)) is at most

    (8/5)·2·(22/7)·(65/7)·(32/31)<100.                       (5)

The rational script also verifies (5). Evenness supplies x<0, proving (2).

In particular, on every horizontal line |y|<=1/2,

    integral_R |m(x+iy)|dx
      <=(40/3)exp(−3/4)<40/3.                               (6)

This follows by taking the square root of (2), integrating on x>=0 and substituting u=exp(2x), then doubling.

### 4. Whole-line Fourier bounds for actual trial vectors

Use fhat(t)=integral_R f(x)exp(−itx)dx. Consider a finite vector-valued trigonometric polynomial

    Y(x)=exp(−x²) sum_(nu in F) a_nu exp(i nu x),
    A_half=sum_nu ||a_nu||_2 exp(|nu|/2).

The coefficients may be exact binary rational numerical trial data; no arbitrary continuation of a grid vector is permitted. On |y|<=1/2,

    ||Y(x+iy)||_2<=exp(1/4−x²) A_half.

For the actual source f=mY, (6) and exp(1/4)<4/3 give

    ||fhat(t)||_2<=(160/9) A_half exp(−|t|/2).               (7)

To prove (7), shift the Fourier contour to y=−sign(t)/2. The function is holomorphic on a larger strip by (1), and the double-exponential envelope makes both vertical boundary integrals tend to zero. This supplies an actual whole-line envelope, not a periodic FFT estimate.

The same estimate may be combined with the original b(t)<=18t² when bounding high-frequency aliases of b(D)f. Finite-prime multipliers C_N(t) are explicitly bounded by c_N. No derivative constant is hidden in (7); A_half is a finite, directly computable coefficient sum.

### 5. Whole-line envelope for the exact finite-compression inputs

Let e_1,...,e_r be any finite orthonormal family in the original even L2(dx) space. Let Q=rho(D), where 0<=rho<=1 and rho is supported in [−2T,2T]. Define the row vector

    z(x)=((Qe_1)(x),...,(Qe_r)(x)).

For complex x+iy the band-limited evaluation is well-defined. Bessel's inequality in the original L2 space gives

    ||z(x+iy)||_2²
      <=(1/(2pi)) integral_(-2T)^(2T) rho(t)²exp(−2ty)dt
      <=(2T/pi)exp(2T),  |y|<=1/2.                           (8)

In particular there is no artificial factor r in this bound. For the actual input row F_in(x)=m(x)z(x), the same contour argument gives

    ||F_in_hat(t)||_2
       <=(40/3)sqrt(2T/pi)exp(T−|t|/2).                     (9)

This applies to the reviewed global even Legendre compression as well as to any other finite orthonormal spatial projection. It controls a matrix row in Euclidean norm and can therefore be used without summing a separate error r times.

### 6. What remains to turn this into a residual certificate

Equations (7) and (9) control Fourier alias tails of the actual full-line functions. A sampled periodic computation must separately account for the spatial periodization of b(D)f, the finite-frequency multiplier/window, interval rounding, and the integration of the residual. In particular b(D)f generally has only the original exponential jump-kernel spatial tail even though f itself decays doubly exponentially.

The estimates above prove neither a pointwise FFT equality nor a completed Gram sign. They make that subsequent continuous error calculation possible using the unchanged theta multiplier and explicit trial functions.

### Explicit squared strip integral used in Part I

The proved envelope in Appendix B also gives, for |y|<=1/2,

 integral_R |m(x+iy)|^2 dx <=100 integral_1^infinity u exp(-3u/2)du
                           =(1000/9) exp(-3/2)<25.

The last strict inequality follows from exp(3/2)>sum_(j=0)^6 (3/2)^j/j!>40/9. Thus the constant 50 in the squared residual's two-term bound is twice a proved strip L2 bound, rather than a sampled maximum.

## Appendix C. Whole-line jump periodization and its original-weight error

### 1. Original objects and explicit trial data

Use the original m(x)=sqrt(Phi(x)/(2cosh(x/2))) and

    b(t)=Re psi(1/4+it/2)−psi(1/4),
    k(h)=exp(−|h|/2)/(1−exp(−2|h|)).

The exact normalization is

    b(D)f(x)=integral_R k(h)[f(x)−f(x+h)]dh.                 (1)

The digamma integral, with its variable replaced by 2|h|, gives (1); in particular no extra factor 2 is inserted on the full line.

Let the finite vector-valued trial be the actual function

    Y(x)=exp(−x²) sum_(nu in F) a_nu exp(i nu x),
    f(x)=m(x)Y(x),
    A0=sum_nu ||a_nu||_2,   A1=sum_nu |nu| ||a_nu||_2.       (2)

The frequencies and coefficients must be specified exactly or rigorously enclosed. They need not have any periodic relation to the numerical box chosen below. Every norm in this note is the Euclidean vector norm, so the estimates do not acquire a separate column-count factor.

We use the already reviewed original real envelope and complex-strip estimate:

    m(x)² <= Astar exp(4|x|−pi exp(2|x|)),
    Astar=4pi²(125/121)<2000/49,                            (3)
    |m(x+iy)|² <=100 exp(4|x|−(3/2)exp(2|x|)), |y|<=1/2.  (4)

Their sources are [REPORT.md](REPORT.md), Section 1, and this report, Appendix B, Sections 1–3. The latter proves holomorphicity on the larger strip |Im z|<pi/6, not merely a real-axis bound.

### 2. Direct whole-line constants

Define

    F_inf=sup_x exp(|x|/2)||f(x)||_2,
    D1=sup_x exp(|x|/2)||f'(x)||_2,
    F1=integral_R exp(|x|/2)||f(x)||_2 dx.

Then

    F_inf <= (8/5) A0,
    D1 <=25 A0+(8/5) A1,
    F1 <=7 A0,                                            (5)
    ||m exp(|x|/2)||_L2 <6/5.                              (6)

Here are proofs with explicit constants. From (3), pi>3 and exp(3)>20,

    ||m||_inf² <(2000/49)/20=100/49<9/4.

Indeed exp(4x−3exp(2x)) decreases on x>=0. Equation (4), with u=exp(2|x|), gives |m(z)|<5 on its closed strip: the maximum of 100u²exp(−3u/2), u>=1, is (1600/9)exp(−2)<25, using exp(1)>8/3. Cauchy's formula on radius 1/4 circles consequently gives |m'(x)|<=20 for real x.

Also

    sup_(x>=0) exp(x/2−x²)=exp(1/16)<16/15,
    sup_(x>=0) 2x exp(x/2−x²)<16/7.

For the second inequality, x/2−x²<=1/8−x²/2, x exp(−x²/2)<=1, and exp(1/8)<8/7 suffice. Thus the derivative term not containing a frequency is bounded by

    20(16/15)+(3/2)(16/7)=520/21<25.

This proves the first two claims in (5). Completing the square and using sqrt(pi)<2 shows

    integral_R exp(|x|/2−x²)dx
       <=2 exp(1/16)sqrt(pi)<64/15,

so F1<(32/5)A0<7A0. Finally (3), u=exp(2x), and u^(3/2)<=u² on u>=1 imply

    ||m exp(|x|/2)||_2²
       <=Astar integral_1^infinity u^(3/2)exp(−pi u)du
       <(2000/49) exp(−3)(17/27)
       <34000/(49·18·27)<36/25.                            (7)

Only elementary strict rational inequalities are used; the accompanying standard-library script checks them. The exponential lower bounds follow from the displayed finite Taylor sums in that script.

### 3. The full jump-multiplier tail

For any continuously differentiable f with the three finite quantities above, the integral in (1) converges and

    ||b(D)f(x)||_2 <= C_f exp(−|x|/2),
    C_f=9exp(1/2)D1+3F_inf+(6/5)F1.                       (8)

For |h|<=1, the mean value theorem bounds the difference in (1) by

    |h| D1 exp(−|x|/2) exp(1/2).

The elementary inequality 1−exp(−2h)>=2h/(1+2h), 0<h<=1, gives integral_(|h|<=1)|h|k(h)dh<=3, which is smaller than the permitted constant 9 in (8). For |h|>1, k(h)<(6/5)exp(−|h|/2), and

    integral_(|h|>1)k(h)dh <(24/5)exp(−1/2)<3.

This pays the f(x) term. The other term is bounded by (6/5)exp(−|x|/2)F1, using |x|<=|h|+|x+h|. These estimates prove (8), with complete large-|h| integration, not a truncated jump operator.

Since exp(1/2)<5/3, (5) yields the convenient exact coefficient bound

    C_f <=389 A0+24 A1.                                   (9)

### 4. Exact periodization and the Fourier multiplier

Let P=2L>0 and set

    P_L f(x)=sum_(j in Z)f(x+2Lj).

For the trials (2), both this series and its first derivative converge locally uniformly. The series P_L(b(D)f) converges locally uniformly by (8). Moreover

    b(D)(P_L f)=P_L(b(D)f).                                (10)

One can first prove (10) directly from (1): for small h, the sum of the translated derivative bounds makes the sum of differences absolutely integrable; for |h|>1, k is integrable and the translated f-sum is bounded. Fubini then gives (10).

Equivalently, use the Fourier convention fhat(t)=integral f(x)exp(−itx)dx and t_k=pi k/L. The exact periodic function in (10) is

    P_L(b(D)f)(x)
       =(1/(2L))sum_(k in Z)b(t_k) fhat(t_k) exp(i t_k x).  (11)

The sum in (11) is absolutely convergent. The reviewed strip lemma gives ||fhat(t)||<=C exp(−|t|/2) with explicit C, and the original b(t)<=18t² pays the multiplier. Integrating the locally uniform periodizations over one period gives the stated Fourier coefficients. Thus (11) is an actual analytic Poisson periodization identity. It is not an equality between the whole-line function and a finite FFT.

### 5. Complete original-weight error from periodic images

For all real x, the reverse triangle inequality and (8) give

    ||sum_(j!=0)b(D)f(x+2Lj)||_2
       <=2 C_f exp(−L)/(1−exp(−L)) exp(|x|/2).

Consequently the whole-line, original-m-weighted error obeys

    ||m [P_L(b(D)f)−b(D)f]||_L2(R;ell2)
       <=(12/5) C_f exp(−L)/(1−exp(−L))
       <=(12/5)(389 A0+24 A1) exp(−L)/(1−exp(−L)).         (12)

This estimate holds on the full line, not just the central period. It remains valid when the trial's trigonometric frequencies have a different period from 2L. For example, a trial with trigonometric period 40 may be evaluated using source period 48; no frequency redefinition or altered trial is implied.

The final certificate must still pay: replacing the exact periodized samples P_L f by literal f-samples; finite Fourier alias and truncation errors; all other multiplier/window terms; quadrature and interval arithmetic; and the actual finite signed inertia test. In particular the unweighted eY part of (Dbase+e)Y remains its genuine Gaussian-trigonometric whole-line function. Equation (12) bounds only the indicated m b(D)(mY) periodic-image discrepancy.

The two exact rational constant checks are `full_gamma_certificate/check_theta_strip_constants.py` and `full_gamma_certificate/check_periodization_constants.py`. Their assertions certify the elementary constants; the analytic proofs above establish their domains and uses.
