# A global explicit sub-Weyl coefficient of 57 using block-dependent differencing

Status: complete analytic proof, directed computation and independent internal review completed.

## 1. Theorem and dependencies

For every real t with |t| >= 3,
\[
 |\zeta(1/2+it)|\le 57|t|^{27/164}.                         \tag{1}
\]

This improves the coefficient, retaining the exponent and entire range, of
Patel–Yang's published 66.7 theorem and the previously established coefficient
61. It is a function bound, not a percentage of zeros excluded.

We use the complete raw-block lemma and integer-endpoint repair from
[the finite unsplit-PY theorem](../20261016_unsplit_py_subweyl_table/REPORT.md),
and the uniform infinite-tail summation argument from
[the global coefficient 61 theorem](../20261016_global_subweyl_61/REPORT.md).
Their full derivative-test, Poisson-error and Riemann–Siegel hypotheses remain
unchanged. The new finite-height choice is an explicit block-dependent
integer differencing parameter. No improved exponent pair is assumed.

It suffices to prove t >= 3. The four closed ranges are [3,exp(60)],
[exp(60),exp(220)], [exp(220),exp(1800)], and [exp(1800),infinity).

## 2. The new block-dependent parameter

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
Let c3,c4,E4,E5 be its complete raw-block constants, evaluated at these
uniform parameters. In particular E4=5.686*sqrt(pi)*h^(3/2), including the
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

## 3. The entire unsplit finite sum

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
This is exactly the dependency's complete normalized bound, with Q+ and Q-
now computed separately for each block. No square-root summand is discarded.
The last line decreases with the height variable because its logarithmic
factor has derivative at most (5/pi)(7/41), whereas its positive bracket is
at least6 and 6*(27/82) > (5/pi)(7/41). Thus its left-endpoint use remains
valid even though the constants vary between blocks.

Sum (5)'s square roots over 1 <= k <= K_*. If fewer blocks actually exist,
including the remaining positive upper bounds only enlarges the result.
The initial sum, both middle-block series with their finite R_* factors,
the truncated top middle block and both Riemann–Siegel remainder terms are
retained exactly as in the dependency. Consequently the bound returned by
`adaptive_block.bound` is valid for every real height in the closed cell.

The file contains 79 closed cells [220+20j,240+20j], 0 <= j <= 78. The verifier
asserts this exact contiguous cover. Their maximum outward rounded coefficient
is56.42, strictly below57. The full balls, q guards, theta ranges, counts and
parameters are recorded in the scientific output.

For 3 <= t <= exp(60), the published .618*t^(1/6)*log(t) bound gives a
normalized coefficient below41.890. For exp(60) <= t <= exp(220), the
previously proved 32-row table has coefficients at most46.49. Both are below57.

## 4. Fixed parameters for the infinite tail

Set x0=1800 and fix, independently of t,
\[
 (h_1,h_2,\eta_1,\eta_2,\theta_1,\theta_2,\theta_3)
 =(1.015,1.03,1.8,1,1.3,10^{12},.00002).
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

## 5. Entire third-range tail

Let c3,c4,E4,E5 be the constants in the dependent raw block lemma (with
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
first two together. A weighted block is at most
\[
 C_1a^{5/82}t^{11/82}+C_2a^{-17/328}t^{61/328}
 +C_4a^{87/164}t^{-15/82}+C_5a^{-5/246}t^{5/41}
 +\sqrt{\alpha E_6(a,q,t)}.                                 \tag{6}
\]
This is a coarser bound than the finite unsplit sum, but its geometric sums
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
row is omitted at arbitrarily large t. Let U3=T1+T2+T4+T5+T6.

## 6. Initial and middle tail sums

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
 54.450823153427062101037<57.
\]
This completes the fourth range and proves (1).

## 7. Reproduction and scope

Run `python certify_global.py` with python-flint0.9.0 / FLINT3.6.0.
The 192-bit program checks all79 finite cells and every explicit infinite-tail
guard and sum. It records all parameters and file hashes. The previously
accepted [60,220] table is a named dependency, not an unrecorded extrapolation.

The finite differencing rule is block-dependent; the infinite tail deliberately
uses its separately specified single fixed theta1=1.3. These are different
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
