# A strict actual-theta obstruction to the naive grouped variance payment

The definitions here are those of `GROUPED_PRIME_POWER_FACTORIZATION.md`.
The exact theta source proves

\[
 \boxed{H_2\left(\tfrac34\log2\right)<-\tfrac23.}
\tag{1}
\]

This is not a negative vector for `P-N`. It proves that the coefficient
multiplying the first grouped within-fiber variance need not be positive,
so the simplest separate per-prime variance payment fails.

Put `d=log2`, `t=3d/4`, `a=2^(-1/2)` and

\[
 M(t)=\sum_{j\ge0}a^j\psi(t+jd),\quad
 U=\pi e^{2t}=2\pi\sqrt2,\quad V=\pi e^{2(d-t)}=\pi\sqrt2.
\]

The exact differentiated theta expansion is

\[
 \psi(x)=e^{x/2}\sum_{n\ge1}e^{-u_n}
       (8u_n^3-30u_n^2+15u_n),\qquad u_n=\pi n^2e^{2x}.
\tag{2}
\]

Elementary rational bounds give

\[
 \frac{222}{25}<U<\frac{889}{100},\quad
 \frac{111}{25}<V<\frac{89}{20},\quad
 e^{222/25}>7000,\quad e^{89/20}<90,
\]
\[
 2^{3/8}<\frac{13}{10},\qquad a>\frac7{10},\qquad \pi^3<32.
\tag{3}
\]

The companion script `check_factorizations.py` verifies the rational
steps in (3) without floating-point arithmetic: the pi bounds use
Machin's identity and alternating arctangent bounds, square-root bounds
are verified by squaring, and exponential bounds use Taylor sums with a
geometric upper bound for the remainder.

For the `j=0,n=1` term in `M(t)`, (2)--(3) give the upper bound

\[
 B_0=\frac{13}{10\cdot7000}
 \left[8\left(\frac{889}{100}\right)^3
       -30\left(\frac{222}{25}\right)^2
       +15\frac{889}{100}\right].
\tag{4}
\]

For all remaining terms, `8u^3-30u^2+15u < 8u^3` because `u>1/2`.
Since `U>8`, `e>2`, and
`8 pi^3 e^(13t/2) < 8192`, the theta-index tail at `j=0` is bounded by

\[
 8192\sum_{n\ge2}n^6 2^{-8n^2}
 <8192\cdot 2\cdot64\cdot2^{-32}<\frac1{1000}.
\tag{5}
\]

The factor 2 bounds a geometric series: the ratio of consecutive terms
for `n>=2` is at most `(3/2)^6 2^(-40)<1/2`.

For all translated tails `j>=1`, use
`a^j e^(13jd/2)=64^j` to obtain

\[
\begin{aligned}
 \sum_{j\ge1}a^j\psi(t+jd)
 &<8192\sum_{j\ge1}64^j\sum_{n\ge1}n^6 2^{-8\cdot4^j n^2}\\
 &<16384\sum_{j\ge1}64^j 2^{-8\cdot4^j}
 <2^{-11}<\frac1{1000}.
\end{aligned}
\tag{6}
\]

Both geometric bounds in (6) use consecutive ratios at most
`64*2^(-24*4^j)<1/2`. Combining (4)--(6), exact rational arithmetic gives

\[
 M(t)<B_0+\frac2{1000}<\frac23.
\tag{7}
\]

At `d-t=d/4`, every theta summand in (2) is positive, since
`u_n>=V>111/25` and `8u^2-30u+15>0` there. Keeping its first term and
using `e^((d-t)/2)>1` gives

\[
\begin{aligned}
 aM(d-t)&\ge a\psi(d-t)\\
 &>\frac7{10\cdot90}
 \left[8\left(\frac{111}{25}\right)^3
       -30\left(\frac{89}{20}\right)^2
       +15\frac{111}{25}\right]
 >\frac43.
\end{aligned}
\tag{8}
\]

Subtract (8) from (7) to prove (1). The script in fact verifies the
slightly stronger rational upper bound

\[
 H_2(3d/4)<-\frac{18698870059}{26250000000}<-\frac23.
\]

No finite prime cutoff, floating-point sign inference, or RH assumption
enters this obstruction. It concerns only the indicated mass coefficient;
the higher tail variances, Gamma energy, and pole energy remain present
in the complete comparison.
