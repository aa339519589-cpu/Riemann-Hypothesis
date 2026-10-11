## Round 32 — the cited source identifies positivity as the missing assertion

The source audit gives a sharper formulation of the failure in the semilocal
descent manuscript. CCM defines the bottom of the semilocal form by

\[
 \mu_\lambda
 =\inf_{0\ne f\in L^2([\lambda^{-1},\lambda])}
   \frac{QW_\lambda(f,f)}{\|f\|_2^2},
\tag{32.1}
\]

and states that the lower bound is the limit of the smallest eigenvalues
\(\epsilon_N\) of the finite restrictions \(QW_\lambda^N\). The same source
then explicitly says that one cannot assert \(\mu_\lambda\ge0\); it proves
only that \(\mu_\lambda\) is decreasing in \(\lambda\), and that the further
assertion \(\lim_{\lambda\to\infty}\mu_\lambda=0\) would imply RH.

Therefore the manuscript's Theorem 2, if proved, would establish the precise
missing statement:

\[
 QW_\lambda^N(g,g)\ge0\quad\forall g,N
 \Longrightarrow\quad \epsilon_N\ge0
 \Longrightarrow\quad \mu_\lambda\ge0.
\tag{32.2}
\]

But the cited determinant theorem proves no implication of this kind. It uses
the tautological shift

\[
 T_N=QW_\lambda^N-\epsilon_N I\ge0
\tag{32.3}
\]

to construct a self-adjoint quotient operator. The shift removes the unknown
sign of \(\epsilon_N\); it cannot restore that sign. This is the exact point
where the proposed proof becomes circular.

The source formula for the finite restriction is instead the explicit form

\[
 QW_\lambda(f,f)=
 \int_{\mathbb R}|\widehat f(t)|^2\frac{2\theta'(t)}{2\pi}\,dt
 +2\Re\!\left(\widehat f(i/2)\overline{\widehat f(-i/2)}\right)
 -\sum_{1<n\le\lambda^2}\Lambda(n)\langle f,T(n)f\rangle.
\tag{32.4}
\]

The regularized determinant of the auxiliary quotient is not a diagonalization
of the three terms in (32.4). In particular, the source establishes a real
zero theorem for the Fourier transform of one simple-even lowest eigenvector;
it does not establish the candidate manuscript's equation (31.4), which would
be a full spectral resolution of (32.4) and would immediately imply (32.2).

### Independent limit defects

The compact-support observation also has a narrower scope than claimed. If
\(g\) is supported in \([\varepsilon,M]\), then stabilization of the local
terms of \(g*\bar g^\sharp\) can be obtained after the relevant multiplicative
support is contained in \([\lambda^{-1},\lambda]\). It does not identify that
stabilized value with \(QW_\lambda^N(g_N,g_N)\) for Fourier approximants
\(g_N\). Those approximants are functions on the whole logarithmic interval,
and their convolutions generate the entire finite-section range. The cutoff,
the prime powers, and the finite-dimensional space must therefore be coupled
in one proved limiting estimate.

Moreover, if the finite place set \(S\) is held fixed, its form is not the CCM
form (32.4), which contains all \(n\le\lambda^2\). If \(S\) grows, the
manuscript provides no uniform bound permitting the claimed interchange of
the \(N\), \(\lambda\), and \(S\) limits. Fejér convergence also does not
preserve \(\widetilde g(0)=\widetilde g(1)=0\) without an explicit correction
argument.

**Closed finding:** the candidate argument has replaced the unproved inequality
\(\mu_\lambda\ge0\) by a proved reality statement for a shifted auxiliary
operator. Those are different assertions.

**Remaining exact target:** prove \(\epsilon_N\ge0\) (with the relevant
finite-section and limit controls), or derive an independent positivity
identity for the actual form (32.4). No such identity has been established.

**RH status:** no unconditional proof has been produced.
