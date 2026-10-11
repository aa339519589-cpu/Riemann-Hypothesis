## Round 40 — finite Galerkin data do not close the continuum Weil form

I checked the independent 2026 Galerkin study *High-Precision Approximation of
Riemann Zeros via the Truncated Weil Form*, arXiv:2605.20224. Its mathematical
status is explicit: the finite-cutoff ground-state transform has real zeros,
but convergence of those zeros to the actual Riemann zeros as the cutoff tends
to infinity is open; the paper makes no proof claim.

The data distinguish three different assertions:

\[
\begin{aligned}
 &QW_{c,N}\text{ has a numerically selected positive/even eigenvector},\\
 &\widehat\xi_{c,N}\text{ has real zeros},\\
 &\widehat\xi_{c,N}\longrightarrow\Xi\text{ in a zero-preserving topology}.
\end{aligned}
\tag{40.1}
\]

The first two can hold at many finite cutoffs while the third remains
unproved. The finite matrices also exhibit cutoff-dependent negative blocks in
some computations; removing a numerical archimedean cutoff can remove those
blocks, but that numerical stability check does not establish positivity of the
continuum form for every cutoff.

The exact analytic implication needed for a proof is a uniform statement such
as

\[
 c_{j,N}\,\widehat\xi_{c,N}(z)\longrightarrow\Xi(z)
\quad\text{locally uniformly on every compact subset of }\mathbb C,
\tag{40.2}
\]

with nonzero normalization, plus a theorem ensuring that the vectors used in
(40.2) are the actual lowest-eigenvalue branch and satisfy the required
simple-even hypotheses. Real zeros at each finite stage do not imply that the
limit has only real zeros unless (40.2) and nonvanishing of the limit are
proved. This is the same branch-selection and convergence bottleneck already
isolated in Rounds 13 and 31--33.

**Established:** high-precision finite agreement is evidence about the
truncated operator, not a proof of the continuum limit.

**Remaining load-bearing statement:** prove the zero-preserving convergence
(40.2), with a source-defined ground-state branch and all normalization/error
controls. No finite numerical sweep supplies it.

**RH status:** no unconditional proof has been produced.
