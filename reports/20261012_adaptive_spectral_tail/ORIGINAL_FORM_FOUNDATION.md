# Foundational derivation of the original even jump operator

This note derives the source identity and the complete-form realization used by the three-eighths certificate. It uses the full theta kernel and every prime power. It assumes neither RH nor any zero-location statement. In particular, no spectral identification from an earlier report is used.

The analytic inputs are the Jacobi theta identity for the kernel below, the meromorphic continuation and functional equation of ζ, and Stirling's formula for Γ in fixed vertical strips. The functional equation and definition of ξ are recorded in [DLMF 25.4.3](https://dlmf.nist.gov/25.4#E3) and [25.4.4](https://dlmf.nist.gov/25.4#E4), the gamma estimate used below follows from [DLMF 5.11.1](https://dlmf.nist.gov/5.11#E1), and the digamma growth used for the multiplier follows from [DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2). The needed vertical bound for ζ′ is derived directly in §2, rather than assumed. The derivation of the source identity is included.

## 1. Definitions and Fourier multiplier

Use
\[
 \widehat f(t)=\int_{\mathbb R}f(x)e^{itx}\,dx,\qquad
 f(x)=\frac1{2\pi}\int_{\mathbb R}\widehat f(t)e^{-itx}\,dt,
\]
and
\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad \Xi(t)=\xi(\tfrac12+it).
\]
The complete theta kernel is
\[
 \Phi(x)=\sum_{r\ge1}
 (4\pi^2r^4e^{9x/2}-6\pi r^2e^{5x/2})e^{-\pi r^2e^{2x}},
 \qquad \widehat\Phi=\Xi.
\]
The Jacobi identity gives that \(\Phi\) is even, smooth, strictly positive, and has double-exponential tails together with all derivatives. In particular \(\Phi\in\mathcal S(\mathbb R)\), and its Fourier transform is entire and decreases faster than every power on each fixed horizontal strip.

The Mellin normalization can also be checked directly. For \(\operatorname{Re}s>1\), put \(u=\pi r^2e^{2x}\) in each summand. The two component integrals are
\[
 2\pi^{-s/2}r^{-s}\Gamma(2+s/2)
 \quad\text{and}\quad
 -3\pi^{-s/2}r^{-s}\Gamma(1+s/2),
\]
respectively. Their absolute integrals are summable over \(r\), since for \(\sigma=\operatorname{Re}s>1\) their sum is
\[
 \pi^{-\sigma/2}\zeta(\sigma)
 \bigl(2\Gamma(2+\sigma/2)+3\Gamma(1+\sigma/2)\bigr)<\infty.
\]
Thus Fubini gives
\[
 \begin{aligned}
 \int_{\mathbb R}\Phi(x)e^{(s-\frac12)x}\,dx
 &=\pi^{-s/2}\zeta(s)
   \bigl[2\Gamma(2+s/2)-3\Gamma(1+s/2)\bigr]\\
 &=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
 =\xi(s),\qquad \operatorname{Re}s>1,
 \end{aligned}
\]
where the last equality uses the gamma recurrence. The double-exponential theta tails make the Mellin integral locally uniformly convergent for every \(s\in\mathbb C\), so it is entire; by analytic continuation the identity holds for all \(s\). In particular, taking \(s=\tfrac12+it\) gives \(\widehat\Phi(t)=\Xi(t)\) with the stated Fourier convention.

Put
\[
 h(x)=\cosh(x/2),\quad p(x)=2\Phi(x)h(x),\quad d\nu(x)=p(x)\,dx,
 \quad m(x)^2=\frac{\Phi(x)}{2h(x)},\quad (Uq)(x)=\sqrt{p(x)}q(x).
\]
Then \(U:L^2(\nu)\to L^2(dx)\) is unitary once \(\int\Phi e^{x/2}=\int\Phi e^{-x/2}=1/2\), which follows by evaluating \(\Xi(\pm i/2)=\xi(0)=\xi(1)=1/2\). Thus \(\int d\nu=1\). Also \(m\sqrt p=\Phi\).

Let \(\alpha_n=\Lambda(n)/\sqrt n\), \(d_n=\log n\), and define the symmetric shift sum
\[
 (Sf)(x)=\sum_{n\ge2}\alpha_n\{f(x+d_n)+f(x-d_n)\}.
\]
The sum is locally normally convergent on \(\Phi\) and its derivatives: on a fixed compact set, the shifted theta tails are bounded by \(C n^C e^{-c n^2}\). Define
\[
 a(t)=\operatorname{Re}\psi(\tfrac14+it/2)-\log\pi,
 \quad C_0=\gamma+\tfrac\pi2+3\log2+\log\pi,
 \quad b(t)=a(t)+C_0.
\]
The digamma value \(\psi(1/4)=-\gamma-\pi/2-3\log2\), from the reflection and duplication formulas and \(\psi(1/2)=-\gamma-2\log2\) ([DLMF 5.5.4](https://dlmf.nist.gov/5.5#E4), [DLMF 5.5.8](https://dlmf.nist.gov/5.5#E8), [DLMF 5.4.13](https://dlmf.nist.gov/5.4#E13)), gives \(b(0)=0\). Its positive expansion is
\[
 b(t)=\sum_{j\ge0}
 \frac{(t/2)^2}{(j+1/4)((j+1/4)^2+(t/2)^2)}\ge0.
\]
For \(u\ne0\), define the even kernel
\[
 k(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}.
\]
On \(u>0\), expanding \(k(u)=\sum_{j\ge0}e^{-(2j+1/2)u}\) and integrating each term gives the exact representation
\[
b(t)=2\int_0^\infty k(u)(1-\cos(tu))\,du.
\]
Consequently, with \(A=a(D)=b(D)-C_0\), for Schwartz \(f\)
\[
 (Af)(x)=-C_0f(x)+\int_0^\infty k(u)
       [2f(x)-f(x+u)-f(x-u)]\,du.                 \tag{1}
\]
The integral converges at zero by the second difference. Also \(A\Phi\in\mathcal S\), since \(a(t)\) is smooth with logarithmic growth and \(\Xi\) is Schwartz on the real axis.

## 2. The source identity, derived by zero-cancelling contour shifts

We prove, pointwise on \(\mathbb R\),
\[
                         S\Phi=A\Phi+h.            \tag{2}
\]
Fix \(1/2<\eta<3/2\). Fourier inversion and a contour shift of the individual entire integrand give
\[
 \sum_{n\ge2}\alpha_n\Phi(x+d_n)
 =\frac1{2\pi}\int_{\mathbb R-i\eta}
     \Xi(t)\frac{-\zeta'}{\zeta}(\tfrac12+it)e^{-itx}\,dt.       \tag{3}
\]
Indeed, on \(\operatorname{Im}t=-\eta\), the Dirichlet terms have absolute size \(\Lambda(n)n^{-1/2-\eta}\), whose sum converges. The strip decay of \(\Xi\) justifies both the individual contour shift and exchanging the sum and integral. The other direction similarly gives
\[
 \sum_{n\ge2}\alpha_n\Phi(x-d_n)
 =\frac1{2\pi}\int_{\mathbb R+i\eta}
     \Xi(t)\frac{-\zeta'}{\zeta}(\tfrac12-it)e^{-itx}\,dt.       \tag{4}
\]

Before shifting either contour back to the real line, use the functional equation explicitly:
\[
 \Xi(t)=\xi(\tfrac12+it)=\xi(\tfrac12-it),
\]
by \(\xi(s)=\xi(1-s)\) [DLMF 25.4.3](https://dlmf.nist.gov/25.4#E3). Thus the product in (3) uses \(s=\tfrac12+it\), while the product in (4) uses \(s=\tfrac12-it\). During either sweep from the shifted line to the real line, \(\operatorname{Re}s\) lies between \(\tfrac12\) and \(\tfrac12+\eta\), so the gamma factor has no poles in the swept region.

No zero-free estimate is used in moving these contours. Before moving either contour, use the exact identity
\[
 \xi(s)\frac{-\zeta'}{\zeta}(s)
 =-\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta'(s).                 \tag{5}
\]
It removes every zeta-zero pole in the swept region, including its full multiplicity, algebraically. The right side is meromorphic there; because \(\operatorname{Re}s\) stays positive, its only pole is \(s=1\). Thus there are no poles from nontrivial zeros, whether or not they lie on the critical line.

At \(s=1\), the right side of (5) has residue \(+1/2\), since \(\zeta'(s)\sim-(s-1)^{-2}\) and
\(\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\sim(s-1)/2\). For (3), \(s=1/2+it\), so the corresponding residue in \(t\) is \(-i/2\). For (4), \(s=1/2-it\), it is \(+i/2\). Including \(e^{-itx}\) and orienting the rectangles gives
\[
 I_-(x)=I_{\mathbb R,+}(x)+\tfrac12e^{-x/2},\qquad
 I_+(x)=I_{\mathbb R,-}(x)+\tfrac12e^{x/2},                    \tag{6}
\]
where \(I_-\) is the integral on \(\mathbb R-i\eta\), \(I_+\) the integral on \(\mathbb R+i\eta\), and the two \(I_{\mathbb R,\pm}\) are the respective continued-product integrals on the real line.

For completeness, the needed polynomial bound for \(\zeta'\) follows directly from the partial-summation identity
\[
 \zeta(s)=\frac{s}{s-1}-s\int_1^\infty \{x\}x^{-s-1}\,dx,
 \qquad \operatorname{Re}s>0,                              \tag{5a}
\]
initially obtained for \(\operatorname{Re}s>1\) and then continued to \(\operatorname{Re}s>0\). On a fixed strip \(\sigma_0\le\operatorname{Re}s\le M\) with \(\sigma_0>0\), set \(I(s)=\int_1^\infty\{x\}x^{-s-1}dx\). Since \(0\le\{x\}<1\),
\[
 |I(s)|\le\sigma_0^{-1},\qquad |I'(s)|\le\sigma_0^{-2},
\]
and differentiating (5a) gives, for \(|\operatorname{Im}s|\ge2\),
\[
 |\zeta'(s)|\le |s-1|^{-2}+\sigma_0^{-1}+|s|\sigma_0^{-2}
 =O_{\sigma_0,M}(1+|\operatorname{Im}s|).
\]
The pole of \(\zeta'\) at \(s=1\) has already been treated by the residue calculation. The horizontal edges therefore vanish: after (5), Stirling gives exponential decay of \(\Gamma(s/2)\) in the fixed strip, which dominates this direct polynomial bound. No reciprocal-zeta bound occurs.

Differentiate \(\xi(s)=\xi(1-s)\) logarithmically. The rational terms from \(s(s-1)\) cancel between \(s\) and \(1-s\), yielding
\[
 -\frac{\zeta'}{\zeta}(s)-\frac{\zeta'}{\zeta}(1-s)
 =\tfrac12\psi(s/2)+\tfrac12\psi((1-s)/2)-\log\pi.           \tag{7}
\]
Equation (7) is an identity of meromorphic functions, first obtained away from the zero sets and then continued. Multiplying by \(\xi(s)=\xi(1-s)\) gives
\[
 \xi(s)\left(-\frac{\zeta'}{\zeta}(s)-\frac{\zeta'}{\zeta}(1-s)\right)
 =\xi(s)\left(\tfrac12\psi(s/2)+\tfrac12\psi((1-s)/2)-\log\pi\right).
\]
Each product on the left is removable at nontrivial zeta zeros: for the first this is the exact cancellation in (5), and for the second it is the same identity with \(1-s\) in place of \(s\). Thus the multiplied identity extends across zeros, including any on the critical line, without evaluating a logarithmic derivative there. For \(s=1/2+it\), \(t\in\mathbb R\), its right side is \(\Xi(t)a(t)\), with values at zeros given by analytic continuation. Therefore the sum of the two real-line integrals in (6) is
\[
 \frac1{2\pi}\int_{\mathbb R}\Xi(t)a(t)e^{-itx}\,dt=(A\Phi)(x).
\]
The residues in (6) add to \(\tfrac12(e^{x/2}+e^{-x/2})=h(x)\). Equations (3)--(7) prove (2). The only crossed poles are the two copies of the pole \(s=1\); all zero cancellation precedes contour deformation. This proves the identity unconditionally.

## 3. The full weighted prime operator is bounded

The theta envelope needed for the complete prime sum follows directly from the defining series and evenness. For \(z=|x|\),
\[
 0<m(x)^2\le A_*e^{4z-\pi e^{2z}},\qquad A_*=4\pi^2\frac{125}{121}.             \tag{8}
\]
For \(x\ge0\), factor the first Gaussian \(e^{-\pi e^{2x}}\), use \(2h(x)\ge e^{x/2}\), and bound the remaining \(\sum_{r\ge1}r^4e^{-\pi(r^2-1)e^{2x}}\) by \(125/121\); evenness handles \(x<0\).

For \(d_n=\log n\), put \(r=e^{2|x|}\), \(s=e^{2|x+d_n|}\), and \(u=\sqrt{rs}\). Then \(u\ge n\), and (8) gives
\[
 m(x)m(x+d_n)\le A_*u^2 e^{-\pi u}\le A_*n^2e^{-\pi n},\qquad n\ge2.       \tag{9}
\]
The last inequality follows because \(u^2e^{-\pi u}\) decreases for \(u\ge2\). Thus
\[
 \sum_{n\ge2}\alpha_n\|M_m\tau_{d_n}M_m\|
 \le A_*\sum_{n\ge2}\Lambda(n)n^{3/2}e^{-\pi n}<\infty.       \tag{10}
\]
The same estimate applies to \(-d_n\). Consequently
\[
 V=C_0M_{m^2}+M_mSM_m
\]
is a bounded self-adjoint operator on the full even \(L^2(dx)\) space, with the prime series converging in operator norm. This accounts for all prime powers.

We also need boundedness of the prime jump form on \(L^2(\nu)\). From (2), \(S\Phi/h=1+A\Phi/h\) is bounded, since \(A\Phi\) is Schwartz and \(h\ge1\). For every \(q\),
\[
 \begin{aligned}
 E_P(q)&=\sum_{n\ge2}\alpha_n\int\Phi(x)\Phi(x+d_n)|q(x)-q(x+d_n)|^2dx\\
 &\le 2\int\Phi(x)S\Phi(x)|q(x)|^2dx
 =\int \frac{S\Phi(x)}{h(x)}|q(x)|^2d\nu(x).
 \end{aligned}                                                   \tag{11}
\]
Hence \(E_P\) is a bounded nonnegative quadratic form on \(L^2(\nu)\).

## 4. The maximal jump form and its compact-smooth core

Let \(\mathcal E=E_\Gamma+E_P\), where
\[
 E_\Gamma(q)=\frac12\iint\Phi(x)\Phi(y)k(x-y)|q(x)-q(y)|^2dxdy,
\]
and let its domain be the maximal finite-energy domain in \(L^2(\nu)\). This maximal form is closed: regard the continuous difference and each prime difference as a single map from \(q\) into the direct sum of their weighted \(L^2\) edge spaces. If \(q_j\to q\) in \(L^2(\nu)\), a subsequence converges almost everywhere; the edge differences then converge almost everywhere to the differences of \(q\), identifying the limit of any Cauchy sequence in the form graph. The form is dense since it contains \(C_c^\infty\).

Here is the core argument for the *maximal* domain. First truncate values with the radial projection \(P_M\) onto \(|z|\le M\). The residual map \(z-P_Mz\) is Lipschitz, vanishes in the limit pointwise, and has difference bounded by \(2|z-w|\). Dominated convergence in every edge integral and in \(L^2(\nu)\) gives convergence in the form norm. Thus bounded finite-energy functions are dense.

Choose even smooth cutoffs \(\chi_R\), equal to one on \([-R,R]\), supported in \([-2R,2R]\), with \(0\le\chi_R\le1\) and \(\|\chi_R'\|_\infty\le C/R\). For a bounded \(q\), \(\chi_Rq\to q\) in \(L^2(\nu)\). In the continuous energy, write
\[
 (1-\chi_R(x))q(x)-(1-\chi_R(y))q(y)
 =(1-\chi_R(x))(q(x)-q(y))+q(y)(\chi_R(y)-\chi_R(x)).
\]
The first squared term tends to zero by dominated convergence. The second is bounded by
\[
 C\|q\|_\infty^2\int_{\mathbb R}k(u)\min(1,u^2/R^2)
       \left(\int\Phi(x)\Phi(x+u)dx\right)du
 \le \frac{C'\|q\|_\infty^2}{R^2}\int u^2k(u)du\longrightarrow0,
\]
using Cauchy--Schwarz for the autocorrelation of \(\Phi\). The prime energy of a difference is bounded by (11) times its \(L^2(\nu)\) norm, so it also tends to zero. Hence compactly supported finite-energy functions are form dense.

On a fixed compact set, \(\Phi\) is smooth and bounded above and below by positive constants. Since \(k(u)\asymp |u|^{-1}\) near zero, finite continuous energy of a compactly supported function implies
\[
 \int_{|u|<1}\frac{\|q(\cdot+u)-q\|_2^2}{|u|}\,du<\infty.
\]
By Plancherel, this is equivalent, together with \(L^2\), to
\(\int\log(2+|t|)|\widehat q(t)|^2dt<\infty\), because
\(1+\int_0^1(1-\cos(tu))du/u\asymp\log(2+|t|)\) for all real \(t\). An even standard mollifier therefore approximates \(q\) in this logarithmic Sobolev norm. On a common compact support, the small-jump weighted energy is bounded by that norm; the part \(|u|\ge1\) is bounded by the \(L^2\) norm because \(k\) is integrable there and \(\Phi\) is bounded. The prime energy is bounded by (11). Thus mollification converges in the full form norm. Symmetrizing the cutoffs and using an even mollifier proves that even \(C_c^\infty\) is a core for the original maximal even form.

## 5. Closed source form and its core

Define
\[
 \mathcal H_{\log}=\left\{f\in L^2:\int\log(2+|t|)|\widehat f(t)|^2dt<\infty\right\},
 \qquad
 \mathfrak b[v]=\frac1{2\pi}\int b(t)|\widehat{mv}(t)|^2dt.
\]
The form domain is
\[
 \mathcal D=\{v\in L^2_{\rm even}:mv\in\mathcal H_{\log}\}.                 \tag{12}
\]
The positive series for \(b\) shows \(b(t)\asymp\log(2+|t|)\) at infinity, so \(\|g\|_2^2+\int b|\widehat g|^2\) is equivalent to the \(\mathcal H_{\log}\) norm. The form \(\mathfrak b\) is closed: if \(v_j\) is Cauchy in its form norm, then \(v_j\to v\) in \(L^2\); boundedness of \(m\) makes \(mv_j\to mv\) in \(L^2\), while the form seminorm makes \(mv_j\) Cauchy in the \(b\)-weighted Fourier norm. Hence \(mv_j\) converges in \(\mathcal H_{\log}\) to \(mv\).

Even \(C_c^\infty\) is a form core. For \(v\in\mathcal D\), put \(g=mv\). First cut off \(v\) by \(\chi_R\); its source becomes \(\chi_Rg\). The logarithmic norm has the equivalent difference representation with kernel \(k\), so
\[
 \|\chi_Rg-g\|_{\mathcal H_{\log}}\to0.
\]
For clarity, in the difference representation the error is the sum of a dominated term involving \((1-\chi_R(x))(g(x)-g(y))\) and a term bounded by \(C R^{-2}\|g\|_2^2\int u^2k(u)du\). The \(L^2\) error also tends to zero. For fixed \(R\), mollify the compactly supported source \(\chi_Rg\) in \(\mathcal H_{\log}\) and divide by \(m\) on the common compact support. Since \(m\) is smooth and strictly positive there, this gives compact smooth approximants to \(\chi_Rv\) in the form norm and in \(L^2\). Even cutoffs and mollifiers keep the approximants even. This proves the core assertion.

Let \(B\) denote the nonnegative self-adjoint operator associated with \(\mathfrak b\); the notation \(B=M_m b(D)M_m\) is interpreted through this form. In particular, (12) is the *form* domain, not an assertion that \(b(D)(mv)\) itself belongs to \(L^2\) for every \(v\) in it.

## 6. Exact form identity on the core and extension to the maximal domain

Take even \(q\in C_c^\infty\) and set \(F=\Phi q=mUq\). Write \(J=A+C_0I\), so (1) is its continuous jump operator. Symmetrizing the two variables in the continuous integral gives the ground-state identity
\[
 E_\Gamma(q)=\langle F,JF\rangle-
              \int\Phi(x)|q(x)|^2(J\Phi)(x)dx.                    \tag{13}
\]
For each prime shift, expanding the square and changing variables in the second diagonal term gives
\[
 E_P(q)=\int\Phi(x)|q(x)|^2(S\Phi)(x)dx-\langle F,SF\rangle.   \tag{14}
\]
These calculations are justified first with the continuous integral cut off at \(|x-y|>\delta\) and then by dominated convergence; near the diagonal the smooth difference is \(O(|x-y|)\), and the kernel is \(O(|x-y|^{-1})\). The prime sums converge locally normally as noted above.

Adding (13)--(14), using \(J=A+C_0\) so the scalar terms cancel, and then applying (2), yields
\[
 \begin{aligned}
 \mathcal E(q)
 &=\langle F,(A-S)F\rangle
   +\int\Phi(x)|q(x)|^2\{S\Phi(x)-A\Phi(x)\}dx\\
 &=\langle F,(A-S)F\rangle+\int\Phi(x)h(x)|q(x)|^2dx\\
 &=\tfrac12\|q\|_{L^2(\nu)}^2+\mathfrak b[Uq]
      -C_0\|mUq\|_2^2-\langle Uq,M_mSM_mUq\rangle.             \tag{15}
 \end{aligned}
\]
All constants follow from \(d\nu=2\Phi h\,dx\) and \(mUq=\Phi q\).

The right side of (15) is a closed, lower-bounded form on \(\mathcal D\): it is the closed nonnegative form \(\mathfrak b\) plus the bounded form \(\tfrac12I-V\), where \(V=C_0M_{m^2}+M_mSM_m\) is bounded by (10). Its form core is even \(C_c^\infty\) by Section 5. The left side is the original *maximal* jump form, closed with the same core by Section 4. Moreover, multiplication by \(\sqrt p\) maps even \(C_c^\infty\) bijectively onto even \(C_c^\infty\), since \(p\) is smooth and strictly positive. Therefore the two closed forms agree on a common core and their closures agree. This proves equality of the entire form domains, not just equality on test functions:
\[
 U\,D(\mathcal E)=\mathcal D,
 \qquad
 \mathcal E(q)=\tfrac12\|Uq\|_2^2+\mathfrak b[Uq]-\langle Uq,VUq\rangle
 \quad(q\in D(\mathcal E)).                                  \tag{16}
\]

Let \(\mathfrak h[v]=\mathfrak b[v]-\langle v,Vv\rangle\) on the form domain \(\mathcal D\), and let \(H=B-V\) be its associated operator. Equation (16) is the form identity
\[
 \mathcal E(q)=\tfrac12\|Uq\|_2^2+\mathfrak h[Uq],
 \qquad q\in D(\mathcal E).
\]
The ordinary operator inner product \(\langle Uq,(H+\tfrac12)Uq\rangle\) is an equivalent notation only when \(Uq\in D(B)=D(H)\), since \(V\) is bounded; for general \(Uq\in\mathcal D\), it is the closed-form value above that is defined.

If \(L\) is the nonnegative self-adjoint operator associated with the original maximal even jump form, (16) gives
\[
                  ULU^{-1}=\tfrac12+B-V,\qquad D(ULU^{-1})=D(B).            \tag{17}
\]
The operator-domain statement follows because \(V\) is bounded: the form sum has the same operator domain as \(B\). Equivalently, if the total form represents an \(L^2\) vector, adding back the bounded terms shows that the \(B\)-form represents an \(L^2\) vector, which is precisely membership in \(D(B)\).

## 7. The normalized ground state

Let \(g_0=U1=\sqrt p\). It has norm one because \(\int p=1\), and \(mg_0=\Phi\). The source identity gives, pointwise,
\[
 (A-S)\Phi=-h.
\]
Since \(mh=g_0/2\), the operator in (17) satisfies
\[
 (B-V)g_0=M_m(A-S)\Phi=-mh=-\tfrac12g_0,
 \qquad (ULU^{-1})g_0=0.                                     \tag{18}
\]
This is an operator identity: \(\Phi\in\mathcal S\) implies \(b(D)\Phi\in L^2\), so \(g_0\in D(B)\); the weighted prime sum is bounded by (10), and (2) makes its value on \(\Phi\) well-defined after multiplication by \(m\). Finally, \(E(q)=0\) forces the continuous positive jump integrand to vanish for almost every pair, so \(q\) is constant. Thus the zero direction is exactly the original constant, and \(\langle Uq,g_0\rangle=\int q\,d\nu\).

The formulae above concern the complete even form domain and the original full prime-power sum. They establish the unconditional foundation used by the positive-depth gap certificate; they do not prove the critical half-gap or RH.

Independent analytic verification is [REFEREE_ORIGINAL_FORM_CONTOUR.md](REFEREE_ORIGINAL_FORM_CONTOUR.md); the complete-domain verification is [REFEREE_ORIGINAL_FORM_DOMAIN.md](REFEREE_ORIGINAL_FORM_DOMAIN.md). The full-operator interval certificate using this realization is [CERTIFIED_GAP.md](CERTIFIED_GAP.md). The present result establishes its exact operator and domain inputs; the critical half-gap remains a separate mathematical target.
