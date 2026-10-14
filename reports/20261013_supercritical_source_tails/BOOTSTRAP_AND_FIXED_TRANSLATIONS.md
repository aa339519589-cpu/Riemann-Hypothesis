# A second source bootstrap and every sufficiently small fixed translation

This note uses the [fixed-depth normalized-source theorem](FIXED_DEPTH_REGULARITY.md)
once more, with Sobolev regularity in the commutator input. For each
fixed positive lower spectral depth it proves all source orders below
one. Crossing order \(1/2\) removes the exceptional translation parameters
in the [raw-translation domain theorem](../20261014_translation_neutral_covariance/RAW_TRANSLATION_DOMAIN.md).
The resulting covariance inequalities still require a signed comparison.

## 1. Actual source and statement

Keep the complete auxiliary operator, its actual core closure, and all
normalizations of [fixed-depth regularity](FIXED_DEPTH_REGULARITY.md):
\[
g=\psi r,\quad v=g/\mu,\quad P_0=P[r],\quad
\delta=1-\lambda^{-1},\qquad
(B_N+K_\delta+2\delta)v=0.
\tag{1}
\]
The full pole and every Mangoldt label remain in \(K_\delta\).

**Theorem.** For every \(0<d<1\) and \(0<s<1\), every actual scalar
centered source in (1) with \(\delta\ge d\) satisfies
\[
\|v_o\|_{H^s(\mathbb R)}+\|g_o\|_{H^s(\mathbb R)}
\le C_{d,s}\sqrt{P_0}.
\tag{2}
\]
The constants may diverge as \(d\downarrow0\). No endpoint \(s=1\),
derivative trace, or mixed-eigenvalue packet estimate is asserted.

There is also a fixed \(A>0\), independent of the source and its depth,
such that for every real \(a\in[-A,A]\),
\[
(T_ag)_o(x)=\tfrac12\{g_o(x+a)+g_o(x-a)\}
\tag{3}
\]
is an actual centered \(P\)-source. The map
\(a\mapsto[T_ag/\psi]\) is continuous into that completion, and
\[
\sup_{|a|\le A}\|[T_ag/\psi]\|_P\le C_d\sqrt{P_0}
\quad(\delta\ge d).
\tag{4}
\]
Consequently the full covariance and neutral-compensation matrices are
legal for every finite tuple with \(|a_i|\le A/2\), including all
prescribed nodes in this range. Their nonnegativity requires the source
to correspond to the largest supercritical eigenvalue, as before.
No such eigenvalue is excluded here.

## 2. A Sobolev-input commutator

Let
\[
\tfrac12<r<1,\quad 0<t<\tfrac12,\quad s>0,\quad\beta>0,\qquad
\gamma=r+t-\tfrac12-s-\beta>0.
\tag{5}
\]
Fix \(m\ge2\). Let \(G_\varepsilon\) have the even multiplier
\[
m_\varepsilon(\xi)=
\langle\xi\rangle^s(1+\varepsilon\langle\xi\rangle^2)^{-m},
\qquad 0<\varepsilon<1.
\]
Then
\[
\boxed{\quad
\|[G_\varepsilon,a]f\|_{H^\beta}
\le C_{r,t,s,\beta,m}\|a\|_{H^r}\|f\|_{H^t},
\quad}
\tag{6}
\]
uniformly in \(\varepsilon\). The symbol has uniform derivative bounds
\(\left|\partial_\xi^j m_\varepsilon\right|
\le C_j\langle\xi\rangle^{s-j}\). An annular localization at scale
\(2^k\) therefore has a convolution kernel whose first absolute moment
is at most \(C2^{(s-1)k}\), by rescaling and integration by parts.

Here is the complete dyadic estimate. Use inhomogeneous blocks \(a_l,f_k\)
and put \(A_l=2^{rl}\|a_l\|_2\), \(F_k=2^{tk}\|f_k\|_2\).
All index-zero terms are interpreted at scale one.

For \(l<k-4\), sum the coefficient blocks first. Bernstein and
Cauchy--Schwarz give
\[
\|\partial a_{<k-4}\|_\infty
\le C2^{(3/2-r)k}\|a\|_{H^r}.
\]
Both the input and output remain in an annulus of scale \(2^k\).
The localized kernel commutator and its first moment give
\[
\|[G_\varepsilon,a_{<k-4}]f_k\|_{H^\beta}
\le C2^{-\gamma k}\|a\|_{H^r}F_k.
\tag{7}
\]

For \(k<l-4\), the two low-frequency input bounds are
\[
\|f_{<l-4}\|_\infty\le
C_t2^{(1/2-t)l}\|f\|_{H^t},\qquad
\|G_\varepsilon f_{<l-4}\|_\infty\le
C2^{(s+1/2-t)l}\|f\|_{H^t}.
\]
Each product has frequency support in a ball of radius \(C2^l\).
Applying the order-\(s+\beta\) ball bound to the first term, and the
order-\(\beta\) ball bound to the second, proves
\[
\|[G_\varepsilon,a_l]f_{<l-4}\|_{H^\beta}
\le C2^{-\gamma l}A_l\|f\|_{H^t}.
\tag{8}
\]

For \(|l-k|\le4\), the product can have arbitrarily low output frequency.
Use its entire frequency ball, rather than projecting away those outputs:
\[
\|a_lf_k\|_2\le C2^{k/2}\|a_l\|_2\|f_k\|_2,\qquad
\|G_\varepsilon f_k\|_\infty
\le C2^{(s+1/2)k}\|f_k\|_2.
\]
The same two ball estimates give
\[
\|[G_\varepsilon,a_l]f_k\|_{H^\beta}
\le C2^{-\gamma k}A_lF_k.
\tag{9}
\]
Thus every low-output interaction is included. Summing (7)--(9)
by Cauchy--Schwarz proves (6), first for finite expansions and then
by convergence. For each fixed \(\varepsilon\), multiplication by
\(a\in H^r\subset L^\infty\) and \(G_\varepsilon\) are bounded on
\(L^2\), so this limit is the actual commutator.

## 3. Apply the estimate to the complete auxiliary operator

The coefficient estimates in [fixed-depth regularity, §3](FIXED_DEPTH_REGULARITY.md)
give a little more than their Fourier \(L^1\) consequence:
\[
\mu\in H^r(\mathbb R),\qquad
\sum_{\text{all prime branches}}\|a_{\rm branch}\|_{H^r}<\infty
\quad\text{for every }r<1.
\tag{10}
\]
Indeed choose \(1<p<2\) with \(r<3/2-1/p\) and use the already
summable \(W^{1,p}\) estimates. The coefficients include their actual
Mangoldt factors, zero extensions, and both odd-extension mirrors.
The exact affine shift/reflection formulas before equation (11) of
that note apply unchanged.

The mass coefficient \(\mu^2\) has the same property. The odd pole
vector \(e_N=\sinh(x/2)\mu(x)\) belongs to \(H^1\): it is
\(O(x^{3/2})\) with derivative \(O(x^{1/2})\) at zero; its continuous
threshold values and theta-decaying a.e. derivative pay the rest.
This also bounds the pole commutator for every \(s<1\).

For \(t<1/2\), the published theorem and the logarithmic Gamma symbol
give
\[
\|v_o\|_{H^t}+\|g_o\|_{H^t}+\|(B_og)_o\|_{H^t}
\le C_{d,t}\sqrt{P_0}.
\tag{11}
\]
For the last term choose a slightly larger source order below \(1/2\).
For any target \(s<1\), choose \(r,t,\beta\) satisfying (5).
Translations and reflections preserve every full-line Sobolev norm.
Equations (6), (10), and (11), with the complete coefficient sums,
therefore prove
\[
\begin{split}
\|[K_\delta,G_\varepsilon]v\|_2&\le C_{d,s}\sqrt{P_0},\\
\|[G_\varepsilon,\mu]B_og\|_2
+\|B_o[G_\varepsilon,\mu]v\|_2&\le C_{d,s}\sqrt{P_0}.
\end{split}
\tag{12}
\]
Any \(\beta>0\) absorbs the logarithmic multiplier in the second line.

Put \(u_\varepsilon=G_\varepsilon v\) and
\(A_\varepsilon=[G_\varepsilon,\mu]\). As in the first bootstrap,
\[
\mu u_\varepsilon=G_\varepsilon g-A_\varepsilon v,\qquad
B_o(\mu u_\varepsilon)
=G_\varepsilon B_og-B_oA_\varepsilon v\in L^2.
\]
The established natural-form-domain identification puts this vector
in the actual \(D(B_N)\). The exact identity is still
\[
(B_N+K_\delta+2\delta)u_\varepsilon
=-2\mu B_oA_\varepsilon v-2A_\varepsilon B_og
  +[K_\delta,G_\varepsilon]v=:F_\varepsilon,
\quad \|F_\varepsilon\|_2\le C_{d,s}\sqrt{P_0}.
\tag{13}
\]
No centering of the regularized vector is required; the full pole
operator has not been removed.

Use the same \(L_d=a_\chi P_{\le N_d}M_\mu\) and coercivity estimate
from the first bootstrap:
\[
\langle u,(B_N+K_\delta+2\delta)u\rangle
\ge\delta\|u\|_2^2-2M\|L_du\|_2^2.
\tag{14}
\]
The previous uniform \(L^2\) operator bound for \(L_dG_\varepsilon\)
is not being asserted at this higher order. On the actual vector,
\[
L_du_\varepsilon
=a_\chi P_{\le N_d}(G_\varepsilon g-A_\varepsilon v).
\]
The low-frequency multiplier is uniformly bounded and (6), (11)
bound the second term. Hence
\(\|L_du_\varepsilon\|_2\le C_{d,s}\sqrt{P_0}\).
Testing (13) in (14) proves a quadratic bound for
\(\|u_\varepsilon\|_2\), uniform in \(\varepsilon\).
Fatou gives \(v_o\in H^s\) with the norm in (2).

To recover \(g_o\), choose \(q\in(\max(s,1/2),1)\).
The now proved assertion gives \(v_o\in H^q\), and (10) gives
\(\mu\in H^q\). The one-dimensional \(H^q\) product estimate for
\(q>1/2\) gives \(g_o=\mu v_o\in H^q\), proving (2).

## 4. Every fixed translation belongs to the actual completion

Fix \(s\in(1/2,1)\) and \(0<\alpha<s-1/2\).
Sobolev embedding gives a continuous odd representative of \(g_o\).
More generally, for every odd \(f\in H^s\),
\[
|T_af(x)|=\tfrac12|f(a+x)-f(a-x)|
\le C_s\|f\|_{H^s}|x|^\alpha.
\]
Thus, uniformly in the real parameter \(a\),
\[
\int_0^\eta |T_af(x)|^2\,\frac{dx}{x}
\le C_{s,\alpha}\eta^{2\alpha}\|f\|_{H^s}^2.
\tag{15}
\]
This replaces the averaged origin estimate in the raw-translation proof.
It does not assert \(T_af/x\in L^2\).

Choose \(A>0\) sufficiently small that an interval strictly larger
than \([-A,A]\) lies within both the inherited legal smooth-convolution
radius and the raw theorem's far-tail radius
\(e^{2R}-1<1/2\). These radii are independent of \(\delta\).
That theorem's complete theta/row tail estimate gives, uniformly for
all these shifts and their small even mollifications,
\[
\int_X^\infty |T_ag(x)|^2
       \{V(x)+m(x)^{-2}\}\,dx
\le C_{d,A}P_0 e^{C_AX-c_Ae^{2X}}
\quad(\delta\ge d).
\tag{16}
\]
The constants are allowed to depend on the lower depth \(d\).

Let \(\rho_\varepsilon\) be a nonnegative even smooth mollifier and
\(f_{a,\varepsilon}=T_a(\rho_\varepsilon*g_o)\).
These are legal smooth convolutions with the required tails and exactly
zero pole moment. In (15) use
\(f=(\rho_\varepsilon-\rho_{\varepsilon'})*g_o\), whose \(H^s\)
norm tends to zero. The resulting origin convergence in
\(L^2(V\,dx)\) is uniform in \(a\). On compact sets away from zero,
ordinary \(L^2\) convergence is uniform in \(a\), since \(T_a\) is
a contraction. The uniform tail (16) pays the omitted far wing.
The same argument gives convergence in physical \(L^2(dx/m^2)\);
its weight is bounded at zero. Finally,
\[
q_b[(f_{a,\varepsilon}-f_{a,\varepsilon'})_o]
\le q_b[(\rho_\varepsilon-\rho_{\varepsilon'})*g_o]\longrightarrow0
\]
uniformly in \(a\).

The complete estimates, already used in the raw-domain theorem, are
\[
N[f]\le C\|f/\mu\|_2^2,\qquad
|h[f]|\le q_b[f_o]+C\|f_o/m\|_2^2,\qquad P=N+h.
\tag{17}
\]
They retain the absolutely convergent full prime correlations.
Equations (15)--(17) prove that the smooth ratios are uniformly Cauchy
in the actual \(P\)-completion. The injective continuous centered-source
map identifies each limit with \(T_ag\). This proves membership for
every \(a\) and (4). The pole moment remains zero, since it is multiplied
by \(\cosh(a/2)\) and by the even mollifier's cosh moment.

Continuity in \(a\) follows from the same estimates.
\((T_a-T_b)g_o\to0\) in \(H^s\) as \(a\to b\), by its Fourier
multiplier and dominated convergence. It is odd, so its origin weighted
norm is controlled by the analogue of (15) with \(a=0\).
Compact and far-wing terms are paid as above. Equation (17), now on
the identified completion vectors, proves \(P\)-norm continuity.

## 5. Consequence for the complete finite matrices

For every finite tuple \(|a_i|\le A/2\), all the sources
\(T_{a_i}g\), \(T_{a_i+a_j}g\), and \(T_{a_i-a_j}g\) are now legal.
The exact identity \(T_aT_b=(T_{a+b}+T_{a-b})/2\) and the complete
commuting source pairing therefore give, for a largest source,
\[
B_{ij}:=N(T_{a_i}g,T_{a_j}g)
-\tfrac12N(g,(T_{a_i+a_j}+T_{a_i-a_j})g)
=\delta^{-1}Q_\delta(T_{a_i}g,T_{a_j}g).
\tag{18}
\]
This is positive semidefinite for every such tuple. For a finite family
of independent known neutral sources \(s_j\), retain the exact common
projection in [neutral-leakage compensation](../20261014_translation_neutral_covariance/NEUTRAL_LEAKAGE_COMPENSATION.md):
\[
M_{jk}=N(s_j,s_k),\qquad L_{ji}=N(s_j,T_{a_i}g),\qquad
B-L^\mathsf{T}M^{-1}L\succeq0.
\tag{19}
\]
No nullspace identification or dropped mixed term is used.

The change from the earlier raw-translation theorem is the removal of
exceptional parameter sets. Equations (18)--(19) remain necessary
inequalities. No actual source and mask violating (19) has been
constructed here, and no critical positivity or RH conclusion follows.
