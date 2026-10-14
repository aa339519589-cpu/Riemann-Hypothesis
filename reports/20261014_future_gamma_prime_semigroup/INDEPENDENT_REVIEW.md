# Independent mathematical review

## Reviewed versions

This review applies to the following SHA-256 versions:

- `REPORT.md`: `32cb45cbdaaeecf8920927bd9a3890e0ae275760af2dbc838b5e49ee023d0f4a`
- `FOUNDATIONAL_INTERTWINING.md`: `f00a5f014b87a2875ac7bfa7058677d73377190b53b4d09b34865a0a0b22fe3a`
- `SEMIGROUP_AND_HIDDEN_LIFT.md`: `f0a803b6ac8c0369dcd9a52fab7d49974e6b21c7d37ba25f232a9fa5596f8b52`
- `REFLECTION_AND_WALL.md`: `1c77882d138a67d6dbc9f7f785d3f4ebc10c54d08b71883046246f88d05d0de4`
- `check_future_intertwining.py`: `b51bcb9c3c12333828ffeb80dc3e88bab3ddb331e72ab368da7662872ef8227c`
- `check_semigroup_coefficients.py`: `ab508858602b55a7179eb637e55d518771587d389de819b7e2ac44d87f460146`

## Conclusion

The complete future intertwining, positive semigroup, full-filtration hidden realization, and reflected wall formulas are correct in their stated domains. They do not establish positivity of the original two-sided odd quadratic form.

## Checks of the proof

1. **Future normalization and commutator.** With `z=pi exp(2x)`, the Gaussian row is `L_+B/B=x+C0/2`. The translation convention gives `[C,X]=F_+ C`, hence `D C=C D0`. All future sums converge normally on the stated theta class. The positive ground generator contains both the continuous Gamma rate and every Mangoldt prime-power rate. The eta/Phi intertwining retains its rational potential and complete covariance defect; it is not an unweighted Markov intertwining.

2. **Finite-time kernel.** The finite divisor identities imply normalization by positive Tonelli summation and composition by the beta integral. In particular all integer labels occur at positive times, although only prime powers survive the derivative at zero. The exact diagonal identity involving `log n=sum_{d|n}Lambda(d)` gives the displayed generator, including its diagonal payment. The argument proves strong continuity on `C_0([z0,infinity))` for each `z0>0`; the generator calculation uses its stated differentiable core. No inverse zeta operator or inverse Hardy-domain claim is used.

3. **Full observed filtration.** The integer transition probability `d^(-t)J_t(n/d)` is normalized, composes, and has the claimed death rates. In the joint endpoint density the factor `d^(-t)` cancels the Gamma scaling factor `d^t`. Crucially, the resulting identity is the full fiber-kernel relation `Lambda Q_t=P_t Lambda`, not only equality of observed marginals. Together with fiber multiplication it proves the posterior by induction for arbitrary finite observed-time cylinders. The monotone-class and cadlag extension then retain the entire natural observed past. Independence is imposed on the driving increments and clocks conditional on the initial sample, not on the dependent initial variables `Y0=N0^2 z` and `N0`.

4. **Reflection and wall.** The substitution `z -> pi^2/z` gives the stated powers of `pi`, `z`, and the integration variable in the reflected kernel. The wall coefficient follows from the elementary mean of `J_t`, a dominated weighted Riemann sum, and the exact Mellin conversion. It is a leading term plus a little-oh remainder, allowing a zero coefficient. Pole centering removes the first-order wall coefficient but does not imply a vanishing finite-time wall. The polynomial Phi/psi ladder agrees with both the reflected formulas and the source pole normalization.

5. **Domains and exclusions.** The reflected source formulas require the specified two-sided theta decay. The raw theta constant does not meet the reflected integration domain, and a divergent backward theta prime row is never assigned a separate finite value. The odd polynomial seed changes sign near the wall, and the original odd ground vanishes there. Therefore positivity of the future kernel cannot be transferred to the original signed form without its reflected, trace, differential-ladder, and pole contributions.

Both accompanying checkers were independently run and passed. Their exact divisor, covariance, hidden-chain, and polynomial checks supplement the analytic proofs; their numerical row checks are not substitutes for convergence arguments or a quadratic-form sign proof.

## Scope of the result

This is a constructive positive realization of the full **future** Gamma-plus-prime operator, with an exact account of its reflection and wall. It neither proves `K <= I` nor rules out a supercritical Green state. Any application to that comparison must additionally prove the relevant original-domain closure and retain the complete signed boundary and pole terms.
