# Independent reviews of the complete original spectral-gap certificates

## Part A. One-quarter certificate

Status: approved after mathematical, source-normalization and interval-code review.

Reviewed mathematical manuscript: [CERTIFIED_GAP.md, Part A](CERTIFIED_GAP.md). The publication version adds precise original-space definitions and a link to the complete operator proof.
Reviewed program: [certify_quarter_gap_intervals.py](certify_quarter_gap_intervals.py), SHA-256 `65434e518759bf4fd047af2d19c9d7c44757d45236d746e1cad6767a059dfdc7`.
Saved author output: [interval_result_2000.json](interval_result_2000.json), SHA-256 `f71823b9f7acad4d166b268eef9eb9f8118158f948397206bb773013326c2140`.

I read the entire manuscript and program, independently reconstructed the lower operator comparison and even-space formulas, and reran the corrected 2000-cell certificate. The rational assertions all passed. This is a full original-form lower bound E>=one quarter times the squared original norm on the even mean-zero subspace; it is not a finite Ritz extrapolation and does not prove the critical half-gap or RH.

### 1. Direction and normalization of the operator comparison

The first three positive Gamma summands have constant sum 4+4/5+4/9=236/45. Their subtracted rational Fourier multipliers have inverse kernels exp(-|x|/2), exp(-5|x|/2), exp(-9|x|/2), with no missing Fourier factor. The omitted Gamma terms are nonnegative. Hence the displayed inequality for B is a genuine lower form bound on its complete domain.

For each actual prime-power shift, 2 Re(conjugate(v(x))v(x+d))<=|v(x)|^2+|v(x+d)|^2 gives exactly the multiplication majorant p_N after translating the second integral. The complete weighted prime tail is bounded in operator norm by delta_6, so S_m<=p_6+delta_6 I. Both inequalities therefore combine in the correct direction: H+1/4>=D-m R(D)m. The n<=6 terms are precisely 2,3,4,5, including Lambda(4)=log 2. No other prime power is lost.

The inherited tail constant also follows directly from the full theta envelope: sup_x m(x)m(x+log n)<=Astar n^2 exp(-pi n), then log n<=sqrt n and the geometric tail ratio below 1/10 give delta_N=(20Astar/9)(N+1)^2 exp(-pi(N+1)). This is a bound for the entire omitted operator, not a truncated arithmetic model.

### 2. All higher directions are controlled

The interval proof gives D bounded below by 159/1000 on the whole real axis. It is also bounded above. Thus multiplication by sqrt(D) is boundedly invertible, and the comparison is congruent to I-T. The convolution R(D) is positive because its exact Fourier multiplier is nonnegative; positivity is not inferred merely from pointwise kernel positivity. Its integrable multiplier and w in L2 give trace class through the Fourier square-root factorization.

Under the unitary sqrt(2) restriction to the positive half-axis, the kernel is exactly w(x)w(y)[R(x-y)+R(x+y)]. Its diagonal gives the full even trace integral with coefficient 3+sum exp(-2lambda x). The test w has denominator A=integral a. Splitting the double integral across its diagonal and using the folded exponential identity gives the factor four in the Volterra formula. These are full-space quantities. Positivity and trace class imply lambda_2<=Tr(T)-lambda_1<=Tr(T)-Q, controlling every omitted direction at once.

### 3. Outward arithmetic and all omitted tails

The normalized theta remainder after n=4 is bounded above by 5^4 exp(-24pi)/(1-(6/5)^4 exp(-11pi)), uniformly for t=exp(2|x|)>=1. This follows by dropping a positive bracket bounded by one and using the decreasing geometric ratio for n>=5. Thus every m evaluation, including intervals crossing zero, encloses the complete theta series.

The exterior D bound uses the actual global m bound and the full theta tail. The half-axis m^2 integral tail is evaluated exactly under its exponential envelope; dividing by the positive Dtail bounds A's omitted tail, and multiplying by six bounds the omitted trace. The Rayleigh numerator has a positive integrand, so omitting exterior and same-cell triangles provides a valid lower bound. Whole-cell ranges, not point samples, enclose every retained rectangle.

The original preliminary code used a scalar sum of extracted lower endpoints for the three numerator components. I required that sum to be performed inside the interval type. The reviewed code contains this correction. The final quotient and subtraction are likewise interval operations. Endpoint transport uses scalar precision higher than the interval endpoint precision, so the binary endpoints are carried exactly; scalar minima and formatting do not enter arithmetic bounds. The proof relies on separated interval comparisons with rational numbers, not on rounded displayed decimal strings.

My independent execution reproduced and verified:

- inf D>159/1000;
- complete even trace<353/100;
- actual test Rayleigh>2749/1000;
- lambda_2<781/1000<1.

The program is a reproducible interval-arithmetic certificate with its stated trusted arithmetic implementation, not a formal proof-assistant verification. Its unrounded internal assertions and the analytic omitted-tail bounds are the certificate; exploratory quadrature is not used.

### 4. Transfer to the original mean-zero form

The positive compact comparison has at most one eigenvalue above one, so D-mRm has at most one negative direction. The lower form comparison implies the same negative-index upper bound for H+1/4 on its original even form domain. The known normalized ground state has H eigenvalue -1/2 and supplies one negative direction. Its orthogonal complement reduces H, and any negative form vector there would produce a second negative direction together with the ground state. This is impossible. Hence H>=-1/4 on that complement, equivalently the claimed E>=1/4 inequality.

The result uses the unchanged full theta, full prime operator and original weighted Hilbert space. It does not certify the earlier unresolved source-resolvent Gram, extend to epsilon=0, or establish the half-gap. No relation from this quarter-gap to an unproved RH statement is asserted.

## Part B. Three-eighths certificate

Status: approved after full mathematical review and an independent execution of the directed-interval certificate.

Reviewed mathematical manuscript: [CERTIFIED_GAP.md, Part B](CERTIFIED_GAP.md).
Reviewed program: [certify_three_eighths_gap.py](certify_three_eighths_gap.py), SHA-256 `3db4c42f136b58ce242201565a77f476eb82acd25e3a97adb662f96a8fd597fd`.
Author output: [interval_result_10000.json](interval_result_10000.json), SHA-256 `5ac66c5e9e1c80ec33bb7fd60afdafd8887360559ffa195c136a03d28d13565b`.
The independent 10000-cell execution passed all exact-rational assertions.

The conclusion approved here is E(q)>=3/8 ||q||^2 for every even, original-form-domain, original-mean-zero q. It uses the unchanged full operator. The critical one-half gap and RH remain unproved.

### 1. Original comparison and complete arithmetic tails

I checked the full original normalization against the previous quarter-gap certificate: ULU^{-1}=1/2+H, H=B-V, the genuine normalized ground state has H eigenvalue -1/2, and B is the closed form associated with m b(D)m. The six retained digamma summands have constant sum sum_{j=0}^5 1/(j+1/4). Their subtracted multipliers are exactly 2 lambda_j/(lambda_j^2+t^2), lambda_j=2j+1/2, whose inverse Fourier kernels are exp(-lambda_j |x|). No Fourier normalization factor is missing. The omitted digamma summands are nonnegative, so this is a lower form comparison on the entire original form domain.

For every retained prime-power edge, the symmetric inequality 2 Re(conjugate(a)b)<=|a|^2+|b|^2 gives exactly p_6. The complete omitted weighted prime operator is bounded in norm by delta_6; the four retained integers are 2,3,4,5 with Lambda(4)=log 2. Thus H+1/8>=D-mRm has the required direction. The inherited delta_6 is a full-prime bound, not a model truncation: it follows from sup_x m(x)m(x+log n)<=Astar n^2 exp(-pi n), log n<=sqrt(n), and the geometric tail ratio below 1/10.

The manuscript and program use the actual full theta formula in every shifted m evaluation. The positive normalized n>=5 remainder is bounded by the displayed geometric expression, uniformly for exp(2|x|)>=1. The exterior m envelope gives an all-axis D lower bound and the exact exponential-envelope integral of m^2 beyond x=2. Consequently the assertion D>43/500 is for the whole line, with no sampled-positivity inference.

### 2. Positive comparison, folding and squared trace

D is bounded above and bounded strictly away from zero. Congruence by its square root is therefore legitimate. Positivity of convolution R follows from its nonnegative Fourier multiplier, rather than only from positivity of its kernel. With a=m^2/D integrable, Fourier square-root factorization also shows that the full comparison is trace class. Restriction to the even subspace remains positive and trace class.

The sqrt(2) half-axis unitary produces exactly sqrt(a(x)a(y))[R(x-y)+R(x+y)], with no extra factor two. On x>=y, its bracket is 2 sum_j exp(-lambda_j x)cosh(lambda_j y). The true test w=sqrt(a) consequently has numerator factor four. Squaring the bracket gives factor four, and using both off-diagonal triangles gives the squared-trace factor eight. Grouping j<=k with multiplicity two for j<k accounts for all 36 ordered pairs through 21 retained pairs.

Within a single cell, the two triangles together have area Delta^2. The expanded squared kernel is bounded by four times its interval range, explaining the code's factor four, not eight, on a same-cell square. Interval dependency can only widen this upper bound. Off-diagonal preceding-cell rectangles carry factor eight. All these integrands are nonnegative. Omitting same-cell triangles from the Rayleigh numerator gives a valid lower bound; retaining their squared-trace interval upper bound is necessary and is done.

For a positive compact T, the actual test quotient Q satisfies lambda_1>=Q>=0. Hence lambda_2^2<=Tr(T^2)-Q^2. This controls every remaining direction; it is not a finite-section eigenvalue claim.

### 3. Code and omitted integration regions

I read the entire executable and reran it with 10000 cells. Whole interval cells, including intervals crossing zero after a prime shift, are evaluated with outward arithmetic. The scalar endpoint transport has higher precision than interval endpoints. All numerical additions, quotients and squares relevant to the final lower/upper enclosures remain in the interval type before endpoints are extracted. In particular the Rayleigh numerator uses lower(sum(DOUBLE_LOWER, interval_zero)), avoiding the earlier preliminary quarter-code endpoint-summation issue.

The exterior squared-trace region has total product mass 2 A_inside A_tail+A_tail^2 and kernel square at most (2J)^2=4J^2. The exact displayed bound is therefore correct. The Rayleigh denominator includes A_tail, while its omitted numerator tail is positive. The internal trace accumulator is optional and is not substituted for the squared trace.

The independent run gave separated bounds

- inf D > 43/500;
- Tr(T^2) < 7197/1000;
- Q > 623/250;
- Tr(T^2)-Q^2 < 987/1000 < 1.

The actual upper remainder was approximately 0.9845726040780324. The rounded rational bounds alone also suffice: 7197/1000-(623/250)^2=0.986936<0.987. Decimal strings, elapsed time, and exploratory numerics do not enter the proof. The reproducibility claim relies on the stated trusted mpmath.iv elementary interval implementation; this is not a proof-assistant formalization.

### 4. Transfer to the complete original mean-zero space

The squared-trace certificate implies at most one eigenvalue of T at or above one. In particular I-T, and hence D-mRm, has negative index at most one. The lower form inequality transfers this upper bound on negative index to H+1/8, on the complete original domain. The actual ground state supplies one negative direction. Its orthogonal complement reduces the selfadjoint H. A negative form vector in that complement would form a two-dimensional negative subspace together with the ground state, which is impossible. Therefore H>=-1/8 there, and ULU^{-1}=1/2+H gives exactly the three-eighths conclusion.

No original eigenvalue is numerically identified, no mean-zero condition is imposed separately on B or V, and no omitted prime, theta mode, spatial tail or Hilbert-space complement is discarded. This proof does not give the critical half-gap or an arithmetic same-bad-row correlation improvement.
