# An explicit extra-dual-B bound with exponent 77/468

Status: complete proof and directed constant certificate, with completed independent internal review and reproducible replay.

## 1. Statement and scope

The theorem is
\[
 |\zeta(1/2+it)|\le90|t|^{77/468},\qquad |t|\ge3.       \tag{1}
\]
The exponent improves on 27/164 by exactly 1/9594. The coefficient is larger
than that of [the established global 49 bound](../20261016_nested_dual_subweyl_49/REPORT.md),
so the useful combined bound retains the minimum of these two expressions.
No claim about a proportion of zeros, the Riemann hypothesis, or exhaustive
literature priority is made. The formal exponent word alone is not used as a
theorem: all local processes and their errors are given below.

We use the published explicit fourth-derivative test and complete Poisson
formula in Patel–Yang, Sections1.2 and2, with the integer-endpoint repair
proved in [the finite unsplit-PY theorem](../20261016_unsplit_py_subweyl_table/REPORT.md).
The numerical functions A4(eta,H),B4(eta) are exactly the published recurrence,
reproduced in the certificate. In particular the fourth-derivative estimate is
\[
 |S_f|\le A_4H^{1/4}n\lambda^{1/14}
                     +B_4n^{3/4}\lambda^{-1/14},          \tag{2}
\]
for an integer-endpoint interval of length n, with monotone fourth derivative
of constant sign and lambda<=|f''''|<=H lambda. The full Poisson error is
\[
 4.686\lambda_2^{-1/2}+\frac5\pi\log(M+2)
 +\frac{2\,3^{2/3}}{\pi^{2/3}}H_2H_3^{1/3}L\lambda_3^{1/3}+6. \tag{3}
\]
Here L is the original interval length, M the dual interval length, and
lambda_j<=|f^(j)|<=H_j lambda_j for j=2,3. When (2) is applied to the dual
sum, its first integer is removed before using the test on every remaining
partial sum. This costs at most lambda_2^(-1/2), so 4.686 is replaced by5.686.
All uses of the Poisson formula below retain this repair and all terms of(3).

Only t>=exp(5800) requires the new argument. On 3<=t<=exp(5800), the already
established coefficient49 gives
\[
 |\zeta(1/2+it)|/t^{77/468}\le49e^{5800/9594}<89.691<90. \tag{4}
\]
Conjugation handles negative t.

## 2. Exact derivative control of the first dual phase

For an original logarithmic block a<n<=b<=ha and an integer1<=r<a, put
\[
 g_r(x)=-\frac{t}{2\pi}\log(1+r/x),\quad
 C=\sqrt{tr/(2\pi)},\quad \epsilon=\pi r/(2t).
\]
The first dual phase phi(nu)=g_r(x_nu)-nu*x_nu, where g_r'(x_nu)=nu, satisfies
\[
 \phi'(\nu)=r/2-C\sqrt{1/\nu+\epsilon}.                 \tag{5}
\]
Only nonempty correlations are used: x ranges over [a,b-r], so both x and
x+r remain in the original block [a,b]. In particular its lower dual endpoint
is tr/[2pi*b*(b-r)]>=tr/(2pi*h^2*a^2), while the upper endpoint is
tr/[2pi*a*(a+r)]<=tr/(2pi*a^2). Thus the complete dual interval is contained in
[N,h^2 N], where
\[
 N=tr/(2\pi h^2a^2).                                    \tag{6}
\]
For F(nu)=sqrt(1/nu+epsilon), the exact Stieltjes representation is
\[
 F(\nu)=\sqrt\epsilon+\frac1\pi\int_0^{1/\epsilon}
                  \frac{\sqrt{1/s-\epsilon}}{\nu+s}\,ds.
\]
For example, substitute s=sin(theta)^2/epsilon and evaluate the elementary
integral. Differentiation on compact positive nu intervals is absolute. For
n>=1 comparison with epsilon=0 gives
\[
 1-\frac{\epsilon\nu}{2n-1}\le
 \frac{(-1)^nF^{(n)}(\nu)}{(1/2)_n\nu^{-n-1/2}}\le1.     \tag{7}
\]
Indeed the density loss is at most epsilon*s both below1/epsilon and in the
removed tail above it. The ratio of the resulting beta integrals is exactly
B(3/2,n-1/2)/B(1/2,n+1/2)=1/(2n-1).

Consider f=-Delta_i Delta_j Delta_k phi and D=(3/4)Cijk. If the total shift
is at most .001N and epsilon times every shifted argument is at most .001,
then, for v in its whole real phase interval and m=2,3,4,5,
\[
 qD c_m v^{-5/2-m}\le(-1)^m f^{(m)}(v)
                 \le D c_m v^{-5/2-m},\quad
 q=99/100,\quad c_m=(5/2)_m.                              \tag{8}
\]
This follows by writing the differences as three integrals of phi^(m+3).
The lower relative factor is at least
(1001/1000)^(-5/2-m)(1-1/[1000(2m+3)]), which is greater thanq for each listedm.
All four finite inequalities are checked with directed arithmetic.

## 3. The second dual and its complete error

Write H=h^2. For the Legendre dual Psi(y)=f(v)-yv with y=f'(v),
\[
 \Psi^{(4)}=\frac{f^{(4)}f''-3(f''')^2}{(f'')^5},\qquad
 \Psi^{(5)}=\frac{f^{(5)}(f'')^2-10f'''f^{(4)}f''+15(f''')^3}{(f'')^7}.
\]
For the second Poisson application use -f, whose derivative is decreasing,
as required by the printed source lemma. Its dual phase is -Psi(-nu).
Conjugation preserves all absolute bounds; that dual has positive fourth
derivative and negative fifth derivative once the signs below are proved.
Its positive weight is decreasing in its increasing dual coordinate, since
f'' is decreasing in the original coordinate. Thus Abel partial summation
uses the maximum weight once, not twice, and retains the source half-open
endpoint convention. The first Poisson weight is decreasing in its dual
coordinate for the same reason.

The bounds(8) imply strict negativity of both numerators. The exact upper
coefficients, after removing positive common scales, are
\[
 c_4c_2-3q^2c_3^2=-68190507/25600<0,
\]
\[
 -q^3c_5c_2^2+10c_3c_4c_2-15q^3c_3^3
                         =-505752535827/2048000<0.
\]
Thus Psi^(4) has constant sign and is monotone on every required dual
interval. Define the positive constants
\[
 m=3q^2c_3^2-c_4c_2,\quad M=3c_3^2-q^2c_4c_2,
 \quad l=m/c_2^5,\quad H_4=(M/m)q^{-5}H^{23/2},
\]
\[
 d_M=(H-1)c_2,\qquad W=q^{-1/2}c_2^{-1/2}H^{9/4}.
\]
Then the second dual interval length is at most d_M D N^(-7/2), its fourth
derivative has scale l D^(-3)N^(23/2) and ratio H4, and the partial-summation
weight is at most W D^(-1/2)N^(9/4). Hence(2), after the first-integer repair,
and(3) give the following bound for every triple correlation:
\[
 |S_f|\le T_1D^{2/7}N^{-3/7}+T_2D^{13/28}N^{-67/56}
       +T_3D^{-1/2}N^{9/4}+T_4D^{1/3}N^{-5/6}
       +6+(5/\pi)\log(2+d_MDN^{-7/2}),                  \tag{9}
\]
where
\[
 T_1=WA_4H_4^{1/4}d_Ml^{1/14},\quad
 T_2=WB_4d_M^{3/4}l^{-1/14},\quad T_3=5.686W,
\]
\[
 T_4=\frac{2\,3^{2/3}}{\pi^{2/3}}
       (H^{9/2}/q)(H^{11/2}/q)^{1/3}(H-1)
                         (qc_3H^{-11/2})^{1/3}.
\]
Here A4,B4 use eta=6/5 and ratioH4. In(3) we used the explicit valid lower
scales qc2 D(HN)^(-9/2), qc3 D(HN)^(-11/2) and corresponding ratios
H^(9/2)/q,H^(11/2)/q. No inverse-phase sign is assumed from a formal exponent
pair; it was proved above. Dual endpoints may be negative, which does not
change the integer-endpoint derivative test.

## 4. Three explicit A-processes

For any positive integerQ, zero extension and Cauchy give
\[
 |S|^2\le(n+Q-1)\left[n/Q+\frac2Q\sum_{j=1}^{Q-1}(1-j/Q)|S_j|\right]. \tag{10}
\]
No Q<=n premise is needed; correlations with j>=n vanish. For -1<s<=1 the
published weighted-power inequality gives
\[
 \frac2Q\sum_{j=1}^{Q-1}(1-j/Q)j^s\le b_sQ^s,
 \qquad b_s=2/[(1+s)(2+s)].                              \tag{11}
\]
Set kappa=(N^5/C)^(1/21). On the good range kappa>=2, choose the integer
K=floor(kappa), and use lengths K,K^2,K^4 in successive applications of(10).
Since kappa/2<=K<=kappa, their sum is at most(11/8)kappa^4. If
\[
 NC^4\ge1375^{21},                                      \tag{12}
\]
this sum is at most .001N. Every nonempty correlation stays inside the
original first-dual interval. Thus(8) applies without extension of its phase.

Put ell=H-1 and J=ell+.001. All lengths are at most ell*N and all factors
n+Q-1 are at most JN. Iterating(10), using Jensen for its subprobability
weighted averages and sqrt(u+v)<=sqrt(u)+sqrt(v), yields
\[
 |S_\phi|\le N[\sqrt{J\ell}+J^{3/4}\ell^{1/4}+J^{7/8}\ell^{1/8}]K^{-1/2}
 +(JN)^{7/8}\big(\mathbb E_1\mathbb E_2\mathbb E_3|S_f|\big)^{1/8}. \tag{13}
\]
Each E is exactly the2/Q weighted sum from(10). Apply(11) separately to all
three positive shift labels in each power row of(9).

For a row T D^d N^n in(9), its contribution to(13) is at most
\[
 U(T,d) C^{d/12}N^{7/8+n/8+5d/24},\quad
 U(T,d)=J^{7/8}[T(3/4)^d b_d^3]^{1/8}2^{\max(0,-7d/8)}. \tag{14}
\]
The factor2 for negative d retains the lower floor bound. The diagonal
coefficient from(13) is
\[
 U_0=\sqrt2[\sqrt{J\ell}+J^{3/4}\ell^{1/4}+J^{7/8}\ell^{1/8}].
\]
It has the same C,N powers as the first row of(14), so combine them. The four
resulting pairs of C,N powers are exactly
\[
 (1/42,37/42),\quad(13/336,1105/1344),\quad(-1/24,101/96),\quad(1/36,121/144).
                                                                    \tag{15}
\]
For the log row, ijk<=K^7<=kappa^7 implies
\[
 d_MDN^{-7/2}\le(3d_M/4)C^{2/3}N^{-11/6}.
\]
On the good range N>1; also C<=t^(3/4), as proved below. Consequently this
row is bounded by d+e*x, where x=logt,
\[
 d=6+(5/\pi)\log(2+3d_M/4),\qquad e=5/(2\pi).
\]
Its contribution is J^(7/8)(d+ex)^(1/8)N^(7/8). This full logarithmic row is
kept, not replaced by a fixed constant at arbitrarily large heights.

## 5. Return through the first B-process; bad range

The first partial-summation weight is at most sqrt(pi)h^(3/2)a^(3/2)/(tr)^(1/2).
For each coefficientU and powers(k,l) in(15), this gives a correlation row
\[
 V a^\alpha(tr)^\beta,\quad
 V=U\sqrt\pi h^{3/2}(2\pi)^{-k/2-l}h^{-2l},\quad
 \alpha=3/2-2l,\quad\beta=k/2+l-1/2.                    \tag{16}
\]
The log row uses(k,l)=(0,7/8). Thus all five(alpha,beta) pairs are
\[
 (-11/42,11/28),\ (-97/672,153/448),\ (-29/48,17/32),
 \quad(-13/72,17/48),\ (-1/4,3/8).                       \tag{17}
\]
The coefficient of the last row retains(d+ex)^(1/8).
The complete first Poisson formula additionally contributes
\[
 E_4a^{3/2}(tr)^{-1/2}+E_5a^{-1/3}(tr)^{1/3}
 +6+(5/\pi)\log(2+(h-1)tr/(\pi a^2)),                  \tag{18}
\]
where E4=5.686sqrt(pi)h^(3/2), E5=6h^3(h-1)/pi. Thus both Poisson formulas
retain separate endpoint and logarithmic errors.

If kappa<2, do not use(9)–(15). The original first-dual sum is bounded by its
length, giving at most d_T a^(-1/2)(tr)^(1/2) after the first weight, where
d_T=(h-1)h^(3/2)/sqrt(pi). This bad range is contained in r<R0, where
\[
 R_0=d_Ra^{20/9}/t,\qquad d_R=2\pi h^{20/9}2^{14/3}.     \tag{19}
\]
This follows directly from kappa<2 and(6). The first Poisson errors(18)
continue to apply. The first-integer debit covers a possible single first
dual integer even when the interval length is less than1. We may extend all
nonnegative good rows to the bad labels after paying this complete debit.

## 6. Outer A-process, uniform guards and partition

Fix
\[
 x_0=5800,\quad h_1=1.02,\quad h_2=1.03,\quad\theta_2=1,
 \quad\theta_3=10^{-5},\quad\vartheta=77/468.
\]
Use first large blocks a_k=floor(h1^(-k)sqrt(t/(2pi))) down to exponent3/7,
with Kouter=ceil[(x/14-log(theta2sqrt(2pi)))/logh1]. The last endpoint is
between theta2*t^(3/7)/h1-1 and theta2*t^(3/7). Set fixed constants
\[
 c=1-(h_1/\theta_2)e^{-3x_0/7},\quad h=h_1/c,\quad
 B_0=\theta_2/h_1-e^{-3x_0/7}>0.                         \tag{20}
\]
Every actual large block has ratio at mosth and a>=B0*t^(3/7).
For its outer integer length use
\[
 q_a=\lfloor\theta a^{106/117}t^{-11/39}\rfloor.          \tag{21}
\]
Here theta is the following specified positive real number, with V1 the
first coefficient in(16) and beta1=11/28:
\[
 \theta=[(h-1)/(\beta_1b_{\beta_1}V_1)]^{1/(1+\beta_1)}.
\]
It is merely a valid choice, not an assertion of exact optimization. Define
\[
 q_0=\theta B_0^{106/117}e^{29x_0/273},\quad Z=1-q_0^{-1},
 \quad p_0=\theta B_0^{-11/117}e^{-88x_0/273},\quad A=h-1+p_0.
                                                                    \tag{22}
\]
The directed certificate proves q0>2 and0<p0<.01, so throughout x>=x0,
1<=qa<=a, qa>=Ztheta*a^(106/117)t^(-11/39), and qa/a<=p0.
It also proves p0^2/4<.001 and
\[
 e^{2x_0}/[(2\pi)^2h^2]>1375^{21}.                       \tag{23}
\]
For every1<=r<qa, epsilon times the upper first-dual endpoint is at most
r^2/(4a^2)<=p0^2/4. Moreover a^2<=t/(2pi) gives NC^4>=t^2/[(2pi)^2h^2].
Thus both smallness hypotheses in Section2 and(12) hold uniformly on every
good correlation and every needed partial sum. Also C>=sqrt(t/(2pi))>1,
and C<=sqrt(ta/(2pi))<t^(3/4), proving the claims used for the log row.

Apply(10) once more to the original logarithmic block, with q=qa. After
partial summation by n^(-1/2), the squared weighted-block bound is at most A
times the sum of (h-1)a/qa and the weighted averages of all correlation rows.
For a row(16), (11) gives b_beta V a^alpha(t qa)^beta. After taking its
square root, put
\[
 u=(\alpha+(106/117)\beta)/2,\quad v=14\beta/39,
 \quad D=\sqrt{A b_\beta V\theta^\beta Z^{\min(\beta,0)}}. \tag{24}
\]
The row is D a^u t^v. Its coefficient and complete geometric sum are retained
below. The outer diagonal has exactly the same powers as the first row,
namely u=11/234,v=11/78, so their combined coefficient is
\[
 D_1=\sqrt{A[(h-1)/(\theta Z)+b_{11/28}V_1\theta^{11/28}]}.
                                                                    \tag{25}
\]
For(18), apply(24) separately to(E4,3/2,-1/2) and(E5,-1/3,1/3).

For the bad labels(19), use
sum_(1<=r<R0)sqrt(r)<=(2sqrt2/3)(R0^(3/2)+1). Their weighted average is at most
\[
 d_S[d_R^{3/2}a^{17/6}t^{-1}/q_a+a^{-1/2}t^{1/2}/q_a],
 \qquad d_S=(4\sqrt2/3)d_T.                              \tag{26}
\]
After taking roots the two additional pairs(u,v) and coefficients are
\[
 (451/468,-14/39),\quad\sqrt{A d_Sd_R^{3/2}/(\theta Z)},
\]
\[
 (-329/468,61/156),\quad\sqrt{A d_S/(\theta Z)}.
\]
No bad-label probability is discarded.

## 7. Whole infinite sums and height monotonicity

For u>0, the full geometric sum of a^u is bounded by
(2pi)^(-u/2)t^(u/2)/(h1^u-1). For u<0 it is bounded by
\[
 \frac{c^u(h_1/\theta_2)^{-u}}{1-h_1^u}\,t^{3u/7}.       \tag{27}
\]
This uses the floor comparison a_k>=c h1^(-k)sqrt(t/(2pi)) and the complete
lower-endpoint geometric series. Therefore define
\[
 G(D,u,v)=
 \begin{cases}
 D(2\pi)^{-u/2}(h_1^u-1)^{-1}e^{(u/2+v-\vartheta)x_0},&u>0,\\
 Dc^u(h_1/\theta_2)^{-u}(1-h_1^u)^{-1}
                      e^{(3u/7+v-\vartheta)x_0},&u<0.
 \end{cases}                                           \tag{28}
\]
Every height exponent is nonpositive and is checked as an exact rational
number. The first row has exponentzero. The second-Poisson endpoint row has
negative u=-115/1872; this is the reason for the new3/7 cutoff. Its exponent
3u/7+119/624-vartheta is strictly negative. At the old7/17 cutoff it would be
positive, so that older partition is not reused.

The second-Poisson logarithmic row has the coefficient(d+ex)^(1/16) after
all processes. Its residual exponential is strictly decreasing, and
1/(16x0) plus that exponent is negative. Thus its value in(28), using the
full coefficient atx0, bounds the entire tail, not just an endpoint.

For the first-Poisson logarithmic row, qa<=a and a>=B0*t^(3/7) give the bound
\[
 d_1+e_1x,\quad d_1=6+(5/\pi)\log(2+(h-1)/(\pi B_0)),
 \quad e_1=20/(7\pi).
\]
The number of large blocks is at most k*x, where
k=1/(14logh1)+1/x0, since theta2sqrt(2pi)>1. Its complete contribution,
normalized by t^vartheta, is at most
\[
 \sqrt A\,k\sqrt{d_1/x_0+e_1}\,x_0^{3/2}e^{-\vartheta x_0}. \tag{29}
\]
Indeed x^(3/2)e^(-vartheta*x) is decreasing for x>=x0. Let U3 be the sum of
(28) for the combined row(25), all four other rows(17), both power errors
from(18), both rows(26), and(29). This includes both logarithmic errors and
both sets of endpoint errors.

## 8. Initial and middle sums, certificate and completion

Below the large blocks use the same integer geometric fourth-derivative
partition from the accepted finite unsplit-PY theorem, now between
approximately theta3*t^(2vartheta) and theta2*t^(3/7). Its fixed ratio bound is
\[
 h_3=h_2/[1-(h_2/\theta_3)e^{-2\vartheta x_0}].
\]
With A4,B4 evaluated at eta=1,H=h3^4, put
\[
 D'_1=(3/\pi)^{1/14}A_4h_3^{5/7}(h_3-1),\quad
 D'_2=(\pi/3)^{1/14}B_4h_3^{2/7}(h_3-1)^{3/4}.
\]
The complete positive geometric sums, including a possibly shortened top
block, are bounded after normalization by
\[
 U_2=\frac{D'_1\theta_2^{3/14}}{h_2^{3/14}-1}e^{(8/49-\vartheta)x_0}
    +\frac{D'_2\theta_2^{15/28}}{h_2^{15/28}-1}e^{(31/196-\vartheta)x_0}.
                                                                    \tag{30}
\]
Both exponents are strictly negative. The initial sum is bounded by
U1=2sqrt(theta3+exp(-2vartheta*x0)/2). The certificate checks1<h,h3<2,
the existence/order of both partitions, all floor guards, and x0>log200.
Including both halves of the Riemann–Siegel sum and its complete remainder,
\[
 |\zeta(1/2+it)|/t^\vartheta\le
 2(U_1+U_2+U_3)+1.48e^{(-1/4-\vartheta)x_0}
                  +.127e^{(-3/4-\vartheta)x_0}.           \tag{31}
\]
The 192-bit directed certificate gives the right side strictly less than
87.718667171368722. Together with(4), this proves the theorem(1).

Run `python certify_exponent.py` with python-flint0.9.0/FLINT3.6.0. It checks
all listed scalar signs, rational height exponents, uniform guards, both
splice sides and the entire analytic infinite sum. The generated JSON pins
the script and records its exact parameters, coefficients and component
bounds. It contains no sampled-height extrapolation, installation log or
machine-specific path.

## Primary sources and dependencies

1. D. Patel and A. Yang, *An explicit sub-Weyl bound for zeta(1/2+it)*,
Journal of Number Theory262(2024),301–334,
https://doi.org/10.1016/j.jnt.2024.03.011 ; readable primary preprint
https://arxiv.org/html/2302.13444v1 . The argument uses its complete A-process,
weighted power sum, explicit Poisson formula and fourth-derivative test.
2. G. A. Hiary, D. Patel and A. Yang, *An improved explicit estimate for
zeta(1/2+it)*, https://arxiv.org/html/2207.02366v1 , for the unchanged complete
Riemann–Siegel setup and remainder as used in the accepted dependency.
3. The two fully written, reproducible dependencies linked in Section1.

The formal pair A B A^3 B A^2 B(0,1)=(11/78,161/234) only explains the
choice of powers. The proof above instead verifies the actual logarithmic
phase and its inverse, all finite shifts and every error term. The still
stronger classical exponent229/1392 mentioned by Patel–Yang is not claimed
here. Neither is a zero-free-region transfer from(1).
