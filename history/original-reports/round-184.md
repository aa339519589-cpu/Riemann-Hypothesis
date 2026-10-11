## Round 184 — the projection-valued-defect/GNS route supplies valid algebra, but keeps the arithmetic inputs open

I continued the current version of the defect route:

<https://zenodo.org/records/20635632>

The source explicitly presents itself as a conditional structural reduction.
Its useful contribution is to separate three logically different tasks:
null-pair gauge compensation (NGC), faithful prime-side norm--GNS
factorization (FANG), and the determinant realization of the completed
\(\xi\)-function.  NGC alone is not positivity, and the paper does not claim
that it is.

Several operator identities in the bounded setting are valid and can be
retained.  If a shifted root \(K'\) satisfies
\[
 (K')^2=K_P-I,\qquad A=K'+J,
\]
then the factorization defect
\[
 \Delta_{K'}:=K_P-AA^*
 =A(K'-K'^*)
 \tag{184.1}
\]
is self-adjoint whenever the products are defined.  If a bounded
self-adjoint operator \(T\) is nilpotent, \(T^q=0\), its spectrum is
\(\{0\}\), hence \(T=0\).  Therefore the conditional implication
\[
 \Delta_{K'}\in\mathcal N,\qquad \mathcal N^q=\{0\}
 \Longrightarrow
 \Delta_{K'}=0
 \Longrightarrow
 K_P=A A^*
 \tag{184.2}
\]
is correct in the bounded common-algebra setting.  The pure-skew calculation
is also exact: if \(K'=JB\), \(B=B^*\), and \(BJ=JB\), then
\[
 K_P=I-B^2,\qquad
 \Delta_{K'}=-2B(B+I).
 \tag{184.3}
\]
Vanishing of the defect gives \(B=-P\), \(P=P^*=P^2\), and
\(K_P=I-P\succeq0\).  These are useful lemmas for any future construction.

The missing step is not this algebra but the arithmetic construction of the
hypotheses.  Hypothesis 7.3 requires a shifted root \(K'\) built from the
prime channel, the archimedean contribution, and functional-equation
symmetry, plus a defect ideal \(\mathcal N\) built before the closure
argument, with a uniform nilpotence exponent.  The source gives no
prime-side definition of \(K'\), no generators or multiplication table for
\(\mathcal N\), no proof that \(\mathcal N\) is an ideal in the relevant
operator/form algebra, and no proof that its power vanishes.  Defining
\(\mathcal N\) after observing the particular defect would be circular; the
non-circularity condition is correctly stated but not discharged.

The GNS step has the same separation.  If the genuine prime Weil form
\(W_P\) already has a faithful square-norm representation
\[
 W_P(g^\sharp*f)=\langle A_Pf,A_Pg\rangle,
 \tag{184.4}
\]
then quotienting by its null space and completing does give a Hilbert space.
If translations preserve the form and are strongly continuous, Stone's
theorem gives a self-adjoint generator.  But (184.4) is precisely a
global faithful positivity/factorization statement for the prime-side Weil
kernel; NGC changes auxiliary channels while preserving \(K_P\), so it cannot
establish (184.4) by itself.  Strong continuity and the required translation
invariance also have to be proved for the completed quotient, not assumed
from the test-function space.

The spectral-pencil portion gives another valid conditional lemma.  For a
self-adjoint \(H\) and \(t=\tau+J\eta\), the source obtains
\[
 P_{\rm CRE}(t)^*P_{\rm CRE}(t)
 =
 \bigl((H-\tau I)^2+\eta^2I\bigr)\otimes I_2.
 \tag{184.5}
\]
For \(\eta\ne0\), this operator is bounded below by \(\eta^2\), so its kernel
is zero, provided the unbounded products and domains are defined in the
standard way.  This proves the off-axis exclusion for the pencil itself.
It does not identify the zeros of \(\Xi(t)=\xi(\tfrac12+it)\) with the
zero set of that pencil.

That identification is isolated by the source as Hypothesis 9.5:
\[
 |\Xi(t)|^2
 =
 E(t,\bar t)\,
 \det_{\zeta}\!\left(P_{\rm CRE}(t)^*P_{\rm CRE}(t)\right),
 \qquad E(t,\bar t)\ne0.
 \tag{184.6}
\]
Equation (184.6) is the load-bearing trace-formula/explicit-formula
comparison, not a consequence of (184.5).  In infinite dimension the
\(\zeta\)-regularized determinant requires a specified compact-resolvent or
relative-trace-class framework, a choice of regularization, and control of
the nonvanishing factor \(E\).  None of those data are produced by the
off-axis coercivity calculation.

The direct continuation of this route is therefore constructive: define the
actual prime kernel and shifted root independently of zero ordinates; build
the nilpotent ideal before evaluating the defect; verify all boundedness,
closure, and form-domain conditions; prove strong continuity of the GNS
translations; and derive (184.6) from the Weil explicit formula with complete
normalization and multiplicity control.  The valid nilpotent-collapse and
off-axis-coercivity lemmas remain available throughout, while FANG, nilpotent
confinement, and the CRE determinant identity remain to be supplied.

**Established:** the bounded self-adjoint-nilpotent collapse, the
factorization-defect identities (184.1)--(184.3), and the formal off-axis
coercivity identity (184.5) are valid under their stated operator-domain
assumptions.  The arithmetic construction of those assumptions and the
determinant identity (184.6) are not yet present.

**Remaining load-bearing statement:** construct the faithful prime-side
shifted root and pre-specified nilpotent defect ideal, extend the identities
to the relevant unbounded forms, and prove the exact CRE
\(\zeta\)-regularized determinant identity.  Keep this route active alongside
the Fredholm, CM-potential, Bombieri, Shimizu, Weil, Thorin, and
arithmetic-coding routes.

**RH status:** no unconditional proof has been produced.
