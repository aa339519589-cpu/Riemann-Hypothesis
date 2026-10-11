## Round 42 — the Section 10 limit is weighted-ℓ∞, not weighted-ℓ²

I rechecked the actual compactness step in Bombieri's Section 10 against the
stronger weighted-range model used in Rounds 23--27. The source normalizes the
finite eigenvectors by

\[
 \sum_{\gamma\in\Gamma_N}|w_{\gamma;N}|^2=1,
 \qquad
 w_{\gamma;N}=\left(\tfrac14+\gamma^2\right)z_{\gamma;N}.
\tag{42.1}
\]

It then takes a diagonal subsequence in the individual coordinates and obtains
only

\[
 |w_\gamma|\leq 1
 \quad\text{for every fixed }\gamma,
 \qquad
 z_\gamma=\frac{w_\gamma}{\tfrac14+\gamma^2}.
\tag{42.2}
\]

There is no assertion that the limiting sequence satisfies

\[
 \sum_{\gamma\in\Gamma}|w_\gamma|^2=1
 \quad\text{or even}\quad
 (w_\gamma)\in\ell^2(\Gamma).
\tag{42.3}
\]

This is not a technical distinction. Coordinatewise convergence does not
preserve Hilbert mass: the normalized sequence (w^{(N)}=e_N) converges to
zero in every fixed coordinate while \(\|w^{(N)}\|_2=1\). For the Section 10
coefficients, the analogous escape is compatible with
\(z_{\gamma;N}=w_{\gamma;N}/(\tfrac14+\gamma^2)\) becoming uniformly small on
compact real intervals. The finite normalization therefore cannot be used to
deduce that the limiting function \(F\) is nonzero.

The source does obtain an \(H^1(-t,t)\) bound for the functions \(F_N\) from
(10.4); that supplies a weak derivative of the function limit. It does not
give (42.3), nor does it give the weighted coefficient tightness

\[
 \lim_{K\to\infty}\sup_N
 \sum_{|\gamma|>K}|w_{\gamma;N}|^2=0.
\tag{42.4}
\]

Without (42.4), the exact Section 10 limit belongs naturally to the class

\[
 \sup_{\gamma\in\Gamma}
 \left|\left(\tfrac14+\gamma^2\right)z_\gamma\right|<\infty,
\tag{42.5}
\]

not to the \(\ell^2\)-weighted range used by the ideal synthesis operator in
Rounds 24--27. The distinction also matters for regularity: (42.5) gives
\(\sum|z_\gamma|<\infty\) from zero counting, so \(Z\) is uniformly convergent
on compact real intervals, but termwise differentiation would require control
of \(\sum|\gamma z_\gamma|\), which does not follow from (42.5). The source's
derivative statement must therefore be read through the finite-\(N\) \(H^1\)
bound/weak-limit argument, not as a consequence of an \(\ell^2\) coefficient
limit.

**Established:** Rounds 24--27 prove valid statements for a stricter auxiliary
weighted-\(\ell^2\) operator, but those statements are not the source-faithful
limit theorem for Section 10.

**Remaining load-bearing statement:** prove weighted tightness such as (42.4),
or independently rule out a nonzero finite-section negative branch whose
weighted mass escapes to infinity. Either result must use the actual eigenvalue
equations; finite normalization, coordinate extraction, and the local \(H^1\)
bound alone do not supply it.

**RH status:** no unconditional proof has been produced.
