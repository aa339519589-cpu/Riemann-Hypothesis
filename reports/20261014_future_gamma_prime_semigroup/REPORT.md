# A positive all-prime future semigroup, its hidden arithmetic lift, and exact reflected boundary

This package gives a constructive positive Markov model for the complete
future Gamma-plus-prime generator. It also computes its exact reflection and
wall leakage, retaining the theta differential ladder and pole normalization.
It does **not** prove positivity of the original two-sided odd Weil form.

## Main results

1. With z=pi exp(2x), theta(z)=sum_(n>=1)exp(-n^2z), and
   J_t(k)=product_(p|k)(1-p^(-t)), the complete future transition kernel is

       P_t f(z)=1/[Gamma(t/2)theta(z)] sum_k J_t(k)
            integral_0^infinity v^(t/2-1)theta(k^2z+v)f(k^2z+v)dv.

   This is a genuine strongly continuous Markov semigroup. Its generator
   contains the full Gamma jump measure and every Mangoldt prime-power row.
   Positive divisor identities, not a critical inverse-zeta domain, prove
   stochastic normalization, composition, and Gaussian intertwining.

2. The kernel has a full-filtration hidden model. A gamma subordinator moves
   Y, while independently driven integer prime-power deaths move N by
   n->n/p^j at rate log p. The observation Z=Y/N^2 has the displayed Markov
   kernel. Its exact conditional integer law remains
   exp(-n^2Z)/theta(Z) given the entire observed past, not merely at one time.

3. Reflection z->pi^2/z has an explicit positive backward integral kernel
   on two-sided theta sources. The raw theta constant is outside its domain.
   The future source wall is exactly

       S_t h(x) = exp(-x/2) M_h(t)/[2Gamma((t+1)/2)zeta(1+t)]
                    + o(exp(-x/2)), x->-infinity,
       M_h(t)=integral_0^infinity z^((t-1)/2)H(z)dz,
       h(x)=exp(x/2)H(pi exp(2x)).

   Pole centering makes this coefficient O(t^2), possibly smaller, but does
   not erase the finite-time wall. Exact Phi/psi polynomial identities recover
   the original pole coefficients and keep the higher Theta/Theta' terms.

## Proofs

- [Foundational future intertwining and exact eta defect](FOUNDATIONAL_INTERTWINING.md)
  proves the Gaussian row, arithmetic commutator, positive future generators,
  and the complete eta/Phi covariance identity.
- [Positive semigroup and hidden arithmetic lift](SEMIGROUP_AND_HIDDEN_LIFT.md)
  proves all finite-time, domain, generator, and full-filtration claims.
- [Exact reflected kernel and wall coefficient](REFLECTION_AND_WALL.md)
  computes reflection before any divergent backward prime row is separated.

The actual-source use of the two-sided theta envelope is supplied by the
[bounded actual-ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md).
The original odd source convention and complete reflected-prime pairing are
those of the [full odd variation and boundary report](../20261013_full_prime_green_reference/ODD_VARIATION_PRIME_BOUNDARY.md).
The semigroup identities themselves are independent of any hypothetical
supercritical state.

## Reproducible checks

Run `python check_semigroup_coefficients.py` with the Python standard library
for exact divisor normalization/composition, hidden-chain transitions, and
polynomial gamma-ladder identities. Run `python check_future_intertwining.py`
with mpmath installed for the foundational exact coefficient checks and
high-precision absolute-row checks. Neither checker is a test of the RH sign.

## Exact remaining scope

A positive future Markov semigroup is not a contraction assertion in the
original Weil/source metric. Its original adjoint defect, odd reflection,
trace repair, and full pole contribution must still be controlled together.
No backward theta prime row is integrated separately, no unrestricted
Hardy inverse is assumed, and no full quadratic-form positivity follows
from the positive future kernel alone.
