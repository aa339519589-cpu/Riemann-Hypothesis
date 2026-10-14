# A complete bound for the adverse SAME-current storage density

This note bounds the actual signed original adjoint density, not an
independently chosen majorant or a modified source metric. It is intended
for the closed current/forward-energy absorption calculation, whose
threshold depends on keeping this coefficient below the previously
available coarse bound.

## 1. Statement and scope

Use the original source psi=-Phi'>0, K=3Phi+Theta/2, and

    H(x)=int_0^infinity kappa(x+y)psi(y)dy,
    L(x)=sum_(log n>x)Lambda(n)n^(-1/2)psi(log n-x),
    b(x)=psi(x)[sinh(x/2)/2+2K(x)-2xpsi(x)-H(x)-L(x)],
    rho(x)=psi(x)exp(x/2), b_-(x)=max(0,-b(x)).

Then on the COMPLETE positive wing,

    0<=b_-(x)<=2rho(x).                                    (1)

All prime powers in L and every theta label are retained. The origin
localization is the independently checked theorem
[POSITIVE_ORIGIN_BAND.md](POSITIVE_ORIGIN_BAND.md),
which proves b>0 on (0,1/12]. On that interval (1) is automatic. The
remaining compact and infinite-wing estimates are given below.

For the actual current V=T|w-u|^2, (1) gives

    -int bV<=2int rho V.                                   (2)

This changes neither V nor the canonical/current distinction. It does
not assert that b itself is nonnegative, does not delete its favorable
positive part from exact identities, and is not a sign for the original
full Q_delta form.

## 2. A complete three-moment upper bound for the Gamma wall

Since kappa(t)=sum_(j>=0)exp[-(2j+1/2)t], put

    V_j=int_0^infinity exp[-(2j+1/2)y]psi(y)dy.

Every V_j is positive and sum_j V_j=H(0). The exact origin source identity
is H(0)+L(0)=K(0), hence H(0)<=K(0). The following upper bounds are certified
by directed intervals and full theta tails:

    V_0<4/5, V_1<1/2, V_2<1/3, K(0)<3.                    (3)

The computational upper enclosures for the three moments are respectively
0.7835709188798083, 0.4816321882804543 and 0.3183707358271529.
Their proof is elementary and does not use numerical quadrature without
an enclosure. For a_j=2j+1/2, integration by parts gives

    V_j=Phi(0)-a_j int_0^infinity exp(-a_j y)Phi(y)dy.

Use the complete upper bound for Phi(0), and integrate a directed-interval
LOWER bound of its positive first Gaussian term over500 rational cells
in [0,1]. All omitted positive terms and the omitted infinite tail lower
the resulting upper bound for V_j. This proves (3).

For x>=0, grouping the remaining positive j>=3 rows gives

    H(x)/exp(x/2)
       <=exp(-x){(1-exp(-6x))(4/5)
                +(exp(-2x)-exp(-6x))/2
                +(exp(-4x)-exp(-6x))/3
                +exp(-6x)K_upper(0)}=:H_upper(x).           (4)

Every coefficient of a substituted moment is nonnegative. No alternating
moment bound or discarded negative contribution is used. The exact
complete theta upper value K_upper(0)<2.710 is used by the checker rather
than replacing it by3 on the compact interval.

## 3. Complete compact prime and theta enclosures

Write z=pi exp(2x), P(z)=4z^2-6z and c(z)=8z^3-30z^2+15z. The standard
complete theta bounds used in the earlier checked graph theorem are

    Phi(x)<=exp(x/2)[P(z)exp(-z)+128z^2exp(-4z)],
    psi(x)<=exp(x/2)[c(z)exp(-z)+1024z^3exp(-4z)],
    K(x)>=exp(x/2-z)[3P(z)+1/2].                           (5)

The second bound is valid for z>=pi even when its first term is negative:
all n>=2 terms are positive and their full absolute upper sum is bounded
by the displayed tail. On an interval crossing a prime threshold the
argument log n-x is intersected with [0,infinity) before this upper bound
is used. Thus no positive threshold collar is omitted.

For the entire compact range 1/12<=x<=6, the checker retains all genuine
prime powers n<=2048 in L, with their actual Mangoldt coefficients. For
n>=N0=2049 set a=pi exp(-12). The complete omitted row is at most

    256 exp(-3) a^3 N0^7 exp(-a N0^2)<10^(-24).              (6)

Indeed for those labels, z_n=pi n^2 exp(-2x)>12, so
psi(log n-x)<=16sqrt(n)exp(-x/2)z_n^3 exp(-z_n).
Use Lambda(n)<=log n<=n for this UPPER tail only. Each resulting summand
increases with x up to6, since its logarithmic derivative is
-13/2+2z_n>0. At x=6 the consecutive integer ratio is at most15/16,
certified directly; hence the full tail is at most16 times its first
upper summand. This gives the coefficient256 in (6). No prime-label
truncation is treated as exact.

Now divide -b by rho and use (4)-(6):

    -b/rho <=H_upper+exp(-x/2)L_upper
           +2x exp(-x/2)psi_upper
           -(1-exp(-x))/4-2exp(-x/2)K_lower.                (7)

The retained negative K and polar terms are necessary on the compact
wing. The checker covers [1/12,6] by rational intervals, starting with
width1/100 and bisecting only when an upper enclosure does not yet prove
(7)<2. All operations use directed50-digit interval arithmetic; the final
accepted intervals cover the entire range without gaps. The certificate
records their number, largest upper endpoint, and the complete prime-tail
enclosure. Thus (7)<2 on the full compact range, not just at sample points.

## 4. Unconditional infinite arithmetic tail

For x>=log349, use the complete reflected-row Stieltjes identity with
F0(t)=exp(-t/2)psi(t):

    L(x)/exp(x/2)
       =-int_0^infinity F0'(t)Psi_C(exp(x+t))/exp(x)dt.

The already sourced unconditional Chebyshev bounds .91Y<Psi_C(Y)<1.04Y
for Y>=349 give

    L(x)/exp(x/2)<=1.04 J+.13 I_+,
    J=int_0^infinity exp(t/2)psi(t)dt,
    I_+=int_0^infinity exp(t)max(F0'(t),0)dt<293/100.        (8)

The bound for I_+ is the full theta variation theorem in the published
[analytic reflected-row proof](../20261014_positive_reflected_storage/ANALYTIC_TAIL.md).
For completeness J<6/5 follows from a very coarse positive estimate:

    J=Phi(0)+(1/2)int_0^infinity exp(t/2)Phi(t)dt,
    Phi(0)<9/10, int_0^infinity Phi<1/4.

On [0,1], exp(t/2)<5/3. On t>=1 one has z>=20 and the logarithmic
derivative of exp(t/2)Phi(t) is at most7-2z<=-33, term by positive term.
Its entire tail integral is therefore at most exp(1/2)Phi(1)/33<1/100,
again certified from (5). Consequently
J<9/10+(1/2)(5/12+1/100)<6/5.

For x>=log349 the remaining positive terms in -b/rho satisfy

    H(x)/exp(x/2)<=K(0)exp(-x)<3/349<1/100,
    2xpsi(x)exp(-x/2)<=16z^4exp(-z)<1/10.

The second uses 2x=log(z/pi)<=z and z>=20; z^4exp(-z) decreases there,
and 16*20^4/(5/2)^20<1/10. Discarding only the favorable negative polar
and K terms gives

    -b/rho <(104/100)(6/5)+(13/100)(293/100)+1/100+1/10
             =17389/10000<2.                              (9)

Since log349<6, this overlaps the compact certificate. Combining (9),
(7), and the positive-origin theorem proves (1) everywhere.

## 5. One actual variance budget, not an independent gain

The exact current identity remains

    E_current=F[u]-int bV.

The estimate (2) can be combined with an honest SAME-current contrast
bound in L2(rho p_n), and the incoming-prime hub theorem pays its first-label
input by original F[w_1]. A closed absorption argument must retain its
full recursive reference forcing and the exact relation between V and
w_n-w_1. Neither a canonical xi variance nor an independently resampled
edge variance may replace V. The current-to-forward bridge obtained that
way is a finite quantitative comparison, not the coefficient-one original
signed inequality. The original reflected/pole and neutral terms remain.
