# Whole-packet smoothing and finite-active frames for the complete odd Green operator

For every actual dyadic supercritical Green band, this report proves a depth-independent H^s source bound for s<1/16 in the original P metric. On the full band A>=1+epsilon, the squared source and complete zero-sampling bounds cost only O(log(e/d_min)), where d_min=epsilon/(1+epsilon). A positive Sylvester inverse handles the noncommuting spectral depth. The resulting finite-active lower frame retains half of the complete matrix A-I and every positive zero term.

This is an actual odd Green whole-packet statement. It supplies no matching upper signed comparison, coefficient-one bound, or new zero exclusion, and does not identify this packet with the original even physical negative band.

## Inputs and fixed conventions

The original centered source map, its bound ||V||^2<=193, and the dimension-free full-band exterior estimate are proved in [the complete Green-band theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4083b39d557f10ffcf9395c8ae55ff4bcf6be824/reports/20261013_full_prime_green_reference/WHOLE_SUPERCRITICAL_BAND.md) and [its explicit logarithmic source-cost proof](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4083b39d557f10ffcf9395c8ae55ff4bcf6be824/reports/20261014_green_band_log_cost_candidate/GREEN_BAND_LOG_COST.md). The compact-propagation Poisson operators, true-weight comparison, complete reflected commutator, and full Gamma/prime frequency calculation used here are proved in [Source smoothing](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4083b39d557f10ffcf9395c8ae55ff4bcf6be824/reports/20261013_supercritical_source_tails/SOURCE_SMOOTHING.md). The local graph-domain input used only for the common core approximation is [Origin graph domain](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4083b39d557f10ffcf9395c8ae55ff4bcf6be824/reports/20261013_supercritical_source_tails/ORIGIN_GRAPH_DOMAIN.md). The original signed orbit conventions and core zero identity are in [Signed zero pairing](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4083b39d557f10ffcf9395c8ae55ff4bcf6be824/reports/20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md).

Explicitly, psi=-Phi'>0 on the positive wing, d_n=log n, alpha_n=Lambda(n)/sqrt(n),

    L(x)=sum_(d_n>x)alpha_n psi(d_n-x), mu^2=psi/L,
    (Rv)(x)=sum_n alpha_n mu(x)mu(d_n-x)1_(0,d_n)(x)v(d_n-x),
    H=I-R>=0.

Every prime power is retained. The complete source form is h=P-N, with the original Gamma multiplier b, scalar C0, both prime wings, and the coefficient-two pole. Inner products are conjugate-linear in their first slot. The symbol H is the bounded normalized reflected operator, not the original physical Hamiltonian. No whole-band conclusion is inferred merely by summing the individual-source theorem; Sections 2–4 supply the additional noncommuting argument.

## 1. Original metric, maps and domains

Work on the original P-gradient Hilbert space K_P, with its bounded complete Green operator A=T* T. No sharpened numerical upper bound for A is needed below. Let E be a spectral band of A lying strictly above one, and on E write

    Delta=I-A^-1,
    d I <= Delta <= 2d I, d>0.                            (1)

The band is finite-dimensional by compactness of the positive Green excess. Constants below do not depend on its dimension. A terminal partial dyadic band also satisfies (1).

For a in E let r_a be its actual pole-centered ratio representative and g_a=psi r_a. Define the original linear source map

    Va=g_a/mu, mu^2=psi/L,
    H=I-R >=0 on L2(0,infinity).

The published reference embedding and complete reflected-energy identity give

    ||V||^2<=193,
    N(r_a,r_b)=<a,A b>_P=2<Va,H Vb>,
    M:=V* H V=A/2,
    [M,Delta]=0.                                         (2)

The adjoint V* and every coefficient-space operator below use the P metric. V is not an isometry into ordinary L2, and no lower frame bound is assumed.

The complete source equation on this band is

    h(g_a,k)=-N(r_(Delta a),k/psi).                        (3)

It follows by linearity from the true scalar equations in a P-orthonormal eigenbasis. This does not replace different depths by a common scalar. In particular

    h(g_a,g_b)=<a,(I-A)b>_P=-2<a,Delta M b>_P.            (4)

All these are original closed forms. For every a in E, the already established whole-band tail estimate is

    ||1_(x>R) Va||_2 <= C d^-1 exp(CR-c exp(2R))||a||_P.  (5)

It follows from the complete exterior Gamma Sylvester equation of the published Green-band theorem, not by summing bounds on individual eigenvectors. The same theorem gives physical L2 membership. The original source map also has a dimension-free logarithmic Gamma form bound on this band: h[g_a]<=0, the complete normalized prime perturbations are bounded, and ||Va||<=sqrt(193)||a|| imply

    ||g_a||_2^2+q_b[(g_a)_o]<=C||a||_P^2.                (6)

## 2. Smoothing and the exact self-adjoint product

Let C=C_t^alpha be the even compact Dirichlet Poisson smoothing of SOURCE_SMOOTHING.md. Its positive-wing propagation is at most 2alpha. Use the true frozen weight mu_R, Z=mu_R^-1 C mu_R, and the complete reflected commutator and square-root gates from that report.

Define the bounded map, on the finite actual band,

    W2 a=mu^-1 C^2 g_a,
    M_C=V* H W2.                                         (7)

For each eigenvector, Cg/psi and C^2g/psi belong to the actual P core completion. Hence the same is true for every finite-band combination. This justifies (3) with k=C^2g_b. The complete source convolution identity, with both prime wings and the pole retained, gives

    h(Cg_a,Cg_b)=h(g_a,C^2g_b)
                =-2<a,Delta M_C b>_P.                   (8)

The pole is zero because every source is centered and even compact convolution preserves this condition. Complete prime exchange follows from the actual theta bounds, not boundedness of the bare source prime sum on unweighted L2.

Consequently

    B:=Delta M_C=B*,                                    (9)

even though M_C itself need not be self-adjoint. Neither [Delta,M_C]=0 nor [Delta,V*V]=0 is asserted.

## 3. The mixed upper gate in the correct metric

The previously proved quasi-contraction and square-root mixed estimate holds for every v in ordinary L2:

    Re<v,H Z^2v> <= <v,Hv>+C e0 ||v||^2,
    e0=epsilon+sqrt(eta).                                (10)

Here epsilon and eta are the exact complete quantities in SOURCE_SMOOTHING.md; this is a mixed estimate, so it has no squared source-tail error. Repeating the true-weight comparison with the dimension-free band tail (5), including propagation 4alpha, gives

    ||W2 a-Z^2Va||_2
       <=C d^-1 exp(CR-c exp(2R))||a||_P.                (11)

Combining (10)-(11), bounded H, and (2), gives in P-operator order

    Herm M_C <= M+e I,
    e=C[e0+d^-1 exp(CR-c exp(2R))].                       (12)

The first error before (2) is C e0 V*V. The bound V*V<=193I is essential in obtaining (12); it is not an implicit isometry assumption.

## 4. Positive Sylvester inversion without commuting the depth

Put

    Q=Delta^-1>0, D=B-Delta M=D*.

Equations (9), (12) and [M,Delta]=0 give exactly

    QD+DQ <= 2e I.                                      (13)

Indeed Q B=M_C and B Q=M_C*, while Q Delta M+Delta M Q=2M. The inverse of this Sylvester map preserves positive order:

    D=integral_0^infinity exp(-sQ)(QD+DQ)exp(-sQ) ds
      <=2e integral_0^infinity exp(-2sQ) ds=e Delta.      (14)

The integral is a coefficient-space operator-norm integral. No dimension factor, matrix-entry estimate, or condition-number factor is introduced. Inserting (4), (8) yields the actual whole-packet kinetic-loss bound

    h[g_a]-h[Cg_a] <= 2e<a,Delta a>_P
       <=C[d e0+exp(CR-c exp(2R))]||a||_P^2.             (15)

This is the precise point where the far d^-1 source cost cancels. It uses both exact Hermiticity (9) and the dyadic upper bound Delta<=2d I. A scalar-source estimate alone would not justify it on a packet.

## 5. Complete Gamma/prime frequency comparison

Use the same parameters as the published scalar theorem, relabeling alpha for the spatial smoothing radius:

    t=N^-1, b=N^-1/2, alpha=b/8, beta=1/3,
    exp(2R)=M0 log N,

where M0 is fixed sufficiently large. For N>=N0 with N0 independent of d and of E,

    e0<=C N^-1/8,
    exp(CR-c exp(2R))<=C_B N^-B.

Thus (15) is

    h[g_a]-h[Cg_a] <= C[d N^-1/8+N^-B]||a||_P^2.         (16)

The complete prime-tail comparison also extends with no dimension factor. The identity g_a=mu Va and (2) give

    |<g_o,tau_(log n)g_o>|
     +|<(Cg)_o,tau_(log n)(Cg)_o>|
       <=C exp(-c n)||a||_P^2.

For the smoothed term this is the same double-convolution estimate with shifts of size at most 4alpha. It does not spend ||Cg/mu||. Truncate only for comparison at P=L_B log N, paying all omitted prime powers by O(N^-B)||a||_P^2. The retained finite symbol is exactly

    b(xi)-C0-2 sum_(n<=P) alpha_n cos(xi log n).

Its prime cost is O(sqrt(log N)loglog(e^e N))=o(log N). The compact Poisson multiplier obeys the same low-frequency leakage and high-frequency loss bounds as before. Applying the complete Gamma absorption to (16) therefore gives

    integral_(|xi|>=N) log(2+|xi|)|hat(g_a)_o(xi)|^2 dxi
     <=C[d N^-1/8
          +N^-1/2 sqrt(log N)loglog(e^e N)]||a||_P^2.    (17)

In particular for each 0<=s<1/16,

    ||(g_a)_o||_(H^s) <= C_s ||a||_P                    (18)

on every actual dyadic band (1), with constants independent of depth, dimension and eigenvalue multiplicity. The bound concerns actual P-normalized packets in the displayed dyadic spectral band; it has no eigenvector-count or separation factor.

## 6. Direct actual odd packet sampling

We now apply the operator estimate directly to the actual odd Green packet. The uniform estimate (18) and g=mu Va also pay any fixed exponential spatial weight after a small Sobolev exponent loss. Fix 0<t<s<1/16, A0<infinity and an integer q>=0. On each unit spatial cell the theta bound gives

    ||chi_j g_o||_2 <= C exp(C|j|-c exp(2|j|))||a||_P,
    ||chi_j g_o||_(H^s) <= C_s ||a||_P.

Interpolation and summation of the weighted cell cutoffs imply

    ||x^q exp(eta x)(g_a)_o||_(H^t)
       <=C_(t,s,A0,q)||a||_P, |eta|<=A0.                 (19)

No weighted regularity is inferred directly from an unweighted bound alone; the first cell estimate is the additional input. Let G_a(z)=hat(g_a)_o(z). It is entire by the theta L1 bound. Analytic mean-value sampling on fixed disks, and the unconditional multiplicity-counted O(log T) unit-height zero count, applied on a fixed strip slightly wider than |Im z|<=1/2, yield

    sum_(z in Z_Xi, |Re z|>T) j_z |G_a(z)|^2
       <=C_t T^-2t log(2+T)||a||_P^2                    (20)

for a in any dyadic Green band and T>=2, after adjusting a constant depending on t to cover the bounded initial range. Every nontrivial Xi zero lies in that fixed strip. The disk overlap costs only the complete unit-height zero count; it needs no zero separation or simplicity.

For E_epsilon=Ran 1_[1+epsilon,infinity)(A), let

d_min=epsilon/(1+epsilon), J<=C log(e/d_min).

Partition its Delta spectrum into at most J dyadic bands. They are P-orthogonal. Apply (18)-(20) on each band and then Hilbert-space Cauchy--Schwarz in the J bands. This gives, for any packet a in E_epsilon,

    ||(g_a)_o||_(H^s)^2<=C_s J||a||_P^2,
    sum_(|Re z|>T)j_z|G_a(z)|^2
       <=C_t J T^-2t log(2+T)||a||_P^2.                 (21)

The loss is a logarithm in the depth range, not the rank of the packet or the number of eigenvectors. Equation (21) bounds the source samples themselves. It does not erase any separate inverse-depth factor in actual current residue coefficients.

The complete signed zero identity extends by a single actual ratio-core approximation as follows. Choose a smooth even weight omega comparable to exp(a0|x|), with fixed a0>1 and bounded logarithmic derivatives; the cell argument gives omega g in H^t. First apply even compact cutoffs at infinity. These converge in weighted H^t, physical L2, and the normalized v norm. Next cut out a neighborhood of zero. The older ORIGIN_GRAPH_DOMAIN theorem gives g/x locally in L2 for each scalar source; a finite-band combination retains this membership without any uniform band constant being needed. For a fixed compact support, the fractional product estimate for an even cutoff at scale eta bounds its additional H^t error by

    C eta^(2-2t)||g/x||_2^2+C eta||g/x||_2^2,

besides the removed original H^t energy, which tends to zero by absolute continuity. To verify the second term, outside |x|<=4eta the cutoff energy density is at most C eta/|x|^(1+2t); multiplication by |g(x)|^2=x^2|g(x)/x|^2 is bounded by C_R eta|g(x)/x|^2 because t<1/2 and the support is fixed. Inside that region use the bound C eta^(-2t). The normalized and physical L2 errors also tend to zero. Finally, on the fixed compact set with a gap at zero, odd smooth mollification converges in all those norms. Its quotient by psi lies in the original smooth compact even ratio core.

The same diagonal sequence therefore converges in weighted H^t, physical L2 and the normalized v norm. Its complete Gamma, prime and pole pairings converge. In particular, the weighted correlation bound costs C exp(-a0 d_n) times the weighted L2 error and a bounded source norm; sum alpha_n exp(-a0 d_n) is finite. For two members of this same core sequence, the N and complete h forms of their difference tend to zero; P=N+h therefore makes the sequence P-Cauchy. The continuous reference embedding and its normalized-v limit identify that P-limit with the original packet. The disk estimate gives convergence of all samples in l^2(j). Thus the original core signed identity passes to the limit with every term and true multiplicity. No maximal-domain identification is used.

For a real packet let z=gamma-i beta. In the critical sum below each pair +/-gamma is counted once with gamma>0. In the off-line sum each quartet +/-gamma +/-i beta is counted once with gamma>0 and beta>0, carrying its true common multiplicity. The identity is

    <a,(A-I)a>_P
      +2 sum_critical j|G_a(gamma)|^2
      +4 sum_offquartets j(Im G_a(z))^2
       =4 sum_offquartets j(Re G_a(z))^2.               (22)

Let P_all(a) be the sum of both complete nonnegative terms on the left of (22). Delete only the high-height terms on its right. Their cost is at most C times (21). Choose T so that C_t J T^-2t log(2+T)<=epsilon/2. Because <a,(A-I)a>_P>=epsilon||a||_P^2, this gives the stronger retained-positive interface

    (1/2)<a,(A-I)a>_P + P_all(a)
       <=4 sum_(offquartets, gamma<=T) j(Re G_a(z))^2.    (23)

Every positive term, including all high-height positive terms, remains on the left. The retained depth is the full spectral matrix A-I, not merely an averaged scalar depth. This is an actual odd Green whole-packet finite signed interface.

A thin-strip cutoff is also paid on this same packet. Fix 0<t<s1<s0<1/16. Apply (19) with q=1 and exponent s1, using s0 as its input exponent. The analytic disk estimate for G_a', uniformly over |Im z|<=1/2, and the extra exponent s1-t to absorb the multiplicity logarithm give

    sum_z j_z <Re z>^(2t)
       sup_(|eta|<=1/2)|G_a'(Re z+i eta)|^2
          <=C_t J||a||_P^2.                              (24)

Here <u>=(1+u^2)^(1/2). For the supremum, each disk lies in one fixed enlarged rectangle centered on Re z, so its mean-value bound is at most the integral over that rectangle; the multiplicity-counted overlap remains O(log(2+|Re z|)). This proves (24) without a separation assumption or pointwise derivative envelope.

For real odd g, G_a(gamma) is purely imaginary. The vertical fundamental theorem of calculus therefore gives

    |Re G_a(gamma-i beta)|
       <=|beta| sup_(|eta|<=1/2)|G_a'(gamma+i eta)|.

Delete off-line negative slots with |beta|<=c_t sqrt(epsilon/J)<gamma>^t. Their total costs at most epsilon||a||_P^2/4 by (24), after fixing c_t sufficiently small. Choose T so that the high slots cost at most another epsilon||a||_P^2/4. With the genuine finite active set

    A_(epsilon,T)={offquartets: 0<gamma<=T,
                  |beta|>c_t sqrt(epsilon/J)<gamma>^t},

the complete retained-positive statement is

    (1/2)<a,(A-I)a>_P+P_all(a)
       <=4 sum_(z in A_(epsilon,T)) j_z(Re G_a(z))^2.      (25)

Both discarded costs are uniform on the whole P-normalized packet. All true multiplicities and all positive slots remain. Equation (25) is the direct actual odd Green finite-active analysis frame needed by a later joint comparison; it supplies no upper comparison for that frame.

In particular the real-linear map a -> (sqrt(j_z) Re G_a(z))_(z in A_(epsilon,T)) has squared norm at least epsilon||a||_P^2/8 and is injective on the real band. Thus the real dimension of that band is at most the number of distinct active quartets. Multiplicity weights remain in the frame but do not require extra sample coordinates. This is a consequence of the displayed lower frame bound, not a new upper signed comparison.

It supplies no matching upper comparison for the retained off-line real-square aggregate. It neither identifies this packet with the original even physical E_kappa nor proves the required active-region upper comparison. The original even physical negative band and its current residue coefficients require their own interfaces and retain their separately established depth costs.
