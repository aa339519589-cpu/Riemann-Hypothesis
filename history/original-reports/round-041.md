## Round 41 — direct countermodel to the real-locus topology argument

I audited *A Proof of the Riemann Hypothesis via the Real Locus of the
Riemann--Siegel \(\Xi\)-Function*, Zenodo record 20805270. The verdict is
**不成立**. Its central topological inference is false even for very regular
entire functions with the symmetries used in the manuscript.

### I. The local cross does not prevent a transverse zero

Consider

\[
 F(z)=(1+16z^2)\cos z.
\tag{41.1}
\]

This is an even, real entire function of order one. It has infinitely many
real zeros from \(\cos z\), but also the non-real zeros
\(z=\pm i/4\). At \(c=0\),

\[
 F(0)=1,\qquad F'(0)=0,
\qquad F''(0)=31\ne0.
\]

Writing \(z=u+iv\), the real locus near \(0\) has the same local cross
structure as in the manuscript: the leading imaginary part is a nonzero
multiple of \(uv\), with the real axis and the imaginary axis as the two
branches. Nevertheless, on the transverse branch,

\[
 F(iy)=(1-16y^2)\cosh y,
\tag{41.2}
\]

which vanishes at \(y=\pm1/4\). Thus a transverse real-locus branch can
contain a non-real zero. The manuscript's monotonicity proof silently handles
the case of a positive local maximum on the real axis, but (41.1) has a
positive local minimum at the starting critical point; its asserted “symmetric”
case does not yield the required one-sided monotonicity.

### II. The topological pairing claim is invalid

At a cross \(xy=0\), the union of two rays from different axes is a connected
set homeomorphic to an interval. A corner is not a topological obstruction to
being an interval. Therefore the statement that a connected component “cannot
switch” from one local line to the other because the switched set is not
homeomorphic to an interval is false. At a singular point, the real-analytic
zero set is a graph of analytic half-branches; connectedness alone does not
select a pairing of those half-branches into a globally continued transverse
curve.

The manuscript also treats the whole real locus as a single real-analytic curve,
although it is singular at every critical point. The local cross description
does not provide the global branch-selection theorem that the proof requires.

### III. The localization step is unproved

The claim that every non-real zero lies on a transverse component issuing from a
real critical point uses the assertion that every non-real component of
\(\{\Im F=0\}\) must meet the real axis. Noncompactness only says that a
component is unbounded; it does not imply that it intersects the real axis.
The Riemann--Siegel asymptotic cited in the manuscript is not converted into a
global intersection or endpoint theorem. Hence Proposition 9 does not follow.

The maximum-principle argument for a hypothetical closed loop, even if valid
for that loop, rules out only compact components with the specified boundary; it
does not rule out unbounded components containing non-real zeros, as (41.1)
demonstrates for the proposed local mechanism.

**Exact break:** the local cross geometry supplies neither a no-switch theorem
for singular analytic sets nor a theorem that all non-real components meet the
real axis. Equation (41.2) is an explicit countermodel to the claimed
transverse nonvanishing conclusion.

**RH status:** no unconditional proof has been produced.
