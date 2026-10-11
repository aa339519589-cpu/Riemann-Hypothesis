## Round 159 — Proposition 6.83 does not supply the scalar-to-trace map it claims

The latest v2.4 PDF contains a proposition immediately before the trace-ideal
determinant theorem that can look like a repair of the scalar/cyclic gap.  On
physical pages 228--229 (printed pages 227--228), Proposition 6.83 says that
the open-band comparison from Section 6.1 “transports” to the coefficients

\[
 c_m(K_N)=\frac{(-1)^{m+1}}{m}\operatorname{Tr}(K_N^m),
 \qquad
 c_m(K_N)\longrightarrow c_m(K).
\tag{159.1}
\]

The convergence in (159.1) is supported by the preceding Schatten/trace
coefficient results and is not the issue.  The problem is the second claim:
equality of two linear functionals on the open-band scalar class

\[
 \langle\mu_R^{\mathrm{fp}},\phi\rangle
   =\langle\mu_{\mathrm{EF}},\phi\rangle,
 \qquad \phi\in\mathcal A_\eta,
\tag{159.2}
\]

does not by itself identify a nonlinear trace power with the value of an
ordinary scalar coefficient.  The proof of Proposition 6.83 establishes the
following two facts:

1. the finite-rank trace coefficients converge to the trace-ideal
   coefficients; and
2. the two scalar functionals agree on \(\mathcal A_\eta\).

It then says that the \(K\)-component of the first functional is represented
by the kernel of \(K\), and that its finite-rank approximation is represented
by finite trace coefficients.  The missing implication is an actual map from
the scalar coefficient/test to the cyclic product of matrix readouts.  No
formula of the form

\[
 \langle\mu_{\mathrm{EF}},\psi_m\rangle
   =\frac{(-1)^{m+1}}{m}\operatorname{Tr}(K^m)
\tag{159.3}
\]

is displayed or derived for an independently defined ordinary scalar
\(\psi_m\), and no multiplicative evaluation theorem is supplied.  This is
not a cosmetic omission: the source itself keeps the open-band test class
\(\mathcal A_\eta\) separate from the central test family
\(\mathcal C^{\mathrm{cen}}\), and Definition 6.13 explicitly introduces the
latter independently rather than recovering it from the open-band equality.

At finite rank, knowing the one-factor readouts
\(c_{ab}=\langle\mu_R^{\mathrm{fp}},\Omega_{ab}\rangle\) does give the
cyclic polynomial \(\sum c_{a_1a_2}\cdots c_{a_ma_1}\) once that polynomial is
defined.  It does not show that the ordinary scalar test used by the explicit
formula evaluates to that polynomial.  The explicit quadratic instance is
already the requirement recorded in (158.4).  A linear functional need not be
multiplicative on products; the concrete model in Round 153 gives
\(\mu(\Omega^2)=3\) while \(\mu(\Omega)^2=4\).  Thus the phrase “represented by
finite trace coefficients” cannot replace the missing scalar product/evaluation
identity.

**Established:** Proposition 6.83 adds a trace-coefficient convergence statement
and an asserted compatibility, but its proof does not establish the scalar
coefficient map or the scalar-to-cyclic evaluation needed for that compatibility.
It therefore repeats the load-bearing bridge rather than proving it.

**Remaining load-bearing statement:** prove (159.3), or an equivalent explicit
ordinary-scalar realization of every trace coefficient, independently of the
desired determinant identity; then pass through the central and infinite-window
limits.

**RH status:** no unconditional proof has been produced.
