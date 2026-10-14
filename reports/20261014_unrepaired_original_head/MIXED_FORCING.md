# A quantitative complete mixed-forcing bound from the actual bounded seed

The full original mixed forcing is not bounded by only hidden mass at its
degenerate endpoint. The actual common seed has additional boundedness.
This note gives a quantitative estimate using that genuine source constraint,
retaining the complete odd Gamma kernel, every prime and the pole.

Use b=log2, Y=b+31/100, m=Wxi and the complete safe-ray functions from the
[published hidden comparison](../20261014_safe_xi_hidden_comparison/REPORT.md).
Its [head bounds](../20261014_safe_xi_hidden_comparison/HEAD_GAP.md) and
[complete theta rows](../20261014_safe_xi_hidden_comparison/BULK_TAIL.md)
are the elementary inputs used below. Let a be the true safe common seed and c a
single constant. Put

    a0=a-c,  V=integral_b^infinity m|a0|^2,
    M=||a0||_Linfinity(b,infinity),
    F_T(x)=sum_(n>=1)n^(-1/2)xi(x+log n)a0(x+log n), x>b.

Thus F_T=f_T-c psi_T, not a replacement source. For 0<=delta<=1 let
B_delta F_T be the ordinary L2 head density of the COMPLETE original mixed
pairing Q_delta(F_T,h). Then

    ||B_delta F_T||_L2(0,b)^2 <=4000 M sqrt(V).        (1)

The estimate is homogeneous of degree two in the source. It does not assert
linear domination by V, and it is not a coefficient-one signed comparison.
For actual fixed-depth sources M is finite by their proved bounded ratio
and the explicit complete future Mobius/theta majorant in Section 5. The
constant c and its unchanged original psi channel remain explicit.

## 1. An explicit weak-L2 weight bound

Let dmu=m(y)dy and q(y)=exp(2y)xi(y)/W(y). Then

    sup_(t>0) t^2 mu{q>t} <=7/200.                  (2)

Only already certified elementary theta bounds enter this estimate. On
0<s<=31/100, y=b+s, the exact starting row is W=psi(s)/sqrt2. The certified
concavity and endpoint estimates give

    psi(s)>=6s, psi(s)<=17s, xi(b+s)<1/10,
    W(b+s)>4s, m(b+s)<(17/10)s,
    exp(2Y)<8.

Consequently q(b+s)<1/(5s), and the head contribution to the weak square
bound is at most

    (17/20)(1/5)^2=17/500.                          (3)

For y>=Y put z=pi exp(2y)>20. The positive n=2 starting summand and the
same cubic estimate used in the published cap proof give

    xi(y)/W(y)<=512 exp(-3z/4),
    xi(y)^2<=64 exp(y)z^6 exp(-2z).

Therefore

    integral_Y^infinity q^2 dmu
       =integral_Y^infinity exp(4y)xi(y)^3/W(y)dy
       <=16384*pi^(-5/2) integral_20^infinity
                                  z^(15/2) exp(-11z/4)dz
       <1/1000.                                    (4)

For a fully elementary final bound, the logarithmic derivative of the
integrand on z>=20 is at most -19/8, so its integral is at most
(8/19)20^(15/2)exp(-55). Use pi^(-5/2)<1,
20^(15/2)<20^8, and exp(55)>exp(54)>20^18, the last following from exp(3)>20.
Then the upper bound in (4) is less than (131072/19)20^(-10)<1/1000.
Chebyshev on the tail and (3) prove (2). These estimates retain the full W;
no asymptotic prime density or finite-label replacement is involved.

For any 0<=w<=M^2 with integral w dmu=V, layer cake gives, for t>0,

    integral q w dmu
       <=tV+M^2 integral_t^infinity mu{q>s}ds
       <=tV+(7/200)M^2/t.

Optimizing t proves the exact interpolation estimate

    integral q |a0|^2 dmu <=2M sqrt(7V/200).          (5)

Zero cases follow by a limit. This is the endpoint weak-L2 estimate; it
requires actual boundedness and does not turn q into a strong L2 dual.

## 2. Complete future lift in an original weighted source norm

Minkowski and y=x+log n give

    ||F_T||_L2(exp(2x)dx)
      <=sum_(n>=1)n^(-3/2)
          [integral_(b+log n)^infinity exp(2y)xi(y)^2|a0(y)|^2dy]^(1/2)
      <=3 [integral q|a0|^2 dmu]^(1/2).             (6)

Here sum n^(-3/2)<=1+integral_1^infinity x^(-3/2)dx=3. The n=1 branch
and every later branch are retained; no relative source asymptotic or
nonzero sample division is needed. Combining (5)-(6) proves that the
actual compensated tail lies in this original weighted L2 class.

## 3. The COMPLETE mixed operator has an explicit weighted bound

Let S=||F_T||_L2(exp(2y)dy). Its exact density on 0<x<b is

    B_delta F_T(x)
      =-2 integral_b^infinity [kappa(y-x)-kappa(y+x)]F_T(y)dy
       -2sum_n alpha_n F_T(x+log n)
       +2(1-delta)sum_n alpha_n F_T(log n-x)1_(log n-x>b)
       -8sinh(x/2) integral_b^infinity sinh(y/2)F_T(y)dy. (7)

The diagonal potential does not cross disjoint supports. The complete
reflected coefficient is 2(1-delta), not 2; the full pole stays in (7).

For Gamma, write x=b-s,y=b+t. Since

    kappa(u)<=1/(2u)+exp(-u/2),

its positive odd kernel is dominated by a Carleman kernel plus a rank-one
exponential kernel. The Carleman norm is at most pi by the Schur weight
s^(-1/2); the rank-one norm is at most 2. Thus the first term of (7) has
L2 norm at most (pi+2)||F_T||_2 <=(pi+2)S/2.

Put A=sum_(n>=2)Lambda(n)n^(-3/2). Every shifted L2 norm is bounded by its
weighted norm: the forward prime sum has norm at most AS, and the reflected
sum has norm at most 2AS. The latter uses y=log n-x>=log n-b before the
positive-tail indicator is imposed. Since Lambda(n)<=log n and
(log x)x^(-3/2) is decreasing for x>=2,

    A<=log2/(2sqrt2)+integral_2^infinity (log x)x^(-3/2)dx<5.

The two prime terms in (7) therefore contribute at most 30S in norm,
uniformly for 0<=delta<=1. There is no finite-prime cutoff in this bound.

Finally

    ||sinh(x/2)||_L2(0,b)^2=(sinh b-b)/2,
    integral_b^infinity sinh(y/2)^2 exp(-2y)dy=7/96.

Cauchy--Schwarz bounds the pole term by
8 sqrt[(sinh b-b)/2]sqrt(7/96) S. Altogether

    ||B_delta F_T||_2 <34 S.                        (8)

The simple bound 34 follows, for example, from pi<22/7, b>69/100 and
sinh b=3/4, together with A<5. Equations (5), (6) and (8) give

    ||B_delta F_T||_2^2
       <=20808 sqrt(7/200) M sqrt(V)<4000 M sqrt(V),

which proves (1). All density identities extend from finite cutoffs by
these absolute operator bounds, so there is no infinity-minus-infinity
pairing or unproved pointwise prime convergence.

## 4. Actual stationarity and what is still unpaid

For an actual source, both f and f-c psi have the SAME original stationarity.
Thus the compensated source head has original forcing exactly minus (7).
This supplies an ordinary L2 forcing estimate on the actual class, stronger
than merely assigning it an abstract form-dual meaning.

If c is the full m-weighted mean of a, V is the hidden variance, and the
published comparison gives V<=125000 B[a]. The known actual ratio bounds
also control M by C_(delta,s)sqrt(P0). Consequently (1) quantitatively
excludes arbitrary hidden-mass boundary spikes among normalized actual
sources. It does not imply B_delta is a bounded linear map of hidden mass
alone; that false statement would omit M.

Balanced finite-rank repaired loads can be added with their separately
proved JOINT Gram inequality, retaining the exact rank-two mixed terms.
Their global zero identities belong to the plateau gauge; after replacing
f by f-c psi any changed global U component must be kept. In particular
one may not apply the repaired stationarity equation unchanged to this
new representative without its explicit scalar forcing.

The remaining original signed Schur inequality is not settled by (1).
Its square-root dependence on V is weaker than the coefficient-one linear
payment that a final full-form comparison would need.

## 5. Explicit boundedness of the genuine actual Mobius seed

Write the actual source f=psi R, with its proved bounded ratio R from
[the actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md).
A fixed constant-ratio representative is retained throughout.
On the POSITIVE safe ray y>=b the complete xi sum is positive, so absolute
future Mobius convolution and divisor regrouping give

    |Mf(y)|/xi(y)
      <=||R||infinity sum_(k>=1)d(k)k^(-1/2)xi(y+log k)/xi(y).

Here d(k) is the number of divisors. This is an upper bound of the actual
signed Mobius sum, not a replacement seed. All summations converge
absolutely by their Gaussian tails. For z=pi exp(2y)>=4pi>12, the exact
cubic ratio obeys c(k^2z)/c(z)<=2k^6. Since d(k)<=k and the square-root
translation factor cancels k^(-1/2), the k>=2 contribution is at most

    2 sum_(k>=2)k^7 exp[-12(k^2-1)]
      <=512 exp(-36)<1.

The first term is 256 exp(-36), and each successive majorant has ratio
at most (3/2)^7 exp(-60)<1/2. The k=1 term is exactly one. Consequently

    ||a||infinity=||Mf/xi||infinity<=2||R||infinity.

For either a full m-weighted mean or the published positive head-weighted
mean, |c|<=||a||infinity and therefore M<=4||R||infinity. This proves the
actual boundedness input using the full signed seed and all integer labels.
It neither divides by a possibly zero source sample nor extends xi
positivity through its unsafe first band.
