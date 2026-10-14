# Fractional regularity of the actual normalized source at fixed depth

For a supercritical depth bounded away from zero, this note proves every
Sobolev order below \(1/2\) for the actual normalized source \(v=g/\mu\),
and consequently for \(g\). The constants may deteriorate as the depth
tends to zero. This does not replace the depth-uniform \(s<1/8\) theorem.
It supplies no endpoint trace, fixed-node translation theorem, critical
sign comparison, or RH proof.

## 1. Actual auxiliary operator and statement

Use the actual centered source and the closed auxiliary realization in
[REPORT.md](REPORT.md). Thus
\[
g=\psi r,\quad v=g/\mu,\quad \mu^2=\psi/L,\quad
\delta=1-\lambda^{-1}>0,\quad P_0=P[r],
\]
and on ordinary positive-wing \(L^2\),
\[
H_\delta v=-2\delta v,\qquad H_\delta=B_N+K_\delta,
\tag{1}
\]
\[
K_\delta=-2C_0M_{\mu^2}+P_N
 -8|e_N\rangle\langle e_N|-2\delta\mathcal R,\qquad
e_N(x)=\sinh(x/2)\mu(x).
\tag{2}
\]
Every prime-power term in \(P_N\) and \(\mathcal R\), and the full pole
operator, is retained. The positive \(B_N\) is defined by closing
\[
\mathfrak b_N[u]=q_b[(\mu u)_o]
\]
on the transformed actual ratio core. Its positive-wing differential
expression, when justified, is \(2\mu B_o\mu\). The factor two comes
from the full-line odd normalization of \(q_b\).

The existing [uniform source theorem](COMPRESSED_MIXED_SMOOTHING.md)
and reference bound give
\[
\|v\|_2+\|B_og\|_2\le C\sqrt{P_0}.
\tag{3}
\]
For the second term, use any fixed positive source Sobolev order below
\(1/8\), which dominates the logarithmic Gamma multiplier.

**Theorem.** For each fixed \(0<d<1\) and \(0<s<1/2\), there is a finite
constant \(C_{d,s}\), depending only on the displayed parameters and the
fixed theta/prime coefficients, such that every actual scalar source
with \(\delta\ge d\) satisfies
\[
\boxed{\quad
\|v_o\|_{H^s(\mathbb R)}+\|g_o\|_{H^s(\mathbb R)}
\le C_{d,s}\sqrt{P_0}.
\quad}
\tag{4}
\]
This includes every vector in a fixed eigenspace, with no multiplicity
factor. No bound for arbitrary mixtures of different eigenvalues is
inferred by adding these estimates.

## 2. Identify the auxiliary form domain used by the regularization

For this particular positive operator,
\[
D(\mathfrak b_N)
=\{u\in L^2(0,\infty):q_b[(\mu u)_o]<\infty\}.
\tag{5}
\]
The right side is a closed composition-form domain because \(M_\mu\)
is bounded and \(b(D)^{1/2}\) is closed. It remains to prove that the
transformed ratio core is dense in it.

Write \(f=(\mu u)_o\). Smooth even cutoffs at infinity converge both in
\(L^2(dx/\mu^2)\) and in the logarithmic form. For the latter, the
product-difference estimate leaves the removed original jump energy
and \(CR^{-2}\|f\|_2^2\int t^2\kappa(|t|)\,dt\).
After this cutoff, radial amplitude clipping makes \(f\) bounded and
compact while preserving oddness. The clipping residuals tend to zero
pointwise, their jump differences are bounded by a fixed multiple of
the original differences, and their weighted squares are bounded by
\(|f|^2/\mu^2\). Dominated convergence pays both norms.

For a bounded compact odd \(f\), remove a smooth even neighborhood of
zero. The origin-cutoff calculation in
[ORIGIN_GRAPH_DOMAIN.md, §4](ORIGIN_GRAPH_DOMAIN.md) gives a logarithmic
form error bounded by the removed original jump energy plus
\[
C\|f\|_\infty^2\eta(1+\log(1/\eta)),
\]
which tends to zero. The weighted error tends to zero by integrability
of \(|f|^2/\mu^2\). Finally, odd smooth mollification on the resulting
compact set with a gap at zero converges in the logarithmic form and
in weighted \(L^2\): \(1/\mu^2\) is bounded on that common compact set.
Every approximant \(f_j\) has \(f_j/\psi\) in the actual smooth ratio
core, since it vanishes near zero. The vectors \(f_j/\mu\) give the
required approximation, proving (5).

In particular, if \(u\) is in (5) and \(B_o(\mu u)\in L^2\), the form
functional is represented by \(2\mu B_o(\mu u)\in L^2\). Thus
\[
u\in D(B_N),\qquad B_Nu=2\mu B_o(\mu u).
\tag{6}
\]
Only this sufficient operator-domain statement will be needed.

## 3. Complete coefficient moments and a uniform commutator

For \(0<\rho<1/2\), write
\[
\|a\|_{\mathcal A_\rho}
=\int_{\mathbb R}\langle\xi\rangle^\rho|\widehat a(\xi)|\,d\xi.
\]
The even extension of \(\mu\) belongs to \(\mathcal A_\rho\).
Indeed \(\mu'=O(|x|^{-1/2})\) at zero. Away from zero, the complete
row is locally absolutely continuous, and the theta/row bounds give
double-exponential decay for \(\mu\) and its almost-everywhere
derivative. Hence \(\mu\in W^{1,p}(\mathbb R)\) for \(1<p<2\).
Choose \(p\) sufficiently close to two and
\(\rho+1/2<h<3/2-1/p\). Hausdorff--Young and weighted Hölder give
\(W^{1,p}\subset H^h\); Fourier Cauchy--Schwarz then gives
\(\mathcal A_\rho\).

The same argument applies to every zero-extended shift/reflection
coefficient in \(K_\delta\), with the actual Mangoldt coefficient
included. For the reflected coefficients
\[
a_n(x)=\alpha_n\mu(x)\mu(d_n-x)\mathbf1_{(0,d_n)}(x),
\]
the summable \(\mathcal A_\rho\) bound is proved in
[SOURCE_SMOOTHING.md, §4](SOURCE_SMOOTHING.md).
For the forward coefficients
\(\alpha_n\mu(x)\mu(x+d_n)\mathbf1_{x>0}\), the identical
\(W^{1,p}\) calculation has the stronger tail
polynomial in \(n\) times \(e^{-c n^2}\); reversing a shift or reflecting
a wing preserves these norms. To see summability directly, split off
fixed neighborhoods of the endpoints, where the only derivative
singularity is \(x^{-1/2}\). On the remaining reflected interval use
\(e^{2x}+e^{2(d_n-x)}\ge2n\); for forward shifts use
\(e^{2(x+d_n)}=n^2e^{2x}\). Differentiation costs only fixed
polynomial factors. Threshold jumps in \(L'\) are allowed; \(L\) is
not assumed \(C^1\). The mass coefficient \(\mu^2\) is in
\(\mathcal A_\rho\) by its algebra property. The odd extension of
\(e_N\) lies in \(H^s\) for \(s<1/2\).

Fix an integer \(m\ge2\) and let \(G_\varepsilon\) on odd extensions
have multiplier
\[
m_\varepsilon(\xi)
=\langle\xi\rangle^s(1+\varepsilon\langle\xi\rangle^2)^{-m},
\qquad 0<\varepsilon<1.
\tag{7}
\]
Uniformly in \(\varepsilon\),
\[
|m_\varepsilon(\xi)|\le\langle\xi\rangle^s,\qquad
|m_\varepsilon'(\xi)|\le C_{s,m}\langle\xi\rangle^{s-1}.
\]
If \(\beta>0\) and \(s+\beta<\rho<1/2\), these bounds imply
\[
\sup_\eta\langle\eta+\zeta\rangle^\beta
|m_\varepsilon(\eta+\zeta)-m_\varepsilon(\eta)|
\le C\langle\zeta\rangle^{s+\beta}.
\tag{8}
\]
For \(|\eta|\le2|\zeta|\), use the order bound. In the other region,
use the derivative bound along the intervening segment; the power
\(s+\beta-1<0\) puts the maximum at the smallest relevant scale.
Bounded frequencies are absorbed by the brackets.

Fourier Young applied to (8) gives
\[
\|[G_\varepsilon,a]\|_{L^2\to H^\beta}
\le C\|a\|_{\mathcal A_\rho}.
\tag{9}
\]
Since \(b(\xi)\le C_\beta\langle\xi\rangle^\beta\), in particular
\[
\|[G_\varepsilon,\mu]\|+
\|B_o[G_\varepsilon,\mu]\|\le C_s.
\tag{10}
\]
Here the commutator preserves oddness. To pass from the half-line
prime operators to full-line multipliers, put
\[
a_+(x)=\alpha_n\mu(x)\mu(x+d_n)\mathbf1_{x>0},\qquad
a_-(x)=\alpha_n\mu(x)\mu(x-d_n)\mathbf1_{x>d_n},\qquad
r_+(x)=\alpha_n\mu(x)\mu(d_n-x)\mathbf1_{0<x<d_n},
\]
with zero extension and with the positive arguments of \(\mu\) used
on each support. For \(\tau_d f(x)=f(x+d)\) and
\(R_df(x)=f(d-x)\), the exact odd lifts of the three branches are
\[
M_{a_+}\tau_{d_n}+M_{a_+(-\cdot)}\tau_{-d_n},\quad
M_{a_-}\tau_{-d_n}+M_{a_-(-\cdot)}\tau_{d_n},\quad
M_{r_+}R_{d_n}+M_{r_+(-\cdot)}R_{-d_n}.
\]
Each global translation and reflection commutes with
\(G_\varepsilon\); each mirrored coefficient has the same
\(\mathcal A_\rho\) norm. Thus the support boundaries stay inside
the coefficient commutators, rather than being discarded. The summable
coefficient bounds give
\[
\|[K_\delta,G_\varepsilon]\|\le C_s
\quad(0<\delta<1,\ 0<\varepsilon<1).
\tag{11}
\]
The rank-one contribution is included: its commutator norm is bounded
by a fixed multiple of \(\|e_N\|_2\|G_\varepsilon e_N\|_2\).

## 4. Coercivity after retaining a low-frequency term

The complete bounded perturbation has
\[
\lim_{\eta\downarrow0,\ R\uparrow\infty}
\sup_{0<\delta<1}
\|\mathbf1_{(0,\eta)\cup(R,\infty)}K_\delta\|=0.
\tag{12}
\]
The far-row bound is the complete bounded-part estimate in
[the source-tail theorem](REPORT.md).
At zero the outgoing shift and reflected rows contain
\(\mu(x)=O(\sqrt x)\), and
\(\sum_n\alpha_n\sup_{|y-d_n|<\eta}\mu(y)<\infty\)
uniformly for small \(\eta\). The reverse-shift row is absent below
\(\log2\), while the mass and pole rows vanish there as well.
Self-adjointness also controls the column norm.

For fixed \(d>0\), choose
\(\chi=\mathbf1_{[\eta,R]}\) so that
\[
\|K_\delta-\chi K_\delta\chi\|\le d/2
\quad(0<\delta<1).
\]
Take \(M>0\) larger than the uniform norm of \(K_\delta\).
For \(\delta\ge d\), in form order,
\[
H_\delta+2\delta I
\succeq B_N+\tfrac32\delta I-M\chi^2.
\tag{13}
\]
Put \(a_\chi=\chi/\mu\), a bounded multiplier, and let \(P_{\le N}\)
be the ordinary Fourier low-frequency projection on odd extensions.
The logarithmic growth of \(b\) gives, for large \(N\),
\[
\|\chi u\|_2^2
\le {C\|a_\chi\|_\infty^2\over\log N}\mathfrak b_N[u]
   +2\|a_\chi P_{\le N}(\mu u)\|_2^2.
\tag{14}
\]
Choose one \(N=N_d\) large enough to absorb the first term into half
of \(B_N\), and set
\[
L_d=a_\chi P_{\le N_d}M_\mu.
\]
Equations (13)--(14) imply on the whole domain (5)
\[
\langle u,(H_\delta+2\delta)u\rangle
\ge \delta\|u\|_2^2-2M\|L_du\|_2^2,
\tag{15}
\]
with the left side interpreted as a form if necessary.

Moreover
\[
\sup_{0<\varepsilon<1}\|L_dG_\varepsilon\|<\infty.
\tag{16}
\]
Indeed commute \(G_\varepsilon\) through \(M_\mu\), use (10) for the
commutator, and use its bounded multiplier on \(|\xi|\le N_d\).
No eigenprojection or unproved regularity of an eigenbasis enters
(15)--(16). The interval and frequency cutoff may depend on \(d\).

## 5. Apply the actual auxiliary equation

Let \(u_\varepsilon=G_\varepsilon v\) and
\(A_\varepsilon=[G_\varepsilon,\mu]\). For fixed \(\varepsilon\),
\[
\mu u_\varepsilon=G_\varepsilon g-A_\varepsilon v,\qquad
B_o(\mu u_\varepsilon)
=G_\varepsilon B_og-B_oA_\varepsilon v\in L^2.
\]
Equations (5)--(6) therefore put \(u_\varepsilon\) in the actual
operator domain \(D(B_N)\). On the actual vector \(v\), the exact
commutator is
\[
[B_N,G_\varepsilon]v
=-2\mu B_oA_\varepsilon v-2A_\varepsilon B_og.
\tag{17}
\]
Using (1), (3), (10), (11), and (17) now gives
\[
(H_\delta+2\delta)u_\varepsilon
=[B_N,G_\varepsilon]v+[K_\delta,G_\varepsilon]v
=F_\varepsilon,\qquad
\|F_\varepsilon\|_2\le C_s\sqrt{P_0}.
\tag{18}
\]

These regularized vectors need not be centered original \(P\)-sources.
They are used only in the already established auxiliary operator,
whose complete pole term was retained throughout.

Insert (18) in (15), and use (16) and (3):
\[
d\|u_\varepsilon\|_2^2
\le C_s\sqrt{P_0}\|u_\varepsilon\|_2+C_{d,s}P_0.
\tag{19}
\]
Thus \(\|u_\varepsilon\|_2\le C_{d,s}\sqrt{P_0}\) uniformly in
\(\varepsilon\). Fatou as \(m_\varepsilon(\xi)\to\langle\xi\rangle^s\)
proves the \(v_o\) assertion in (4). Multiplication by
\(\mu\in\mathcal A_\rho\), with \(s<\rho<1/2\), is bounded on \(H^s\)
by Fourier Young, proving the \(g_o\) assertion.

The argument makes no estimate uniform as \(d\downarrow0\).
It does not attain \(s=1/2\), and it does not justify endpoint Taylor
jets or the weighted increment at a prescribed raw-translation center.
In particular, the complete covariance and neutral-compensation
inequalities retain their unresolved signed comparison.
