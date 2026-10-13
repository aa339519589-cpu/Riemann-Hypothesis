# Exact projected theta profiles and the Green load beyond its logarithmic baseline

[PROJECTED_FRAME.md](PROJECTED_FRAME.md) constructs growing theta-jet combinations after exact projection away from a fixed finite old theta-jet space. For m <= (log k)^(1/4), every prescribed degree-<m polynomial is approximated on the whole tail in a fixed weighted H1 norm, with relative error k^(-1) exp(C_(d,A) m^2 log(m+2)). The cutoff old vector satisfies the Q orthogonality exactly. The proof includes growing-index global jet bounds, projection conditioning and all theta frequencies.

For every fixed nonzero smooth compact collar profile W, this gives a Q-admissible source trial with full next-window energy tending to zero. The actual nonnegative-Q Green dual therefore obeys

    G_k(y_k) >= D_k[y_k]-o(1).

Here D_k is the complete new-collar diagonal, including the actual pole, and G_k is defined on the whole old-Q form domain without an L2 norm cap or assumed inverse. The [Green-load proof](GREEN_LOAD.md) combines this with the exact collar subprincipal operator C=B_cell-(gamma+log pi)I. For

    eta_k^Q = sup_(nonzero y in new form domain)
                  G_k(y)/(log(k)||y||^2),

it proves liminf log(k)(eta_k^Q-1)=+infinity along any unbounded set of endpoints where M_k is nonnegative. In particular this logarithmic-baseline quotient exceeds one eventually at such endpoints. The actual signed short remains D_k[y]-G_k(y); only an upper bound tending to zero is proved for it.

The [projected-frame review](REFEREE_PROJECTED_FRAME.md) and [Green-load review](REFEREE_GREEN_LOAD.md) verify the full-domain interfaces and limit order. A separate second review of the Green calculation reached the same conclusion.

The already published [finite-pivot flatness theorem](../20261013_finite_pivot_flatness/FINITE_PIVOT_FLATNESS.md) supplies existential collar trials for arbitrary fixed-rank old constraints. Its finite-dimensional trial method, combined with the collar subprincipal form, also yields the scalar Green-quotient obstruction. The additional construction here preserves each prescribed profile through the exact theta-pivot projection; it does not replace that earlier theorem or claim the scalar obstruction as a new arithmetic estimate.

These results identify why the logarithmic baseline cannot certify the desired contraction. They do not determine the true Schur sign, prove full old-block positivity, improve the original even spectral gap, or prove RH. The remaining estimate must compare the Green load with the complete new energy and retain the finite-pivot, mixed-row and target terms together.
