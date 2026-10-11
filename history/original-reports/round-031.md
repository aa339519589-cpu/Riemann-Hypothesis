## Round 31 — audit of the semilocal spectral-descent proof claim

I checked the April 2026 manuscript *A Proof of the Riemann Hypothesis for the
Riemann Zeta Function: Weil Positivity via Semilocal Spectral Descent* against
the cited primary sources, in particular Consani--Connes--Moscovici,
arXiv:2511.22755, and Connes--van Suijlekom, arXiv:2511.23257.

### I. The claimed unconditional spectral-reality theorem does not follow

The cited CCM Theorem 1.1 (also Theorem 5.10 in the paper) begins with the
explicit hypotheses

\[
 \epsilon_N=\min\operatorname{spec}(QW_\lambda^N)\text{ is simple},
 \qquad \xi_N\text{ is even}.
\tag{31.1}
\]

Only under (31.1) does it construct the quotient operator and identify its
regularized determinant with the Fourier transform of the single lowest
eigenvector. The paper itself lists simplicity and evenness as two missing
steps. The cited Connes--van Suijlekom result has the same simple, isolated,
even lowest-eigenfunction hypothesis. In the multiple-eigenvalue case, the
radical statement concerns common zeros of all radical eigenfunctions; it does
not say that the zeros of each individual radical eigenfunction are real.

There is also a direct algebraic error in the positivity inference. Writing

\[
 QW_\lambda^N=T_N+\epsilon_N I,
 \qquad T_N\geq0,
\tag{31.2}
\]

the inequality for \(T_N\) is true by the definition of the smallest
eigenvalue. Reality of the spectrum of the quotient operator therefore does
not imply \(\epsilon_N\geq0\), which is the missing assertion needed for
positivity of \(QW_\lambda^N\). For example,
\(Q=\operatorname{diag}(-1,2)\) has \(\epsilon=-1\) and
\(Q-\epsilon I=\operatorname{diag}(0,3)\geq0\), while \(Q\) itself is
indefinite. Thus self-adjointness after the minimum shift cannot prove Weil
positivity.

### II. The asserted sum-of-squares identity is not supplied by the cited
spectral theorem

The primary source proves, under (31.1), the determinant relation

\[
 \det_{\rm reg}(D_{\log}^{(\lambda,N)}-z)
   =-i\,\lambda^{-iz}\,\widehat{\xi_N}(z),
\tag{31.3}
\]

and hence the reality of the zeros of \(\widehat{\xi_N}\). It does not prove
the manuscript's asserted identity

\[
 QW_\lambda^N(g*\bar g^\sharp)
 =\sum_k\widetilde g(\rho_k)\widetilde g(1-\bar\rho_k)
\tag{31.4}
\]

for the zeros \(\rho_k\) of that auxiliary determinant. Here
\(QW_\lambda^N\) is the restriction of the Weil form to the finite space
\(E_N\), whereas \(D_{\log}^{(\lambda,N)}\) acts on a quotient of \(E_N\)
plus the infinite-dimensional complement. A determinant formula for one
lowest-eigenvector transform is not a spectral resolution of the original
quadratic form. The bridge from (31.3) to (31.4), including completeness,
normalization, and the arithmetic weights, is absent.

Consequently, even if all zeros in (31.3) are real, that fact alone gives no
sign for the unshifted form in (31.4). The claimed sum of squares would already
encode the positivity that the argument is supposed to prove.

### III. The compact-support limit does not repair the missing bridge

For a fixed compactly supported test function, choosing \(\lambda\) large
enough can stabilize the finitely many local evaluations appearing in its
explicit-formula value. That observation is not the same as

\[
 QW_\lambda^N(g_N)\longrightarrow QW(g)
\tag{31.5}
\]

for the finite-dimensional Fourier approximants used by the manuscript. The
approximants \(g_N\), extended by zero outside the logarithmic interval, have
convolutions whose support reaches the full finite-section range; the relevant
prime powers and the cutoffs change with \(\lambda\). A fixed finite set of
places \(S\) is not the same object as the CCM form (whose displayed formula
contains all \(n\leq\lambda^2\)). If \(S\) grows, the manuscript supplies no
uniform dominated-convergence estimate. In addition, Fejér approximation does
not automatically preserve the two Mellin constraints
\(\widetilde g(0)=\widetilde g(1)=0\); preserving them requires explicit
finite-rank corrections and corresponding error bounds.

### IV. Exact audit result

The manuscript establishes neither an unconditional version of (31.1), nor
the finite spectral-to-Weil identity (31.4), nor the simultaneous
\((N,\lambda,S)\)-limit required to pass positivity to the global Weil form.
The source-faithful result remains: under the simple-even hypothesis, the
auxiliary lowest-eigenvector transform has real zeros. The sign of the
unshifted Weil form, and therefore RH, remains unclosed.

**RH status:** no unconditional proof has been produced.
