# A global explicit sub-Weyl coefficient of 61

Status: complete analytic proof, directed computation and independent internal review completed.
Dependency: the independently audited finite unsplit-PY block theorem,
[Finite-height sub-Weyl bounds from an unsplit A-process](../20261016_unsplit_py_subweyl_table/REPORT.md).
The dependency was published with its complete proof and reproducible certificates.

## 1. Theorem

For every real t with |t|>=3,
\[
 \boxed{\quad |\zeta(1/2+it)|\le61\,|t|^{27/164}.\quad}       \tag{1}
\]

This retains the height range and exponent of Patel–Yang's global theorem,
while replacing its coefficient 66.7 by 61. No zero-count percentage or
Riemann Hypothesis conclusion follows from (1) alone. The numerical coefficient
reduction is about 8.55%; that is a reduction of a function upper bound, not a
fraction of zeros excluded.

It suffices to prove t>=3 by conjugation. The proof has four overlapping
closed ranges: [3,exp60], [exp60,exp220], [exp220,exp1300], and [exp1300,infinity).
The infinite range has an analytic bound, not a numerical extrapolation.

## 2. Low and finite middle ranges

The published global Hiary–Patel–Yang theorem gives
\[
 |\zeta(1/2+it)|\le .618t^{1/6}\log t\qquad(t\ge3).
\]
The normalized function .618*x*exp((1/6-27/164)x) is increasing for x>=log3.
Its directed value at x=60 is less than61. This pays the complete first range.

The dependent finite-block theorem supplies all 32 closed five-unit intervals
covering x=log t in [60,220], with coefficients at most46.49<61.

For [220,1300], use exactly the same proved normalized block formula, including
its first-dual-lattice-point debit, complete logarithmic error, and all floor
constraints. `parameters.txt` fixes 54 closed intervals [220+20j,240+20j],
0<=j<=53, and seven rational parameters for each. In particular, h1=1.015,
h2=1.03, eta1=1.8, eta2=1, theta1=1.15 and theta3=.00002 throughout; theta2
is the displayed exact rational in each row. No assumed analytic relation
between successive theta2 values is used.

For each row, `unsplit_block.bound` encloses the entire real interval, using
the upper integer block counts at its right endpoint and directed decreasing
exponential bounds at its left endpoint. The returned bound is less than61
in every row. These are interval certificates, not samples. The underlying
block functions are the functions of the dependency, with its standalone
file-writing main routine omitted; their arithmetic is unchanged.

## 3. Fixed parameters for the infinite tail

Set x0=1300 and fix, independently of t,
\[
 (h_1,h_2,\eta_1,\eta_2,\theta_1,\theta_2,\theta_3)
 =(1.015,1.03,1.8,1,1.15,10^9,.00002).
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

## 4. Entire third-range tail

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
 +\sqrt{\alpha E_6(a,q,t)}.                                 \tag{2}
\]
This is a coarser bound than the finite unsplit sum, but its geometric sums
are simple and sufficient at x>=1300.

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
       t^{-7p/17}.                                         \tag{3}
\]
Dropping the subtracted1 is favorable for an upper bound. Thus the first four
rows of (2), divided by t^(27/164) and summed, are bounded by
\[
 T_1=\frac{C_1(2\pi)^{-5/164}}{h_1^{5/82}-1},\qquad
 T_2=\frac{C_2c^{-17/328}(h_1/\theta_2)^{17/328}}
             {1-h_1^{-17/328}},
\]
\[
 T_4=\frac{C_4(2\pi)^{-87/328}}{h_1^{87/164}-1}e^{-27x_0/328},
 \quad
 T_5=\frac{C_5c^{-5/246}(h_1/\theta_2)^{5/246}}
             {1-h_1^{-5/246}}e^{-427x_0/8364}.              \tag{4}
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
 \le T_6:=\sqrt\alpha\,k\sqrt{D/x_0+E}\,x_0^{3/2}e^{-27x_0/164}. \tag{5}
\]
The last inequality follows from 3/(2x0)<27/164. No portion of the logarithmic
row is omitted at arbitrarily large t. Let U3=T1+T2+T4+T5+T6.

## 5. Initial and middle tail sums

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
                   +.127e^{(-3/4-27/164)x_0}.               \tag{6}
\]
The directed enclosure of (6) is
\[
 59.704127024126934949604<60<61.
\]
This completes the fourth range and proves (1).

## 6. Reproduction and comparison scope

Run `python certify_global.py` with python-flint0.9.0 / FLINT3.6.0.
The 192-bit checker verifies all54 finite intervals and all explicit guards
and infinite-tail constants above. Its JSON records every finite component,
parameter and bound, the low-height splice, the tail components and hashes.
The [60,220] calculation is the separately supplied dependency, not silently
recomputed or replaced. Run that dependency's checker to verify the full chain.

The primary comparator is Patel–Yang's Theorem1.1, which states66.7 with the
same exponent and full range t>=3. More favorable height-dependent bounds
from their table and other Weyl bounds remain useful and are not claimed to
be pointwise superseded by the single global coefficient61.

## Primary sources

1. D. Patel and A. Yang, *An explicit sub-Weyl bound for zeta(1/2+it)*,
Journal of Number Theory262(2024),301–334,
https://doi.org/10.1016/j.jnt.2024.03.011 ; readable preprint
https://arxiv.org/html/2302.13444v1 .
2. G. A. Hiary, D. Patel and A. Yang, *An improved explicit estimate for
zeta(1/2+it)*, https://arxiv.org/html/2207.02366v1 , Theorem1.1.
3. The finite unsplit-PY theorem linked above, including the full raw-block
and integer-endpoint proof and its32-row directed certificate.
