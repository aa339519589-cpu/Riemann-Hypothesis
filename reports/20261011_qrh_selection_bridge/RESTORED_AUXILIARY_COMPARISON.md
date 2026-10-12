# Exact principal restoration and the complete auxiliary-averaged high comparison

This independently reviewed supplement defines an additional Gaussian-scale operation on the half-damped observation and proves its complete auxiliary-averaged high comparison. It is a new scale-dependent family of physical observations, with the original prime slots, radial windows, character masks and compensation coefficients frozen at each ambient Z.

Under the user's finite-order Q input and the stated safe principal reciprocal-line hypothesis, the normalized ensemble with R₀=Z^128 equals a FIXED S₀ principal Mellin signal up to a strictly smaller power. The full nonprincipal contribution, including every other unit, every frequency and the original three common heights, is O(Z^(-1)). Its absolute finite-marker price is explicitly Z^(505/96), not an unpriced constant.

The Gaussian-only restoring operation also preserves the existing complete cubic and six other covered nonprincipal NONFLAT low bounds, by their actual positive-T envelopes. The low estimate for the whole new observation remains open: the unit good core and the missing residue-1 types have not been bounded. No RH theorem or zero exclusion follows from this high comparison alone.

## Sources and definitions

The exact weighted-subset ensemble and its same-row local multiplier are proved in [POLYNOMIAL_AUXILIARY_ENSEMBLE.md](POLYNOMIAL_AUXILIARY_ENSEMBLE.md), published at commit 7fade07afd1bd829ce9eb637db5aafa278585f74. The original source is [the pinned September 30 QRH manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). The half-damped observation and its existing principal factor are in [HALF_DAMPED_PROBE.md](HALF_DAMPED_PROBE.md); complete physical-type proofs are retained in [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md).

The user's [FORMAL_INPUT_Q.md](FORMAL_INPUT_Q.md), [GENERAL_SELECTED_Q_GAIN.md](GENERAL_SELECTED_Q_GAIN.md) and [PURE_FIFTH_SELECTED_Q_GAIN.md](PURE_FIFTH_SELECTED_Q_GAIN.md) keep their original attribution and finite-order/common norm-mode scope. No new formal-assistant build is claimed. The user's exact outside-phase correction in [REFEREE_MOVING_HOLE_PHASE.md](REFEREE_MOVING_HOLE_PHASE.md) remains in force; the former phase-free signed identity is not used below.

Parts A–C give the physical restoring operator, the complete absolute nonprincipal projection and the other six actual scale bounds. Part D combines these into the full high statement, keeping its safe-line assumption distinct from Q. Equation numbers restart within each part. Throughout, A_T(Z) denotes the fixed ambient prime-slot normalizer; its subscript does not mean that it is rescaled with the independent Gaussian variable T.

## Part A. The physical Gaussian-scale operator and exact principal restoration

### 1. Freeze the genuine physical data before scaling

Fix the original target eta=1, fixed S0 and xi0, half-damped physical n weight, original Gaussian and radial windows, and either reviewed original/core nonflat marker. At an ambient Z fix X=Z^lx, Y=Z^ly and every prime slot and its weight. Write ell=sum ell_i, h=1-lx+ell>0 and C(s)=s+lx/2-1+h/6. Let I_b(T) denote this same finite-compensated physical observation with ONLY its Gaussian scale changed from Z to T>0. All occurrences of the base Gaussian scale in its compensated summands change together; X,Y, selected primes, original rescaling coefficients and all character masks are frozen.

The additional auxiliary b is selected once at this ambient Z. It is a squarefree product of k primes of norm in [P,2P], P=(log R)^64, k<=log R/(65 log log R), Nb<=R<=Z^C0. Its primes are outside S0 and the original prime-slot supports. The enlarged bad set is Sb=S0 union supp(b), and the auxiliary character is xi0 times any admissible order-dividing-six nonprincipal local choices at b. The same b is used for EVERY T. No pool is reselected at a smaller Gaussian scale.

Let c_S denote the original double scalar residue constant. Put

 J_b(T)=I_b(T)/c_Sb.

For this enlargement c_Sb=c_S0 product_(p|b)(1-(Np)^(-1))^2, since both original scalar zeta residues lose the same local factor. This inverse normalization is uniformly bounded in the ensemble. After exact first Poisson summation let J_b,1(T) denote only its literal principal good-core u=1 component; every u!=1 contribution remains in J_b(T)-J_b,1(T). The slot normalizer A_T(Z) is fixed at the ambient Z and independent of this Gaussian variable T; no T-dependent change of the prime windows is made.

### 2. The exact missing principal factor

At the double scalar residue w=1,z=1/6 the half-damped local principal factor, for P=Np, is

 H_p(s)=(1-P^-2)/(1-r) * [1+(d-r)/(P(1-d))],
 d=P^-s, r=kappa(p)P^(2-6s), kappa=bar alpha^6.

Consequently define

 F_p(s)=(1-P^-s)H_p(s)
       =(1-P^-2)[1-(1-P^-1)P^-s-kappa(p)P^(1-6s)]
                                                 /(1-kappa(p)P^(2-6s)). (1)

After the c_Sb normalization, the literal u=1 double residue for J_b has the S0 principal signal multiplied by product_(p|b) F_p(s)^(-1). Its target denominator and angular factors have not been changed or assumed zero-free. Equation (1) is an exact rational identity, not an asymptotic approximation.

### 3. An independently defined physical restoring operator

For a good prime p define a dilation on the frozen-T family by

 (D_p J)(T)=P^(-5/6)J(T/P).

The high Mellin integrand contains T^(x+z-1). Therefore D_p has exact high symbol P^(-(x+z-1/6)); it has symbol P^-x ONLY at z=1/6. Define

 A_p=(1-P^-2)[1-(1-P^-1)D_p-kappa(p)P D_p^6]
                                      [1-kappa(p)P^2 D_p^6]^(-1),
 A_b=product_(p|b) A_p.                              (2)

The inverse in (2) is the explicit geometric Gaussian-scale series

 [1-kappa(p)P^2 D_p^6]^(-1)J(T)
      =sum_(j>=0) kappa(p)^j P^(-3j) J(T/P^(6j)).      (3)

For each fixed b these are commuting scalar dilations. Define the restored observation to be A_b J_b(Z). Formula (3), together with the three finite numerator terms, is the definition; it does not require assigning a formal Mellin multiplier to an unconstructed physical sum.

The full exchange can be justified directly on the original absolute lines (Re x,Re w,Re z)=(3,3,2). The exact source CRT bound |K(c,n,s,a;u)|<=Ns N(c n^3) gives the five convergent ideal sums with respective exponents -5/2,-7,-2,-12,-2, and hence the whole absolute scale C X^(-3/2)T^4Y^2, with a jointly integrable Schwartz majorant in all three heights. The j-th summand of (3) therefore gains P^(-3j)P^(-24j)=P^(-27j). The finite numerator dilations have the same domination. For every fixed finite b, this proves joint absolute convergence of all geometric series, all ideal sums and all height integrals; it commutes with the original finite prime compensation and the first Poisson identity. The Gaussian also gives the original rapid small-scale decay on each physical annulus, but no unproved passage from those annuli to a global interchange is needed. The good-core frequency label is preserved because T is only a Gaussian scale. On the absolute high lines the common symbol is exactly

 product_(p|b) F_p(x+z-1/6).                          (4)

### 4. Principal comparison is restored exactly, uniformly in b

Assume the same reviewed safe reciprocal-line condition for S0: 1/2<sigma<1 and 1/zeta_K^S0 is holomorphic on Re s>=sigma with fixed polynomial-height bounds on closed bounded strips. Choose the principal comparison's w0=1-dw and z0=1/6-eta0, reducing eta0 so that sigma-eta0>1/2. On its entire genuine crossing box, Re(x+z-1/6)>=sigma-eta0>1/2.

Equation (1) gives uniformly there, in all heights,

 F_p(x+z-1/6)=1+O(P^(-(sigma-eta0)))
                         +O(P^(-(6(sigma-eta0)-2)))+O(P^-2).

All three exponents are positive. By taking the log-pool exponent 64 as fixed and choosing eta0 relative to sigma first, the full product is bounded by exp(O(kP^(-c_sigma))) for a fixed c_sigma>0. More explicitly the first exponent exceeds 1/2 and the second exceeds 1, so kP^(-c_sigma) tends to zero. Fixed height derivatives have only predetermined powers of log R.

The original scalar deleted factors at b, the same holomorphic selected-prime corrections, and the positive majorant for the unselected factors are uniformly bounded on this crossing box. No division by an unknown H_p zero is used away from the displayed absolutely nonzero principal factors. In particular the same proof applies to the exact four-term contour order: x from 3 to sigma, w from 3 to 1-dw, and z from 2 to 1/6-eta0 on both w pieces.

At the double residue (4) becomes product F_p(s), and cancels the missing factors of section 2 exactly. The original selected-slot residue error R_Z(s) is unchanged, since every selected prime is outside b. Thus, writing the original S0 signal as

 f_half,S0(Z)=int_(2) Z^C(s)e^((s-5/6)^2)
                         H_half,S0(s)/zeta_K^S0(s) ds/(2pi i),

one obtains for some fixed m>0

 A_b J_b,1(Z)/A_T(Z)=f_half,S0(Z)+O(Z^(C(sigma)-m)).      (5)

Equation (5) concerns only the literal principal component. A comparison for the whole restored observation requires a separate bound for A_b[J_b-J_b,1]. Part B below supplies that independent estimate, and Part D combines the two; equation (5) itself remains a principal-component assertion. The error is uniform over the specified auxiliary ensemble. The three retained contours cost the same Z^(-ly dw), Z^(-h eta0), and their product; the finite prime-slot error costs the same fixed Z^(-kappa_P). Original independent-height Gaussian/M/What1 decay pays all fixed height orders. The target signal in (5) is genuinely fixed and independent of b and R, rather than a pointwise 1+o(1) surrogate depending on Z.

### 5. A sufficient positive-T low norm and the exact new prices

The numerical exponent in this section is asserted only for the reviewed original geometry l_x=17/48, l_y=23/48, ell=1/6 and its actual finite-subset compensation rescalings. Sections 1-4 allow their stated general positive principal geometry; no numerical cubic bound for arbitrary l_x,l_y,ell is inferred. For this transfer use the actual complete cubic low proof before taking T=Z, with all ambient X,Y,slots and b frozen. It supplies the positive-T envelope

 |I_cubic,b(T)| << (RZ)^epsilon Z^(-271/32256-c0)
                                   (Z/T)^(1/6+epsilon),
 0<T<=Z.                                            (6)

Here and in (6) c0 may be slightly decreased to pay preliminary fixed losses. A direct verification from the reviewed whole-scale proof is as follows. In the high-M branch its T exponent is beta-1+J(beta)/2; the original physical-square convergence condition -2-6[beta-1+J/2]<-1 makes this exponent >-1/6 with fixed room. The improved density keeps that strict margin. In the small-M branch the true r/a' allocation has C(beta)=max(1,5-6beta), so its T exponent is beta-1+C(beta)/6>=-1/6. This is the original complete count, not a single convenient smooth-column scale. For effective scales below one retain the original Schwartz tail before making this weaker positive enlargement. The half-damping is discarded only at the already reviewed positive n0/r stage. The simultaneous b holes are paid by the same direct product lemma, with ambient R,Z; it never requires Nb<=T^C0.

With a=1/6+epsilon, the weighted norm in (6) gives

 ||D_p||<=P^(-5/6+a),
 ||kappa P^2 D_p^6||<=P^(-3+6a),
 ||kappa P D_p^6||<=P^(-4+6a).

Hence for sufficiently small epsilon,

 ||A_p||<=1+O(P^(-2/3+epsilon)),
 ||A_b||<=exp(O(kP^(-2/3+epsilon)))=O(1).             (7)

Equations (3) and (7) show exactly why the infinitely many deeper Gaussian scales cost no power of the auxiliary modulus. They also preserve all original Fourier and physical-square tails. Therefore the restored observation retains the same complete cubic low estimate as (6) at T=Z. This is only the cubic core and does not establish whole-probe R2 or bound the principal/unit good core.

### 6. Interaction with the high auxiliary average

On a genuine dynamic central line x_r>=1/2+fixed buffer, z_r>=1/6+fixed buffer, (4) is a product of local factors F_p(v) with v=x+z-1/6 and Re v>1/2. Each satisfies F_p(v)=1+O(P^(-c)), c>1/2, uniformly in all heights. Thus in a prime-by-prime auxiliary ensemble one must multiply the exact local deletion factor by F_p(v); it is not correct to replace it everywhere by F_p(x).

This modification has a uniformly small local absolute error and fixed-logarithmic seminorm cost. The exact scalar normalization and full nonprincipal average are checked separately in Part B below, rather than inferred from the positive operator-norm bound (7). The principal/unit frequency is intentionally restored, not removed. The remaining whole-probe low burden remains explicit.

## Part B. The complete absolute Poisson projection and its restored form

Use the unrestricted all-good-prime ensemble of [POLYNOMIAL_AUXILIARY_ENSEMBLE.md](POLYNOMIAL_AUXILIARY_ENSEMBLE.md), Part A §§2, 5 and 8, with ambient R0, P=(log R0)^64 and k=floor(log R0/(65 log log R0)). Keep X,Y and the original Gaussian scale T positive. The auxiliary subset J is fixed throughout each physical observation, with the original calibration and all new holes. For an arbitrary fixed subset E of the original nonprincipal sixth-power-free rows u!=1, let I_(J,E) be its contribution after the exact first Poisson transformation. This includes the actual bad set E_b with its original primitive labels and selected zeros. The set must be independent of J; the new p holes are represented by zero multipliers, not by relabeling E.

Under the same user finite-order Q hypothesis, the claim is

  | E_J I_(J,E)(X,Y,T) |
       << R0^(-1/20) X^(-3/2) T^4 Y^2.                    (1)

This is asserted for the unmarked original probe and its fixed half-damping. The implied constant depends on the original fixed S0 and profiles, not on E, X,Y,T or R0. It holds for sufficiently large R0, and bounded remaining R0 may be absorbed if needed. The actual observations being averaged have different auxiliary moduli, each of norm at most R0.

### 1. An absolute bound with no auxiliary-modulus power

Use the exact source local-full-coefficient with A=c n^3 and frequency H=u a^6. The first-Poisson coefficient F(s,A,H) is a sum of at most Ns residues. At the bad auxiliary modulus b*, its primitive Gauss factor has modulus exactly sqrt(Nb*) when the frequency is a unit, and is zero otherwise. After this CRT factor is extracted, the remaining Gauss sum has modulus at most NA. Every original phase and normalized squarefree gamma_2(c) has modulus at most one. Consequently the normalized source coefficient satisfies

              |K(c,n,s,a;u)| <= (Ns)(NA).                  (2)

This bound uses the exact sqrt(Nb*) cancellation in the source. It is independent of the norm and number of new auxiliary primes. Their unit masks only remove terms.

On the original lines Re x=3, Re w=3, Re z=2, formula (2) bounds the coefficient sum by

  [sum_c (Nc)^(-5/2)] [sum_n (Nn)^(-7)]
  [sum_s (Ns)^(-2)] [sum_a (Na)^(-12)] [sum_u (Nu)^(-2)],   (3)

with the original squarefree/sixth-power-free restrictions harmlessly retained or enlarged. All five sums converge. The half-damping only inserts the additional factor (Nn)^(-1/2)<=1 into this absolute bound. In particular every base S0 Euler row F_u(3+it_x,3+it_w,2+it_z) is bounded by an absolute fixed constant uniformly in u and all imaginary parts.

The common Mellin factor has absolute scale exactly X^(-3/2)T^4Y^2. Its height profile is rapidly decreasing in all three real variables: Phi(4+i(t_x+t_z)) gives exp(-(t_x+t_z)^2), while M(2+it_z) and What_1(3+it_w) are rapidly decreasing. The invertible change (t_x,t_z,t_w)->(t_x+t_z,t_z,t_w) proves a joint integrable Schwartz majorant. Its constants are independent of b* and of the physical scales, whose imaginary powers have modulus one.

### 2. Uniform row and common-height truncation

Write the exact resummed row multiplier for subset J as Z_J(u;x,w,z)=product_(p in J) Z_p. On the absolute lines, the reviewed local expansion gives Z_p=chi_p(u)+O((Np)^(-3)), including its zero definition at an excluded prime. Hence

                        |Z_J| <= 2                        (4)

for all sufficiently large R0, uniformly in EVERY u and in the full unbounded height range. This estimate needs no Q and no conductor restriction.

The ideal counting bound # {a:Na<=U}=O(U) implies

             sum_(Nu>R0) (Nu)^(-2) << R0^(-1).             (5)

Thus the full row tail contributes O(R0^(-1) X^(-3/2)T^4Y^2), uniformly in E and J. On the remaining rows Nu<=R0 the actual Kummer conductor is at most 6^12 R0^5, by the reviewed conductor-discriminant argument. Truncate all three COMMON heights to |t_x|,|t_w|,|t_z|<=R0. The Schwartz majorant and (3)--(4) make the removed height portion O_A(R0^(-A) X^(-3/2)T^4Y^2), with arbitrary fixed A. This is done on the original absolute lines, so crosses no reciprocal-L poles.

On the retained row/height box the reviewed ensemble estimate applies simultaneously with the same prime pool and the same positive normalization. It gives |E_J Z_J|<=R0^(-1/20). Multiplication by the original base S0 coefficient, absolute summation using (3), and integration against the original profile prove (1). All interchanges are justified by (3)--(4). No infinite conditionally continued u sum has been exchanged on a critical line.

### 3. Finite markers and actual polynomial physical scales

The same argument accepts any original fixed finite number of selected-prime slots and finite compensation terms, PROVIDED their actual prime supports are disjoint from the auxiliary pool and their absolute coefficient/scale mass has been retained. The high multiplier at a newly deleted unselected p is still exactly Z_p. Alternatively impose the selected divisibility constraints in (2), which only remove terms, and then pay the actual finite outside weights and scale changes by triangle.

Concretely, if those fixed operations have a known absolute bound Z^B times the right side of (3), with B fixed independently of R0, their averaged nonprincipal contribution is bounded by Z^B times (1). For the original marked windows at fixed positive powers of Z and R0=Z^C with C fixed, the auxiliary prime scale (C log Z)^64 is eventually below every marked prime annulus, so the required disjointness is literal. The constant C is fixed before taking Z to infinity. No number of marked slots is allowed to grow with k in this extension.

If X,Y,T and the fixed finite outside weights are bounded above and below by fixed powers of Z, their whole absolute scale is at most Z^B0 for some fixed B0. Choosing a fixed C>20(B0+A) and setting R0=Z^C gives an averaged nonprincipal contribution O(Z^(-A)), for any requested A>0. This is a property of the new ensemble of admissible observations. It is not a pointwise bound for a previously fixed observation, and the auxiliary modulus is now as large as Z^C.

For the actual original finite compensation no conditional outside-price assumption is needed. In the source compensated-probe-definition, write D=p_J for the rescaled slot product and E=p_(J^c) for the marked product (this E is not the selected row set). The summand has coefficient (ND)^(-3/2), scales (X/ND,Y/ND,T NE), and a bounded divisibility indicator. Its absolute scale is exactly

 (ND)^(-3/2)(X/ND)^(-3/2)(T NE)^4(Y/ND)^2
       =(ND)^(-2)(NE)^4 X^(-3/2)T^4Y^2.

Summing all subset choices and actual slot tuples costs at most

 product_i sum_(p in slot_i) |W_i(Np/P_i)|[(Np)^4+(Np)^(-2)]
       << product_i P_i^5=Z^(5 ell),

by the elementary ideal count; ell=sum ell_i is fixed. The original and core marker are both bounded indicators, so the same absolute bound holds for either of their actual finite compensation formulas. Disjointness from the auxiliary pool ensures the unselected local factor at every new prime remains Z_p. In the fixed geometry X=Z^(17/48), Y=Z^(23/48), T=Z and ell=1/6, the complete marked scale is thus Z^(505/96). The original principal normalizer satisfies |A_T(Z)|^(-1)<< (log Z)^K, with K fixed. Therefore the corresponding normalized marked nonprincipal average, including the restored version of Section 5, is

                   << R0^(-1/20) Z^(505/96+epsilon).         (5a)

For example R0=Z^128 makes the displayed power before epsilon equal to -547/480; hence (5a) is O(Z^(-1)) for any fixed sufficiently small preliminary epsilon. This is an asymptotic assertion with 128 fixed before Z tends to infinity, including the eventual disjointness of the polylogarithmic auxiliary pool and the original positive-power slot annuli.

### 4. What remains

The only Kummer-principal sixth-power-free row is u=1. Its coefficient is NOT reduced by this projection. It still contains the original target reciprocal and all removed Euler factors. Even if a separately justified Gaussian-scale restoration fixes its principal residue exactly, one must still prove a compatible bound for the entire resulting physical observation, including this unit good-core contribution. Equation (1) and its arbitrary-power specialization do not provide that bound or a zero exclusion.

### 5. The exact Gaussian-scale restoration and scalar normalization

This section applies the explicitly defined operator of Part A. Its estimates are proved directly on the absolute lines and do not borrow Part A's principal contour or positive-T low conclusion. For the half-damped observation let c_Sb=c_S0 product_(p in J)(1-(Np)^(-1))^2 and J_b(T)=I_b(T)/c_Sb. Keep the prime pool, X,Y,slots,all holes and every compensation coefficient fixed while changing only T. Set

 D_p f(T)=Pp^(-5/6) f(T/Pp),
 F_p(v)=(1-Pp^-2)[1-(1-Pp^-1)Pp^-v-kappa(p)Pp^(1-6v)]
                                      /[1-kappa(p)Pp^(2-6v)].

The physical restoring operator A_p has high symbol F_p(a), where a=x+z-1/6; this is not F_p(x) away from z=1/6. Relative to the base normalized row I_S0/c_S0, the EXACT new local multiplier is

 Zp_rest(u;x,w,z)=(1-Pp^-1)^(-2) F_p(x+z-1/6) Z_p,half(u;x,w,z). (6)

The scalar normalization in (6) is essential: it cannot be dropped or absorbed into arbitrary subset weights after the ensemble law has been fixed. It is included as part of each prime's complex factor in the same elementary-symmetric-polynomial average.

On the original absolute lines a_r=29/6. The denominator of F_p has modulus at least 1-Pp^-27, so F_p(a)=1+O(Pp^-2), uniformly in all heights. Consequently

 Zp_rest=chi_p(u)+O(Pp^-1),  |Zp_rest|<=1+O(Pp^-1),           (7)

with the same zero convention at p|u or a hole. All constants are independent of u and of the heights. Thus product |Zp_rest|<=exp(O(k/P))<=2 for all sufficiently large R0. On the retained row/height box the weighted prime mean differs from the already reviewed leading-character mean by only O(P^-1). This is O((log R0)^(-64)), smaller than (log R0)^(-4). The exact without-replacement lemma is unchanged, and gives the same R0^(-1/20) mean of product Zp_rest.

The geometric defining series of A_p has coefficients kappa(p)^j Pp^(-3j) and arguments T/Pp^(6j). Applied to the unaveraged absolute majorant of Section 1 (without its later ensemble saving), its j-th term has the additional price Pp^(-24j) from T^4. The numerator has only three explicitly prescribed dilations. All these series converge absolutely, jointly with the five ideal sums and the full common-height integrals. For each finite J one may therefore multiply their true high symbols before applying the ensemble. The truncation argument of Section 2 now proves

 | E_J A_b J_(b,E)(X,Y,T) |
       << R0^(-1/20) X^(-3/2) T^4 Y^2,                     (8)

where J_(b,E) is the literal selected nonprincipal frequency component, and E is unchanged. The fixed c_S0 is absorbed in the constant. The actual finite markers of Section 3 are permitted with their stated outside price. Combining (8) with a separately established principal-component comparison is legitimate; replacing that component comparison by a formula for the whole unaveraged J_b is not.

The same LOCAL ensemble statement also holds on the reviewed half-damped domain C, with x_r>=1/2+delta, w_r>=1-epsilon and z_r>=1/6-epsilon, where epsilon<min(delta/8,1/200). Here a_r>=1/2+delta-epsilon, so 6a_r-2>1 and direct evaluation gives F_p(a)=1+O_delta(Pp^(-1/2)). Equation (6) therefore still has leading chi_p(u) and an O_delta(Pp^(-1/2)) remainder. Its prime-average error is O((log R0)^(-32)), and the identical without-replacement argument applies. This is uniform for finite original row sets, the prescribed polynomial common-height/conductor/hole windows, and genuinely absolutely convergent sums with their actual majorants. It is not permission to move or interchange a conditionally continued infinite sum on C.

### 6. Independence from the corrected moving Gauss-hole formula

The user's correction 3c92c606 inserts the necessary outside factor bar rho_u(d) in the different identity expressing a Gauss-series hole R_(u,M) through R_(ud). Neither (2) nor the exact local Z_p used here calls that identity. They follow directly from the source first-Poisson coefficient, its full bad-modulus CRT cancellation, and deletion of its scalar local P_p. In particular no moving-hole phase has been discarded in the signed high average. This statement concerns these specific derivations, and does not excuse use of the earlier phase-free Gauss-hole identity elsewhere.

## Part C. Actual positive-scale envelopes for the six other covered types

### 1. Frozen geometry and assertion

Use eta=1 and the original physical geometry for each finite compensation subset of length d_slot:

 X'=Z^(17/48-d_slot), Y'=Z^(23/48-d_slot), P~Z^(1/6-d_slot), 0<=d_slot<=1/6.

The slot windows, their weights, X',Y', every rescaling coefficient, the fixed bad data and a chosen auxiliary modulus b are fixed at the AMBIENT Z. Only the common Gaussian scale T varies, with 0<T<=Z. It varies in every compensated summand, without choosing new slots or a new auxiliary at the smaller scale. Write I_(j,b)(T) for the actual contribution of one of the six nonprincipal types of the published POLYNOMIAL_AUXILIARY_ENSEMBLE.md, Part D, to this observation. Both original/core nonflat markings and original or half-damped physical n weights are allowed. The auxiliary is squarefree, disjoint from bad data and selected slots, with Nb<=Z^C and nonprincipal order-dividing-six local factors.

Under the SAME finite-order Q assumptions, for each prescribed epsilon>0,

 |I_(j,b)(T)| << (Nb Z)^epsilon Z^(theta_j) (Z/T)^(1/6+epsilon).   (1)

Here theta_j are, in order quadratic, pure fifth, mixed35, mixed245, mixed234, mixed2345:

 -439/2304, -209/960, -3073/16384, -133/34560, -1/512, -1/512.

The pure-fifth bound and selected-slot input are the user's contributions. Constants have the same fixed-data dependence as the published transfer and are independent of b and T. In particular this statement does not require Nb<=T^C. The factor (Z/T)^epsilon allows the fixed small-power and logarithmic losses of the actual scale decompositions. No first-flat, exclusive-s, unit-core, missing residue-1 or whole-probe assertion is added.

### 2. Why the common holes and contours survive

The exact first-Poisson bad CRT is applied with the single chosen b before any type split. It cancels the auxiliary norm and leaves the actual joint-row phase conjugate(xi_b(u6)), together with its unit masks. Changing T affects only the Gaussian argument, never that phase, the ray group or a column character. The inverse-column correction and phased smooth-hole identity are exactly those in published Part D:

 J_b(v)=product_(p|b)(1-eta(p)psi_row(p)(Np)^(-v))^(-1),
 B_row(S;b-unit)=sum_(d|b)mu(d)psi_row(d)B_row(S/Nd).

In particular the moving phase psi_row(d) is retained; no omitted-phase Gauss-series identity is used. Fix the reciprocal contours in a compact subinterval of (1/2,1) before T varies. The actual full e measure is dS/S, and L/S is independent of e for each of the six types. After S'=S/Nd, the scalar payment remains (Nd)^(sigma-1), independently of T. The two divisor products and their fixed derivatives cost (Nb)^epsilon uniformly. The ambient for every unbounded sum contains Nb,Z, the actual labels and Z/T; it does not replace Nb by a smaller-scale bound.

It therefore suffices to inspect the actual powers of T in the six already proved full Fourier/Gaussian envelopes. The following inspections keep the complete square-layer sums and their boundary ranges. Inferring (1) solely from a numerical exponent at T=Z would not be valid.

### 3. Quadratic: retain the true finite square-layer boundary

Use the complete quadratic-density proof, published QUADRATIC_DUAL_N1.md Part XI, equations (14)--(17). Put a=1-sigma in [1/8,1/2], D=3a/(1+a),

 F=7D/8+1/2-a/2, kappa=F or F-D/4, K=TP/X'.

Both kappa are strictly greater than 1/2. Before bounding the physical square sum its genuine expression, for K>=1 and apart from T-independent coefficients, is

 K^beta sum_(q_r<=K^(1/6)) q_r^(-2-6beta+epsilon),
 beta=kappa/3-a.                                         (2)

This is the finite bound in that proof, not an extension of a divergent ideal series to infinity. Ideal counting gives, uniformly on these compact a intervals,

 (2) <<_epsilon K^(max(beta,-1/6)+epsilon).                (3)

At equality the extra logarithm is absorbed by epsilon. For beta<-1/6 the actual upper cutoff supplies the -1/6 boundary power. This point matters: the second printed main monomial in (17), viewed alone at a=1/2, has beta=-5/24 and cannot be used as a uniform scale exponent. Formula (3), not that artificially separated monomial, is the required bound. The corresponding actual boundary coefficient is precisely equation (16) of the same proof, whose normalized Z exponent is at most -7/24, stronger than theta_quadratic.

When K<1, the original Fourier factor [1+X' V^3 q_a'^6/U]^(-M) is retained. Its positive moment gives any predetermined positive power K^M; choose M large enough before summing the now strictly convergent r series. This is stronger than K^(-1/6-epsilon). The a' series is convergent because 2kappa>1. Every Gaussian annulus has K_l=e^l K; the powers and logarithms in (3) only create fixed exponentials or polynomial factors in |l|, absorbed by the original e^(-c l^2).

For a branch beta>=-1/6, changing T from Z decreases its monomial by (T/Z)^beta, no worse than (T/Z)^(-1/6). For beta<-1/6 use the actual boundary branch (3), already present and stronger at T=Z. Thus the same complete numerical quadratic bound at Z implies (1), without assuming all isolated monomials in (17) have acceptable powers.

### 4. Pure fifth: the user's actual full-scale estimate

The user's PURE_FIFTH_SELECTED_Q_GAIN.md, equation (C) and its immediately following flat-transfer paragraph, gives the actual all-scale bound

 const(Z,nu) max_(1/8<=a<=1/2) (Y'/T)^a (TP/X')^([F_5(a)+(6a-2)_+]/5),

including the selected multiplier P^(-1/8), all physical r,h0,a' and genuine exceptional j=5 boundary. That proof establishes

 beta_5(a)=[F_5(a)+(6a-2)_+]/5-a >= -1/10.                (4)

The selected-slot pointwise improvement is uniform in T and does not change (4). The same full Schwartz moments handle subunit cutoff, and the genuine physical h0 divisor support was already used in obtaining this bound. Consequently this entire term at T is at most (T/Z)^(-1/10) times its proved bound at Z. This preserves the user's theta_fifth=-209/960 and is stronger than (1).

### 5. Mixed35: low-bin cumulative contraction and high-bin formula

In the complete pair-Q-slot proof (published Part XXIII), the low-bin range 1/8<=a<=1/4 has true cumulative frequency contraction gamma=3/16, including the whole smooth scale and actual Fourier/Stieltjes integration. The full scalar is (Y'/T)^a, so its total T power is

 beta_35,low=3/16-a >= -1/16.                            (5)

The h0<=r boundary has already been summed there, leaving r^(6a-3) and q_a'^(-9/8); both series have strict margins. Changing T does not alter the fixed slot bound or the rational reference boxes.

For 1/4<=a<=1/2 the same proof's exact all-scale equation (12) is

 (Y'/T)^a P^(-1/8)(TP/X')^(kappa/3),
 kappa=3a/(1+a)+(1-a)/2.

Its T power kappa/3-a decreases on this interval because its derivative is 1/(1+a)^2-7/6<0. At a=1/2 it is -1/12. The W shell, true h0 boundary and complete r/a' tails have already been included in this formula. Thus (1) preserves the complete -3073/16384 bound, not merely the clean reference-box calculation.

### 6. Mixed245: the oversized-slot and finite harmonic cases

In published Part XIX, let D(a) be 1/6+3a on [1/8,1/6], 1/3+2a on [1/6,1/3], and 1 on [1/3,1/2]. Put

 J=max{7D/8+(1-a)/2, D(4-a)/4+(2-3a)/4}, B=2-a+D/3.

For P_c<=sqrt(M), the actual M Fourier moment has T power J/2-a. The source's strict first-flat exponent is 6a-2-3J<=-19/8, so

 J/2-a >= 1/16 > -1/6.                                  (6)

Its actual r exponent with the fifth boundary is at most -95/48 and the a' exponent at most -175/64, both strict. These facts are statements before substituting T=Z.

For P_c>sqrt(M), the proof first integrates W and obtains (C_l/X')^(B/5), C_l=e^l TP, multiplied by its fixed M/slot factors. The resulting T exponent is

 beta_245,large=B/5-a.

On the three a intervals it is respectively 37/90-a, 19/45-16a/15, and 7/15-6a/5, whose minimum is -2/15. The remaining physical r exponent is 6a-4<=-1. At equality it is only summed to its TRUE finite nonempty Gaussian-annulus cutoff r<=O(C_l^(1/6)), costing a logarithm, not a positive T power. Small or empty annuli retain their original rapid tail. The enlarged upper bound M<=Z^(1/3) and the selected-slot scale are fixed at the ambient Z; using them when T decreases is a positive enlargement, and leaves the endpoint exponent calculation unchanged. Therefore the complete theta_245 survives with scale loss at most (Z/T)^(2/15+epsilon), sufficient for (1).

### 7. Mixed234 and mixed2345

Both complete physical proofs (published Parts XX and XXII) keep the exact scalar (Y'/C_l)^a and C_l=e^l TP. In the low bins 1/8<=a<=3/8 their true cumulative exponent is gamma=(2-2a)/5. Hence

 beta_low=gamma-a=(2-7a)/5 >= -1/8.                      (7)

The full physical r exponent is (42a-22)/5<=-5/4 and the a' exponent <=-3/2. For mixed2345 the extra true shell W/H0 is included before this result; its remaining W power is a-1/2<=-1/8 and its H0 power -1/10-7a/5<0. No density bound is divided by H0.

For high bins 3/8<=a<=1/2, the three actual Fourier exponents are

 gamma_1=1/2-a/6, gamma_2=3/4-a/4, gamma_3=2/3-a/4.

Subtracting the inverse scalar a gives minima respectively -1/12, 1/8 and 1/24. The remaining family shell exponents are strictly negative; in mixed2345 the fifth shell and H0 have already been paid by the proof's equations (25)--(27). The r and first-flat powers are <=-3/2, and the a' powers are <=-5/2. Thus neither type loses more than (Z/T)^(1/8+epsilon), and each keeps theta=-1/512.

### 8. Uniform losses and the Gaussian-only restoring operator

For every finite compensation subset, the old Z-point budget is valid before taking its signed finite sum. The bounds above insert the SAME factor (Z/T)^(1/6+epsilon), independently of the subset. The original subset-dependent coefficients and slot ranges are frozen at Z, so summing them retains (1). Fourier/Gaussian derivatives and all common-hole losses are paid at their actual labels before infinite sums; the strict source margins above absorb label powers. The only marginal r case was retained as a finite logarithm. Optional half damping is inserted at the already proved positive n0/r stage. It never compares the modulus of two signed completed sums.

As a corollary for the explicitly defined HALF-damped Gaussian-only restoring operator in Part A, set a0=1/6+epsilon and use the norm sup_(0<T<=Z) (T/Z)^a0 |I(T)|. Its elementary dilation D_p f(T)=P^(-5/6)f(T/P) has norm <=P^(-5/6+a0). Therefore the exact local operator

 A_p=(1-P^-2)[1-(1-P^-1)D_p-kappa(p)P D_p^6]
                           [1-kappa(p)P^2 D_p^6]^(-1)

has an absolutely convergent geometric definition and norm <=1+O(P^(-2/3+epsilon)). The denominator ratio is P^(-3+6a0)=P^(-2+6epsilon)<1; the other sixth-power numerator price is P^(-3+6epsilon). For a polynomial auxiliary ensemble P=(log R)^64, k<=log R/(65loglog R), product_(p|b)||A_p||=O(1). Its scalar c_Sb inverse is also uniformly bounded because product(1-P^-1)^(-2)=exp(O(k/P))=O(1). Consequently, once this additional physical operator is used, the six complete nonflat low exponents in (1) persist for its half-damped observation.

This last step uses the new operator's exact definition, not a claim that it is an original probe or an original first-flat. It provides no full principal comparison, no unit-core bound and no missing core-type bound. The arithmetic input Q remains unchanged.

## Part D. The complete restored auxiliary-averaged high theorem

### 1. One exact physical family at each ambient scale

Fix eta=1, the original data S0 and xi0, the half-damped physical n weight, and either the original or core nonflat marker with its literal finite compensation. Use the original geometry

 X=Z^(17/48), Y=Z^(23/48), ell=sum ell_i=1/6,
 h=13/16, C(s)=s-11/16.

There are a fixed number K of original disjoint positive prime slots. Their windows, coefficients and all subset rescalings are the original ones. Set R0=Z^128, P=(log R0)^64 and k=floor(log R0/(65 loglog R0)). On the pool of ALL good primes outside S0 choose an unordered k-element subset J with the exact positive law

 Prob(J)=product_(p in J) W(Np/P) / e_k((W(Np/P))_p).

Here W is the fixed smooth nonnegative norm weight of the reviewed ensemble. The pool is not conditioned on a reciprocity ray. For sufficiently large Z it is disjoint from all the original marked prime supports. Put b=product_(p in J)p, so Nb<=R0, use xi_p=bar chi_p at each added prime, and form the actual enlarged-bad-set observation I_b(T). At this ambient Z, ONLY its Gaussian scale T varies: X,Y, all slots, the same b, every mask and every original compensation coefficient remain fixed.

Use the reviewed scalar and physical dilation definitions

 c_Sb=c_S0 product_(p|b)(1-(Np)^(-1))^2,
 J_b(T)=I_b(T)/c_Sb,
 D_p f(T)=(Np)^(-5/6)f(T/Np),
 A_b=product_(p|b)(1-(Np)^(-2))
       [1-(1-(Np)^(-1))D_p-kappa(p)(Np)D_p^6]
       [1-kappa(p)(Np)^2 D_p^6]^(-1),

where kappa=bar alpha^6. The inverse is the actual absolutely convergent series sum_(j>=0) kappa(p)^j (Np)^(-3j) f(T/(Np)^(6j)). Define

       mathscr J_rest(Z)=A_T(Z)^(-1) E_J [A_b J_b(Z)].       (1)

The ambient slot normalizer A_T(Z) is unchanged. Its inverse is O((log Z)^K). Equation (1) averages explicitly defined physical observations; it is not a formal multiplier assigned to a previously fixed auxiliary probe.

### 2. Full high theorem

Assume the same finite-order Q hypothesis as the reviewed auxiliary ensemble. Fix 1/2<sigma<1 and also retain the original principal safe-line assumption: 1/zeta_K^S0 is holomorphic on Re s>=sigma and has fixed polynomial-height bounds on closed bounded real strips. This latter condition is not inferred from the nonprincipal ensemble estimate.

Define the FIXED signal

 f_half,S0(Z)=int_(2) Z^(s-11/16) exp((s-5/6)^2)
                      H_half,S0(s)/zeta_K^S0(s) ds/(2pi i).

Then there is a fixed m_sigma>0, which may be chosen at most 1/96, such that

 |mathscr J_rest(Z)-f_half,S0(Z)|
                 << Z^(sigma-11/16-m_sigma).              (2)

All original common heights and the complete frequency sum are included. The constants may depend on the fixed principal buffer, original profiles and slot system. The auxiliary exponent 128 is fixed before Z tends to infinity. The signal is independent of b,R0 and the selected subset J.

### 3. Proof using the actual principal and nonprincipal pieces

The reviewed global convergence of the physical dilation series allows the exact first-Poisson split J_b=J_b,1+J_b,neq1, before any comparison is asserted. Here J_b,1 is the literal u=1 good-core contribution. The other five units belong to J_b,neq1.

By Part A of this report, uniformly in J,

 A_T(Z)^(-1) A_b J_b,1(Z)
      =f_half,S0(Z)+O(Z^(sigma-11/16-m0))                  (3)

for a fixed m0>0. The complete four-contour proof of (3) keeps the original reciprocal-line assumption and all three scalar residue/remainder pieces. Its exact high symbol is product F_p(x+z-1/6), which becomes product F_p(s) only at z=1/6. At the double scalar residue this exactly cancels the principal deleted factors. No logarithmically close varying signal is substituted for the fixed one.

For the complementary piece, the independently reviewed Part B of this report, equations (5a) and (8), gives directly on the original absolute (3,3,2) lines

 |A_T(Z)^(-1) E_J A_b J_b,neq1(Z)|
       << R0^(-1/20) Z^(505/96+epsilon)
        = Z^(-547/480+epsilon).                           (4)

The exponent in (4) includes the ENTIRE original finite compensation. Specifically, a subset with rescaled product D and marked product E has outside coefficient (ND)^(-3/2) and scales (X/ND,Y/ND,T NE). Its absolute Poisson scale is therefore multiplied by (ND)^(-2)(NE)^4. All subset and prime-tuple sums cost at most product_i P_i^5=Z^(5ell). Combining this with X^(-3/2)Z^4Y^2 gives 505/96. The slot-normalizer logarithms have been included in epsilon.

The exact normalized local multiplier used in (4) is

       (1-(Np)^(-1))^(-2) F_p(x+z-1/6) Z_p,half.

Thus neither the c_Sb scalar nor a moving Euler phase has been discarded in the signed average. On the absolute lines it equals chi_p(u)+O((Np)^(-1)); the no-replacement law and full row/common-height truncation have already been paid in the cited theorem. The geometric inverse has the joint absolute price (Np)^(-27j), so its series commutes with the five absolutely convergent ideal sums, the three height integrals and the finite ensemble. No conditionally continued infinite sum is interchanged on a critical contour.

Choose the preliminary epsilon small enough that (4) is O(Z^(-1)). Take 0<m_sigma<=min(m0,1/96). Since sigma>1/2,

 sigma-11/16-m_sigma > -19/96 > -1.

Averaging (3), adding (4) and decreasing m_sigma if needed proves (2).

### 4. Scope and remaining analytic burden

The reviewed half-damped principal factor is nonzero in Re s>1/2, so this fixed signal retains the original off-line target poles and their multiplicities. This is the existing principal visibility statement; theorem (2) does not say that such poles are absent.

The complete cubic low estimate survives the physical restoring operator by its reviewed full positive-T norm. Part C supplies the actual positive-T envelopes and hence the corresponding transfer for the six other explicitly covered types. None of these separate statements supplies the missing bound for the WHOLE expression (1). In particular the u=1 good core has not been bounded by the auxiliary projection, and no complete low estimate or zero exclusion follows here. The result is a high comparison for the new auxiliary ensemble, not a bound for the same signed row sum of one fixed auxiliary observation.
