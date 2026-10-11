## Round 252 — A/B result: Ip's self-adjoint-operator manuscript assumes the spectral correspondence and is internally inconsistent

Source audited: Lawrence Ip, *Proof of the Riemann Hypothesis via a Self-Adjoint Operator*, Zenodo version v5,
[record 15334802](https://zenodo.org/records/15334802), PDF dated 2025-05-04, SHA-256
936f5db867fb18b5af90f54f2497095981d8684d025ccecf4cf8294a88a5da67.
The record itself now describes the document as an architectural proof with several
central correspondences still open, but the PDF was independently checked.

First, the claimed arithmetic independence is contradicted by the definition of
the operator. Theorem 7.1 (PDF p. 10) uses
\[
R(x)=\sum_{\gamma>0}\left(\frac{b_\gamma}{x^{2+i\gamma}}+
\frac{\overline b_\gamma}{x^{2-i\gamma}}\right),
\qquad b_\gamma=\frac{1}{2(\frac12+i\gamma)},
\]
and says that \(\gamma\) ranges over the imaginary parts of the zeros
without assuming their real parts. But the same theorem and Appendix I
(PDF pp. 10 and 27) represent the zeros as \(\rho=\frac12+i\gamma\).
An off-critical zero \(\beta+i\gamma\) is not represented by this formula;
its real part has been replaced by \(\frac12\) before the operator is built.
Thus the claimed self-adjoint operator cannot independently force the omitted
real parts to equal \(\frac12\); the critical-line coordinate is already
built into the input.

Second, the operator claims are mutually incompatible. On \(L^2(\mathbb R)\),
Section 3.1 says that the real potential \(V\) is smooth and decays at
infinity, while Theorem 7.1 claims that the resulting Schrödinger operator
has a purely discrete simple spectrum. Even granting the manuscript's own
bounded-decay assertion, \(-d^2/dx^2+V\) is a relatively compact perturbation
of the free Laplacian and has essential spectrum \([0,\infty)\), not a
purely discrete spectrum. A confining potential could change this conclusion,
but the manuscript neither supplies one nor reconciles it with its decay
claim. The later switch to a half-line inverse-square expression does not
define an equivalent whole-line operator or a valid unitary bridge.

Third, the asserted spectral completeness is circular and too weak for the
conclusion. Theorem 4.1 defines
\(N_\zeta(T)\) by counting zeros written as
\(\rho_n=\frac12+i\lambda_n\), which already restricts the counted zeros
to the critical line. Moreover, an estimate
\(N_O(T)=N_\zeta(T)+O(\log T)\) is only an asymptotic count; it does not
produce an exact zero--eigenvalue bijection or exclude unmatched zeros.
Theorem 4.2 then defines the map \(\lambda\mapsto\frac12+i\lambda\);
self-adjointness makes \(\lambda\) real, but that definition cannot prove
that every zero of \(\zeta\) has that form.

Fourth, Lemma 16.1's convergence proof contains a direct false step. The
PDF p. 28 states that \(\lvert b_{\gamma_n}\rvert=O(1/\gamma_n)\), then
claims that \(\sum_n1/\gamma_n\) converges conditionally and therefore
that the displayed series converges absolutely. Since \(\gamma_n>0\),
\(\sum_n1/\gamma_n\) has positive terms and cannot converge conditionally;
the Riemann--von Mangoldt growth also gives
\(\gamma_n\sim 2\pi n/\log n\) at the scale relevant here, so this
reciprocal sum diverges. Oscillation of the paired factors could at most
support a separate conditional-convergence argument; it does not imply
absolute or uniform convergence. Consequently the claimed regularity of
\(R\) and the operator potential is not proved.

Finally, the trace identity is not derived: the manuscript writes
\(\operatorname{Tr}(e^{-tO})=\sum_ne^{-t\lambda_n^2}\), although an
eigenvalue \(\lambda_n\) of \(O\) contributes \(e^{-t\lambda_n}\),
not \(e^{-t\lambda_n^2}\). An identity for \(e^{-tO^2}\) would be a
different assertion and requires a separate trace-class and heat-kernel
proof. The subsequent equality to the zeta zero density is therefore
not established.

These independent failures occur before any claimed exclusion of off-critical
zeros. The self-adjointness of a proposed operator cannot supply the missing
arithmetic determinant/bijection, and the final RH conclusion does not follow.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
