## Round 18 — finite-section residual convergence still does not select the Bombieri representative

Round 17 used an exact limiting kernel vector. The same obstruction persists at
the level of finite-section approximations: local residual convergence and the
half-mass inequality do not identify the finite-truncation eigenvector branch.

### I. Correctness decision

**成立 (as a conditional no-go theorem for residual-only finite-section data).**

Retain the notation of Round 17. Let \(B\subset\Gamma_C\) be a Riesz-basis
subsequence, let \(S_B:\ell^2(B)\to L^2(I)\) be its bounded invertible synthesis,
and let \(k\in\ker S_C\) be the nonzero kernel vector constructed there. For any
finite exceptional vector \(e\ne0\), choose \(c^{(0)}\in\ell^2(B)\) so that

\[
 S_Bc^{(0)}=-S_Ee.
\]

Let \(P_N\) be truncation to an increasing finite subset of \(B\) together with
the coordinate \(\eta\) used in \(k\). Then

\[
 P_Nc^{(0)}\to c^{(0)},\qquad P_Nk\to k
 \quad\text{in }\ell^2,
\]

and boundedness of \(S_B\) gives

\[
 \bigl\|S_C(P_Nc^{(0)}+\alpha P_Nk)+S_Ee\bigr\|_{L^2(I)}
 \leq \|S_B(P_Nc^{(0)}-c^{(0)})\|_2
 +|\alpha|\|S_B(P_Nk-k)\|_2
 \longrightarrow0
\]

for every fixed \(\alpha\in\mathbb C\). Define

\[
 w_N=(P_Nc^{(0)}+\alpha P_Nk,e).
\]

For each fixed \(\alpha\), \(w_N\to(c^{(0)}+\alpha k,e)\) in coefficient norm.
Choose \(\alpha\) as in Round 17 so that

\[
 \|c^{(0)}+\alpha k\|_2\geq\|e\|_2.
\]

Then, for all sufficiently large \(N\), the normalized vectors
\(w_N/\|w_N\|_2\) have a nonzero exceptional component and critical mass at
least \(1/2-o(1)\), while their local synthesis residual tends to zero.

Thus the data

\[
 \text{finite support},\quad \text{normalized coefficients},\quad
 \text{local residual}\to0,\quad \text{critical mass}\geq\tfrac12-o(1)
\]

admit sequences converging to different representatives of the same limiting
local null state. The residual condition does not remove the critical-kernel
gauge.

### II. Hostile audit and exact repair condition

This argument does not assert that the displayed \(w_N\) are eigenvectors of
Bombieri's exact finite matrix. It proves the narrower and necessary statement
that finite support plus residual convergence cannot establish that fact. The
actual finite matrix must contribute an additional representative-selection
theorem, such as a resolvent estimate, an asymptotic minimization property, or a
source-specific identity that is not invariant under \(c\mapsto c+\alpha k\).

In particular, the following implication is not justified by the local
synthesis argument alone:

\[
 \lambda_N\to0\ \text{and}\ 
 \|H_Nw_N\|\to0
 \quad\Longrightarrow\quad
 w_N\ \text{is the Bombieri-selected limiting state}.
\]

The displayed construction directly supplies the analogous obstruction for
local synthesis residuals. To use an \(H_N\)-residual instead, one must first
prove a source-specific estimate linking \(\|H_Nw_N\|\) to the representative
class; that estimate is exactly part of the missing finite-\(N\) theorem.

The finite-\(N\) eigenvector route remains live only through the exact equations
of the arithmetic matrices, not through abstract compactness or residual limits.

### III. Next-route decision

**Route X:** derive a source-specific Schur-complement or resolvent formula for
Bombieri's actual \(H_N\), and prove that its selected negative branch has a
representative-independent invariant that survives \(N\to\infty\).

**Route Y:** abandon local representative selection and construct a nontracial
source-evaluable arithmetic observer. It remains the competitive bypass.

### IV. Ledger update

**Established:** even finite-section local residual convergence with the Bombieri
half-mass lower bound does not select a unique critical coefficient
representative; the critical synthesis kernel survives truncation in the form of
arbitrarily chosen approximate-null sequences.

**Failure / error:** replacing the exact finite-\(N\) eigenvector provenance by
generic residual convergence is insufficient.

**Still assumed / unknown:** whether the exact arithmetic finite matrices impose
the missing representative-selection invariant.

**Next route:** compute and prove the actual finite-\(N\) Schur-complement/rate
identity; keep the nontracial source route as the competitor.

**RH status:** no unconditional proof has been produced.

## Ledger erratum — chronological placement of Round 19

The Round 19 block was inserted before the Round 18 block by an editing-anchor
error. Its mathematics and status are unchanged. For chronological reading,
the canonical order is Round 17, then Round 18, then Round 19; this erratum is
appended without altering either earlier block.
