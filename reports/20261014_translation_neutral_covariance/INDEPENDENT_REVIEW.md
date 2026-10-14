# Independent mathematical review

## Versions and scope

The reviewed files have these SHA-256 digests:

- `REPORT.md`: `1ca6995eaebb0a5c5db14c70190f6b808b7e464974fd1141d460c7cf9fac70ba`.
- `RAW_TRANSLATION_DOMAIN.md`: `8dbf590fe2207206b0abdd3edaa54bd4797d1458c2ebbef3bfcc98280c2f76db`.
- `NEUTRAL_LEAKAGE_COMPENSATION.md`: `cf71a349578bcd112810425bfc32420eb70de2abcb0c9404a8c6dd3d817268b3`.

The results concern an actual hypothetical largest-supercritical Green source, the original completed forms, and the known neutral theta directions. They establish additional legal variations and exact necessary matrix inequalities. They do not construct a negative compensated matrix, exclude that source, or prove the coefficient-one Green comparison.

## 1. Raw-translation domain

The singular-origin estimate is valid. Oddness gives

\[
T_af(x)=\tfrac12[f(a+x)-f(a-x)].
\]

Integrating first in the translation parameter bounds the squared origin norm by the full-line translation difference. The \(H^s\) estimate then leaves the finite integral \(\int_0^\epsilon x^{2s-1}\,dx\). No value of the source or its derivative at an individual point is required.

The actual source-tail estimate and the complete theta/row asymptotics pay all sufficiently small shifts in both normalized and physical source norms. The exponential margin is positive after the stated fixed restriction on the translation radius. These bounds may depend on the fixed supercritical depth; the proof does not incorrectly assert depth-uniform bounds for the complete translated norms.

The completion argument is substantive and correct. Smooth even mollifications preserve exact pole centering. They are Cauchy in the averaged normalized norm by the origin estimate, in the physical norm by local convergence and uniform tail control, and in the Gamma norm by the Fourier contraction property. The complete prime bound and \(P=N+h\) then give convergence in the Bochner space with values in the actual \(P\)-completion. The centered pole square controls a source norm whose coefficient has a positive global minimum, identifying the limiting vector with the raw translated source.

Thus legality is established for almost every sufficiently small translation parameter, not merely for a formal source distribution.

## 2. Product domains and covariance matrices

The identity

\[
T_aT_b=\tfrac12(T_{a+b}+T_{a-b})
\]

has the correct normalization. For each finite tuple, the finitely many nonconstant linear parameter maps pull exceptional null sets back to null sets. Identically zero differences are already legal. This proves the stated almost-everywhere tuple assertion without claiming that one arbitrary conull set is closed under sums and differences.

The warning concerning predetermined arithmetic spacings is essential: an almost-everywhere result does not establish legality at a prescribed countable collection of nodes. The notes correctly require smoothing or a separate pointwise-domain proof there.

On the legal tuples, the Gamma and complete prime pairings commute with the real even translations. Absolute convergence follows from the retained physical source norms and complete weighted prime estimate. The centered pole term vanishes. Combining this commutation with actual top-state stationarity gives exactly

\[
Q_\delta(T_{a_i}g,T_{a_j}g)=\delta B_{ij}.
\]

The positive-semidefinite matrix conclusion uses the largest supercritical eigenvalue, not an arbitrary supercritical eigen-source.

## 3. Full reflected boundary and constants

Direct computation with odd extensions confirms the two commutator corners:

\[
[R_d,T_a]g(x)=\tfrac12[g(d+a-x)+g(d-a+x)]
\quad(0<x<a),
\]

and

\[
[R_d,T_a]g(d+t)=-\tfrac12g(a-|t|)
\quad(|t|<a).
\]

They give the displayed line-boundary formula with coefficient \(1/2\), not an extra factor from counting the two corners. The complete local prime load converges in the inherited fractional Sobolev norm and hence in local \(L^2\). Weighted absolute convergence of the global reflected pairings identifies the same limit without omitting prime powers.

The doubled-interval estimates are also correctly normalized:

\[
\|T_ag\|_{L^2(0,a)}\le2^{-1/2}\|g\|_{L^2(0,2a)},
\]

with the analogous estimate for the even complete load. Together with the actual fractional-origin bounds they prove \(\delta|D_{\rm pr}(a)|\le C_s a^{1+2s}P_0\). This removes smooth-profile concentration constants, but supplies an absolute boundary estimate, not its sign. Singular potential pairings must remain grouped as in the proof.

## 4. Common neutral projection and leakage

For the closed known-neutral span \(S\), the identity \(h(s,u)=0\) implies \(P(s,u)=N(s,u)\). Consequently its \(P\)-orthogonal projection is also the \(N\)-orthogonal projection after the isometric reflected-gradient identification. This is one common projection, not two unrelated minimizations.

All mixed terms vanish in the stated splitting of \(Q_\delta\). Finite Gram projection therefore gives the exact correction \(L^TM^{-1}L\); for a dependent family the Moore--Penrose inverse is legitimate because the leakage columns belong to the Gram range. Increasing finite spans converge to the full closed-span projection cost. None of this requires the known theta span to exhaust the full nullspace.

The additional commutator interpretation is proved on its correct domain. A fixed theta jet retains legal theta tails and its odd origin zero under each sufficiently small smooth or raw even convolution. Testing against compact ratio-core sources gives \(h(Cs,z)=h(s,Cz)=0\); continuity in the actual \(P\) norm extends this identity to the completion. Thus \(Cs\) belongs to the full neutral space, without an unsupported assertion that it lies in the known jet span. The proof does not assume convolution is bounded on every completed neutral vector.

Actual stationarity now gives \(N(g,Cs)=0\), making each leakage entry an exact complete commutator. The raw leakage line has coefficient one, because the factor two in the \(N\)-commutator multiplies the raw translation's factor \(1/2\). The stated \(a^{3/2+\sigma}\) bound follows from the fixed jet's smooth load and linear origin vanishing, together with the actual fractional estimates. It bounds only the boundary piece; the bulk contribution remains part of every entry.

## Conclusion

The raw-domain extension, complete reflected formulas, and common-neutral compensation are supported by the displayed proofs and the stated original-source inputs. They provide exact tests on the known-neutral complement while retaining all mixed terms and all arithmetic labels. A violation of the compensated inequality for an actual source remains unproved.
