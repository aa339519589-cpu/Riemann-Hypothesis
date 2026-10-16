# An explicit additional partial-dual bound with exponent 53/324

Status: complete proof with independent internal analytic, source and code review, and separate directed-arithmetic replays. This is not external peer review or formal kernel verification.

## 1. Statement and complete dependencies

The theorem is

|zeta(1/2+it)|<=10^23 |t|^(53/324)(log|t|)^(25/54), |t|>=3.        (1)

Retain the minimum with all prior bounds, in particular the accepted
[10^7 |t|^(19/116)(log|t|)^(33/58)](../20261016_mixed_coordinate_subweyl_19_116/REPORT.md).
The new exponent is smaller by1/4698, but is not asserted to be a new unrestricted asymptotic exponent record. No zero-free region, zero count, RH conclusion or exhaustive priority claim is made.

This proof includes two new local appendices:

- [Partial dual transform and bounded-frequency boundary payment](PARTIAL_DUAL_LEMMA.md), including its complete negative-phase Poisson convention, interval implicit jets, full stationary amplitude, all new boundary errors and complementary parameter ranges;
- [Actual order-eleven comparison and common-length outer assembly](ACTUAL_OUTER_ASSEMBLY.md), retaining all five propagated error rows.

We also use the fully proved [rectangular second-derivative lemma](../20261016_mixed_coordinate_subweyl_19_116/SECOND_DERIVATIVE_LEMMA.md) and [inclusive mixed-A, original curved-cutoff and amplitude identities](../20261016_mixed_coordinate_subweyl_19_116/MIXED_A_AND_CUTOFF.md) from the accepted dependency. These are explicit scientific inputs, not implicit multidimensional estimates. The earlier global bound is used only for the lower-height splice. The entire new global assembly is given here, with no dependency on an unpublished transfer.

Put e(u)=exp(2pi i u), x=log t, c=t/(2pi), theta=53/324, p=2theta=53/162, a0=43/100, gamma=10^(-8), and s=10^(-16). By conjugation it suffices to treat t>0. First suppose x>=x0=160000.

## 2. Original integer partition and signed first correlation

Let A be the least integral power of2 not smaller than t^a0, and B the least integral power of2 not smaller than t^p. The certificate proves

B<=A<sqrt(c), t^p<=B<2t^p, t^a0<=A<2t^a0.

Partition the Riemann--Siegel sum into n<=B, the integer dyadic middle blocks from B to A, and the large blocks from A to floor sqrt(c), shortening only the last block. Every large block is a<n<=b<=2a, with integer endpoints, and

t^a0<=a<=sqrt(c).

For every integer partial endpoint b, choose

q=floor(gamma a^(26/27)t^(-25/81)x^(-25/27)).                      (2)

The complete floor bounds are

q>=gamma a^(26/27)t^(-25/81)x^(-25/27)/2,
q_unfloored>=gamma t^(427/4050)x^(-25/27)>2,
q/a<=t^(-2629/8100)<1.                                          (3)

The lower expression is increasing above x0. These estimates are uniform over all shortened endpoints.

For f(n)=-c log n and C_r=sum_(a<n<=b-r)e(f(n+r)-f(n)), set C_r=0 if the interval is empty. Zero-extension Cauchy before taking absolute values gives

|S_f(a,b-a)|² <=(b-a+q-1)[(b-a)/q
                    +(2/q)Re sum_(1<=r<q)(1-r/q)C_r].            (4)

We retain this signed sum of correlations until its two-dimensional treatment. Partial summation by n^(-1/2), using the uniform partial-endpoint bound, reduces the squared weighted block to

2a/q+(4/q)|sum_(1<=r<q)(1-r/q)C_r|.                             (5)

For the first correlation g_r(y)=-c log(1+r/y), both y and y+r stay in the original block. The stationary frequency interval is

alpha_r=cr/[b(b-r)]<nu<=beta_r=cr/[a(a+r)].

Its exact first-dual phase and amplitude are

phi(r,nu)=rnu/2-2c[asinh z+z sqrt(1+z²)], z=sqrt(rnu/(4c)),
w(r,nu)=(cr)^(1/4)/(sqrt2 nu^(3/4))(1+rnu/(4c))^(-1/4).           (6)

Patel--Yang's complete Poisson formula gives its main sum w e(phi-1/8), with all endpoint conventions retained. Its error for each r is bounded by

E(r)<=E4 a^(3/2)t^(-1/2)r^(-1/2)
       +E5 a^(-1/3)t^(1/3)r^(1/3)
       +6+(5/pi)log(2+tr/(pi a²)),                               (7)

where E4=5.686 sqrt(pi)2^(3/2)<30 and E5=48/pi<16. The source coefficient4.686 has been increased by one maximum stationary weight, reserved once for the lattice endpoint in the bad-r range below. No extra endpoint is removed in the good range.

## 3. Uniform good-range hypotheses

Partition r into integer dyadic intervals R<=r<2R, truncated by r<q and r<b-a. Define

R0=64 a^(4/3)c^(-5/9).

Call a block good if R>=R0. Cover its entire stationary interval by three adjacent half-open bins [N,2N], where

N=alpha cR/a², alpha in{1/4,1/2,1}.

This follows from cr/(4a²)<=alpha_r<beta_r<=cr/a². Put M=R and F=2sqrt(cRN). All phase formulas extend to the enlarged positive rectangles needed in the local appendices.

First, N>=R/4 and R>=64t^(4/225), so M,N>=2. The common outer length parameter satisfies

kappa^30=M^4N^7/F²=alpha^6 c^5 R^9/(4a^12)>=2^40,

hence kappa>2. Moreover

2kappa^4/min(M,N)
 <=8c^(2/3)R^(1/5)a^(-8/5)
 <=8t^(49/81)a^(-38/27)
 <=8t^(-1/4050)<=s.                                             (8)

This is why the new large-block threshold is43/100, not the older3/7. The latter would give a growing shift guard and is not reused.

On the actual extended domain the series condition is

(3+s)(4+s)MN/(4c)
 <=4(R/a)²<=4t^(-2629/4050)<=10^(-40).                           (9)

Thus the order-eleven appendix verifies every C8 relative-monomial hypothesis of the new partial-dual lemma after every outer finite difference. Both small-F3 and all partial-dual failure ranges are already paid in those appendices.

The complete logarithmic scales satisfy

log(2+FMN)<=2x, log(4N)<=x.                                     (10)

For example FMN<=2t^(2771/2700) and N<=t^(497/2025); the certificate pays the fixed additive constants at x0. Every bound in(3), (8)--(10) improves thereafter.

## 4. Original curved cutoffs and all five good-range rows

The original alpha_r,beta_r increase with r. Splitting at their crossings with N and2N gives at most five pieces. The already proved arbitrary-frequency first-cutoff lemma gives, with every strict/inclusive equality retained,

40log(4N) B_rect+640R

on each bin after summing all pieces. Its Fourier twists are exactly separable and vanish under the OUTER mixed three differences. This does not assert that the single INNER difference kills the later partial-B cutoff; that separate bounded-frequency payment is retained in the new local lemma.

By the outer appendix,

B_rect<=10^7 [log(2+FMN)]^(1/4)
                 sum_j F^(k_j) R^(l_j) N^(m_j),

where the five triples are

main: (1/30,14/15,53/60),
boundary: (0,1,15/16),
endpoint: (-1/30,241/240,491/480),
derivative: (1/45,359/360,619/720),
constant: (0,1,7/8).

The complete two-variable Abel norm of (1-r/q)w is at most5 sup w, with sup w<=c^(1/4)R^(1/4)N^(-3/4). Thus each monomial becomes

2^k alpha^(k/2+m-3/4) c^u R^v a^w,
u=k+m-1/2, v=k+l+m-1/2, w=3/2-k-2m.

Every alpha exponent is positive and every v>1. Summing all three bins and all dyadic R, including the shortened last one, and using(10), gives

G_good<=10^11 x^(5/4) sum_j t^(u_j)a^(w_j)q^(v_j)
              +3*10^5 t^(-1/2)a^(3/2)q^(1/2),                  (11)

with the complete rows

main: u=5/12, v=27/20, w=-3/10;
boundary: u=7/16, v=23/16, w=-3/8;
endpoint: u=47/96, v=239/160, w=-41/80;
derivative: u=55/144, v=331/240, w=-29/120;
constant: u=3/8, v=11/8, w=-1/4.

The checker verifies each unrounded coefficient using the geometric denominator1-2^(-v). The last row of(11) is the full first-curved-cutoff lattice debit, not a strip-area replacement.

## 5. All complementary labels and complete original-block ledger

Every bad dyadic block has r<2R0. The first-dual interval has length at most2cr/a² and maximum weight at most2a^(3/2)/sqrt(cr). After the once-reserved lattice endpoint in(7), its trivial main row is at most4sqrt(c)a^(-1/2)sqrt(r). Therefore, without assuming R0<q,

G_bad<=4sqrt(c)a^(-1/2)(2R0)^(3/2)
          <20000 t^(-1/3)a^(3/2).                              (12)

This covers every small kappa and small original dual scale. No other outer failure range remains, since(8)--(9) hold uniformly on every good block.

Set T_a=a^(1/27)t^(25/81)x^(25/27). Insert(7), (11), (12) into(5), using(3). For each good row define

A_j=u_j-(25/81)v_j,
B_j=w_j-1+(26/27)v_j,
C_j=5/4-(25/27)v_j.

Its normalized contribution is at most

8*10^11 gamma^(v_j-1) t^(A_j)a^(B_j)x^(C_j).

The exact pairs (worst t exponent, C_j), using a<=sqrt(t) when B_j>=0 and a>=t^(43/100) when B_j<0, are

main: (0,0);
boundary: (-1/648,-35/432);
endpoint: (-107/32400,-115/864);
derivative: (-1/1944,-35/1296);
constant: (-1/81,-5/216).                                       (13)

In particular the negative a power in the endpoint row is evaluated at the LOWER block threshold, not at sqrt(t).

The remaining normalized rows are, respectively,

4/gamma,
(160000/gamma)t^(-1/12),
(3*10^6/sqrt(gamma))x^(-25/54)t^(-theta),
64gamma^(1/3)x^(-100/81)t^(-604/6075),
40x^(2/27)t^(-2629/8100).                                      (14)

These are the diagonal, small-r row, combined cutoff/first-Poisson endpoint row, first-Poisson derivative row, and full first-Poisson logarithm. We used sum r^(-1/2)<=2sqrt(q), sum r^(1/3)<=q^(4/3) and the complete logarithm in(7)<=10x. The last row is decreasing above x0 because (2/27)/x<2629/8100; every other correction is plainly decreasing.

The directed certificate sums ALL rows(13)--(14) at x0 and proves the result below10^10. Thus every large weighted original block is at most

10^5 a^(1/54)t^(25/162)x^(25/54).

The positive original-block power is retained in the complete geometric sum:

sum a^(1/54)<=c^(1/108)/(1-2^(-1/54)).

Since25/162+1/108=theta, the entire large range is bounded by

[10^5(2pi)^(-1/108)/(1-2^(-1/54))] t^theta x^(25/54).              (15)

## 6. Initial/middle ranges, full remainder and lower splice

The initial sum is at most2sqrt2 t^theta. On every middle block use the published fourth-derivative test with eta=1, H=16 and lambda=3t/(16pi a^4). All integer endpoints and derivative monotonicity hypotheses hold. After partial summation its two rows are

D1 t^(1/14)a^(3/14)+D2 t^(-1/14)a^(15/28),
D1=(3/pi)^(1/14)A4(1,16)2^(5/7),
D2=(pi/3)^(1/14)B4(1)2^(2/7).

The complete dyadic sums ending below A<2t^(43/100) give height powers

1/14+(43/100)(3/14)=229/1400<theta,
-1/14+(43/100)(15/28)<theta.

The first gap is only1/113400 and is retained exactly. The checker includes the complete explicit recurrence for A4,B4 and both full geometric coefficients.

The Riemann--Siegel estimate is

|zeta(1/2+it)|<=2(initial+middle+large)
                    +1.48t^(-1/4)+.127t^(-3/4).

The directed complete infinite-tail coefficient at x0 is below15416724, hence below10^23. Every normalized remainder decreases, so this proves(1) for all x>=x0, not just sampled heights.

For 3<=t<=exp(x0), use the accepted19/116 theorem. Since

19/116-theta=1/4698,
33/58-25/54=83/783>0,

its ratio to t^theta x^(25/54) is at most

10^7 exp(x0/4698) x0^(83/783)<10^23.

This increasing envelope pays the WHOLE lower interval, since log3>1. There is no circular use of the new bound in its own rectangle or splice. Conjugation pays negative heights.

The certificate also checks that(1) is smaller than the accepted19/116 bound for log|t|>=250000. Their ratio is then strictly decreasing. This is a comparison of function estimates only.

## 7. Reproduction and scope

Run certify_partial_dual_jets.py, certify_outer_assembly.py and certify_global_partial_dual.py with python-flint0.9.0 / FLINT3.6.0. The finite inverse calculations and global scalar enclosures use192-bit outward arithmetic; all exponents are exact rational numbers. The complete proofs, not numerical PASS alone, must pass independent review before acceptance.

The retained minimum remains necessary: the coefficient10^23 is deliberately large, and the improvement applies only at very large heights. This result does not establish an unrestricted exponent record or any new proportion of zeros.

Primary sources: Patel--Yang, An explicit sub-Weyl bound for zeta(1/2+it), arXiv2302.13444v1, Section1.2, Poisson Lemma2.3 and raw Section3.0.2 errors; Hiary--Patel--Yang, An improved explicit estimate for zeta(1/2+it), arXiv2207.02366v1, for the full Riemann--Siegel remainder, as retained in the accepted dependency. All new multidimensional inputs are proved in the linked accepted appendices and the two new appendices here.
