# Odd Green variation and the complete reflected-prime boundary

For a hypothetical largest supercritical Green eigenvalue, this note gives
an exact necessary convolution inequality in the original source domain.
Every reflected-prime commutator reduces to an explicit pairing between a
short interval at zero and intervals around the true prime-power logarithms.
The complete pairing has a bound linear in the convolution support radius,
after multiplication by the supercritical depth. Its sign is not determined.

The [fractional origin follow-up](../20261013_supercritical_source_tails/FRACTIONAL_ORIGIN_BOUNDARY.md)
improves this absolute bound to every fixed power \(a^{1+\theta}\),
\(0<\theta<1/8\), with the same depth uniformity.

We also construct an exactly pole-centered compact core source for which the
same covariance defect is negative. This shows that its required positivity
is not automatic on the core. **That source is not a Green eigen-source;
the construction neither gives a negative Weil test nor excludes an actual
eigenvalue. RH remains unproved.**

## 1. Actual source and legal convolution tests

Use [the full-prime forms](REPORT.md), the
[actual source-tail theorem](../20261013_supercritical_source_tails/REPORT.md),
and the [origin graph-domain theorem](../20261013_supercritical_source_tails/ORIGIN_GRAPH_DOMAIN.md).
Write \(d_n=\log n\), \(\alpha_n=\Lambda(n)/\sqrt n\),
\[
\psi=-\Phi'>0,\quad
L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x),\quad
V=L/\psi,\quad\mu^2=1/V.
\]
In this note \(N(f,g)\) abbreviates the original ratio form
\(N(f/\psi,g/\psi)\), with no change of normalization. On its core,
\[
N(f,g)=2\int_0^\infty V\overline f g
-2\sum_n\alpha_n\int_0^{d_n}\overline{f(x)}g(d_n-x)\,dx.   \tag{1}
\]
Let \(\lambda=\|T\|^2>1\) be the largest Green eigenvalue and choose a
corresponding real source \(g=\psi r\), with \(\int_0^\infty\sinh(x/2)g(x)dx=0\).
The [compact positive-excess theorem](../20261013_compact_green_excess/REPORT.md)
ensures that such a largest eigenvalue exists if there is any supercritical
spectrum. Put \(\delta=1-1/\lambda\) and \(P_0=P[r]\). Then
\[
Q_\delta=P-(1-\delta)N\succeq0,\qquad
h(g,z)=-\delta N(g,z),\qquad h=P-N.                       \tag{2}
\]
The nonnegativity uses the largest eigenvalue, not an arbitrary member of
the supercritical spectrum.

Fix a real even \(k\in C_c^\infty((-1,1))\), and set
\(k_a(t)=a^{-1}k(t/a)\). Let \(C_a\) be convolution on odd extensions.
For all sufficiently small \(a>0\), both \(C_ag/\psi\) and
\(C_a^2g/\psi\) lie in the actual \(P\)-completion and are pole-centered.
This domain statement allows signed kernels. Here are the needed details.

The published actual-source bound, with \(v=g/\mu\), is
\(\int_X^\infty |v|^2\le C_\delta\exp(9X-\pi e^{2X})\).
Convolution against \(|k_a|\), Cauchy--Schwarz, and the theta estimate
\[
\mu(y)^2/\mu(x)^2\le C_a\exp(Ca e^{2(y+a)})
\quad (|x-y|\le a,\ x,y\text{ sufficiently large})
\]
show that \(C_ag/\mu\) has a double-exponential squared tail when \(a\)
is below one fixed constant. Taking \(2a\) below that constant treats
\(k_a*k_a\) as well. Since \(\mu^2/m^2\le Ce^{3x}\), both physical
quotients by \(m\) are in \(L^2\). Both smoothed sources are odd and
\(H^1\), with a smooth \(O(x)\) zero at the origin; division by \(\psi\)
there gives a smooth even ratio. Spatial cutoffs of these ratios are core
vectors. They converge in normalized \(L^2(dx/\mu^2)\), physical
\(L^2(dx/m^2)\), and source \(H^1\). The first controls \(N\), the last
two control the complete source form \(h\). The identity \(P=N+h\) on
the core therefore makes the cutoffs \(P\)-Cauchy and identifies their
limits with these sources. This is the closure argument in
[source smoothing, §§6–7](../20261013_supercritical_source_tails/SOURCE_SMOOTHING.md),
with absolute-kernel Cauchy--Schwarz replacing the positivity of its kernel.

The pole moment is multiplied by \(\int k_a(t)\cosh(t/2)dt\), so remains
zero. The full Gamma multiplier, mass term, and each original prime shift
commute with real even convolution in their pairings. The complete prime
series passes through this identity: the physical source norms and the
complete theta-weighted prime bound make its absolute correlation sum
finite. Thus
\[
h[C_ag]=\operatorname{Re}h(g,C_a^2g).
\]
Testing (2) by the legal \(C_a^2g\) yields the exact necessary inequality
\[
\boxed{\quad
Q_\delta[C_ag]
=\delta\{N[C_ag]-\operatorname{Re}N(g,C_a^2g)\}\ge0.
\quad}                                                   \tag{3}
\]
No derivative or point trace of the unsmoothed actual source is assumed.

## 2. Exact triangular boundary pairing for all prime powers

The positive-half-line kernel of \(C=C_a\) is
\(K_a(x,y)=k_a(x-y)-k_a(x+y)\). Define
\[
(R_df)(x)=\mathbf1_{0<x<d}f(d-x),\qquad
D_V=\int V|Cg|^2-\operatorname{Re}\int V\overline g\,C^2g,
\]
\[
D_d=\operatorname{Re}\langle Cg,[R_d,C]g\rangle,
\qquad D_{\rm pr}=\sum_n\alpha_nD_{d_n}.
\]
Equation (1) gives
\[
N[Cg]-\operatorname{Re}N(g,C^2g)=2(D_V-D_{\rm pr}).         \tag{4}
\]
For the potential term, keep the two displayed weighted pairings grouped;
one can first replace \(V\) by \(\min(V,M)\) and then pass to the limit
by weighted Cauchy--Schwarz. Separate fixed-shift integrals can diverge at
zero because \(V(x)=c/x+O(1)\). The odd kernel cancellation must precede
that limit.

The single-reflection commutator kernel is exactly
\[
[R_d,C](x,y)=\mathbf1_{x<d}K_a(d-x,y)
             -\mathbf1_{y<d}K_a(x,d-y).                  \tag{5}
\]
For \(a<d/4\), it vanishes outside the corner near \((0,d)\) and its
transpose. At the first corner, \(0<x<a\), \(|t|<a-x\),
\[
[R_d,C](x,d+t)=k_a(x+|t|),
\quad [R_d,C](d+t,x)=-k_a(x+|t|).
\]
Consequently
\[
D_d=\int_0^a dx\int_0^{a-x}dt\,k_a(x+t)
\operatorname{Re}\left\{
\overline{Cg(x)}[g(d+t)+g(d-t)]
-[\overline{Cg(d+t)}+\overline{Cg(d-t)}]g(x)\right\}.       \tag{6}
\]
Both sides of each prime boundary are present; there is no extra factor two.

Let \(\epsilon>0\) be the fixed origin interval in the graph-domain theorem
and choose \(4a<\min(\epsilon,\log2)\). The complete translated load
\[
\mathcal F_g(t)=\sum_n\alpha_n[g(d_n+t)+g(d_n-t)]
\]
belongs to \(L^2(0,2a)\) by that theorem, equation (11). Extend it evenly
to \((-2a,2a)\). Evenness of \(k_a\) and local \(L^2\) convergence of
the full prime sum give
\(\mathcal F_{Cg}(t)=(k_a*\mathcal F_g)(t)\) for \(0<t<a\).
Summing (6) therefore gives the full signed boundary formula
\[
\boxed{\quad
D_{\rm pr}=\int_{x,t>0,\ x+t<a}k_a(x+t)
\operatorname{Re}\left\{
\overline{Cg(x)}\mathcal F_g(t)
-\overline{(k_a*\mathcal F_g)(t)}g(x)\right\}dx\,dt .
\quad}                                                   \tag{7}
\]
This uses local averages, not endpoint sampling. All labels in the original
Mangoldt sum are retained.

## 3. A depth-uniform bound for the complete boundary term

The origin theorem, equations (11) and (17), gives fixed constants such that
\[
A_g:=\|g/x\|_{L^2(0,2a)}\le C\delta^{-1}\sqrt{P_0},\qquad
B_g:=\|\mathcal F_g\|_{L^2(0,2a)}\le C\sqrt{P_0}.          \tag{8}
\]
For a signed smooth profile, odd cancellation still gives
\[
\|Cg/x\|_{L^2(0,a)}\le C_k A_g.                          \tag{9}
\]
Indeed the rescaled conjugated kernel is
\(Y[k(X-Y)-k(X+Y)]/X\), \(0<X<1\), \(0<Y<2\).
Its absolute value is at most \(2Y\|k'\|_\infty\), by evenness and the
mean-value formula, hence it has a fixed Hilbert--Schmidt bound.
Young's inequality also gives
\(\|k_a*\mathcal F_g\|_{L^2(0,a)}\le\sqrt2\|k\|_1B_g\).
Use \(\|Cg\|_{L^1(0,a)}\le(a^3/3)^{1/2}C_kA_g\), the analogous
bound for \(g\), and \(\|k_a\|_\infty=a^{-1}\|k\|_\infty\) in (7).
The two terms each have absolute value at most \(C_k a A_gB_g\). Thus
\[
\boxed{\qquad \delta|D_{\rm pr}|\le C_k a P_0.\qquad}     \tag{10}
\]
The constant is independent of the source, \(a\), and \(0<\delta<1\).
This is an absolute bound. From (3) it gives only
\(\delta D_V\ge-C_k aP_0\), not a negative variation.

The actual local source equation retains a signed load:
\[
B_og+\delta Vg=C_0g+F_+-(1-\delta)F_-,\qquad
F_\pm(t)=\sum_n\alpha_n g(d_n\pm t),
\]
\[
\mathcal F_g=B_og+\delta Vg-C_0g+(2-\delta)F_-.            \tag{11}
\]
All terms are locally \(L^2\). Substitution in (7) is legal but does not
supply a sign for its two opposed terms.

## 4. Positivity of the covariance defect is not automatic on the core

Here the source is constructed independently of an eigen-equation. Choose
a real even mass-one profile \(k\in C_c^\infty((-1,1))\) with
\(\mu_2=\int t^2k(t)dt\ne0\). For a fixed compact smooth odd source \(f\),
Taylor expansion, preserving odd vanishing in its remainders, gives
\[
\int V\{(C_af)^2-f C_a^2f\}
=\frac{\mu_2^2a^4}{4}J_V(f)+O_{f,k}(a^6),\qquad
J_V(f)=\int_0^\infty V(f''^2-ff'''').                     \tag{12}
\]
The remainder is integrable at zero: it is \(O(a^6x^2)\) there, while
\(V\asymp1/x\). No integration by parts through a singular boundary is used.

For \(f_b(t)=t(1-bt^2)e^{-t^2}\), exact differentiation and Gaussian
moments give
\[
J_{1/t}(f_b)=2(b^2-b-1),\qquad J_{1/t}(f_{2/3})=-22/9.     \tag{13}
\]
The [exact rational replay](check_origin_covariance.py) checks this algebraic
coefficient, not the analytic theorem or RH.

Take a fixed nonnegative smooth even cutoff \(\chi_R(t)=\chi(t/R)\),
supported in \([-R,R]\) and equal to one on an expanding central interval.
For small \(r>0\), put
\[
b_R(r)=\frac{\int_0^\infty\sinh(rt/2)\chi_R(t)t e^{-t^2}dt}
 {\int_0^\infty\sinh(rt/2)\chi_R(t)t^3 e^{-t^2}dt},\quad
F_{R,r}=\chi_R f_{b_R(r)},\quad g_r(x)=rF_{R,r}(x/r).
\]
The denominator is positive, and \(\int_0^\infty\sinh(x/2)g_r(x)dx=0\)
exactly. For fixed \(R\), as \(r\downarrow0\),
\[
b_R(r)\longrightarrow
\frac{\int\chi_R(t)t^2e^{-t^2}dt}{\int\chi_R(t)t^4e^{-t^2}dt}
\longrightarrow\frac23\quad(R\to\infty).
\]
Gaussian tails control all cutoff derivatives through order four. Choose
\(R\) large enough that the limiting truncated functional in (13) is
negative; it stays bounded away from zero negatively as \(r\downarrow0\).
The complete row expansion \(V(x)=c/x+O(1)\), \(c=L(0)/c_\psi>0\), gives
\[
J_V(g_r)=cr^{-2}J_{1/t}(F_{R,r})+O_R(r^{-1})<0             \tag{14}
\]
for sufficiently small \(r\). The quotient \(g_r/\psi\) is a smooth compact
even core ratio, since both numerator and denominator have odd smooth
extensions and \(\psi\) has a simple zero at zero.

Fix such \(r\), then take \(a\) small enough that
\(rR+2a<\log2/2\). Every off-diagonal reflected product in
\(N[C_ag_r]\) and \(N(g_r,C_a^2g_r)\) is exactly zero by support separation.
The diagonal part remains the complete \(2\int V\overline f g\), containing
every Mangoldt label through \(L\). Hence (12)–(14) give
\[
N[C_ag_r]-\operatorname{Re}N(g_r,C_a^2g_r)
=\frac{\mu_2^2a^4}{2}J_V(g_r)+O_{g_r,k}(a^6)<0.           \tag{15}
\]

This shows that the restriction (3) on an actual largest eigen-source is
substantive. The constructed \(g_r\) does not satisfy its eigen-equation,
so (3) cannot be applied to \(g_r\). To exclude a supercritical eigenvalue
by this route one still must find a legal kernel for its **actual** source
such that \(D_V<D_{\rm pr}\), with the latter given by (7). Equations
(10), (11), and (15) do not establish that step.
