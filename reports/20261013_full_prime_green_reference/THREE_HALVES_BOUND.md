# A three-halves bound for the complete reflected-prime Green operator

For the original full-prime Green map K=TT* on its entire current space K_N,

    0 <= K <= (3/2) I.

Equivalently, the original complete energies satisfy N[r] <= (3/2) P[r] on their actual common ratio-core completion, and Gamma_P[h] <= (3/2)||h||_N² for every reflected-prime current. Every prime power and the coefficient-two source pole are retained.

This excludes the complete Green spectral range lambda>=3/2. The remaining critical problem is K<=I; possible excess in (1,3/2) is not excluded. No equality of the known theta-gradient span with an entire kernel is assumed. The proof uses the established rigorous verification of the Riemann zeros up to height 3*10^12 through the original physical finite-height theorem. It performs no new zeta-zero verification and does not prove RH.

The argument is a direct comparison with the original odd physical operator, rather than a finite-current approximation. Its scalar enclosures and all infinite tails are proved below.

## 1. Exact source and parity interface

Use the user's full reflected-prime Green operator K=TT*, with P and N as in the full-prime Green reports. All prime powers are retained. The published compact-positive-excess theorem implies that spectrum strictly above one consists of finite-multiplicity eigenvalues, with accumulation possible only at one. For a hypothetical eigenvalue lambda>1, the corresponding T*T eigen-source has a pole-centred representative r, normalized by P[r]=1. Put

    gamma=lambda-1, delta=gamma/lambda,
    g=psi r, psi=-Phi'>0 on x>0,
    L(x)=sum_(log n>x) alpha_n psi(log n-x),
    mu²=psi/L, v=g/mu, u=g_o/m,
    m²=Phi/(2 cosh(x/2)), alpha_n=Lambda(n)/sqrt n.

Then N[r]=lambda, integral sinh(x/2)g=0, and the complete odd source identity is

    H_o[u]=P[r]-N[r]=-gamma.                     (1)

The source-tail paper proves v is in its actual auxiliary operator domain and H_delta v=-2delta v. It also places g_o in the full logarithmic source form. The bounds below prove u in L²; hence u belongs to the original odd physical form domain, not merely an auxiliary completion. The full bounded physical prime operator identifies the same source pairing in (1). No H² condition on the original source is needed.

The published original finite-height argument has the same constants on the odd physical block:

    H_o >= -1/100000.                            (2)

For clarity, the change in its proof is exactly this. For an actual odd negative-band vector u and F(z)=integral m(x)u(x)exp(izx)dx, the complete quadratic Weil formula is

    H_o[u]=sum_z j_z F(z)overline(F(bar z))
               +2|integral sinh(x/2)m(x)u(x)dx|².

The last term is nonnegative. All low critical-zero terms are |F(real z)|². The complete high-zero estimate and every original second-derivative, Lyapunov, theta and paired-prime constant are parity-blind; even Fourier regularizers preserve the odd block. The same certified strict test at height 3*10^12 therefore excludes its band below -10^-5. The original odd-domain report independently supplies the graph-core and parity extension. This does not give that lower bound to the pole-inclusive form by subtracting the rank-one pole.

Combining (1) and (2),

    gamma <= 10^-5 ||u||².                       (3)

## 2. A deliberately coarse reference budget

The existing reference R=P_pole+P_F,2 is transported by D_R=w+c+c(.−log2) to a Jacobi operator with entries beta_k. Appendix A proves the scalar certificates

    rho=sup_t ||A_t|| <=2/3+1/1000,
    sup_(x>0) psi(x)L(x)/D_R(x) <=64.

These imply, for every pole-centred source,

    ||v||² = integral psi L |r|² <=193 P[r]=193. (4)

This follows on the actual completion from the reference inverse/core theorem. Appendix A includes the complete theta and prime tails and the infinite Jacobi-fiber estimate; the constant is not inferred from a finite numerical matrix.

## 3. Scalar theta and prime-row certificates

The supplied directed-interval script checks, with complete theta tails,

    ||mu||infinity <=4,
    L(x)>=2^-6 exp(-x/2), x>=0,
    mu(x)²/m(x)² <=128, 0<=x<=7/5.               (5)

For the row lower bound it is enough to use one genuine prime power 2^j with

    1/128 <= j log2-x <=1/128+log2.

The script certifies log2 exp(-t/2)psi(t)>1/64 throughout the slightly larger rational interval [1/128,90/128]. For the central bounds it uses only the positive row terms n=2,3,4,5,7,8,9,11,13,16 as lower bounds. Terms crossing their threshold are set to zero in the lower enclosure, never continued to a negative argument. Complete psi positivity makes every omitted term nonnegative.

The complete theta expression is

    Phi(x)=exp(x/2) sum_n (4u_n²-6u_n)exp(-u_n),
    psi(x)=exp(x/2) sum_n (8u_n³-30u_n²+15u_n)exp(-u_n),
    u_n=pi n²exp(2x).

For n>=5, the omitted summands are positive and decreasing in x>=0. Using 3<pi<4 and their geometric n-ratios, their total Phi and psi tails are respectively at most 80000exp(-75)<10^-26 and 16000000exp(-75)<10^-24. These tails are added outward in every interval evaluation. The tests are comparisons of directed intervals, not sampled extrema.

Also, for all x>=0,

    psi(x)<=256 exp(13x/2-pi exp(2x)),
    Phi(x)>=2pi² exp(9x/2-pi exp(2x)).

For the upper bound, discard the two lower polynomial terms and use
sum n^6 exp[-pi(n²−1)]<65/64 and 8(22/7)^3(65/64)<256. The Phi lower bound is the unchanged foundation bound. Consequently, with

    M(x)=128 exp(7x/2-pi exp(2x)/2),

we have

    mu(x)<=M(x),
    mu(x)²/m(x)²<=2048 exp(3x).                  (6)

M is decreasing for x>=1. The central interval test actually covers [0,45/32], which contains [0,7/5]; its tail value M(7/5)<1/12 proves the global ||mu||infinity assertion in (5).

## 4. Explicit complete row tail for the actual auxiliary equation

Let R>=7/5, a=exp R>4, and M_R=M(R). The source-tail paper's core-legal exterior estimate gives, for arbitrary normalization,

    integral_R^infinity |v|²
      <= ||v||² [D_delta(R)+E_N(R)]²/(4delta²). (7)

Here D_delta contains the full constant term, rank-one pole, both forward rows, and every reflected prime row; E_N<=4pi||mu||infinity mu_R is the actual odd Gamma cross estimate. We claim the complete explicit bound

    D_delta(R)+E_N(R)<=256 exp(R) M_R.            (8)

The details are as follows.

* The constant term is at most 12M_R²<=M_R. The Gamma cross term is at most 64M_R.
* Write e_N=sinh(x/2)mu(x). The bounds ||mu||infinity<=4 and (6) give ||e_N||₂<2: on [0,1] use 16 integral sinh²(x/2)<8/3, and on [1,infinity) use 4096 integral exp(8x-pi exp(2x))<1/4. For R>=7/5,

      ||1_(x>R)e_N||₂ <=(1/2)exp(R/2)M_R,

  by integration with derivative denominator 2pi exp(2R)-8>1. Thus the rank-one row is at most 8 exp(R/2)M_R.
* The elementary complete Chebyshev bound gives A(X)=sum_(n<=X)alpha_n<=6sqrt X. For both forward rows, n<=a contributes at most 96sqrt(a)M_R. For n>a, the global shift coefficient is at most 4M(log n). With F(t)=128t^(7/2)exp(-pi t²/2), Stieltjes integration and -F'/F>=a for t>=a give

      sum_(n>a)alpha_n F(n)<=9sqrt(a)F(a).

  The two complete forward tails thus contribute at most 144sqrt(a)M_R. Their combined bound is 240sqrt(a)M_R.
* Reflected labels n<=a² cost at most 48aM_R. For n>a², the complete product envelope is

      b_n <=2^14 n^(7/2)exp(-pi n).

  For B(t)=2^14 t^(7/2)exp(-pi t) and t>=a²>=16, one has -B'/B>=2, so integral_(a²)^infinity B(t)/sqrt(t)dt<=B(a²)/(2a). Applying the Stieltjes argument with this bound gives the remaining reflected row at most 18a*2^14 a^7 exp(-pi a²). Its ratio to aM_R is 2304a^(7/2)exp(-pi a²/2), which is below 294912exp(-24)<1 for a>=4. Thus the entire reflected contribution is at most 49aM_R. The factor 1-delta has only been bounded above by one.

The sum is [65+248sqrt(a)+49a]M_R<=190aM_R<256aM_R, proving (8). None of these estimates truncates the original operator; the infinite labels are paid by their complete Stieltjes tails.

Equations (7) and (8) give

    V_tail(R)<=2^28 delta^-2 ||v||²
                         exp(9R-pi exp(2R)).          (9)

## 5. Original physical norm and the actual exclusion test

By (6), integration by parts against the nonnegative tail in (9) gives

    integral_R^infinity (mu²/m²)|v|²
      <=2^40 delta^-2 ||v||² exp(12R-pi exp(2R)),       (10)

for R>=7/5. Indeed the integral of exp(12x-pi exp(2x)) beyond R is at most its initial value divided by 2pi exp(2R)-12>=84; the integration-by-parts bracket costs 1+3/84<2.

The directed scalar test gives

    2^40 exp(84/5-pi exp(14/5))<1/1000.                (11)

Thus, if lambda>=3/2, then delta>=1/3 and (4),(5),(10) give

    ||u||²=2 integral_0^infinity (mu²/m²)|v|²
      <=2*193*(128+9/1000)=24705737/500<50000.                    (12)

The full-line factor two is retained. Combining (3) with (12) gives gamma<1/2, contradicting gamma=lambda-1>=1/2. This excludes every lambda>=3/2. Compactness of positive excess then gives the full operator bound K<=3I/2 on every current, including the known theta complement, rather than a finite-current statement.

The coefficient-one target K<=I remains open. The result retains the entire Green space and its actual source normalization; it is not a claim that any Riemann zero beyond the existing verified height has been excluded.


# Appendix A. The explicit centered reference bound

Use the existing full reflected-prime reference theorem and its actual ratio-core completion. All integrals below are on the positive half-line. Let d=log 2, alpha=(log 2)/sqrt 2, a=2 alpha, psi=-Phi',

w=psi sinh(x/2), c=a psi(x)psi(x+d), D=w+c+1_(x>d)c(x-d),
L(x)=sum_(log n>x) Lambda(n)n^(-1/2)psi(log n-x).

The source theorem proves psi>0 for x>0, psi(0)=0, and, for pole-centered r (integral wr=0),

(1-rho) integral D|r|² <= R[r] <= P[r],
R=P_pole+P_F,2,
rho=ess sup_(0<t<d) ||A_t||,
(A_t)_(k,k+1)=beta(t+kd), beta(x)=c(x)/sqrt(D(x)D(x+d)).

It also identifies this inequality with the original centered completion. We give explicit full-tail bounds rho<=2/3+1/1000 and psi L/D<64. Since v=(psi r)/mu and mu²=psi/L, these prove

||v||²=integral psi L|r|² <=193 P[r].

No prime truncation or finite-fiber hypothesis is imposed.

## A.1. Full theta bounds and interval enclosures

Put y_n=pi n² exp(2x). The exact derivative formula is

psi(x)=exp(x/2) sum_(n>=1) (8y_n³-30y_n²+15y_n)exp(-y_n).

For x>=0, each positive upper summand is bounded by

572 n^6 exp(13x/2-3n²exp(2x)),

using 3<pi<4, discarding -30y_n², and exp(5x/2)<=exp(13x/2). For n>=5 the exact summands are positive. The displayed upper envelope decreases in x>=0 for those n, and its successive n-ratio at x=0 is at most (6/5)^6 exp(-33)<1/2. Thus the complete omitted theta tail after n=4 lies in

[0, 2*572*5^6 exp(-75)].

Every compact interval evaluation uses the four exact summands and this outward tail. No sampled-value positivity is substituted for the known exact positivity theorem.

A useful global envelope follows from

sum_(n>=1) n^6 exp[-3(n²-1)u] <5/4, u>=1.

Indeed the n=2 term is 64 exp(-9)<1/8, and each subsequent ratio is at most (3/2)^6 exp(-15)<1/2. Consequently

psi(x)<=1000 exp(13x/2-3exp(2x)), x>=0.                 (A)

The attached interval program partitions [0,1] into 4096 closed cells and bounds psi throughout each cell, obtaining an upper bound below 2.473<3. Envelope (A) is decreasing above 1 and its value at 1 is below 3. Therefore psi<=3 globally.

All decisions in the program compare exact rational representations of outward interval endpoints to rational targets. The readable decimal summaries are not used as decisions. The enclosure engine is mpmath.iv, with a 45-decimal run and a separate 75-decimal rerun. These are reproducible interval computations, not a claim of a formally verified arithmetic implementation.

## A.2. Complete prime row

Use the elementary complete Chebyshev bound sum_(n<=X)Lambda(n)<=3X. In the shell j<=log n-x<j+1,

sum alpha_n <=3 exp(x/2+j/2+1).

For j=0, sup psi<=3. For every integer j>=1, envelope (A) gives

exp(j/2) sup_[j,j+1] psi <=1000 exp(7j-3exp(2j)).

The successive ratio is at most exp(7-3(exp(2)-1)exp(2))<1/2, and therefore the sum over j>=1 is at most 2000 exp(7-3exp(2))<1/1000. It follows that

L(x)<=3e(3+1/1000)exp(x/2)<25exp(x/2).

For x>=2, D>=psi sinh(x/2), so

psi L/D <=50/(1-exp(-x)) <=50/(1-exp(-2))<64.          (B)

For 0<=x<=2 the interval program evaluates every prime-power label through 64, with Lambda(p^j)=log p, and includes the full remaining tail. Since log65-2>1 and exp(4)<55, envelope (A) gives for n>=65

alpha_n psi(log n-x)<=1000 n^7 exp(-3n²/55).

Here log n<=n and exp(-13x/2)<=1 were used; the bound is deliberately loose. The successive ratio is at most (66/65)^7 exp(-393/55)<1/2. The complete omitted tail is therefore at most

2000*65^7 exp(-3*65²/55)<2^(-200).

The exact canceled ratio is

psi L/D = L/[sinh(x/2)+a psi(x+d)+a psi_+(x-d)],

where psi_+(s)=psi(s) for s>0 and zero otherwise. It has a continuous limit at zero. For intervals crossing a threshold, the enclosure evaluates psi on [0,b] and includes zero, rather than continuing the source to negative arguments. On 4096 closed cells covering [0,2], the program proves the denominator strictly positive and bounds the complete ratio above by less than 5.868<64. Together with (B), this proves the global bound.

## A.3. Infinite Jacobi fibers

For 0<=t<=d, dropping only the nonnegative c(t+d) term from D(t+d) gives

beta(t)² <= a² psi(t)psi(t+d) /
 [(sinh(t/2)+a psi(t+d)) (sinh((t+d)/2)+a psi(t))].

This expression has its continuous endpoint value at t=0. On 4096 cells covering [0,d], its denominator has a strictly positive interval lower bound and its upper bound is less than 0.404<4/9. Hence beta_0(t)<2/3 uniformly.

For x>=d, use D>=w. Since a<1, psi(x)<=3, and x+d>=2d, the decreasing envelope (A) gives

psi(x+d)<=1000*2^13 exp(-48)<10^(-12).

Also sinh(d/2)=1/(2sqrt2)>1/3 and sinh(d)=3/4. Thus

beta(x)² <=a² psi(x)psi(x+d)/[sinh(x/2)sinh((x+d)/2)]
          <12*10^(-12)<10^(-6),

so every beta_k with k>=1 is below 1/1000. The complete infinite Jacobi row sums are bounded by 2/3 for row zero, 2/3+1/1000 for row one, and 2/1000 thereafter. The Schur test gives

rho <=2/3+1/1000<3/4.

This bound controls every fiber and its entire infinite tail.

## A.4. Completion and normalization

The established reference theorem extends the fiber identity to L²(D dx), with centered representatives satisfying integral wr=0. On that subspace R=Rhat, since Rhat-R=8|integral wr|². Its core-density argument preserves this centering, and the full P completion embeds in the centered reference completion. Consequently the preceding scalar inequalities apply to every actual full-P source, not merely smooth ratios:

||g/mu||²=integral psi L|r|²
 <=64 integral D|r|²
 <=64/(1-rho) R[r]
 <=193 P[r].

Here 64/(1-rho)<=192000/997<193. The last integer is intentionally coarse. In particular P[r]=1 implies the positive-half-line norm ||v||²<=193. This statement makes no full-line factor-two identification and proves no coefficient-one Green comparison.


## Sources and reproducibility

The exact original objects and closed realizations are in the [full-prime Green report](REPORT.md), [positive reference inverse](REFERENCE_INVERSE.md), [supercritical source and core-legal tail theorem](../20261013_supercritical_source_tails/REPORT.md), and [odd original-domain theorem](../20261013_odd_operator_domains/REPORT.md). The spectral endpoint argument uses [compactness of the complete positive Green excess](../20261013_compact_green_excess/REPORT.md), whose proof works on the full gradient completion. Positivity and tails of psi are proved in the [reflected-prime energy report](../20261013_reflected_prime_energy/REPORT.md).

The physical estimate (2) uses the unchanged constants and executed certificate in [FINITE_HEIGHT_GAP.md, Parts I–III](../20261012_adaptive_spectral_tail/FINITE_HEIGHT_GAP.md). Its sole parity modification is proved in Section 1 above. The external complete-height input is [Platt and Trudgian, Theorem 1](https://arxiv.org/pdf/2004.09765), conservatively used at 3*10^12.

The necessary scalar certificate programs are [certify_green_reference.py](certify_green_reference.py) and [certify_green_physical_tail.py](certify_green_physical_tail.py). They use directed interval arithmetic from mpmath.iv (tested with mpmath 1.3.0). The reference program uses 4096 closed cells in each of its three compact tests; all omitted prime and theta labels are bounded by the explicit complete tails in Appendix A. The physical program adaptively partitions exact dyadic covers and includes its full theta tails. Readable decimal summaries are not used for pass/fail decisions.

Run from this directory:

    REF_DPS=75 python certify_green_reference.py
    python certify_green_physical_tail.py > green_physical_tail_result.json

The actual outputs are [green_reference_result_75.json](green_reference_result_75.json) and [green_physical_tail_result.json](green_physical_tail_result.json). They record outward rational endpoints, precision and all scalar comparison results. The independent reference run at 45 digits and the 75-digit rerun both passed; the physical run at 40 digits also passed. These are reproducible directed-interval certificates, not a claim of a formally verified interval-arithmetic implementation.
