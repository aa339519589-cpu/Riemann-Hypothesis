## Round 120 — semilocal spectral reality does not imply Weil positivity

I checked the April 2026 manuscript [*A Proof of the Riemann Hypothesis for
the Riemann Zeta Function: Weil Positivity via Semilocal Spectral
Descent*](https://zenodo.org/records/19546495) and its cited spectral
papers.  The advertised chain breaks at the passage from a shifted
semidefinite form to the original Weil form.

### 120.1 The shift by the lowest eigenvalue is load-bearing

The manuscript defines \(\epsilon_N\) as the lowest eigenvalue of a finite
form \(Q^N_{W,\lambda}\), then uses

\[
 Q^N_{W,\lambda}-\epsilon_N I\ge0
\tag{120.1}
\]

and self-adjointness of an operator constructed for the shifted form to claim
that its spectral zeros are real and hence that \(Q^N_{W,\lambda}\) is
positive.  Equation (120.1) is true for every self-adjoint finite matrix by
the definition of its smallest eigenvalue, including an indefinite matrix.
For example,

\[
 Q=\operatorname{diag}(-1,2),\qquad
 \epsilon_{\min}=-1,\qquad Q-\epsilon_{\min}I=\operatorname{diag}(0,3)\ge0.
\tag{120.2}
\]

Thus reality of the shifted spectral zeros supplies no sign information about
\(\epsilon_N\).  The missing statement is exactly
\(\epsilon_N\ge0\), which is equivalent to the finite Weil positivity being
claimed.  It cannot be obtained from (120.1) by repeating the definition of
\(\epsilon_N\).

### 120.2 The arithmetic-spectral identity is not connected to the shifted operator

The manuscript next writes the unshifted form as a sum of squares over
“spectral zeros” of the semilocal operator.  To justify that identity in the
present setting one must identify, with all normalizations,

\[
 Q^N_{W,\lambda}(g*\bar g^\sharp)
 =\sum_k\widetilde g(\rho_k)\,
   \widetilde g(1-\overline{\rho_k}),
\tag{120.3}
\]

where the \(\rho_k\) are the zeros of the operator whose self-adjointness was
proved for the shifted form.  The cited real-zero theorem instead has
hypotheses about a specified quadratic-form operator and, in its general
statement, a simple isolated lowest eigenvalue with an even eigenfunction.
The candidate supplies no derivation showing that its shifted quotient,
its determinant, and (120.3)'s unshifted arithmetic form are the same
objects.  Without that bridge, the phrase “spectral zeros are real” concerns
an auxiliary semilocal spectrum, not the zero divisor in the Weil identity.

### 120.3 Compact support does not justify the claimed threefold limit

If \(g\) is supported in \([\varepsilon,M]\), choosing
\(\lambda>M/\varepsilon\) can stabilize those local multiplicative terms whose
arguments lie in the selected window.  It does not make the Fourier partial
sums \(g_N\) compactly supported in the same interval, nor does it by itself
control the archimedean quadratic term or the full collection of prime terms.
If the finite place set \(S\) is fixed, the limit is only the \(S\)-truncated
form; if \(S\) grows, a uniform form-norm bound is required.  Pointwise
convergence of \(g_N(p)\) at each fixed prime is insufficient for exchanging
the growing prime sum with \(N\to\infty\).

Consequently the manuscript's implication

\[
 Q^N_{W,\lambda}(g_N)\ge0
 \ \Longrightarrow\
 Q_W(g)\ge0
\tag{120.4}
\]

has not been proved.  The needed uniform convergence is a statement about the
complete quadratic form, not ordinary Fejér convergence on the support of
\(g\).

**Established:** semilocal self-adjointness or reality of a shifted auxiliary
spectrum does not imply \(\epsilon_N\ge0\) or positivity of the original Weil
form.

**Failure / missing step:** the candidate neither proves the sign of the
lowest form value nor supplies the unshifted arithmetic-spectral identity and
the uniform \(N,\lambda,S\) form convergence required by (120.4).

**Route decision:** this candidate does not close the RH implication.  The
source-faithful targets remain an independent global Weil-positivity theorem
or a complete finite-section limit with its sign and spectral identification
proved separately.

**RH status:** no unconditional proof has been produced.
