## Round 118 — audit of the overdetermined Weil-system claim

I checked the July 2026 preprint [*Overdetermined Weil Systems and the
Riemann Hypothesis*](https://zenodo.org/records/21218854) directly, including
its displayed construction and appendix.  The advertised proof does not
close because its admissibility/regularization step is invalid before the
linear-algebra argument begins.

### 118.1 The Fourier cutoff is not an approximation to the stated test

The preprint defines a compactly supported bump \(\varphi_\delta(t)\) with
support shrinking to \(0\), and sets

\[
 \widehat h_{n,\delta}(t)=\widehat h_n^{\rm even}(t)\varphi_\delta(t).
\tag{118.1}
\]

It then asserts \(h_{n,\delta}(z)\to h_n^{\rm even}(z)\) as
\(\delta\downarrow0\).  Multiplication by a shrinking-support factor cannot
have that limit: at every \(t\ne0\), \(\varphi_\delta(t)=0\) for all sufficiently
small \(\delta\), while the claimed target Fourier distribution is not
supported at \(\{0\}\).  If the factor is normalized by \(1/\delta\), it instead
approaches a multiple of a point mass in the distributional sense, not the
constant multiplier \(1\) required to recover \(\widehat h_n^{\rm even}\).
Thus (118.1) is not a convergent regularization of the original test family.

There is a separate Paley--Wiener reversal in the same construction.  A
\(C^\infty\) bump compactly supported in the physical variable has an entire
Fourier transform, generally not compact Fourier support.  The preprint
states the converse (“by the Paley--Wiener theorem”); that statement is false.
Even if a different cutoff were supplied, one would still need a continuity
theorem in the exact Barner test-function topology, with the zero-side limit
and the prime/Gamma terms controlled.  The displayed pointwise convergence is
not that theorem.

### 118.2 The claimed transform formula is not established

The source test contains \(1/(z\log z)\) and its even projection, with
principal-value singularities at the relevant real points and branch-cut
choices.  The preprint states, without a derivation,

\[
 \widehat h_n^{\rm even}(t)
 =\frac{\pi}{2}\mathbf 1_{[-\log n/(2\pi),\,\log n/(2\pi)]}(t)+R_n(t),
\tag{118.2}
\]

with a globally bounded \(R_n\), and then uses smoothness of the product in
(118.1).  A distributional principal-value calculation would have to specify
the contributions from both branch cuts, both singularities, and the behavior
at the endpoints of the step.  No such calculation is supplied; an assertion
that a “full contour integration derivation” is available is not a proof.
In particular, boundedness of a remainder alone would not make the product
\(\widehat h_n^{\rm even}\varphi_\delta\) \(C^\infty\), which is what the cited
Barner application requires.

### 118.3 A repairable but missing discrete lemma

The later linear-independence argument also says that the set
\(\{\log n:n\ge2\}\) has \(+\infty\) as an accumulation point and invokes the
identity theorem for an exponential polynomial.  Infinity is not a finite
accumulation point, so that invocation is invalid as written.  The underlying
claim can be repaired, but it needs a proof:

If

\[
 P(t)=\sum_{j=1}^m c_j e^{\lambda_jt},\qquad \lambda_j\ {\rm distinct},
\]

and \(P(\log n)=0\) for all sufficiently large integers \(n\), choose the
largest real part \(\alpha\) among the \(\lambda_j\).  After division by
\(n^\alpha\), the lower-real-part terms tend to \(0\), so the trigonometric
polynomial formed by the terms with real part \(\alpha\) tends to \(0\) along
\(\log n\).  Since
\(\log(n+1)-\log n\to0\) and that trigonometric polynomial is uniformly
continuous, it tends to \(0\) on the whole half-line at infinity.  Its finite
Fourier expansion then has all coefficients zero (for example by averaging its
squared modulus on long intervals).  Removing the maximal group and
inducting proves \(P\equiv0\).

This repairs only the discrete exponential-polynomial step.  It does not
repair (118.1), (118.2), or the Barner admissibility claim.  The alleged
contradiction therefore never reaches a valid Weil identity.

**Established:** the preprint's final finite-dimensional implication would be
valid if its reality constraints were first obtained for the stated
\(h_n^{\rm even}\) and if the coefficient functions were rigorously shown to
be independent.

**Failure / missing step:** the proposed regularization does not converge to
\(h_n^{\rm even}\); the stated Paley--Wiener implication is reversed; and the
principal-value transform formula is asserted rather than derived.

**Route decision:** this candidate cannot supply the arithmetic reality
constraint needed for an RH proof.  The repaired discrete lemma is retained as
an auxiliary fact only; the primary Bombieri/Weil positivity and
source-faithful null-cone gaps remain open.

**RH status:** no unconditional proof has been produced.
