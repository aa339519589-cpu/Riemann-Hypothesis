## Round 30 — the corrected off-line mass cone is also locally realizable

The source-mass correction in Round 29 leaves a sharper question: perhaps the
off-line half-mass condition, unlike the pure-critical kernel, prevents local
cancellation. On sufficiently short intervals it does not.

### I. Correctness decision

**成立 (conditional local realizability theorem).**

Assume that only finitely many nontrivial zeros are off the critical line. Write
an off-line zero in the \(\gamma\)-coordinate as
\(\rho=a+ib\), with \(b\neq0\), and use its conjugate
\(\bar\rho=a-ib\). Let \(I_t=(-t,t)\).

For every sufficiently small \(t>0\), the critical ordinates contain a
sequence \((\lambda_n)_{n\in\mathbb Z}\) satisfying

\[
 |t\lambda_n-\pi n|<\delta
\qquad(n\in\mathbb Z),
\tag{30.1}
\]

for one fixed \(\delta<\pi/4\). Indeed, choose one fixed critical ordinate for
\(n=0\), so that \(t|\lambda_0|<\delta\). For \(n\neq0\), the intervals

\[
 J_n=\left(\frac{\pi n-\delta}{t},\frac{\pi n+\delta}{t}\right)
\]

are disjoint and have fixed length \(2\delta/t\). The
Riemann--von Mangoldt count, after deleting the finitely many exceptional
ordinates, gives at least one critical ordinate in every \(J_n\) once \(t\) is
small enough. Reflection supplies the negative indices.

After the change of variables \(u=tx\), (30.1) is Kadec's \(1/4\) condition.
Consequently the normalized critical exponentials

\[
 \phi_n(u)=(2t)^{-1/2}e^{-i\lambda_nu}
\]

form a Riesz basis of \(L^2(I_t)\), with a basis constant \(C_\delta\) depending
only on \(\delta\), not on \(t\).

Now take the exceptional coefficient vector \(e\) supported on
\(\rho,\bar\rho\) with entries \(1,-1\). Its norm is
\(\|e\|_2^2=2\), and its local exceptional waveform is

\[
 h_E(u)=e^{-i\rho u}-e^{-i\bar\rho u}
       =2e^{-iau}\sinh(bu).
\]

The Riesz-basis expansion of \(-h_E\) in the critical exponentials gives a
coefficient vector \(c\in\ell^2\) with

\[
 \|c\|_2^2
 \leq
 \frac{C_\delta^2}{2t}\|h_E\|_{L^2(I_t)}^2
 =
 C_\delta^2\left(\frac{\sinh(2|b|t)}{|b|t}-2\right).
\tag{30.2}
\]

Since the nontrivial-zero strip gives \(|b|<1/2\), the right side of (30.2)
tends uniformly to zero as \(t\downarrow0\). Thus \(t\) can be chosen so that
\(\|c\|_2^2<2=\|e\|_2^2\). With the critical coefficients \(c\) and the
off-line coefficients \(e\),

\[
 S_Cc+S_Ee=0\quad\text{on }I_t,
\tag{30.3}
\]

and, after normalization, the off-line mass is

\[
 \frac{\|e\|_2^2}{\|c\|_2^2+\|e\|_2^2}>\frac12.
\tag{30.4}
\]

Therefore local vanishing and the correct Section-11 off-line mass cone are
simultaneously realizable under the finite-exception hypothesis.

### II. Hostile audit

This construction is a conditional counterexample to a proposed local
separation argument; it does not construct an off-line zero and does not
identify Bombieri's particular finite-truncation eigenvector. It also uses a
sufficiently short interval and unweighted Section-11 coefficients. It cannot
be transferred to the weighted first variational problem without a separate
source-normalization theorem.

The key point is nevertheless decisive for route selection: correcting the
mass direction does not restore a local contradiction. Any proof must use
additional arithmetic or finite-branch provenance beyond (30.3)--(30.4).

### III. Ledger update

**已确认事实:** under finite exceptions, short-interval critical zeros can
satisfy a uniform Kadec perturbation of the Fourier lattice, and every
conjugate off-line pair then has a critical representation whose coefficient
cost is \(o(1)\) as the interval shrinks.

**成立点:** the local null equation and the source-correct off-line half-mass
condition are compatible.

**失败 / 错误点:** attempting to exclude finite exceptions from local
linear-independence or mass-cone conditions alone.

**仍属假设:** the finite-exception hypothesis and the use of the Section-11
unweighted coefficient category.

**未知 / 待验证:** whether arithmetic source data or the exact selected
finite-eigenvector branch impose a constraint not present in (30.3)--(30.4).

**下一步路线:** abandon local unweighted separation as a complete route and
focus on a genuinely source-bearing invariant; the weighted auxiliary rounds
remain conditional and must not be merged with Section 11.

**RH status:** no unconditional proof has been produced.
