# Independent mathematical review: complete boundary graph coercivity

The theorem in [REPORT.md](REPORT.md), SHA-256
`1008609f71c3cce86990e172184bf13fff686587b100d459cd3461b245e39aef`,
is correct on its stated finite-form domain. For 0<=delta<=1/3 it proves

    H[u]+(1-delta)N[u]-P_pole[u]
       >=(9/50) integral psi |u-c_C(u)|^2,
    C=(0,7/10), c_C=(integral_C psi u)/(integral_C psi).

This is a complete nonlocal signed boundary-graph inequality, not merely a
positive diagonal row. It is not positivity of Q_delta=2F_G-B_delta.

## Factors and absence of duplicated edges

The central wall is spent only once. Its symmetric central square gives
h_C=2kappa(7/5)integral_C psi. The negative pole is bounded by its diagonal
after the same constant gauge, with its original mass integral s psi=1/8
and its retained positive remainder +8|integral s psi(u-c_C)|^2.

The reflected cross part has both orientations and therefore coefficient
2beta, beta=1-delta. Its exact elementary identity is

    2beta|a-b|^2
      =|a|^2-k_beta|b|^2+(2beta-1)|a-k_beta b|^2,
    k_beta=2beta/(2beta-1)<=4.

It yields the tail credit L_C and central debit k_beta L_T. The central-central
and tail-tail reflected energies remain unused nonnegative terms. No Gamma
future energy is used by this proof. The complete central and tail brackets
are respectively greater than .185304 and 1/4, exceeding the claimed 9/50.

## Complete scalar enclosures

The central upper row uses the actual reflection restriction for n=2,3,
and the favorable all-integer majorant only for an upper bound when n>=4.
The derivative polynomial proves decreasing psi throughout the required
tail. Both the inner theta sum and outer integer sum have explicit complete
geometric remainders; no omitted term has the wrong sign.

The truncated reflected lower row uses only genuine prime powers in its
moving window. The complete analytic tail uses the .91/349 Chebyshev entry
and J_C>1. The negative endpoint jump of the truncated F is present as
F(R)Psi_C((X exp R)-)/X. At a prime endpoint its left-limit lower bound is
valid because X exp R>349. This yields L_C>.5291 exp(x/2), hence the stated
uniform positive tail margin. The compact interval lower certificate omits
all moving-endpoint and nonpositive lower-enclosure terms favorably.

Checker SHA-256:
`09c6509fc8692e69924b770bc81f0e840cbb65e3590464a1bed7e9b65193475a`.
It was independently executed successfully. The resulting certificate
matched SHA-256
`9e19c1515ba92a94a05f396c22a18266f495a98bf4586c62f17e361c7ecdfb2d`
byte for byte. The minimum compact L_C-s margin is greater than .360180,
not an endpoint or point-sample estimate.

## Domain and random-field scope

Finite central H gives a representative in L2(C,psi dx), so its central
mean exists. Finite polar difference energy gives L2 modulo constants for
s psi dx; thus the displayed pole estimate is not an infinity-minus-infinity
operation. The direct finite-energy proof then applies to real or complex
ratios. Alternatively it extends through common bounded truncations using
the positive edge expressions.

For the previously proved coherent polynomial bridge field, the pair cocycle
and a fixed reference start give a jointly measurable random ratio. Its
polynomial second-moment bounds pay all three edge expectations and its
psi-weighted central mean. Almost every sample therefore lies in this graph
domain. Applying the deterministic inequality and then taking expectations
proves V_H+(1-delta)V_N-V_P>=0, with the stronger stated coercive remainder.
No singular forward-Gamma energy or random original-P membership is needed.
All stochastic neutral mixed terms and finite projection costs remain.

The positive variance correction is the difference between the lifted and
mean boundary graph; it is not a second independent energy budget. The
opposite comparison B_delta<=2F_G required to sign the original Q_delta
remains unproved.

## Exact factorization and common neutral projection

The independently checked companion [POSITIVE_FACTORIZATION.md](POSITIVE_FACTORIZATION.md),
SHA-256 `6cb3d4405ae9ee60729372de038708e49ea7f9602fdb952656dd426bccda3564`,
retains every remainder square. Its cross square is oriented once and has
coefficient 2beta-1, whereas the original reflected cross energy contains
both orientations. This distinction is necessary and is correct.

For genuine common neutral vectors, the radical identity q(s,f)=0 gives
identical Gram matrices and mixed loads in F=2F_G and B_0. Their finite
projections consequently agree, and subtracting that common projection
preserves F-B_0 exactly. The corresponding statement for B_delta would
require its delta N correction and is not claimed. Abstract neutral
completion does not by itself establish extra physical tails or a new
source-domain assertion.

This review also pins [certify_boundary_graph.py](certify_boundary_graph.py)
to the checker hash above and [boundary_graph_certificate.json](boundary_graph_certificate.json)
to its displayed output hash. The package copies change only dependency
links, the reproduction command and the output basename from the executed
mathematical certificate; the arithmetic and interval computations are
unchanged. All cited relative mathematical dependencies resolve.

The proved result is the lower bound B_delta>=0, including its quantitative
coercivity and stochastic graph application. It supplies neither the
opposite comparison B_delta<=2F_G nor K<=1 nor the Riemann Hypothesis.
