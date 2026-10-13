# Independent stress review: exact-Q Green load at subprincipal order

**Date:** 2026-10-13  
**Scope:** Independent check of [GREEN_LOAD.md](GREEN_LOAD.md) against the [projected frame](PROJECTED_FRAME.md), the [full-tail trial](../20261013_growing_theta_trial/LAGUERRE_SCHUR_TRIAL.md) interfaces, and the collar subprincipal/resolvent identities. Review is conditional on those stated inputs and on (M_k\ge0) at the endpoints in question.

## Verdict

| Item | Verdict |
|---|---|
| Exact-Q projected source trial and use of the full-tail null witness | **PASS**, with the stated growing-frame/tail hypotheses |
| Unit-cell (C^1) limit, negative normalization, and operator-graph continuity under (C) | **PASS** |
| High-frequency lower bound for the cell form using (h=1) and bounded (e_1) | **PASS** |
| Fixed-profile and subsequent endpoint-limit quantifiers and the liminf conclusion | **PASS** |
| Green-dual test sign, extended-(+\infty) case, and interpretation of the short | **PASS** |
| Scope: baseline-ratio obstruction only; no actual Schur sign or RH | **PASS** |

The claimed conclusion is valid under (M_k\ge0) on an unbounded set of endpoints and the cited exact-Q projected-frame theorem and [full-tail trial](../20261013_growing_theta_trial/LAGUERRE_SCHUR_TRIAL.md) estimates. It yields
\(\liminf L(\eta_k^Q-1)=+\infty\) along every such qualifying sequence. It does **not** show that the actual new-collar Schur short is negative (or positive), nor that (\eta_k^Q\to\infty\).

## 1. Exact-Q trial interface and the full-tail (o(1)) energy

For each (k), the projected frame construction gives finite coefficients and an uncut combination
\[
F_k=\sum_{\ell<m}a_{\ell,k}\left(f_{d+\ell}-\sum_{i<d}p_{i,d+\ell,k}f_i\right)
\]
whose cutoff (v_k=\chi_kF_k/\sigma_k\) lies in (Q_k) **exactly**. Every coefficient is a scalar constant in (x) at that (k). Thus (F_k) remains a finite combination of exact odd theta-source nulls and is polar-neutral; no uniform bound on the raw old-window norm is needed for the Green supremum. Each (v_k) is in the old form domain because it is smooth and compactly supported in the old window.

To match the tail full-tail trial hypothesis, choose (P_{m(k)}) to be the Laguerre approximant of the fixed (W\in C_c^\infty(0,\pi)), extended by zero. Its weighted (H^1_{24}) norm stays bounded and its value/derivative residuals satisfy
\[
\epsilon_{0,k}=O(m(k)^{-r}+k^{-1+o(1)}),\qquad
\epsilon_{1,k}=O(m(k)^{1-r}+k^{-1+o(1)})
\]
for any fixed (r>2). Indeed, projected-frame theorem adds the relative profile error
\(k^{-1}\exp(C_{d,24}m^2\log(m+2))=k^{-1+o(1)}\) for
\(m=\lfloor(\log k)^{1/4}\rfloor\). The projected-frame theorem pointwise envelope has coefficient (\exp(Cm^2\log(m+2))=k^{o(1)}) and polynomial degree (O(m+d)); after multiplying by the theta amplitude, the extra polynomial is absorbed into a fixed exponential (e^{-(1-c)s_+}) at a cost (e^{O(m\log(m+2))}\), still (k^{o(1)}). The transition derivative is also controlled: (d\chi_k/ds=(d\chi_k/dx)(dx/ds)=O(k)O(k^{-1})=O(1)). Thus the actual projected profile satisfies the full-tail residual and envelope requirements, rather than relying on weighted (L^2/H^1) alone for the prime estimate.

With (m(k)=\lfloor(\log k)^{1/4}\rfloor),
\((\log k)\epsilon_{0,k}^2\to0\) and \(\epsilon_{1,k}^2\to0\) when (r>2). The tail envelope factor is (k^{o(1)}), so its complete signed prime contribution, including every prime power, is bounded by
\(k^{o(1)}(e^{-c k}+\log k/\sqrt{k})=o(1)\); its polar debit is (k^{o(1)}k^{-1/2}=o(1)). The Gamma residual estimate is also (o(1)). This verifies that the full-tail theorem applies to the exact-Q projected combination. Since its uncut source is null, the cutoff/tail pairing identity gives the actual finite-window trial
\[
\mathfrak A_{a_{k+1}}[v_k+y_k]=\epsilon_k(W)\longrightarrow0.
\]
The argument uses the growing-(m(k)) frame bound; it does not substitute a fixed-jet limit for this step.

## 2. Green-dual test, sign, and the infinite case

For a Q vector (v_k\) in the form domain, the exact block form reads
\[
\epsilon_k(W)=\mathfrak m_k[v_k]+2\operatorname{Re}\langle v_k,Y_ky_k\rangle+D_k[y_k].
\]
Testing the positive-form Green dual at (-v_k) gives
\[
G_k(y_k)\ge-2\operatorname{Re}\langle v_k,Y_ky_k\rangle-\mathfrak m_k[v_k]
              =D_k[y_k]-\epsilon_k(W).
\]
The minus sign is correct: the trial is (-v_k), while the block cross term in the finite-window energy is (+2\operatorname{Re}\langle v_k,Y_ky_k\rangle). No inverse or positive spectral gap is invoked. The statement needs only (M_k\ge0) to interpret the Green functional as the nonnegative extended supremum. If (G_k(y_k)=+\infty), the same inequality holds in the extended-real sense and the beta-zero quotient is (+\infty); the subsequent lower bounds remain valid.

For the explicitly defined standalone quotient, the denominator is exactly (L\|y_k\|_2^2). Therefore
\[
L(\eta_k^Q-1)\ge
\frac{D_k[y_k]-L\|y_k\|_2^2-\epsilon_k(W)}{\|y_k\|_2^2}.
\]
This algebra is the needed comparison; it is an inequality for the baseline quotient and says nothing about the sign of (D_k[y_k]-G_k(y_k)).

## 3. Collar unit-cell limit and continuity in the operator graph of (C)

For the physical collar vector
\(y_k(x)=\sigma_k^{-1}f_0(x)W(\pi e^{2x}-\pi k)\) on the positive wing and its odd reflection, its unit-cell representative is
\[
g_k(u)=\sqrt{2h_k}\,y_k(a_k+h_ku),\qquad 0\le u\le1.
\]
Here
\[
\pi k(e^{2h_ku}-1)=\pi u+O_{C^1}(k^{-1}),
\qquad
\sqrt{2h_k}\frac{f_0(a_k+h_ku)}{\sigma_k}
=-\sqrt{2\pi}\,e^{-\pi u}+O_{C^1}(k^{-1}),
\]
using (e^{2h_k}=1+1/k), (h_k\sim1/(2k)), and the first theta term
\(\mathcal F_0(u)=-32u^5(1+O(u^{-1}))\), which is negative on this tail. The omitted theta frequencies and their first derivatives are exponentially smaller. Because (W) is smooth with compact support strictly inside ((0,\pi)), composition and multiplication give convergence on the whole cell in (C^1([0,1])):
\[
g_k\longrightarrow g_W(u)=-\sqrt{2\pi}e^{-\pi u}W(\pi u).
\]
The negative normalization sign is therefore correct. The support of (g_W) is compactly contained in ((0,1)), and for (W\ne0),
\[
n_W=\|g_W\|_2^2=2\int_0^\pi |W(s)|^2e^{-2s}\,ds>0.
\]
The unitary collar map makes (|y_k|_2^2=\|g_k\|_2^2\to n_W\), with both wings already accounted for.

The cell-domain lemma in the resolvent note gives, for every (g\in C^1([0,1])),
\[
Cg=Jg+Vg-(\gamma+\log\pi)g\in L^2,
\quad
\|Cg\|_2\le\tfrac12\|g'\|_\infty+\|V\|_2\|g\|_\infty
   +|\gamma+\log\pi|\|g\|_2.
\]
Applying this bound to (g_k-g_W\) proves convergence in the **operator graph norm** of (C), not only in the cell form norm. Hence
\(\langle g_k,Cg_k\rangle\to\langle g_W,Cg_W\rangle\). From the exact reconstruction
\(D_k=L I+C+R_k\), (\|R_k\|=O(k^{-1/2})), and boundedness of (g_k),
\[
D_k[y_k]-L\|y_k\|_2^2
=\langle g_k,Cg_k\rangle+\langle g_k,R_kg_k\rangle
\longrightarrow\langle g_W,Cg_W\rangle.
\]
This proves the constant-order input (5).

## 4. High-frequency cell profiles: (h=1), bounded (e_1), and the lower bound

For \(\phi\in C_c^\infty(0,1)\setminus\{0\}\), set
\(\phi_N(u)=e^{iNu}\phi(u)\). The symbol series has a direct monotone-integral lower bound. With (y=t/2),
\[
f_y(x)=\frac{y^2}{x(x^2+y^2)}
\]
is decreasing for (x>0), so
\[
b(t)=\sum_{j\ge0}f_y(j+\tfrac14)
\ge\int_{1/4}^{\infty}f_y(x)\,dx
=\tfrac12\log(1+16y^2)=\tfrac12\log(1+4t^2).
\]
On the Fourier band where the shifted variable has modulus at most (N/2), the multiplier variable has modulus at least (N/2), hence (b(t)\ge\log N). The omitted Fourier mass of \(\widehat\phi\) is (O_\phi(N^{-2})) by Plancherel and \(\phi\in H^1\). Therefore
\[
\mathfrak g[\phi_N]\ge\log N\bigl(\|\phi\|_2^2-O_\phi(N^{-2})\bigr).
\]
The source single-interval form of physical length (h=1) satisfies, by the exact interval identity,
\[
q_a[\phi_N]=\mathfrak b_{\rm cell}[\phi_N]
-(\gamma+\log(2\pi))\|\phi\|_2^2+e_1[\phi_N].
\]
The global bound 
\(|e_h[g]|\le2C_\rho h\|g\|_2^2\) applies at the endpoint (h=1), so
\(\|e_1\|\le2C_\rho\) on (L^2(0,1)). Since
\(C=B_{\rm cell}-(\gamma+\log\pi)I\), rearranging gives
\[
\frac{\langle\phi_N,C\phi_N\rangle}{\|\phi\|_2^2}
\ge\log N-O_\phi(1).
\]
Thus the right side of (6) is unbounded above on smooth compact profiles. The exact profile map
\[
W_N(s)=-(2\pi)^{-1/2}e^s\phi(s/\pi)e^{iNs/\pi}
\]
satisfies (W_N\in C_c^\infty(0,\pi)\) and (g_{W_N}=\phi_N\), with the minus sign cancelling the negative first-theta normalization.

## 5. Order of quantifiers and what the conclusion means

Fix any unbounded qualifying sequence (k_j\to\infty) with (M_{k_j}\ge0). For each **fixed** nonzero (W\in C_c^\infty(0,\pi)), Sections 1–3 give
\[
\liminf_{j\to\infty}L_j(\eta_{k_j}^Q-1)
\ge\frac{\langle g_W,Cg_W\rangle}{\|g_W\|_2^2}.
\]
Given any finite threshold (A), first choose one fixed (N) large enough that the quotient for (W_N) exceeds (A), using the high-frequency lower bound. Keep this (N) fixed while sending (k_j\to\infty). The constants in the tail and frame estimates may depend on this (W_N), but they are fixed in this limit. Since (A) was arbitrary, the liminf is (+\infty). This argument never uses (N=N(k)) or a uniform-in-(N) frame estimate. It follows that \(\eta_{k_j}^Q>1\) for every sufficiently large qualifying endpoint; it does not follow that \(\eta_{k_j}^Q\to\infty\).

Finally, the Green test gives only
\[
D_k[y_k]-G_k(y_k)\le\epsilon_k(W)=o(1).
\]
If (G_k(y_k)=+\infty), this is the extended value (-\infty\le o(1)); otherwise it is an upper bound which is compatible with a positive short tending to zero. No lower bound for this short is proved. The report correctly treats (8) as a baseline (L\|y\|^2) quotient obstruction and explicitly leaves the true Schur sign, full-window positivity, and RH open.
