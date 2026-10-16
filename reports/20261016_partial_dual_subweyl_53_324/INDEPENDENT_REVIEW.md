# Independent internal review

## Verdict and exact scope

The complete additional partial-dual argument passes this internal analytic, source and code audit, together with independent separate-copy replays. Under the explicit dependencies identified in the report, it proves

\[
 |\zeta(1/2+it)|\le 10^{23}|t|^{53/324}(\log|t|)^{25/54}
 \qquad (|t|\ge3).
\]

The retained minimum with the preceding bounds is important. The coefficient is large, and the report only claims improvement over the specified preceding function bound at sufficiently large heights. This is not an unrestricted exponent-record, priority, zero-free-region, zero-count, or RH claim. This review is not external peer review or formal kernel verification.

## Frozen files reviewed

- `REPORT.md`: `f5633fbb7e8901b6666df460260a743691faa4a19433b76e4fb4c1d8ebd1fc7a`.
- `PARTIAL_DUAL_LEMMA.md`: `285613cd68b10bd811556528a36b3a8a64ac71053e09943b17f45ca004cb8e65`.
- `ACTUAL_OUTER_ASSEMBLY.md`: `5127ed090ecb01c977fdad03583107a6f1d5b3b04a0d215fcf79a6082ac3ad00`.
- `certify_partial_dual_jets.py`: `d6af1dca6629ea0fc169dcd85b0d319a5a519092bea824a92252ac7cbf66117f`.
- `partial_dual_jets.json`: `67d5703245d4405965a738caa1e80737f499c565b08e17f2a97a23efb81ae916`.
- `certify_outer_assembly.py`: `0369a1acd0b79bdb78134a7e21e1d58d3bfe0515786bf6ae5cd0191d156bb90e`.
- `outer_assembly.json`: `de4d7c2ab7b445308ece97d8987f6d9d6ac58109699c7efa525737c3110ee568`.
- `certify_global_partial_dual.py`: `6bf9289fbb14a9f0deb2b85cb99670063fb48196076d2ccb8f93c4c36930ecfd`.
- `global_partial_dual.json`: `29f5d9574f35682b147e689dc16d098d3fb0ea65a41b6ef5025cd63eecfdefaf`.

## Local and source interface

I fully checked the separate local partial-dual lemma, not merely its numerical output. The audit reopened [Patel--Yang, arXiv2302.13444v1](https://arxiv.org/html/2302.13444v1), in particular the decreasing-derivative Poisson Lemma 2.3 and its complete endpoint, third-derivative and logarithmic errors. The negative-phase convention, extended stationary inverse domain, finite triangular inverse-jet recurrence, full amplitude Abel norm, bounded-frequency boundary twist, signed Hessian lower bounds, inclusive lattice recurrence and exact boundary-equality debit all check. The local complementary cases cover small phase scale, short dual intervals, small cutoff degree and short differencing length.

The accepted rectangular lemma and original mixed-coordinate cutoff/amplitude argument are substantive dependencies. Their role is explicit, and they are not replaced by an unspecified multidimensional estimate. The predecessor report exists at the stated sibling publication target. The earlier global bound is used for the lower-height splice only.

## New actual-phase and outer assembly

The three coordinate differences annihilate the original bilinear term and every separable cutoff phase before the new partial Poisson step. The resulting leading mixed derivative has the stated positive normalization. Differentiating the shift average through order eight uses the original phase through order eleven. The falling-factorial denominator bound, geometric differentiated-series remainder and total-shift relative error jointly imply the full local C8 hypothesis on the enlarged rectangle.

All five local rows use the same outer lengths `H,H^2,H^4`. I independently recalculated their rational exponents and the floor losses. The boundary row survives as `M N^(15/16)`. The inverse and derivative rows are not optimized using incompatible lengths, and the small terminal phase scale is paid by the explicit inverse row. The constant `10^7` dominates every complete propagated coefficient.

## Complete global range and errors

The signed first-correlation sum is preserved until the two-dimensional step. Its actual stationary endpoints, phase and amplitude agree with the original logarithmic correlation. The first Poisson error retains the complete logarithm and reserves exactly one additional maximum stationary weight for the bad-label lattice endpoint. No second endpoint debit is silently omitted or charged to a different range.

For the good range, `R0=64 a^(4/3)c^(-5/9)` enforces the common outer parameter lower bound. The new lower original-block scale `t^(43/100)` is necessary for the displayed shift proof: it yields the decaying exponent `-1/4050`. The former `3/7` cutoff is not reused. Every good block satisfies the enlarged series and derivative domains, all dual bins have length at least two, and the complete logarithmic bounds improve above the fixed height threshold.

Both original curved boundaries and all three dual bins are retained. The original arbitrary-frequency twists are annihilated by the three outer differences; the different inner cutoff uses only the bounded-frequency lemma. These two mechanisms are not conflated. The full Abel amplitude, geometric sum over correlation scales, and lattice row give all five rows in the main ledger and the separate cutoff debit.

Every bad label is below `2R0`, whether or not `R0<q`. Its full trivial stationary length, after the once-reserved endpoint, gives the claimed small-r row. Thus small outer parameter and short original dual-scale complements are paid without an unstated range exclusion.

I independently checked every normalized exponent in (13)--(14). In particular, the endpoint row has a negative original-block power and is evaluated at the lower block endpoint, not at `sqrt(t)`. The entire first-Poisson derivative and logarithmic rows remain present. The large-block square coefficient is below `10^10`; retaining the positive original-block power then gives the complete geometric sum rather than a sampled or truncated sum.

## Initial range, middle range and all-height closure

The original integer partition has no gaps, including shortened final blocks. The initial trivial sum, both published fourth-derivative middle rows and both Riemann--Siegel remainder terms are included. The small positive middle-range exponent gap is exactly `1/113400`, and is retained in the infinite-tail estimate.

All normalized error functions decrease above `log t=160000`, except the constant main and diagonal terms. The directed certificate therefore pays a whole infinite tail, not only its endpoint. The preceding `19/116` bound pays the entire lower interval because its normalized comparison envelope is increasing there. Conjugation pays negative heights. The comparison with the preceding bound above `log|t|=250000` has the claimed decreasing ratio.

## Independent reproduction

On 2026-10-16 I ran all three pinned certificate scripts from a separate audit copy, using 192-bit Arb arithmetic with python-flint 0.9.0 / FLINT 3.6.0. Every script terminated with PASS, and all three regenerated scientific JSON files were byte-identical to the pinned originals. The complete script implementations were read, including the finite series identities, exact rational exponent ledger, sign-dependent endpoint selection, fourth-derivative constants and every monotonicity/splice assertion.

The replay gives:

- complete large-block square coefficient less than `1667914553.970`, hence below `10^10`;
- full infinite-tail coefficient less than `15416723.203`, hence below `10^23`;
- full lower splice coefficient less than `2.200072354235e22`, hence below `10^23`;
- comparison ratio less than `2.075870e-8` at `log|t|=250000`.

These interval outputs certify the written finite expressions. The analytic source normalization, full range coverage and limiting statements were checked separately as described above.
