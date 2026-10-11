## Round 17 — the unweighted Bombieri mass cone can be inflated inside the critical kernel

This entry isolates a stronger obstruction to the quantitative coefficient-range
route. It is a theorem about the limiting local synthesis equation; it does not
claim that Bombieri's selected finite-truncation eigenvectors may be replaced by
arbitrary kernel representatives.

### I. Correctness decision

**成立 (as a conditional no-go theorem for the unweighted limiting category).**

Assume the finite-exception hypothesis and fix a finite interval \(I=(0,L)\).
Let \(\Gamma_C\) be the distinct critical ordinates and let

\[
 S_C c=\sum_{\gamma\in\Gamma_C}c_\gamma e^{-i\gamma u}
\]

denote local synthesis on the coefficient sequences for which the sum is
defined. The already established gap/Kadec argument supplies a subset
\(B\subset\Gamma_C\) whose exponentials form a Riesz basis of \(L^2(I)\).
Consequently its synthesis map

\[
 S_B:\ell^2(B)\longrightarrow L^2(I)
\]

is a bounded bijection with bounded inverse.

Take any \(\eta\in\Gamma_C\setminus B\). Since \(e^{-i\eta u}\in L^2(I)\),
there is a unique \(b\in\ell^2(B)\) with

\[
 e^{-i\eta u}=S_B b.
\]

The sequence \(k\in\ell^2(\Gamma_C)\) defined by

\[
 k_\eta=1,\qquad k_\gamma=-b_\gamma\ (\gamma\in B),qquad
 k_\gamma=0\ (\gamma\notin B\cup\{\eta\})
\]

is nonzero and satisfies

\[
 S_Ck=0.
\]

Thus the unweighted critical synthesis has a nontrivial kernel. If
\(h\in L^2(I)\) has one critical representation \(c^{(0)}\), then for every
\(\alpha\in\mathbb C\),

\[
 S_C(c^{(0)}+\alpha k)=h,
\]

while \(\|c^{(0)}+\alpha k\|_2\to\infty\) as \(|\alpha|\to\infty\).
The last assertion follows from the reverse triangle inequality, since
\(k\ne0\).

Now let \(e\ne0\) be any finite exceptional coefficient vector and put

\[
 h=-S_Ee\in L^2(I).
\]

The Riesz basis gives a critical representation \(c^{(0)}\) of \(h\). Choose
\(\alpha\) so large that

\[
 \|c^{(0)}+\alpha k\|_2\geq\|e\|_2.
\]

Then the combined coefficient vector

\[
 w=(c^{(0)}+\alpha k,e)
\]

is a nonzero local null state,

\[
 S_C(c^{(0)}+\alpha k)+S_Ee=0,
\]

and its critical mass obeys

\[
 \frac{\|c^{(0)}+\alpha k\|_2^2}
 {\|c^{(0)}+\alpha k\|_2^2+\|e\|_2^2}\geq\frac12.
\]

After normalizing \(w\), this is exactly the type of half-mass inequality
appearing in Bombieri's limiting null-state statement. The exceptional component
remains nonzero throughout; only the representative in the critical kernel has
been changed.

### II. Premise audit

The only substantive premise is the Riesz-basis subsequence. Under finitely many
off-line zeros, all sufficiently high zeros are on the critical line. Littlewood's
gap theorem gives consecutive critical ordinates with gaps tending to zero. For
any fixed \(I\), choose one critical ordinate within a small prescribed error of
each sufficiently high lattice point \(2\pi n/L\). With error below
\(\pi/(2L)\), Kadec's one-quarter theorem gives the required Riesz basis.
The omitted set is nonempty because the basis can be selected from a high tail,
leaving at least one lower critical ordinate (and infinitely many other choices).

All sequences used above lie in \(\ell^2\), and the only synthesis map invoked
as a bounded operator is the Riesz-basis synthesis \(S_B\). No unbounded full
\(\ell^2\to L^2\) synthesis is assumed.

### III. Hostile audit and exact scope

1. This does **not** prove that Bombieri's finite-\(N\) negative eigenvector
   branch can be altered by adding \(k\). Finite-\(N\) provenance may impose a
   representative-selection rule that is lost in the limit.
2. It does prove that the limiting local equation, normalization, nonzero
   exceptional component, and half-mass inequality cannot by themselves exclude
   a null state. Any proof using this route must add a condition that survives
   the limit and is not invariant under \(c\mapsto c+\alpha k\).
3. A weighted coefficient norm could in principle remove this inflation, but
   only if the actual Bombieri variational norm is proved to control the kernel
   direction and the selected finite-\(N\) representatives. That theorem is not
   present in the record.

### IV. Next-route decision

**Route X:** prove a finite-\(N\) provenance or weighted-norm inequality that
selects the actual limiting representative and is not preserved by the critical
kernel. This is now the only viable continuation of the Bombieri branch.

**Route Y:** construct a source-defined nontracial arithmetic observer, bypassing
local unweighted synthesis altogether. It remains genuinely competitive because
it does not rely on a representative-selection theorem.

The unweighted minimum-norm/range-separation target is therefore closed as a
complete RH route: its limiting mass condition is structurally adjustable.

### V. Ledger update

**Established:** under the finite-exception hypothesis, every finite exceptional
waveform has a critical representation whose critical coefficient mass can be
made arbitrarily large by adding an exact critical synthesis-kernel vector.

**Failure / error:** treating Bombieri's limiting half-mass inequality as a
source-independent obstruction to exceptional cancellation is invalid.

**Still assumed / unknown:** whether the finite-truncation eigenvector provenance
or a source-faithful weighted norm forbids this kernel inflation.

**Next route:** finite-\(N\) representative selection first; nontracial
source-evaluable arithmetic observer in parallel.

**RH status:** no unconditional proof has been produced.
