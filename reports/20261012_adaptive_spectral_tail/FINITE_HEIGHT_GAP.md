# An unconditional original-form gap of 49999/100000 from a verified finite zero height

For the original complete-Gamma, complete signed-prime operator H on even complex L2(dx), let e0 be its normalized ground with H e0=-e0/2. The following unconditional bound holds:

    H >= -1/100000 on e0-perp.

Equivalently, on the original closed even jump-form domain,

    E(q) >= (49999/100000) Var_nu(q).

The original unitary identification is v=e0 q, with E(q) the form of H+1/2 and the constant direction corresponding to e0. It is the user's [original closed-form realization](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/138d806005cf50c030a5797bb051ee107c351e1c/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), with its theta, prime and Gamma normalization unchanged.

The proof uses the established complete finite-height theorem of [Platt and Trudgian, Theorem 1](https://arxiv.org/pdf/2004.09765), and conservatively takes T=3,000,000,000,000. Their theorem verifies all zeros in that range; this report does not perform or claim a new zero verification. Part I first states a general bridge under a complete-height hypothesis. Part III discharges that hypothesis with the published theorem and a directed-interval scalar inequality, so the displayed application has no unproved RH, Q, Mobius-cancellation or matrix-positivity assumption.

This improves the previously certified original-form value 511/1024. It is a new bound for this original operator, not a new zeta-zero exclusion, a proof of RH, or a claim of a record among other comparisons. The remaining distance from 1/2 is 1/100000.

## Complete proof and reproducibility

The chain is: unconditional actual-band regularity; the full quadratic Weil identity with every complex zero and multiplicity; a specialized second-derivative estimate; and the verified strict numerical test. The [independent mathematical and executed review](REFEREE_FINITE_HEIGHT_GAP.md) covers every stage. The only required code and its actual output are [certify_second_derivative_height_test.py](certify_second_derivative_height_test.py) and [second_derivative_height_test_result.json](second_derivative_height_test_result.json), with exact file hashes and the command in [finite_height_certificate_manifest.json](finite_height_certificate_manifest.json).

All original operator-domain, theta strip and complete-prime inputs are in the fixed public [ACTUAL_NEGATIVE_BAND_COVERAGE.md, Part I](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/138d806005cf50c030a5797bb051ee107c351e1c/reports/20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md) and its [underlying realization and graph core](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/138d806005cf50c030a5797bb051ee107c351e1c/reports/20261012_adaptive_spectral_tail/REPORT.md). Part II uses that theorem only to know the actual second-derivative norm is finite, then eliminates the unknown norm by an explicit scalar inequality. No previous positive-depth gap is a premise of the new bound. Section and equation numbers are local to each Part.

# Part I. Complete finite-height Weil bridge

## 1. Exact statement and computable test

Work on the original even complex L2(dx), with H=B-V>=-1/2, normalized ground e0=2m cosh(x/2), H e0=-e0/2, and

    Acrit=H+(1/2)|e0><e0|.

For 0<kappa<=1/2 let Q_kappa be the spectral projection on [-1/2,-kappa], with the original ground removed. Let M_p(kappa) be ANY of the explicit, reviewed constants satisfying

    ||<D>^p Q_kappa||<=M_p(kappa).

They may be evaluated by the complete-prime moment, double-commutator, Lyapunov and interpolation recursion in Part I of the published [ACTUAL_NEGATIVE_BAND_COVERAGE.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bf5ee119d3b6687d34cd708f1a755aea9efd9679/reports/20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md). They require no computation of Q_kappa. For every fixed p they obey M_p(kappa)<=kappa^(-p/2-o(1)).

For an integer p>=2 and T>=10 define

    J_p=10*4^p*p!,
    W_p(T)=16p T^(1-2p)
             [log T/(2p-1)+1/(2p-1)^2],
    E_p(kappa,T)=J_p^2 M_p(kappa)^2 W_p(T).              (1)

Assume every nontrivial zeta zero rho with |Im rho|<=T lies on Re rho=1/2; this assumption includes ALL zeros and their full multiplicities, not just a list of located critical zeros. Then

    E_p(kappa,T)<kappa  ==>  Q_kappa=0.                 (2)

The strict inequality is an executable sufficient test once the elementary recursion defining M_p, the finite-height input, and the displayed real quantities are rigorously enclosed. It is not a hidden O_p test. The conclusion implies H>=-kappa on e0-perp, or the original even mean-zero jump-form bound E(q)>=(1/2-kappa)Var_nu(q). Equality at the endpoint need not be claimed from a non-strict numerical test.

## 2. An elementary complete zero-counting bound from the original theta kernel

Write Xi(z)=xi(1/2+iz)=integral Phi(x)exp(izx)dx. The original Phi is even and positive and obeys, for x>=0,

    2pi^2 exp(9x/2-pi exp(2x))<=Phi(x)
               <=2Astar exp(9x/2-pi exp(2x)),
    Astar=4pi^2(125/121)<42.

On |x|<=1/10, pi>3, pi<4 and exp(1/5)<5/4 give Phi(x)>=18 exp(-5). Hence

    Xi(0)>(18/5)exp(-5)>1/100,                         (3)

using e<3. For |z|<=R, the same original upper bound and u=exp(2x) give

    |Xi(z)|<=2Astar integral_1^infinity
                        u^(R/2+5/4) exp(-pi u)du
             <=2Astar Gamma(R/2+9/4).                 (4)

All nontrivial zeros satisfy 0<Re rho<1, so the Xi zeros corresponding to |Im rho|<=T lie in |z|<T+1. Take R=2(T+1), a=T+13/4, and k=ceil a. Splitting the Gamma integral at one gives

    Gamma(a)<=1+k!<=2(T+5)^(T+5).

Indeed k<=T+5 and k!<=k^k. Thus (3)-(4) imply

    log[max_(|z|<=2(T+1))|Xi(z)|/Xi(0)]
                    <=10+(T+5)log(T+5),              (5)

since 16800<exp(10); for example (8/3)^10>16800 and e>8/3. Jensen's formula, with inner radius T+1 and outer radius 2(T+1), now counts every zero with its full multiplicity and gives

    M(T):=#{rho: |Im rho|<=T}
       <=2[10+(T+5)log(T+5)]<=8Tlog T, T>=10.          (6)

For the last inequality use T+5<=3T/2, log(T+5)<=2log T, and Tlog T>=10. No RH or finite-height verification is used in (6). This deliberately coarse complete count avoids reliance on a delicate numerical error constant in a sharper zero-count theorem.

Stieltjes integration of (6) gives, for every integer p>=1 and T>=10,

    sum_(rho:|Im rho|>T) |Im rho|^(-2p)
       <=2p integral_T^infinity M(t)t^(-2p-1)dt
       <=W_p(T).                                     (7)

The negative boundary term at T has only been dropped in the upper bound. Both signs of the ordinates and all multiplicities are included.

## 3. Uniform complex-shift evaluation bounds in the actual source class

Let v belong to Ran Q_kappa and put f=mv, F(z)=integral f(x)exp(izx)dx. For every real a with |a|<=1, the original strip bound

    |m(x+iy)|^2<=100 exp(4|x|-(3/2)exp(2|x|)), |y|<=1/2

implies

    integral |exp(a(x+iy))m(x+iy)|^2 dx
       <=100 integral_1^infinity u^2 exp(-3u/2)du<49.   (8)

The integral equals (5800/27)exp(-3/2), which is below 49 using exp(3/2)>40/9. Cauchy's formula on radius 1/4 circles, followed by the L2 triangle inequality and translation invariance in x, therefore proves

    ||(exp(a x)m(x))^(j)||2<=7 j!4^j,
               j=0,1,..., |a|<=1.                    (9)

The actual-band H^p estimate and Leibniz/Cauchy-Schwarz give

    ||(exp(a x)f(x))^(p)||1
       <=7 sum_(j=0)^p binom(p,j)j!4^j M_p(kappa)||v||
       <=J_p M_p(kappa)||v||.                         (10)

For the last inequality, sum binom(p,j)j!4^j<=4^p p!exp(1/4), and 7exp(1/4)<10. All lower derivative norms of v are at most ||<D>^p v||. The same argument proves the lower-order weighted L1 bounds needed for integration by parts.

For every gamma!=0 and |beta|<=1, integration by parts p times in the actual W^(p,1) function exp(-beta x)f(x) gives

    |F(gamma+i beta)|
                <=J_p M_p(kappa)|gamma|^(-p)||v||.     (11)

The boundary terms vanish in the W^(p,1) realization. In particular (11) is uniform over the full complex displacement |Re rho-1/2|<1/2 of every actual nontrivial zero. Nothing sets those displacements to zero in the unverified tail.

## 4. The exact quadratic Weil identity and its domain passage

Use the Fourier sign convention just given and put

    f_tilde(x)=conj(f(-x)), h=f*f_tilde,
    hhat(z)=F(z)conj(F(conj z)).

Evenness of f makes h real and even. The original additive explicit formula, including the complete zero multiset, is

    sum_rho hhat(-i(rho-1/2))
       =hhat(i/2)+hhat(-i/2)
        +integral [b(t)-C0]hhat(t)dt/(2pi)
        -sum_(n>=2) alpha_n[h(log n)+h(-log n)].         (12)

For compact smooth h, this is the exact normalization in [FIXED_GAMMA_FULL_KERNEL_BARRIER.md, Appendix C, equation (C4)](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md). Its primary explicit-formula reference is J.-F. Burnol, The Explicit Formula in Simple Terms, Sections 1 and 3, https://arxiv.org/pdf/math/9810169. The zero sum counts all nontrivial zeros with multiplicity; it is not restricted to simple or critical zeros.

Here (12) is applied to a larger but carefully justified original source class. The reviewed negative-band theorem gives v in H^j for every j. Multiplication by the actual doubly exponentially decreasing m and its derivatives implies that f has every exponentially weighted derivative in L1 and L2. Thus h has the same weighted L1 derivative properties by convolution, and all required derivatives are smooth. Multiply h by expanding even smooth cutoffs h_R. They converge to h in every fixed exponentially weighted derivative L1 norm. Repeated integration by parts gives, uniformly for |Im z|<=1/2,

    |hhat_R(z)-hhat(z)|
                   <=epsilon_R(1+|Re z|)^(-4),
    epsilon_R ->0.

The complete count (6) makes the zero sum of this majorant finite, so dominated convergence passes the ENTIRE zero side to the limit. The Gamma term passes by the same Fourier majorant and b(t)<=7<t>^(1/2). The two pole terms pass by weighted L1 convergence. For the prime terms, weighted L2 Cauchy-Schwarz gives, for any fixed a>1/2,

    |h(y)|<=exp(-a|y|)||exp(a|x|)f(x)||2^2.

Take a=2. Then alpha_n|h(+-log n)| is bounded by a constant times log n/n^(5/2), summable over all integers n>=2. The cutoffs can be chosen bounded by one, and dominated convergence pays every prime power. This proves (12) for the actual autocorrelation, with no assumed full-space identity on an unjustified rough source domain.

Now write rho=1/2+beta_rho+i gamma_rho and z_rho=gamma_rho-i beta_rho. On the real axis hhat(t)=|F(t)|^2. The prime autocorrelation pairing is exactly the original V prime form. Also

    F(i/2)=F(-i/2)=(1/2)<e0,v>,
    hhat(i/2)+hhat(-i/2)=(1/2)|<e0,v>|^2.

Consequently (12) is precisely the genuine identity

    Acrit[v]
       =sum_rho F(gamma_rho-i beta_rho)
                       conj(F(gamma_rho+i beta_rho)). (13)

The series is absolutely convergent by (7),(11). The sum is real by zero symmetries, or directly by equality with the real form. Individual unverified terms need not be nonnegative.

## 5. Negative-depth exclusion and the order of the quantifiers

Assume the stated COMPLETE height-T verification. Every term in (13) with |gamma_rho|<=T is then |F(gamma_rho)|^2>=0, including every multiplicity. For the remaining zeros, use (11) for both opposite complex shifts, then (7). This gives the actual whole-band inequality

    Acrit[v]>=-E_p(kappa,T)||v||^2,
                         v in Ran Q_kappa.            (14)

On this ground-orthogonal band the spectral theorem gives Acrit[v]=H[v]<=-kappa||v||^2. If (2) holds, (14) is contradictory for any nonzero v. This proves the test.

For each fixed epsilon>0 choose a fixed integer p>=2 with

    (1/2+epsilon)(2p-1)>p+1.

Then the reviewed explicit bound M_p(kappa)<=kappa^(-p/2-o(1)) and (1) show that

    T=kappa^(-1/2-epsilon)

is sufficient for (2) once kappa is sufficiently small. This is an effective asymptotic consequence of an explicit sufficient inequality, not a replacement for evaluating that inequality at any proposed numerical depth. All constants entering the finite test are given by (1) and the reviewed M_p recursion. Inverting this scale, a complete verified height tending to infinity would yield lower gaps approaching the critical value at rate T^(-2+epsilon), with suitable fixed parameters and sufficiently large T. No unverified infinite sequence of height checks is assumed.

As one possible EXTERNAL input, Platt and Trudgian's primary paper, The Riemann hypothesis is true up to 3*10^12, https://arxiv.org/pdf/2004.09765, Theorem 1, proves the complete verification up to 3,000,175,332,800; its method includes a Turing completeness count and rigorous ball arithmetic. Thus the conservative T=3*10^12 is an available finite-height hypothesis. Part II supplies a sharper second-derivative evaluation in place of (11), and Part III verifies its numerical sufficient inequality. Finite-height verification is not identified with RH.

# Part II. Specialized actual-band second-derivative constants

Use the same original H=B-V, full paired prime coefficients a_n(x)=m(x)m(x+log n), Q=1_[-1/2,-kappa](H) (optionally ground removed), Kspec=-H|Ran Q, delta_N<=kappa/2, a=kappa-delta_N, c_N and frequency cutoff T0 with b(T0)>=c_N. Below a_j(g)=(1/(2pi)) integral <t>^j |ghat(t)|dt.

## 1. Smaller complete Wiener moments from the same strip

The actual strip and the complete paired-coefficient envelope proved in [ACTUAL_NEGATIVE_BAND_COVERAGE.md, Part I, Section 2](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/138d806005cf50c030a5797bb051ee107c351e1c/reports/20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md) give uniformly for |y|<=1/2:

    ||m(.+iy)||1<14,
    C0 ||m(.+iy)^2||1+2 sum alpha_n ||a_n(.+iy)||1<800.

The paired coefficients have the reviewed absolutely summable strip envelope S_n. Shift the Fourier contour to Im z=-(1/2)sgn(t). The vertical closing integrals vanish by the actual doubly exponential envelopes, and hence

    |mhat(t)|<=14 exp(-|t|/2),
    C0 |(m²)hat(t)|+2 sum alpha_n |a_nhat(t)|
                        <=800 exp(-|t|/2).

Put I_j=integral_0^infinity (1+t²)^(j/2) exp(-t/2)dt. For j=0,2,4,

    I0=2, I2=18, I4=802,
    A_j=(14/pi)I_j, P_j=(800/pi)I_j,
    P3=sqrt(P2 P4).

Thus a_j(m)<=A_j. Holder on the complete positive Fourier coefficient measure bounds its order-3 V moment by P3. For 0<epsilon<=1/2, Holder on the positive m Fourier measure gives

    a_(3+epsilon)(m)<=A2^((1-epsilon)/2) A4^((1+epsilon)/2)
                         =:A_(3+epsilon).             (1)

This is a contour-moment improvement using the already verified actual strip, not a change of the operator.

## 2. Exact rational second-derivative multiplier

Let L_h be the bounded real even multiplier l_h(t)=t²/(1+h t²), h>0. Its exact difference is

    l_h(t)-l_h(u)=(t-u)(t+u)/[(1+ht²)(1+hu²)].

For fixed h it maps Schwartz into Schwartz. Put C_h=max(1,h^(-2)). Since 1+ht²>=min(1,h)(1+t²) and 2|t|<=1+t², its derivative satisfies |l_h'(t)|<=C_h<t>^(-2). The two-sided Peetre inequality therefore gives |l_h(t)-l_h(u)|<=2C_h|t-u|<t-u>²<u>^(-2). This makes its first commutator with H L2-bounded, after the same logarithmic-symbol convolution estimate used in the reviewed regularization. The original operator graph core and closedness imply L_h D(H) is contained in D(H), and the exact double-commutator identity is legal.

Fix 0<epsilon<=1/2, q=1+epsilon and beta=2epsilon. Set

    G_beta=4+2^beta/beta,
    D_epsilon=16 G_beta 2^epsilon A_(3+epsilon)^2
                       +4sqrt(2)P3,
    Lstar=2T0² A0+2A2.                                 (2)

Then, uniformly in h,

    |<v,[L_h,[L_h,H]]v>|<=D_epsilon ||v||_(H^q)^2,
    ||1_|D|<=T0 m L_h||<=Lstar.                        (3)

Here is the full kernel bound. With k=t-u, dropping the denominator in the exact difference and dividing by <t>^q<u>^q gives k²(t+u)²/(<t>^q<u>^q). The two-sided Peetre inequalities give

    (t+u)²/(<t><u>)
       <=<t>/<u>+<u>/<t>+2
       <=(2sqrt(2)+2)<k><=4sqrt(2)<k>,
    k²<k><=<k>³.

For the translated-prime kernel the extra factor (<t><u>)^(-epsilon) is at most one. Thus its full coefficient sum costs 4sqrt(2)P3.

For the Gamma kernel integral mhat(t-z)b(z)mhat(z-u) dz/(2pi), put k1=t-z, k2=z-u. The two Peetre inequalities multiplied together give

    <z>²<=2<t><u><k1><k2>.

Since b(z)<=G_beta<z>^(2epsilon), the factors (<t><u>)^epsilon cancel. Moreover <k1+k2>³<=2^(3/2)<k1>³<k2>³. Two normalized Young inequalities now give exactly the first term of D_epsilon in (2), with a_(3+epsilon)(m) on each side. The factor 4sqrt(2)*2^(3/2) is exactly 16. This proves the quadratic bound in (3) by weighted-kernel domination and density. The low-frequency bound follows from l_h(u)<=u²<=2t²+2(t-u)² for |t|<=T0, followed by the normalized Young inequality.

## 3. A closed scalar bound using known finiteness

[ACTUAL_NEGATIVE_BAND_COVERAGE.md, Part I](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/138d806005cf50c030a5797bb051ee107c351e1c/reports/20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md) already implies that the UNKNOWN actual K=||D²Q|| is finite. For unit v in Ran Q,

    ||v||_(H^q)^2<=(1+K)^q,

by Fourier interpolation between L2 and H2 and ||<D>²Q||<=1+K. This inequality uses K only in its proof; it will be eliminated from the final bound.

For W=L_hQ, X=W*W, the original operator identity and low-frequency lower form bound give

    (Kspec-delta_N)X+X(Kspec-delta_N)
       <=[2c_N Lstar²+D_epsilon(1+K)^(1+epsilon)]I.

The positive Lyapunov inverse, followed by monotone Fourier convergence as h decreases to zero, yields

    aK²<=c_N Lstar²+(D_epsilon/2)(1+K)^(1+epsilon).

For K>=1, (1+K)^(1+epsilon)<=2^(1+epsilon)K^(1+epsilon). At least one right-hand summand is at least half of aK². Consequently the explicit bound

    K<=Ksharp:=max{1,
          sqrt(2c_N/a)Lstar,
          [2^(1+epsilon)D_epsilon/a]^(1/(1-epsilon))}   (4)

holds. No uncomputed unknown norm remains in (4). One may use any admissible N,T0,epsilon; all complete-prime tails are unchanged.

## 4. Special p=2 complex evaluation without a uniform Leibniz loss

For the exclusion test in this section, Q is the original negative band with the known ground removed. Sections 1-3 also allow the full negative band, but exclusion uses Acrit[v]=H[v] on the ground-orthogonal band.

The actual weighted-m derivative bounds proved in Part I, Section 3 are, uniformly for real |b|<=1,

    ||e^(bx)m||2<=7,
    ||(e^(bx)m)'||2<=28,
    ||(e^(bx)m)''||2<=224.

For unit v in Ran Q, Fourier Cauchy-Schwarz gives ||v'||2<=sqrt(K), while ||v''||2<=K. Hence for f=mv,

    ||(e^(bx)f)''||1<=7K+56sqrt(K)+224
                    <=7Ksharp+56sqrt(Ksharp)+224=:Csharp.

Integration by parts gives |F(gamma+i beta)|<=Csharp |gamma|^-2||v|| for every |beta|<=1. Therefore, under COMPLETE critical-line verification to height H0>=10, the independently reviewed Weil-tail argument yields the sharper executable sufficient test

    Csharp² W2(H0)<kappa  ==> Q_kappa=0.                (5)

Here W2 is the full all-zero, all-multiplicity tail in Part I, equations (1) and (7). The numerical instance of (5) is certified by the separate independent directed-interval ledger. This page supplies the analytic refinement and its exact sufficient condition.

# Part III. Executed strict inequality and the unconditional application

## 1. Exact parameters and complete terms

Take kappa=1/100000, N=6, beta=1/32 and the Part II parameter epsilon=beta/2=1/64. The finite-prime scalar, including the prime power n=4 and Lambda(6)=0, is exactly

    c6=C0+2log2/sqrt2+2log3/sqrt3+log2+2log5/sqrt5,
    delta6=(980/9)*49*exp(-7pi),
    a=kappa-delta6, T0=exp(c6).

The script verifies delta6<kappa/2 and b(T0)>=c6 through the proved full-Gamma lower bound (1/2)log(1+4T0^2)>c6. It uses the complete contour moments I0=2, I2=18, I4=802 and both Holder bounds of Part II. Its two branches of Ksharp are exactly those in Part II (4), without replacing the paired full-prime measure by a finite-prime moment.

A rigorously upward integer bound for the actual ||D^2 Q_kappa|| is

    K_bound=70775112944571.

The code obtains this integer from exact rational interval endpoints and checks it strictly above both analytic branches. With C=7K_bound+56sqrt(K_bound)+224 and the all-zero tail

    W2(T)=32T^(-3)[log(T)/3+1/9], T=3*10^12,

the directed interval computation gives

    C^2 W2(T)/kappa < 0.281814251924 < 1.

The printed decimal here is a slack summary; interval assertions use exact dyadic endpoints, not the displayed decimals.

## 2. A short exact rational margin

The same interval enclosures imply K_bound<71*10^12, W2(T)<115/10^37, and

    sqrt(71*10^12)<9*10^6,
    C<7*(71*10^12)+56*(9*10^6)+224
      =497000504000224<5*10^14.

Consequently exact rational arithmetic gives

    C^2 W2(T)<(5*10^14)^2*(115/10^37)
               =(23/80)*(1/100000)<1/100000.

This pays the entire unverified zero tail with both ordinate signs, all multiplicities, and both opposite complex displacements. Individual high-zero contributions have not been assumed positive.

## 3. Why this is an unconditional spectral bound

The low-zero input is a theorem already proved by Platt and Trudgian, whose Theorem 1 covers height 3,000,175,332,800. Its completeness argument is part of that theorem, so the smaller T used here satisfies the complete-height premise in Part I. Negative ordinates are covered by conjugation. There is no nontrivial zero at ordinate zero: for every real beta, the original positive theta kernel gives Xi(i beta)=integral Phi(x)exp(-beta x)dx>0. Thus the entire |Im rho|<=T multiset, including the height-zero boundary, is covered. No conjectural extension beyond T is used.

Suppose the actual ground-orthogonal Q_kappa were nonzero. The unconditional actual-band regularity cited in Part I permits the full-domain Weil identity, and Part II gives the explicit complex evaluation constant just certified. Every low-height term is nonnegative by the published finite-height theorem. The remaining terms have total absolute value at most C^2W2(T)||v||^2. Hence for v in that band,

    Acrit[v]>=-C^2W2(T)||v||^2,
    Acrit[v]=H[v]<=-kappa||v||^2.

The strict rational margin contradicts any nonzero v. Thus Q_kappa=0. The original ground is handled exactly, and the spectral theorem then gives H>=-1/100000 on its orthogonal complement. The original unitary closed-form identity gives the stated variance inequality for every vector in its even form domain. This conclusion does not assert critical positivity at kappa=0.

## 4. Reproduction

Run, in this directory, with Python 3 and mpmath 1.3.0:

    python certify_second_derivative_height_test.py

The independent repeated runs used Python 3.12.14. The retained script uses 90 decimal digits of directed interval precision; a separate 150-digit verification gave the same integer bounds and displayed upper ratios. The 90-digit output is byte-identical to the supplied JSON. Its additional successful kappa=1/65536 row is a weaker cross-check; the reported theorem uses the kappa=1/100000 row.

Every inequality decision converts the binary interval endpoints exactly to Fraction. Decimal display uses explicit downward or upward rounding. The elementary interval functions are exp, log, square root and positive-base real powers; no uncertified floating eigenvalue or Gamma-function evaluation is used. The result JSON deliberately describes the scalar test separately from its analytic hypotheses; the full proofs and independent review in this report supply those hypotheses.
