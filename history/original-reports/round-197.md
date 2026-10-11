## Round 197 — A/B result: the cited semilocal theorem does not prove Proposition 6.1

The objects in Velez's Proposition 6.1 were compared directly with
Connes's cited semilocal theorem:

<https://arxiv.org/abs/math/9811068>

Velez defines
\[
C_X=\mathbb A_{S_X}^{\times}/\mathbb Q_{S_X}^{\times},
\qquad
H_X=L^2(C_X,d^\times u)\ominus H_X^{0,1},
\]
and treats \(|u|^0\) and \(|u|^1\) as an ordinary two-dimensional pole
subspace.  Connes's Theorem VII.4 instead works with
\[
X_S=\mathbb A_S/\mathcal O_S^\times,\qquad
C_S=J_S/\mathcal O_S^\times,
\]
and its Hilbert space is the quotient/completion of functions on \(X_S\)
with the specified quotient norm.  The theorem is therefore not a theorem
about the \(L^2(C_X,d^\times u)\) space written in Proposition 6.1.

There is also an independent integrability obstruction.  Connes's Haar
normalization satisfies
\[
\int_{|g|\in[1,\Lambda]}d^\times g\sim\log\Lambda.
\]
Consequently the constant character \(|u|^0\) has infinite \(L^2\)-norm
along the modulus direction, and \(|u|^1\) is likewise not an \(L^2\)
vector on the full modulus range.  Thus
\(L^2(C_X,d^\times u)\ominus\operatorname{span}\{|u|^0,|u|^1\}\) is not
defined as an ordinary Hilbert-space orthogonal complement without an
additional regularized or distributional construction.  None is supplied
in the proposition.

Finally, Connes's theorem gives only
\[
\operatorname{Tr}(R_\Lambda U(h))
=2h(1)\log'\Lambda+
\sum_{v\in S}\int'_{k_v^\times}
\frac{h(u^{-1})}{|1-u|}\,d^\times u+o(1)
\]
as \(\Lambda\to\infty\).  It does not provide a finite-\(X\) vector
\(\eta_X\), remove the divergent term by an exact pole projection, or
identify the resulting expression with
\[
\langle U_X(g_F)\eta_X,U_X(g_G)\eta_X\rangle=q_X(F,G).
\]
Therefore the cited theorem cannot supply the missing assertion in
Proposition 6.1.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
