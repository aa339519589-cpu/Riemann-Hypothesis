# Retained slot powers and random-sign factorization enlarge the physical quotient band

This short refinement keeps the negative prime-slot powers in the already proved [all-s fixed-c estimate and quotient-band algebra](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/ca7be214e825dab063ea332a27e833b601d109e5/reports/20261011_qrh_selection_bridge/PHYSICAL_COPRIME_QUOTIENT_BAND.md). For the SAME half-damped, positive-auxiliary, original/core nonflat observation with its old Gaussian-T restorer, the divisor-weighted literal-unit energy improves to

    sum_(gamma,c)d(c)^K |U_(gamma,c)|^2
        <=C_(K,epsilon) Z^(-13/24+epsilon).

Part I retains the true negative slot powers. Part II uses an elementary random-sign factorization of the actual triangular class mask to improve its price from R to sqrt(R). Together they give

    |C_R|<=C_epsilon [R Z^(-13/24+epsilon)
                        +sqrt(R) Z^(-23/48+epsilon)]+O_N(Z^(-N)).

Thus for every fixed 0<eta<1/24,

    |C_R|<=C_epsilon Z^(-3/8-eta+epsilon),
    R=Z^(1/6-eta),
    N(cc'/(c,c')^2)<=R^2=Z^(1/3-2eta).

C_R is exactly the actual mean-before-square off-class expression defined in the linked report, with independent auxiliary primes in its two copies and unchanged Mobius coefficients. This strictly enlarges its controlled quotient band. The larger-quotient complement remains unestimated; there is no whole-cross or zero-exclusion conclusion. The previously published weaker bound remains valid and needs no correction.

The complete new proof is below. Part I uses the explicit fixed slot support and normalizer in the [original compensated definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L6868-L6908) and [principal scalar](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L15563-L15588). In the formulas, W_i(Np) abbreviates the original scaled slot weight W_i(Np/P_i); no new amplitude factor is introduced. All earlier all-s, marked, labelled-high-error and old-restorer proofs are retained by their exact reference to the linked mathematical report. Part II proves the additional random-sign factorization in full and explicitly verifies its weighted bounded-row input at the physical Gaussian. The [independent review](REFEREE_PHYSICAL_COPRIME_BAND_SLOT_REFINEMENT.md) includes source-level checks of the slot partition and the order of summation. No first-flat or further infinite-prime normalization is included.

## Part I. Retained physical slot powers

### 1. Fixed slot data and the previously proved exact prices

Use the half-damped, positive-auxiliary, old-T-restored observation of the fixed-c theorem and the growing coprime-quotient-band theorem. All slots and their normalizer remain frozen at the original ambient Z. Write the finitely many original prime-slot norm scales as P_i. Each W_i(Np) is a bounded fixed smooth profile on a compact annulus Np comparable to P_i. In the original geometry

                         product_i P_i = Z^ell, ell=1/6,

up to fixed compact ratios. The original A_T(Z)^(-1) costs only logarithms. This can be checked directly in the pinned original paper.tex at commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb: its fixed geometry and compensated-probe definition give positive fixed ell_i, P_i=Z^ell_i and D=p_J, E=p_(J complement), with exactly the product of the original W_i weights and no extra slot power. Its principal normalizer is A_T(Z)=(-1)^K Z^(-ell/6) product_i S_i(Z), where S_i(Z) is asymptotic to a positive constant times P_i^(1/6)/log(P_i). Thus A_T has size comparable to (log Z)^(-K). The exact source passages are the [fixed slots and compensated definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L6868-L6908) and the [principal scalar](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L15563-L15588).

In each finite-compensation term the original slot set is partitioned into the rescaled tuple D and the marked tuple E; there is no unused slot. On the literal unit support n=r^2, the true marked tuple is further partitioned by its original priority into Ec|c and Er|r, with (Er,c)=1. Core restrictions only reduce that support. Thus every slot belongs to exactly one of D, Ec, Er.

The independently reviewed weighted c-square proof gives, before summing the slots, the exact prices

  (i)   Ec^(-5/3) in the squared c-marked sum;
  (ii)  Er^(-4/3) in the r-marked norm/l1 sum;
  (iii) D^(-11/6) in the rescaled norm/l1 sum.

These include the complete all-s unit reduction, original r Gaussian, original c label, all holes and ray sectors. In particular (i) arises from Cauchy only in actual Ec divisors of c, with its divisor multiplicity paid by the already proved divisor-weighted c estimate. It is not replaced by an l1 sum over marked-c primes.

### 2. The slot-scale factors that can be retained

Elementary ideal counting, with prime restrictions retained or dropped in a positive majorant, gives uniformly at every fixed slot scale P_i

  sum_p |W_i(Np)|^2 (Np)^(-5/3) << P_i^(-2/3),
  sum_p |W_i(Np)|   (Np)^(-4/3) << P_i^(-1/3),
  sum_p |W_i(Np)|   (Np)^(-11/6)<< P_i^(-5/6).          (1)

No prime number theorem is needed for these upper bounds. Empty or bounded initial annuli are covered by a fixed constant. All Ec pools are first summed inside the positive c-SQUARE estimate, after the actual divisor Cauchy step; only then is its single square root taken. The first line of (1) therefore yields the product of P_i^(-1/3) over the Ec slots, without an intervening triangular l1 loss. Each slot costs at most P_i^(-1/3) in the unit c-norm, regardless of its assignment to Ec, Er or D. The rescaled-D assignment is strictly cheaper. Prime distinctness and cross-slot shared masks can only reduce these positive majorants. There are only finitely many original assignments.

Consequently the same true compensated unit vector satisfies, for every fixed divisor power K and epsilon>0,

  ||U(T)||_(ell2(gamma,c;d(c)^K))
       <<_(K,epsilon) Z^epsilon (X/T)^(1/3)
                                  product_i P_i^(-1/3)
       <<_(K,epsilon) Z^(-ell/3+epsilon)(X/T)^(1/3).     (2)

All preliminary divisor-power losses are chosen after the final epsilon and absorbed in Z^epsilon. The same old restoring-operator bound on T^(-1/3) applies; the slot scales do not move when T is dilated. The original normalization c_(S_p), fixed base limit U, and the raw weighted l1(c) prime-projection error are exactly as in the already reviewed theorem. Equation (2) therefore applies to that same actual mean-before-square observation.

At X=Z^(17/48), T=Z and ell=1/6, its squared version is

                   sum_(gamma,c)d(c)^K |U_(gamma,c)|^2
                            << Z^(-13/24+epsilon).      (3)

Indeed 2*(17/48-1)/3-2*(1/6)/3=-13/24. The one-sided fixed-c cross upper bound inherits (3). This improvement uses slot support, not cancellation of a replaced c coefficient; the true mu(c) remains unchanged.

### 3. Consequence for the already reviewed quotient-band algebra

Let A_R(c,c') indicate N(cc'/(c,c')^2)<=R^2, R>=1. The reviewed weighted Schur estimate and the exact physical h!=h' subtraction give

 |C_R| << R [sum_(gamma,c)d(c)|U_(gamma,c)|^2
                    +sum_(gamma,c,h)d(c)|V_(gamma,c,h)|^2]
                                                   +O_N(Z^(-N)).

The second term is still only bounded by the separately reviewed divisor-weighted positive-class estimate Z^(-23/48+epsilon). No slot improvement for that term is asserted here: its marked-g diagonal has the different local price sum_p W_i(Np)^2/Np, which does not save a power of P_i.

Combining that actual class bound with (3) therefore yields

                   |C_R| << R Z^(-23/48+epsilon)
                                                   +O_N(Z^(-N)). (4)

For every fixed 0<eta<5/48, one may now take

 R=Z^(5/48-eta),
 N(cc'/(c,c')^2)<=Z^(5/24-2eta),

and conclude |C_R|<<Z^(-3/8-eta+epsilon). The physical classes, independent auxiliary primes, original roots and original c coefficients are the same as in the earlier band theorem. This is a larger controlled band, not a bound on its complement or a zero-exclusion result.

### Sources and scope

The exact all-s unit and slot prices are the reviewed fixed-c theorem, proved in [PHYSICAL_COPRIME_QUOTIENT_BAND.md, Part A](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/ca7be214e825dab063ea332a27e833b601d109e5/reports/20261011_qrh_selection_bridge/PHYSICAL_COPRIME_QUOTIENT_BAND.md). Its Part B supplies the unchanged weighted Schur/class algebra. The exact finite compensation D=p_J, E=p_(J complement), total slot scale ell=1/6 and frozen normalizer are also recorded in PHYSICAL_KUMMER_BLOCKS.md and UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md at the fixed source commits used in those reviews. This note retains the old-restored, original/core nonflat scope. Any additional all-prime or rational normalization requires its own already-reviewed operator transfer.

## Part II. Random-sign factorization of the actual class mask

### 1. The actual bounded-phase input

Keep the half-damped positive-auxiliary observation, the exponential single-prime probability law, original/core nonflat marks, all compensation, ambient normalizers and the old T-restorer. Write V_c=(V_(gamma,c,h))_(gamma,h) for its already prime-averaged class vector, with the original physical c retained. All inner products below use these actual vectors.

The published uniform-large-B pair proof permits an arbitrary scalar alpha(c) of modulus at most one in the ORIGINAL c row. Its two-copy product is independent of h0, so the auxiliary cancellation and moving character (6) in that proof are unchanged. All principal and remainder majorants take its modulus only after this exact cancellation. Higher-s reductions, core restrictions, finite compensation and T-restoration preserve c. Hence, by Jensen for the positive auxiliary mean, the same proof gives

  ||sum_c alpha(c)V_c||_H << Z^epsilon Y^(-1/2)+exp(-cZ)Z^C,
                              |alpha(c)|<=1.             (1)

This is the proof-level phase-uniform input already checked in the published quotient-band theorem. It is stronger than its Rademacher trace consequence, and is being used only for the positive CLASS vector, not for the whole signed observation.

For any fixed small delta>0 it also gives the weighted version

  M_delta := sup_(|alpha(c)|<=1)
                 ||sum_c alpha(c)(Nc)^delta V_c||_H
       << Z^(7delta/6+epsilon)Y^(-1/2)+exp(-cZ)Z^(C_delta). (2)

Indeed in each true compensation summand T_eff=T NE<=C Z^(7/6), and exactly

 (Nc)^delta V_G(Nc(Nn)^3/T_eff)
   =T_eff^delta (Nn)^(-3delta)
       V_delta(Nc(Nn)^3/T_eff),
 V_delta(v)=v^delta V_G(v).

This is another fixed log-Schwartz profile. The n weight gains extra decay, so its original positive Minkowski summation is no worse. One may bound T_eff^delta by C Z^(7delta/6) before the unchanged slot proof. Higher-s branches only change X,Y and temporary auxiliary data, leaving this Gaussian identity intact. The old restorer only lowers T; its norm on this slightly positive T envelope is still bounded. Thus (2) has no B^epsilon or log B cost, even for B comparable to exp(Z).

All statements may first be made with finite original c sums. The original Gaussian and the same weighted positive proof supply their limits. In particular the bounds are uniform in those cutoffs.

### 2. The actual triangular column degree

Let

 A_R(c,c')=1_(N(cc'/(c,c')^2)<=R^2), R>=1.

Choose once a total order refining increasing norm, and let B_R(c,c')=A_R(c,c')1_(c precedes or equals c'). For fixed c', write c=g a,c'=g a', with a'|c'. Every retained partner satisfies Na<=Na' and Na Na'<=R^2. Thus

                    Na<=min(Na',R^2/Na')<=R.

For each a'|c' there are O(R) possible primary a. Original coprimality and squarefree restrictions may only reduce this count. Consequently

            sum_c B_R(c,c') <= C R d(c').                (3)

This is a genuine UNWEIGHTED column-degree bound for the triangular mask. It does not assert an unweighted O(R) row degree for the symmetric full mask.

### 3. Random signs give a square-root mask cost

Set W_c=(Nc)^delta V_c. On any finite cutoff choose independent real Rademacher signs e_c. Define

 b_(c')=(Nc')^(-delta)
                sum_c B_R(c,c')(Nc)^(-delta)e_c.          (4)

Then E[e_c b_(c')]=B_R(c,c')(Nc Nc')^(-delta). Hence the exact triangular class sum is

 sum_(c,c') B_R(c,c')<V_c,V_c'>
       =E <sum_c e_c W_c, sum_c' b_(c') W_c'>.           (5)

The first vector on the right has norm at most M_delta and the second at most M_delta sup_c'|b_(c')|. This uses precisely the bounded-row input (2); no signs in the true final coefficient have been substituted.

By (3), the variance of b_(c') is bounded by

 (Nc')^(-2delta) sum_c B_R(c,c')(Nc)^(-2delta)
     <= C R d(c')(Nc')^(-2delta)
     <= C_delta R (Nc')^(-delta).                       (6)

The elementary exponential-moment inequality for a sum of independent signs therefore implies

 Pr(|b_(c')|>u sqrt(R))
          <=2 exp[-c_delta u^2 (Nc')^delta].             (7)

Summing (7) over all primary ideals is legitimate: ideal counting is O(H), and the sum of exp[-c_delta u^2(Nc')^delta] is finite for each u>0. For large u it is integrably small in u. For example (Nc')^delta>=1+delta log(Nc'), and once c_delta delta u^2>=2, the union bound is at most a fixed multiple of exp(-c_delta u^2) times zeta_K(2). For smaller u the probability is bounded by one. Thus

                    E sup_c'|b_(c')|<=C_delta sqrt(R),   (8)

uniformly in the finite cutoff. Equations (5)--(8) give a dimension-free bound C_delta sqrt(R)M_delta^2 for the triangular sum, using only independent signs and ideal counting.

The full symmetric mask is the triangular mask plus its transpose minus the diagonal. Its diagonal trace is at most M_delta^2: apply independent signs to W_c and then use Nc>=1. Consequently

 |sum_(c,c') A_R(c,c')<V_c,V_c'>|
                          <=C_delta sqrt(R)M_delta^2.   (9)

The previously reviewed weighted Schur bound and the weighted c/class square estimate provide absolute summability of this masked sum for every fixed R. They justify passing from finite cutoffs to (9). Equivalently one may first pass in finite physical and class sums, then use their unchanged Gaussian majorants. The expectation estimate itself is uniform in all those cutoffs.

Choose delta and the preliminary epsilon sufficiently small after any prescribed final epsilon. Since R is at most a fixed power of Z, (2) and (9) prove

 |sum_(gamma,h,c,c') A_R(c,c')
          V_(gamma,c,h) conjugate(V_(gamma,c',h))|
           <<_epsilon R^(1/2)Z^(-23/48+epsilon)
                                                   +O_N(Z^(-N)). (10)

No Grothendieck inequality, unproved spectral estimate, or long-conductor prime average is needed for this step.

### 4. The larger controlled physical band

The exact off-class identity remains

 C_R=sum_(gamma,c,c') A_R(c,c')
       [S_(gamma,c) conjugate(S_(gamma,c'))
         -sum_h V_(gamma,c,h) conjugate(V_(gamma,c',h))],
 S_(gamma,c)=sum_h V_(gamma,c,h).

The reviewed raw first-Poisson argument replaces S by the fixed base unit U with a weighted l1(c) error O_N(Z^(-N)). Its application is still to complete m columns, before the pair mask is inserted. The reviewed weighted Schur inequality and the slot-power refinement in Part I bound its scalar part by R Z^(-13/24+epsilon). Combine this with (10), retaining the class subtraction exactly, to obtain

 |C_R| <<_epsilon R Z^(-13/24+epsilon)
                    +R^(1/2) Z^(-23/48+epsilon)
                                                   +O_N(Z^(-N)). (11)

For every fixed 0<eta<1/24, take R=Z^(1/6-eta). The first term is Z^(-3/8-eta+epsilon); the second is Z^(-19/48-eta/2+epsilon), which is smaller on this eta range. Therefore

 N(cc'/(c,c')^2)<=Z^(1/3-2eta)
       implies |C_R|<<Z^(-3/8-eta+epsilon).              (12)

Here 'implies' refers to the complete contribution restricted to that pair band. The original h!=h' condition, two independently averaged auxiliary primes, full roots, all s/n layers and all original c coefficients are retained. Equation (12) removes a larger genuine degeneracy band; its complement still contains the original long Mobius correlation and is not estimated.

The scope is the same old-restored, half-damped, original/core nonflat observation as in the two reviewed inputs. Additional normalization operators are not included by implication.

The bounded-row input in Part II is the [uniform-large-modulus positive pair proof, Part A](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/ca7be214e825dab063ea332a27e833b601d109e5/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md), with the original-c phase and divisor extension proved in [the quotient-band report, Part B](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/ca7be214e825dab063ea332a27e833b601d109e5/reports/20261011_qrh_selection_bridge/PHYSICAL_COPRIME_QUOTIENT_BAND.md). Part I supplies its scalar unit estimate. No additional unprinted pruning or normalization lemma is needed.
