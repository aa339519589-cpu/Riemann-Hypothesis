# A certified positive bounded factor and a bounded comparison operator

On the original even physical Hilbert space, let H be the original signed operator, e0 its normalized ground vector, and K=H+(1/2)Pi_e0 the ground-deflated operator. This report proves an unconditional factorization K=A-B with A and B nonnegative, B bounded, and the SAME original closed form domain. A is the complete Gamma remainder after removing its first exponential jump kernel; B contains the full original prime jump, the first Gamma jump and the actual ground projection. No prime-power or theta tail is omitted.

The substantive scalar certificate is a full-line relative weighted-prime bound r<0.72435021<4/5. It proves

    0<=B<=(1/2)(I-Pi_e0),  ker B=span(e0),
    B[v]>=(1/5) integral D_B(x)|v(x)|^2 dx,  v perpendicular to e0,
    D_B(x)>(1/100)exp(-3|x|),  |x|>=2.

A further complete analytic argument proves, on the ground-perpendicular space,

    A[v]>=2^(-9) integral exp(-3|x|)|v(x)|^2 dx,
    B[v]<=2^17 integral exp(-3|x|)|v(x)|^2 dx,
    0<=B<=2^26 A.

This defines a genuinely bounded form-sandwich Q with 0<=Q<=2^26 I even though A has no assumed bounded inverse. The exact threshold equivalence is K>=0 if and only if Q<=I. The inequality Q<=I is NOT established. In fact the original known null family gives eigenvalue 1 of infinite multiplicity for Q, so Q is not compact and no strict contraction is possible. The coarse constant 2^26 is a relative bound, not a measure of proximity to RH. No new original spectral gap or zeta-zero exclusion follows from this report.

Here Q denotes a spectral comparison operator, not a prime-distribution hypothesis. No such arithmetic hypothesis enters either proof. Part I retains the complete certified positive-factor proof. Part II supplies the original-domain relative bound and threshold structure. Equation numbers restart in each part.

## Original forms and complete-theta input

The [user's original form foundation](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), Sections 1–7, fixes the complete theta normalization, derives the source identity without assuming RH, proves boundedness of the full prime jump and identifies the maximal closed form domain. For v=e0 q, define explicitly

    E_prime(q)=sum_(n>=2) Lambda(n)/sqrt(n)
       integral Phi(x)Phi(x+log n)|q(x)-q(x+log n)|^2 dx,
    E_Gamma,j(q)=(1/2)double_integral Phi(x)Phi(y) k_j(x-y)
                          |q(x)-q(y)|^2 dxdy,
    k1(t)=exp(-|t|/2),
    k_rem(t)=exp(-5|t|/2)/(1-exp(-2|t|)),
    E_Gamma=E_Gamma,1+E_Gamma,rem.

The unitary map is v=e0 q, with e0=sqrt(2hPhi), h=cosh(x/2), dnu=e0^2 dx and integral dnu=1. On the original maximal form domain,

    E_Gamma(q)+E_prime(q)=(1/2)||v||_2^2+H[v].

The source multiplier and source identity are

    b(t)=sum_(j>=0) (t/2)^2/[(j+1/4)((j+1/4)^2+(t/2)^2)],
    (b(D)-C0-S)Phi=-h,
    S f=sum_(n>=2) Lambda(n)/sqrt(n)[f(x+log n)+f(x-log n)],
    C0=EulerGamma+pi/2+3log2+log pi.

The original kinetic operator m b(D)m is not denoted B in this report. B below is the new bounded difference of jump forms. H and its ground identity H e0=-e0/2 remain unchanged. Subtracting the bounded first-Gamma jump preserves the complete Gamma form domain; all associated operator statements use bounded perturbation, not a claim that the bounded perturbation preserves that operator domain as a map.

For clarity, the full-theta envelope used in both parts can be checked directly. For x>=0, discarding only the negative term of each theta summand gives

    Phi(x)<=4pi^2 exp(9x/2-pi exp(2x))
                    sum_(n>=1)n^4 exp[-pi(n^2-1)exp(2x)].

The last sum is at most 125/121: its n=2 tail term is at most 16e^-9<16/8000 and subsequent ratios are below 1/2, so the entire tail is <1/250<4/121. Thus, with Astar=4pi^2(125/121),

    Phi(x)<=Astar exp(9|x|/2-pi exp(2|x|)),
    m(x)^2<=Astar exp(4|x|-pi exp(2|x|)).

Evenness gives both rays. The directed certificate checks Astar<41; the later analytic comparison needs only Astar<64. The exact Mellin identity integral Phi(x)exp((s-1/2)x)dx=xi(s) and all original-domain identities above are those proved in the cited foundation. No positive-depth gap certificate is used as an input.

## Reproducing the interval certificate

The unique [certificate program](certify_bounded_factor.py) uses Python 3.12.14 and mpmath 1.3.0, as in the executed runs. Run it in this directory with CERT_DPS=35 and CERT_BOX_DENOM=4096. It writes the complete result and all 8192 rational box bounds. [The original 35-digit result](bounded_factor_interval_result.json) is included; an independent 60-digit rerun is included as [bounded_factor_interval_result_60.json](bounded_factor_interval_result_60.json). To reproduce that second run without replacing the first output, copy the same program to a separate directory and run with CERT_DPS=60.

The generated box table has SHA256 c9cabd8cb1e417d6a264f62b025be27cd1f1899c2ff5d6dc009b797e9e6c8276 at BOTH precisions. It is a reproducible output, not an omitted input; the only program inputs are its explicit constants and the two displayed environment parameters. The [certificate manifest](certificate_manifest.json) records all published files and the regenerated table hash. The compact interval checks are combined with the complete analytic exterior and theta/prime tails in Part I; sampling alone would not prove the theorem. [The mathematical review](REFEREE.md) separately audits the analytic proof, the full interval rerun, and Part II's original-domain comparison.

## Part I. Complete bounded positive factor

### 1. Original objects and exact factors

All objects are on the original even physical L2(R). Put
h(x)=cosh(x/2),
Phi(x)=sum_{n>=1}(4pi² n⁴ exp(9x/2)-6pi n² exp(5x/2))exp(-pi n² exp(2x)),
m²=Phi/(2h), e0=sqrt(2hPhi), ||e0||=1,
alpha_n=Lambda(n)/sqrt(n),
Vp=sum alpha_n m(tau_log n+tau_-log n)m,
C0=EulerGamma+pi/2+3log2+logpi.
Phi is evaluated by its even complete theta continuation; on x>=0 every displayed summand is positive. The original H=m b(D)m-C0 m²-Vp has H e0=-e0/2, and K=H+.5|e0><e0|. The public original-domain foundation is linked above.

The complete Gamma jump kernel is k(t)=exp(-|t|/2)/(1-exp(-2|t|)). Set k1(t)=exp(-|t|/2), krem=k-k1. Its first-piece multiplier is b1(t)=4-1/(t²+1/4). For q=v/e0 define the original closed jump forms Eprime(q), EΓ1(q), EΓrem(q). Then

 A=EΓrem >=0,
 B=.5(I-|e0><e0|)-Eprime-EΓ1,
 K=A-B.                                                     (1)

A has the original Gamma form domain because EΓ1 is bounded. B is bounded self-adjoint because the complete positive prime jump form is bounded (its exact diagonal is retained). Both annihilate e0. Every original operator null vector w of K satisfies A w=B w, hence the equality holds in every mixed pairing with an original form-domain column. Quadratic equality alone is not being substituted for this operator statement.

Write
 dp(x)=sum alpha_n[Phi(x+logn)+Phi(x-logn)]/(2h(x)),
 D_B(x)=.5-dp(x)-(k1*Phi)(x)/(2h(x)).
Then the exact bounded factor is

 B=D_B+Vp+m(k1*)m-.5|e0><e0|.                             (2)

No diagonal or prime power is dropped. In particular C=B+.5|e0><e0| obeys C e0=.5 e0.

### 2. A sufficient full-prime scalar certificate

Suppose D_B(x)>0 for every x, and put W(x)=m(x)/sqrt(D_B(x)). If

 r=2 sum_{n>=2} alpha_n sup_x W(x)W(x+logn)<1,               (3)

the complete relative weighted-shift series converges in norm and gives
D_B +/- Vp >=(1-r)D_B. This is a form identity even though D_B has no uniform positive lower bound. More explicitly Vp=D_B^(1/2) T D_B^(1/2), where T=sum alpha_n W(tau_log n+tau_-log n)W converges absolutely in operator norm by(3). No bounded inverse of D_B is asserted or needed. The convolution k1* is positive because its Fourier multiplier is 1/(t²+1/4). Consequently C>=0. Since e0 is a unit eigenvector of C with eigenvalue .5, its orthogonal complement reduces C, and (2) gives B>=0. More precisely, on e0-perpendicular physical vectors,

 B[v]>= (1-r) integral D_B|v|².                            (4)

This is not the general invalid inference that a positive operator remains positive after subtracting a projection. The exact reducing eigenvector is essential.

Even a proof of (3) does not prove A>=B. In particular A has no uniform gap on e0-perp, so an inverse square root or a bounded Birman-Schwinger contraction may not be assumed.

### 3. Exact first-exponential convolution

For x>=0 put Theta(x)=exp(x/2)sum_{n>=1}exp(-pi n² exp(2x)). Then (D²-1/4)Theta=Phi. Theta modularity gives the even decaying solution

 (k1*Phi)(x)=.5exp(-|x|/2)-Theta(|x|).                     (5)

Indeed (-D²+1/4)k1=delta, the expression on the right has no derivative jump at zero (Theta'(0)=-1/4), and solves the same inhomogeneous equation with decay at both ends. This identity eliminates numerical quadrature from D_B.

### 4. Analytic exterior lower bound

The required lower bound is

 D_B(x)> (1/100)exp(-3|x|), |x|>=2.                        (6)

By the original exact diagonal identity,
D_B=(C0-4)m²-(brem(D)Phi)/(2h), where C0-4>0. On x>=2, write
-bremPhi(x)=integral_0^infinity krem(t)[Phi(x+t)+Phi(x-t)-2Phi(x)]dt.
Each theta summand has second derivative
exp(x/2-u)[16u⁴-112u³+165u²-(75/2)u], u=pi n²exp(2x).
It is positive on x>=1, since u>=pi e²>20. Therefore t<=x-1 contributes nonnegatively. On the remainder use integral_(x-1)^infinity krem(t)dt <=.5exp(-5(x-1)/2), and keep only the positive term Phi(x-t), t in[x-1/4,x]. This yields

 -bremPhi(x)>=exp(-5x/2)[integral_0^1/4 Phi(y)dy-exp(5/2)Phi(x)].

The complete first theta term gives Phi>1/8 on[0,1/4]; the complete upper envelope gives Phi(x)<=70exp(-141) for x>=2, so exp(5/2)Phi(x)<1/1000. Since2h<=2exp(x/2), the resulting coefficient is .5(1/32-1/1000)>.01. This proves (6). For example Phi>1/8 follows from u in[pi,pi sqrt(e)] subset[3,6], monotonicity of(4u²-6u)e^-u there, and108e^-6>4/27>1/8. The upper envelope at x=2 uses e^4>50 and then9-3e^4<-141. These estimates retain the full theta series.

### 5. Directed-interval compact certificate and remaining checks

The unique implementing script is certify_bounded_factor.py in this directory. It uses mpmath.iv directed intervals. It partitions[0,2] into dyadic boxes with denominator4096, and records exact rational lower bounds for D_B and upper bounds for W². The test is strict D_B>0 on every box and W²<2. Prime powers n<128 are all included in the diagonal; the remainder is bounded before division by2h by2^-100. For Phi and Theta it retains n=1,2,3 and adds the positive enclosure[0,2^-40]. These are full-theta enclosures, not replacements of the original theta.

Elementary tail ledger: each Phi theta summand with n>=4 decreases on x>=0 and is <=64n⁴ exp(-3n²). The series from4 is <2^-40 (use e³>20 and a geometric ratio below1/2). The Theta tail is smaller. For diagonal primes n>=128 and |x|<=2, both Phi(x+logn) and Phi(x-logn) are <=41 n^(9/2) exp(-n²/27), since e<3. Hence the raw tail is at most82 sum_{n>=128}n⁵ exp(-n²/27)<2^-100. Its first term is below2^-558 and its successive ratio is below1/256.

For (3), all prime powers2<=n<=54 are paid by exact integer maximum pairing of the rational W² box bounds. The interval logn determines all possible shifted boxes; no maximizer-location or concavity assertion is used. If one endpoint is outside[-2,2], (6) and the full theta envelope give

 W(x)<=65 exp(7|x|/2-(3/2)exp(2|x|))<2^-80, |x|>=2.

Together with W²<2 on the compact interval, the product with any other endpoint is <2^-79. For n>=55>exp(4) at least one endpoint has |x|>=.5logn>2, hence the whole remaining sum is at most
200 sum_{n>=55}n³4^-n <2^-70. The elementary numerical premises exp(4)<55, 4pi²(125/121)<41 and exp(3)>20 are also enclosed by the directed script.
This retains every prime power by the larger all-integer sum.

The printed certificate below gives r<4/5. It establishes only B>=0 and(4), not the required A-B>=0. All n>=55 in the tail estimate are integers, so every prime power is included.

### 6. Executed enclosure and exact rational check

The final35-digit directed interval run completed all8192 boxes. It obtained

 D_B>=337582935/10^12 on[0,2],
 W²<=1656527021676/10^12<2 on[0,2].

Including both exterior-endpoint allowances and the full n>=55 allowance, its calculated upper budget U for r has the exact dyadic upper endpoint

 U <=481413283109510196756504807006805137/
       664613997892457936451903530140172288 <4/5.          (7)

The comparison with4/5 is an exact rational comparison. U is an upper budget for the actual relative shift sum, not a two-sided enclosure of that operator norm. The numerical display is U<0.72435021.

Reproducible artifacts (the box table is generated by the included program):

- certify_bounded_factor.py, SHA2561492ad662d0fe82d23ee049f227af927f6b095bc0b73e737c77d5cec5913798c;
- bounded_factor_interval_result.json, SHA2562833016820e98e55d28c38f5df37b1ab179ca7ccd27e29042c1cd16b7967893e;
- bounded_factor_interval_boxes.json, SHA256c9cabd8cb1e417d6a264f62b025be27cd1f1899c2ff5d6dc009b797e9e6c8276.

Therefore the sufficient chain in Section2 gives

 0<=B<=.5(I-|e0><e0|),
 B[v]>=(1/5)integral D_B|v|² for v perpendicular to e0,
 ker B=span(e0).                                         (8)

The upper bound in(8) follows immediately from(1), since Eprime and EΓ1 are positive. The two original-domain factors satisfy K=A-B with A>=0 and B>=0, and the complete known-null family has A w=B w in every mixed pairing. Part I alone does not construct the form-sandwich A^(-1/2)BA^(-1/2), whose domain is addressed in Part II; neither part proves the sign of K=A-B. The outstanding critical assertion remains A>=B.

## Part II. Weighted original-domain bridge and bounded form-sandwich

Keep exactly Part I's A, B, K and original even physical space. Write H0={e0}^perp, rho(x)=exp(-3|x|), p=2hPhi, and k_rem(t)=exp(-5|t|/2)/(1-exp(-2|t|)). The form domain of A is the original maximal Gamma form domain. In this part Z is a scalar integral of a weight, unrelated to the ambient arithmetic scale used elsewhere in the repository. Positivity B>=0 is now the proved conclusion of Part I, rather than a further assumption.

### 1. The complete remainder controls a weighted norm

For q=v/e0 put

    w(x)=Phi(x)exp(-5|x|/2),
    Z=integral w(x)dx,
    L=integral p(x)^2/w(x)dx.

Both Z and L are finite, with Z>0. Since |x-y|<=|x|+|y|,

    krem(x-y)>=exp(-5|x-y|/2)
              >=exp(-5|x|/2)exp(-5|y|/2).

Thus the ORIGINAL complete remainder form satisfies

    A[v]>=(1/2)double_integral w(x)w(y)|q(x)-q(y)|^2 dxdy
         =Z integral w|q-c|^2,
    c=(1/Z)integral w q.                                (1)

Suppose v is perpendicular to e0, equivalently integral p q=0. Since integral p=1,

    c=-integral p(q-c),
    |c|^2<=L integral w|q-c|^2.

Consequently

    integral w|q|^2
       =integral w|q-c|^2+Z|c|^2
       <=(1+ZL)integral w|q-c|^2.

Combining with (1), and using 2h(x)<=2exp(|x|/2), gives

    A[v]>=Z/[2(1+ZL)] integral rho|v|^2.                 (2)

The argument holds on the entire original finite-energy domain. In fact integral w|q|^2 is finite already for physical v in L2, because w/p<=1/2. No cutoff, boundary condition or new test domain is introduced.

Here are deliberately loose explicit constants. The complete first-theta estimate Phi>1/8 on [-1/4,1/4] and e<3 imply Z>1/48. Also Z<=integral Phi<=1/2, since integral 2hPhi=1. The complete Mellin identity is

    integral Phi(x)exp((s-1/2)x)dx=xi(s).

Using h^2<=exp(|x|), positivity, and e^(a|x|)<=e^(ax)+e^(-ax),

    L=4 integral Phi h^2 exp(5|x|/2)
       <=4 integral Phi exp(7|x|/2)
       <=8xi(4)=48 zeta(4)/pi^2<64/9<8.

The last step uses only zeta(4)<1+integral_1^infinity t^-4 dt=4/3 and pi>3. Therefore (2) has coefficient greater than 1/480, and in particular

    A[v]>=2^-9 integral rho|v|^2,  v in D(A^(1/2)) cap H0. (3)

This is a weighted lower bound. It is not a positive uniform spectral gap in physical L2.

### 2. Elementary complete-theta weighted bounds

The original complete envelope is

    Phi(x)<=Astar exp(9a/2-pi exp(2a)),
    m(x)^2<=Astar exp(4a-pi exp(2a)),
    a=|x|, Astar=4pi^2(125/121)<64.

Put

    M0=sup_x exp(5|x|/2)Phi(x),
    M1=integral exp(5|x|/2)Phi(x)dx,
    M2=sup_x exp(5|x|/2)|Phi''(x)|.

The following sufficiently loose bounds will be used:

    M0<4,  M1<3/2,  M2<2^13,
    sup_x exp(3|x|)m(x)^2<4.                            (4)

For M0 and the last bound, set u=exp(2a)>=1. Both are at most Astar times the supremum of u^(7/2)exp(-pi u). Bound this by u^4 exp(-3u), whose maximum is (4/3)^4 exp(-4)<1/16 because e>8/3. Multiplication by Astar<64 proves these two bounds.

The Mellin identity gives

    M1<=2xi(3)=3zeta(3)/pi<3/2,

using zeta(3)<3/2 and pi>3.

For M2, the second derivative of an individual theta term, with U=pi n^2 exp(2a), is

    exp(a/2-U)[16U^4-112U^3+165U^2-(75/2)U].

For U>=pi>3, its absolute value is at most 74 exp(a/2-U)U^4. Hence

    exp(5a/2)|Phi''(a)|
      <=74pi^4 exp(11a) sum_(n>=1)n^8 exp(-pi n^2 exp(2a)).

Uniformly for exp(2a)>=1,

    sum_(n>=1)n^8 exp(-pi(n^2-1)exp(2a))<2.

To check this last elementary bound, the n=2 term is less than 256e^-9<256/20^3, and each subsequent-to-previous ratio is at most (3/2)^8 e^-15<1/2. The entire tail is therefore less than 512/8000<1. Again setting u=exp(2a), and using pi<4,

    M2<148*4^4 sup_(u>=1)u^6 exp(-3u)
       =148*256*64 exp(-6)
       <148*256*64/400<8192=2^13.

Evenness of Phi handles both half-lines. Every theta term is retained in these estimates.

### 3. A weighted upper bound for the exact cancellation potential

The exact identity established in the bounded-factor calculation is

    DB=(C0-4)m^2-(b_rem(D)Phi)/(2h),
    C0=EulerGamma+pi/2+3log2+log pi,
    0<C0-4<4.                                         (5)

We show

    |DB(x)|<2^16 rho(x), for every real x.              (6)

For 0<t<=1, krem(t)=exp(-t/2)/(exp(2t)-1)<=1/(2t). The second-difference estimate and |x|<=|y|+1 for |x-y|<=1 give

    exp(5|x|/2)|2Phi(x)-Phi(x+t)-Phi(x-t)|
       <=t^2 exp(5/2)M2.

The small-jump contribution to exp(5|x|/2)|b_rem(Phi)(x)| is therefore at most exp(5/2)M2/4<27*8192/4=55296.

For t>=1, krem(t)<(7/6)exp(-5t/2). The diagonal part contributes at most M0, because integral_1^infinity krem(t)dt<(1/2)exp(-5/2). For the two off-diagonal parts together, use |x|<=t+|x+t| and |x|<=t+|x-t|. Their domains in y=x+t and y=x-t are disjoint, so their total contribution is at most (7/6)M1, not two times this number. Thus

    sup_x exp(5|x|/2)|b_rem(Phi)(x)|
       <55296+4+7/4=55301.75.

Finally 2h>=exp(|x|/2), so exp(3|x|)/(2h)<=exp(5|x|/2). Combining this with (4)-(5) yields

    exp(3|x|)|DB(x)|<16+55301.75<65536=2^16,

proving (6). In particular this is an original complete-Gamma estimate, not an asymptotic with an unspecified onset.

### 4. Full weighted prime and convolution upper bounds

Let N(x)=exp(3|x|/2)m(x), a bounded multiplier by (4). For z=rho^(1/2)v,

    m v=N z.

The Gamma-one convolution is therefore bounded in the weighted physical norm:

    <v,m(k1*)m v>=<Nz,k1*(Nz)>
       <=4||N||_infinity^2 ||z||^2<16 integral rho|v|^2. (7)

For the complete prime operator, if a=|x|, b=|x+log n| and u=exp(a+b), then u>=n and

    N(x)N(x+log n)
      <=Astar u^(7/2)exp(-pi u)
      <=Astar n^(7/2)exp(-pi n), n>=2.

Here the first step uses exp(2a)+exp(2b)>=2exp(a+b), and the second uses monotonicity for u>=2. Thus the entire weighted shift series has operator norm at most

    2Astar sum_(n>=2)Lambda(n)n^3 exp(-pi n)
      <128 sum_(n>=2)n^4 exp(-3n)<8.                    (8)

For the last inequality, the first term of the series is 16e^-6<1/25, and successive ratios are at most (3/2)^4 e^-3<1/3; hence the series is less than 3/50 and 128*(3/50)<8. The all-integer upper sum includes every prime power. Therefore

    |<v,Vp v>|<8 integral rho|v|^2.                     (9)

### 5. An explicit relative bound on the original domain

Use the exact formula

    B=DB+Vp+m(k1*)m-(1/2)Pi_e0.

Dropping the final nonpositive rank-one term and applying (6), (7), (9) proves, on the entire physical L2 space,

    B[v]<= (2^16+8+16) integral rho|v|^2
           <2^17 integral rho|v|^2.                    (10)

In conjunction with (3),

    B[v]<=2^26 A[v], v in D(A^(1/2)) cap H0.            (11)

The upper comparison (11) is entirely analytic and does not require B>=0. Once the separate complete bounded-factor certificate supplies B>=0, it becomes the genuine two-sided form comparison

    0<=B<=2^26 A on H0.                                (12)

The constants are intentionally coarse. Their role is to prove finite relative boundedness, not the missing threshold-one estimate.

### 6. Construction of the bounded form-sandwich

Now assume the independently certified B>=0. Both A and B annihilate e0 and reduce H0. By (3), ker(A|H0)={0}. The range of A^(1/2) on H0 is therefore dense, although A has no claimed positive uniform gap and A^(-1/2) is not claimed bounded.

On that dense range define

    T(A^(1/2)v)=B^(1/2)v,  v in D(A^(1/2)) cap H0.

This is well-defined and (12) gives ||T||<=2^13. It extends uniquely to a bounded operator on H0. Put

    Q=T* T,  0<=Q<=2^26 I.                             (13)

Equivalently, Q is the bounded extension of the nonnegative form

    q[z]=||B^(1/2)A^(-1/2)z||^2,
    z in D(A^(-1/2))=Ran(A^(1/2)).

This is the precise form interpretation of A^(-1/2) B A^(-1/2). No unsupported everywhere-defined product of unbounded operators is asserted. For every original form-domain v in H0,

    B[v]=<A^(1/2)v,Q A^(1/2)v>,
    K[v]=<A^(1/2)v,(I-Q) A^(1/2)v>.                    (14)

The range is dense, so

    K>=0 on H0 if and only if Q<=I on H0.               (15)

The threshold-one inequality in (15) remains unproved. The bound 2^26 in (13) gives no sign for I-Q and proves no new zero exclusion or RH.

### 7. Exact original nulls remain threshold-one eigenvectors

If w belongs to the original operator domain, w is in H0 and Kw=0, then Aw=Bw. In every original form-domain pairing, (14) implies

    <A^(1/2)v,(I-Q)A^(1/2)w>=0.

Density of Ran(A^(1/2)) gives

    Q A^(1/2)w=A^(1/2)w.                               (16)

For w nonzero, (3) ensures A^(1/2)w is nonzero. Thus even one known exact null already prevents a strict contraction ||Q||<1.

The complete original null family supplies infinitely many such eigenvectors. Explicitly, for j=0,1,2,... set

    f_j=D^(2j)(D^2-1/4)Phi,
    w_j=f_j/m.

These are even physical vectors in the original operator domain: complete-theta derivative bounds imply w_j in L2 and f_j in the logarithmic Fourier domain, while m b(D)f_j is in L2. Differentiating the complete source equation is justified by locally normal convergence of the full prime series. The constant-coefficient source operator commutes with differentiation, and (D^2-1/4)h=0, so H w_j=0. Also <e0,w_j>=2 integral h f_j=0 by integration by parts. Therefore Kw_j=0.

The family is linearly independent. A finite dependence, after multiplying by m and taking Fourier transforms, would say

    (t^2+1/4) P(t^2) Xi(t)=0

for a polynomial P. Since Xi(0)=integral Phi>0, the polynomial vanishes on a neighborhood and hence identically. Because A^(1/2) is injective on H0, its images of the w_j are still linearly independent. Equation (16) therefore gives eigenvalue 1 of infinite multiplicity for Q. In particular Q is not compact, 1 belongs to its essential spectrum, and its essential norm is at least 1.

This identifies a necessary structural feature of any valid threshold-one proof. It does not assert that Q has eigenvalues above 1, or that K has negative spectrum. RH and the original spectral bound are unchanged.
