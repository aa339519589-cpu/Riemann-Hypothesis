## Round 27 — zero counting gives the universal finite-section tail envelope

The finite-section theorem in Round 26 leaves a concrete scale question. The
zero-counting estimate supplies a universal upper envelope for the truncation
tail of the weighted critical synthesis.

### I. Correctness decision

**成立 (uniform Hilbert--Schmidt tail estimate).**

Order the critical coordinates by increasing height and let \(P_T\) retain
those with \(|\gamma|\leq T\). On \(I=(-t,t)\), the weighted synthesis column
has squared norm

\[
 \left\|\frac{e^{-i\gamma u}}{\sqrt{d_\gamma}}\right\|_{L^2(I)}^2
 =
 \frac{2t}{d_\gamma},
 \qquad
 d_\gamma=\frac14+\gamma^2.
\]

The Riemann--von Mangoldt upper bound

\[
 N_C(U)\ll U\log(2+U)
\]

and partial summation give

\[
 \sum_{|\gamma|>T}\frac1{d_\gamma}
 \ll \frac{\log(2+T)}{T}.
\tag{27.1}
\]

Hence

\[
 \|A(I-P_T)\|_{\mathrm{HS}}^2
 =
 2t\sum_{|\gamma|>T}\frac1{d_\gamma}
 \ll_t \frac{\log(2+T)}{T},
\tag{27.2}
\]

and, for every \(q\in\ell^2\),

\[
 \|A(I-P_T)q\|_{L^2(I)}
 \ll_t
 \sqrt{\frac{\log(2+T)}{T}}\;\|q\|_2.
\tag{27.3}
\]

If \(P_N\) is the first \(N\) coordinates in height order, then
\(N_C(T_N)\asymp T_N\log(2+T_N)\), so
\(T_N\asymp N/\log(2+N)\) up to constants. Therefore

\[
 \|A(I-P_N)q\|_{L^2(I)}
 \ll_t
 \frac{\log(2+N)}{\sqrt N}\,\|q\|_2.
\tag{27.4}
\]

Combining (27.4) with Round 26 shows the following sufficient scale gate:

\[
 \varepsilon_N\gg \frac{\log^2(2+N)}{N}
\tag{27.5}
\]

implies the required \(O(\sqrt{\varepsilon_N})\) tail bound for every fixed
weighted representation \(h=Aq\). Under (27.5), ideal weighted range
membership is enough to obtain the finite-section coefficient bound and
residual estimate.

### II. Hostile audit

Equation (27.5) is only a sufficient universal envelope. It is not a lower
bound on the actual Bombieri eigenvalue scale, and the known fact
\(\varepsilon_N\to0\) does not imply (27.5). If \(\varepsilon_N\) is smaller,
a particular representing vector \(q\) might still satisfy the sharper
condition

\[
 \|A(I-P_N)q\|=O(\sqrt{\varepsilon_N}),
\]

but this must be proved from the representation itself. Conversely, (27.1)
does not establish weighted range membership of an exceptional waveform.

The estimate also assumes height-ordered finite sections and treats the
finite-exception branch only. It says nothing about infinitely many
off-critical zeros or about the arithmetic selection of the negative branch.

### III. Route decision and ledger update

**Route X:** first determine whether the exceptional waveform has a weighted
representation; then compare its actual tail with \(\varepsilon_N\). The
universal threshold (27.5) is the fastest branch test, while failure of that
threshold redirects the proof to a waveform-specific tail estimate.

**Route Y:** prove a zeta-specific lower bound on \(\varepsilon_N\), or derive
the same tail estimate directly from the Schur-selected direction.

**已确认事实:** zero counting gives (27.1)--(27.4), and (27.5) is sufficient
for the finite-section rate once weighted range membership is known.

**成立点:** the tail estimate follows from the Hilbert--Schmidt norm of the
discarded weighted columns; no orthogonality assumption is used.

**失败 / 错误点:** treating the universal upper envelope as an eigenvalue
lower bound, or treating \(\varepsilon_N\to0\) as a rate.

**仍属假设:** height ordering of the finite sections matches the relevant
Bombieri truncation and the exceptional packet is finite.

**未知 / 待验证:** weighted range membership, the actual asymptotic size of
\(\varepsilon_N=-\lambda_N\), and any sharper packet-specific tail.

**下一步路线:** obtain a source-faithful estimate for \(\varepsilon_N\) or
for the exceptional packet's weighted tail, then apply (26.6)--(26.11).

**RH status:** no unconditional proof has been produced.
