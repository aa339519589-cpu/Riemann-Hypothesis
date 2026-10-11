## Round 211 — A/B result: Tope v1's algebraic pair inequality has an explicit counterexample

**Source inspected:** Cheikh Ahmadou Bamba Tope, *Proof of the Riemann
Hypothesis via the Tope Operator*, Zenodo record
<https://zenodo.org/records/20208426>, PDF pp. 2--4.

The proof's Lemma 2 claims that for every
\(a\in(0,\frac12)\), \(\sigma\in(0,1)\), and \(\delta\in\mathbb R\),
\[
\frac{a-\sigma}{(a-\sigma)^2+\delta^2}
+\frac{a-(1-\sigma)}{(a-(1-\sigma))^2+\delta^2}<0
\]
apart from the stated special case.  This sign assertion is false.  Take
\[
a=\frac14,\qquad \sigma=\frac9{10},\qquad \delta=0.
\]
Then \(u=a-\sigma=-\frac{13}{20}\), \(v=a-(1-\sigma)=\frac3{20}\), and
\[
\frac{u}{u^2}+\frac{v}{v^2}
=-\frac{20}{13}+\frac{20}{3}
=\frac{200}{39}>0.
\]
Equivalently, the manuscript's numerator
\((2a-1)(uv+\delta^2)\) is positive in this allowed case because
\(2a-1=-\frac12\) and \(uv=-\frac{39}{400}\).

Therefore the claimed pairwise negativity in Lemma 2 does not hold for an
off-critical zero pair with matching ordinate.  Lemma 3's strict
monotonicity of \(|\xi(a+ib_*)|\), Corollary 4's uniqueness of a zero of
\(\Re\zeta(a+ib_*)\), and the subsequent Tope-operator contradiction all
depend on this false inequality.  The finite numerical table cannot repair
an algebraic counterexample.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
