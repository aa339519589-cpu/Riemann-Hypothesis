# Certified original even spectral gap 511/1024

The full original even theta jump form satisfies

    E(q) >= (511/1024) Var_nu(q)

for every q in its original even form domain. This actual interval certificate improves the earlier 3/8 bound to 511/1024, retaining the complete Gamma multiplier, all finite-prime translations with their signs, and a rigorous norm bound for every omitted prime power. A genuine 127-dimensional resolvent Gram is now certified at epsilon=1/1024; its rational congruence has one negative and 126 positive directions.

The desired critical constant remains 1/2. The remaining difference is 1/1024. A certificate at this one depth does not prove arbitrarily small depths, a limiting inequality or RH. The other multiband spaces retain their previously stated norm-budget status unless separately certified.

## Exact inherited objects and independently checked inputs

The probability measure and unitary map are the original dnu=2Phi(x)cosh(x/2)dx and Uq=sqrt(2Phi cosh(x/2))q, with m=sqrt(Phi/(2cosh(x/2))). Here Phi is the complete positive even theta series. The original closed operator identity, ground state, even form domain and complete prime-tail bound are [REPORT.md, Sections 1, 8 and 9](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6fd81bda32183ebb0bb459b350c0565381691e56/reports/20261012_adaptive_spectral_tail/REPORT.md). The exact signed positive-base comparison is retained throughout.

The hard-frequency cover and the complete 127-dimensional norm-tail estimate are [MULTIBAND_COMPRESSION.md, Sections 1-5](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6fd81bda32183ebb0bb459b350c0565381691e56/reports/20261012_adaptive_spectral_tail/MULTIBAND_COMPRESSION.md). The supplied hardband_parameters.json is exactly its epsilon=1/1024 budget, including all band endpoints and Taylor orders. Basis scaling by 2^k changes the coordinate matrices but not that finite operator or its error bound. No sign from the previous 373-dimensional example is reused.

The three analytical tools used below have complete public proofs in [ACTUAL_FULL_GAMMA_CERTIFICATE.md, Appendices A-C](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6fd81bda32183ebb0bb459b350c0565381691e56/reports/20261012_adaptive_spectral_tail/ACTUAL_FULL_GAMMA_CERTIFICATE.md): one-sided true-Gram counting with signed finite matrices, the actual theta strip/Fourier bounds, and full-line jump periodization. The complete-Gamma Binet enclosure is proved in that report, Part I Section 3.2. The present proof separately pays its changed compact-input endpoints, hard-band quadrature, quadratic least-residual form term, sampling and finite arithmetic.

[REFEREE_CERTIFIED_MULTIBAND_GAP.md](REFEREE_CERTIFIED_MULTIBAND_GAP.md) records the independent complete mathematical and four-program review. The [exact reproduction package](gap_511_over_1024_certificate) contains both specified inputs, all four unchanged verified programs and all four actual result files.

## 1. Exact original operator and the different finite space

Use the original even Hilbert space L2_even(R,dx), H=B−V and ULU^−1=1/2+H. The actual ground vector g0 has H g0=−g0/2 and norm one. The published original operator, theta multiplier, whole-prime tail, and source-resolvent theorems are unchanged. In particular

 B=m b(D)m,
 C_N(t)=C0+2 sum_(n<=N) Lambda(n)n^−1/2 cos(t log n),
 ||V−m C_N(D)m||<=delta_N,
 delta_N=(20Astar/9)(N+1)^2 exp[−pi(N+1)],
 Astar=4pi^2(125/121).

Set epsilon=1/1024, N=4, e=epsilon−delta_4. Use precisely the already certified N=4 multiband set E, R=34/25, sigma=1/100 and eta=1/4096 in hardband_parameters.json. The positive frequency intervals, listed by endpoints divided by eight, are

 [0,16], [33,53], [69,92], [131,151], [215,230],
 [281,285], [357,371], [500,511], [726,731], [867,873].

Their total positive length is 134/8. Their Taylor remainder orders are, respectively,

 20,16,17,16,14,9,14,12,9,10.

The central band retains its ten even orders. Every other band retains orders k=0,...,n_i−1. There are exactly 127 functions. Let nu_i=0 on the central band and the interval midpoint on every other band. Rescale the reviewed carrier functions by the exact factor 2^k:

 phi_(i,k)(x)=1_[−R,R](x) (2x)^k cos(nu_i x+k pi/2)/k!.

Let F have columns f_(i,k)=m phi_(i,k). These are the actual compactly supported L2 inputs, not operator-domain trial vectors. The exact base and low symbol are

 h(t)=1_E(t) C_4(t),
 d(t)=b(t)−1_(R\E)(t) C_4(t),
 A=m d(D)m+e.

The frequency-cover certificate gives d>=b/100, so A>=e>0; this is a bounded perturbation of B on the same operator domain. It retains the complete Gamma multiplier. Define the true whole-line Gram G=F* A^−1 F and the block matrix

 D_(i,k),(i,l)=(1/pi) integral_(I_i) C_4(t)
                            [(t−nu_i)/2]^(k+l)dt,       (1)

with zero entries between distinct frequency-feature bands. All cross-band entries of the true resolvent Gram G are retained. This is the same finite operator as in the reviewed multiband theorem, just expressed in a better-scaled nonorthogonal basis.

The already verified full operator norm error is below 0.00011615<eta. By the reviewed one-sided signed-Gram inertia theorem, it suffices to produce G<=G_plus>0, D<=D_plus, with

 Ccert=(4095/4096)G_plus−G_plus D_plus G_plus             (2)

having at most one negative direction. No sign from the previous 373-dimensional Gram is transferred here.

## 2. Exact whole-line trial vectors and the quadratic identity

The sole non-regenerable trial input is trial_cosine_dyadic_eps1024_scaled.npz. Its integer matrix n_(qj) has shape 1900 by 127 and denominator exponent 44. Define exactly

 Y_j(x)=exp(−x^2) sum_(q=0)^1899 (n_(qj)/2^44) cos(pi q x/20).

All stored integers have modulus below 2^53. Their conversion and division by 2^44 are exact binary64 operations. The trial frequencies are exact pi q/20, not rounded FFT frequencies. Each Y_j lies in D(B)=D(A), since mY_j has ample Sobolev regularity and d−b is bounded. The manner in which the trial coefficients were proposed is irrelevant to the final residual certificate.

For the actual residual Rop=F−AY one has the exact operator identity

 G=2 Herm(F*Y)−Y*AY+Rop* A^−1 Rop.                     (3)

It follows, with Q0=2 Herm(F*Y)−Y*AY and rho>=||Rop||,

 0<=G−Q0<=rho^2/e.                                    (4)

This uses a quadratic least-residual upper bound, rather than the linear residual/e estimate used for the earlier executed instance. The entire form term Y*AY is separately enclosed.

## 3. A controlled analytic extension of the input

Write tilde_phi_(i,k)(x)=(2x)^k cos(nu_i x+k pi/2)/k! on the whole line, and tilde_F=m tilde_phi. The extension is used only to simplify continuous integration. It is not substituted for the true compact-input Gram.

For every k used here,

 a_k=2pi exp(2R)−4−2k/R>0.

For x>=R the logarithmic derivative of x^(2k)exp[4x−pi exp(2x)] is at most −a_k. The actual theta envelope therefore gives the two-sided Hilbert–Schmidt bound

 ||tilde_F−F||_HS^2 <=delta_F^2,
 delta_F^2=sum_(i,k) 2 Astar (2R)^(2k)
                   exp[4R−pi exp(2R)]/[(k!)^2 a_k].     (5)

The code verifies delta_F<13/10^9. This error is added to the residual norm. Independently, it is charged as delta_F||Y||_HS in enclosing F*Y. Both payments are required. The extension does not remove the original endpoint jump by assumption.

The verified whole-line trial norm is ||Y||_HS<35. Thus all cross corrections in (3) refer to the actual compact inputs.

## 4. Actual scalar interval tables

All scalar tables are enclosed with 80-decimal-digit interval arithmetic.

The elementary table supplies the exact cosine roots for period 20480, m(j/256), exp[−(j/256)^2] for |j|<=1024, the full symbol b(pi j/40)−C_4(pi j/40) for j=0,...,5120, and every value of the analytic carrier input tilde_phi on the evaluation grid. The finite arithmetic uses the exact source step 1/128, source period 80, trial cosine period 40, and residual integration step 1/256.

The actual theta sum retains n=1,...,4 and pays its full positive normalized remainder

 5^4 exp(−24pi)/[1−(6/5)^4 exp(−11pi)].

The complete Gamma values use psi recurrence through 64 shifts to z=257/4+it/2 and eight Bernoulli terms, with the actual Binet remainder

 |remainder|<=43867/[798*18*64^18].                     (6)

This is the same independently reviewed complete-Gamma formula used in the earlier actual certificate; no finite Gamma lower comparison replaces b. The component verifies the uniform binary64 conversion radii

 cosine and Gaussian: 2^−52; m: 2^−50;
 b−C_4: 2^−44; tilde_phi: 2^−42.

### 4.1 Actual hard-band quadrature tables

Each positive interval is integrated by Clenshaw–Curtis order 128. Its exact nodes are affine images of cos(pi j/128). The positive weights are evaluated with the explicit finite cosine formula and interval arithmetic, rather than accepting library quadrature outputs.

For each exact band node t, all needed cos(t j/256) values are evaluated by the identities

 cos(2u)=2cos(u)^2−1,
 cos((2k+1)u)=2cos(ku)cos((k+1)u)−cos(u).

The computation uses already available half-index entries, avoiding unstable sequential recurrence wrapping. It encloses every value, and retains conversion error below 2^−52. The weighted quadrature coefficients C_4(t)w_t/pi have conversion error below 2^−48.

The same actual quadrature also encloses (1). On each band |(t−nu_i)/2|<=1. For the largest polynomial degree 2k_max, expand each prime cosine through degree 128−2k_max about the band midpoint. Its product with the moment polynomial has degree at most 128 and is integrated exactly by the rule. The integral plus positive-weight sum error is bounded entrywise by

 [2 width(I_i)/pi] sum_(n=2,3,4) 2alpha_n
      [w_i log n]^(129−2k_max)/(129−2k_max)!,           (7)

where w_i is half the interval width, including on the central band. The sum of the resulting block norm errors is below 10^−70. Interval moment accumulation and conversion then give

 ||D−D_mid||<3.61e−12<1/10^10.

Hence D_plus=D_mid+(1/10^10)I is a valid upper matrix. The basis scaling in (1) is essential for making this certificate numerically well-conditioned; it leaves the exact finite operator unchanged.

## 5. Complete continuous operator-action error

Let f=mY. The actual decomposition applied to f is

 d(D)f=b(D)f−C_4(D)f+h(D)f.

Only the b−C_4 part is periodized, with period 80. The sharp multiplier h is integrated on its actual bands. It is never sampled as a discontinuous periodic Fourier symbol.

### 5.1 Whole-line b−C_4 periodization and sampling

Set A0=sum_q ||a_q||_2 and A1=sum_q (pi q/20)||a_q||_2, where a_q is the exact dyadic trial coefficient row. The already proved Gaussian-trigonometric periodization estimate gives

 ||m[P_L b(f)−b(f)]||_HS
 <=(12/5)(389A0+24A1) exp(−L)/(1−exp(−L)), L=40.       (8)

The local prime translations have image shifts of modulus at least 80−log4. Their actual m-weighted image tails follow from

 ||m tau_s m||<=||m||_infinity m_tail(|s|/2).

Their complete sum is below the explicitly allocated tiny remainder. Likewise, literal source samples differ from samples of their periodization only by a paid theta tail.

The reviewed theta strip theorem gives

 ||fhat(t)||_2 <=C_f exp(−|t|/2),
 C_f=(160/9) sum_q ||a_q||_2 exp(pi q/40).

With dt=pi/40, t0=128pi and v=exp(−dt/2), the complete source-FFT alias plus omitted-frequency error for b−C_4 is bounded by

 (C_f/80)(72S2+4c_NS0),
 S0=exp(−t0/2)/(1−v),
 S2=exp(−t0/2)[t0^2/(1−v)+2t0 dt v/(1−v)^2
                                      +dt^2v(1+v)/(1−v)^3].       (9)

Here b<=18t^2 and |C_4|<=c_N. The factor ||m||_2 is at most one. The evaluated bound is below 2.75e−24.

### 5.2 Sharp-band integration, including non-grid source frequencies

For the hard-band term use the exact even Fourier formula

 h(D)f(x)=(1/pi) sum_(positive I_i) integral_(I_i)
                         C_4(t) cos(tx) fhat(t)dt.       (10)

In each source Fourier integral, f is sampled on step 1/128. Band nodes need not be Fourier-grid nodes. Poisson summation and the preceding Fourier envelope independently bound their source alias by

 2 C_f exp[t_max/2−128pi]/[1−exp(−128pi)],
 t_max=873/8.

After the positive quadrature weights and |C_4| are applied, its operator-action error is at most this expression times

 c_N total_positive_band_width/pi.                     (11)

This term is explicit in the program, in addition to (9).

For |x|,|y|<=4, the kernel phases after expanding C_4 are t(x−y), t(x−y±log n). Their absolute spatial lengths are at most 8+log4. Taylor expansion about a band's midpoint through degree 127, together with exactness and positivity of the Clenshaw–Curtis rule, gives the entire hard-band quadrature error

 (2c_N A0/pi) sum_(positive I_i) width(I_i)
                         [w_i(8+log4)]^128/128!.        (12)

There is no additional exponential factor in the real oscillatory Taylor remainder. The evaluated upper bound is below 6.52e−68. The source integral uses ||mY||_L1(vector)<=A0, by the actual ||m||_1<1. For the implemented finite source sample sum, the program also directly verifies, with the already enclosed m and Gaussian values, (1/128) sum_(|j|<=512) m(j/128)exp[−(j/128)^2]<1. Thus the discrete source l1 norm is separately bounded by A0; a continuous integral estimate is not silently substituted for a sample-sum estimate. The omitted |y|>4 source and |x|>4 m-weighted target tails are separately paid by the actual double-exponential theta envelope. Thus the genuine 1/x tail of a sharp-band kernel is not mistaken for an exponentially decaying unweighted kernel.

### 5.3 Directed finite arithmetic and coefficient errors

Every numerical matrix product is an explicit real cosine product. Midpoints use binary64 round-to-nearest. For inner dimension n, the code charges gamma_(4n+8)||X||_F||Y||_F plus all propagated input radii and a subnormal allowance, where gamma_j=ju/(1−ju), u=2^−53. All outward Frobenius norms are obtained from positive sums of squares with gamma_(2 size+4), and additive terms accounting for at least four subnormal units per operation group. Diagonal multiplications, scalings, additions and final symmetrizations are charged separately. All error accumulation and final assertions use interval arithmetic.

The resulting finite b−C_4 and hard-band synthesis coefficients define exact finite cosine sums. Their differences from the actual coefficients are paid by Cauchy–Schwarz: an l2 coefficient error costs at most the square root of the number of coefficients in the l1 bound. The actual ||m||_2<1 then gives an original L2 operator-action error. It is conservative but fully retained. The total finite-coefficient contribution is below 2.278e−6 and dominates this ledger.

The scalar midpoint e0 of e is also paid as |e−e0|||Y||_HS. The script explicitly verifies A0<1000, A1<100000 and the real synthesis coefficient sums below 10^8, so the fixed tiny theta remainders include the sizes of all finite sums rather than assuming that finiteness alone supplies a numerical constant.

## 6. Continuous integration of the synthesis and the form term

The exact synthesis operator action is A_syn Y=m(s_b+s_h)+e0Y. Let R_syn=tilde_F−A_syn Y. The two synthesis coefficient sets are the exact stored binary-rational values, with their exact specified cosine frequencies.

At strip height a=1/4, let C_P(a)=sum ||a_q|| exp(a pi q/20), and let S(a) bound the corresponding total coefficient sum of s_b+s_h. For the hard-band sum it is enough to multiply the unweighted coefficient sum by exp(a t_max).

The actual theta strip implies

 integral |m(x+ia)|^2 dx<25,
 integral |m(x+ia)|^2 exp(4|x|)dx<120.                  (13)

For the second inequality, the envelope 100 exp[4|x|−(3/2)exp(2|x|)] gives exactly the upper integral 100 integral_1^infinity u^3 exp(−3u/2)du<120. For the ten carrier bands, the finite Taylor coefficient vector is bounded by sqrt(10) exp(2|x|+2a+a t_max). Thus the following bounds are valid for the strip integrals of the analytic squared-norm extensions:

 M_Y=exp(2a^2) C_P(a)^2 sqrt(pi/2),
 M_F=120*10 exp(4a+2a t_max),
 M_A=2[25 S(a)^2+e0^2 M_Y],
 M_R=3[M_F+25 S(a)^2+e0^2 M_Y].                        (14)

For any such analytic integrand with strip integral bound M, shifted-contour Poisson summation bounds the whole-line trapezoidal error on step h=1/256 by

 2M/[exp(2pi a/h)−1].                                 (15)

For the cross products use M=sqrt(M_F M_Y) or sqrt(M_A M_Y). These are rank-free operator bounds obtained by Cauchy–Schwarz on the vector integrands. For the squared residual and trial norm use M_R and M_Y.

Only samples |x|<=4 are evaluated. The omitted Gaussian trial norm is bounded by

 T_Y=2 A0 exp(−16)/sqrt8.

It is included in the trial norm and as |e0|T_Y in the synthesis residual. The omitted form samples include the separate term |e0|T_Y^2, because Y*A_synY contains e0|Y|^2. All remaining omitted products contain m and are below the separately charged theta remainder. No Gaussian-only tail is silently called a theta tail.

Let E_A bound ||AY−A_synY||_HS using Section 5. The complete ledger then uses

 ||F−AY||_HS <=||R_syn||_HS+E_A+delta_F,
 cross error <=finite arithmetic+quadrature+delta_F||Y||_HS,
 energy error <=finite arithmetic+quadrature+E_A||Y||_HS
                                  +|e0|T_Y^2+tiny remainder.       (16)

The error in the symmetric midpoint Q_mid for Q0 in (3) is at most twice the cross error plus the energy error and the explicitly charged final symmetrization/combination rounding.

## 7. Actual completed bounds and exact finite inertia

The directed computation gives the slack bounds

 A0<366.786, A1<18972.94, ||Y||_HS<34.111,
 delta_F<1.265e−8,
 ||R_syn||_HS<1.855e−8,
 E_A<2.278e−6,
 ||F−AY||_HS<2.310e−6<1/400000,
 ||Q0−Q_mid||<7.858e−5,
 rho^2/e<8.40e−9,
 ||G−Q_mid||<1/12000.                                 (17)

The actual final assertions compare outward endpoints to exact rational thresholds. From G>=0 and (17),

 G_plus=Q_mid+(1/10000)I>=G,
 G_plus>=(1/60000)I>0.                                (18)

The earlier upper matrix D_plus=D_mid+(1/10^10)I is used in (2). Its entries and the midpoint Q_mid are exact binary-rational data; both ridges and c=4095/4096 are exact rationals.

The final program proposes a binary-rational congruence matrix W, checks its invertibility by ||W*W−I||<1/1000, and encloses W*Ccert W with the full multiplication, ridge-conversion and symmetrization errors. Strict Gershgorin separation verifies

 exactly one negative and 126 positive directions,
 minimum positive Gershgorin lower bound >6/100000,
 negative Gershgorin upper bound <−1,
 total congruence row error <3e−9.                     (19)

Floating eigenvalue signs are not accepted as a proof: the eigensolver only proposes W; (19) follows from the verified congruence of the specified exact rational matrix.

The independently accepted chain (2), (18), (19) and the full multiband norm tail imply at most one negative direction for H+1/1024. The actual ground eigenvalue −1/2 supplies one such direction. Its orthogonal complement therefore satisfies

 H>=−1/1024, equivalently L>=511/1024.

This is a single depth. An all-epsilon sign theorem or a uniform limiting argument is still required for the critical conclusion.

## 8. Reproduction

Run in [gap_511_over_1024_certificate](gap_511_over_1024_certificate), with OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1:

    python verify_hardband_scalar_tables_scaled.py
    python verify_hardband_quadrature_tables.py
    python certify_hardband_continuous_residual_v4.py
    python certify_hardband_signed_inertia.py

The exact inputs are hardband_parameters.json and trial_cosine_dyadic_eps1024_scaled.npz. All other tables, midpoints, congruence proposals and component outputs are reproducible. The parameter JSON is the already certified epsilon=1/1024 case of the physical-first multiband theorem. Neither the trial-proposal scripts nor any exploratory periodic eigenvalue calculation is needed to reproduce these checks.

The independently reproduced environment is Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0, with the two thread variables above set to 1.

The precise input/program/result hashes and reproducible binary-table hashes are in [certificate_manifest.json](gap_511_over_1024_certificate/certificate_manifest.json). Only the dyadic trial and parameter JSON are independent inputs; the large scalar/quadrature tables, least-residual matrix and congruence proposal are regenerated by the four displayed commands. Historical component labels are retained unchanged: the whole theorem relies on every directed test passing together, as checked by the accompanying independent review.

## Explicit tiny-remainder proof supplement, 2026-10-12

The original proof named the omitted source/lattice and remote-output objects but did not expand their fixed constants. [MULTIBAND_TINY_TAIL.md](MULTIBAND_TINY_TAIL.md) supplies those bounds for this exact 127-column implementation, with its [independent review](REFEREE_MULTIBAND_TINY_TAIL.md). In particular it uses the actual extended carrier input, the period-80 source DFT and the nonperiodized sharp-band integral. The user's earlier [373-column correction](FULL_GAMMA_TINY_TAIL.md) prompted this separate check; it is not substituted for the different 127-column proof. Every omitted term fits its existing allowance. All four programs, exact inputs, generated matrices, numerical outputs and the single-depth 511/1024 conclusion remain unchanged. This proof completion yields no new spectral depth or zeta-zero exclusion.
