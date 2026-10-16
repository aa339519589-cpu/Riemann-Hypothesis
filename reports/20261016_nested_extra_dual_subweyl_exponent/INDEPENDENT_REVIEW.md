# Independent internal review

16 October 2026, UTC. **Pass** for the stated bound
`|zeta(1/2+it)| <= 110 |t|^(229/1392)` for `|t| >= 3`.
This is an internal mathematical and computational audit, not external
peer review or formal-kernel verification.

## Reviewed bytes

- `REPORT.md`: `4efba9382f2cc1963b0b3fe1adf5a0a62d0fd80455aed720376107574f729251`.
- `certify_nested_exponent.py`: `9cf535114aba1e4a4ef11b0e98d84a9979073c21410f846247cd36cee24ee071`.
- `nested_extra_dual_exponent_229_1392.json`: `e4159b9be38adb83cbc79dfe6f0b9f78145683d01081246213fc4baaddee17c4`.

The complete report and standalone verifier were read. The primary
Patel--Yang preprint's Lemmas 1.2, 1.4 and 2.3, and its conclusion identifying
the classical exponent `229/1392`, were checked directly. The previously
reviewed coefficient-90 theorem supplies only the explicitly stated
dependencies and low-height splice, not an unproved formal pair transfer.

## Analytic audit

1. The Stieltjes derivative comparison and its integrated triple-difference
   form give all seven required derivatives on the actual shifted domains.
   The inverse-derivative polynomial recurrence, its common homogeneity,
   and the extra factor from the actual inverse variable were independently
   derived. Negating the phase and reversing its dual variable preserves
   the relative comparisons used in (10).
2. The second dual interval, monotone positive weight and complete Poisson
   error are correctly normalized. The two new A-processes use the actual
   derivative-domain restriction. The fourth- and fifth-inverse-derivative
   signs justify the monotone fourth-derivative test after the third
   Poisson step. Every noninteger dual partial sum retains its first-point
   debit; the printed decreasing-derivative convention is respected.
3. Both failures of the new inner construction are paid separately by the
   full trivial second-dual length. Reweighting on each failure set gives
   exactly `D^(1/4) N^(-17/56)` and `D^(1/4) N^(-13/24)`, with their cutoff
   constants. Their union is bounded by a sum, not discarded. The second
   Poisson endpoint, derivative and logarithmic errors remain on all ranges.
4. The weighted A-process averages, their masses, negative-power floor
   factors, diagonal terms and all ten returned rows were checked. An
   independent exact-rational calculation recovers the third-Poisson
   powers from its weight/length/inverse-derivative scales, then every
   power in (21), (22), (24) and (29). In particular the small-second-length
   complement has the claimed negative normalized exponent `-1/7424`.
5. The outer integer length, first-dual argument and triple-shift guards
   hold uniformly above the fixed starting height. The bad first-length
   range retains its complete trivial first-dual contribution. Positive
   and negative block powers use their respective complete geometric sums;
   the negative-power endpoint row is not evaluated at the top endpoint.
6. Both nested logarithms keep their height growth, with a negative
   derivative of the complete exponential product. The original first
   logarithm and every original Poisson error are also retained. The
   initial and middle Riemann--Siegel pieces include the shortened top
   block, both halves and both remainder terms. No finite sampling replaces
   the infinite-height argument.

## Independent replay and scope

The standalone verifier was replayed independently from a separate copy,
using official python-flint 0.9.0 / FLINT 3.6.0 at 192-bit precision and
ordinary, non-optimized Python. It exited successfully. The generated
scientific JSON matched the frozen file byte for byte.

The directed enclosures give:

- Complete tail above `log |t| = 10000`: less than `103.140912578044659`.
- Established-bound splice through that height: less than
  `108.203362294481255`.

Both are strictly below 110. Exact arithmetic also verifies
`77/468 - 229/1392 = 1/54288`, so the splice uses its correct exponent.
Conjugation pays negative heights.

The new exponent is classical. This result supplies the explicit constant
and complete ranges for the stated bound, not a new unrestricted asymptotic
exponent, a zero proportion, or a priority claim. The useful bound retains
the minimum with the earlier explicit estimates rather than declaring
this larger-coefficient bound better at every height.
