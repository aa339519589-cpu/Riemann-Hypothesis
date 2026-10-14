# Endpoint \(C=1\) for the complete signed prime pair

This note proves the endpoint estimate for the complete backward-minus-reflected prime sum in [EDGE_CARLEMAN.md](EDGE_CARLEMAN.md). It uses the actual-source estimate from [SOURCE_SMOOTHING.md](SOURCE_SMOOTHING.md) and the classical unconditional zero-free region at \(\sigma=1\). Every von Mangoldt label is retained. The proof is an \(L^2\) Fourier-multiplier argument: it never samples the source at prime points and does not assert that the atomic prime measure converges in total variation.

The signed-pair endpoint gives a uniform Hardy norm for the ordinary
current transform on the whole half-plane Im z>1/2 and its L2 boundary
value. The same weighted source lemma also gives the polynomial
zero-square estimate (17). There are no separate endpoint bounds for
the two unsigned prime sums, and no critical sign or RH conclusion.

## The statement

Let \(g\) be an actual pole-centered source from the open-edge theorem, set \(g_o\) to be its odd extension, and put
\[
 d_n=\log n,\qquad \alpha_n=\Lambda(n)n^{-1/2},\qquad
 F_b(x)=\sum_{d_n<x}\alpha_n g(x-d_n),\quad
 F_r(x)=\sum_{d_n>x}\alpha_n g(d_n-x).
\]

Write \(M=\|g/\mu\|_{L^2(0,\infty)}^2\). The source-smoothing theorem gives, for every \(s_0<1/16\),
\[
 \|g_o\|_{H^{s_0}(\mathbb R)}\le C_{s_0}\sqrt M.
\]
Also \(g_o(x)=\mu(|x|)v_o(x)\), with \(\|v_o\|_2=\sqrt{2M}\). The fixed theta envelope for \(\mu\) implies, for every \(A>0\),
\[
 \|e^{A|x|}g_o\|_2\le C_A\sqrt M. \tag{1}
\]
Consequently, for every \(0<t<1/16\),
\[
 \|e^{A_0|x|}g_o\|_{H^t}\le C_{A_0,t}\sqrt M
 \quad\text{for each fixed }A_0>0. \tag{2}
\]
This is the spatial-cutoff/interpolation step; a proof is given below.

The endpoint conclusion is
\[
 \boxed{\quad
 \left\|e^{-x/2}\big(F_b-F_r\big)\right\|_{L^2(0,\infty)}
 \le C\sqrt M,
 \quad} \tag{3}
\]
where \(C\) depends on a fixed \(t\in(0,1/16)\) and on the theta kernel, but not on the source, its depth \(\delta\), or any truncation in \(n\). In particular, the constant is depth-uniform under the normalization \(M=1\).

## Weighted Sobolev input without point values

For completeness, fix \(0<t<s_0<1/16\) and a target weight \(A_0>0\). For \(0<|h|\le1\), the Fourier definition of \(H^{s_0}\) gives
\[
 \|g_o(\cdot+h)-g_o\|_2\le C|h|^{s_0}\|g_o\|_{H^{s_0}}.
\]
For any \(A>A_0\), translation and (1) give
\[
 \|e^{A|x|}(g_o(x+h)-g_o(x))\|_2\le C_A\sqrt M,
\]
uniformly for \(|h|\le1\). Hölder interpolation between these two norms yields
\[
 \|e^{A_0|x|}(g_o(\cdot+h)-g_o)\|_2
 \le C|h|^{s_0(1-A_0/A)}\sqrt M. \tag{4}
\]
Choose \(A\) so large that \(s_0(1-A_0/A)>t\). The difference-quotient characterization of \(H^t\), together with the Lipschitz bound
\[
 |e^{A_0|x+h|}-e^{A_0|x|}|\le C_{A_0}|h|e^{A_0|x|}\quad(|h|\le1),
\]
then gives (2). This argument uses only \(L^2\) increments; it assumes no continuous representative or pointwise prime samples.

Choose \(A_0>1/2\) and set
\[
 f(x)=e^{-x/2}g_o(x).
\]
Since \(f=e^{-x/2-A_0|x|}(e^{A_0|x|}g_o)\), and the prefactor is bounded and Lipschitz, (2) implies
\[
 \|f\|_{H^t}+\|e^{a|x|}f\|_2\le C_{t,a}\sqrt M
 \quad (0<a<A_0-1/2). \tag{5}
\]
One can first take \(A_0>1/2+a\); all constants remain independent of \(\delta\).

## A log-prime convolution multiplier

Define the signed measure on the log-prime line
\[
 \nu=\sum_{n\ge2}\frac{\Lambda(n)}n\,\delta_{\log n}-\mathbf1_{[0,\infty)}(u)\,du.
\]
This notation is distributional: \(\nu\) has infinite total variation, and no total-variation convergence to Lebesgue measure is claimed. For \(0<\varepsilon\le1\), its Abel regularization
\[
 d\nu_\varepsilon(u)=e^{-\varepsilon u}d\nu(u)
\]
is a finite signed measure. With the Fourier convention \(\widehat f(\xi)=\int f(x)e^{i\xi x}dx\), the convolution
\[
 (\nu_\varepsilon*f)(x)=\int f(x-u)\,d\nu_\varepsilon(u)
\]
has multiplier
\[
 m_\varepsilon(\xi)
 =-\frac{\zeta'}{\zeta}(1+\varepsilon-i\xi)
   -\frac1{\varepsilon-i\xi}. \tag{6}
\]
Indeed, the atomic series is the absolutely convergent Euler-product identity
\(\sum_{n\ge2}\Lambda(n)n^{-1-\varepsilon+i\xi}=-\zeta'(1+\varepsilon-i\xi)/\zeta(1+\varepsilon-i\xi)\), and the continuous term has transform
\(\int_0^\infty e^{-\varepsilon u+i\xi u}du=(\varepsilon-i\xi)^{-1}\). This explicitly keeps all prime powers.

The classical unconditional zero-free region gives, for some fixed \(c>0\), no zeros of \(\zeta\) in \(\sigma\ge1-c/\log(|t|+3)\) at large \(|t|\). The standard local logarithmic-derivative formula and \(O(\log T)\) zero count in unit-height windows therefore give
\[
 \left|\frac{\zeta'}{\zeta}(\sigma+it)\right|
 \le C\log^2(|t|+3),\qquad 1\le\sigma\le2,\ |t|\ge3. \tag{7}
\]
Here is a direct justification of the required uniformity. For
s=σ+it, 1<=σ<=2, and s0=2+it, the regularized Hadamard difference is

    xi'/xi(s)-xi'/xi(s0)
      =(s0-s) sum_rho 1/[(s-rho)(s0-rho)].

The sum is absolutely convergent and keeps all zero multiplicities.
For |Im rho-t|<=1, the zero-free region gives |s-rho|>=c/log(2+|t|),
while |s0-rho|>=1; the O(log(2+|t|)) local zero count therefore pays
this part by O(log^2(2+|t|)). For farther unit shells, the two denominators
supply a reciprocal-square factor, and their locally counted sum is
O(log(2+|t|)). The Euler series at s0 and Stirling give
xi'/xi(s0)=O(log(2+|t|)); subtracting the elementary factors and the
Gamma logarithmic derivative gives (7). The argument is uniform up to
σ=1 for large |t|. This is the usual logarithmic-derivative consequence
of the effective PNT zero-free input; for example the classical \(\Psi(X)=X+O(Xe^{-c\sqrt{\log X}})\) is obtained from the same region. It is enough here to use the weaker log-squared bound (7). The explicit zero-free region in [Mossinghoff–Trudgian–Yang, arXiv:2212.06867v1](https://arxiv.org/abs/2212.06867v1) is more than sufficient, but no numerical zero-free constant is needed. In particular, no \(7/8\) input is used.

At bounded \(\xi\), the pole is canceled in (6): the Laurent expansion at \(s=1\) is
\[
 -\zeta'(s)/\zeta(s)=\frac1{s-1}-\gamma+O(s-1),
\]
so \(m_\varepsilon(\xi)\) remains bounded as \(\varepsilon,\xi\) tend to zero. Away from that neighborhood, \(\zeta\) has no zeros on or to the right of \(\sigma=1\), as in [NIST DLMF 25.10(i)](https://dlmf.nist.gov/25.10.i), and compactness gives a uniform bound. Combining with (7),
\[
 \sup_{0<\varepsilon\le1}|m_\varepsilon(\xi)|
 \le C\log^2(2+|\xi|). \tag{8}
\]
For every fixed \(t>0\), \(\log^4(2+|\xi|)\le C_t(1+\xi^2)^t\). Plancherel therefore gives
\[
 \|\nu_\varepsilon*f\|_2\le C_t\|f\|_{H^t}, \tag{9}
\]
uniformly in \(\varepsilon\). As \(\varepsilon\) decreases to zero, \(m_\varepsilon(\xi)\) converges pointwise to the pole-subtracted multiplier
\[
 m(\xi)=-\frac{\zeta'}{\zeta}(1-i\xi)-\frac1{-i\xi},
\]
with its removable value at \(\xi=0\). By (8) and dominated convergence, \(\nu_\varepsilon*f\) converges in global \(L^2(\mathbb R)\) to a function denoted \(Tf\), and
\[
 \|Tf\|_2\le C_t\|f\|_{H^t}. \tag{10}
\]

It remains to identify this limit with the actual atomic-minus-continuous convolution; this is where the spatial weight in (5) pays the tail, in \(L^2\) rather than at selected points. If \(K\subset[-R,R]\) is compact and \(d\ge R+1\), then
\[
 \|\mathbf1_K f(\cdot-d)\|_2
 \le e^{-a(d-R)}\|e^{a|\cdot|}f\|_2.
\]
Consequently,
\[
 \sum_{n\ge2}\frac{\Lambda(n)}n
       \|\mathbf1_K f(\cdot-\log n)\|_2<\infty,
\]
because the tail is bounded by a constant times \(\sum_n\Lambda(n)n^{-1-a}\). The continuous tail has the analogous bound \(\int_{R+1}^\infty e^{-a(u-R)}du<\infty\). Dominated convergence in these local \(L^2\) sums proves that \(Tf\) is exactly the local \(L^2\) limit of
\[
 \sum_{n\ge2}\frac{\Lambda(n)}n f(x-\log n)
       -\int_0^\infty f(x-u)du. \tag{11}
\]
This identifies the complete arithmetic distribution without requiring pointwise values of \(f\).

## Pole centering and the boundary estimate

By oddness,
\[
 \int_{\mathbb R}f(y)dy
 =\int_0^\infty\big(e^{-y/2}-e^{y/2}\big)g(y)dy
 =-2\int_0^\infty\sinh(y/2)g(y)dy=0. \tag{12}
\]
Thus the continuum term in (11) is
\[
 I(x)=\int_0^\infty f(x-u)du=\int_{-\infty}^x f(y)dy
 =-\int_x^\infty f(y)dy.
\]
For \(x\ge0\), (5) and Cauchy--Schwarz give
\[
 |I(x)|\le (2a)^{-1/2}e^{-ax}\|e^{a(\cdot)}f\|_{L^2(0,\infty)},
 \qquad \|I\|_{L^2(0,\infty)}\le (2a)^{-1}\|e^{a(\cdot)}f\|_{L^2(0,\infty)}. \tag{13}
\]

For \(x>0\), the odd extension gives the exact complete signed-pair identity in local \(L^2\):
\[
\begin{aligned}
 e^{-x/2}(F_b(x)-F_r(x))
 &=e^{-x/2}\sum_{n\ge2}\alpha_n g_o(x-\log n)\\
 &=\sum_{n\ge2}\frac{\Lambda(n)}n f(x-\log n)\\
 &= Tf(x)+I(x).
\end{aligned} \tag{14}
\]
The equality at the boundary \(x=\log n\) is immaterial in \(L^2(dx)\). Combining (5), (10), and (13) proves (3).

## Consequence for the complete divergence and its Hardy boundary

The already proved actual-source identity in [EDGE_CARLEMAN.md, (6)](EDGE_CARLEMAN.md) is

    delta W=C0g+F_++F_b-F_r-B_o g.

The complete forward sum F_+ and B_o g are in ordinary L2 with norms
bounded by a fixed constant times sqrt(M); so is g. Restriction to x>0
and multiplication by exp(-x/2) cannot increase any of these norms.
Together with (3), this proves the new endpoint conclusion

    integral_0^infinity exp(-x)|W(x)|^2 dx
      <=C delta^(-2)M <=193C delta^(-2)P[r].                 (15)

This is a bound for the signed divergence W. It is not a separate bound
for Lr or F_r at this weight, nor an unweighted L2 assertion for r.

Let C_+(z) be the same ordinary integral and B_ent its existing entire
numerator. On Im z>1/2 it converges absolutely as already proved.
Equation (15) strengthens its Hardy estimate to the whole open half-plane:

    sup_(sigma>1/2) integral_R |C_+(t+i sigma)|^2 dt
      <=2pi C delta^(-2)M.                                 (16)

Indeed let w(x)=1_(x>0)exp(-x/2)W(x) in ordinary L2(R). Then
C_+(t+i(1/2+epsilon)) is the Fourier transform of exp(-epsilon x)w(x).
Plancherel and dominated convergence also give its boundary convergence
in L2(dt) as epsilon decreases to zero, to the Fourier transform of w.
This specifies an L2 boundary value, without claiming absolute convergence
of the original integral on the boundary line. The pointwise interior
bound is C delta^(-1)sqrt(M)/sqrt(2(sigma-1/2)).

The same B_ent=Xi C_+ and all signed residues remain unchanged. The
whole-half-plane Hardy norm supplies no pole-free continuation below
Im z=1/2. No nontrivial zero is excluded.

## A depth-uniform polynomial zero-square sampling consequence

For completeness the weighted source lemma (2) gives a second consequence
of the same smoothing input. Set G(z)=integral_R g_o(x)exp(izx)dx and
Xi(z)=xi(1/2+iz). For every fixed 0<=q<1/8,

    sum_(Xi(zeta)=0) m_zeta (1+|Re zeta|)^q |G(zeta)|^2
      <=C_q M,                                             (17)

where each distinct nontrivial zero is listed once with its true
multiplicity m_zeta. Constants are independent of delta and the source.

To prove this, choose q/2<s<1/16. Equation (2), followed by multiplication
by exp(-eta x-A0|x|) for a fixed A0>3/4, gives

    sup_(|eta|<=3/4)||exp(-eta x)g_o||_(H^s)<=C_s sqrt(M).  (18)

The multipliers are bounded and Lipschitz uniformly in that compact eta
interval, which suffices on H^s with 0<s<1. The all-exponential L2
bounds also give all-exponential L1 bounds, so G is entire and
G(t+i eta) is exactly the Fourier transform of exp(-eta x)g_o.

The short-interval Riemann--von Mangoldt count, including multiplicity,
is O(log(2+|T|)) on every unit height interval. This follows by subtracting
the formula at T+1 and T with its O(log(2+T)) remainder; a global
O(T log T) count alone would not be sufficient. In height coordinates
all zeros have |Im zeta|<1/2. Fix 0<r<1/4. The analytic disk mean-value
inequality gives

    |G(zeta)|^2 <= (pi r^2)^(-1) integral_(|z-zeta|<r)|G(z)|^2 dA(z).

After multiplication by m_zeta (1+|Re zeta|)^q, Tonelli and the unit-height
count bound the sum by

    C integral_(-3/4)^(3/4) integral_R
       (1+|t|)^q log(2+|t|)|G(t+i eta)|^2 dt d eta.

Since q<2s, the frequency weight is bounded by C_(q,s)(1+t^2)^s.
Plancherel and (18) prove (17). There is no separation or simplicity
assumption for the zeros. The strict q<1/8 restriction pays both the
Sobolev interpolation loss and the logarithm in the overlap count.
No assertion at q=1/8, derivative sampling, lower sampling estimate,
or signed coefficient-one comparison is made.

## Scope

The endpoint loss from treating \(F_b\) and \(F_r\) separately is removed only after their full signed pairing. This proves depth-uniform \(e^{-x/2}(F_b-F_r)\in L^2(0,\infty)\) and supplies an endpoint term suitable for the exact identity \(\delta W=C_0g+F_++F_b-F_r-B_og\). It does not prove either unsigned series has this endpoint norm, and it does not justify an absolutely convergent Laplace integral on the boundary line. Any boundary value there is an \(L^2\) Fourier boundary value.


The independent proof checks are recorded in
[REFEREE_ENDPOINT_PRIME_PAIRING.md](REFEREE_ENDPOINT_PRIME_PAIRING.md).
