# An anisotropic explicit mixed-coordinate bound with classical exponent 19/116

Status: complete proof and certificates have passed independent internal mathematical review and reproducible checks. This is not external peer review or formal-kernel verification, and no zero-count consequence is asserted.

## 1. Statement and complete local inputs

The theorem is

|zeta(1/2+it)| <= 10^7 |t|^(19/116) (log|t|)^(33/58),    |t|>=3.       (1)

Retain the minimum with the accepted 49 |t|^(27/164), 90 |t|^(77/468), and [110 |t|^(229/1392)](../20261016_nested_extra_dual_subweyl_exponent/REPORT.md). The last bound is used only for the lower-height splice. The exponent19/116 is classical, not a new unrestricted exponent or an exhaustive explicit-bound priority claim. This is a critical-line function estimate, not a percentage of zeros excluded.

This proof includes three indispensable local appendices:

- [Explicit rectangular second-derivative lemma](SECOND_DERIVATIVE_LEMMA.md), including indefinite/definite gradient injectivity, boundary integrals, exact smoothing and every absolutely summable Fourier tail.
- [Mixed three-A and curved-cutoff lemma](MIXED_A_AND_CUTOFF.md), including all diagonal/floor terms, frequency-uniform separable twists, exact boundary lattice points and the full two-variable amplitude variation.
- [Actual order-nine derivative proof](ACTUAL_MIXED_DERIVATIVES.md), including its rational certificate.

No implicit multidimensional constant or formal exponent-pair rule is an input. In particular, the relatively degenerate undifferenced first-dual Hessian is never used as a nondegenerate two-dimensional phase.

We otherwise use Patel–Yang's complete one-dimensional Poisson formula, the elementary A-process before taking absolute values of correlations, its explicit fourth-derivative test, and the Riemann–Siegel remainder already stated in the accepted dependency. Their exact roles are specified below. Put e(y)=exp(2pi i y), x=log t, c=t/(2pi), p=19/58 and theta=p/2=19/116. Set gamma=10^(-7). It suffices by conjugation to treat t>0.

## 2. Integer partitions and the first correlation

First assume x>=x0=10000. Let A be the least integral power of2 not smaller than t^(3/7), and let B be the least integral power of2 not smaller than t^p. Thus

t^(3/7)<=A<2t^(3/7),  t^p<=B<2t^p.

The certificate proves B<=A<sqrt(c). Partition the Riemann–Siegel sum into the initial segment n<=B, dyadic integer blocks from B to A, and dyadic integer blocks from A to floor sqrt(c), shortening only the last block. Every large block is a<n<=b<=2a with integer endpoints and

t^(3/7)<=a<=sqrt(c).

Put q=floor(gamma a^(28/29)t^(-9/29)x^(-33/29)). Then

q>=gamma a^(28/29)t^(-9/29)x^(-33/29)/2
 >=gamma t^(3/29)x^(-33/29)/2>1,
q/a<=t^(-66/203)<1.                    (2)

All estimates below hold uniformly when b is replaced by any integer partial endpoint. This is necessary for partial summation by n^(-1/2).

For f(n)=-c log n, let C_r be the correlation on a<n<=b-r and take C_r=0 when this interval is empty. The exact zero-extension Cauchy identity gives

|S_f(a,b-a)|² <=(b-a+q-1)[(b-a)/q+(2/q) Re sum_(1<=r<q)(1-r/q) C_r]. (3)

We do NOT replace the last sum by the sum of its individual absolute values. This retained cancellation is where the new two-dimensional input enters. After division by a, the right side is at most

2a/q+(4/q)|sum_(1<=r<q)(1-r/q) C_r|.                              (4)

The correlation phase is g_r(y)=-c log(1+r/y). Its derivative decreases; its stationary interval is

alpha_r=cr/[b(b-r)] < nu <= beta_r=cr/[a(a+r)].

The exact dual phase and weight are

phi(r,nu)=rnu/2-2c[asinh z+z sqrt(1+z²)], z=sqrt(rnu/(4c)),
w(r,nu)=(cr)^(1/4)/(sqrt2 nu^(3/4)) (1+rnu/(4c))^(-1/4).           (5)

Patel–Yang Lemma2.3 yields the complete main sum of w e(phi-1/8). Using its Section3.0.2 bounds at h=2, we retain the following error for every r:

E(r)<=E4 a^(3/2)t^(-1/2)r^(-1/2)
       +E5 a^(-1/3)t^(1/3)r^(1/3)
       +6+(5/pi)log(2+tr/(pi a²)),                               (6)

where E4=5.686 sqrt(pi) 2^(3/2)<30 and E5=48/pi<16. The primary coefficient is4.686; the extra one maximum stationary weight is reserved for the lattice-count endpoint in the small-r range below. Thus it is not used twice. No first dual endpoint is removed in the good two-dimensional range, where its original half-open convention is retained.

## 3. Uniform good-range scale guards

Partition 1<=r<q into the integer dyadic intervals R<=r<2R, truncating by r<q and r<b-a when necessary. Define

R0=64 a^(3/4)c^(-1/4).

Call a dyadic block good when R>=R0. Cover its entire dual interval by the three adjacent half-open bins [N,2N] with

N=alpha cR/a², alpha in{1/4,1/2,1}.

Indeed cr/(4a²)<=alpha_r<beta_r<=cr/a² and R<=r<2R. Put M=R and F=2sqrt(cRN). The phase is defined analytically on the enlarged rectangles even where a cutoff makes the original sum empty.

Here are all hypotheses of the local mixed-A theorem, uniformly on every good bin. First, N>=R/4 and R>=64t^(1/14), so M,N>=2. Also F>=max(M,N), since a<=sqrt(c). Direct substitution gives

kappa_x^11=alpha^(3/2)cR^4/(2a³)>=2^20,
kappa_y^11=alpha^(5/2)c²R^4/(2a^5)>=2^18.                          (7)

Both kappas therefore exceed2. Since c>=a², their fourth powers are at most c^(8/11)R^(16/11)a^(-20/11). Consequently

2 max(kappa_x^4,kappa_y^4)/min(M,N)
 <=8 t^(-1/203)<=s=10^(-12).                                    (8)

The last inequality is certified at x0 and decreases thereafter. For the inverse row, exact substitution and c>=a² show

F^8/max(M^13N^5,N^13M^5)
 >=256 c^(-5)a^18 R^(-10)
 >=256 t^(341/203)>2^40.                                         (9)

Finally

(2+s)^2 MN/(4c)<=(2+s)^2 t^(-132/203)/4<=10^(-30).                      (10)

Thus the actual order-nine derivative appendix and BOTH mixed-coordinate words apply. These are pointwise uniform guards, not average-shift conditions. Write L=log(2+10^12 F). The certificate also proves

L<=x, log(4N)<=x                                                   (11)

throughout this range. These follow from F<=t^(137/203) and N<=t^(50/203); the fixed additive constants are explicitly paid at x0.

## 4. Curved boundaries and the complete good-range sum

On each bin, alpha_r and beta_r are increasing functions of r. Split the r interval at their crossings with N and2N. There are at most five pieces. On each piece, a nonconstant boundary lies in[N,2N], while an inactive boundary gives a full or empty piece. Therefore the cutoff appendix applies with L0=1. Its two-boundary estimate, including strict/inclusive equality errors, gives at most

40 log(4N) B_rect+640R

after all five pieces, where

B_rect=10^6 sqrt(L) F^(1/22)R^(10/11)N^(19/22).

This uses the TRANSPOSED mixed word in the local appendix, before taking its geometric mean. Its explicit coefficient is at most80 C^(1/8)<10^6. Retaining the anisotropic powers, rather than the balanced geometric mean, is essential for the final positive original-block power.

The triangular weight 1-r/q and stationary weight in(5) have the full two-variable Abel norm at most5 sup w, with

sup w<=c^(1/4)R^(1/4)N^(-3/4).

Uniformity on all subrectangles is retained before applying Abel summation. In particular no derivative of a sharp cutoff is assigned a fictitious small total variation. The curved sum on one bin is bounded by

200*10^6 log(4N)sqrt(L) 2^(1/22) alpha^(3/22)
   c^(9/22)R^(29/22)a^(-3/11)
 +3200 alpha^(-3/4)c^(-1/2)a^(3/2)R^(1/2).                        (12)

Summing the three bins and the complete dyadic R series, using (11), gives the safe complete bound

G_good<=2*10^9 x^(3/2)t^(9/22)a^(-3/11)q^(29/22)
          +3*10^5 t^(-1/2)a^(3/2)q^(1/2).                        (13)

The checker explicitly verifies the coefficients before rounding: the geometric denominators are 1-2^(-29/22) and1-2^(-1/2). The second row is the retained curved-cutoff lattice debit. It is not absorbed by an unjustified strip-area estimate.

## 5. Every complementary range and first-Poisson error

Every bad dyadic block has R<R0 and hence all its labels have r<2R0. The first dual interval has length at most2cr/a² and maximum weight at most2a^(3/2)/(sqrt(c r)). After the one-point lattice debit already reserved in E4, its trivial main row is at most

4sqrt(c)a^(-1/2)sqrt(r).

Therefore, without assuming R0<q, the sum over all bad labels is at most

4sqrt(c)a^(-1/2)(2R0)^(3/2)<6000 t^(1/8)a^(5/8).                  (14)

This covers all small kappas, small dual scales and all labels where the new two-dimensional lemma is not invoked. There are no other failure ranges: (7)-(10) hold for every good block.

Sum (6) over every 1<=r<q, with the triangular weights bounded by1. Use sum r^(-1/2)<=2sqrt(q), sum r^(1/3)<=q^(4/3), and the full logarithmic bound in(6)<=10x. Define the positive block scale

T_a=a^(1/29)t^(9/29)x^(33/29).

The diagonal and main row of (4), (13) are at most

[4/gamma+8*10^9 gamma^(7/22)] T_a.                                (15)

The small-r row (14), divided by T_a, is at most

(48000/gamma)t^(-1/28).

For the full cutoff-lattice and first-Poisson endpoint rows, (2) and a<=sqrt(t) give the normalized upper bound

(2*10^6/sqrt(gamma)) x^(-33/58)t^(-theta).

The first-Poisson derivative row is at most64 gamma^(1/3)t^(20/87)a^(-1/87)x^(-11/29). After division by T_a and use of a>=t^(3/7), it is at most

64 gamma^(1/3)x^(-44/29)t^(-61/609).

Finally the full first-Poisson logarithm gives the normalized row

40 x^(-4/29)t^(-66/203).

Every correction is decreasing for x>=x0. The complete sum at x0, including the exact coefficient in(15), is less than10^8. Thus every large weighted block is at most

10^4 a^(1/58)t^(9/58)x^(33/58).                                  (16)

Now retain the positive a power. The complete dyadic sum, including a shortened top block, satisfies

sum a^(1/58)<=c^(1/116)/(1-2^(-1/58)).

Consequently the entire large range is at most

[10^4 (2pi)^(-1/116)/(1-2^(-1/58))] x^(33/58)t^theta.              (17)

This replaces the cruder height-proportional count of large blocks. No geometric endpoint or positive block power is discarded.

## 6. Initial/middle sums and both infinite-height splices

The initial sum is at most2sqrt(B)<=2sqrt2 t^theta. On each middle block a<n<=2a, use the published fourth-derivative test with eta=1, H=16 and lambda=3t/(16pi a^4). Its monotone derivative and integer-endpoint hypotheses hold exactly. After partial summation by n^(-1/2), the two rows are

D1 t^(1/14)a^(3/14)+D2 t^(-1/14)a^(15/28),
D1=(3/pi)^(1/14) A4(1,16) 2^(5/7),
D2=(pi/3)^(1/14) B4(1) 2^(2/7).

The complete positive dyadic sums up to A<2t^(3/7) are bounded by

D1*2^(3/14)/(2^(3/14)-1) t^(8/49)
 +D2*2^(15/28)/(2^(15/28)-1) t^(31/196).                            (18)

Both exponents are below theta. The checker includes the complete source recurrence defining A4,B4 and verifies the resulting normalized tail at x0; both rows decrease thereafter.

The full Riemann–Siegel estimate, including both halves and its remainder, now gives

|zeta(1/2+it)|<=2(initial+middle+large)
                  +1.48t^(-1/4)+.127t^(-3/4).

Equations(17)-(18) and the directed scalar check prove(1) for x>=10000. No finite-height sampling is used for this infinite tail.

For 3<=t<=exp(10000), the accepted 110t^(229/1392) theorem applies. Since

229/1392-theta=1/1392,
110 exp(10000/1392)<10^7, and log t>1,

it implies(1) throughout this entire lower interval. Thus the two covers overlap without any change in the valid |t|>=3 domain.

For a concrete comparison, the certificate proves that(1) is smaller than110t^(229/1392) whenever log t>=25000. The ratio is decreasing there because33/(58x)<1/1392. This comparison concerns function upper bounds only.

## 7. Reproduction and scope

Run certify_mixed_derivative_constants.py (exact rational arithmetic), then certify_anisotropic_mixed_bound.py with python-flint0.9.0 / FLINT3.6.0. The latter uses192-bit outward arithmetic and exact rational height exponents. It checks all scale guards, constants, complete tail monotonicities, partitions, low-height splice and stated comparison. The analytical argument is the full text plus its three appendices, not the numerical PASS alone.

No new zero-free region, RH assertion, proportion-of-zeros improvement, or unrestricted asymptotic record follows from this report. The minimum envelope should be retained because the new explicit coefficient is deliberately large.

## Primary sources

1. D. Patel and A. Yang, *An explicit sub-Weyl bound for zeta(1/2+it)*, Journal of Number Theory262(2024),301–334, https://doi.org/10.1016/j.jnt.2024.03.011 ; readable version https://arxiv.org/html/2302.13444v1 . Used here: the explicit derivative-test recurrence in Section1.2, complete Poisson Lemma2.3, and the raw logarithmic-correlation errors of Section3.0.2. Its Section4 identifies19/116 as a classical higher-dimensional exponent.
2. G. A. Hiary, D. Patel and A. Yang, *An improved explicit estimate for zeta(1/2+it)*, https://arxiv.org/html/2207.02366v1 , for the Riemann–Siegel setup and complete remainder, as reproduced in the accepted dependency.
3. The fully proved accepted 110t^(229/1392) dependency linked in Section1, used solely for the lower-height splice.
