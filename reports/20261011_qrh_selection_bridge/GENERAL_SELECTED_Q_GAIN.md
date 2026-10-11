# Q prime gain for actual mixed finite-order selected slots

## The claim

Let (K=\mathbb Q(\sqrt{-3})), and assume Q for every finite-order Hecke character over (K): its nonprincipal (L)-function has no zero in \(\Re z>7/8\). Let \(\mathfrak S\) contain the fixed conductors of \(\eta\), the ray data, and all fixed bad factors. Let \(\chi\) be the actual finite-order moving character in the column, with conductor norm \(C_\chi\), and assume its good ramification support is nonempty and disjoint from \(\mathfrak S\). The cases used in the joint physical calculation are
\[
 \chi=\psi_v\chi_w,\qquad \psi_v=\chi_v^3,
 \quad v,w\text{ good, nonunit, squarefree},\quad (v,w)=1,
\tag{1}
\]
and the corresponding product of a good cube-free character \(\chi_u\) with a good \(\chi_w\) on disjoint support. In these cases the conductor is bounded by the product of the moving norms (and is comparable to \(q_vq_w\) in (1)).

For a fixed number (J\ge1) of disjoint prime slots, let \(P_i\ge2\) be their scales, \(P_c=\prod_iP_i\), and let \(W_i\) be fixed smooth weights on fixed positive annuli. After freezing the physical divisor choices, common holes, finite ray/unit choices, and a joint log-Fourier mode, the actual slot coefficient has the form
\[
 z_D=\prod_{i=1}^J W_i(q_{\mathfrak p_i}/P_i)
             \nu_i(\mathfrak p_i)q_{\mathfrak p_i}^{iu},
 \qquad D=\prod_i\mathfrak p_i,
\tag{2}
\]
where each \(\nu_i\) is a finite-order ray character supported on \(\mathfrak S\), and the common holes are \((\mathfrak p_i,M)=1\). Any additional fixed finite-order factor from the exact normalization is folded into \(\nu_i\). The prime sign mu(p)=-1 is a fixed scalar per slot and is pulled outside the character; the original conjugate-eta(p) marker is a fixed S-ray factor. Neither introduces a moving good character into nu_i. Crucially, no moving good-prime character is put into \(\nu_i\); the moving character is the displayed \(\chi\), with all its zero values retained.

For \(s=\sigma+it\), \(1/2+\delta_0\le\sigma\le1\), define the exact rational multiplier
\[
 E_\chi(s)=P_c^{s-1}\sum_D z_D
 \prod_{\mathfrak p\mid D}
 \frac{\eta(\mathfrak p)\chi(\mathfrak p)q_{\mathfrak p}^{-s}}
 {1-\eta(\mathfrak p)\chi(\mathfrak p)q_{\mathfrak p}^{-s}}.
\tag{3}
\]
Then for every \(\epsilon>0\),
\[
 \boxed{\quad |E_\chi(s)|\ll_{\epsilon,\delta_0}
 (C_\chi q_M)^\epsilon
 (1+|t|+|u|)^B P_c^{-1/8+\epsilon}.
 \quad}
\tag{4}
\]
The constants depend on the fixed ray data, (J), annular supports, and finitely many smooth seminorms, but not on the moving row. If the holes differ by slot, replace (q_M^\epsilon) by \(\prod_iq_{M_i}^\epsilon\). The bound is for a frozen summand/mode, not for arbitrary bounded coefficients (z_D).

## Why the actual joint physical coefficient is factorable

The factorization is made after the exact arithmetic split, not inferred from a size bound on (z_D). In Part XVIII A the moving column character is explicitly \(\eta\psi_v\chi_w\), with the two good supports disjoint; Part XVII A records the same actual moving-conductor family. In the physical interface of Part XVIII, §1, one first fixes (r,h_0,a',e), the finite ray/unit choices, and the dyadic norm blocks. The (c_2) coefficient is then the common coefficient \(\mu(c_2)\eta(c_2)/q_{c_2}\) with character \(\psi_v(c_2)\chi_w(c_2)\); all moving (v,w) masks are already the genuine zero extensions of that character. The priority allocation sends each selected prime either to a fixed scalar, to the frozen joint-row coefficient, or to this common (c_2) multiplier. Thus a remaining column prime sees only the common hole (M), the fixed bad-ray phase, and the moving character \(\chi\) in (3). No moving \(v\)- or \(w\)-character is hidden inside \(\nu_i\).

The selected-prime weights themselves separate. The original fixed slot weights are products over the slots. Any common smooth cutoff in (d=q_D/P_c) is separated by the retained log-Fourier rule: for a fixed mode (u),
\[
 d^{iu}=(q_D/P_c)^{iu}=P_c^{-iu}\prod_iq_{\mathfrak p_i}^{iu}.
\tag{5}
\]
The scalar (P_c^{-iu}) is common and each prime gets its own norm phase. The joint Gaussian/log-Fourier decomposition retains the fixed compact product cutoffs in every mode, so (5) is an exact factorization mode by mode, with the original integrable mode envelope. Unit and ray restrictions have only finitely many choices/characters, all supported at \(\mathfrak S\). The common deleted Euler primes remain in (M) and in its conductor loss. These are precisely the factorization and mask conditions recorded in Part XVIII, §1 and the slot multiplier in Part XVIII A, §4; the moving twist and its conductor are those of Part XVII A. Summing the finitely many assignments or ray characters only changes constants. One must not multiply after first adding different unfrozen modes or row divisors.

## Smooth mixed prime sum under Q

For any fixed finite-order ray character \(\nu\) supported at \(\mathfrak S\), set
\(\theta=\nu\eta\chi\). Since the moving good support of \(\chi\) is nonempty and disjoint from \(\mathfrak S\), \(\theta\) is ramified at a moving good prime, and hence is nonprincipal. This is the needed pole exclusion: a fixed bad-ray character cannot cancel ramification at a good moving prime. For the examples in (1), the disjoint (v,w) supports ensure the mixed product character remains nonprincipal. The same reasoning applies to the disjoint good supports of \(\chi_u\) and \(\chi_w\).

Let (W\in C_c^\infty((0,\infty))) be supported in ([a,b]), (0<a<b<\infty). Mellin inversion gives, initially on \(\Re z>1\),
\[
 \mathcal P(z,\theta)=\sum_{\mathfrak p}\theta(\mathfrak p)q_{\mathfrak p}^{-z}
 =\log L_K(z,\theta)-
 \sum_{\mathfrak p}\sum_{k\ge2}
       \frac{\theta(\mathfrak p)^k}{kq_{\mathfrak p}^{kz}},
\tag{6}
\]
and
\[
 \sum_{\mathfrak p}W(q_{\mathfrak p}/P)\theta(\mathfrak p)
 q_{\mathfrak p}^{-s+iu}
 =\frac1{2\pi i}\int_{(1/2)}
 \widehat W(z)P^z\mathcal P(s-iu+z,\theta)\,dz.
\tag{7}
\]
The initial line is absolutely convergent because \(\sigma+1/2>1\). Q, nonprincipality, and standard fixed-field Hecke growth imply that on every fixed buffered strip \(\Re z\ge7/8+\rho\),
\[
 |\log L_K(z,\theta)|\ll_{\rho}
       \log\!\big(C_\chi(3+|\Im z|)\big).
\tag{8}
\]
Indeed the zero-free half-plane gives an analytic logarithm; fixed-field growth bounds \(\log^+|L|\) by the right side, and Borel--Caratheodory on fixed-radius discs centered on the Euler line bounds the analytic logarithm in a narrower strip. This is the same buffered log/derivative argument used for the finite-height reciprocal estimate in Part VII, §4. The fixed \(\nu\eta\) changes the conductor only by a constant.

Shift just the log-(L) integral in (7) to \(\Re z=7/8+\rho-\sigma\), with (0<\rho<1/8). There is no pole because \(\theta\) is nonprincipal, and no zero is crossed by Q. The Mellin transform decays faster than every power uniformly over the bounded range of real parts. Consequently,
\[
 P^{s-1}\int_{(7/8+\rho-\sigma)}
 \widehat W(z)P^z\log L_K(s-iu+z,\theta)\,dz
 \ll_{\rho,\epsilon,W}
 C_\chi^\epsilon(1+|t|+|u|)^B P^{-1/8+\rho}.
\tag{9}
\]
Here \(|P^{s-1}|=P^{\sigma-1}\), which cancels the \(P^{-\sigma}\) in the contour length exponent. The height of (L) is (t-u+\Im z), and rapid Mellin decay absorbs the whole height integral into the displayed polynomial.

The prime-power correction in (6) returns under Mellin inversion as
\[
 \sum_{k\ge2}\sum_{\mathfrak p}
 \frac{\theta(\mathfrak p)^k}{k}q_{\mathfrak p}^{-k(s-iu)}
 W(q_{\mathfrak p}^k/P).
\]
On its support (q_{\mathfrak p}^k\asymp P). The elementary ideal count gives at most (O(P^{1/k})) possible prime ideals for each (k\ll\log P), while each summand is (O(P^{-\sigma}/k)). Hence the absolute sum is
\[
 \ll P^{-\sigma}\sum_{2\le k\ll\log P}P^{1/k}/k
 \ll P^{1/2-\sigma}.
\]
After the (P^{\sigma-1}) normalization this is (O(P^{-1/2})). This step uses only \(|\theta(\mathfrak p)|\le1\), so it keeps every mixed-character zero mask.

It follows that the leading prime term satisfies
\[
 P^{s-1}\sum_{\mathfrak p}W(q_{\mathfrak p}/P)
 \theta(\mathfrak p)q_{\mathfrak p}^{-s+iu}
 \ll C_\chi^\epsilon(1+|t|+|u|)^B
      (P^{-1/8+\rho}+P^{-1/2}).
\tag{10}
\]
If primes dividing the frozen (M) are omitted, their restoration costs
\[
 P^{\sigma-1}\sum_{\substack{\mathfrak p\mid M\\q_{\mathfrak p}\asymp P}}
 q_{\mathfrak p}^{-\sigma}
 \ll P^{-1}\frac{\log q_M}{\log P}
 \ll_\epsilon q_M^\epsilon P^{-1}.
\tag{11}
\]
For bounded (P), enlarge the constant. Thus the fixed/common holes do not threaten the Q saving.

## Geometric Euler expansion and product over slots

For each prime in (3), put (x=\chi(\mathfrak p)), which is either (0) at a ramified prime or a root of unity at an unramified prime, and (y=\eta(\mathfrak p)xq_{\mathfrak p}^{-s}). Since \(|y|\le q_{\mathfrak p}^{-\sigma}\le2^{-1/2-\delta_0}<1\),
\[
 \frac{y}{1-y}=y+\frac{y^2}{1-y}=y+O_{\delta_0}(q_{\mathfrak p}^{-2\sigma}).
\tag{12}
\]
This geometric first-term reduction is valid for every finite order and also gives zero when (x=0); it does not use the special quadratic identity.

For one frozen slot, factor the Cartesian product in (3):
\[
 E_\chi(s)=\prod_{i=1}^J F_{i,\chi}(s),\quad
 F_{i,\chi}(s)=P_i^{s-1}
 \sum_{\substack{\mathfrak p\text{ in slot }i\\(\mathfrak p,M)=1}}
 W_i(q_{\mathfrak p}/P_i)\nu_i(\mathfrak p)q_{\mathfrak p}^{iu}
 \frac{\eta(\mathfrak p)\chi(\mathfrak p)q_{\mathfrak p}^{-s}}
 {1-\eta(\mathfrak p)\chi(\mathfrak p)q_{\mathfrak p}^{-s}}.
\tag{13}
\]
The leading term of \(F_i\) is (10) with \(\theta_i=\nu_i\eta\chi\), which is nonprincipal by the good-support argument. The geometric remainder is bounded without cancellation:
\[
 P_i^{\sigma-1}\sum_{q_{\mathfrak p}\asymp P_i}
 O_{\delta_0}(q_{\mathfrak p}^{-2\sigma})
 \ll P_i^{\sigma-1}P_i^{1-2\sigma}=P_i^{-\sigma}.
\tag{14}
\]
The common-hole loss is (11) with (P=P_i). Therefore for every \(\epsilon>0\),
\[
 |F_{i,\chi}(s)|\ll
 (C_\chi q_M)^\epsilon(1+|t|+|u|)^B
 P_i^{-1/8+\epsilon}.
\tag{15}
\]
Choose smaller losses per slot and multiply over fixed (J). Since \(\prod_iP_i=P_c\), this proves (4). If the common log-Fourier mode is subsequently integrated, its original rapidly decreasing envelope absorbs the polynomial in (|u|); the estimate is uniform in each mode before that integration.

## Endpoint implication and exact limitation

The selected-column contour extraction pays (P_c^a) when the selected product of norm (P_c) is forced into the inverse column. Combining it with (4) gives
\[
 P_c^a|E_\chi(s)|\ll (C_\chi q_M)^\epsilon
 (1+|t|+|u|)^B P_c^{a-1/8+\epsilon}.
\]
At the (a=1/8) endpoint the scale powers cancel exactly, leaving only (P_c^\epsilon), uniformly in the joint row sizes and without a density factor such as (R/V) or (R/W). This removes the endpoint selected-slot loss in the frozen mixed summand.

It does not alone re-prove the joint exceptional-row budget or the full mixed physical estimate: those still require summing the frozen divisor/row factors, the deleted-modulus losses, and all log-Fourier/Gaussian tails in the audited common-cutoff organization. If a concrete summand leaves a moving good character in (\nu_i), fails the product-mode identity (5), or has row-dependent slot coefficients after freezing, this lemma does not apply to it.


The finite-order Q input is [FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md). The exact mixed slot interfaces are [QUADRATIC_DUAL_N1, Parts XVII–XVIII](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/7821372494c3cc9b675f694549ca2550db0ff423/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md). The independent review is [REFEREE_GENERAL_SELECTED_Q_GAIN](REFEREE_GENERAL_SELECTED_Q_GAIN.md). This lemma does not change any complete-sector exponent without its separate full budget.
