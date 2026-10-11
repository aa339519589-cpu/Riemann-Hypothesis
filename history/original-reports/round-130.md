## Round 130 — the semilocal trace shortcut does not prove positivity of the full Weil form

I audited Velez's six-page manuscript *A proof of the Riemann Hypothesis*,
[Zenodo record 21184595](https://zenodo.org/records/21184595), against
Connes's primary semilocal trace paper
[arXiv:math/9811068](https://arxiv.org/abs/math/9811068).
The manuscript defines, for a fixed support-exhausted prime cutoff \(X\),

\[
 q_X(F,G)=\langle L_{\rm arch},C_{F,G}\rangle
 -2\sum_{p^k\le X}(\log p)p^{-k/2}C_{F,G}(k\log p),
\tag{130.1}
\]

and then asserts that there are a Hilbert space \(H_X\) and a vector
\(\Phi_X(F)\) satisfying

\[
 q_X(F,G)=\langle\Phi_X(F),\Phi_X(G)\rangle_{H_X}.
\tag{130.2}
\]

Equation (130.2) is the entire positivity step.  It is not obtained merely
from the finite semilocal trace formula.  Connes's Theorem 4 gives, for a
finite set \(S\) of places, an asymptotic formula for a cutoff operator of
the form

\[
 \operatorname{Trace}(R_\Lambda U(h))
 =2h(1)\log'\Lambda
 +\sum_{v\in S}\int'_{k_v^\ast}
 \frac{h(u^{-1})}{|1-u|}\,d^\ast u+o(1)
\tag{130.3}
\]

as \(\Lambda\to\infty\).  The theorem therefore contains both a cutoff
limit and the divergent \(2h(1)\log'\Lambda\) term.  It does not state that
a finite-\(X\) pole-compressed vacuum vector has inner product (130.1), nor
that the finite-part subtraction converting the divergent diagonal into
\(L_{\rm arch}\) commutes with the ultraviolet/infrared cutoff and the
orthogonal pole projection.

Velez's Proposition 6.1 introduces an “\(X\)-cutoff-renormalized completed
vacuum vector” \(\eta_X\) and says that applying the semilocal expansion to
\(h_{F,G}\), followed by pole compression, yields (130.2).  No explicit
formula for \(\eta_X\), no convergence estimate for its cutoff, and no
identity relating the compressed matrix coefficient
\(\langle U^X(g_F)\eta_X,U^X(g_G)\eta_X\rangle\) to the trace in (130.3)
are supplied.  The sentence “the pole projection ... collapses these to
the global residues” is exactly an unproved trace-to-vector assertion; it is
not a consequence of support exhaustion of the prime sum.

The logical distinction matters.  For a fixed \(F\), choosing \(X>e^R\)
does make the prime-power sum finite because \(C_F\) is supported in
\([-R,R]\).  It does not turn the finite-\(S\) asymptotic trace formula into
an exact positive representation of the completed archimedean-minus-prime
form.  If (130.2) were established for every compactly supported \(F\), then

\[
 Q_{\rm arith}(F)=q_X(F,F)\ge0
\]

would already be complete Weil positivity and hence RH.  Thus the claimed
“support-exhausted” conclusion is not a harmless normalization check; it is
the missing global theorem.

This is also the boundary identified in Connes's original paper: the finite
\(S\)-local trace formula is proved, while the corresponding global trace
formula is described as equivalent to the Riemann hypothesis.  The Velez
manuscript imports the finite theorem but does not prove the required global
cutoff/pole-compression bridge.

**Established:** finite semilocal trace identities and the algebraic
decomposition of the explicit formula are valid under their stated
cutoffs.

**Failure / missing lemma:** the claimed positive Hilbert-space realization
(130.2) is asserted without proving the cutoff-renormalized vacuum
construction and its exact matrix-coefficient identity.  Support exhaustion
of \(C_F\) does not supply that missing limit.

**Remaining load-bearing statement:** construct \(\eta_X\) explicitly and
prove (130.2), including all cutoff, finite-part, and pole-projection limits,
without assuming global Weil positivity.

**RH status:** no unconditional proof has been produced.
