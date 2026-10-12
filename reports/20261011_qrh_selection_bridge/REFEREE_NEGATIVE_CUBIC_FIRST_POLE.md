# Independent review of the negative cubic first-pole bridge

Reviewed [NEGATIVE_CUBIC_FIRST_POLE](NEGATIVE_CUBIC_FIRST_POLE.md), the exact physical source at `e62ca4a`, and [CUBIC_NONCUBIC_LAMBDA](CUBIC_NONCUBIC_LAMBDA.md). The published bridge specifies the primary generator of R and distinguishes its intact bad vector from the expanded d-mask organization; the review's requested clarifications below are applied. No complete first-remainder or RH estimate is claimed.

# Independent audit: negative-unit first pole, current Part XXIV VII

## Verdict and audited scope

At repository HEAD `bed10bb`, Part XXIV VII passes the row-to-theorem audit for the specified first Gauss polar functional, using the unconditional all-lambda-cusps theorem in Part XXVII A. The new `CUBIC_NONCUBIC_LAMBDA` result supplies an unconditional quantitative theorem for every one of the nine primary cubic lambda-ray channels. Current Part VII's finite bad-vector Poisson identity is the operative formulation; the nine-channel analytic input is now an unconditional theorem.

The conclusion is exactly this: with target `eta=1`, for each original frequency unit `epsilon` in `{-1,-omega,-omega^2}`, the normalized first `v_1` Gauss row is holomorphic at `s=5/6`, so its residue is zero on each fixed admissible physical fiber. In the original norm-Mellin coordinate this is the specified pole at `z=1/3`. Thus the ordered first-polar-then-second-remainder functional for these three units is zero; the all-six-unit specified secondary bound inherits the positive-unit `O(Z^(-19/480+epsilon))` result.

This does not estimate the first nonpolar remainder, the complete cubic sector, the whole critical probe, or RH, and it does not identify this ordered decomposition with the coupled Mellin wall. The statement concerns the current nonunit cube-free core `w=v_1 v_2^2` and the actual Part XXIV physical decomposition; its exact physical source retains the full fixed-a masks.

## Exact free-row character

Current Part VII keeps the full fixed bad-vector period `M`, with 2-part exactly `4`, the primary selector, the original holes, and the lambda data. Its finite CRT identity (4) has the factors

`S/(q_M sqrt(q_q)) * tau_epsilon(q) * chi(M lambda) * gamma_D(chi) * Ahat(h) * bar(chi(h))`,

where `q=v_1v_2`, `gamma_o(chi)=chi(lambda) gamma_D(chi)`, and `Ahat` includes the primary selection exactly once. This is consistent with splitting a residue as `q b + M r`: the bad part contributes `tau_epsilon(q)`, the good character contributes `chi(M)`, and conversion from the original additive Gauss sum to `gamma_D` contributes `chi(lambda)`. Do not append another primary factor or another `chi(lambda)`.

After fixing the actual physical data and writing `v_1=n_+ g_+ rho`, the fixed divisors contribute only the scalar `psi_4(n_+g_+)`; `psi_4(rho)` remains in the moving row. The row numerator carried from Part V is the actual `Z_0=kappa d^2 j f^2 c_2 h`. In particular the `f^2` phase, its `q_f` scale, the actual `a`-mask, and the full mixed core are retained. The `j` phase and every other moving factor from the physical square layer are cubic. On the odd branches the free core in `rho_p^(-3)` is `rho^2`, giving `chi_p(rho)^(-6)=1` for both branches. None cancels `psi_4(rho)`.

At the prime above 2 the exact factors are

`theta_(v_1)(4)=xi_pi(v_1)^(j_pi)` and `bar(theta_(v_1)(kappa))|_pi=xi_pi(v_1)`,

so their product is `xi_pi(rho)^(j_pi+1)`, with exponent 2 for `j_pi=1` and exponent 0 for `j_pi=2`. Thus the exact residue character is

`phi = psi_4 * xi_pi^(j_pi+1) * chi_R` modulo `(4R)`,

with a separate fixed primary lambda-ray character. Here `R` is prime to 6 and the odd component has been reduced to its exact primitive character. Since `xi_pi` factors through modulo 2 and `chi_R` is cubic, `phi^3|_(4)=psi_4 != 1`. The CRT witness `y=lambda (mod 4)`, `y=1 (mod R)` has `psi_4(y)=chi_4(Nlambda)=chi_4(3)=-1`; all cubic factors cube to 1. It also witnesses primitivity at `(4)`, since `y=1 (mod 2)` but `psi_4(y)=-1`. Hence the auxiliary order-three factor cannot cancel the order-two character.

The free lambda-ray twist is finite and cubic. The actual row factors are products of fixed cubic residue symbols, including the supplementary symbols at `omega` and `lambda`; on primary `rho=1+a_2 lambda^2+a_3 lambda^3 (mod 9)`, they are among

`alpha_(k,l)(rho)=omega^(-k a_2(rho)+l a_3(rho))`, `k,l in {0,1,2}`.

The map from the source labels `T=A+B omega (mod 3)` to `alpha_T(rho)=omega^(B a_2+(2A-B)a_3)` is invertible over `F_3`, so these are precisely the nine channels of `CUBIC_NONCUBIC_LAMBDA`. Higher lambda powers in the fixed period reside in the fixed finite vector `Ahat(h)` or in fixed scalar shifts; they do not make a higher-period moving character. The row has no archimedean/angular twist. This nine-channel identification is explicit in the published bridge; the current Part XXVII A is broader and independently covers any fixed multiplicative lambda-ray factor if one uses that route instead.

The theorem's hypotheses now match: `phi` is primitive modulo `(4R)`, prime to 3, its cube is nonprincipal, the summation variable is primary, and the lambda character is one of the nine `alpha_T`. The unconditional `CUBIC_NONCUBIC_LAMBDA` theorem gives holomorphy for `Re(s)>1/2` (and its stated `Q^(3/4)(1+|t|)^3` bound); the all-lambda-cusps qualitative theorem in Part XXVII A gives the same needed continuation with arbitrary fixed lambda-ray data. No zero-free conjecture or GRH input is used. The quantitative theorem's explicit finite-mask cost is not a license to sum moving moduli or first-remainder contours without their separate norm ledger; Part VII only needs a fixed-fiber holomorphic germ.

## Additive sign and exact CRT roots

In the pinned original convention `e_o(z)=exp(2 pi i Tr(z/lambda))`, for `u=a+b omega` one has `e_o(u/4)=i^b`; direct summation over the sixteen classes gives

`sum_(u mod 4) psi_4(u) e_o(u/4)=+4`,

and the full transform is `4 psi_4(h) 1_(h,2)=1`. In the literal DR convention `check e(z)=exp(2 pi i Tr(z))`, the corresponding value is `-4`. I recomputed both finite sums; this sign difference is expected from the change of additive character. Keep the original bad vector in `e_o` and use `gamma_o(chi)=chi(lambda)gamma_D(chi)` only for the good factor.

For the fully factored CRT display at modulus `4 m q`, the local additive arguments are respectively `h overline(mq)`, `h overline(4q)`, and `h overline(4m)`. Their Gauss factors are exactly `psi(h)psi(mq)`, `bar(alpha(h))alpha(4q)`, and `bar(chi(h))chi(4m)`. The complement-modulus roots and their signs are therefore correct. The current `Ahat` formulation packages the bad-period roots, which is safer than layering the factored extension formula on top of (4); neither formulation permits an extra primary average after `Ahat` has already selected primaries.

## Fixed physical fibers, masks, and order of operations

The actual physical `e`-first restriction is made before the second Poisson and both pole extractions. The Part V cutoff is `q_(n_-) q_g q_j^2 q_e <= C_1 Y`. Once the physical `n=n_0 r_phys^2` layer, `n_+|v_1`, `n_-|v_2`, `g=g_+g_-g_a`, `a`, `j`, `e`, `f`, `c_2`, and dual frequency `h` are fixed, this is a finite scalar cutoff independent of the free `rho` and common to the norm-four bad sum. If the bad mask is expanded over `d`, each nonzero `d` is odd at 2 and retains the same primitive `psi_4` factor; keeping the mask in `A` is the exact alternative. All shared-divisor, numerator, and zero-extension masks remain in the row. Any overlap exclusions become fixed finite holes or zero branches; they do not change `phi^3|_(4)`.

The original/core marker assignments and each inner first-flat sector are likewise fixed before taking this one-variable residue. The first-flat map preserves `epsilon,v_1,v_2`; its `b`-dependent phase is cubic at a fixed good numerator, while its exact coefficient and scale stay outside the `rho` row. The first-flat `b`-sum is not silently treated as finite: each negative-unit polar summand is zero for every fixed `b`, and the established flat interface defines the decomposition inner-sector first. The first remainder is the original flat limit minus the specified secondary series; it is never obtained by summing or regrouping its unestimated integrals. The original compensation is a finite sum of these actual probes and also preserves the norm-four factor. Therefore the zero applies fiberwise through all original `n,a,g,h` rows, both markers, both first-flat operations, and the finite compensation. It is not obtained by dropping a tail or replacing the actual `e`-cutoff by an infinite convolution.

Part VII uses fixed-fiber holomorphy only. It neither moves a family of first-remainder contours using a nonexistent uniform bound nor aggregates the infinite first-nonpolar remainder. The remainder stays the original sector minus this zero polar functional, with each first-flat operation defined inner-sector first. Existing full physical-tail and logarithmic costs belong to the already audited positive-unit/secondary ledger; the negative polar zero creates no additional tail estimate and proves no estimate for the remaining integral.

## Clarification worth keeping in the main proof

Part VII is mathematically covered as written by Part XXVII A's arbitrary fixed lambda-ray theorem. For a direct citation to the newer nine-channel quantitative theorem, one short sentence displaying the `alpha_(k,l)` reduction above would make the interface completely explicit; the current abstract phrase “a fixed multiplicative lambda-ray factor” is enough for Part XXVII A but does not by itself show the nine-label match. This is a presentation clarification, not a gap in the zero-residue argument.

## Bounded review of `NEGATIVE_CUBIC_FIRST_POLE.md`

The published bridge's Eq. (1) CRT prefactor is correct at current HEAD `bed10bb`: the unnormalized Fourier vector carries primary selection once, the bad-side covariance contributes `tau_epsilon(q)`, and the good-side factors are `chi(M)` and `chi(lambda)` combined as `chi(M lambda)`. Here `chi` is the good cubic character `theta_(v_1) bar(theta_(v_2))`; `tau_epsilon` is the original sextic unit factor, not that good cubic character. The bridge has no additive-orientation conflation: it keeps the bad vector in `e_o` and converts only the good Gauss factor by `gamma_o(chi)=chi(lambda)gamma_D(chi)`. The two norm-four signs and the direct transform are correct.

Eqs. (5)--(7) retain primitivity at `(4)`, give `phi^3|_(4)=psi_4`, and match all nine labels with `B=-k`, `A=2(l-k)`. The published bridge explicitly chooses the primary generator of R, so `4R` satisfies the primary-modulus hypothesis. The local proof of primitivity otherwise checks: the `(4)` component is `psi_4` times a character factoring through `(2)`, and the exact odd component is primitive at `R`.

The published bridge distinguishes the two exact bad-mask organizations. Its Eq. (1) keeps the mask inside the bad vector and Eq. (3) therefore has no d factor. In the alternative expanded organization, the mask-free vector is used with the original mu(d), tau_epsilon(d)chi(d), the actual S/q_d scale and its q_d^(-1) Poisson prefactor, and the numerator kappa d^2 j f^2 c_2 h. This resolves the duplication flagged in the draft without changing the norm-four noncancellation proof.

The rest of the requested scope checks pass: the actual finite cutoff `q_(n_-)q_gq_j^2q_e<=C_1Y` precedes the Poisson/pole steps; all fixed `n,a,g,h`, zero extensions and shared masks survive; original/core mark assignments become fixed divisors or holes; first-flat is defined inner-sector first, with no summation of first-remainder integrals; and the `N(rho)^(-1/2)` factor gives `s=z+1/2`, hence `5/6` corresponds to `1/3`. The bridge does not claim a first-remainder or whole-probe estimate. The mathematical review passes with the primary-generator and bad-mask clarifications applied; it also explicitly defines `tau_epsilon(c)=chi_c(epsilon)=psi_4(c)tau_+(c)` to separate the original sextic unit factor from the good cubic character.
