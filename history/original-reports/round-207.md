## Round 207 — A/B result: Kubalalika v2 cannot apply its Dirichlet-polynomial approximation on the contour

**Source inspected:** Tatenda Kubalalika, *The Riemann Hypothesis is
false*, Version 2, pp. 1--4,
<https://www.cambridge.org/engage/coe/article-details/6a64c69c810b9dcc82785f56>.

Under the assumption \(\Theta<1\), the manuscript sets \(N=T/\pi\) and
uses the rectangular contour whose imaginary coordinate ranges over
\(t\in[T,2T]\).  Its Lemma 2.1, however, explicitly requires the
Dirichlet-polynomial cutoff \(x\) to satisfy
\[
x>\frac{C|\operatorname{Im}z|}{2\pi}
\qquad\text{for a fixed }C>1.
\]
In the proposed application \(z=1-s\), so
\(|\operatorname{Im}z|=|t|\), and \(x=N=T/\pi\).  At the upper horizontal
side \(t=2T\), the required inequality becomes
\[
\frac{T}{\pi}>\frac{C(2T)}{2\pi}
\quad\Longleftrightarrow\quad 1>C,
\]
which contradicts the lemma's \(C>1\).  Thus the approximation (4.2) is
not established uniformly on the contour.

The subsequent reduction of the contour integrand in (4.3), the estimate
(4.6), and Proposition 4.1 all depend on (4.2).  Therefore the claimed
\(O(T^{1/2}(\log T)^2)\) upper bound is not proved.  The order-\(T\)
lower estimate in Theorem 4.2 cannot contradict an unproved upper bound,
so the claimed conclusion \(\Theta=1\) and the disproof of RH do not follow.
This is a direct failure of a stated analytic hypothesis, independent of
any numerical calculation.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
