# Odd logarithmic domain separation and the actual source at zero

Date: 2026-10-14. Inputs were read at repository snapshot
`02dd349f21d7c9cde4c8a3b0580ee55188223cf4`.

For every actual centered supercritical Green eigen-source, this note proves
that its ratio and complete reflected divergence belong to ordinary local
L2 at zero. The proof uses the odd restriction of the logarithmic Gamma
operator and a positive inverse-distance potential. It also supplies a
quantitative dependence on the supercritical parameter. It does not prove
an endpoint trace, a sign comparison, or exclusion of that eigen-source.

## 1. Objects and statement

Use the actual gradient completions and centered source of the
[source-tail report](REPORT.md):
\[
T^*T u=\lambda u,\quad \lambda>1,\quad
\delta=1-\lambda^{-1}\in(0,1),\quad g=\psi r,\quad
\int_0^\infty\psi(x)\sinh(x/2)r(x)\,dx=0.
\]
Write \(P=P[r]=\|u\|_P^2\), \(g_o\) for the odd extension, and
\[
d_n=\log n,\quad \alpha_n=\Lambda(n)n^{-1/2},\quad
L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x),\quad
V=L/\psi,\quad \mu^2=1/V.
\]
All prime powers are retained. The established source and reference bounds
give
\[
\int_0^\infty V|g|^2\le193P,\quad
\|g\|_{L^2(0,\infty)}^2\le3088P,\quad q_b[g_o]<\infty.
\tag{1}
\]
Here \(3088=193\cdot4^2\), using \(\mu\le4\) from
[THREE_HALVES_BOUND.md](../20261013_full_prime_green_reference/THREE_HALVES_BOUND.md).
The normalization is
\[
\kappa(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
q_b[f]=\frac12\iint_{\mathbb R^2}\kappa(|x-y|)|f(x)-f(y)|^2dxdy
=\int_{\mathbb R}b(t)|\widehat f(t)|^2\frac{dt}{2\pi}.
\]
Thus \(b(D)f=\int_{\mathbb R}\kappa(|x-y|)(f(x)-f(y))dy\)
on smooth functions, with \(b(t)\asymp\log(2+|t|)\) at infinity.
Let \(B_o\) be its restriction to odd functions, identified with
\(L^2(0,\infty)\) by restriction; its quadratic form is half the
full-line odd form. No additional factor two is included in \(B_o\).

**Theorem.** Fix \(0<\epsilon<\log2/4\) and an even smooth cutoff
\(0\le\chi\le1\), supported in \((-\epsilon,\epsilon)\) and equal
to one on \([-\epsilon/2,\epsilon/2]\). Set \(h=\chi g\) on the
positive half-line. There are constants depending only on the fixed
theta source and this cutoff, independent of \(\lambda,u\), such that
\[
\begin{split}
h&\in D(B_o),\qquad h/x\in L^2(0,\infty),\\
\|B_oh\|_2^2&\le C_1P,\\
\|r\|_{L^2(0,\epsilon/2)}^2+
\|W\|_{L^2(0,\epsilon/2)}^2&\le C_2\delta^{-2}P,
\end{split}\tag{2}
\]
where the actual complete divergence is
\[
W(x)=L(x)r(x)-\sum_{d_n>x}\alpha_n g(d_n-x).
\]
The constants in (2) are analytically specified below; no decimal
enclosure or threshold-uniform bound for \(r,W\) is claimed.

## 2. A domain separation theorem for the odd kinetic operator

For \(a>0\), let \(A_a\) be the positive closed form sum of \(B_o\)
and multiplication by \(a/x\). Then
\[
\boxed{D(A_a)=D(B_o)\cap\{h:h/x\in L^2(0,\infty)\},}
\tag{3}
\]
and on this domain
\[
\boxed{\|B_oh\|_2^2+a^2\|h/x\|_2^2
\le\|A_ah\|_2^2+304a\|h\|_2^2.}
\tag{4}
\]
This assertion concerns the odd operator and positive \(a\).

Put
\[
D(x,y)=\kappa(|x-y|)-\kappa(x+y)\ge0,\qquad
k(x)=2\int_0^\infty\kappa(x+y)dy.
\]
The odd operator is exactly
\[
B_of(x)=\int_0^\infty D(x,y)(f(x)-f(y))dy+k(x)f(x).
\tag{5}
\]
For \(w_\eta(x)=(x+\eta)^{-1}\), \(0<\eta\le1\), direct
symmetrization gives
\[
\begin{split}
\operatorname{Re}\langle B_oh,w_\eta h\rangle
={}&\frac14\iint D(x,y)(w_\eta(x)+w_\eta(y))|h(x)-h(y)|^2dxdy\\
&+\frac12\int(B_ow_\eta+k w_\eta)|h|^2dx.
\end{split}\tag{6}
\]
First take \(h\) smooth compact odd on the full line. The expression
\(B_ow_\eta\) uses the odd extension of \(w_\eta\), whereas the
multiplier acting on \(h_o\) is the even function \(w_\eta(|x|)\).
These two uses must be distinguished.

Let \(F(t)=t\kappa(t)\). Combining the terms before integration yields
\[
\begin{split}
\frac{B_ow_\eta(x)}{w_\eta(x)}={}&
\int_0^x\frac{F(x+y)-F(x-y)+2\eta\kappa(x+y)}{y+\eta}dy\\
&+\int_x^\infty\frac{F(y-x)+F(x+y)+2\eta\kappa(x+y)}{y+\eta}dy.
\end{split}\tag{7}
\]
The second integral is positive. Moreover
\[
F'(t)=\kappa(t)\left(1-\frac t2-\frac{2t}{e^{2t}-1}\right)\ge0
\quad(0<t\le1).
\]
Indeed \((e^{2t}-1)(2-t)\ge(2t+2t^2)(2-t)\ge4t\) there.
Consequently \(B_ow_\eta\ge0\) for \(0<x\le1/2\).

For \(x\ge1/2\), write \(f_-=(-F')_+\). It vanishes on \((0,1]\),
and \(f_-(t)\le2t e^{-t/2}\) for \(t\ge1\). To check the latter,
use \(e^2>4\), so \((1-e^{-2t})^{-1}\le4/3\) and
\(2/(e^{2t}-1)\le2/3\). Dropping the negative \(-1\) term in
\(-F'\) gives the coefficient \((1/2+2/3)(4/3)=14/9<2\).
The negative part of the first integral in (7) is at most
\[
I(x,\eta)=\int_0^{2x}f_-(t)
\log\frac{x+\eta}{|t-x|+\eta}\,dt.
\tag{8}
\]
This follows by Tonelli applied to
\(F(x+y)-F(x-y)=\int_{x-y}^{x+y}F'(t)dt\).
Outside \([x/2,3x/2]\) the logarithm is at most \(\log2<1\);
this part is less than \(\int_0^\infty2t e^{-t/2}dt=8\).
Inside that interval, \(f_-(t)\le3x e^{-x/4}\), and
\[
\int_{x/2}^{3x/2}\log\frac{x+\eta}{|t-x|+\eta}dt
\le x(1+\log6)<3x.
\]
Here \(x+\eta\le3x\), the integrable singularity is bounded by
\(\log(3x/|t-x|)\), and \(e>5/2\) implies \(\log6<2\). Since
\(\sup_{x>0}x^2e^{-x/4}=64/e^2<16\), (8) is less than \(152\).
Finally \(w_\eta\le2\) for \(x\ge1/2\), proving globally
\[
B_ow_\eta\ge-304.
\tag{9}
\]
Equations (6) and (9) give
\(\operatorname{Re}\langle B_oh,w_\eta h\rangle\ge-152\|h\|_2^2\).

For fixed \(\eta\), first interpret the left side as the closed form
pairing \(\operatorname{Re}\mathfrak b_o(h,w_\eta h)\). The even
extension of \(w_\eta\) is a bounded Lipschitz multiplier on the
logarithmic form domain: the product-difference estimate pays its extra
term by \(C_\eta\|h\|_2^2\int\kappa(|t|)\min(t^2,1)dt\).
Smooth Fourier cutoffs approximate an odd vector in its weighted
Fourier form norm. The resulting smooth vector can then be spatially
cut off: the error is the removed original jump energy plus
\(CR^{-2}\|h\|_2^2\int t^2\kappa(|t|)dt\), tending to zero.
Thus smooth compact odd functions form a form core. Form continuity
extends the inequality to the
whole form domain. For \(h\in D(B_o)\), the representation theorem
identifies this pairing with \(\operatorname{Re}\langle B_oh,w_\eta h\rangle\).
This passage requires no assertion about an operator core for a singular
potential. Expanding the square gives
\[
\|B_oh\|_2^2+a^2\|w_\eta h\|_2^2
\le\|(B_o+aw_\eta)h\|_2^2+304a\|h\|_2^2.
\tag{10}
\]

The nonnegative forms of \(A_{a,\eta}=B_o+aw_\eta\) increase to the
form defining \(A_a\). For \(h\in D(A_a)\), put
\(h_\eta=(A_{a,\eta}+1)^{-1}(A_a+1)h\).
Monotone convergence of closed forms gives \(h_\eta\to h\) in L2 and
\(A_{a,\eta}h_\eta\to A_ah\) in L2. Equation (10) uniformly bounds
\(B_oh_\eta\) and \(w_\eta h_\eta\). Weak graph closure of the
selfadjoint \(B_o\) identifies their first weak limit with \(B_oh\).
On compact intervals away from zero, uniform convergence of \(w_\eta\)
identifies the second with \(h/x\). Weak lower semicontinuity proves
(4) and the forward inclusion in (3). Conversely, the intersection in
(3) lies in the sum's form domain by Cauchy--Schwarz, and its form
functional is represented by \(B_oh+ah/x\in L^2\). This proves (3).

## 3. The complete translated forcing is locally L2

On \((0,\epsilon)\) every label is outgoing. Define
\[
F_\pm(x)=\sum_{n\ge2}\alpha_n g(d_n\pm x),\quad
S_\pm(x)=\sum_{n\ge2}\alpha_n\psi(d_n\pm x),\quad
s_\pm=\sup_{0\le x\le\epsilon}S_\pm(x)<\infty.
\]
Weighted Cauchy gives
\[
|F_\pm(x)|^2\le S_\pm(x)
\sum_n\alpha_n\psi(d_n\pm x)|r(d_n\pm x)|^2.
\]
After integration and change of variable \(y=d_n\pm x\), the
label multiplicity is bounded by
\[
\sum_{|d_n-y|\le\epsilon}\alpha_n
\le3e^{3\epsilon/2}e^{y/2}.
\]
This is the complete Chebyshev bound \(\sum_{n\le X}\Lambda(n)\le3X\).
The unconditional PNT row theorem, [equation (7)](../20261013_reflected_markov_essential_edges/REPORT.md),
and positivity and continuity on compact sets give
\[
c_L:=\inf_{y\ge0}e^{-y/2}L(y)>0.
\]
Consequently
\[
\|F_+\|_2^2+\|F_-\|_2^2\le C_FP,\qquad
C_F=\frac{579e^{3\epsilon/2}}{c_L}(s_++s_-).
\tag{11}
\]
All norms in (11) are over \((0,\epsilon)\). The same argument for
omitted labels, whose theta row sums tend uniformly to zero, proves L2
convergence of the full series. No translated point values are assumed.

## 4. Actual weak equation, localization and the singular form core

Dividing the positive-wing weak identity in
[SIGNED_ZERO_PAIRING.md, (4)--(5)](SIGNED_ZERO_PAIRING.md) by its common
factor two gives, on \((0,\epsilon)\),
\[
B_og+\delta Vg=C_0g+F_+-(1-\delta)F_-.
\tag{12}
\]
The coefficient is \(\delta\). The auxiliary weighted equation has
eigenvalue \(-2\delta\), but its kinetic form is the full-line odd form
on a positive-wing inner product. The same-wing shift on this interval
is \(F_+\); the negative-argument odd shift contributes \(-F_-\).
The reflected variation contributes \(\delta(Vg-F_-)\).
The centered pole term vanishes.

For \(x<\log2\), the complete series for \(L\) and all fixed
derivatives converge normally. Therefore
\[
V(x)=c/x+U(x),\quad c=L(0)/c_\psi>0,\quad
U_0:=\sup_{0<x<\epsilon}|U(x)|<\infty,
\tag{13}
\]
using \(\psi(x)=c_\psi x+O(x^3)\). Put \(a=\delta c\).
The localized \(h=\chi g\) belongs to the positive form domain of
\(A_a\), by (1) and the bounded Lipschitz multiplier estimate. On tests
away from zero, (12) gives
\[
A_a h=\chi\{(C_0-\delta U)g+F_+-(1-\delta)F_-\}
       +[B_o,\chi]g=:J.
\tag{14}
\]
In this identity the cutoff makes the local forcing into a function on
the half-line. The commutator is bounded on L2, with
\[
C_\chi=\int_{\mathbb R}\kappa(|t|)
\min\{\|\chi'\|_\infty|t|,2\|\chi\|_\infty\}\,dt<\infty.
\]
By (1) and (11),
\[
\|J\|_2\le M\sqrt P,\quad
M=\sqrt{3088}(|C_0|+U_0+C_\chi)+\sqrt{2C_F}.
\tag{15}
\]

To infer the operator statement in (14), a form core at zero is needed.
Here is its proof. Work with odd full-line functions and the equivalent
form norm \(\|f\|_2^2+q_b[f]+\int|f|^2/|x|\). Radial amplitude
clipping preserves oddness and converges in this norm: the residual
contraction converges pointwise to zero and its jump differences are
dominated by a constant times those of \(f\). Smooth even spatial
cutoffs next reduce to a bounded compact function \(f\). Their energy
error is the removed original jump energy plus at most
\(CR^{-2}\|f\|_2^2\int t^2\kappa(|t|)dt\).

Let \(\theta_\eta\) be even smooth, zero on \(|x|\le\eta\) and
one on \(|x|\ge2\eta\). For bounded compact \(f\), put
\(e_\eta=(1-\theta_\eta)f\) and
\(\Gamma_f(x)=\frac12\int\kappa(|x-y|)|f(x)-f(y)|^2dy\).
The full product-difference estimate is
\[
q_b[e_\eta]\le2\int_{|x|\le2\eta}\Gamma_f(x)dx
 +C\|f\|_\infty^2\eta(1+\log(1/\eta))\longrightarrow0.
\tag{16}
\]
Only the second term uses the cutoff scaling bound; the first tends to
zero by absolute continuity of the original finite jump energy. The
potential error tends to zero by integrability of \(|f|^2/|x|\).
Finally convolve with an **even** smooth mollifier of support smaller
than half the gap at zero. Fourier dominated convergence gives kinetic
form convergence, and the potential is bounded on the common compact
support. Thus smooth compact odd functions vanishing near zero form a
core. Equation (14), already valid on this core and with \(J\in L^2\),
extends by continuity to the whole form domain. This proves
\(h\in D(A_a)\) and (14) as an operator identity.

## 5. Quantitative consequence and remaining boundary

Apply (4), (15), and \(\|h\|_2^2\le3088P\):
\[
\|B_oh\|_2^2+a^2\|h/x\|_2^2\le QP,\qquad
Q=M^2+304c\cdot3088.
\tag{17}
\]
Let \(c_*:=\inf_{0<x\le\epsilon/2}\psi(x)/x>0\) and
\(L_*:=\sup_{0\le x\le\epsilon/2}L(x)\). Since \(\chi=1\)
there, (17) implies
\[
\|r\|_{L^2(0,\epsilon/2)}^2
\le\frac{Q}{c^2c_*^2}\delta^{-2}P=:C_r\delta^{-2}P.
\]
On the same interval \(W=Lr-F_-\), so
\[
\|W\|_{L^2(0,\epsilon/2)}^2
\le(2L_*^2C_r+2C_F)\delta^{-2}P.
\tag{18}
\]
Thus one can take \(C_1=Q\) and
\(C_2=(1+2L_*^2)C_r+2C_F\) in (2).
The localized logarithmic operator norm is bounded
independently of \(\delta\), while the ratio and divergence estimates
lose \(\delta^{-2}\) in squared norm.

The existing endpoint estimate was only \(\int_0^1x|W(x)|^2dx<\infty\).
Ordinary local L2 now permits a canonical one-sided function extension
of the actual \(W\), without an origin finite-part subtraction. The
exponential tail and the signed residue identities remain separate inputs.

No trace of \(r\) follows from (17). For example, disjoint smooth bumps
of fixed height in \(r\) on geometrically shrinking annuli give no
limit at zero, while \((\psi r)_o\) is compact Lipschitz and both
\(B_o(\psi r)\) and \(\psi r/x\) belong to L2. This is a domain
counterexample, not an eigen-source. A trace theorem must still use more
of the actual equation. None of (2)--(18) supplies the missing complete
critical inequality \(K\le I\).
