## Round 70 — the real-locus proof does not control global components or crossings

I audited Luca Eliseo Pavesi's [*A Proof of the Riemann Hypothesis via the
Real Locus of the Riemann--Siegel \(\Xi\)-Function*](https://zenodo.org/records/20805270),
including the [version-3 PDF](https://zenodo.org/records/20805270/files/ipotesi_di_riemann.pdf?download=1).
The local description of a nondegenerate crossing is compatible with the
Cauchy--Riemann equations, but the global conclusions drawn from it do not
follow.

### I. A local cross does not determine a global connected branch

At a real critical point \(c\) with \(\Xi(c)\in\mathbb R\),
\(\Xi'(c)=0\), and \(\Xi''(c)\ne0\), the local equation for the real locus
\(\operatorname{Im}\Xi=0\) is indeed, after coordinates are chosen,
\[
 uv=0+O\bigl((u^2+v^2)^{3/2}\bigr).
\tag{70.1}
\]
This gives two crossing analytic branches locally. It does not make the
global real locus a one-dimensional embedded manifold, nor does it choose a
unique continuation through the crossing. The connected component of a
crossing contains the arms that meet at the critical point; it need not be
homeomorphic to an interval and need not coincide with the particular
transverse arc selected by the paper.

The assertion that a connected component cannot switch from one line to the
other therefore uses an unproved global regularity assumption. A
real-analytic set can have a singular crossing, and its connected component
can contain several analytic arcs meeting there. Saying that a corner is not
an embedded analytic curve does not prove that the connected component has
to be an embedded curve.

### II. The local quadratic model contradicts the claimed monotonicity through a crossing

Let a selected transverse arc pass through another critical point and use a
signed local parameter \(s\) along the same analytic line. The expansion has
the form
\[
 \operatorname{Re}\Xi(\gamma(s))
 =U_*+Cs^2+O(s^3),\qquad C\ne0.
\tag{70.2}
\]
Its derivative is
\[
 \frac{d}{ds}\operatorname{Re}\Xi(\gamma(s))
 =2Cs+O(s^2),
\tag{70.3}
\]
so the sign reverses as the arc crosses \(s=0\). The fact that the two
opposite rays have the same *change in value* \(Cs^2\) does not mean that the
oriented derivative has the same sign on the incoming and outgoing rays.
Indeed, a gradient trajectory cannot pass through a stationary point in the
finite-time way assumed by the proof; the vector field vanishes there and
the usual uniqueness/energy behavior must be handled separately.

Thus Proposition 8 does not establish the premise used in Theorem 1, namely
that the function along a global transverse arc is monotone. The sign of the
initial quadratic term at \(c\) says nothing about later critical points on
the component.

### III. Noncompactness does not imply attachment to the real axis

The localization proposition asserts that a nonreal zero lies on a transverse
curve emanating from some real critical point. Its proof argues that the
component containing the zero cannot be compact and therefore “must connect”
to the real axis through a critical point. This is a non sequitur:
\[
 \text{noncompact connected component}
\ \not\Longrightarrow\
 \text{component intersects the real axis}.
\tag{70.4}
\]
A real-analytic component may be an unbounded curve contained entirely in the
upper half-plane. Even an asymptotic approach to the real axis would not be an
intersection with it. The paper proves neither a classification of all
components of \(\Xi^{-1}(\mathbb R)\) nor a theorem forcing every nonreal
component to meet a real critical point.

The preceding “no return” argument only addresses a curve that is already
known to start at a real critical point; it cannot be reversed to classify
all nonreal components. The claimed asymptotic direction from a brief appeal
to the Riemann--Siegel formula is also not a proof of such a classification.

**Established:** the Cauchy--Riemann calculation gives the local cross at a
nondegenerate real critical point.

**Failure / error:** local crossing geometry is promoted to a global
single-branch theorem; the quadratic crossing model does not preserve an
oriented monotonicity; and noncompactness is incorrectly used to force
attachment to the real axis.

**Remaining load-bearing statement:** prove that every component of
\(\Xi^{-1}(\mathbb R)\) containing a nonreal zero attaches to a real critical
point and remains a globally monotone embedded arc, including all degenerate
critical points and all behavior at infinity. The preprint supplies neither
result.

**RH status:** no unconditional proof has been produced.
