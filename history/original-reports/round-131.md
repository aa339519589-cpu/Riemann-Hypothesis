## Round 131 — Makraini Paper 4 imports the coercive hypotheses and has a non-uniform density passage

I audited Makraini, *Convergence, Density, and Final Weil Positivity —
Paper 4* ([Zenodo record](https://zenodo.org/records/19357525)), including
Theorem 1.1, the finite-scale axioms in Definition 5.5, and the density
argument in Theorem 5.13.

Theorem 1.1 is explicitly conditional on four master hypotheses.  In the
paper's notation, H1 is uniform modal-commutator coercivity on the kernels
\(K_\Lambda\), H2 is a restricted bridge inequality with a vanishing
residual, H3 is modal concentration/commutator regularity on a dense regular
subclass \(W_0\), and H4 is density and limit stability.  Table 1 labels H1,
H2, and H3 as supplied by Papers 1–3, but Paper 4 does not derive those
properties from the zeta function, the prime coefficients, or the completed
explicit formula.  Its later discussion says the same thing more plainly:
H1 still depends on structural assumptions such as Hmix, Hexp, and Hnc; H2
depends on a positive bridge constant and Schur decay; H3 depends on Schur
admissibility; only H4 is claimed as the unconditional density result.

The finite-scale axioms make the logical boundary visible.  Q4 (finite-scale
positivity on \(W_0\)) is verified by referring back to Papers 1–3, Q3
(convergence to the Weil form) is attributed to consistency of the
finite-scale framework, and Q5 is only a uniform boundedness assertion.  A
conditional density extension from these inputs would be useful, but it is
not a proof of the inputs themselves.

There is an additional quantifier gap in Theorem 5.13.  Its three-term
estimate has the form
\[
 |Q_\Lambda(g)-W(g)|
 \le |Q_\Lambda(g)-Q_\Lambda(g_n)|
   +|Q_\Lambda(g_n)-W(g_n)|
   +|W(g_n)-W(g)|.
\]
The last term can be made small by density, and the middle term can be made
small for a fixed \(n\) after taking \(\Lambda\) large.  But the first term
is controlled in the cited lemma only by continuity for each fixed
\(\Lambda\) (with uniformity on finite cutoff ranges).  To conclude a limit
uniformly over the unbounded tail, the argument needs an estimate such as
\[
 \lim_{n\to\infty}\sup_{\Lambda\ge\Lambda_0}
 |Q_\Lambda(g)-Q_\Lambda(g_n)|=0,
\]
or an equivalent equicontinuity bound on bounded subsets.  Q5, as stated,
is uniform boundedness and does not imply this equicontinuity.  Choosing
\(n\), then choosing a cutoff threshold depending on \(n\), and finally
using fixed-\(\Lambda\) continuity gives a continuity threshold that may
depend on \(\Lambda\); it does not produce one threshold valid for every
larger \(\Lambda\).  Thus the displayed argument does not establish Q3 on
the full class from the listed axioms.

Even if this uniformity gap were repaired, the result would only transfer
positivity already assumed in H1–H3/Q4 to a larger test-function class.  It
would not supply the missing arithmetic coercivity or exclude off-line
zeros.

**Established:** Paper 4 contains a recognizable conditional density and
continuity strategy, and H4 is separated from the imported structural
hypotheses.

**Failure / missing lemmas:** H1–H3 are not proved unconditionally in Paper
4; moreover, fixed-cutoff continuity plus Q5 does not justify the required
uniform-in-\(\Lambda\) density passage in Theorem 5.13.

**Remaining load-bearing statement:** prove H1–H3 directly from the
arithmetic data with bounds uniform as \(\Lambda\to\infty\), and prove the
uniform form convergence/equicontinuity needed to pass from \(W_0\) to the
complete Weil test-function space.

**RH status:** no unconditional proof has been produced.
