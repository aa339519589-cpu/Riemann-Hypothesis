# Referee report: signed-path correction

**Recommendation: pass.** The [proof](CORRECTION_WITH_SIGNED_PATHS.md) is
consistent with the form domains and centered reference inverse in the
[full-prime report](REPORT.md) and [reference inverse](REFERENCE_INVERSE.md).

The aggregate load is correctly defined on the whole completion by
\(q=(I-A)\eta\), with \(\eta=\mathcal U(\sqrt D\,(u_0-u))\).
The smooth divergence formulas are used only when represented by functions.
The correction identity retains the complete signed load, and both lower
bounds in (5) follow by functional calculus on \([-\rho,\rho]\).
In particular, the second bound uses
\((A+I)(A+\rho I)\succeq0\); it does not imply the coefficient-one target.

The finite Dirichlet construction correctly has terminal flux
\(c_Ms_M^{(M)}\to0\), rather than zero at finite \(M\). The limiting
flux identity and the actual theta tail imply a strictly decreasing right
solution with \(s_j/s_{j+1}\to\infty\). Uniform coercivity of the principal
sections of \(I-A_t\) gives Galerkin convergence of their inverses, so the
finite Green formula passes to (6) and yields the strict sign in (9).
The prime-four edge pair has the claimed negative coefficient. Equation
(11) retains the current residual and the original signed form. The remaining
coefficient-one comparison and RH are expressly left open.

The final proof incorporates the finite-terminal-flux correction and the
typographical repair identified during review. This is a model-generated
mathematical review; it is neither Lean verification nor human certification.
