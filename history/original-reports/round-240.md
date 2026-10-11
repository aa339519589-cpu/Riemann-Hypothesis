## Round 240 — A/B result: Grant's geometric manuscript has no prime-error bridge and uses an invalid harmonic substitution

**Source inspected:** Robert Edward Grant, *Proof of the Riemann Hypothesis:
A Geometric Constraint on Prime Fluctuations*, PDF
<https://robertedwardgrant.com/wp-content/uploads/2026/01/REG-RH_Proof-Jan1.pdf>,
January 2026, pp. 1–14.
Downloaded source SHA-256:
9af71d0e3615c8277116355f09dec2799440d89e3f03aa504457154e900828ee.

The lattice calculations do not encode the prime-counting error. The
triangular lattice norm and the circle-intersection construction describe
geometric representations of integers, but the manuscript gives no
bijective or inequality-preserving map from prime occurrences to the
intersection events on a circle. The fact that an annulus has
\(O(\sqrt{x})\) lattice points therefore does not imply
\[
\left|\pi(x)-\operatorname{Li}(x)\right|=O(\sqrt{x}).
\]
That implication is stated as the “Holographic Bound”; its proof merely
repeats that prime fluctuations are boundary events. The preceding
definitions do not establish that premise, so Theorem 6.2 is not proved.

The central analytic application also does not satisfy the hypotheses of the
manuscript's own Theorem 5.1. That theorem is stated for an absolutely
summable coefficient family \(\sum_k|c_k|<\infty\), whereas its application
uses \(c_\rho=1/\rho\) over all non-trivial zeros. The zero-counting
asymptotic implies
\[
\sum_\rho\frac1{|\rho|}=\infty.
\]
The explicit-formula zero sum is conditionally interpreted through
truncation and symmetric limiting procedures, not as the absolutely
convergent exponential sum required by Theorem 5.1. The manuscript supplies
no theorem that replaces this missing hypothesis or proves the claimed
tail estimate uniformly in \(x\). In addition, the proof of Theorem 5.1 as
written assumes that \(\sup_k\beta_k\) is attained and that the remaining
infinite sum is a uniform \(o(1)\); no argument is given for a non-attained
supremum. Thus Theorem 8.2 cannot be obtained from the stated result.

The “harmonic imaginary unit” is not a valid complex-analytic change of
coordinates. With \(i_h=-1/\sqrt{10}\), one has \(i_h^2=1/10\), not
\(-1\). Replacing \(i\) by \(i_h\) therefore does not preserve multiplication,
holomorphicity, the functional equation, or the zero set of \(\zeta\).
Equation (5) only rewrites a zero already assumed to have the form
\(\rho=1/2+i\gamma\); an off-line zero \(\rho=\beta+i\gamma\) would be mapped
to the real number \(\beta-\gamma/\sqrt{10}\) as well. No conclusion about
\(\beta\) follows.

The recursive argument contains a separate logical gap. Reciprocal
admissibility of \(\lambda\) and \(\lambda^{-1}\), together with a bound
\(C(n)=O(\sqrt n)\), does not imply \(\lambda=1\). For example, the stated
assumptions are compatible with a generator having \(\lambda=2\),
\(\lambda^{-1}\) admissible, and no distinguishable events, so that
\(C(n)=0\). The proof's missing assertion that monotone scale drift must
create a comparable number of boundary events is not a consequence of the
definitions. Definition 7.8 likewise gives no exact map from \(\lambda\) to
the Mellin exponent, so neutral \(\lambda=1\) does not imply
\(\operatorname{Re}(s)=1/2\).

The functional-equation symmetry would force equality only after a valid
upper bound \(\beta\leq1/2\) had been proved. Since the geometric bound and
the exponential-sum application both fail, the final symmetry step cannot
repair them. The manuscript gives no unconditional proof or disproof of RH.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
