## Round 138 — Bombieri's λ_N→0 branch is an explicit linear-dependence obstruction

I rechecked the original Bombieri paper, Sections 10–11, against the finite-to-infinite
passage rather than treating the resulting trichotomy as an RH proof
([official record and PDF](https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0)).

For a finite set of off-line zero pairs, Bombieri truncates the full symmetric zero
multiset to Γ_N, chooses a negative eigenvalue λ_N<0, and normalizes the eigenvector
by ∑|w_{γ,N}|^2=1.  His equations (10.2)–(10.5) give a subsequence with

\[
  z_{\gamma,N}=\frac{w_{\gamma,N}}{1/4+\gamma^2}\longrightarrow z_\gamma,
  \qquad \lambda=\liminf_N\lambda_N\le 0,
\]

and a locally square-integrable limit

\[
  F(u)=\sum_{\gamma\in\Gamma}z_\gamma e^{-i\gamma u}
       -Ae^{u/2}-Be^{-u/2}.
\]

The normalization estimates retain at least half of the limiting ℓ2 mass on the
off-line frequencies.  If F is not zero on the chosen interval, the limiting
eigen-equation gives a genuinely negative Weil value; Bombieri then invokes his
short-support positivity theorem to rule out this strict-negative branch.

The surviving branch is not a sign conclusion.  Section 11 proves, via (11.2)–(11.6),
that

\[
  \lambda=0 \quad\Longleftrightarrow\quad F|_E=0,
\]

so the limit is a nonzero interval relation

\[
  \sum_{\gamma\in\Gamma}z_\gamma e^{-i\gamma u}=0
  \quad (u\in E),
  \qquad \sum|z_\gamma|^2=1,
  \qquad \sum_{\gamma\notin\mathbb R}|z_\gamma|^2\ge\tfrac12.
\]

Bombieri's own text then records that relations on intervals of arbitrary length can
arise from shrinking gaps between consecutive critical-line ordinates, and that the
finite-eigenvector calculations only suggest (numerically) rapid convergence.  No
theorem there excludes this branch or proves a uniform lower bound for
\(|\lambda_N|\).  Consequently, Theorem 11 and its corollary are a conditional
trichotomy: RH, infinitely many off-line zeros, or a weighted interval dependence;
they are not an unconditional elimination of off-line zeros.

### A strict model check on the missing uniqueness implication

The coefficient bounds used in the compactness passage cannot by themselves imply
interval independence.  Let I be a proper interval on the circle and choose a
nonzero smooth 2π-periodic function G that vanishes on I.  Its Fourier coefficients
a_n in

\[
  G(u)=\sum_{n\in\mathbb Z}a_n e^{-inu}
\]

decay faster than every power.  Put

\[
  z_n=a_n,\qquad w_n=(1/4+n^2)a_n.
\]

Then w\inℓ2, z_n=w_n/(1/4+n^2), and the absolutely convergent exponential series
\(\sum z_ne^{-inu}\) is nonzero globally but vanishes identically on I.  Thus even
much stronger polynomial decay than Bombieri's subsequential estimate does not
give a generic identity theorem for interval relations.  This is not a counterexample
at the zeta frequencies; it isolates the exact missing input: a special uniqueness
theorem for the actual zero set, with the required weighted mass control.

**Established:** the finite truncation argument has a precise surviving null-cone
branch.  It yields a weighted interval dependence when \(\lambda_N\to0\), not a
contradiction.

**Failure:** no unconditional result currently supplied in this route excludes the
actual zeta-frequency relation, prevents critical-line mass from absorbing the
off-line finite-dimensional direction, or handles the separate case of infinitely
many off-line zeros.

**Remaining load-bearing statements:** prove a zeta-specific weighted exponential
uniqueness theorem or a uniform finite-section spectral gap; independently close the
infinite-off-line branch; then re-audit the full Weil positivity implication.

**RH status:** no unconditional proof has been produced.
