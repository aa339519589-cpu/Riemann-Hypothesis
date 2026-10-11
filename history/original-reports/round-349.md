## Round 349 — Velez’s Bochner–Schwartz corollary lacks temperedness

Velez Corollary 7.2 claims that positivity of \(Q_{\rm arith}\) yields a positive
tempered measure representing \(L_{\rm arith}\). But the distribution defined in
Section 4 is not tempered under the stated ordinary translation structure. Let
\(\varphi\ge0\) be a nonzero compactly supported smooth function and translate it
to \(\varphi_R(a)=\varphi(a-R)\), with \(R\to+\infty\). The archimedean term in
Definition 3.2 contributes
\[
2e^{R/2}\int e^{u/2}\varphi(u)\,du+o(e^{R/2}).
\]
By the prime number theorem, the \(k=1\) prime part in Definition 4.1 contributes
\[
-e^{R/2}\int e^{u/2}\varphi(u)\,du+o(e^{R/2}),
\]
while the \(k\ge2\) prime powers and the remaining archimedean kernel are
\(o(e^{R/2})\). Hence
\[
\langle L_{\rm arith},\varphi_R\rangle
\sim e^{R/2}\int e^{u/2}\varphi(u)\,du.
\]
A tempered distribution evaluated on translates of one fixed test function can
grow at most polynomially in \(R\), because its Schwartz seminorms do. Thus the
claimed temperedness is false for the displayed \(L_{\rm arith}\) (unless a
different regularized distribution is defined, which the manuscript does not do).
Bochner–Schwartz therefore cannot be invoked in the stated form. This is separate
from, and does not repair, the missing Proposition 6.1 positivity proof.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
