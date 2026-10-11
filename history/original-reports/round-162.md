## Round 162 — an independent finite-interval operator route leaves the same global limit open

As an independent hostile comparison, Masatoshi Suzuki's arXiv v2 paper
[*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096)
(last revised 17 August 2026) proves substantial finite-interval facts without
assuming RH.  Its Theorem 1.1 identifies the localized operator \(A_a\) as a
Friedrichs self-adjoint extension, and its Theorem 1.5 proves that the zeros of
the finite-interval self-adjoint-extension function \(W(a,\theta;z)\) are real.

Those facts do not identify the finite-interval functions with \(\xi\).  The
paper's Corollary 1.6 states the exact remaining implication: if one can choose
\(\theta=\theta(a)\) and a finite normalization \(\varphi(a,z)\) so that

\[
 \lim_{a\to\infty}e^{\varphi(a,z)}W(a,\theta(a);z)
 =\frac{\xi(\tfrac12-iz)}{\xi(\tfrac12-iz)+\xi'(\tfrac12-iz)}
\tag{162.1}
\]

uniformly on compact subsets of \(\mathbb C\), then RH follows from the
finite-\(a\) reality theorem.  The paper does not prove (162.1): it labels the
statement conjectural, and its discussion says that controlling the auxiliary
spectral parameter requires detailed arithmetic estimates beyond the finite-
interval argument.  Its Section 7 derives the motivation under RH rather than
an unconditional proof of the limit.

This is a distinct construction from the Shimizu determinant ledger, so it does
not by itself prove that Shimizu's bridge fails.  It does establish the precise
general warning needed here: self-adjointness of every finite truncation and
reality of every finite approximant do not imply that the limiting analytic
function is \(\xi\).  A uniform global identification theorem, including its
normalization and arithmetic control, is the load-bearing step.

**Established:** the independent finite-interval route proves finite real
spectra but leaves the \(a\to\infty\) identification with the zeta function as
an explicit conditional limit.

**Remaining load-bearing statement:** for any proposed spectral proof, prove an
unconditional global limit/trace identity that identifies the limiting entire
function with \(\xi\), not merely a self-adjoint finite-window approximation.

**RH status:** no unconditional proof has been produced.
