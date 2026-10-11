## Round 87 — the curvature--homology manuscript confuses a jet's spectrum with the full distribution's spectrum

The latest candidate [*A Curvature-Homology Proof of the Riemann Hypothesis*](https://www.cambridge.org/engage/coe/article-details/6a43d3b14770e67d926bdd2f) (Jordan Farrell, Version 2, 3 July 2026; the associated PDF is an unrefereed working paper) advertises a local second-order projection of a hypothetical off-critical quartet. Its actual body proves only an operational statement about a separately defined prime-side functional
\[
P[g]=-2\sum_{n\ge 2}\Lambda(n)\sqrt n\,\widehat g(\log n).
\tag{87.1}
\]
The prime-side calculation gives an atomic probe-center spectrum. It does not, by itself, produce the lifted Weil identity whose other terms contain the zero distribution, nor does it identify the proposed projection of the full explicit formula with the quartet defect.

The internal cancellation error is explicit. Let
\[
J=c_2\partial_\gamma^2\delta_\gamma,\qquad c_2\ne0,
\]
and write \(S=P-J\). For the chosen probe family, put
\[
h_\gamma(\xi)
=\xi^2\bigl(e^{-i\gamma\xi}+e^{i\gamma\xi}\bigr)\widehat\psi_\ell(\xi),
\tag{87.2}
\]
up to the fixed Fourier-normalization constant. The manuscript's own computation gives
\[
\widehat R_P=A_{\mathrm{at}},
\qquad
\widehat R_J=c_2h_\gamma,
\]
where \(A_{\mathrm{at}}\) is purely atomic and \(h_\gamma\,d\xi\) is a nonzero absolutely continuous measure. Therefore linearity gives the exact identity
\[
\widehat R_S=A_{\mathrm{at}}-c_2h_\gamma\,d\xi.
\tag{87.3}
\]
Consequently
\[
\widehat R_P=\widehat R_J+\widehat R_S
\]
is purely atomic because the two absolutely continuous terms cancel exactly. This is not an absorption of an absolutely continuous measure into an atomic measure; it is cancellation between the jet and the remainder.

The paper's Proposition 12.2 merely says that exclusion would follow if no remainder with the opposite operational component existed. No theorem proves that premise. Proposition 13.1 correctly observes that \(S\) is then not purely atomic, but that observation is irrelevant: \(S\) was never proved to be prime-type. Theorem 15.3 excludes what the paper defines as an “operationally visible” singularity of a prime-type distribution; it does not show that a local jet in a general decomposition of \(P\) remains visible after the remainder is included. Theorem 9.3 also states only the contribution of the jet term, and Remark 9.4 explicitly acknowledges that other terms may cancel it. Theorem 16.1 nevertheless invokes the forward theorem as though it applied to the complete response without cancellation.

A one-line abstract countermodel captures the logical failure. In the vector space of finite complex measures on the probe-frequency axis, take any nonzero absolutely continuous measure \(H\) and any atomic measure \(A\). Set \(P=A\), \(J=H\), and \(S=A-H\). Then \(P=J+S\) and \(P\) is purely atomic, while \(J\) has a nonzero absolutely continuous spectrum. Lebesgue decomposition validates (87.3); it does not contradict it.

Even after repairing this cancellation step, the manuscript would still need all of the following independent bridges:
1. an explicit-formula identity in one common distribution space;
2. a proof that the proposed local jet is the zero-sector component of that identity;
3. a direct-sum or microlocal separation theorem ruling out cancellation by every remaining sector; and
4. a proof that the resulting \(-\delta^2=0\) projection is defined and nonzero on the admissible test space.

The source supplies none of these bridges. Its conclusion is therefore not an unconditional zero-exclusion theorem.

**Established:** the prime-side operational spectrum is atomic; the paper's “jet contribution” formula is a valid linear calculation in isolation.

**Failure / missing step:** atomicity of the complete prime-side response does not exclude a local jet, because the remainder can carry the exact opposite absolutely continuous component. The candidate never connects its prime-side distribution to the full zero-side explicit formula with a valid no-cancellation theorem.

**Remaining load-bearing statement:** prove the full lifted identity and a genuine cancellation/separation theorem that survives arbitrary remainders; only then could a local curvature projection imply RH.

**RH status:** no unconditional proof has been produced.
