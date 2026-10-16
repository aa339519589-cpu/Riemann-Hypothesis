# Two partial dual transforms with both curved-boundary debits

Status: complete local proof and certificate have passed independent internal review. Its global zeta consequence additionally uses ACTUAL_DOUBLE_OUTER.md and REPORT.md; the finite jet output alone does not prove it.

## 1. Local statement

Let M,N>=2 and F>=1. Let f be real and C^10 on

[M/16,32M] x [N/4,8N].

Set X=x/M, Y=y/N and f0=(F/8)X^(-1/2)Y^(-3/2). Suppose, for every i+j<=10 on this enlarged rectangle,

|partial_x^i partial_y^j f / partial_x^i partial_y^j f0 -1|<=10^(-25). (1)

All denominators are nonzero. Put L=log(2+FMN). Uniformly for every subrectangle of [M,2M]x[N,2N], the bound is

|sum e(f(m,n))| <=10^100 L^4 times the sum of the following eleven rows:

F^(7/10) M^(3/10) N^(1/10),
F^(3/4) M^(1/4),
F^(3/4) N^(1/4),
F^(4/5) M^(-1/20) N^(3/20),
F^(7/8) M^(-1/8),
M sqrt(N),
M,
F^(5/6),
sqrt(F),
MN/sqrt(F),
M F^(1/3).                                                        (2)

Here e(u)=exp(2pi i u). In particular the capped-inner-length inverse row F^(7/8)M^(-1/8) and the short-first-dual row M sqrt(N) are retained. No extra inverse-range hypothesis is imposed to delete either row.

The inputs are the explicit [rectangular second-derivative lemma](../20261016_mixed_coordinate_subweyl_19_116/SECOND_DERIVATIVE_LEMMA.md), the elementary inclusive-lattice A and finite Fejer identities from its [companion appendix](../20261016_mixed_coordinate_subweyl_19_116/MIXED_A_AND_CUTOFF.md), and the complete decreasing-derivative Poisson Lemma 2.3 in [Patel--Yang, arXiv2302.13444v1](https://arxiv.org/html/2302.13444v1). All new transformations and their range complements are given below.

## 2. First partial transform and first boundary cutoff

Initially suppose F>=512 max(M,N) and delta F>=2, where delta=10^(-40). The complementary cases are paid in section7. Apply Poisson to -f(x,y), followed by conjugation. The first stationary coordinate is nu=-f_y>0 and

Psi(x,nu)=-f(x,y)-nu y.

The complete first-Poisson error, over all x, is at most

10^5[MN/sqrt(F)+M F^(1/3)+M log(2+F)].                            (3)

The same derivative constants as in the earlier one-partial-transform lemma suffice on the original strip: lambda2=F/(40N^2), h2=20, lambda3=F/(20N^3), h3=34. No first stationary lattice point is deleted from this main sum. Both half-open curved endpoints are preserved.

The stationary labels lie in F/(64N)<nu<F/(4N). Split into four bins T=alpha F/N, alpha=1/64,1/32,1/16,1/8. For every X in[1/16,32] and V=nu N/F in[1/64,1/4], the first stationary inverse remains in Y in[1/4,8]. The model values at the two extreme corners give strict margins, certified below. Thus Psi is defined on the extended rectangles needed for the second inverse.

The model first dual is

Psi0=-C F X^(-1/5)V^(3/5),
C=(5/2)8^(-2/5)(3/2)^(-3/5).                                    (4)

The first stationary amplitude w1=f_yy^(-1/2) has full two-dimensional Abel norm at most 10^12 N/sqrt(F), uniformly over every relevant subrectangle. This includes the mixed derivative. It is peeled off before the boundary cutoffs are expanded.

For either first curved endpoint b(x)=-f_y(x,y_end), use the finite Fejer approximation with L0=3, degree J=floor(delta F). On the original x range and the complete nu bins, |log(b/nu)|<3. Its Fourier phase is

Psi(x,nu)+tau log b(x)-tau log nu,
|tau|<=delta F/12.                                               (5)

The total coefficient norm is at most 8L. For the two boundaries, including points exactly on either boundary, the absolute lattice error is at most

100 M+10^4 L MT/(delta F).                                       (6)

This follows from the per-row estimate 2+16 L0 T(1+log(4T+1))/J and J>=delta F/2. The two orientations use the original half-open convention. The constants also cover shortened bins. No replacement of the endpoint allowance by strip area is made.

The twist in (5) is NOT annihilated before the second B transform. It is incorporated into its derivative hypothesis in section3.

## 3. Both implicit inverses and the second stationary domain

The finite checker uses ordinary Taylor coefficients, not sampled phase values. For a local model (1+xi)^a(1+u)^b, replace each coefficient through degree D+1 by its exact binomial coefficient times the relative interval in (1). Normalize the derivative in the inverted coordinate by b. Its constant is v00, and the stationary equation is

v(xi,u)=v00(1+tau).

At total degree n, all unknown coefficients of u of degree n enter only through the nonzero linear coefficient v01. Therefore each is exactly (target coefficient - known residual)/v01. This finite triangular recurrence encloses every actual inverse jet satisfying (1).

For the first inverse use (a,b)=(-1/2,-3/2), D=9 and the negative Legendre phase. The checker encloses every derivative through total order9 within relative error 10^(-14) of (4). Passing from the actual stationary basepoint to the model stationary basepoint costs less than a further 10^(-14), by the stationary equation and (1).

It also certifies |x^j (log b)^(j)|<10^6 for1<=j<=9. On the full enlarged inverse domain the smallest normalized nonzero derivative of (4), through order9, exceeds10^(-5) F. The first cutoff perturbation therefore contributes relative error less than10^(-20). A constant phase can be subtracted at a basepoint when forming the value coefficient; it does not alter any stationary derivative. Thus the phase Phi in(5) satisfies the fresh relative derivative box of radius10^(-12) required for the second inverse.

Its x derivative is positive and its second derivative negative. On the original x interval[M,2M],

10^(-4)F/M^2 < |Phi_xx| < F/M^2,
10^(-4)F/M^3 < |Phi_xxx| < F/M^3.                               (7)

Apply the same Poisson convention directly to Phi, without a sign reversal. Write mu=Phi_x and

Theta(mu,nu)=Phi(x,nu)-mu x.                                    (8)

All original stationary mu labels lie in F/(256M)<mu<F/(8M), hence five bins U=beta F/M with beta=1/256,1/128,1/64,1/32,1/16.

For every V in[1/64,1/4] and mu M/F in[1/256,1/7], the stationary x remains strictly in[M/16,32M]. The model derivative at X=1/16 is greater than F/(7M) even at the smallest V; at X=32 it is less than F/(256M) even at the largest V. The perturbations have ample margin. This is a genuine inverse extension, not an extrapolation from a curved image; it also covers the later total mu shift of at most10^(-16) times its bin scale.

For the second jet recurrence, interchange the coordinate roles: known exponent3/5, inverted exponent-1/5, degreeD=8, input relative radius10^(-12). The checker encloses every derivative with mu order<=5 and nu order<=3, total<=8, within10^(-4) of the model. After the basepoint correction we may use relative radius2*10^(-4). The model is

Theta0=-D F (mu M/F)^(1/6)(nu N/F)^(1/2),
D=6(C/5)^(5/6).                                                 (9)

The second stationary amplitude w2=|Phi_xx|^(-1/2) has full Abel norm at most10^12 M/sqrt(F), on each complete extended inverse rectangle. The checker bounds its two first logarithmic derivatives and mixed derivative by100 times w2, and |Phi_xx|>10^(-6)F/M^2 there. These bounds hold for every allowed first cutoff frequency.

## 4. Complete second Poisson and second cutoff errors

Using (7), the second Poisson error on each fixed nu row is bounded by

10^8[M/sqrt(F)+F^(1/3)+log(2+F)].                               (10)

For example lambda2=F/(10^4 M^2), h2=10^4 and lambda3=F/(10^4 M^3), h3=10^4 suffice; the original complete error coefficients are smaller than this displayed bound. The number of nu rows is at most3T/2. After multiplication by the first amplitude and summing its four bins, (10) is at most10^22 times

M+F^(5/6)+sqrt(F)L.                                             (11)

The first Fourier coefficient norm contributes one additional L, retained in(2).

Peel off w2, keeping its full Abel norm. For the second endpoints b2(nu)=Phi_x(x_end,nu), use L0=4 and J=floor(delta F). The ratio of every endpoint and mu on the complete bins is below32 in either direction. Its Fourier phase is

Theta(mu,nu)+sigma log b2(nu)-sigma log mu,
|sigma|<=delta F/16.                                             (12)

The coefficient norm is at most8L. The complete error for both second boundaries is at most

100 T+10^4 L TU/(delta F).                                       (13)

Again the exact boundary equalities are included. After the two stationary amplitudes, all bins and the first coefficient norm, (13) is bounded by10^70 L^2 M. Likewise (6), after its first amplitude, is bounded by10^60 L MN/sqrt(F). These are existing rows of(2).

## 5. Two inner differences with a capped length

Write u=mu/U and v=nu/T. Model(9) is -D F beta^(1/6)alpha^(1/2)u^(1/6)v^(1/2). Two positive mu differences annihilate the nu-only term in(12) exactly. The remaining -sigma log mu has normalized differentiated size at most1000 delta times the terminal scale. The model twice-differenced phase is a positive average of

D(5/36) F beta^(1/6)alpha^(1/2) U^(-2)u^(-11/6)v^(1/2).

Its xx diagonal is positive and its yy diagonal negative. The finite checker, followed by a total-shift average of at most s=10^(-16) times U, gives terminal normalized xx and negative yy lower bounds exceeding10^(-6), determinant lower bound exceeding10^(-12), and every required mixed derivative upper bound below10^4. Hence the explicit rectangular lemma applies with K=10^20. Its full coefficient and logarithm are bounded by10^90 L. Every one of these facts is uniform in both cutoff frequencies.

Put kappa=(U^3 T/F)^(1/5). If kappa>=2 and sqrt(sU)/4>=2, take

H=floor min(kappa,sqrt(sU)/4).

The two A lengths are H,H^2 in the mu coordinate. Thus the total shift H+H^2<=2H^2<=sU/8. The normalized inclusive-lattice recurrence gives

a0<=12H^(-1/2)+8(average a2)^(1/4).                              (14)

The terminal scale is F2=F d1d2/U^2. It is at most F. When F2<1 the trivial lattice count is paid by the same inverse-scale term used below; no terminal estimate is invoked outside F2>=1.

The complete average inside(14) is bounded by10^92 L times

F H^3/(U^3 T)+1/U+1/T+U^2 L^2/(F H^3).                         (15)

The harmonic factors come from both inverse-shift sums; log H<=L. Since

H>=min(kappa/2,sqrt(sU)/8),

(14)--(15), including the diagonal terms, yield a rectangular bound of10^32 L times the following five rows:

F^(1/10) U^(7/10) T^(9/10),
U^(3/4) T,
U T^(3/4),
F^(-1/10) U^(21/20) T^(17/20),
F^(-1/4) U^(9/8) T.                                             (16)

The last row is the inverse-shift cost when the optimal length is capped. It cannot be omitted. The logarithmic exponent in(16) is valid because the worst inverse contribution has L^(3/4).

If kappa<2, the trivial UT is paid by sqrt(2) times the first row in(16). If sqrt(sU)/4<2, then U<64/s and UT is paid by (64/s)^(1/4) times its second row. Thus(16) holds in all cases, not only in an unrecorded optimal-length range.

## 6. Return through both transforms

Multiply (16) by the two Abel norms, whose scale product is MN/F, and substitute U=beta F/M, T=alpha F/N. All alpha and beta factors, including the negative one, are bounded by10^4 on the listed finite bins. This gives exactly the first five rows in(2), in the same order. There are at most24 rectangular bins. Both Fourier coefficient norms, the two amplitudes, the explicit inner bound and every bin factor together are below10^75 L^3. The looser10^100 L^4 covers these and all errors(3),(6),(10),(13).

## 7. All complementary ranges

If delta F<2, the original trivial count is at most(9/4)MN and is paid by4*10^20 MN/sqrt(F), an existing row of(2).

If F<512N, use the first Poisson transform and its complete error directly. Its stationary count is bounded by a constant times F/N+1, and its amplitude by10^12 N/sqrt(F). The main contribution is at most10^15[M sqrt(F)+MN/sqrt(F)], hence at most10^17[M sqrt(N)+MN/sqrt(F)]. This is the sixth and tenth row of(2).

It remains that F>=512N but F<512M. The first transform, cutoff and second transform are still legal. The second stationary count is O(F/M+1), with an explicit bound10(F/M+1). Summing over T and applying both amplitudes gives at most10^28 L(F+M), including the first cutoff coefficient norm, hence at most10^31 L M. The complete second Poisson error remains(11), while the first boundary errors remain(6). There is no invocation of the two-dimensional inner lemma on a short mu interval. These are again rows of(2).

All shortened intervals, inclusive lattice counts and half-open stationary endpoints have therefore been covered. The original-phase C13 comparison and complete global zeta assembly are proved separately in ACTUAL_DOUBLE_OUTER.md and REPORT.md.

## Reproduction

Run certify_double_inverse_jets.py with python-flint0.9.0 / FLINT3.6.0. The finite192-bit certificate checks both triangular inverse recurrences, every listed stationary-domain endpoint, both amplitude jets, the first cutoff derivative budget, and the full terminal Hessian/derivative range. It does not itself certify the analytic Poisson/cutoff/Abel proof or a global theorem.
