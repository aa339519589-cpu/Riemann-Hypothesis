# Referee 27: fixed-finite theta jet tail frame

## Verdict

**PASS for the stated fixed finite-dimensional estimates.** I find no fatal gap in the finite-dimensional frame argument. In particular, the document supplies the global weighted-tail control needed to pass from the (m=1) Taylor frame to the full theta jets; it does not rely only on convergence for bounded (s). The resulting Gram limits are positive definite, and the claimed exterior-mass, (L^1/L^2), and (H^1/L^2) bounds follow with constants depending on (d).

This verdict is strictly for each fixed (d). It gives no estimate uniform as (d\to\infty), no infinite-jet or arbitrary-mixture result, no inverse-weighted Schur bound, and no RH conclusion. The scope limitations in the note are mathematically necessary.

## Frame normalization and conditioning

The leading coefficient calculation is consistent: applying \(\mathscr D\) raises degree by one and multiplies the leading coefficient by \(-2\), so \(\deg \mathcal F_j=5+2j\) and \(R_j(u)=4^ju^{2j}+O_d(u^{2j-1})\). Differentiating this fixed-degree rational asymptotic gives the displayed Taylor-matrix factorization
\[
M(U)=\operatorname{diag}(U^{-\ell})(B+O_d(U^{-1}))\operatorname{diag}(U^{2j}).
\]
The matrix \(B\) is invertible because the polynomials \(\binom{x}{\ell}\), \(0\le\ell<d\), form a basis of polynomials of degree below \(d\), evaluated at the distinct nodes \(0,2,\ldots,2d-2\). Thus \(M(U)\) is invertible for all sufficiently large \(U\), and
\[
|(M(U)^{-1})_{j\ell}|\le C_d U^{\ell-2j},\qquad
\|M(U)^{-1}\|\le C_d U^{d-1}.
\]
The factorization also gives norm bounds ||M|| <= C_d U^(2d-2) and ||M^-1|| <= C_d U^(d-1), hence condition number O_d(U^(3d-3)). This polynomial condition-number control ensures multiplication of the exponentially small full-theta remainder by the frame coefficients remains exponentially small. No uniform conditioning in d is claimed or needed.

The exact interpolation statement applies to the rational (m=1) profiles \(\phi_{\ell,U}\). The corresponding full-theta profiles are not asserted to have exactly those finite Taylor coefficients; their difference is controlled by the (m\ge2) remainder. This distinction is correctly maintained in the note.

## Full-theta remainder and global weighted convergence

For (u\ge U_d), factoring out (e^{-u}) leaves the modes (m\ge2) with exponential factor (e^{-(m^2-1)u}\le e^{-3u}). Any fixed number of (u)-derivatives only adds fixed powers of (m) and (u); the resulting sums are bounded by a fixed polynomial in (u) times (e^{-3u}). Since \(\mathcal F_0(u)\asymp u^5\), division by the (m=1) denominator preserves an estimate of the form in (4), including fixed derivatives. Multiplying by the frame coefficients costs only a fixed power of (U).

The split at (s=U/2) closes the global-tail issue. On \(-2\pi\le s\le U/2\), Taylor's theorem is applied with all intermediate arguments at least (U/2), yielding the stated (C_dU^{\ell-d}|s|^d) profile error (and its derivative counterpart). These errors tend to zero in every fixed polynomially weighted (e^{-s}) or (e^{-2s}) norm. On (s\ge U/2), the rational profiles and their first derivatives grow at most polynomially in (U,s), while the weights are exponentially decaying; this part tends to zero. The (m\ge2) full-theta error is smaller still, since it carries (e^{-3(U+s)}). Consequently the asserted convergence holds on the entire half-line, not merely on compact (s)-sets.

The density bookkeeping also checks: \(|f_0|^2dx\) has leading density \((512/\sqrt\pi)u^{19/2}e^{-2u}du\), and \(|f_0|dx\) has scale \(u^{17/4}e^{-u}du\). The global polynomial-envelope bounds in (12) and its (L^1) counterpart provide the domination needed for the moving endpoint (s_R\to-2\pi) and for the Gram limits.

## Gram matrices and exterior mass

In the normalized basis, a vector has profile tending to a polynomial \(P_\beta(s)=\sum_{\ell<d}\beta_\ell s^\ell\). The limiting quadratic forms are
\[
C_*\int_{-2\pi}^{\infty}|P_\beta(s)|^2e^{-2s}\,ds,
\qquad
C_*\int_{\pi}^{\infty}|P_\beta(s)|^2e^{-2s}\,ds.
\]
Each is positive for every nonzero coefficient vector: a nonzero polynomial cannot vanish almost everywhere on either interval. In fixed dimension, convergence of the matrices and compactness of the coefficient unit sphere give a positive lower bound for the generalized exterior/full-tail ratio. The endpoint (a_{k+1}) is indeed (s=\pi), while the support endpoint tends to (s=-2\pi). Oddness doubles both one-sided masses and does not change the ratio. Since (r=f) on the exterior and \(0\le\eta_k\le1\) on the support tail, this proves (14) and the comparison (14a).

## Norm estimates and scope

The weighted (L^1) and (L^2) profile bounds give respectively \(\|f\|_{L^1(|x|\ge R_k)}\le C_dU^{17/4}e^{-U}\|\beta\|\) and \(\|f\|_{L^2(|x|\ge R_k)}\ge c_dU^{19/4}e^{-U}\|\beta\|\). Combining \(|r|\le|f|\) with the exterior/full-tail comparison yields \(\|r\|_1^2\le C_dU^{-1}\|r\|_2^2\), hence the stated (C_d/k) bound.

For the derivative estimate, the full-theta tail has no zeros for sufficiently large (u), and the differentiated theta envelope gives \(|f_0'|/|f_0|\le C u\). Also (ds/dx=2u). The profile and first-profile-derivative weighted bounds therefore give \(\|f'\|_{L^2(|x|\ge R_k)}\le C_dU\|f\|_{L^2(|x|\ge R_k)}\). The cutoff term costs at most \(Ck\|f\|\) on the transition; (14a) compares both terms with \(\|r\|_2\). This proves the stated \(H^1/L^2\) estimate.

The zero-mode statement is the algebraic consequence of the exact source identity and commutation on the specified theta-source class. It should continue to be read with the document's explicit qualification that this does not assert a closed unweighted L^2 realization of T. The finite-frame results themselves are tail estimates only; they do not imply sign control for arbitrary growing-dimensional mixtures or any RH conclusion.
