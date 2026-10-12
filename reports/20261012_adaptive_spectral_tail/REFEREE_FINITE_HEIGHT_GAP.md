# Independent review: unconditional original-form gap 49999/100000

The complete [mathematical proof](FINITE_HEIGHT_GAP.md), its original-domain assumptions, and its executed scalar test have been independently reviewed. It proves H>=-1/100000 on the original known-ground complement, equivalently E(q)>=(49999/100000)Var_nu(q) on the original even closed form domain.

The general Weil bridge and numerical test were reviewed independently of their author. The special second-derivative refinement received two full separate mathematical reviews independent of its author, including the review reproduced below. The final numerical chain was then checked against that independent analytic review. The statement uses the already proved complete finite-height theorem of [Platt and Trudgian, Theorem 1](https://arxiv.org/pdf/2004.09765), conservatively at T=3*10^12, and assumes no RH or unproved arithmetic hypothesis. It is an original spectral bound, not a new zeta-zero verification or a proof of RH.

# Review of Part I: full Weil identity and complete zero tail

## Complete zero count

The original theta upper and lower envelopes imply the displayed Xi bounds with the stated normalization. On |x|<=1/10, Phi>=18 exp(-5), hence Xi(0)>(18/5)exp(-5)>1/100. For |z|<=R, evenness and u=exp(2x) give exactly 2Astar integral_1^infinity u^(R/2+5/4)exp(-pi u)du, bounded above by 2Astar Gamma(R/2+9/4).

For R=2(T+1), a=T+13/4 and k=ceil a, splitting the Gamma integral at one gives Gamma(a)<=1+k!<=2(T+5)^(T+5). The constants 2Astar<84 and Xi(0)>1/100 give the factor below 16800, whose logarithm is below 10. Every nontrivial zero with |Im rho|<=T corresponds to an Xi zero in |z|<T+1 because |Re rho-1/2|<1/2. Jensen's radius ratio 2 therefore counts the complete multiset with weight at least log2>1/2, giving (6). The final simplification to 8T log T is valid for every T>=10. It assumes no critical-line location.

Integration by parts in the counting measure gives the complete tail sum <=2p integral_T^infinity M(t)t^(-2p-1)dt. Dropping its nonpositive boundary term is legitimate, and evaluating this integral yields exactly W_p(T)=16p T^(1-2p)[log T/(2p-1)+1/(2p-1)^2]. Both ordinate signs and all multiplicities are already included.

## Actual complex-shift evaluations

For |a|<=1 the theta strip envelope gives the squared weighted L2 norm at most 100 integral_1^infinity u^2 exp(-3u/2)du=(5800/27)exp(-3/2)<49. The real translation in a radius-1/4 Cauchy circle does not change that L2 estimate. Thus the derivative bound 7 j!4^j in (9) is valid for the actual multiplier.

Leibniz and Cauchy-Schwarz bound the p-th weighted source derivative in L1 by 7M_p||v|| sum binom(p,j)j!4^j. The sum is bounded by 4^p p! exp(1/4), and 7exp(1/4)<10. This proves (10) with J_p=10*4^p*p!, without an unweighted substitute for v. All lower weighted derivatives are also integrable. The genuine W^(p,1) integration-by-parts theorem gives (11); its boundary values vanish. Its allowed shifts |beta|<=1 more than cover every actual nontrivial zero displacement.

## Quadratic Weil identity and complete domain passage

The pinned original normalization was reread in [FIXED_GAMMA_FULL_KERNEL_BARRIER.md, Appendix C (C4)](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md). The primary reference [Burnol, The Explicit Formula in Simple Terms](https://arxiv.org/pdf/math/9810169), sections on the distributional formula and classical derivation, was also actually opened and checked. Its compact smooth test identity becomes (12) under additive coordinates. In particular b-C0=Re psi(1/4+it/2)-log pi, so neither the archimedean constant nor the prime normalization has changed.

Actual-band regularity puts v in every H^j. Multiplication by the true m gives every fixed exponentially weighted derivative of f=mv in L1 and L2; the same conclusion for h=f*f_tilde follows by weighted convolution inequalities. Thus expanding even smooth cutoffs of h converge in each fixed weighted derivative L1 norm. Four integrations by parts give the stated uniform strip Fourier majorant epsilon_R(1+|Re z|)^(-4). The complete Jensen count makes its zero-side sum finite. The complete Gamma integral passes by the same majorant, and the poles pass by weighted L1 convergence.

For the prime side, the inequality |x|+|x-y|>=|y| and weighted L2 Cauchy-Schwarz imply |h(y)|<=exp(-a|y|)||exp(a|x|)f||_2^2. Taking a=2 pays alpha_n |h(+-log n)| by a summable multiple of log n/n^(5/2). Cutoffs bounded by one preserve this majorant. Hence the passage includes the entire prime series, not only finitely many primes.

For complex even f, its autocorrelation is real and even and its entire transform is F(z)conjugate(F(conjugate z)). Its prime pair is precisely the original V quadratic form. Evenness gives F(i/2)=F(-i/2)=(1/2)<e0,v>, so the two residues give exactly (1/2)|<e0,v>|^2. The resulting identity is (13) for the genuine pole-corrected form Acrit. Absolute convergence follows from the complete count and the two opposite complex evaluation bounds; individual unverified zero terms need not be positive.

## The sufficient test and its quantifiers

Under complete height-T verification, every low-height term in (13) is nonnegative, with multiplicities. The tail has absolute value at most J_p^2 M_p(kappa)^2 W_p(T)||v||^2. On the original ground-orthogonal negative band Acrit[v]=H[v]<=-kappa||v||^2. Therefore the strict inequality E_p<kappa contradicts every nonzero vector in the entire band. No common eigenvalue is assigned to a mixed-band vector.

For any fixed epsilon>0, a fixed integer p can satisfy (1/2+epsilon)(2p-1)>p+1. Substitution of the reviewed M_p<=kappa^(-p/2-o(1)) then makes T=kappa^(-1/2-epsilon) sufficient at sufficiently small kappa. This is a consequence of the explicit test, not its numerical evaluation at a proposed finite depth. The inverse rate statement T^(-2+epsilon), with suitable fixed parameters, has the correct direction. It neither presupposes nor manufactures an infinite sequence of verified heights.


# Review of Part II: special full-prime second-derivative constants

## Checks

1. **Actual strip and complete coefficient moments.** The previously reviewed strip estimates are uniform on the closed half-unit strip; their doubly exponential bounds justify closing Fourier contours. The complete positive coefficient measure has exponential envelope 800 exp(-|t|/2), including both prime translates and the C0 multiplier. Thus no finite-prime omission enters the new Wiener bounds. Direct integration gives I0=2, I2=2+16=18, I4=2+32+768=802. Holder on the normalized positive Fourier measures gives both P3 and the stated A_(3+epsilon), with no missing normalization or extra pairing factor.

2. **Rational regularization and true operator domain.** The exact divided difference of l_h is correct. A completely explicit fixed-h estimate is

       |l_h'(t)| <= max(1,h^-2) <t>^-2,
       |l_h(t)-l_h(u)| <= 2 max(1,h^-2)|t-u|<t-u>^2<u>^-2.

   The first follows from 1+ht² >= min(1,h)(1+t²) and 2|t| <= 1+t²; the second follows by integration and the two-sided Peetre inequality. In the already proved complete Fourier-kernel argument this decaying input factor absorbs the logarithmic Gamma growth; hence the fixed-h first commutator is L2 bounded. The multiplier preserves Schwartz space, maps the compact smooth graph core into D(H), and the bounded commutator extends the domain identity by closedness and graph-core approximation. The fixed-h double commutator is also bounded, while its uniform estimate is correctly only a quadratic-form estimate in H^(1+epsilon).

3. **Order-three complete double kernel.** Dividing the squared exact difference by <t>^(1+epsilon)<u>^(1+epsilon) leaves at most

       4 sqrt(2) <t-u>^3 (<t><u>)^-epsilon.

   This gives 4 sqrt(2) P3 for the complete paired-prime/C0 part. In the Gamma integral, <z>² <= 2<t><u><t-z><z-u> cancels the remaining input/output factors after using b(z) <= G_(2epsilon)<z>^(2epsilon). The convolution inequality for the cubic difference contributes 2^(3/2), so 4 sqrt(2) times 2^(3/2) equals 16 exactly. The resulting coefficient is 16 G_(2epsilon) 2^epsilon A_(3+epsilon)^2. Both normalized Young inequalities have the same 1/(2pi) convention as the stated Wiener moments. The bound for the low output frequency follows from u² <= 2t²+2(t-u)² and is precisely Lstar=2T0²A0+2A2.

4. **Whole-band Lyapunov and elimination of the unknown norm.** The previously proved Sobolev theorem supplies finiteness of K=||D²Q||, rather than assuming a bound to be proved. For a unit band vector, interpolation yields ||v||_(H^(1+epsilon))² <= (1+K)^(1+epsilon). The exact double-commutator identity and the original signed lower form imply the displayed operator Lyapunov inequality. Its positive inverse is legitimate because Kspec-delta_N >= a>0. The Fourier regularizations converge monotonically in the squared multiplier, yielding

       aK² <= c_N Lstar² +(D_epsilon/2)(1+K)^(1+epsilon).

   If K>=1, splitting the two right terms at half of aK² gives exactly the two nontrivial alternatives in Ksharp. In particular the factor in its last branch is 2^(1+epsilon)D_epsilon/a, and the power is 1/(1-epsilon). There is no remaining unknown K in the resulting bound.

5. **Complex evaluations and exclusion scope.** The half-strip weighted L2 estimate in the finite-height source is <49 for every real weight |b|<=1. Cauchy radius 1/4 gives the three constants 7, 28, 224. For a unit band vector, ||v'||2 <= sqrt(||v''||2) <= sqrt(K); the Leibniz coefficients therefore give exactly 7K+56sqrt(K)+224. The lower weighted derivative norms are integrable too, so two integrations by parts have no boundary term. Both opposite complex shifts of every nontrivial zero satisfy the bound. The complete-zero tail W2 includes signs of the ordinates and multiplicities. The added ground-removal paragraph in Section 4 is essential and correct: only there is Acrit[v]=H[v] on the whole tested band. Its strict numerical sufficient condition has the claimed implication, with its numerical verification reviewed separately below.


# Review of Part III: executed interval arithmetic

The entire [script](certify_second_derivative_height_test.py) was read before independent execution. An exact copy was run at 90 interval decimal digits under Python 3.12.14 and mpmath 1.3.0; its result is byte-identical to the retained [JSON](second_derivative_height_test_result.json). A separate 150-digit interval rerun gives the same integer derivative bounds and the same displayed 50-digit upper ratios. A further exact-Fraction summary verifies the rational margin below.

All decisions use exact Fraction conversions of dyadic interval endpoints. Decimal rendering is only for display and uses ROUND_FLOOR or ROUND_CEILING as appropriate. The mpmath interval implementations of exp, log, sqrt and positive-base real powers were checked for directed endpoints; real powers use interval log, multiplication and exp. Thus no ordinary floating evaluation is substituted for the strict interval decisions.

## Matching the code to the exact analytic bounds

The code uses N=6, beta=1/32, epsilon=beta/2=1/64 and q=1+epsilon. Its finite-prime scalar is exactly

    c6=C0+2log2/sqrt2+2log3/sqrt3+log2+2log5/sqrt5.

Here the log2 term is the full n=4 contribution and Lambda(6)=0; no n<=6 prime-power term is omitted. The complete omitted-prime norm tail is bounded above by

    delta6=(980/9)*49*exp(-7pi)<kappa/2.

The code verifies both a=kappa-delta6>0 and the tail condition by directed intervals. Its frequency T0=exp(c6) satisfies the original full-Gamma lower test (1/2)log(1+4T0^2)>c6, also explicitly checked by intervals.

The exact polynomial contour integrals I0=2, I2=18, I4=802 are used with A_j=(14/pi)I_j and P_j=(800/pi)I_j. The code's Ap=A2^((1-epsilon)/2)A4^((1+epsilon)/2) and P3=sqrt(P2 P4) are the exact Holder bounds in the reviewed analytic page. Its commutator constant

    D=16 G_beta 2^(beta/2) Ap^2+4sqrt2 P3

and low-frequency value Lstar=2T0^2 A0+2A2 match that page without replacing the complete operator. The two positive Ksharp branches are exactly sqrt(2c6/a)Lstar and [2^q D/a]^(1/(2-q)). The integer K is rounded strictly upward using exact rational endpoints and is rechecked against both interval branches.

The code then evaluates C=7K+56sqrt(K)+224 and the complete all-zero tail

    W2(3*10^12)=32(3*10^12)^(-3)
                      [log(3*10^12)/3+1/9].

These are precisely the two factors in the reviewed sufficient test C^2 W2<kappa. The interval run includes kappa=1/65536 as a weaker check and kappa=1/100000 as the reported bound.

## Enclosures and a short rational ledger

For kappa=1/100000 the independently repeated output gives

    delta6 < 0.000001501568570316180463,
    c6 < 9.753681975556488,
    K < 70775112944571,
    C^2 W2 / kappa < 0.281814251924.

For the weaker kappa=1/65536 check, the ratio is below 0.069409393891. Both are strict successes.

To avoid reliance on long decimal displays, a separate exact-Fraction summary checker verifies the following deliberately looser ledger directly from the interval endpoints:

    K < 71*10^12,
    sqrt(71*10^12) < 9*10^6,
    C < 7*(71*10^12)+56*(9*10^6)+224
      =497000504000224 < 5*10^14,
    W2(3*10^12) < 115/10^37.

Therefore

    C^2 W2 < (5*10^14)^2*(115/10^37)
            = (23/80)*(1/100000) < 1/100000.

These exact Fraction comparisons close the strict arithmetic inequality with ample margin; the same rational ledger is displayed in Part III of the mathematical proof.


## Complete external premise and absence of circularity

Platt and Trudgian's primary Theorem 1 explicitly supplies complete critical-line verification through height 3,000,175,332,800, with its completeness count. The exact smaller height 3,000,000,000,000 is therefore available without a conjectural assumption. Conjugation covers negative ordinates; the original Phi>0 gives Xi(i beta)>0 for real beta and excludes ordinate zero. Merely finding a list of critical zeros would not suffice, and is not the input used here.

The general actual-band regularity uses only the original lower bound H>=-1/2, complete signed-prime and Gamma forms, original operator graph core and actual theta strip. It does not use the previously certified 511/1024 gap. The special estimate uses that theorem only for finiteness of the true H2 band norm, then eliminates the unknown norm with its scalar inequality. Jensen's count uses the unconditional theta bounds and standard critical strip; the full Weil identity retains every complex displacement. No Q hypothesis, Mobius estimate, unproved central sign or unknown negative-band computation enters the proof.

The independently verified strict inequality C^2W2<kappa, combined with the complete finite-height theorem, contradicts any nonzero vector of Q_kappa. The known ground and original unitary form identity are retained. The final application is consequently unconditional, although the general bridge is correctly stated for an arbitrary assumed complete height. No critical-depth sign, new zero exclusion, or record claim follows.
