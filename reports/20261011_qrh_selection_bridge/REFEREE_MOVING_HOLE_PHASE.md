# Independent exact-identity review: moving-hole CRT phase

## Verdict

**The displayed phase-free identity (13) in [QUADRATIC_DUAL_N1.md at 07ed84c](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/07ed84c4d0a560125d12b9ed5700600c04285dd8/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md), Part XXVII B §6, is missing a phase and is false as an exact signed identity.** With the definitions stated immediately above it, the correct formula has an additional outside factor \(\bar\rho_u(d)\):

\[
R_{(u,M)}(s)=\sum_{d\mid M_0}\mu(d)G(d)\chi_0(d)\,\bar\rho_u(d)(Nd)^{-s}R_{ud}(s).
\]

Here \(R_{(u,M)}\) is \(R_u\) with the common hole \((A,M)=1\), and \(M_0\) is supported away from \(6Lu\), so every such \(d\) is coprime to \(u\). The phase cannot be folded into \(\chi_0(d)\): the public definition gives \(R_u\) the coefficient \(G(A)\chi_0(A)\bar\rho_u(A)\), and \(\chi_0\) is the fixed character with its own presentation primes and does not include the moving character modulo \(u\).

## Coefficientwise derivation

Inclusion-exclusion gives

\[
R_{(u,M)}(s)=\sum_{d\mid M_0}\mu(d)(Nd)^{-s}
 \sum_{B\ \mathrm{primary}}G(dB)\chi_0(dB)\bar\rho_u(dB)(NB)^{-s}.
\]

For \((d,B)=1\), the normalized DR Gauss CRT convention is
\[
G(dB)=G(d)G(B)\bar\rho_d(B).
\]
The same identity extends to the full sum: if \((d,B)>1\), then \(\bar\rho_d(B)=0\), while \(G(dB)=0\) because \(dB\) is non-squarefree and the DR cube identity gives \(G(dB)^3=\mu(dB)\alpha(dB)=0\). Multiplicativity on the allowed unit support gives
\[
\chi_0(dB)=\chi_0(d)\chi_0(B),\qquad
\bar\rho_u(dB)=\bar\rho_u(d)\bar\rho_u(B).
\]
Since \((u,d)=1\), the residual character is
\(\bar\rho_u(B)\bar\rho_d(B)=\bar\rho_{ud}(B)\). Substitution yields the corrected identity above. The factor \(\bar\rho_u(d)\) comes specifically from splitting the pre-existing moving coefficient \(\bar\rho_u(dB)\); it is independent of the Gauss-CRT cross factor \(\bar\rho_d(B)\).

## Direct counterexample to the phase-free formula

For a transparent admissible instance, take \(\chi_0=\psi_4\rho_2\) with trivial odd and lambda components. The period defining \(\Phi_0\) also includes the primary condition modulo 3, so take \(L=12\), whose 2-part is exactly 4. Now take
\[
u=-2-3\omega,\qquad d=1+6\omega.
\]
Both are primary and squarefree, \(Nu=7\), \(Nd=31\), and both are coprime to \(6L\). In \(\mathbb Z[\omega]/(u)\), \(\omega\equiv4\pmod 7\), so \(d\equiv4\pmod u\) and
\[
\rho_u(d)=(d/u)_3\equiv d^{(7-1)/3}=d^2\equiv 2\equiv\omega^2\pmod u,
\quad\text{hence}\quad \bar\rho_u(d)=\omega\ne1.
\]
Set \(M_0=d\). The coefficient at \(A=d\) on the left is zero because it violates the hole. In the proposed phase-free right side, the \(d'=1\) term contributes \(G(d)\chi_0(d)\bar\rho_u(d)(Nd)^{-s}\); the \(d'=d\) term contributes \(-G(d)\chi_0(d)(Nd)^{-s}\), since the coefficient of \(B=1\) in \(R_{ud}\) is one. Their sum is nonzero. With the corrected outside factor, these terms cancel exactly. This is an exact coefficient mismatch, not a choice of convention for \(\chi_0\).

The CRT and zero statements used here match Dunn–Radziwiłł's primary cubic reciprocity and normalized Gauss-sum conventions, equations (1.4) and (1.7)–(1.8): [Dunn–Radziwiłł, *Bias in cubic Gauss sums*](https://arxiv.org/html/2109.07463v3). The companion public review is `REFEREE_CUBIC_MOVING_ROOT_PHASE.md` (with local notes in [REFEREE_CUBIC_MOVING_ROOT_PHASE.md](REFEREE_CUBIC_MOVING_ROOT_PHASE.md)); it uses the same chirality: its \(G\)-row moving scalar is \(\bar G(u)\bar\rho_u(c_0)\), so the hole factor here is likewise conjugated when the moving coefficient is \(\bar\rho_u\). The public counterpart for this hole-phase review is `REFEREE_MOVING_HOLE_PHASE.md`.

## Quantitative consequence and occurrence scan

The omission does **not** change the stated hole bound. On every allowed divisor \(d\), \(|\bar\rho_u(d)|=1\). Applying the bound for \(R_{ud}\) still contributes \((N(ud))^{1/4}=U^{1/4}(Nd)^{1/4}\); after the outside \((Nd)^{-s}\), the divisor weight is still
\[
(Nd)^{1/4-\sigma}\le (Nd)^{-1/4-\epsilon}
\quad (\sigma\ge1/2+\epsilon),
\]
and its squarefree divisor sum remains \(O_\epsilon((NM)^\epsilon)\). Thus Part XXVII B's norm estimate and its claimed common-hole cost survive after correcting the exact identity.

The public Part XXVII B display (13) is the only occurrence of the exact \(R_{(u,M)}\) identity found in the report. The separate cube-free moving theorem in [CUBIC_CUBE_FREE_MOVING.md](CUBIC_CUBE_FREE_MOVING.md), “Common holes and conjugation,” already retains the corresponding outside CRT phase: it explicitly records \(\bar\vartheta_{A_1A_2^2}(d)\) among the unit-modulus factors while moving \(d\) into the squarefree first part. Its bound is therefore consistent with this correction. The earlier squarefree common-hole estimate records a coefficient mask and does not display a competing exact CRT identity.

No RH claim follows from this local correction.
