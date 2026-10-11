## Round 198 — A/B result: support exhaustion is algebraic, while Proposition 6.1 carries full Weil positivity

For \(F,G\in A_0\) with
\(\operatorname{supp}C_{F,G}\subset[-R,R]\), the definition alone proves
only
\[
q_X(F,G)
=\langle L_{\rm arith},C_{F,G}\rangle
\qquad (X>e^R),
\]
because every omitted term has \(k\log p>R\) and hence vanishing
correlation.  This is finite-sum stabilization; it contains no sign
information.

If the asserted Proposition 6.1 factorization were valid, then setting
\(G=F\) would give, for every \(F\in A_0\),
\[
\langle L_{\rm arith},C_F\rangle
=q_X(F,F)
=\|\Phi_X(F)\|_{H_X}^2\ge0.
\]
Thus the proposition would already prove positivity of the complete
arithmetic Weil form on the full test class.  The source's subsequent use
of Weil's criterion confirms that this is the entire RH-bearing implication,
not a finite-place technical consequence.

The manifestly positive finite graph energy does not supply this conclusion.
For \(P_X=\{(p,k):p^k\le X\}\),
\[
E_{P_X}(F)
=2W_X\|F\|_2^2
-2\sum_{(p,k)\in P_X}(\log p)p^{-k/2}C_F(k\log p),
\]
whereas
\[
q_X(F,F)
=E_{P_X}(F)+D_\infty(F)-2W_X\|F\|_2^2.
\]
The second summand is the unproved finite-part replacement and has no
positivity consequence from \(E_{P_X}(F)\ge0\).  Therefore graph-energy
positivity cannot establish the asserted Gram identity.

Together with the direct half-density calculation in Round 196, this shows
two independent facts: support exhaustion does not prove positivity, and
the source's claimed prime-side identification is not an identity from its
definitions.  No complete unconditional proof of Proposition 6.1 follows.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
