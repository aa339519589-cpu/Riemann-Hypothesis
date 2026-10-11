## Round 106 — the real-locus proof fails at the claimed monotonicity and component topology

I audited Pavesi's six-page manuscript [*A Proof of the Riemann Hypothesis via the Real Locus of the Riemann--Siegel \(\Xi\)-Function*](https://zenodo.org/records/20805270). The basic facts about \(\Xi\), its real locus \(\{\Im\Xi=0\}\), and the local Cauchy--Riemann calculation are valid where their stated nondegeneracy hypotheses hold. The global conclusion does not follow.

The decisive error is Proposition 8 / Theorem 1. Let \(c\in\mathbb R\) satisfy \(\Xi'(c)=0\), \(\Xi(c)\in\mathbb R\setminus\{0\}\), and \(\Xi''(c)=A\in\mathbb R\setminus\{0\}\). On the transverse branch \(t=c+iv\), the Taylor expansion is
\[
\Xi(c+iv)=\Xi(c)-\frac{A}{2}v^2+O(v^3),
\qquad
\Re\Xi(c+iv)=\Xi(c)-\frac{A}{2}v^2+O(v^3).
\tag{106.1}
\]
Thus \(c\) is a strict local extremum of \(\Re\Xi\) along the transverse curve. If the curve is parametrized through \(c\) with \(v=s\), then
\[
\frac{d}{ds}\Re\Xi(c+is)=-As+O(s^2),
\tag{106.2}
\]
whose sign is opposite on the two sides of \(s=0\). The fact that the two rays both increase away from a local minimum (or both decrease away from a local maximum) does not make the function monotone along the connected curve passing through the critical point. The manuscript's inference that “straight through” preserves the sign of the gradient is therefore false. A gradient line reaching a nondegenerate critical point changes its oriented direction; \(f'(s)=\pm|\nabla\Re\Xi|\) does not have a globally fixed sign.

There is a second independent gap in Proposition 9. Showing that a real-locus component is noncompact does not show that it meets the real axis at a finite point. A component can remain in the upper half-plane and escape to infinity. The assertion that it “must connect to the real axis through a critical point” is not a consequence of noncompactness or of the claimed asymptotic direction. Proposition 6 supplies no rigorous exclusion of oscillating/unbounded components, no properness statement, and no finite endpoint argument.

Finally, the local argument is only stated for \(\Xi(c)\ne0\) and \(\Xi''(c)\ne0\). The manuscript does not prove that every real critical point is nonzero and nondegenerate, nor does its one-sentence higher-order remark classify the real-analytic branches at degenerate critical points or at multiple real zeros. Those are precisely possible attachment points for a hypothetical off-axis zero component. The maximum-principle loop argument also presupposes that a transverse branch and a real-axis segment form a simple closed Jordan loop; this is not established for an arbitrary component.

**Established:** local descriptions of the real locus under explicit noncritical/nondegenerate hypotheses.

**Failure / missing step:** global monotonicity across critical points, the connection of every off-axis component to the real axis, and the treatment of degenerate/multiple critical points are unproved; (106.1)--(106.2) directly contradict the claimed sign preservation.

**Route decision:** reject this as an RH proof. The failure is independent of the Bombieri range question and leaves the unconditional zero exclusion unresolved.

**RH status:** no unconditional proof has been produced.
