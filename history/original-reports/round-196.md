## Round 196 — A/B result: Proposition 6.1 has no complete unconditional proof

**Source inspected:** Simon Velez, *A Proof of the Riemann Hypothesis*,
v5, Zenodo record
<https://zenodo.org/records/21184595>, PDF
/tmp/velez-rh-v5.pdf.

The definitions in the source give a direct algebraic obstruction to the
prime-side identification used around Proposition 6.1.  With
\[
g(x)=x^{-1/2}F(\log x),\qquad
h(x)=\int_0^\infty g(xy)g(y)\,dy,
\]
the substitution \(x=e^a,\ y=e^u\) gives
\[
h(e^a)=e^{-a/2}C_F(a).
\]
Since \(C_F(-a)=C_F(a)\), for \(a=k\log p>0\),
\[
h(p^k)+h(p^{-k})
=\left(p^{-k/2}+p^{k/2}\right)C_F(k\log p).
\]
The source instead uses
\[
h(p^k)+h(p^{-k})
=2p^{-k/2}C_F(k\log p)
\]
to identify its Definition 3.1 prime term with the prime term in the
explicit formula.  These expressions differ whenever
\(C_F(k\log p)\ne0\); such \(F\in C_c^\infty(\mathbb R)\) exist, for example
a nonnegative bump whose support overlaps its translate by \(\log 2\).
Therefore the printed prime-side matching calculation is false as an
identity from the stated definitions.

Independently, Proposition 6.1 does not define or prove the asserted Gram
identity.  It writes
\[
H_X=L^2(C_X,d^\times u)\ominus H_X^{0,1}
\]
and calls the characters \(|u|^0,|u|^1\) a two-dimensional pole subspace.
Those characters are not ordinary \(L^2\) vectors along the noncompact
modulus direction, so the displayed orthogonal subtraction requires an
additional generalized-vector or regularized construction.  The source
does not provide one.  Its \(\eta_X\) is only named as a
“cutoff-renormalized completed vacuum vector”; no explicit vector,
renormalization limit, domain, or convergence proof is given.  The cited
semilocal result is an asymptotic cutoff trace with a divergent term and
an \(o(1)\) remainder, not the exact matrix-coefficient identity asserted
in Proposition 6.1.  The passage from that trace to
\[
\langle U_X(g_F)\eta_X,U_X(g_G)\eta_X\rangle
=q_X(F,G)
\]
is consequently not proved.

The support condition \(X>e^R\) proves only the algebraic stabilization of
the finite prime sum.  It does not prove the Hilbert-space factorization or
the nonnegativity of \(q_X\).  Hence the implication to Weil positivity and
then to RH is not established.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
