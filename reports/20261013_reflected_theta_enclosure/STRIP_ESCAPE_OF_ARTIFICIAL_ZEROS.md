# Spurious zeros of every fixed reflected Eisenstein-theta truncation escape arbitrarily far right

Date: 2026-10-13. New structural obstruction for the exact fixed-principal denominator studied in the immediately preceding [reflected theta enclosure](REPORT.md). This note strengthens its fixed-cutoff zero statement from "infinitely many zeros with real part >1/2" to **zeros with unbounded positive real parts, in particular infinitely many in the Euler-product zero-free half-plane Re s>1**. It gives an explicit finite-height zero-exclusion test in *every bounded vertical strip* for the truncated completed function.

These are zeros of the **finite approximation**, never asserted to be zeros of the actual Dedekind zeta function. The growing-cutoff, finite-height enclosure and all of its retained coherent cross terms remain unchanged. No RH theorem is inferred.

## Exact original objects

Use the unchanged Eisenstein ideal theta series and reflection from REPORT.md. Put
\[
a=\frac{2\pi}{\sqrt3},\qquad
\Theta(u)=\sum_{z\in\mathbb Z[\omega]}e^{-au N(z)}
          =1+6\sum_{n\ge1}r(n)e^{-anu},\qquad
\Theta(u)=u^{-1}\Theta(1/u).
\]
Here \(r(n)\) counts all integral Eisenstein ideals of norm \(n\), so \(r(n)\ge0\), \(r(1)=1\), and \(r(n)\le d(n)\). For **any fixed integer \(M\ge1\)** define the same reflected entire integrals and meromorphic partial completion as in that report:
\[
I_n(s)=\int_1^\infty e^{-anu}\bigl(u^{s-1}+u^{-s}\bigr)\,du,
\quad
\Lambda_M(s)=\frac1{6s(s-1)}+\sum_{n=1}^M r(n)I_n(s),
\]
\[
X_M(s):=s(s-1)\Lambda_M(s)
=\frac16+s(s-1)\sum_{n=1}^M r(n)I_n(s).
\tag{1}
\]
Thus \(X_M\) is entire, \(X_M(s)=X_M(1-s)\), and \(X_M(\bar s)=\overline{X_M(s)}\).

For the original fixed finite deleted ideal-prime set \(S\), the *exact previously defined* truncated denominator is
\[
Z_M^S(s)=D_S(s)\frac{a^s}{\Gamma(s)}\Lambda_M(s),
\quad
D_S(s)=\prod_{\mathfrak p\in S}(1-(N\mathfrak p)^{-s}).
\tag{2}
\]
No local factor or source activation is modified here.

## Theorem: bounded-strip asymptotic and escape of all fixed-cutoff zeros

For each \(M\ge1\), let
\[
d_n=(2an-1)e^{-an}>0,\qquad
c_M=\frac16-\sum_{n=1}^M r(n)d_n
=\sum_{n>M}r(n)d_n>0 .
\tag{3}
\]

**(A) Uniform strip asymptotic.** For every finite \(B\ge1\),
\[
\boxed{X_M(\sigma+it)=c_M+O_{B,M}(|t|^{-1}),
\qquad |\sigma|\le B,\quad |t|\to\infty.}
\tag{4}
\]
There is an explicit, finite and calculable threshold \(T_{B,M}\), described below, such that
\[
\boxed{|X_M(\sigma+it)|\ge c_M/2\quad
 (|\sigma|\le B,\ |t|\ge T_{B,M}).}
\tag{5}
\]
In particular each bounded vertical strip contains only finitely many zeros of \(X_M\).

**(B) Unbounded rightward spurious zeros.** For every real \(A\),
\[
\boxed{\#\{s:X_M(s)=0,\ \operatorname{Re}s>A\}=\infty,
\quad \sup_{X_M(s)=0}\operatorname{Re}s=+\infty.}
\tag{6}
\]
For each fixed \(A>1\), these are **genuine zeros of \(Z_M^S\)** by (2), while the actual \(\zeta_K^S(s)\) is nonzero throughout \(\operatorname{Re}s>1\) by its absolutely convergent Euler product. Thus no *fixed* truncated theta denominator is globally zero-free on any right half-plane, however far right that half-plane begins.

Part (B) asserts existence of zeros of the fixed approximant; it does not locate any specific one, bound their count by height, or imply that an individual prescribed vertical line contains a zero.

### Proof of (3) and the uniform asymptotic

Differentiating the exact theta reflection at \(u=1\) gives
\[
2\Theta'(1)+\Theta(1)=0,
\quad
\Theta'(1)=-6a\sum_{n\ge1}nr(n)e^{-an},
\]
hence the absolutely convergent identity
\[
\frac16=\sum_{n\ge1}r(n)(2an-1)e^{-an}.
\tag{7}
\]
Since \(a>1/2\), every summand on the right is nonnegative and \(r(n)>0\) at arbitrarily large n (in particular at every \(n=m^2\)), so the last expression in (3) is strictly positive for every finite M.

Let \(s=\sigma+it\), \(|\sigma|\le B\), and substitute \(u=e^x\) in \(I_n\). With
\[
A_{n,\sigma}(x)=e^{-an e^x+\sigma x},\qquad
B_{n,\sigma}(x)=e^{-an e^x+(1-\sigma)x},
\quad x\ge0,
\]
we have the **exact oscillatory identity**
\[
I_n(\sigma+it)=\int_0^\infty
[A_{n,\sigma}(x)e^{itx}+B_{n,\sigma}(x)e^{-itx}]\,dx.
\tag{8}
\]
All derivatives through order three are absolutely integrable and their L1 norms, as well as their boundary values, are uniformly bounded when \(|\sigma|\le B\). The bounds are completely elementary because \(e^{-an e^x}\) dominates every fixed exponential or polynomial in \(e^x\).

Integrate each term in (8) three times by parts. The order-\(t^{-1}\) boundary contributions cancel **exactly**, since
\(A_{n,\sigma}(0)=B_{n,\sigma}(0)=e^{-an}\). The next boundary coefficient is
\[
-\bigl(A'_{n,\sigma}(0)+B'_{n,\sigma}(0)\bigr)
=-(\sigma-an+1-\sigma-an)e^{-an}
=d_n,
\]
independent of \(\sigma\). Consequently
\[
\boxed{I_n(\sigma+it)=d_n/t^2+O_{B,n}(|t|^{-3}).}
\tag{9}
\]
The expansion also holds for negative t; its uniformity is the key additional observation missing from the earlier critical-line-only argument.

Since
\(s(s-1)=-t^2+it(2\sigma-1)+\sigma(\sigma-1)\),
substitution of (9) into (1), with fixed finite M, yields
\(X_M(\sigma+it)=1/6-\sum_{n\le M}r(n)d_n+O_{B,M}(|t|^{-1})\).
Equation (3) identifies this limit with \(c_M>0\), proving (4).

For an entirely explicit height threshold, define
\[
D_M=\sum_{n\le M}r(n)d_n,\qquad
J_{B,M}=\sum_{n\le M}r(n)\sup_{|\sigma|\le B}
 \Bigl(
 |A''_{n,\sigma}(0)|+|B''_{n,\sigma}(0)|
 +\|A'''_{n,\sigma}\|_{L^1(0,\infty)}
 +\|B'''_{n,\sigma}\|_{L^1(0,\infty)}
 \Bigr).
\tag{10}
\]
The finite sum and integrals in (10) are nonnegative finite real numbers, given by explicit exponentials and derivatives; no special-function or zero-finding oracle occurs. Three integrations by parts give
\[
\left|I_n(\sigma+it)-d_n/t^2\right|
\le
\frac{
|A''_{n,\sigma}(0)|+|B''_{n,\sigma}(0)|
+\|A'''_{n,\sigma}\|_1+\|B'''_{n,\sigma}\|_1
}{|t|^3}.
\tag{11}
\]
If \(|t|\ge\max(1,B+1)\), then \(|s(s-1)|\le4t^2\). Therefore
\[
|X_M(\sigma+it)-c_M|
\le \frac{C_{B,M}}{|t|},\quad
C_{B,M}:=[B(B+1)+2B+1]D_M+4J_{B,M}.
\tag{12}
\]
Thus any explicit
\[
\boxed{T_{B,M}:=\max\{1,B+1,2C_{B,M}/c_M\}}
\tag{13}
\]
works in (5). The threshold may be extremely large when M increases; no uniform-in-M assertion is made.

### Proof of the unbounded rightward zeros

For fixed finite M, each \(I_n\) is entire by uniform convergence on compact s sets, so \(X_M\) is entire and has the exact reflection \(X_M(s)=X_M(1-s)\). For \(|s|\le R\) and \(R\ge1\),
\[
|I_n(s)|\le2\int_1^\infty e^{-anu}u^Rdu
\le 2\,\Gamma(R+1)(an)^{-R-1}.
\]
Consequently \(\log\max_{|s|\le R}|X_M(s)|=O_M(R\log(R+2))\), so \(X_M\) has entire order at most one.

For real \(S>1\) every integral \(I_n(S)\) is positive. Since \(r(1)=1\), for \(S>a\)
\[
X_M(S)\ge S(S-1)I_1(S)
\ge S(S-1)e^{-S-a}(S/a)^{S-1},
\tag{14}
\]
where the second inequality restricts the positive first Mellin integral to \(u\in[S/a,S/a+1]\). Thus \(X_M(S)\) grows faster than every polynomial.

If \(X_M\) had only finitely many zeros in the whole plane, Hadamard factorization for an entire function of order at most one would yield \(X_M(s)=e^{\alpha s+\beta}P(s)\), with \(P\) a polynomial. Exact reflection would then require
\[
e^{\alpha(2s-1)}=P(1-s)/P(s).
\]
For real \(s\to+\infty\) the right side tends to \((-1)^{\deg P}\). This finite nonzero limit forces \(\alpha=0\), so \(X_M\) would be a polynomial, contradicting (14). Hence \(X_M\) has infinitely many zeros.

By (5) and isolated zeros, **each fixed bounded real-part strip contains only finitely many of these infinitely many zeros**. Thus the real parts of the zeros are unbounded in absolute value. Reflection sends each zero \(s\) to \(1-s\), so unboundedness in either direction forces zeros with real parts arbitrarily far to the right. This proves (6). On \(\operatorname{Re}s>1\), the factors \(D_S(s)\), \(a^s\), \(1/\Gamma(s)\) and \(1/[s(s-1)]\) are all finite and nonzero. Therefore (2) preserves every such rightward \(X_M\) zero, and the original Euler-product \(\zeta_K^S\) has no zeros there. □

## 3. A diagnostic at the smallest nontrivial cutoff

For \(M=1\), \(r(1)=1\), the exact strip limit is
\[
c_1=\frac16-(2a-1)e^{-a}>0.
\tag{15}
\]
A separate 60-decimal-digit mpmath diagnostic (not an interval certificate) gives
\(a\approx3.6275987284684357\) and
\(c_1\approx0.0004039343794162574\). Directly evaluating
\[
I_1(s)=a^{-s}\Gamma(s,a)+a^{s-1}\Gamma(1-s,a)
\tag{16}
\]
at \(t=100\), in the three vertical lines \(\sigma=-2,1/2,2\), gives \(X_1\) real parts near \(0.000400776,0.000400770,0.000400772\), approaching the **same** \(c_1\); for \(\sigma=1/2\), the imaginary part vanishes by symmetry. These numbers check the direction and normalization of (9), not the infinite-zero conclusion, which rests on the exact analytic proof.

## 4. Consequence for the complete RH program

The preceding finite-height enclosure legitimately uses \(M=O(R)\), \(T=O(\sqrt R)\) and **a separately proved** lower bound for \(Z_M^S\) on a certified safe-line height window. This new theorem explains why those safeguards are indispensable. At every fixed finite M, reflection symmetry fails to protect even the *classical Euler-product zero-free half-plane* from infinitely many artificial zeros extending arbitrarily far right. Hence a proof of an all-height inverse or global contour shift by **fixed-cutoff** reflection would contain a mathematical error.

The exact growing-cutoff finite-height enclosure is unaffected. The missing RH-bearing task is still a bound on the unchanged actual coherent principal/physical observation strong enough to exclude every hypothetical off-critical ζ zero, or equivalently a global sign theorem for the exact Weil form. No such bound is established here.

**Acceptance: rigorous strengthened fixed-cutoff failure theorem; NO NEW UNCONDITIONAL RH THEOREM PROVED.**
