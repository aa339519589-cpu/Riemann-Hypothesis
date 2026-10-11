## Round 53 — explicit weighted-range countermodel with boundary correction

The preceding threshold is not merely a technical concern. The coefficient
class appearing in (47.11) can realize a nontrivial finite off-line packet on
an interval, even with the same quadratic weight \(d_n=n^2+\tfrac14\).
This is a model calculation, not a statement about the actual zeta
ordinates, but it rules out a purely functional-analytic range-exclusion
argument.

Take \(I=(-\pi,\pi)\), \(\Gamma_C=\mathbb Z\), and let

\[
 g_E(u)=\sum_{j=1}^{m}c_j e^{-i\eta_j u}
\tag{53.1}
\]

be any finite packet, including packets with non-real exponents. Put
\(D=e^{\pi/2}-e^{-\pi/2}\), and choose \(A,B\) from

\[
 A-B=\frac{g_E(\pi)-g_E(-\pi)}{D},
 \qquad
 A+B=\frac{2\bigl(g_E'(\pi)-g_E'(-\pi)\bigr)}{D}.
\tag{53.2}
\]

For

\[
 h(u)=A e^{u/2}+B e^{-u/2}-g_E(u),
\tag{53.3}
\]

equations (53.2) give
\[
 h(\pi)=h(-\pi),\qquad h'(\pi)=h'(-\pi).
\tag{53.4}
\]

Let \(a_n\) be the Fourier coefficients of \(h\) on \(I\), with convention

\[
 a_n=\frac1{2\pi}\int_{-\pi}^{\pi}h(u)e^{inu}\,du,
 \qquad
 h(u)=\sum_{n\in\mathbb Z}a_n e^{-inu}.
\tag{53.5}
\]

The endpoint equalities in (53.4) make the first two integration-by-parts
boundary terms vanish. A third integration, using that \(h'''\) is integrable
on the closed interval, gives

\[
 a_n=O(n^{-3})\quad (|n|\to\infty).
\tag{53.6}
\]

Consequently, with

\[
 w_n=(n^2+\tfrac14)a_n,
 \qquad
 q_n=\frac{w_n}{\sqrt{n^2+\tfrac14}},
\tag{53.7}
\]

one has \(w\in\ell^2(\mathbb Z)\) and \(q\in\ell^2(\mathbb Z)\). The Fourier
series in (53.5) converges absolutely, so (53.3) is an exact pointwise
relation on \(I\):

\[
 \sum_{n\in\mathbb Z}\frac{w_n}{n^2+\tfrac14}e^{-inu}
 =
 A e^{u/2}+B e^{-u/2}-g_E(u).
\tag{53.8}
\]

Thus finite boundary terms plus a finite non-real packet can lie in the
weighted range with precisely the type of \(\ell^2\) coefficient control
used in the zero-collapse branch. The construction is source-independent
and does not use a zeta zero; it therefore cannot disprove RH. Its narrower
conclusion is rigorous: local \(L^2\) range membership, the quadratic
\(d_\gamma\)-weight, smoothness, and a finite boundary correction do not by
themselves exclude the exceptional packet.

For the actual problem, \(\mathbb Z\) must be replaced by the critical
ordinates and the model Fourier coefficients by a zeta-specific synthesis.
That replacement is exactly the unresolved arithmetic range-exclusion
statement; no general density or compactness argument supplies it.

**Established:** the abstract coefficient and boundary structure of the
zero-collapse relation admits an explicit nontrivial model.

**Not established:** that the corresponding relation exists for the actual
critical zeta ordinates, or that it is selected by Bombieri's eigenvectors.

**RH status:** no unconditional proof has been produced.
