# Independent review: Euler decompletion and core-marked probe

Companion: [EULER_DECOMPLETION.md](EULER_DECOMPLETION.md). The reviews below distinguish the original marking, the changed core marking, local correction continuation, and the still-unproved global high/low comparison.

# Review of Part I

## Referee: principal Euler factor and exact arithmetic scale transform

### Verdict

The stated factorization, exact physical transform, and local principal continuation are valid. They do not supply the unproved global high comparison or the critical low estimate. In particular, they cannot be substituted into the original coupled-scale estimates without new bounds.

Reviewed manuscript: the corresponding Part I manuscript. The underlying definitions and local table were compared directly with the fixed `openai/math` source `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`, especially its definitions of the physical probe and the complete local Euler identity.

### 1. Exact principal factor and nonvanishing

Write P for a good prime norm, d=eta(p)P^{-x}, and r=kappa(p)P^{3-6x}, with kappa=eta^6 bar(alpha)^6. The angular sixth power is invariant under the six units, so kappa is a genuine unitary Hecke character on the good ideals. The source's j=0 local identity at w=1,z=1/6 gives

H_p=(1-P^{-2})(1-r)^{-1}[1+(d-r)/(P(1-d))].

This was independently simplified from the original local P_p and P_p^* expressions. Consequently, initially in Re x>2/3,

H_eta(x)=zeta_F^S(2)^{-1} L^S(6x-3,kappa) E_eta(x).

For Re x>=1/2+delta, the local perturbation is O(P^{-3/2-delta}+P^{-1-6delta}), uniformly in imaginary parts and the unit target phases. Elementary ideal counting proves normal absolute convergence of E_eta on Re x>1/2.

In fact no enlargement of S is necessary to prove its local factors nonzero. Their numerator, before division by P(1-d), is P-(P-1)d-r. For every P>=2 and Re x>1/2,

|(P-1)d+r| < (P-1)/sqrt(P)+1 < P.

The denominator is nonzero there. Thus the normally convergent product E_eta is nonzero for the original fixed excluded set. The direct inequality preserves all original physical data and is included in the final manuscript.

No assertion that the angular L-function is zero-free in Re(6x-3)<=1 is used or obtained. The factorization itself is not a nonvanishing theorem for the original H_eta throughout Re x>1/2.

### 2. Exact physical operation and initial absolute identity

The operation is precisely

I_flat(X,Y,Z)=sum_d mu(d) kappa(d) q_d^{-2} I(X,Y,Z/q_d^6),

with X,Y, the auxiliary primitive character xi, all zero extensions, and any fixed physical slot tuple unchanged. The original annular weights make the s,m sums finite for fixed X,Y. The full all-scale absolute row estimate bounds I(X,Y,T) by C_{X,Y} sqrt(T). Hence the transform is absolutely dominated by C_{X,Y} sqrt(Z) sum_d q_d^{-5}.

The marked-row counterpart has the same original D and satisfies |B_D^flat(U)|<=C sqrt(U)/q_D. This follows from the uniform original estimate before summing d. No character chi_d(m) is introduced by the transform; this warning is essential.

In the exact high integral the original third-scale exponent is x+z-1. Therefore the transformed coefficient is q_d^{4-6x-6z}, and on the original lines (Re x,Re w,Re z)=(3,3,2) its absolutely convergent sum is 1/L^S(6x+6z-4,kappa), at real argument 26. The rapidly decaying Mellin weights and the source's initial absolute convergence justify the exchange.

This calculation would be different if one scaled the entire balanced function J(Z/q_d^6), since that would also change X,Y and possibly the slots. The displayed identity only concerns the third-scale operation actually defined.

### 3. Cancellation before continuation

Multiplication of each exact local factor by 1-R, R=kappa(p)P^{4-6x-6z}, gives H_p^flat=N_p/(1-d). Independently expanding the source table gives exactly the ten perturbation terms displayed in equation (9); a separate symbolic rational simplification gave zero difference.

At (Re x,Re w,Re z)=(sigma,1,1/6), the ten decay exponents are

sigma+2, sigma+3, sigma+1, sigma+1, sigma+1,
6sigma, 6sigma-1, 6sigma-1, 6sigma-2, 2.

All exceed one for sigma>1/2. More explicitly, the region where Re x>0 and all ten affine exponents exceed one is convex. It includes the original point (3,3,2) and every such principal point. On this region the new product converges normally; its continuation is connected to the initial identity. There is no division through an angular L-zero in this argument: the factor 1-R is cancelled algebraically at every prime before the new product is continued.

At the principal residue, the result is exactly zeta_F^S(2)^{-1}E_eta(x). In particular it is holomorphic and nonzero for Re x>1/2. The original scalar residue constants are unchanged wherever the residue calculation can be carried out in their common initial continuation domain. This does not justify reaching those residues across the full infinite family of other rows.

### 4. Bounds that cannot be inherited

A hypothetical fixed-X,Y bound |I(X,Y,T)|<=C T^a is preserved by absolute summation only if sum_d q_d^{-2-6a} converges, namely a>-1/6. The desired exponent -3/16 is outside that range. The actual source low estimates also couple X,Y,Z and moving slots, whereas this operation fixes the first two scales and those slots.

The physical transformed weight is sum_d mu(d)kappa(d)q_d^{-2} W_G(q_d^6 y). Its absolute small-y estimate does not automatically retain arbitrary log-Gaussian decay: the transition q_d approximately y^{-1/6} already gives a natural y^{1/6} absolute scale. Thus preservation of all old profile seminorms, shifted contours, and low/high error budgets is not a consequence of sum_d q_d^{-2}<infinity.

The manuscript accurately leaves these matters open. Its new result is an exact transformed probe with a locally continued nonvanishing unmarked principal correction, rather than a completed zero-exclusion argument.

# Review of Part II

## Referee addendum: finite physical core and all-row correction domain

The two appendices in the corresponding Part II manuscript pass independently, with the original fixed S, xi and b_* unchanged. The conclusions concern the exact modified row and its Euler correction, not the complete compensated principal multiplier or a global contour estimate.

### A. Finite physical identity

The source's sign-valued reciprocity bicharacter and quadratic refinement give R(k^6,s)=1 and G(k^6)=1, without coprimality restrictions. Indeed G(k^2)=chi_k(4) has order dividing three, while R(k^2,k^2)=1. Moreover Xi(k)^6=1 for good k. Consequently the actual coefficient satisfies b(c,nk^2;s)=b(c,n;s)kappa(k), including all shared-prime cases.

Write n=v k^2 with v squarefree. With F=D/gcd(D,cv), the marker is precisely F|k. The original character is chi_{cv^3}(m) times 1_{(k,m)=1}. If (D,m)>1, every original marked row vanishes. Otherwise F is prime to m and, initially at Re t=4 with a=2+6t,

sum_{F|k,(k,m)=1} kappa(k)q_k^{-a}
= kappa(F)q_F^{-a} L^S(a,kappa)
  product_{p|rad_S(m)}(1-kappa(p)q_p^{-a}).

There is no extra factor at primes of F: after k=Fj, shared primes of F and j remain allowed. Multiplication by the actual scale-transform reciprocal cancels L in this absolute region. Expanding the remaining finite product and inverting Mellin proves equation (A2), with the positive mandatory F^6 norm factor and the signed h^6 factor both retained.

The proof correctly does not replace the whole physical row by an unrestricted squarefree n sum. For D=1 the core cv^3 has exponents 0,1,3,4; the surviving finite h-divisor correction is still present. For nontrivial D the F-dependent square layer cannot be omitted. Absolute convergence follows either on the original Mellin line or, after inversion, from finite F/h decompositions and positive Gaussian majorants. The uniform sqrt(U)/q_D bound comes from the original convolution and need not be rederived by discarding these distinctions.

### B. All physical numerator rows

For 0<delta<=1/4, set Re x>=1/2+delta, Re w>=1-delta/4, Re z>=1/6-delta/12. At p not dividing u, the source j=0 table with d=eta(p)bar(rho)P^{-x}, W=rho P^{-w} gives the same ten-term polynomial as in the main note. Their precise lower decay exponents are those in (B3); each is at least 1+2delta. In particular the potentially limiting terms are 3/2+delta/4 and 2-3delta/4, both safely above 1+2delta on the stated interval. The denominator 1-d is bounded away from zero.

At p|u the original zero extensions make d=W=0. Direct substitution gives exactly

H_p^flat=1-R/P-eta(p)(P-1)P^{-x-w}V^{1_{j<=1}}+(1-V)J_j.

The five original J_j entries yield the six exponents listed in the manuscript. The smallest genuinely new ones are 3delta and 4delta; the common term is at least 1/2+3delta/4. All are at least 2delta. Thus |H_p^flat-1|<=C P^{-2delta} at row primes and <=C P^{-1-2delta} elsewhere.

Normal convergence of the unramified product and the elementary estimate product_{p|u}(1+C P^{-2delta})<=C_{delta,epsilon} q_u^epsilon prove the claimed uniform bound. The estimates have strict margins, so they hold on a neighborhood of each point of the displayed closed region. All constants are uniform in imaginary parts and the unit phases. No bound uniform as delta decreases to zero is implied.

The modified correction is therefore holomorphic with q_u^epsilon growth on this all-row domain. This does not remove zeros of the separate target/twisted L-function denominators, justify summing and moving every contour, or prove a nonvanishing statement for the additional finite selected-prime compensation factors. These restrictions must remain explicit.

# Review of Part III

## Referee: core marking repairs the selected principal factors

### Verdict

The final the corresponding Part III manuscript, including equations (5.7)–(5.8), passes. It constructs a different physical marking, retains the actual auxiliary primitive character and original zero extensions, and proves a nonvanishing local principal correction throughout Re x>1/2. The manuscript now correctly separates its fixed arithmetic multiplier from its Z-dependent finite-slot error. It does not prove the complete high comparison or the negative low correlation for the new probe.

### 1. Remaining obstruction in the old marking

Substituting the source's exact principal local table into the original marked-minus-rescaled operation gives the displayed formulas (2.1) and (2.2). The surviving term r/d=eta(p)^5 bar(alpha(p))^6 P^{3-5x} is real arithmetic structure, not an arbitrarily chosen coefficient. For every fixed 1/2<sigma<3/5 it dominates the other local terms in magnitude uniformly in imaginary parts and unit phases, giving (2.4). This rules out a uniform local approximation to -1 for the old selected factor across that half-plane; it does not prove a lower bound after the actual prime-slot sums.

### 2. New marker and the exact removed family

The new condition D|cv, where n=v k^2 and v is squarefree, is explicitly a changed physical probe. It preserves all source coefficients, nonunit character values, Gauss sums and slot scales. It depends only on v_p(c) and the parity of v_p(n), so its local high restriction is exactly e_0=1 or l odd. The scale convolution is still performed only in the third variable, with the original tuple, X/q_r and Y/q_r fixed.

For j=0 in the source local Gauss table, the terms removed from the old completed-index mark are precisely e_0=0 and l positive even. Their two nonzero s-valuation families sum to (1+P^{-1})r/(1-r) at w=1,z=1/6. No shared c,n prime is removed, because every e_0=1 term remains. The two odd-l families vanish at j=0 by the original prime-power Gauss support: the required valuation congruences are incompatible with a multiple of six. Thus P_core^*=-(1+P^{-1})d/(1-r) is exact.

### 3. Principal selected replacement and nonvanishing

Independent substitution of P_core^* into the marked-minus-rescaled operation, followed by multiplication by 1-r, gives

G_core^flat=(1-P^{-2})/(1-d) * [-1+(1-P^{-1})d/P+r/P^2].

With A=1-d+(d-r)/P and B_core=G_core^flat/H_p^flat, this simplifies to

B_core+1=-(1-P^{-1})[(1-P^{-1})d+r/P]/A.

For Re x>1/2 and selected P>=100, |A| is bounded below by an absolute positive constant and |B_core+1|<1/4. Only selected primes need this cutoff; it is automatic for sufficiently large Z in the fixed positive-exponent slots. The unselected product already has the all-prime nonvanishing proof from the decompletion referee, so the main statement need not change S, xi or b_*.

Each normalized slot factor C_i is a positive weighted average of -B_core and lies in the disk |C_i-1|<1/4. Hence it is holomorphic and nonzero. Disjoint slot supports give exactly H_eta^flat times the product of these factors. This proves nonvanishing of the full finite selected correction at the principal residue. In particular its absolute finite-factor lower bound is at least (3/4)^K; no smallness condition inversely proportional to K is needed for mere nonvanishing.

The optional stronger near-one assertion obtained by enlarging S is correctly identified as a choice before constructing a new fixed set of probe data, including its xi and b_*. It is not an invariance claim about an already fixed probe.

### 4. Fixed signal versus Z-dependent error

This distinction is essential. The finite normalized correction is not a fixed function of x alone. At the principal residue the exact factor is

H_fixed(x) Z^{ell/6} A_T(Z) [1+R_Z(x)],

where H_fixed=zeta_F^S(2)^{-1}E_eta is holomorphic and nonzero on Re x>1/2, while A_T=(-1)^K Z^{-ell/6} product_i N_i is the original nonzero prime normalizer. The local bound is uniformly O(P^{-1/2}) on the entire open half-plane, so fixed positive slot exponents give

sup_{Re x>1/2}|R_Z(x)| <= C_slots Z^{-ell_min/2}.

The original fixed-ray prime normalizer yields |A_T| comparable to (log Z)^{-K}. Finally X^{1/3}Z^{x-5/6}Z^{ell/6}=Z^{x-11/16} at X=Z^{17/48} and ell=1/6. This normalization and exponent were independently checked.

These are local residue-factor statements. Uniform pointwise smallness of R_Z does not by itself control the complete contour integral in the presence of L-function denominators, nor does it justify moving the whole sum of nonprincipal rows. The final manuscript correctly retains this open requirement.

### 5. Finite physical row

The finite h|rad_S(m) formula (6.1) follows in the initial absolute Mellin region from the exact identity b(c,vk^2;s)=b(c,v;s)kappa(k), the original mask 1_{(k,m)=1}, and cancellation of L^S(2+6t,kappa). Because core marking already lies on c,v, no missing-mark F-square layer is present. All m-divisor signs and original zeros remain. No estimate for Mobius partial sums or angular L zeros is assumed.

The pointwise positive-majorant bound and the companion finite-energy stability theorem are compatible with this identity. Neither transfers the old stronger reflected row theorem or establishes the target negative R4 exponent for the new marking.

# Review of Part IV

## Referee: finite-row energy for the core-marked decompleted probe

the corresponding Part IV manuscript passes with its stated Z>=2, Q>=1 and, in the double mean-square statement, Y>=1. The constants are uniform in the fixed nonzero dilation a of the physical frequency and in the number of marking primes. The result preserves the coarse sixth-sieve finite-row energy, not the desired negative mixed-correlation exponent.

1. Core marking is a subset only in the positive coefficient majorant. Thus the all-scale bound C sqrt(U)/q_D is valid without a false inequality between two oscillating row absolute values.

2. In the previously proved E/F decomposition, core marking imposes odd valuations at F primes in the outer n variable. This restriction is independent of m. After n=Fn_0 it says the corresponding n_0 valuations are even. The original proof works separately for every n_0 and uses positive Minkowski majorants, so restricting these terms preserves the bound. The c_0 squarefree column restrictions and coefficients remain of the required type. A frozen dilation m->am contributes a column/outer scalar of modulus at most one, retaining all nonunit zeros; all bounds are independent of a.

3. Splitting the scale transform at q_d=(Z/2)^{1/6} respects the valid large-scale range of the sieve estimate. In the small-d part, the four norm terms have summable d exponents 2,5,3,9/2. Their epsilon factors can be bounded by the value at Z. The large-d part is bounded with the all-scale positive estimate and ideal counting, giving norm at most C sqrt(Q/q_D) Z^{-1/6}. This is covered by the first norm term. Minkowski also justifies convergence of the transformed infinite sum in the finite-row Hilbert norm.

4. The prior positive Gauss-divisor transfer applies to this genuinely uniform frozen-dilation estimate. Its four base Q exponents are 1,1/6,5/6,1/3; the small Q^epsilon loss is taken outside before the transfer. Hence no invalid exponent above one enters the divisor moment theorem. The sixth-power Gauss branch uses the proved endpoint moment rather than a maximum-Gauss bound.

5. The exact finite m-divisor representation is the core-marked specialization of the independently checked Mellin identity. No mandatory F-square factor remains because D already divides cv. The original condition (D,m)=1 is still enforced by the character zeros.

The stated single-row and actual Gauss-weighted double mean-square estimates are therefore valid. They do not inherit the stronger old reflected completed-row theorem or sum all compensation labels with the correlation savings needed for R4.

