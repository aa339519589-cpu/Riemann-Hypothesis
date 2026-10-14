# Actual-vector compression improves the complete mixed smoothing bound

This note improves the depth-uniform scalar source conclusion in
[SOURCE_SMOOTHING.md](SOURCE_SMOOTHING.md) to every \(H^s\) with
\(s<1/8\). It estimates the complete mixed source loss, including its
signed reflected term. The improvement uses the actual source's origin
bound before applying the positive square-root estimate. It does not
replace that mixed loss by a bound on the prime boundary commutator.
No critical sign, supercritical eigenvalue exclusion, or RH proof follows.

## 1. Statement and unchanged actual objects

Let \(g=\psi r\) be any actual pole-centered scalar Green eigen-source,
with \(\lambda>1\), \(\delta=1-\lambda^{-1}\), and \(P_0=P[r]\).
Use the actual source and completion in [the source-tail theorem](REPORT.md).
Set \(v=g/\mu\) on the positive half-line. The complete normalized
reflection is
\[
(\mathcal Rv)(x)=\sum_{n\ge2}\alpha_n\mu(x)\mu(d_n-x)
               \mathbf1_{0<x<d_n}v(d_n-x),\qquad
H=I-\mathcal R,
\]
where \(d_n=\log n\), \(\alpha_n=\Lambda(n)n^{-1/2}\), and
\(\mu^2=\psi/L\). Its unitary equivalence with the
[complete reversible Markov operator](../20261013_reflected_markov_essential_edges/REPORT.md),
together with the existing diagonal reference bound, gives
\[
\|\mathcal R\|\le1,\quad H\succeq0,\quad \|H\|\le2,
\quad N[r]=2\langle v,Hv\rangle,\quad \|v\|^2\le193P_0.
\tag{1}
\]
All prime-power labels are retained.

For every fixed \(0<\beta<1/2\), there are constants and a threshold
independent of the source and of \(\delta\) such that
\[
\boxed{\quad
\int_{|\xi|\ge N}\log(2+|\xi|)|\widehat{g_o}(\xi)|^2d\xi
\le C_\beta P_0\{\delta N^{-\beta/2}+N^{-1/4}\}.
\quad}                                                        \tag{2}
\]
Here \(g_o\) is the odd extension and the Fourier convention is the
one in the source-smoothing report. Consequently
\[
\boxed{\qquad \|g_o\|_{H^s(\mathbb R)}\le C_s\sqrt{P_0},
\qquad 0\le s<1/8.\qquad}                                     \tag{3}
\]
This is a scalar eigen-source statement. No whole-band assertion or
endpoint \(s=1/8\) is made.

## 2. Existing bounded smoothing estimates

Take the same nonnegative compact Poisson kernel as in source smoothing:
\[
k_t^a(u)=\frac{t}{\pi(t^2+u^2)}\chi_0(u/a),\qquad 0<t\le a,
\]
where \(\chi_0\) is fixed, smooth and even, equals one on \([-1,1]\),
vanishes outside \([-2,2]\), and decreases on the positive half-line.
Let \(C\) act by convolution on odd extensions; its propagation is \(2a\).
For the far spatial cutoff \(X\), put
\[
\phi(x)=\log(\mu(x)/\sqrt{x}),\quad
\mu_X(x)=\sqrt{x}\exp(\phi(\min(x,X))),\quad
Z=\mu_X^{-1}C\mu_X,\quad E=Z-C.
\]
The previous estimates give \(K_X\le C e^{2X}\) and
\[
\|Z\|\le1+\varepsilon_0,\qquad
\varepsilon_0=C e^{2aK_X}
       \{t/a+K_Xt\log(1+a/t)\}.                            \tag{4}
\]
Choose parameters with \(\varepsilon_0\le1\).
For a small endpoint scale \(b\), with \(a\le b/16\), equation (3.2)
of source smoothing, applied at scale \(b/2\), gives
\[
\|E\mathbf1_{x\ge b/2}\|+\|\mathbf1_{x\ge b/2}E\|
\le C e^{2aK_X}(K_X+b^{-1})t\log(1+a/t).                    \tag{5}
\]
Its complete coefficient estimate (4.3) gives
\[
\|[C,\mathcal R]\|\le C_\beta t^\beta,
\qquad 0<\beta<1/2.                                       \tag{6}
\]
These are estimates on ordinary half-line \(L^2\). They do not truncate
the prime series.

## 3. Compress the operator after removing the actual endpoint vector

Choose an even smooth multiplier \(\theta_b\), zero for \(|x|\le b/2\),
one for \(|x|\ge b\), with \(0\le\theta_b\le1\) and
\(\|\theta_b'\|_\infty\le C/b\). Denote multiplication by \(\Theta\).
Define
\[
\mathcal R_b=\Theta\mathcal R\Theta,\qquad H_b=I-\mathcal R_b.
\]
For any \(u\),
\(\langle u,\mathcal R_bu\rangle\le\|\Theta u\|^2\le\|u\|^2\).
Hence \(0\preceq H_b\preceq2I\), uniformly in \(b\).

The full-line convolution commutator with the even multiplier gives
\[
\|[C,\Theta]\|\le \frac Cb\int |u|k_t^a(u)du
\le C(t/b)\log(1+a/t).                                    \tag{7}
\]
It preserves the odd subspace, so the same bound holds on the half-line.
Use the exact decomposition
\[
[C,\mathcal R_b]=[C,\Theta]\mathcal R\Theta
 +\Theta[C,\mathcal R]\Theta+\Theta\mathcal R[C,\Theta].
\]
Also \([E,\mathcal R_b]=E\Theta\mathcal R\Theta
-\Theta\mathcal R\Theta E\), and (5) controls both terms. Thus
\[
\|[H_b,Z]\|\le\eta_b,
\quad\eta_b=C_\beta\{t^\beta+
 e^{2aK_X}(K_X+b^{-1})t\log(1+a/t)\}.                     \tag{8}
\]
There is no endpoint operator-norm error \(\sqrt b\) in (8).

Put \(v_b=\mathbf1_{x\ge2b}v\), \(v_0=v-v_b\). The
[origin graph-domain bound](ORIGIN_GRAPH_DOMAIN.md) gives
\(\delta\|g/x\|_{L^2(0,\epsilon/2)}\le C\sqrt{P_0}\).
Since \(\mu(x)^2\asymp x\) at zero, for \(2b<\epsilon/2\),
\[
\delta\|v_0\|\le C\sqrt b\sqrt{P_0}.                    \tag{9}
\]
This step uses the actual vector, rather than an operator norm on arbitrary
endpoint inputs.

Both \(Z\) and \(C\) have propagation \(2a\). Consequently \(Z^2v_b\)
is supported in \(x\ge2b-4a>b\), so
\(\Theta v_b=v_b\) and \(\Theta Z^2v_b=Z^2v_b\). In particular
\[
\langle v_b,H_bZ^2v_b\rangle=\langle v_b,HZ^2v_b\rangle,
\qquad \langle v_b,H_bv_b\rangle=\langle v_b,Hv_b\rangle.
\tag{10}
\]

For \(\eta_b\le1\), the bounded square-root commutator estimate and
mixed inequality in source smoothing, (5.1) and (5.3), apply to \(H_b\)
and \(Z\). Uniformly in \(b\), they give
\[
\operatorname{Re}\langle v_b,H(Z^2-I)v_b\rangle
\le C(\varepsilon_0+\sqrt{\eta_b})\|v_b\|^2.              \tag{11}
\]
The norm of \(H(Z^2-I)\) is uniformly bounded by (1), (4). Replacing
\(v_b\) by \(v\) therefore costs at most
\(C\|v_0\|\|v\|\). Multiplying by \(\delta\), (1) and (9) yield
\[
\boxed{\quad
\delta\operatorname{Re}\langle v,H(Z^2-I)v\rangle
\le CP_0\{\delta(\varepsilon_0+\sqrt{\eta_b})+\sqrt b\}.
\quad}                                                        \tag{12}
\]
The sharp cutoff of \(v\) in this argument is only a decomposition of a
vector in a bounded-operator estimate. It is never asserted to be a legal
test in the source completion.

## 4. True weight, actual equation, and Fourier loss

Keep the legal source tests \(Cg\) and \(C^2g\) exactly as in source
smoothing, §§6–7. Write \(w_2=(C^2g)/\mu\). Its true-weight replacement
is the established linear estimate
\[
\|w_2-Z^2v\|\le T_\delta(X,a)\sqrt{P_0},\qquad
\delta T_\delta(X,a)\le C\exp(CX-ce^{2X}).                 \tag{13}
\]
Apply (13) to the original full vector \(v\), before any endpoint
decomposition. No action of the true-weight operator on \(v_b\) is needed.
The actual equation and the unchanged factor two in (1) give
\[
h[g]-h[Cg]=2\delta\operatorname{Re}\langle v,H(w_2-v)\rangle,
\qquad h=P-N.
\]
Equations (12)–(13) thus prove the complete one-sided mixed loss estimate
\[
h[g]-h[Cg]\le CP_0\{
\delta(\varepsilon_0+\sqrt{\eta_b})+\sqrt b+\delta T_\delta\}.
\tag{14}
\]
Every reflection term remains inside \(H\). There is no quadratic
\(T_\delta^2\) error and no use of a sign for the separate prime collar.

For sufficiently large \(N\), choose
\[
t=N^{-1},\quad b=N^{-1/2},\quad a=b/16,
\quad e^{2X}=M\log N.
\]
The fixed constant \(M\) can make \(\delta T_\delta=O(N^{-1})\).
All parameter thresholds are independent of \(\delta\).
For every fixed \(\beta<1/2\), (4) and (8) give
\(\varepsilon_0+\sqrt{\eta_b}\le C_\beta N^{-\beta/2}\);
the factors \(N^{-1/2}\log N\) inside \(\eta_b\) are absorbed by
\(N^{-\beta}\). Thus
\[
h[g]-h[Cg]\le C_\beta P_0
       \{\delta N^{-\beta/2}+N^{-1/4}\}.                 \tag{15}
\]

The full prime-tail and Gamma lower-loss argument in source smoothing,
§§9.1–9.2, applies with these same parameters. Changing \(a=b/8\) to
\(b/16\) changes only fixed constants: \(t/a=16N^{-1/2}\), so its
low-frequency multiplier estimate and high-frequency damping still hold.
With the finite prime cut at \(L\log N\), the omitted complete tail is
\(O(N^{-1})P_0\), and the finite-prime low-frequency penalty is
\(O(N^{-1/2}\sqrt{\log N}\log\log(e^eN))P_0\).
Both are absorbed by \(N^{-1/4}P_0\). The complete Gamma loss then
combines with (15) to prove (2).

Dyadic summation proves (3): for any \(s<1/8\), choose
\(4s<\beta<1/2\), so both powers in (2) exceed \(2s\).
The bounded-frequency part is covered by (1) and boundedness of \(\mu\).

## 5. Consequences and limits

The weighted Sobolev argument in
[ENDPOINT_PRIME_PAIRING.md, (2)](ENDPOINT_PRIME_PAIRING.md) uses only
the available source Sobolev order and the fixed theta spatial envelope.
Using (3), it now gives each fixed weighted order \(s<1/8\).
Repeating the exact translated-load and source-equation proof of
[FRACTIONAL_ORIGIN_BOUNDARY.md](FRACTIONAL_ORIGIN_BOUNDARY.md) therefore gives
its local \(r,g/x,W\) estimates and
\[
\delta|D_{\rm pr}|\le C_{k,s}a^{1+2s}P_0
\quad\text{for every fixed }0<s<1/8.
\]
These remain below the trace threshold. Neither the improved complete
mixed bound nor this absolute collar bound proves
\(D_V<D_{\rm pr}\) for an actual largest eigen-source. The complete
coefficient-one Green comparison remains unresolved.
