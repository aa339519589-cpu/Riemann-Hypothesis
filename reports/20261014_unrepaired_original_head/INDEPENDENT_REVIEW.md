# Independent mathematical review

## Verified theorem

The complete original source form restricted to (0,log 2) satisfies

    q0[f] >= 10^(-10) ||f||_L2^2

on the stated closed restricted odd-Gamma form domain. No auxiliary pole, neutral, or moment penalty is added. Both internal prime reflections and the full negative polar rank-one term are included. This is a rigorous infinite-dimensional, computer-assisted head theorem, not positivity inferred from a finite sampled matrix.

## Exact analytic and numerical checks

1. **Complete original matrix.** The odd Gamma boundary Gram has the stated factor 4/b and damped numerator. Its positive rank-one expansion and Hilbert-kernel bound yield the full high-mode lower comparison. The n=2 reflection is diagonal; the compressed n=3 reflection and -8 ell tensor ell pole have the displayed signs and normalizations. All other prime overlaps vanish by this support geometry, not by truncating their coefficients.

2. **Structured infinite tail.** The complete off-diagonal Gamma/reflection/pole expression was independently recomputed. Its six exact low-mode vectors retain the signed endpoint cancellation before a positive rank estimate. In particular v0 is proportional to the complete endpoint load, not to a sampled eigenvector. Both geometric denominator remainders, the |theta_j|<3/2 bound, and the factor-seven Loewner envelope are correct. The damped S sum is retained throughout. Every omitted j>4096 column is covered by the analytic inverse-power sums and remainder; the high block is not replaced by a finite matrix.

3. **Outward kernel enclosures.** The Binet expansion at shift 128 has the explicit remainder in the proof. The diagonal spacing-two Euler--Maclaurin coefficients are 1/2, 1/2 and -1/6; its absolute remainder is -f'''/90 because the displayed fourth derivative is nonnegative on the entire remaining ray. This derivative and normalization were checked independently. The omitted exponential Gamma and scalar-S tails are included. Serialized endpoints are checked outward as exact dyadic rationals.

4. **Exact Schur and interval LDL.** The finite cross-column sum uses integer centers, integer radius enclosures and upward integer reciprocal weights. Its full rank-one uncertainty is subtracted once. The structured infinite tail is subtracted as a positive rank envelope, not replaced by an unjustified small scalar. Symmetric interval intersection and every LDL operation preserve outward enclosures.

5. **Fresh reproduction.** The complete kernel was regenerated independently without a saved coefficient file, and the exact Schur calculation and grouped rational checker were rerun. All 64 pivot intervals have positive lower endpoints. The minimum lower pivot is 0.0009073396631342025; the first high comparison is greater than 2.0732853777616627. The finite cross uncertainty is below 8.594e-15 and the structured scalar remainder below 3.330e-26. These pivots are not asserted to be eigenvalues. The theorem's lower bound is the separately inserted 10^(-10) target.

The regenerated interval data had SHA-256 5b6d56a17d725aeb7fba30495032807f60facad2da84613f8403288fea87e8d9. This identifies a reproducible output, not a frozen input required for the proof.

## Domain and actual endpoint consequence

The matrix identity differs from its logarithmic diagonal by bounded forms. The finite-span inequality therefore extends by the stated closed-form convergence. The actual sharp head restrictions have stronger positive fractional regularity and belong to this domain. An arbitrary nonzero-trace source is not thereby assigned separate original P and N membership; the actual application retains the weighted potential domain.

The accompanying mixed-forcing and reflected-potential estimates were checked with the complete odd Gamma kernel, all forward and reflected primes, the full pole, the true Mobius seed and the same hidden mean. The degenerate hidden endpoint is paid by its explicit amplitude/mass split, not by a false bounded generic endpoint operator.

For an actual source at positive depth, the new head sign gives

    delta N_head <= Q_delta[head] <= ||B_delta tail||_2^2 / gamma_H,
    gamma_H = 10^(-10).

Combining the full mixed bound, the reflected tail estimate, and the N triangle inequality yields exactly the coefficient 8000/(delta gamma_H)+8 C_V. The actual amplitude bound then gives the squared mass observability stated in ACTUAL_ENDPOINT.md. The changed constant-psi gauge and pole remain intact; no global U constraint is silently imposed. C_V and C_amp(delta) retain their proved analytic definitions, with no claimed certified numerical product or uniformity as delta tends to zero.

## Limits

The positive head does not make its complete mixed Gamma/prime/pole incidence vanish. Its tail Schur subtraction and the remaining original signed form have no favorable sign supplied by this package. The actual norm-transfer consequence is not a supercritical-state exclusion or a proof of RH.

## Pinned source artifacts

The nine mathematical/code artifacts below were reviewed. The manifest and all 22 prospective mathematical links were checked. Generated JSON, cache files and run logs are excluded from the publication source whitelist.

- `REPORT.md`: `cf7b3eec7010f56c87f47c75b27348396a5ccf506089215ae81faada688f6c6e`
- `GAMMA_SINE_GRAM.md`: `e639c47fda61f1026ca7ff3e80bb4c13a11ff8509466b629cdb9eb8d974c01da`
- `GROUPED_HIGH_TAIL.md`: `90fc15ba44b0766c812af6e702f3e6d137700ac64aecbd5692cbee223e4a8f52`
- `MIXED_FORCING.md`: `2166db109787266aef7e5550358656de9d6e2b9c1da24246c344325591e53894`
- `POTENTIAL_TAIL.md`: `dcb2b18bd991628adf363bb1eca5677ca28a7be2c4c788e042bfb5255a7d8925`
- `ACTUAL_ENDPOINT.md`: `b59740ed9558f1d23ac3e3624d9fddcf1eb9b41b3eaa97aacb1c93f880933280`
- `certify_unrepaired_head_kernel.py`: `8a7e57019acb6f75c49e2f9630af25e8e1fe873226a383b9d5b62f8f3775b25a`
- `certify_unrepaired_head_schur.py`: `56aee58c8d35efc69f7d09ea9fc00f7b53f50d412a665da41ff8e4ce33c2802c`
- `check_grouped_head_high_remainder.py`: `7a6e700b925eabd3ebbf4082196c8ee88d446d0fab999ad6536ade84d9582b6c`

Manifest `SHA256SUMS`: `e2316a3a07d63f65e8ef68e069f7c5ff236dfd446e4646f3322e86af3e8b4f64`.
