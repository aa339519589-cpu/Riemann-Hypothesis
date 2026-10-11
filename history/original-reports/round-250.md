## Round 250 — A/B result: Franchi's semilocal spectral-descent manuscript does not establish finite or global Weil positivity

Source audited: Christian Franchi Viceré, *A Proof of the Riemann Hypothesis for the Riemann Zeta Function — Weil Positivity via Semilocal Spectral Descent*, local copy
[semilocal-claimed-proof.pdf](work/semilocal-claimed-proof.pdf), dated 2026-04-12, SHA-256
`f2624e1a23c058595ae28e823f226f8a5fe815aa9f4ed4ffd1e78fbd3d2a3b34`.
The finite-dimensional construction is attributed to Connes--Consani--Moscovici
(CCM), [arXiv:2511.22755](https://arxiv.org/abs/2511.22755). I checked the
attributed primary source rather than accepting the claimed finite positivity
as a premise.

The manuscript's Theorem 1 treats the finite Weil form as already yielding
real semilocal zeros and Theorem 2 then asserts
\[
 Q_{W,\lambda}^{N}(g*\bar g^\sharp)
   =\sum_k\left|\widetilde g(\rho_k)\right|^2\ge 0.
\]
That implication is not what CCM's Theorem 1.1 proves. CCM defines
\(\epsilon_N\) to be the smallest eigenvalue of \(Q_{W,\lambda}^{N}\), and
assumes, rather than proves for every \((N,\lambda)\), that it is simple and
that its eigenvector \(\xi\) is even. Its self-adjoint operator is constructed
for the shifted form
\[
 Q_{W,\lambda}^{N}-\epsilon_N\langle\cdot,\cdot\rangle
\]
on the quotient by the corresponding eigendirection. The shifted form is
positive semidefinite by the definition of the smallest eigenvalue; this does
not imply that the unshifted \(Q_{W,\lambda}^{N}\) is positive semidefinite.
Nor does self-adjointness alone supply the omitted simple/even hypotheses.
CCM's Section 8 explicitly lists these hypotheses and the approximation of
\(k_\lambda\) by a scalar multiple of \(\xi_\lambda\) as missing steps, and
states that rigorous zero convergence would amount to a proof of RH.

There is a second independent gap in the proposed passage from finite to
global positivity. The manuscript chooses Fourier partial sums \(g_N\) and
claims that, because \(g\) is compactly supported in \([\varepsilon,M]\), all
local terms stabilize for large \(\lambda\), with dominated convergence over
finitely many primes. But a Fourier/trigonometric partial sum \(g_N\) is
generally not compactly supported in \([\varepsilon,M]\); it can have
nonzero values outside that interval. The stated finite-support stabilization
and the asserted finite dominating set therefore do not apply to \(g_N\).
The manuscript supplies no separate domain, continuity, or core argument
that repairs this mismatch, and it also does not prove that the relevant
finite forms are the unshifted nonnegative forms required by Theorem 2.

Thus the claimed finite Weil positivity is not established, and the subsequent
limit to \(Q_W^S\ge0\), global Weil positivity, and RH does not follow. No
finite numerical verification changes either missing hypothesis or logical gap.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
