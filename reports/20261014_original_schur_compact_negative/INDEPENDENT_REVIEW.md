# Independent review: compact negative part of the original Schur operator

Reviewed proof: [REPORT.md](REPORT.md), SHA-256
`9d6b06f8f8a4ab9ad6bc89580268ccdeae4691376016941f52940c7cd85c187e`.
Its prerequisite [closed Schur realization](../20261014_original_seed_schur/CLOSED_OPERATOR.md)
is the reviewed published version
`451d09cc2f823ae9473b3b2a5299433115e6e45afa3f466bc20b9dcb90663337`.
The publication proof differs from the independently reviewed source only
by its public dependency link and corresponding exact published-file hash.

The proof passes an independent derivation of the topology, complete
quadratic coefficients, and spectral conclusion.

1. The retained closed-graph bound supplies a uniform original source L2
   and logarithmic Gamma bound. Frequency truncation makes this family
   compact on every finite source interval. The full future-map estimate
   in weighted L2 has the exact n^(-3/2) coefficient and its complete
   Gaussian ratio Q_R tends to zero. These two facts prove compactness
   into L2(exp(2x)dx), including the collar at the degenerate mass endpoint.
   No false mass-to-source endpoint bound is used.

2. If the seeds are mass-weakly zero, every compact source limit has zero
   tail by local boundedness of C_xi away from b. The COMPLETE weighted
   tail-to-head map is bounded; original harmonicity and A0>=10^(-10)
   therefore force its head to zero as well. This establishes the exact
   weak-zero consequence required for the spectral argument.

3. The forward and reflected absolute source pairings both have coefficient
   A=sum Lambda(n)n^(-3/2). For reflection, the factor 1/n is exactly
   exp(-x-y) on x+y=log n. The full source formula thus contributes 4A+2A,
   and the pole dual integral is exactly 1/12. The displayed complete
   negative bound 2|C0|+6A+2/3 is correct, with no separate unweighted
   backward row or missing pole term.

4. An infinite orthonormal spectral family below any fixed -epsilon would
   be bounded in the closed form norm, have a source subsequence tending
   to zero in the weighted space, and contradict the complete negative
   bound. The spectral interval is bounded because S is semibounded, so
   these vectors are legitimately in its operator domain. Hence every
   such spectral projection has finite rank and S_- is compact.

The scope is exact: negative eigenvalues may still exist, with finite
multiplicity and accumulation at zero. Total finite negative index, an
effective eigenvalue separation, and nonnegativity of S are NOT proved.
The result concerns the same original Schur operator, not an auxiliary
hidden-current generator, and introduces no original-P membership claim.
