# Audit of quantitative prime-two gamma-depth obstruction

Date: 2026-10-12. Internal analytic audit of QUANTITATIVE_PRIME_TWO_GAMMA_DEPTH.md. This result concerns the specified lower comparator, not RH.

The full Jacobi theta identity has the exact factor \(m^2=4\pi^2r^2e^{-\pi r}S(r)/(1+r^{-1/2})\), with \(S(r)=\sum_{n\ge1}n^4(1-3/(2\pi n^2r))e^{-\pi(n^2-1)r}\), r=e^(2x). On r>=4 all terms are positive; the n=1 term gives \(m^2>\pi^2r^2e^{-\pi r}\). Using \(n^4\le16^{n-1}\), \(n^2-1\ge3(n-1)\), and \(16e^{-12\pi}<1/2\) gives \(S(r)<2\) and \(m<4\pi r e^{-\pi r/2}\).

The same bounds at r/4 prove, for r>=16, \(m(x-\log2)/m(x)>(1/16)e^{3\pi r/8}\). Let \(b=1+|c_J-C_0|\), K=e^(6pi), and \(r=8\log(Kb)/(3\pi)\). Then r>=16 and the n=2 coefficient \(\alpha_2=\log2/\sqrt2>1/3\) yields \(\alpha_2 m(x-\log2)>2b\,m(x)\). All other retained n<=N coefficients are nonnegative for N>=2, so \(g_{J,N}(x)<-b m^2(x)\).

Substitution gives
\[
-g_-\ge b\pi^2r^2e^{-\pi r}
=\frac{64}{9}e^{-16\pi}\log(Kb)^2b^{-5/3}
\ge256\pi^2e^{-16\pi}b^{-5/3}.
\]
The original constant satisfies \(0<C_0<8\), and \(c_J\le5+\log J\), so \(b<14+\log J\). The bound is uniform in N and all expressions retain the true theta source.

The previous exact essential spectrum formula places \(\varepsilon-\delta_N+g_-\) in the comparator's essential spectrum. For epsilon below the displayed \(C_*(14+\log J)^{-5/3}\), it is strictly negative for every finite N>=2. Avoiding this obstruction requires \(\log J\ge(C_*/\varepsilon)^{3/5}-14\), excluding any fixed polynomial scaling \(J=O(\varepsilon^{-M})\).

The result supplies no sign conclusion for the original H and does not prove RH.

**Audit accepted at these quantifiers; NO NEW UNCONDITIONAL RH THEOREM PROVED.**
