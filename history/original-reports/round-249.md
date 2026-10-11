## Round 249 — A/B result: Abe's circle-tangent calculation drops a factor and invalidates its zero-free region

**Source inspected:** Yukitaka Abe, *A Rigorous Proof of the Riemann
Hypothesis*, Cambridge Open Engage DOI
<https://doi.org/10.33774/coe-2022-d3nj5-v26>, version 26, PDF pp. 15--18.
Downloaded source SHA-256:
128a8e156b0f47cca587c9ec57c01406979c0e1c2c45b6fe88430645f824ea55.

The manuscript derives two circles from the necessary equations for a zero,
then claims in (5.3)--(5.6) that a tangent-length identity yields a
necessary algebraic condition. The calculation of the \(X\)-axis intercept
of the tangent to the second circle is incorrect.

Write \(r=R(s)\), \(i=I(s)\), and
\[
d=\sqrt{\alpha^{-1}r-r^2}.
\]
The tangent line printed in the manuscript is
\[
Y=\frac{\frac1{2\alpha}-r}{d}(X-r)+i.
\]
Setting \(Y=0\) gives, by direct algebra,
\[
X_B=r-\frac{i\,d}{\frac1{2\alpha}-r}.
\]
Under the manuscript's circle equations \(i^2=\alpha^{-1}r-r^2\);
in its chosen high-\(t\) region \(i>0\), so \(d=i\) and therefore
\[
X_B=r-\frac{i^2}{\frac1{2\alpha}-r}.
\]
But equation (5.5) in the manuscript writes
\[
X_B=r-\frac{d}{\frac1{2\alpha}-r},
\]
omitting the multiplicative factor \(i\). This is not a
notation issue: the two expressions differ by a factor \(i\), which is
not identically \(1\). Consequently the asserted equality \(PA=OB\)
does not produce equation (5.6). The asymptotic contradiction in Section 6
therefore rests on a condition that has not been derived from
\(\xi(s)=0\).

The later Dirichlet-series argument depends on that unsupported zero-free
region to show that the supremal real part of a zero cannot be attained.
Thus neither the claimed zero-free region nor the final RH conclusion is
established; no finite calculation changes this algebraic failure.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
