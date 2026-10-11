## Round 100 — the finite-\(S\) trace formula does not give the claimed global Weil norm

I audited Velez's six-page v5 manuscript [*A proof of the Riemann Hypothesis*](https://zenodo.org/records/21184595) and compared its decisive Proposition 6.1 / Appendix D with Connes' original trace-formula paper [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068).

The manuscript defines the completed form
\[
Q_{\rm arith}(F)=D_\infty(F)-2\sum_{p^k}\log p\,p^{-k/2}C_F(k\log p)
\tag{100.1}
\]
and then claims that, for \(X\) larger than the support radius, there is a Hilbert space \(H_X\), a vector \(\Phi_X(F)\), and the exact identity
\[
Q_{\rm arith}(F)=q_X(F,F)=\|\Phi_X(F)\|_{H_X}^2.
\tag{100.2}
\]
The support observation only proves the algebraic stabilization \(q_X=Q_{\rm arith}\): the omitted prime-power summands vanish because \(C_F\) has compact support. It does not prove positivity of \(q_X\), nor does it construct a norm representation.

The sole justification for (100.2) is Appendix D's asserted equation
\[
\langle U_X(g_F)\eta_X,U_X(g_G)\eta_X\rangle
=P_{\rm pole}(h_{F,G})-W_\infty(h_{F,G})
-2\sum_{p^k\le X}\log p\,p^{-k/2}C_{F,G}(k\log p).
\tag{100.3}
\]
But \(\eta_X\) is only described as a “cutoff-renormalized completed vacuum vector”; no vector, normalization, projection, or convergence construction is supplied. The cited semilocal theorem is a trace formula for the finite set of places \(S_X\), not a theorem that the proposed vector coefficient has the global pole-minus-archimedean value in (100.3). In particular, the manuscript does not derive (100.3) from the cited theorem or control the pole projection and the cutoff-renormalization terms. Equation (100.3) is therefore the missing positivity assertion written in inner-product notation.

This is not a harmless presentation gap. Connes' paper states that the \(S\)-local trace formula is proved for every finite set of places, while the corresponding global trace formula is left open; it further identifies that global statement with the Riemann-hypothesis condition. A finite-\(S_X\) formula cannot be promoted to (100.3) merely because the particular prime sum has finite support. The archimedean/pole completion and the global Hilbert-space projection are exactly the nonlocal part that remains to be established.

Thus Theorem 7.1,
\[
Q_{\rm arith}(F)\ge0,
\]
does not follow. The final appeal to Weil's criterion is valid only after this unproved global positivity statement has been supplied. The manuscript has not closed the RH-bearing step; it has renamed it as the existence of \(\eta_X\) satisfying (100.3).

**Established:** support exhaustion gives a stabilized algebraic expression, but not a positive Hilbert-space representation.

**Failure / missing step:** prove the global norm identity (100.3), including construction and normalization of \(\eta_X\), rather than invoking the finite-\(S\) trace formula.

**Route decision:** discard this as a completed RH proof. Continue the source-faithful Bombieri weighted-null-cone analysis.

**RH status:** no unconditional proof has been produced.
