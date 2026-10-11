## Round 24 — the weighted critical synthesis has dense nonclosed range

The condition in Round 23 is substantially stronger than ordinary local
completeness. This can be made precise at the operator level.

### I. Correctness decision

**成立 (operator-theoretic range classification under the finite-exception
hypothesis).**

Let \(\Gamma_C\) be the distinct critical ordinates and, on
\(I=(-t,t)\), define

\[
 A q
 =
 \sum_{\gamma\in\Gamma_C}
 \frac{q_\gamma}{\sqrt{d_\gamma}}e^{-i\gamma u},
 \qquad
 d_\gamma=\frac14+\gamma^2.
\]

The column corresponding to \(\gamma\) has squared \(L^2(I)\)-norm
\(2t/d_\gamma\). The zero-count bound gives

\[
 \sum_{\gamma\in\Gamma_C}\frac1{d_\gamma}<\infty.
\]

Hence \(A:\ell^2(\Gamma_C)\to L^2(I)\) is Hilbert--Schmidt, and in particular
compact. It has infinite rank because any finite collection of distinct
exponentials is linearly independent on \(I\). Therefore

\[
 \operatorname{Ran}A
 \quad\text{is not closed in }L^2(I).
\tag{24.1}
\]

Under the finite-exception hypothesis, the distinct critical ordinates have
eventual mesh tending to zero. The resulting zero set has more than linear
growth on arbitrarily long scales, whereas the Fourier transform of a compactly
supported \(L^2\) function is an entire function of finite exponential type.
Thus, if \(g\in L^2(I)\) satisfies \(A^*g=0\), its Fourier transform vanishes
on all critical ordinates and must be identically zero. Consequently

\[
 \overline{\operatorname{Ran}A}=L^2(I).
\tag{24.2}
\]

Equations (24.1)--(24.2) show that weighted critical synthesis is dense but not
onto. In particular, for an exceptional waveform \(h\), the assertion

\[
 h=Aq\quad\text{for some }q\in\ell^2
\]

is a genuine compact-range membership statement; it does not follow from the
unweighted exact-range theorem or from density.

For finite sections \(A_N\), the decomposition used in Round 23,

\[
 h=A_Nq_N+r_N,
\]

therefore requires both a bounded weighted coefficient cost and a
scale-sensitive residual estimate. The latter is not a cosmetic strengthening:
the resolvent multiplier has size \(1/(2\sqrt{\varepsilon_N})\) on its worst
singular mode.

### II. Hostile audit

Compactness alone does not say whether the particular finite-dimensional
exceptional waveform belongs to \(\operatorname{Ran}A\); it only rules out a
general surjectivity claim. Likewise, (24.2) relies on the finite-exception
zero-density/mesh input and establishes density, not exact weighted
representability.

The statement does not address infinitely many off-critical zeros. It is a
finite-exception branch result and cannot be promoted to full RH without a
separate argument excluding the infinite-exception case.

### III. Next-route decision

**Route X:** characterize \(\operatorname{Ran}A\) for the actual critical zero
set and prove the finite-section rate in (23.2) for every exceptional direction
selected by (20.4).

**Route Y:** construct a nontracial arithmetic observer that avoids the
nonclosed weighted-range problem.

The next concrete test for Route X is now exact: determine whether the
exceptional exponential packet lies in the weighted critical range and, if so,
obtain approximation tails at the \(\sqrt{\varepsilon_N}\) scale.

### IV. Ledger update

**Established:** the weighted critical synthesis is compact, infinite-rank,
dense-range, and nonclosed; ordinary local density does not supply the weighted
range or rate required by the Schur argument.

**Failure / error:** replacing the compact-range membership and rate condition
by unweighted exact synthesis, closure, or an unspecified \(o(1)\) residual.

**Still assumed / unknown:** weighted range membership of the exceptional
waveform and the required finite-section rate.

**Next route:** prove or refute that membership/rate statement using the
nonharmonic Fourier structure of the critical ordinates.

**RH status:** no unconditional proof has been produced.
