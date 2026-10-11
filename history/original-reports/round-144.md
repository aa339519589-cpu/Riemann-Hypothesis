## Round 144 — audit of the 2026 “Overdetermined Weil Systems” claim

I audited the preprint *Overdetermined Weil Systems and the Riemann
Hypothesis*, Zenodo v1 (6 July 2026):
<https://zenodo.org/records/21218854>.  Its advertised conclusion is not a
verified proof.  Two independent breaks occur before the final theorem.

### 144.1 The infinite-case inference is invalid

The paper obtains, formally,

\[
 \sum_{k=1}^{M} f_k(n)=0,\qquad n=2,3,\ldots,
\tag{144.1}
\]

and proves, at most, that every finite subfamily of the functions \(f_k\) is
linearly independent.  In the case \(M=\infty\), it then says that the
one-pair case can be applied to any individual pair.  That does not follow
from (144.1): the other infinitely many terms do not disappear when one pair
is selected.

Finite linear independence does not exclude a convergent infinite relation.
For example, in a Hilbert space let \(e_0,e_1,\ldots\) be an orthonormal
sequence and set

\[
 g_0=\sum_{j\ge1}2^{-j}e_j,
 \qquad g_j=e_j\ (j\ge1).
\]

Every finite subfamily of \(\{g_0,g_1,\ldots\}\) is linearly independent, but

\[
 g_0-\sum_{j\ge1}2^{-j}g_j=0
\tag{144.2}
\]

is a nontrivial convergent infinite relation.  Therefore the paper would need
both a rigorously specified function/distribution space in which (144.1)
converges and an infinite-series uniqueness theorem for these particular
\(f_k\).  Neither is supplied.  Moreover, the displayed \(f_k(n)\) contain
hyperbolic factors in \(\log n\), so convergence of the sum over infinitely
many zero heights is itself an unproved issue.  This alone invalidates the
claimed Case 3.

### 144.2 The stated Fourier cutoff is not an approximation to the test
function

The paper defines

\[
 \varphi_\delta(t)=\delta^{-1}\varphi(t/\delta),
 \qquad
 \widehat h_{n,\delta}(t)=\widehat h_n(t)\varphi_\delta(t),
\tag{144.3}
\]

and asserts that the inverse transforms converge pointwise to
\(h_n^{\rm even}\).  But

\[
 \operatorname{supp}\widehat h_{n,\delta}\subset[-\delta,\delta].
\]

Consequently every distributional limit as \(\delta\downarrow0\) is supported
at \(\{0\}\).  It cannot equal the displayed \(\widehat h_n\), which the paper
itself writes as a nonzero interval-indicator term plus a remainder.  In the
regular case the calculation is explicit: for every test function \(\psi\),

\[
 \int \widehat h_n(t)\varphi_\delta(t)\psi(t)\,dt
 =\int \widehat h_n(\delta s)\varphi(s)\psi(\delta s)\,ds
 \longrightarrow
 \widehat h_n(0)\psi(0)\int\varphi(s)\,ds,
\tag{144.4}
\]

which is a multiple of \(\delta_0\), not \(\widehat h_n\).  The operation that
could approximate a function is an appropriately normalized convolution, not
the shrinking-support multiplication in (144.3).  Thus the asserted Barner
continuity step is not established by the construction actually given.

There is also a direct admissibility warning: near \(z=1\),

\[
 \frac{\cos(z\log n)}{z\log z}
 \sim \frac{\cos(\log n)}{z-1},
\]

for generic \(n\), so the proposed \(h_n^{\rm even}\) is not analytic at the
point \(z=1\) under the paper's own stated analytic-test-function hypothesis.
The paper's distributional discussion does not prove that this singular test
function lies in the required Weil--Barner continuity class.

### 144.3 The claimed self-adjoint “corroboration” is not a spectral bridge

Appendix C lists \(E_n=\tfrac14+\gamma_n^2\) using only the real ordinates
\(\gamma_n=\operatorname{Im}\rho_n\), even when
\(\operatorname{Re}\rho_n\ne\tfrac12\).  A self-adjoint operator with real
spectral data \(E_n\) does not by itself identify the complex zeros
\(\rho_n\), nor does its \(J\)-symmetry imply that the omitted real parts vanish.
A determinant or characteristic-function identity equating the constructed
spectral object to \(\xi(s)\) is required and is not proved.  This is a
restatement of the scalar-to-spectral identification gap already found in
earlier audits, not an independent corroboration.

**Established:** the cited preprint does not close RH; its infinite-case
logical step and its stated mollifier limit fail as written.

**Remaining load-bearing statement:** obtain a genuine zeta-specific theorem
that excludes the infinite off-line null-cone/escape branch, or a separate
unconditional positivity/spectral argument with every identification proved.

**RH status:** no unconditional proof has been produced.
