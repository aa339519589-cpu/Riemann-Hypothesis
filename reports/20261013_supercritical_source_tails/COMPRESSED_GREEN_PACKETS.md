# Compressed smoothing on the complete supercritical Green packet

This extends the actual-vector compression argument to every actual dyadic
supercritical Green band. The resulting source bound is uniform in the
band's depth and dimension for every Sobolev order below \(1/8\). The full
band keeps the previously proved logarithmic depth cost. In particular, a
sufficient finite sampling height can be chosen with any fixed power
greater than four of that depth cost divided by the excess.

These are bounds on the actual odd Green packet. They provide no upper
signed comparison, critical positivity, or exclusion of a supercritical
eigenvalue. They do not identify this packet with an even physical band.

## 1. Objects, inputs and statement

Use the original \(P\)-gradient space and complete Green operator

\[
A=T^*T,\qquad E\subset\operatorname{Ran}\mathbf1_{(1,\infty)}(A),
\qquad \Delta=I-A^{-1}|_E,\qquad dI\preceq\Delta\preceq2dI.
\tag{1}
\]

Here \(E\) is an actual spectral band, including a terminal partial band.
It is finite dimensional by compactness of the positive excess; no
estimate below depends on that dimension. For \(a\in E\), let

\[
g_a=\psi r_a,\quad Va=g_a/\mu,\quad
\mu^2=\psi/L,\quad H=I-\mathcal R,\quad M=V^*HV=A/2.
\tag{2}
\]

The letter \(V\) in this note is the source map, not the row potential.
All adjoints and coefficient-space norms use the original \(P\) metric.
The complete normalized reflection satisfies

\[
0\preceq H\preceq2I,\quad \|V\|^2\le193,\quad
[M,\Delta]=0,\quad 0\prec\Delta\prec I.
\tag{3}
\]

We use the domains, full-band exterior estimate, convolution identities
and positive Sylvester argument of
[GREEN_PACKET_SMOOTHING.md](GREEN_PACKET_SMOOTHING.md), and the bounded
operator compression estimates in
[COMPRESSED_MIXED_SMOOTHING.md](COMPRESSED_MIXED_SMOOTHING.md).
The older packet theorem, including its \(H^s\) bound for \(s<1/16\),
is an input, not a conclusion inferred from the scalar improvement.

For every fixed \(0<\beta<1/2\), uniformly over (1),

\[
\int_{|\xi|\ge N}\log(2+|\xi|)|\widehat{(g_a)_o}(\xi)|^2d\xi
\le C_\beta\{dN^{-\beta/2}+N^{-1/4}\}\|a\|_P^2.
\tag{4}
\]

The threshold \(N_0\) is independent of depth and dimension. Hence

\[
\boxed{\ \|(g_a)_o\|_{H^s(\mathbb R)}\le C_s\|a\|_P,
\qquad 0\le s<1/8.\ }
\tag{5}
\]

## 2. A dimension-free origin bound for the actual band

Fix \(0<\ell_0<\log2/4\) and put \(I=(0,\ell_0)\).
The older packet theorem supplies any one fixed positive Sobolev order
below \(1/16\). Since the Gamma symbol grows logarithmically, this gives

\[
\|B_o g_a\|_{L^2(I)}+\|g_a\|_2\le C\|a\|_P.
\tag{6}
\]

For example, fix \(s_0\in(0,1/16)\) and use
\(b(\xi)\le C_{s_0}\langle\xi\rangle^{s_0}\).
The complete weighted-Cauchy argument in
[ORIGIN_GRAPH_DOMAIN.md, §3](ORIGIN_GRAPH_DOMAIN.md) uses only
\(\|g_a/\mu\|^2\le193\|a\|_P^2\). It therefore proves directly
for every packet, without summing eigenvector estimates, that

\[
F_\pm(g_a)(x)=\sum_{n\ge2}\alpha_n g_a(\log n\pm x),\qquad
\|F_+(g_a)\|_{L^2(I)}+\|F_-(g_a)\|_{L^2(I)}\le C\|a\|_P.
\tag{7}
\]

All prime powers remain in these locally \(L^2\) convergent series.
Linearity of the actual band equation, with its distinct depths retained,
gives on \(I\)

\[
B_o g_a+Lr_{\Delta a}
=C_0g_a+F_+(g_a)-F_-(g_a)+F_-(g_{\Delta a}).
\tag{8}
\]

This is the scalar equation with \(\delta g_a\) replaced by
\(g_{\Delta a}\), not by a common scalar multiple of \(g_a\).
Equations (3), (6), (7), and the smooth strictly positive row \(L\) on
\([0,\ell_0]\) show that

\[
\|g_{\Delta a}/x\|_{L^2(I)}\le C\|a\|_P.
\]

Indeed divide (8) by \(L\) and multiply by the smooth bounded
\(\psi(x)/x\). Replacing \(a\) by \(\Delta^{-1}a\) now gives

\[
\boxed{\ \|g_a/x\|_{L^2(I)}\le Cd^{-1}\|a\|_P.\ }
\tag{9}
\]

For \(2b<\ell_0\), the actual endpoint map consequently satisfies

\[
\|\mathbf1_{x<2b}V\|_{E\to L^2}\le C\sqrt b/d,
\tag{10}
\]

because \(\mu^2\asymp x\) at zero. The old positive Sobolev exponent
is used only to establish (6); there is no bootstrap circularity.

## 3. Full mixed gate and the noncommuting depth

Use the compact Poisson convolution \(C=C_\tau^\alpha\), frozen weight operator \(Z\),
endpoint multiplier \(\Theta\), and compressed operator
\(H_b=I-\Theta\mathcal R\Theta\) from the scalar compression proof.
The support radius is \(2\alpha\), with \(\alpha\le b/16\).
Write its bounds as

\[
\|Z\|\le1+\varepsilon_0,\qquad
\|[H_b,Z]\|\le\eta_b,\qquad e_b=\varepsilon_0+\sqrt{\eta_b}.
\]

For each \(a\), apply the bounded square-root gate to
\(v_b=\mathbf1_{x\ge2b}Va\). Finite propagation identifies the compressed
and full \(H\) pairings on this vector exactly. Restoring the endpoint
piece using (10) and \(\|V\|\le\sqrt{193}\) gives

\[
\operatorname{Re}\langle Va,H(Z^2-I)Va\rangle
\le C(e_b+\sqrt b/d)\|a\|_P^2.
\tag{11}
\]

This uses sharp cutoffs only in bounded-operator algebra.
For the actual legal source map \(W_2a=\mu^{-1}C^2g_a\), the existing
dimension-free far-tail comparison on the original full vector is

\[
\|W_2-Z^2V\|\le Cd^{-1}\tau_X,\qquad
\tau_X=\exp(CX-ce^{2X}).
\tag{12}
\]

There is no invocation of the true-weight operator on \(v_b\).
Put \(M_C=V^*HW_2\). Equations (11), (12) imply

\[
\operatorname{Herm}M_C\preceq M+eI,\qquad
e=C(e_b+\sqrt b/d+\tau_X/d).
\tag{13}
\]

The complete convolution identity and the actual source equation give

\[
h(Cg_a,Cg_c)=-2\langle a,\Delta M_Cc\rangle_P,
\qquad B:=\Delta M_C=B^*,\qquad h=P-N.
\tag{14}
\]

These are the original closed-form identities from the packet theorem;
both prime wings and pole centering are retained. In particular, (14)
does not assert that \(\Delta\) commutes with \(M_C\).

For \(Q=\Delta^{-1}\) and \(D=B-\Delta M=D^*\), (13) says

\[
QD+DQ\preceq2eI.
\]

The positive Sylvester inverse yields

\[
D=\int_0^\infty e^{-sQ}(QD+DQ)e^{-sQ}ds
\preceq e\Delta.
\]

It follows that the complete mixed loss obeys

\[
\boxed{\ h[g_a]-h[Cg_a]
\le C\{de_b+\sqrt b+\tau_X\}\|a\|_P^2.\ }
\tag{15}
\]

Both inverse-depth errors in (13) are paid by the actual spectral-depth
operator in this order argument. No dimension or spectral separation
factor has been used, and the tail error remains linear.

## 4. Frequency loss and complete zero sampling

Choose

\[
\tau=N^{-1},\qquad b=N^{-1/2},\qquad \alpha=b/16,
\qquad e^{2X}=M_0\log N.
\]

The compression estimates give \(e_b\le C_\beta N^{-\beta/2}\)
for every fixed \(\beta<1/2\), and fixed sufficiently large \(M_0\)
makes \(\tau_X=O(N^{-1})\). The complete prime/Gamma comparison in
the packet theorem applies unchanged to (15). Its omitted prime tail
is \(O(N^{-1})\|a\|_P^2\); its low-frequency penalty is
\(O(N^{-1/2}\sqrt{\log N}\log\log(e^eN))\|a\|_P^2\).
Both are absorbed by \(N^{-1/4}\|a\|_P^2\), proving (4).
For (5), choose \(4s<\beta<1/2\) in the dyadic frequency sum.

The weighted-cell interpolation, analytic sampling and common-core
passage in the packet theorem now allow every fixed \(0<t<s<1/8\).
For \(E_\epsilon=\operatorname{Ran}\mathbf1_{[1+\epsilon,\infty)}(A)\),
put \(d_{\min}=\epsilon/(1+\epsilon)\) and
\(J=\log(e/d_{\min})\). There are at most \(CJ\) dyadic bands. Thus

\[
\|(g_a)_o\|_{H^s}^2\le C_sJ\|a\|_P^2,\qquad
\sum_{|\operatorname{Re}z|>T}j_z|\widehat{(g_a)_o}(z)|^2
\le C_tJT^{-2t}\log(2+T)\|a\|_P^2.
\tag{16}
\]

These sums include true zero multiplicities. The same improvement holds
for its weighted first-derivative sampling bound: choose
\(0<t<s_1<s_0<1/8\) in that argument. The original retained-positive
finite-active inequality therefore holds with this larger range of \(t\),
with all its positive terms and the full matrix \(A-I\) retained.

More explicitly, for any fixed \(p>4\), choose
\(1/(2p)<t<1/8\). A sufficiently large constant \(A_p\ge2\) makes

\[
T=A_p(J/\epsilon)^p
\tag{17}
\]

pay the complete discarded high-height cost by
\(\epsilon\|a\|_P^2/4\), uniformly for \(0<\epsilon\le1\).
To see the constant is uniform, write \(y=J/\epsilon\ge1\).
The ratio of the right side of (16) to \(\epsilon\|a\|_P^2\)
is bounded by

\[
C_tA_p^{-2t}y^{1-2tp}
  \{\log(2+A_p)+p\log y\}.
\]

Since \(2tp>1\), its supremum tends to zero as \(A_p\to\infty\).
Choosing the original thin-strip constant small enough pays the other
discarded cost by \(\epsilon\|a\|_P^2/4\). With the packet theorem's
notation for its full positive sum \(P_{\mathrm{all}}\), the result is

\[
\frac12\langle a,(A-I)a\rangle_P+P_{\mathrm{all}}(a)
\le4\sum_{z\in\mathcal A_{\epsilon,T}}
 j_z\bigl(\operatorname{Re}\widehat{(g_a)_o}(z)\bigr)^2,
\tag{18}
\]

for real packets, taking one representative \(z=\gamma-i\beta_z\) per
quartet with \(\gamma>0\), \(\beta_z>0\). Here
\(\mathcal A_{\epsilon,T}\) consists of true off-line quartets with
\(0<\gamma\le T\) and
\(|\beta_z|>c_t\sqrt{\epsilon/J}\langle\gamma\rangle^t\).
This is still a lower sampling frame. Neither (17) nor (18) supplies
the missing upper signed bound, and no numerical value of \(A_p\) or
new zero-free height is claimed.
