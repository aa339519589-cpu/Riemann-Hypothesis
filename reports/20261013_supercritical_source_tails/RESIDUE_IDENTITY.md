# Zero-spectrum identity and Carleman residues for a supercritical source

Date: 2026-10-13. For a hypothetical Green eigenvalue \(\lambda>1\), the
actual source-tail theorem, the full-prime ground transform, and the
additive explicit formula give an exact zero-spectrum representation of
the reflected divergence. Its one-sided finite-part Carleman continuation
has explicit residues in terms of the source's Fourier samples. These
identities do not exclude \(\lambda>1\) or imply RH. The source tail is
equation (6) of the [source-tail report](REPORT.md); the finite-part
normalization is from [GLOBAL_MEAN_PERIODIC.md](GLOBAL_MEAN_PERIODIC.md).

Let \(\mathcal Z\) be the set of distinct zeros of
\(\Xi(z)=\xi(\tfrac12+iz)\), and let \(m_\rho\) denote the multiplicity of
\(\rho\in\mathcal Z\). Sums over \(\mathcal Z\) carry the displayed weight
\(m_\rho\), so each zero is counted once per multiplicity. The only prime sums used
are the complete sums with
\(\alpha_n=\Lambda(n)/\sqrt n\); no series for \(W\) is assumed.

## The eigenrelation as a distribution equation

Let \(r\) be a pole-centered actual eigen-potential, \(g=\psi r\) on the
positive wing, and extend \(g\) oddly to \(\mathbb R\). Let \(W\) be the
complete reflected divergence of \(\nabla_N r\), with the odd distribution
\[
\langle W_o,\varphi\rangle
=\int_0^\infty W(x)\bigl(\varphi(x)-\varphi(-x)\bigr)\,dx.
\]
For a compact odd source test \(f=\psi z\), the full-line pairing against
\(W_o\) is
\[
\int_{\mathbb R}\overline{f(x)}W_o(x)\,dx
=2\int_0^\infty \psi(x)\overline{z(x)}W(x)\,dx
=N(z,r).
\]
The factor two is exactly the factor in the vertex identity for \(N\).
There is no additional factor when writing the full-line distribution
equation.

Put
\[
\delta=\frac{\lambda-1}{\lambda}\in(0,1),\qquad
\mathcal T_{\rm source}=a(D)-S,\qquad
\mathcal A_s=\mathcal T_{\rm source}-2s_0\ell,\quad
s_0(x)=\sinh(x/2),\quad
\ell(f)=\int_{\mathbb R}s_0(x)f(x)\,dx.
\]
The eigenrelation \(N(r,z)=\lambda P(r,z)\), its conjugate, and the
ground-transform identity \(\mathfrak A_s=P-N\) give, weakly against every
compact odd source test,
\[
\boxed{\mathcal A_s g=-\delta W_o.} \tag{1}
\]
Indeed \(P(z,r)-N(z,r)=-\delta N(z,r)\), and the displayed full-line
pairing identifies \(N(z,r)\) with \(W_o\). For the centered representative \(\ell(g)=0\), so
\(\mathcal A_sg=\mathcal T_{\rm source}g\). The same equation holds
without centering when the polar contribution is retained in \(\mathcal A_s\).

## The complete explicit formula gives the divergence spectrum

Write \(G(z)=\int_{\mathbb R}g(x)e^{izx}\,dx\). The actual tail theorem and
the reference control at zero imply \(g\in L^1(e^{a|x|}dx)\cap
L^2(e^{2a|x|}dx)\) for every fixed \(a>0\); in particular \(G\) is entire
and bounded on every fixed horizontal strip.

The additive explicit formula, with its original Gamma, pole, and
full-prime coefficients, is recorded as equation (C4) in Appendix C of the
[full-kernel report](../20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md).
Its classical source is Burnol, [“The Explicit Formula in Simple
Terms,” §§1, 3](https://arxiv.org/pdf/math/9810169). For compact smooth
source tests it gives the source identity with the complete prime row
\(\sum_{n\ge2}\alpha_n[h(\log n)+h(-\log n)]\), including every prime
power:
\[
(a(D)-S)g=Z_g-P_g,\qquad
Z_g(x)=\sum_{\rho\in\mathcal Z}m_\rho G(\rho)e^{-i\rho x}, \tag{2}
\]
where, for odd \(g\),
\[
P_g(x)=e^{x/2}G(i/2)+e^{-x/2}G(-i/2).
\]
The Fourier sign in (2) follows directly by inserting the translate
\(y\mapsto g(x-y)\) into (C4): its transform at \(z\) is
\(e^{izx}G(-z)\); relabel the symmetric zero set by \(z\mapsto-z\).
The series is linear in \(g\). In the sesquilinear pairing its term against
a test \(f\) is
\(m_\rho G(\rho)\overline{\widehat f(\bar\rho)}\), so the conjugation is
on the test transform, not on \(G(\rho)\).

For odd \(g\), \(G(-z)=-G(z)\) and
\(\ell(g)=-G(i/2)\). Hence \(P_g=-2s_0\ell(g)\). Since
\(\mathcal A_s=\mathcal T_{\rm source}-2s_0\ell\), the two pole terms cancel exactly:
\[
\boxed{\mathcal A_sg=Z_g
=\sum_{\rho\in\mathcal Z}m_\rho G(\rho)e^{-i\rho x}
\quad\hbox{in }\mathcal D'(\mathbb R).} \tag{3}
\]
For a pole-centered source both individual pole terms vanish. This check
fixes the coefficient-two polar normalization and is valid for complex
sources as well.

Here is the domain passage for (3). With \(\mu(x)^2=\psi(x)/L(x)\) as in
the [source-tail report](REPORT.md), the actual source-tail construction
places \(g/\mu\) in \(L^2(0,\infty)\), and
\(\sup_x e^{a|x|}\mu(x)<\infty\) for every fixed \(a>0\); hence
\(g\in L^2(e^{2a|x|}dx)\) for every \(a\). Weighted \(L^1\) follows from
Cauchy-Schwarz using any slightly larger exponential weight. First cut
\(g\) off by smooth even
\(\chi_R\), with \(\chi_R=1\) on \([-R,R]\), \(\chi_R=0\) outside
\([-2R,2R]\), and \(|\chi_R|\le1\). The logarithmic jump-form cutoff
argument from the source-tail report gives \(\chi_Rg\to g\) in the
logarithmic Fourier form: the cutoff multipliers have a uniform form bound, and convergence first holds on the compact core and then on its closure by density. The source \(L^2\) tail gives convergence in
\(L^2(e^{2a|x|}dx)\) and weighted \(L^1\) for every fixed \(a>1/2\).
Mollify each compactly supported odd cutoff by an even smooth approximate
identity. On its fixed compact support this converges in the logarithmic
form and in weighted \(L^1,L^2\); a diagonal sequence gives compact smooth
odd \(g_j\) converging in all these norms. The \(a(D)\) terms converge
distributionally because \(a(t)=O(\log(2+|t|))\). For the complete prime
shifts, Minkowski and
\[
|x|\ge d_n-|x\pm d_n|,\qquad
\sum_{n\ge2}\alpha_ne^{-a d_n}
=\sum_{n\ge2}\Lambda(n)n^{-(a+1/2)}<\infty
\]
give convergence in the weighted space \(L^2(e^{-2a|x|}dx)\). This keeps
every prime power. On the zero side, weighted \(L^1\) convergence makes
\(G_j\to G\) uniformly for \(|\operatorname{Im}z|\le1/2\). For
\(\varphi\in C_c^\infty(\mathbb R)\), the pairing is
\[
\langle Z_{g_j},\overline\varphi\rangle
=\sum_{\rho\in\mathcal Z}m_\rho G_j(\rho)
  \overline{\widehat\varphi(\bar\rho)}.
\]
The test transform decreases faster than every power uniformly on the
zero strip, and \(N_\Xi(T)=O(T\log(2+T))\) makes this majorant summable.
Thus the full zero sum passes by dominated convergence. These passages
prove (3) for the actual, possibly rough, source; no pointwise regularity
of \(W\) is used.

Combining (1) and (3) yields the stronger exact representation
\[
\boxed{W_o=-\frac1\delta
\sum_{\rho\in\mathcal Z}m_\rho G(\rho)e^{-i\rho x}
\quad\hbox{in }\mathcal D'(\mathbb R).} \tag{4}
\]
This is a zero-spectrum distribution identity, not an ordinary Dirichlet
series and not convergence in the \(N\)-energy norm.

The coefficients are uniformly bounded because
\(|G(\rho)|\le\int |g(x)|e^{|x|/2}dx\) for every \(\rho\in\mathcal Z\).
The zero count and rapid decay of a compact smooth test show that the
series in (4), tested on a translate by \(R\), is
\(O_\varphi(\delta^{-1}e^{a_*|R|})\), where
\[
a_*=\sup_{\rho\in\mathcal Z:\,G(\rho)\ne0}|\operatorname{Im}\rho|
\le \sup_{\rho\in\mathcal Z}|\operatorname{Im}\rho|.
\]
If every sample vanishes, set \(a_*=0\); then (4) is the zero
distribution.
Using only the classical critical strip gives \(a_*\le1/2\). The
repository's separate verified zero-free input sharpens the universal
strip bound to
\[
|\operatorname{Im}\rho|\le
\frac{1361-4\sqrt{921}}{3306}
=0.374957\ldots<\frac38
\]
for every \(\rho\in\mathcal Z\); see the [updated strip input](../20261013_updated_qrh_input/REPORT.md)
for its external source and scope. This bounds the distributional
exponential type by the largest imaginary height of an active mode. It is
not a strict descent below that active height, and it does not
imply pointwise or weighted \(L^2\) bounds for \(W\).

## Carleman numerator and residues

Let \(W_+^\eta\), \(Z=\Phi*W_+^\eta\), and
\(B(z)=\int Z(t)e^{izt}dt\) be as in
[GLOBAL_MEAN_PERIODIC.md](../20261013_supercritical_source_tails/GLOBAL_MEAN_PERIODIC.md).
The established convolution identity gives
\[
\mathcal W_+^\eta(z)=\frac{B(z)}{\Xi(z)}
\]
in the initial upper half-plane. The zero expansion (4) gives a direct
meromorphic formula for this same continuation without applying a
discontinuous half-line cutoff to a distribution at the origin.

Choose a smooth \(\chi\) on \([0,\infty)\) that vanishes near zero and is
one for \(x\ge2\). Split the finite-part transform as
\[
\mathcal W_+^\eta(z)=C_{\eta,\chi,W}(z)
+\int_0^\infty W(x)\chi(x)e^{izx}\,dx,
\]
where
\[
C_{\eta,\chi,W}(z)
=\int_0^\infty W(x)\bigl((1-\chi(x))e^{izx}-\eta(x)\bigr)\,dx
\]
is entire: its test is compactly supported and \(O(x)\) at zero. In the
initial half-plane, pair (4) with the smooth tail test \(\chi e^{izx}\).
To justify this noncompact test, insert a smooth cutoff \(\theta_R\) equal
to one up to \(R\) and zero after \(2R\). Since \(\chi\) vanishes near
zero, repeated integration by parts in
\(\int\chi\theta_R e^{i(z-\rho)x}dx\) has no endpoint term there. For
fixed \(z\) with \(\operatorname{Im}z>C/2>1/2\), the exponential
\(e^{-(\operatorname{Im}z-\operatorname{Im}\rho)x}\) makes the derivative
\(L^1\) bounds uniform in \(R\), giving
\(O_{z,N}((1+|\operatorname{Re}\rho|)^{-N})\) for every \(N\). The zero
count and boundedness of \(G(\rho)\) dominate the sum as \(R\to\infty\).
On the actual-function side, the weighted \(L^2\) tail makes
\(\int W\chi e^{izx}\) converge. This gives
\[
\mathcal W_+^\eta(z)
=C_{\eta,\chi,W}(z)
-\frac1\delta\sum_{\rho\in\mathcal Z}m_\rho G(\rho)L_\chi(z-\rho),
\qquad
L_\chi(w)=\int_0^\infty\chi(x)e^{iwx}\,dx. \tag{5}
\]
For \(\operatorname{Im}w>0\), integration by parts gives
\[
L_\chi(w)=-\frac1{iw}\int_0^\infty\chi'(x)e^{iwx}\,dx.
\]
Because \(\chi'\) is smooth, compactly supported, and
\(\int\chi'=1\), this formula continues \(L_\chi\) meromorphically to the
plane, with a single simple pole at \(w=0\) of residue \(i\). Its numerator
is rapidly decreasing in \(\operatorname{Re}w\) on bounded horizontal
strips. Since \(G\) is bounded on the zero strip and
\(\sum_\rho m_\rho(1+|\operatorname{Re}\rho|)^{-N}<\infty\) for \(N>2\),
the series in (5) converges normally on compact sets away from its poles.
The compact-origin term is entire and cannot affect residues.

Consequently every zero \(\rho\) of \(\Xi\) contributes at most a simple
pole, even if its multiplicity is larger:
\[
\boxed{\operatorname*{Res}_{z=\rho}\frac{B(z)}{\Xi(z)}
=-\frac{i\,m_\rho}{\delta}\,G(\rho).} \tag{6}
\]
If \(\rho\) has multiplicity \(m\), then \(B\) vanishes to order at least
\(m-1\), and
\[
B^{(m-1)}(\rho)
=-\frac{i}{\delta}\,G(\rho)\Xi^{(m)}(\rho). \tag{7}
\]
For a simple zero, (7) reads
\(B(\rho)=-i\Xi'(\rho)G(\rho)/\delta\). If \(G(\rho)=0\), the possible
pole in (6) is removable. The sign in (6) can also be checked from the
single mode in (4): its tail transform is
\(-m_\rho G(\rho)\delta^{-1}\int_0^\infty
\chi(x)e^{i(z-\rho)x}dx\), whose residue is
\(-i m_\rho G(\rho)/\delta\).

For a real odd eigen-source and a real zero \(\gamma\),
\[
G(\gamma)=2i\int_0^\infty g(x)\sin(\gamma x)\,dx,\qquad
\operatorname*{Res}_{z=\gamma}B/\Xi
=\frac{2m_\gamma}{\delta}
\int_0^\infty g(x)\sin(\gamma x)\,dx\in\mathbb R. \tag{8}
\]
This is a signed sample identity, not a sign restriction: the sine moment
of the eigen-source has no known sign. For a nonreal zero, conjugation and
oddness pair the four residues but do not make their aggregate terms
nonnegative.

## What this does and does not give toward \(\lambda>1\)

The residue formula is an explicit constraint on the numerator \(B\): its
zero values and first nonzero derivatives are fixed by the entire Fourier
samples of the actual eigen-source. The distributional growth bound does
not force additional residue cancellation.
Independently, the direct finite-part estimate gives
\(\mathcal W_+^\eta(t+i\sigma)=O_\delta(\sqrt{\log(2+|t|)})\) on each
fixed line \(\sigma>C/2\): near zero use
\(\int x|W|^2<\infty\) and
\(\int_0^\epsilon\min(|t|^2x^2,1)\,dx/x=O(\log(2+|t|))\); away from zero
use the exponential weighted \(L^2\) tail. This slow upper bound is
compatible with the pole set in (5) and does not force the residues to
vanish.

The residue identity and distributional zero expansion do not exclude \(\lambda>1\). The [weighted logarithmic argument](SIGNED_ZERO_PAIRING.md) separately justifies quadratic pairing and absolute zero-square summability. The resulting products retain the conjugate zero argument and need not be nonnegative off the real axis. An independent signed estimate controlling those contributions is still missing. No supercritical eigenvalue or zeta zero is excluded.
