## Round 180 — the Fredholm--scattering branch is retained, with its closure obligations made explicit

I audited the newest Fredholm--scattering proposal as a live route rather
than discarding it:

<https://zenodo.org/records/21889389>

The four-page manuscript proposes a cusp-truncated Laplacian on
\(M=\Gamma_0(163)\backslash\mathbb H\), a nonlocal Fredholm boundary anchor,
projection to an Eisenstein sector, Mosco convergence, and a scattering
determinant identification with \(\xi\).  The route would be sufficient if all
of those bridges were proved.  The source, however, currently states several
of them without the required definitions or estimates.

First, the asserted Fredholm coercivity does not follow from compactness.  The
boundary equation is written in the form

\[
 u-Ku=0,
 \tag{180.1}
\]

with \(K\) described as a compact positive-definite integral kernel.  On an
infinite-dimensional boundary \(L^2\)-space, a compact operator has \(0\) in
its spectrum and its nonzero eigenvalues can accumulate at \(0\).  Fredholm
theory gives discreteness of the nonzero spectrum; it does not give a
positive lower spectral gap for \(K\), nor a \(Y\)-uniform Poincare inequality
for the Dirichlet form.  If the intended assertion is instead that
\(I-K\) is invertible, that is a different statement and still does not imply

\[
 \int_{M_Y}|\nabla u|^2\,d\mu\ge C\|u\|^2_{L^2(M_Y)}
 \tag{180.2}
\]

uniformly in the cusp height.  The proof of Theorem 2.1 consists only of the
sentence that Euler--Maclaurin applied to a boundary counting function gives
a universal flux constant; no boundary operator, counting asymptotic, trace
estimate, or constant \(C\) is supplied.  In particular, the later use of the
specific threshold \(1/4\) is not obtained from the merely asserted \(C>0\).

Second, the claimed Eisenstein projection requires a precise Hilbert-space
model.  The manuscript writes
\(L^2(M)=H_{\rm cusp}\oplus H_{\rm Eis}\) and treats the latter as if it were
spanned by \(L^2\) Eisenstein eigenfunctions.  For a finite-volume
noncompact surface, the Eisenstein series are generalized spectral vectors;
the continuous part is represented by a direct-integral spectral transform,
not by an \(L^2\) basis of eigenfunctions.  An orthogonal projection onto the
continuous component can be defined through the spectral theorem, but the
source does not define its restriction to \(M_Y\), its boundary trace, or the
extension/restriction maps needed for
\(J_Y(P_Eu)\).  “No scattering resonances are discarded” is not a consequence
of cusp-form orthogonality and needs a separate completeness and resonance
theorem.

Third, the Mosco step changes both the domain and the boundary condition with
\(Y\).  The source cites general Mosco theory but gives neither a common
ambient Hilbert-space realization nor the liminf and recovery-sequence
arguments.  Even after form convergence, strong resolvent convergence alone
does not identify scattering poles with point eigenvalues.  Scattering poles
are resonances of a meromorphic continuation; a self-adjoint operator has a
real spectral measure.  A cusp truncation or pseudo-Laplacian can create
discrete eigenvalues, so one must prove that the limiting divisor is exactly
the desired resonance divisor, with no spurious modes and no lost modes.

Fourth, Theorem 5.1 contains a direct internal inconsistency.  It prints

\[
 C(s)=\Phi(s)\,\frac{\xi(2s)}{\xi(2s-1)L(s,\chi)},
 \tag{180.3}
\]

and then says that \(\xi(2s)\) is in the denominator and therefore a zeta
zero supplies a pole.  In the displayed formula \(\xi(2s)\) is in the
numerator, so a zero of \(\xi(2s)\) supplies a zero of this displayed factor
unless another factor cancels it.  The manuscript does not define
\(\Phi(s)\), \(L(s,\chi)\), or the cancellation mechanism, and it does not
derive (180.3) from the \(2\times2\) cusp scattering matrix of
\(\Gamma_0(163)\).  Thus the required zero/pole divisor correspondence is not
yet an identity that can be used in the spectral argument.

The route can be advanced constructively by replacing the asserted steps with
the following concrete lemmas: (i) define the cusp boundary operator and prove
a height-uniform form inequality with its exact constant; (ii) realize the
continuous spectral component in a fixed direct-integral Hilbert space and
define the truncated forms there; (iii) prove Mosco liminf and recovery
sequences; (iv) establish a determinant/resonance theorem for the resulting
self-adjoint realization; and (v) derive the exact scattering determinant,
including every cusp, gamma factor, Euler factor, and zero multiplicity, before
applying the map \(\lambda=1/4+\gamma^2\).  Those are repair targets inside
the same route, not reasons to remove the route from the search.

**Established:** the Fredholm--scattering proposal gives a coherent
conditional architecture, and its final implication is valid once the form
bound, Mosco limit, resonance/eigenvalue correspondence, and exact
\(\xi\)-determinant identity are independently established.  The current text
does not establish those bridges; it also contains the numerator/denominator
contradiction (180.3).

**Remaining load-bearing statement:** construct the actual \(Y\)-uniform
self-adjoint limit and prove that its complete spectral divisor is precisely
the nontrivial zero divisor of \(\xi\), with multiplicities.  Continue this
route together with the Weil, Thorin, and arithmetic-coding routes.

**RH status:** no unconditional proof has been produced.
