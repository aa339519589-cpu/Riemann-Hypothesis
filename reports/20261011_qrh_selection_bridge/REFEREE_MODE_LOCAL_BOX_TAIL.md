# Independent audit of [MODE_LOCAL_BOX_TAIL.md](MODE_LOCAL_BOX_TAIL.md)

## Verdict

The supplement closes the specific common-box and pooled high-Mellin-tail gap raised in the earlier mode-window review, conditional on the separately reviewed local reciprocal-\( L \) rectangle estimate and the original detector's common-weight / full-column bounds. I found no exponent or mode-count error in the stated (79/125) application. It does not prove those inherited analytic inputs anew, nor make a claim for arbitrary row-dependent Fourier weights.

The audit compared the supplement with Part XXXI A–C of [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md) at commit `cdf5271`.

## Checks

The full retained range lies in the shifted-height domain. With \(\eta=7/500\), \(\tau_0=1/500\), and \(\zeta\le1/100000\), for (M\ge2) and (T\le M^{\tau_0}),

\[
H_F\le 3M^{\eta+\tau_0}=3M^{2/125},\qquad
L\le2M^{\zeta+\tau_0}\le2M^{201/100000}.
\]

Thus every retained center and local-box point is bounded by a fixed constant times (M^{2/125}); the gap to (M^{1/50}) is exactly (1/250), enough to absorb fixed \(\omega,C_0,K\) constants for sufficiently large (M). Bounded (M) is absorbed in the implied constant. This controls every (j) in the finite Fejér range, not a sampled subset. At \(\alpha_0=47/300\), the source function gives \(p_2=611/4429\), which lies in \((0,1)\); a sufficiently small fixed compact interval therefore supplies common positive lower and upper bounds for \(p_2\).

Covering the bad-mode interval centered at \(-\nu_j\) costs (O(M^\zeta(1+T))). The height factor contributes at most another (M^{\zeta p_2}(1+T)^{p_2}(1+|j|)^{p_2}), so the displayed (M^{2\zeta}) row-count cost is valid since (p_2<1). With \(|c_j|\ll(1+|j|)^{-1}\), the sum is \(\ll H_F^{3p_2/8+\epsilon}\), uniformly on the compact interval because (p_2) has a positive minimum. Raising the row-count bound to the (3/8) Holder factor turns (2\zeta) into (3\zeta/4), as in Part XXXI B (10).

The Mellin formula and sign are consistent with the convention

\[
\widehat W(s)=\int_0^\infty W(x)x^{s-1}\,dx,
\qquad W(x)=\frac1{2\pi i}\int \widehat W(s)x^{-s}\,ds.
\]

Substitution of (x=N\mathfrak d/D) gives the argument \(\rho-i\nu_j-iu+s\) and the summand \((N\mathfrak d)^{-\rho+i\nu_j+iu}\). On \(\Re s=c_\beta=1+\delta_{\rm abs}-\beta\), the (L^S) argument has real part (1+\delta_{\rm abs}). For the incomplete Euler product,

\[
\left|\frac1{L^S(1+\delta_{\rm abs}+it,\chi)}\right|
\le\prod_{\mathfrak p\notin S}(1+(N\mathfrak p)^{-1-\delta_{\rm abs}})
\le\zeta_K(1+\delta_{\rm abs}),
\]

uniformly in (t,\chi,S). The Mellin transform is independent of (j) and (u); those variables shift only the (L)-argument. Hence the original-line estimate has no \((1+|j|)^N\) derivative loss. The horizontal joins have real part of the (L)-argument at least (b+2h), and imaginary displacement at most \((K+1)L\) from \(\gamma_i-\nu_j\). Choosing \(C_0>K+3\) keeps both joins and the new vertical segment inside the good-row zero-free rectangle. The source's buffered reciprocal estimate is stated on that rectangle, so it covers the joins; it is stronger than a bound only on the central vertical line. The fixed deleted Euler factors have no zeros there.

For \(|v|>L\), uniform integration by parts gives \(|\widehat W(c_\beta+iv)|\ll_N(1+|v|)^{-N}\). Since (D\ge1), (D\le M^{x_{\max}}), and \(\beta\ge b_{\min}\), the original-line tail is bounded by

\[
C_N M^{x_{\max}(1+\delta_{\rm abs}-b_{\min})}L^{1-N}.
\]

The horizontal joins have the same arbitrary (M)-power decay after paying their fixed contour length and the inherited reciprocal-L small conductor-height power. Choosing (N) after \(\zeta\) absorbs any fixed polynomial (M)-cost from restoring the actual detector columns. (N)'s seminorm-dependent height degree is kept as \((1+T)^{B_N}\), rather than converted to an (M)-power using the temporary range for (T).

The restoration and pooling order in the supplement is sound under the stated detector input. For example, the absolute (d)-column is bounded by a fixed power of (X\le M^{x_{\max}}); the reflected (m)-column tail is summable uniformly for \(\beta\le b_{\max}<1\), since

\[
\sum_m (Nm)^{\beta-1}\min(1,K_0/Nm)\ll (1+K_0)^{b_{\max}+1}
\]

is a fixed polynomial bound (and the sharper \(\ll(1+K_0)^{b_{\max}}\) also follows by splitting at (K_0)). The original gamma-height dependence remains polynomial in (1+T), with the relative-height Gamma decay retained. Thus a fixed polynomial (M^B(1+T)^{C_B}), uniform in (j), is available before pooling. With the actual row masks retained,

\[
\sum_i\left|\sum_jc_jE_{i,j}\right|^r
\ll M^{1-rA+\epsilon}(1+T)^{rC_A+\epsilon},\qquad r\ge1,
\]

after using \(\sum_j|c_j|\ll\log(2H_F)\). Choose (A) after the restoration cost (B) and the finite derivative orders are fixed; Markov then leaves a negative (M)-power. The final (T)-degree is selected last, so no circular substitution (T\le M^{1/500}) is needed for tail smallness.

## Exact clarifications to make

1. In the displayed Mellin identity, make the presentation-hole mask explicit: either write \(\mathbf1_{(\mathfrak d,S)=1}\) in the sum, or state that the imprimitive character is extended by zero on every deleted prime. Without that convention, the coefficient series is (1/L) for the full Euler product rather than (1/L^S). With the source's genuine-hole convention, the bound above is uniform in the deleted set.
2. Replace “fixed finite dyad counts” by “the finite number of separated columns and the (O((\log M)^C)) dyadic pieces.” The latter polylogarithmic cost is absorbed by (M^\epsilon); it need not be treated as a uniformly bounded count.
3. Keep the conditional scope explicit: the common norm-weight seminorms and the (M^B(1+T)^{C_B}) detector restoration must be uniform in every row/physical tuple before tuple or dyad pooling. The supplement states this as an inherited input and excludes arbitrary row-dependent weights; under that input no uncontrolled Fourier seminorm family remains. If that common-family bound is not available from the separately reviewed detector, the tail estimate does not certify such a family.

These are convention/scope clarifications, not changes to the rational ledger. Subject to them and the separately reviewed analytic inputs, I accept the supplement as closing the mode-box and pooled-tail accounting objection from referee 14.

The exact all-mode height slack and center value of (p_2) are also checked with the standard-library `Fraction` script [check_mode_local_boxes.py](check_mode_local_boxes.py); it reports `PASS`.

The published supplement incorporates clarifications 1--2 above and preserves the conditional common-family scope of clarification 3. These changes do not strengthen the audited analytic claims.
