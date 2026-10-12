# Laguerre approximation and conditional Schur witness

Independent derivation for the local real old-Green constant-order question,
2026-10-13. This note uses the source form and notation in
[SOURCE_FORM.md](../20261012_localized_odd_schur/SOURCE_FORM.md)
It does not quantify the
growing theta-jet interpolation matrix; that is a separate input.

Set \(U=\pi k\),
\(\sigma_k^2=(512/\sqrt\pi)U^{19/2}e^{-2U}\), and
\(s_k(x)=\pi e^{2x}-U\) on the positive wing. The positive collar has
exactly \(0<s_k<\pi\).

Use the conjugate-linear-first convention
\(\langle f,g\rangle=\int_{\mathbb R}\overline{f(x)}g(x)\,dx\), the Fourier
convention \(\widehat z(t)=\int_{\mathbb R}z(x)e^{itx}dx\), and put
\(C_0=\gamma+\pi/2+3\log2+\log\pi\),
\(\alpha_n=\Lambda(n)/\sqrt n\). On the odd theta/cutoff class used here,
whenever the full Gamma energy is finite, the complete prime correlations
converge absolutely, and the polar integral exists absolutely, write the
full-source quadratic form as
\[
 \mathfrak t[z]=\mathfrak q_\Gamma[z]+\mathfrak p[z]-2|\ell(z)|^2,
 \quad
 \mathfrak q_\Gamma[z]=\frac1{2\pi}\int_{\mathbb R}b(t)|\widehat z(t)|^2dt
                    -C_0\|z\|_2^2,
\]
\[
 \mathfrak p[z]=-2\sum_{n\geq2}\alpha_n
   \operatorname{Re}\int_{\mathbb R}\overline{z(x)}z(x+\log n)\,dx,
 \qquad
 \ell(z)=\int_{\mathbb R}\sinh(x/2)z(x)\,dx.
 \tag{0}
\]
This is the complete source form on the stated pairing class, not a claim
that \(T\) is a globally closed operator on unweighted \(L^2\). For compactly
supported odd \(z\) in \((-a,a)\), it agrees with the finite-window form
\(\mathfrak A_a[z]\) in SOURCE_FORM. Denote its Hermitian polarization by
\(\mathfrak t[u,v]\), conjugate-linear in \(u\).

The exact theta density needed below follows directly from
\[
 f_0(x)=e^{x/2}\sum_{n\ge1}\mathcal F_0(n^2u)e^{-n^2u},
 \qquad \mathcal F_0(u)=-32u^5(1+O(u^{-1})).
\]
The sum of theta frequencies \(n\ge2\), relative to the first frequency,
is \(O(u^M e^{-3u})\), including one derivative, for a fixed \(M\).
On \(u=U+s\ge U-2\pi\), both errors are \(O(U^{-1})\) uniformly.
Using \(dx=du/(2u)\) and the definition of \(\sigma_k\) gives
\[
 d\nu_k(s):=\sigma_k^{-2}|f_0(x_k(s))|^2dx_k(s)
 =\left(1+\frac{s}{U}\right)^{19/2}e^{-2s}
       (1+O(U^{-1}))\,ds.
 \tag{0a}
\]
The leading coefficient of \(\mathcal F_0\) is negative, so the associated
pointwise amplitude is
\[
 \frac{f_0(x_k(s))}{\sigma_k}
 =-\sqrt{2U}\left(1+\frac{s}{U}\right)^{21/4}e^{-s}
       (1+O(U^{-1})).
 \tag{0b}
\]
Also \(f_0'(x)/f_0(x)=O(u)\) on this tail. These statements justify the
uniform density, pointwise envelope, and physical derivative conversions
used below; no fixed-degree limit is needed for them.

## 1. Full-half-line Laguerre approximation

Let \(W\in C_c^\infty(0,\pi)\), and let \(W_0\) denote its zero extension to
\([-2\pi,\infty)\). Put

\[
 t=s+2\pi\geq0,\qquad x=2t=2(s+2\pi),\qquad
 F(x)=W_0(x/2-2\pi).
\]

Then \(F\in C_c^\infty((0,\infty))\), in fact its support is contained in
\((4\pi,6\pi)\). The measure changes by

\[
 e^{-2s}\,ds=\frac{e^{4\pi}}2 e^{-x}\,dx.
\]

Use the classical Laguerre polynomials \(L_n=L_n^{(0)}\), normalized by
\(\int_0^\infty e^{-x}L_nL_j\,dx=\delta_{nj}\). Thus

\[
 \phi_n(s)=\sqrt2 e^{-2\pi}L_n(2(s+2\pi)),\qquad n\geq0,
\]

is an orthonormal basis of \(L^2([-2\pi,\infty),e^{-2s}ds)\). In particular,
this is a whole-half-line basis: its tail estimates include every
\(s\geq-2\pi\), not just a fixed compact interval. Let

\[
 P_m=\sum_{n=0}^{m-1}c_n\phi_n,
 \qquad c_n=\langle\phi_n,W_0\rangle_{e^{-2s}}.
\]

It is a polynomial in \(s\) of degree less than \(m\).

The self-adjoint Laguerre Sturm--Liouville operator is

\[
 \mathcal L=-x\partial_x^2-(1-x)\partial_x,
 \qquad \mathcal L L_n=nL_n.
\]

Every iterate \(\mathcal L^pF\) is again smooth and compactly supported
away from zero. Repeated integration by parts therefore has no endpoint
terms and gives, for each integer \(p\geq1\),

\[
 \sum_{n\geq1}n^{2p}|c_n|^2\leq C_p\|\mathcal L^pF\|_{L^2(e^{-x}dx)}^2<\infty.
 \tag{1}
\]

Consequently,

\[
 \|W_0-P_m\|_{L^2(e^{-2s})}
 \leq C_p m^{-p}.
 \tag{2}
\]

For the ordinary weighted derivative, use the exact identity
\(L_n'=-\sum_{j=0}^{n-1}L_j\), hence
\(\|L_n'\|_{L^2(e^{-x})}=\sqrt n\). Minkowski and Cauchy--Schwarz yield

\[
 \begin{aligned}
 \|(W_0-P_m)'\|_{L^2(e^{-2s})}
 &\leq C\sum_{n\geq m}|c_n|\sqrt n\\
 &\leq C_p\Big(\sum_{n\geq m}n^{1-2p}\Big)^{1/2}
 \leq C_p m^{1-p},\qquad p>1.
 \end{aligned}
 \tag{3}
\]

The factor (2) from \(\partial_s=2\partial_x\) is absorbed into \(C_p\).
Given any \(r>0\), choose an integer \(p\geq\max(2,r)\). Equations
(2)--(3) prove

\[
 \boxed{\quad
 \|W_0-P_m\|_{L^2(e^{-2s})}\leq C_r m^{-r},\qquad
 \|(W_0-P_m)'\|_{L^2(e^{-2s})}\leq C_r m^{1-r}.
 \quad}
 \tag{4}
\]

The derivative estimate is deliberately stated for the un-degenerate
weighted \(H^1\) norm. It does not rely on the Laguerre quadratic form with
its extra factor \(x\), which alone would not control an unweighted
derivative near \(x=0\).

We also need polynomially weighted variants when converting an \(s\)-profile
to an \(x\)-derivative. These follow from the same argument. Indeed,

\[
 xL_n=(2n+1)L_n-(n+1)L_{n+1}-nL_{n-1},
 \tag{5}
\]

and derivatives of \(L_n\) have Laguerre expansions with coefficients
bounded by a fixed power of \(n\) at every fixed derivative order.
Equations (1) and (5) imply, for fixed integers \(A,j\geq0\) and every
\(N\),

\[
 \|(1+s_+)^A\partial_s^j(W_0-P_m)\|_{L^2(e^{-2s})}
 \leq C_{A,j,N}m^{-N},\qquad s_+=\max(s,0).
 \tag{6}
\]

Thus the approximation controls the whole tail and any fixed polynomial
weight or finite derivative loss.

## 2. The growing degree and the exact tail residual

Take \(m_k=\lfloor(\log k)^{1/4}\rfloor\). From (4), for any selected
\(r>2\), the ideal profile error has

\[
 \epsilon_{0,k}=O(m_k^{-r}),\qquad
 \epsilon_{1,k}=O(m_k^{1-r}),
 \tag{7}
\]

where \(\epsilon_0\) controls the weighted \(L^2\) profile and
\(\epsilon_1\) controls the first derivative and the fixed polynomially
weighted norms in (6). In particular

\[
 (\log k)\epsilon_{0,k}^2=o(1),\qquad
 \epsilon_{0,k}^2\log(1+\epsilon_{1,k}/\epsilon_{0,k})=o(1).
 \tag{8}
\]

The second relation also holds if \(\epsilon_1/\epsilon_0\) is bounded by a
fixed power of \(m_k\).

Here is the precise growing-jet input needed to use (7). Let \(F_k\) be a
finite linear combination of exact odd source-null jets, including any
projection away from a fixed old pivot space, and suppose its positive-tail
profile is

\[
 \Phi_k(s)=F_k(x_k(s))/f_0(x_k(s)),\qquad
 x_k(s)=\tfrac12\log((\pi k+s)/\pi).
\]

Set \(\eta_k=1-\chi_k\), extended by zero below
\(s_{R,k}=\pi k(e^{-2/k}-1)\), and define

\[
 H_k(s)=\eta_k(s)\Phi_k(s)-W_0(s),\qquad s\geq s_{R,k}.
 \tag{9}
\]

For fixed sufficiently large \(A\), define
\[
 d\nu_k(s)=\sigma_k^{-2}|f_0(x_k(s))|^2\,dx_k(s),\qquad
 \|G\|_{L^2_{A,k}}^2=
 \int_{s_{R,k}}^\infty(1+s_+)^A|G(s)|^2\,d\nu_k(s).
\]
Require
\[
 \|H_k\|_{L^2_{A,k}}\leq \epsilon_{0,k},\qquad
 \|(1+s_+)(H_k,H_k')\|_{L^2_{A,k}}\leq\epsilon_{1,k},
 \tag{10}
\]
with errors no larger than the right sides of (7), up to constants. For
the physical derivative it suffices to take \(A=2\): the factor
\(u/U=1+s/U\) is bounded by \(C(1+s_+)\). The \(m=1\) theta density
contributes \((1+s/U)^{19/2}e^{-2s}\); globally the full-theta estimate
gives \(d\nu_k\leq C(1+s_+)^{19/2}e^{-2s}ds\). Thus (10) is implied by an
ordinary profile \(H^1_{24}\) bound.

The fixed-weight Laguerre estimates (6) supply errors
\(O(m_k^{-r})\) and \(O(m_k^{1-r})\). The growing-jet realization estimate
in GROWING_JET_FRAME.md, equation (1), adds
\[
 k^{-1}e^{C_A m_k^2\log(m_k+2)}\|P_{m_k}\|_{H^1_{24}}.
\]
Since \(\|P_{m_k}\|_{H^1_{24}}=O(1)\) and
\(m_k^2\log(m_k+2)=o(\log k)\), this is \(k^{-1+o(1)}\). Hence (10) holds
with
\[
 \epsilon_{0,k}=O(m_k^{-r}+k^{-1+o(1)}),\qquad
 \epsilon_{1,k}=O(m_k^{1-r}+k^{-1+o(1)}).
 \tag{10a}
\]
The same growing-jet note's pointwise Taylor remainder (15), remote-tail
bound (17), and omitted-frequency bound (21), together with (22), imply
the envelope (19) below with
\[
 A_k\leq\exp(C_A m_k^2\log(m_k+2))=k^{o(1)}.
 \tag{10b}
\]
In the Taylor region, the factor
\((1+s_+)^{21/4}e^{-(1-c)s_+}|s|^{m_k}\) has maximum
\(e^{O(m_k\log(m_k+2))}\); on \(s\geq U/2\), the separate remote estimate
pays the remaining exponential. The ideal Laguerre polynomial itself has
an \(e^{O(m_k)}\) envelope as shown below. These statements use explicit
pointwise and remote-tail estimates, not an inference from weighted
\(H^1\) alone.

The first-\(m_k\)-jet realization is a valid old trial in the variational
short of the full old space. If trials are additionally restricted to the
\(Q_k\) complement of a fixed pivot \(E_k\), the growing projection and
its tail error need a separate estimate; it is not part of the input used
here. Fixed-\(m\) convergence in the fixed finite frame result alone would not imply (10), and no
limits are interchanged.

For the ideal profile, \(\eta_k=1\) on the support of \(W_0\), so
\(\eta_kP_m-W_0=\eta_k(P_m-W_0)\). The transition derivative
\(\eta_k'P_m\) is supported where \(W_0=0\), and
\(\eta_k'\) is uniformly bounded in \(s\) under the narrow-cutoff
assumptions: \(\chi_k'=O(k)\) while \(dx_k/ds=O(1/k)\) on the transition.
Thus (4), (6) give (7) for the ideal cutoff profile, including the
transition derivative.

## 3. Full Gamma residual bound, without a global closed source operator

Let \(z\in H^1(\mathbb R)\). The source symbol has the positive series
\[
 b(t)=\sum_{j\geq0}
 \frac{(t/2)^2}{(j+1/4)((j+1/4)^2+(t/2)^2)}.
\]
The \(j=0\) term is at most \(4\); comparing the remaining decreasing
summand with its integral from \(1/4\) gives
\[
 0\leq b(t)\leq4+\frac12\log(1+4t^2)
 \leq\log k+4+2(t/k)^2,\qquad k\geq2.
 \tag{11}
\]
For the last inequality, factor
\(1+4t^2\leq k^2(1+4(t/k)^2)\) and use
\(\frac12\log(1+4u^2)\leq2u^2\).

The exact Gamma form is
\(\mathfrak q_\Gamma[z]=\mathfrak g[z]-C_0\|z\|_2^2\), with
\(\mathfrak g[z]=(2\pi)^{-1}\int b(t)|\widehat z(t)|^2dt\). Plancherel gives
the signed two-sided estimate
\[
 -C_0\|z\|_2^2
 \leq\mathfrak q_\Gamma[z]
 \leq(\log k+4-C_0)\|z\|_2^2+\frac{2}{k^2}\|z'\|_2^2.
 \tag{12}
\]
This is the useful estimate for the Schur upper bound: it controls the
positive energy by \((\log k)\|z\|_2^2\) plus a derivative-controlled
subprincipal term, without requiring a relative \(H^1/L^2\) estimate.

For the tail profile (9), the theta density and
\(f_0'/f_0=O(u)\), \(ds/dx=2u\), imply from (10), with a fixed sufficiently
large polynomial weight,
\[
 \|z_k\|_2\leq C\epsilon_{0,k},\qquad
 \|z_k'\|_2\leq Ck\epsilon_{1,k},\qquad
 z_k(x)=\sigma_k^{-1}f_0(x)H_k(s_k(x))
 \tag{13}
\]
on the positive tail, with the odd reflection on the negative tail.
Therefore
\[
 -C\epsilon_{0,k}^2
 \leq\mathfrak q_\Gamma[z_k]
 \leq C\big((1+\log k)\epsilon_{0,k}^2+\epsilon_{1,k}^2\big).
 \tag{14}
\]
When (7) holds with \(r>2\), both bounds tend to zero. This uses the full
multiplier and does not assert that the formal complete source operator is
closed on all of unweighted \(L^2(\mathbb R)\).

## 4. The complete signed prime sum

The prime contribution \(\mathfrak p\) from (0) must be kept as the
complete correlation series. Put \(d_n=\log n\). For an odd \(z\), write
its positive wing as \(h(x)\), supported in
\(x\geq R_k=a_k-1/k\). Define

\[
 J_n=\int_{R_k}^\infty\overline{h(x)}h(x+d_n)\,dx,
 \qquad
 C_n=\int_{R_k}^{d_n-R_k}\overline{h(x)}h(d_n-x)\,dx,
 \tag{16}
\]

and set \(C_n=0\) if \(d_n<2R_k\). Splitting the two same-wing pieces
and the opposite-wing crossing in the exact odd correlation gives

\[
 \mathfrak p[z]
 =-4\sum_{n\geq2}\alpha_n\operatorname{Re}J_n
   +2\sum_{n\geq2}\alpha_n\operatorname{Re}C_n,
 \qquad \alpha_n=\Lambda(n)/\sqrt n,
 \tag{17}
\]

and hence the exact absolute majorant

\[
 |\mathfrak p[z]|
 \leq4\sum_{n\geq2}\alpha_n|J_n|
      +2\sum_{n\geq\lceil e^{2R_k}\rceil}\alpha_n|C_n|.
 \tag{18}
\]

This is an all-prime-power bound. Enlarging a sum to all integers is
permitted only after using \(\alpha_n\leq(\log n)/\sqrt n\).

For the actual collar vector, \(q_{\mathfrak p}[y_k]=0\): same-wing
collar distances are less than \(\log2\), while opposite-wing distances lie
strictly between \(\log k\) and \(\log(k+1)\), with endpoints irrelevant
in \(L^2\). Thus one may equivalently split \(q_{\mathfrak p}[r_k-y_k]=q_{\mathfrak p}[r_k]-2\operatorname{Re}q_{\mathfrak p}(r_k,y_k)\).

The estimate below bounds
the complete signed sum of the combined residual directly, including its
tail-tail and tail-collar correlations.

For a convenient sufficient condition on a growing profile, suppose its
positive wing obeys the explicit pointwise envelope

\[
 |h(x_k(s))|\leq C\sqrt{k}\,A_k e^{-c s_+},
 \qquad s\geq s_{R,k},
 \tag{19}
\]

for some fixed \(c>0\). A sufficient profile condition for (19) is

\[
 A_k\geq C\sup_{s\geq s_{R,k}}
 (1+s_+)^{21/4}e^{-(1-c)s_+}|H_k(s)|.
 \tag{20}
\]

The direct theta amplitude estimate (0b) supplies the factor
\(\sqrt{k}(1+s_+)^{21/4}e^{-s}\) (the additional \(1/2\) power comes from
converting the \(ds\) density to the pointwise \(dx\) amplitude). On a same wing,
\(s'=n^2(U+s)-U\), so \(s+s'\geq c_1(n^2-1)U\) for \(n\geq2\),
large \(k\), and \(s\geq s_{R,k}\). Substitution in \(J_n\), with
\(dx=ds/(2(U+s))\), gives

\[
 \sum_{n\geq2}\alpha_n|J_n|
 \leq C A_k^2 e^{-c_2 k}.
 \tag{21}
\]

The crossing term is even more directly localized. If \(x,d_n-x\geq R_k\),
then

\[
 s_1+s_2
 =\pi e^{2x}+\pi e^{2(d_n-x)}-2\pi k
 \geq 2\pi(n-k),
 \tag{22}
\]

by AM--GM, and the crossing interval has length
\(L_n=(\log(n/k)+2/k)_+\). It is empty unless
\(n\geq\lceil ke^{-2/k}\rceil=k-1\). Equations (19), (22) imply

\[
 |C_n|\leq Ck A_k^2 L_n e^{-2\pi c(n-k)}.
\]

For \(n=k+j\), \(j\geq-1\), use
\(kL_n\leq C(j+2)\) and
\(\alpha_n\leq(\log n)/\sqrt n\). Summing the resulting exponentially
decaying majorant gives

\[
 \sum_{n\geq k-1}\alpha_n|C_n|
 \leq C A_k^2\frac{\log k}{\sqrt k}.
 \tag{23}
\]

Together,

\[
 \boxed{\quad
 |\mathfrak p[z_k]|
 \leq C A_k^2\left(e^{-c_2k}+\frac{\log k}{\sqrt k}\right).
 \quad}
 \tag{24}
\]

Thus \(A_k=k^{o(1)}\) suffices for the full signed prime contribution to be
\(o(1)\). The ideal Laguerre profile has such a subpower envelope at
\(m_k=(\log k)^{1/4}\): the explicit finite-sum formula
\(L_n(x)=\sum_{j\leq n}(-1)^j\binom njx^j/j!\), optimized against a fixed
exponential weight, gives
\(\sup_{x\geq0}(1+x)^A e^{-\delta x}|L_n(x)|\leq C_{A,\delta}e^{C_{A,\delta}n}\);
the Laguerre coefficients \(c_n\) are bounded (indeed rapidly decreasing),
so the degree-\(m_k\) sum is at most \(e^{O(m_k)}=k^{o(1)}\). For the actual
jet realization, the same envelope must be verified for its realization
error. A weighted \(L^2/H^1\) bound alone does not imply (19), and no
uniform growing-jet claim follows from the fixed-\(m\) statements in the fixed finite frame result.

The coefficient-2 polar term also needs a separate bound; it cannot be
discarded just from \(\|z_k\|_2\to0\), because its vector grows with the
window. Under (19), the theta envelope and
\(|\sinh(x_k(s)/2)|\leq Ck^{1/4}(1+s_+)^{1/4}\) give

\[
 \left|\int\sinh(x/2)z_k(x)\,dx\right|
 \leq C k^{-1/4}A_k,
 \qquad
 2\left|\int\sinh(x/2)z_k(x)\,dx\right|^2
 \leq Ck^{-1/2}A_k^2=o(1)
 \tag{25}
\]

when \(A_k=k^{o(1)}\). The local term is \(o(1)\) by (10).

Combining (14), (24), (25), the full signed source energy satisfies

\[
 |\mathfrak t[z_k]|
 \leq C\big((1+\log k)\epsilon_{0,k}^2+\epsilon_{1,k}^2\big)
 +C A_k^2\left(e^{-c_2k}+\frac{\log k}{\sqrt k}+k^{-1/2}\right)
 =o(1),
 \tag{26}
\]

under (7), (10a), and (10b). Formula (18), or the stronger
profile bound (24), is the required complete-prime estimate; a
Gaussian-only cutoff or a claim of a globally closed symbol-plus-prime
operator is not a substitute.

## 5. Exact source-null cancellation and the Schur trial

Let \(F_k\) be the raw finite jet combination whose positive-tail profile
is \(\Phi_k=F_k/f_0\) in Section 2, and set
\[
 G_k=\sigma_k^{-1}F_k.
\]
Since \(f_j=D^{2j}f_0\), the source commutes with these derivatives on the
theta class, and integration by parts gives
\(\int\sinh(x/2)f_j(x)\,dx=0\). Therefore \(G_k\) is source-null and
polar-neutral. Define
\[
 v_k=\chi_kG_k\quad\hbox{(old-window vector)},\qquad
 r_k=(1-\chi_k)G_k,\qquad
 y_k(x)=\sigma_k^{-1}f_0(x)W(s_k(x))
 \tag{27}
\]
on the positive collar, oddly reflected to the negative collar. For
\(W\ne0\), the tail-density limit gives
\[
 \|y_k\|_2^2\longrightarrow
 2\int_0^\pi |W(s)|^2e^{-2s}\,ds>0.
 \tag{27a}
\]
The scaling now matches the profile residual exactly:
\[
 G_k=v_k+r_k,\qquad
 z_k=r_k-y_k=\sigma_k^{-1}f_0(x)H_k(s_k(x)).
\]
For the Hermitian source form, polarization gives
\[
 \mathfrak t[v_k+y_k]-\mathfrak t[r_k-y_k]
 =\operatorname{Re}\mathfrak t[v_k-r_k+2y_k,G_k]=0,
 \tag{28}
\]
because \(G_k\) is source-null and the complete source pairings are
defined on these theta-tail vectors.
 
Since \(v_k+y_k\) is compactly supported in the next window,
SOURCE_FORM identifies its full source form with the finite-window form:

\[
 \boxed{\quad
 \mathfrak A_{a_{k+1}}[v_k+y_k]
 =\mathfrak t[v_k+y_k]
 =\mathfrak t[r_k-y_k]=o(1).
 \quad}
 \tag{29}
\]

The last expression in (29) is the complete source form on the
noncompact theta-tail residual, defined by its finite Gamma energy,
absolutely convergent prime correlations, and polar functional. It is not
literally the compact-support operator form \(\mathfrak A_{a_{k+1}}[r_k-y_k]\):
that residual extends beyond \(a_{k+1}\), so the latter notation is
undefined under SOURCE_FORM (1). This distinction matters for the prime
sum and for the domain statement.

The old/collar form-domain direct sum and bounded off-diagonal source
block are established in
[SHARP_WINDOW_DOMAIN.md](../20261012_localized_odd_schur/SHARP_WINDOW_DOMAIN.md),
Sections 1--4. This supplies the form-domain basis for the actual Schur
variational identity.

If the old block is coercive on its full old space so that its Schur
variational characterization is valid, let \(\mathcal D_{\rm old}\) be its full old form domain. Using \(v_k\) as the old trial gives

\[
 \operatorname{Schur}_{k+1}[y_k]
 =\inf_{v\in\mathcal D_{\rm old}}
     \mathfrak A_{a_{k+1}}[v+y_k]
 \leq \mathfrak A_{a_{k+1}}[v_k+y_k]=o(1).
 \tag{30}
\]

The growing-jet realization estimates (10a), (10b), and the envelope (19)
are supplied by the proved, independently reviewed profile theorem in
[GROWING_JET_FRAME.md](GROWING_JET_FRAME.md),
including its Taylor, remote-tail, and omitted-frequency bounds; no
fixed-m limit is interchanged here. Thus, on the stated theta-tail form
domain, the remaining structural hypothesis for (30) is coercivity of the
full old block. The independent review is in [REFEREE_TRIAL.md](REFEREE_TRIAL.md).
This conditional result is only a variational upper bound: it gives no lower bound,
determines no Schur sign, and implies no positivity or RH claim.
