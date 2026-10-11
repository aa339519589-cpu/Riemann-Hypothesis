# Independent audit: current n=1 pure-first row transfer

**Verdict: ACCEPT for the n=1 frozen-character lemma, conditional on the stated Q input.** The row character, its primary-ideal Hecke extension, nonprincipality, conductor bound, squarefree Euler identity, and forced-​divisor (g_0) loss are correct. This is not an acceptance of the all-physical-(n) transfer or a complete sector bound; the manuscript does not claim either.

## Exact row character and auxiliary phase

The pinned September 30 source chooses ξ primitive modulo (b_*), nonprincipal at each local factor, with order 3 at the prime over 2. Its high Poisson identity carries the outer factor \(\overline{\xi(u)}\), while the local full coefficient has denominator \(\xi(s)\overline{\xi(u)}\). At (b_*), the local Gauss factor is \(\xi(A)\overline{\xi(H/s)}\); for (H=u a^6), \(\overline{\xi(H/s)}=\overline{\xi(u)}\xi(s)\). Multiplying these factors leaves \(\xi(A)\overline{\xi(u)}\). The \(\xi(A)\) cancels the \(\xi(A)^{-1}\) inside \(\Xi(A)^{-1}\), and the remaining \(\chi_A(b_*)^{-1}\) cancels with \(\chi_s(b_*)\) through the last local unit factors. The outer row factor \(\overline{\xi(u)}\) remains. Thus for (u=\varepsilon v), the row part is exactly
\[
\theta(v)=\overline{\xi(v)}\chi_t(v)\overline{\chi_{c_1}(v)},
\]
with no second auxiliary phase. This matches the first-Poisson identity quoted in the manuscript.

For fixed (\varepsilon), the (a^6) terms are exactly \(\overline{\xi(a^6)}=1\) and \(\chi_t(a^6)\overline{\chi_{c_1}(a^6)}=1_{(a,tc_1)=1}\), retaining the zero extensions. The unit factor is \(\overline{\xi(\varepsilon)}\chi_t(\varepsilon)\overline{\chi_{c_1}(\varepsilon)}\). The original probe is radial in the norm, so all six units carry the same smooth weight; after fixing \(t,c_1\), summing them gives exactly zero or six. This is valid without assuming the raw generator character is unit-trivial. If a later variant has a unit-dependent weight, keep the six pieces separate; that variant is outside this radial application.

## Hecke character, nonprincipality, and conductor

For primary (v\), the symbols \(\chi_t(v)\) and \(\chi_{c_1}(v)\) are fixed-denominator residue characters: as functions of the primary generator they depend only on its residues modulo (t) and (c_1). The primary normalization is imposed modulo (3\mathcal O), and \(\xi(v)\) depends on residues modulo (b_*). Since every ideal has a unique primary generator and primary generators multiply, (2) defines a finite-order ray character on good ideals with defining modulus dividing a modulus supported on (3b_*tc_1). In particular the two good-symbol factors have no conductor at 2; their good-prime supports are in (tc_1), and the only primary-convention factor is at 3. Therefore the order-3 local component of \(\xi\) at 2 cannot be canceled. The primitive conductor bound \(q_f(\theta)\le C q_tq_{c_1}\) follows directly from this defining modulus.

To check nonprincipality on the primary subgroup, use CRT to choose an element congruent to 1 modulo (3tc_1), all other fixed ray factors, and any additional good-prime mask, while prescribing at the prime over 2 a unit on which \(\xi\ne1\). The element is primary and its ideal is good; the two symbol factors are 1 there, while \(\overline\xi\ne1\). This proves nonprincipality even after any stated fixed good-prime exclusions. It avoids relying on an unsupported claim that an arbitrary residue character remains nonprincipal after restricting to primary generators.

## Euler series and Q shift

Equation (4) follows prime by prime from \(1+x=(1-x^2)/(1-x)\); zero-extended primes contribute 1, and the extra common mask (M) removes the displayed finite Euler factors. For imprimitive characters, using the same actual deleted factors in both L-functions preserves this identity. Since \(\theta\) is nonprincipal, the numerator is entire. Q for \(\theta^2\) makes the reciprocal denominator holomorphic for \(\Re z>7/16\); when \(\theta^2\) is principal, the pole of its L-function at 1 gives a zero of the reciprocal. No boundary claim at (7/16) is used.

On a fixed line (7/16<\sigma<1) with the stated buffer, degree-two Hecke convexity gives \(q_f(\theta)^{(1-\sigma)/2+\epsilon}\) times a height polynomial for the numerator. The buffered reciprocal estimate for \(\theta^2\), whose conductor is no larger than that of \(\theta\), and the finite inverse Euler factors cost only the stated small powers of the actual modulus. Mellin inversion then yields (5); the smooth Mellin transform absorbs the height powers and contour edges. The unit-ideal term can be removed at (O(1)) if the sector requires (v\ne1).

The only archimedean twists needed for the original probe are norm Mellin modes \(q_v^{iu}\): the source weight \(W_0(q_m/(q_bq_sX))\), its Fourier transform, and the Gaussian norm weight are radial. Thus (5) uses a vertical shift of a finite-order Hecke L-function, with a polynomial cost in \(u\). There is no angular Fourier mode \(e^{im\arg v}\) in this scope. Such a mode would be an infinite-type twist and is not covered by the stated finite-order Q input. If the two-column joint Mellin separation is used, its exact retained cutoff identity \(\rho_x\rho_y=1\) on \(\operatorname{supp}F_\lambda\) must be in force before Fourier inversion; an unrestricted pure Mellin mode does not by itself justify absolute convergence of the separated sums.

## (g_0) and scope

For (H=\varepsilon v a^6), a prime in (g_0\mid v) with (p\nmid a) has (v_p(H)=1), so \(\mathfrak c_p(H/p)=-1\); its Möbius sign cancels this sign but leaves the exact (q_p^{-1}). A prime in (g_1\mid\operatorname{rad}(a)), including a shared (v,a) prime, has (v_p(H)\ge6), so its Ramanujan value is (q_p-1). Thus only (g_1) carries the \(\varphi(g_1)\) factor. Forcing (g_0\mid v) and applying (5) at scale (X/q_{g_0}) pays (q_{g_0}^{-1-\sigma}), with the actual masks retained; this ideal sum converges.

The manuscript correctly limits itself to an n=1 row input and says that the remaining joint (c,t), physical-layer, slot, tail, and flat sums are open. The radial source justifies the common unit weight and its 0/6 sum. The Mellin argument must remain norm-only, and any two-column use must retain the stated product cutoff before inversion. No angular-mode, all-(n), or global-sector conclusion is accepted here.
