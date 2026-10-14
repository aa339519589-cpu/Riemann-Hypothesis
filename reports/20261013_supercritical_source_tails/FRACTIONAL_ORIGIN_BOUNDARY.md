# Fractional origin control and a sharper complete prime-boundary bound

For each actual scalar supercritical Green source, the complete translated
prime loads are locally in every fixed \(H^s\), \(0<s<1/16\), uniformly
in its depth. The source equation then puts its ratio and reflected
divergence in the same local space, with a displayed \(\delta^{-1}\) loss.
For the exact odd convolution variation this improves the complete boundary
estimate from \(O(a)\) to \(O(a^{1+2s})\), after multiplication by \(\delta\).
This is an absolute estimate. It supplies neither a boundary trace nor the
signed comparison needed to exclude the source. RH remains unproved.

## 1. Actual source and statement

Use the actual gradient completion and centered scalar eigen-source in
[the source-tail theorem](REPORT.md). Put
\[
g=\psi r,\quad \psi=-\Phi',\quad P_0=P[r],\quad
\lambda>1,\quad \delta=1-\lambda^{-1},\quad
d_n=\log n,\quad \alpha_n=\Lambda(n)n^{-1/2},
\]
\[
L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x),\qquad
V=L/\psi,\qquad \mu^2=1/V.
\]
The source is pole-centered. Let \(g_o\) be its odd extension, and
\(B_o\) the positive-wing restriction of the full logarithmic multiplier
\(b(D)\), with the normalization of
[the origin graph-domain theorem](ORIGIN_GRAPH_DOMAIN.md).

Fix \(0<\epsilon<\log2/4\), set \(I=(0,\epsilon)\), and define on \(I\)
\[
F_\pm(x)=\sum_{n\ge2}\alpha_n g(d_n\pm x),\qquad
\mathcal F_g=F_++F_-,\qquad W=Lr-F_-.
\]
Every prime-power label is included. Sobolev spaces on \(I\) are restriction
spaces with their usual fixed-interval norm. For every \(0<s<1/16\),
\[
\boxed{\begin{aligned}
\|F_+\|_{H^s(I)}+\|F_-\|_{H^s(I)}+\|B_og\|_{H^s(I)}
 &\le C_{s,\epsilon}\sqrt{P_0},\\
\delta\bigl(\|r\|_{H^s(I)}+\|g/x\|_{H^s(I)}
                   +\|W\|_{H^s(I)}\bigr)
 &\le C_{s,\epsilon}\sqrt{P_0}.
\end{aligned}}                                                     \tag{1}
\]
Constants may depend on the fixed theta kernel and displayed fixed
parameters, but not on the source, \(\lambda\), or \(\delta\).
The statement does not require \(\lambda\) to be the largest eigenvalue.

## 2. Convergence of the complete loads in the fractional norm

The [source smoothing theorem, (9.11)](SOURCE_SMOOTHING.md) and
the [diagonal reference bound, (4)](../20261013_full_prime_green_reference/THREE_HALVES_BOUND.md)
give, for every \(s_0<1/16\),
\[
M:=\|g/\mu\|_2^2\le193P_0,\qquad
\|g_o\|_{H^{s_0}(\mathbb R)}\le C_{s_0}\sqrt{P_0}.
\tag{2}
\]
The weighted Sobolev lemma already proved in
[the endpoint prime-pair report, (2)](ENDPOINT_PRIME_PAIRING.md) gives
\[
\|e^{A|x|}g_o\|_{H^s(\mathbb R)}
\le C_{A,s}\sqrt{P_0}
\quad(A>0\text{ fixed},\ 0<s<1/16).                       \tag{3}
\]
It combines (2) with the fixed theta envelope for \(\mu\); it has no
negative power of \(\delta\). We use it as an existing input.

Choose an even smooth cutoff \(\eta\), supported in
\((-2\epsilon,2\epsilon)\), equal to one on
\([-\epsilon,\epsilon]\). Put \(w(x)=e^{|x|}g_o(x)\).
Since \(d_n-2\epsilon>0\), on the support of \(\eta\) the exact identity is
\[
\eta(t)g(d_n+t)=n^{-1}\eta(t)e^{-t}w(d_n+t).
\]
Translation invariance and the fixed smooth multiplier bound in \(H^s\)
therefore give
\[
\|\eta(\cdot)g(d_n+\cdot)\|_{H^s(\mathbb R)}
\le C_{s,\epsilon}n^{-1}\sqrt{P_0}.                       \tag{4}
\]
Reflection gives the same bound for \(g(d_n-t)\). Moreover
\[
\sum_{n\ge2}\alpha_n n^{-1}
\le\sum_{n\ge2}(\log n)n^{-3/2}<\infty.
\]
Thus both complete cutoff load series converge absolutely in
\(H^s(\mathbb R)\), and their restrictions prove the two load bounds
in (1). Their limits agree with the existing local \(L^2\) definitions.
This uses translated functions, with no value assigned at an individual
prime logarithm.

## 3. The ratio and divergence from the actual equation

Choose \(s<s_0<1/16\). Since
\(b(\xi)\le C_{s,s_0}\langle\xi\rangle^{s_0-s}\), (2) implies
\[
\|b(D)g_o\|_{H^s(\mathbb R)}\le C_{s,s_0}\sqrt{P_0}.
\tag{5}
\]
Its restriction is \(B_og\), proving the remaining first-line bound
in (1). This is a consequence of the known positive Sobolev order of
\(g_o\); it asserts no positive-order gain from inverting \(b(D)\).

The actual local equation, with all labels outgoing on \(I\), is
\[
B_og+\delta Vg=C_0g+F_+-(1-\delta)F_-.
\tag{6}
\]
Here the coefficient and positive-wing normalization are exactly those
in [the origin theorem, (12)](ORIGIN_GRAPH_DOMAIN.md). On this interval
\(Vg=Lr\). The complete row \(L\) is smooth on \([0,\epsilon]\) and
strictly positive there: all its fixed derivative series converge normally,
and no reflection threshold occurs below \(\log2\). Dividing (6) by
\(\delta L\) is therefore a bounded smooth-multiplier operation in
\(H^s(I)\), apart from the explicit \(\delta^{-1}\). This proves
the ratio estimate. The function \(\psi(x)/x\) extends smoothly across
zero, so the same estimate holds for \(g/x=(\psi/x)r\).

For the complete reflected divergence, the equation gives exactly
\[
\delta W=C_0g+F_+-F_--B_og.                              \tag{7}
\]
Equations (2), (4), and (5) finish (1). These are conclusions for the
actual source class, not substituted compact core vectors.

## 4. Uniform power saving in the complete boundary term

For \(0<s<1/16\), set \(p_s=2/(1-2s)\). Fixed-interval Sobolev
embedding \(H^s(I)\hookrightarrow L^{p_s}(I)\) and Hölder's inequality
give, for \(0<t<\epsilon\),
\[
\begin{aligned}
\|g/x\|_{L^2(0,t)}&\le C_{s,\epsilon}\delta^{-1}t^s\sqrt{P_0},\\
\|g\|_{L^2(0,t)}&\le C_{s,\epsilon}\delta^{-1}t^{1+s}\sqrt{P_0},\\
\|\mathcal F_g\|_{L^2(0,t)}&\le C_{s,\epsilon}t^s\sqrt{P_0}.
\end{aligned}                                                     \tag{8}
\]
Take the legal real even profile \(k\in C_c^\infty((-1,1))\) and
\(k_a(t)=a^{-1}k(t/a)\) from
[the complete odd variation](../20261013_full_prime_green_reference/ODD_VARIATION_PRIME_BOUNDARY.md).
Take \(a\) below its fixed domain threshold and
\(4a<\min(\epsilon,\log2)\). Its exact all-prime triangular pairing,
with the unchanged normalization
\(N[C_ag]-\operatorname{Re}N(g,C_a^2g)=2(D_V-D_{\rm pr})\), satisfies
\[
|D_{\rm pr}|\le C_k a
       \|g/x\|_{L^2(0,2a)}\|\mathcal F_g\|_{L^2(0,2a)}.
\tag{9}
\]
This is the odd-kernel cancellation and triangle estimate proved there;
it includes both sides and both corners of every actual reflected edge.
Substitute (8) in (9) to obtain
\[
\boxed{\qquad
\delta|D_{\rm pr}|\le C_{k,s,\epsilon}\,a^{1+2s}P_0,
\qquad 0<s<1/16.
\qquad}                                                        \tag{10}
\]
Equivalently every fixed exponent \(1+\theta\), \(0<\theta<1/8\),
is allowed. The endpoint \(\theta=1/8\) is not asserted.

For a largest supercritical source, the existing variational inequality
therefore gives only
\(\delta D_V\ge-C_{k,s,\epsilon}a^{1+2s}P_0\).
The estimates remain below the Sobolev trace threshold and do not justify
an endpoint Taylor expansion. The unresolved exclusion step is still to
prove \(D_V<D_{\rm pr}\) for a legal kernel and that actual source.
