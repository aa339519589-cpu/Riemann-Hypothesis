## Round 243 — A result: the terminal-episode exclusion is a verified unconditional subtheorem, not an RH closure

**Source inspected:** Rainer Andreas Mittermeier, *Deep Episodes in the
Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem,
an Exact Chebyshev Bridge, and Sharp Recovery Recurrence — Part 5*, Zenodo
record
<https://zenodo.org/records/22076088>, PDF pp. 1–29.
Downloaded source SHA-256:
30668cdd8a6aeefe16e0d1fbfc76a9e41bcf85f53b1da07c53f5e04cd1f0c279.

### VERIFIED PROOF CHAIN addition

The source's Theorem 3.5 survives an independent check as the following
unconditional subtheorem, using only the stated standard inputs (the prime
number theorem, the functional equation, the Riemann--von Mangoldt existence
of non-trivial zeros, and the classical one-sign singularity theorem):
\[
\text{There is no }t_0\text{ such that }Y(t)>0\text{ for every }t\geq t_0.
\]
Here \(Y=-\Psi'\) is the right-continuous workload. The exact synchronization
is
\[
Y(t)=\eta(e^t)-R_A(e^t),\qquad
\eta(u)=\sum_{n\leq u}\frac{\Lambda(n)}{\sqrt n}-2\sqrt u+\alpha,
\]
where \(R_A(u)>0\) is integrable against \(du/u\).

For completeness, the contradiction can be checked as follows. A terminal
episode would imply \(\eta(u)>0\) eventually. For \(\Re s>1/2\), the Mellin
transform \(H(s)=\int_1^\infty\eta(u)u^{-s-1}\,du\) equals
\[
H(s)=\frac1s\left(-\frac{\zeta'}{\zeta}\right)
\left(s+\frac12\right)
-\frac2{s-\frac12}+\frac{\alpha}{s}.
\]
The cancellations at \(s=0\) and \(s=1/2\), together with
\(\zeta(\sigma)<0\) for \(0<\sigma<1\), make \(H\) regular on the real
segment \([0,1/2]\).

If \(\int^\infty\eta(u)\,du/u=\infty\), the positive-tail Mellin transform
has a finite abscissa of convergence in \([0,1/2]\). The
Pringsheim--Landau theorem forces a singularity at the corresponding real
boundary point, while the difference between the tail transform and \(H\)
is an entire compact-interval integral. This contradicts the regularity just
established.

If \(\int^\infty\eta(u)\,du/u<\infty\), then \(H\) is continuous on
\(\Re s\geq0\) and analytic on \(\Re s>0\). Analytic continuation of the
displayed identity first excludes zeros of \(\zeta\) with
\(\Re\rho>1/2\). Functional-equation symmetry then excludes zeros with
\(\Re\rho<1/2\). A non-trivial zero on the critical line is known to exist;
approaching its shifted point \(s=\rho-1/2\) from \(\Re s>0\) makes
\(-\zeta'/\zeta(s+1/2)\) unbounded, whereas the right side remains finite
because \(H\) has a finite boundary value. This is the second contradiction.
Both possible integrability cases are impossible, proving the subtheorem.

This is a genuine unconditional theorem and is therefore entered in the
VERIFIED PROOF CHAIN. It does not prove \(\Psi(t)\geq0\): it only ensures
that every sufficiently late active episode eventually recovers. The
remaining universal recovery-witness inequality
\[
V_q=C_q-J_q\geq0
\]
is not proved by this theorem and remains the RH-equivalent load-bearing
condition.
