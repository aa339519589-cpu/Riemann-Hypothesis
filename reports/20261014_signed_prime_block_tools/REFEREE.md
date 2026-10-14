# Independent mathematical review

## Reviewed scope

The four notes establish exact identities and a structural obstruction for the unchanged theta source and full prime-power forms. The displayed remaining coefficient-one inequalities are not proved. None of the reviewed results establishes the Riemann hypothesis or a negative vector for the complete Weil form.

The reviewed versions have the following SHA-256 digests:

- `SIGNED_LOAD_CUT_CURRENT_FACTORIZATION.md`: `c3e6c11c29c58e0206589024abbf6fa8130a3835de99ecadcf2f12aacb4862b7`.
- `GROUPED_PRIME_POWER_FACTORIZATION.md`: `b4abf2e93e30fd80a6cd62bd4112548a7fd1881e2c54d14a39c7fcb8567032f3`.
- `PRIME_TWO_MASS_IMBALANCE.md`: `a1e06784476fdb3515d2c4cd2ae407fcaf43550f02c048130833f6bb8ddcc4d8`.
- `PRIME_BLOCK_POSITIVITY_OBSTRUCTION.md`: `4e7b88a6248eab60323c4d1b934775fedca05b17a8a4cb5942a312d2b04ef41d`.
- `check_factorizations.py`: `84977c28edd485b6690c3dd275e8dc3b01e28f9cd33e0e12a0b1e38e044ab580`.

## 1. Signed reference loads

The Wronskian identity and the reference solution's boundary behavior imply

\[
g(i,j)=p_ip_j\sum_{k\ge\max(i,j)}\frac1{c_kp_kp_{k+1}}.
\]

Expanding a finite load gives precisely the squared weighted prefix sums in equation (3). In particular, the nonzero tail of a dipole is retained; the identity does not incorrectly replace signed cross-coefficients by positive path counts.

The extension uses the normalized load \(Q_j=\sqrt{D_j}q_j\), not an unsupported bounded inverse on unweighted vertex loads. The uniform reference gap gives the stated two-sided bounds and a measurable bounded direct integral. Coordinatewise finite prefix sums identify the extension without any conditionally convergent interchange of edge terms. Potential recovery follows from Cauchy--Schwarz against the finite tail resistance and selects the reference boundary condition at infinity.

The Cholesky continuation in Section 7 is also valid. Its pivots are the finite-section Schur complements, so \(\gamma_j\ge1-\rho\). Direct multiplication gives \(B B^*=I-A\), including the first row. This lower bound makes \(B\) onto; its nonzero diagonal and triangular recurrence make its kernel zero. Telescoping then identifies \(B^{-1}\) with the completed prefix transform. The argument is not limited to finite loads.

Applying this factorization to the completed aggregate correction preserves all prime/prime and Gamma/prime interactions. Equation (13) remains an unproved comparison against the reference excess. Positivity of the correction alone does not establish it.

## 2. Complete prime-power grouping

For a fixed prime, the weight of a forward pair \(i<j\) is exactly \(q_iq_j a^{-2i}\). Expanding \(a^{-2i}\) into its positive increments proves the hierarchical variance formula by Tonelli's theorem. The reflected index is \(j+l+1\); consequently the factor in equation (3) is \(d a\), with no additional factor two. The two-population variance identity, followed by base-point reflection, gives equation (4), including its mean-mismatch term.

All prime sums in the remaining payment formula are controlled by the original positive energies. In particular, the two contributions defining the signed coefficient \(H_p\) must be kept separate for convergence estimates. This is a legal regrouping of the complete forms, not a deletion of the negative coefficient region.

The folded adjacency blocks are \(T_a-avv^*\) and \(T_a+avv^*\). The geometric covariance expansion proves their strict positivity and the stated triangular factorization. The review confirms the minus sign and the indispensable subtraction of the identity in the source contribution. Separating the resulting divergent prime diagonal would be invalid; the notes do not do so.

## 3. Strict prime-two mass imbalance

The differentiated theta polynomial, its prefactors under translation, and both infinite-tail estimates give the claimed strict bound

\[
H_2(3\log(2)/4)<-\frac{18698870059}{26250000000}<-\frac23.
\]

The lower estimate on the reflected mass retains a positive theta summand, while the forward estimate bounds every omitted theta index and every translated fiber. The rational bounds on \(\pi\), roots, and exponentials are sufficient for the displayed inequalities. The exact checker was independently rerun and all assertions passed. Its finite algebra checks supplement the analytic proofs; they do not certify an infinite-dimensional sign by themselves.

This result concerns a coefficient of the first within-fiber variance. It leaves the higher variances, Gamma energy, pole energy, and shared-source compatibility intact.

## 4. Obstruction to positive summable arithmetic blocks

Assuming all proposed blocks are nonnegative, their partition identities and the complete two-energy cutoff convergence force each block to annihilate every neutral theta jet. This inference correctly uses positivity and the actual simultaneous neutral identities; it does not assume per-prime neutrality.

For a compact smooth odd source, a block of summable arithmetic strength has an ordinary odd \(L^2\) source row after removing its explicit pole functional. The translation operator is bounded by twice the summable strength. The Gamma multiplier has logarithmic growth, and the displayed local diagonal is locally bounded: its numerators are smooth odd functions, its denominator has a simple odd zero, and the summable arithmetic coefficients justify local differentiation. Hence the claimed row really belongs to \(L^2\).

The embedded density lemma is sufficient and does not assume RH. A vector annihilating all even derivatives of the odd theta seed gives an even holomorphic convolution whose Taylor coefficients vanish. Fourier uniqueness applies because the seed multiplier is nonzero almost everywhere; zeros of the nonzero entire Xi function have measure zero. Therefore the neutral jets are dense in ordinary odd \(L^2\).

The source row must consequently vanish. The remaining block is exactly \(-2d_b|\ell(g)|^2\); positivity forces \(d_b=0\). This contradicts the total pole allocation. The conclusion covers an individual prime with all its powers, or any block having the stated summable strength, even when that block contains the full nonlocal Gamma form.

It does not cover an unrestricted nonsummable global arithmetic block, signed allocations, state-dependent allocations, or compensating cross-block terms outside the stated decomposition. In particular, it gives no contradiction to positivity of the complete form.

## Conclusion

The displayed identities, extensions, strict mass estimate, and summable-block impossibility theorem are mathematically supported within the specified reference and theta-form framework. Their limitations are correctly stated. The full coefficient-one signed comparison remains open.
