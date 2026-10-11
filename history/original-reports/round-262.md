## Round 262 — A-result: the large-prime positive-part memory estimate can be completed unconditionally, but it does not close RH

This audit completes the estimate stated as Theorem 3 in the same PIHR-XV
source. For a prime \(p\), put
\[
A_p=\prod_{q<p}(1-q^{-3/2}),
\qquad
\beta_p=\zeta(1/2)\prod_{q<p}(1-q^{-1}),
\qquad
c=\frac1{\zeta(3/2)}.
\]
For \(y=x/p<p\), the exact finite Euler-state identity is
\[
\widetilde D_p(y)=u(y)+\varepsilon_p(y),
\qquad
u(y)=\frac{M(y)}{\sqrt y},
\]
with
\[
\varepsilon_p(y)=-\beta_p-(A_p-c)\sqrt y-\frac{c}{\sqrt y}.
\]
The infinite Euler product is positive and every finite partial product is
larger than its limit, so \(A_p\ge c>0\). Hence the last two terms are
nonpositive and, by subadditivity of the positive part,
\[
\widetilde D_p(y)^+
\le u(y)^++(-\beta_p)^+.
\tag{262.1}
\]

Let
\[
S(x)=\sum_{\sqrt x<p\le x}\frac1p
\widetilde D_p(x/p)^+.
\]
Theorem 2 of Round 261 gives \(u(y)\to0\). Fix \(Y>1\). For the terms
with \(x/p\ge Y\), (262.1) and Mertens' prime reciprocal estimate give
\[
\sum_{\substack{\sqrt x<p\le x\\x/p\ge Y}}
\frac1p u(x/p)^+
\le (\log2+o(1))\sup_{y\ge Y}u(y)^+.
\tag{262.2}
\]
The supremum on the right tends to zero as \(Y\to\infty\). For the
remaining terms \(x/p<Y\), one has \(p>x/Y\); since \(u\) is bounded on
the fixed compact interval \([1,Y]\), another Mertens estimate gives
\[
\sum_{\substack{\sqrt x<p\le x\\x/p<Y}}
\frac1p u(x/p)^+
\ll_Y \sum_{x/Y<p\le x}\frac1p
=O_Y\!\left(\frac1{\log x}\right).
\tag{262.3}
\]

Finally, Mertens' product theorem implies
\[
(-\beta_p)^+\ll\frac1{\log p}.
\]
Since \(p>\sqrt x\), \(1/\log p\le2/\log x\), while
\(\sum_{\sqrt x<p\le x}1/p=O(1)\). Therefore
\[
\sum_{\sqrt x<p\le x}\frac1p(-\beta_p)^+=O\!\left(\frac1{\log x}\right).
\tag{262.4}
\]
Combining (262.2)--(262.4), taking \(x\to\infty\), and then taking
\(Y\to\infty\), proves
\[
\boxed{
\sum_{\sqrt x<p\le x}\frac1p
\widetilde D_p(x/p)^+=o(1).
}
\]
This is a complete unconditional Euler-specific positive-part decay
theorem and is added to the VERIFIED PROOF CHAIN.

### Remaining RH load-bearing claim

The estimate is only an \(o(1)\) bound on a positive part. It neither gives
the signed \(x^{-1/2}\)-scale barrier \(M(x)\ge0\) nor proves the universal
recovery-witness inequality \(V_q=C_q-J_q\ge0\). Therefore it does not
close the Weil/Landau implication or the Riemann Hypothesis.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的大素数正部衰减定理，但没有产生新的无条件 RH 证明进展。
