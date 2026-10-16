# Two additional partial dual transforms: an explicit 155/948 bound

Status: complete proof and code have passed independent internal analytic/source review and separate-copy certificate replay. This is not external peer review.

## 1. Statement and exact dependencies

The bound is

|zeta(1/2+it)|<=2*10^12 |t|^(155/948)(log|t|)^(89/158), |t|>=3.       (1)

Retain the minimum with the published [10^23 |t|^(53/324)(log|t|)^(25/54)](../20261016_partial_dual_subweyl_53_324/REPORT.md) and its predecessors. The exponent difference from that bound is1/12798, and from the published19/116 bound it is2/6873. This report makes no unrestricted exponent-record, exhaustive priority, zero-free-region, zero-count or RH claim. The large coefficient makes the comparison relevant only at extremely large heights.

The new analytic inputs are the complete [two-partial-dual local lemma](DOUBLE_PARTIAL_DUAL_LEMMA.md) and [actual C13/common-length outer assembly](ACTUAL_DOUBLE_OUTER.md). Both bounded-frequency boundaries, the capped-inner-length inverse cost, short dual ranges and all endpoint errors are explicit there.

The prior [19/116 report](../20261016_mixed_coordinate_subweyl_19_116/REPORT.md) supplies the proved rectangular second-derivative lemma, original cutoff/amplitude identities and, crucially, its LOCAL weighted-block estimate (16). That local estimate is not inferred from its global zeta theorem. It supplies a finite scale bridge below the new large-block threshold. The published19/116 global theorem also supplies the lower-height splice; the53/324 theorem is retained only as an optional comparator, not as a necessary input. No unpublished result is a dependency.

Put e(u)=exp(2pi i u), x=log t,c=t/(2pi), theta=155/948,p=2theta, pa=12/25, gamma=10^(-12). By conjugation it suffices to prove t>0. First assume x>=x0=10000.

## 2. Original partition and retained signed correlation

Let B,A0,A be the least integral powers of2 not smaller than t^p,t^(3/7),t^pa respectively. The directed checker verifies B<=A0<=A<sqrt(c). Partition the Riemann--Siegel sum into n<=B, middle dyadic blocks from B to A0, bridge blocks from A0 to A, and large blocks from A to floor sqrt(c). Shorten only the final block. There are no omitted transition intervals.

On every large block a<n<=b<=2a, including every integer partial endpoint b, set

q=floor(gamma a^(76/79)t^(-73/237)x^(-89/79)).                    (2)

The uniform floor/range inequalities are

q>=gamma a^(76/79)t^(-73/237)x^(-89/79)/2,
q_unfloored>=gamma t^(911/5925)x^(-89/79)>2,
q/a<=t^(-1933/5925)<1.                                          (3)

The lower expression increases above x0.

For f(n)=-c log n the exact zero-extension A identity gives, after division by a,

|S_f(a,b-a)|^2/a <=2a/q+(4/q)|sum_(1<=r<q)(1-r/q) C_r|.          (4)

The correlation is zero if its interval is empty; otherwise it runs only where both y and y+r lie in the original block. We retain this signed sum before the multidimensional bound, not the sum of the absolute values of its individual correlations.

The first Poisson transform of g_r(y)=-c log(1+r/y) has stationary endpoints

alpha_r=cr/[b(b-r)] < nu <= beta_r=cr/[a(a+r)],

phase and weight

phi(r,nu)=rnu/2-2c[asinh z+z sqrt(1+z^2)], z=sqrt(rnu/(4c)),
w=(cr)^(1/4)/(sqrt2 nu^(3/4))(1+rnu/(4c))^(-1/4).

We use the full source error, unchanged from the accepted predecessor:

E(r)<=E4 a^(3/2)t^(-1/2)r^(-1/2)
       +E5 a^(-1/3)t^(1/3)r^(1/3)
       +6+(5/pi)log(2+tr/(pi a^2)),                              (5)

E4=5.686 sqrt(pi)2^(3/2)<30, E5=48/pi<16. The primary4.686 has one additional maximum stationary weight reserved for the bad-r endpoint count. This is not charged twice. The good-range main sum retains the exact half-open endpoints.

## 3. Every good-range hypothesis

Partition r into dyadic intervals R<=r<2R, truncated by r<q and the correlation support. Put

R0=64 a^(13/10)c^(-8/15).

A bin is good if R>=R0. Cover its complete stationary nu range with three adjacent bins N=alpha cR/a^2, alpha in{1/4,1/2,1}, nu in[N,2N]. Put M=R,F=2sqrt(cRN).

Since a<=sqrt(c), N>=R/4. Also R>=64t^(34/375), so both dimensions are at least2. The common outer parameter obeys

kappa^89=alpha^(39/2)c^16R^30/(2^7a^39)>=2^134,                 (6)

and therefore kappa>2. Its total-shift guard follows from

2kappa^4/min(M,N)
 <=8 c^(64/89)R^(31/89)a^(-156/89)
 <=8 t^(145/237)a^(-112/79)
 <=8t^(-407/5925)<10^(-30).                                     (7)

The enlarged actual-series guard, including X up to32 and Y up to8, is

(32+s)(8+s)MN/(4c)<=100(R/a)^2
 <=100t^(-3866/5925)<10^(-80).                                  (8)

All bounds are certified at x0 and improve thereafter. Thus every terminal finite difference satisfies the complete C10 input of the new local lemma, using the original phase through order13. Both later cutoff frequencies are separately accounted for by that lemma; the original arbitrary-frequency boundary twist is annihilated by the three outer mixed differences.

The complete logarithmic ranges are

L=log(2+FMN)<=2x, log(4N)<=x.                                   (9)

For example FMN<=2t^(85/79)a^(-9/79), and N<=t^(164/237)a^(-82/79). The checker substitutes the lower a endpoint and verifies(9), rather than discarding the factors2 and4.

The threshold pa=12/25 is substantive. The new by row has a negative a exponent after normalization, and would grow at a=t^.44. Its worst exponent at the actual chosen lower endpoint is -71/189600. The explicit bridge in section7 pays the higher threshold instead of silently reusing the old middle range.

## 4. The original curved cutoffs and all eleven rows

For each good rectangle apply the proved original finite Fejer cutoff to both original boundaries, retaining all five monotone pieces, all boundary equalities, and the full Abel norm of (1-r/q)w. These unchanged identities give, for an unweighted rectangular bound B,

40log(4N)B+640R,

and amplitude Abel norm at most5 sup w. They are the original frequency-uniform cutoffs, not the bounded-frequency cutoffs used inside the new local theorem.

For each output row F^k M^l N^m in the actual-outer appendix, the weighted powers are

u=k+m-1/2,
v=k+l+m-1/2,
w_a=3/2-k-2m.                                                   (10)

Its coefficient on a bin is at most200*10^16 log(4N)sqrt(L)2^k alpha^(k/2+m-3/4)c^uR^v a^w_a. Every alpha exponent is positive, every u>0 and every v>1. The full geometric sum over R and all three alpha bins gives coefficient less than10^20 after using(9). Thus

G_good<=10^20 x^(3/2) sum_rows t^u a^w_a q^v
          +3*10^5 t^(-1/2)a^(3/2)q^(1/2).                        (11)

The last row is the full original-cutoff lattice debit. It is not absorbed into a phase-scale assumption.

## 5. All bad labels and first-Poisson errors

If R<R0, every label in its bin has r<2R0, including when R0>=q. After the once-reserved endpoint in(5), the trivial first-dual main row is at most4sqrt(c)a^(-1/2)sqrt(r). Therefore

G_bad<=4sqrt(c)a^(-1/2)(2R0)^(3/2)
       <20000 t^(-3/10)a^(29/20).                               (12)

This pays every label for which any outer good-range hypothesis is not used. There is no uncovered short first-dual range.

Sum(5) over all labels, using sum r^(-1/2)<=2sqrt(q), sum r^(1/3)<=q^(4/3), and its logarithmic row<=10x. The first-Poisson endpoint row combines with the last row of(11), with total normalized coefficient less than3*10^6. Both derivative and full logarithmic errors remain in section6.

## 6. Complete large-block normalization

Define

T_a=a^(3/79)t^(73/237)x^(89/79).

For a good row(10), write

A=u-(73/237)v,
B=w_a-1+(76/79)v,
C=3/2-(89/79)v,
Z=A+B/2 if B>=0, and Z=A+(12/25)B if B<0.                       (13)

Using(2)--(4), its normalized contribution is at most

8*10^20 gamma^(v-1)x^C t^Z.                                     (14)

The main row has A=B=C=Z=0. For the other ten rows the complete worst height powers Z, in the order of the appendix, are

bx:-11/7584;
by:-71/189600;
inverse2:-379/189600;
cap:-841/189600;
short:-5/3792;
constant:-23/1896;
derivative2:-199/56880;
log2:-481/31600;
inverse1:-659/94800;
derivative1:-1/5688.

Their logarithmic powers C, which can be positive, are retained exactly in the checker and scientific ledger. In every case Z+C/x0<0, so the whole function decreases above x0. Negative original-block powers are evaluated at the LOWER a endpoint in(13).

The other normalized rows are exactly bounded by

4/gamma,
(160000/gamma)t^(-3/40),
(3*10^6/sqrt(gamma))x^(-89/158)t^(-theta),
64gamma^(1/3)x^(-356/237)t^[1/3-292/711-(12/25)(4/79)],
40x^(-10/79)t^(-1933/5925).                                     (15)

These are respectively the original diagonal, bad labels, combined cutoff/endpoint, first-Poisson derivative, and first-Poisson logarithm. Every nonconstant row decreases. The directed finite sum of(14)--(15) at x0 is below10^20. Hence every large weighted block, uniformly in its final integer endpoint, is at most

10^10 a^(3/158)t^(73/474)x^(89/158).                             (16)

Retaining its positive a power, the entire dyadic large-block sum is at most

10^10 (2pi)^(-3/316)/(1-2^(-3/158))
       *t^theta x^(89/158),                                    (17)

because73/474+3/316=155/948. No height-proportional count replaces this geometric sum.

## 7. Initial, middle and the necessary local bridge

The initial sum is at most2sqrt(B)<=2sqrt2 t^theta. On the middle blocks from B to A0 use the same explicit fourth-derivative test as the accepted report, with eta=1,H=16 and lambda=3t/(16pi a^4). After partial summation its rows are

D1t^(1/14)a^(3/14)+D2t^(-1/14)a^(15/28),
D1=(3/pi)^(1/14)A4*2^(5/7), D2=(pi/3)^(1/14)B4*2^(2/7).

The exact source recurrence for A4,B4 is reproduced in the checker. Since a<A0<2t^(3/7), both complete geometric sums have exponent strictly below theta; the first is8/49. These full sums, with the factor2 endpoint excess, are included.

For each bridge block A0<=a<A, use the PUBLISHED LOCAL estimate (16) of the19/116 report:

10^4 a^(1/58)t^(9/58)x^(33/58),
valid for every a>=t^(3/7), x>=10000 and every partial endpoint.

Our x>=10000 satisfies that entire domain. The geometric bridge sum is at most

10^4*2^(1/58)/(1-2^(-1/58))
   *t^[9/58+(12/25)/58]x^(33/58).                               (18)

Its height exponent is strictly below155/948. Its logarithmic excess33/58-89/158 is retained; the normalized function decreases at and above x0. This step uses an actual local block theorem with all its original errors, not an inference from a bound on the completed zeta sum.

The Riemann--Siegel formula contributes twice the complete sum, plus1.48t^(-1/4)+.127t^(-3/4). Combining every displayed contribution, the normalized infinite-tail coefficient is below1.504*10^12, in particular below2*10^12. All monotonicity assertions are directed checks of the full expressions.

## 8. Entire lower interval and comparison

For3<=t<=exp(x0), use the published19/116 theorem. The exact differences are

19/116-155/948=2/6873,
33/58-89/158=13/2291.

Both differences are positive. Therefore the entire lower-interval ratio to t^theta(log t)^(89/158) is increasing in t and is at most

10^7 exp(20000/6873)10000^(13/2291)
 <1.935*10^8<2*10^12.                                           (19)

This pays the entire lower interval without a circular use of(1). Conjugation gives negative t.

At log|t|=50000, the ratio of the new bound to the preceding19/116 bound is below.090265, and its logarithmic derivative is negative thereafter. This is a comparison of two function upper bounds, not a proportion of zeros removed. The53/324 bound is not needed to obtain the new coefficient.

## Reproducibility

Run the three certificate scripts in this directory using python-flint0.9.0 / FLINT3.6.0. certify_double_inverse_jets.py checks the local stationary derivative data. certify_double_outer.py checks the actual order13 box and all eleven common-length exponents. certify_global_double.py retains the full rational normalized ledger, every sign-dependent endpoint, source derivative constants, original diagonal/boundary/Poisson rows, geometric sums, both height splices and the stated comparison.

The complete written proof and all code have passed the independent internal analytic/source review recorded in INDEPENDENT_REVIEW.md. The scientific JSON files record finite rigorous expressions, not sampled-height evidence or a replacement for those analytic obligations.
