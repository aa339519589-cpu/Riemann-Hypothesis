# Reflected Markov paths and odd physical negative inertia

Date: 2026-10-13. All inner products are conjugate-linear in the first slot and linear in the second. For a self-adjoint operator, its negative index means the negative index of its associated form.

This note records two interfaces for the complete reflected-prime Green problem. First, the reflected energy is a reversible Markov Dirichlet
form; a positive reference inverse then bounds every positive Green spectral band by an inverse moment of the lazy path operator. Second, the
\(P-N\) form and the odd physical pole-inclusive form have the same negative index by their common compact smooth core, and the coefficient-two
pole identity preserves that index on \(H_o\). This is an inertia transfer, not a bounded similarity. Every Mangoldt sum includes prime powers.

The conclusions do not prove the unit Green bound, do not settle the original even mean-zero interface, and imply no RH result.

## 1. Reflected edges as a Markov Dirichlet form

Let
\[
 \psi(x)=-\Phi'(x)>0\quad(x>0),\qquad
 d_n=\log n,\qquad \alpha_n=\frac{\Lambda(n)}{\sqrt n},
 \qquad L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x),
 \qquad d\mu_N(x)=2\psi(x)L(x)\,dx.                             \tag{1}
\]
The complete theta and Mangoldt bounds give \(0<L(x)<\infty\), \(L(x)\le Ce^{x/2}\) for large \(x\), and \(\psi(x)L(x)=O(x)\) at zero. The theta
tail makes \(0<\mu_N((0,\infty))<\infty\).

The reflected energy and its edge gradient are
\[
\begin{aligned}
 N[r]&=\sum_{n\ge2}\alpha_n\int_0^{d_n}
    \psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2\,dx,\\
 (\nabla_Nr)_n(x)&=r(x)-r(d_n-x),\qquad 0<x<d_n,
\end{aligned}                                                     \tag{2}
\]
with edge measure \(\alpha_n\psi(x)\psi(d_n-x)\,dx\). Let \(K_N\) be the closure of these gradients from the compact smooth ratio core \(\mathcal C\).

For \(x>0\), \(q_n(x)=\alpha_n\psi(d_n-x)/L(x)\), \(d_n>x\), is a probability distribution. Define
\[
 (Ar)(x)=\sum_{d_n>x}q_n(x)r(d_n-x).                             \tag{3}
\]
Detailed balance is
\[
 \langle f,Ag\rangle_{\mu_N}
 =2\sum_{n\ge2}\alpha_n\int_0^{d_n}
       \psi(x)\psi(d_n-x)\overline{f(x)}g(d_n-x)\,dx.             \tag{4}
\]
Reflection \(x\mapsto d_n-x\) shows \(A=A^*\); Jensen gives \(\|A\|\le1\), and \(A1=1\). Hence, with
\[
 D=I-A,\qquad B=\frac{I+A}{2},
 \qquad 0\le B\le I,\quad D=2(I-B)\ge0,                         \tag{5}
\]
polarization of (2) gives
\[
 N[r]=\langle r,Dr\rangle_{\mu_N}=\|D^{1/2}r\|_{\mu_N}^2.         \tag{6}
\]

The kernel of \(D\) is precisely the constants. If \(N[r]=0\), every reflected edge has zero difference. The \(2^j\)- and \(2^{j+1}\)-edges
compose to translation by \(\log2\) on \(0<x<j\log2\); the \(3^j\)- and \(3^{j+1}\)-edges similarly give period \(\log3\) on increasing
intervals. Both are genuine prime-power edges, with \(\alpha_{2^j}=\log2/\sqrt{2^j}>0\) and \(\alpha_{3^j}=\log3/\sqrt{3^j}>0\). Extending by the
\(\log2\) period gives a locally \(L^2\) function on the line. Since \(\log3/\log2\) is irrational, the generated period group is dense;
continuity of translations in \(L^2_{\rm loc}\) forces \(r\) to be constant.

Let \(\mathscr H_0=\{1\}^{\perp}\subset L^2(\mu_N)\). The core is dense, and \(\overline{\operatorname{Ran}D^{1/2}}=\mathscr H_0\). Thus
\[
 U_N(D^{1/2}r)=\nabla_Nr,\qquad r\in\mathcal C,                  \tag{7}
\]
extends to a unitary \(U_N:\mathscr H_0\to K_N\). This uses no inverse for \(D\) and no spectral gap.

## 2. The positive reference inverse and the Green comparison

On ratios, retain the complete positive form
\[
\begin{aligned}
 \kappa(u)&=\frac{e^{-u/2}}{1-e^{-2u}},\\
 P_\Gamma[r]&=\iint_{(0,\infty)^2}\psi(x)\psi(y)
 [\kappa(|x-y|)-\kappa(x+y)]|r(x)-r(y)|^2\,dx\,dy,\\
 w_*(x)&=\psi(x)\sinh(x/2),\\
 P_{\rm pole}[r]&=4\iint w_*(x)w_*(y)|r(x)-r(y)|^2\,dx\,dy,\\
 P_{F,n}[r]&=2\alpha_n\int_0^\infty\psi(x)\psi(x+d_n)
                         |r(x)-r(x+d_n)|^2\,dx,\\
 P[r]&=P_\Gamma[r]+P_{\rm pole}[r]+\sum_{n\ge2}P_{F,n}[r].
\end{aligned}                                                     \tag{8}
\]
Together with (2), the exact source identity on the common core is \(P[r]-N[r]=\mathfrak a_o[v]\), \(v=\psi r/m\); it includes the
coefficient-two pole and all prime powers.

Use the positive reference \(R=P_{\rm pole}+P_{F,2}\). Put
\[
 d=\log2,\quad \alpha_2=\frac{\log2}{\sqrt2},\quad
 c_2(x)=2\alpha_2\psi(x)\psi(x+d),\quad
 D_R(x)=w_*(x)+c_2(x)+\mathbf1_{\{x>d\}}c_2(x-d).
                                                                    \tag{9}
\]
Since \(\int w_*=1/8\), the pole variance gives
\[
 \widehat R[r]=R[r]+8\left|\int w_*r\right|^2
              =\int w_*|r|^2+P_{F,2}[r].                         \tag{10}
\]
For \(x=t+kd\), \(0<t<d\), put
\[
 D_k(t)=D_R(t+kd),\qquad v_k(t)=\sqrt{D_k(t)}r(t+kd),\qquad
 (\mathcal J_R f)_k(t)=f(t+kd).
\]
Here \(\mathcal J_R:L^2((0,\infty),dx)\to L^2((0,d);\ell^2)\) is the fiber unitary and \(v=\mathcal J_R(\sqrt{D_R}\,r)\). The published [positive
reference inverse](../20261013_full_prime_green_reference/REFERENCE_INVERSE.md) identifies the transported operator \(\mathcal A_R=\mathcal J_R^{-1}(\int_0^d{}^\oplus A_t\,dt)\mathcal J_R\) on \(L^2(dx)\), with
\[
 \widehat R[r]=\langle \sqrt{D_R}r,(I-\mathcal A_R)\sqrt{D_R}r\rangle,
 \quad (A_tv)_k=\beta_{k-1}(t)v_{k-1}+\beta_k(t)v_{k+1},\quad
 \beta_k(t)=\frac{c_2(t+kd)}{\sqrt{D_k(t)D_{k+1}(t)}}.
\]


The same reference theorem proves
\[
 \rho:=\|\mathcal A_R\|=\sup_{0<t<d}\|A_t\|<1.
\]
This uniform bound is used below; no compactness of the direct integral is asserted.

Let \(K_P=\overline{\nabla_P\mathcal C}\). The full-prime report [proves \(N\le CP\) and the bounded map \(T:K_P\to K_N\)](../20261013_full_prime_green_reference/REPORT.md); on the core \(T\nabla_Pr=\nabla_Nr\). Put \(K=TT^*\), so \(\Gamma_P[h]=\langle h,Kh\rangle_N\). For \(h\in K_N\), define the full vertex current and its normalized load
\[
 W_h(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x)h_n(x),\qquad
 w_h(x)=\frac{W_h(x)}{L(x)},\qquad
 b_h(x)=\frac{2\psi(x)W_h(x)}{\sqrt{D_R(x)}}.                    \tag{11}
\]
The complete incidence estimate and pairing identity are
\[
 \int_0^\infty\frac{\psi}{L}|W_h|^2\le\|h\|_N^2,\qquad
 \langle h,\nabla_Nr\rangle_N
   =2\int_0^\infty\psi\,\overline{W_h}r
   =\langle w_h,r\rangle_{\mu_N}.                               \tag{12}
\]
Antisymmetry on each reflected edge gives \(\int_0^\infty\psi W_h=0\) for finite currents, and the incidence estimate extends it to every \(h\in K_N\). Thus the reference load annihilates constants and is valid on the centered \(R\)-completion. If \(q_h=U_N^*h\), polarization through (7)
gives \(w_h=D^{1/2}q_h\). The reference inverse is its uniformly convergent Neumann series,
\[
 \Gamma_R[h]=\langle b_h,(I-\mathcal A_R)^{-1}b_h\rangle
            =\sum_{j\ge0}\langle b_h,\mathcal A_R^jb_h\rangle.             \tag{13}
\]
The reference constants are
\[
 C_D=\sup_{x>0}\frac{2\psi(x)L(x)}{D_R(x)}<\infty,\qquad
 C_*=\frac{C_D}{1-\rho}.                                        \tag{14}
\]
At zero, numerator and \(c_2(x)\) in \(D_R\) vanish linearly with positive leading coefficients; away from zero use \(D_R\ge w_*\) and \(L(x)\le Ce^{x/2}\). Thus
\[
 \|b_h\|_2^2
 =\int_0^\infty\frac{2\psi L}{D_R}|w_h|^2\,d\mu_N
 \le C_D\|w_h\|_{\mu_N}^2.
\]

Since \(P\ge R\), \(\Gamma_P\le\Gamma_R\), so (13)–(14) and \(w_h=D^{1/2}q_h\) give
\[
 \boxed{\quad
 0\le\widehat K:=U_N^*KU_N\le C_*D\quad\text{on }\mathscr H_0.
 \quad}                                                          \tag{15}
\]
No unit bound for \(\widehat K\) is asserted.

## 3. Inverse moment and finite lazy paths

For \(a>0\), let \(E_a=\mathbf1_{[a,\infty)}(\widehat K)\). Douglas's range theorem applied to (15) gives a bounded \(C\) with
\[
 \widehat K^{1/2}=D^{1/2}C,\qquad \|C\|\le\sqrt{C_*}.             \tag{16}
\]
For \(q\in\operatorname{Ran}E_a\), the band inverse \(z=\widehat K^{-1/2}q\) satisfies \(\|z\|\le a^{-1/2}\|q\|\). Hence
\(q=D^{1/2}Cz\in\operatorname{Ran}D^{1/2}\), and the unique inverse on \(\mathscr H_0\) obeys
\[
 \boxed{\quad \|D^{-1/2}q\|^2\le\frac{C_*}{a}\|q\|^2.\quad}       \tag{17}
\]
This is a range statement, not an assumed spectral gap for \(D\).

Define the positive finite lazy-path sum
\[
 S_J[U_Nq]=\frac12\sum_{j=0}^J
             \langle D^{1/2}q,B^jD^{1/2}q\rangle_{\mu_N}.
\]
For every \(q\in\mathscr H_0\), the exact remainder identity is
\[
 \|q\|^2-S_J[U_Nq]=\langle q,B^{J+1}q\rangle.
\]
If \(q\in\operatorname{Ran}E_a\), (17) defines \(D^{-1/2}q\), and the remainder also has the spectral representation
\[
 \langle q,B^{J+1}q\rangle
 =\int_{(0,2]}d(1-d/2)^{J+1}\,d\|D^{-1/2}q\|_d^2.
\]
The scalar maximum of \(d(1-d/2)^{J+1}\) on \([0,2]\) is attained at \(d=2/(J+2)\) and is at most \(2/(J+2)\). Thus every positive Green spectral
band satisfies the explicit uniform tail
\[
 \boxed{\quad
 0\le\|q\|^2-S_J[U_Nq]
 \le\frac{2C_*}{a(J+2)}\|q\|^2,\qquad q\in\operatorname{Ran}E_a.
 \quad}                                                          \tag{19}
\]
For the supercritical band \(a=1+\gamma>1\), the full N norm is approximated by positive paths with error \(O(C_*/((1+\gamma)J))\). The
compact-excess result separately makes each fixed supercritical band finite dimensional; (16)–(19) do not require computing that
finite-dimensional matrix.

## 4. Common-core negative inertia on the odd physical block

Let \(S_N\) be the closed span of the known neutral theta-jet gradients \(\nabla_Nr_j\), \(r_j=f_j/\psi\),
\(f_j=\Phi^{(2j+3)}-\tfrac14\Phi^{(2j+1)}\). The mixed null identity in the [odd-domain report](../20261013_odd_operator_domains/REPORT.md) and
[compact Green excess report](../20261013_compact_green_excess/REPORT.md) makes \(S_N\) a reducing eigenspace of \(K\) with eigenvalue one; no
identification with the full kernel is assumed. Let \(H_o\) be the odd restriction of the original closed physical operator, with pole-free form
\(\mathfrak h_o\). Let
\[
 s_0(x)=\sinh(x/2),\qquad s=ms_0,\qquad
 \mathfrak a_o[v]=\mathfrak h_o[v]-2|\langle s,v\rangle|^2,\qquad
 \mathcal A_o=H_o-2|s\rangle\langle s|.
\]
The bounded rank-one term preserves the form domain and form core. The parity-preserving original form core is \(C_c^\infty(\mathbb R)_{\rm odd}\). On the common core, set \(f=mv=\psi r\); because \(m\) is smooth positive even and \(\psi\) has a simple odd zero, \(v\leftrightarrow r=f/\psi\) is a bijection between compact smooth odd physical sources and compact smooth ratios with smooth even extension at zero. The exact
source identity is
\[
 \mathfrak a_o[v]=P[r]-N[r],                                   \tag{20}
\]
with \(P,N\) from (8),(2), including every prime power.

The finite global comparison in the published [full-prime Green report](../20261013_full_prime_green_reference/REPORT.md) gives \(N\le C P\) and
a bounded \(T:K_P\to K_N\). Therefore
\[
 q_{PN}[u,v]=\langle u,v\rangle_P-\langle Tu,Tv\rangle_N
\]
is continuous on the P-gradient completion. Moreover \(q_{PN}\) is closed and lower semibounded there: adding \((C+1)\|u\|_P^2\) gives a form
norm equivalent to the P norm. For a Hermitian form define
\[
 \nu_-(q)=\sup\{\dim E:q[x]<0\text{ for all }0\ne x\in E\},
\]
with finite-dimensional subspaces \(E\) in the form domain. A finite strictly negative Gram matrix remains negative under sufficiently small
form-norm perturbations. Applying this to the gradient core, which is dense by definition, and to the odd physical form core proves
\[
 \boxed{\quad
 \nu_-(q_{PN},K_P)=\nu_-(\mathfrak a_o,\mathcal Q_H^{\rm odd}).
 \quad}                                                          \tag{21}
\]
This is an equality of negative indices via a common core. It does not identify the two completions or assert that every completed source divided
by \(m\) belongs to physical \(L^2\).

## 5. Pole rank-one inertia and physical negative eigenstates

The established odd null-payment vector satisfies
\[
 u_*=\frac{\psi}{m}\in D(H_o),\qquad
 H_ou_*=\frac12s,\qquad \langle s,u_*\rangle=\frac14.             \tag{22}
\]
For \(v\in\mathcal Q_H^{\rm odd}\), let \(a=4\langle s,v\rangle\), \(z=v-au_*\). Then \(z\perp s\) and
\[
 \mathfrak h_o[u_*,z]=\langle H_ou_*,z\rangle=0,\qquad
 \mathfrak h_o[u_*]=\frac18,\qquad \mathcal A_ou_*=0.
\]
Consequently
\[
 \boxed{\quad
 \mathfrak h_o[v]=\frac18|a|^2+\mathfrak h_o[z],\qquad
 \mathfrak a_o[v]=\mathfrak h_o[z],\qquad
 \nu_-(H_o)=\nu_-(\mathcal A_o).
 \quad}                                                          \tag{23}
\]
This is form-orthogonal splitting over \(\mathbb C u_*\) and \(\mathcal Q_H^{\rm odd}\cap s^\perp\). It is not a bounded operator congruence and
gives no eigenvalue correspondence.

If \(K=TT^*\) has an eigenvalue \(\lambda>1\) of multiplicity \(d\), \(T^*\) maps that eigenspace injectively to the \(\lambda\)-eigenspace of
\(T^*T\), preserving multiplicity. For a nonzero source vector \(u\) in the latter space,
\[
 q_{PN}[u]=\|u\|_P^2-\|Tu\|_N^2
          =(1-\lambda)\|u\|_P^2<0.                              \tag{24}
\]
Equations (21),(23) give \(\nu_-(H_o)\ge d\). To see that the transfer produces physical vectors, first approximate the resulting negative
\(\mathfrak a_o\)-subspace by compact smooth odd core vectors \(v_j\). Decompose \(v_j=a_j u_*+z_j\) as in (23). The corresponding \(z_j\)'s span
a strictly negative subspace for the \(H_o\) form, but need not be compactly supported. Approximate this finite \(z\)-basis again in the \(H_o\)
form norm by compact smooth odd vectors; strict negativity is preserved. This yields genuine physical negative directions without mapping
generalized Green-source vectors into \(L^2\).

The published [negative-band theorem](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md) has finite rank on every odd band
\(\mathbf1_{[-1/2,-\kappa]}(H_o)\), by parity-preserving extension, and \(H_o\ge-1/2\). The closure of the increasing union of these bands is the
negative spectral subspace. Each band is finite dimensional and invariant under \(H_o\), hence has an eigenbasis. A negative index at least \(d\)
therefore forces at least \(d\) genuine negative odd \(H_o\) eigenstates, counting multiplicity. Each selected eigenstate \(H_ow=\mu w\),
\(\mu<0\), lies in a published band with \(0<\kappa\le|\mu|\), so the derivative and double-exponential tail theorem applies to that actual
physical eigenvector. No generalized source is differentiated.

By the polar decomposition of \(T\), the nonzero spectral parts of \(TT^*\) and \(T^*T\) have equal multiplicities. Equations (21) and (23)
therefore give the exact total count
\[
 \operatorname{rank}\mathbf1_{(1,\infty)}(K)
 =\nu_-(I-T^*T)
 =\nu_-(q_{PN})
 =\nu_-(\mathfrak a_o)
 =\operatorname{rank}\mathbf1_{(-\infty,0)}(H_o),                              \tag{25}
\]
finite or infinite. This is a count only: it neither pairs an individual Green eigenvalue \(\lambda\) with a physical eigenvalue \(\mu\), nor
gives an eigenvalue/eigenspace correspondence. Since \(S_N\) is a reducing eigenvalue-one space, the desired critical assertion is exactly
\(K|_{S_N^\perp}\le I\). Neither this bound nor \(\ker(I-K)=S_N\) is proved. Nothing here settles the original even mean-zero block or RH.

## References

- [Original odd-domain and eigenstate identities](../20261013_odd_operator_domains/REPORT.md).
- [Actual negative-band regularity and finite-depth coverage](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md).
- [Positive reference inverse and strict Jacobi bound](../20261013_full_prime_green_reference/REFERENCE_INVERSE.md).
- [Finite full-prime Green comparison](../20261013_full_prime_green_reference/REPORT.md).
- [Compact excess and known-theta reducing space](../20261013_compact_green_excess/REPORT.md).
- [Reflected-prime energy and theta bounds](../20261013_reflected_prime_energy/REPORT.md).
