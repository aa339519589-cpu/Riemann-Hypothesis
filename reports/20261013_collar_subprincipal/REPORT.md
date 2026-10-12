# Exact next-collar Gamma form and a controlled inverse expansion

For the explicit odd source form in [SOURCE_FORM.md](../20261012_localized_odd_schur/SOURCE_FORM.md), the entire next collar, with its maximal Gamma energy domain and true polar coefficient two, admits the exact reconstruction in [SUBPRINCIPAL_FORM.md](SUBPRINCIPAL_FORM.md). In unit interval coordinates, its new/new block is

    D_k = log(k) I + B_cell -(gamma+log(pi)) I + R_k,
    ||R_k|| = O(k^(-1/2)).

If the exact negative polar rank one is retained explicitly, the remaining bounded error is O(1/k). The same calculation identifies the first Gamma remainder as -h/4 times the constant-profile rank one and proves the odd reflection kernel is positive semidefinite. The complete prime-power diagonal on the new collar is exactly zero by its physical support geometry.

[RESOLVENT_EXPANSION.md](RESOLVENT_EXPANSION.md) turns this into a constant-order expansion of the actual new-collar inverse on operator-domain profiles. For a source row b_k=-log(k) g_k+e_k it keeps both the subprincipal form and the constant-order term -2 Re<g_k,e_k>, with an explicit remainder. A bounded row error cannot be discarded in a Schur difference whose leading terms saturate.

The [form review](REFEREE_FORM.md) and [inverse review](REFEREE_RESOLVENT.md) independently check the normalization, full domains, coefficients and remainder estimates. These are mathematical reviews, not proof-assistant verification.

The results concern the entire new/new block of this explicitly defined odd source form. They do not evaluate the Green correction from eliminating the entire old window, whose sign is the outstanding step in this local Schur route. They do not prove RH. The repository's separate latest original even closed-form bound, [49999/100000 at commit f46a42a](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/f46a42a55eec41ecfb8b45c9c28ed2849ee8379a/reports/20261012_adaptive_spectral_tail/FINITE_HEIGHT_GAP.md), is not an input to these calculations.
