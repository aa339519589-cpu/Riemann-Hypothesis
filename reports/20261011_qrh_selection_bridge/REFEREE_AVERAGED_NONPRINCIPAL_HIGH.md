# Independent referee audit: averaged nonprincipal high bound

Date: 2026-10-12. Verdict: **accepted within the stated averaged high-side scope**, conditional on the attributed finite-order Q input. I found no hidden positive power of the auxiliary modulus in the high-side argument. This proves a bound for a new average of admissible observations; it does not prove a high bound for one fixed bad set or a low bound for the whole averaged probe.

## Exact ensemble and local deletion

The law in `POLYNOMIAL_AUXILIARY_ENSEMBLE.md` is the positive law on distinct unordered (k)-sets

\[
 \mathbb P(J)=\frac{\prod_{p\in J}W(Np/P_0)}{e_k((W(Np/P_0))_p)},\qquad
 P_0=(\log R)^{64},\quad k=\left\lfloor\frac{\log R}{65\log\log R}\right\rfloor.
\]

It is a genuine without-replacement distribution, not a product approximation. Since every selected prime has norm at most (2P_0), 
\(N B_J\le(2P_0)^k\le R\) for sufficiently large (R). The high-side version keeps the pool unrestricted over good primes outside (S_0); conditioning it on a ray would invalidate the unit-row cancellation. If (R=Z^\lambda) with fixed \(\lambda\) and every physical slot exponent \(\ell_i>0\), then (P_0\ll(\log Z)^{64}\) is eventually below each slot support, so (J) is disjoint from all original slot primes.

For each added prime the exact ratio of the (S_0\cup J) row to the (S_0) row is

\[
 Z_{p,\mathrm{half}}(u;x,w,z)
 =\frac{(1-V)[\chi_p(u)-\chi_p(u)^2(Np)^{-w}]}{(1-D)H_p^{[1/2]}(x,w,z)},
\]

with zero extension when (p\mid u). This retains the deleted scalar-zeta factor, both (L)-factors, and the local correction. It is not a bare character replacement. The exact row identity is the original/core (S_0) row times \(\prod_{p\in J}Z_{p,\mathrm{half}}\). The added bad Gauss norm cancels the first-Poisson normalization coefficientwise; the remaining supplementary phase has modulus one and lies in the original fixed reciprocity group. Thus there is no (N B_J\) power in the high amplitude or a change to the physical radial scale.

At the original absolute contours \((\Re x,\Re w,\Re z)=(3,3,2)\), the half-damped local identity gives (H_p^{[1/2]}=1+O((Np)^{-1-c})), hence (Z_{p,\mathrm{half}}=\chi_p(u)+O((Np)^{-1/2})), uniformly in all three heights. The same formula multiplies the complete original or core slot correction because (J) avoids slot supports. The core correction remains its separately derived holomorphic difference term; it is not obtained by substituting a core local sum into the original simplified marker.

## Cancellation for every nonprincipal row

On the unrestricted good-prime pool, (p\mapsto\chi_p(u)) is the Kummer Hecke character attached to (K(u^{1/6})/K). For sixth-power-free (u\ne1) it is nonprincipal, including each of the five nontrivial units: a sixth root in (K) would have zero valuation at every finite prime and would therefore be an Eisenstein unit with sixth power 1. The checked conductor bound (C_{\chi_u}\ll (Nu)^5) makes the logarithmic finite-order-Q prime estimate uniform for (Nu\le R^{A_0}). In particular, the proof averages all six unit rows and does not rely on a ray-restricted unit character remaining nonprincipal.

With \(L=\log R\), the smooth prime mean of the leading character is (O(L^{-4})) uniformly on the prescribed row, common-hole and height windows. The exact local error and removal of primes dividing a row or common hole are smaller. The no-replacement symmetric-polynomial lemma then gives

\[
\left|\mathbb E_J\prod_{p\in J}Z_{p,\mathrm{half}}(u;x,w,z)\right|
 \le [C(L^{-4}+B\sqrt{k/N})]^k\le R^{-1/20},
\]

for fixed (A_0,A_1,A_2) and sufficiently large (R). Here (N\asymp P_0/\log P_0); even the more generous (B\ll L^{16/25}) used in the source estimate gives (B\sqrt{k/N}\ll L^{-1543/50}=o(L^{-4})). The resulting exponent (4/65) strictly exceeds (1/20). Constants may depend on the fixed window exponents and real-part margins, as required.

## Initial-contour majorant and tails

The high bound is taken on the original absolutely convergent \((3,3,2)\) contours; no reciprocal contour is shifted. There (L^S(w,\chi_u)), (1/L^S(x,\bar\chi_u)), and \(\zeta^S(6z)\) have uniform absolute Euler-product bounds. The half-damped Euler correction is \(\ll_\epsilon(Nu)^\epsilon\). For both exact original and core markers, each selected local (G_p\) is (O(1)) at all six valuation states. Summing (O(P_i)\) selected primes with weight ((Np)^{z-1}) at (z=2) costs (P_i^2) per slot. The original (A_T(Z)=(-1)^K Z^{-\ell/6}\prod_i S_i(Z)\) is unchanged, since the slots are unchanged; its size is logarithmic up to fixed constants, so its reciprocal costs (Z^\epsilon). This yields the stated normalized finite-slot majorant (\ll_\epsilon(Nu)^\epsilon Z^{2\ell+\epsilon}).

There are (O(U)) ideals in a norm dyad (Nu\asymp U), and the exact outside row weight is ((Nu)^{-2}). Thus the unaveraged tail (Nu>R^{A_0}) is (\ll Z^{C(3)+2\ell+\epsilon}R^{-A_0(1-2\epsilon)}). The independent Gaussian/Mellin factors in the three actual high-contour heights give their original Schwartz tails outside \(|t|+|v|+|r|\le R^{A_2}\), at cost (R^{-A_2N_1}) for arbitrary fixed (N_1). The local products and finite slot sums are uniform in those heights. This cutoff concerns only Mellin heights; it does not replace any selected-zero or Fejér height. The averaged multiplier is applied rowwise on the finite norm/height box, and the two tails are added using the absolute majorant.

The scalar residue constant does not create a modulus loss. If a later normalization includes it, then
\[
 c_{S_0\cup J}/c_{S_0}=\prod_{p\in J}(1-1/Np)^2=1+O(k/P_0),
\]
since \(c_S\) contains the square of \(\operatorname{Res}_{s=1}\zeta_K^S(s)\). This ratio stays bounded above and below. The high-contour estimate itself is unshifted and does not need to insert a principal residue constant. In either convention, (c_S) contributes no power of (R), and (A_T) remains the original slot normalization.

Consequently the stated estimate
\[
 \frac{|\mathbb E_J\mathscr R^{\star}_{\ne1}(Z)|}{|A_T(Z)|}
 \ll Z^{C(3)+2\ell+\epsilon}
 \bigl(R^{-1/20}+R^{-A_0(1-2\epsilon)}+R^{-A_2N_1}\bigr)
\]
has the claimed implication. Since (C(3)-C(\sigma_0)=3-\sigma_0), fix \(\epsilon>0\), choose fixed \(\lambda\) with \(\lambda/20>3-\sigma_0+2\ell+m+2\epsilon\), set (R=Z^\lambda), and then fix (A_0,A_2,N_1) large enough for both tail exponents. All constants and cutoffs are fixed before (Z\to\infty). This gives the sufficient averaged high bound (O(Z^{C(\sigma_0)-m})) for any fixed \(\sigma_0>1/2\), (m>0\). The auxiliary physical modulus is polynomially bounded in (Z), but its norm has already canceled exactly; no hidden (R^{+c}\) term remains.

## Scope limits

This is an average over varying bad sets, not a pointwise estimate for the original fixed observation. It uses finite-order Q for the Kummer prime mean, but it does not use Q to bound (1/L(x,\bar\chi_u)) below its zero-free region: the reciprocal stays on \(\Re x=3\). No denominator zero is crossed and no (L'(\rho)\) occurs. The old single-probe low bounds are not used to turn this into a contradiction; the polynomial-ensemble note explicitly leaves the whole averaged low bound and the (R\)-dependent principal multiplier comparison open. At (u=1), the deleted multiplier is only (1+O(kP_0^{-1/2})), a logarithmic error relative to the signal, so no principal power comparison follows.

Audited sources: `AVERAGED_NONPRINCIPAL_HIGH.md`; `POLYNOMIAL_AUXILIARY_ENSEMBLE.md`, Part A §§2–8; `HALF_DAMPED_PROBE.md`, §§2, 4, 6, 9; `EXCLUSIVE_S_UNIT_PROBE.md` §1 for the distinct physical marker; and `GENERAL_SELECTED_Q_GAIN.md` for the separate selected-prime Q scope. No author report or repository source was changed.

Publication scope update: the subsequently reviewed [AVERAGED_PRINCIPAL_CONTRACTION.md](AVERAGED_PRINCIPAL_CONTRACTION.md) supplies an exact coefficient-contraction comparison, with the safe-error restriction and abscissa descent proved separately. The same averaged whole-low bound remains open. The present review does not import the old fixed-probe low bounds.
