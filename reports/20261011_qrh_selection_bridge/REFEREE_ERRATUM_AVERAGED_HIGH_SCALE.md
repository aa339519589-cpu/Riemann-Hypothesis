# Source review of the user's averaged high, principal contraction and descent

Review completed 2026-10-12 09:14 UTC. The principal coefficient contraction and the conditional safe-line descent are approved in their stated conditional scope. The nonprincipal averaging mechanism is valid, but its displayed complete scale exponent and sufficient auxiliary-power threshold require the explicit correction below before quantitative use.

User-authored sources at [commit 1e8bb596](https://github.com/aa339519589-cpu/Riemann-Hypothesis/commit/1e8bb596a0dcb6a489ad5df47e872ae77ef3343b):
- AVERAGED_NONPRINCIPAL_HIGH.md: 71720340dc851480e978a013636d0a450128dc43019bf70c0b00c74b4c37bbda.
- AVERAGED_PRINCIPAL_CONTRACTION.md: 5036e9ce3c6a1deac33ce4ca434e795bb48526bf41da187f670797fdd738114c.
- PRINCIPAL_ABSCISSA_DESCENT.md: c58662ee9c73005c67274f3e668871da7d83a0a6db211542eee82620a5d09199.
Both accompanying user reviews were also read. No user file was edited.

## 1. Required quantitative correction in the nonprincipal high bound

The actual original common Mellin weight at pinned source fd4aeeb2, paper.tex lines 3825 and 5645, is

 X^(1/2-z) Z^(x+z-1) Y^(w-1)

multiplied by the unchanged Gaussian and two Mellin windows. At real parts (3,3,2) its modulus scale is X^(-3/2) Z^4 Y^2. The user's already stated bound for the complete normalized finite-slot factor is Z^(2 ell+epsilon). Therefore the full integrated absolute majorant has scale

 A_abs = 4 - (3/2) l_x + 2 l_y + 2 ell
       = C(3) + 2 l_y + (11/6) h,
 h=1-l_x+ell, C(s)=s+l_x/2-1+h/6.

The h in the second expression already contains the slot contribution; one must not add another 2 ell to it. With l_x=17/48, l_y=23/48, ell=1/6 this is 457/96. The printed C(3)+2 ell is only 127/48 in this geometry and does not pay the original w and z scale factors. The accompanying high-side audit repeats the same omission.

Consequently the complete bound (17) should use Z^(A_abs+epsilon), including in both unaveraged tails. A correct sufficient condition replacing (18) is

 lambda/20 > 3-sigma_0 + 2 l_y + (11/6) h + m + 2 epsilon.

The row and height cutoffs are then chosen as before. This correction is also independently confirmed against the pinned prefactor by the source author of the principal-comparison input. The previously reviewed coarse raw physical majorant 505/96 is an alternative sufficient, larger exponent; it is unaffected by this error.

The correction does not destroy the qualitative claim that any fixed desired high-side power can be obtained by a sufficiently large fixed lambda, under the stated finite-order prime input. The auxiliary pool is still polylogarithmic in Z and remains disjoint from the physical prime slots. It does invalidate the specific smaller printed lambda threshold. No claim is made that the stronger printed inequality has been disproved by a lower bound; it is not established by the supplied absolute-majorant argument.

## 2. The remaining nonprincipal mechanism

The exact local deletion multiplier retains the scalar-zeta, numerator, inverse and correction factors. Its zero extension and the unrestricted Kummer prime pool are essential, including for nontrivial units. The exact without-replacement elementary-symmetric average and its R^-1/20 estimate are used only on a finite row/height box. The absolute Euler bounds on (3,3,2), complete finite-slot G replacements, row norm tail and independent Mellin-height tail then permit the full average and infinite sums to be exchanged. No reciprocal contour below the initial line is used. These steps remain valid with the corrected full scale exponent.

The separate dynamic-route formulas preserve their reflected-numerator and row-conditioned reciprocal hypotheses; they do not themselves settle all required bins. The exclusive physical marker remains a different observation. The finite-order prime hypothesis is the user's separately supplied Q input and is not independently unconditionalized by this review.

## 3. Exact principal multiplier and contraction

The local multiplier h_p includes both residue factors (1-P^-1)^2, deletion of the half-damped correction, and deletion in the target reciprocal. Its exact formula (10) and constant coefficient c_p=(P-1)/(P+1) agree. Expanding its rational denominator in the absolute Dirichlet coefficient norm is valid for every fixed sigma_*>1/2. The positive fixed-size ensemble gives the stated relative tail o(1), without Bernoulli substitution or an assertion that averages of nonzero complex values remain nonzero.

The separate original/core slot formulas have constant one after the minus sign, retain the full finite compensation, and have absolute coefficient tails O(P^-sigma_*). Combining equal norm indices by the triangle inequality is legitimate. The auxiliary/physical slot disjointness is an eventual deterministic norm separation.

The exact convolution f_Z(Z)=sum a_Z(n)n^-c_exp f(Z/n) follows on the absolute line. Small arguments are controlled by shifting the fixed Mellin kernel right to sigma'>max(2,sigma_*). Isolating the constant coefficient and taking a running supremum proves the contraction with theta<1. It remains valid at every jump of the sampled set size. It transfers a genuinely established varying-signal bound; it does not upgrade the logarithmic error estimate to a power bound by fiat.

## 4. Safe-line descent and its unproved premise

The pole-cleared Dedekind function is zero-free strictly to the right of beta*=sup Re rho. The anchored Euler line, polynomial strip upper bound, and the explicitly buffered Borel-Caratheodory disk give the required polynomial reciprocal-height bound there. This does not assume RH. The document uses the user's Q input to ensure beta*<=7/8; that use is explicit.

Once beta*>1/2 is fixed, the local w,z margins and slot exponent have a uniform positive lower bound in a small right neighborhood. Thus m0 is fixed first, then sigma_safe-beta*<m0/2. The possible worsening of the reciprocal height constant changes the fixed integrated constant, not the Z exponent, because the full Gaussian/Mellin integrals are retained. The pole at s=1 of zeta becomes a zero of its reciprocal. Exactly four w,z contour pieces remain.

The contraction can be applied below beta* only if the actual literal-row bound and the comparison error both fit sigma_new=sigma_safe-m0. If that matching low bound were proved, the fixed signal's Mellin transform would be holomorphic across a genuine pole, giving the stated contradiction without assuming a highest zero is attained. The half-damped numerator is nonzero on Re s>1/2 by its absolute Euler product.

No matching whole-low estimate is proved here. The principal contraction and the corrected nonprincipal high estimate are conditional tools for the same explicitly chosen observation; neither removes the original signed arithmetic low-side requirement. They exclude no new zeta zero at present.

The correction is stated separately in [ERRATUM_AVERAGED_HIGH_SCALE.md](ERRATUM_AVERAGED_HIGH_SCALE.md). The original user files are preserved.
