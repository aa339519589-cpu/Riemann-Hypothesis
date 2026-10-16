# Prior-source comparison for the Heath-Brown crossing corollaries

16 October 2026. This note corrects the scope of the comparison and provenance, not the mathematical proofs of the linked corollaries.

## The relevant prior source

Mark Lewko's [zero-density repository, pinned registered version](https://github.com/mrklwk/zeta-density-39-over-17-lean/tree/ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0) states, for every fixed 3/4<sigma<=1 and epsilon>0,

    N(sigma,T) <= C_(sigma,epsilon) T^(3(1-sigma)/(2 sigma)+epsilon), T>=2.

Its count is for the actual Mathlib Riemann zeta function, with multiplicity, both ordinate signs, real-part equality and height endpoints included. The theorem is `GuthMaynard.Improvement.combined_density_curve`; its right-hand branch calls the native stronger-density theorem. This is not merely a desired analytic estimate restated as an unproved premise.

The inspected registered commit is `ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0`. Its README describes a Lean 4.35.0-rc2 compatibility migration, distinguishes its local checks from the unrun full hosted preflight, and identifies the earlier [public Lean 4.34.1 release](https://github.com/mrklwk/zeta-density-39-over-17-lean/tree/6a2c941b69f2ae91bfa0a63a8b867bfa829db6df). Both pinned versions contain the displayed actual-zeta endpoint. Selected endpoint and large-values files differ only in module/import/exposure syntax. This does not assert that every file of the two releases is identical.

The [machine-readable registry](https://data.palomar-registry.org/recent.json), entry `PALOMAR-2026-10-11-000010`, version 1, records `published_at: 2026-10-11T09:00:10Z` and source commit `ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0`. This is the registry publication timestamp supporting the prior-source comparison, not a public-time inference from Git author metadata. A registry label alone was not used as mathematical verification.

## Effect on our comparisons

The source's coefficient 3/(2 sigma) is strictly smaller throughout the stated intervals of our following reports:

- [The k=3 crossing corollary](../20261016_hb_crossing_density/REPORT.md), coefficient 7/(29 sigma-19), sigma in [.770,.7735]. The comparison is equivalent to sigma<57/73, which holds throughout.
- [The k=4 crossing corollary](../20261016_hb_crossing_family/REPORT.md), coefficient 15/(89 sigma-61), sigma in [29/38,13/17]. The comparison is equivalent to sigma<61/79.
- [The k=5 crossing corollary](../20261016_hb_crossing_family/REPORT.md), coefficient 39/(301 sigma-211), sigma in [547/720,127/167]. The comparison is equivalent to sigma<211/275.

Thus those correct established-input corollaries are improvements over the explicitly identified table entries, not improvements over every prior announced bound. They must not be presented as a new best-known zero-density curve or as gains over Lewko's stated curve. Their proofs, exact arithmetic certificates, and original identified-table comparisons are unchanged. No percentage of actual zeros is implied.

Our later general-pair and local-envelope reports explicitly compare against 3/(2 sigma) on their respective stated improvement intervals; this note does not change those comparisons.

## What was independently checked

An independent internal read-only audit traced the actual-zero count, endpoint parameters, the new comparison/Mellin-reflection/local-cover/bootstrap large-values argument, and the short/long zero-detector conversion. No concrete gap was identified in those reviewed parts. A separate lexical import traversal found 822 local modules in the inspected endpoint/large-values closure, no missing local imports, and no proof-hole or unsafe declaration tokens in that closure. The challenge specification's placeholders are outside it.

These checks do not amount to an independent Lean build, kernel replay, NanoDa run, or a line-by-line verification of every imported analytic foundation. No downloaded author code was executed. The repository's verification receipts are author-supplied evidence, not runs performed by us. The exact distinction between the registered migration and earlier release is retained.

The appropriate conclusion is to acknowledge a substantive prior primary source and qualify our comparison claims, while neither dismissing it as an empty conditional criterion nor claiming that we independently kernel-certified its complete formalization.
