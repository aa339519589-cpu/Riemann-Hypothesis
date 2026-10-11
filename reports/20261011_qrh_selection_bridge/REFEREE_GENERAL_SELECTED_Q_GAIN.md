# Independent audit: general selected-prime Q pointwise lemma

## Verdict

The selected-prime pointwise gain extends from the accepted quadratic lemma to any finite-order Hecke character whose conductor has a genuinely ramified good prime outside the fixed bad set. The order-two identity used in the earlier rational-multiplier moment lemma is not needed here: isolate the first geometric term, bound the remaining geometric tail absolutely, and apply Q to the prime sum for the first term.

The actual mixed (3/5) slot interface in Parts XVII–XVIII meets the needed factorization after row divisors, slot assignments, finite ray modes, and norm-Mellin variables are frozen. The precise conclusion is a pointwise bound for each such factorized summand. It does not apply to arbitrary bounded (z_D), nor before the row-coupled coefficient has been frozen. The estimate has conductor and deleted-prime losses which must be charged in the ambient budget.

At the zero-free endpoint (a=1/8), its factor (P_c^{-1/8+\rho}) cancels the (P_c^{a}) from the selected-column scalar ((L/P_c)^{-a}), leaving only (P_c^{\rho}). Since the shift parameter (\rho>0) can be chosen arbitrarily small, this is an epsilon loss for the fixed finite collection of actual slots. This offers a way to improve the endpoint slot budget. For bins with (a>1/8), the pointwise estimate alone leaves (P_c^{a-1/8+\rho}); it does not replace the existing all-bin slot-moment argument by itself.

## General factorized-slot statement

Let (S) be the fixed bad prime set. Let χ be a finite-order Hecke character with at least one ramified good prime outside (S). In the applications χ is the genuine moving factor ψ_vχ_w, with the good supports disjoint and at least one nonunit; hence it has such a ramified prime. For each slot (i=1,\dots,J), fix (P_i\ge2), a smooth (W_i\in C_c^\infty((0,\infty))) supported in a fixed positive annulus, a fixed (S)-ray character ν_i from a finite list, a real Mellin frequency (u_i), a fixed finite-order twist η, and a common exclusion (M_i). Slots are disjoint sets of good prime ideals. After resolving any finite ray condition and freezing the row data, suppose the exact coefficient is the Cartesian product
\[
z_D=\prod_{i=1}^J W_i(q_{\mathfrak p_i}/P_i)\,ν_i(\mathfrak p_i)q_{\mathfrak p_i}^{iu_i}μ(\mathfrak p_i)\overline{η(\mathfrak p_i)},\qquad D=\prod_i\mathfrak p_i,
\]
with ((\mathfrak p_i,M_i)=1). Define (P_c=\prod_iP_i) and
\[
E_\chi(s)=P_c^{s-1}\sum_D z_D\prod_{\mathfrak p\mid D}
\frac{η(\mathfrak p)χ(\mathfrak p)q_{\mathfrak p}^{-s}}
{1-η(\mathfrak p)χ(\mathfrak p)q_{\mathfrak p}^{-s}},
\qquad \tfrac12+\delta_0\le\Re s=\sigma\le1.
\]
For every ρ>0, ε>0, this summand satisfies
\[
|E_\chi(s)|\ll_{\rho,\epsilon}
\left(q_\chi\prod_i q_{M_i}\right)^\epsilon
\prod_i(1+|\Im s|+|u_i|)^{B_i}
P_c^{-1/8+\rho}.
\tag{1}
\]
The constants depend on the fixed field, δ_0, the finite ray list, (J), and the indicated smooth seminorms. In particular, for a common Mellin frequency (u_i=u), the height factor is a fixed polynomial in (1+|\Im s|+|u|).

The fixed-ray twist ν_i cannot remove the nonprincipal character: it is unramified outside (S), while χ is ramified at a good prime outside (S). Thus θ_i=ν_iχ is nonprincipal. This criterion is essential; a principal/unit-core character cannot be put through the nonprincipal logarithmic argument.

## Prime term, Q shift, and the two remainders

On every slot prime, η is a unit because the slot is supported on good primes outside (S), and χ has χ(𝔭)=0 at its conductor primes and modulus one elsewhere. Uniformly for σ\ge1/2+\delta_0,
\[
\overline{η(\mathfrak p)}
\frac{η(\mathfrak p)\chi(\mathfrak p)q_{\mathfrak p}^{-s}}
{1-\eta(\mathfrak p)\chi(\mathfrak p)q_{\mathfrak p}^{-s}}
=\chi(\mathfrak p)q_{\mathfrak p}^{-s}
+O_{\delta_0}(q_{\mathfrak p}^{-2\sigma}).
\tag{2}
\]
This follows from the exact identity (z/(1-z)=z+z^2/(1-z)) and |1-ηχq^{-s}|\ge1-2^{-\sigma}>0. It remains true at χ(𝔭)=0, where both terms vanish. The first term, including μ(𝔭)=-1 and ν_i, is the prime sum for the genuine character θ_i=ν_iχ. No moving good character has been placed in ν_i.

For a smooth annular (W), consider
\[
\sum_{\mathfrak p}W(q_{\mathfrak p}/P)\theta_i(\mathfrak p)q_{\mathfrak p}^{-s+iu_i}.
\]
Mellin inversion starts on ℜ(w)=1/2, where ℜ(s-iu_i+w)=σ+1/2>1, and uses
\[
\mathcal P(z,\theta_i)=\sum_{\mathfrak p}\theta_i(\mathfrak p)q_{\mathfrak p}^{-z}
=\log L_K(z,\theta_i)-\sum_{\mathfrak p}\sum_{k\ge2}
\frac{\theta_i(\mathfrak p)^k}{kq_{\mathfrak p}^{kz}}.
\]
The prime-power series is analytic for ℜ(z)>1/2. By Q, (L_K(z,\theta_i)) has an analytic logarithm in ℜ(z)>7/8. Standard fixed-field Hecke growth and Borel–Carathéodory on fixed-radius discs centered at (2+i\Im z) give, for fixed ρ>0,
\[
|\log L_K(z,\theta_i)|\ll_\rho
\log(q_{\theta_i}(3+|\Im z|)),
\qquad \Re z\ge7/8+\rho,
\]
on the bounded strip used in the shift. The conductor obeys (q_{\theta_i}\ll_S q_\chi). Shift the logarithm integral to ℜ(w)=(7/8+\rho-\sigma), choosing (0<\rho<\min(\delta_0,1/8)). There is no pole because θ_i is nonprincipal, and no zero is crossed. Rapid Mellin decay kills the horizontal sides and gives, after multiplication by |(P^{s-1})|,
\[
P^{\sigma-1}\left|\sum_{\mathfrak p}W(q_{\mathfrak p}/P)\theta_i(\mathfrak p)q_{\mathfrak p}^{-s+iu_i}\right|
\ll_{\rho,\epsilon,W}q_\chi^\epsilon
(1+|\Im s|+|u_i|)^B P^{-1/8+\rho}.
\tag{3}
\]
The polynomial height dependence is integrable against the source's rapid Mellin/Gaussian mode decay; the bound is not intended as an unweighted supremum over an unintegrated Mellin parameter.

The two remaining errors have different origins and should be kept distinct.

- The geometric remainder in (2) is bounded absolutely using (O(P)) ideals in the annulus:
\[
P^{\sigma-1}\sum_{q_{\mathfrak p}\asymp P}O(q_{\mathfrak p}^{-2\sigma})
\ll P^{-\sigma}.
\]
- In (3), the (k\ge2) terms from the logarithmic Euler expansion, on the original smooth window (W(q_{\mathfrak p}^k/P)), are
\[
\ll P^{-\sigma}\sum_{2\le k\ll\log P}P^{1/k}/k
\ll P^{1/2-\sigma}.
\]
After normalization (P^{\sigma-1}), this is (O(P^{-1/2})). It is the logarithmic-Euler prime-power tail, not the geometric remainder.

For the common holes ((\mathfrak p,M_i)=1), restore the omitted primes and bound them absolutely. Since a prime divisor in the annulus has norm ≫(P_i), there are at most (O(\log q_{M_i}/\log P_i)) such primes, so the normalized deletion costs
\[
P_i^{-1}\frac{\log q_{M_i}}{\log P_i}
\ll_\epsilon q_{M_i}^\epsilon P_i^{-1}.
\]
For bounded (P_i), adjust the constant. Fixed bad primes are either excluded in the same way or absorbed into the finite ray partition.

Equations (2)–(3), the two tails, and the hole cost give the one-slot estimate. Multiplying over the fixed (J) slots is legitimate because, after the stated freezing, both the coefficient and the local Euler factors are primewise products and (P_c^{s-1}=\prod_iP_i^{s-1}). Spending ε/J per slot yields (1). A finite Fourier expansion of a ray indicator preserves this structure: if (D=\prod_i\mathfrak p_i), every finite ray character on (D) factors as ∏_i ξ(𝔭_i), and there are only finitely many terms.

## Match to the actual Part XVII/XVIII slot interface

The actual mixed characters are ψ_vχ_w, with good coprime supports and conductor norm comparable to (VW). Part XVII A explicitly freezes (w) before the quadratic (v)-average and retains χ_w as a common coefficient; its Q/inverse-(L) ambient size includes (VW) and all deleted Euler factors (Part XVII A, §1). The pointwise argument here is applied rowwise to the genuine product character, not to a fixed-(w) character with its moving χ_w hidden in a constant.

The actual coefficient structure is also explicit in Part XVIII B, §1: after fixing (r,h_0,a',e), finite rays, and dyadic norm blocks, (c_2) has the true μ(c_2)η(c_2)/q_{c_2}) coefficient and common masks; its moving character is ψ_vχ_w. Each selected prime is assigned to a fixed scalar, a joint row coefficient, or the common (c_2)-column multiplier. Only the last category is included in (E_{v,w}); after assignment, its remaining coefficient is independent of (v,w). The complete mixed local audit and Part XIII keep the moving zero extensions and deleted Euler factors in place.

The remaining conditions needed for (1) are supplied by the accepted selected-slot audit: the original prime slots have disjoint prime supports; their smooth weights multiply slotwise; μ(𝔭)=-1 and the original marked conjugate-η(D) split as primewise factors; norm Mellin dependence is (q_D^{iu}=\prod_iq_{\mathfrak p_i}^{iu}); and finite ray conditions reduce by finite Fourier expansion. Once row divisors and the priority assignment are frozen, each restriction is a fixed common hole (M_i). The joint Fourier modes in Parts XVII/XVIII retain their compact product cutoffs and rapid seminorm decay, so the polynomial factors in their heights are absorbed after integration. This is exactly the factorized setting of the accepted `selected_prime_q_gain3.md`/`selected_prime_q_referee3.md` argument, with ψ_v replaced by any genuine χ having good ramification outside (S).

The loss in (1) is ((q_\chi\prod_iq_{M_i})^\epsilon), not a conductor-free constant. For the mixed family (q_\chi\asymp VW) up to fixed factors, and the source's ambient parameter already records (VW), deleted primes, physical labels, and Gaussian/Fourier tails. It must be charged in the existing strict divisor summations or the original rapid-decay budget. This audit does not absorb an unbounded moving modulus into a fixed ray constant.

## Endpoint consequence and limitation

For a zero bin with (a=1-b), extracting selected primes from the true Möbius column gives the scalar factor
\[
(L/P_c)^{-a}=L^{-a}P_c^a
\]
(up to the source's small contour-buffer displacement). At the Q endpoint (b=7/8), (a=1/8), so (1) turns this into
\[
L^{-1/8}P_c^{\rho},
\]
with the conductor, hole, and height small powers still present. There are a fixed finite number of slots, and their actual product scale is bounded by a fixed power of the ambient physical scale. Choosing ρ smaller than the allotted ambient epsilon absorbs (P_c^{\rho}). Thus the selected slots cost no fixed power at this endpoint.

For (a>1/8), the same calculation leaves (L^{-a}P_c^{a-1/8+\rho}). Therefore the pointwise Q gain is a valid endpoint improvement but is not, on its own, a replacement for the moment bounds in bins farther left. Any improved complete mixed exponent still requires re-optimizing the existing physical/divisor budget with this endpoint input and retaining the original common-mode tails and hole costs.

The reviewed proof is [GENERAL_SELECTED_Q_GAIN](GENERAL_SELECTED_Q_GAIN.md). The actual mixed interfaces are [QUADRATIC_DUAL_N1, Parts XVII–XVIII](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/7821372494c3cc9b675f694549ca2550db0ff423/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md), and the verified finite-order input is [FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md). The review accepts the factorized pointwise lemma and its endpoint implication only.
