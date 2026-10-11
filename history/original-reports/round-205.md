## Round 205 — A/B result: Abe v26's zero-free-region proof loses a factor in (5.5)

**Source inspected:** work/abe-audit/abe-v26.pdf, pp. 15--16,
DOI <https://doi.org/10.33774/coe-2022-d3nj5-v26>.

Write \(R=R(s)\), \(I=I(s)\), and retain the paper's \(\alpha,\beta\).
On the second circle, \(I^2=\frac{1}{\alpha}R-R^2\).  The tangent line
displayed in the paper is \(Y=\frac{\frac{1}{2\alpha}-R}{I}(X-R)+I\).
Setting \(Y=0\) therefore gives
\(X_B=R-\frac{I^2}{\frac{1}{2\alpha}-R}\).
Equation (5.5) instead prints
\(X_B=R-\frac{I}{\frac{1}{2\alpha}-R}\); the numerator must be \(I^2\),
not \(I\).

This is an exact algebraic failure, not a numerical objection.  For
\(\alpha=4,\beta=1\), the nonzero intersection of the two displayed
circles is \(P=(R,I)=(4/17,1/17)\).  The paper's displayed formula for
\(A\) gives \(A=(0,-17/255)\), hence \(PA=4/15\).  Its printed formula
(5.5) gives \(X_B=196/255\), whereas the tangent-line equation gives
\(X_B=4/15\).  Thus the printed \(OB\) is \(196/255\), not \(PA=4/15\);
the asserted equality (5.3) does not follow from the printed coordinates.

The error propagates directly into (5.6).  With the correct intersection
coordinate, the squared relation corresponding to (5.3) has right-hand
side \(-2(\frac{1}{\alpha}-R)/(\frac{1}{2\alpha}-R)
+(\frac{1}{\alpha}-R)^2/(\frac{1}{2\alpha}-R)^2\).  Equation (5.6)
instead uses \(-2\sqrt{\frac{1}{\alpha R}-1}/(\frac{1}{2\alpha}-R)
+(\frac{1}{\alpha R}-1)/(\frac{1}{2\alpha}-R)^2\).  These expressions
are different.

For the asymptotics used in the paper,
\(\alpha\sim t^2\), \(\beta=(2\sigma-1)t\), and
\(\frac{1}{\alpha}-R=\frac{(2\sigma-1)^2}{t^4}+O(t^{-5})\), while
\(\frac{1}{2\alpha}-R=-\frac{1}{2t^2}+O(t^{-4})\).  The correct
right-hand side is consequently of order \(t^{-2}\), matching the
left-hand side, rather than producing the order-\(t^2\) contradiction
claimed from the erroneous square-root expression.  Proposition 1 and
Theorem 1 are therefore not proved, so the subsequent argument for RH has
no valid zero-free-region input.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
