# Proof audit: reflected PNT row, endpoint Weyl sequences, and improved eigen-source tails

Date: 2026-10-13. Scope: audit of [REPORT.md](REPORT.md) against the *actual* full reflected-prime theta Green definitions. This is an internal mathematical re-derivation and finite normalization check, not an external referee or a formal proof certificate. **Complete unconditional RH remains unproved.**

## I. PNT normalization and theta tails

Original row (from the complete Green construction):
\[
L(x)=\sum_{n>e^x}\frac{\Lambda(n)}{\sqrt n}\psi(\log n-x),
\qquad \psi=-\Phi'>0.
\]
Set \(X=e^x\), \(u=n/X\). An exact algebraic check gives
\[
e^{-x/2}L(x)=\frac1X\sum_{n> X}
\Lambda(n)\,u^{-1/2}\psi(\log u).
\]
There is **no extra 2, no missing square root of X, no division by the prime-counting function**, and prime powers stay in the von Mangoldt sum.

For u>1, the test \(u^{-1/2}\psi(\log u)\) is continuous at u=1 because \(\psi(0)=0\); its tail is \(8\pi^3u^6e^{-\pi u^2}[1+o(1)]\). The unconditional Chebyshev bound \(\sum_{n\le Y}\Lambda(n)\le3Y\) pays the dyadic shells uniformly in X. The unconditional real PNT upgrades compact-interval vague convergence to the full test, giving
\[
J=\int_1^\infty u^{-1/2}\psi(\log u)du
=\int_0^\infty e^{y/2}\psi(y)dy.
\]
This is strictly positive and finite. Multiplication by the first theta mode
\(\psi(x)\sim8\pi^3e^{13x/2-\pi e^{2x}}\)
gives precisely
\[
\mu^2=\psi/L\sim(8\pi^3/J)e^{6x-\pi e^{2x}},
\quad
2\psi L\sim16\pi^3J\,e^{7x-\pi e^{2x}}.
\]
The "6" and "7" exponents arise from \(13/2-1/2=6\) and \(13/2+1/2=7\), respectively. This resolves the normalization that the earlier coarse row bounds left unspecified.

Replacing the test by \(u^{a-1/2}\psi(\log u)\), for each *fixed real* a, remains legitimate because any algebraic power is dominated by the Gaussian e^(-pi u²). Thus the return law has every fixed real exponential moment. This is **weak convergence only**: the actual discrete row measure and its absolutely continuous limiting measure are mutually singular for every x, with Borel total-variation distance one. No operator-norm or bounded-measurable-test inference is permitted.

As a **nonrigorous check of scale only**, a six-to-fourteen-mode numerical theta quadrature on the positive half-line gives \(J\approx1.02919815233591039\); correct von Mangoldt prime-power enumeration gives approximate normalized rows \(e^{-x/2}L(x)\): 1.030698 at x=5, 1.023284 at x=6, and 1.027280 at x=7. These finite checks are not used in any proof. The PNT and complete theta tail, not numerical convergence, establish the theorem.

## II. Exact plus/minus forms and recurrence

Put \(w_n=\alpha_n\int_0^{d_n}\psi(x)\psi(d_n-x)dx\).
The actual reversibility measure has mass \(M_N=2\sum_nw_n\).
The elementary quadratic identities are
\[
\begin{aligned}
\langle r,(I-A)r\rangle_{\mu_N}
 &=\sum_n\alpha_n\int_0^{d_n}\psi\psi_{\rm ref}
 |r(x)-r(d_n-x)|^2dx,\\
\langle r,(I+A)r\rangle_{\mu_N}
 &=\sum_n\alpha_n\int_0^{d_n}\psi\psi_{\rm ref}
 |r(x)+r(d_n-x)|^2dx .
\end{aligned}
\]
There is **no factor 1/2** in these conventions. For \(r=\cos(tx)\), t log n near 2pi integers makes the minus difference uniformly small. For \(r=\sin(tx)\), the same arithmetic condition makes the plus difference uniformly small; this second assertion uses \(\sin(-u)=-\sin u\), not a second independent approximation.

Dirichlet simultaneous approximation is applied to the finite list \(\log p/(2\pi)\) for primes p≤N. If \(n=\prod p^{\nu_p}\le N\), its accumulated angular error is at most \((\sum\nu_p)\eta\le\lfloor\log_2N\rfloor\eta\). Tail \(n>N\) costs at most \(4\sum_{n>N}w_n\), which vanishes by the genuine finite edge mass. This pays *every prime power in the original form*. The return times can be chosen strictly increasing: a bounded sequence of Dirichlet denominators would force an exact integer return, whose unbounded multiples also return.

Since \(d\mu_N/dx=2\psi L\) is an integrable density, Riemann--Lebesgue applies against **every** \(L^2(\mu_N)\) vector. Centering cosine and sine gives weakly null, asymptotic norm-\(\sqrt{M_N/2}\) sequences in \(1^\perp\). Since \(0\le I\pm A\le2I\), vanishing quadratic energies force vanishing residual norms, producing Weyl singular sequences at +1 and -1. This proves **essential** spectral endpoints, not merely small Rayleigh quotients.

At the exact endpoints, \(\langle r,(I\mp A)r\rangle=0\) forces a relation on each positive edge individually. For every j≥1, reflection at j log 2 followed by reflection at (j+1) log 2 gives period log 2 on \(0<x<j\log2\). The same prime powers of 3 give log 3. Since \(\log3/\log2\notin\mathbb Q\), any local L² function with both periods is constant a.e. The minus-energy zero vectors are constants, and the plus-energy zero vector is zero. Thus ±1 are **continuous essential endpoints** after removing the constants, not spurious residual eigenvalues. \(\|(I+A)^j/2^j\|_{1^\perp}=1\) follows for all j.

The original ratio core remains dense: continuous even-at-zero compact test functions can approximate functions supported away from zero, and those functions are dense in the actual finite measure \(L^2(\mu_N)\). The bounded Markov form introduces no larger nonphysical space. One must not demand that sin(tx) itself have a smooth-even trace at zero; its core approximation is sufficient.

## III. Independent check of all exponents in the improved supercritical source bound

The inherited half-line eigen-source proof uses \(G(R)=\int_R^\infty|\mu(x)v(x)|^2dx\), where v has unit ordinary L² norm, \(\delta=(\lambda-1)/\lambda\), and
\[
\int_R^\infty|v|^2\le(D_\delta(R)+E_N(R))^2/(4\delta^2).
\]
With the new exact denominator \(\mu(x)\le Ce^{3x}e^{-\pi e^{2x}/2}\) and \(\mu_R=\sup_{x>R}\mu(x)\), the *complete* exterior prime budget is:

| Component | Upper exponential envelope, with the common \(e^{-\pi e^{2R}/2}\) suppressed |
|---|---|
| \(n\le e^R\), each forward orientation | \(e^{3R}e^{R/2}=e^{7R/2}\) |
| \(n>e^R\), forward orientations, via \(a_n\le Cn^3e^{-\pi n^2/2}\) | \(e^{7R/2}\) |
| \(e^R<n\le e^{2R}\), reflected orientations | \(e^{3R}e^R=e^{4R}\) |
| \(n>e^{2R}\), reflected orientations, via \(b_n\le Cn^{3/2}e^{-\pi n/2}\) | \(e^{4R}\) |
| Pole rank-one tail, bounded gamma crossing | at most \(e^{7R/2}\) and \(e^{3R}\) |
| Local mass \(\mu_R^2\) | super-exponentially smaller |

The prime sums use the genuine Chebyshev estimate \(\sum_{n\le X}\Lambda(n)/\sqrt n\ll\sqrt X\). No truncation remainder is discarded, and the outer \(n\)-shells are paid by the super-exponential \(n^2\) or exponential-in-n tails.

Therefore \(D_\delta+E_N\ll e^{4R}e^{-\pi e^{2R}/2}\),
\(\int_R^\infty|v|^2\ll\delta^{-2}e^{8R}e^{-\pi e^{2R}}\),
and multiplication by \(\mu_R^2\ll e^{6R}e^{-\pi e^{2R}}\) gives
\[
G(R)\ll\delta^{-2}e^{14R}e^{-2\pi e^{2R}}.
\]
These are all **upper bounds** for the actual hypothetical eigen-source, not normalized asymptotic equivalences.

For \(r=g/\psi\), Stieltjes integration with
\(w_B=e^{-Bx}/\psi^2\) has derivative
\(w'_B\ll e^{-(B+11)x}e^{2\pi e^{2x}}\).
The product with \(G(x)\) is \(O_\delta(e^{(3-B)x})\), integrable precisely for B>3 under this estimate. The origin is separately paid in the existing Green-source theorem; the new conclusion is only the large-x weighted ratio tail. The current \(W=Lr-F\) is then in weighted L² for every C>4 by the established C−1>B argument and the separately convergent entire von Mangoldt return sum. The finite-part one-sided transform has initial domain \(\operatorname{Im}\zeta>2\). No claim of analyticity inside the critical strip follows.

## IV. Exact relationship to RH and failure mechanisms

The sharp row law is a **real unconditional PNT statement**. It does not improve the known zero-free domain of zeta, and its limiting probability measure cannot replace the original discrete arithmetic reflection in total variation. The no-gap theorem means the lazy path remainder has operator norm one for each finite path depth over the *whole mean-zero vertex Hilbert space*. It does not contradict the previously proved \(O(1/J)\) bound **on positive Green spectral bands**, whose vectors have a separate inverse-moment estimate.

The sharpened source tail applies to a *hypothetical* \(\lambda>1\) eigen-source and by itself does not exclude it. None of these facts establish \(K\le I\), positivity of the original odd and even mean-zero forms, or the complete zero-location theorem.

**Audit outcome: the stated arithmetic and functional-analytic theorems follow from the displayed hypotheses and classical unconditional tools; NO NEW UNCONDITIONAL RH THEOREM PROVED.**
