## Round 13 — semilocal ground-state branch: exact obstruction

This round isolates what can and cannot be proved from the finite-matrix structure
used in the semilocal Weil/prolate proposal.

### 1. The structural matrix identities do not force an even simple minimum

For \(N=1\), index the basis by \((-1,0,1)\), choose

\[
b_{-1}=-1,qquad b_0=0,qquad b_1=1,
\]

and choose \(a_{-1}=a_1=0,\ a_0=100\). The matrix required by the displayed
off-diagonal rule

\[
T_{ij}=\frac{b_i-b_j}{i-j}\quad(i\ne j)
\]

is

\[
T=\begin{pmatrix}0&1&1\\1&100&1\\1&1&0\end{pmatrix}.
\]

It is real symmetric, commutes with the reflection \(V_j\mapsto V_{-j}\), and
has the prescribed even/odd \(a,b\) symmetries. The odd vector

\[
o=(1,0,-1)/\sqrt2
\]

has eigenvalue \(-1\). On the even subspace the matrix is

\[
\begin{pmatrix}1&\sqrt2\\\sqrt2&100\end{pmatrix},
\]

whose smaller eigenvalue is

\[
\frac{101-\sqrt{9809}}2>-1.
\]

Thus the lowest eigenvalue is unique but odd. With the same \(b\)'s and
\(a_{-1}=a_0=a_1=0\), the matrix has eigenvalues \(2,-1,-1\), so its lowest
eigenvalue is not simple. Therefore the identities in the finite-matrix lemma,
including reflection symmetry and the rank-two commutator relation, do not by
themselves prove the two hypotheses required by the real-zero theorem.

These are counterexamples to the structural implication only; they do not claim
that the actual arithmetic distribution \(\mathcal D\) produces either matrix.
An additional, genuinely arithmetic inequality for the actual \(QW_\lambda\) is
required to prove evenness and simplicity.

### 2. Small quadratic energy does not select the ground-state branch

Let \(A\) be a lower-bounded self-adjoint operator with compact resolvent, with
normalized eigenvectors \(v_j\) and eigenvalues

\[
\epsilon_0<\epsilon_1\leq\epsilon_2\leq\cdots,
\]

and let \(k=\sum_j c_jv_j\) be normalized. Put

\[
q=\langle k,Ak\rangle,qquad g=\epsilon_1-\epsilon_0.
\]

Then

\[
q-\epsilon_0
=\sum_{j\geq1}(\epsilon_j-\epsilon_0)|c_j|^2
\geq g\,\operatorname{dist}(k,\mathbb Cv_0)^2.
\]

Equivalently, with the residual \(r=(A-\epsilon_0)k\),

\[
\operatorname{dist}(k,\mathbb Cv_0)\leq \frac{\|r\|}{g}.
\]

Hence \(QW_\lambda(k_\lambda,k_\lambda)\to0\), even together with
\(\epsilon_0(\lambda)\to0\), does not imply that \(k_\lambda\) approaches the
lowest eigenvector. A lower bound on the spectral gap, or a residual estimate
stronger than the Rayleigh quotient, is indispensable. The semilocal proposal's
near-radical estimate supplies neither implication in the required uniform form.

### 3. What would close the final Hurwitz transfer

If one proved, for every sufficiently large parameter, that the actual lowest
eigenvalue is simple and even, and if normalized Fourier transforms of its
eigenvectors converged locally uniformly on the strip

\[
|\operatorname{Im}z|<\tfrac12
\]

to a nonzero multiple of \(\Xi(z)\), then Hurwitz would exclude every non-real
zero of \(\Xi\) in that strip. A zero
\(s=\tfrac12+iz\) off the critical line has
\(|\operatorname{Im}z|<\tfrac12\), so this would imply RH.

The exact missing implication is therefore not the final Hurwitz step. It is the
source-faithful estimate that identifies the arithmetic lowest-eigenvector branch
with the prolate candidate, including the needed simplicity/evenness and
spectral-gap or residual control. This remains unproved.

### Round 13 status

**Established:** the finite-matrix symmetries alone do not imply even simplicity;
the Rayleigh-quotient estimate alone does not imply eigenvector convergence; and
the conditional Hurwitz transfer is exact.

**Not established:** the arithmetic inequality and branch-convergence theorem
needed to obtain an unconditional RH proof.
