## Round 134 — a direct finite-cutoff sign countercheck targets Proposition 6.1

The printed statement of Proposition 6.1 says that \(q_X\) is nonnegative
for every \(X>1\) and every \(F\in C_c^\infty(\mathbb R)\) in the paper's
class.  If \(1<X<2\), then \(P_X=\varnothing\), so Definition 6.1 reduces to
\[
 q_X(F,F)=D_\infty(F).
\]
The cited Connes–Consani archimedean theorem does not assert this universal
claim: its local positivity statement is made with a restricted support
interval and Mellin/Fourier vanishing conditions, and the paper itself
describes an archimedean obstruction outside that setup.  Thus the scope of
the citation must be checked independently of the unconstructed vector
\(\eta_X\).

As a direct diagnostic, take
\[
 F(u)=e^{-u^2/(2\sigma^2)}\cos(\gamma u)\,\chi(u),
 \qquad \sigma=\tfrac12,\quad \gamma=3.25,
\]
where \(\chi\in C_c^\infty(\mathbb R)\) equals \(1\) on \([-3,3]\), equals
zero outside \([-4,4]\), and uses the standard smooth exponential transition
on the two boundary strips.  This is an admissible real compactly supported
smooth test function.  Evaluating the displayed Definition 3.2 integral
from the manuscript using the autocorrelation
\[
 C_F(a)=\int_{\mathbb R}F(u+a)F(u)\,du
\]
and independently refining the correlation grid gives
\[
\begin{array}{c|c}
\text{grid spacing }h & \text{computed }D_\infty(F)\\
\hline
0.004 & -0.249968116088\\
0.002 & -0.249968116126\\
0.001 & -0.249968116129\\
0.0005& -0.249968116129
\end{array}
\]
The calculation uses the exact compact support of \(F\), FFT correlation, and
quadrature of the two finite \(a\)-integrals; the values stabilize to much
more precision than is needed to see the negative margin.

This table is intentionally recorded as a numerical diagnostic, not as a
formal interval-arithmetic proof.  It nevertheless gives a high-margin,
reproducible target for a rigorous countercheck: an interval enclosure of
the same compact integral, together with continuity of \(D_\infty\) under
smooth compactly supported approximation, would contradict the universal
finite-cutoff positivity assertion.  Even before that final interval
certificate, the result shows why the cited restricted archimedean theorem
cannot be silently substituted for Proposition 6.1.

**Established:** for \(1<X<2\), the claimed finite positivity is exactly the
unqualified positivity of \(D_\infty\); the cited local theorem has narrower
hypotheses.

**Diagnostic countercheck:** a compact \(C^\infty\) test with a stable
computed value near \(-0.249968116129\) conflicts with that unqualified
claim, subject to formal interval verification.

**Remaining load-bearing statement:** either produce a rigorous interval
certificate for this sign and thereby refute Proposition 6.1 as printed, or
give the missing hypotheses that exclude this test and then prove positivity
under those hypotheses.  In the latter case, the excluded directions still
have to be handled by the global Weil criterion.

**RH status:** no unconditional proof has been produced.
