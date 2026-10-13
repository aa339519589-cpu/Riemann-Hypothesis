# Weighted logarithmic regularity and the signed zero-pair identity

## Result and scope

For an actual supercritical reflected-energy eigen-source, the published
source-tail report gives a double-exponential spatial \(L^2\) tail and an
auxiliary equation \(H_\delta v=-2\delta v\). The tail alone does not imply
any weighted logarithmic Fourier regularity. Using the equation with smooth
saturated exponential weights does give the stronger fact
\[
q_b[e^{a|x|}g_o]<\infty\qquad\text{for every fixed }a>0.
\]
This yields an entire transform \(G(z)=\widehat{g_o}(z)\) and, by local
upper sampling with the unconditional \(O(\log T)\) zero count,
\[
\sum_{z\in Z_\Xi} j_z|G(z)|^2<\infty.
\]
It is therefore possible to extend the full quadratic Weil identity to this
generalized source without placing it in the original physical operator's
operator domain. Combining that identity with the exact eigen-source
equation gives a coefficient-one signed constraint. It requires a positive
aggregate off-line zero contribution for any \(\lambda>1\) eigen-source;
the off-line summands are indefinite, so this does not itself exclude the
eigen-source or prove RH.

Use the notation and exact closed domains in the [source-tail theorem](REPORT.md), and the current in the [global convolution theorem](GLOBAL_MEAN_PERIODIC.md). Write \(T^*Tu=\lambda u\), \(\lambda>1\), \(g=\psi r\) for its centered positive-wing source, \(g_o\) for its odd extension, and \(\delta=(\lambda-1)/\lambda\). The new regularity is the logarithmic Fourier form of exponentially weighted sources; it uses the eigen-equation and is not inferred from a spatial tail alone.

## Exponentially weighted logarithmic form

Let
\[
V(x)=L(x)/\psi(x),\qquad v(x)=g(x)/\mu(x),\qquad
\mu^2=\psi/L.
\]
The published reference comparison gives \(v\in L^2(0,\infty)\), with
\(\|v\|_2^2=\int_0^\infty V|g|^2\). At the endpoints,
\(V(x)\sim L(0)/(c_\psi x)\) near zero, while the actual power
\(n=2^j\), with \(j=\lfloor x/\log2\rfloor+2\), gives
\[
L(x)\ge c e^{-x/2},\qquad
V(x)\ge c e^{-7x}e^{\pi e^{2x}}
\quad (x\text{ large}).                                      \tag{1}
\]
Thus for any fixed \(a>0\) one may choose a positive smooth even function
\(\phi_a\), constant near zero, nondecreasing in \(|x|\), and equal to
\(e^{a|x|}\) for large \(|x|\), such that
\[
\rho_a(x)=\phi_a(x)/\sqrt{V(x)}\in L^2(0,\infty).
\tag{2}
\]
Near zero \(\rho_a=O(\sqrt{x})\); at infinity it has a double-exponential
decay. No derivative of \(g\) is used.

For \(R\ge1\), saturate the weight by
\[
\phi_{a,R}=\frac{R\phi_a}{R+\phi_a},\qquad F_{a,R}=\phi_{a,R}^2.
\]
Then \(\phi_{a,R}\uparrow\phi_a\), \(\phi_{a,R}\le\phi_a\), and each
\(F_{a,R}\) is bounded, smooth, even, and Lipschitz. The test
\(F_{a,R}v\) is legal in the core closure defining the kinetic form
\(q_b[(\mu v)_o]\): on the transformed ratio core
\(v=\psi z/\mu\), it is \(\psi(F_{a,R}z)/\mu\), again in that core.
For a bounded Lipschitz multiplier \(F\), the jump representation
\[
q_b[f]=\frac12\iint_{\mathbb R^2}\kappa(|x-y|)|f(x)-f(y)|^2dxdy
\]
gives
\[
q_b[Ff]\le 2\|F\|_\infty^2q_b[f]
 +C_F\|f\|_2^2,
\quad
C_F\le C\int_0^\infty\kappa(u)
             \min\{\operatorname{Lip}(F)^2u^2,\|F\|_\infty^2\}\,du<\infty.
\tag{3}
\]
The integral is finite because \(\kappa(u)\asymp u^{-1}\) at zero and
decays exponentially at infinity. Applied to differences of core vectors,
(3) extends multiplication by \(F_{a,R}\) to the actual core closure.
The weak equation for \(H_\delta\) holds on this whole form domain: it
holds on the transformed core, the kinetic form is continuous in its core
closure, and all other terms are bounded on \(L^2\). Thus \(F_{a,R}v\)
is a legal eigen-equation test.

Write the centered weak eigen-source equation in the positive-wing source
variables as
\[
q_b[g_o,h_o]-2C_0\langle g,h\rangle+p[g,h]
 -8\overline{m(g)}m(h)+\delta\,\mathscr N[g,h]=0,
\qquad m(g)=\int_0^\infty\sinh(x/2)g(x)dx=0,
\tag{4}
\]
for core tests \(h\), where \(p\) retains all same-wing and reflected
prime-power correlations and
\[
\mathscr N[g,h]=2\int_0^\infty V(x)\overline{g(x)}h(x)dx
 -2\sum_{n\ge2}\alpha_n\int_0^{d_n}\overline{g(x)}h(d_n-x)dx.
\tag{5}
\]
The rank-one term is kept in (4) for uncentered tests; it vanishes here
because the eigen-source is centered. Since all non-kinetic terms are
bounded on the transformed \(L^2\) space, (4) extends to the closed
kinetic form domain.

Test with \(h=F_{a,R}g\). The logarithmic jump-form IMS identity is
\[
\operatorname{Re}q_b[g_o,F_{a,R}g_o]
 =q_b[\phi_{a,R}g_o]-I_{a,R}.
\tag{6}
\]
Set \(X_R^2=\int_0^\infty V\phi_{a,R}^2|g|^2\). The error in (6) is
bounded uniformly in \(R\): for \(|x|\ge|y|\), monotonicity and the
bound \(|\phi_a'|\le C_a\phi_a\) give
\[
\frac{|\phi_{a,R}(x)-\phi_{a,R}(y)|^2}
 {\phi_{a,R}(x)\sqrt{V(|x|)}}
 \le C_a\rho_a(|x|)|x-y|.
\]
For \(|x-y|\le1\) use the derivative bound; for larger separation use
\(|\phi_{a,R}(x)-\phi_{a,R}(y)|\le\phi_{a,R}(x)\). The resulting kernel
\(\rho_a(|x|)|x-y|\kappa(|x-y|)\) is Hilbert--Schmidt because both
\(\rho_a\) and \(u\kappa(u)\) are in \(L^2\). Hence
\[
|I_{a,R}|\le C_a X_R\|g\|_2.
\tag{7}
\]

The reflected cross term in (5) and every term in \(p[g,F_{a,R}g]\)
have the same bound. On a reflected edge choose its larger endpoint
\(X=\max(x,d_n-x)\ge d_n/2\); on a forward edge choose
\(X=x+d_n\). In either case the test weight at either endpoint is at
most \(\phi_{a,R}(X)^2\), and factor
\[
\phi_{a,R}(X)^2|g(X)g(Y)|
\le [\sqrt{V(X)}\phi_{a,R}(X)|g(X)|]\,[\rho_a(X)|g(Y)|].
\]
Cauchy--Schwarz on each edge and summation give
\[
|p[g,F_{a,R}g]|+|\mathscr N_{\rm cross}[g,F_{a,R}g]|
 \le C_a X_R\|g\|_2,
\tag{8}
\]
since
\(\sum_n\alpha_n\sup_{X\ge d_n/2}\rho_a(X)<\infty\) and
\(\sum_n\alpha_n\sup_{X\ge d_n}\rho_a(X)<\infty\). These are complete
Mangoldt sums; the double-exponential in (2) pays every prime power.

Finally split the mass term at a fixed large \(x_0\). On the compact part
\(\phi_{a,R}\le\phi_a\), and on the tail choose \(x_0\) so
\(2C_0\le\delta V(x)\). Then
\[
2C_0\int_0^\infty\phi_{a,R}^2|g|^2
 \le C_{a,\delta}\|g\|_2^2+\delta X_R^2.
\tag{9}
\]
Using (6)--(9) in (4), with \(m(g)=0\), yields
\[
q_b[\phi_{a,R}g_o]+\delta X_R^2
 \le C_{a,\delta}X_R\|g\|_2+C_{a,\delta}\|g\|_2^2.
\]
Young's inequality absorbs the first term, uniformly in \(R\), and gives
\[
\sup_{R\ge1}\left(q_b[\phi_{a,R}g_o]+X_R^2\right)
 \le C_{a,\delta}\|g\|_2^2.
\tag{10}
\]
The \(q_b\) term must be retained here; the earlier source-tail theorem
alone only bounded an \(L^2\) tail. As \(R\to\infty\), \(\phi_{a,R}g_o\)
converges in \(L^2\) by the \(X_R\) bound and the global lower bound \(V\ge c_*>0\) (continuity and divergence of \(V\) at both ends), so lower semicontinuity
of \(q_b\) gives \(q_b[\phi_ag_o]<\infty\). A bounded Lipschitz
multiplier transfers this to \(q_b[e^{a|x|}g_o]<\infty\). Since \(a>0\)
was arbitrary, the assertion holds for every fixed exponential weight.

## Entire transform and zero-density sampling

Define
\[
G(z)=\int_{\mathbb R}g_o(x)e^{izx}dx.
\]
The weighted \(L^2\) result for every \(a\) implies weighted \(L^1\) by
Cauchy--Schwarz, locally uniformly for every complex \(z\). Thus \(G\) is
entire. If \(|\eta|\le3/4\), then
\(G(t+i\eta)=\widehat{e^{-\eta x}g_o}(t)\). Choose any fixed \(a>3/4\).
The multiplier \(e^{-\eta x-a|x|}\) is bounded Lipschitz, uniformly in
\(|\eta|\le3/4\); (3) and (10) therefore give
\[
\sup_{|\eta|\le3/4}\left(\|e^{-\eta x}g_o\|_2^2
 +q_b[e^{-\eta x}g_o]\right)<\infty.
\]
Because \(b(t)\asymp\log(2+|t|)\) at infinity and the \(L^2\) term
controls bounded frequencies,
\[
\sup_{|\eta|\le3/4}\int_{\mathbb R}
 \log(2+|t|)|G(t+i\eta)|^2dt<\infty.
\tag{11}
\]

Every zero \(z\) of \(\Xi\) lies in \(|\operatorname{Im}z|<1/2\).
The Riemann--von Mangoldt formula with an \(O(\log T)\) remainder gives the following unit-height count, with multiplicity. A primary explicit bound is [Hasanalizade, Shen and Wong, Corollary 1.2](https://arxiv.org/pdf/2107.06506); subtracting its estimates at heights one unit apart gives this consequence:
\[
\sum_{\substack{z\in Z_\Xi\\n\le\operatorname{Re}z<n+1}}j_z
 \le C\log(2+|n|).
\tag{12}
\]
No separation of zeros is needed. Fix a disk radius \(r<1/4\). Since
\(|G|^2\) is subharmonic,
\[
|G(z)|^2\le (\pi r^2)^{-1}\int_{|w-z|<r}|G(w)|^2dA(w).
\]
For each \(w\), (12) bounds the total multiplicity of zero centers in
\(|z-w|<r\) by \(C\log(2+|\operatorname{Re}w|)\). Summing the submean
inequality and using (11) gives the local upper-sampling estimate
\[
\boxed{\quad\sum_{z\in Z_\Xi}j_z|G(z)|^2
 \le C_a\int_{|\eta|\le3/4}\int_{\mathbb R}
 \log(2+|t|)|G(t+i\eta)|^2dt\,d\eta<\infty.\quad}
\tag{13}
\]
This is a sampling bound for the generalized source \(g_o\), not the
physical eigenstate transform in the [infinite high-tail estimate](../20261013_growing_rank_source_estimates/INFINITE_HIGH_TAIL.md).

## Full Weil identity and the signed orbit constraint

For compactly supported smooth odd \(f\), apply the [full additive explicit formula](../20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md), Appendix C, equation (C4) to the autocorrelation
\(H_f=f*\widetilde f\), where
\(\widetilde f(x)=\overline{f(-x)}\). Its transform is
\[
\widehat H_f(z)=\widehat f(z)\,\overline{\widehat f(\bar z)}.
\]
The pole terms are
\(\widehat H_f(i/2)+\widehat H_f(-i/2)\). For odd \(f=g_o\), the
full-line moment is \(\int_{\mathbb R}\sinh(x/2)f(x)dx=
2\int_0^\infty\sinh(x/2)g(x)dx\), so these terms equal
\(-2|\int_{\mathbb R}\sinh(x/2)f(x)dx|^2
=-8|\int_0^\infty\sinh(x/2)g(x)dx|^2\). The gamma term is
\(q_b[f]-C_0\|f\|_{L^2(\mathbb R)}^2\), and, writing \(g=f|_{(0,\infty)}\),
the complete prime term is
\[
p[g]=-4\sum_{n\ge2}\alpha_n\operatorname{Re}
       \int_0^\infty\overline{g(x)}g(x+d_n)dx
      +2\sum_{n\ge2}\alpha_n\operatorname{Re}
       \int_0^{d_n}\overline{g(x)}g(d_n-x)dx.
\]
Thus, with exactly the
source normalization of the published identity,
\[
\mathfrak A_s[f]
 =q_b[f]-C_0\|f\|_{L^2(\mathbb R)}^2+p[g]
       -8\left|\int_0^\infty\sinh(x/2)g(x)dx\right|^2
 =\sum_{z\in Z_\Xi}j_z\,
       \widehat f(z)\overline{\widehat f(\bar z)},
\quad z=-i(\rho-1/2)\text{ for a nontrivial zero }\rho\text{ of }\zeta.
\tag{14}
\]
Here \(Z_\Xi\) is the set of distinct zeros and \(j_z\) their
multiplicities. Each occurrence in the explicit formula has coefficient
one. In particular the two
pole terms combine to the coefficient-two source rank term, with the
negative sign for odd parity.

Equation (14) extends to the present generalized \(g_o\). Choose \(a>1\)
and a smooth positive even weight \(\omega_a\asymp e^{a|x|}\). The
weighted-form result and (3) imply \(\omega_ag_o\in D(q_b)\). Since
\(C_c^\infty\) is a form core for the logarithmic jump form, approximate
\(\omega_ag_o\) in \(q_b+L^2\) by odd compact-smooth functions \(f_k\),
and set \(g_k=\omega_a^{-1}f_k\). Then \(g_k\) are odd compact-smooth and
converge to \(g_o\) in weighted \(q_b+L^2\). The gamma and pole terms in
(14) converge. For the prime terms,
\[
|H_f(d)|\le e^{-a|d|}\|e^{a|x|}f\|_2^2,
\qquad
\sum_{n\ge2}\alpha_ne^{-a d_n}
 =\sum_{n\ge2}\Lambda(n)n^{-a-1/2}<\infty,
\]
and polarization gives convergence of the complete correlations, including
every prime power. The sampling estimate (13), applied to differences,
gives convergence of the zero side in the corresponding weighted
\(\ell^2(j_z)\) norm; Cauchy--Schwarz then passes the zero products. Hence
(14) holds for \(g_o\), with an absolutely convergent zero sum, despite
the absence of any \(H^1\) or physical \(H\)-operator-domain assertion.

Finally, the actual edge divergence in the global report is normalized so
\(\mathscr N[g,h]=2\int_0^\infty\overline{W(x)}h(x)dx\) on compact
source tests. For the eigen-source, the incidence bound and the reference
weight give
\[
\int_0^\infty\frac{\psi}{L}|W|^2\le N[r],
\qquad
\int_0^\infty\frac{L}{\psi}|g|^2=\|v\|_2^2<\infty.
\]
Cauchy--Schwarz therefore gives \(\int_0^\infty|Wg|<\infty\), and the
closed edge polarization yields the absolutely defined energy pairing
\[
\int_{\mathbb R}\overline{W_o(x)}g_o(x)dx
 =2\int_0^\infty\overline{W(x)}g(x)dx=N[r].
\]
Thus the weak eigen equation is the exact distributional statement
\[
\mathcal A_s g_o=-\delta W_o,
\qquad \mathfrak A_s[g_o]=-\delta N[r].
\tag{15}
\]
Combining (14) and (15) gives the exactly normalized full-zero identity
\[
\sum_{z\in Z_\Xi}j_z G(z)\overline{G(\bar z)}
 =-\delta N[r]=-(\lambda-1)P[r].
\tag{16}
\]

Since the forms and eigen-operator are real, a nonzero real or imaginary
part of an eigenvector is a nonzero real eigenvector; take its source real.
For this real odd eigen-source, \(G(-z)=-G(z)\) and
\(\overline{G(z)}=G(-\bar z)\). Keep the Weil term in its actual form
\(G(z)\overline{G(\bar z)}\); off the real axis it is not a Hermitian
square. Group the zero multiset into the critical
orbits \(\{\pm\gamma\}\) and off-critical quartets
\(\{z,-z,\bar z,-\bar z\}\), with \(z=\gamma-i\beta\),
\(\gamma,\beta>0\), one representative per quartet. There are no zeros
with zero real part since \(\Xi(iy)=\xi(1/2-y)>0\) for \(|y|<1/2\).
Formula (16) becomes
\[
2\sum_{\substack{\gamma>0\\\Xi(\gamma)=0}}
       j_\gamma|G(\gamma)|^2
-4\sum_{\substack{z=\gamma-i\beta\in Z_\Xi\\\gamma,\beta>0}}
       j_z\operatorname{Re}\bigl(G(z)^2\bigr)
=-\delta N[r].
\tag{17}
\]
Equivalently,
\[
\boxed{\quad
4\sum_{z=\gamma-i\beta,\ \gamma,\beta>0}
       j_z\operatorname{Re}\bigl(G(z)^2\bigr)
=\delta N[r]
 +2\sum_{\substack{\gamma>0\\\Xi(\gamma)=0}}
       j_\gamma|G(\gamma)|^2>0.\quad}
\tag{18}
\]
Since \(\operatorname{Re}(G(z)^2)\le|G(z)|^2\), this also yields the
quantitative off-line sampling lower bound
\[
\boxed{\quad
\sum_{z=\gamma-i\beta,\ \gamma,\beta>0}j_z|G(z)|^2
 \ge \frac{\lambda-1}{4}P[r]
   +\frac12\sum_{\substack{\gamma>0\\\Xi(\gamma)=0}}
       j_\gamma|G(\gamma)|^2.\quad}
\tag{19}
\]
Thus any supercritical eigen-source forces nonzero off-critical zero
contribution. The explicit-formula identity has unit coefficient per zero
occurrence; this is not a coefficient-one positivity or operator comparison.
The real parts in (18) have no fixed sign term by term, and the absolute
sampling bound (13) does not supply the missing sign. No eigenvalue
exclusion or RH conclusion follows from these identities alone.
