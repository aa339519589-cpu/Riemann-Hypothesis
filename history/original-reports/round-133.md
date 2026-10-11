## Round 133 — Velez's completed-kernel factorization assumes the missing positive vector

I audited Velez, *A Proof of the Riemann Hypothesis by Positivity of the
Completed Arithmetic Weil Kernel* ([Zenodo record](https://zenodo.org/records/21173721)),
especially Proposition 6.1, Lemma 7.1, and Theorems 8.1–9.1.  The manuscript
claims that the completed arithmetic form is positive for every cutoff and
then passes to the full kernel.

The load-bearing step is Proposition 6.1.  It defines
\[
 q_X(F,G)=\langle L_{\rm arch},C_{F,G}\rangle
 -2\sum_{k\log p\le\log X}(\log p)p^{-k/2}C_{F,G}(k\log p)
\]
and asserts the existence of a Hilbert space vector \(\eta_X\) satisfying
\[
 q_X(F,G)=\langle U_X(g_F)\eta_X,U_X(g_G)\eta_X\rangle.
\]
The text calls \(\eta_X\) a “cutoff-renormalized completed vacuum vector”
and refers to a semilocal trace construction, but gives no definition that
can be checked in \(H_X\), no cutoff convergence estimate, and no proof that
the finite-part subtraction and pole projection produce the displayed
matrix coefficient.  The finite graph energy appearing earlier in the paper
does not repair this: it has a divergent diagonal
\[
 E_T(F)=2W_T\lVert F\rVert_2^2
 -2\sum_{(p,k)\in T}(\log p)p^{-k/2}C_F(k\log p),
\]
whereas \(q_X\) replaces that diagonal by the archimedean finite-part term.
That replacement is exactly the renormalized trace-to-vector identity that
must be proved; positivity of the unrenormalized graph energy does not imply
positivity of the renormalized form.

The cited Connes finite-place theorem does not supply the missing identity.
For a finite set of places it gives an asymptotic cutoff trace with a
divergent term of the form
\[
 \operatorname{Trace}(R_\Lambda U(h))
 =2h(1)\log'\Lambda+\text{finite local terms}+o(1),
\]
not an exact finite-\(X\) pole-compressed vector whose matrix coefficients
are \(q_X\).  The manuscript's sentence that pole projection “collapses”
the terms is therefore an assertion of the required bridge, not a proof of
it.

Lemma 7.1 has a second independent issue.  For fixed compactly supported
\(F,G\), the omitted prime-power tail in the scalar pairing does tend to
zero; this establishes pointwise convergence of the scalar forms on those
tests.  It does not by itself establish convergence of the positive measures
\(\mu_X\) in \(\mathcal S'(\mathbb R)\).  Passing from convergence on the
claimed products \(\widehat F\widehat G\) to all Schwartz test functions
requires a uniform temperedness/equicontinuity bound for \(\mu_X\), or an
equivalent uniform seminorm estimate for \(q_X\).  No such bound is proved.
Pointwise convergence on a dense family of test functions is not a substitute
for this uniform control.  Moreover, identifying
\(d\mu_{\rm arith}=(2\pi)^{-1}\widehat L_{\rm arith}(t)\,dt\) as a positive
measure is the conclusion sought; it cannot be used before the distributional
limit and its positivity have been established.

Consequently, Theorem 8.1 depends on the unproved positivity and limit
claims, and Theorem 9.1 merely applies Weil's criterion after those claims
are assumed.  The manuscript's finite algebraic decompositions are useful,
but they do not close the global arithmetic-to-Hilbert-space bridge.

**Established:** the explicit-formula decomposition and the fixed-test
prime-power tail convergence are valid under the stated test class.

**Failure / missing lemmas:** construct \(\eta_X\) and prove its exact
matrix-coefficient identity; prove uniform tempered bounds needed for the
measure limit; and establish positivity without presupposing the completed
Weil form.

**Remaining load-bearing statement:** prove Proposition 6.1 from an
independent semilocal construction, including all renormalization and pole
projection limits.  Without that proposition, the claimed positive spectral
factorization and the RH conclusion are circular.

**RH status:** no unconditional proof has been produced.
