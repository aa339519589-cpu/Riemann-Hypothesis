## Round 219 — A/B result: Paltoo's adelic SSBF manuscript is undefined on its quotient and uses the zero--spectrum correspondence circularly

**Source inspected:** Nigel Stafford Paltoo, *The Adelic Standing/Sitting
Band Framework (SSBF): A Rigorous Operator-Theoretic Realization and
Non-Circular Proof of the Riemann Hypothesis*, Parts 1--6, August 2026,
Zenodo record
<https://zenodo.org/records/22096430>, PDF pp. 1--9.

There is a direct well-definedness failure in the proposed potential.  The
manuscript sets
\(X_1=\mathbb A_{\mathbb Q}^{\times}/(\mathbb Q^{\times}\mathbb R_+^{\times})\)
and then uses the coordinate \(y=\log|x|_\infty\) to define
\[
V_{\rm prime}^{(\epsilon)}(y)=
\sum_p\frac{\log p}{\sqrt p}e^{-\epsilon\sqrt p}\cos(y\log p).
\]
But multiplication by any \(r\in\mathbb R_+^{\times}\) identifies \(x\) and
\(rx\) in \(X_1\), while it changes \(y\) to \(y+\log r\).  The displayed
cosine sum is not invariant under all such translations.  Hence it is not a
function, and therefore not a multiplication operator, on the stated quotient
without an additional construction that the manuscript does not provide.

The claimed compact-group argument also does not construct the missing
analytic data.  No global hyperbolic metric in the coordinate \(y\), closed
quadratic-form domain, or valid finite-difference convergence theorem on this
idele quotient is supplied.  The finite symmetric matrices only have real
eigenvalues at each finite tier; that fact does not identify the spectrum of a
limiting operator with zeta zeros.

The central trace assertion is the desired correspondence written as a
theorem.  Theorem 11.1 simply states the Weil explicit formula with a real
sequence \(\{\gamma_k\}\) and then declares those numbers to be the spectrum
of \(D\).  Tate factorization and an Euler product do not, by themselves,
prove that the trace of this newly defined operator equals the zero side of
the explicit formula, nor do they handle a hypothetical zero with
\(\operatorname{Re}\rho\ne1/2\).  The introductory notation already writes
\(\rho_k=1/2+i\gamma_k\), and Theorem 13.1 uses the same parametrization in
step 1 before self-adjointness is invoked.  This is precisely the load-bearing
zero-location assumption, not a downstream consequence.

The Li-coefficient section repeats the circular step: it invokes Li's
criterion, whose positivity is equivalent to RH, and then substitutes
\(\rho_k=1/2+i\gamma_k\) to obtain positivity.  Self-adjointness can make
operator eigenvalues real only after a valid zero-to-spectrum map has been
proved; it cannot prove that arbitrary zeta zeros have that form.

Thus the potential, trace formula, and spectral correspondence are not
established, and the claimed non-circular RH proof does not close.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
