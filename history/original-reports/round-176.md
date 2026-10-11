## Round 176 — Velez v5 replaces Connes' asymptotic semilocal trace formula by the missing global norm identity

I audited the latest Velez record, v5, *A proof of the Riemann hypothesis*:

<https://zenodo.org/records/21184595>

The six-page paper defines the arithmetic form

\[
 Q_{\rm arith}(F)=D_\infty(F)-2\sum_{p^k\le X}
     (\log p)p^{-k/2}C_F(k\log p),
\]

and correctly observes that the prime sum is exhausted when
\(X>e^R\) and \(\operatorname{supp}C_F\subset[-R,R]\).  That is only the
support identity.  The load-bearing assertion is Proposition 6.1:

\[
 q_X(F,G)=\langle\Phi_X(F),\Phi_X(G)\rangle_{H_X}.
\tag{176.1}
\]

The proof of (176.1) is not supplied.  It introduces a “cutoff-renormalized
completed vacuum vector” \(\eta_X\), then says that Connes' semilocal trace
formula gives (176.1).  No construction of \(\eta_X\), no domain statement,
and no calculation showing that its matrix coefficient is the displayed
global pole-minus-archimedean term plus exactly the prime-power sum are given.
Thus Proposition 6.1 is the positivity theorem being claimed, not a
consequence of the preceding support calculation.

The cited Connes result is materially different.  In §VII, Theorem 4 of the
source

<https://arxiv.org/pdf/math/9811068>

the operator is a cutoff operator \(R_\Lambda=\widehat P_\Lambda P_\Lambda\)
on \(L^2(X_S)\), where \(X_S=\mathbb A_S/\mathcal O_S^*\), and the conclusion
is only the asymptotic formula, as \(\Lambda\to\infty\),

\[
 \operatorname{Tr}(R_\Lambda U(h))
 =2h(1)\log'\Lambda
  +\sum_{v\in S}\int_{k_v^*}'
       \frac{h(u^{-1})}{|1-u|}\,d^*u+o(1).
\tag{176.2}
\]

It is not an exact finite-\(X\) inner-product factorization of the global
Weil form.  Moreover, Velez sets
\(C_X=\mathbb A_{S_X}^{\times}/\mathbb Q_{S_X}^{\times}\) and takes
\(H_X=L^2(C_X)\ominus H_X^{0,1}\), whereas the cited theorem acts on the
additive quotient \(L^2(X_S)\), not on \(L^2(C_S)\).  In the stated ordinary
\(L^2(C_X)\) space the characters \(|u|^0\) and \(|u|^1\) are not square
integrable along the noncompact modulus direction, so the displayed
“two-dimensional pole subspace” and its orthogonal complement are not defined
without an additional regularized construction.  None is supplied.

The original source itself records the missing global step.  In §VIII it says
that the global analogue of the cutoff trace formula is only “natural to
expect” and that it cannot be proved there for arbitrary test functions; it
then states that this global formula implies Weil positivity and is equivalent
to the relevant Riemann hypotheses.  Consequently, importing the finite-place
asymptotic (176.2), deleting its cutoff/trace limit, and declaring the result
to be \(\|\Phi_X(F)\|^2\) simply reinstates the unresolved global trace-formula
bridge under a new name.

**Established:** Velez v5 gives the elementary finite prime-support identity
and a correctly stated implication from the proposed norm identity to Weil
positivity.  It does not prove the norm identity, define its Hilbert-space
objects in the stated spaces, or establish the required global trace formula.

**Remaining load-bearing statement:** construct the claimed pole-compressed
Hilbert representation and prove (176.1) from first principles, including the
global arithmetic normalization and the passage from the semilocal cutoff to
the full Weil distribution.  That statement is absent and is precisely the
RH-sized gap.

**RH status:** no unconditional proof has been produced.
