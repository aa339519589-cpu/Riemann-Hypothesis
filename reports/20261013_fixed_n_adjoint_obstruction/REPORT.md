# A conditional obstruction to a fixed-truncation adjoint scheme

## Result and scope

Assume that the original full-Gamma, all-prime even operator has a lowest negative eigenvalue on the orthogonal complement of its known ground vector. For the Gaussian arithmetic adjoint construction defined below, freeze

\[
N(U)=\lfloor e^{bU}\rfloor,\quad b>1,\qquad
A(U)=\tfrac12\log(2+U)+C.
\]

Here \(C\) is a sufficiently large fixed constant, chosen after \(b\), an absolute convergence line, and a fixed error margin.

The complete localized adjoint deficit is positive on an unbounded sequence of observation endpoints and exceeds the actual Gaussian observation energy by an exponential factor. In particular, this construction cannot supply the proposed negative leading-order upper bound for that deficit. The proof retains the full Gamma operator, every prime power, the cutoff ground term, and the actual mixed pairing.

A separate ingredient is an interval-averaged coercivity theorem for genuine mean-periodic translation columns. Its constant is uniform over their coefficients and over the arithmetic truncation length.

These are conditional statements about this specific proposed proof method. They neither prove RH nor disprove the original coefficient-one comparison or the original signed-energy target. The arithmetic observable here has a rational-zeta denominator and is explicitly defined as an auxiliary observable; no identification with the older physical Dedekind-zeta signal is made.

## 1. Original operator and contradiction source

All inner products are conjugate-linear in their first variable. Use the original even Hilbert space, and set

\[
h_0(x)=\cosh(x/2),\quad m(x)^2=\frac{\Phi(x)}{2h_0(x)},\quad
 e_0=2mh_0,\quad\|e_0\|=1.
\]

Here \(\Phi\) is the complete even Riemann theta kernel, normalized by
\(\widehat\Phi(z)=\Xi(z)=\xi(1/2+iz)\), with Fourier kernel \(e^{-izx}\). The original source operator and physical operator are

\[
Lf=a(D)f-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 [f(x+\log n)+f(x-\log n)],\qquad H=mLm,
\]
\[
a(t)=\Re\psi(1/4+it/2)-\log\pi.
\]

Thus the constant part of the Gamma symbol is included in \(a\). We use the original selfadjoint realization, not an unweighted operator on the source ratio. The established identities are

\[
He_0=-e_0/2,\qquad L\Phi=-h_0.
\]

Suppose that \(-\kappa<0\) is the bottom eigenvalue of \(H\) on \(e_0^\perp\), and choose a real even unit eigenvector \(v\) there. Write

\[
f=mv=m^2r,\qquad r=v/m,\qquad Lf=-\kappa r,
\quad B(s)=\int_{\mathbb R}f(x)e^{-(s-1/2)x}\,dx.
\tag{1}
\]

We use the original negative-state regularity: \(r\) and its fixed derivatives have at most exponential growth, \(|r(x)|\le C e^{|x|/2}\), \(\Phi*r=0\), and the source and its fixed derivatives have theta tails. In particular \(B\) is entire and bounded on each fixed vertical strip. The complete explicit formula and \(\langle v,Hv\rangle<0\) imply that some right Riemann zero

\[
\rho=1/2+a+i\gamma,\qquad a>0,
\tag{2}
\]

has \(B(\rho)\ne0\). Indeed, if all off-line evaluations vanished, the absolutely convergent zero form would consist only of nonnegative critical-line terms. Reality and evenness place a nonzero off-line evaluation at a right zero. Fix such a \(\rho\), and fix \(0<d<a\).

Put

\[
E=\ker(H+\kappa)\cap e_0^\perp,\qquad
Q=H+\kappa-(\kappa-1/2)\Pi_{e_0}.
\tag{3}
\]

The compact negative spectral part of the original operator gives finite-dimensional \(E\), nonnegative \(Q\), and a positive spectral gap \(g\) off \(\operatorname{span}(e_0)\oplus E\):

\[
Q[t]\ge g\|(1-\Pi_{e_0}-\Pi_E)t\|^2.
\tag{4}
\]

All constants below may depend on this fixed hypothetical state and operator. No uniformity as \(\kappa\downarrow0\) is claimed.

## 2. Genuine division columns, including multiple complex zeros

For a zero \(z\) of \(\Xi\) of multiplicity \(j\), define

\[
c_z=\frac{j!(2z)^j}{(z^2+1/4)\Xi^{(j)}(z)},\qquad
W_z(t)=c_z\frac{(t^2+1/4)\Xi(t)}{(t^2-z^2)^j}.
\tag{5}
\]

This even entire transform is one at \(\pm z\), zero at every other distinct zero pair, and zero at \(\pm i/2\). Here neither \(z=0\) nor \(z^2+1/4=0\) is a zero case.

For clarity, the original-domain extension to complex zeros and multiplicities is explicit. Start with \(u_0=\Phi\) and, on \(x\ge0\), set

\[
u_k(x)=z^{-1}\int_x^\infty\sin(z(y-x))u_{k-1}(y)\,dy,
\quad 1\le k\le j.
\]

The preceding transform still vanishes at \(z\) when \(k\le j\), so \(u_k'(0)=0\). The equation \(u_k''+z^2u_k=u_{k-1}\) gives a smooth even extension, with transform \((-1)^k\Xi(t)/(t^2-z^2)^k\). All fixed derivatives retain bounds of the form
\(C\exp(C|x|-\pi e^{2|x|})\). Hence

\[
f_z=c_z(-1)^j(-\partial_x^2+1/4)u_j,\qquad w_z=f_z/m
\]

belongs to the original physical operator domain. The source is in \(H^2\) with the necessary weighted derivative bounds, division by \(m\) remains square-integrable, and the complete bounded physical prime operator is retained. The full explicit formula yields

\[
Hw_z=2j\psi_z,\qquad \psi_z=m\cos(zx).
\tag{6}
\]

Only the two zero evaluations \(\pm z\) survive. This construction does not differentiate an identity off the zero set.

### Pure-mode exclusion

No nonzero vector in \(E\) is of the form \(m C\cos(zx)\). Mean-periodicity first forces \(\Xi(z)=0\). The exact Hermitian pairing is

\[
\langle w_z,\psi_z\rangle=\overline{W_z(\bar z)}
 =\begin{cases}0,&\bar z\notin\{z,-z\},\\1,&\bar z\in\{z,-z\}.
 \end{cases}
\]

If \(H\psi_z=-\kappa\psi_z\), selfadjointness and (6) would give

\[
2j\|\psi_z\|^2=-\kappa\langle w_z,\psi_z\rangle,
\]

impossible in either case. This statement concerns pure modes in the actual fixed negative eigenspace. It is not a finite-spectral-support assumption on an arbitrary negative state.

## 3. Interval-averaged coercivity for complete columns

Call a smooth scalar function \(h\) admissible if its fixed derivatives have at most exponential growth and \(\Phi*h=0\). Set

\[
T_h(c,x)=\frac{m(x)}2[h(c+x)+h(c-x)].
\tag{7}
\]

Each column is even, lies in the original domain, and satisfies

\[
\langle e_0,T_h(c)\rangle=0,\qquad
\partial_c^2T_h=\mathcal D T_h,\quad
\mathcal D=m\partial_x^2m^{-1}.
\tag{8}
\]

**Lemma.** For every compact interval \(I\) of positive length, a constant \(\delta_I>0\), independent of \(h\), satisfies

\[
\int_I Q[T_h(c)]\,dc\ge\delta_I\int_I\|T_h(c)\|^2\,dc.
\tag{9}
\]

**Proof.** Otherwise take normalized columns with total squared norm one and total \(Q\)-energy tending to zero. With an orthonormal basis \(v_1,\ldots,v_k\) of \(E\), write
\(T_n=\sum_j a_{nj}(c)v_j+Z_n\). Equation (4) gives \(Z_n\to0\) in \(L^2(I;L^2)\).

For these fixed eigenvectors, the original theta bounds give

\[
\mathcal Dv_j=m(v_j/m)''\in L^2,\qquad
\mathcal D^*v_j=(mv_j)''/m\in L^2.
\]

The exact wave equation and integration by parts therefore imply
\(a_n''=A a_n+g_n\), where
\(A_{ij}=\langle\mathcal D^*v_i,v_j\rangle\) is fixed and
\(\|g_n\|_{L^2}\le C\|Z_n\|_{L^2}\to0\). Boundary terms in the source variable vanish by the theta and exponential bounds. Consequently \(a_n\) and \(a_n''\) are uniformly bounded in \(L^2(I)\).

This controls the whole closed interval: if \(a''=F\), subtract
\(\int_{c_0}^c(c-t)F(t)\,dt\). The remaining function is affine, and its two coefficients are controlled by its \(L^2(I)\) norm. Thus
\(\|a\|_{H^2(I)}\le C_I(\|a\|_2+\|a''\|_2)\), with no endpoint conditions. Compact embedding gives a nonzero strong limit \(T(c)\in E\), of total norm one. The wave equation passes in distributions; the coefficient ODE gives a smooth representative.

The finite-dimensional nonzero space \(V=\operatorname{span}\{T(c):c\in I\}\) is \(\mathcal D\)-invariant, since its curve derivatives remain in \(V\). An eigenvector of \(\mathcal D|_V\) has \(v=mr\) with \(r''=\lambda r\). Evenness forces \(r=C\cos(zx)\). This contradicts the pure-mode exclusion above. No commutation of \(\Pi_E\) with \(\mathcal D\) has been assumed. ∎

The same lemma applies to arbitrary fixed complex linear combinations of admissible functions, and hence to their integrated Gram matrices on a common interval. It gives no pointwise-in-center Gram inequality or inequality with center-dependent coefficients.

Translation of the center does not change \(\delta_{[0,1]}\). Cover \([0,U]\), \(U\ge1\), by unit intervals and the final interval \([U-1,U]\), with overlap at most two. Since \(e^{-2dc}\) varies by at most \(e^{2d}\) on one interval, (9) gives

\[
\int_0^U e^{-2dc}Q[T_h(c)]\,dc\ge\delta_d
 \int_0^U e^{-2dc}\|T_h(c)\|^2\,dc,
\quad\delta_d=\tfrac12e^{-2d}\delta_{[0,1]}>0.
\tag{10}
\]

## 4. Exact auxiliary multiplier and finite columns

Retain the fixed half-damped Euler factor from the original project. For each prime ideal \(\mathfrak p\notin S\), put
\(P=N\mathfrak p\), \(d_P=P^{-s}\), and
\(r_P=\kappa_6(\mathfrak p)P^{2-6s}\), where \(|\kappa_6(\mathfrak p)|=1\) is the original angular character. Define

\[
\mathcal H(s)=\prod_{\mathfrak p\notin S}
 \frac{1-P^{-2}}{1-r_P}
 \left(1+\frac{d_P-r_P}{P(1-d_P)}\right).
\tag{11}
\]

The fixed data \(S,\kappa_6\) are unchanged. This is \(H_{\mathrm{half},S}\) of [the half-damped probe, §3](../20261011_qrh_selection_bridge/HALF_DAMPED_PROBE.md). It is holomorphic and nowhere zero for \(\Re s>1/2\); both it and its reciprocal are bounded on every buffered half-plane \(\Re s\ge1/2+\epsilon\). Indeed the local numerator is
\(P-(P-1)d_P-r_P\), and
\(|(P-1)d_P+r_P|<(P-1)/\sqrt P+P^{-1}<P\).
The nonconstant absolute local coefficient sum on such a half-plane is
\(O_\epsilon(P^{-1-\Re s}+P^{2-6\Re s})\), summable over prime ideals. Grouping by integer norm gives an absolutely convergent ordinary Dirichlet expansion of \(\mathcal H\). Multiplying it by the rational Möbius expansion of \(1/\zeta_{\mathbb R}\) defines

\[
\frac{\mathcal H(s)}{\zeta_{\mathbb R}(s)}=
\sum_{n\ge1}a(n)n^{-s},\qquad
\sum_{n\ge1}|a(n)|n^{-\sigma}<\infty\quad(\sigma>1).
\tag{12}
\]

These \(a(n)\) are the actual coefficients of (12), not their absolute values and not the ideal Möbius coefficients of a Dedekind reciprocal.

Define the Gaussian and the auxiliary observation

\[
\ell(x)=\frac1{2\sqrt\pi}e^{x/3-x^2/4},\qquad
G(c)=\frac1{2\pi i}\int_{(\sigma>1)}e^{(s-1/2)c}
 e^{(s-5/6)^2}\frac{\mathcal H(s)B(s)}{\zeta_{\mathbb R}(s)}\,ds.
\tag{13}
\]

The exact bilateral transform of \(\ell\) is
\(\int\ell(x)e^{-zx}dx=e^{(z-1/3)^2}\); no Gaussian scalar is omitted. Let \(A_N\) be convolution by
\(\sum_{n\le N}a(n)n^{-1/2}\ell(x-\log n)\), and put

\[
F_{N,c}(x)=\tfrac12[(A_Nf)(c+x)+(A_Nf)(c-x)],
\quad
R_{N,c}(x)=\tfrac12[(A_Nr)(c+x)+(A_Nr)(c-x)].
\tag{14}
\]

At finite \(N\), all source operations are legitimate and
\(LF_{N,c}=-\kappa R_{N,c}\). Also \(mR_{N,c}\) is an admissible column in §3: Gaussian convolution preserves \(\Phi*r=0\), with absolute Fubini supplied by the theta tails and the exponential bound. Its uncut ground overlap is exactly zero.

## 5. The actual localized deficit

Choose real even \(0\le\chi_A\le1\), equal to one on \([-A,A]\), zero off \([-A-1,A+1]\), with fixed-order derivatives bounded independently of \(A\). Write \(w(c)=e^{-2dc}\). Define

\[
\begin{split}
\mathcal J(U)=\int_0^U w(c)\{&Q[m\chi_A R_{N,c}]\\
 &-\kappa\Re\langle\chi_A F_{N,c},\chi_A R_{N,c}\rangle\}\,dc.
\end{split}
\tag{15}
\]

This is the complete joint deficit, rather than an upper bound obtained by separating absolute norms. To identify the retained terms, put \(P=\chi F\), \(S=\chi R\), \(K_\chi=m^2S\), \(\Delta=P-K_\chi\), \(C_\chi=[L,\chi]F\), \(\tau=\langle e_0,mS\rangle\), and \(W[u]=\langle u,Lu\rangle\). Direct expansion using \(LP=-\kappa S+C_\chi\) gives

\[
W[\Delta]-\Re\langle P-2K_\chi,C_\chi\rangle
 -(\kappa-1/2)|\tau|^2
 =Q[mS]+\kappa\|mS\|^2-\kappa\Re\langle P,S\rangle.
\tag{16}
\]

Thus (15) is exactly the left side of (16), less \(\kappa\|mS\|^2\), integrated in \(c\). The cutoff ground correction is included in \(Q\).

All adjoint averages here start at \(c=0\). Finite \(N\) does not justify splitting these terms over \(c\to-\infty\) with the growing weight, even though \(G\) itself has a rapidly decaying left tail.

Set \(F_c(x)=[G(c+x)+G(c-x)]/2\), and define the true observation budget

\[
\mathcal E(U,A)=\int_{-\infty}^U w(c)\|\chi_A F_c\|_2^2\,dc.
\tag{17}
\]

## 6. Signed arithmetic lower bound for physical adjoint mass

Let
\(\alpha_0=\sup\{\Re\sigma-1/2:\zeta_{\mathbb R}(\sigma)=0,\ \Re\sigma>1/2\}\).
Under (2), \(0<\alpha_0\le1/2\). Define the signed sums
\(S_s(N)=\sum_{n\le N}a(n)n^{-s}\).

If \(S_{1-\rho}(N)=O(N^p)\), Abel summation makes
\(\mathcal H(s)/\zeta_{\mathbb R}(s)\) holomorphic on
\(\Re s>\Re(1-\rho)+p\), by continuation from the absolute half-plane. Every right zeta zero remains a nonzero pole by (11). Consequently

\[
\limsup_{N\to\infty}\frac{\log|S_{1-\rho}(N)|}{\log N}
 \ge\alpha_0+a.
\tag{18}
\]

No maximum at the abscissa \(\alpha_0\) and no visibility of the other zeros are required. For each \(\eta>0\), arbitrarily large integers \(N\) satisfy
\(|S_{1-\rho}(N)|\ge N^{\alpha_0+a-\eta}\).

Use (5) at \(z=-i(\rho-1/2)\). Commuting the full source operator through the convolution of the theta-decaying sources \(f_z,f\) gives

\[
f_z*r=-\frac{2j_z}{\kappa}B(\rho)\cos(zx).
\tag{19}
\]

Every prime exchange is absolute: the convolution of the two source envelopes has decay \(\exp(-c e^{|x|})\), sufficient for the complete prime sum. The Gamma convolution passage follows on the weighted smooth sources. Therefore

\[
(f_z*R_{N,c})(0)=-\frac{j_z B(\rho)}\kappa
 [\widehat\ell(z)S_\rho(N)e^{izc}
  +\widehat\ell(-z)S_{1-\rho}(N)e^{-izc}].
\tag{20}
\]

Both Gaussian factors are nonzero. The exponentials have a positive-definite two-dimensional Gram matrix on every fixed nondegenerate center interval \([0,C]\). On the other hand,
\(|(f_z*R_{N,c})(0)|\le\|f_z/m\|_2\|mR_{N,c}\|_2\).
Hence

\[
\int_0^C\|mR_{N,c}\|_2^2dc\ge c_{\rho,C}
 (|S_\rho(N)|^2+|S_{1-\rho}(N)|^2).
\tag{21}
\]

For \(N(U)=\lfloor e^{bU}\rfloor\), let

\[
\mathcal M(U)=\int_0^U w(c)\|mR_{N(U),c}\|_2^2dc.
\]

Equations (18)–(21), using \(U=\log(N+1/2)/b\), give an unbounded sequence with

\[
\mathcal M(U)\ge c_\eta e^{2b(\alpha_0+a-\eta)U}.
\tag{22}
\]

The fixed early-center interval supplies only this lower bound for the full mass. No claim that it contains all of that mass is used.

## 7. Upper bound for the actual observation

Move the contour in (13) to \(\Re s=1/2+\alpha_0+\epsilon\), which lies a fixed distance to the right of every zeta zero. The Hadamard product for \(\xi\) and \(N(T)=O(T\log(2+T))\) give the sufficient coarse bound
\(|1/\zeta(s)|\le\exp(O_\epsilon(|\Im s|\log^2(2+|\Im s|)))\)
in the fixed contour strip. The Gaussian dominates it and the horizontal tails. The boundedness of \(\mathcal H\) and \(B\) there gives

\[
|G(c)|\le C_\epsilon e^{(\alpha_0+\epsilon)c}\quad(c\ge0).
\tag{23}
\]

For \(c<0\), the original absolute Dirichlet expansion and the Gaussian convolution of \(f\) give a Gaussian left tail. More explicitly, with \(L=A+1\) and \(E_G(t)=\int_{-\infty}^t e^{-2dc}|G(c)|^2dc\), the two changes of variable \(c\mapsto c\pm x\) and \(|(z_1+z_2)/2|^2\le(|z_1|^2+|z_2|^2)/2\) give

\[
\mathcal E(U,A)\le 2L e^{2dL}E_G(U+L).
\]

Thus, for \(A=O(\log U)\), both shifted windows and the entire negative-center part in (17) satisfy

\[
\mathcal E(U,A)\le
 \exp\{2(\alpha_0+\epsilon-d)U+o(U)\}.
\tag{24}
\]

This is the unweighted-in-source observation energy (17), not an energy with the exponentially costly factor \(m^{-2}\) at its window edge.

## 8. Same-truncation domain and tail bounds

Fix an absolute convergence line \(\sigma>1\). With \(a_r=1/2\), every fixed source derivative obeys, uniformly for \(0\le c\le U\),

\[
|R_{N,c}^{(j)}(x)|\le C_j B_U e^{a_r|x|},\qquad
 B_U=e^{a_rU}N^{\sigma+a_r-1/2}.
\tag{25}
\]

This uses the fixed finite sum \(\sum|a(n)|n^{-\sigma}\), not a cancellation estimate. The original theta envelopes imply, for \(t=mR_{N,c}\), \(u=(1-\chi_A)t\),

\[
\|u\|_2+\|mu\|_{H^1}\le C B_Ue^{-c_1e^{2A}},\qquad
\|t\|_2+\|mt\|_{H^1}\le C B_U.
\]

The complete form is bounded by
\(|Q[t,u]|\le C(\|mt\|_{H^1}\|mu\|_{H^1}+\|t\|_2\|u\|_2)\).
This follows from the logarithmic Gamma upper bound and the full bounded physical potential, including all prime powers. Thus the error costs \(B_U^2\), not \(B_U\). For each desired \(M>0\), choose the constant \(C=C_M\) in
\(A=\frac12\log(2+U)+C_M\) sufficiently large. Then

\[
|Q[m\chi_A R_{N,c}]-Q[mR_{N,c}]|+|\langle e_0,m\chi_A R_{N,c}\rangle|^2
 \le e^{-MU}
\tag{26}
\]

uniformly in the center. This also controls the cutoff mass difference. The ground estimate uses the exactly zero uncut overlap.

Finally, \(\ell*f\) and each fixed derivative have Gaussian tails with any fixed exponent below \(1/4\). Since
\(\log N-(U+A)=(b-1)U-O(\log U)\), for \(b>1\) the same absolute coefficient sum gives

\[
\|F_{N,c}-F_c\|_{C^j(|x|\le A+1)}\le C_j e^{-c_bU^2}.
\tag{27}
\]

This approximation concerns \(F\) alone; it does not assert convergence of \(R_{N,c}\).

## 9. A subexponential bound for the actual mixed window

The needed relative window estimate avoids an \(m^{-1}\) edge bound. The exact entire Gaussian identity is
\(|\ell(u+iv-y)|=e^{v^2/4}\ell(u-y)\). Equations (12) and (1) give

\[
|A_Nr(u+iv)|\le C_\sigma e^{v^2/4+a_r|u|}
 N^{\sigma+a_r-1/2}.
\]

For \(0\le c\le U\), \(|z|\le\sqrt U\), this bounds \(|R_{N,c}(z)|\) by
\(C\exp(C_0U+a_r\sqrt U)\), with a fixed \(C_0\).
Let \(L=A+1=O(\log U)\), and truncate the Taylor series at degree
\(p=\lceil C_M' U/\log U\rceil\). Cauchy's estimate on \(|z|=\sqrt U\) bounds its remainder on \([-L,L]\) by

\[
C e^{C_0U+a_r\sqrt U}
 \frac{(L/\sqrt U)^{p+1}}{1-L/\sqrt U}.
\]

Choosing \(C_M'\) large makes this at most \(e^{-MU}\). For a polynomial of degree \(p\), its Legendre expansion on \([-1,1]\) gives

\[
\|P\|_{L^2[-L,L]}\le\operatorname{poly}(p,L)(2L+1)^p
 \|P\|_{L^2[-1,1]}.
\]

The logarithm of this extension price is
\(O(U\log\log U/\log U)=o(U)\). Increase the initial remainder margin before this extension. Since \(m\) has a positive lower bound on \([-1,1]\),

\[
\|\chi_A R_{N,c}\|_2\le e^{o(U)}\|mR_{N,c}\|_2+e^{-MU},
\tag{28}
\]

uniformly for the same \(N,c,U\). This estimate uses the entire Gaussian family. It is not an inequality for arbitrary mean-periodic sources with those constants.

Combining (28), Cauchy in source and center, and (27), with sufficiently large error margins, yields

\[
\left|\int_0^U w(c)\Re\langle\chi_A F_{N,c},\chi_A R_{N,c}\rangle dc\right|
\le e^{o(U)}\sqrt{\mathcal E(U,A)\mathcal M(U)}+e^{-MU}.
\tag{29}
\]

The crude exponential mass bound from (25) makes the Gaussian approximation error in (27) negligible even in this mixed product.

## 10. Complete lower bound and the obstruction

Use (10) on the entire center interval, then (26) and (29). Young's inequality gives

\[
\boxed{\displaystyle
\mathcal J(U)\ge\frac{\delta_d}{2}\mathcal M(U)
 -e^{o(U)}\mathcal E(U,A)-e^{-MU}.}
\tag{30}
\]

For any fixed \(b>1\), choose \(\eta,\epsilon>0\) sufficiently small that

\[
b(\alpha_0+a-\eta)>\alpha_0+\epsilon-d.
\]

Equations (22) and (24) then show that on an unbounded sequence
\(\mathcal M/\mathcal E\) grows exponentially. In particular, for some \(c_*>0\), along that sequence and for large endpoints,

\[
\mathcal J(U)>0,\qquad
\mathcal J(U)\ge e^{c_*U}\mathcal E(U,A).
\tag{31}
\]

Thus \(\mathcal J\) cannot have a negative leading-order upper bound, or even an \(e^{o(U)}\mathcal E\) upper budget, for this regularization. This is a signed lower-bound obstruction for the actual retained expression, not a conclusion drawn from an overly large absolute upper estimate.

The assumptions and boundaries are essential: the lowest negative state is hypothetical; \(N=e^{bU}\) with fixed \(b>1\) is frozen over the whole center interval; the source cutoff has the stated logarithmic size with a sufficiently large fixed constant; the multiplier is (11)–(13); and all comparisons use the same finite \(N\). Center-dependent truncations or other regularizations introduce different terms and are not covered by this theorem. The original coefficient-one form comparison and signed arithmetic upper bound remain open.

## Original-source references

- [Complete theta normalization and original maximal form domain](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md).
- [Half-damped Euler multiplier and its full half-plane nonvanishing](../20261011_qrh_selection_bridge/HALF_DAMPED_PROBE.md), §3, equations (4)–(6).
- [Original-domain division and full explicit formula](../20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md), Appendices C–D. Section 2 above supplies the repeated complex-zero division extension used here.
- [Original negative-band coverage](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md) and [negative-state Gamma-tail regularity](../20261012_adaptive_spectral_tail/EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md). All operator statements here retain their full physical realization.
