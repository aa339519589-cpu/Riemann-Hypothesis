# Independent review: retained slot powers and randomized class mask

The complete [short refinement](PHYSICAL_COPRIME_BAND_SLOT_REFINEMENT.md) has been independently checked against the original compensated definition and the already proved all-s fixed-c theorem. It retains the same original/core nonflat, half-damped, positive-auxiliary, old-restored observation. Its larger quotient band is a restricted part of the physical cross sum; the complement remains open.

## Part I. Review of the retained slot powers

### Original source quantities were checked

The proof uses the exact original [compensated slot definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L6868-L6908) and [normalizer](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L15563-L15588). These confirm positive fixed slot lengths, P_i=Z^ell_i, disjoint compact annular prime windows, bounded fixed W_i, and the exact finite compensated definition. Every slot is either in the rescaled subset D=p_J or in the marked complement E=p_(J complement). There is no unassigned slot or additional slot power in the physical weights. At eta=1 the displayed marked character factor is one.

The same actual source confirms S_i is asymptotic to a positive fixed constant times P_i^(1/6)/log P_i, and A_T=(-1)^K Z^(-ell/6) product S_i. Hence its reciprocal costs logarithms, with all data fixed as stipulated. No moving-conductor normalizer is inserted. The fixed geometry ell=1/6 is the same geometry used in the established fixed-c theorem.

## Prices and order of summation

On the literal unit support n=r^2, each marked prime is assigned first to Ec when it divides original c; otherwise it belongs to Er and divides r. This is an exhaustive disjoint assignment. Any core mask further restricts the terms and cannot introduce an unused slot. The previously proved exact prices are Ec^(-5/3) inside the c square sum, Er^(-4/3) in the norm/l1 sum, and D^(-11/6) in the rescaled norm/l1 sum.

Counting ideals in each fixed annulus gives respectively P_i^(-2/3), P_i^(-1/3), and P_i^(-5/6) for the three displayed sums. The Ec pools must be summed inside the positive square estimate, after the actual-divisor Cauchy step, before its square root is taken. With that correct order their norm factor is P_i^(-1/3). This order is explicitly maintained in the manuscript. The Er factor equals the same P_i^(-1/3), and the D factor is stronger. Distinctness and shared masks are removed only in these positive majorants. There are finitely many original assignments.

It follows that the total unit-vector norm gains product_i P_i^(-1/3)=Z^(-ell/3). All fixed divisor multiplicities and preliminary small exponents are selected after the desired final epsilon. Ambient slots do not change under T-only restoring dilations, so the gain is retained by that already proved operator bound. Neither the moving auxiliary scalar nor the raw labelled high error acquires a new power.

## Exponents and exact scope

The improved divisor-weighted unit square is

  Z^(-2ell/3+epsilon)(X/T)^(2/3)=Z^(-13/24+epsilon)

at the original geometry. The fixed-c off-class estimate inherits this as a one-sided upper bound. The true Möbius coefficient is unchanged.

The separately proved divisor-weighted same-class square remains Z^(-23/48+epsilon). No improvement is claimed for it; its marked-g diagonal has a different local prime price without the required negative scale power. The exact scalar-minus-class identity and weighted Schur inequality therefore give the absolute band bound R Z^(-23/48+epsilon). For R=Z^(5/48-eta), 0<eta<5/48, the exponent is -3/8-eta+epsilon and the quotient-product range is Z^(5/24-2eta).

This is a strict enlargement of the controlled quotient band. It does not estimate its larger-quotient complement, change the observation, prove a new whole-low estimate, or exclude a zero. The previously published weaker theorem remains correct and does not require a correction.

## Part II. Review of the randomized class mask

### Actual bounded-phase input and weighted domain

The input is the already source-checked uniform positive class estimate, with an arbitrary bounded scalar in each original c row. Such a scalar is independent of the common h0 variable, so it does not change the exact pair character or the auxiliary cancellation. Its modulus is taken in the principal and nonprincipal majorants only after those identities. The higher-s reductions, compensation and old T-restorer preserve original c. Jensen for the auxiliary probability mean therefore gives the displayed ell-infinity-to-class-Hilbert bound for the actual averaged V_c.

The weighted version is correctly proved at the physical Gaussian, rather than inferred by differentiating a final estimate. Multiplication by (Nc)^delta gives exactly T_eff^delta(Nn)^(-3delta) V_delta(Nc(Nn)^3/T_eff), with V_delta another fixed log-Schwartz profile. T_eff<=C Z^(7/6), the n weight gains decay, and all original slot estimates remain the same. The old restorer lowers T. Thus M_delta has only the stated Z^(7delta/6) cost, with no auxiliary B power or log B loss. Finite original c sums have uniform bounds and the existing weighted Gaussian estimates justify their limits.

### Correct triangular counting

The unweighted degree assertion is made only for the mask oriented by a total order refining increasing norm. For fixed c'=g a', every c=g a in that triangular column has Na<=Na' and Na Na'<=R^2, hence Na<=min(Na',R^2/Na')<=R. Each divisor a' of c' therefore permits O(R) ideals a, yielding CR d(c'). This proof would be false for the full symmetric mask; the manuscript explicitly preserves the orientation and later restores its transpose.

### Exact random-sign factorization

With W_c=(Nc)^delta V_c and b_c'=(Nc')^-delta sum_c B_R(c,c')(Nc)^-delta e_c, independence gives E[e_c b_c']=B_R(c,c')(Nc Nc')^-delta. Hence the displayed Hilbert inner-product factorization is exact, also under the convention conjugate-linear in the first argument, since e_c and b_c' are real. The first vector is bounded by M_delta and the second by M_delta sup|b|, precisely by the bounded-row input. The final physical coefficients are unchanged; the signs are only an auxiliary proof device.

The variance is at most C R d(c')(Nc')^-2delta<=C_delta R(Nc')^-delta. The elementary sign exponential-moment bound gives the stated sub-Gaussian tail. Its union over the entire infinite ideal set is legitimate: x^delta>=1+delta log x, and above a fixed u threshold the bound is exp(-c_delta u^2) times the convergent ideal zeta sum at 2. Below that threshold use probability at most one. Thus E sup|b|<=C_delta sqrt(R), uniformly in every finite cutoff. No implicit physical c cutoff, dimension factor, or large-conductor estimate appears.

The symmetric mask equals the triangular mask plus its transpose minus the diagonal. Rademacher averaging bounds the diagonal trace by M_delta^2. The already verified divisor-weighted Schur majorant gives absolute summability of the actual masked class sum at every fixed R, so the finite-cutoff result passes to the complete c, class and physical sums. Choosing delta after the final epsilon absorbs its fixed Z power and proves (10).

### Scalar-plus-class bound and exponents

The scalar completed-column term still uses the separately proved unit-vector estimate and ordinary weighted Schur, giving R Z^(-13/24+epsilon). The exact h!=h' subtraction is retained; its class term now costs sqrt(R) Z^(-23/48+epsilon). The labelled raw high error is used before imposing the pair mask and remains arbitrarily power-small.

At R=Z^(1/6-eta), the two exponents are -3/8-eta and -19/48-eta/2. The second is strictly smaller than the first precisely on the stated range 0<eta<1/24. The quotient-product range is Z^(1/3-2eta). All original sectors, masks, roots, two independent prime averages and Möbius coefficients are retained. Additional normalization operators and the larger-quotient complement are outside this result.
