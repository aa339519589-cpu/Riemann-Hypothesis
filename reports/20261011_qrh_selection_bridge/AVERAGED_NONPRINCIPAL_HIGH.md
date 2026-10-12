# Nonprincipal high remainder: safe-line ensemble and the exact gap

Date: 2026-10-12. This note concerns the half-damped η=1 probe and its original/core nonflat finite-slot markers. It gives an exact dynamic decomposition, then a separate safe-line estimate for the nonprincipal rows after the polynomial auxiliary-prime average. It does not claim a low bound for the averaged whole probe or an RH result.

## 1. Notation and what is being estimated

Let (S_0) be the original fixed bad set and let the fixed physical prime slots have scales (P_i=Z^{\ell_i}), (1\le i\le K), with \(\ell=\sum_i\ell_i\). Write (x,w,z) for the three *high-contour variables*. The (s) in the exclusive marker below is the original physical divisibility label; it is not (x), and the s-unit condition is never changed into a condition on a contour variable.

For \(\star\in\{\mathrm{orig},\mathrm{core}\}\), write \(\mathfrak H^{\star}_{u,Z}(x,w,z)\) for the exact finite-slot correction: each selected prime contributes the original holomorphic \(G_p\) replacement (or the separately derived core replacement), and every unselected prime contributes the full half-damped \(H_p\). In particular the core replacement is

\[
G_{p,\mathrm{core}}=G_{p,\mathrm{orig}}-
 \frac{P^x(1-V)(1-W)F_{p,\mathrm{first}}}{1-D},
\]

with the removed first even family retained in \(F_{p,\mathrm{first}}\). One must not substitute \(P^*_{p,\mathrm{core}}\) into the simplified original \(G_p\) formula while leaving its old unmarked complement in place.

Up to the unchanged outer Gaussian/Mellin kernel and the fixed unit phase, the row in the exact high identity is

\[
\mathcal A^{\star}_{u}(x,w,z;Z)=
q_u^{-z}\,\zeta_K^{S}(6z)
\frac{L^{S}(w,\chi_\bullet(u))}{L^{S}(x,\overline{\chi_\bullet(u)})}
\mathfrak H^{\star}_{u,Z}(x,w,z).
\tag{1}
\]

This is the row identity, not a claim that the three contours may be moved through every zero of the denominator. The denominator is kept as the literal reciprocal in (1).

## 2. Exact whole-slot decomposition on the dynamic line

For the half-damped original/core markers, the reviewed dynamic line is

\[
x_r=a+16e,\qquad w_r=1-a-6e,\qquad z_r=17/50,
\quad 51/100\le a\le1,\quad 0<e\le10^{-3}.
\tag{2}
\]

At a selected identity-ray prime \(p\), put \(P=Np\). The original holomorphic replacement is

\[
G_{p,\mathrm{orig}}=
\frac{(P^x-P^{-w})(1-V)(1-W)P_p^*-P^{-w}(1-VW)}{1-D}.
\tag{3}
\]

The core replacement is (3) minus the explicit first-family correction displayed in Section 1. Set \(\mathcal B_{p,\star}=G_{p,\star}/H_p\) on (2), where the proof gives \(|H_p-1|<1/2\) for all sufficiently large selected primes. Define the actual whole slot sums

\[
\mathcal B_{i,\star}(u)=\sum_{p\in\mathcal P_i(Z)}
 W_i(P/P_i)P^{z-1}\mathcal B_{p,\star}(u),\qquad
\mathcal Q_i(u;z)=-\sum_{p\in\mathcal P_i(Z)}
 W_i(P/P_i)P^{z-1}\overline{\chi_p(u)},
\]

and \(\mathcal D_{i,\star}=\mathcal B_{i,\star}-\mathcal Q_i\). On the dynamic line the exact identity is

\[
\boxed{\quad \mathfrak H^{\star}_{u,Z}
=\mathcal H^{[1/2]}_u\prod_{i=1}^K(\mathcal Q_i+\mathcal D_{i,\star})
=\mathcal H^{[1/2]}_u\sum_{I\subseteq[K]}
  \prod_{i\in I}\mathcal D_{i,\star}
  \prod_{i\notin I}\mathcal Q_i.\quad}
\tag{4}
\]

Here \(\mathcal H^{[1/2]}_u=\prod_{p\notin S_0}H_p^{[1/2]}\), with the selected factors divided out exactly once in \(\mathcal B_i\). The flat local baseline is \(H_p=1+(H_p-1)\); (4) does not replace the full Euler product by 1. It retains every local defect and every finite compensation term.

For \(p\nmid u\), the exact local identity from the half-damped table is

\[
G_{p,\mathrm{orig}}+\overline{\chi_p(u)}H_p
=\frac{(1-V)(1-W)}{1-D}
\left[(\overline{\chi_p(u)}-P^{-w})\left\{\frac{V}{1-V}-D\right\}
+(P^x+\overline{\chi_p(u)}-P^{-w})E_p\right],
\quad E_p=P_p^*+D.
\tag{5}
\]

Thus (5), divided by \(H_p\), is the exact local error \(\mathcal B_{p,\mathrm{orig}}+\overline{\chi_p(u)}\). On (2), its magnitude is \(O(P^{-51/100})\), uniformly in all heights and unit phases. The core difference contributes less: at \(j=v_p(u)=0\) its exponent is at most \(24/25-5a-68e\); at ramified states its common-family and \(j=5\) exponents, after the slot normalization, are at most \(2-5x_r-6z_r\) and \(1-5x_r\). Both are below \(-1/2\). Hence the same unramified error bound and the same strict ramified term govern both original and core markers.

The exact whole-error estimate, for every slot subset \(I\), is the source's conditional functional-equation bound

\[
\left|L^S(w,\chi_\bullet(u))\prod_{i\in I}\mathcal D_{i,\star}(u)\right|
\ll U^{a-1/2+O(e)+\epsilon}(3+T_1)^C
       \prod_{i\in I}P_i^{z_r-1/2+O(e)+\epsilon},
\quad q_u\asymp U.
\tag{6}
\]

It assumes the actual retained-height bound \(|L^S(1-w,\overline{\psi_u^*})|\ll U^\epsilon\). The ramified strict second-family term is exactly \(-(P-1)P^{-x-w}\); it is not locally small when \(w_r\) approaches or crosses zero. Its payment uses the *whole* primitive conductor once: if \(J_0\) is the set of distinct selected ramified labels, then

\[
q_{\mathfrak f_u}\ll_{S_0}q_{\operatorname{rad}(u)}
\le q_u\prod_{p\in J_0}P^{-(j_p-1)},\qquad
A_*=\tfrac12-w_r=a-\tfrac12+6e,
\]

and the exponent at a strict label is \(-w_r-(j_p-1)A_*\le-1/2\) because \(j_p\ge2\). This is the exact finite-conductor allocation; it is not a bound for \(1/L(x,\overline{\chi_u})\).

The core correction uses its actual holomorphic \(G_{p,\mathrm{core}}\), and (6) remains unchanged. This preserves the full finite compensation and all original/core nonflat masks.

## 3. What the selected-prime Q lemma does prove

For a nonprincipal row character with genuinely good ramification outside the fixed bad set, freeze the row divisors, common holes, ray choices, and joint log-Fourier mode before applying the factorized-prime lemma. The main slot has the *physical prime-sum exponent* \(s_Q=1-z\), not the reciprocal contour variable \(x\). Since \(\Re(1-z_r)>1/2\) both for \(z_r=17/50\) and for \(z_r=1/6+e\), the Q prime-sum shift is legal and gives

\[
P_i^{-z}\mathcal Q_i(u;z)
=P_i^{s_Q-1}\sum_{p\in\mathcal P_i}W_i(P/P_i)
 \overline{\chi_p(u)}P^{-s_Q}
\ll (q_{\chi_u}q_{M_i})^\epsilon
 (1+|\Im z|+|\omega|)^B P_i^{-1/8+\rho}.
\tag{7}
\]

Equivalently \(|\mathcal Q_i|\ll(q_{\chi_u}q_{M_i})^\epsilon
\langle\Im z,\omega\rangle^B P_i^{z_r-1/8+\rho}\). The conductor, deleted-prime, and height losses are displayed; the coefficient must be factorable after freezing, and the moving good character cannot be hidden in a slot coefficient. For a normalized slot \(\mathcal Q_i=P_i^{z-1/2}Q_i\), (7) gives \(|Q_i|\ll P_i^{3/8+\rho+\epsilon}\).

Combining (6) and (7), a fixed factorable summand with good-moving conductor satisfies the exact sufficient product inequality

\[
\begin{aligned}
\left|L^S(w,\chi_u)\prod_{i\in I}\mathcal D_{i,\star}
                        \prod_{i\notin I}\mathcal Q_i\right|
\ll{}&(q_u\prod_iq_{M_i})^\epsilon(3+T_1)^B
 U^{a-1/2+O(e)+\epsilon}\\[-2pt]
&\times\prod_{i\in I}P_i^{z_r-1/2+O(e)+\epsilon}
 \prod_{i\notin I}P_i^{z_r-1/8+\rho+\epsilon}.
\end{aligned}
\tag{8}
\]

The source stage exponent therefore has the sufficient dynamic form

\[
E_{\sigma_0}^{\star}(d;R,g,z_0)
=a-\sigma_0+h(z_0-1/6)-a l_y-\ell/2+g
+d(R+\delta/2-z_0),\qquad \delta=2a-1,
\tag{9}
\]

provided the actual row count is \(\#E_{U,a}\ll U^{R+\epsilon}(1+T_1)^A\), every selected reciprocal is bounded on the retained row-conditioned contour, and the same finite-height and external-tail budgets are paid. The Q bound permits \(g\le3\ell/8+\epsilon\) for all-main slots with good-moving conductor (or the better of this and the old amplitude bin); error slots use (6). To claim a power-saving high remainder one must still prove \(\sup_{d,R,a,I}E_{\sigma_0}^{\star}\le-m\), after all fixed losses, for every required row bin.

Equation (7) does **not** control \(1/L(x,\overline{\chi_u})\). The prime Q shift is in the auxiliary Mellin variable for a prime sum with exponent \(1-z\). It does not move the reciprocal \(L\)-contour and does not bound its poles.

## 4. The exclusive s-unit operation is a different probe

The exclusive marker at commit `5615d29` imposes, at each physical slot prime,

\[
p\mid cn\ \text{and}\ p\nmid s_{\rm physical}
\]

(or \(p\mid cn_0\) and \(p\nmid s_{\rm physical}\) for the core marker). It sets the *local physical valuation* \(k=v_p(s_{\rm physical})\) to zero. It does not set or constrain the high variable \(x\).

Its exact half-damped local formula is

\[
P^*_{p,\rm ex}=(1-R')^{-1}\left\{
\frac{R'(1-P^{-1})}{1-V}-\mathbf1_{j=0}D
+\mathbf1_{j=2}a_p\rho^{-3}P^{1-3x}
+\mathbf1_{j=3}b_p^2\rho^{-4}P^{3/2-4x}
-\mathbf1_{j=5}a_p^2P^{2-6x}\right\},
\]

\[
G_{p,\rm ex}=\frac{(1-V)(1-W)}{1-D}
       [P^xP^*_{p,\rm ex}-P^{-w}P_p],
\qquad
G_{p,\rm ex,core}=G_{p,\rm ex}
-\frac{P^x(1-V)(1-W)F_{p,\rm ex,first}}{1-D}.
\tag{10}
\]

The unmarked \(P_p\) in (10) is the original full local sum. The stated exclusive dynamic line is \(x_r=a+16e, w_r=1-a-6e, z_r=1/6+e\), with \(1/2+\delta\le a\le1-\delta_w\) and \(e<\delta_w/12\). The literal s-unit table removes the strict \((e_0,l,k,m)=(1,0,1,0)\) term, and yields the same error estimate as (6), now with \(z_r=1/6+e\), without that strict-label conductor allocation. This is a valid improvement for the *new exclusive physical observation*. It is not a replacement of the original/core probe.

## 5. A nonprincipal high bound that avoids every unsafe reciprocal line

There is a clean way to avoid the reciprocal-L obstruction on the high side: average the admissible auxiliary bad moduli, but leave every nonprincipal row on the original absolute line \((\Re x,\Re w,\Re z)=(3,3,2)\). This is a bound for the new averaged observation, not for any one fixed modulus. This is the source's original absolutely convergent starting line, so no contour move is made for these rows.

Use the unrestricted good-prime ensemble of `POLYNOMIAL_AUXILIARY_ENSEMBLE.md` at `7fade07`: \(R\to\infty\), \(L=\log R\), \(P_0=L^{64}\), \(k=\lfloor L/(65\log L)\rfloor\), and choose an unordered \(k\)-set \(J\) with the stated positive elementary-symmetric law. Let \(B_J=\prod_{p\in J}p\); then \(N B_J\le R\). Keep the pool unrestricted by ray class. Put each \(p\in J\) outside every fixed physical slot support, which holds for large \(Z\) when \(R=Z^\lambda\) and every \(\ell_i>0\). Choose ensemble parameters \(A_0,A_1,A_2\) to cover, respectively, the truncated row norms, every frozen common-hole norm in the selected-slot coefficients, and the common three-height window. These are fixed powers of \(R\) after the physical labels are frozen.

For the half-damped unmarked factor define the exact deleted-prime multiplier

\[
Z_{p,\rm half}(u;x,w,z)=
\frac{(1-V)[\chi_p(u)-\chi_p(u)^2P^{-w}]}
 {(1-D)H_p^{[1/2]}(x,w,z)},
\tag{11}
\]

with zero value if \(p\mid u\). This retains the deleted scalar-zeta factor, both numerator/denominator Euler factors, and the local correction. Because the auxiliary primes are disjoint from the original selected slots, (11) multiplies the *whole* original/core finite-slot row; it does not alter any \(G_{p,\star}\) term. The CRT/Gauss cancellation removes the auxiliary norm prefactor exactly. Thus, for each fixed row and common heights,

\[
\mathcal A^{\star}_{u,J}(x,w,z;Z)
=\mathcal A^{\star}_{u,S_0}(x,w,z;Z)
 \prod_{p\in J}Z_{p,\rm half}(u;x,w,z).
\tag{12}
\]

At \((\Re x,\Re w,\Re z)=(3,3,2)\), the half-damped critical-window estimate gives \(Z_{p,\rm half}=\chi_p(u)+O(P^{-1/2})\), uniformly in all heights. For each sixth-power-free \(u\ne1\), \(\chi_p(u)\) is a nonprincipal Kummer character on the *unrestricted* good-prime monoid, including the five nontrivial unit rows. Its conductor satisfies \(C_{\chi_u}\ll (Nu)^5\) up to fixed data. The exact no-replacement ensemble lemma therefore gives

\[
\left|\mathbb E_J\prod_{p\in J}Z_{p,\rm half}(u;3+it,3+iv,2+ir)\right|
\le R^{-1/20}
\tag{13}
\]

for \(Nu\le R^{A_0}\), actual common holes \(q_{M_i}\le R^{A_1}\), and \(|t|+|v|+|r|\le R^{A_2}\), with any fixed \(A_0,A_1,A_2\). No ray conditioning is permitted in this average: it would remove the needed cancellation for bad-supported unit characters.

On the same absolute line, all factors of (1) are harmless without Q. Uniformly in finite-order \(\chi_u\),

\[
|L^{S_0}(3+iv,\chi_u)|\ll1,
\qquad |L^{S_0}(3+it,\overline{\chi_u})|^{-1}\ll1,
\qquad |\zeta_K^{S_0}(12+6ir)|\ll1.
\tag{14}
\]

The inverse bound follows from the absolutely convergent Euler product at real part 3; it is not a claim about any line below \(7/8\). The D2 local product is \(\ll_\epsilon (Nu)^\epsilon\), uniformly in heights. Directly at real parts \((3,3,2)\), each exact selected \(G_{p,\star}\) is \(O(1)\) for every valuation state \(j=0,\ldots,5\); the same holds for the core correction and for the local restriction (10). For long rows, \(|Z_{p,\rm half}|\le1+O(P^{-1/2})\), so \(\prod_{p\in J}|Z_{p,\rm half}|=O(1)\) because \(kP^{-1/2}=o(1)\). Thus the full finite compensation, not only its flat leading term, obeys

\[
\left|\frac{\mathfrak H^{\star}_{u,Z}(3+it,3+iv,2+ir)}{A_T(Z)}\right|
\ll_\epsilon (Nu)^\epsilon Z^{2\ell+\epsilon}.
\tag{15}
\]

This can also be seen by summing \(O(P_i)\) selected primes with weight \(P^{z-1}\) and \(|G_{p,\star}|\ll1\), giving \(P_i^2\) per slot. The original/core and exclusive local replacements all remain quotient-free at selected primes.

There are \(O(U)\) sixth-power-free ideals in a dyad \(Nu\asymp U\), and the row has the exact outside factor \((Nu)^{-2}\). Equations (14)--(15) imply the absolutely convergent majorant

\[
\sum_{u\ne1}|\mathcal A^{\star}_{u,S_0}(3+it,3+iv,2+ir;Z)|/|A_T(Z)|
\ll_\epsilon Z^{C(3)+2\ell+\epsilon},
\tag{16}
\]

with a finite height seminorm. For \(Nu>R^{A_0}\), the same direct majorant gives a tail \(\ll Z^{C(3)+2\ell+\epsilon}R^{-A_0(1-2\epsilon)}\). The Gaussian in \(x\), the original \(w\)-Mellin transform, and \(M(z)\) retain their three independent heights. Outside the box \(|t|+|v|+|r|\le R^{A_2}\), use their original Schwartz/Gaussian tails, giving \(O_N(Z^{C(3)+2\ell+\epsilon}R^{-A_2N})\). No selected-zero or Fejér height is replaced by this Mellin-height box.

Applying (13) rowwise to the finite range, using the actual absolutely convergent row majorant (16), and then adding the two unaveraged tails proves

\[
\boxed{
\frac{|\mathbb E_J\mathscr R^{\star}_{\ne1}(Z)|}{|A_T(Z)|}
\ll_{\epsilon,N}
 Z^{C(3)+2\ell+\epsilon}
 \left(R^{-1/20}+R^{-A_0(1-2\epsilon)}+R^{-A_2N}\right).
}
\tag{17}
\]

Here \(\mathscr R^{\star}_{\ne1}\) is the full nonprincipal part of the exact high identity, integrated on the original \((3,3,2)\) contours, including all rows, all original/core finite compensation terms, and all six units. Equation (17) does not shift a nonprincipal reciprocal contour and crosses no denominator zero. It has no \(L'(\rho)\) term.

Since \(C(s)=s+l_x/2-1+h/6\) has slope one, \(C(3)-C(\sigma_0)=3-\sigma_0\). For any fixed \(\sigma_0>1/2\) and desired \(m>0\), set \(R=Z^\lambda\), choose

\[
\frac{\lambda}{20}>3-\sigma_0+2\ell+m+2\epsilon,
\tag{18}
\]

then choose \(A_0,A_2,N\) so that the other two exponents in (17) exceed the right side of (18). This gives the sufficient high-side estimate

\[
|\mathbb E_J\mathscr R^{\star}_{\ne1}(Z)|/|A_T(Z)|
\ll Z^{C(\sigma_0)-m}.
\tag{19}
\]

For the source geometry \(\ell=1/6\), it is enough to take \(\lambda>20(3-\sigma_0+1/3+m+2\epsilon)\), before choosing the row and height cutoffs. The prime slots remain on their original \(Z^{\ell_i}\) scales; the auxiliary primes are only polylogarithmic in \(Z\).

The nonprincipal rows have deliberately stayed on the original \(x=3\) line. This is why (19) is compatible with an arbitrary comparison line \(\sigma_0>1/2\) without asserting any zero-free region for \(L(x,\overline{\chi_u})\) below (7/8). The selected-prime Q gain (7) is not what proves (19); (13) is.

## 6. Exact remaining gap

1. **Fixed-probe dynamic route.** If the auxiliary average is not used, (8) still leaves \(1/L(x,\overline{\chi_u})\). The finite-order Q input only gives the unconditioned reciprocal bound in a buffered zero-free region to the right of (7/8). A dynamic contour below that line must keep every row's selected zeros and residues under the existing zero-conditioned argument and then prove the all-bin exponent condition following (9). Neither the (P_c^{-1/8}) prime gain nor the local damping factor cancels a pole of (1/L(x,\overline{\chi_u})). Counting zeros alone does not bound the residues (\mathcal H_u(\rho)/L'(\rho)); no lower bound for (L'(\rho)) is available or used here.

2. **Averaged high versus a full contradiction.** Equation (19) is for a new positive average of probes with many different bad sets, not for a single fixed (S_0) probe. A matching low bound for the *whole* averaged observation is not in the reviewed ensemble note: its low transfers cover the complete cubic core and six named nonflat types, not every residue/unit/first-flat sector. The corrected moving-hole phase from `c191be4` must remain in any physical low expansion; the unrestricted high average cannot be conditioned on the resulting finite ray option.

3. **Principal signal.** At (u=1), the exact ensemble multiplier is \(\Phi_R(s)=1+O((\log R)^{-31}/\log\log R)\) on the stated critical box. This logarithmic estimate is not a power error to a fixed signal. The separate varying-principal-series calculation is recorded in the private [AVERAGED_PRINCIPAL_CONTRACTION.md](AVERAGED_PRINCIPAL_CONTRACTION.md); its contraction is conditional on a genuinely safe signal line and on the stated error budget. In the normalization \(C(s)=s-c_{\rm exp}\), if transfer from a safe line \(\sigma_{\rm safe}\) to the signal contributes error \(O(Z^{\sigma_{\rm safe}-c_{\rm exp}-m_0})\), the resulting exponent is \(\sigma_{\rm safe}-m_0\). If the separate low estimate contributes exponent \(\sigma_{\rm low}\), the total transfer exponent is \(\max(\sigma_{\rm low},\sigma_{\rm safe}-m_0)\), so both terms must fit at the target \(\sigma_*\). In particular, the safe-line term contracts only when
\[
\sigma_{\rm safe}-m_0\le \sigma_*.
\]
For example, conditional descent from a putative exponent \(\beta_*>1/2\) is arithmetically possible if \(\sigma_{\rm safe}=\beta_*+\epsilon<1\) is independently proved safe and \(\epsilon<m_0<\beta_*-1/2+\epsilon\): then \(\sigma_{\rm new}=\sigma_{\rm safe}-m_0\in(1/2,\beta_*)\). A matching averaged low bound at this new exponent would still be needed to obtain the contradiction. The principal-series note does not prove that low bound or establish the safe line. The fixed-data safe-line comparison in Section 9 of `HALF_DAMPED_PROBE.md` does not by itself give the ensemble version. No “safe \(\zeta\)-line” is inferred from damping.

The no-go results added at `c191be4` and `ba52377` concern a different spectral comparison that diagonally majorizes the signed (n=2) prime shift. They do not contradict (17), which averages exact auxiliary Euler deletions on the unchanged high identity; they also do not establish the missing averaged low bound.

## Source checks

- `reports/20261011_qrh_selection_bridge/HALF_DAMPED_PROBE.md`, Sections 2, 6, 8, 9 (origin `ba52377`): exact local half-damped factorization, enlarged correction domain, original/core holomorphic markers, conditional dynamic error allocation, and principal-only safe-line comparison.
- `reports/20261011_qrh_selection_bridge/EXCLUSIVE_S_UNIT_PROBE.md` at `5615d29`: physical (p\nmid s) definition, exact (k=0) local table, dynamic line and retained reflected-numerator hypothesis.
- `reports/20261011_qrh_selection_bridge/POLYNOMIAL_AUXILIARY_ENSEMBLE.md` at `7fade07`, Part A Sections 1--8: actual no-replacement ensemble, all removed local Euler factors, logarithmic-height finite-order Q input, and explicit exceptions/scopes for the low transfers.
- `GENERAL_SELECTED_Q_GAIN.md` at `113702d`: factorized finite-order prime gain (P_c^{-1/8+\rho}), its conductor/hole/height losses, and its explicit limit.
- `reports/20261012_diagonal_prime_threshold_no_go/REPORT.md` at `c191be4` and `WEIGHTED_YOUNG_NO_GO.md` at `ba52377`: threshold-mode obstruction to weighted diagonal prime-shift comparisons only.
- Fixed arithmetic source checked for the original row identity and local tables: `openai/math` commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.

Independent verification is [REFEREE_AVERAGED_NONPRINCIPAL_HIGH.md](REFEREE_AVERAGED_NONPRINCIPAL_HIGH.md). The exact principal comparison and conditional abscissa descent are [AVERAGED_PRINCIPAL_CONTRACTION.md](AVERAGED_PRINCIPAL_CONTRACTION.md) and [PRINCIPAL_ABSCISSA_DESCENT.md](PRINCIPAL_ABSCISSA_DESCENT.md).
