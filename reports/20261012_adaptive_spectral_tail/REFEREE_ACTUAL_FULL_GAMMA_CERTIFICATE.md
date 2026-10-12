# Independent review: actual full-Gamma certificate

This review accompanies [ACTUAL_FULL_GAMMA_CERTIFICATE.md](ACTUAL_FULL_GAMMA_CERTIFICATE.md), its exact dyadic input, six reproducible programs and complete analytic appendices. The approved conclusion is the original full-even mean-zero gap 3/8 at epsilon=1/8.

## Part I. Complete executed certificate

### Verdict and reviewed artifact

Approved: the stated actual 373-dimensional certificate for epsilon=1/8, with the full Gamma multiplier and the finite-prime shifts retained off diagonal, establishes the original even mean-zero inequality L>=3/8. This is a successfully executed instance of the exact-positive-base framework. It is not an improvement of the already certified numerical gap, nor a uniform-in-epsilon sign certificate or an RH theorem.


The exact trial data, six programs, scalar tables, finite matrices and outputs are listed in [full_gamma_certificate/certificate_manifest.json](full_gamma_certificate/certificate_manifest.json), with binary intermediate tables identified as reproducible outputs. The continuous program reviewed here is `f113960822cf08b1dc5a27f9b010450f6fbda3cd95b413f9200a71bff18c4ca1`; the finite-inertia program is `4de2d0990e32eee368ca47caa37eac6930873f83e226b07be40e7ef78b673194`.

### 1. Actual operator comparison and true Gram

The original full even operator is H=B-V, with its actual ground eigenvalue -1/2. The reviewed prime tail, exact high-frequency base and global even-polynomial compression are used with N=3, epsilon=1/8, e=epsilon-delta_3, T=65, k=14, R=209/100 and rank 373. Their actual parameter certificate gives d>=b/100, A=m d(D)m+e>=e, and the full comparison H+epsilon >= A-mQ C_N Qm. The complete Gamma symbol b has not been replaced by a finite Gamma truncation. C_N retains the real prime shifts and is allowed to be indefinite.

The normalized even Legendre basis has degree 2j and support [-R,R]. Thus its actual input columns are f_j=mQe_j, and G=F*A^-1F is the whole-line resolvent Gram. For the exact dyadic Gaussian-cosine trial column map Y, Rop=F-AY gives G-F*Y=F*A^-1 Rop. Since ||F||<=3/2 and A>=e, the two-sided error in Herm(F*Y) is bounded by (3/2)||Rop||/e. This is not a claim that a periodic inverse or a Galerkin lower matrix equals the true G.

Every trial is a genuine whole-line, even Gaussian times a finite trigonometric polynomial. Its coefficients are the exact dyadic integers divided by 2^42; no floating inverse is assumed correct. Its membership in D(B)=D(A) follows from the previously proved actual theta strip/Sobolev bounds and the bounded change of base.

### 2. Scalar special functions and exact quadrature

The Fourier transform of the normalized even Legendre input is sqrt(2R(4j+1))(-1)^j j_(2j)(Rt). The Bessel program uses the exact series at orders 766 and 767, adds an alternating-tail interval after the terms are decreasing, and propagates intervals down the exact recurrence. For its maximal x<272 the term ratio is already below one after the stated index 50. The whole recurrence wrapping remains in the interval. Zero frequency is treated exactly. The 360-digit enclosure and the final 2^-44 scalar conversion radius were independently reproduced.

The theta table retains the positive n<=4 terms and a genuine geometric bound for every n>=5. The actual denominator 2cosh(x/2) and the original theta coefficients are correct. Trigonometric and Gaussian values are enclosed at their exact rational arguments, not rounded frequency arguments.

The full digamma calculation was checked directly from the differentiated [DLMF Binet formula](https://dlmf.nist.gov/5.9.E10). After 64 recurrence shifts, Re z=257/4. Expanding through B16 leaves the B18 remainder bounded by |B18|/[18 cos(arg z)|z|^18]. Since cos(arg z)|z|^18=(Re z)|z|^17>=64^18, the stated uniform remainder is valid even at the largest imaginary argument. It is explicitly added before reversing the recurrence. Thus all Gamma terms are represented, not only an unchecked finite asymptotic series.

The finite signed prime matrix is the literal overlap of two compact even Legendre polynomials shifted by log 2 or log 3. Each product has degree at most 1488. The Clenshaw-Curtis rule of order 2048 is exact on these products in exact arithmetic. Its positive weights and the 500-digit directed Legendre evaluation enclose the scalar conversions. Restricting either exact polynomial evaluation map to the overlap interval is a contraction; this justifies the norm bounds used for its value perturbations. Weight, interval-length, multiplication and symmetrization errors are paid. The actual D remains signed.

### 3. Whole-line continuous residual, including all images

The trial frequencies have period 40, while the rapidly decreasing source mY is periodized with period 48. These are different objects; no equality of their periods is required. The Gaussian term eY remains on the whole line.

The finite residual is represented by literal binary-rational cosine coefficients. At strip height 1/4, the actual analytic theta envelope bounds the integral of sum_j R_j(z)^2; on the real axis this equals the squared Hilbert-Schmidt norm. Contour shifting and Poisson summation then give the explicit exponential trapezoidal alias error. The cross-Gram analogue is controlled in operator norm by the rank-free coefficient envelope. The omitted real samples are paid using the Gaussian integral tail and the actual double-exponential theta tail, with the coefficient sizes explicitly asserted in the program.

The independently reviewed b-periodization theorem gives the full weighted image bound (12/5)(389A0+24A1)e^-24/(1-e^-24). This is the dominant continuous error and is not replaced by a grid residual. The exact periodic Fourier coefficients follow from the whole-line source Fourier transform. The strip Fourier envelope and |d(t)|<=18t^2+c_N bound both the folded aliases and the omitted high modes, with the stated frequency-step and Nyquist factors.

The decomposition d=b-C_N+Q^2 C_N requires three separate image controls. The Q^2 component uses the genuine convolution kernel, its L1 bound, its explicit remote tail and the actual L1 norm of m. Source truncation at |y|=2 is not treated as compact support: its outer theta tail is paid. The outer x region is likewise weighted by the true m tail. The -C_N component is independently controlled by ||M_m tau_s M_m||<=||m||_infinity m_tail(|s|/2), with |s|>=48-log 3 for every first nonzero image; its entire remaining image sum fits the explicit tiny allowance. This was specifically checked to avoid silently counting the local-shift images as Q^2 images.

For the periodized input Qe_j, the compact support really is [-R,R]. Its operator bound carries sqrt(2R), and conversion to a Hilbert-Schmidt bound explicitly carries sqrt(rank). There is no omitted rank factor. The input period 40 remains distinct from the source period 48.

### 4. Finite arithmetic and the required correction

The scripts use the stated standard binary64 round-to-nearest model, with conservative operation-count gamma bounds, outward interval accumulation, and additive subnormal allowances. Matrix products are midpoint proposals whose errors are bounded by actual input Frobenius norms and their propagated radii. Scalar norms are rounded outward from sums of squares; they are not accepted as exact floating norms. Powers of two used for the dyadic data and frequency multiplicities are exact apart from explicitly covered subnormal cases.

During this independent review, the last rounded operation Gmid=fl((cross+cross.T)/2) was found not to have its own stated error in the earlier program. Version 4 correctly adds 2u||Gmid||_F+4r^2*2^-1074 before the final Gram assertion. This addition is approximately 1.218e-16, well inside the existing strict margin, but is necessary for the exact finite-arithmetic claim. The present approval is for the corrected version 4. Its stronger explicit coefficient-sum assertion and its corrected written subnormal count were also read back.

The resulting ||G-Gmid||<1/30000 proves Gplus=Gmid+(1/10000)I>=G and Gplus>=(1/15000)I, using only the positivity of the actual G. The signed D error is less than 1/100000, so Dplus=Dmid+(1/100000)I>=D. These are one-sided upper enclosures with the correct directions; no positive-matrix assumption on D is used.

### 5. Rational congruence and full-space consequence

The target Ccert=(31/32)Gplus-Gplus Dplus Gplus is an exact rational symmetric matrix. A floating eigensolver is used only to propose a rational change of basis. Its invertibility is subsequently verified by the strict ||W*W-I|| bound. All products forming the congruence are enclosed, including the conversion of the exact rational ridges and the symmetrization.

The congruence has one strictly negative Gershgorin component and 372 strictly positive ones, separated from zero by the displayed rigorous row error. Equivalently, scaling the off-diagonal part to zero preserves nonsingularity, and its inertia is the signed diagonal inertia. This certifies the inertia of Ccert without trusting an approximate eigenvalue sign.

The reviewed one-sided signed-Gram theorem applies even if the true G is singular, because Gplus is strictly positive. It gives at most one compressed eigenvalue above 31/32. Adding the full original norm error below 1/32 gives at most one changed-base Birman-Schwinger eigenvalue above one. The original H+1/8 consequently has at most one negative direction. Its actual ground eigenvalue supplies that direction, so its ground-perpendicular even space satisfies H>=-1/8, equivalently L>=3/8. This uses the full-space inertia argument; B and V are not incorrectly restricted separately to the original mean-zero space.

### 6. Independent actual reproduction

All six programs were rerun independently in a separate independent replay directory, using a separate copy and one BLAS thread. This included regeneration of the slow Bessel tables, both elementary/Gamma tables and the complete 2048-node signed-prime matrix, not just replay of the final inertia calculation. After the version-4 correction, the last continuous and inertia programs were rerun again. All assertions passed.

The independently generated five binary artifacts matched the author's hashes exactly:

- Bessel input table: `eb44eacfcab028bddbf226838b6fed4f8cce1c3c310031b6f7092d804deefbbd`.
- Period-40 scalar table: `2c7860f6492436cbbc791c949403a5f3e66baec7a93db32cca00ebeed170ee7b`.
- Period-48 scalar table: `532b78fb9f53ee1662299d814369962b873b15d0f929cf4123d222f1a8ac504c`.
- Actual signed-prime midpoint: `f7e8244f343859779a45ecc29c7f1f25d48398272301f60c0d90ee3aec5a6d95`.
- Actual cross-Gram midpoint: `26d3d177821bca8333f32e51d932ab45cda01774a9d7c5d9175ad76319c1b10e`.

The reproduced upper bounds are residual 0.00000200315144011985834 and true Gram error 0.0000250525617388227078. The certified inertia is one negative and 372 positive directions. The minimum positive Gershgorin lower bound is 0.0000967622711666508741; the negative upper bound is -0.0919419387049205141; the complete congruence row error is at most 0.0000000402081218627636. 

The new achievement is a verified actual full-Gamma/signed-prime resolvent instance at this single depth. No claim about deeper depths, an interval of epsilon values, a limiting half-gap, computational complexity, or RH follows from this certificate.

## Appendix A. Signed upper-Gram counting

Status: approved as a sufficient finite-certificate interface; no new spectral sign is asserted.


With G<=G_plus>0, S=G_plus^{-1/2}G^{1/2} satisfies SS*<=I, and G^{1/2}D_plus G^{1/2}=S* A_plus S. On a subspace whose form for the latter exceeds c||x||^2 with c>0, S is injective and its image has A_plus form exceeding c||Sx||^2. The variational count above c therefore cannot increase under this contraction, even though D_plus is indefinite. The preliminary D<=D_plus comparison is ordinary Loewner order with fixed G. This proves exactly the claimed positive-threshold count, not Loewner monotonicity under a signed change of Gram.

Congruence C_cert=G_plus^{1/2}(cI-A_plus)G_plus^{1/2} has the stated negative inertia. No inverse of singular true G is used. The strict threshold c=1-eta is correct: an operator-norm error at most eta carries a two-dimensional subspace strictly above one for K to a two-dimensional subspace strictly above c for its finite approximation. Thus at most one negative eigenvalue of C_cert suffices for the existing original-form depth conclusion, with the actual ground state and the previously proved comparison retained.

The true residual Gram identity is correct with the standard conjugate-first inner product. Entrywise symmetric radius bounds give spectral norm at most the maximum row sum, so adding that scalar ridge gives a valid Loewner upper bound. This must be applied to the complete residual upper matrix, and the manuscript does so. A separate positive ridge may enforce G_plus>0. Actual prime-overlap errors must likewise be enclosed in D_plus. Exact rational or verified-pivot interval symmetric elimination can then certify inertia without a numerical Gram square root or inverse.

The argument is exact also for Hermitian matrices with the corresponding conjugations; the proposed real-even computation uses real symmetric matrices. Core density only gives the availability of convergent least-residual approximations for each fixed parameter choice. It is not itself an evaluated residual bound or a proof that the required inertia condition holds. Those limitations are explicitly retained.

## Appendix B. Actual theta strip

Exact Fraction checker: `check_theta_strip_constants.py`, SHA-256 `4f5ae8b1705c51e072bdb8c131d8c2f4e03d5763fdf0a881911eddd3f09590c4`. It was independently executed on 2026-10-12 and returned ALL_PASS. This checker certifies the displayed rational constants, while the analytic proof below supplies the full strip and Fourier statements.

### Verdict

Approved for the actual original theta multiplier and the stated full-line trial/input classes. The result excludes zeros of the explicit kernel Phi in a horizontal strip. It makes no zero-free assertion about its Xi transform and certifies no residual norm or matrix sign by itself.

### Analytic kernel and square root

The literal theta series is locally normally convergent for |Im z|<pi/4. Its original modular evenness on the real line extends throughout this strip by analytic uniqueness. For Re z>=0, t=exp(2Re z)>=1, its first summand is nonzero. On |Im z|<pi/6, pi Re exp(2z)>(3/2)t. Dividing each higher summand by the first yields the stated bound 3 n^4 exp[-(3/2)(n^2-1)]. The rational factor inequality follows directly from pi>3 and n>=2. The ratios of successive majorant terms are at most (3/2)^4 exp(-15/2), so the geometric upper sum is valid.

The fourth Taylor polynomial gives exp(1/2)>211/128. Replacing the two negative exponentials by powers of 128/211 enlarges the geometric bound. The exact resulting fraction is 39068406334789555738738008338202624/72948430300416205277377935950067739, less than 3/5. Thus Phi cannot vanish in the right half-strip; evenness supplies the left half. Omega=2cosh(z/2) has no zero there. A holomorphic logarithm of Phi/omega exists on the simply connected strip, so the square root agreeing with positive m(0) exists uniquely and is even.

### Explicit complex and Fourier bounds

The 8/5 first-summand upper factor and |2cosh((x+iy)/2)|>=2cos(1/4)cosh(x/2) yield the exact coefficient bound 146432/1519<100 on |y|<=1/2. This proves (2) on both half-axes. Integrating its square root after u=exp(2x) gives (40/3)exp(-3/4), hence (6), with all factors of two retained.

For Y=e^(-x^2)sum a_nu exp(i nu x), its vector norm on the displaced contour is at most exp(1/4-x^2) Ahalf. The contour may be shifted to Im z=-sign(t)/2: it lies strictly inside the holomorphic strip, and the true double-exponential envelope makes the vertical closing pieces vanish. Combining (6) with exp(1/4)<4/3 proves (7), with Fourier convention fhat=integral f exp(-itx). This is a whole-line contour argument, not a grid or periodic continuation argument.

For the orthonormal compression basis, band-limited evaluation is a bounded functional on L2. Bessel's inequality gives the full Euclidean row bound (1/(2pi))integral rho(t)^2 exp(-2ty)dt. The support [-2T,2T] and |y|<=1/2 imply (2T/pi)exp(2T), with no dimension factor. The same contour shift and L1 multiplier bound then prove (9). This remains valid for the compactly supported even Legendre basis; Q is applied before complex evaluation, so no analytic extension of the discontinuous spatial basis is asserted.

### Remaining computational obligations

The finite trial coefficients must describe an actual full-line function. Periodic FFT errors, the long spatial tail of b(D)f, finite-window approximation, continuous residual integration and directed rounding are all still separate obligations. These envelopes may help discharge them but do not replace them. No new spectral gap or certified finite Gram matrix is asserted.

## Appendix C. Whole-line periodization

The exact Fraction script `check_periodization_constants.py`, SHA-256 `516f40c331782595c115f727c4714ec55289db48e566bac9bb87eb4162b4697d`, was independently run and returned ALL_PASS. The analytic proof and normalization were separately checked.

### Verdict

Approved for the explicit finite Gaussian-trigonometric whole-line trials and the genuine original multiplier b(D). The whole-line m-weighted image-error bound is valid for any positive period parameter L; the trial frequencies need not lie on that period's Fourier grid. Finite sampling, aliases, quadrature and matrix inertia remain additional obligations.

### Normalization and constants

The digamma difference is the positive-half-line integral with 1-cos(tu/2). Substituting u=2h gives twice the positive-half-line kernel, which is exactly the stated full-line even kernel k(h). Thus (1) has no additional factor two.

The original real envelope with Astar<2000/49 gives ||m||infinity<3/2. The previously reviewed complex envelope has maximum below 25 for |m| squared on its closed half-strip. Radius-1/4 Cauchy circles therefore give |m'|<=20 on the real line. The Gaussian inequalities in Section 2 yield F_inf<=(8/5)A0, D1<25A0+(8/5)A1, and F1<7A0. All are vector triangle estimates and introduce no number-of-columns factor.

The weighted multiplier integral is correctly transformed into Astar integral_1^infinity u^(3/2)e^(-pi u)du. Replacing u^(3/2) by u^2 and pi by 3 gives the explicit 17e^(-3)/27 factor. The conservative rational square bound 17000/11907 is below 36/25. This proves ||m e^(|x|/2)||2<6/5 with the full-line factor included.

For the small-jump part, the difference is bounded by |h|D1 e^(-|x|/2)e^(1/2), and integral_(|h|<=1)|h|k(h)dh<=3 is conservative. For |h|>1, k(h)<(6/5)e^(-|h|/2); its total mass is below 3. The translated-f contribution follows from |x|<=|h|+|x+h| and the weighted L1 norm. Thus (8) holds with the stated deliberately loose factor 9. Using e^(1/2)<5/3, its coefficient of A0 is 1941/5<389 and its coefficient of A1 is 24, proving (9).

### Exact periodization and full-line error

The exponential bounds for f, f' and b(D)f justify local uniform periodization. Small h is dominated by the translated derivative sum; large h by the bounded periodic f sum against the integrable kernel. These give the required Fubini justification for (10). The Fourier coefficient of the exact periodization is b(pi k/L) fhat(pi k/L)/(2L), with the stated Fourier convention. The full-line strip estimate makes the corresponding infinite Fourier series absolutely convergent. This is not a claim that any finite discrete Fourier transform equals that function.

For each nonzero period index j, |x+2Lj|>=2L|j|-|x|. Summing the genuine exponential b(D)f tail therefore gives 2Cf e^(-L)/(1-e^(-L)) e^(|x|/2) for every real x, not only in the central period. Multiplication by m and the independently verified weighted L2 bound proves (12) with coefficient 12/5.

The eY part of the positive-base residual retains its original whole-line value. No periodization is imposed on it by this result. Source sample replacement, Fourier truncation/aliasing, other multiplier terms and rigorously enclosed residual integration must still be certified before an upper Gram matrix or spectral sign is reported.

## Supplemental proof correction, 2026-10-12

The original review did not expand the three required tiny-remainder bounds for the omitted computed cross lattice and the remote input/output images. The user's [FULL_GAMMA_TINY_TAIL.md](FULL_GAMMA_TINY_TAIL.md), first supplied in [e4326b0a](https://github.com/aa339519589-cpu/Riemann-Hypothesis/commit/e4326b0a16552c2de3024754d25721cea8ffbddf), now supplies that missing explicit ledger. The [independent supplemental review](REFEREE_FULL_GAMMA_TINY_TAIL_INDEPENDENT.md) verifies the exact periodic-input object, full theta tails and actual trial dimensions. Read this supplement together with the review above. Existing error allowances cover these terms and all numerical results remain unchanged. This correction is specific to the 373-column certificate; the [127-column tail review](REFEREE_MULTIBAND_TINY_TAIL.md) is separate.
