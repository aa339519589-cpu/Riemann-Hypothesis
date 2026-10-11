## Round 116 — source-faithful separation of Bombieri's two variational problems

The primary Bombieri text makes the coordinate distinction explicit.  The
first variational problem in Sections 8--10 uses

\[
 d_\gamma=\frac14+\gamma^2,
 \qquad w_\gamma=d_\gamma z_\gamma,
 \qquad
 Z(u)=\sum_\gamma \frac{w_\gamma}{d_\gamma}e^{-i\gamma u},
\tag{116.1}
\]

and its normalization is on the \(w\)-coordinates.  The second variational
problem in Section 11 instead uses the pure local Gram form

\[
 F(u)=\sum_\gamma z_\gamma e^{-i\gamma u},
 \qquad
 \lambda z_\gamma=\int_E e^{i\gamma u}F(u)\,du,
\tag{116.2}
\]

with normalization \(\sum_\gamma|z_\gamma|^2=1\).  There is no
\(d_\gamma^{1/2}\) change of variables in (116.2).  These formulas and the
two separate theorems are stated in [Bombieri's paper](https://paperzz.com/doc/7088948/remarks-on-weil-s-quadratic-functional-in-the-theory-of-p...).

### 116.1 Consequence for the zero-collapse branch

When the Section-11 limit has \(\lambda=0\), the source equation reduces to
the local null relation \(F=0\) on \(E\), together with the unweighted
normalization and the off-critical mass inequality.  Under the separate
finite-exception hypothesis, the eventual-mesh theorem and the Kadec
construction of Round 115 give a critical Riesz-basis representation on every
fixed finite interval.  The short-interval estimate in Round 30 then gives,
for a finite conjugate off-line packet \(h_E\), a critical coefficient vector
\(c\in\ell^2\) with

\[
 S_Cc=-h_E\quad\text{on }E,
 \qquad \|c\|_2<\|e_E\|_2
\tag{116.3}
\]

after shrinking \(E\), where \(e_E\) is the off-critical coefficient
vector.  The combined vector \((c,e_E)\), after normalization, therefore
satisfies the source's off-critical half-mass orientation while its local
waveform vanishes.  This is a conditional compatibility result for the
theorem-level Section-11 limit conditions; it is not an assertion that the
finite eigenvector sequence selects this particular representation.

### 116.2 Why the weighted target cannot close Section 11 by itself

The operator

\[
 A q=\sum_{\gamma\in\Gamma_C}
 \frac{q_\gamma}{\sqrt{d_\gamma}}e^{-i\gamma u}
\tag{116.4}
\]

and the dual inequality (103.6) belong to the weighted coordinate model
(116.1).  A proof that a packet is outside \(\operatorname{Ran}A\) would
exclude a weighted representation, but it would not exclude an unweighted
Section-11 null state unless a separate theorem identifies the two finite
problems, their selected eigenvectors, and their norm constraints.  Round 28
already records that no such bridge has been derived.

**Established:** the source equations, normalizations, and limiting null
conditions for Sections 8--10 and Section 11 are different; (116.4) cannot be
silently substituted for (116.2).  The conditional local unweighted null
state remains compatible with the displayed Section-11 limit conditions.

**Failure / missing step:** no source-faithful finite-Section-11 provenance
theorem excludes the selected null branch, and no proved bridge transfers the
weighted range nonmembership problem to that branch.

**Route decision:** treat (103.6) as an auxiliary weighted-model target only;
the source-faithful load-bearing alternatives are a finite-eigenvector
provenance obstruction or an independent global Weil-positivity theorem.

**RH status:** no unconditional proof has been produced.

## Ledger erratum — placement of Round 117 (canonical end marker)

The Round 117 text appears earlier in this append-only record because the first
insertion matched an earlier generic status line.  The later placement note is
the canonical end marker: read Round 117 after Round 116.  The record is
append-only; no earlier mathematical entry is overwritten.

**RH status:** no unconditional proof has been produced.
