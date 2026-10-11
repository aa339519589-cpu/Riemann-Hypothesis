## Round 182 — the Heegner/DSM metric route remains active, and its positivity bridge is explicitly repairable

I continued the Heegner branch instead of removing it:

<https://zenodo.org/records/21136548>

The manuscript's arithmetic starting point is valid in the weaker form
\[
 \zeta_K(s)=\zeta(s)L(s,\chi_{-163}).
 \tag{182.1}
\]
Thus every zero of \(\zeta\) is a zero of the product.  It is not true that
the nontrivial zeros of \(\zeta_K\) are exactly the nontrivial zeros of
\(\zeta\): zeros of the Dirichlet factor contribute as well, and
multiplicities add.  The manuscript itself first says “among” and later
changes this to “exactly”.  Also, the level-\(163\) trivial-character
scattering matrix computed in Round 181 is not automatically the scattering
matrix of the Dedekind factor in (182.1); a \(\chi_{-163}\)-twisted
automorphic space would have to be defined and its scattering data derived.

The source correctly identifies one genuine issue: second-sheet scattering
poles are resonances, not ordinary \(L^2\) eigenvalues of the primary
self-adjoint Laplacian.  Its proposed repair is the “Phase Rigidity Pillar”,
which states that a self-adjoint operator with exactly the unchanged
resonance spectrum exists.  That statement is the central spectral bridge,
not a consequence of the preceding arithmetic factorization.  The subsequent
Lax--Phillips construction defines an interacting subspace and a dissipative
generator, but does not prove that the proposed incoming/outgoing subspaces
have the asserted completeness, that the compressed evolution has the stated
domain, or that its resonance spectrum can be made point spectrum without
altering the scattering divisor.

The proposed metric is
\[
 G=I+M_{861},
 \qquad
 \langle f,g\rangle_G
 =
 \langle f,g\rangle_{L^2}
 +\sum_{j,k=1}^{861}W_{jk}f(\tau_j)\overline{g(\tau_k)}.
 \tag{182.2}
\]
Several independent construction statements are needed before (182.2) is a
Hilbert-space inner product.  Point evaluation is not a bounded functional on
an \(L^2\) space; the graph/Sobolev domain on which all evaluations are
defined, and the bounded extension of \(M_{861}\) to the interacting space,
are not supplied.  The weights are described as the dual frame for the
unknown continuous dissipative flux, so their “exact” definition already
depends on the equality they are meant to prove.  A PID property, a
maximum-packing assertion, or a positive separation of finitely many lattice
nodes does not prove that those point evaluations form a tight frame for an
infinite-dimensional automorphic core, nor that a finite-rank operator
reproduces the full boundary-flux commutator.

There is also a direct algebraic failure in the proof of strict positivity.
Writing \(m=\|M_{861}\|\), the source bounds the metric from below by
\[
 a^2+(1-m)b^2-2ab,
 \tag{182.3}
\]
where \(a=\|f_\perp\|\) and \(b=\|f_\parallel\|\), and represents this bound
by
\[
 \begin{pmatrix}1&-1\\-1&1-m\end{pmatrix}.
 \tag{182.4}
\]
But
\[
 \det\begin{pmatrix}1&-1\\-1&1-m\end{pmatrix}
 = (1-m)-1=-m,
\]
which is negative for \(m>0\), not positive when \(m<1\).  For example,
at \(a=b=1\), (182.3) equals \(-m\).  At \(m=0\) the determinant is zero,
so the displayed lower bound still does not establish strict positivity.
The Cauchy--Schwarz estimate has simply discarded the structure that could
make the cross term vanish; it cannot prove the claimed conclusion.

There is a clean repair target inside the same route: prove independently
that \(M_{861}\) is a self-adjoint bounded operator on the actual interacting
space and establish
\[
 \|M_{861}\|_{\mathcal B(\mathcal K)}<1.
 \tag{182.5}
\]
Then positivity follows directly from
\(\langle f,(I+M_{861})f\rangle\ge(1-\|M_{861}\|)\|f\|^2\), without the
invalid two-variable estimate.  The current proof only estimates an
undefined finite nodal matrix, and its claimed Gershgorin margin is not
calculated.  It therefore does not establish (182.5).

Finally, even a valid positive metric and the formal relation
\(B^*G=GB\) would yield symmetry in an equivalent norm only after domains,
closability, and essential self-adjointness were proved.  Symmetry on a dense
core alone is not essential self-adjointness.  The exact resonance-to-spectrum
identification and the twisted-versus-trivial scattering identification
remain separate obligations.  These are constructive repair tasks in the
Heegner/DSM route, which remains coupled to the Fredholm, Weil, Thorin, and
arithmetic routes.

**Established:** the factorization (182.1) and the resonance-versus-\(L^2\)
distinction are valid starting facts.  The manuscript supplies a concrete
metric ansatz and a possible positivity target, but its proof of
positive-definiteness contains the sign error (182.4), and the exact
resonance, frame, domain, and determinant bridges are not established.

**Remaining load-bearing statement:** define the twisted or untwisted
scattering Hilbert space unambiguously, construct the metric as a bounded
positive operator on its full domain, prove the self-adjoint resonance
realization without changing the divisor, and identify that divisor with the
zeros of \(\zeta\) rather than merely with the larger product (182.1).

**RH status:** no unconditional proof has been produced.
