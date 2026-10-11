## Round 235 — A/B result: the Heegner/Lax--Phillips manuscript does not construct the required symmetrizing operator

**Source inspected:** M. I. Aksman, *The Heegner Spectral
Compactification Program: A Spectral Framework Toward the Riemann Hypothesis
via the DSM-861 Manifold*, Zenodo record
<https://zenodo.org/records/21138428>, PDF pp. 1–8.

The arithmetic factorization
\(\zeta_K(s)=\zeta(s)L(s,\chi_{-163})\) is a standard fact, but the next
identification is not established. The manuscript asserts that the zeros of
\(\zeta_K\) are precisely second-sheet scattering poles for
\(\Gamma_0(163)\), and writes a one-factor scattering matrix
\(\Phi(s)=\Lambda(2s-1)/\Lambda(2s)\). It gives no derivation of this
identification for the multi-cusp group \(\Gamma_0(163)\), nor a theorem
showing that the relevant pole set is exactly the zeros of the classical
\(\zeta\)-function rather than a larger collection of scattering factors.
The “Perturbation Dilemma” is also not a proved universal dichotomy: a
perturbation can move some poles while leaving others unchanged.

The proposed load-bearing object is the metric
\(G=I+M_{861}\) on the infinite-dimensional interacting subspace. The
formula
\[
\langle f,g\rangle_G
=\langle f,g\rangle_{L^2}
+\sum_{j,k=1}^{861}W_{jk}f(\tau_j)g(\tau_k)
\]
is not an \(L^2\)-bounded form as written, because point evaluation is not a
bounded functional on \(L^2\). A Sobolev domain, a bounded extension, and
compatibility with the domain of the unbounded generator are required and
are not supplied.

The claimed intertwining equation
\[
B^*G=GB
\]
is never derived from the displayed Green-function expression for
\(W_{jk}\). The paper simply asserts that the 861-node kernel reproduces the
entire continuous cusp flux. The class-number-one property and a positive
pairwise separation do not imply this operator identity or any exact
finite-rank representation of an infinite-dimensional boundary flux.

Lemma 2's positivity proof is likewise incomplete. It invokes an
“explicit margin” \(\varepsilon>0\) and a bound
\(\|W\|_\infty<1-\varepsilon\), but does not calculate the matrix entries,
prove the bound, or establish the sign assumptions needed for the
Gershgorin conclusion. The geometric maximality of the discriminant does
not entail a norm estimate for a Green-function matrix. Extending a bound
from a finite nodal subspace to all of \(K\) also presupposes that
\(M_{861}\) is a well-defined bounded operator with exactly that range.

Finally, the claim that the resonances are precisely the spectral data of
the contractive Lax--Phillips generator is used before a valid generator
domain and resonance-spectrum theorem are provided. Changing to a positive
metric cannot by itself alter a non-real eigenvalue into a real one; the
unproved identity \(B^*G=GB\) is exactly the condition that would have to
exclude such eigenvalues. Since neither this condition nor the exact
zeta--resonance correspondence is established, self-adjointness and the
critical-line conclusion do not follow.

Therefore the manuscript supplies a spectral proposal and several standard
background facts, but no complete unconditional operator construction or
zero-location theorem.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
