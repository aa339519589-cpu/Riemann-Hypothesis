## Round 44 — correction: Fatou restores weighted-ℓ² membership, but not norm conservation

The statements in Rounds 42--43 that the Section 10 coordinate limit need not
belong to \(\ell^2\), and that the displayed toy sequence is a countermodel to
the full Section 10 compactness conclusion, were too strong and are withdrawn.
The finite vectors can be extended by zero outside \(\Gamma_N\). If

\[
 w_{\gamma;N}\longrightarrow w_\gamma
 \quad\text{for each fixed }\gamma,
 \qquad
 \sum_{\gamma\in\Gamma}|w_{\gamma;N}|^2=1,
\tag{44.1}
\]

then Fatou's lemma gives

\[
 \sum_{\gamma\in\Gamma}|w_\gamma|^2
 \leq
 \liminf_{N\to\infty}\sum_{\gamma\in\Gamma}|w_{\gamma;N}|^2
 =1.
\tag{44.2}
\]

Moreover, under the finite-exception hypothesis the off-critical set is finite,
and Bombieri's finite-dimensional inequality gives

\[
 \sum_{\gamma\notin\mathbb R}|w_{\gamma;N}|^2\geq\frac12.
\tag{44.3}
\]

Passing to the coordinate limit on this finite set yields

\[
 \sum_{\gamma\notin\mathbb R}|w_\gamma|^2\geq\frac12,
 \qquad
 \frac1{\sqrt2}\leq\|w\|_2\leq1.
\tag{44.4}
\]

Thus the limiting vector is nonzero and is genuinely in \(\ell^2\), although
the equality \(\|w\|_2=1\) is not justified: critical mass may escape to
infinity. Since \(d_\gamma=\tfrac14+\gamma^2\geq\tfrac14\), the sequence

\[
 q_\gamma=\frac{w_\gamma}{\sqrt{d_\gamma}}
\]

also lies in \(\ell^2\), and the limiting synthesis has the form

\[
 Z(u)=\sum_{\gamma}\frac{q_\gamma}{\sqrt{d_\gamma}}e^{-i\gamma u}.
\tag{44.5}
\]

This means that the ideal weighted \(\ell^2\) range framework in Rounds
24--27 is relevant to the actual extracted limit. The missing statement is
not weighted \(\ell^2\) membership; it is one of the following equivalent
source-faithful closures:

\[
\begin{array}{ll}
\text{(a)}&\text{prove that the nonzero finite-exception packet cannot satisfy
               the local relation }F=0;\\[2mm]
\text{(b)}&\text{prove that its boundary-corrected waveform is outside the
               weighted critical range;}\\[2mm]
\text{(c)}&\text{prove finite-section tightness strong enough to retain the
               source's negative branch with }\lambda<0.
\end{array}
\tag{44.6}
\]

The explicit Fourier example in Round 43 remains a valid warning only about
the pointwise bound (42.5) considered in isolation: its constant weighted
coefficients are not in \(\ell^2\), so it is not a counterexample to (44.2).
The precise conclusion is that Fatou removes the alleged \(\ell^2\)-membership
gap but does not remove the nontrivial local-relation/range-membership gap.

**Established:** the Section 10 subsequence has a nonzero weighted-ℓ² limit
with at least half of its mass on the finite off-critical set; only total-norm
conservation is lost.

**Failure / correction:** the earlier claim that coordinate extraction alone
permits a non-ℓ² limit was false because it omitted Fatou's lemma.

**Remaining load-bearing statement:** exclude the nonzero weighted-ℓ² local
relation (44.6a)--(44.6b), or establish the corresponding source-faithful
finite-section lower bound. No such exclusion has yet been derived for the
actual zeta ordinates.

**RH status:** no unconditional proof has been produced.
