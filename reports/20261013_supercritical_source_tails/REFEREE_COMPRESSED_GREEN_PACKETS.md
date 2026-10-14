# Mathematical review: compressed Green packets

Reviewed text: [Compressed smoothing on the complete supercritical Green packet](COMPRESSED_GREEN_PACKETS.md).

Disposition: pass, conditional on the cited upstream mathematical results.
An independent model-assisted review checked the exact final candidate
against the earlier packet theorem, scalar compression, origin-domain,
source-domain and complete prime/Gamma calculations. This is not
proof-assistant verification or external human peer review.

The reviewed proof has SHA-256:

    843fdbf5bdee7a26670f3e8cdac338fe6f6f034a5d22c2263a268bbd51081f97

The origin step is dimension independent and noncircular. The old packet
Sobolev estimate controls \(B_og_a\) in \(L^2\). The complete translated
loads are bounded directly as maps of the actual packet, using its
normalized source bound. The band equation first bounds
\(g_{\Delta a}/x\); applying \(\Delta^{-1}\) only afterward gives (9).
It neither sums scalar eigenvector estimates nor replaces distinct
depths by one scalar.

For (11), finite propagation makes the compressed and full reflected
pairings identical on the cut vector. Restoring its endpoint costs
\(C\sqrt b/d\). The true-weight comparison is applied only to the
original full packet and costs \(C\tau_X/d\), linearly. The sharp cut
does not enter a source-equation test. Every prime-power label remains
inside the complete reflected operator.

The exact actual-source identity makes \(\Delta M_C\) self-adjoint;
it does not make \(M_C\) commute with \(\Delta\). The displayed positive
Sylvester inverse correctly turns the Hermitian bound (13) into (15).
Both inverse-depth costs cancel against the dyadic spectral-depth
bound. The original factor two and the source-map norm bound are
accounted for, with no rank or separation cost.

The inherited full prime/Gamma comparison yields the Fourier tail in
(4). Its two powers exceed \(2s\) when \(4s<\beta<1/2\), giving every
\(s<1/8\). The weighted-cell, zero-sampling and common-core arguments
remain valid in that range; their full-band squared-norm loss is still
only the number \(O(J)\) of dyadic depth bands.

For any \(p>4\), choose \(1/(2p)<t<1/8\). The displayed bound involving
\(y^{1-2tp}\log y\) has finite supremum, proving that one sufficiently
large \(A_p\) in (17) pays the high-height tail for all displayed depths.
The thin-strip deletion uses strictly larger intermediate Sobolev
orders below \(1/8\). Equation (18) retains half of the full matrix
\(A-I\), every positive zero term, and true multiplicities.

No endpoint exponent, numerical constant \(A_p\), new zero-free height,
signed upper comparison, supercritical exclusion, or RH proof follows.
