# A global explicit sub-Weyl coefficient of 49 from nested local dual estimates

Status: complete analytic proof and directed computation, independently internally reviewed and replayed.

## 1. Theorem and dependencies

For every real t with |t| >= 3,
\[
 |\zeta(1/2+it)|\le 49|t|^{27/164}.                         \tag{1}
\]

This improves the coefficient, retaining the exponent and entire range, of
Patel–Yang's published 66.7 theorem and the previously established coefficient
57. It is a function bound, not a percentage of zeros excluded.

We use the complete raw-block lemma and integer-endpoint repair from
[the finite unsplit-PY theorem](../20261016_unsplit_py_subweyl_table/REPORT.md),
and the uniform infinite-tail summation argument from
[the global coefficient 61 theorem](../20261016_global_subweyl_61/REPORT.md).
Their full derivative-test, Poisson-error and Riemann–Siegel hypotheses remain
unchanged. The new analytic input is two explicit local A-process estimates ending in the published third-derivative test
for the Poisson dual phase, with every additional error row retained. The
finite-height choice also uses block-dependent integer differencing. No
improved exponent pair or fifth-derivative constant is assumed.

It suffices to prove t >= 3. The four closed ranges are [3,exp(60)],
[exp(60),exp(220)], [exp(220),exp(1800)], and [exp(1800),infinity).

## 2. Nested local estimates ending in the third-derivative test

Let A3=A3(eta1,H) and B3=B3(eta1) be the complete published third-derivative
constants reproduced in the finite unsplit-PY dependency. Fix E=3. All
integer sums below have their phase defined on the whole real interval
between their endpoints; all nonempty correlations stay inside that interval.

For a sum of length n and any positive integer Q, zero extension and Cauchy
give
\[
 |S|^2\le(n+Q-1)\left[\frac nQ+
       \frac2Q\sum_{j=1}^{Q-1}(1-j/Q)|S_j|\right].          \tag{L1}
\]
No Q<=n hypothesis is needed: correlations with j>=n are zero. We repeatedly
use the complete positive weighted power-sum bound
\[
 \sum_{j=1}^{Q-1}(1-j/Q)j^s\le
       Q^{1+s}/[(1+s)(2+s)],\qquad -1<s\le1.
\]

First let f have monotonic fourth derivative of constant sign, with
mu <= |f^(4)| <= H mu and 0<mu<=1. Choose Q=ceil(E mu^(-1/7)).
The third derivative of f(x+j)-f(x) is the integral of f^(4) over [x,x+j],
so it is monotonic, has constant sign, and has absolute value between j*mu
and H*j*mu. The published third-derivative test bounds its sum by
A3 H^(1/2) n(j mu)^(1/6)+B3 n^(1/2)(j mu)^(-1/6).
Using Q>=E mu^(-1/7), Q< E mu^(-1/7)+1 and mu<=1 in (L1) proves
\[
 |S_f|^2\le[n+(E+1)\mu^{-1/7}]
                   [a n\mu^{1/7}+b n^{1/2}\mu^{-1/7}],    \tag{L2}
\]
\[
 a=E^{-1}+\frac{72}{91}A_3H^{1/2}(E+1)^{1/6},\qquad
 b=\frac{72}{55}B_3E^{-1/6}.
\]
In particular the complete four-row bound is
\[
 |S_f|\le\sqrt a\,n\mu^{1/14}
       +\sqrt b\,n^{3/4}\mu^{-1/14}
       +\sqrt{a(E+1)}\,n^{1/2}
       +\sqrt{b(E+1)}\,n^{1/4}\mu^{-1/7}.                \tag{L3}
\]
All rows are retained.

Now let phi have monotonic fifth derivative of constant sign, with
lambda<=|phi^(5)|<=H lambda. Set
\[
 \lambda_* = E^{-15/14},\qquad 0<\lambda\le\lambda_*.
\]
Choose the outer local parameter Q=ceil(E lambda^(-1/15)). For every j<Q,
\[
 j\lambda < E\lambda^{14/15}\le1.
\]
The fourth derivative of phi(x+j)-phi(x) is the integral of phi^(5), is
monotonic with constant sign, and lies between j*lambda and H*j*lambda.
Thus (L3) applies to every nonempty correlation, with mu=j*lambda.
Another application of (L1) gives
\[
 |S_\phi|^2\le[n+(E+1)\lambda^{-1/15}]
 [A n\lambda^{1/15}+B n^{3/4}\lambda^{-1/15}
                +C n^{1/2}+D n^{1/4}\lambda^{-2/15}],     \tag{L4}
\]
where
\[
 A=E^{-1}+\frac{392}{435}\sqrt a(E+1)^{1/14},\quad
 B=\frac{392}{351}\sqrt b E^{-1/14},
\]
\[
 C=\sqrt{a(E+1)},\qquad D=\frac{49}{39}\sqrt{b(E+1)}E^{-1/7}.
\]
The coefficients 392/435,392/351,1,49/39 come from s=1/14,-1/14,0,-1/7,
respectively; in the zero-power row the weighted factor is at most1.

Expand (L4) and bound the square root by the sum of all eight square roots.
Write this bound as sum_i c_i n^(p_i) lambda^(s_i), with the exact table
\[
\begin{array}{c|c|c}
 c_i&p_i&s_i\\\hline
 \sqrt A&1&1/30\\
 \sqrt B&7/8&-1/30\\
 \sqrt C&3/4&0\\
 \sqrt D&5/8&-1/15\\
 \sqrt{A(E+1)}&1/2&0\\
 \sqrt{B(E+1)}&3/8&-1/15\\
 \sqrt{C(E+1)}&1/4&-1/30\\
 \sqrt{D(E+1)}&1/8&-1/10
\end{array}.                                                   \tag{L5}
\]
These are local inequalities, not a claimed improved global fifth-derivative
test outside lambda<=lambda_*.

## 3. Complete transfer to the original logarithmic-phase block

Use the Poisson dual phase phi_r of the finite unsplit-PY theorem, and put
\[
 L_0=53632\sqrt2\pi^4/729,\quad H=76545\sqrt2h^9/107264,
 \quad n_0=(h-1)/\pi,\quad w_0=\sqrt\pi h^{3/2}.
\]
Its fifth derivative has the sign and monotonicity proved there, with
lambda=L0*a^9/(tr)^4. The dual interval has length at most n0*tr/a^2,
and the maximum monotone partial-summation weight is at most
w0*a^(3/2)/(tr)^(1/2).

Remove the first lattice point from every partial dual sum, paying its unit
cost as in the dependency. The remaining integer length is at most the real
dual interval length. For lambda<=lambda_*, (L5) and monotone partial
summation give eight positive rows
\[
 d_i a^{\alpha_i}(tr)^{\beta_i},\qquad
 d_i=w_0c_i n_0^{p_i}L_0^{s_i},\quad
 \alpha_i=3/2-2p_i+9s_i,\quad\beta_i=-1/2+p_i-4s_i.        \tag{L6}
\]
The exponent pairs (alpha_i,beta_i), in the same order, are
\[
 (-1/5,11/30),\ (-11/20,61/120),\ (0,1/4),\ (-7/20,47/120),
\]
\[
 (1/2,0),\ (3/20,17/120),\ (7/10,-7/60),\ (7/20,1/40).
\]
In particular every beta_i lies strictly above -1 and at most1.

For lambda>lambda_*, namely r<R0=(L0/lambda_*)^(1/4)*a^(9/4)/t, use only
the trivial remaining dual-length bound. Its weighted contribution is at
most w0*n0*a^(-1/2)*(tr)^(1/2). The first removed point is paid for every r,
so the Poisson coefficient remains E4=5.686, not 4.686. The complete cubic
and logarithmic Poisson errors are unchanged.

Apply the original A-process with its lawful integer 1<=q<=a. Extending the
eight nonnegative rows over every r<q is harmless after the separate
lambda>lambda_* debit is retained. Put F_i=2/[(1+beta_i)(2+beta_i)].
In the weighted square a^(-1)|S_f|^2, after the common factor h-1+q/a,
these rows contribute at most
\[
 \sum_i F_i d_i a^{\alpha_i}(qt)^{\beta_i}.
\]
The separately retained large-lambda debit contributes at most
\[
 d_S\left[\frac{(L_0/\lambda_*)^{3/8}a^{23/8}}{tq}
                         +\frac{a^{-1/2}t^{1/2}}q\right],
 \qquad d_S=4\sqrt2w_0n_0/3.                              \tag{L7}
\]
Indeed sum_(1<=r<R0) sqrt(r) <= (2/3)(R0+1)^(3/2)
<= (2sqrt(2)/3)(R0^(3/2)+1), and dropping the outer weights only enlarges
this positive debit. The inequality also covers R0<1 and q<R0.
All original diagonal, endpoint and Poisson terms remain in the square bound.
Every partial interval uses the same original-block q, so the weighted-block
partial-summation step remains valid. No prefix of an oscillatory sum is
bounded by the magnitude of a longer sum.

## 4. The new block-dependent parameter

Fix one closed cell l <= log t <= u. Its six positive rational parameters,
in their file order, are h1,h2,eta1,eta2,theta2,theta3. Define the partition
counts and floor constants exactly as in the finite dependency:
\[
 K_* = \left\lceil\frac{3u/34-\log(\theta_2\sqrt{2\pi})}{\log h_1}\right\rceil,
 \quad R_* = \left\lceil\frac{115u/1394-\log(\theta_3/\theta_2)}{\log h_2}\right\rceil,
\]
\[
 h=\frac{h_1}{1-(h_1/\theta_2)e^{-7l/17}},\qquad
 h_3=\frac{h_2}{1-(h_2/\theta_3)e^{-27l/82}}.
\]
Let c3=d1 and c4=d2 be the first two constants (L6), with
A3,B3 evaluated at eta1,H5; let dS be (L7). Let E4,E5 be the unchanged complete
Poisson constants, all evaluated at these uniform parameters. In particular E4=5.686*sqrt(pi)*h^(3/2), including the
first-dual-lattice-point debit. Set
\[
 c_B=\frac{1800}{2911}c_3,\quad c_C=\frac{28800}{54481}c_4,
 \qquad \theta_0=\left(\frac{30(h-1)}{11c_B}\right)^{30/41}.
\]
For each integer 1 <= k <= K_*, put
\[
 A_k^+=h_1^{-k}/\sqrt{2\pi},\qquad A_k^-=A_k^+-e^{-l/2},
\]
\[
 \rho_k=\frac{61c_C}{44c_B}\theta_0^{17/120}
                  (A_k^+)^{-37/164}e^{-3l/328},\qquad
 \theta_k=\theta_0(1+\rho_k)^{-120/181}.                   \tag{2}
\]
Every quantity in (2) is a specified exact positive real number depending
only on the cell and the block index. Floating optimization is not part of
this definition or proof; (2) need not be the exact optimizer.

For an actual block whose integer left endpoint is a_k(t), choose
\[
 q_k(t)=\left\lfloor\theta_k a_k(t)^{36/41}t^{-11/41}\right\rfloor. \tag{3}
\]
The raw-block lemma applies separately to each block and each lawful integer
q. It nowhere requires the same theta across different blocks. All partial
sums within a given block use its same integer q_k(t), preserving the
partial-summation bound and the first-dual-endpoint repair.

Here are the explicit floor checks. Set
\[
 Q_k^+=\theta_k(A_k^+)^{36/41},\qquad
 Q_k^-=\theta_k(A_k^-)^{36/41}-e^{-7l/41}.
\]
The directed checker verifies A_k^-,Q_k^- > 0 and
\[
 (Q_k^+/A_k^-)e^{-27l/82}<1                               \tag{4}
\]
for every 1 <= k <= K_*. Since a_k(t)/sqrt(t) lies between A_k^- and A_k^+,
\[
 Q_k^-t^{7/41}\le q_k(t)\le Q_k^+t^{7/41},\qquad
 q_k(t)/a_k(t)\le(Q_k^+/A_k^-)e^{-27l/82}<1.
\]
Thus (3) is an integer with 1 <= q_k(t) <= a_k(t) throughout the cell.
The checker also retains the partition endpoint condition a_K >= a'_R,
1 < h,h3 < 2, and both positive integer block-count conditions.

## 5. The entire unsplit finite sum

For clarity, write A+=A_k^+, A-=A_k^-, Q+=Q_k^+, Q-=Q_k^- in the next formula.
The normalized weighted-block upper bound is the square root of
\[
 (h-1+(Q^+/A^-)e^{-27l/82})\,T_k,
\]
where
\[
\begin{aligned}
 T_k={}&(h-1)A^+/Q^-
 +c_B(A^-)^{-1/5}(Q^+)^{11/30}\\
 &+c_C(A^-)^{-11/20}(Q^+)^{61/120}e^{-3l/328}\\
 &+\frac83E_4(A^+)^{3/2}(Q^-)^{-1/2}e^{-27l/164}\\
 &+\frac9{14}E_5(A^-)^{-1/3}(Q^+)^{1/3}e^{-13l/123}\\
 &+\left[6+\frac5\pi\log\left(2+\frac{(h-1)Q^+}{\pi(A^-)^2}
                                e^{7l/41}\right)\right]e^{-27l/82}.
\end{aligned}                                                    \tag{5}
\]
Add to T_k all six rows i=3,...,8:
\[
 F_i d_i (A^{\epsilon_i})^{\alpha_i}(Q^{\delta_i})^{\beta_i}
           e^{[\alpha_i/2+(48/41)\beta_i-27/82]l},        \tag{11}
\]
where A^(epsilon_i) means A+ for alpha_i>=0 and A- otherwise; Q^(delta_i)
means Q+ for beta_i>=0 and Q- otherwise. The six height exponents, in order,
are -3/82,-15/328,-13/164,-29/328,-19/164,-1/8, all strictly negative.
Also add both complete large-lambda debits
\[
 d_S(L_0/\lambda_*)^{3/8}(A^+)^{23/8}(Q^-)^{-1}e^{-l/16}
 +d_S(A^-)^{-1/2}(Q^-)^{-1}e^{-l/4}.
\]
All positive corrections from the inner and outer A-processes are retained.
In particular the negative beta_7=-7/60 uses Q-, not Q+.
The last line of (5) decreases with the height variable because its logarithmic
factor has derivative at most (5/pi)(7/41), whereas its positive bracket is
at least6 and 6*(27/82) > (5/pi)(7/41). Thus its left-endpoint use remains
valid even though the constants vary between blocks.

Sum the square roots of the complete augmented T_k bound over 1 <= k <= K_*. If fewer blocks actually exist,
including the remaining positive upper bounds only enlarges the result.
The initial sum, both middle-block series with their finite R_* factors,
the truncated top middle block and both Riemann–Siegel remainder terms are
retained exactly as in the dependency. Consequently the bound returned by
`dual_block.bound` is valid for every real height in the closed cell.

The file contains 79 closed cells [220+20j,240+20j], 0 <= j <= 78. The verifier
asserts this exact contiguous cover. Their maximum outward rounded coefficient
is48.61, strictly below49. The full balls, q guards, theta ranges, counts and
parameters are recorded in the scientific output.

For 3 <= t <= exp(60), the published .618*t^(1/6)*log(t) bound gives a
normalized coefficient below41.890. For exp(60) <= t <= exp(220), the
previously proved 32-row table has coefficients at most46.49. Both are below49.

## 6. Fixed parameters for the infinite tail

Set x0=1800 and fix, independently of t,
\[
 (h_1,h_2,\eta_1,\eta_2,\theta_1,\theta_2,\theta_3)
 =(1.015,1.03,1.2,1,2.7,10^{12},.00002).
\]
Use the same integer partitions a_k, a'_r and counts K(x), R(x) as in the
dependent proof. Define
\[
 c=1-(h_1/\theta_2)e^{-7x_0/17},\quad h=h_1/c,\quad
 h_3=\frac{h_2}{1-(h_2/\theta_3)e^{-27x_0/82}},\quad
 B_0=\theta_2/h_1-e^{-7x_0/17},
\]
\[
 q_0=\theta_1 B_0^{36/41}e^{65x_0/697},\quad
 p_0=\theta_1 B_0^{-5/41}e^{-222x_0/697},\quad
 \alpha=h-1+p_0.
\]
Directed arithmetic checks c,B0>0, q0>2, p0<1 and 1<h,h3<2, as well as
\[
 (\theta_2/h_1)e^{115x_0/1394}-e^{-27x_0/82}>\theta_3.
\]
Exactly as in the finite proof these imply a_K>=a'_R and the required ratios
throughout x>=x0. For every existing third-range block,
\[
 a_k\ge B_0t^{7/17},\qquad
 c h_1^{-k}\sqrt{t/(2\pi)}\le a_k\le h_1^{-k}\sqrt{t/(2\pi)}.
\]
With q=floor(theta1*a_k^(36/41)*t^(-11/41)), put
y=theta1*a_k^(36/41)*t^(-11/41). Then y>=q0, and consequently
\[
 q\ge y(1-q_0^{-1}),\qquad 0<q/a_k\le p_0<1.
\]
All q are therefore lawful integers between1 and a_k. These are uniform
infinite-height implications; no finite endpoint guard is extrapolated without
its monotonic dependence on x being specified.

## 7. Entire third-range tail

Let c3,c4 be d1,d2 from (L6), and E4,E5 the unchanged Poisson constants (with
E4=5.686*sqrt(pi)*h^(3/2), so the endpoint debit is retained). Set
\[
 C_1=\sqrt{\alpha\left(\frac{h-1}{\theta_1(1-q_0^{-1})}
            +\frac{1800}{2911}c_3\theta_1^{11/30}\right)},\quad
 C_2=\sqrt{\alpha\frac{28800}{54481}c_4\theta_1^{61/120}},
\]
\[
 C_4=\sqrt{\alpha\frac83 E_4\theta_1^{-1/2}(1-q_0^{-1})^{-1/2}},
 \qquad C_5=\sqrt{\alpha\frac9{14}E_5\theta_1^{1/3}}.
\]
For this tail only, split the positive square-root rows after keeping the
first two together. The square root of the sum of the original five rows
is at most
\[
 C_1a^{5/82}t^{11/82}+C_2a^{-17/328}t^{61/328}
 +C_4a^{87/164}t^{-15/82}+C_5a^{-5/246}t^{5/41}
 +\sqrt{\alpha E_6(a,q,t)}.                                 \tag{6}
\]
The six additional rows from (L6) and both large-lambda debits (L7) are
summed explicitly below. This
splitting is coarser than the finite unsplit sum, but its geometric sums
are simple and sufficient at x>=1800.

Use
\[
 K(x)\le \frac{3x/34-\log(\theta_2\sqrt{2\pi})}{\log h_1}+1.
\]
For positive powers, sum the infinite decreasing geometric series. For a
negative power -p, use the lower floor comparison and the displayed upper
bound on K. Specifically,
\[
 \sum_{k=1}^{K}a_k^{-p}
 \le c^{-p}(2\pi)^{p/2}t^{-p/2}
       \frac{h_1^{pK}-1}{1-h_1^{-p}}
 \le \frac{c^{-p}(h_1/\theta_2)^p}{1-h_1^{-p}}
       t^{-7p/17}.                                         \tag{7}
\]
Dropping the subtracted1 is favorable for an upper bound. Thus the first four
rows of (6), divided by t^(27/164) and summed, are bounded by
\[
 T_1=\frac{C_1(2\pi)^{-5/164}}{h_1^{5/82}-1},\qquad
 T_2=\frac{C_2c^{-17/328}(h_1/\theta_2)^{17/328}}
             {1-h_1^{-17/328}},
\]
\[
 T_4=\frac{C_4(2\pi)^{-87/328}}{h_1^{87/164}-1}e^{-27x_0/328},
 \quad
 T_5=\frac{C_5c^{-5/246}(h_1/\theta_2)^{5/246}}
             {1-h_1^{-5/246}}e^{-427x_0/8364}.              \tag{8}
\]
The powers in the latter two terms decrease with x. For the secondary row
T2 the t exponent is exactly zero, not discarded with an incorrect sign.

The logarithmic row remains complete. Since a>=B0*t^(7/17) and q<=y,
\[
 \frac{(h-1)tq}{\pi a^2}\le C e^{188x/697},\qquad
 C=(h-1)\theta_1B_0^{-46/41}/\pi.
\]
For x>=0,
\[
 E_6\le D+Ex,\quad D=6+(5/\pi)\log(2+C)>0,\quad E=940/(697\pi)>0.
\]
This follows from 2+C*exp(v)<=exp(v)(2+C), v>=0. Also log(theta2*sqrt(2pi))>0,
so K(x)<=k*x where k=3/(34log h1)+1/x0. Hence its normalized sum is bounded by
\[
 \sqrt\alpha\,k\sqrt{D/x_0+E}\,x^{3/2}e^{-27x/164}
 \le T_6:=\sqrt\alpha\,k\sqrt{D/x_0+E}\,x_0^{3/2}e^{-27x_0/164}. \tag{9}
\]
The last inequality follows from 3/(2x0)<27/164. No portion of the logarithmic
row is omitted at arbitrarily large t. The six additional correlation rows are also summed. For i=3,...,8, put
\[
 u_i=(\alpha_i+(36/41)\beta_i)/2,\quad v_i=15\beta_i/41,
 \quad Z=1-q_0^{-1},
\]
\[
 D_i=\sqrt{\alpha F_i d_i\theta_1^{\beta_i}
                              Z^{\min(\beta_i,0)}}.
\]
For u_i>0 their complete normalized tail is bounded by
\[
 T_i'=\frac{D_i(2\pi)^{-u_i/2}}{h_1^{u_i}-1}
                   e^{(u_i/2+v_i-27/164)x_0}.
\]
For u_i<0 use the negative-power sum (7), giving
\[
 T_i'=\frac{D_i c^{u_i}(h_1/\theta_2)^{-u_i}}{1-h_1^{u_i}}
                   e^{(7u_i/17+v_i-27/164)x_0}.           \tag{12}
\]
Only i=4 has negative u_i=-1/328. The six resulting height exponents are
-3/164,-63/2788,-13/328,-29/656,-19/328,-1/16. Thus all are decreasing
throughout x>=x0. The factor Z for beta_7<0 retains the lower integer-q bound.

Finally put C_S=sqrt(alpha*dS/[theta1*(1-q0^(-1))]). The two large-lambda
rows have complete normalized geometric bounds
\[
 T_{S1}=\frac{C_S(L_0/\lambda_*)^{3/16}(2\pi)^{-655/1312}}
                    {h_1^{655/656}-1}e^{-x_0/32},
\]
\[
 T_{S2}=\frac{C_Sc^{-113/164}(h_1/\theta_2)^{113/164}}
                      {1-h_1^{-113/164}}e^{-179x_0/2788}.
\]
The latter uses p=113/164 in (7). Let
U3=T1+T2+T4+T5+T6+sum_(i=3,...,8) T_i'+TS1+TS2.

## 8. Initial and middle tail sums

Use the same D1,D2 as in the finite-block proof, with the fixed h3 above.
The entire fourth-derivative block series is bounded by
\[
 U_2=\frac{D_1\theta_2^{3/14}}{h_2^{3/14}-1}
                     e^{(19/119-27/164)x_0}
     +\frac{D_2\theta_2^{15/28}}{h_2^{15/28}-1}
                     e^{(71/476-27/164)x_0}.
\]
Both exponents are negative. The initial sum is at most
U1=2sqrt(theta3+exp(-27x0/82)/2). Including the complete Riemann–Siegel
remainder, the uniform tail coefficient is at most
\[
 2(U_1+U_2+U_3)+1.48e^{(-1/4-27/164)x_0}
                   +.127e^{(-3/4-27/164)x_0}.               \tag{10}
\]
The directed enclosure of (10) is
\[
 45.821582134220449880018<49.
\]
This completes the fourth range and proves (1).

## 9. Reproduction and scope

Run `python certify_global.py` with python-flint0.9.0 / FLINT3.6.0.
The 192-bit program checks all79 finite cells and every explicit infinite-tail
guard and sum. It records all parameters and file hashes. The previously
accepted [60,220] table is a named dependency, not an unrecorded extrapolation.

The finite differencing rule is block-dependent; the infinite tail deliberately
uses its separately specified single fixed theta1=2.7. These are different
valid bounds on overlapping closed ranges, not a claim that (2) holds uniformly
at arbitrary heights with fixed finite-cell constants.

The primary 66.7 comparator has the same exponent and range. No exhaustive
priority claim, zero-count proportion, or RH conclusion follows. Favorable
finite-height and Weyl bounds remain available and are not all pointwise
superseded by a single global coefficient.

## Primary sources

1. D. Patel and A. Yang, *An explicit sub-Weyl bound for zeta(1/2+it)*,
Journal of Number Theory262(2024),301–334,
https://doi.org/10.1016/j.jnt.2024.03.011 ; readable preprint
https://arxiv.org/html/2302.13444v1 .
2. G. A. Hiary, D. Patel and A. Yang, *An improved explicit estimate for
zeta(1/2+it)*, https://arxiv.org/html/2207.02366v1 , Theorem1.1.
3. The two complete proof and reproducibility dependencies linked in Section1.
