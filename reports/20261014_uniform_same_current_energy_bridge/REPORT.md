# Uniform original-forward / same-current energy comparison

For an actual positive-depth source u=r-c_infinity, let w be its complete
eta current-adapted hidden field, v=w_1, e=v-u, and
V=sum_n p_n|w_n-u|^2. Keep the original one-forward-orientation energy F
and the SAME integrated hidden Gamma/divisor/reset bracket E_current.
This package proves

    F[u]/3 <= E_current <= (219/19) F[u].

The key strengthened field comparison is

    int psi(x)exp(x/2)V(x)dx
        <=int psi(x)exp(x/2)|u(x)-c|^2 dx

for every common constant c. It follows from the exact posterior covariance
and the reference-canceled all-label killed-resolvent decomposition, not
from independently budgeting its dominant and higher-label parts.

Consequently the actual first-label error satisfies

    F[e] <= (2847/7600) F[u],
    P_original[psi e] <= (996669/1330000) F[u],
    0 <= B_delta[e] <= (219/950) F[u].

The first two coefficients are strictly below 3/8 and 3/4. Their denominator
is F[u], NOT P_original[psi u]. These are actual-input estimates. Neither e
nor w_1 inherits the actual source equation merely by being a legal test,
so this contraction cannot be iterated on them. The full reflected/pole
form and common neutral projection debit remain explicit.

## Complete proofs

* [UNIFORM_ENERGY_BRIDGE.md](UNIFORM_ENERGY_BRIDGE.md) proves the normalized
  5/4 inverse refinement, the exact reference cancellation, the coupled
  SAME-V inequality and the complete signed-storage payment.
* [INCOMING_PRIME_GAMMA_HUB.md](INCOMING_PRIME_GAMMA_HUB.md), Section 6,
  proves F[f]>=(19/100)int psi exp(x/2)|f-c_(0,1/2)|^2 using the full
  incoming prime-power graph and a central Gamma block, including its
  negative central transfer cost. The earlier 1/10 allocation is retained
  as an intermediate result, not a second energy expenditure.
* [NEGATIVE_TRANSPORT_BOUND.md](NEGATIVE_TRANSPORT_BOUND.md) proves the
  complete bound (-b)_+<=2psi exp(x/2) for the exact original adjoint
  density in F[u]=E_current+int bV. It retains all theta labels, prime
  powers, Gamma-wall terms and the original pole contribution.
* [POSITIVE_ORIGIN_BAND.md](POSITIVE_ORIGIN_BAND.md) proves b>0 on
  (0,1/12], completing the origin part of that bound.

The prior [same-current transfer package](../20261014_same_current_boundary_transfer/REPORT.md)
contains the exact triangular-current equations, normalized strong-metric
operator domains, conditional-tail Schur identity and homogeneous Euler
bound used here. All other public dependencies are linked at their use.

## Reproduction

Run with Python 3 and mpmath installed:

    python check_uniform_bridge.py
    python check_transport_positive_origin.py
    python check_incoming_prime_hub.py
    python check_negative_variance_transport.py

The first two use exact rational arithmetic only. The latter two use
60-digit and 50-digit directed interval arithmetic, respectively, and
regenerate their JSON certificates beside the scripts. The full infinite
arithmetic tails additionally use the explicitly sourced unconditional
Chebyshev bounds; finite computations do not substitute for those bounds.
The certified compact incoming row has 565 rational cells, and the
negative-storage certificate has 667 accepted rational cells.

## Exact remaining limitation

The sought original signed exclusion still concerns Q_delta=2F-B_delta.
The uniform energy bridge does not supply its coefficient-one comparison,
make w_1 an actual null source, or give a favorable sign after neutral
projection. No proof of RH or supercritical-state exclusion is asserted.
