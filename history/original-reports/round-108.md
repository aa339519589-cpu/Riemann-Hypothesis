## Round 108 — the finite Guinand--Weil dictionary is exact at finite level but does not globalize

I audited Groskin's v3 paper, *A finite Guinand--Weil dictionary and archimedean tail order for the truncated Weil quadratic form* ([arXiv:2607.02828](https://arxiv.org/abs/2607.02828), [archived record](https://doi.org/10.5281/zenodo.21124802)).  The correct verdict is **条件成立**: it supplies useful finite-level theorems and a calibrated cutoff error, but not a proof of global Weil positivity or RH.

### 108.1 What is established

For each fixed prime cutoff \(c\) and Fourier band \(N\), a finite real-even Galerkin vector \(v\) is mapped explicitly to a band-limited Guinand--Weil test function \(g_v\).  Applying the explicit formula gives the exact identity
\[
\langle v,Q_\infty v\rangle
=\sum_{\rho}g_v\!\left(\frac{\rho-\frac12}{i}\right),
\]
with multiplicity and with the full nontrivial zero divisor on the right.  This is an algebraic finite dictionary, not a numerical approximation to the zero sum.

The paper also derives an exact rank-two integral for the omitted archimedean tail once \(T>\rho N\).  Its positivity and trace bound imply, for the fixed finite matrix,
\[
0\preceq Q_\infty-Q_T^{\rm tot}\preceq B_T I,
\qquad
\lambda_j(Q_T^{\rm tot})<\lambda_j(Q_\infty)
\leq\lambda_j(Q_T^{\rm tot})+B_T.
\]
Thus a finite-cutoff sign can be certified for that particular \(c,N\) if it lies outside the explicit error band.

### 108.2 The global implication is still absent

The exact finite identity does not provide any of the following:

1. a proof that \(Q_\infty(c,N)\) is positive semidefinite for every \(c\) and \(N\);
2. a uniform lower bound that survives \(N\to\infty\) and \(c\to\infty\);
3. a density or inverse theorem showing that the nonlinear finite dictionary \(v\mapsto g_v\) contains, or is sufficiently dense in, every Weil autocorrelation required by the positivity criterion.

The manuscript explicitly limits its scope to a one-way finite map and states that it proves neither Weil positivity nor RH.  The first two items are a uniform spectral-positivity problem; the third is a separate closure problem.  Agreement with finitely many known zeros, even when the matrix identity is exact, cannot settle any of them.

### 108.3 Relation to the active Bombieri branch

The result sharpens finite computation and rules out archimedean-cutoff artifacts as an explanation for a certified finite negative eigenvalue.  It does not exclude the Bombieri zero-collapse alternative: an off-line packet could still be detected only after the global finite-dimensional subspaces are shown to contain a valid separating test function with controlled limit.  That is logically distinct from the weighted complex-evaluation inequality (103.6).

**Established:** exact finite dictionary; exact finite zero-sum identity; positive rank-two archimedean tail and two-sided finite cutoff budget.

**Failure / missing step:** no all-\((c,N)\) positivity theorem, no uniform limiting spectral gap, and no inverse/density theorem from the finite dictionary to the full Weil test class.

**Route X:** use the dictionary for rigorous finite certificates and prove a uniform global positivity theorem plus a closure theorem.

**Route Y:** prove the direct Bombieri weighted-range exclusion (103.6), which attacks the surviving exceptional packet without first solving the entire finite-dictionary closure problem.

**Route decision:** retain Route Y as the load-bearing route; retain Route X as a source of exact finite identities and hostile checks, not as a completed RH implication.

**RH status:** no unconditional proof has been produced.
