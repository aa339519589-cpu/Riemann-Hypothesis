# Independent internal review

16 October 2026. All three written proofs were read, their arithmetic inputs and limiting arguments checked, and the primary Rudnick--Sarnak coefficient rechecked directly. This is an internal mathematical review, not external peer review or a novelty certification.

## Reviewed final bytes

- `REPORT.md`: `cda8a5cac3fe32732a844f5d5c567a27dfa67fa140f9f8de14031fd312288ad1`.
- `DYADIC_ABSOLUTE_CUBIC_TAIL.md`: `1658ac9f7d50af80003d62664e0bb7b6dcf6f85d4fbc8b6a095d0dbc33d9bfd0`.
- `UNIFORM_PREFIX_CUBIC_MAJORANT.md`: `23b63a59ae01bfee500cb9acfb7af9562c3197850b236121118692821935635b`.

The final changes from the checked research texts are relative links, a clickable primary citation, and generic wording of the separate conditional wide-window comparison. No mathematical premise or estimate changed.

## Arithmetic and absolute-cycle checks

The fixed-order Tsang increment input and uniform near-line density bound have distinct roles and are both retained. The preceding-bin injection and dyadic real-height summation use a fixed moment order, the same normalization L=log T at every height, and an explicit fixed-low-height contribution. The constants in the density input are uniform in sigma; reflection and a left limit pay the counting convention and both sides of the strip.

The discrete cubic kernel w(m)w(n)w(m-n), w(m)=(1+|m|)^(-1), is summable. Jensen followed by shifted Holder gives exactly the anchored factor (sum d)^(1-1/p)(sum c^(2p+1))^(1/p). Applying the maximal-imaginary-band restriction before enlarging the other label counts is lawful. A three-cycle's imaginary growth is controlled by twice the range, yielding the required 4 pi lambda band exponent, not a product of three independent worst endpoint bounds.

For U>=T^kappa, the resulting prefactor is

    U L R^(1-1/p)(1+R)^(2+1/p) <= U L(1+R)^3,

where R=log U/L. The chosen fixed gap theta(1-1/p) kappa-lambda>0 pays all imaginary bands uniformly. This proves the stated same-logT prefix majorant and the small-label deletion estimate, without assuming a fourth moment or an absolute spectral-third bound.

## Complete sharp transfer

The finite operator is Hermitian by the actual conjugate-reflection zero pairing, with multiplicities. Its finite-rank cubic trace is the literal unrestricted cycle sum. The smooth height family is nonnegative and bounded on the real line, entire with smooth compact Fourier preimage, and lawful for the primary theorem.

The sharp approximation treats a fixed real-height prefix, boundary labels and the entire complementary tail separately. Boundary intervals contain O(epsilon T log T)+O(log T) labels; fixed-imaginary-strip Holder followed by the uniform imaginary tail makes their normalized contribution small. Away from those intervals the height-factor error is uniform. On every outside max-height shell, at least one smoothed factor has the stated eta^(M-1) Schwartz decay; the prefix majorant grows only linearly in shell height times a cubic logarithmic factor, so the complete shell sum is paid.

The order of limits is explicit: T tends to infinity first, then the smoothing scale tends to zero at fixed boundary width, and finally that width tends to zero. The analytic-height/real-height difference is O_eta(log T), using the full absolute weighted prefix majorant on both ordinate signs. No sharp signed limit is inferred merely from pointwise smoothing.

## Primary coefficient

Rudnick--Sarnak Theorem 3.1, equations (3.2)--(3.9), printed pages 19--20, sums unrestricted indices with multiplicity. For the cycle pushforward the zero-sum-plane map has unit Jacobian and support sum |xi_j|=2(max u_j-min u_j)<2. Its value at zero is integral f^3. Each of the three disjoint-pair lines contributes double-integral |s-t| f(s)^2 f(t). Thus the stated D(f), with coefficient 3 and no additional coincidence correction, is the direct primary coefficient. The RH-only sharp Theorem 3.2 is not used.

## Conclusion and limits

The stated unconditional sharp signed cubic trace formula is supported for every fixed smooth even probability window of width lambda<4/7. The proof does not establish a near-unit-window fourth moment, spectral absolute-third uniform integrability, a new critical-line proportion, or novelty over all literature. The narrower support restriction and all fixed-parameter dependence remain essential. No mathematical correction is requested.
