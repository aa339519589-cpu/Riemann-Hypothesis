## Round 193 — A/B result: Yang's Euler-product matrix construction fails before the limit operator

**Source inspected:** Jianning Yang, *Proof of the Riemann Hypothesis via
Euler Product Linearization and Self-Adjoint Operator Recursion*, Zenodo
record
<https://zenodo.org/records/20436693>, main PDF and technical appendix
downloaded as /tmp/yang-rh.pdf and /tmp/yang-rh-appendix.pdf.

There is a basic variable inconsistency at the start.  The manuscript defines
the standard completed function
\(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), whose functional
equation is \(\xi(s)=\xi(1-s)\), but then asserts \(\xi(-z)=\xi(z)\) and
uses \(\xi(t)=0\) for zeros \(\rho=\tfrac12+it\).  Evenness holds only after
introducing the centered variable \(z=s-\tfrac12\); that change is not made
in the displayed definition.  The claimed zero parametrization therefore
already presupposes the critical-line form.

Theorem 3.4 asserts, without a coefficient calculation, that the
characteristic polynomial of \(M_n=A_n^\dagger A_n\) is a scalar multiple of
the Taylor polynomial of \(\xi\).  The characteristic coefficients depend on
the chosen sampling ordinates through the phase factors
\(e^{i\tau_m(\log p_l-\log p_k)}\), whereas the Taylor coefficients of \(\xi\)
do not.  The sentence that both sets of coefficients have the same symmetric
prime-product structure is not a derivation of the asserted polynomial
identity.

The full-rank proof (Theorem 4.3) contains a direct logical error: an entire
function that vanishes at \(n\) distinct points need not vanish identically.
The function
\[
 f(s)=\sum_{k=1}^n\alpha_k\frac{\log p_k}{p_k^s}
\]
is an entire Dirichlet polynomial, but the manuscript has only \(n\) zeros of
it.  The identity theorem requires an accumulation point of zeros (or
infinitely many zeros under a separate argument), not merely as many zeros as
terms.  Thus full column rank, and hence positive definiteness rather than
mere semidefiniteness, is not proved.

Lemma 5.1 uses a divergent quantity as a tail bound.  On \(\operatorname{Re}s
=1/2\), the proposed right side is
\[
 \sum_{p>p_k}\frac{\log p}{\sqrt p-1},
\]
which diverges: its summands are asymptotic to \(\log p/\sqrt p\), and the
prime sum has divergent partial sums.  The Euler-product Dirichlet series is
not absolutely convergent on the critical line, so the claimed exponentially
small tail estimate and Theorem 5.2 do not follow.

The induction in Section 6 is not an induction on nested matrices.  The
sampling ordinates for \(M_k\) and \(M_{k+1}\) use different \(\delta_k\), and
\(M_{k+1}\)'s top-left block includes a different set of sampling rows.  Thus
the block displayed as
\[
 M_{k+1}=\begin{pmatrix}M_k&u\\u^\dagger&d\end{pmatrix}
\]
is false for the definitions in Section 3, so Cauchy interlacing cannot be
applied.  In addition, the base claim that the fixed scalar \(M_1\) “converges”
to \(t_1^2\) has no limiting parameter.

The infinite-dimensional step has two independent failures.  First,
\[
 \sum_{k\le n}\frac{(\log p_k)^2}{p_k}
 \sim \frac12(\log p_n)^2\longrightarrow\infty
\]
by the prime number theorem and partial summation, contrary to the asserted
uniform bound.  Second, the matrices act on the varying spaces
\(\mathbb C^n\), and no common embedding is defined; consequently the claimed
operator inequality \(M_{n+1}-M_n\succeq0\) is not even a well-formed
statement as written.  The appendix's Rouche estimate also compares a lower
bound of order at most \(c_k(\log k)^2/k^3\) with an upper bound of order
\(1/\sqrt{k\log k}\), then incorrectly calls the latter exponentially small.

Therefore the finite spectral correspondence and the asserted self-adjoint
limit with spectrum \(\{t_j^2\}\) are not established.  The final RH
inference has no valid load-bearing premise.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
