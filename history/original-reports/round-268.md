## Round 268 — Connes 2026 finite-prime approximation: the explicit convergence gap remains open

Source audited: Alain Connes, *The Riemann Hypothesis*, arXiv:2602.04022,
version downloaded 2026-08-29, SHA-256
`9b7a5cdd2d39453360f2899a4681ddb2862e9be51a1a89746a11674acbeb7eea`.

The paper's finite-prime construction does contain a precise conditional/local
statement. For a cutoff \(x\), it forms a Weil quadratic form from the finite
prime powers below \(x\); under the stated lower-bounded self-adjointness and
simple isolated even-minimum hypotheses, Theorem 6.1 gives that the Fourier
transform of the minimizing vector has all its zeros on the real line. The
paper also states a separate convergence fact for the explicitly constructed
prolate approximation \(k_\lambda\): its Fourier transform tends to Riemann's
\(\Xi\)-function on compact substrips as \(\lambda\to\infty\).

Those facts do not identify the finite minimizer with the prolate approximation,
nor do they prove the limiting spectral hypotheses needed for the actual Weil
quadratic forms. The paper states this explicitly in the letter (pp. 24--25):
when the prime cutoff is increased, convergence of the approximating zero sets
to the zeta zeros is “not proved.” Section 6.6 repeats the two missing
load-bearing assertions: simplicity of the smallest eigenvalue of the Weil
quadratic form with an even eigenvector, and a sufficiently strong approximation
of the true eigenvector \(\theta_x\) by \(k_\lambda\), \(\lambda=\sqrt{x}\).
Section 6.4 also records that positivity of the restricted Weil form for all
\(\lambda>1\) is itself equivalent to RH; the numerically tiny eigenvalues of
the constructed approximants do not prove that positivity.

Consequently no finite-prime accuracy, finite-line zero reality, or stated
compact convergence result supplies the missing implication

\[
\text{finite Weil minimizers with real-line zeros}
Longrightarrow
\text{all nontrivial zeros of }\zeta\text{ lie on }\Re s=\tfrac12.
\]

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}

本步没有产生新的无条件 RH 证明进展。
