# An explicit critical-line proportion from causal clipping

16 October 2026. Let N(T) count all nontrivial zeta zeros with
0<Im(rho)<=T, with multiplicity, and let N0,simple(T) count the simple
zeros on Re(rho)=1/2. The complete argument below proves

 liminf_(T->infinity) N0,simple(T)/N(T)
   >= 16693751490453664439209480356677
                          /24783250000000000000000000000000.

This is 0.673590085660825938454782175730664864... . It improves the
[previous independently reproduced nine-point bound](../20261016_nine_point_proportion_certificate/REPORT.md)
by exactly 2.8e-9 in the proportion. The increment is small; no percent-scale
improvement, formal-kernel verification, or literature-priority claim is made.

The proof uses the [sharp causal-square theorem](../20261016_sharp_causal_square/REPORT.md),
the [direct sharp cubic theorem](../20261016_direct_sharp_cubic/REPORT.md),
and the complete [finite clipping interface](FINITE_CLIPPING_INTERFACE.md).
The [reproduction instructions](code/README.md) identify every scalar
input and the already published exhaustive all-gap certificate.

## 1. An elementary numerical triangular-projection constant

Let S(X)(s,t)=sign(s-t)X(s,t) on a continuous interval, and T=(I+S)/2.
For Hilbert--Schmidt kernels the elementary sign identity gives

 S(X)S(Y)=S(S(X)Y+X S(Y))-XY.                               (Q1)

Diagonal sets have measure zero. Also S(X*)=-S(X)* and S is an S2
isometry. Apply (Q1) with X* and X, take the S2 norm, and use Schatten
Holder. Writing a=||SX||4 and b=||X||4 gives

 a^2 <= 2ab+b^2, hence ||T(X)||4 <= (1+1/sqrt(2))||X||4.    (Q2)

All products in this argument are lawful for HS kernels; the resulting
S4 estimate extends by finite-rank density. In particular C4<2.

## 2. A uniform explicit leading causal-square budget

Use the sharp causal-square and direct cubic notation on J=[T+O(1),2T+O(1)],
N=# {rho:T<Im rho<=2T}, L=log T. Thus N~TL/(2pi). Suppose f is fixed,
smooth, nonnegative, a probability, supported on an interval of length less
than one, and ||f||infinity<=F. The following deliberately coarse bound is

 limsup_T ||B_T(f)^2||HS^2/N <= 49 F^4.                     (Q3)

Every error below is o(TL) at the fixed f and fixed lambda<mu<1. There is
no assertion of a uniform starting height as the taper changes.

For the full Gamma block G, its multiplier is
1_(LJ) Omega(xi/L)/L, of supremum 1+o(1). Thus ||G||op<=F(1+o(1)).
Plancherel and the support length at most one give
||G||HS^2<=F^2 N(1+o(1)), hence ||G||4^4<=F^4 N(1+o(1)). By (Q2),

 limsup ||C^2||HS/sqrt(N) <= 4 F^2.                        (Q4)

For Q_RR use the exact reduced kernel from the causal-square proof.
Its coefficient b_q(t) has modulus at most F*(Lambda*Lambda)(q).
Write S(X)=sum_(p^a<=X) log(p)^2/p^a=(1/2+o(1))log^2 X.
The distinct-prime-base terms in the square sum are at most 4S(X)^2;
the one-base terms sum to O(1). Consequently

 sum_(q<=X)(Lambda*Lambda)(q)^2/q <= (1+o(1))log^4 X.

The elementary mean-square bound on J is
(|J|+O(X log X))*sum |coefficients|^2. After the kernel prefactor
1/(2pi L), Plancherel factor 2pi/L, outer bound f(s)f(t)<=F^2,
and t-support length at most one, this proves

 limsup ||Q_RR||HS/sqrt(N) <= F^2.                          (Q5)

For either one of the two mixed quadratic rows, fix its prime-center
endpoint (t for one row, s for the other) before Plancherel. The coefficients
are Lambda(n)/sqrt(n) times a shifted f, bounded by F. The regularized
multiplier obeys

 (1/|J|) integral_J |H(u)|^2 du -> 1/3,
 sup_J|H|+Var_J(H)=O(log T).                                (Q6)

Indeed after rescaling J to [0,1], the explicit formula converges pointwise
to 1/2+(i/(2pi))log((1-x)/x), with an integrable squared-log majorant.
The integral of log^2((1-x)/x) is pi^2/3. Thus the average is 1/3.
Also Var(|H|^2)=O(log^2 T). Integrating every off-diagonal exponential by
parts, and using the same absolute harmonic row bound, shows that the
weighted mean-square off-diagonal is O(X log^C T)=o(TL) after all prefactors.
The diagonal uses sum Lambda(n)^2/n=(1/2+o(1))log^2 X. Therefore each mixed
row has squared norm at most (F^4/6+o(1))N, and in particular

 limsup ||Q_mix||HS/sqrt(N) <= 2 F^2.                       (Q7)

The triangle inequality with (Q4)--(Q7), and the already checked product
errors, proves (Q3). For F<=2, 49F^4<=784<1024. Accordingly each fixed such
window satisfies, for all sufficiently large T,

                 ||B_T(f)^2||HS^2 <= 1024 N.               (Q8)

## 3. Numerical clipping coefficient

Apply the [finite clipping interface](FINITE_CLIPPING_INTERFACE.md) with the dimension bound N,
M=1024, and C4<2. Its coefficient can be taken to be the rational integer

             k=204, since 6(32+16)/sqrt(2)<204.             (Q9)

The resulting proportion inequality, for 0<eta<1/9, is

 P >= [H-B+eta(B-d)-eta^2*41616/(4(1-9eta))]
                   /[1-c+eta c],                          (Q10)

where H=2-C, d=D-3C+2, and c,B are the same window's all-gap certificate.
This is the SAME sharp zero operator: no analytic-height or PSD surrogate
is substituted. For the finite decomposition A=P_simple+Q, the simple
Gram vectors have norm one, tr A=N, rank A<=N, tr Q=N-n, and
n_+(Q)<=(N-n)/2, exactly as in the original trace-energy transfer.

## 4. A fixed smooth inward taper and its complete error budget

Let f0 be the frozen rational cosine window from the published nine-point
certificate, normalized to mass one on [-1/2,1/2]. Its elementary coefficient
bound gives ||f0||infinity<3/2. Let delta=10^(-14), and choose an even
C-infinity cutoff chi with 0<=chi<=1, chi=1 on |x|<=1/2-2delta,
and chi=0 on |x|>=1/2-delta. Choose chi=varphi^2 with varphi smooth
and nonnegative, so the square root of the resulting window is smooth as
well. Define f=f0 chi / integral(f0 chi).
Then f is a fixed smooth probability of width lambda=1-2delta<1,
||f||infinity<2, and

 epsilon=10^(-12),     ||f-f0||1 <= 12delta < epsilon.       (Q11)

The two end collars have total length 4delta, so the lost mass is at most
6delta; normalization doubles the lost mass in L1. No derivative bound
uniform in delta is required in (Q8), and delta is fixed before T grows.

The Fourier transforms satisfy |K-K0|<=epsilon and |K^2-K0^2|<=2epsilon.
The frozen pair weights sum to 15.99999984<16. Thus the same nonnegative
pressures and pair weights certify ALL gaps with

             B=0.00437542, c'=0.00867-32epsilon.            (Q12)

This is not a sampled-gap claim. The [previously reproduced side-condition certificate](verification/side_conditions_320.json) pins the old majorant
margin at greater than 0.06044448 on [-1/2,1/2], its mass at less than
1.789429154<2, and the close-pair floor at exactly the certified lower bound

 beta=13669479/268435456 > 0.0509, for |g|<=theta=17/20.

Since f<=f0/(1-6delta), its pointwise increase is at most
(3/2)*6delta/(1-6delta)<10^(-12). Thus the SAME majorant still exceeds f
by more than 0.06044. The new close floor is at least beta-2epsilon>0.05,
whereas c'<0.009. These explicit margins preserve both side conditions;
no new finite verification of all gaps is needed.

Both windows are probabilities of height at most two and width at most one.
Directly expanding the defining integrals gives

 |C(f)-C(f0)|<=6epsilon,
 |D(f)-D(f0)|<=30epsilon,
 |d(f)-d(f0)|<=48epsilon.                                  (Q13)

For the C square term use |f^2-f0^2|<=4|f-f0|; the double-product term
costs at most 2epsilon. For D the cube costs at most 12epsilon; its
|s-t| f(s)^2 f(t) term costs at most 6epsilon, with coefficient three.

## 5. The literal sharp simple-zero Gram interface

Let x_j=gamma_j L/(2pi) for the simple critical-line zeros in the sharp
height interval. Their exact finite Gram matrix has entries K_f(x_i-x_j)
and diagonal one; its nonzero eigenvalues equal those of P_simple.
Scan the ordered points, greedily pairing adjacent points at distance at
most theta=17/20. The remaining unpaired points have separation greater
than theta. This is the exact interval covered by the certified close-pair
floor, not the larger interval of gaps up to one.

For that separated block, the unchanged nonnegative majorant G has
Fourier support in [-0.85,0.85] and mass Lambda<2. Hence, for every
coefficient vector, direct Fourier expansion gives

 sum_(i,j) a_i conjugate(a_j) K_f(x_i-x_j)
   <= integral G(u)|sum_j a_j exp(2pi i x_j u)|^2 du
   =Lambda sum_j |a_j|^2.

Thus its Gram spectrum lies in [0,2), with no auxiliary analytic-height
or finite-compression operator. The nine-frame telescope has total
index-distance capacity at most two and total pressure at most B per gap.
It gives, for m remaining points of span S,

 2 sum_(i<j)|K_f(x_i-x_j)|^2 >= c'(m-8)-B S.

For m<9 the same lower bound follows from nonnegativity. Therefore the
separated block has phi2 trace at least (1+c')m-B S-8c'. Each paired
2-by-2 block has eigenvalues 1+|K_f(g)| and 1-|K_f(g)|, both in [0,2].
Its phi2 trace is 2+2|K_f(g)|^2 >=2(1+c') by the close-pair floor.
Convex trace pinching of the exact full Gram matrix now proves

 tr phi2(P_simple) >= (1+c')n-B S_total-8c'.                 (Q14a)

Here S_total<=|J|L/(2pi)=N+o(N). This is precisely the sharp finite
interface used in (Q10); there is no smoothing or operator-identification
premise left in this step.

## 6. The exact second moment of the same sharp operator

For completeness the second-moment premise can be obtained directly from
the already checked linear causal reduction, without replacing A by an
energy upper bound. It gives

 tr A^2=2||C-P||HS^2+o(N).

The pure Gamma row is N integral f^2+o(N), by its bounded sharp multiplier
and the smooth-window Fourier commutator (or the same kernel freezing as
in the direct cubic proof). For the prime square, extend d>0 to the full
line with the paid O(X log^C T) collar, then use the bilinear freezing
identity. Its diagonal, together with the prime-square measure
L^(-2) sum Lambda(n)^2/n delta_(log n/L) -> x dx, gives

 2||P||HS^2/N -> 2 integral_0^lambda x integral f(t)f(t+x)dt dx
                 = double-integral |s-t|f(s)f(t) dsdt.

Every off-diagonal is o(N) by the harmonic row estimate. The mixed Gamma/
prime row is o(N) by the degree-one H0 Fourier-product bound at nonzero
frequency log n. Therefore tr A^2=C(f)N+o(N) exactly. The cubic premise
is the separately proved direct sharp cubic theorem, for this same A.

## 7. Exact scalar acceptance

The [finite-cosine Arb certificate](verification/scalar_256.json) gives

 C0=1.32787452315757742243...,
 D0=1.97124747355732153614...,
 d0=-0.01237609591541073115...,
 G0=B-d0-c0*(H0-B)/(1-c0) > 0.01091148.                    (Q14)

These displayed decimals are descriptive; the certified balls and exact
rational input must be used by the final arithmetic checker.

Take eta=1/2000000, epsilon=1/10^12, c'=c0-32epsilon.
Insert H>=H0-6epsilon and d<=d0+48epsilon in (Q10).
The exact rational/ball calculation certifies that this lower bound exceeds

 P_star + 28/10^10,
 P_star=16693751421060564439209480356677
                     /24783250000000000000000000000000.   (Q15)

The Arb calculation passes independently at 256, 320 and 384 bits;
[256-bit](verification/scalar_256.json), [320-bit](verification/scalar_320.json)
and [384-bit](verification/scalar_384.json) outputs are included. The
coarse lower ball is 0.673590085712730284759890774276392825... and its
slack above (Q15) is greater than 5.1904346305e-11. Exact input and builder
hashes, not these descriptive decimal strings, fix the reproducible check.
The certified increment is only 2.8e-9 in the zero proportion, not a
percent-scale gain. No formal-kernel verification or priority claim is made.

A dyadic interval lower proportion passes to the global liminf by summing
fixed dyadic intervals above the asymptotic starting height; the finitely
many lower labels contribute o(N(T)). Each taper and eta is fixed first.
