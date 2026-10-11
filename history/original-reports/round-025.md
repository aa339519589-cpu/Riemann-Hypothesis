## Round 25 — exact spectral characterization of the weighted-range target

The compact weighted synthesis from Round 24 supplies an exact criterion for
the infinite-dimensional version of the remaining approximation problem.

### I. Correctness decision

**成立 (spectral criterion for the ideal weighted operator).**

Let \(A:\ell^2(\Gamma_C)\to L^2(I)\) be the weighted critical synthesis from
Round 24 and put \(T=AA^*\). For an exceptional waveform \(h\in L^2(I)\), define
the regularized coefficient vector

\[
 x_\varepsilon=A^*(T+\varepsilon I)^{-1}h.
\]

Let \(\nu_h\) be the spectral measure of \(T\) associated with \(h\). The
singular-value identity gives

\[
 \|x_\varepsilon\|_2^2
 =
 \int_{(0,\infty)}
 \frac{\lambda}{(\lambda+\varepsilon)^2}\,d\nu_h(\lambda).
\tag{25.1}
\]

Since the weighted critical synthesis has dense range, \(h\) has a weighted
critical representation \(h=Aq\) if and only if

\[
 \int_{(0,\infty)}\frac{1}{\lambda}\,d\nu_h(\lambda)<\infty.
\tag{25.2}
\]

In that case the left side of (25.2) is the squared norm of the minimum
\(\ell^2\) representation \(q\), and (25.1) remains uniformly bounded as
\(\varepsilon\downarrow0\). Conversely, monotone convergence in (25.1) shows
that uniform boundedness of the regularized coefficient vectors forces (25.2).

The regularized waveform residual is

\[
 r_\varepsilon
 =h-T(T+\varepsilon I)^{-1}h
 =\varepsilon(T+\varepsilon I)^{-1}h,
\]

so

\[
 \|r_\varepsilon\|_2^2
 =
 \int_{(0,\infty)}
 \frac{\varepsilon^2}{(\lambda+\varepsilon)^2}\,d\nu_h(\lambda).
\tag{25.3}
\]

If \(h=Aq\), the elementary bound

\[
 \frac{\varepsilon\sqrt{\lambda}}{\lambda+\varepsilon}
 \leq\frac{\sqrt{\varepsilon}}2
\]

implies

\[
 \|r_\varepsilon\|_2
 \leq \frac{\sqrt{\varepsilon}}2\,\|q\|_2.
\tag{25.4}
\]

Thus the infinite-dimensional analogue of (23.2) has a complete
characterization: weighted range membership gives bounded coefficient cost and
the required \(\sqrt{\varepsilon}\) residual rate automatically.

### II. Hostile audit

The finite-section problem is not automatically identical to the ideal
operator: \(A_N\) changes with \(N\), and no operator-norm convergence
\(A_N\to A\) at the scale \(\varepsilon_N\) has been proved. Therefore
(25.2)--(25.4) do not by themselves establish the finite-section estimate
(23.2).

Conversely, the unweighted exact-range theorem says nothing about (25.2).
Because \(A\) is compact with nonclosed range, a generic \(L^2\) waveform can
be approximated arbitrarily well while its regularized coefficient cost
diverges. This is precisely the failure mode that the finite-\(N\) Bombieri
branch must distinguish.

The spectral criterion is also conditional on a finite exceptional packet. It
does not treat infinitely many off-critical zeros and is not an RH proof.

### III. Next-route decision

**Route X:** identify the spectral measure \(\nu_h\), or an equivalent
nonharmonic-Fourier/de Branges representation, for each exceptional waveform
and prove (25.2) together with finite-section stability at
\(\varepsilon_N\).

**Route Y:** prove that at least one exceptional waveform violates (25.2), which
would close the Bombieri finite-exception branch by ruling out the required
representative. This is a genuine refutation target, not a proof of RH by
itself.

**Route Z:** construct a nontracial arithmetic observer that bypasses the
weighted range.

### IV. Ledger update

**Established:** (25.2) is exactly equivalent to bounded regularized weighted
coefficient cost for the ideal critical operator, and it implies the
\(\sqrt{\varepsilon}\) residual estimate (25.4).

**Failure / error:** inferring (25.2) from unweighted local synthesis, density,
or finite-section residual convergence without scale control.

**Still assumed / unknown:** the spectral measure of the actual exceptional
waveform and stability of (25.2) under Bombieri's finite sections.

**Next route:** compute or characterize \(\nu_h\) using the explicit critical
zero set; test membership before attempting any RH conclusion.

**RH status:** no unconditional proof has been produced.
