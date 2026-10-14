# Independent mathematical review

## Verified scope

The pinned package establishes an original-source head gap with two exact
balanced loads:

\[
 q_0[f]+2|H_U(f)|^2+2|H_V(f)|^2
 \ge \frac1{100}\|f\|_{L^2(0,\log2)}^2.
\]

Unlike the earlier unbalanced loads, each load here has both zero value at
the safe-tail endpoint and zero pairing with the tail of `psi`. Its complete
tail functional is consequently bounded on the constant-quotiented hidden
variance space. The two exact Riesz vectors have a strictly positive Gram.
The resulting actual-source head estimate spends that variance through one
joint Gram bound and retains the full original tail form and mixed forcing.

The package does not prove positivity of the uncorrected head, the original
head/tail Schur complement, or the remaining original residual.

## Independent analytic checks

1. **Both balances are exact.** The calibration coefficients are defined
   by the displayed inverse matrix, not their decimal approximations.
   The complete Mangoldt/theta regrouping uses every prime power.
   The moment integrand `psi n_j` is evaluated without an origin quotient;
   the degree-seven midpoint integral has precisely the remainder
   `sup|F^(8)| length^9/(2^8 9!)`. The elementary U-tail primitive and all
   ordinary/mirrored theta tails were independently checked. The
   determinant enclosure is strictly positive, so the two defining
   endpoint and constant constraints hold exactly.

2. **The balanced coefficients are genuine interval enclosures.** All
   calibration uncertainty is propagated. The removable odd-source
   quotient uses the correct Taylor remainder through order 28. The
   sharper variation estimate retains the mean-value error
   `(length/2) sup_box|l''|`; it does not replace a whole-box bound by a
   point sample. Right endpoint values are zero by exact calibration.
   The Simpson remainder and integration-by-parts endpoint terms yield
   the full high tails `4/48` and `9/48`.

3. **The complete original operator is unchanged.** The exact Gamma
   boundary Gram, n=2 and n=3 reflections, full pole, Binet remainder and
   infinite high-block bound are the previously verified original-source
   kernel. The new two-load Young estimate spends `26/N` once. The
   balanced checker correctly subtracts `6/N` from the earlier diagonal
   and recomputes the infinite Schur remainder with the smaller
   denominator. Its exact integer rank-one sums and upward uncertainty
   bound retain all cross-column intervals. Positive interval LDL pivots
   certify the finite Schur lower matrix, not an asserted eigenvalue
   estimate.

4. **The stated domain is respected.** The theorem extends from finite
   sine spans by the closed restricted Gamma form and bounded lower-order
   forms. Actual head restrictions have stronger zero-extension
   fractional regularity. Nonzero-trace direct signed half-sources are
   not silently assigned separate original-P/N membership.

5. **The hidden dual needs two conditions.** The exact future adjoint
   is `A_l/W`. A nonzero `l(log2)` creates the stated logarithmic norm
   divergence. The independent zero tail-psi moment removes the hidden
   constant. The complete theta far majorant pays the remaining integral.
   The joint inverse-Gram inequality follows by Hilbert projection and
   spends one variance budget, not one budget per load.

6. **Strict Gram positivity is analytic.** On `(log2,log3)` the prefix
   transform is the load itself. Continuing the fixed prime-three row,
   rather than the changing piecewise positive-wing row, gives distinct
   nonzero polynomial degrees multiplying the dominant Gaussian tail.
   This proves independence of the two exact loads and hence strict
   positivity of their finite Gram. No numerical Gram eigenvalue is
   asserted or needed.

## Fresh independent reproduction

The complete original kernel, exact calibration and balanced sine
coefficients were independently regenerated from the pinned scripts. The
balanced Schur computation was then run on those fresh enclosures; the
publication copy of that checker was also rerun. Results include:

* calibration determinant
  `[4773295124.153197, 4773295124.153244]`;
* maximum first-48 coefficient radii below
  `5.073892169e-7` and `9.053768362e-7`;
* first high-diagonal lower endpoint `0.9550209029378011`;
* complete omitted Schur upper endpoint `0.0041228093197589275`;
* cross-interval scalar uncertainty below `2.733003e-10`;
* all 48 interval LDL pivots positive, minimum lower endpoint
  `0.5868143457817604`.

The fresh calibration and coefficient JSON hashes are respectively
`89d93cde94b0aef5219edcf192f45cfbc3d459ebb9330fe2a3b7f2a81c13026b`
and `920c6158d484b17026c190890f0dff6c081a36108d0cfae49f773186cdc20ddb`.
The fresh complete original-kernel JSON hash is
`39b2caafadc33ec5bd802e3b390b9fa0f5b0155d112c57dabc94389fba7b7ee0`.
All mathematical dependency links were checked. These computational
assertions rely on the supplied analytic complete-tail and domain proofs,
not on a finite sampled eigenvalue test.

## Actual-source consequence and limitation

The actual plateau representative has globally zero U and neutral N loads.
Thus each balanced head load equals the negative genuine tail load; it is
not set to zero separately. Actual stationarity gives equality of the head
and tail `Q_delta` energies. Combining the head gap with the joint hidden
Gram yields precisely the report's inequality (7), with the finite exact
`lambda_max(G)` left explicit.

The effective-head Schur construction is also valid for this balanced pair:
add their globally vanishing squares to the full form, retain the induced
rank-two mixed forcing, and use the proved head gap. The corresponding
inverse on a general tail forcing is a form-dual inverse, not an assumed
L2 kernel. The unbalanced U discussion in `ACTUAL_SCHUR.md` correctly
uses source representatives, not the original quotient where `psi` is
null; the same construction applies to the independently certified
balanced loads.

The remaining original `Q_delta[f_T]` and its complete Gamma/prime/pole
forcing are not controlled by this finite-rank payment. No RH exclusion or
free addition of the hidden and head gaps follows.

## Pinned artifacts

| Artifact | SHA-256 |
|---|---|
| `REPORT.md` | `40a8b981bea07ae32145952aa70d8e406d184bea6ad200567d2ff05a8987804f` |
| `CALIBRATION.md` | `4c2635d6fea7c3db1d380bcb28e06471d2323bb2d88b384c2ffb9a3032c45eab` |
| `COEFFICIENTS.md` | `cfe76718509863f4fd2d9fd4a3695e975bba6a9cb2e445960924453cf05c7a30` |
| `GRAM_RIGIDITY.md` | `fec1a0215d87ba1da2a498d72bf6af91b512c07ab7d7ab2808f192ca1394928a` |
| `TAIL_DUAL.md` | `211b1d48627a4d45600caacb54d56b2da2e8f8f7cc85a5a895fc6944fab20aa4` |
| `ACTUAL_SCHUR.md` | `e4622f152072821e2a1b532837ba8f0706374c03299f020298aba8b94c239915` |
| `certify_balanced_head_loads.py` | `9b9450d7d6d35103997838c914c472b6873d7222b986ac60675710dbf98172dd` |
| `certify_balanced_head_coefficients.py` | `88e1e383e0082038d533a259e961c6fd5475c8792a3705271a8232b1e613bb79` |
| `certify_original_head_kernel.py` | `e525264c1fbeceb81a24d2550567a5cab1c553f938c0f04fe034424d61a4702f` |
| `certify_balanced_original_head_schur.py` | `86e4a4d50eca25f104c0f7191bef17b88ab07ffb4b64b257d2cac24c61a7d9dc` |
| `SHA256SUMS` | `01c31eeb1a20129be84cb9c50cca5785b890354bf76d74db4c955546dadc9243` |
