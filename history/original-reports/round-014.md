## Round 14 — the Krein–Rutman compactness claim fails in the continuum

I audited a newer proposed route that tries to prove the first missing spectral
hypothesis by applying Krein–Rutman to the prime part

\[
P_\lambda=\sum_{1<n\leq\lambda^2}\Lambda(n)n^{-1/2}T(n).
\]

The positivity statement is elementary: each summand is a positive weighted
sum of two multiplicative translations, so a nonnegative input remains
nonnegative. The required compactness statement is false.

Put \(x=\log u\), \(I=(-\log\lambda,\log\lambda)\), and write

\[
(S_bf)(x)=\mathbf 1_I(x)f(x+b).
\]

After this unitary change of variables, \(P_\lambda\) is a finite sum of
operators \(S_{\pm\log n}\) with positive nonzero coefficients. For
\(\lambda>\sqrt2\), choose a nonempty interval \(J\subset I\) so small that
\(J+\log2\subset I\), and so small that the translated intervals
\(J-b\), for the finitely many distinct shifts \(b=\pm\log n\), are pairwise
disjoint whenever they are nonempty. Define

\[
f_k=|J|^{-1/2}\mathbf 1_J(x)e^{ikx}.
\]

Choosing integer frequencies along an orthogonal subsequence gives
\(f_k\rightharpoonup0\) in \(L^2(I)\). But the output pieces of \(P_\lambda f_k\)
have disjoint supports, and the \(n=2\) piece alone gives

\[
\|P_\lambda f_k\|_2^2\geq
\left(\frac{\Lambda(2)}{\sqrt2}\right)^2\|f_k\|_2^2
=\left(\frac{\log2}{\sqrt2}\right)^2.
\]

Thus \(P_\lambda f_k\not\to0\) although \(f_k\rightharpoonup0\); hence
\(P_\lambda\) is not compact. Equivalently, its distribution kernel is a
finite sum of delta graphs, not an \(L^2\) kernel. “Finite sum of shifts” is
finite-term, not finite-rank.

This directly invalidates the proposed Krein–Rutman inference. Positivity of a
bounded noncompact operator does not give a simple maximal eigenvalue, and a
near-rank-one singular-value picture from a discretized grid is not a continuum
theorem. The actual semilocal Weil operator can still have discrete spectrum
because its archimedean part is unbounded; that is a different fact and does not
restore a Perron–Frobenius argument for \(P_\lambda\).

The proposed route therefore does not prove either global simplicity or
evenness of the lowest eigenvector. It also does not address the separate
ground-state identification and uniform convergence needed for the Hurwitz
step.

### Round 14 status

**Established:** the prime operator is positivity-preserving but, for every
large enough window, rigorously noncompact; the Krein–Rutman compactness premise
is unavailable.

**Not established:** simplicity/evenness of the actual lowest semilocal Weil
eigenvector for all scales, its identification with the prolate candidate, and
therefore an unconditional RH proof.
