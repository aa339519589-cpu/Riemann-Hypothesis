## Round 269 — the updated zeta-spectral-triple paper leaves the same two load-bearing steps open

Source audited: Alain Connes, Caterina Consani and Henri Moscovici,
*Zeta Spectral Triples*, [arXiv:2511.22755](https://arxiv.org/abs/2511.22755),
PDF downloaded 2026-08-29, SHA-256
c98d89f7fc999d038e15e80a9aaaee2af797c17711c4329ca7ce48ad49cb336b.

The paper's Theorem 1.1 is conditional. If the smallest eigenvalue
\(\epsilon_N\) of the finite-dimensional restricted Weil form is simple and
its eigenvector is even, then the constructed rank-one perturbation is
self-adjoint, its regularized determinant is expressed through the Fourier
transform of that eigenvector, and that Fourier transform has only real zeros.
The theorem does not prove the simplicity or evenness assumptions.

The paper's numerical tables and determinant calculations do not establish
the required limiting identification. Section 7 says that proving convergence
of the spectra to the zeros of \(\zeta(1/2+is)\) would amount to proving RH.
It then proposes convergence of suitably normalized regularized determinants
to \(\Xi\), but this is presented as a strategy, not as a proved convergence
theorem. Section 8 states the two essential missing steps explicitly: prove
that the smallest eigenvalue of \(Q^W_\lambda\) is simple with an even
eigenvector, and prove that the prolate function \(k_\lambda\) approximates
the corresponding true eigenvector \(\xi_\lambda\) sufficiently accurately
to transfer its real-zero property to the zeta zeros.

Thus the exact implication needed for RH,
\[
\text{finite self-adjoint approximants with real-line zeros}
\Longrightarrow
\text{the limiting }\Xi\text{-function has only real zeros},
\]
is not established. No finite numerical agreement or determinant ansatz
changes that status.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
