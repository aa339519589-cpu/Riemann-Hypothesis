# Validated series and complex bounds for the stable-filter test

Use A>4pi, integer k>=1, nu=k-3/4, and u from
[the stable reciprocal-heat construction](SOURCE_DEFINITION.md).
These formulas supply enclosures for concrete signed-Schur test evaluation;
they do not evaluate or sign the Schur form.

## 1. An entire density after the fourth-root substitution

The exact density is

    u(A+s)=s^nu F(s),
    F(s)=sum_(n>=0)(-1)^n D_n s^n/Gamma(n+nu+1),
    D_n=sum_(j=0)^n A^j/j! binom(2k+n-j-1,n-j)>0.    (1)

It follows either from the Laplace transform at infinity or directly from
the absolutely convergent Bessel/convolution expansions. The series for F
is entire. With s=w^4 the density is the entire function

    U(w)=w^(4k-3)F(w^4).                              (2)

There is no fractional branch in U. The generating function of D_n is
exp(Az)(1-z)^(-2k), which gives D_0=1 and

    (n+1)D_(n+1)=(A+2k+n)D_n-A D_(n-1),             (3)

with D_(-1)=0. Formula (1), not a subtractive floating recurrence, can be
used for rigorous interval coefficient evaluation.

For R>=0 put T_n=D_n R^n/Gamma(n+nu+1). Positivity and (3) imply

    T_(n+1)/T_n<=q_n
       :=R(A+2k+n)/[(n+1)(n+nu+1)].                 (4)

The rational function q_n is strictly decreasing in n>=0: differentiating
its real-variable extension gives numerator
-n^2-2(A+2k)n+(nu+1)-(A+2k)(nu+2)<0. Therefore, whenever q_N<1,

    sum_(n>=N) T_n<=T_N/(1-q_N).                     (5)

This bounds the complete complex-disc remainder for |s|<=R after truncating
(1) at n=N-1, without assuming an alternating real-series error rule.
It also proves entire convergence directly. Derivative enclosures follow
by Cauchy's formula on a strictly larger disc or by differentiating the
polynomial plus the corresponding power-series majorant.

## 2. A useful complex-disc majorant without long summation

The Bessel series and (nu+1)_j>=j! give

    |(s/A)^(nu/2)J_nu(2sqrt(A s))|
         <=|s|^nu exp(2sqrt(A|s|))/Gamma(nu+1).       (6)

The elementary inequality sum x^j/(j!)^2<=exp(2sqrt x) follows by bounding
the central binomial coefficient by 4^j in the even exponential series.
Apply the stable convolution along the straight segment v=t s. For
|s|<=R and Re s>=-D, D>=0, its finite j-th convolution is bounded using
|exp(-t s)|<=exp(D), (1-t)^nu<=1, and integral_0^1 t^(j-1)dt=1/j.
The result is

    |u(A+s)|<=R^nu exp(2sqrt(A R)+D)(1+R)^(2k)
                                                    /Gamma(nu+1). (7)

Interpreted through (2), (7) holds without a branch convention: if a
complex w-disc has |w|<=r and Re(w^4)>=-D, then

    |U(w)|<=r^(4k-3) exp(2sqrt(A r^4)+D)(1+r^4)^(2k)
                                                    /Gamma(k+1/4). (8)

A disc contained in Re(w^4)>=0 uses D=0. For a general disc |w-w0|<=d,
one may take r=|w0|+d and D=max(0,-Re(w0^4)+4d r^3).
Cauchy's bound on an enclosing disc of radius d then gives
|U^(j)(w0)|<=j! sup|U|/d^j. These are analytic majorants, not sampled
numerical maxima. Factors involving the true W must still use their
correct fixed integer branch on each quadrature interval.

## 3. Explicit k=2 stable kernel

For k=2, nu=5/4 and the finite kernel is

    u(A+s)=g(s)+integral_0^s exp(-v)
                     [-4+6v-2v^2+v^3/6]g(s-v)dv,
    g(s)=(s/A)^(5/8)J_(5/4)(2sqrt(A s)).              (9)

In general its density is -exp(-v)L_(2k-1)^(1)(v), equivalently the finite
binomial polynomial already given in the construction. No Laguerre
identity is needed to implement the explicit sum. The complete W-knot
and rational future-knot bookkeeping is retained in
[the finite-variation interface](FILTERED_MAIN_FORCE_VARIATION.md).
