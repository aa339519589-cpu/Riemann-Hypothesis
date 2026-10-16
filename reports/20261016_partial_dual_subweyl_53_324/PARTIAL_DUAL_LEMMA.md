# A partial dual transform with a bounded-frequency boundary payment

Status: complete local lemma with independent internal review. The separate actual-phase and global assembly in this package retain all scale complements and original-sum errors.

## 1. Hypotheses and local conclusion

Let M,N>=2, F>=1, and let f be real and C^8 on
[M,3M] x [N/2,4N]. Put X=x/M, Y=y/N and

f0(x,y)=(F/8) X^(-1/2)Y^(-3/2).

Assume, for every i+j<=8 throughout that rectangle,

|partial_x^i partial_y^j f / partial_x^i partial_y^j f0 -1|<=10^(-12). (1)

Every denominator in(1) is nonzero. Set L=log(2+FMN). The bound, uniformly for every subrectangle of[M,2M]x[N,2N], is

|sum e(f(m,n))| <=10^40 L² [F^(1/2)M^(1/2)N^(1/4)
                    +M sqrt(N)+MN/sqrt(F)+M F^(1/3)+M].             (2)

This deliberately loose constant includes both boundary orientations, exact lattice equalities, the complete one-dimensional Poisson error and all small parameter cases. The term M sqrt(N) is not discarded or absorbed into a stronger hypothesis on F.

We use the previously proved explicit rectangular second-derivative lemma, included in the accepted mixed-coordinate report, and Patel--Yang's complete Poisson Lemma2.3. The finite certificate here proves the inverse-derivative and amplitude bounds from(1), not their application to a particular outer finite-difference phase.

## 2. Partial Poisson transform and its exact error

For each fixed x, apply Poisson Lemma2.3 to -f(x,y), then conjugate if necessary. Its stationary labels satisfy

nu=-f_y(x,y)>0,
Psi(x,nu)=-f(x,y)-nu y,                                          (3)

where the unique y solves the first equation. The negative-phase convention is essential: -f has negative second derivative. The y derivative bounds on the original strip allow

lambda2=F/(40N²), h2=20; lambda3=F/(20N³), h3=34.

They follow directly from(1); in particular f_yy>0 and f_yyy<0. The full Poisson error, summed over at most M+1<=3M/2 rows, is at most

10^5 [MN/sqrt(F)+M F^(1/3)+M log(2+F)].                           (4)

Indeed the first source coefficient is4.686 sqrt(40)<30, the derivative-error coefficient is below1000, and |f_y|<=F/N bounds the complete logarithm. No first stationary integer is deleted in the main transformed sum. Its original half-open endpoints are retained in the curved cutoffs below.

All stationary labels on the original rectangle lie in

F/(64N)<nu<F/(4N).                                               (5)

Use the four dyadic bins T=alpha F/N, alpha in{1/64,1/32,1/16,1/8}, with nu in[T,2T]. For X in[1,3] and V=nu N/F in[1/64,1/4], the stationary equation has its solution in Y in[1/2,4]. This follows by monotonicity in Y and the explicit model endpoint values, with the error in(1). Thus the dual phase is genuinely defined on every full rectangle used below, including the required inner x-shifts, not just on the stationary image.

The model dual phase is

Psi0= -C F X^(-1/5)V^(3/5),
C=(5/2) 8^(-2/5)(3/2)^(-3/5).                                  (6)

## 3. Certified inverse derivatives and amplitude

The standalone verifier uses ordinary Taylor coefficients at an arbitrary point (X,Y). Normalize f by f0(X,Y), and write local increments xi=Delta X/X and u=Delta Y/Y. The input coefficients through total degree8 are independently enclosed by

binom(-1/2,i) binom(-3/2,j) [1-10^(-12),1+10^(-12)].

Let v=-2 f_u/3 in these normalized units. The implicit equation is

v(xi,u)=v(0,0)(1+tau), tau=Delta nu/nu.

Its linear u coefficient is bounded away from zero. At each total degree n, solve the coefficient of u by dividing the known residual by that linear coefficient. This is a finite, exact triangular recurrence, not a sampled inverse. Substituting the resulting series through degree7 into

Psi=-f-(3/2)v(0,0)(1+tau)(1+u)

encloses every normalized dual coefficient with i<=4,j<=3,i+j<=7. Relative to

-(5/2) binom(-1/5,i) binom(3/5,j),

the error is below10^(-4). The slight difference between the actual and model stationary Y adds less than10^(-10), so use the safe relative error2*10^(-4) against the global model(6).

The same certificate proves:

- for either stationary boundary b(x)=-f_y(x,y_end),
  |x^j (log b)^(j)(x)|<4, 1<=j<=4;
- for the stationary amplitude w=(f_yy)^(-1/2),
  w<=100 N/sqrt(F), and |x w_x|, |nu w_nu|,
  |x nu w_(x nu)| are each <=10w.

Consequently its complete two-variable Abel norm on any bin/subrectangle is at most10^4 N/sqrt(F). The certificate obtains these derivatives by the same inverse-series substitution into f_yy and a degree-two binomial expansion, not by assuming that the exact amplitude is a monomial.

## 4. A bounded-frequency inner A estimate

Fix a bin T=alpha F/N. Consider the added phase

Psi(x,nu)+tau0 log b(x)-tau0 log nu,
|tau0|<=delta F/12, delta=10^(-12).                              (7)

After an x-difference of length d, the log nu part vanishes. The remaining twist has every normalized derivative through x order3 bounded by delta F d/M. The model x-difference is an average of the positive phase

(CF/(5M)) X^(-6/5)V^(3/5).

Its xx entry is positive and yy entry negative. The inverse certificate, including all required mixed derivatives, proves uniformly for 1<=d<=M that the differenced phase satisfies the rectangular lemma with scale F_d=Fd/M and K=10^12 whenever F_d>=1. The certificate explicitly checks both signed diagonal lower bounds and their product. The x-only perturbation in(7) leaves yy and xy unchanged; its xx debit is below delta in normalized units. Hence it preserves the opposite diagonal signs and the determinant lower bound. No arbitrary-frequency twist assertion is made.

If F_d<1, use the trivial normalized lattice count<=9/4, which is covered by the inverse row C_B log(2+K²F)/F_d, where C_B=20000K^4=2*10^52.

Suppose for now F>=128N, delta F>=2, and M>4sqrt(N). Then T>=2, and H=floor(M/sqrt(N)) satisfies H>=M/(2sqrt(N))>=2 and H<=M. Inclusive-lattice Cauchy and the exact correlation expansion give

a²<=9/H+8 average_(1<=d<H) a_d,

where a is the transformed rectangular sum divided by MT, and average means H^(-1)sum. The rectangular lemma gives

average a_d<=60 C_B L [F H/(M²T)+1/M+1/T
                         +M(1+log H)/(FH)].                      (8)

The factor60 bounds log(2+K²F)/L. Here

F H/(M²T)<=64/H, 1/M<=1/H, 1/T<=64N/F,
M(1+logH)/(FH)<=4LN/F.

Thus, rounding the square root outward, every rectangular sum with twist(7) is bounded by

B=2*10^29 L [F M^(1/2)N^(-3/4)+M sqrt(F)N^(-1/2)].               (9)

The second term in(9) is the full boundary row of the two-dimensional lemma. It is not removed by requiring H<=T, a restriction that the x-only A-process does not need.

## 5. Curved boundary cutoffs with all endpoints

For one curve b(x), split at its crossings with T/2 and4T; outside those values the bin is full or empty. The curves are decreasing because f_xy>0. The upper and lower curves therefore produce at most five x-pieces in total.

On each nontrivial piece choose L0=3, theta=pi log(b/nu)/(2L0), and Fejer degree J=floor(delta F). Its coefficient norm is <=2log(2J)<=2L. Every Fourier term has tau0=k/(4L0), hence satisfies(7). The pointwise discrepancy obeys

error<=min(1,2L0/[J |log(b/nu)|]).

At exact boundary equality use error<=1. Since b in[T/2,4T], summing unit distance annuli in nu gives, on each x row,

sum error<=2+(16L0 T/J)[1+log(4T+1)].

The full row count is <=3M/2. Retaining both curves, all five pieces, J>=delta F/2 and the complete logarithm gives

|curved transformed sum|<=20 L B+30M+6000 L MT/(delta F).          (10)

This is the new frequency-limited boundary debit. It is not the O(M) debit of the earlier arbitrary-frequency mixed-word lemma.

Apply the complete amplitude Abel norm10^4 N/sqrt(F) to(10), on every subrectangle. Sum all four bins. Formula(9) supplies at most

1.6*10^35 L² [sqrt(F) sqrt(M) N^(1/4)+M sqrt(N)],

and the remaining terms are below10^22 L² MN/sqrt(F). Together with(4), these are safely below the right side of(2).

## 6. Complete complementary cases

If delta F<2, the original trivial lattice count<=9MN/4 is bounded by4*10^6 MN/sqrt(F), already covered by(2).

If F<128N, use the stationary-label count<=F/(4N)+1 directly in(3). The weight bound gives at most200M[sqrt(F)+N/sqrt(F)], in addition to(4). Its first term is <=2400M sqrt(N), so(2) holds.

In the remaining case, if M<=4sqrt(N), the same direct label count gives M sqrt(F)<=2 sqrt(F)sqrt(M)N^(1/4), and the endpoint term remains MN/sqrt(F). Thus(2) again follows. These cases cover every F>=1,M,N>=2, and no short dual interval, small A length, cutoff-degree floor or stationary endpoint is omitted.

## Reproduction and scope

Run certify_partial_dual_jets.py with python-flint0.9.0 / FLINT3.6.0; it uses192-bit outward arithmetic. Its finite jet identity is proved above; the certificate only encloses those finite expressions and the stated explicit model constants. Its zeta consequence additionally uses the actual-phase comparison in ACTUAL_OUTER_ASSEMBLY.md and the complete original-sum assembly in REPORT.md.

Primary input: D. Patel and A. Yang, An explicit sub-Weyl bound for zeta(1/2+it), arXiv2302.13444v1, Lemma2.3. The exact rectangular lemma is in the accepted mixed-coordinate package and must accompany any self-contained release that uses this local result.
