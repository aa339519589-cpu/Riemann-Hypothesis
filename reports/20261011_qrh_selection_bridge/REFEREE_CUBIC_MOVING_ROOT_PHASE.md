# Independent bounded review: moving radial root scalar

## Verdict

**Accepted as an arithmetic identity under the stated hypotheses.** I found no sign, λ-factor, conjugation, or Mobius-algebra correction needed in [CUBIC_MOVING_ROOT_PHASE.md](CUBIC_MOVING_ROOT_PHASE.md). The actual cusp normalizing unit is handled correctly: with `c_cusp = c0 u`, the result is `barG(u) barρ_u(c0)`; if one substitutes a primary associate for `c0`, the factor `barρ_u(ε)` must remain.

The note also keeps the bad additive CRT phase, the joint cubic kernel, and the original radial divisor condition. Its final warning is appropriate: restoring a formal `μ(c*)` does not produce an ordinary Mertens column or a bound for the pooled signed row, and it asserts no angular estimate for `Q`.

## Local phase, λ convention, and CRT

For a good primary prime `p`, write `ρ_p = χ_p^2`; then `barρ_p = χ_p^4`. The source local factor is `τ_{p,4}^- = P^(-1/2) Σ_x χ_p(x)^4 e(-x/p)`. Since `χ_p(-1)^4=1`, changing `x` to `-x` makes this equal to the normalized sum with `e(x/p)`. Now use `e(z) = check_e(z/λ)`,

\[
e(x/p)=\check e(\lambda^{-1}x/p).
\]

Rescaling the summation variable by `λ^{-1}` therefore contributes `barρ_p(λ)`. The DR sum with character `barρ_p` and additive character `check_e` equals `barG(p)`: conjugating the DR sum for `ρ_p` changes the additive sign, and replacing `x` by `-x` removes that sign because `ρ_p(-1)=1`. Thus

\[
\gamma_4(p)=\bar\rho_p(\lambda)\,\overline{G(p)}.
\]

The other local factor is

\[
\chi_p(\lambda^2c_0u/p)^{-2}
 =\chi_p(\lambda)^{-4}\bar\rho_p(c_0)\bar\rho_p(u/p).
\]

Its λ scalar cancels: `barρ_p(λ) χ_p(λ)^(-4) = χ_p(λ)^(-6) = 1`. The remaining primewise product is exactly

\[
\prod_{p\mid u}\overline{G(p)}\,\bar\rho_p(c_0)\,\bar\rho_p(u/p)
 =\overline{G(u)}\,\bar\rho_u(c_0).
\]

For the last equality, CRT applied to the DR sum gives, for coprime primary `a,b`,

\[
G(ab)=G(a)G(b)\,\bar\rho_a(b).
\]

Indeed the two CRT additive scalings contribute `ρ_a(b)ρ_b(a)`; cubic reciprocity makes these equal, and their product is `barρ_a(b)`. Iterating and conjugating gives the displayed primewise formula. This checks the direction of the cubic character as well as the conjugation.

The cited DR identity `G(u)^3=μ(u)α(u)` and squarefreeness give `|G(u)|=1`; with `Q(u)=G(u)/barG(u)=G(u)^2`,

\[
\overline{G(u)}=\mu(u)\,\bar\alpha(u)\,Q(u).
\]

So the conversion in (4) is exact. For coprime primary `c,h`, CRT gives `G(ch)=G(c)G(h)barρ_c(h)` and its conjugate has cross factor `ρ_c(h)`. Hence

\[
Q(ch)=Q(c)Q(h)\frac{\bar\rho_c(h)}{\rho_c(h)}
     =Q(c)Q(h)\rho_c(h),
\]

since the symbol has order three. Cubic reciprocity identifies `ρ_c(h)=(h/c)_3=(c/h)_3`. The split factors in (6) follow, and no extra unit or cross-character factor is missing.

## Fixed cusp data and the Ramanujan coefficient

The source's conjugated multiplier is `barκ_F ∏_{p|u} χ_p(λ²c0u/p)^(-2)`. The local calculation above identifies its moving root scalar while leaving `barκ_F` fixed on the stated `(h0, bad-sector)` block. In the source additive CRT identity, the nonconstant phase is

\[
\psi_{h_0,u}(x)=e\!\left(-\delta'_F u^{-1}x/D_F\right),
\qquad D_F=\lambda^3c_0.
\]

Both inverses are in the fixed quotient modulo `D_F`; therefore `u=ch` gives the exact factor `c^{-1}h^{-1}` in (8). This is a finite joint residue factor. It is retained in (9) and (12), not mistaken for a constant-mode phase or absorbed into a one-variable weight. The finite unit in `c0` also remains in both `D_F` and `barρ_u(c0)`.

For the sign calculation, put `c=R_c c_*`, `h=R_h h_*`, with all four pieces squarefree and the stated coprimalities. Direct multiplicativity of the Mobius function gives

\[
\frac{\mu(c)}{Nc}\,\mu(ch/R)NR
 =\frac{\mu(R_c)\mu(h_*)NR_h}{Nc_*}.
\]

Multiplying by the root scalar's `μ(u)=μ(R_c)μ(c_*)μ(R_h)μ(h_*)` leaves

\[
\mu(c_*)\mu(R_h)\frac{NR_h}{Nc_*}.
\]

Thus the formal `μ(c_*)` restoration in (11) is correct. The remaining factors in (12), especially `Q(c)Q(h)`, `(h/c)_3`, and the finite bad phase, still couple the variables; this calculation alone yields no Mertens estimate.

## Source/provenance note

The pinned QRH source's equations `reflection-local-fourier`, `reflection-cusp-fraction`, `reflection-multiplier`, and `reflection-additive-phase`, together with Part XXVII B §§3--4, support the local factor and the exact bad phases. [Dunn--Radziwiłł](https://arxiv.org/html/2109.07463v3), equations (1.4), (1.7)--(1.8), supplies cubic reciprocity, the normalized Gauss-sum convention, and the cube identity. The two-variable CRT product formula is an elementary derivation from that definition and reciprocity; describing it as derived by CRT is precise. This is a provenance clarification only, not a mathematical correction.

The review concerns only the fixed squarefree good `u` scalar and its formal compact-block deconvolution. It establishes no estimate for the pooled signed column, no angular cancellation, and no RH claim.
