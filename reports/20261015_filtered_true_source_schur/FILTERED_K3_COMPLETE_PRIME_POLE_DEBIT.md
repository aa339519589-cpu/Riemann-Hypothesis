# Complete prime and pole debit for the A=16, k=3 filtered source

This note supplies a quantitative COMPLETE negative-row bound for the
concrete source used in the signed original-Schur certificate. It uses
[the stable filtered seed](SOURCE_DEFINITION.md),
not a finite-prime surrogate. The finite one-dimensional mass and pole
inputs below are explicitly separated from the analytically paid infinite
remainders. This note alone does not sign the original Schur form.

Set A=16, k=3, b=log2, x_A=(1/2)log(16/pi),

    phi(x)=2z c(z)exp(-z)u(z)/W(x), z=pi exp(2x),
    t=1_(x>b)C phi,
    M(Z)=integral_(pi exp(2x)>=Z)phi(x)^2dx,
    M0=M(16), E=t-phi.

All functions here are real. The main phi is already supported above b.
Use the full source q0, with the prime/pole portion

    -4 sum_n alpha_n integral_b^infinity t(x)t(x+log n)dx
    +2 sum_n alpha_n integral_b^(log n-b)t(x)t(log n-x)dx
    -8 ell(t)^2,
    alpha_n=Lambda(n)/sqrt(n), ell(t)=integral_b^infinity sinh(x/2)t(x)dx. (1)

An empty reflected interval contributes zero. The Gamma part is retained
separately by the certificate, not bounded below in this note.

## 1. A uniform real seed bound with small constants

For nu=9/4, the Bessel Poisson integral, verified by its beta-integral
power series, is

    g(s)=s^nu/[sqrt(pi)Gamma(11/4)]
              integral_(-1)^1 exp(2i sqrt(16s)y)(1-y^2)^(7/4)dy.

The weight and its first derivative vanish at both endpoints. Its second
derivative is integrable and has L1 norm at most7. Indeed the first
derivative has exactly one extremum on each half interval, and
|(7/2)y(1-y^2)^(3/4)|<=7/4. Two integrations by parts therefore give

    |g(s)|<=[7/(64 sqrt(pi)Gamma(11/4))]s^(5/4)
            <(21/320)s^(5/4), s>0.

Here sqrt(pi)>5/3 and Gamma(11/4)>1; the latter follows from
Gamma(11/4)=(21/16)Gamma(3/4) and
integral_0^1(1-v)v^(-1/4)dv=16/21.

The k=3 stable signed convolution measure is delta_0+exp(-v)P(v)dv,

    P(v)=-6+15v-10v^2+(5/2)v^3-(1/4)v^4+v^5/120.

Exact polynomial integration gives integral_0^infinity exp(-v)P(v)^2dv=6.
Thus its total variation is at most1+sqrt6<7/2, by Cauchy--Schwarz.
The complete stable convolution consequently obeys

    |u(16+s)|<=s^(5/4)/4, s>=0 (strict for s>0).                       (2)

This global real bound does not require a large-argument asymptotic or
sampled oscillatory cancellation.

For z>=48 the n=2 term of W gives
W(x)>=exp(x/2)c(z/4)exp(-z/4)/2. Also
c(z)<=8z^3 and c(z/4)>=(11/2)(z/4)^3. Combining this with (2) yields

    |phi(x)|<=140 z^2 exp(-3z/4), z>=48.             (3)

Every future label n>=2 has n^2 z>=48 when x>=b. Its complete sum gives

    |E(x)|<=140 z^2 sum_(n>=2)n^(7/2)exp(-3n^2z/4)
            <=2000 z^2 exp(-3z), z>=4pi.            (4)

For the final inequality, the first summand is at most12exp(-3z);
consecutive summands have ratio at most(3/2)^4exp(-45)<1/1000.
The elementary lower bound exp(3)>20 pays all exponential comparisons.

## 2. Weighted control of every arithmetic cross term

Write ||f||_G^2=integral_b^infinity exp(2x)|f(x)|^2dx. Formula (4) gives

    ||E||_G^2
       <=(2000^2/6) integral_12^infinity z^4exp(-6z)dz
       <10^(-20).                                   (5)

Assume the certified main mass input

    M0<2*10^(-9).                                    (I)

On z<=48 the weight exp(2x) is at most16. On z>=48 use (3). This gives

    ||phi||_G<1/5000.                                (6)

All numerical inequalities in (5)-(6) are exact rational upper checks
using the finite incomplete-Gamma polynomial and exp(3)>20; see the
companion checker.

Let A_pr=sum_n Lambda(n)n^(-3/2)<5, the already verified complete arithmetic
constant in [the complete source Schur bounds](../20261014_original_seed_schur/SOURCE_SCHUR.md). For arbitrary G functions,

    |sum alpha_n integral f(x)g(x+log n)dx|
                                   <=A_pr exp(-2b)||f||_G||g||_G,
    |sum alpha_n integral f(x)g(log n-x)dx|
                                   <=A_pr ||f||_G||g||_G.       (7)

Since exp(-2b)=1/4, the TOTAL change in the forward-plus-reflected portion
of (1) on replacing phi by phi+E is bounded by

    3A_pr[2||phi||_G||E||_G+||E||_G^2]<6.1*10^(-13). (8)

This is one complete bilinear bound. No individual prime or mixed source
term is omitted or assigned a favorable sign.

## 3. Main prime rows: only five finite reflected masses remain

For reflection n, splitting at x=(log n)/2 and applying Cauchy--Schwarz
gives

    |integral phi(x)phi(log n-x)dx|<=2sqrt(M0 M(pi n)). (9)

No pure-phi reflection is possible for n<=5, since n<exp(2x_A)=16/pi.
The next integer6 is not a prime power. Hence the first such row is n=7.
Among n<16 the exact remaining labels are

    F={7,8,9,11,13}.

For every Z>=48, (3) gives

    M(Z)<=9800 integral_Z^infinity z^3exp(-3z/2)dz
           <=6860 Z^3exp(-3Z/2).                    (10)

For n>=16, use first M(pi n)<=M(3n), since pi>3 and M is decreasing.
Applying (10) at Z=3n therefore gives
sqrt(M(pi n))<431 n^(3/2)exp(-9n/4). Using Lambda(n)<=log n<=n and the
consecutive ratio bound for n^2exp(-9n/4), the COMPLETE reflected debit
from n>=16 is less than10^(-14). This includes all nonzero prime powers;
bounding by all integers only enlarges the absolute upper estimate.

For the main forward row,

    |integral phi(x)phi(x+log n)dx|<=sqrt(M0 M(16n^2)). (11)

All n>=2 in (11) are in the range of (10). The full forward debit is less
than3*10^(-20), by the same Gaussian consecutive-ratio estimate. These
infinite sums are checked with outward rational bounds in the companion
checker, not by stopping at a finite prime.

## 4. Full same-source bound and the exact remaining certificate input

Assume also the signed pole input

    |ell(t)|<2*10^(-10).                              (II)

Its debit is then less than3.2*10^(-19). Combining (8)-(11) with the pole
shows that the COMPLETE portion (1) is bounded below by minus

    4sqrt(M0) sum_(n in F) [Lambda(n)/sqrt(n)]sqrt(M(pi n))
                                      +6.2*10^(-13). (12)

Thus certified upper bounds on the five masses M(pi n), n in F, together
with (I)-(II), suffice. For example if their displayed finite term is
less than9.9*10^(-11), the full prime-plus-pole debit is less than10^(-10).
The finite hypothesis must be checked from outward mass enclosures, not
from sampled tail estimates.

An optional exact trace-zero gauge t#=t-c_b psi_T leaves the original
Schur value unchanged, but changes all source rows together. If a
certificate instead uses that representative, retain its own signed
pole interval. Under |c_b|<6*10^(-16), the same proof applies with the
remainder E-c_b psi_T: the complete bound ||psi_T||_G<1/10 gives
||E-c_b psi_T||_G<1.000001*10^(-10), so the reserve6.2*10^(-13) in (12)
still pays the arithmetic cross change. The Gamma and head inverse must
use the same chosen source representative.

## 5. Outward finite-cell input and the resulting numerical debit

The companion checker can consume the separately generated outward JSON
from the complete main-seed cell calculation. The sufficient rational
input bounds are

    M0<1/28000^2,
    sqrt(M(7pi))<111/10^8,
    sqrt(M(8pi))<7/10^8,
    sqrt(M(9pi))<9/10^9,
    sqrt(M(11pi))<2/10^11,
    sqrt(M(13pi))<5/10^14,
    |ell(phi)|<13/10^11.                              (13)

These are checked by squaring positive rational numbers, not by rounding
square roots downward. Since log n/sqrt(n)<1 for every n>=1, the finite
term in (12) is at most

    (1/7000)[111/10^8+7/10^8+9/10^9+2/10^11+5/10^14].

After the full reserve in (12), the COMPLETE prime/pole debit is therefore

    less than 1.71*10^(-10).                           (14)

The pole input (II) follows from the last bound in (13) and (5):
|ell(E)|<=sqrt(7/96)||E||_G<10^(-10)/3, so their sum is below2*10^(-10).
This also pays the optional trace correction under its stated bound.
For the latter, the auxiliary norm ||psi_T||_G<1/10 used above follows
from psi<=2xi on x>=b and the exact incomplete-Gamma bound

    ||psi_T||_G^2
       <=(64/9) integral_12^infinity z^7exp(-2z)dz<1/100.

The complete pointwise estimate psi<=2xi follows directly by summing
xi(x+log n)/sqrt(n) relative to xi(x), using
c(n^2z)/c(z)<(16/11)n^6 and z>=4pi>12. Its nontrivial-label sum is
bounded by a geometric series with first term (16/11)64exp(-36)<1/2.

For reproducibility, the input used in the first finite replay is
filtered_bessel_tail_mass_enclosures.json,
SHA256 cf59df43e80791ed56bc44a96a62b9426a28670d4c8381649453e5c328157708.
Its validated Taylor-cell construction is a separate prerequisite. The
checker here verifies the exact implication of its outward numbers plus
all infinite arithmetic remainders; it does not replace the independent
audit of the cell construction. The final Gamma lower bound and full
source-head residual are also separate, still required inputs.
