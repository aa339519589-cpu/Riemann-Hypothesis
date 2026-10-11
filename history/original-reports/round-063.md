## Round 63 — critical exponentials are dense, while the weighted range is dense and nonclosed

The known positive-density theorem for simple critical zeros gives a precise
functional-analytic refinement of the remaining Bombieri problem. Bui,
Conrey, and Young define \(N_0^*(T)\) as the number of simple zeros on the
critical line up to height \(T\), and prove

\[
 \liminf_{T\to\infty}\frac{N_0^*(T)}{N(T)}\geq0.4058.
\tag{63.1}
\]

Together with the Riemann--von Mangoldt estimate
\(N(T)\asymp T\log T\), this yields a set of distinct critical ordinates
\(\Gamma_C^*\) satisfying

\[
 \#\{\gamma\in\Gamma_C^*:|\gamma|\leq T\}\gg T\log T.
\tag{63.2}
\]

For any bounded interval \(I=(-t,t)\), the unweighted exponentials
\(\{e^{-i\gamma u}:\gamma\in\Gamma_C^*\}\) are complete in \(L^2(I)\). Indeed,
if \(F\in L^2(I)\) is orthogonal to all of them, then

\[
 \widehat F(z)=\int_I F(u)e^{izu}\,du
\tag{63.3}
\]

is an entire function of exponential type at most \(t\), bounded on the real
axis, and vanishes at every \(\gamma\in\Gamma_C^*\). A nonzero Cartwright
function of this type has \(O(T)\) real zeros up to height \(T\), contradicting
(63.2). Hence \(F=0\).

This completeness result does not close (61.3). Define the actual weighted
synthesis operator

\[
 (A_Iq)(u)=\sum_{\gamma\in\Gamma_C}
 \frac{q_\gamma}{\sqrt{\tfrac14+\gamma^2}}e^{-i\gamma u}.
\tag{63.4}
\]

Using \(N(T)=O(T\log T)\),

\[
 \|A_I\|_{\mathrm{HS}}^2
 =|I|\sum_{\gamma\in\Gamma_C}
 \frac{1}{\tfrac14+\gamma^2}<\infty.
\tag{63.5}
\]

Thus \(A_I\) is Hilbert--Schmidt and therefore compact. Its finite-support
image contains the span in (63.2), so

\[
 \overline{\operatorname{Ran}A_I}=L^2(I).
\tag{63.6}
\]

The range itself is not all of \(L^2(I)\): a compact operator from an
infinite-dimensional Hilbert space cannot be onto an infinite-dimensional
Hilbert space. Consequently \(\operatorname{Ran}A_I\) is a proper dense
nonclosed subspace. The exact Bombieri relation (61.3) is therefore a
membership question for one special finite exponential packet \(h\), not a
question of completeness. Neither density nor uniqueness of the unweighted
exponentials can decide that membership.

The source for (63.1) is Bui--Conrey--Young,
*More than 41% of the zeros of the zeta function are on the critical line*:
https://arxiv.org/abs/1002.4127.

**Established:** the critical exponentials are complete on every finite
interval, while the Bombieri weighted synthesis is compact with a proper
dense range.

**Failure / error:** replacing exact weighted-range membership by
completeness, or treating dense range as surjectivity, does not exclude
(61.3).

**Unknown / next verification:** a quantitative characterization of
\(\operatorname{Ran}A_I\) for the actual zeta ordinates that rules out the
specific boundary/off-critical packet selected by Bombieri.

**RH status:** no unconditional proof has been produced.
