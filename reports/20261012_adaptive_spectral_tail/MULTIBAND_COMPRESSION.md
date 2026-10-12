# Physical-first multiband compression of the exact full-Gamma base

Status: independently reviewed and frozen. The referee independently reran both interval programs; all covers and all four complete norm budgets passed. This is a new finite-rank approximation of the original full operator. The parameter instances below do not calculate a resolvent Gram or certify its sign. The already reviewed 373-dimensional full-Gamma Gram instance uses a different finite space and is not silently transferred to these smaller spaces.

The original objects and complete prime-tail proof are [REPORT.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261012_adaptive_spectral_tail/REPORT.md), and the joint-accuracy source estimate is [POLYNOMIAL_ACCURACY_TAIL.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261012_adaptive_spectral_tail/POLYNOMIAL_ACCURACY_TAIL.md). The signed-Gram counting theorem is proved in [ACTUAL_FULL_GAMMA_CERTIFICATE.md, Appendix A](ACTUAL_FULL_GAMMA_CERTIFICATE.md#appendix-a-one-sided-upper-gram-bounds-with-an-indefinite-finite-matrix). The latter report supplies the separate executed 373-dimensional example; this report supplies only approximation bounds for its own different spaces.

## 1. Exact hard-frequency base

Work on the original even complex Hilbert space H=L2_even(R,dx), with H_original=B−V, B=m b(D)m, and the previously established actual theta multiplier m. Write C=C_N for the real even finite-prime Fourier symbol and c=c_N for its uniform absolute upper bound. Retain the literal complete Gamma symbol b. The original prime tail satisfies ||V−m C(D)m||<=delta_N. In the original spectral range 0<epsilon<=1/2 with delta_N<epsilon, put e=epsilon−delta_N>0. This range makes the logarithms in the reviewed bound (3) well-defined.

Fix 0<sigma<1. Suppose E is a finite symmetric union of bounded frequency intervals satisfying

 {t: C(t)>(1−sigma)b(t)} subset E.                         (1)

Endpoints are immaterial. Define the exact bounded low-frequency multiplier and the exact base by

 h(t)=1_E(t) C(t),
 d(t)=b(t)−1_(R\E)(t) C(t),
 A=m d(D)m+e.

On E, d=b. Outside E, (1) gives d>=sigma b. Thus A>=e and

 B−m C(D)m = m d(D)m−m h(D)m,
 H_original+epsilon >= A−m h(D)m.                         (2)

There is no smooth-frequency-window error. The jumps at the endpoints of E are bounded multiplier perturbations: A and B have the same operator domain and the same operator cores. The whole Gamma tail and all finite-prime translations are retained exactly.

Let J=m A^−1/2 and K=J* h(D)J. From the reviewed original source-resolvent bound one may use

 ||J||<=M,
 M^2=min{Astar exp(−pi)/e, (10/sigma) R_e^2},
 R_e=max{1, (1/2)log[(2/pi)log(Astar/e)]}.                 (3)

An upward integer bound for M^2 is also valid. For R>=0 let P_R be multiplication by 1_[−R,R], and write

 tau_R=m_tail(R)/sqrt(e),
 m_tail(R)=sqrt(Astar) exp[2R−(pi/2)exp(2R)].

The actual theta envelope and A>=e give ||(1−P_R)J||<=tau_R. Hence

 ||K−J* P_R h(D)P_R J|| <=2cM tau_R.                     (4)

Indeed expand the difference as J*(1−P_R)h(D)J + J*P_R h(D)(1−P_R)J and use ||h||_infinity<=c. Spatial truncation is applied before the frequency kernel, directly to J. Consequently no spatial tail of a sharp Fourier projection is needed.

The original Birman–Schwinger operator is compact: h has compact support and m belongs to L2, so |h|^1/2 F m is Hilbert–Schmidt; multiplication by A^−1/2 is bounded. This statement is independent of the finite approximation.

## 2. Positive-frequency feature map and exact carriers

Write the positive part E_+ as disjoint intervals I_i=[a_i,b_i], allowing a_0=0. For even functions use the unitary even Fourier convention

 (F_even f)(t)=(1/sqrt(pi)) integral_R cos(tx) f(x)dx, t>=0.

Define Q_R=|h|^1/2 F_even P_R and S=sign h on E_+. Then

 P_R h(D)P_R=Q_R* S Q_R,  ||Q_R||<=sqrt(c).               (5)

For a band with a_i>0 set nu_i=(a_i+b_i)/2 and w_i=(b_i−a_i)/2. For a positive integer n_i, expand cos((nu_i+s)x) in the real variable s through degree n_i−1:

 T_i(t,x)=sum_(k=0)^(n_i−1) [(t−nu_i)^k/k!]
                              x^k cos(nu_i x+k pi/2).

All functions of x displayed here are even, including the odd-k terms. Taylor's theorem for the real cosine gives, uniformly on I_i times [−R,R],

 |cos(tx)−T_i(t,x)| <=beta_i,
 beta_i=(R w_i)^n_i/n_i!.                               (6)

There is no exponential factor in this real oscillatory remainder. The potentially large center nu_i is kept as an exact carrier, and does not enter beta_i.

For the band [0,b_0], choose n_0=2r_0 and nu_0=0. The odd Taylor coefficients vanish, so only r_0 even monomials are needed, with

 beta_0=(R b_0)^(2r_0)/(2r_0)!,  rank contribution r_0.  (7)

Let Q_p be the feature map obtained by replacing cos(tx) by the appropriate T_i(t,x). Its rank is at most

 r=r_0+sum_(i>0) n_i.                                   (8)

If zero does not lie in E, omit r_0. Since the frequency intervals are disjoint, the literal Hilbert–Schmidt kernel estimate is

 ||Q_R−Q_p||^2 <=||Q_R−Q_p||_HS^2 <=zeta^2,
 zeta^2=(2R/pi) sum_i [integral_(I_i) |h(t)|dt] beta_i^2.
                                                                  (9)

The factor 2R is the length of the original full spatial interval; the factor 1/pi comes from the even Fourier normalization. One may replace each integral by c(b_i−a_i).

Define the actual finite-rank operator K_p=J* Q_p* S Q_p J. From (5),(9), ||Q_p||<=sqrt(c)+zeta, so

 ||K−K_p|| <=2cM tau_R + M^2[2sqrt(c)zeta+zeta^2].       (10)

This is a full norm bound on the original even Hilbert space. It allows signed h. No critical source-domain assumption, discretized eigenvalue, or Gamma truncation has entered the proof.

## 3. The changed true finite Gram

For each noncentral band define the compactly supported, even basis functions

 phi_(i,k)(x)=1_[−R,R](x) x^k cos(nu_i x+k pi/2)/k!.

For the central band keep only even k. Let F be the column map with columns m phi_(i,k). These functions are in the original L2 space; they are not asserted to be in D(B). They are inputs to a resolvent, not trial vectors for applying A.

With s=t−nu_i, define a block-diagonal real symmetric matrix

 D_(i,k),(i,l)=(1/pi) integral_(I_i) h(t) s^(k+l)dt,
 D_(i,k),(j,l)=0 for i!=j.                               (11)

The central block uses nu_0=0 and only its even indices. Equations (5) and the polynomial feature definition give the exact factorization

 K_p=A^−1/2 F D F* A^−1/2,
 G=F* A^−1 F.                                          (12)

The block structure in (11) comes only from disjoint frequency-feature intervals. The full original carrier functions are not orthogonal, and every cross-band entry of G in (12) is retained. In particular no prime-translation interaction is discarded by imposing a block-diagonal resolvent Gram. The basis need not be orthogonal and may be rescaled by any explicitly recorded nonzero factors. The reviewed one-sided signed Gram inertia certificate therefore applies directly to this changed G,D. A matrix sign from the previous global Legendre space is not a certificate for (12).

All entries of D are integrals of a finite trigonometric polynomial times a polynomial over rational endpoints, so they have explicit finite recurrences or interval integral evaluations. A future actual certificate must additionally enclose the true resolvent Gram, for example by genuine operator-domain trial vectors and whole-line residuals. The input m phi has a finite endpoint jump; the previous analytic-strip input envelope for m rho(D)e_j cannot be reused for it. Endpoint effects or a separately controlled smooth-input replacement must be paid explicitly.

## 4. Actual interval certification of the frequency sets

The attached certify_frequency_well_cover.py constructs covers for N=3,4,7, with sigma=1/100, using exact dyadic intervals. It does not infer a sign from sampled values.

For t>=0 the complete Gamma multiplier is increasing and satisfies

 b(t)>=sum_(j=0)^31 [(t/2)^2/((j+1/4)((j+1/4)^2+(t/2)^2))]
            +(1/2)log[1+(t/(2(32+1/4)))^2] = b_low(t).  (13)

The tail bound follows by integrating the positive decreasing summand as a function of j+1/4 from 32+1/4 to infinity. On every candidate interval [a,b], outward interval cosine evaluation encloses C([a,b]); consequently

 sup_(t in[a,b]) [C(t)−.99 b(t)]
       <=upper(C([a,b])−.99 b_low(a)).                  (14)

A strictly negative interval upper bound discards the entire cell. Other cells are bisected until their length is 1/8, when they are included in E_+. Adjacent retained cells are merged. The initial positive ranges are [0,128], [0,256], [0,4096] for N=3,4,7. Beyond the initial endpoint, the script verifies .99 b_low(endpoint)>c_N and uses monotonicity to exclude the whole infinite tail.

The actual covers have these exact properties:

 N=3: 7 intervals, total positive length 110/8, last endpoint 370/8;
 N=4: 10 intervals, total positive length 134/8, last endpoint 873/8;
 N=7: 60 intervals, total positive length 456/8, last endpoint 12402/8.

Every endpoint is saved as an integer divided by eight. These are conservative covers; extra intervals are allowed. They are not claimed to be the exact connected components of the positive set. All special values and all sign comparisons are enclosed in 50-decimal-digit mpmath.iv arithmetic.

## 5. Actual full-norm parameter budgets

The attached certify_multiband_kernel_budgets.py uses the above actual frequency covers, e=epsilon−delta_N, sigma=1/100, and eta=epsilon/4. The complete-prime tail is still paid in e. It selects an actual R with 2cM tau_R<eta/2, then chooses Taylor orders using (9),(10), with all final comparisons against exact rational thresholds.

The completed interval calculations give:

 epsilon=1/8: N=3, R=107/100, M^2<=15, rank<=58,
 whole norm error <0.019648 <1/32;

 epsilon=1/64: N=3, R=123/100, M^2<=167, rank<=77,
 whole norm error <0.001882 <1/256;

 epsilon=1/1024: N=4, R=136/100, M^2<=1000, rank<=127,
 whole norm error <0.00011615 <1/4096;

 epsilon=1/1048576: N=7, R=156/100, M^2<=4000, rank<=853,
 whole norm error <0.00000010754 <1/4194304.

The corresponding previously certified smooth-window global-polynomial budgets were 373,517,858,17332. The reduction arises from changing the exact approximation ordering and retaining the individual frequency carriers, rather than merely lowering the precision requirement.

For each band the output records its exact endpoints and Taylor remainder order. The spaces, changed base, and finite matrices are different from the previously executed 373-dimensional certificate. No entry of the new true Gram is supplied here, and no new spectral gap or all-epsilon sign is inferred from these parameter budgets.

## 6. General joint-accuracy scope

For all sufficiently small epsilon one can use a single frequency interval E=[−T,T] with b(T)>=c_N/(1−sigma). The same proof then gives a physical-first even-polynomial approximation without any window regularity cost. With N=O(log(1/epsilon)), c_N=O(sqrt(N)log N), T=exp(O(sqrt(log(1/epsilon))loglog(1/epsilon))), the established source bound and theta tail permit R=O(loglog(1/epsilon)). For eta=C epsilon^a, a fixed positive a, choosing the even Taylor order of size O(TR+log(1/eta)+log M) gives rank epsilon^(−o(1)). This is a rank existence estimate, not a runtime or finite-matrix sign theorem. The certified multiband covers in Section 4 improve four concrete budgets without assuming an unproved general density law for the arithmetic frequency set.

Reproduce the parameter certificates in [multiband_certificate](multiband_certificate):

    python certify_frequency_well_cover.py
    python certify_multiband_kernel_budgets.py
