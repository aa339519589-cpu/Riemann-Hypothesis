# Independent review: original gap 511/1024

This review accompanies [CERTIFIED_MULTIBAND_GAP.md](CERTIFIED_MULTIBAND_GAP.md) and its [exact four-program reproduction package](gap_511_over_1024_certificate).

## Verdict

Approved. The stated certificate proves, for the unchanged complete original even theta jump operator, the mean-zero inequality L>=511/1024. This improves the previously certified numerical lower bound 3/8. It is a single-depth theorem at epsilon=1/1024; neither an all-epsilon sign result, the critical bound 1/2, nor RH follows.

The complete mathematical proof in the accompanying report and the final v4 programs were independently reviewed. All four programs were independently executed in a separate cloud directory, including regeneration of both scalar/quadrature tables. The last two programs were rerun with the corrected continuous script v4. Every assertion passed. The four regenerated binary artifacts matched the author's hashes exactly.

## 1. Exact base, actual new space and full-space consequence

The underlying original objects H=B-V, B=m b(D)m and ULU^-1=1/2+H are unchanged. N=4 retains the actual prime-power shifts 2,3,4, with their correct coefficients, and the complete omitted prime tail is paid by e=1/1024-delta_4>0. The already independently certified ten-band cover has d=b-1_(R\E)C_4>=b/100. Its difference from b is bounded, so the closed operator domain and genuine operator core remain those of B. The full original form comparison H+epsilon>=A-m h(D)m holds with A=m d(D)m+e and h=1_E C_4.

The actual spatial radius is R=34/25 and the actual 127 carrier functions are compactly supported on [-R,R]. Rescaling each original Taylor carrier by 2^k requires the inverse factor [(t-nu)/2]^(k+l) in D. Equation (1) implements exactly that change of basis. Only the frequency-feature matrix D is block diagonal; the whole-line resolvent Gram G=F*A^-1F retains every cross-band entry. No 373-dimensional Gram value or sign is reused.

The previously certified full-operator approximation error for precisely these bands/orders is 0.0001161447989409985..., below eta=1/4096. Thus the positive threshold c=4095/4096 in the signed-Gram test is correct. Once its actual upper matrices and inertia are verified, the full-space min-max and signed Birman-Schwinger comparison give at most one negative direction of H+1/1024. The known original ground eigenvalue -1/2 supplies that direction. The original even ground-perpendicular space consequently satisfies H>=-1/1024, or L>=511/1024. B and V have not been restricted separately to a subspace they need not preserve.

## 2. Actual inputs, operator-domain trials and quadratic Gram identity

The exact trial input is an integer matrix of shape 1900 by 127, divided by 2^44. Its entries have modulus below 2^53, so the stated conversion is exact. The whole-line trial functions are exp(-x^2) times finite cosines at exact frequencies pi q/20. The actual analytic theta bounds show these trials belong to D(B)=D(A). The compactly supported input functions need only be in L2; their endpoint jumps are not treated as operator-domain regularity.

For the true residual Rop=F-AY, expansion gives the exact identity
G=2 Herm(F*Y)-Y*AY+Rop*A^-1Rop.
The last term is positive and bounded above by ||Rop||^2/e. This quadratic identity, rather than an unverified inverse or a Galerkin lower matrix alone, is the basis of the computation. The cross product and full form term are separately enclosed.

The temporary analytic input extension tilde_F=m tilde_phi is not substituted for F. Its two-sided tail is bounded from the actual theta envelope and the decreasing logarithmic derivative 4+2k/x-2pi exp(2x). At x>=R this is at most -a_k<0 for every retained k. The resulting sum in (5) correctly counts both tails and all 127 columns. Its Hilbert-Schmidt norm is less than 1.265e-8. This is charged once in the residual and separately as delta_F ||Y|| in the cross Gram. Both payments are present in the final script.

## 3. Complete scalar and signed-matrix enclosures

The elementary program independently encloses the true theta values using four modes plus the complete positive tail, the actual 2cosh(x/2) denominator, all exact cosine roots, Gaussians and scaled carriers. The full digamma symbol uses the already reviewed Binet formula, 64 recurrence shifts, eight Bernoulli terms, and the explicit B18 remainder 43867/(798*18*64^18). Thus b is the complete Gamma symbol, not a finite-Gamma lower comparison. All asserted conversion radii were independently reproduced.

The hard-band rule is the literal positive Clenshaw-Curtis rule of order 128 on each actual interval. Exact node cosines and their integer multiples are enclosed by interval identities with retained wrapping. The coefficient C_4(t) is signed; positivity is used only for the quadrature weights and error bounds.

For D, the constant part is polynomial-exact. Expanding each prime cosine about the band midpoint through degree 128-2k_max makes the product with the moment polynomial exact. On all these bands |(t-nu)/2|<=1, including the central interval. Therefore the displayed factorial remainder controls each moment without an omitted polynomial-growth factor. Positive quadrature weights give the stated integral-plus-rule factor, and block row sums give a valid operator error. The total D error is below 1e-10, justifying Dplus=Dmid+1e-10 I despite D being indefinite.

## 4. Full-line operator action, sharp bands and both Fourier discretizations

The source period is 80, its sample step is 1/128, the trial trigonometric period is 40, and the final integration step is 1/256. These objects are deliberately distinct. The sampled source cosine coefficients have the correct 1/10240 base normalization, doubled away from zero and the Nyquist endpoint. The target cosine-root indices agree with these exact scales.

Only b-C_4 is periodized. The original b-periodization estimate at half-period 40 gives (12/5)(389A0+24A1)e^-40/(1-e^-40). The separate -C_4 image shifts have modulus at least 80-log 4 and are paid by the genuine weighted translation norm bound. Literal source truncation and periodization-image differences are likewise paid by the actual theta envelope, not declared zero.

For the complete-Gamma-minus-prime alias, the original strip Fourier envelope and |b(t)-C_4(t)|<=18t^2+c_N bound all omitted and folded frequencies. Summing both frequency signs and both folded/unfolded multipliers gives precisely the conservative coefficients 72 S2+4 c_N S0 in (9), with dt=pi/40 and Nyquist threshold 128pi. Endpoint cosine multiplicities are compatible with this bound.

The sharp h multiplier is integrated on its true bands, never treated as a sampled periodic symbol. At every non-grid band node the source Fourier integral has its own Poisson alias bound. The final v4 program explicitly includes it, even though it is very small. Its complete positive-weight and |C_4| factor is c_N times the positive-band width divided by pi.

The hard-band quadrature estimate follows by expanding the actual real oscillatory kernels, whose spatial phase lengths on |x|,|y|<=4 are at most 8+log 4. The real Taylor remainder needs no artificial complex exponential factor. A necessary implementation point was checked during review: the code uses a discrete source sum, so the continuous ||m||_1<1 estimate alone is insufficient for its coefficient. The corrected v4 program separately encloses (1/128)sum m(j/128)exp(-(j/128)^2), obtaining 0.4699792248460494...<1. Thus the exact discrete source mass is at most A0, as required by (12).

The remaining source and weighted-target regions outside |x|=4 are paid by the double-exponential theta bound. This is a weighted argument; it does not incorrectly assign exponential spatial decay to the unweighted sharp-band kernel. Actual coefficient-size assertions A0<1000, A1<100000 and synthesis sums<1e8 make the tiny tail allocations numerical bounds rather than unspecified asymptotics.

## 5. Continuous integration and finite arithmetic

The analytic extension has a rank-free strip bound: summing the carrier powers gives exp(4|x|+4a) per band, and the actual theta envelope yields the strip integral below 120. With ten bands and maximal frequency 873/8 this gives M_F as stated. The earlier squared strip integral below 25 controls the action synthesis. The Gaussian trial bound, squared residual bound and cross-product bounds in (14)-(15) follow by vector Cauchy-Schwarz and the analytic extension sum_j R_j(z)^2, whose real values are the real squared norm.

Contour-shift Poisson summation therefore controls the entire trapezoidal sum, not just the displayed grid. The omitted Gaussian-only trial tail is retained in ||Y||, the synthesis residual and the form term's e0|Y|^2 contribution. Terms containing m have their separate theta tails. The temporary extension is then removed by the two endpoint payments above.

The code encloses products using conservative gamma_(4n+8) bounds, actual Frobenius input norms, propagated component radii and additive subnormal allowances. Outward norms include the positive-sum rounding bounds. Diagonal multiplications, divisions, additions, scalar e conversion, both symmetrizations and the final 2*cross-energy combination have explicit errors. The continuous error E_A multiplies the true whole-line Y norm in the form enclosure. The final Gram error is the complete center error plus rho^2/e; it is not the much smaller grid residual.

## 6. Independently reproduced values and rational inertia

The final v4 execution gives the following outward upper bounds:

- source sample mass: 0.46997922484604941084429865736;
- input-extension norm: 0.0000000126441326549372831213408151472;
- true residual Hilbert-Schmidt norm: 0.00000230903613745745751845606448097;
- center error: 0.0000785701104245691496682001935002;
- quadratic residual Gram error: 0.00000000839483966342070211812736402437;
- total true Gram norm error: 0.0000785785052642325703703183208642 < 1/12000.

Since the true G is positive, Gplus=Qmid+(1/10000)I is an upper matrix and is at least (1/60000)I. Dplus is the independently enclosed signed matrix upper bound. The midpoint entries are exact binary rationals, and both ridges and c are exact rationals.

The final eigensolver only proposes a binary-rational congruence basis. Its invertibility is subsequently verified, with ||W*W-I|| bounded by 7.51533522009791e-12. All products, rational-ridge conversions and symmetrizations in the congruence are enclosed. The strict Gershgorin separation yields exactly one negative and 126 positive directions. The minimum positive lower bound is 0.000064541217145654502542856117945, the negative upper bound is -1.00796112985057298499406957137, and the row error is 2.971517429062852e-9. Consequently the finite inertia is certified independently of the proposed floating eigenvalue signs.

## 7. Reproduction record and exact hashes

All four programs were executed in a separate independent replay directory, starting with only copies of the four programs and the two exact inputs. The final continuous v4 and inertia programs were then rerun after the discrete-source assertion was added. The numerical environment is the same Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0 environment as the earlier full-chain reproduction, with one BLAS/OpenMP thread.

Exact inputs:
- hardband_parameters.json: 26570a1cc3687814c8702e86a2b65f852f46850836865e5077639f253c4f1027;
- trial_cosine_dyadic_eps1024_scaled.npz: c34ed29a9d4beb48652b7b25a7566064bf5eb8c2c33dba41df430984f0b63c04.

- verify_hardband_scalar_tables_scaled.py: 6dac9a93b253e2ea6cb1b4bc888367cb1bc1553b9cee8dc6cb65443ab0d41d72;
- verify_hardband_quadrature_tables.py: 71d2af1c106726f92a5d39d2060b460e19453bc4f2bc04bd8858846c84c8e3da;
- certify_hardband_continuous_residual_v4.py: 43e08e869b08f0097bd1b06721ae5e2d76a383de6b9eba026f64e449451e1312;
- certify_hardband_signed_inertia.py: fb054e026aa0770e8264ae263f2f89542a1c3978418ad92c387b753cfdeb370e.

The following four regenerated binary outputs match the author's artifacts exactly:
- elementary table: 350ddb07e602d23487b5c5de53e64869aefb343649012d6fd232063b1661c2bc;
- band quadrature table: 5a63650e8282ed628e36ff0967c3fc181f8e8b4dfdd89861cd4cab7d73409269;
- Gram center: 1939a1e10fc8366bbac8400ad520a687a558253db3712519d45200b3bd2437c7;
- congruence basis: 0eb53a8c88824db5ee24e6b7b730a9120203f25fdf814e7dd8bb98f61ad03f40.

No exploratory trial-proposal script is a proof dependency. The approved package uses the new 127-dimensional actual Gram, not a transferred sign from the older 373-dimensional certificate. The all-epsilon and critical-half-gap questions remain open.
