## Round 114 — correction of the gap-to-Kadec bridge

This round corrects two related assertions used by the earlier local
unweighted route.  The correction is append-only: it records exactly which
inference was invalid and which stronger theorem would repair the conditional
step.

### 114.1 Arbitrarily small gaps are not a Kadec hypothesis

Kadec's one-quarter theorem requires a globally indexed sequence
\(\{\lambda_n\}_{n\in\mathbb Z}\) satisfying, after normalization,

\[
 \sup_{n\in\mathbb Z}|t\lambda_n-\pi n|<\frac{\pi}{4}.
\tag{114.1}
\]

By contrast, the statement that consecutive critical ordinates have
arbitrarily small gaps, or even that some successive gaps tend to zero,
provides only local clustering.  It does not put a critical ordinate near
every prescribed lattice point.  A direct counterexample to that logical
implication is

\[
 \Lambda=\{\pm n^2,\ \pm(n^2+1/n): n\geq1\}.
\]

This set has gaps \(1/n\to0\) inside its pairs, but also has arbitrarily long
empty intervals; no enumeration of it can satisfy (114.1) for a fixed
positive \(t\).  Therefore the sentence in the original Round 12 that
deduced a Kadec tail from the small-gap statement is not a valid proof.

### 114.2 The conditional local route can be repaired, but with a stronger input

The desired interval-occupancy statement is instead a fixed-window local
zero-count theorem.  Titchmarsh's fixed-\(h\) estimate has the form

\[
 N(T+h)-N(T)\geq K(h)\log T
 \qquad (T\geq T_0(h),\ h>0\text{ fixed}),
\tag{114.2}
\]

for the total nontrivial zero count.  This is stronger than the bare
Riemann--von Mangoldt asymptotic with an \(O(\log T)\) error and is the
appropriate source for filling every interval \(J_n\) of fixed length.  The
statement is recorded in Titchmarsh's fixed-interval theorem (see the cited
scan of *The Theory of the Riemann Zeta-function*, Theorem 9.14).

Under the separate finite-exception hypothesis, all zeros above one fixed
height are critical.  Applying (114.2) to

\[
 J_n=\left(\frac{\pi n-\delta}{t},\frac{\pi n+\delta}{t}\right),
 \qquad 0<\delta<\frac{\pi}{4},
\]

with \(t\) sufficiently small makes the lower endpoint of every positive
\(J_n\) exceed the theorem's threshold.  Hence one may choose a critical
ordinate in every \(J_n\), and reflection supplies the negative indices.
This repairs the *conditional* Kadec construction used in Round 30.  Its
written justification as “the Riemann--von Mangoldt count” was too weak and
must be replaced by (114.2).

### 114.3 Scope after correction

The repaired statement is still conditional on finitely many off-line zeros
and applies to the unweighted local coefficient category.  It does not
exclude the finite-exception hypothesis, identify Bombieri's selected finite
eigenvector branch, or establish the weighted range inequality (103.6).
Consequently it cannot be promoted to RH.  Round 109's dense-range argument
and Round 112's restricted convolution-square closure do not use the invalid
small-gap inference and remain logically separate.

**Correction:** replace the Round 12 small-gap-to-Kadec justification and the
Round 30 bare-Riemann--von-Mangoldt justification by the fixed-window theorem
(114.2).  Do not use either earlier wording as an unconditional step.

**RH status:** no unconditional proof has been produced.
