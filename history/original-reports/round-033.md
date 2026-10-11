## Round 33 — form convergence is stronger than Fejér convergence

The finite-section limit in the semilocal manuscript has a further precise
analytic gap. For fixed \(\lambda\), CCM's form is

\[
 QW_\lambda(f,f)=
 \int_{\mathbb R}|\widehat f(t)|^2\frac{2\theta'(t)}{2\pi}\,dt
 +2\Re\!\left(\widehat f(i/2)\overline{\widehat f(-i/2)}\right)
 -\sum_{1<n\le\lambda^2}\Lambda(n)\langle f,T(n)f\rangle,
\tag{33.1}
\]

and \(QW_\lambda^N\) is its restriction to the first \(2N+1\) logarithmic
Fourier modes. The cited source gives only the closed-form/core statement

\[
 QW_\lambda(f,f)=\liminf_{N\to\infty}QW_\lambda^N(f_N,f_N)
\tag{33.2}
\]

for suitable approximating sequences. Uniform convergence of Fejér sums on
the support of \(f\) does not by itself upgrade (33.2) to equality of the
quadratic-form values: the archimedean term in (33.1) has the unbounded weight
\(\theta'(t)\sim\tfrac12\log|t|\), and the finite-section prime terms change
with \(\lambda\). A proof would need a form-norm estimate, not only pointwise
convergence at prime powers.

The same issue affects the claimed interchange of limits. For fixed \(\lambda\),
one can seek an \(N\)-estimate in the form domain; for fixed compactly
supported \(g\), one can then choose \(\lambda\) large enough for the exact
global arithmetic value. But the manuscript takes a diagonal
\((N,\lambda,S)\)-limit without giving a bound uniform in the changing
cutoff. The displayed finite-set dominated-convergence argument controls only
the selected local evaluations; it does not control the archimedean form or
the growing collection \(1<n\le\lambda^2\) in (33.1).

This defect is separate from the decisive sign defect in Rounds 31--32. Even a
fully repaired form-limit theorem would pass along positivity only after the
finite forms had been proved positive. The source's spectral-reality theorem
does not provide that finite positivity; it only makes the shifted quotient
operator self-adjoint under its simple-even hypotheses.

**Established:** support stabilization and Fourier approximation are not,
without form-norm estimates, a proof of finite-section Weil-form convergence.

**Remaining load-bearing statement:** a source-faithful theorem proving
\(QW_\lambda^N(g_N,g_N)\to QW(g,g)\) along a specified diagonal, together with
\(QW_\lambda^N\ge0\). Neither statement is supplied by the cited determinant
theorem.

**RH status:** no unconditional proof has been produced.
