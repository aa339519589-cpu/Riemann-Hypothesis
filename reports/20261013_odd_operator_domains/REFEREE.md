# Referee note: fixed-order derivative ladder and reflected-energy obstruction

## Scope

For the parity-preserving full-line realization, the fixed-order pole-free
derivative ladder is valid on a genuine odd negative eigenstate. The
unprojected reflected-prime energy is not a symmetric metric for the
induced second derivative; that derivative operator on the dense
compact-core gradient image is not closable. These results invalidate the
unprojected \(N\)-metric route to a positive spectrum. They prove neither
nonnegativity of the original odd Weil form nor RH. The pole-inclusive
second-order intertwining is a core identity in general and extends to
even powers on a genuine negative eigenstate by an explicit rank-one
payment; this does not make the eigenstate an eigenvector of the
pole-corrected operator.

Throughout the reflected-edge formulas, set
\(d_n=\log n\), \(\alpha_n=\Lambda(n)/\sqrt n\), and
\(\kappa(u)=e^{-u/2}/(1-e^{-2u})\) for \(u>0\).

## Full realization and the fixed-order ladder

Use the Fourier convention for which \(D_F=-i\partial_x\) is the
self-adjoint multiplier with symbol \(t\). Let
\[
m(x)^2=\frac{\Phi(x)}{2\cosh(x/2)},\qquad
H_{\rm full}=M_m b(D_F)M_m-V,
\]
where \(b\) is the complete Gamma multiplier and \(V\) is the bounded
complete-prime perturbation, including every prime power. The closed
full-line form is parity reducing and has the positive theta jump
representation
\[
H_{\rm full}[Uq]=\mathcal E(q)-\frac12\|Uq\|_2^2,\qquad
Uq=\sqrt{2\Phi(x)\cosh(x/2)}\,q,\qquad \mathcal E(q)\ge0.
\tag{1}
\]
Thus \(H_{\rm full}\ge-\frac12 I\) on both parity blocks. Its operator
graph core can be taken to be compact smooth functions in each parity.
For a smooth even spatial cutoff \(\chi_R(x)=\chi(x/R)\), the Gamma jump
kernel and its finite first moment give
\[
\|[b(D_F),\chi_R]\|_{2\to2}
\le\|\chi_R'\|_\infty\int_{\mathbb R}|u|\kappa(|u|)\,du
=O(R^{-1}).
\]
In associated-form pairings,
\[
\mathfrak b(z,\chi_Rv)=\mathfrak b(\chi_Rz,v)
+\langle M_mz,[b(D_F),\chi_R]M_mv\rangle .
\]
For \(v\in D(B)\), this yields
\[
B\chi_Rv=\chi_RBv+M_m[b(D_F),\chi_R]M_mv.
\]
Hence the cutoff converges in graph norm without assuming
\(M_mv\in D(b(D_F))\). If \(v\) is compactly supported and \(f=M_mv\),
then \(b(D_F)f=Bv/M_m\) locally in \(L^2\); outside a fixed collar of the
support its kernel is the exponentially decaying off-support convolution
\(-\kappa*f\). Even mollification of \(f\) converges both in \(L^2\) and
in the \(b(D_F)\) graph norm. Dividing the mollifications by positive
smooth \(M_m\) on a common compact support gives the parity-preserving
smooth graph core. A bounded perturbation preserves this core for
\(H_{\rm full}\).

Let \(\partial=\partial_x\), and set
\[
T=a(D_F)-S,\qquad
G=M_m^{-1}\partial M_m=\partial-\sigma,\qquad
\sigma=\frac12\frac{-\Phi'}{\Phi}+\frac14\tanh(x/2).
\tag{2}
\]
The formal physical adjoint is \(G^*=-\partial-\sigma\), and
\(H_{\rm full}=M_mTM_m\) in the source-form sense. Translation invariance
gives \(T\partial^j=\partial^jT\) on the theta/source core and locally on
the smooth theta-decaying sources below. In particular,
\[
H_{\rm full}G=-G^*H_{\rm full}.
\tag{3}
\]

Suppose \(w\) is a genuine odd eigenvector with
\(H_{\rm full}w=\lambda w\), \(\lambda<0\), and \(\|w\|_2=1\). Put
\(\kappa=|\lambda|\). The actual negative-band regularity and full-space
localization estimates give, for every fixed \(s\), a finite
\(M_s(\kappa)\) with \(\|w\|_{H^s}\le M_s(\kappa)\), and
\[
\|1_{\{|x|\ge R\}}w\|_2^2
\le \frac{D(R)^2}{\kappa^2}+\frac{2E(R)}{\kappa},
\quad
D(R)=70000e^{5R/2}e^{-\pi e^{2R}/2},\quad
E(R)=70e^{3R/2}e^{-\pi e^{2R}/2}.
\tag{4}
\]
These full-space cutoff bounds apply to odd eigenvectors and do not use
the even signed-prime moment cancellation. The inputs are in the
repository reports [ACTUAL_NEGATIVE_BAND_COVERAGE.md](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md)
and [SIGNED_PRIME_LOW_SPECTRUM.md](../20261012_adaptive_spectral_tail/SIGNED_PRIME_LOW_SPECTRUM.md).

Choose smooth even cutoffs \(\eta_R\) that vanish on \(|x|\le R-1\), equal
one on \(|x|\ge R\), and have uniformly bounded derivatives. Define
\[
T_\kappa(R)=\left(D(R)^2/\kappa^2+2E(R)/\kappa\right)^{1/2}.
\]
Then \(\|\eta_Rw\|_2\le T_\kappa(R-1)\) and
\(\|\eta_Rw\|_{H^s}\le C_sM_s(\kappa)\). Fourier interpolation gives, for
integers \(0\le j<s\),
\[
\|1_{\{|x|\ge R\}}\partial^j w\|_2
\le C_{s,j}T_\kappa(R-1)^{1-j/s}M_s(\kappa)^{j/s}.
\tag{5}
\]
For each fixed derivative order this still decays faster than every
exponential in \(R\). The theta coefficient bounds show that
\(M_m^{(j)}/M_m\) and \(M_m\partial^j(M_m^{-1})\) grow at most
exponentially for each fixed \(j\). Consequently
\[
G^jw,\quad (-G^*)^jw\in L^2(\mathbb R)
\qquad\text{for every fixed }j.
\tag{6}
\]
Cutoff and mollification also converge in each fixed differential graph
norm: cutoff commutators contain bounded cutoff derivatives times lower
powers, whose weighted tails vanish. Moreover
\(M_mG^jw=\partial^j(M_mw)\in H^1\), so each \(G^jw\) is in the
logarithmic Gamma form domain.

The source eigen-equation \(T(M_mw)=\lambda M_m^{-1}w\) is used locally
as a distributional identity. The complete prime sum and its fixed
derivatives converge locally normally on \(M_mw\); neither
\(M_m^{-1}w\) nor \(T(M_mw)\) is asserted to be globally \(L^2\). For a
compact smooth physical test \(z\), the closed-form pairing is
\[
\mathfrak h(z,G^jw)
=\langle M_mz,b(D_F)\partial^j(M_mw)\rangle
-\langle z,VG^jw\rangle
=\langle z,M_mT\partial^j(M_mw)\rangle .
\tag{7}
\]
The right side is the physical \(L^2\) vector
\(\lambda(-G^*)^jw\), by (5) and local derivative commutation. The
same-parity form core and associated-form operator criterion therefore
give the actual fixed-order ladder
\[
\boxed{\quad
H_{\rm full}G^jw=\lambda(-G^*)^jw,\qquad j=0,1,2,\ldots\ \text{fixed}.
\quad}
\tag{8}
\]
The constants may depend on \(\kappa\) and \(j\); there is no uniform
in-order or critical-depth assertion. At first order,
\[
H_{\rm full}[Gw]
=\lambda\left(\|w'\|_2^2-\|\sigma w\|_2^2\right).
\tag{9}
\]
No sign for the derivative-minus-drift quantity follows from the stated
bounds. The fixed-order ladder therefore does not exclude a negative odd
eigenvalue.

The pole-inclusive source operator
\[
\mathcal A_sf=Tf-2\sinh(x/2)\ell(f),\qquad
\ell(f)=\int_{\mathbb R}\sinh(x/2)f(x)\,dx,
\]
commutes with \(\partial^2\) on theta/core pairings because
\(\partial^2\sinh(x/2)=\sinh(x/2)/4\) and
\(\ell(\partial^2f)=\ell(f)/4\). With
\(s=M_m\sinh(x/2)\) and \(\mathcal A_o=H_o-2|s\rangle\langle s|\),
this gives the core identity
\[
\mathcal A_oG^2=G^{*2}\mathcal A_o.
\tag{10}
\]
This is an indefinite core intertwining. On a genuine negative eigenstate,
the fixed-order ladder pays the pole in every even order. Since
\[
(G^*)^{2r}s=M_m\partial^{2r}\sinh(x/2)=4^{-r}s,
\]
the theta tail puts these vectors in the required adjoint domains, and
adjointness gives
\(\langle s,G^{2r}w\rangle=4^{-r}\langle s,w\rangle\). With
\(H_ow=\lambda w\), \(G^{2r}w\in D(H_o)\), and
\(\mathcal A_ow=\lambda w-2s\langle s,w\rangle\in D((G^*)^{2r})\),
one obtains the actual identity
\[
\boxed{\quad
\mathcal A_oG^{2r}w
=\lambda(G^*)^{2r}w-2\,4^{-r}s\langle s,w\rangle
=(G^*)^{2r}\mathcal A_ow,
\qquad r\ge0\text{ fixed}.
\quad}
\tag{10a}
\]
This uses the pole-free eigenstate ladder and the rank-one eigenvalue
calculation; it does not assert that \(w\) is an eigenvector of
\(\mathcal A_o\), extend (10) to every vector in the maximal form
domain, or prove \(\mathcal A_o\ge0\).

## The reflected-prime energy is not a symmetrizing metric

On the positive ratio core, let \(r=g/\psi\), where
\(\psi=-\Phi'>0\) on \((0,\infty)\), and put
\[
L(x)=\sum_{n>e^x}\alpha_n\psi(d_n-x),\qquad
V_N(x)=L(x)/\psi(x),\qquad
d_n=\log n,\quad \alpha_n=\Lambda(n)/\sqrt n.
\]
The complete reflected form, in the positive source coordinates
\(g=\psi r\), is
\[
N_s[g,h]
=2\int_0^\infty V_N(x)\overline{g(x)}h(x)\,dx
-2\sum_{n\ge2}\alpha_n\int_0^{d_n}
\overline{g(x)}h(d_n-x)\,dx.
\tag{11}
\]
For compact odd source tests, integration by parts gives the complete
prime-power defect
\[
\begin{aligned}
N_s[g,\partial^2h]-N_s[\partial^2g,h]
={}&-2\int_0^\infty V_N'(x)
  (\overline g h'-\overline{g'}h)(x)\,dx\\
&-2\sum_{n\ge2}\alpha_n
  (\overline{g'(0)}h(d_n)-\overline{g(d_n)}h'(0)).
\end{aligned}
\tag{11a}
\]
The second line is the half-line reflection endpoint term. Near zero,
\(\psi(x)=c_\psi x+O(x^3)\), \(c_\psi>0\), and
\(L(x)=L_0+L_1x+O(x^2)\), with \(L' (x)=L_1+O(x)\) by locally normal convergence of the complete theta-derivative sum, where
\(L_0=\sum_{n\ge2}\alpha_n\psi(d_n)>0\). Hence
\[
V_N'(x)=-\frac{L_0}{c_\psi x^2}+O(1)<0
\]
on a sufficiently short interval. Choose a nonzero real
\(\chi\in C_c^\infty((\varepsilon,2\varepsilon))\) with
\(4\varepsilon<\log2\), supported where \(V_N'<0\), and set
\(g=\chi\), \(h=x\chi\). Every actual reflected-prime endpoint term
vanishes, while \(g h'-g'h=\chi^2\). Therefore
\[
N_s[g,\partial^2h]-N_s[\partial^2g,h]
=-2\int V_N'(x)\chi(x)^2\,dx>0.
\tag{12}
\]
Thus \(N_s\) is not a symmetric metric for the induced second derivative
even on the compact odd core. The calculation retains the complete
prime-power diagonal and every reflection endpoint.

The \(N\)-seminorm annihilates constant ratios, but
\[
\mathcal B_\psi r=\psi^{-1}\partial^2(\psi r),\qquad
\mathcal B_\psi1=\frac{\psi''}{\psi}=\frac14-r_0,\quad
r_0=\frac{f_0}{\psi},\quad
f_0=(\partial^3-\tfrac14\partial)\Phi.
\tag{13}
\]
The theta tail gives \(r_0(x)\sim-4(\pi e^{2x})^2\), so \(N[r_0]>0\).
The unprojected operator therefore does not preserve the constant
nullspace and does not descend to the quotient by constants.

## The unprojected reflected-energy derivative is not closable

On the compact ratio core \(\mathcal C\), define
\[
K_N=\overline{\{\nabla_Nr:r\in\mathcal C\}},\qquad
Z_0(\nabla_Nr)=\nabla_N(\mathcal B_\psi r).
\tag{14}
\]
The compact-core gradient is injective: if \(r\) is supported in
\([0,R]\), choose an actual power \(n=2^j\) with \(d_n>2R\); its reflected
partner lies outside the support, and the positive edge weight forces
\(N[r]>0\) unless \(r=0\). Also \(\mathcal B_\psi r\) remains in the
compact ratio core because \(\psi r\) and its second derivative are smooth odd, while
\(\psi\) has a simple zero at zero; their quotient is smooth even.

Take smooth even cutoffs \(\chi_R=1\) on \(|x|\le R\), zero on
\(|x|\ge R+1\), with uniformly bounded derivatives. The complete-edge
bound
\[
N[u]\le4\int_0^\infty\psi(x)L(x)|u(x)|^2\,dx,\qquad
L(x)\le C(1+x)e^{x/2},
\tag{15}
\]
and the double-exponential theta tail show that
\(\nabla_N\chi_R=\nabla_N(\chi_R-1)\to0\) in \(K_N\). The same
bound shows \(N[r_0]<\infty\): the fixed jet has at most exponential
growth, while \(\psi(x)L(x)\) has a double-exponential tail. Hence
\(\nabla_Nr_0\) is a vector in \(K_N\). Direct differentiation gives
\[
\mathcal B_\psi\chi_R
=\chi_R(\tfrac14-r_0)
+2\chi_R'\frac{\psi'}{\psi}+\chi_R''.
\tag{16}
\]
The first term converges in \(N\) energy to \(1/4-r_0\). The last
two are supported on \([R,R+1]\), grow at most like \(e^{2x}\), and
vanish in \(N\) by (15). Consequently,
\[
\nabla_N\chi_R\longrightarrow0,\qquad
Z_0(\nabla_N\chi_R)\longrightarrow-\nabla_Nr_0\ne0.
\tag{17}
\]
For the nonzero limit, fix \(x\) in a positive compact interval and take
large actual powers \(n=2^j\). Then \(r_0(d_n-x)\to-\infty\), whereas
\(r_0(x)\) is bounded and the edge weights are positive. Equation (17)
violates the sequential criterion for closability. Therefore the
unprojected differential operator \(Z_0\) has no closed extension agreeing
with its entire compact core. The limit lies in the theta-jet gradient
span, however, so this gives no conclusion about an operator after
quotienting by that closed span.

## Scope

The theta-null gradients are not total in the actual reflected-prime
completion; the repository report
[reflected-prime energy report](../20261013_reflected_prime_energy/REPORT.md) constructs real-zero
functionals in their orthogonal complement. The unclosability result
concerns only the unprojected \(N\)-energy operator. Projection away from
the jet span may remove the sequence in (17), but the projected domain,
symmetry, and metric properties remain unproved. The full \(\Phi\)-ground
jump generator is already self-adjoint and nonnegative in \(L^2(d\nu)\).
The remaining assertion is the odd spectral gap
\(\mathcal L_{\rm odd}\ge\frac12 I\); neither the fixed-order ladder nor
the \(N\)-metric obstruction proves or disproves it.

The closed-form and actual-band inputs are stated in the repository reports
[ORIGINAL_FORM_FOUNDATION.md](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md),
[ACTUAL_NEGATIVE_BAND_COVERAGE.md](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md),
and [SIGNED_PRIME_LOW_SPECTRUM.md](../20261012_adaptive_spectral_tail/SIGNED_PRIME_LOW_SPECTRUM.md).
No RH assumption or conclusion is used.
