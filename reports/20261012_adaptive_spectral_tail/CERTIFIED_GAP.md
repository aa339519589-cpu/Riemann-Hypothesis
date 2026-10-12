# Certified full-operator spectral gaps: one quarter and three eighths

The strongest result in this supplement is

    E(q) >= (3/8) ||q||_(L2(nu))²

for every even vector in the unchanged original full-theta/full-prime form domain with integral q dnu=0. The proof includes the entire real line and every omitted spectral direction. It is unconditional, relying on the stated trusted outward interval implementation. The critical coefficient 1/2 and RH remain unproved.

Part A gives a three-term Gamma comparison with a trace certificate for 1/4. Part B strengthens the actual bound to 3/8 using six Gamma terms and a squared-trace certificate. Both actual interval programs and their saved outputs are included. Neither proof numerically identifies the second eigenvalue of the original operator or asserts that the separate source-resolvent Gram has passed. The original operator, its domains and the complete prime-tail proof are fixed in [REPORT.md, §1](REPORT.md#1-exact-original-operator-domains-and-complete-prime-tail).

Status: both mathematical reductions and both interval programs have undergone independent review and independent execution. The [proof review](REFEREE_CERTIFIED_GAP.md) records the verified inequalities and scope. Equations and subsection numbers are local to each part.

## Part A. One-quarter trace certificate

Status: independently reviewed and approved, including an independent rerun of the interval certificate. The interval program has actually passed the rational inequalities below. This is a positive-depth certificate for the original operator, not an RH proof, and no literature-priority claim is made.

### 1. Result and exact scope

For the original full-theta/full-prime even jump operator L, the argument and interval certificate below establish

    E(q)>= (1/4)||q||_nu²                                     (1)

for every even original form-domain q with nu(q)=0. Equivalently H=ULU^(−1)−1/2 has no second eigenvalue below −1/4. The known original ground state at H eigenvalue −1/2 is retained throughout.

This is an actually checked full-domain lower bound. It does not assert the desired critical coefficient 1/2. It does not infer an infinite-domain result from sampled Ritz eigenvalues. A positive compact comparison operator, its complete trace, and one rigorously enclosed Rayleigh quotient control every omitted direction simultaneously.

### 2. Inherited original inputs

Use the unchanged full even original Hilbert space. Precisely, set

    p(x)=2Phi(x)cosh(x/2), dnu=p(x)dx, Uq=sqrt(p)q,
    m²=Phi/[2cosh(x/2)], integral p=1.

The original maximal jump form E and the complete operator-domain realization are given in [REPORT.md, §1](REPORT.md#1-exact-original-operator-domains-and-complete-prime-tail). Its theta/Gamma/prime identity and ground state, used here without altering the form, are


    H=ULU^(-1)−1/2=B−V,  B=M_m b(D)M_m,
    b(t)=Re psi(1/4+it/2)−psi(1/4),
    V=C0m²+S_m,
    S_m=sum_(n>=2) alpha_n M_m(tau_(log n)+tau_(−log n))M_m,
    alpha_n=Lambda(n)/sqrt(n),
    C0=EulerGamma+pi/2+3log 2+log pi.

The real theta function is normalized as

    Phi(x)=sum_(n>=1) [4pi²n⁴e^(9x/2)−6pi n²e^(5x/2)]
                         e^(−pi n²e^(2x)),  x>=0,
    Phi(−x)=Phi(x).

The known normalized vector g0=sqrt(p)=Phi/m has H g0=−g0/2. Orthogonality to g0 is exactly original nu mean zero. The inherited complete-prime norm tail is

    ||S_m−S_(m,N)||<=delta_N,
    delta_N=(20Astar/9)(N+1)²e^(−pi(N+1)),
    Astar=4pi²(125/121).                                      (2)

The full-theta envelope is m²(x)<=Astar exp(4|x|−pi exp(2|x|)). Its square-root supremum is bounded by M0=sqrt(Astar)e^(−pi/2).

### 3. A true Gamma-resolvent lower comparison

For a_j=j+1/4, the exact positive Gamma expansion gives

    b(t)=sum_(j>=0) (t/2)²/[a_j(a_j²+(t/2)²)]
         >=c−r(t),
    c=sum_(j=0)^2 1/a_j=236/45,
    r(t)=sum_(j=0)^2 4a_j/[t²+4a_j²].                        (3)

The omitted summands are nonnegative. With the Fourier convention hat f(t)=integral f(x)e^(itx)dx and inverse measure dt/(2pi), the inverse transform of r is

    R(x)=e^(−|x|/2)+e^(−5|x|/2)+e^(−9|x|/2).                (4)

Thus R(D) is a positive bounded convolution operator and

    B>=c m²−M_m R(D)M_m                                      (5)

on the complete original B-form domain. This is a lower bound obtained directly from the original Gamma terms, not a replacement spectral model assumed equal to B.

Fix N=6 and define the explicit nonnegative function

    p_N(x)=m(x) sum_(2<=n<=N) alpha_n
                         [m(x+log n)+m(x−log n)].             (6)

Only n=2,3,4,5 contribute; alpha_4=log(2)/2. For every complex original v, the inequality 2 Re(conjugate(u)w)<=|u|²+|w|², followed by translation of one integral, gives

    <v,S_(m,N)v><=integral p_N(x)|v(x)|²dx.                   (7)

Together with (2), this proves the complete-prime form upper bound S_m<=p_N+delta_N I. No omitted prime has been set to zero.

Set epsilon=1/4 and

    D(x)=epsilon−delta_6+(c−C0)m²(x)−p_6(x).                 (8)

Then

    H+epsilon>=D−M_m R(D)M_m.                                (9)

Here D on the right is the multiplication operator by (8); R(D) is the Fourier/convolution operator (4), and these two uses of D are distinguished by the displayed context. The interval certificate proves

    D(x)>159/1000 for every real x.                          (10)

Thus the right side of (9) is legitimately congruent to I−T, where

    T=M_w R(D)M_w,  w=m/sqrt(D),  a=w²=m²/D.                 (11)

T is compact, positive, and trace class. Positivity follows from r(t)>=0; trace class follows, for example, by the square-root Fourier factorization since r is integrable and w is in L2. Restricting to the even space preserves these properties.

### 4. Complete even trace and one exact Rayleigh quotient

Identify even L2(R) with L2(0,infinity) by the usual sqrt(2) restriction. The kernel of T in this representation is

    sqrt(a(x)a(y))[R(x−y)+R(x+y)],  x,y>0.

Writing lambda in {1/2,5/2,9/2}, its COMPLETE trace is

    Tr_even(T)=integral_0^infinity a(x)
                       [3+sum_lambda e^(−2lambda x)]dx.     (12)

The nonzero test vector sqrt(a(x)) has squared norm

    A=integral_0^infinity a(x)dx,

and Rayleigh quotient

    Q=(1/A) sum_lambda I_lambda,
    I_lambda=4 integral_0^infinity a(x)e^(−lambda x)
                     [integral_0^x a(y)cosh(lambda y)dy]dx.   (13)

The factor four comes from symmetry across x=y and the folded kernel identity

    e^(−lambda(x−y))+e^(−lambda(x+y))
       =2e^(−lambda x)cosh(lambda y), x>=y.

Since T is positive trace class, lambda_1(T)>=Q and

    lambda_2(T)<=Tr_even(T)−lambda_1(T)
                 <=Tr_even(T)−Q.                            (14)

This includes ALL higher eigenvalues through the complete trace. No finite Ritz lower bound is mistaken for an upper bound on lambda_2.

### 5. Verified rational inequalities

The enclosed program `certify_quarter_gap_intervals.py` was actually run with 2000 cells and 45 decimal digits of mpmath.iv interval arithmetic. It verified the conservative rational inequalities

    inf_R D >159/1000,
    Tr_even(T)<353/100,
    Q>2749/1000,
    lambda_2(T)<781/1000<1.                                  (15)

Its narrower enclosures, shown only for orientation, were

    inf_[0,2] D >0.15967266692058932958,
    inf_(2,infinity) D >0.24999875022029261848,
    Tr_even(T)<3.52903375607544394412,
    Q>2.74991502452588376214,
    Tr_even(T)−Q<0.77911873154956018198.

The proof uses the rational comparisons (15), not the rounding of these printed decimal displays. The primary output is `interval_result_2000.json`. The implementation and all analytic omitted-tail bounds are specified below so this is reproducible without any zero table or RH assumption.

Reproduce the certificate with Python 3 and the already available mpmath package (the independent integration rerun used mpmath 1.3.0):

```sh
python certify_quarter_gap_intervals.py 2000
```

The program output includes runtime metadata; only the mathematical interval assertions enter the proof. The saved output is an example certificate, not a substitute for the full analytic reduction or a formal proof-assistant verification.

### 6. What the intervals enclose

#### 6.1 Complete theta, including its omitted modes

For x>=0, put t=e^(2x)>=1. Factor the actual theta series as

    Phi(x)=4pi²e^(9x/2−pi t)
       sum_(n>=1) n⁴[1−3/(2pi n²t)]e^(−pi(n²−1)t).           (16)

Every summand is positive. The program retains n=1,...,4 and adds the interval from zero to

    Btheta=5⁴e^(−24pi)/[1−(6/5)⁴e^(−11pi)].                  (17)

This encloses ALL remaining modes for every t>=1: discard the bracket by its upper bound one, use t>=1, and bound the ratio of successive majorants for n>=5 by (6/5)⁴e^(−11pi). The universal normalized theta remainder is below 1.125×10^(−30). Evenness handles all negative arguments in (6), including cells crossing zero. Every m or m² evaluation uses (16)–(17) and the exact omega=2cosh(x/2).

#### 6.2 Complete prime tail

The finite sum in (6) includes 2,3,4,5 exactly through interval elementary functions. All prime powers n>6 are paid by the inherited delta_6 from (2); the interval encloses it near 0.00000124977970738151718269. No prime-density estimate or finite zero verification is used.

#### 6.3 The infinite spatial tail

Let X=2 and t0=e^(2X). The theta envelope gives

    m_tail(X)<=sqrt(Astar)e^(2X−pi t0/2)=:Mtail,
    D(x)>=epsilon−delta_6−|c−C0|Mtail²
                      −2M0(sum_(n<=6)alpha_n)Mtail=:Dtail>0

for x>=X. It also gives the exact-integral upper bound

    integral_X^infinity m²(x)dx
      <=(Astar/2)e^(−pi t0)[t0/pi+1/pi²].                    (18)

Divide (18) by Dtail to bound the omitted A-tail, which the program bounds above by 4.589×10^(−72). The omitted trace is at most six times that A-tail. For the Rayleigh numerator all integrands in (13) are nonnegative, so discarding the outer tail is a VALID lower bound.

#### 6.4 Continuous cells rather than point samples

The interval [0,2] is partitioned into 2000 cells of exact rational length 1/1000. On each whole cell the program evaluates interval ranges for m², D, a, and the exponential factors. It proves D positive on every cell, and sums interval range times exact cell length to enclose the integrals A and (12).

For the numerator (13), retain only rectangles with y in an earlier cell than x. Their positivity permits omitting each same-cell triangle. A running interval prefix integral of a(y)cosh(lambda y) bounds each retained rectangle; multiplication by the interval enclosure of the outer a(x)e^(−lambda x) and the exact cell length is rigorous. This reduces the enclosure to a linear-time cumulative calculation. The lower endpoint of the interval sum gives a lower bound on the full numerator. Divide it by the upper endpoint of A, including the infinite tail, to get the lower bound on Q.

All final arithmetic that produces the certificate is performed with interval operations before extracting endpoints. Exact rational inequalities are checked by separated interval endpoints. mpmath scalar arithmetic outside the interval type is used only to carry/examine interval endpoints, take minima, format outputs, and time the run. The first exploratory floating-point quadrature suggested a margin but is not used in this proof or its final inequalities.

### 7. Transfer to the original mean-zero spectrum

By (15), I−T has at most one negative direction. Since multiplication by sqrt(D) is bounded and boundedly invertible, (9) implies that H+1/4 has at most one negative direction on its full even form domain.

The known original ground state g0 has H eigenvalue −1/2, so it provides one negative direction. Its original orthogonal complement reduces H. If a vector in that complement had <v,(H+1/4)v><0, the span with g0 would be a two-dimensional negative subspace, a contradiction. Therefore H>=−1/4 on g0-perpendicular, proving (1) for the complete original form domain.

This certificate bypasses the unevaluated finite source-resolvent Gram by a rigorously ordered comparison built out of actual positive Gamma summands and the unchanged prime-tail envelope. It does not compute that earlier Gram or claim its proposed finite matrix passed. It DOES supply the requested mathematically meaningful actual positive-depth full-domain instance. Any strengthening toward 1/2 needs additional verified estimates; the present 1/4 result is not extrapolated to the critical limit.

## Part B. Three-eighths squared-trace certificate

Status: independently reviewed and frozen. The computation below is a directed-interval certificate for a sufficient condition on the unchanged original theta jump operator. It is not a finite-section spectral guess. The certified conclusion is a gap of 3/8 on the original even mean-zero space; the required gap of 1/2 remains open.

### 1. Exact original operator and conclusion

Use the original normalization

    omega(x)=2cosh(x/2), p(x)=Phi(x)omega(x), dnu=p(x)dx,
    integral dnu=1, Uq=sqrt(p)q, m=sqrt(Phi/omega).

The original closed jump form and its generator L are retained, with

    U L U^(-1)=1/2+H, H=B−V,
    B=M_m b(D)M_m,
    b(t)=Re psi(1/4+it/2)−psi(1/4),
    V=C0 m²+M_m S M_m,
    C0=gamma_E+pi/2+3log2+log pi,
    S=sum_(n>=2) [Lambda(n)/sqrt(n)](tau_(log n)+tau_(-log n)).       (1)

Here B is the closed form operator, and V is the actual bounded operator defined by the complete weighted prime sum. Work on the full even L2(dx) space until the final mean-zero restriction. The exact ground state e0=U1 satisfies H e0=−e0/2.

The certified theorem is

    E(q)>=3/8 ||q||_(L2(nu))²,
    q even, q in the original form domain, integral q dnu=0.        (2)

Only the already reviewed original operator identity, the actual theta formula, and the explicit complete-prime norm envelope are inputs. No zero location hypothesis is used.

The exact original normalization and complete-prime constants are proved in [REPORT.md, §1](REPORT.md#1-exact-original-operator-domains-and-complete-prime-tail). The algebraic lower comparison uses Part A above. This part adds the six-term Gamma comparison, a squared-trace criterion in place of trace minus Rayleigh, and its own full interval certificate.

### 2. Exact lower comparison using six Gamma terms

The digamma series, all summands nonnegative, gives

    b(t)=sum_(j>=0) [1/(j+1/4)−(j+1/4)/((j+1/4)²+t²/4)].         (3)

For J=6 define

    lambda_j=2j+1/2, 0<=j<6,
    c=sum_(0<=j<6)1/(j+1/4)=4+4/5+4/9+4/13+4/17+4/21,
    R(x)=sum_(0<=j<6)exp(−lambda_j|x|).

With Fourier convention fhat(t)=integral f(x)exp(−itx)dx, the multiplier of convolution by R is

    r(t)=sum_(0<=j<6) 2lambda_j/(lambda_j²+t²).

Thus (3) yields the exact form inequality

    B>=c m²−M_m R* M_m.                                         (4)

The convolution operator R* is positive, since every rational summand r(t) is positive. It is a bounded operator; all comparisons here have their ordinary form meaning on D(B^(1/2)).

Take the finite prime cutoff N=6, and put

    alpha_n=Lambda(n)/sqrt(n),
    S6=sum_(n=2,3,4,5) alpha_n(tau_(log n)+tau_(-log n)),
    p6(x)=m(x) sum_(n=2,3,4,5) alpha_n[m(x+log n)+m(x−log n)].

For complex or real v, symmetry of the edges and 2Re(a conjugate b)<=|a|²+|b|² give

    <v,M_m S6 M_m v><=integral p6(x)|v(x)|²dx.                    (5)

All omitted prime powers remain through the reviewed full-prime bound

    ||V−(C0 m²+M_m S6 M_m)||<=delta6,
    delta6=(20Astar/9)·49·exp(−7pi),
    Astar=4pi²·125/121.                                         (6)

Set epsilon=1/8 and define the actual even multiplication function

    D(x)=epsilon−delta6+(c−C0)m²(x)−p6(x).                       (7)

Equations (4)–(6) give on the complete original form domain

    H+epsilon >= M_D−M_m R* M_m.                                (8)

The certificate below proves D(x)>43/500 for every real x. In particular D^(−1/2) is bounded. The positive compact operator

    T=M_(m/sqrt(D)) R* M_(m/sqrt(D))                              (9)

then controls the negative index of the right-hand side of (8). This is an exact lower comparison on the entire Hilbert space, not a truncation of H.

### 3. A squared-trace sufficient condition for at most one negative direction

Write a(x)=m²(x)/D(x)>0. Under the standard even-space unitary to L2(0,infinity), the integral kernel of T is

    sqrt(a(x)a(y)) [R(x−y)+R(x+y)], x,y>0.                       (10)

There is no additional factor of two in (10). Both T and T² are trace class, since a is integrable and R is a finite sum of positive convolution kernels. For the Hilbert–Schmidt assertion alone, the bound |R(x−y)+R(x+y)|<=12 is enough.

Let w(x)=sqrt(a(x)) on the half-line, A=integral_0^infinity a, and let Q be its Rayleigh quotient. Positivity gives 0<=Q<=lambda1(T). Therefore

    lambda2(T)² <= sum_(j>=2)lambda_j(T)²
                 =tr(T²)−lambda1(T)²
                 <=tr(T²)−Q².                                (11)

No finite-dimensional eigenvalue approximation enters this inequality. In particular, if its last expression is below 1, then T has at most one eigenvalue at least 1, and hence at most one eigenvalue strictly greater than 1. By the bounded invertible D^(1/2) congruence, the right side of (8) has negative index at most one. The form inequality gives the same assertion for H+1/8.

The genuine ground state e0 has (H+1/8)e0=−3e0/8. If a mean-zero v=Uq had <v,(H+1/8)v><0, its span with e0 would be a two-dimensional negative subspace: the cross term is zero because v is orthogonal to e0 and e0 is an actual eigenvector. This contradiction proves (2).

This argument does not infer a gap from finitely many nonnegative Ritz eigenvalues, nor assume that a trial space is invariant.

### 4. Exact one-dimensional positive integral representations

For x>=y>=0,

    R(x−y)+R(x+y)=2 sum_j exp(−lambda_j x)cosh(lambda_j y).

Consequently the Rayleigh numerator is

    I=4 sum_j integral_0^infinity a(x)exp(−lambda_j x)
                    [integral_0^x a(y)cosh(lambda_j y)dy] dx,
    Q=I/A.                                                     (12)

The full squared trace is

    tr(T²)=8 sum_(j,k) integral_0^infinity a(x)exp(−(lambda_j+lambda_k)x)
                 [integral_0^x a(y)cosh(lambda_j y)cosh(lambda_k y)dy] dx.
                                                                    (13)

The diagonal x=y has measure zero. The factor 8 is exactly: four from squaring the folded kernel, and two from the two half-plane triangles. The program collects pairs j<=k, with multiplicity two for j<k.

All integrands in (12)–(13) are nonnegative. This permits rigorous one-sided cell sums without oscillatory quadrature.

### 5. Interval enclosures, including every omitted theta mode and spatial tail

The attached program `certify_three_eighths_gap.py` uses mpmath.iv at 45 decimal digits. Values are outward-enclosed intervals; the displayed decimal output is not used as an exact constant. The success assertions compare interval endpoints to separately enclosed rational numbers.

#### 5.1 Actual theta enclosure

For z=|x| and t=exp(2z)>=1, use the exact formula

    m²(x)=[4pi² exp(9z/2−pi t)/(2cosh(z/2))]
           sum_(n>=1) n^4[1−3/(2pi n²t)]exp(−pi(n²−1)t).      (14)

The n<=4 part is evaluated by interval arithmetic. The remaining positive sum lies between zero and

    Etheta=5^4 exp(−24pi)/[1−(6/5)^4 exp(−11pi)].             (15)

Indeed the bracket in (14) is in (0,1), t>=1, and the ratio of successive terms n^4exp(−pi(n²−1)) for n>=5 is at most (6/5)^4exp(−11pi). Formula (15) is a global uniform enclosure, including every moving argument x±log n in p6.

The global envelope and its supremum are

    m²(x)<=Astar exp(4|x|−pi exp(2|x|)),
    ||m||_infinity<=sqrt(Astar)exp(−pi/2).                     (16)

#### 5.2 Whole-line positivity of D and the spatial tail

On [0,2], enclose D on all 10000 complete interval cells using (14)–(15). Outside 2, (16) gives

    m_tail=sqrt(Astar)exp(4−(pi/2)exp4),
    D>=1/8−delta6−|c−C0|m_tail²
                   −2||m||_infinity m_tail sum_(n=2,3,4,5)alpha_n.    (17)

The right side is positive and larger than 43/500. Thus the inside and outside checks together prove D>43/500 globally. No sampled-grid positivity assertion is used.

For t0=exp4,

    integral_2^infinity m²(x)dx
      <=(Astar/2)exp(−pi t0)[t0/pi+1/pi²].                    (18)

Divide this upper bound by the positive right side of (17) to obtain A_tail>=integral_2^infinity a. It is less than 10^(−70).

The kernel in (10) is bounded by 12. Hence the portion of tr(T²) with x>2 or y>2 is at most

    4J² [2A_inside A_tail+A_tail²], J=6.                       (19)

All quantities in (19) are interval upper-enclosed; using A_inside as an interval rather than a point retains a valid upper bound.

#### 5.3 Positive cell sums and same-cell squares

Let Delta=2/10000. Store interval cell ranges of a(x), exp(−lambda_j x), and cosh(lambda_j x).

For (12), sum only rectangles with y in a cell strictly preceding the x-cell. Lower endpoints give an integral lower bound. Same-cell triangles and all exterior terms are positive and may be omitted for this lower bound.

For (13), sum all preceding-cell rectangles with upper endpoints. The remaining same-cell square is bounded by its full interval range times Delta². In the expanded pair (j,k), this contribution is

    4 Delta² [a(cell)]² exp(−(lambda_j+lambda_k)cell)
                       cosh(lambda_j cell)cosh(lambda_k cell),      (20)

with multiplicity two if j<k. The off-diagonal rectangles have factor 8 as in (13). Formula (20) includes both same-cell triangles without double-counting. It is a safe enclosure even though interval arguments are not independent.

Finally add (19). The denominator A in (12) is upper-enclosed by the complete cell sum plus A_tail.

### 6. Exact-rational certificate and reproducibility

Run

    python certify_three_eighths_gap.py 10000

The saved [interval_result_10000.json](interval_result_10000.json) and an independent integration rerun using mpmath 1.3.0 give the conservative exact rational assertions

    inf_x D(x)>43/500,
    tr(T²)<7197/1000,
    Q>623/250,
    tr(T²)−Q²<987/1000<1.                                    (21)

For transparency, approximate enclosing endpoint outputs are

    D lower on [0,2]: .0861173972864658,
    tr(T²) upper:      7.19692669470252,
    Q lower:          2.49245944613437,
    squared remainder upper: .98457260407804.

Only (21), the analytic inequalities above, and directed intervals carry the proof. The displayed elapsed time and floating decimal strings carry no mathematical role. The rational inputs themselves already have margin:

    7197/1000−(623/250)²=.986936<.987.

Thus (11) applies and proves the full-operator conclusion (2).

### 7. Scope

The certificate includes the exact full theta sum, all prime powers through the explicit complete-prime tail, the original Gamma multiplier through a rigorous lower comparison, the entire real line, and every even form-domain vector. The sufficient condition bounds the second eigenvalue of a different positive comparison operator globally. It does not identify the second eigenvalue of the original jump operator.

The conclusion leaves an unproved interval between 3/8 and the required 1/2. It does not improve the separate same-bad-row arithmetic correlation estimate, change the physical probe, or prove RH.
