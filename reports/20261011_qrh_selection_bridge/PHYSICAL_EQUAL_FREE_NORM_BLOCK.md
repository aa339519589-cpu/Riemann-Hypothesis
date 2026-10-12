# The physical equal-free-norm block with all compensation tags retained

Retain the actual compensation tag t=(D,Ec,En; every original slot prime), the original physical c, and the free squarefree ideal d=c/Ec. For the same half-damped, positive-auxiliary, original/core nonflat observation and old Gaussian-T restorer, this theorem proves

    |C_E| <<_epsilon Z^(-3/8+epsilon),
    E((t,c),(t',c'))=1_(N(c/Ec)=N(c'/Ec')).

The estimate also holds for any real symmetric submask 0<=B<=E that depends only on these retained original labels, as specified in Section 4. It can therefore remove the equal-free-norm part left after the already controlled original-c quotient band. Distinct ideals of the same norm are included. The tag-level bounded-phase input, fully labelled unit-square estimate and infinite-cutoff justification are proved below.

This is exactly the exponent -3/8 with an arbitrarily small epsilon loss, without a fixed additional power saving. The different-free-norm sum with its original Mobius coefficients remains unestimated; no whole-cross or zero-exclusion conclusion follows.

## Original observation and complete published inputs

The physical sum, auxiliary probability law, roots, compensation and normalization are those of [UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a99fbcda6b496eb36811ed80f3bfe5b18b7e2585/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md). The actual class vectors are averaged over the auxiliary prime BEFORE taking their two-copy product; the two copies use independent means. The [all-s fixed-c unit proof and exact h!=h' subtraction](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a99fbcda6b496eb36811ed80f3bfe5b18b7e2585/reports/20261011_qrh_selection_bridge/PHYSICAL_COPRIME_QUOTIENT_BAND.md) remain unchanged. The retained slot powers and elementary random-sign mask factorization are [Parts I and II of the subsequent refinement](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a99fbcda6b496eb36811ed80f3bfe5b18b7e2585/reports/20261011_qrh_selection_bridge/PHYSICAL_COPRIME_BAND_SLOT_REFINEMENT.md).

The present proof extends the bounded coefficient to each retained compensation tag by revisiting the positive-pair proof at its original common-column step. It does not infer that stronger input solely from a norm estimate for the sum over tags. All new tag counts, equality-block estimates and arbitrary-submask bounds are included. The [independent review](REFEREE_PHYSICAL_EQUAL_FREE_NORM_BLOCK.md) checks those source-level steps. No first-flat or further infinite-prime normalization is included.

## 1. Original labels and the source-level bounded-phase input

Keep the same half-damped, positive-auxiliary, original/core nonflat observation, all original prime slots and their ambient normalizer, exponential prime mean, and OLD Gaussian-T restorer. In each original compensation term let

 t=(D,Ec,En; actual prime in each original slot).

The original priority puts a marked prime in Ec when it divides c, and in En otherwise; then it divides n. Thus D,Ec,En partition the original fixed slot set, Ec|c, and (En,c)=1. This definition is on the original physical sum, before completing m or extracting its unit part. It is a disjoint subdivision, not an extra prime sum. Set

 lambda=(t,c), d_lambda=c/Ec,
 V_lambda=(V_(gamma,t,c,h))_(gamma,h),
 S_(gamma,lambda)=sum_h V_(gamma,t,c,h).

All compensation signs, scaled windows, actual slot weights and outside factors are included in V and S. The two auxiliary prime means remain independent. The quotient d_lambda is a good squarefree ideal with (d_lambda,Ec)=1. Its norm is an integer.

The true uniform-B positive-pair proof allows an arbitrary bounded coefficient alpha_(t,c), not only alpha_c. This follows directly from Part A, Sections 3--7 of the published UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md:

* Freeze the rescaled tuple D, the assignment of marked slots, and En, and apply the ORIGINAL Minkowski step in the same n column.
* Its Section 5 already expands Ec and Ec' separately in the two copies. The new multiplier alpha_(D,Ec,En,c) conjugate(alpha_(D,Ec',En,c')) is independent of the common six-free variable h0. It does not change the auxiliary-character cancellation, the conductor of the remaining Hecke character, or its unit holes.
* The displayed principal lcm majorant and the displaced-contour error take absolute values after that cancellation. A multiplier of modulus at most one leaves each bound valid. The same original l1 sums over En and D, with their exact negative powers, then apply. No cardinality factor for the set of tags is charged here.
* Each higher-s reduction retains original c and all compensation labels. Its temporary row phases and complete-column principal boundary are unchanged. The old restorer only changes T; alpha_(t,c) is fixed during every such dilation.

Consequently, for finite sums and then their source-defined limits,

 M_delta:=sup_(|alpha_lambda|<=1)
           ||sum_lambda alpha_lambda (Nc)^delta V_lambda||
  << Z^(7delta/6+epsilon) Y^(-1/2)+exp(-cZ)Z^(C_delta),             (1)

for fixed small delta>=0. For delta>0 this is proved at the actual Gaussian:

 (Nc)^delta V_G(Nc(Nn)^3/T_eff)
    =T_eff^delta(Nn)^(-3delta)V_delta(Nc(Nn)^3/T_eff),
 T_eff=T NE<=C Z^(7/6).

V_delta is a fixed log-Schwartz profile. Thus the same source proof applies without any auxiliary-modulus power. Equation (1) is solely a positive-class estimate; it is not a whole-observation bound with arbitrary replacement coefficients.

## 2. Fully labelled unit-square estimate

Complete each m column and take the actual auxiliary mean before inserting any pair mask. The raw first-Poisson projection, with labels lambda kept outside its sums, gives the fixed-base unit vector U_(gamma,lambda) with

 sum_(gamma,lambda)(Nc)^e |S_(gamma,lambda)-U_(gamma,lambda)|
                                             <<_(e,N) Z^(-N).    (2)

The complete raw absolute proof already sums absolute values over all original compensation tuples. Retaining them as labels does not change that proof or introduce a new count. Small c powers are absorbed in the same actual Gaussian moments. The vector U has no moving auxiliary-prime holes; their removal is in the raw polynomial-box tail, exactly as in the reviewed fixed-c result.

On this literal unit part n=r^2, so En is denoted Er. For a FIXED tag, put r=Er v and c=Ec c0 in the exact all-s unit kernel. The reviewed fixed-c argument gives the square price

 (X/T)^(2/3) (ND)^(-11/3)
                 (NEc)^(-5/3)(NEr)^(-8/3),                       (3)

times the squared original slot weights, logarithms and preliminary small powers. Here D^(-11/3) is exactly the square of the physical D^(-3/2) times X'^(1/3), X'=X/D. The c label is still the ORIGINAL c. There is no Cauchy sum over Ec in (3), since the tag is fixed.

Sum the squared quantities over all actual tags. Elementary ideal counting gives, in a slot of norm scale P_i,

 sum_p |W_i|^2 (Np)^(-5/3)<<P_i^(-2/3),
 sum_p |W_i|^2 (Np)^(-8/3)<<P_i^(-5/3),
 sum_p |W_i|^2 (Np)^(-11/3)<<P_i^(-8/3).

The weakest factor per slot is P_i^(-2/3), and every slot occurs exactly once. Since product_i P_i=Z^ell, ell=1/6, and the ambient A_T inverse is only logarithmic,

 Q_e:=sum_(gamma,lambda)(Nc)^e |U_(gamma,lambda)|^2
       << Z^(-2ell/3+O(e)+epsilon)(X/T)^(2/3)
       = Z^(-13/24+O(e)+epsilon),                               (4)

at X=Z^(17/48), T=Z. Fixed extra divisor powers are allowed as in the reviewed Gaussian estimate. The all-s powerful-ideal sum and the old-restorer bound are taken at each fixed tag and are uniform; their square-sum version uses Hilbert-space Minkowski, not a new unbounded sum of tag constants.

## 3. The complete equal-free-norm block

Let E(lambda,lambda')=1_(Nd_lambda=Nd_lambda'). It retains the ORIGINAL h!=h' subtraction:

 C_E=sum_(gamma,lambda,lambda') E(lambda,lambda')
      [S_(gamma,lambda) conjugate(S_(gamma,lambda'))
       -sum_h V_(gamma,lambda,h) conjugate(V_(gamma,lambda',h))].  (5)

The number of possible original tags is O(Z^ell), by the fixed compact slot supports and ordinary ideal counting; there are finitely many assignments. For fixed N, the number of good squarefree ideals d of norm N is at most d(N)<<_e N^e. Therefore every equality block has at most O_e(Z^ell N^e) labels. Cauchy in this FINITE block and (4) give

 sum_(gamma,N)|sum_(lambda:Nd_lambda=N)U_(gamma,lambda)|^2
                  << Z^ell Q_e
                  << Z^(-3/8+epsilon).                         (6)

The equality Nd=N is imposed on the ideal norm; different ideals of that norm remain present. In (6), N^e<= (Nc)^e, and e is chosen after the final epsilon.

The class term in (5) is positive. Give each norm N an independent random sign and apply (1) with alpha_lambda equal to that sign. Sign expectation yields exactly

 sum_N ||sum_(lambda:Nd_lambda=N)V_lambda||^2
                       <=M_0^2<<Z^(-23/48+epsilon).              (7)

The labelled l1 error (2), paired with the complete polynomial l1 bound, is arbitrarily power-small. Thus

                            |C_E|<<Z^(-3/8+epsilon).             (8)

This conclusion uses no replacement of the true mu(c). On r=1 and Er=1, the actual compensated signs satisfy mu(c)(-1)^(#D)=(-1)^K mu(d), since c=Ec d and (Ec,d)=1. The unresolved free-d signs are therefore still precisely the original Mobius signs.

## 4. Keeping an additional symmetric submask

One can also estimate ANY real symmetric mask 0<=B(lambda,lambda')<=E(lambda,lambda'), independent of p,p',h,m and the remaining column variables. In particular this permits excluding an already treated original-c coprime-quotient band. Positivity of (7) is not used for such a submask.

Order lambda by increasing original Nc. Each triangular column has degree at most O_e(Z^ell(Nc')^e). Apply the reviewed random-sign factorization with W_lambda=(Nc)^delta V_lambda. Its random column b_lambda' has variance

               <=C_delta Z^ell (Nc')^(-delta),                  (9)

on taking e<=delta. There are at most C Z^ell labels over each original ideal c, since this is an upper bound for all original tags. The ideal union bound therefore has one additional prefactor Z^ell. Integrating min(1,C_delta Z^ell exp(-c_delta u^2)) above the same fixed threshold gives

 E sup_lambda' |b_lambda'|
                        <<_delta Z^(ell/2)sqrt(log(2+Z)).        (10)

The first Z^(ell/2) is the square root of the variance scale in (9); the tag multiplicity costs only the displayed logarithm. All bounds are uniform in finite c cutoffs. Weighted Schur and the power-weighted sign trace from (1) justify the complete limits.

Accordingly the absolute class submask is

 << Z^(ell/2+epsilon)Y^(-1)=Z^(-19/48+epsilon).                    (11)

Its scalar part obeys the same degree/Cauchy bound (6), since |B|<=E. The complete actual cross contribution for B is thus still O(Z^(-3/8+epsilon)). This permits the equal-free-norm degeneracy to be removed AFTER the whole original-c quotient band, without assuming that a PSD bound survives an arbitrary intersection.

No estimate for Nd_lambda!=Nd_lambda' follows from this result. No near-fibre cutoff or incomplete m restriction is inserted before (2). If further physical pruning is combined with this labelled mask, its compatibility must be proved separately; only the stated mask depending on the original compensation labels and c is covered here.

## Published source locations

The precise inputs are [UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md, Part A Sections 3–7](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a99fbcda6b496eb36811ed80f3bfe5b18b7e2585/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md), [PHYSICAL_COPRIME_QUOTIENT_BAND.md, Part A](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a99fbcda6b496eb36811ed80f3bfe5b18b7e2585/reports/20261011_qrh_selection_bridge/PHYSICAL_COPRIME_QUOTIENT_BAND.md), and [PHYSICAL_COPRIME_BAND_SLOT_REFINEMENT.md, Parts I–II](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a99fbcda6b496eb36811ed80f3bfe5b18b7e2585/reports/20261011_qrh_selection_bridge/PHYSICAL_COPRIME_BAND_SLOT_REFINEMENT.md). The present Sections 1–4 supply the additional tag-phase admissibility, fixed-tag square prices, equality-block counts, and symmetric-submask argument. These are all fixed public mathematical dependencies.
