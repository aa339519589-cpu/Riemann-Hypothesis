# Explicit zero-free Mellin activation in the original theta Hilbert space

Date: 2026-10-12. Research objective remains the complete unconditional RH. This note removes a specific open activation condition in the unchanged half-damped arithmetic principal: a single **explicit** admissible even source has a Mellin transform with no zeros anywhere off Re(s)=1/2. This does not estimate the still-uncontrolled signed physical low term and does not prove RH. The order-zero Bessel property is classical; no historical-priority claim is made.

## 1. Actual source and domain

Use the original full positive even theta density Phi, completed-zeta Mellin identity
\[
\int_{\mathbb R}\Phi(x)e^{(s-1/2)x}dx=\xi(s),
\quad d\nu=2\Phi(x)\cosh(x/2)dx,\quad
m^2=\Phi/(2\cosh(x/2)),\quad Uq=\sqrt{2\Phi\cosh(x/2)}q.
\]
Fix any \(A>2\pi\), e.g. \(A=8\), and define
\[
f_A(x)=e^{-A\cosh(2x)},\qquad q_A(x)=f_A(x)/\Phi(x). \tag{1}
\]
The exact first theta mode gives
\(\Phi(x)=4\pi^2e^{9x/2-\pi e^{2x}}(1+O(e^{-2x}))\) as \(x\to+\infty\); evenness handles the other tail. Thus
\[
q_A(x)=\frac{e^{-9x/2}}{4\pi^2}
 \exp[-(A/2-\pi)e^{2x}-Ae^{-2x}/2](1+O(e^{-2x})).\tag{2}
\]
Every fixed derivative obeys the analogous rapidly decreasing bound. Because \(A>2\pi\), \(q_A\) is real, positive, even, smooth and double-exponentially decaying; it is in \(L^2_{\rm even}(\nu)\). Moreover \(v_A=Uq_A=f_A/m\) lies in the actual operator domain \(D(H)=D(B)\). Indeed \(m v_A=f_A\) is Schwartz, the complete Gamma multiplier satisfies \(b(t)=O(\log(2+|t|))\), so \(b(D)f_A\in L^2\) and \(m\,b(D)f_A\in L^2\). This represents the closed positive B-form on its whole domain. The original full prime-power potential is bounded, hence adding it does not alter \(D(B)\). No cutoff or hypothetical eigenvector is used.

The arithmetic activation uses exactly
\[
\mathcal B_q(s)=\int_{\mathbb R}\Phi(x)q(x)e^{-(s-1/2)x}dx.
\]
With \(u=2x\) and \(\nu_s=(s-1/2)/2\), the defining K-Bessel integral gives the **exact entire identity**
\[
\boxed{\mathcal B_{q_A}(s)
=\int_0^\infty e^{-A\cosh u}\cosh(\nu_su)du
=K_{\nu_s}(A).}\tag{3}
\]
It automatically obeys reflection about Re(s)=1/2.

## 2. Strong theorem: no off-line zeros, all critical zeros simple

**Theorem.** For every fixed \(A>2\pi\),
\[
\boxed{\mathcal B_{q_A}(s)\ne0\quad
  (\operatorname{Re}s\ne1/2).}\tag{4}
\]
All zeros of this entire function are simple, lie on the critical line, and have \(|\operatorname{Im}s|>2A\). In fact they are precisely \(s=1/2\pm2i\sqrt{\lambda_j}\), where \(\lambda_j>A^2\) are the increasing simple Dirichlet eigenvalues of
\[
T_A=-\partial_y^2+e^{2y}\quad
\text{on }(\log A,\infty),\qquad g(\log A)=0.\tag{5}
\]

**Proof.** The integral in (3), differentiated in A and integrated by parts in its integration variable, satisfies
\[
r^2K_\nu''(r)+rK_\nu'(r)-(r^2+\nu^2)K_\nu(r)=0.
\]
With \(g_\nu(y)=K_\nu(e^y)\), this becomes exactly
\[
-g_\nu''(y)+e^{2y}g_\nu(y)=-\nu^2g_\nu(y). \tag{6}
\]
For each fixed complex \(\nu\), the same integral shows \(g_\nu,g_\nu'\) decay super-exponentially as \(y\to\infty\). Substituting \(u=w/\sqrt r\) gives
\(K_\nu(r)\sim\sqrt{\pi/(2r)}e^{-r}\), so \(g_\nu\not\equiv0\). If \(K_\nu(A)=0\), then the boundary in (5) is Dirichlet; multiplication of (6) by \(\overline{g_\nu}\) and integration by parts yields
\[
-\nu^2\|g_\nu\|_2^2
=\|g_\nu'\|_2^2+\int_{\log A}^\infty e^{2y}|g_\nu|^2dy
>A^2\|g_\nu\|_2^2. \tag{7}
\]
Hence \(-\nu^2>A^2\) is real, forcing \(\nu=i\tau\), \(\tau\) real, \(|\tau|>A\). Since \(\nu=(s-1/2)/2\), (4) and the height exclusion follow.

Conversely the Dirichlet operator \(T_A\) is positive with compact resolvent. Compactness follows from Rellich on finite y-intervals and the tail inequality
\(\int_Y^\infty|g|^2\le e^{-2Y}\int_Y^\infty e^{2y}|g|^2\).
It has infinitely many positive eigenvalues, all simple by uniqueness of the one-dimensional decaying solution. At any eigenvalue \(\lambda>0\), the unique decaying solution is \(K_{i\sqrt\lambda}(e^y)\); hence its boundary zero produces a zero of (3).

For completeness the zeros are simple as **order-variable** zeros, not merely distinct y-eigenvalues. Near an eigenvalue set \(g(y,\lambda)=K_{i\sqrt\lambda}(e^y)\) and \(W=g\,\partial_\lambda g'-g'\partial_\lambda g\). Equation (6) gives \(W'=-g^2\). At the real eigenvalue, \(g\) is real and \(W(\infty)=0\), so
\[
-g'(\log A,\lambda)\partial_\lambda g(\log A,\lambda)
=\int_{\log A}^\infty g(y,\lambda)^2dy>0.
\]
ODE uniqueness implies \(g'(\log A,\lambda)\ne0\), so \(\partial_\lambda K_{i\sqrt\lambda}(A)\ne0\); \(\lambda=-\nu^2\) and \(\nu=(s-1/2)/2\) have nonzero derivatives at these roots. Thus every root of (3) is simple. QED.

## 3. An exact mean-zero source and direct zeta-zero activation

The original probability measure gives the exact mean
\[
\int q_A\,d\nu=2\int_{\mathbb R}\cosh(x/2)e^{-A\cosh 2x}dx
=\boxed{2K_{1/4}(A)}. \tag{8}
\]
Indeed substitute \(u=2x\) and the same Bessel defining integral. Define the genuine even mean-zero function
\[
q_A^\circ=q_A-2K_{1/4}(A),\qquad \int q_A^\circ d\nu=0.
\]
It belongs to the unchanged complete jump-form and operator domains: both \(q_A\) and the exact ground state 1 do. Its source is \(f_A-2K_{1/4}(A)\Phi\), so it retains double-exponential source tails even though \(q_A^\circ\) itself tends to a constant at infinity.

As \(\mathcal B_1(s)=\xi(s)\) by theta reflection,
\[
\boxed{\mathcal B_{q_A^\circ}(s)
=K_{(s-1/2)/2}(A)-2K_{1/4}(A)\xi(s).}\tag{9}
\]
At **every hypothetical nontrivial zero** \(\rho\) of the ordinary zeta function with \(\operatorname{Re}\rho\ne1/2\), \(\xi(\rho)=0\), and therefore
\[
\boxed{\mathcal B_{q_A^\circ}(\rho)
=K_{(\rho-1/2)/2}(A)\ne0.}\tag{10}
\]
One fixed \(A=8\) works at every height and for any multiplicity. The uncentered \(q_A\) also activates *all* off-line zeros of \(\zeta_{\mathbb Q(\omega)}\), even those coming only from the quadratic Dirichlet L factor. For those Dirichlet-only zeros, (10) is not asserted for the centered source.

## 4. Uniform explicit size on bounded complex windows

**Quantitative theorem.** If \(|\nu|\le R\) and \(A\ge100(1+R^2)\), then
\[
\boxed{|K_\nu(A)|\ge\tfrac9{10}K_0(A)
\ge\tfrac9{10}e^{-A-1}/\sqrt A.}\tag{11}
\]

**Proof.** For \(0\le u\le1\), \(\cosh u\le1+u^2\); restriction of the positive K0 integral to \(u\le A^{-1/2}\) gives \(K_0(A)\ge e^{-A-1}/\sqrt A\). The entire cosh series gives
\(|\cosh(\nu u)-1|\le|\nu|^2u^2e^{|\nu|u}/2\). Using \(\cosh u\ge1+u^2/2\), the inequality \(Ru\le Au^2/4+R^2/A\), and the elementary Gaussian moment,
\[
|K_\nu(A)-K_0(A)|
\le\frac{R^2}{2}e^{-A+R^2/A}\int_0^\infty u^2e^{-Au^2/4}du
=\frac{R^2\sqrt\pi}{A^{3/2}}e^{-A+R^2/A}.
\]
Divide by the positive K0 lower bound:
\[
|K_\nu-K_0|/K_0
\le e\sqrt\pi\,(R^2/A)e^{R^2/A}
\le e\sqrt\pi\,e^{1/100}/100<1/10,
\]
using \(e<3,\sqrt\pi<2,e^{1/100}<11/10\). Reverse triangle proves (11). QED.

In particular \(A\ge100(1+T^2)\) ensures the explicit lower bound (11) simultaneously for all \(0\le\operatorname{Re}s\le1\), \(|\operatorname{Im}s|\le T\), since \(|\nu_s|^2\le 1/16+T^2/4\). At ordinary-zeta zeros, the **same** bound applies to the mean-zero source (9). These amplitudes are for unnormalized q; norm-rescaling must be accounted for in any later use.

## 5. Exact effect on the original full RH strategy

The fixed principal factor in HALF_DAMPED_PROBE.md / the reflected theta enclosure is
\[
e^{(s-5/6)^2}H_{\mathrm{half},S}(s)
\mathcal B_q(s)/\zeta_{\mathbb Q(\omega)}^S(s).
\]
The inherited \(H_{\mathrm{half},S}\) and the finite deleted Euler factors are nonzero at every \(\operatorname{Re}s>1/2\). Choosing the **explicit uncentered** source \(q_A\) proves that a hypothetical Dedekind-zeta right-half off-line zero produces a principal pole of exactly its full multiplicity: no numerator activation hypothesis is needed. At an ordinary-zeta off-line zero one may instead use the explicit mean-zero \(q_A^\circ\). All original Gaussian factors, prime powers, physical masks and signed correlations remain unchanged.

This theorem removes **source cancellation** as a possible obstruction in the stated principal. It supplies neither the unproved signed physical low estimate nor a global Weil positivity theorem. Thus it does not rule out a single actual off-line zero and does not prove RH.

**Result:** rigorous explicit all-height activation, true-domain realization, center projection, elementary finite-window lower bound; **NO NEW UNCONDITIONAL RH THEOREM PROVED**.

Dependencies: ORIGINAL_FORM_FOUNDATION.md (unchanged true theta/operator domain); HALF_DAMPED_PROBE.md (principal Euler multiplier); ../20261013_reflected_theta_enclosure/REPORT.md (fixed q activation and exact principal). The paired AUDIT_EXPLICIT_MELLIN_ACTIVATOR.md checks the ODE sign, mean, constants and limitations independently. Bessel integral/differential-equation references: DLMF 10.32.9, 10.25.1.
