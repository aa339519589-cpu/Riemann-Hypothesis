# Domain-valid eigenstate identities and the reflected-energy metric obstruction

Date: 2026-10-13. The pole-payment identity reduces the true
odd source sign to nonnegativity of \(H_o\), the odd block of the
parity-preserving full closed realization
\(H_{\rm full}=M_m b(D_F)M_m-V\) on \(L^2(\mathbb R)\). The source gives an
exact second-derivative intertwining on the theta core. Actual negative odd
eigenstates can be brought into the common domains for the pole-free ladder
\(H_{\rm full}G^j w=\lambda(-G^*)^j w\) for every fixed \(j\). Its
parity-transfer Gram constraints give no sign contradiction. The pole-inclusive even-order identity also extends to these negative \(H_o\) eigenstates by the exact rank-one correction below. A
natural candidate metric, the reflected-prime energy \(N\), fails to make
the induced second derivative symmetric and does not descend to the quotient
by the \(N\)-kernel.

## Original normalization and dependencies

Use the complete positive even theta source
\[
 \Phi(x)=\sum_{n\ge1}(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
 \quad h=\cosh(x/2),\quad m^2=\Phi/(2h),\quad e_0=2mh.
\]
Write \(d_n=\log n\), \(\alpha_n=\Lambda(n)/\sqrt n\), and
\(\kappa(u)=e^{-u/2}/(1-e^{-2u})\) for \(u>0\).
The Fourier symbol, full prime shift, and bounded physical perturbation are
\[
 b(t)=\operatorname{Re}\psi_{\rm digamma}(1/4+it/2)-\psi_{\rm digamma}(1/4),
 \quad a(t)=b(t)-C_0,
 \quad C_0=\gamma_{\rm Euler}+\pi/2+3\log2+\log\pi,
\]
\[
 Sf(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
     [f(x+\log n)+f(x-\log n)],
 \qquad V=C_0M_{m^2}+M_mSM_m.
\]
The nonnegative kinetic form has the maximal domain
\[
 \mathcal Q_{\rm full}=\{v\in L^2(\mathbb R):
       b(D_F)^{1/2}(mv)\in L^2(\mathbb R)\},\qquad
 \mathfrak b[v]=\|b(D_F)^{1/2}(mv)\|_2^2.
\]
Its closed associated operator is \(B\); \(H_{\rm full}=B-V\) has
\(D(H_{\rm full})=D(B)\). The full weighted series for \(V\) converges in operator norm. Its bounds,
the source identity \(T\Phi=-h\), and the Gamma jump kernel are those of
[the original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md).
The fixed-depth Sobolev and spatial tail inputs are from
[the actual negative-band theorem](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md),
Parts I and II; the parity extension and all fixed-order domain passages
used here are proved below. Positivity of \(\psi=-\Phi'\) on the positive
half-line, its simple zero at zero, its complete theta asymptotic, and the
reflected-energy cutoff estimates are proved in
[the reflected-prime energy report](../20261013_reflected_prime_energy/REPORT.md).

For completeness the pole payment at the start is exact in the original
weighted Hilbert space. Put \(u_*=\psi/m\) and \(s=m\sinh(x/2)\).
The theta tails put \(u_*\) in the odd operator domain, and the source
identity gives \(H_ou_*=s/2\), \(\langle s,u_*\rangle=1/4\),
\(H_o[u_*]=1/8\). If \(H_o\ge0\), its form Cauchy--Schwarz inequality gives
\(2|\langle s,v\rangle|^2\le H_o[v]\), so
\(\mathcal A_o=H_o-2|s\rangle\langle s|\ge0\). The converse follows by
adding the positive rank-one term. This equivalence does not prove either
sign.

## Pole-inclusive source commutation

Let \(\partial=d/dx\), let \(D_F=-i\partial\) denote the self-adjoint Fourier multiplier, \(T=a(D_F)-S\), \(s_0(x)=\sinh(x/2)\), and
\[
\ell(f)=\int_{\mathbb R}s_0(x)f(x)\,dx,\qquad
\mathcal A_s f=Tf-2s_0\,\ell(f).
\]
On the full theta source/core class, \([T,\partial^2]=0\). Integration by parts
gives
\[
\ell(\partial^2 f)=\int s_0 f''=\int s_0''f=\frac14\ell(f),
\qquad \partial^2s_0=\frac14s_0.
\]
Therefore the *complete* coefficient-two polar source operator satisfies
\[
\boxed{\quad \mathcal A_s\partial^2=\partial^2\mathcal A_s.\quad}\tag{1}
\]
No prime label is cut off in this identity; the commutation is termwise for
the translation-invariant full shift sum and passes to theta/core pairings
by the complete tail bounds.

For every \(j\ge0\), let \(g_j=\Phi^{(2j+1)}\). The theta source equations
and integration by parts yield
\[
Tg_j=-\frac12\,4^{-j}s_0,\qquad
\ell(g_j)=-\frac14\,4^{-j},\qquad
\mathcal A_sg_j=0.
\tag{2}
\]
This is the full odd theta-derivative null family. The smaller combinations
\(f_j=\Phi^{(2j+3)}-\frac14\Phi^{(2j+1)}\) satisfy \(Tf_j=0\) and
\(\ell(f_j)=0\); they are null for the pole-free source operator as well.

## Physical \(G^2\) intertwining and its exact scope

With \(m^2=\Phi/(2h)\), \(h=\cosh(x/2)\),
\(\rho=-\Phi'/\Phi\), and \(\tau=\tanh(x/2)\), put
\[
\sigma(x)=\frac12\rho(x)+\frac14\tau(x),\qquad
G=m^{-1}\partial m=\partial-\sigma
\]
on \(C_c^\infty(\mathbb R)\). The formal \(L^2(dx)\) adjoint is
\(G^*=-\partial-\sigma\). The physical pole-inclusive odd form/operator is
\[
\mathcal A_o=H_o-2|s\rangle\langle s|,\qquad s=m s_0,
\]
and is represented from the source by \(m\mathcal A_s m\).
Since
\[
mG^2w=\partial^2(mw),\qquad G^{*2}=m\partial^2m^{-1},
\]
(1) gives the core identity
\[
\boxed{\quad \mathcal A_oG^2=G^{*2}\mathcal A_o.\quad}\tag{3}
\]
It is a symmetry relation for the *indefinite* form \(\mathcal A_o\).
If \(\mathcal A_o\) were already known nonnegative, and its operator domain
were invariant under \(G^2\), its form would provide a positive metric on
the quotient by its full nullspace, and (3) would make \(G^2\) symmetric
on the induced domain. Using that metric to prove nonnegativity would be
circular; neither nonnegativity nor quotient-domain invariance is asserted.

The null vectors in (2) are preserved by \(G^2\):
\[
G^2(g_j/m)=g_{j+1}/m.
\tag{4}
\]
Thus (3) is compatible with an infinite-dimensional odd null family; it
does not force the null family to be total or the quotient to vanish.

For the pole-free full physical operator, translation invariance gives a
separate first-order core relation:
\[
H_{\rm full}=M_mTM_m,\qquad
H_{\rm full}G=-G^*H_{\rm full}.
\]
Indeed \(mG=\partial m\), \(G^*=-m\partial m^{-1}\), and \(T\partial=\partial T\). This is the core
identity used below on actual negative eigenstates.

## Fixed-order derivative ladder on an actual negative odd eigenstate

There is a domain gap between the logarithmic source form domain and the
first-order expression \(G=\partial-\sigma\): the former does not itself control
\(\partial w\) or \(\sigma w\). For a *genuine odd* eigenvector \(H_ow=\lambda w\),
\(\lambda<0\), normalize \(\|w\|_2=1\). The actual-band estimates supply enough extra regularity for
every fixed-order pole-free \(G\)-identity.

For clarity, the domain extension used here is the full parity-preserving
form \(B=M_m b(D_F)M_m\) on \(L^2(\mathbb R)\), with bounded complete
\(V\). Its even and odd subspaces reduce both \(B\) and \(V\). The
cutoff/mollification graph-core proof applies to both parities: for
\(\chi_R(x)=\chi(x/R)\), the Gamma jump kernel gives
\(\|[b(D_F),\chi_R]\|_{2\to2}\le C/R\), using
\(\int |x|\kappa(|x|)\,dx<\infty\). In associated-form pairings,
\[
 B\chi_Rv=\chi_RBv+m[b(D_F),\chi_R]mv\qquad(v\in D(B)).
\]
More explicitly, multiplication by \(\chi_R\) preserves the Gamma form
domain by the jump-form estimate for \(\chi_R(x)-\chi_R(y)\). With
\(\mathfrak b\) the associated form (conjugate-linear in its first slot),
\[
 \mathfrak b(z,\chi_Rv)=\mathfrak b(\chi_Rz,v)
   +\langle mz,[b(D_F),\chi_R]mv\rangle
 \qquad(z\text{ in the form domain}).
\]
The right side is represented by the stated physical \(L^2\) vector.
The bounded commutator first shows \(\chi_Rv\in D(B)\); its norm tends
to zero and \(\chi_R\to I\) strongly, giving convergence in the graph
norm. This does not presume \(mv\in D(b(D_F))\) for arbitrary \(v\in D(B)\).
For a compactly supported source
\(f=m\chi_Rv\), \(b(D_F)f\) is locally \(L^2\) by dividing \(B\chi_Rv\) by
the positive \(m\) on an expanded compact interval; outside that interval
it equals the exponentially decaying kernel tail \(-\kappa*f\). Mollifying
\(f\) in the \(b\)-graph norm and dividing by \(m\) on its common compact
support gives the smooth graph core. The complete-prime norm tail is unchanged. The
regularity and localization estimates in [ACTUAL_NEGATIVE_BAND_COVERAGE.md](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md)
use these parity-preserving bounds and the same constants on the odd block.

Fix \(0<\kappa\le|\lambda|\) and put \(Y=e^{2R}\). The reviewed
negative-band regularity and whole-band localization estimates were stated
for the original even realization in
[ACTUAL_NEGATIVE_BAND_COVERAGE.md](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md), Parts I–II. Their cutoff, commutator, and
prime-tail proofs are parity-blind and apply to the odd block as well:
the full form and all cutoffs preserve parity, and an odd vector is
automatically orthogonal to the even ground. Thus \(w\in H^r(\mathbb R)\)
for every fixed \(r\), with, for every sufficiently large cutoff radius \(R\),
the estimate
\[
\|1_{\{|x|\ge R\}}w\|_2^2
\le \frac{D(R)^2}{\kappa^2}+\frac{2E(R)}{\kappa},
\quad
D(R)=70000Y^{5/4}e^{-\pi Y/2},\qquad
E(R)=70Y^{3/4}e^{-\pi Y/2},
\tag{5}
\]
which decay faster than every exponential in \(R\) for fixed \(\kappa\).
For weighted derivatives, choose smooth even cutoffs \(\eta_R\) that vanish
on \(|x|\le R-1\), equal one on \(|x|\ge R\), and have uniform derivative
bounds. Put
\[
T_\kappa(R)=
\left(\frac{D(R)^2}{\kappa^2}+\frac{2E(R)}{\kappa}\right)^{1/2}.
\]
Then \(\|\eta_Rw\|_2\le T_\kappa(R-1)\) and the band regularity theorem gives
\(\|\eta_Rw\|_{H^s}\le C_sM_s(\kappa)\). For every integer \(0\le\ell<s\),
Gagliardo–Nirenberg interpolation yields
\[
\|1_{\{|x|\ge R\}}\partial^\ell w\|_2
\le C_{s,\ell}T_\kappa(R-1)^{1-\ell/s}
M_s(\kappa)^{\ell/s}.
\tag{5a}
\]
Thus \(e^{a|x|}\partial^\ell w\in L^2\) for every fixed \(a,\ell\). The theta
derivative bounds give
\[
\left|\frac{m^{(k)}}m\right|
+\left|m(m^{-1})^{(k)}\right|\le C_ke^{2k|x|}.
\]
Consequently \(G^jw,(-G^*)^jw\in L^2\) for every fixed \(j\). Smooth spatial cutoffs and mollification also converge in each
of these differential graph norms: on a cutoff shell,
\([G,\chi_R]=\chi_R'\), and the higher commutators contain only bounded
cutoff derivatives times lower iterates, whose weighted tails tend to zero.
Thus the powers here are actual differential-operator powers on these
vectors, not merely symbolic expressions. Also
\(\partial^j(mw)\in H^1\), so \(G^jw\) lies in the logarithmic Gamma form
domain. The complete prime series is locally normally differentiable on
\(mw\); using \(T\partial^j=\partial^jT\) and the eigen-equation gives
\[
\begin{aligned}
H_{\rm full}G^jw
&=mT \partial^j(mw)
=m\partial^jT(mw)\\
&=\lambda m\partial^j(m^{-1}w)
=\lambda(-G^*)^jw.
\end{aligned}\tag{5b}
\]
The source eigen-equation \(T(mw)=\lambda w/m\) here is local and
distributional; neither \(w/m\) nor \(T(mw)\) is claimed to lie in global
\(L^2\). Pair the distributional identity with compact smooth physical
tests. Pairing \(w_j=G^jw\) against a compact smooth \(z\) gives explicitly
\[
 \mathfrak h(z,w_j)=\langle mz,b(D_F)\partial^j(mw)\rangle
 -\langle z,Vw_j\rangle
 =\langle z,mT\partial^j(mw)\rangle.
\]
Here \(b(D_F)\partial^j(mw)\in L^2\) and \(Vw_j\in L^2\); the final
expression denotes this physical representative even when the unweighted
source \(T\partial^j(mw)\) is not globally square integrable. Since \(G^jw\) is in the form domain, its closed-form pairing is
continuous there; the right side of (5b) is in physical \(L^2\).
The graph-core proof also gives a form core, so this equality extends to
all form-domain tests. The associated-form operator criterion places every
fixed \(G^jw\) in \(D(H_{\rm full})\). The constants can depend on
\(\kappa,j\); there is no uniform-in-\(j\) assertion. This eigenstate
ladder does not assert a global bounded \(G\)-flow or extend the core
identity to every vector in the logarithmic form domain.

At \(j=1\), the ladder gives
\[
w\in D(G)\cap D(G^*),\quad Gw\in D(H_{\rm full}),\qquad
H_{\rm full}Gw=-\lambda G^*w.
\tag{5c}
\]

Taking the \(H\)-form against \(Gw\) in the \(j=1\) case of (5c) yields the exact parity-transfer
identity
\[
\boxed{\quad
H_e[Gw]=\lambda\bigl(\|w'\|_2^2-\|\sigma w\|_2^2\bigr).
\quad}\tag{7}
\]
The virial identity from (5c) is
\(\int \sigma(x)|w(x)|^2dx=0\); for odd \(w\) it also follows directly
from oddness of \(\sigma\) and evenness of \(|w|^2\). It gives no sign for
the difference in (7).

The ground component of the even partner is known exactly:
\[
\langle e_0,Gw\rangle=-\ell(mw)
=-2\lambda\langle u_*,w\rangle,\qquad
e_0=2mh,\quad u_*=\psi/m.
\tag{8}
\]
The first equality follows from \(e_0Gw=2h(mw)'\) and one integration by
parts. The second follows from \(H_ou_*=\frac12s\) and self-adjointness.
Thus the odd eigenstate's image under \(G\) has ground component \(O(|\lambda|)\)
when \(\|w\|_2=1\).

The certified even mean-zero bound \(H_e\ge-1/100000\) from
[FINITE_HEIGHT_GAP.md](../20261012_adaptive_spectral_tail/FINITE_HEIGHT_GAP.md), applied only to the even vector
\(Gw-\langle e_0,Gw\rangle e_0\), gives, with
\(\delta=1/100000\),
\[
H_e[Gw]\ge-\delta\|Gw\|_2^2
-\left(\frac12-\delta\right)
|\langle e_0,Gw\rangle|^2.
\tag{9}
\]
Combining (7)–(9) yields a necessary estimate on
\(\|w'\|^2-\|\sigma w\|^2\), but no contradiction. The global positive
jump representation gives only \(\lambda\ge-\frac12\) for an odd
eigenstate; the even mean-zero gap applies to \(Gw\), not to \(w\). The
sign/magnitude of the derivative-minus-drift quantity is not controlled by
the selected-state Sobolev bounds. In the common case
\(\|\sigma w\|\ge\|w'\|\), (7) is nonnegative and is entirely compatible
with (9). In the other case, ruling out the eigenstate requires a
quantitative comparison of the derivative excess with the mean-zero
component of \(Gw\); no such estimate follows from (5). No bound on this operator ratio follows from the proved fixed-depth estimates.

The full fixed-order ladder records an infinite sequence of cross-Gram
constraints. Define these only in the physical Hilbert space:
\[
C_j(w)=\operatorname{Re}\langle G^jw,(-G^*)^jw\rangle_{L^2},\qquad
N_j(w)=\|G^jw\|_2^2.
\]
By (5b),
\[
H_{\rm full}[G^jw]=\lambda C_j(w),\qquad
C_0(w)=\|w\|_2^2,\qquad
C_1(w)=\|w'\|_2^2-\|\sigma w\|_2^2.
\tag{10}
\]
The last identity follows by expanding \(Gw=w'-\sigma w\) and
\((-G^*)w=w'+\sigma w\); the mixed term is purely imaginary. Locally the
physical pairing for general \(j\) can be written
\(\operatorname{Re}\int\overline{\partial^j(mw)}\partial^j(m^{-1}w)\,dx\), but this is
only an \(L^1\) product defined by the physical \(L^2\) pairing; \(m^{-1}w\)
and its source derivatives are not asserted to be in \(L^2\). There is no
sign for the higher \(C_j\) from the factorization.

For the lower bound used in even \(j\), the \(\Phi\)-ground identity is
available on both parities. With \(Uq=\sqrt{2\Phi h}\,q\),
\[
H_{\rm full}[Uq]=\mathcal E(q)-\frac12\|Uq\|_2^2,\qquad
\mathcal E(q)=\mathcal E_\Gamma(q)+\mathcal E_P(q)\ge0,
\tag{10a}
\]
Here the full positive energies are
\[
 \mathcal E_\Gamma(q)=\tfrac12\iint\Phi(x)\Phi(y)\kappa(|x-y|)
       |q(x)-q(y)|^2dxdy,
\]
\[
 \mathcal E_P(q)=\sum_{n\ge2}\alpha_n\int\Phi(x)\Phi(x+d_n)
       |q(x)-q(x+d_n)|^2dx.
\]
For compact smooth \(q\), expanding these squares gives, with \(f=\Phi q\),
\(\mathcal E_\Gamma=\langle f,b(D_F)f\rangle-
\int\Phi|q|^2b(D_F)\Phi\) and
\(\mathcal E_P=\int\Phi|q|^2S\Phi-\langle f,Sf\rangle\).
Their sum is \(H_{\rm full}[Uq]+\int\Phi h|q|^2\), proving (10a).
The full smooth form core extends its lower bound to the closed form. The algebraic source identity
\(S\Phi=a(D_F)\Phi+h\) proving (10a) has no parity restriction. Thus
\(H_{\rm full}\ge-\frac12 I\) on odd and even vectors; this does not infer
an odd gap from the certified even mean-zero theorem.

For even \(j\), \(G^jw\) is odd and the full jump representation gives
\[
\lambda C_j(w)\ge-\frac12N_j(w).
\tag{11}
\]
For odd \(j\), \(G^jw\) is even. Put \(f=mw\). Its ground coordinate is
\[
c_j:=\langle e_0,G^jw\rangle
=2(-1)^j\int h^{(j)}(x)f(x)\,dx
=(-1)^j2^{2-j}\lambda\langle u_*,w\rangle,
\qquad |c_j|^2=2^{4-2j}\lambda^2|\langle u_*,w\rangle|^2.
\tag{12}
\]
The even-gap certificate therefore yields only
\[
\lambda C_j(w)\ge-\delta N_j(w)
-\left(\frac12-\delta\right)
2^{4-2j}\lambda^2|\langle u_*,w\rangle|^2
\qquad(j\text{ odd}).
\tag{13}
\]
These infinitely many inequalities supply no contradiction to \(\lambda<0\) from the stated bounds alone:
they bound cross-Gram moments relative to \(N_j\), but do not give the
needed sign or a uniform comparison of \(C_j/N_j\) as \(j\) grows. The
actual band bounds legalize each fixed \(j\); their constants depend on
\(j,\kappa\). Thus the ladder alone does not exclude negative odd inertia.

## The pole-inclusive identity on these actual eigenstates

The fixed-order domain result also pays the pole in every even order. For
\(s=m\sinh(x/2)\), the true adjoint differential powers satisfy
\[
 (G^*)^{2r}s=m\partial^{2r}\sinh(x/2)=4^{-r}s\qquad(r\ge0).
\]
These are actual \(L^2\) vectors in the successive adjoint domains, by
the theta tail. The weighted derivative bounds and integration by parts
then give
\(\langle s,G^{2r}w\rangle=4^{-r}\langle s,w\rangle\).
The bounded pole perturbation has the same domain as \(H_o\), and
\(G^{2r}w\in D(H_o)\). Also
\(\mathcal A_ow=\lambda w-2s\langle s,w\rangle\) belongs to
\(D((G^*)^{2r})\). Consequently all terms in the following identity
are in the original physical \(L^2\):
\[
 \boxed{
 \mathcal A_oG^{2r}w
 =\lambda(G^*)^{2r}w-2\,4^{-r}s\langle s,w\rangle
 =(G^*)^{2r}\mathcal A_ow.}
 \tag{13a}
\]
This proves the even-order pole-inclusive identity for a genuine negative
\(H_o\) eigenvector, beyond its initial compact-core statement. It does
not declare that \(w\) is an eigenvector of \(\mathcal A_o\), and does
not extend the identity to every vector in the maximal form domain.
The metric defined by \(\mathcal A_o\) still has unproved sign.

## The reflected-prime energy is not an independent \(G^2\) metric

On the positive ratio core \(r=g/\psi\), let
\[
L(x)=\sum_{n>e^x}\alpha_n\psi(d_n-x),\qquad
V_N(x)=\frac{L(x)}{\psi(x)},\qquad d_n=\log n.
\]
The complete reflected-prime form, written in the positive source
coordinates \(g=\psi r\), has polarization. In (14), \(g,h\) denote the
positive-wing restrictions of odd sources:
\[
N_s[g,h]=
2\int_0^\infty V_N(x)\overline{g(x)}h(x)\,dx
-2\sum_{n\ge2}\alpha_n\int_0^{d_n}
\overline{g(x)}h(d_n-x)\,dx.
\tag{14}
\]
For compact smooth positive-wing source functions \(g,h\), with odd
extensions, compare \(\partial^2\) in the two slots and integrate by parts. The
exact defect is
\[
\boxed{\begin{aligned}
N_s[g,\partial^2h]-N_s[\partial^2g,h]
={}&-2\int_0^\infty V_N'(x)
\bigl(\overline{g(x)}h'(x)-\overline{g'(x)}h(x)\bigr)\,dx\\
&-2\sum_{n\ge2}\alpha_n
\bigl(\overline{g'(0)}h(d_n)-\overline{g(d_n)}h'(0)\bigr).
\end{aligned}}\tag{15}
\]
The second line is the half-line endpoint term; commutation of \(\partial^2\)
with the point reflection \(x\mapsto d_n-x\) does not remove it.

The first line is already nonzero on a small interior test. For
\(0\le x<\frac12\log2\), every prime-power label is active in \(L(x)\).
The theta tails make this fixed-label sum locally normally convergent with
all derivatives, so
\(L(x)=L_0+L_1x+O(x^2)\) and \(L'(x)=L_1+O(x)\), with \(L_0>0\).
Also \(\psi(x)=c_\psi x+O(x^3)\) and
\(\psi'(x)=c_\psi+O(x^2)\). Therefore
\[
V_N(x)=\frac{L_0}{c_\psi x}+O(1),\qquad
V_N'(x)=-\frac{L_0}{c_\psi x^2}+O(1)<0
\]
on some sufficiently small interval \((0,\epsilon)\subset(0,\frac12\log2)\).
Choose
\(\chi\in C_c^\infty((0,\epsilon))\), nonzero, and put \(g=\chi\),
\(h=x\chi\). Then
\(\bar g h'-\bar g'h=\chi^2\), and all endpoint terms in (15) vanish
because both tests are supported below \(\log2\). The defect is nonzero.
So \(N_s\) is not \(\partial^2\)-symmetric even on the compact core.

There is a second quotient obstruction. In the ratio variable \(r\), the
\(N\)-seminorm annihilates constants. Its reflection centers \(d_n/2\)
generate a dense additive
translation group (use \(\log2\) and \(\log3\)), so on smooth functions its
kernel consists only of constants. The induced ratio operator is
\[
\mathcal B_\psi r=\psi^{-1}\partial^2(\psi r).
\]
But
\[
\mathcal B_\psi 1=\frac{\psi''}{\psi}
=\frac14-r_0,\qquad r_0=\frac{f_0}{\psi},
\tag{16}
\]
which is nonconstant and has positive \(N\)-energy. Indeed, the first theta
term gives \(r_0(x)\sim-4(\pi e^{2x})^2\) as \(x\to+\infty\). Thus
\(\mathcal B_\psi\)
does not preserve the \(N\)-kernel and is not even well-defined on the
quotient by that kernel. Quotienting further by the entire theta-jet
nullspace could change the domain or require a projected metric, but the
raw \(N\)-form does not descend to that quotient: for example, \(r_0\) is a
pole-inclusive source-null jet with \(N[r_0]>0\). The known real-zero dual
functionals also show that the theta jets are not total in the
\(N\)-completion.

## The induced derivative is not closable in the unprojected energy space

This failure already occurs for a densely defined operator on the compact
ratio-core gradient image, without assigning a noncompact representative to
an arbitrary completed vector. Write
\[
 K_N=\overline{\{\nabla_N r:r\in\mathcal C\}},\qquad
 Z_0(\nabla_N r)=\nabla_N(\mathcal B_\psi r).
\]
The compact ratio-core gradient map is injective: if \(N[r]=0\),
choose an actual prime power \(2^j\) with \(j\log2\) more than twice the
support radius of \(r\). Its reflected partner of each supported positive
\(x\) is outside that support, and positivity of the edge weight forces
\(r(x)=0\). Thus \(Z_0\) is well-defined on this dense gradient domain. The expression
\(\mathcal B_\psi r\) is again in this core: near zero both \(\psi r\)
and its second derivative are odd, and division by the simple odd zero
of \(\psi\) leaves a smooth even ratio.

Take smooth even \(\chi_R\), equal to one for \(|x|\le R\), zero for
\(|x|\ge R+1\), with uniformly bounded fixed-order derivatives. The
complete reflected-energy bound
\[
 N[u]\le4\int_0^\infty\psi(x)L(x)|u(x)|^2dx,
 \qquad L(x)\le C(1+x)e^{x/2},
\]
and the theta tail show
\(\nabla_N\chi_R\to0\), since it equals the gradient of \(\chi_R-1\).
On the other hand,
\[
 \mathcal B_\psi\chi_R
 =\chi_R(1/4-r_0)+2\chi_R'\,\psi'/\psi+\chi_R''.
\]
The first term converges in \(N\)-energy to \(1/4-r_0\). The last two
terms are supported in \([R,R+1]\) and have size \(O(e^{2x})\); their
\(N\)-energies tend to zero by the same displayed bound. Therefore
\[
 \nabla_N\chi_R\longrightarrow0,\qquad
 Z_0(\nabla_N\chi_R)\longrightarrow-\nabla_Nr_0\ne0.
 \tag{17}
\]
To see the last nonvanishing without any completeness assertion, keep
\(x\) in a fixed positive compact interval and choose a sufficiently large
actual prime power \(n=2^j\). Then
\(r_0(\log n-x)\to-\infty\) uniformly there by its theta asymptotic,
while \(r_0(x)\) is bounded and both edge weights are positive. At least
one term of \(N[r_0]\) is strictly positive; its finiteness was already
proved by the same complete theta bound.

Equation (17) is an explicit failure of closability of \(Z_0\). It rules
out extending this unprojected reflected-energy differential operator to a
closed self-adjoint operator while retaining its entire compact core.
Projecting away the closed theta-jet gradient span removes the particular
limit \(\nabla_Nr_0\). The argument therefore makes no assertion about
closability or symmetry after that additional projection, nor about the
sign of the original Weil form.

## What the full identity says, and what remains

The nonzero defect (15) must be canceled by the other pieces when they are
combined into \(P-N\): the full pole-inclusive source form commutes with
\(\partial^2\) by (1). In particular the complete forward-prime and Gamma/pole
contributions cannot be dropped while trying to build an independent
positive metric from reflected edges. Their exact cancellation reproduces
\(\mathcal A_o\), whose positivity is the target itself.

The checked results therefore give the actual pole-free eigenstate ladder at every fixed order, its pole-inclusive even-order counterpart on the same eigenstates, and a concrete failure of
the unprojected \(N\)-metric shortcut. They neither exclude a negative odd
eigenstate nor prove \(H_o\ge0\). A successful route still needs a positive
metric on a precisely defined quotient that is independent of the unknown
sign of \(\mathcal A_o\), or uniform control of the full cross-Gram sequence
\(C_j(w)/N_j(w)\) from (10)–(13). No global source closability,
theta-null completeness, off-critical source, or finite-matrix sign is
assumed.
