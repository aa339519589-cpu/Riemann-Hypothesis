## Round 231 — A/B result: Kubalalika's off-line-zero disproof fails in the exponential-sum step

**Source inspected:** T. Kubalalika, *The Riemann Hypothesis Is False*,
Cambridge Open Engage preprint, DOI
<https://doi.org/10.33774/coe-2026-jt6vl>, pp. 3–8; comparison with the
standard uniform Landau--Gonek formula reproduced in B. Durkan, C. Hughes,
and A. Pearce-Crump, *Generalisations of the Landau--Gonek Theorem*,
<https://arxiv.org/abs/2601.18025>, Theorem 2.

The first suspected defect in Lemma 2 is not, by itself, decisive. For
integer \(n\), the uniform Landau--Gonek estimate, after division by \(n\),
has an error of the order

\[
O\!\bigl(\log(2ny)\log\log(3n)\bigr)
\]

up to the other standard terms. On Kubalalika's range
\(n\le y/\log^2 y\), this particular error sums to
\(O(y\log\log y/\log y)=o(y)\). Thus Lemma 2 cannot be rejected solely by
quoting the uniform formula; its actual use must be audited elsewhere.

The fatal gap is earlier, in equations (20)--(25). Equation (19) has an
interval \([\alpha_m-\eta,\beta_m+\eta]\) depending on \(m\). The paper then
writes a single \(v\) in (20)--(22), although no common \(v\) exists across
the full \(m\)-range: the relevant derivative

\[
\phi_m'(x)=\frac{T}{2\pi(m+x)}
\]

varies from order \(1\) to order \(\log^2T\) as \(m\) runs from
\(T/\log^2T\) to \(T\). A valid argument would have to partition the \(m\)'s
and retain the resulting \(v\)-dependence. No such argument is supplied.

More directly, the displayed estimate (22) is false even for the
unweighted sum that it actually displays. Put \(x=T^{1/4}\),
\(V=T/((1+\varepsilon)\log^2T)\), and

\[
S(T)=\sum_{V\le m\le T(1+\varepsilon)}
\exp\!\left(iT\log\!\left(1+\frac{x}{m}\right)\right).
\]

The factor \(e^{-2\pi ivx}\) in (22) has modulus one and is independent of
\(m\). Since \(x/m=o(1)\) on this range, Euler summation followed by one
integration by parts (or the substitution \(u=Tx/m\)) gives

\[
S(T)=\frac{T}{x}\,c_T+o\!\left(\frac{T}{x}\right),\qquad |c_T|=1,
\]

because the upper endpoint contributes \(T/x=T^{3/4}\), while the lower
endpoint is smaller by a factor \(\log^4T\) and the sum--integral error is
\(O(x\log^2T)\). Consequently

\[
|S(T)|\gg T^{3/4},
\]

whereas (22) asserts \(S(T)\ll T^{1/2}\log^2T\). These bounds are
incompatible as \(T\to\infty\).

There is a second independent bookkeeping failure: the factor
\(\Lambda(m)\) present in (17) is omitted in (20)--(23) and then restored in
(25). An estimate for the unweighted exponential sum does not imply the
corresponding \(\Lambda(m)\)-weighted estimate; partial summation or a
weighted exponential-sum theorem is required and is absent. Therefore
(23), and hence the transition through (25)--(57), is not proved. The
claimed contradiction under \(\Theta<1\) does not establish an off-line zero.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
