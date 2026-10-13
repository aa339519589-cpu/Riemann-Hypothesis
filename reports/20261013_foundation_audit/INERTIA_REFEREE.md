# Independent checks of the even, odd and Green inertia counts

Date: 2026-10-13. Two independent mathematical reviews checked the [even inertia audit](ZERO_INERTIA.md) and the [odd/Green interface](ODD_GREEN_INERTIA.md), followed by a separate check of the preparation for publication. Both reviews approve the count statements under the original closed-form and complete explicit-formula inputs reviewed in this directory. This is not a proof-assistant certificate or a proof of RH.

## Scope and provenance

The even distinct-quartet theorem is inherited from [Round 5, section 7, Theorem 7.1](../../rounds/05/REPORT-pages-06-10.txt). It is not presented as a new zero-exclusion theorem. Its audit checks the weighted source domain in the exact zero-division proof and supplies an alternative proof using only compact sources and complete-zero-tail estimates. The odd compact-source count then connects the published Green inertia transfer to the same quartet count.

## First independent check

For a real even source, the quartet contribution is positive four times the multiplicity times the real part of the squared transform value. Its negative coordinate is the imaginary part of that value. For a real odd source the sign reverses, so the negative coordinate is the real part. A critical-line pair contributes a nonnegative square in either parity. Each distinct off-critical quartet therefore has one negative real coordinate, regardless of zero multiplicity.

The cosine and sine interpolation maps are onto for finite nonzero nodes modulo sign; their even and odd derivatives produce Vandermonde systems in the squared nodes. Realification preserves the required conjugation symmetry. In the odd case, real nodes have imaginary values, while purely imaginary nodes have real opposite values. The odd pole values may be nonzero because the coefficient-two pole term is retained in the form.

A shared even convolution factor equals one at all selected quartets. After the finitely many exceptional classes are killed by the individual interpolants, its powers suppress every remaining zero. The full diagonal and polarized tails are bounded by a geometric factor times the absolutely summable, actual-multiplicity-weighted products of the compact-source transforms. One common convolution power therefore gives a negative definite Gram matrix for any finite selection. The finite upper bound follows by imposing one real evaluation constraint per quartet. No finite-height approximation is used.

## Second independent check

The second review independently verified the parity signs, target interpolation values, full-tail Gram estimate, real/complex index agreement and form-core passage. Strict negative definiteness of a finite Gram matrix survives sufficiently accurate form-norm approximation. Consequently neither completion introduces extra negative index beyond the compact-source count.

For the inherited zero-division witness, each linear division uses two endpoint integral formulas joined by the exact vanishing transform value. This retains every fixed double-exponential decay rate below the theta rate. Choosing a rate above half that rate puts the divided source in the original weighted physical space. Smooth cutoffs converge in physical L2 and source H1; the logarithmic Gamma form is bounded by the H1 norm and the complete physical prime perturbation is bounded. These facts prove the actual form-domain passage without invoking an unspecified continuity assertion. Uniform weighted derivative tails also justify dominated convergence over all zeros with multiplicity.

The rank-one odd pole splitting has one positive scalar direction for the pole-free physical form and one null scalar direction for the pole-inclusive form; the remaining form is the same. Their negative indices therefore agree. The already-published common-core and polar-decomposition argument identifies this index with the dimension of the entire supercritical Green spectral subspace. It does not identify the completed Hilbert spaces or match individual eigenvalues.

## Clarifications incorporated in the final statements

- The even theorem is explicitly credited to Round 5.
- Orthogonality to a fixed negative-depth spectral band permits positive spectral components. The remaining spectrum is above minus that depth; strict negativity of the constructed subspace separately makes its Rayleigh quotient negative.
- The polarized tail is taken outside the union of all selected quartets, whose cross terms vanish exactly.
- The zero-division domain argument now uses the explicit original Gamma-form and bounded-prime estimates instead of an ambiguous source-estimate equation reference.
- Spectral ranks count eigenvalue multiplicities; the zero-side count includes each distinct quartet once. Zero multiplicity changes coefficients, not the number of independent negative coordinates.

Both counts may be infinite while each fixed-depth band is finite dimensional. The count equalities do not determine whether any of the counts is zero. The full critical sign remains unproved.
