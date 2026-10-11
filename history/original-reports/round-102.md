## Round 102 — Connes' 2026 prolate strategy still requires convergence of the actual minimizers

I audited Connes' February 2026 survey, [*The Riemann Hypothesis: Past, Present and a Letter Through Time*](https://arxiv.org/abs/2602.04022), including §§6.1--6.6 and §§7.1--7.6. This is a serious source and it gives a useful conditional real-zero theorem, but it does not claim an RH proof.

Theorem 6.1 has the following conditional form: if a Weil-kernel quadratic form produces a lower-bounded self-adjoint operator whose lowest eigenvalue is simple and isolated with an even eigenfunction \(\eta\), then the Fourier transform \(\widehat\eta\) has only real zeros. The theorem is not the missing arithmetic assertion. For the finite-support Weil form \(Q_W^\lambda\), the same source states that positivity for every \(\lambda>1\) is equivalent to RH. Therefore applying Theorem 6.1 to the actual minimizer requires precisely the global positivity/spectral information that must be obtained without assuming RH.

The proposed bridge is
\[
\theta_x\longrightarrow E(h)=k,
\qquad
\widehat{k_\lambda}\longrightarrow\Xi
\tag{102.1}
\]
after recentering the minimizer \(\eta_x\) to \(\theta_x\). The source explicitly distinguishes the actual lowest-eigenvalue vector \(\theta_x\) from \(k_\lambda=E(h_\lambda)\), calling the latter an “educated guess”/approximation. The proved convergence of \(\widehat{k_\lambda}\) to \(\Xi\) therefore does not imply convergence of the Fourier transforms of \(\theta_x\). To make Hurwitz applicable one still needs, at minimum, a ground-state selection estimate (for example a spectral-gap/angle bound comparing \(k_\lambda\) with \(\theta_x\)) and a compact-uniform transform estimate on every fixed complex compact set. A Rayleigh quotient tending to the bottom eigenvalue is insufficient when the gap may also tend to zero.

The source itself identifies this comparison as the remaining difficulty in §7.4 and describes the finite-prime eigenvalues/eigenvectors as numerical evidence and a potential strategy. Its conclusion says that whether the path leads to a proof remains open. The semilocal trace formula displayed there is a finite-place identity; no argument in this survey turns it into the required all-\(\lambda\) positivity or proves the global minimizer convergence in (102.1).

**Established:** finite-support self-adjoint constructions and a conditional theorem transferring simple even ground states to real Fourier zeros; convergence of the explicitly constructed candidate transforms \(\widehat{k_\lambda}\) to \(\Xi\).

**Failure / missing step:** identify the actual Weil-form minimizers with the candidate \(k_\lambda\), prove the necessary spectral-gap/normalization and compact-uniform convergence estimates, and then derive global Weil positivity without assuming RH.

**Route decision:** retain this as the strongest closely related auxiliary framework, but not as a completed proof. The direct Bombieri weighted-null-cone exclusion remains the active unconditional target.

**RH status:** no unconditional proof has been produced.
