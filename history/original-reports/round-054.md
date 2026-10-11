## Round 54 — the tangent-intercept error in Abe v26

I audited the latest version-26 manuscript
(\url{https://www.cambridge.org/engage/coe/article-details/6a52f0d3810b9dcc82011b00}).
The load-bearing geometric identity leading to its Proposition 1 contains a
missing square.

At a putative zero, the manuscript has

\[
 R=\alpha(R^2+I^2),\qquad I=\beta(R^2+I^2),
\tag{54.1}
\]

so the second circle is

\[
 (X-\tfrac1{2\alpha})^2+Y^2=\tfrac1{4\alpha^2},
 \qquad
 I^2=\tfrac{R}{\alpha}-R^2.
\tag{54.2}
\]

The tangent line \(\ell_2\) displayed in the manuscript is

\[
 Y=
 \frac{\tfrac1{2\alpha}-R}
 {\sqrt{\tfrac{R}{\alpha}-R^2}}\,(X-R)+I.
\tag{54.3}
\]

Setting \(Y=0\) in (54.3) gives the \(x\)-intercept

\[
 B_x
 =
 R-\frac{I^2}{\tfrac1{2\alpha}-R}
 =
 R-\frac{\tfrac{R}{\alpha}-R^2}
 {\tfrac1{2\alpha}-R},
\tag{54.4}
\]

not the manuscript's equation (5.5), which uses

\[
 R-\frac{\sqrt{\tfrac{R}{\alpha}-R^2}}
 {\tfrac1{2\alpha}-R}.
\tag{54.5}
\]

The distinction is not cosmetic. Take any \(\sigma\in(\tfrac12,1)\),
\(t>0\), set

\[
 s=\sigma+it,\quad
 \alpha=t^2-\sigma(\sigma-1),\quad
 \beta=(2\sigma-1)t,\quad
 \Phi=-\frac1{s(s-1)}.
\tag{54.6}
\]

Then \(R=\operatorname{Re}\Phi\) and \(I=\operatorname{Im}\Phi\) satisfy
(54.1) exactly, so they are an exact non-origin intersection of the two
circles used in the manuscript. With the correct intercept (54.4), direct
substitution gives \(OB=PA\), as the elementary orthogonal-circle geometry
requires. With the manuscript's intercept (54.5), the equality fails. For
\(\sigma=\tfrac34\) and \(t=100\), the two sides are

\[
 PA\approx1.0000062495703157\cdot10^{-4},
 \qquad
 OB_{\mathrm{printed}}\approx1.0100058120941425\cdot10^{-2}.
\tag{54.7}
\]

The ratio is approximately \(101\), not \(1\). The correct formula (54.4)
restores equality, but it produces a different algebraic equation from the
manuscript's (5.6). Therefore the proof of Proposition 1 does not follow,
and Theorem 1's claimed fixed-\(\sigma\) zero-free region, as well as the
final supremum argument, is unsupported by this version.

**Established:** the integral representations and the two circle equations
do not imply the displayed equation (5.6); equation (5.5) is algebraically
wrong.

**Failure / error:** the missing factor of \(I(s)\) breaks the only step that
turns the asymptotic expansions into a zero-free region.

**RH status:** this candidate is not an unconditional proof.
