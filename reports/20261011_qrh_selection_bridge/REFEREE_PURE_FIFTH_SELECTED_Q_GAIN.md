# Referee note: pure-fifth Q-gain composition

## Scope

I reviewed only the composition of the public finite-order selected-slot Q gain in [GENERAL_SELECTED_Q_GAIN.md](GENERAL_SELECTED_Q_GAIN.md) with Part XIV (especially §1 of B and §§1–3 of A) of `QUADRATIC_DUAL_N1.md`, as used in [PURE_FIFTH_SELECTED_Q_GAIN.md](PURE_FIFTH_SELECTED_Q_GAIN.md). I take Part XIV's sixth-family density input and its prior arithmetic / physical estimates as established. This note does not re-review those theorems or the formal provenance of Q.

## Composition check

The frozen-column application is valid for the pure-fifth character. For each frozen physical row, the moving column character is the actual χ_w, with w squarefree, good, and nonunit. A prime dividing w is a genuine zero of χ_w, and any fixed η or ray factor is supported on the fixed bad set, so it cannot cancel ramification at a good prime dividing w. Thus the mixed prime character in each residual c_2 slot is nonprincipal, as required by the public lemma.

Part XIV B, §1 fixes the physical divisors, ordinary-mask branch, finite ray/unit choices, and dyadic blocks before estimating c_2. Its original/core priority assignments put each selected slot either in a frozen scalar/row factor or in the common Möbius c_2 column. The remaining c_2 slots therefore have the true μ(c_2)η(c_2)χ_w(c_2)/q_{c_2} coefficient. Fixed-prime restrictions become frozen common holes or fixed masks. The retained compact product cutoffs and the real-part-zero log-Fourier separation give the required Cartesian product of one-slot weights, with each mode's norm phase factoring as a common scalar times ∏_i q_{p_i}^{iu}. I found no moving good-prime character hidden in a fixed ray factor and no use of the lemma for arbitrary bounded z_D. These are the hypotheses the public result expressly needs.

The exact Euler multiplier also matches: after extracting a forced selected product D_c, its outside factor is μ(D_c)η(D_c)χ_w(D_c)/q_{D_c}, while the residual c_2 column has the same moving character and its actual common exclusions. The public multiplier's local factor y/(1-y) preserves the zeros at primes dividing w. Common holes that differ by slot are allowed by the public result and contribute ∏_i q_{M_i}^ε.

Consequently, on each nonempty frozen column, the public pointwise estimate inserts P_c^{-1/8+ε} into Part XIV B's selected-column cost. For a zero-bin parameter a in [1/8,1/2], this changes

\[
 (Y'P_cq_r^6/C_l)^a W^{F(a)}
 \quad\hbox{to}\quad
 (Y'q_r^6/C_l)^a P_c^{a-1/8+\epsilon}W^{F(a)}.
\]
Since a-1/8 is nonnegative and P_c is at most a constant times P, this is bounded by P^{-1/8+\epsilon} times the old uniform bin envelope with P_c^a replaced by P^a. If no selected slot reaches c_2, P_c=1 and there is no individual column saving; nevertheless 1\le P^{a-1/8+\epsilon} for P\ge1, so the same global envelope holds. This empty-column case is correctly handled as an upper-envelope comparison, not as a claimed Q saving on that summand.

## Losses and full physical transfer

The added conductor loss q_w^\epsilon, frozen-hole losses q_{M_i}^\epsilon, and the polynomial in contour/Fourier heights must be carried into the ambient bound before summation. Part XIV B, §1 already retains the complete Gaussian/Schwartz envelope and actual finite column cutoffs; its strict a' summability, actual r cutoff, finite e ranges, and rapid mode decay absorb these small powers and mode polynomials with an arbitrarily small final exponent loss. This is the required use of the full tails, including subunit K_l; a hard cutoff is not substituted. The gain is uniform in T and in the frozen physical labels, so it does not alter the exact h_0|w boundary bookkeeping or introduce a density factor 1/q_{h_0} into the zero count.

The same insertion applies before the physical sums for every n=r^2, every original and core priority assignment, and every ordinary-mask branch, because it changes only the frozen c_2 multiplier. For each exact first-flat operator, Part XIV B substitutes T=Z/q_\delta^6 while retaining X', Y', and the slot windows. The new factor depends on P_c and the moving w character, not on T or \delta. The existing flat exponent \beta(a)\ge-1/10 therefore remains, giving the summable q_\delta^{-7/5+\epsilon} weight. The redundant frequency lift preserves the pure-fifth type. I found no loss of an original/core contribution or first-flat term in this transfer.

## Exponent check and verdict

Writing d\in[0,1/6] for the compensation parameter, the old normalized exponent G_0(a)-ad becomes

\[
 G_{\rm new}(a,d)=G_0(a)-\frac1{48}+d(\tfrac18-a)
 \le G_0(a)-\frac1{48},
\]

because a\ge1/8. With the Part XIV maximum max G_0=-63/320, the normalized exponent is at most -209/960. The raw convention is \(G_{\rm norm}=G_{\rm raw}-5/12+d/2\), so the correct fixed-d upper bound is \(G_{\rm raw}\le191/960-d/2\); its global maximum over d is 191/960 at d=0. At d>0 this is a uniform bound, not a claim that the bin a=1/2 maximizes the raw exponent for that fixed d. This matches the corrected relation and exact fraction certificate in [PURE_FIFTH_SELECTED_Q_GAIN.md](PURE_FIFTH_SELECTED_Q_GAIN.md) and [check_purefifth_selected_q.py](check_purefifth_selected_q.py).

**Verdict: the composition is sound within the stated conditional scope.** In particular, the improvement is a complete pure-fifth physical bound conditional on the same Q input, not a claim for other frequency types or for RH. The analytic Q gain and Part XIV's imported density and physical estimates remain dependencies; this review checks their interface and transfer only.
