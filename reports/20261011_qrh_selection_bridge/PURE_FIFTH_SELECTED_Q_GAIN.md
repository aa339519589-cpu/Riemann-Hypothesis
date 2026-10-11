# Pure-fifth full-sector upgrade from the selected-prime Q gain

## Claim and scope

Use the same fixed input (Q) as Part XIV, with its verified finite-order scope recorded in [FORMAL_INPUT_Q.md](FORMAL_INPUT_Q.md): every nonprincipal finite-order Hecke (L)-function over (K=\mathbb Q(\sqrt{-3})) is zero-free in \(\Re z>7/8\). Combine the public pointwise selected-slot lemma in [`GENERAL_SELECTED_Q_GAIN.md`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/113702dd9ff055b343a89d2667fb9ff72783de97/reports/20261011_qrh_selection_bridge/GENERAL_SELECTED_Q_GAIN.md#L1) with the reviewed complete physical interface in Part XIV of [`QUADRATIC_DUAL_N1.md`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/113702dd9ff055b343a89d2667fb9ff72783de97/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md#L2899).

For the complete pure-fifth type
\[
 H=\varepsilon w^5a^6,\qquad w\text{ good, squarefree, and nonunit},
\]
the resulting compensated normalized exponent is
\[
 \boxed{-209/960+\epsilon.}
\]
This improves Part XIV's \(-63/320\) by \(1/48\), and lies \(29/960\) below the required \(-3/16\). Under Part XIV's convention, \(G_{\mathrm{norm}}=G_{\mathrm{raw}}-5/12+d/2\); hence the uniform normalized bound gives the raw linear-sum estimate \(O_\epsilon(Z^{191/960-d/2+\epsilon})\) for each original finite-compensation length \(d\in[0,1/6]\). The raw exponent is an upper bound, not a claim that the fixed-\(d\) maximizer is always the endpoint bin.

The scope remains exactly Part XIV's: every physical index (n), the original and core markings, and both markings' exact first Möbius-flat operations. This is conditional on (Q), and asserts no bound for the remaining frequency types or for RH.

## The actual pure-fifth slot multiplier satisfies the pointwise lemma

Fix a zero bin, a physical scale (0<T\le Z), and the exact arithmetic choices before estimating the remaining column: (r,h_0,a'), the ordinary-mask branch and its fixed (s)-divisor extractions, the finite ray/unit choices, and the dyadic norm blocks. This is the order used in Part XIV B, equations (1)–(3). The exact free (c_2) coefficient is the true Möbius column
\[
 \mu(c_2)\eta(c_2)\chi_w(c_2)/q_{c_2},
\]
with its common masks; the (e) coefficient \(\eta(e)/q_e\) remains in the row/external sum. The physical interface assigns each original slot to its first applicable factor (r,g,e,c_2) (or (g,e,c_2) for the core marker). Thus, once row assignments are frozen, the residual (c_2)-assigned slots have only fixed common exclusions and the displayed moving character. A prime dividing (w) remains a genuine zero of \(\chi_w\).

The rational Euler factor is exact for this finite-order character, with no quadratic-denominator identity needed. Write \(L_K^{\mathfrak S}\) for the Hecke L-function with the Euler factors at \(\mathfrak S\) removed. For squarefree selected \(D_c\) with \( (D_c,M\mathfrak S)=1 \) and frozen hole \(M\), the local Euler product gives on \(\Re s>1\)
\[
 \sum_{\substack{D_c\mid c\\(c,M\mathfrak S)=1}}
   \frac{\mu(c)\eta(c)\chi_w(c)}{q_c^s}
 =\frac{1}{L_K^{\mathfrak S}(s,\eta\chi_w)}
   \prod_{\substack{\mathfrak p\mid M\\\mathfrak p\notin\mathfrak S}}
      (1-\eta(\mathfrak p)\chi_w(\mathfrak p)q_{\mathfrak p}^{-s})^{-1}
   \prod_{\mathfrak p\mid D_c}
      \frac{-\eta(\mathfrak p)\chi_w(\mathfrak p)q_{\mathfrak p}^{-s}}
           {1-\eta(\mathfrak p)\chi_w(\mathfrak p)q_{\mathfrak p}^{-s}}.
\tag{0}
\]
Each selected local factor vanishes when \(\chi_w(\mathfrak p)=0\). This is the order-independent Euler calculation behind the exact extraction in Part XIV B, (3); it identifies the normalized selected multiplier with (A), up to fixed signs and ray factors.

Let (J\ge1) be the number of residual column slots, with disjoint prime windows of scales (P_i\ge2), and (P_c=\prod_iP_i). Freeze the common holes (M_i) and the finite ray data. The original slot weights factor over slots. Any shared smooth dependence on their product is a smooth function of (d=q_D/P_c), with the other frozen variables as parameters, on a fixed compact positive interval. In each retained joint log-Fourier mode,
\[
 d^{iu}=P_c^{-iu}\prod_i q_{\mathfrak p_i}^{iu}.
\]
Consequently the exact frozen coefficient is a Cartesian product of slot weights
\[
 z_D=\prod_i W_i(q_{\mathfrak p_i}/P_i)\nu_i(\mathfrak p_i)q_{\mathfrak p_i}^{iu},
 \qquad D=\prod_i\mathfrak p_i,
\]
up to a common unit-modulus scalar. Here each \(\nu_i\) is supported on the fixed bad/ray set \(\mathfrak S\). The sign \(\mu(\mathfrak p_i)=-1\) is fixed per slot, and any conjugate fixed-\(\eta\) marker is also fixed-ray data. Neither can hide a moving good-prime character in \(\nu_i\). This is precisely the frozen-product condition needed by the public lemma, rather than an application to arbitrary bounded \(z_D\). Part XIV B, lines 3132–3141, supplies the pure-fifth priority assignment, retained compact cutoffs, exact column, and actual imprimitive masks; the original slot and zero-real-part Gaussian factorization is also explicit in Parts I and V, including the general physical row split.

For clarity, the single-slot estimate can be read directly from the general proof. Put
\[
 F_i(s)=P_i^{s-1}\sum_{(\mathfrak p,M_i)=1}
 W_i(q_{\mathfrak p}/P_i)\nu_i(\mathfrak p)q_{\mathfrak p}^{iu}
 \frac{\eta(\mathfrak p)\chi_w(\mathfrak p)q_{\mathfrak p}^{-s}}
 {1-\eta(\mathfrak p)\chi_w(\mathfrak p)q_{\mathfrak p}^{-s}}.
\]
On the buffered bin contours \(1/2+\delta_0\le\sigma=\Re s\le1\), with fixed \(\delta_0>0\), set \(y=\eta(\mathfrak p)\chi_w(\mathfrak p)q_{\mathfrak p}^{-s}\). Since \(|\chi_w(\mathfrak p)|\le1\), including its zero values,
\[
 \frac{y}{1-y}=y+O_{\delta_0}(q_{\mathfrak p}^{-2\sigma}).
\]
The leading prime sum has character \(\theta_i=\nu_i\eta\chi_w\). As (w) is nonunit and supported away from \(\mathfrak S\), this character is ramified at a good prime dividing (w), so it is nonprincipal: a fixed ray factor cannot cancel that ramification.

Mellin inversion and the Euler identity
\[
 \sum_{\mathfrak p}\theta_i(\mathfrak p)q_{\mathfrak p}^{-z}
 =\log L_K(z,\theta_i)-
 \sum_{\mathfrak p}\sum_{k\ge2}\frac{\theta_i(\mathfrak p)^k}{kq_{\mathfrak p}^{kz}}
\]
start absolutely on \(\Re z=\sigma+1/2>1\). Shift only the \(\log L\) integral to \(\Re z=7/8+\rho\). Nonprincipality removes the pole, (Q) supplies zero-freeness, and the buffered log bound gives, for any fixed \(0<\rho<1/8\),
\[
 P_i^{s-1}\sum_{\mathfrak p}W_i(q_{\mathfrak p}/P_i)
 \theta_i(\mathfrak p)q_{\mathfrak p}^{-s+iu}
 \ll (q_w)^{\epsilon}(1+|t|+|u|)^B
 \big(P_i^{-1/8+\rho}+P_i^{-1/2}\big).
\]
The last term is the prime-power correction, bounded absolutely on its smooth support. The geometric Euler remainder contributes \(O(P_i^{-\sigma})\) after normalization. Restoring primes removed by (M_i) costs at most \(q_{M_i}^{\epsilon}P_i^{-1}\), by the elementary count of prime divisors in the annulus. Hence, after choosing \(\rho\) below the target loss,
\[
 |F_i(s)|\ll (q_wq_{M_i})^{\epsilon}
 (1+|t|+|u|)^B P_i^{-1/8+\epsilon}.
\]
Multiplication over the fixed number of slots proves the exact frozen multiplier bound
\[
 |E_{w}(s)|\ll (q_w\prod_iq_{M_i})^{\epsilon}
 (1+|t|+|u|)^B P_c^{-1/8+\epsilon}.
 \tag{A}
\]
All moving zeros stay zero throughout. The height polynomial is uniform mode-by-mode; Part XIV's retained Gaussian/Schwartz envelope absorbs it when the modes are integrated. For (J=0), define (P_c=1,E_w=1); that empty-column case is handled separately below.

## Insert the gain into every bin and physical row

Part XIV B, (3), gives the frozen selected-column cost on a bin (1/8\le a\le1/2) as
\[
 \mathfrak X^{\epsilon}
 \left(\frac{Y'P_cq_r^6}{C_l}\right)^a W^{F(a)},
 \qquad C_l=e^lTP,
\]
where \(F(a)=D_6(1-a)+(1-a)/2\). Applying (A) changes its selected factor to
\[
 \mathfrak X^{\epsilon}(1+|t|+|u|)^B
 \left(\frac{Y'q_r^6}{C_l}\right)^a
 P_c^{a-1/8+\epsilon}W^{F(a)}.
 \tag{B}
\]
The exponent (a-1/8+\epsilon) is nonnegative. Since (P_c\le C P), including the assignment where every remaining slot is in (c_2),
\[
 P_c^{a-1/8+\epsilon}\ll P^{a-1/8+\epsilon}.
\]
Thus every frozen assignment is bounded by (P^{-1/8+\epsilon}) times the old uniform bin majorant with (P_c^a\le C^aP^a). If (P_c=1), (B)'s selected factor is (1\le P^{a-1/8+\epsilon}); this proves the same global upper envelope without claiming a (P^{-1/8}) saving on that individual empty-column summand. The finite sum of priority assignments and ray choices only changes the fixed constants.

The new conductor factor (q_w^\epsilon), all actual common-hole factors (q_{M_i}^\epsilon), and the height polynomial are entered into the ambient small powers before any infinite summation. They are not suppressed as fixed constants. Part XIV A/B already requires this ambient-first convention and absorbs its small powers only using the complete Fourier/Gaussian tails and the strict (a')- and (r)-summability margins; its e sum is finite with the exact \(\eta(e)/q_e\) retained. The slot estimate is uniform in the physical labels and (T), so the same absorption applies after the multiplier is inserted. This is also why no moving good character may be folded into \(\nu_i\): all moving conductor dependence is explicitly charged to (q_w^\epsilon).

For each frozen physical row, the slot estimate is uniform in (r,h_0,a',e), the ordinary-mask branch, the retained mode, and (T); its conductor and common-hole losses have already been charged as ambient small powers. After summing the physical rows, actual finite cutoffs, and the retained joint modes using the complete Part XIV Fourier/Gaussian tails and strict (a')- and (r)-summability margins, the unbounded row labels no longer occur in the constant. The resulting complete all-scale bound is, for every (0<T\le Z) and both marker priority rules,
\[
 |S_{\rm fifth}(T)|\ll
 Z^\epsilon(1+|\nu|)^B P^{-1/8+\epsilon}
 \frac{Q}{Y'^{3/2}}
 \max_{1/8\le a\le1/2}
 \left(\frac{Y'}{T}\right)^a
 \left(\frac{TP}{X'}\right)^{[F(a)+(6a-2)_+]/5}.
 \tag{C}
\]
Here \(B\) is a fixed height-polynomial exponent after the joint modes are integrated against their retained Schwartz envelope; it is independent of \(w,r,h_0,a',e\). Uniformity in (T), including subunit (K_l), comes from Part XIV's full Schwartz/Gaussian bound, not a hard cutoff. Every physical (n) is still (r^2); (h_0\mid\operatorname{rad}r,w), (h_0\le r), and the exact exceptional/ordinary masks are untouched. The (r)- and (h_0)-summations use the same support inequality and complete tails as Part XIV B, (5)–(7).

For either first-flat operator, substitute (T=Z/q_\delta^6) in (C), keeping (X',Y') and all slots fixed, and retain its true coefficient of size (q_\delta^{-2}). The slot gain is independent of \(\delta\). The existing \(\beta(a)=[F(a)+(6a-2)_+]/5-a\ge-1/10\) gives the convergent actual flat weight \(q_\delta^{-7/5+\epsilon}\); any \(q_\delta^\epsilon\) entering a common hole is absorbed by this strict margin and the existing ambient/tail argument. The redundant frequency lift still preserves the pure-fifth core and unit. This proves the same upgrade for the original-marked and core-marked first flats; it does not identify the two operators.

## Exact exponent certificate

Use (d\in[0,1/6]) for the original finite-compensation parameter, to distinguish it from the slot ratio (q_D/P_c). At the original scales, (P\asymp Z^{1/6-d}). Part XIV A, (11)–(12), gives the normalized old exponent
\[
 G_{5,\mathrm{old}}(a,d)=G_0(a)-ad,
 \qquad
 G_0(a)=-\frac{29}{96}-\frac{25a}{48}
       +\frac{13}{80}\bigl(F(a)+(6a-2)_+\bigr).
\]
The factor in (C) subtracts \((1/6-d)/8\), so
\[
 \begin{aligned}
 G_{5,\mathrm{new}}(a,d)
 &=G_0(a)-ad-\frac{1/6-d}{8}\\
 &=G_0(a)-\frac1{48}+d\left(\frac18-a\right)
 \le G_0(a)-\frac1{48},
 \end{aligned}
 \tag{D}
\]
for every (a\in[1/8,1/2]), (d\in[0,1/6]). This checks both compensation endpoints and the full interval; the coefficient of (d) is nonpositive, with equality only at (a=1/8).

For completeness, the old exact maximum certificate is as follows. On \([1/8,1/3]\),
\[
 G_0'(a)=-\frac{p(a)}{480(72a^2-12a-7)^2},\quad
 p(a)=1498176a^4-499392a^3-401328a^2+172104a-10877.
\]
Under (a=1/8+5t/24), the degree-four Bernstein coefficients of (p) are
\[
 240361/64,\quad220293/32,\quad54167/8,\quad15921/4,\quad1899,
\]
all positive. Thus (G_0) decreases on this interval and
\(G_0(1/8)=-16641/75520<-63/320\). On \([1/3,1/2]\),
\[
 G_0(a)+\frac{63}{320}
 =\frac{(2a-1)(1074a-101)}{960(6a-1)}\le0.
\]
The maximum is exactly \(-63/320\), attained at the limiting endpoint (a=1/2). Therefore the new maximum is
\[
 -\frac{63}{320}-\frac1{48}
 =-\frac{189}{960}-\frac{20}{960}
 =-\frac{209}{960}.
\]
The required threshold is \(-3/16=-180/960\), so the new margin is exactly \(29/960\). The bin widths, \(\rho\), and all other small losses can be chosen below this strict margin as in Part XIV. For every \(a\) and \(d\), Part XIV's raw convention is
\[
 G_{\rm raw}(a,d)=G_{5,\mathrm{new}}(a,d)+\frac{5}{12}-\frac d2
 \le -\frac{209}{960}+\frac{5}{12}-\frac d2
 =\frac{191}{960}-\frac d2.
\]
At \(d=0\), equality in the global normalized maximum is attained at the limiting endpoint \(a=1/2\); for \(d>0\), this statement is the uniform raw upper bound and does not assert a fixed-\(d\) maximizing bin.

## Source boundary

This uses the public [`GENERAL_SELECTED_Q_GAIN.md`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/113702dd9ff055b343a89d2667fb9ff72783de97/reports/20261011_qrh_selection_bridge/GENERAL_SELECTED_Q_GAIN.md), especially its actual-weight factorization and nonprincipal mixed prime-sum proof (lines 13–54, 56–154), together with the exact pure-fifth physical extraction and uniform scale/flat transfer in Part XIV B of [`QUADRATIC_DUAL_N1.md`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/113702dd9ff055b343a89d2667fb9ff72783de97/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md) and the independent Part XIV audit in [`REFEREE_QUADRATIC_DUAL_N1.md`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/113702dd9ff055b343a89d2667fb9ff72783de97/reports/20261011_qrh_selection_bridge/REFEREE_QUADRATIC_DUAL_N1.md). The exact fraction/derivative checks are also recorded in the same-directory file [`check_purefifth_selected_q.py`](check_purefifth_selected_q.py); that script checks the rational arithmetic only, not the analytic inputs. The arithmetic physical proof and the public mixed-slot lemma are the inputs; the new assertion here is their pure-fifth pointwise composition and the exact exponent update. It remains conditional on the user's attributed Q input and does not assert a new RH result.


The independent composition review is [REFEREE_PURE_FIFTH_SELECTED_Q_GAIN.md](REFEREE_PURE_FIFTH_SELECTED_Q_GAIN.md).
