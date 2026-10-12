# Independent audit of [COMPACT_CUBIC_DUAL.md](COMPACT_CUBIC_DUAL.md)

## Verdict

The compact-block deconvolution, reflection, and absolute-convergence argument is correct for each fixed squarefree row, conditional on the cited Part XXVII B identities and the fixed compact-test seminorm bounds. The exact interfaces are retained: the row-dependent presentation holes are incorporated into (L^\star), the local calculation uses the full cusp denominator (c_{\rm cusp}=\mathfrak c_r u), and the three-cusp coefficient (b^\star) is explicitly only a reference combination, not a replacement for the actual (h_0)-cusp coefficients.

I leave the additional identity \(\Gamma_r(u)=\overline{G(u)}\,\overline{\rho_u(\mathfrak c_r)}\) and the resulting “restored” root Möbius sign conditional on the separate accepted [moving-phase review](REFEREE_CUBIC_MOVING_ROOT_PHASE.md); I do not independently certify them. The bare Möbius quotient in (18) is correct and, by itself, has no \(\mu_K(c^\circ)\) factor. This report establishes no estimate for the pooled signed column.

## Identity and sign checks

The finite coefficient inversion is consistent with Part XXVII B (12). Solving

\[
D_u(s)=3^{5/2+3s}R_u(s)L_{\rm del}(3s-1/2,\chi_0^3)
\]

for (R_u) and expanding (1/L_{\rm del}) in its absolute region gives the inverse coefficient \(\mu_K(\ell)\chi_0^3(\ell)(N\ell)^{1/2-3s}\), with \(\ell\) coprime to the complete deleted set. Combining \(3^{-3s}=27^{-s}\) with \((N\ell)^{-3s}\) gives the physical norm \(27N\nu(N\ell)^3\). The test coefficient contributes its reciprocal square root, exactly as in (2). Since \(\nu\in\lambda^{-3}\Omega\) implies \(N\nu\ge1/27\), support in \(x\le CM\) forces \(N\ell\le(CM)^{1/3}\); for each retained \(\ell\), it also bounds \(N\nu\). Thus this is a finite coefficient comparison on the compact physical block, before reflection, with no illegal inverse-Euler expansion on the reflected line.

The Mellin convention in (3) has the correct sign. From \(\widetilde g(s)=\int g(x)x^s\,dx/x\), inversion uses \(x^{-s}\), so pairing with \(\sum d_0(\nu)(N\nu)^{-s}\) yields the original (g(N\nu)). Direct substitution gives

\[
\widetilde g_{\ell,M}(s)=M^{-1/2}\left(\frac{M}{27(N\ell)^3}\right)^s\widehat W_M(s),
\qquad \widehat W_M(s)=\int W_M(y)y^{s-1/2}\,\frac{dy}{y},
\]

as stated. In (12), multiplying this by \((N\mathfrak c_r)^{1-2s}U^{1/2-2s}(N\nu)^{-(1-s)}\) gives the outside factors \(M^{-1/2}N\mathfrak c_r U^{1/2}\), the \((N\nu)^{-1}\) coefficient, and the kernel ratio

\[
x=\frac{M N\nu}{27(N\ell)^3(N\mathfrak c_r)^2U^2}.
\]

All powers in (12) follow. The frequency center (13) and the reindexed center (14) retain the cusp denominator squared, (U^2), ((N\ell)^3), and the divisor norm (NR); they are correct.

The source reflection has the undifferentiated radial quotient with numerator gamma factors \(\Gamma(5/6-s)\Gamma(7/6-s)\) and denominator \(\Gamma(s-1/6)\Gamma(s+1/6)\). The first pole to the right is (s=5/6); the next is (7/6). At (5/6), the residue is

\[
-(2\pi)^{4/3}\frac{\Gamma(1/3)}{\Gamma(2/3)}.
\]

Shifting the kernel contour right gives the negative of that residue in the leading term, hence the positive coefficient in (17). Shifting left for (x\to\infty) crosses no poles and gives arbitrary power decay. This uses the radial source kernel only; the note correctly distinguishes it from the differentiated angular kernel and its different pole.

## Convergence, masks, and period costs

On \(\Re s=\sigma_L<0\), \(\Re(1-s)>1\), so the reflected (E_{h_0,u}(1-s)) series is absolutely convergent. The displayed majorant (15) controls the undifferentiated series; its phases have modulus one. The finite divisor expansion of (c_u) may therefore be opened. The tail bound (16) follows by applying the majorant at (1+h/2) and summing \(\sum_{R\mid u}NR\); keeping (c_u) grouped gives the stated sharper bound. Rapid vertical decay of \(\widehat W_M\) dominates the polynomial growth of (A_{\rm rad}), so the Mellin integral and the shifted contour are absolutely justified. The \(\ell\)-range is finite for each block but grows with (M), as the note says.

The new mask period is handled correctly at the rowwise level. The extra mask contains exactly the primes of (eB) outside (6L_0u); the primes omitted from that product are already zero by the stated primary, presentation, or moving-character masks. Thus the primal row mask is represented by \(\chi_0^\star\overline{\rho_u}\). Since the new primes avoid (6L_0u), (L^\star=L_0\varpi_{e,B;u}) retains 2-part (4), and (u) remains coprime to the period. The inverse Euler factor in (1) and the finite \(\ell\)-sum in (2) include the presentation primes of \(\chi_0^\star\), the primes dividing (u), and \(\lambda\). There is no uncovered common-hole factor under the source-mask convention stated in the note.

The period-dependent estimates use (NL^\star): normalized Parseval gives \(\sum_{h_0}|\widehat\Phi_{0,L^\star}(h_0)|\le\sqrt{NL^\star}\), the fixed cusp denominator obeys \(N\mathfrak c_r\le NL^\star\), and the reflected left-line estimate carries the displayed power of (NL^\star). The text also says there is no uniformity in (eB); these rowwise costs must not be treated as a globally fixed period or silently pooled. The identity itself is valid for each fixed row.

The cusp data are carefully separated: reflection uses the source's fixed cusp denominator \(\mathfrak c_r\), while the moving-prime \(\sigma_{p,r}\) and \(\epsilon_p\) use \(\mathfrak c_r u\). Equation (10) is the finite additive-character sum after \(\chi_p(h_p)^{-4}\chi_p(h_p)^{-2}=1\), and (11) is its exact Ramanujan divisor expansion. The unit correction for a non-primary stored associate is explicitly retained. The (b^\star) formulas match the source's conjugation and minus-frequency convention; the note then correctly states that each (h_0) term instead uses its own source coefficient and phase. The source's (5.73)–(5.74) support split agrees with the displayed reference formula [in DR](https://arxiv.org/html/2109.07463v3).

Finally, the arithmetic identity (18) is correct under the stated squarefree, pairwise-coprime factorization:

\[
\frac{\mu_K(c)}{Nc}\,\mu_K(ch/R)NR
=\frac{\mu_K(R_c)\mu_K(h^\circ)NR_h}{Nc^\circ}.
\]

The bare quotient cancels \(\mu_K(c^\circ)^2\) and leaves no \(\mu_K(c^\circ)\). The subsequent restoration of that sign relies on the scalar identity for \(\Gamma_r(u)\); I leave this factorization and sign restoration conditional on the separate accepted [moving-phase review](REFEREE_CUBIC_MOVING_ROOT_PHASE.md), without claiming to have independently reviewed it. The note’s no-Mertens conclusion remains valid because the other cusp, root, support, and test factors still couple the variables.

With the scalar step conditional on that separate review, I accept the compact finite-block identity and its rowwise convergence claims. No pooled signed-column estimate follows.
