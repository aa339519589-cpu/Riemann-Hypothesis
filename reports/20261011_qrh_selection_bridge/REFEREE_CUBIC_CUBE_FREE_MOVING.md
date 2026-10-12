# Independent bounded review: corrected cube-free Gauss note

## Verdict

**Accepted for the stated primitive norm-four row and fixed bad data.** [CUBIC_CUBE_FREE_MOVING.md](CUBIC_CUBE_FREE_MOVING.md) uses the full reflection denominator, including the raw exponent-two Gauss factor. Its left-line estimate (9),

\[
 (NL)^{3/2+2h}U_1^{1/2+2h+\eta}U_2^{1+2h+\eta}(1+|t|)^{2+4h},
\]

has the right powers. The direct local calculation gives the stronger (U_2^{1+2h}) without (U_2^\eta); the displayed weaker estimate is harmless. The interpolated statement (1) has (U_1^{1/4}U_2^{1/2}), with no quarter-power assertion on (U_2). I found no correction needed to the current manuscript in the audited chain.

## Local transform and reflection scale

For (P=Np), the pinned source's finite Fourier formula is (C_{p,j}(h)=P^{-1/2}\tau_{p,j}^{-}\chi_p(h)^{-j}) at (h\ne0), zero at (h=0), with the normalized prime Gauss factor of modulus one (source `eq:reflection-local-fourier`). The manuscript's γ notation is the same normalization; the sign change is immaterial for the even exponents (j=2,4).

At a prime of (A_1), (j=4): the cusp multiplier cancels the (h_p)-character, and the reflected additive sum is the Ramanujan sum (c_p(x)=-1+P1_{p\mid x}). The full local transform is a unit phase times (P^{-1/2}c_p(x)), of size at most (P^{1/2}). This matches the (j=4) row of the pinned source's local (B_p) table.

At a prime of (A_2), (j=2): after (y=h_p^{-1}), the remaining raw sum is

\[
 S_p(x)=\sum_{y\ne0}\chi_p(y)^4e(\epsilon_p yx/p).
\]

It vanishes for (p\mid x), and for (p\nmid x) is a primitive raw Gauss sum of size (P^{1/2}). The finite Fourier coefficient's (P^{-1/2}) cancels that size, so the complete normalized local transform has modulus one on its support. This agrees with source `eq:reflection-local-fourier`, `eq:reflection-multiplier`, `eq:reflection-additive-phase`, and the (j\ne4) local transform calculation immediately following them. It also confirms that all moving primes are active and the reduced denominator contains (p), not (p^2).

For the global scale, (q_c=Nc_0U_1U_2) contributes ((Nc_0U_1U_2)^{1-2s}), and the common finite-transform normalization contributes ((U_1U_2)^{-1/2}). Before the remaining raw sums this is

\[
 (Nc_0)^{1-2s}U_1^{1/2-2s}U_2^{1/2-2s}.
\]

The (A_1) Ramanujan factors cost (O_{h,\eta}(U_1^\eta)) against the dual Euler factors. For (A_2), factoring the common normalization leaves (S_p(x)), not (P^{-1/2}S_p(x)); hence its raw size costs (U_2^{1/2}). The residual local factor is a unit character on (p\nmid x) and deletes the (p\mid x) terms, so it costs no additional Euler-product power. At (s=-h+it), this gives

\[
 (NL)^{3/2+2h}U_1^{1/2+2h+\eta}U_2^{1+2h}
 (1+|t|)^{2+4h},
\]

where ((NL)^{3/2+2h}) uses (Nc_0\le NL) and the stated Parseval bound ∑|Φ̂_0(h_0)|\le\sqrt{NL}. Thus current (9), which allows (U_2^\eta), is a valid weakening. Equation (8) is the dual Euler factor; equation (9) retains the (U_2^{1+2h+\eta}) power.

## Interpolation and the full epsilon range

With (h=\eta=\epsilon/4), (b=1+\epsilon/4), the strip has width (b+h=1+\epsilon/2), and the target interpolation weight is

\[
\theta=\frac{b-(1/2+\epsilon)}{b+h}
      =\frac{1/2-3\epsilon/4}{1+\epsilon/2}.
\]

For every (0<\epsilon<1/4), (h=\eta<1/16<1/8), the interpolation interval is nonempty because (b-(1/2+\epsilon)>5/16), and θ is positive. The left gamma degree is (2+4h=2+\epsilon<9/4<3), so division by ((s-2)^3) leaves a strict height margin. Using the manuscript's deliberately weaker exponents (a_L=3/2+\epsilon/2), (a_1=1/2+3\epsilon/4), (a_2=1+3\epsilon/4), the three deficits are exactly

\[
\frac{5\epsilon/4+3\epsilon^2/8}{1+\epsilon/2},\qquad
\frac{\epsilon/8+9\epsilon^2/16}{1+\epsilon/2},\qquad
\frac{5\epsilon/8+9\epsilon^2/16}{1+\epsilon/2}.
\]

All are strictly positive throughout the full open range. The norm exponents decrease as σ runs from (1/2+\epsilon) to (b); for σ\ge b, the original (R_A) series is absolutely bounded at (b>1). The infinity Euler quotient and its inverse are uniformly bounded since its real argument is at least (1+3\epsilon), with the moving primes deleted as stated.

The exact rational certificate at [check_cubic_cube_free_moving.py](check_cubic_cube_free_moving.py) verifies these identities and range inequalities using `Fraction`; it reports success. It checks the displayed mathematical ledger, not an implementation of the proof.

## Remaining audited interfaces and scope

The norm-four cusp-constant argument is applied before absolute values and holds the moving Fourier coordinates fixed on each norm-four fiber; this is the required use of Part XXVII A. At a zero dual frequency the (j=2) factor already vanishes when (A_2\ne1); otherwise the cubic (2)-part factors through reduction modulo (2), and the primitive ψ₄ coefficient cancels on the (1+2\mathcal O\bmod4) fiber. There is no reflected additive factor in a constant mode. This is consistent with Part XXVII A and the pinned source's distinction between the cusp constant and nonconstant reflected expansion.

The common-hole identity adds a squarefree (d\mid M_0) to (A_1), preserving the cube-free form, and the bound's extra divisor weight is ((Nd)^{1/4-\sigma}\le(Nd)^{-1/4-\epsilon}). The stated (O_\epsilon((NM)^\epsilon)) divisor cost follows. Expanding a finite lambda function into multiplicative characters before applying the Euler quotient or hole identity is also necessary and is stated. Conjugation must switch the fixed character and moving chirality together, as the note says.

This verdict is confined to the asserted primitive norm-four row with its fixed bad data, moving good cube-free numerator, and common holes. It does not verify a moving bad-period estimate or any full physical-row/coupled-contour conclusion, and it implies no RH claim.

## Inputs inspected

- [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XXVII A and B, especially B §§2--6 (the active denominator, reflected Mellin scale, absolute Euler majorant, interpolation, and holes).
- [pinned September-30 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), source equations `eq:reflection-local-fourier`, `eq:reflection-cusp-fraction`, `eq:reflection-multiplier`, `eq:reflection-additive-phase`, and `eq:reflection-reflected-mellin`, with the (B_p) table in `eq:reflection`.
- [CUBIC_CUBE_FREE_MOVING.md](CUBIC_CUBE_FREE_MOVING.md), equations (2)--(10) and the exact hole/conjugation formulas.
