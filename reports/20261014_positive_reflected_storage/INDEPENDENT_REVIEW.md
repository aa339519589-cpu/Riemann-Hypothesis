# Independent mathematical review

## Verdict and precise scope

The package proves the following unconditional pointwise inequality for the
original positive-wing theta source and the complete reflected-only prime row:

    H_kappa psi(x)+(1/2)F_r psi(x)-sinh(x/2)/2 > 1/16,
                                                   x>=0.

It also proves the resulting nonlocal storage inequality for the same actual
plateau-zero source and its finite complete Gamma-plus-prime current variance:

    S_delta >= 2 integral psi^2 Gamma_psi[u]
                       +(1/8) integral psi J_u,       0<=delta<=1/2.

These statements and the retained complete current-form identities are correct
with the normalizations and hypotheses stated in the reviewed files. The proof
does not establish positivity of the full original form or the Riemann
hypothesis. In particular the variance debit in the lifted edge forms must
not be counted again as a new positive budget.

## Checks of the proof

1. **Complete arithmetic tail.** The Stieltjes identity uses
   F(t)=exp(-t/2)psi(t), with F(0)=0 and a theta-decaying tail. Applying the
   upper Chebyshev bound where F'>0 and the lower bound where F'<0 gives
   exactly aJ-(b-a)I_plus, with J=integral exp(t/2)psi(t). The source psi
   is distinct from the Chebyshev function. The table entries .84/101 and
   .91/349, and the global upper bound 1.03883X, were checked directly in
   Rosser--Schoenfeld, printed page 71, Theorems 10 and 12. The elementary
   theta estimates J>1 and I_plus<2.93 give the claimed complete-prime
   constants 127/500 and 5291/10000. There is no finite-prime substitution
   in this analytic tail argument.

2. **Compact intervals.** Both interval certificates enclose whole cells,
   not point samples. Their prime-power sieve uses Lambda(p^k)=log p.
   Terms crossing the moving reflection boundary are omitted positively.
   The first xi summand is used only through a positive interval lower
   bound; its negative band is not declared positive. All omitted higher
   theta terms are positive on the wing. The full theta bound
   V_psi>3/5 pays the lower bound on H_kappa psi. The certified intervals
   [0,5] and [0,6] overlap the respective analytic thresholds log(101)
   and log(349). The exact rational checker and both interval checkers
   were independently executed; both generated JSON results matched
   the reviewed results byte for byte.

3. **Current domain.** The homogeneous process has generator -G_psi,
   starts at x>0, and uses the complete continuous and prime-power rates.
   Its physical-coordinate moment and occupation estimates are not
   confused with unweighted physical-coordinate Sobolev estimates.
   The shrinking logarithmic intervals and their overlap counts give
   finite expected total squared current for the actual H^s ratio,
   1/2<s<1. The signed current converges almost surely and in L2. No
   endpoint process at x=0, absolute time integral of each source term,
   or normalized-filter semigroup property is assumed.

4. **Adjoint and source factors.** The Frullani identity gives
   D0 B=0 with C0=log pi-digamma(1/4). The exact divisor relation gives
   F_+C=[C,X] and DC=CD0. The derivative commutator then yields
   Dpsi=-(3Phi+Theta/2). The odd source operator is precisely
   D+D_half*+2X+H_kappa+F_r. With T_odd psi=sinh(x/2)/2, this gives the
   displayed density b=G_psi*(psi^2). The adjoint is used as a paired
   half-line expression, not an unproved global operator-domain claim.

5. **Cutoff passage.** The bound J_u=O(1+1/x), the linear origin zero
   of psi, and the grouped continuous commutator pay the origin cutoff.
   The complete prime row and theta tail pay the infinity cutoff.
   Resolvent duality followed by these cutoffs justifies
   integral psi^2 Gamma_psi[u]=integral b J_u, including its signed
   right-hand side. This is not inferred from a merely formal equation
   G_psi J_u=Gamma_psi[u].

6. **Full-form accounting.** The polar normalization integral sinh(x/2)
   psi(x)dx=1/8 gives the factor 4 in the positive pole edge measure.
   The independent-current edge lifts add respectively
   integral s psi J_u, 2 integral psi H_kappa psi J_u, and
   2 integral psi F_r psi J_u. Substitution gives the stated full h
   and Q_delta identities. In particular the delta-adjusted storage
   contains H_kappa psi+(1-delta)F_r psi-s/2, not the full reflected
   row with its delta debit omitted. The half-row inequality therefore
   covers the whole stated range delta<=1/2, including the cited
   three-halves Green range.

## Limitations that remain essential

The pointwise coefficient K0-x psi changes sign. Its integrated storage is
positive only after the exact same-source occupation identity is used.
The remaining expression is

    P_ray-H_ray-(1-delta)N_ray+S_delta.

No comparison between these three edge forms follows merely from their
individual nonnegativity. Their added product-current variance is exactly
-2 integral psi[H_kappa psi+(1-delta)F_r psi-s/2]J_u, which cancels the
corresponding storage term on returning to the original unlifted form.
Thus the proved result signs a genuine component without closing the
original signed comparison. Polynomially growing neutral-corrected ratios
are not included in the plateau-zero infinite-ray assertion.

## Exact reviewed versions

SHA-256:

- `REPORT.md`: `b6b34db812137b936c964f3537bbbf77668db9444a7e135ba128276675c7ad7c`
- `ACTUAL_DEPTH_STORAGE.md`: `556f1ee2d5eb060f6e734102c4c4b13bc824ceb0b9472c830d3839e7e18a6588`
- `ANALYTIC_TAIL.md`: `c410d90a3f2eb482b1fde74bfe4dbb74bb0dad28c16bc69a322f8ed2d901f8fc`
- `CURRENT_FORM.md`: `870af77dc18c9ab0048f95e388ac3bf73ed92fcd163cf918755bf13be109fad1`
- `FORWARD_RAYS.md`: `7917d80d78d5e3e7d5c242bbab25be7c02f9e9f7fec24fef14e5e9d9bcd1e09b`
- `check_reflected_row_tail.py`: `c047db937c6b517c12de73f1cc16337a637f3e82825c7899836c612916b84536`
- `certify_reflected_storage_row.py`: `0bb89b3046004770b3a652aaee6673500ad1efb4029bc6621ab8cc7d9c6c2eed`
- `reflected_storage_row_certificate.json`: `c39d44f7e4cb9e39c1a689c9a74b10bfa8ff079e056d9e039d03410c6cc8c833`
- `certify_half_reflected_storage_row.py`: `666051d00f200151eb8b475701d7a363251829e41bf054d93c7273515fcb921b`
- `half_reflected_storage_row_certificate.json`: `7609c31aaa602c7637e635d77302e404dbdea5fd0b82336c20d63abb4cfdb974`
