# Growing theta-jet profiles and a true old-space Schur trial

The fixed finite theta frame is now quantified when its dimension grows. [GROWING_JET_FRAME.md](GROWING_JET_FRAME.md) proves that, for m <= (log k)^(1/4), Taylor-normalized combinations of the first m exact theta-source zero modes approximate every degree-<m polynomial on the entire tail in a fixed polynomially weighted H1 norm, with relative error

    k^(-1) exp(C_A m^2 log(m+2)).

The estimate includes matrix conditioning, rational Taylor remainders and every omitted theta frequency. Raw mode coordinates may still grow with k. The [independent frame review](REFEREE_FRAME.md) checks this scope.

[LAGUERRE_SCHUR_TRIAL.md](LAGUERRE_SCHUR_TRIAL.md) uses the estimate to construct an actual full-old-space trial. For every fixed nonzero complex W in C_c^infinity(0,pi), it produces an old-window v_k and a new-collar y_k such that

    ||y_k||^2 -> 2 integral_0^pi |W(s)|^2 exp(-2s) ds > 0,
    A_(k+1)[v_k+y_k] = o(1).

The construction pays the complete Gamma energy, all signed prime-power correlations, the true coefficient-two polar functional and the exact noncompact theta-source pairings. No fixed-dimension limit is substituted for the growing estimate.

If the entire old block is coercive at the endpoints under consideration, the actual full-old Schur form consequently satisfies

    Schur_(k+1)[y_k] <= o(1).

The [independent trial review](REFEREE_TRIAL.md) checks the complex normalization, full tail domains, endpoint terms and variational interpretation. This is a conditional upper bound on nonvanishing collar profiles. It supplies no lower bound or sign and proves no RH result. It does not assert the same conclusion after constraining the old trial to the complement of a fixed pivot; that needs separate projected-frame estimates.

The remaining problem in this local route is to prove nonnegativity of the exact Schur remainder after eliminating all old directions, with its finite-pivot, mixed-row and new-target terms accounted for together. The [exact collar subprincipal form and inverse ledger](../20261013_collar_subprincipal/REPORT.md) specify the terms that this comparison must retain.
