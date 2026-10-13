# Boundary-local coupling for the complete original even form

Date: 2026-10-14 (UTC+8). This proof is based on the complete mathematical
draft supplied by the user and independently checked against the original
operator. Its new estimate retains an exact source Gram term; the
remaining boundary budget has one sampling logarithm. The actual
\(\kappa^{-2}\) factor and the signed diagonal comparison remain unresolved.

## 1. Original objects and theorem

Use the original even physical operator and closed form of
[ORIGINAL_FORM_FOUNDATION.md](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md)
and [INFINITE_HIGH_TAIL.md](INFINITE_HIGH_TAIL.md). Inner products are
conjugate-linear in the first slot, and
\(\widehat F(t)=\int F(x)e^{itx}\,dx\). Put

\[
w=m^2=\frac{\Phi}{2\cosh(x/2)},\qquad
\Phi(x)=\sum_{n\ge1}(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\]
\[
\alpha_n=\frac{\Lambda(n)}{\sqrt n},\quad d_n=\log n,\quad
SF=\sum_{n\ge2}\alpha_n(F(\cdot+d_n)+F(\cdot-d_n)),
\]
\[
b(t)=\sum_{j\ge0}\frac{2t^2}{a_j(a_j^2+t^2)},\quad a_j=2j+\tfrac12,
\qquad C_0=\gamma_E+\frac\pi2+3\log2+\log\pi.
\]

For \(F=mv,G=mu\), the complete form is

\[
\mathfrak h(v,u)=\frac1{2\pi}\int b(t)\overline{\widehat F(t)}\widehat G(t)\,dt
-C_0\langle F,G\rangle-\langle F,SG\rangle.
\tag{1}
\]

The source notation \(S\) is used in its legitimate paired realization;
no bounded unweighted \(L^2\) operator is asserted. The complete physical
perturbation \(M_mSM_m\) is bounded, with its series converging absolutely
in operator norm. Write \(\mathfrak b\) for the nonnegative Gamma form.
The actual closed form domain is

\[
\mathcal Q=\{v\in L^2_{\rm even}:b^{1/2}\widehat{mv}\in L^2\},
\]

with equivalent norm \((\|v\|_2^2+\mathfrak b[v])^{1/2}\).
For \(z=\gamma_z+i\eta_z\), set

\[
\varphi_z=m\cos(zx),\qquad f_z=m\varphi_z=w\cos(zx),\qquad
\ell(t)=\log(2+t)\quad(t\ge0).
\tag{2}
\]

For every fixed \(|\eta_z|\le1/2\), the source \(f_z\) restricted to the
real \(x\)-axis is Schwartz; it may be complex-valued.
Thus \(m b(D)f_z\in L^2\), and the associated-operator criterion and the
bounded complete perturbation give \(\varphi_z\in D(H)\).

Let \(\mathcal Z\) consist of the distinct genuine \(\Xi\) zeros with
\(\gamma_z>0\), retaining both members of each nonreal conjugate pair.
Let \(j_z\) be the actual multiplicity, and fix any constant \(C_{\mathcal Z}\)
such that

\[
\sum_{\gamma_z\in[n,n+1)}j_z\le C_{\mathcal Z}\log(2+n)
\qquad(n=0,1,\ldots).
\tag{3}
\]

This is the unconditional local count used in Section 6 of
INFINITE_HIGH_TAIL.md; it follows from Riemann--von Mangoldt with its
\(O(\log T)\) remainder. No separation or RH is assumed.
For coefficients define

\[
J(a)^2=\sum_z\frac{|a_z|^2}{j_z}\ell(\gamma_z),\qquad
Q(a)^2=\sum_z\frac{|a_z|^2}{j_z}\ell(\gamma_z)^2.
\tag{4}
\]

Assume \(Q(a)<\infty\). Section 5 below proves unconditional convergence
of every subseries in the original form domain. For \(T\ge2\), put

\[
v_<=\sum_{\gamma_z<T}a_z\varphi_z,\quad
v_\ge=\sum_{\gamma_z\ge T}a_z\varphi_z,\quad F_<=mv_<,\quad F_\ge=mv_\ge,
\]
\[
E_<(T)=\sum_{\gamma_z<T}\frac{|a_z|^2}{j_z}\ell(\gamma_z)e^{-(T-\gamma_z)/8},
\qquad
E_\ge(T)=\sum_{\gamma_z\ge T}\frac{|a_z|^2}{j_z}\ell(\gamma_z)e^{-(\gamma_z-T)/8}.
\]

**Theorem.** With \(C=2^{39}C_{\mathcal Z}\),

\[
\boxed{\left|\mathfrak h(v_<,v_\ge)-\ell(T)\langle F_<,F_\ge\rangle\right|
\le C\sqrt{E_<(T)E_\ge(T)}.}
\tag{5}
\]

The main term is the **source** inner product, not
\(\langle v_<,v_\ge\rangle\). Constants are independent of the height,
number of nodes, maximum frequency and smallest spacing. All Gamma terms,
both prime directions and all prime powers are retained.

## 2. Complete theta strip and Gamma estimates

For \(x\ge0,|y|\le1/2\), one has \(\cos(2y)\ge\cos1>1/2\).
The theta summands are bounded by
\(59n^4e^{9x/2}e^{-(3/2)n^2e^{2x}}\). Also
\(|2\cosh((x+iy)/2)|\ge(31/32)e^{x/2}\).
The adjacent ratio in the remaining theta sum is at most
\(16e^{-9/2}<1/4\); hence its complete sum is below \(4/3\).
Since \(59(32/31)(4/3)<100\), analytic evenness gives on the whole strip

\[
|w(x+iy)|\le100e^{4|x|-(3/2)e^{2|x|}},\qquad |y|\le1/2.
\tag{6}
\]

The original Jacobi identity supplies that analytic evenness. The
denominator has no zeros in this strip, and normal convergence pays the
theta continuation. No complex square root of \(w\) is needed.

For real \(|\eta|\le1/2\), shift the Fourier integral for
\(we^{-\eta x}\) to height \(\operatorname{sgn}(t)/2\). Vertical ends vanish
by (6). The inequality \((9/2)r\le(3/4)e^{2r}+2\) gives

\[
\left|\widehat{we^{-\eta(\cdot)}}(t)\right|\le1200e^{-|t|/2},
\qquad
|\widehat f_z(t)|\le600(e^{-|t-\gamma_z|/2}+e^{-|t+\gamma_z|/2}).
\tag{7}
\]

Indeed the shifted \(L^1\) norm is below
\(100e^2\int e^{-(3/4)e^{2|x|}}dx<100\cdot9\cdot4/3\).
This shifts individual modes only; it assumes no fixed strip of an
infinite eigenstate expansion.

For the complete Gamma series, the summand
\(g(a)=2t^2/[a(a^2+t^2)]\) decreases in \(a\). Integral comparison on
the spacing-two lattice gives

\[
\tfrac12\log(1+4t^2)\le b(t)\le4+\tfrac12\log(1+4t^2).
\]

Since \(1/3\le\sqrt{1+4t^2}/(2+|t|)\le2\),

\[
|b(t)-\ell(|t|)|\le5,\qquad 0<C_0<8.
\tag{8}
\]

No Gamma truncation is made.

## 3. All prime shifts and the centered two-mode kernel

In this section assume explicitly
\(0\le\gamma_z\le T\le\gamma_\zeta\) and
\(|\eta_z|,|\eta_\zeta|\le1/2\). The two nodes need not be zeros.
The nonnegative-real-part convention is essential: without it,
\(z=-\zeta\) would represent the same cosine at a large apparent separation.

For each \(d=\pm\log n\), expand both cosines. Each of the four terms in
\(\langle f_z,\tau_df_\zeta\rangle\) has coefficient \(1/4\) and the form

\[
e^{i\epsilon'\zeta d}\int w(x)w(x+d)e^{-\sigma x}e^{i\omega x}\,dx,
\quad \sigma=\epsilon\eta_z+\epsilon'\eta_\zeta\in[-1,1],\quad
\omega=\epsilon'\gamma_\zeta-\epsilon\gamma_z.
\]

The outer factor costs at most \(\sqrt n\). Shift each integral to
\(\operatorname{Im}x=\operatorname{sgn}(\omega)/2\). Its gain is
\(e^{-|\omega|/2}\), and \(|\omega|\ge\gamma_\zeta-\gamma_z\).
By (6), the remaining integral is at most

\[
10^4\int e^{5(|x|+|x+d|)-(3/2)(e^{2|x|}+e^{2|x+d|})}\,dx
\le\frac83\,10^4e^4e^{-3n/4}.
\tag{9}
\]

For the last inequality use \(5r\le(3/4)e^{2r}+2\) twice,
\(e^{2|x|}+e^{2|x+d|}\ge2n\), and split the remaining negative exponent
into two equal parts. The final integrable part is bounded by
\(e^{-(3/4)|x|}\), whose integral is \(8/3\).
Multiplication by \(\alpha_n\) cancels the factor \(\sqrt n\). Both shift
directions give

\[
|\langle f_z,Sf_\zeta\rangle|
\le\frac{16}{3}10^4e^4\sum_{n\ge2}\Lambda(n)e^{-3n/4}
e^{-\lvert\gamma_z-\gamma_\zeta\rvert/2}
<2^{24}e^{-\lvert\gamma_z-\gamma_\zeta\rvert/2}.
\tag{10}
\]

Here \(\Lambda(n)\le n\), \(e^4<81\), and
\(\sum_{n\ge2}ne^{-3n/4}<2\), so the scalar is below
\(8{,}640{,}000<2^{24}\). All interchanges follow the summable complete
majorant in (9).

For the Gamma part let \(\gamma=\gamma_z\), \(\gamma'=\gamma_\zeta\).
For each pair of centers \(a=\pm\gamma,c=\pm\gamma'\), put
\(A=|t-a|,B=|t-c|,d=|a-c|\). Then \(d\ge\gamma'-\gamma\) and
\(\big||t|-T\big|\le A+(T-\gamma)\le A+d\). Equations (7)--(8) imply

\[
|b(t)-C_0-\ell(T)|\le13+A+d.
\]

Since \(A+B\ge d\),

\[
\int(13+A+d)e^{-(A+B)/2}\,dt
\le(136+8d)e^{-d/4}\le200e^{-d/8}.
\tag{11}
\]

The four center pairs and the exact Plancherel factor yield

\[
\left|\frac1{2\pi}\int(b-C_0-\ell(T))\overline{\widehat f_z}\widehat f_\zeta\,dt\right|
\le\frac{600^2\cdot4\cdot200}{2\pi}e^{-|\gamma-\gamma'|/8}
<2^{26}e^{-|\gamma-\gamma'|/8}.
\]

Adding (10), with \(2^{26}+2^{24}<2^{27}\), proves

\[
\boxed{|\mathfrak h(\varphi_z,\varphi_\zeta)
-\ell(T)\langle f_z,f_\zeta\rangle|
\le2^{27}e^{-|\gamma_z-\gamma_\zeta|/8}.}
\tag{12}
\]

## 4. Multiplicity-weighted summation

Using (3), unit-distance shells around any \(\gamma\ge0\) give

\[
\sum_zj_ze^{-|\gamma-\gamma_z|/16}
\le4C_{\mathcal Z}\sum_{k\ge0}e^{-k/16}[\ell(\gamma)+\log(2+k)]
\le2^{12}C_{\mathcal Z}\ell(\gamma).
\tag{13}
\]

Each shell meets at most four integer unit intervals. The last step uses
\(\ell(\gamma)>1/2\), \(\log(2+k)\le k+1\), and
\(1-e^{-1/16}\ge1/17\); the intermediate constant
\(12\cdot17^2\) is below \(2^{12}\).

Weighted Young, followed by optimization of its positive parameter,
therefore gives for any two coefficient families

\[
\sum_{z,\zeta}|p_zq_\zeta|e^{-|\gamma_z-\gamma_\zeta|/16}
\le2^{12}C_{\mathcal Z}J(p)J(q).
\tag{14}
\]

Explicitly use
\(2|p_zq_\zeta|\le r|p_z|^2j_\zeta/j_z+r^{-1}|q_\zeta|^2j_z/j_\zeta\),
and then \(r=J(q)/J(p)\); zero budgets are immediate.
Actual multiplicities enter exactly once in (13), rather than being
replaced by artificial separated nodes.

Across the cut, \(\gamma_\zeta-\gamma_z=(T-\gamma_z)+(\gamma_\zeta-T)\).
Set \(p_z=a_ze^{-(T-\gamma_z)/16}\) below the cut and
\(q_\zeta=a_\zeta e^{-(\gamma_\zeta-T)/16}\) above it. Thus

\[
|a_za_\zeta|e^{-(\gamma_\zeta-\gamma_z)/8}
=|p_zq_\zeta|e^{-(\gamma_\zeta-\gamma_z)/16},\quad
J(p)^2=E_<,\quad J(q)^2=E_\ge.
\]

Combining (12) and (14) proves (5) for finite sums, with
\(C=2^{39}C_{\mathcal Z}\).

## 5. Unconditional convergence in the original form domain

The physical Gram uses the analytic weight \(w\). Its exponential
components have imaginary offsets at most 1. The same contour argument,
now using \(5r\le(3/4)e^{2r}+2\), supplies a fixed constant \(C_1\) with

\[
|\langle\varphi_z,\varphi_\zeta\rangle|
\le C_1e^{-|\gamma_z-\gamma_\zeta|/2}.
\tag{15}
\]

For the nonnegative Gamma Gram, take the smaller nonnegative frequency
as the center in (7). The estimate
\(b(t)\le5+\ell(\min(\gamma_z,\gamma_\zeta))+|t-a|\)
and the same integral argument as (11) give

\[
|\mathfrak b(\varphi_z,\varphi_\zeta)|
\le C_2\ell(\min(\gamma_z,\gamma_\zeta))e^{-|\gamma_z-\gamma_\zeta|/8}.
\tag{16}
\]

Fixed constants are absorbed by \(\ell\ge\log2>1/2\).
The exponential row estimates hold with other fixed positive decay
rates as well. Equations (13), (15), (16) and weighted Young give

\[
\left\|\sum a_z\varphi_z\right\|_2^2\le C_3J(a)^2,\qquad
\mathfrak b\left[\sum a_z\varphi_z\right]\le C_4Q(a)^2.
\tag{17}
\]

For the Gamma estimate, the extra logarithm in row \(z\) is at most
\(\ell(\gamma_z)\). The finite-subset tails of \(Q(a)^2\) tend to zero.
Hence the finite sums form an unconditional Cauchy net in the original
closed form norm, and every subseries converges there. Multiplication by
bounded \(m\) gives source \(L^2\) convergence. The bounded complete
physical perturbation makes its pairings continuous; (10), (14) also
give direct absolute convergence of the prime coefficient pairing.
Thus (5) passes to the asserted infinite form limits. No lower frame
bound, separation, finite total rank or spectral-synthesis assumption is
used.

## 6. The actual negative state and the remaining signed comparison

Write

\[
D_T=\mathfrak h(v_<,v_\ge)-\ell(T)\langle F_<,F_\ge\rangle,
\qquad v=v_<+v_\ge,\quad F=mv.
\]

The exact total identity is

\[
\mathfrak h[v]=\ell(T)\|F\|^2
+(\mathfrak h[v_<]-\ell(T)\|F_<\|^2)
+(\mathfrak h[v_\ge]-\ell(T)\|F_\ge\|^2)+2\operatorname{Re}D_T.
\tag{18}
\]

The source main term has been put back in the complete total, not
discarded. Neither remaining diagonal in (18) is asserted nonnegative.

For genuine nodes, \(\langle g_0,\varphi_z\rangle=\Xi(z)=0\), where
\(g_0=\Phi/m\) is the normalized original ground vector. Their form limits
stay in \(g_0^\perp\). The even source pole moment is half that pairing
and vanishes continuously. No odd pole debit is substituted into (1).

For the actual real even state \(Hu=-\kappa u\), \(u\perp g_0\), the complete
expansion from Section 5 of INFINITE_HIGH_TAIL.md is

\[
u=-\frac2\kappa\sum_{\Re z>0}j_zB(z)m\cos(zx),\qquad
B(z)=\int m(x)u(x)\cos(zx)\,dx,
\qquad a_z=-2j_zB(z)/\kappa.
\tag{19}
\]

Fixed positive-depth source regularity gives the required \(Q(a)<\infty\).
Define \(S_<,S_\ge\) by the formulas for \(E_<,E_\ge\), replacing
\(|a_z|^2/j_z\) by \(j_z|B(z)|^2\). Then

\[
E_<=4\kappa^{-2}S_<,\qquad E_\ge=4\kappa^{-2}S_\ge,\qquad
\boxed{|D_T|\le\frac{4C}{\kappa^2}\sqrt{S_<(T)S_\ge(T)}.}
\tag{20}
\]

The full real quadratic remainder \(2\operatorname{Re}D_T\) has twice this
absolute bound. All conjugate nodes, multiplicities and Hermitian
squares remain.

For an actual *lowest* negative state there is a useful exact formulation
of the unclosed sign. Put \(l=v_<,v=v_\ge\),
\(Q_\kappa=\mathfrak h+\kappa\langle\cdot,\cdot\rangle\) on \(g_0^\perp\), and

\[
K_T(a,b)=\kappa\langle a,b\rangle+\ell(T)\langle ma,mb\rangle.
\]

Since \(Q_\kappa(u,\cdot)=0\) and \(Q_\kappa\ge0\) there,

\[
K_T(l,v)=-Q_\kappa[v]-D_T,
\qquad
|K_T(l,v)+Q_\kappa[v]|\le\frac{4C}{\kappa^2}\sqrt{S_<S_\ge}.
\tag{21}
\]

The positive inner product \(K_T\) need not have a positive mixed value.
Equation (21) does not supply relative absorption, and does not assert a
sign for the renormalized diagonals in (18).

## 7. Average cuts without a frequency gap

For fixed coefficients with \(Q(a)<\infty\), \(A\ge2\) and \(L>0\), there
exists \(T\in[A,A+L]\), avoiding all node heights if desired, such that

\[
|D_T|\le\frac{8C}{L}J(a)^2.
\tag{22}
\]

Indeed, nonnegative Tonelli and the whole-line integral of the
exponential weight give

\[
\int_A^{A+L}(E_<+E_\ge)\,dT
\le16\sum_z\frac{|a_z|^2}{j_z}\ell(\gamma_z)=16J(a)^2.
\]

Apply \(\sqrt{E_<E_\ge}\le(E_<+E_\ge)/2\) and average (5).
This is an absolute coefficient-budget estimate, with no claim about
either side's diagonal sign.

## 8. Provenance and scope

The supplied proof used repository snapshot
`a55c6081bc1509ef9b78829b68add21300a2a207`. Its analytic theta input is the
original Jacobi foundation, also reviewed in
[THETA_STRIP_AND_TAILS.md](../20261013_foundation_audit/THETA_STRIP_AND_TAILS.md).
The local count and actual expansion are the ones already used in
INFINITE_HIGH_TAIL.md, Sections 5--6. A primary counting reference is
Hasanalizade, Shen and Wong,
[Counting zeros of the Riemann zeta function](https://arxiv.org/abs/2107.06506).
Only the local \(O(\log T)\) consequence is used, not optimized numerical
zero-count constants.

The substantive addition is exact source-Gram centering, which removes
the height logarithm from the residual two-mode kernel and lowers the
boundary sampling weight from two logarithms to one. The \(Q(a)\) condition
also suffices for unconditional original-form convergence, without a
graph-absolute-convergence hypothesis. This is distinct from a separated
finite-window estimate or the published odd whole-Green-band comparison.

[check_centered_boundary_constants.py](check_centered_boundary_constants.py)
independently checks 15 of the displayed scalar comparisons using only
Python Fraction arithmetic and exponential Taylor bounds with explicit
remainders. Its executed output is
[centered_boundary_constants.json](centered_boundary_constants.json).
Run `python3 check_centered_boundary_constants.py > centered_boundary_constants.json`
to reproduce it. This is a separately written check, not the supplied
draft's unprovided 19-comparison script. The analytic tails and domain
arguments are proved above and independently reviewed in
[CENTERED_BOUNDARY_REVIEW.md](CENTERED_BOUNDARY_REVIEW.md); scalar execution
does not certify them automatically.

There is no finite-height zero input in this theorem. It does not prove
either renormalized diagonal nonnegative, cancel the actual
\(\kappa^{-2}\), identify Green and physical eigenvalues individually, or
establish \(K\le I\). Relative control of the actual boundary budget
together with both signed diagonal blocks remains the carrying problem.
