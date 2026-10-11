# Round 12 — Bombieri null-cone audit

## Status

This is a new negative theorem about one proposed RH route. It is not a proof or disproof of the Riemann Hypothesis.

## Proposition

Assume that only finitely many nontrivial zeros of ζ lie off the critical line. Let `I=(0,L)` be a finite interval. In Bombieri's literal multiset coefficient category, the following three requirements do not exclude a nonzero null state:

1. `z` is in `l2` and is normalized;
2. at least one half of its `l2` mass lies on critical zeros;
3. its local waveform vanishes on `I`.

More strongly, there is a nonzero coefficient vector supported entirely on critical zeros whose local waveform is zero. Therefore the exceptional coordinates may all be zero while every displayed limiting condition remains true.

## Derivation

Let `Lambda_C` be the distinct critical ordinates and let

`S_C c(u) = sum_{lambda in Lambda_C} c_lambda exp(-i lambda u)`.

Under the finite-exception hypothesis, the unconditional Littlewood gap theorem implies that the distinct critical ordinates have arbitrarily small eventual mesh. With `a=2*pi/L`, choose actual critical ordinates near `a*n` for all sufficiently large positive and negative integers. Kadec's 1/4 theorem, followed by finitely many replacements by unused actual critical exponentials, gives a Riesz basis subfamily `B` of `L2(I)`.

The finite-replacement step is not an appeal to density alone. The zero-existence form of Littlewood's theorem gives the mesh statement for distinct ordinates. The resulting Kadec tail is a finite-codimensional Riesz sequence. If a finite-codimensional complement remained outside the span of all actual critical exponentials, a nonzero `L2(I)` function in its orthogonal complement would have a finite-exponential-type Fourier transform vanishing on the critical divisor; the critical zero count (with only finitely many multiplicity corrections in the simple-eventual case, and the mesh estimate in general) rules this out. Therefore actual critical exponentials fill the finite quotient, and a finite replacement can be chosen with an invertible quotient matrix.

There are now two exhaustive cases.

* If some critical zero has multiplicity at least two, the two literal multiset coordinates at that ordinate give the immediate kernel vector `(1,-1)`.
* If only finitely many critical zeros have multiplicity greater than one, the Riemann--von Mangoldt count gives more distinct critical ordinates than the `O(T)` number used by `B`. Hence an actual critical ordinate `lambda_*` is outside `B`. Its exponential has a unique `l2(B)` expansion

  `exp(-i lambda_* u) = sum_{lambda in B} b_lambda exp(-i lambda u)`.

  The coefficient vector with value `1` at `lambda_*`, values `-b_lambda` on `B`, and zero elsewhere is nonzero, belongs to `l2`, and synthesizes identically to zero on `I`.

Thus in either case there is a nonzero critical-only `k` with `S_C k=0`. After normalizing `k`, its critical mass is `1`, so it satisfies the half-mass condition.

The same kernel also shows why the exceptional packet cannot be separated by the unweighted range condition. For any finite exceptional waveform `f_E` in `L2(I)`, choose a critical representation `S_C c^0=-f_E` using the Riesz basis. Then

`S_C(c^0 + R k) = -f_E`

for every scalar `R`, while the critical coefficient norm tends to infinity as `|R|` tends to infinity. Consequently the normalized vector `(e,c^0+Rk)` has critical mass tending to `1`; for sufficiently large finite `R` it has nonzero exceptional coordinates, vanishes locally, and satisfies the half-mass inequality.

## Source-fidelity audit

Bombieri's Section 11 gives the limiting equation

`lambda z_gamma = integral_I exp(i gamma u) F(u) du`,

the critical-mass inequality, and the implication `lambda=0 => F=0` locally. It does not assert that the selected coordinatewise limit has nonzero exceptional mass, nor that it is the minimum-norm exact representation in the critical coefficient fiber. The pure-critical kernel above therefore satisfies all of the theorem-level conditions that the limiting argument itself exposes.

This does not prove that Bombieri's particular finite-truncation eigenvector sequence has a pure-critical limit. That is the remaining provenance question. It does prove that no contradiction can follow from the limiting null equation, normalization, and half-mass inequality alone.

## Finite-`N` provenance audit

The truncation parameter does not by itself restore coercivity. Let `G_C,N` be the critical-only finite local Gram block. Truncating the nonzero critical kernel `k` above gives critical coefficient vectors `k_N` with

`||S_C,N k_N||_L2(I) -> 0` and `||k_N||_2 -> ||k||_2 > 0`.

Therefore the smallest critical-only singular value tends to zero (and is exactly zero once a literal duplicate pair enters the truncation). This collapse occurs without using any exceptional zero. It is consequently compatible with, and can contaminate, any argument that treats `lambda_N -> 0` as intrinsically exceptional information.

The negative eigenvector branch may still contain additional information, but it must be extracted from the branch itself: a valid theorem would need, for example, a lower bound on its exceptional projection, a canonical quotient/minimizer statement, or a rate inequality that is proved for that selected branch and not just for the critical block. Bombieri's Section 11 does not supply such a statement.

## Route decision

**Closed route:** unweighted exact-range separation and any argument using only the displayed limiting mass cone.

**Live route:** prove a source-faithful theorem about the actual finite-truncation eigenvectors—e.g. a canonical quotient representative, a uniform lower bound on exceptional mass, or a quantitative asymptotic invariant that survives `lambda_N -> 0`.

**Important limitation:** a minimum critical synthesis norm is not automatically relevant. Bombieri does not prove that the selected limit minimizes the norm over the affine critical synthesis fiber; without that missing selection theorem, the minimum norm and the actual provenance vector are different objects.

## Ledger update

### Confirmed facts

- Critical-only nonzero `l2` local kernels exist in the literal multiset category under the finite-exception hypothesis.
- The half-critical-mass condition is compatible with a pure-critical null state.
- Adding a critical kernel direction makes the critical coefficient norm unbounded along every exact local synthesis fiber.

### Failed mechanisms

- Unweighted local range separation.
- The limiting Bombieri equation as an additional exceptional constraint.
- The half-mass inequality as a standalone finite-exception obstruction.

### Still assumed / unknown

- Whether the specific finite negative-eigenvector sequence has a canonical quotient limit.
- Whether its exceptional mass is bounded away from zero.
- Whether any finite-`N` rate or resolvent invariant survives the null limit and is source-specific.

### Next route

Audit the finite-`N` eigenvector provenance in the exact Bombieri matrix, with duplicate directions quotiented source-faithfully. A successful theorem must constrain the selected representative, not merely the existence of a local null vector.

## Nontracial Frobenius/residue audit

There is a genuine algebraic object that sees jets. If `Xi(s)=(s-rho)^m u(s)` near a zero `rho`, with `u(ρ) != 0`, then

`A_rho = O_rho/(Xi)`

is an `m`-dimensional local algebra and

`B_rho([a],[b]) = Res_{s=rho} a(s)b(s)/Xi(s) ds`

is a well-defined nondegenerate Frobenius pairing. The well-definedness follows because replacing `a` or `b` by a multiple of `Xi` changes the integrand by a holomorphic function. The coefficient of `(s-rho)^(-1)` couples the local Taylor jets of both slots.

The canonical logarithmic-derivative slot does not use that extra information:

`Res_{s=rho} F(s) Xi'(s)/Xi(s) ds = m F(rho)`.

This is the trace of multiplication by `[F]` on `A_rho`; all nilpotent directions disappear. Meyer and Connes' source-evaluable formulae are likewise trace/character formulae: they provide the divisor and prime/archimedean terms, but not a proved arithmetic selection of a second holomorphic slot in `A_rho`.

The most obvious alternative, `b=1`, would lead formally to residues of `F/Xi` and, in the half-plane of absolute convergence, to reciprocal-zeta/Mobius data. Extending that contour identity across the complete zero divisor requires uniform growth and contour-limit estimates for `1/Xi` near zeros. Even if supplied, its residues carry local Taylor coefficients of `1/Xi` (for simple zeros, weights such as `1/Xi'(rho)`), not Bombieri's coefficient state. No bridge from those weighted residues to the source-selected Bombieri vector is currently proved.

**Verdict:** the Frobenius pairing is an algebraically valid candidate, but the arithmetic second-slot theorem and the Bombieri-state linkage are missing. It remains a conditional research route, not an RH proof.

## Finite-prime/prolate route audit

The current finite-prime proposal can be stated without numerical shorthand. For each
`lambda`, let `A_lambda` be the selfadjoint operator representing the Weil form on
`L2([lambda^-1,lambda],du/u)`, let `epsilon_0(lambda)` be its lowest eigenvalue,
and let `theta_lambda` be a normalized lowest eigenvector. The real-zero theorem for
Fourier transforms applies to `theta_lambda` only after proving that the lowest
eigenvalue is simple, isolated, and has an even eigenvector.

The explicitly constructed `k_lambda` is a different object. The source proves that
its Fourier transform tends locally uniformly to `Xi` in the relevant strip, but
describes `k_lambda` as a near-radical approximation/educated guess for `theta_lambda`.
That convergence statement therefore cannot be substituted for convergence of the
actual ground states. Hurwitz becomes applicable only after both links are proved:

1. `theta_lambda` and `k_lambda` must be normalized with a fixed phase and satisfy a
   Fourier-controlling error estimate; a bare `L2` or Rayleigh-quotient estimate is
   insufficient while the support length tends to infinity. A sufficient form is
   `int |theta_lambda(t)-k_lambda(t)| exp(R|t|) dt -> 0` for every fixed `R`, which
   gives uniform convergence of their Fourier transforms on `|Im z|<=R`.
2. The candidate must be forced onto the ground-state branch. For example, a spectral
   proof could use a gap estimate
   `delta_lambda=epsilon_1(lambda)-epsilon_0(lambda)>0` together with
   `(<A_lambda k_lambda,k_lambda>-epsilon_0(lambda))/delta_lambda -> 0`.
   Merely showing that both the Rayleigh quotient and `epsilon_0(lambda)` tend to
   zero gives no angle control because the gap may tend to zero faster.
3. The simplicity/evenness claim must hold for the actual Weil operator for every
   sufficiently large `lambda`, not only for the commuting prolate comparison
   operator. A simple eigenvector of a reflection-symmetric operator has definite
   parity, but simplicity alone does not select the even parity.
4. The finite-prime forms and their domains must be identified with the displayed
   `A_lambda` uniformly in `lambda`, including the archimedean term and the two
   vanishing constraints. Otherwise the real-zero theorem is being applied to a
   neighboring operator rather than to the arithmetic truncation.

The primary survey states these as remaining steps: it records the real-zero theorem,
the separate convergence of `k_lambda` to `Xi`, and then explicitly says that
simplicity/evenness and sufficiently good approximation of the minimal eigenvector
remain to be shown. Thus this route is a well-posed conditional implication, not an
unconditional closure of RH. The finite-prime numerical agreement supplies evidence
for the candidate but cannot replace the branch-selection and convergence estimates.

## Reformulation audit: finite-prime Weil positivity

The finite-prime observation does not evade the original target. For compactly
supported test functions, the Weil positivity inequality is equivalent to RH, and
each individual test function uses only finitely many prime factors. The universal
quantifier over all support lengths and all test functions is still the full
conjecture. Establishing positivity for a fixed finite range, or finding a sequence
of nearly null vectors with real-zero transforms, does not establish positivity for
all ranges. A valid closure would need a uniform theorem controlling the entire
increasing family of forms, not only their numerically selected lowest directions.

### Route decision

**Closed as a shortcut:** finite-prime numerical agreement, prolate near-radical
energy, or separate convergence of `k_lambda` to `Xi` without a theorem identifying
`k_lambda` with the arithmetic ground-state branch.

**Live but exactly RH-equivalent:** prove the four items above, then apply the real-zero
theorem and Hurwitz. This remains a legitimate research program, but none of its
load-bearing estimates is currently established in the record.

## Triage of a recent claimed proof

The latest publicly posted version of Yukitaka Abe's manuscript was checked as a
possible direct shortcut. Its Section 5 contains a concrete algebraic error before
the final supremum argument. With

`D = 1/(2*alpha) - R` and `I^2 = R/alpha - R^2`, the displayed tangent line is

`Y = (D/I)(X-R) + I`.

Setting `Y=0` therefore gives the X-axis intercept

`X_B = R - I^2/D = R - (R/alpha - R^2)/D`.

Equation (5.5) in the manuscript instead uses

`X_B = R - I/D`,

replacing `I^2` by `I`. Thus the claimed equation (5.6) is not a consequence of
the two circle equations. This is not a question of uniform asymptotics. For an
independent numerical check, take `alpha=10`, `beta=2`, and the nonzero circle
intersection `R=10/104`, `I=2/104`. The displayed circle relations hold; the correct
intercept is `X_B=5/48`, whereas (5.5) gives `X_B=20/39`. With the corrected
intercept, the tangent identity reduces to the original circle-intersection
relation and supplies no new zero-free constraint.

The manuscript's current hosting page still labels the work an unrefereed working
paper. This audit therefore rejects it as an unconditional RH proof. More broadly,
the latest independently validated AI-assisted result located in the search is a
lower bound for the proportion of zeros on the critical line, not a classification
of the remaining zeros; its authors explicitly state that it does not prove RH.
Likewise, another 2026 manuscript claiming a self-adjoint determinant proof carries
an explicit notice that its proofs contain fatal errors. These items do not close
the canonical task.

## Current closure status

After the ledger audit and the recent-claim triage, the only defensible status is:

`RH unresolved; no unconditional proof or disproof produced in this round.`

The Clay Mathematics Institute's current problem page labels RH “Unsolved.” The
recent Connes survey likewise calls it an unsolved problem and describes the
finite-prime/prolate construction as a potential path whose decisive steps remain
open. These are status checks, not substitutes for the missing theorem.

## Arithmetic-source firewall

The source-side requirement is substantive, not cosmetic. A local residue pairing can be written for any entire function with isolated zeros, so its existence alone has no Riemann-specific force. To become an RH mechanism it would need all of the following in one theorem:

1. a zero-independent global choice of the second slot;
2. a convergent or rigorously regularized sum of the local residues over all zeros, including arbitrary multiplicities;
3. an exact evaluation from primes and the archimedean factor;
4. a positivity or signature statement whose negative directions are exactly the off-critical blocks;
5. a proved map from that state to the Bombieri or Weil quadratic form.

The known canonical source functional meets the arithmetic-evaluation requirement through `Xi'/Xi`, but then meets item 4 only in the usual Weil criterion and loses the jet state by trace. Replacing it by `1/Xi` or a higher-pole logarithmic derivative changes the weights and introduces contour-growth and convergence problems; it does not supply items 4 or 5. A future construction may still exist, but it must close these five separate implications rather than cite the local Frobenius algebra.

## References

- E. Bombieri, [*Remarks on Weil's quadratic functional in the theory of prime numbers, I*](https://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0), especially Section 11 and Theorem 11.
- J. E. Littlewood, [*On the Riemann Zeta-Function*](https://doi.org/10.1112/plms/s2-24.1.175).
- M. I. Kadec's 1/4 theorem is used in its standard Riesz-basis form for exponentials on a finite interval.
- A. Connes, [*The Riemann Hypothesis: Past, Present and a Letter Through Time*](https://arxiv.org/html/2602.04022), §§5–6, records the finite-prime/prolate construction, the real-zero theorem, the separate `k_lambda` to `Xi` convergence, and the remaining ground-state steps.
- A. Connes and W. D. van Suijlekom, [*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*](https://arxiv.org/abs/2511.23257), proves the conditional real-zero localization theorem used by that route.
- Y. Abe, [*A rigorous proof of the Riemann hypothesis*, Version 26](https://www.cambridge.org/engage/coe/article-details/6a52f0d3810b9dcc82011b00), §§5–6, for the tangent-intercept check above; the hosting page identifies it as an unrefereed working paper.
- Anthropic, [*Learning more about Claude's mathematical capabilities*](https://www.anthropic.com/research/riemann-zeta), for the 2026 partial zero-proportion result and its explicit statement that RH was not solved.
- Y. Shimizu, [*Proof of the Riemann Hypothesis*, latest Zenodo record](https://zenodo.org/records/21108581), whose current disclaimer says the working draft contains fatal proof errors.
