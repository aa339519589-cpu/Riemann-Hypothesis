## Round 23 — a weighted approximation-at-the-eigenvalue-scale criterion preserves exceptional mass

The Schur analysis now yields a concrete sufficient theorem rather than only a
diagnosis. It converts the unresolved branch-specific transversality question
into a weighted finite-section approximation estimate.

### I. Correctness decision

**成立 (as a finite-\(N\) sufficient criterion).**

Let \(S_{C,N}\) be the critical synthesis map into \(L^2(I)\), let
\(D_{C,N}=\operatorname{diag}(d_\gamma)\) with
\(d_\gamma=\frac14+\gamma^2\), and set

\[
 A_N=S_{C,N}D_{C,N}^{-1/2}.
\]

For a unit exceptional direction \(v\), write \(h_{N,v}\) for the associated
exceptional waveform in the local \(L^2(I)\) space. The kernel identities give

\[
 G_{CC,N}=S_{C,N}^*S_{C,N},\qquad
 G_{CE,N}v=S_{C,N}^*h_{N,v},
\]

and therefore

\[
 R_N(\varepsilon)
 :=(G_{CC,N}+\varepsilon D_{C,N})^{-1}G_{CE,N}
 \]

satisfies

\[
 R_N(\varepsilon)v
 =
 D_{C,N}^{-1/2}
 (A_N^*A_N+\varepsilon I)^{-1}A_N^*h_{N,v}.
\tag{23.1}
\]

Suppose that for the exceptional directions \(v_N\) selected by the Schur
equation there are \(q_N\) and residuals \(r_N\) such that

\[
 h_{N,v_N}=A_Nq_N+r_N,
\qquad
 \sup_N\|q_N\|_2\leq Q,
\qquad
 \|r_N\|_2\leq C\sqrt{\varepsilon_N}.
\tag{23.2}
\]

Because \(d_\gamma\geq\frac14\),
\(\|D_{C,N}^{-1/2}\|\leq2\). The spectral theorem gives

\[
 \left\|
 A_N^*(A_NA_N^*+\varepsilon I)^{-1}A_N
 \right\|\leq1,
\qquad
 \left\|
 A_N^*(A_NA_N^*+\varepsilon I)^{-1}
 \right\|\leq\frac1{2\sqrt{\varepsilon}}.
\]

Using (23.1)--(23.2), it follows that

\[
 \|R_N(\varepsilon_N)v_N\|_2
 \leq 2Q+C.
\tag{23.3}
\]

Combining (23.3) with the exact normalization identity (21.1) yields

\[
 \|e_N\|_2^2
 =
 \frac{1}{1+\|R_N(\varepsilon_N)v_N\|_2^2}
 \geq
 \frac{1}{1+(2Q+C)^2}.
\tag{23.4}
\]

Thus (23.2) is sufficient to prevent exceptional mass from disappearing along
the selected negative branch.

### II. Hostile audit

The estimate is finite-\(N\) and branch-specific. It is not supplied by the
unweighted exact-range theorem: that theorem gives a critical representation
but neither a uniform \(D_{C,N}^{1/2}\)-weighted coefficient bound nor the
\(\sqrt{\varepsilon_N}\) residual rate.

The residual scale in (23.2) is essential. An \(o(1)\) residual can still be
much larger than \(\sqrt{\varepsilon_N}\), in which case the resolvent factor
\(1/\sqrt{\varepsilon_N}\) can diverge. Likewise, a bound for one fixed
exceptional direction does not suffice if the finite exceptional eigenspace
has dimension greater than one; the estimate must hold uniformly for the
directions \(v_N\) selected by (20.4).

The criterion also does not prove that the required \(q_N,r_N\) exist for the
zeta critical ordinates. It is a valid target theorem, not an RH proof.

### III. Next-route decision

**Route X:** prove (23.2) for the actual exceptional waveform family, using the
critical zero distribution and the explicit sine kernel. This would imply the
nonzero exceptional limit required by the Bombieri finite-exception route.

**Route Y:** construct a nontracial arithmetic observer that avoids the weighted
finite-section approximation problem.

Route X is now reduced to a precise weighted nonharmonic-Fourier estimate:
uniform coefficient cost \(Q\) and approximation error at the exact scale
\(\sqrt{\varepsilon_N}\).

### IV. Ledger update

**Established:** the weighted approximation condition (23.2) implies the
uniform resolvent bound (23.3), which implies the explicit exceptional-mass
lower bound (23.4).

**Failure / error:** replacing (23.2) by unweighted \(L^2\) exact synthesis or
by an unspecified \(o(1)\) residual loses the resolvent-scale control.

**Still assumed / unknown:** whether the actual critical zero set admits
(23.2) for the finite exceptional waveform family and Bombieri's
\(\varepsilon_N\)-branch.

**Next route:** establish or refute the weighted approximation/rate estimate
(23.2) from the explicit zero spacing and kernel; retain the nontracial route
as competitor.

**RH status:** no unconditional proof has been produced.
