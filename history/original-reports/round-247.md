## Round 247 — A/B result: Pavesi's real-locus proof reverses the local behavior at transverse critical points

**Source inspected:** Luca Eliseo Pavesi, *A Proof of the Riemann
Hypothesis via the Real Locus of the Riemann-Siegel \(\Xi\)-Function*, Zenodo
record <https://zenodo.org/records/20805270>, version v3.0, PDF pp. 3--6.
Downloaded source SHA-256:
159f29290b528931926543b2b913148209ee9927bef83df8643336ec256eeb32.

The manuscript's key Proposition 8 and Theorem 1 claim that when a
transverse real-locus branch passes through another nondegenerate critical
point \(t_*\), the values of \(\Xi\) on the two opposite rays are both
directions of growth (or both of decay), so monotonicity cannot change.
The local expansion used in the manuscript gives the opposite conclusion.

Let \(v\) be the tangent direction of the same analytic branch through
\(t_*\), and use a signed local coordinate \(q\) with \(t=t_*+qv+O(q^2)\).
Since \(\Xi'(t_*)=0\) and \(\Xi''(t_*)\ne0\), while the branch lies in
\(\operatorname{Im}\Xi=0\), its leading real restriction has the form
\[
\Xi(t_*+qv)=\Xi(t_*)+\frac12\Xi''(t_*)v^2q^2+O(q^3),
\]
with a nonzero real quadratic coefficient. Differentiating along the
oriented branch gives
\[
\frac{d}{dq}\Xi(t_*+qv)=\Xi''(t_*)v^2q+O(q^2).
\]
This derivative changes sign as \(q\) passes through \(0\). The critical
point is therefore a local extremum of the real restriction, not a point
through which the restriction remains monotone. Replacing the tangent angle
by \(\varphi+\pi\) leaves the quadratic *value* unchanged, but it does not
leave the first derivative unchanged; the missing sign change is exactly the
error in the manuscript's argument.

Thus Theorem 1 does not follow, and the claimed exclusion of zeros on every
transverse curve fails. Independently, Proposition 9 asserts without proof
that every unbounded component of the real locus containing a nonreal zero
must connect to the real axis through a real critical point; noncompactness
alone does not imply such a connection. Consequently the final RH inference
has an unproved load-bearing localization step in addition to the explicit
monotonicity error.
monotonicity error.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
