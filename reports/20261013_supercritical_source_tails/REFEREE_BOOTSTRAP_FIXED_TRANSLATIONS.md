# Review of the second bootstrap and fixed translation domains

Date: 2026-10-14.

Reviewed candidate:
[BOOTSTRAP_AND_FIXED_TRANSLATIONS.md](BOOTSTRAP_AND_FIXED_TRANSLATIONS.md).
Its SHA-256 is

    a2b184bcf90e7a68e05202bcab2694f1a5bb1b507726345d852605df79a0a67f

Published dependency snapshot:
3049083d27f751a1426d9dcf5174c789d6ea96fc.

**Disposition: pass for the stated fixed-depth scalar bootstrap,
every-small-translation domain and continuity, and finite-matrix claims.**
A fresh independent review found no blocking gap. Two separate
derivation checks also supported the commutator and auxiliary-operator
application. These are model-assisted mathematical reviews, not
proof-assistant verification or external human peer review.

## Mathematical checks

1. The commutator proof covers low coefficient/high input, high
   coefficient/low input, and comparable frequencies. In the last
   case the estimate is on the entire output ball, so interactions
   producing arbitrarily low output frequency are retained.
   The exponent condition is exactly
   \(s+\beta<r+t-1/2\), with \(s>0\), \(1/2<r<1\),
   \(0<t<1/2\), and \(\beta>0\).

2. The complete coefficient bounds follow from the existing
   \(W^{1,p}\) estimates with \(1<p<2\). They provide summable
   \(H^r\) norms for every \(r<1\), including zero extensions,
   reverse shifts and both odd-extension mirrors. The pole vector
   is \(H^1\). No half-line support term, prime-power label, or pole
   term is removed.

3. The published first bootstrap supplies both \(v\in H^t\) and
   \(B_og\in H^t\), the latter by taking a slightly larger source
   order below \(1/2\). These are exactly the two inputs to the
   new commutator. The established composition-form domain puts
   \(G_\varepsilon v\) in the actual auxiliary operator domain.
   The factor-two operator commutator has the same sign and
   normalization as in the first bootstrap.

4. The retained low-frequency term is bounded on the actual known
   \(H^t\) vector. No new uniform \(L^2\) operator estimate is
   assumed at the higher order. Coercivity, the bounded residual,
   and Fatou give \(v\in H^s\) for each \(s<1\).
   The one-dimensional Sobolev algebra above \(1/2\) then gives
   the same statement for \(g=\mu v\).

5. Hölder increments provide the weighted origin bound uniformly
   for every translation parameter. The translated theta and
   physical tails are uniform in a fixed slightly larger interval.
   The complete Gamma and prime estimates therefore make the even
   mollified translations uniformly Cauchy in the original
   \(P\)-completion. Every approximant is exactly pole-centered.
   Injectivity of the centered-source map identifies every limit.
   The same three-region argument proves continuity in the
   translation parameter and the stated norm bound.

6. If \(|a_i|\le A/2\), all sums and differences \(a_i\pm a_j\)
   lie in the legal interval. The complete source-pairing identity
   yields the finite covariance matrix for every such tuple.
   Its nonnegativity retains the largest-eigenvalue hypothesis.
   The neutral correction uses the same common projection as the
   cited theorem and keeps all mixed terms.

## Limits of the conclusion

Constants depend on the lower depth \(d>0\). There is no order-one
endpoint, mixed-eigenvalue packet estimate, or derivative trace assertion.
The result removes the exceptional parameter sets from the raw-translation
domain statement. It does not provide a negative compensated covariance,
exclude a supercritical eigenvalue, or prove RH.
