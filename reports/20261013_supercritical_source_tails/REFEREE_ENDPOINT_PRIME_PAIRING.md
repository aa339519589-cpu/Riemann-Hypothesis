# Independent referee check: endpoint signed-prime pairing

I independently checked [ENDPOINT_PRIME_PAIRING.md](ENDPOINT_PRIME_PAIRING.md),
including its weighted Sobolev input, Abel multiplier, local identification
of the full prime distribution, endpoint Hardy estimate, and polynomial zero
sampling consequence. **Disposition: pass**, conditional on the cited actual
source smoothing theorem and its pole-centering identity. I found no missing
prime labels, sign error, depth-dependent constant, or unlicensed pointwise
source evaluation.

This is an independent automated mathematical read-through, not a proof-assistant
certificate or an external human peer review.

## Weighted Sobolev input

The estimate (1) follows directly from $g_o=\mu v_o$, the uniform $L^2$
bound for $v_o$, and the fixed double-exponential envelope for $\mu$. In
(4), interpolate the unweighted translation increment
$\|g_o(\cdot+h)-g_o\|_2=O(|h|^{s_0})$ with its uniformly bounded
$e^{A|x|}L^2$ increment. The pointwise geometric-mean inequality gives the
exponent $s_0(1-A_0/A)$ displayed there. Taking $A$ large enough, then
applying the difference-quotient characterization and the Lipschitz weight
increment, proves (2). Choosing $A_0>1/2+a$ makes the multiplier in (5),
as well as its product with $e^{a|x|}$, bounded Lipschitz. Thus $f\in H^t$
and $e^{a|x|}f\in L^2$ with constants proportional to $\sqrt M$. This
argument uses only translation $L^2$ estimates and does not presume a
continuous representative of $g_o$.

## Multiplier and the full arithmetic distribution

With the stated positive-exponent Fourier convention, the atom at
$d_n=\log n$ contributes $e^{i\xi d_n}$, while the continuous half-line
contributes $(\varepsilon-i\xi)^{-1}$. Hence (6) has the displayed sign and
the Euler product includes all prime powers. For each $\varepsilon>0$, the
Abel measure has finite total variation, so its convolution and multiplier
identity are valid on $L^2$.

The Hadamard difference in the proof of (7) is correctly signed:
\[
 \frac{\xi'}{\xi}(s)-\frac{\xi'}{\xi}(s_0)
 =(s_0-s)\sum_\rho\frac1{(s-\rho)(s_0-\rho)},
 \qquad s=\sigma+it,\quad s_0=2+it.
\]
The difference series is absolutely convergent. In the near unit-height
window the zero-free gap bounds each first denominator below by
$c/\log(2+|t|)$; the local zero count is $O(\log(2+|t|))$, yielding
$O(\log^2(2+|t|))$. In farther unit shells both denominators give the
reciprocal-square majorant and the summed contribution is
$O(\log(2+|t|))$. The anchor and gamma factors are $O(\log(2+|t|))$, which
proves the required uniform estimate through $\sigma=1$. Near $s=1$,
$-\zeta'/\zeta(1+w)-1/w=-\gamma+O(w)$; away from this pole, compactness
and the zero-free line give the remaining bounded-frequency estimate.
These facts establish (8) uniformly for all $0<\varepsilon\le1$. The
cited Mossinghoff--Trudgian--Yang explicit zero-free region is a valid
primary source for the zero-free input; its stronger explicit constants are
not needed.

Since $\log^4(2+|\xi|)\lesssim_t(1+\xi^2)^t$ for each fixed $t>0$,
Plancherel and dominated convergence give (9)--(10), uniformly after source
normalization. The local identification is also valid: on a compact
$K\subset[-R,R]$, the exponential $L^2$ bound for $f$ makes the translated
atom norms summable against $\Lambda(n)/n$, since the tail is bounded by
$C\sum_n\Lambda(n)n^{-1-a}$. The continuous tail is controlled in the
same way. Thus the Abel convolutions converge locally in $L^2$ to the
actual atomic-minus-continuous convolution. This identifies the distribution
without total-variation convergence of $\nu$ and without sampling $f$ at
any prime point.

## Centering, signs, and the endpoint Hardy space

Oddness and the actual pole-centering condition give
\[
 \int_{\mathbb R}f=-2\int_0^\infty\sinh(x/2)g(x)\,dx=0.
\]
Consequently the continuum term in (11) is the tail primitive
$I(x)=-\int_x^\infty f(y)\,dy$ for $x>0$, with the stated exponential
$L^2$ bound. For $x>0$, the odd reflection yields
\[
 e^{-x/2}(F_b-F_r)
 =\sum_n\frac{\Lambda(n)}n f(x-\log n)
 =Tf+I.
\]
The conversion factor is $(\Lambda(n)/n)e^{d_n/2}=\Lambda(n)/\sqrt n$,
so the identity has the correct sign and normalization. Equality is in
local $L^2$, which is sufficient to combine the global $L^2$ bounds.

Inserting this in [EDGE_CARLEMAN.md, (6)](EDGE_CARLEMAN.md) proves (15) with
$M$-uniform constants. Only the signed difference $F_b-F_r$ obtains the
endpoint norm; the note correctly makes no claim for either unsigned prime
sum, for $r$ without a weight, or for an endpoint estimate from the old
arbitrary-$C>1$ bounds alone.

Writing $w=\mathbf1_{x>0}e^{-x/2}W$, the transform on
$\operatorname{Im}z=1/2+\varepsilon$ is the Fourier transform of
$e^{-\varepsilon x}w$. Plancherel gives (16) uniformly over the whole open
half-plane, and dominated convergence gives its $L^2$ boundary value as
$\varepsilon\downarrow0$. This does not assert absolute convergence of the
original integral on the boundary. Holomorphic continuation of the already
established identity $B_{\rm ent}=\Xi C_+$ from
$\operatorname{Im}z>2$ to $\operatorname{Im}z>1/2$ is a valid
identity-theorem step and does not alter residues.

## Polynomial zero-square sampling

For fixed $q<1/8$, select $s$ with $q/2<s<1/16$. The weighted Sobolev
bound (2) and multiplication by $e^{-\eta x-A_0|x|}$, with fixed
$A_0>3/4$, give the uniform tilted $H^s$ bound (18) on
$|\eta|\le3/4$. The short-interval Riemann--von Mangoldt estimate counts
zeros with multiplicity by $O(\log(2+|T|))$; the disk submean inequality
and Tonelli then reduce the sampling sum to the displayed area integral.
Its frequency weight is absorbed by $(1+t^2)^s$ exactly when $q<2s$,
proving (17). The strict endpoint $q<1/8$ is therefore appropriate; no
zero separation, simple-zero assumption, endpoint exponent, or lower
sampling estimate is used.

The endpoint result supplies a boundary $L^2$ value for the ordinary
current transform and an absolute zero-square upper sampling estimate. It
does not give a zero-free continuation below the strip edge, a coefficient-
one sign comparison, or an RH conclusion.
