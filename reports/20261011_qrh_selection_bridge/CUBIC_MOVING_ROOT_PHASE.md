# Moving radial root scalar after the finite deconvolution repair

## Scope and notation

This note isolates the moving-prime scalar in the exact radial $D_u$
reflection of Part XXVII B. It is an arithmetic identity inside the valid
compact-block deconvolution in [COMPACT_CUBIC_DUAL.md](COMPACT_CUBIC_DUAL.md); it is not an
estimate for the pooled signed column.

Let $u$ be squarefree and primary, with $(u,6L)=1$, and write

\[
 \rho_p(x)=\chi_p(x)^2=(x/p)_3,\qquad
 \rho_u(x)=\prod_{p\mid u}\rho_p(x),\qquad G(u)=\widetilde g(u)
 = (Nu)^{-1/2}\sum_{x\bmod u}\rho_u(x)\check e(x/u).
\]

Bars mean complex conjugation. Every prime generator in $u$ is the source's
primary generator. For a fixed Fourier label $h_0\bmod L$ and a fixed
source bad sector \(\mathfrak s=[u]_{\mathfrak m_{\rm bad}}\), write the
*actual normalized cusp denominator element* as
\[
 c_{\rm cusp}=c_0(h_0,\mathfrak s)u.
\]
Thus $c_0$ includes the source's chosen normalizing unit. If instead one
stores only a primary associate (c_0^{\rm pr}), write
\(c_0=\epsilon_{h_0,\mathfrak s}c_0^{\rm pr}\) and retain the factor
\(\bar\rho_u(\epsilon_{h_0,\mathfrak s})\) below. Replacing $c_0$ by an
ideal norm or silently dropping this unit is not valid.

The sector is the finite one fixed by the source cusp construction: it fixes
the denominator representative, source cusp, bad multiplier, and bad
additive character. In the QRH construction one may take the source's
congruence sector for the active radical $u\bmod M^2$, where
\(M=\lambda^{12}L^4\); only finitely many such sectors occur.

## CRT evaluation of the exact moving scalar

The $j=4$ radial local transform in Part XXVII B contributes, before the
Ramanujan factor, the exact product
\[
 \mathcal S(u;c_0)=\prod_{p\mid u}
 \gamma_4(p)\,\chi_p\!\left(\lambda^2c_{\rm cusp}/p\right)^{-2}
 =\prod_{p\mid u}
 \gamma_4(p)\,\chi_p\!\left(\lambda^2c_0u/p\right)^{-2}.       \tag{1}
\]
Here \(\gamma_4(p)\) is the local normalized Gauss sum in the source's
Fourier convention. This convention matters: the source has
\(e(z)=\check e(z/\lambda)\), so
\(e(x/p)=\check e(\lambda^{-1}x/p)\).

For \(\rho_p=\chi_p^2\), the character in \(\gamma_4(p)\) is
\(\chi_p^4=\bar\rho_p\). Changing the additive coefficient from
\(\check e(x/p)\) to \(e(x/p)\) multiplies its Gauss sum by
\(\rho_p(\lambda^{-1})=\bar\rho_p(\lambda)\). Also
\(\tau(\bar\rho_p,\check e)=\overline{G(p)}\), since
\(\rho_p(-1)=1\). The negative-additive version used for the finite Fourier
coefficient gives the same value at exponent (4), since
\(\chi_p(-1)^4=1\). Consequently
\[
 \gamma_4(p)=\bar\rho_p(\lambda)\,\overline{G(p)}.             \tag{2}
\]

Now
\[
 \chi_p(\lambda^2c_0u/p)^{-2}
 =\chi_p(\lambda)^{-4}\bar\rho_p(c_0)\bar\rho_p(u/p).
\]
The two lambda factors in (1) cancel exactly:
\(\bar\rho_p(\lambda)\chi_p(\lambda)^{-4}
=\chi_p(\lambda)^{-6}=1\). For squarefree $u$, CRT for the normalized
DR Gauss sum gives
\[
 G(u)=\prod_{p\mid u}G(p)\rho_p(u/p),\qquad
 \overline{G(u)}=\prod_{p\mid u}\overline{G(p)}\bar\rho_p(u/p).
\]
Therefore the local product has the exact compact form
\[
 \boxed{\mathcal S(u;c_0)=\overline{G(u)}\,\bar\rho_u(c_0).} \tag{3}
\]
This is where the source's additive convention and the actual cusp unit are
both used. If the local γ-factor were instead defined with
\(\check e(x/p)\), (2) would lack \(\bar\rho_p(\lambda)\), and the
lambda cancellation in (1) would leave a different fixed ray factor.

The normalized DR identity is
\(G(u)^3=\mu(u)\alpha(u)\), with
\(\alpha(u)=u/|u|\), for squarefree primary $u$. Since \(|G(u)|=1\), put
\[
 Q(u):=\frac{G(u)}{\overline{G(u)}}=G(u)^2.
\]
Then (3) is equivalently
\[
 \boxed{\mathcal S(u;c_0)
 =\mu(u)\,\bar\alpha(u)\,Q(u)\,\bar\rho_u(c_0).}       \tag{4}
\]
Thus the scalar is the Gauss quotient $Q(u)$, times the explicit
Mobius/archimedean factor and the fixed-numerator cubic ray character. No
unresolved unit remains if $c_0$ means the actual normalized cusp element;
if only its primary associate is fixed, the factor
\(\bar\rho_u(\epsilon_{h_0,\mathfrak s})\) must be restored.

## Splitting $u=ch$: the joint kernel

Suppose $u=ch$ with $c,h$ squarefree, primary, coprime to each other and
to $6L$. CRT and cubic reciprocity give
\[
 G(ch)=G(c)G(h)\bar\rho_c(h),\qquad
 Q(ch)=Q(c)Q(h)\rho_c(h),\qquad
 \rho_c(h)=(h/c)_3=(c/h)_3.                              \tag{5}
\]
The exponent in the second identity is important:
\(\bar\rho_c(h)^2=\rho_c(h)\), since the symbol has order three. Thus the
genuine infinite-modulus $c/h$ interaction is the cubic residue kernel
\((h/c)_3\), not a product of one-variable weights. The fixed-numerator
factor splits as
\(\bar\rho_{ch}(c_0)=\bar\rho_c(c_0)\bar\rho_h(c_0)\). On a fixed bad
sector, the exact reflected coefficient is
\[
\boxed{
 a_{h_0,ch}=
 \widehat\Phi_0(h_0)\,\bar\kappa_F(h_0,\mathfrak s)
 \mu(c)\mu(h)\bar\alpha(c)\bar\alpha(h)
 Q(c)Q(h)\,(h/c)_3\,
 \bar\rho_c(c_0)\bar\rho_h(c_0).}                       \tag{6}
\]
Here \(\bar\kappa_F\) is exactly the conjugated fixed bad multiplier from
the source's three-case cusp table; its chosen unit and the cusp element
$c_0$ are held fixed on \((h_0,\mathfrak s)\). Formula (6) is the
moving dependence in the Part XXVII B scalar. The local radial coefficient
still carries its displayed \((Nu)^{-1/2}\).

For specificity, the source's unconjugated fixed factor is the following
case-dependent entry, with its normalized cusp numerator \(a\), matrix
entry \(b\), and \(A=a-u_0b\) in the middle case:
\[
 \kappa_F=
 \begin{cases}
 (c_0/a)_3,&3\mid c_{\rm cusp},\\
 (-u_0/A)_3\,((c_0/u_0)/a)_3,&v_\lambda(c_{\rm cusp})=1,\\
 (a/c_0)_3,&\lambda\nmid c_{\rm cusp}.
 \end{cases}
\]
These are the fixed factors in the source's full multiplier; the remaining
moving factor is \(\prod_{p\mid u}\chi_p(a)^2\). The chosen lifts make
\(\kappa_F\) constant on \((h_0,\mathfrak s)\), and the scalar in (6) uses
\(\bar\kappa_F\), not \(\kappa_F\).

The bad additive phase is retained alongside (6). In the source's CRT
notation, with $D_F=\lambda^3c_0$, its fixed-bad part has the form
\[
 \psi_{h_0,u}(x)=
 e\!\left(-\delta'_F(h_0,\mathfrak s)
                   u^{-1}x/D_F\right),\qquad x=\lambda^4\nu,
                                                               \tag{7}
\]
where $u^{-1}$ is taken in the fixed quotient modulo $D_F$; the source
choice of lifts fixes \(\delta'_F\) on the sector. Hence for $u=ch$,
\[
 \psi_{h_0,ch}(\lambda^4\nu)=
 e\!\left(-\delta'_F(h_0,\mathfrak s)c^{-1}h^{-1}
                   \lambda^4\nu/D_F\right),                 \tag{8}
\]
with both inverses in that quotient. Equation (8) is a finite, genuinely
joint $c/h$ residue factor. It may be frozen only after partitioning
\(c,h\) into the source's fixed bad residue sectors. It is not a constant
mode phase and is not deleted. This uses only the source cusp-fraction,
multiplier, and additive-CRT identities; no differentiated-theta angular
gamma kernel is imported into the radial $D_u$ equation.

Combining (5)--(8), the arithmetic pair kernel in a fixed bad sector is
\[
 \mathscr K_{h_0,\mathfrak s}(c,h;\nu)=
 (h/c)_3\,\bar\rho_c(c_0)\bar\rho_h(c_0)
 \psi_{h_0,ch}(\lambda^4\nu),                            \tag{9}
\]
with the separate one-variable factors
\(\mu(c)\mu(h)\bar\alpha(c)\bar\alpha(h)Q(c)Q(h)\) and the fixed
\(\widehat\Phi_0(h_0)\bar\kappa_F\). All entries in (9) are the exact
source values on primary generators, including zero extensions. Since
$c_0$ is coprime to $ch$, the fixed-numerator characters in (9) are
nonzero; the zero-extension convention remains relevant for the Ramanujan
divisor condition below.

## What the Ramanujan expansion does to the Mobius sign

The radial factor is
\[
 c_u(\lambda^4\nu)=\sum_{R\mid u}\mu(u/R)NR\,
                         1_{R\mid\nu}.
\]
For $u=ch$, write $R=R_cR_h$, $R_c\mid c$, $R_h\mid h$, and
$c=R_c c_*$, $h=R_h h_*$. The common coefficient cited in the
referee note simplifies by itself to
\[
 \frac{\mu(c)}{Nc}\,\mu(ch/R)NR
 =\frac{\mu(R_c)\mu(h_*)NR_h}{Nc_*},                       \tag{10}
\]
which has no \(\mu(c_*)\). But the exact moving root scalar (4) contributes
\(\mu(u)=\mu(R_c)\mu(c_*)\mu(R_h)\mu(h_*)\). Therefore the product of
the left side of (10) with the Mobius factor in the root scalar is
\[
 \boxed{\mu(c_*)\mu(R_h)\,\frac{NR_h}{Nc_*}.}             \tag{11}
\]
So an ordinary Mobius sign in the (c_*)-complement is formally restored;
it was lost only when the root scalar was omitted. The full term also
contains
\[
 \frac{\bar\alpha(c)\bar\alpha(h)Q(c)Q(h)}{\sqrt{Nc\,Nh}}
 (h/c)_3\bar\rho_c(c_0)\bar\rho_h(c_0)
 \psi_{h_0,ch}(\lambda^4\nu)\,1_{R_cR_h\mid\nu},          \tag{12}
\]
as well as the source cusp coefficient, test, and remaining divisor
weights. If the factors $c=R_c c_*$ and $h=R_h h_*$ are expanded further,
CRT also gives, for example,
\(Q(c)=Q(R_c)Q(c_*)\rho_{R_c}(c_*)\); these extra residue symbols must
stay attached. Thus (11) identifies a real Mobius sign, but it does not
produce an isolated one-variable Mertens column or an RH estimate. The
joint cubic symbol, the finite bad additive phase, and the physical block
weights remain coupled.

## Source checks

The local scalar (1), the fixed-sector dependence, and the Ramanujan
expansion are Part XXVII B, §§3--4, especially (6)--(9), of
[QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md).
The exact cusp fraction, conjugated multiplier, and additive CRT phase are
the QRH source equations `reflection-cusp-fraction`,
`reflection-multiplier`, and `reflection-additive-phase` in
[pinned September-30 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The DR convention is
\(\widetilde g(u)=(Nu)^{-1/2}\sum_{x\bmod u}(x/u)_3\check e(x/u)\),
with \(\widetilde g(u)^3=\mu(u)u/|u|\) and cubic reciprocity; see
[Dunn--Radziwiłł, arXiv:2109.07463v3, (1.4), (1.7)--(1.8)](https://arxiv.org/html/2109.07463v3).

The finite-block identity has the same rowwise scope: apply this
identity inside the finite compact-block deconvolution and retain each
source cusp, phase, mask, and test. It supplies the requested bilinear
arithmetic entry; it supplies no pooled-row bound.

Independent verification is [REFEREE_CUBIC_MOVING_ROOT_PHASE.md](REFEREE_CUBIC_MOVING_ROOT_PHASE.md). The CRT product in (3) is derived from the Gauss-sum definition and reciprocity; it is not assigned to an unstated source theorem.
