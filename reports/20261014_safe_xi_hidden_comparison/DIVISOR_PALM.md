# Positive all-prime xi divisor budget without the negative first label

This is a complete arithmetic square decomposition for the actual future
inverse of a source. It does not assert a Gamma lower bound or positivity
of the full reflected form. Its useful feature is that it never divides
by xi(x): the only seed labels used are n>=2, where xi is positive on the
entire positive half-line.

## 1. Actual source and positive shifted seed

Use the actual origin anchoring:

    f=g-r_0 psi,  r_0=(g/psi)(0),  R=f/psi,
    phi=M f,     C phi=f,       C xi=psi.

Here C u(x)=sum_(n>=1)n^(-1/2)u(x+log n), and M is its honest
future Mobius inverse on theta-decaying half-sources. The source f need
not be pole-centered; no U-gauge or higher neutral correction is made.
Write d_n=log n, alpha_n=Lambda(n)/sqrt(n), and

    xi(x)=exp(x/2)[8z^3-30z^2+15z]exp(-z),
    z=pi exp(2x).

For x>=0 and n>=2, z at x+d_n is at least 4pi>12, and xi(x+d_n)>0.
Define only these shifted ratios and weights:

    a_n(x)=phi(x+d_n)/xi(x+d_n),
    b_n(x)=n^(-1/2)xi(x+d_n),                    n>=2.       (1)

The actual bounded R and theta envelope give a uniform bound on a_n(x),
for x>=0,n>=2. Indeed, for u>=log2, psi(u)/xi(u) is bounded and

    sum_(k>=1)k^(-1/2)psi(u+log k)/xi(u)

is uniformly bounded by a Gaussian majorant. Hence |phi(u)|/xi(u) is
bounded by a constant times ||R||_infinity. The estimates also justify
all the source means and every square sum below.

## 2. Exact divisor disintegration

For any d>=2 define a positive probability on m>=1 by

    q_(d,m)(x)=m^(-1/2)xi(x+log d+log m)/psi(x+log d).

The same-source conditional mean is exactly

    sum_m q_(d,m)(x)a_(dm)(x)=R(x+log d).                  (2)

Let Var_d(a;x) be the variance of a_(dm)(x) under this probability.
For any real scalar c, divisor collection and log n=sum_(d|n)Lambda(d)
give the complete positive identity

    sum_(n>=2)(log n)b_n(x)[a_n(x)-c]^2
      =sum_(d>=2)alpha_d psi(x+log d)
           { [R(x+log d)-c]^2+Var_d(a;x) }.               (3)

Only prime-power d contribute, but every integer n is retained on the
left. To prove (3), expand the nonnegative left sum as

    sum_(d>=2)Lambda(d) sum_(m>=1)b_(dm)(x)[a_(dm)-c]^2,

using Tonelli. Since

    b_(dm)=d^(-1/2)m^(-1/2)xi(x+log d+log m),

conditional variance and (2) give (3), with exactly alpha_d and no
extra power or logarithm. There is no label n=1, because log 1=0.
In particular (3) has no xi_1 denominator, no signed-Gram inverse, and
no singularity when xi(x) changes sign or vanishes.

For clarity, the retained nonnegative conditional variance is

    Var_d(a;x)=1/2 sum_(j,k>=1)q_(d,j)q_(d,k)
                                [a_(dj)-a_(dk)]^2.        (4)

Thus it preserves the common arithmetic source across intersecting
multiple-of-d fibers. It is not a replacement by independent free
per-prime variables.

## 3. The full future-prime energy is one part of this budget

With the original convention

    P_F[R]=2 sum_d alpha_d integral_0^infinity
            psi(x)psi(x+log d)[R(x+log d)-R(x)]^2 dx,

take c=R(x) in (3) and integrate against 2psi(x)dx. The result is

    B_X[R]=P_F[R]+D_div[R],                              (5)

    B_X[R]=2 integral psi(x) sum_(n>=2)(log n)b_n(x)
                                      [a_n(x)-R(x)]^2 dx,
    D_div[R]=2 integral psi(x) sum_d alpha_d psi(x+log d)
                                      Var_d(a;x) dx>=0.

All quantities are finite for the actual source: the ratios are bounded,
the complete forward row has Gaussian integer tails, and psi has a theta
tail. Hence (5) is an equality of finite quantities, not cancellation of
infinite diagonal sums. Both B_X and D_div are unchanged by adding a
constant multiple of psi to f; a_n and R shift by that same constant.

The direction is important: (5) supplies an UPPER bound P_F<=B_X.
It is not a Gamma-to-prime lower estimate and does not by itself pay the
reflected energy or the pole.

## 4. Exact actual-origin specialization

At x=0 the anchored source has R(0)=0 and

    sum_d alpha_d f(log d)=0.

Let

    W_n=(log n)n^(-1/2)xi(log n), n>=2.

These weights are positive and their total is L_0:

    sum_n W_n=sum_d alpha_d psi(log d)=L_0.

The actual mean is zero, sum_n W_n a_n(0)=0. Therefore (3) gives

    L_0 Var_(W/L_0)(a)
       =J_0+sum_d alpha_d psi(log d)Var_d(a;0),           (6)

    J_0=sum_d alpha_d psi(log d)[r(log d)-r_0]^2.

This is an exact quadratic bridge to the original prime sample variance,
unlike an identification of J_0 with the signed eta/xi wall norm.
Probabilistically, the positive joint law proportional to
Lambda(d)b_(dm)(0) records the full prime-power divisor event. Its event
conditional mean is r(log d)-r_0; (6) is its law of total variance.
The log-weighted tail is the total prime-divisor event rate, not a
substitution of the single label d=n for composite integers.

## 5. Scope for the positive hidden Gamma/death process

The death-chain event n -> n/d has rate Lambda(d), d a prime power
dividing n. Identity (3) is the exact corresponding conditional-variance
budget in the xi-weighted positive shifted tail. All event locations
x+log n, n>=2, lie beyond the negative xi_1 band.

This does not make the entire xi-weighted hidden law positive: its n=1
component still has a negative interval, and the Gamma motion sees that
component. Neither a Gamma-only coherent coupling nor a closed original-
metric contraction is claimed. A full signed completion must retain that
Gamma/moving-field term, odd reflection, and the changed source pole.
