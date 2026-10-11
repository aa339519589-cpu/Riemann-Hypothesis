## Round 179 — the current completion-locked v3 preserves the M4 dependency cycle

I checked the current v3 record rather than relying only on the earlier v2
audit:

<https://zenodo.org/records/19487972>

The version-3 note says that the terminal closure stage was reorganized but
that the core proof strategy and main mathematical claims were unchanged.  The
new numbering therefore does not change the following dependency audit.

Theorem 8.69 (printed p. 92) has three hypotheses.  The first assumes the
EMCP primitives are already realized by primitive triangle words.  The second
assumes the cost/length bridge
\(R(\gamma)=\ell(g_\gamma)\).  The third assumes that, for every prime \(p\),
the prime tower is already represented by iterates of a designated
\(g_p^{(\delta)}\).  The calculation \(\ell(g_p^{(\delta)})=\log p\) is
therefore conditional arithmetic labeling, not a proof that the constructed
triangle dynamics has those prime generators.

There is an internal type mismatch at this exact point.  The manuscript's
earlier M4 setup explicitly distinguishes the EMCP roof sum
\(\ell_{r_{\rm EMCP}}\) from geometric translation length and says that prime
values are not being asserted as lengths in a fixed triangle group.  Theorem
8.69 then assumes the opposite equality with a geometric translation length.
Definition 8.67 only constructs \(g_n\) as an element of
\(\operatorname{PSL}_2(\mathbb R)\); it does not prove that \(g_p\) belongs to
the fixed side-pairing group or is represented by a primitive word of its
coding.  Condition (3) simply supplies that missing representation.

Theorem 8.75 (p. 95) proves \(D(s)=0\) only after assuming both Theorem 8.69
and Milestone Statement 8.74.  Statement 8.74 is the needed exhaustion theorem:
single-prime support for every equilibrium primitive and exactly one primitive
per prime.  The v3 Theorem 8.95 still assumes Theorem 8.69 and Theorem 8.91,
while Theorem 8.91 assumes the nondegenerate-minimizer statement 8.87.  The
resulting implication is

\[
 \text{prime generators + unique selector}
 \Longrightarrow
 \text{exhaustion/multiplicity one}
 \Longrightarrow
 D(s)=0,
\]

so naming the intermediate statements as theorems does not make their
premises independent.

The purported discharge in Theorem 8.110 (pp. 107--108) remains assertion
rather than proof.  A Hessian computation at the identity of an unspecified
compact group yields convexity only on a local neighborhood.  The manuscript
then declares the actual dyadic fundamental region to be an arbitrary closed
convex subset of that neighborhood, without proving that the primitive classes
lie there.  It also asserts that the prime-label constraints are convex
products of dyadic cylinder cells and that the feasible sets are closed and
compact, although no coordinate map, constraint equations, finite-dimensional
parameterization, or compactness theorem for the geometric primitive-history
classes is given.  The claimed Weierstrass and strict-convexity conclusions
therefore do not apply to the previously defined classes.

The support argument is conditional for the same reason.  Definitions
8.78--8.79 begin by saying “suppose” a partially defined composition exists and
state additivity only when a composition is already defined.  They do not prove
that a history with disconnected support factors into its support components.
Theorem 8.91 nevertheless invokes Lemma 8.82 and Proposition 8.83, whose proof
uses precisely that unproved converse.  Hence single-place support is imported
into the alleged exhaustion theorem.

**Established:** v3 supplies standard conditional facts about a chosen
transfer operator, a chosen positive operator, and analytic propagation after a
half-plane identity is already known.  Its current M4 section still does not
prove the prime-word realization, the cost/length bridge, support
factorization, selector compactness/uniqueness, or primitive exhaustion.

**Remaining load-bearing statement:** prove those M4 inputs independently for
the actual construction and then derive, rather than assume, the exact
logarithmic-derivative equality with \(-\zeta'/\zeta\).  Until that is done,
the positive determinant is not identified with the classical \(\xi\)-function.

**RH status:** no unconditional proof has been produced.
