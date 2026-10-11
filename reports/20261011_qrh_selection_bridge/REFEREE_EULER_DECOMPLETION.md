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


# Review of Part III, Section 8

## Referee addendum: complete principal-row contour comparison

### Verdict and quantifiers

Section 8 of Part III of the report passes. It proves a genuine power-saving comparison for the isolated u=1 contribution of the new core-marked, decompleted probe. Assume 1/2<beta_*<=1, where beta_* is the original supremum over the finite-order Hecke family; no zero is assumed to attain that supremum. With fixed positive slot exponents and the original geometry, there is sigma_pr>0 such that

P_pr(Z)/(c_S A_T(Z)) - f_fixed(Z)
 = O_{eta,data}(Z^{beta_*-11/16-sigma_pr}).

The choice of the small parameters and sigma_pr may depend on beta_*-1/2 and the fixed slot exponents. This theorem does not estimate the sum of nonprincipal rows or the new probe's negative low correlation.

### General principal local replacement

Deleting the original e_0=0, positive-even-l family gives, at u=1 and general x,w,z,

(1-R)P_core^*=-d-eta(p)(P-1)P^{-x-w}V/(1-V).

Substitution into the exact marked-minus-rescaled operation yields equation (8.2):

G_core^flat=-(1-W)/(1-d) [1-V+(P-1)WV] - W H_p^flat.

There is no denominator 1-R, P_p or H_p. On Omega_delta, |PWV|<=P^{-1+3delta/4} and 1-d is bounded away from zero. Hence G_core^flat is uniformly bounded. Normal positive majorants for the unselected product and elementary slot ideal counts give the full correction bound C Z^{ell Re z} on every fixed real parameter box, uniformly at all heights. The manuscript explicitly includes the required real-box qualification.

### Reciprocal input and contour legality

The original source's Logarithmic Control lemma was read directly. Its global conclusion holds to the right of every b>=beta_* at a fixed positive distance, not only in the old 7/8 range. The fixed target reciprocal therefore has a polynomial height bound on Re x=beta_*+e and the intervening right-hand strip. The finite deleted Euler factors are nonzero on positive real half-planes and have fixed uniform bounds here. For a principal target, the pole of L at one becomes a zero of 1/L and creates no residue.

The original M(z) is holomorphic for Re z>0 and rapidly decreasing on closed positive real strips; W_1's Mellin transform has the corresponding vertical decay. Their product with exp(-(Im x+Im z)^2) is rapidly decreasing jointly in all three heights, by the determinant-one linear change (Im x,Im z,Im w)->(Im x+Im z,Im z,Im w). This absorbs the reciprocal and zeta polynomial bounds and justifies horizontal boundaries and all contour exchanges. The same reasoning applies after taking each residue.

The starting lines (3,3,2), the intermediate lines (beta_*+e,1+e,1/6+e), and the final w,z lines all lie in the proved correction domain. Lowering w crosses only w=1; in that residue lowering z crosses only z=1/6. The unreduced w remainder keeps z above 1/6. No nonprincipal row is moved in this argument.

### Constants and the three errors

The two scalar zeta residues give exactly

c_S=widehat W_1(1) M(1/6) [Res zeta_F^S]^2/6.

After division by c_S A_T, the double residue is the one-dimensional integral displayed in the manuscript, including its factor 1+R_Z(x). The three error exponents are precisely

beta_*-11/16+(1+h)e-l_y delta/8,
beta_*-11/16+e-h delta/24,
beta_*-11/16+e-ell_min/2,

up to an arbitrary positive epsilon. They follow from the exact exponent l_x/2+Re x-1+h Re z+l_y(Re w-1), with h=13/16 and l_y=23/48. The normalization A_T costs only a logarithmic power. The last error uses the independently proved all-height bound for R_Z.

The error-free principal integral can be moved rightward to Re x=2: the reciprocal has no intervening pole, the fixed multiplier is holomorphic and uniformly bounded on the relevant closed strip, and its Gaussian kills the horizontal boundaries. This is exactly f_fixed, not a Z-dependent surrogate.

Finally choose e small relative to all three positive gains, then epsilon smaller still. This proves sigma_pr>0. No angular L zero-free assertion, hidden residue from the removed factor, or attainment of beta_* is used.

The resulting principal integral step is now established. The remaining overall high comparison and low-side correlation require separate estimates.

# Review of Part V

## Referee: all-row core-selected factors and finite-slot savings

### Verdict

Part V of the report passes. It gives exact local identities for every actual sixth-power-free numerator row, a reflected holomorphy tube, and a quotient-free finite-slot dynamic expansion with a power saving. The result is uniform in all heights and moving rows, on the declared fixed real parameter boxes. It does not estimate the complete high integral summed over numerator rows.

### Exact parity deletion

The core mark removes e_0=0 and positive even v_p(n). Direct use of the original prime-power Gauss support gives its three contributions: R(1-P^{-1})/(1-V), the j=0 term rho P^{-w}R, and the j=5 term -kappa(p)P^{3-6x}, all divided by 1-R. In particular the j=5 term is indispensable. For j=5 it comes from the endpoint valuation where the principal-character Gauss sum is -P^{t-1}; for the other nonzero families the usual positive tail begins one six-step later.

Subtracting this family from the original local table yields exactly J_core,0=-D, J_core,5=0 and the unchanged four middle entries. The selected replacement is obtained by the same physical marked-minus-rescaled operation, with its unmarked rescaling term retained. Equations (4)–(7), including every ramified j entry, agree with direct substitution. There is no division by a potentially vanishing P_p or H_p.

### Reflected tube

For 0<delta<1/4 and e>0, take

1/2+delta<=sigma=Re x<=1-delta,
Re w>=1-sigma+e, Re z>=1/6+e.

The ten unramified correction exponents in (10) were checked individually. Each exceeds one by at least nu=min(e,delta). At row primes, the original J_j terms, including J_5, have decay at least nu; the common term has decay at least e and R/P at least 1+6delta+6e. Thus the unmarked product converges normally and has the stated q_u^epsilon positive-product bound, also after arbitrary selected factors are omitted. Strict margins give a neighborhood of each real-tube point.

The exact unramified error is equation (6). Its extra terms are bounded by d, V and PVW, giving O(P^{-delta}) throughout the tube. At p|u, the true selected terms can grow: j=2 contains P^{3/2-2sigma} and j=3 contains P^{2-3sigma}. They are not discarded. Every term in the full table is nevertheless O(P^sigma) on this tube, including the common P^{1-Re w} term. This distinction between local growth and the aggregate saving is essential.

### Finite-slot expansion

In an annular slot of scale P_i, unramified errors have total absolute weighted mass O(P_i^{Re z-delta}). Ramified errors occur at only O(log(2q_u)) prime divisors of u. Their weighted mass is therefore at most

C log(2q_u) P_i^{Re z-1+sigma}
 <= C_epsilon q_u^epsilon P_i^{Re z-delta}.

This sparse count, rather than a false local decay claim, handles the ramified growth. The zero-extended character makes every ramified non-error term zero; unramified non-error mass is O(P_i^{Re z}).

Expanding G_p=-conjugate(chi_p(u))H_p^flat+E_p in the finite tuple gives the main term exactly as the full unmarked product times the K slot character polynomials. Every remaining term has at least one error slot. Positive majorants control the omitted unselected product, and initially allocating epsilon/(2K+2) controls all finite products of divisor losses. Thus equations (14)–(15), with saving delta ell_min, follow without dividing by H_p or assuming its nonvanishing for arbitrary u.

The fixed real-box condition is necessary and correctly stated: q_p^{Re z-1} and P_i^{Re z-1} have comparison constants depending on an upper bound for Re z on a fixed annular support. All imaginary parts remain unrestricted.

### Stronger near-residue region

On the earlier Omega_delta, the unramified error is O(P^{-1/2-delta}). The three extra exponents are at least 1/2+delta, 1-delta/2 and 1-3delta/4, and the latter two exceed the first for delta<=1/4. The ramified bounds in (17) were checked from the same exact table; all are at most P^{1/2}. The identical sparse-count argument gives the stronger ell_min/2 slot saving in (18).

The new expansion is a valid arithmetic input to later numerator-row summation. It supplies no automatic bound for the reciprocal L-functions, the main character polynomials, or the full compensated low correlation. Those separate budgets remain explicit.

### Product majorant in the final Section 5

The additional bound (19) also passes. For sufficiently large unramified selected primes the uniform local estimate gives |H_p^flat-1|<=1/2, so and only so E_p/H_p^flat is safely defined. No division is made at ramified primes or by the full Euler product.

Partitioning tuples by their ramified-slot subset R, and then fixing those primes, leaves the unmarked Euler product with exactly those primes omitted. Its positive majorant is uniformly O(q_u^epsilon). The remaining unramified slot sums factor exactly as -S_i+e_i. The polynomials S_i need no adjustment because their original character is already zero at row primes. The omitted-product factor is independent of all those remaining unramified choices, so this step retains their actual cancellation.

The selected ramified sums have the same sparse-divisor bounds as above. Summing over R therefore gives the product of |S_i| plus its corresponding error mass, with delta in the reflected tube and 1/2 near the residue. Fixed constants inside the K factors can be absorbed in a fixed exterior constant. Epsilon allocation before the finite subset expansion keeps the claimed uniform q_u^epsilon dependence.

This stronger majorant genuinely preserves every unused slot polynomial. It remains a pointwise local/slot input, not a proved global numerator moment bound.

# Review of Part VI

## Referee: reflected joint numerator bound for the exact core probe

### Verdict

Part VI of the report passes on its stated retained family and conditional buffered reflected-numerator hypothesis (2). The source's original Proposition `probe-errors` was read directly for the unchanged conductor and functional-equation inputs. The new local argument permits Re z>=1/4 on a bounded real range, and yields

|L^S(w,chi_u) product_{i in I} D_i^{core,flat}|
 <= C U^{a-1/2+6e+epsilon}(3+T_1)^C
       product_{i in I} P_i^{Re z-1/2}.

Here 1/2+delta<=a<=1-delta, 0<e<delta/100, Re x=a+16e and Re w=1-a-6e. All original zeros and all strict ramified terms remain. This is a local retained-height joint estimate, not a proved global contour move or an unconditional numerator smallness estimate.

### 1. Local factors and admissible division

The exact unmarked polynomial was checked on these new lines. The bottleneck unramified monomial dW has exponent 1+10e; all other terms have larger than one margins, uniformly for Re z>=1/4. At row primes the common term has exponent at least 10e, and the J_j terms have margins at least 2delta, except the smaller J_1 term. Thus H_p^flat=1+O(P^{-nu}) even at row primes, nu=min(10e,delta), and the stronger unramified estimate holds.

Consequently all sufficiently large selected local factors, including ramified ones, are nonzero and have uniformly bounded inverses. The threshold is uniform in moving u and all phases. Division is only performed at these finitely selected factors. No nonvanishing of the whole Euler product or of unselected small-prime factors is required for the exact finite-slot factorization.

For p not dividing u, the exact compensation identity (10) cancels the bare W term. Its potentially leading errors are d and PVW, with decay at least min(a+16e,6 Re z-a-6e)>1/2+delta/2. Every remaining polynomial term has greater decay. This proves (12) with all original unit phases retained.

### 2. Ramified table and the strict term

After the slot weight is included and P^{Re z} is factored out, the non-strict exponents in (13) are correct. In particular the two j=1 terms have exponents -1-Re w and -Re w-6 Re z; the j=2, j=3 and j=4 exponents are respectively bounded above by -1/2-2delta, -1/2-delta and -1/2-2delta, with additional favorable e margins. The common rescaling term is also harmless.

The remaining strict term is exactly -(P-1)P^{-w} for j>=2. It is not removed by core marking and cannot be bounded by the unramified error estimate. Its normalized exponent is -Re w, as the manuscript records.

### 3. One simultaneous conductor allocation

The original Kummer/reciprocity construction gives conductor exponent exactly one at each good p|u, because the local character has order 6/gcd(6,j)>1. Therefore for any distinct selected strict labels J_0,

q_f <= C_S U product_{p in J_0} P^{-(j_p-1)}.

The primitive functional equation, the assumed reflected bound, and Stirling give conductor cost q_f^{A_*}, A_*=1/2-Re w=a-1/2+6e>0. Because Re w>=delta-6e>0, restoring fixed and imprimitive deleted Euler factors costs only U^epsilon; the old extra cost needed when Re w could be negative is not imported.

Applying the conductor inequality once to the entire strict tuple produces, at every strict label,

-Re w-(j_p-1)A_* <= -Re w-A_* = -1/2.

This supplies all central slot exponents simultaneously without spending the same conductor saving twice. Disjoint slots guarantee distinct primes. Divisor counts of ramified labels consume only a previously allocated U^epsilon; unramified labels have elementary positive mass with a strictly better exponent. Expanding any subset of error slots proves (4), including the empty subset.

### Scope

The exact dynamic decomposition (5) follows from local selected nonvanishing and the quotient-free tuple identity. Main slot polynomials retain row-independent coefficients and every original character mask. The bound assumes the source's reflected small-value hypothesis at the retained heights and does not prove it for all rows. No total row-count estimate, global numerator/reciprocal integral, or negative low correlation is inferred.

# Review of Part VII

## Audit of the exact completed-to-core-flat reflection transfer

The full note Part VII of the companion report passes. Its external reflection estimate is the user's result at [user commit 56c6cf64ac7e683e02e2a6fbf0f57f8004e24102](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/56c6cf64ac7e683e02e2a6fbf0f57f8004e24102/reports/20261011_qrh_selection_bridge/MARKED_ROW_REFLECTION.md), already independently audited. The new contribution is the exact change-of-marker identity, not another derivation of the user's completed reflection theorem.

For (D,m)=1, the completed k-series at fixed squarefree c,v is L^{S union supp(m)}(2+6t,kappa) times the product of r_p=kappa(p)P^{-2-6t} over marked primes missing from cv. The inverse product outside the whole D leaves the stated finite denominators. The finite sum over F|D has local factor 1-r_p at a prime of cv and r_p-r_p at a missing prime. Thus it cancels exactly to the core marker. The external indicator is required for shared (D,m)>1. No character of the scaling variable is inserted.

Gaussian inversion and all exchanges are legal by the independent physical majorant

\[
 C\frac{\sqrt U}{q_D}\sum_{F\mid D}q_F^{-4}\sum_aq_a^{-5}.
\]

In particular the identity is absolutely convergent at every U>0 and permits common factors in c,v,k.

For fixed F, discard (a,D)=1 only in the positive upper bound and apply the user's two-bound balance to D'=D/F, U'=U/q_F^6. Multiplication by q_F^{-2} produces respectively sqrt(U)q_D^{-1}q_F^{-4} and H(m)^{2/3}U^{-1/6}q_F^{-1}. Summing gives exactly

\[
 |B_{D,core}^{flat}(U;m,s)|\ll
 \min\{\sqrt U/q_D,
 R(m)^{2/3}U^{-1/6}\prod_{p\mid D}(1+1/q_p)\}.
\]

The product is not an absolute constant for unrestricted squarefree D. It is uniformly bounded in the actual fixed finite K-slot family, which is the stated application. This supplies a legitimate full-scale pointwise bound for the changed core-flat row. It does not transfer the entire slot-summed reflected theorem or prove the full low correlation.
