## Round 178 — the completion-locked Hilbert–Pólya manuscript assumes the prime-spectrum bridge it later declares proved

I audited the 123-page v2 manuscript *A Completion-Locked Hilbert–Pólya Proof
of the Riemann Hypothesis*:

<https://zenodo.org/records/19216994>

Its Hilbert-space implication is standard in form: a positive self-adjoint
operator would constrain the zeros of its own determinant.  The unresolved
issue is identifying that determinant with the classical \(\xi\)-function.
The manuscript's M4 chain does not establish that identification
independently.

First, Theorem 8.69 (printed p. 92) assumes all of the arithmetic bridge it
needs:

1. every EMCP primitive history is realized by the triangle coding;
2. its EMCP cost equals the geometric translation length,
   \(R(\gamma)=\ell(g_\gamma)\);
3. for each prime \(p\), the prime tower is already represented by iterates
   of a designated dilation element \(g_p^{(\delta)}\).

The elementary calculation \(\ell(D_p)=\log p\) then proves only the
conditional inclusion of the already-designated prime towers.  The theorem
itself says that M4 is still reduced to proving that no additional primitive
lengths occur.  Thus the calculation is not a derivation of the prime
realization from the triangle; it assumes the realization and computes its
length.

Second, Theorem 8.75 (printed p. 95) proves defect vanishing only under
Theorem 8.69 and Milestone Statement 8.74.  Statement 8.74 is precisely the
exhaustion and multiplicity-one assertion: every surviving primitive has
single-prime support and there is exactly one primitive for each prime.
Theorem 8.94 is then stated to prove that same assertion, but its proof uses
Theorem 8.91, which in turn assumes Theorem 8.69 and the nondegenerate-minimizer
hypothesis 8.87.  The logical chain is therefore

\[
 \text{prime realization and unique selector}
 \Longrightarrow \text{no extra primitives}
 \Longrightarrow D(s)=0,
\]

not an unconditional derivation of the first two statements.

The attempted discharge of the selector hypothesis in Theorem 8.108 does not
close this loop.  Its item (1) computes a Hessian at the identity of an
unspecified compact symmetry group and obtains convexity only on a local
neighborhood \(U_{t_0}\).  It then simply chooses the “dyadic fundamental
region” to be any closed convex subset of that neighborhood; it never proves
that the actual primitive class \(\mathcal P(p)\) lies there.  Its item (3)
asserts, without defining the coordinate map or the constraint equations, that
the prime classes are products of convex dyadic cylinder cells.  Its item (4)
similarly asserts that the feasible classes are closed subsets of finite
products of compact cells, although the preceding definitions do not establish
finite-dimensionality, closedness, or compactness of the set of geometric
primitive histories.  These are the exact properties needed for existence and
uniqueness, not consequences of the local Hessian calculation.

There is an earlier unsupported factorization as well.  Definitions 8.78--8.79
say “suppose” a partially defined history composition exists and give
additivity only whenever a composition is already defined.  They do not prove
that every history with disconnected support factors into its support
components.  Lemma 8.82 and Proposition 8.83 use that unproved converse to
deduce single-place support.  The later statement that the support pieces
factorize “by the factorization axioms” therefore imports the missing locality
axiom rather than deriving it.

Finally, the transfer-operator theorem supplies a periodic-orbit expansion for
whatever roof function and coding have been constructed.  It does not identify
that expansion with the von Mangoldt tower.  The manuscript defines
\(r_{\rm EMCP}\) from the desired EMCP costs, assumes the coding and cost
compatibility in EC1--EC3, and then uses the assumed prime generators to remove
all other primitives.  Analytic continuation in Theorem 8.117 is valid only
after this half-plane identity has been proved; it cannot create the missing
identity.

**Established:** the manuscript contains valid conditional implications:
positive self-adjointness would confine zeros of the constructed determinant,
and an already-proved prime/trace equality would propagate analytically.  It
does not independently prove the prime realization, exhaustion, multiplicity
one, or the half-plane equality.

**Remaining load-bearing statement:** give an explicit, independently defined
EMCP/triangle construction and prove its global primitive coding, cost
identification, support factorization, selector compactness/uniqueness, and
absence of extra primitive towers.  Without those results M4 is an assumption
package, so the determinant has not been identified with \(\xi\).

**RH status:** no unconditional proof has been produced.
