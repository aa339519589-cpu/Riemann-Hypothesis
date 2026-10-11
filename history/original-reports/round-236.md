## Round 236 — A/B result: Tope v7's central pair inequality is algebraically false

**Source inspected:** C. A. B. Tope, *Proof of the Riemann Hypothesis via
the Tope Operator: Uniqueness, nullity of \(G(f_{b_*})\), and contradiction*,
Zenodo record
<https://zenodo.org/records/20208426>, Version 7, PDF pp. 2–5.

The load-bearing Lemma 2 claims that for every
\(a\in(0,1/2)\), \(\sigma\in(0,1)\), and \(\delta\in\mathbb R\), the
contribution of a functional-equation pair is strictly negative:
\[
\frac{a-\sigma}{(a-\sigma)^2+\delta^2}
+\frac{a-(1-\sigma)}{(a-(1-\sigma))^2+\delta^2}<0.
\]
Its displayed algebraic identity is correct, but the asserted sign is not.
For the explicit values
\[
a=\frac14,\qquad \sigma=\frac1{10},\qquad \delta=0,
\]
the left side equals
\[
\frac{0.15}{0.15^2}+\frac{-0.65}{(-0.65)^2}
=\frac{20}{3}-\frac{20}{13}
=\frac{200}{39}>0.
\]
Equivalently, in the manuscript's notation \(u=0.15\), \(v=-0.65\),
so \((2a-1)(uv+\delta^2)>0\), not \(<0\). The claimed “case analysis”
therefore does not hold for all \(\sigma\) and \(\delta\).

This is not a harmless endpoint issue. If an off-line zero with real part
\(\sigma=1/10\) and ordinate \(b_*\) existed, its reflected partner would
have the same ordinate, so \(\delta=b_*-b_*=0\); at \(a=1/4\) this pair
would contribute positively to the logarithmic derivative. Thus the
manuscript has no termwise negativity theorem from which global monotonicity
of \(|\xi(a+ib_*)|\) can be inferred.

Lemma 3 and Corollary 4 consequently do not follow. Without the claimed
uniqueness of the real part function \(f_{b_*}(a)=\operatorname{Re}
\zeta(a+ib_*)\), the Tope integral formula cannot be applied in the form
\(G(f_{b_*})=a_*-1/2\). The later use of the functional equation to force a
second root and then identify it with the first root depends precisely on
that missing uniqueness. The finite numerical tables only test already
known on-line zeros and cannot replace the false universal inequality.

The kernel antisymmetry \(G(-f)=-G(f)\) and the elementary conditional Tope
integral identity may hold under their stated orientation/unique-zero
hypotheses, but those hypotheses are not established for the hypothetical
off-line zero. Therefore Theorem 6 and Corollary 7 do not provide an
unconditional RH proof.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
