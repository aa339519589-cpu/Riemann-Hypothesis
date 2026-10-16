# Finite-height sub-Weyl bounds from an unsplit A-process

Status: complete proof and directed arithmetic have passed independent internal review and replay.
This report makes no new zero-free-region or zero-proportion claim.

## 1. Result

For each row below, throughout the **closed** interval `u <= log t <= u+5`,

\[
 |\zeta(1/2+it)|\le A_u t^{27/164}.
\]

|u|A_u|u|A_u|u|A_u|u|A_u|
|---:|---:|---:|---:|---:|---:|---:|---:|
|60|29.83|100|36.16|140|40.54|180|43.97|
|65|30.90|105|36.75|145|41.03|185|44.35|
|70|31.81|110|37.35|150|41.48|190|44.73|
|75|32.60|115|37.91|155|41.89|195|45.14|
|80|33.42|120|38.52|160|42.39|200|45.51|
|85|34.08|125|39.02|165|42.79|205|45.83|
|90|34.88|130|39.56|170|43.16|210|46.17|
|95|35.57|135|40.06|175|43.56|215|46.49|

The proof keeps the complete square root in the last A-process, instead of
splitting its positive summands into separate square roots. It also retains
the logarithmic Poisson error, and includes an explicit unit debit for
nonintegral endpoints in the transformed sum. All floor errors are enclosed
directly. The parameters in `parameters.txt` are rational choices, not assumed
solutions of an optimization problem.

For comparison, the journal Table 1 of Patel–Yang gives 36.88 on [60,65],
43.98 on [100,105], and larger bounds in the later listed ranges. This report
uses the journal's corrected source, not the inconsistent q0 substitutions in
the earlier preprint. We do not assert a complete priority comparison with
all literature. Outside [exp(60),exp(220)] no assertion improves the existing
global 66.7 t^(27/164) theorem here.

## 2. Explicit derivative constants

We use Yang's explicit derivative tests [Y, Lemmas 2.4–2.5], also reproduced
as the explicit kth-derivative test in [PY, Section 1.2]. For eta>0 and H>1 put
\[
 l=(\eta^{-1}+32\sqrt\eta H/(15\sqrt\pi))^{-1},\quad
 d_3=\sqrt{\tfrac12+\tfrac12\sqrt{1+3\sqrt\pi\eta^{3/2}/8}},
\]
\[
 A_3=d_3\sqrt{(\eta H)^{-1}+\frac{32}{15\sqrt\pi}\sqrt{\eta+l}
                         +(\eta+l)l/3},\qquad
 B_3=\frac{\sqrt{32}\,d_3}{\sqrt3\pi^{1/4}\eta^{1/4}}.
\]
For j>=3 and J=2^(j-1), define (with a different symbol from d_3)
\[
 \Delta_j=\sqrt{1+2\,2337^{-1+2/J}(9\pi\eta/1024)^{1/J}},
\]
\[
 A_{j+1}=\Delta_j\left(H^{-1/J}+
 \frac{2^{19/12}(J-1)\sqrt{A_j}}{\sqrt{(2J-1)(4J-3)}}\right),
\quad
 B_{j+1}=\Delta_j\frac{2^{3/2}(J-1)\sqrt{B_j}}
 {\sqrt{(2J-3)(4J-5)}}.
\]
For integer a,N, monotonic f^(k), and
lambda<=|f^(k)|<=H lambda, the resulting bound is
\[
 |S_f(a,N)|\le A_k H^{2/2^{k-1}}N\lambda^{1/(2^k-2)}
             +B_kN^{1-2/2^{k-1}}\lambda^{-1/(2^k-2)}.       \tag{1}
\]
Every use below is on an integer-endpoint interval within the stated derivative
range. A partial sum with at most one term is handled trivially.

## 3. A raw block lemma with the whole square root

Let a,b be positive integers, a<b<=ha, 1<h<=2, and 1<=q<=a an integer.
Write f(x)=-t log(x)/(2pi), and define
\[
 H_5=\frac{76545\sqrt2}{107264}h^9,\quad
 b_1=\pi^{-1}(53632\sqrt2\pi^4/729)^{1/30}
                  (76545\sqrt2/107264)^{1/8},
\]
\[
 b_2=\pi^{-7/8}(729/(53632\sqrt2\pi^4))^{1/30},
\quad c_3=b_1\sqrt\pi A_5(\eta_1,H_5)h^{21/8}(h-1),
\quad c_4=b_2\sqrt\pi B_5(\eta_1)h^{3/2}(h-1)^{7/8},
\]
\[
 E_4=5.686\sqrt\pi h^{3/2},\quad E_5=6h^3(h-1)/\pi,
\quad E_6(a,q,t)=6+\frac5\pi\log\left(2+\frac{(h-1)tq}{\pi a^2}\right).
\]
Then
\[
\begin{split}
 |S_f(a,b-a)|^2\le (h-1+q/a)\bigg[&\frac{(h-1)a^2}{q}
 +\frac{1800}{2911}c_3a^{4/5}(qt)^{11/30}
 +\frac{28800}{54481}c_4a^{9/20}(qt)^{61/120}\\
 &+\frac83 E_4a^{5/2}(qt)^{-1/2}
 +\frac9{14}E_5a^{2/3}(qt)^{1/3}+aE_6(a,q,t)\bigg].       \tag{2}
\end{split}
\]

Here is the source-level derivation, including the endpoint debit. For 1<=r<N=b-a,
set g_r(x)=f(x+r)-f(x), alpha=g_r'(b-r), beta=g_r'(a), and
phi_r(nu)=g_r(x_nu)-nu*x_nu, where g_r'(x_nu)=nu. Direct differentiation as
in [PY, Section 3.0.1] gives
\[
 \lambda_5=\frac{53632\sqrt2\pi^4}{729}\frac{a^9}{t^4r^4}
 \le |\phi_r^{(5)}|\le H_5\lambda_5,
 \qquad \beta-\alpha\le(h-1)tr/(\pi a^2).
\]
The fifth derivative has constant sign and monotonic magnitude. Indeed, its
variable factor is nu^(-9/2) P(x)/(x+2)^(7/2), x=pi*r*nu/t,
P(x)=8x^3+36x^2+60x+35; the derivative numerator of the latter ratio is
-4x^3-6x^2-6x-5/2<0. Also 0<x<=1/4 because r<=a.

For a partial dual sum alpha<n<=L<=beta, remove its first lattice point,
if any. Its cost is at most 1. The remaining interval has integer endpoints,
lies inside [alpha,beta], and has length at most beta-alpha. Applying (1)
there gives the two standard main terms in [PY, (3.13)], **plus 1**. Partial
summation against |g_r''(x_nu)|^(-1/2), whose maximum is at most
sqrt(pi)h^(3/2)a^(3/2)/(tr)^(1/2), therefore gives
\[
 \left|\sum_{\alpha<\nu\le\beta}
 \frac{e(\phi_r(\nu))}{|g_r''(x_\nu)|^{1/2}}\right|
 \le c_3a^{-1/5}(tr)^{11/30}+c_4a^{-11/20}(tr)^{61/120}
       +\sqrt\pi h^{3/2}a^{3/2}(tr)^{-1/2}.
\]
Apply [PY, Lemma 2.3], retaining its complete Poisson error. Its 4.686 term
plus this endpoint debit gives E_4 above. Its cubic-derivative term is
E_5(tr)^(1/3)a^(-1/3). Its logarithmic term is bounded by E_6 using r<=q.
Thus the original correlation sum is bounded by all five positive rows before
any square-root splitting. Empty correlations for r>=N are zero and satisfy
the same positive upper bound.

Finally apply the integer A-process [PY, Lemma 1.2] and
\[
 \sum_{r=1}^{q-1}(1-r/q)r^s\le
 \frac{q^{1+s}}{(1+s)(2+s)}\quad(-1<s\le1).
\]
The weights of the constant/logarithmic row sum to at most 1. Substituting
s=11/30,61/120,-1/2,1/3 gives exactly (2). The same bound applies to every
initial partial interval (a,L] with L<=b, using the same a,h,q. Hence partial
summation bounds the weighted block by a^(-1/2) times the square root of (2).

## 4. Partition and floor guards

Fix one closed log interval [l,u] with u=l+5 and its seven rational parameters
(h1,h2,eta1,eta2,theta1,theta2,theta3). For x=log t define
\[
 K(x)=\left\lceil\frac{3x/34-\log(\theta_2\sqrt{2\pi})}{\log h_1}\right\rceil,
 \quad a_k=\lfloor h_1^{-k}\sqrt{t/(2\pi)}\rfloor,
\]
\[
 R(x)=\left\lceil\frac{115x/1394-\log(\theta_3/\theta_2)}{\log h_2}\right\rceil,
 \quad a'_r=\lfloor h_2^{-r}\theta_2t^{7/17}\rfloor.
\]
We have a_K<=a'_0 and a'_R<=theta3*t^(27/82). The checker also certifies
\[
 (\theta_2/h_1)e^{115l/1394}-e^{-27l/82}>\theta_3,
\]
which implies a_K>=a'_R throughout the interval. Divide the Riemann–Siegel sum
at a'_R and a_K. For its middle part, the geometric a'_r blocks cover it;
the top block can be truncated and uses the same initial-partial-sum bound.
No inequality between the magnitude of a prefix and the magnitude of a longer
oscillatory sum is assumed.

Put K*=K(u), R*=R(u),
\[
 h=\frac{h_1}{1-(h_1/\theta_2)e^{-7l/17}},\qquad
 h_3=\frac{h_2}{1-(h_2/\theta_3)e^{-27l/82}}.
\]
The checker verifies 1<h,h3<2. These bound all consecutive integer-block
ratios, since an unfloored final endpoint exceeds theta2*t^(7/17)/h1,
respectively theta3*t^(27/82)/h2.

For each 1<=k<=K* define
\[
 A_k^+=h_1^{-k}/\sqrt{2\pi},\quad A_k^-=A_k^+-e^{-l/2},
 \quad Q_k^+=\theta_1(A_k^+)^{36/41},
 \quad Q_k^-=\theta_1(A_k^-)^{36/41}-e^{-7l/41}.
\]
For the actual block choose q=floor(theta1*a_k^(36/41)*t^(-11/41)). Then
\[
 A_k^-\le a_k/t^{1/2}\le A_k^+,\qquad
 Q_k^-\le q/t^{7/41}\le Q_k^+.
\]
The checker verifies A_k^->0,Q_k^->0 and
(Q_k^+/A_k^-)e^(-27l/82)<1, for **every** k<=K*.
These imply the required integer conditions 1<=q<=a_k.
Extra terms k>K(x) are included only as positive upper bounds.

## 5. Uniform normalized block sum

For each k suppress the subscript and set
\[
\begin{split}
 T_k={}&(h-1)A^+/Q^-+
 \frac{1800}{2911}c_3(A^-)^{-1/5}(Q^+)^{11/30}\\
 &+\frac{28800}{54481}c_4(A^-)^{-11/20}(Q^+)^{61/120}e^{-3l/328}\\
 &+\frac83E_4(A^+)^{3/2}(Q^-)^{-1/2}e^{-27l/164}
 +\frac9{14}E_5(A^-)^{-1/3}(Q^+)^{1/3}e^{-13l/123}\\
 &+\left[6+\frac5\pi\log\left(2+
 \frac{(h-1)Q^+}{\pi(A^-)^2}e^{7l/41}\right)\right]e^{-27l/82},
\end{split}
\]
\[
 U_3=\sum_{k=1}^{K^*}
 \sqrt{\bigl(h-1+(Q_k^+/A_k^-)e^{-27l/82}\bigr)T_k}.
\]
Equation (2), divided by a*t^(27/82), proves |S3|/t^(27/164)<=U3.
All power replacements are directed as displayed. In particular the final
logarithmic row is decreasing as a function of x after its A,Q enclosures
are fixed: its derivative has sign at most
(5/pi)(7/41)-(27/82)*6<0. Thus its evaluation at l is uniform, rather than
a pointwise-height substitution.

For the middle block let
\[
 D_1=(3/\pi)^{1/14}A_4(\eta_2,h_3^4)h_3^{5/7}(h_3-1),
 \quad D_2=(\pi/3)^{1/14}B_4(\eta_2)h_3^{2/7}(h_3-1)^{3/4}.
\]
The fourth-derivative test (1) and geometric summation give
\[
 U_2=D_1\theta_2^{3/14}\frac{1-h_2^{-3R^*/14}}{h_2^{3/14}-1}
                 e^{(19/119-27/164)l}
 +D_2\theta_2^{15/28}\frac{1-h_2^{-15R^*/28}}{h_2^{15/28}-1}
                 e^{(71/476-27/164)l}.
\]
Both exponents are negative. The initial trivial sum is bounded by
\[
 U_1=2\sqrt{\theta_3+\tfrac12e^{-27l/82}}.
\]
This follows by integrating n^(-1/2) over its unit centered cells; the
favorable -sqrt(2) term is simply discarded. Finally [PY, Lemma 3.1] gives
\[
 |\zeta(1/2+it)|/t^{27/164}\le
 2(U_1+U_2+U_3)+1.48e^{(-1/4-27/164)l}
                    +.127e^{(-3/4-27/164)l}.                \tag{3}
\]
The directed calculation encloses (3) below each announced A_u.

## 6. Reproduction and scope

Run `python certify_unsplit_py.py` with python-flint 0.9.0 / FLINT 3.6.0.
All parameters are parsed as exact rational numbers; every transcendental
operation uses 192-bit Arb balls. The integer upper counts K*,R* are checked
against their defining real expressions. Every individual floor/q guard is
checked, not sampled. `unsplit_py_bounds.json` contains the full parameters,
component balls, counts, final bounds and hashes for all 32 closed intervals.
The result is a finite-height critical-line estimate. Feeding it into a
zero-free-region argument is a separate task and is not asserted here.

## References

[PY] D. Patel and A. Yang, *An explicit sub-Weyl bound for zeta(1/2+it)*,
Journal of Number Theory 262 (2024), 301–334,
https://doi.org/10.1016/j.jnt.2024.03.011 . A readable earlier version is
https://arxiv.org/html/2302.13444v1 . We use the raw block derivation, not its
later q0 substitutions, and explicitly pay the dual endpoint debit above.

[Y] A. Yang, *Explicit bounds on zeta(s) in the critical strip and a zero-free
region*, J. Math. Anal. Appl. 534(2) (2024), 128124,
https://doi.org/10.1016/j.jmaa.2024.128124 ; version-pinned text:
https://arxiv.org/html/2301.03165v2 .
