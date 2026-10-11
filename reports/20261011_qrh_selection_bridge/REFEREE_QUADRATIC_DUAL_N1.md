# Independent review: physical nonprincipal dual-sector estimates

Companion: [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md).

# Review of Part I

## Referee: rough-residual quadratic dual elimination

### Verdict and exact scope

The theorem in Part I passes for the stated physical sector: n=1, c=Dc_0 with c_0 squarefree and all its prime norms exceeding the fixed support constant times Y', and first-Poisson indices H=epsilon v^3 a^6 with v nonunit squarefree. All auxiliary xi, original mark phases, and nonunit masks are retained. The conclusion is uniform rapid decay for this sector, not the entire R4 correlation.

### Exact first completion and frequency normalization

The simplified n=1 CRT identity agrees with the original Gauss conventions. If a common prime of c and s occurs to order at least two in s, the row vanishes by the Gauss support and the original chi_c zero mask. In the remaining case, s=gs_1 and c=gc_1 with g,s_1,c_1 pairwise coprime. The g part produces the Ramanujan sum. The unshared parts produce the stated chi_{s_1}, conjugate chi_{c_1}, and conjugate xi factors; the original gamma_1 gamma_2=mu alpha G identity removes the remaining fixed Gauss phases.

The least-period dual variable is k, whereas the original full-modulus dual is H=gk. The manuscript correctly uses H for the subsequent cutoff. Its Fourier parameter is sqrt(Q)H/(bsc), whose squared modulus is X'Y' q_H/(q_s q_c), comparable to X' q_H/q_c on the original s support. Nonzero terms force g=(c,rad H): a c prime in g divides H, and a c prime outside g is excluded from H by conjugate chi_{c/g}(H).

### Cutoffs and all masks

The Gaussian c cutoff q_c<=Z^{1+ell'+delta} and the Fourier cutoff q_H<=Z^{13/16+2delta} have arbitrarily small power tails after taking sufficiently many Schwartz seminorms. The exponent 13/16 is exactly (1+1/6-d)-(17/48-d). All discarded tails are bounded as tails of the exact series, not removed while preserving a false equality.

For H=epsilon v^3 a^6, q_v q_a^2<=Z^{13/48+2delta/3}. Since Y'>=c Z^{5/16}, every prime of v or a is below the roughness threshold for large Z. Thus (c_0,va)=1 and g|D. The same roughness condition gives (t,c_0)=1 automatically on the s=gt support.

The restriction (t,g)=1 is already encoded in chi_t(H). Expanding the remaining D/g mask with e|D/g, then the a mask with f|rad a, is exact. Here e is prime to H. Terms with (f,v)>1 are zero, as stated; f may share primes with g, and the signed finite expansion still correctly retains the original masks. No artificial coprimality between v and a is imposed.

The remaining periodic z coefficient is a bounded fixed bad-ray function times the primitive quadratic character chi_v(z)^3. All auxiliary fixed cosets and unit phases can be included in the bad modulus, which is prime to v. Because v is a nonunit, its complete average is zero even after retaining those cosets.

### Second completion and uniformity

The z norm scale V=Y'/(q_g q_e q_f) satisfies

V/q_v >= c Z^{1/24-2delta/3} q_a > c Z^{1/32}

for 0<delta<1/64. This uses ge|D and q_f<=q_a. The original d cancels exactly, so the margin is uniform for all permitted J.

All differentiation is in the normalized radial variable q_s/Y', which ranges in a fixed positive annulus. Chain-rule powers from the Fourier argument are absorbed by its arbitrarily high Schwartz decay. Hence the polynomial prefactor in Z can be chosen independently of the desired integration-by-parts order; the dependence on the real Mellin parameter is a fixed polynomial for each chosen order.

Finite Fourier coefficients of the bounded periodic function are bounded absolutely. Poisson on its actual modulus, whose norm is a fixed multiple of q_v, has no zero term. The remaining dual lattice sum is bounded by C_B V(q_v/V)^B times the stated seminorms. No additional modulus factor is missing: the finite residue frequencies and the ordinary lattice frequencies together form this scaled dual lattice. The positive uniform margin absorbs all remaining polynomial counts of c,D,H,e,f and all fixed front factors.

The rapid-decay conclusion follows. The manuscript correctly excludes generic cubic/sextic cores, c_0 with smaller prime factors, and n>1. No estimate for those remaining sectors follows from this argument.

# Review of Part II

## Referee: full nonprincipal quadratic dual sector of the n=1 probe

### Verdict

Part II passes. It removes the rough-residual restriction from the companion sector estimate, at the cost of a weaker power upper bound. For the exact n=1 physical layer and all nonprincipal quadratic-core indices H=epsilon v^3 a^6, with v nonunit squarefree and no coprimality imposed between v and a, the R4 contribution is

O_epsilon((1+|nu|)^{C_epsilon} Z^{25/48-d/2+epsilon}).

The corresponding normalized atomic probe is O(Z^{5/48+d/2+epsilon}); after the original r tuple counts and q_r^{-3/2} coefficients, the complete compensation of this layer is O(Z^{5/48+epsilon}). The other physical/kernel sectors remain outside the theorem.

### Exact arithmetic and masks

The first completion and H=gk full-modulus normalization were checked in the companion referee. For fixed c,H, nonzero terms give g=(c,rad H), c=gc_1, s=gt and (c_1,H)=1. The restriction (t,g)=1 is already contained in chi_t(H), while the c_1 mask is expanded exactly over e|c_1. Since e is prime to H, expanding the a mask with f|rad a introduces no missing e mask. The original zero value when (f,v)>1 is retained.

The remaining z character is primitive quadratic at the good primes of v, multiplied by a bounded function on one fixed bad modulus. Dependence of that bounded function on g,e,f,v and the unit does not change its uniform finite-modulus bounds. There are no hidden moving good-prime conditions outside the displayed e,f sums.

### All-scale character estimate

On a modulus equal to a fixed bad ideal times v, normalized finite Fourier coefficients have magnitude at most C/sqrt(q_v). This follows from the primitive quadratic Gauss transform and CRT, while the bad-modulus coefficient is bounded. The zero coefficient vanishes because v is nonunit.

After Poisson at physical norm scale V, the remaining dual Schwartz sum is O(q_v/V) when V<=q_v, and O((V/q_v)^{-B}) when V>=q_v. Multiplication by V/sqrt(q_v) gives the uniform bound C sqrt(q_v) for all V>0. Fixed primary/ray conditions do not spoil the cancellation.

The smooth norm variable is r=q_s/Y' in a fixed positive annulus. All chain-rule factors from the first Fourier transform are absorbed by its Schwartz decay. The stated seminorm estimate retains (1+X'q_H/C)^{-N} without introducing Z powers growing with the derivative order.

### Column and slot sums

In a c annulus, the constraints D/(D,g)|c_1 and e|c_1 imply L=lcm(e,D/(D,g))|c_1. The reciprocal ideal mass of multiples of L in any positive norm annulus is O(1/q_L), uniformly in its center; empty annuli are harmless. This remains true when the Gaussian center depends on D.

The Ramanujan bound q_g exactly cancels the q_g^{-1} from q_c^{-1}. Because actual s support gives q_g q_e q_f<=C Y', the original slot sum over D has bound C_slots/q_e: its local factor is one at primes dividing eg and 1/q_p elsewhere. Each fixed positive-width exponent slot contains O_slots(1) divisors of eg, while the reciprocal sum over the whole slot is bounded by elementary ideal counting. This proves the LCM density inequality with shared primes fully included.

Summing e costs only log(2+Y'). The possible g|rad H and f|rad a contribute arbitrarily small divisor powers, including shared v,a primes.

### Frequency tails and exponents

The weighted H count is O(K^{1/2+epsilon}) for K>=1, with rapid-decay control for K<1. Indeed sum_{q_v<=T} sqrt(q_v)=O(T^{3/2}) and T=K^{1/3}/q_a^2, leaving the convergent ideal sum sum_a q_a^{-3}. The actual Fourier weight, not a discarded tail, permits this estimate.

The c annuli C_j=e^j ZP have a common Gaussian bound exp(-c j^2), uniformly over all D in the prescribed slots. It absorbs both the Fourier small losses and the positive/negative annulus powers. Combining all terms gives

Q/Y'^{3/2} * (ZP/X')^{1/2} Z^epsilon.

At the original scales this is exactly Z^{25/48-d/2+epsilon}. Multiplication by Q^{-1/2} gives Z^{5/48+d/2+epsilon}. The r tuple count contributes Z^d and its explicit coefficient Z^{-3d/2}, leaving Z^{5/48+epsilon} for the compensated layer. Every exponent and normalization has been independently checked.

This is a bound for a full nonzero dual kernel type of the real linear probe. It is still short of the negative low target by 7/24 and yields no R4 or RH conclusion by itself.


# Review of Part III: all physical n

## Referee: complete nonprincipal quadratic dual type, all physical n

### Verdict and scope

Part III of the companion report passes. It proves the complete nonprincipal quadratic dual-sector estimate, summed over all physical n, for both the original completed-index marking and the newly defined core marking. With original X',Y',slots fixed at Z and every 0<T<=Z,

|S_quad(T)| <= C_epsilon (1+|nu|)^{C_epsilon} Z^epsilon
              Q/Y'^{3/2} * sqrt(TP/X').

The same bound transfers to the exact first Mobius-decompleted core probe. At T=Z the entire original finite compensation of this dual type is O(Z^{5/48+epsilon}). This does not cover principal/unit-core or generic cubic/sextic dual types and remains 7/24 above the required negative low exponent.

### 1. Exact square-layer reduction and frequency labels

Writing n=n_0 r^2 preserves the exact source coefficient identity and leaves the unit mask 1_{(r,m)=1}. Its finite Mobius expansion over h|rad r is exact, including zero terms when h meets c n_0. Splitting h into j=(h,rad s) and k=h/j, the prime-power Gauss support gives j^2|s and (s,k)=1, and the residual frequency condition is k|m.

Substitution m=k m' contributes xi(k)chi_{cn_0^3}(k)conjugate(chi_s(k)). The full frequency relation H=(r^6/k)L is exact as an element relation, not merely a norm comparison. A quadratic-core H has valuations 0 or 3 modulo six; the lower bound 6v_p(r)-1 therefore forces r|a. Thus H'=H/r^6 retains the same sixth-power-free core and unit and L=kH'. Unit covariance of the complete periodic arithmetic function cancels the substitution phase at this frequency. The Fourier argument becomes exactly the original argument for H', and the prefactor changes only by 1/q_k.

These steps preserve the original high-side labels. They do not replace the probe by a bare mean without xi.

### 2. Both squarefree physical branches

Direct substitution into the source's local scalar table confirms the only two possibilities at p|n_0:

- e_0=0, s valuation one, H' valuation three: C has magnitude P^3;
- e_0=1, s valuation zero, H' valuation three: C has magnitude P^{7/2}.

All higher H' valuations in this branch vanish. Therefore n_0|v and (n_0,a')=1. With E=(c,n_0), F=n_0/E, the exact normalization gives local magnitudes P^{-2} in E and P^{-3/2} in F, or globally the prefactor Q/(sqrt(q_b)sqrt(q_s)q_c q_{n_0}).

The residual shared c,s divisor is g=(c,rad H')/E. Its Ramanujan factor is at most q_g, not q_{Fg}. Writing c=E g c_1 leaves the important weight 1/(q_{n_0}q_E q_{c_1}). The forced F and g factors are extracted from s; there is no erroneous factor chi_F(H') multiplying the free-t character. The source's coefficientwise CRT and reciprocity cancellation gives precisely chi_t(H') on the remaining free s variable, with only bounded fixed bad-ray factors. The moving good-prime part remains primitive quadratic, and all its zeros are retained.

### 3. Second completion and actual marking density

After the e|c_1 and f|rad(k a') masks, the free norm scale is Y'/(q_F q_g q_j^2 q_e q_f). The all-scale smooth quadratic bound C sqrt(q_v) applies without loss from shortening that scale. Normalized derivatives retain the full first-Fourier decay with denominator C q_{n_0}^3.

The original marker yields L=lcm(e,D/(D,g n_0 r)); the core marker drops r from the gcd. Reciprocal c_1 mass is O(1/q_L) on every positive annular scale. Summing the actual prime slots costs at most (q_r q_H')^epsilon/q_e, even with no hard H' cutoff: the number of slot primes dividing e g n_0 r is controlled by log(Y' q_r q_H')/log Z. All tail losses are thus arbitrarily small powers, not a hidden factor counting every D.

The two physical branches have total positive weight

sum_{n_0|v} sum_{E|n_0} 1/(q_{n_0}q_E)
 = product_{p|v}(1+P^{-1}+P^{-2}) <= C_epsilon q_v^epsilon.

Additional support restrictions can be omitted only at this positive-majorant stage, as done in the manuscript. No physical branch is discarded before its phase and normalization are established.

### 4. Simultaneous tails and uniform third scale

For fixed n_0,r the Gaussian annuli C_l=e^l TP/(q_{n_0}^3 q_r^6) give Fourier scale K_l=C_l q_{n_0}^3/X'=e^l TP/(q_r^6 X'), independent of n_0. This independence justifies performing the weighted physical-branch sum before the quadratic frequency count.

That count, with all Fourier tails, is O(K_l^{1/2+epsilon}) for K_l>=1 and O(K_l^{1/2}) for K_l<=1. Since 0<T<=Z and the original geometric scales are fixed powers of Z, the extra positive small powers are uniformly absorbed by Z^epsilon and exp(O(epsilon|l|)). The Gaussian annulus weight absorbs the latter for all l, including scales below one.

The exact square-layer coefficient q_r^{-2}, the Gaussian square-root scale q_r^{-3}, and the substitution factor q_k^{-1} give q_r^{-5+epsilon}/q_k. The choices h|rad r and j|h cost at most 3^{omega(r)}, absorbed by a previously allocated small power. Hence the entire r sum converges absolutely and the claimed bound is uniform for every positive T<=Z.

Finally the external decompletion has coefficient q_d^{-2} and T=Z/q_d^6. The proved uniform positive T^{1/2} dependence gives the summable factor q_d^{-5}. Modulus lifting by d^6 preserves the core and unit, so the sector commutes with that transform. This is a proved transfer of the present positive-exponent estimate, not an assumption about the unproved negative R4 target.

The Q^{-1/2} normalization and original rescaling tuple count were checked independently and give the final exponent 5/48.

# Review of Part IV

## Audit of the common-coefficient quadratic two-column estimate

The lemma in Part IV of the companion report passes on its stated domain. Its common-coefficient and nonprincipal smooth-column hypotheses are essential.

The primary Goldmakher–Louvel source, arXiv:1112.1642v2, Definition 1, Theorem 1.1 and Corollary 1.2, has been read directly. It treats squarefree ideal rows and columns in a fixed quadratic Hecke family, with squared norm bound (VL)^epsilon(V+L). The Eisenstein quadratic subfamily and fixed ray separation are compatible with this statement. Fixed ray factors can be incorporated into common coefficients and bounded row factors; arbitrary row-dependent column coefficients are not covered.

For common squarefree coefficients of squared mass L^{-1+epsilon}, the resulting norm is (VL)^epsilon sqrt(1+V/L). For the original all-power smooth s column, writing s=t ell^2 and applying Minkowski before the norm bound produces sqrt(VS) sum q_ell^{-1}+S sum q_ell^{-2}. Thus the short-column norm is sqrt(VS) up to small powers when S<=V. The row restriction (v,ell)=1 is removed only from a positive squared norm.

For S>=V, the actual nonprincipal character, including its fixed ray twists, has conductor comparable to V. Primitive two-dimensional Poisson has no zero frequency. Finite Gauss coefficients have size O(sqrt(V)); Schwartz decay gives per row (S/sqrt(V))(S/V)^{-A}, after increasing derivative order. With O(V) rows, the norm is S(S/V)^{-A}. Fixed excluded primes have bounded finite decompositions. This step does not extend to arbitrary s coefficients or to a principal component.

The finite divisor-scale sum is correct. With E_0=Y/(GfV), the range q_e>=E_0 contributes at most

\[
 \sqrt{VY/(Gf)}\sum q_e^{-3/2}
 +V\sqrt{Y/(Cf)}\sum q_e^{-1}.
\]

The first term is O(V) whether E_0>=1 or E_0<1. Below E_0, the two powers A-2 and A-3/2 sum to E_0^{A-1} and E_0^{A-1/2} for A>1. Their contribution is O_A(V(1+sqrt(Y/(Cf)))). The actual finite cutoff makes the harmonic term logarithmic. Constant-factor scales below one are harmless only through the stated fixed rescaling.

Absorbing g|rad(va) into the row is valid only under all four stated separation conditions, including a common integrable smooth decomposition and the absence of a residual moving mask in the long s column. This certificate establishes the analytic lemma; it does not certify a separate arithmetic reduction of R4 to that lemma.

Primary source: https://arxiv.org/pdf/1112.1642

# Review of Part V

## Audit of the complete nonprincipal quadratic bilinear sector

### Verdict

Part V of the companion report, including the explicit finite e cutoff and the j-support clarification, passes on its stated scope. The analytical common-coefficient lemma has a separate certificate, the preceding Part IV review. The result covers the original completed marking, the changed core marking, all physical n, and the exact first Möbius-decompleted core marking, within the nonprincipal quadratic dual type H=epsilon v^3 a^6 with v nonunit squarefree. It does not cover the principal/unit-core or generic cubic/sextic types.

The original geometry gives S_quad(Z) bounded by Z^{37/96-d/2+epsilon}, with the stated polynomial dependence on the fixed real Fourier parameter. The original normalization and finite signed compensation give Z^{-1/32+epsilon} for this complete type.

### Arithmetic and common coefficients

At n=1 the exact first completion has c=g c_1, s=g t and Ramanujan factor phi(g), because H'/g still has each prime of g to exponent at least two. Expanding the remaining gcd mask with e|c_1 gives c_1=e c_2 and t=e f s_2. Squarefreeness makes mu(c)mu(e)=mu(g)mu(c_2), and the two quadratic e-character factors cancel on their genuine unit support. The factor eta(e) remains. The residual c_2 character and s_2 character are the same quadratic family. The conditions (c_2,e a')=1 are fixed common-column masks; the v part of g is already enforced by the character zero extension. The a' and k masks on the s variable are expanded, rather than dropped from a mixed product.

The actual marks partition into the first applicable factor among r,n_0,g,e,c_2 (omitting r for core marking). Choices at fixed factors are scalar; choices at n_0,g are row coefficients; choices at c_2 are divisor-bounded common column coefficients. Their squared reciprocal-column mass is L^{-1+epsilon}. The Gaussian's D dependence is separated on a zero-real-part Mellin line, so D contributes unit-modulus powers rather than an unrecorded real power.

For general n=n_0r^2, the previous exact two-branch CRT calculation is retained. The support n_0|v and (n_0,a')=1 and the split n_0=EF produce the factor 1/(q_{n_0}q_E). The forced F branches have already been extracted; no character is evaluated at their forced nonunits. The j primes are disjoint from c n_0. Their ordinary free-s branch vanishes when (j,H')>1; surviving j^2 phases have modulus one and belong to the row. This distinguishes them from the special forced F branches.

The whole divisor-many g and n_0,E choices in each dyadic block can be included in row coefficients after common smooth separation. No remaining moving divisor coefficient is inserted into the long s column. The source local factorization leaves only the true quadratic free-variable characters and fixed finite ray factors. Thus the long-column Poisson step applies to actual nonprincipal characters, not to an arbitrary bounded-coefficient sum.

### Scale budget and tails

The physical scales are C_*=U_l/(N^3B), Y_*=Y'B/(N q_j^2), with outside factor 1/(NB). The exact cancellation is

\[
 \frac{V}{NB}\left(1+\sqrt{Y_*/(C_*q_f)}\right)
 =V\left(\frac1{NB}+\frac1{q_j}\sqrt{Y'/(U_lq_f)}\right).
\]

The finite e range comes from nonempty c and s annuli. Dyadic n_0,E,g and divisor f counts incur only arbitrarily small powers. Common logarithmic Fourier separation has integrable seminorm bounds; powers of the first Fourier argument are absorbed by its Schwartz decay.

Summing quadratic rows with the complete Fourier weight gives K^{1/3} for K>=1 and an arbitrary prescribed K^M for K<=1, with K=U_l/X'. The sum over a' has convergent norm power -2. For square layers the first large-K term has q_r^{-4}; the second has q_r^{-1}, but only up to q_r^6<=e^l TP/X'. Beyond this finite range the small-K Schwartz bound gives convergent powers. Gaussian annuli preserve an arbitrary small-K power after increasing derivative order. This justifies the stated uniform independent-T estimate without replacing it by a coupled-scale estimate.

Applying that estimate to T=Z/q_d^6 with the exact outer q_d^{-2} Möbius weight has the same summable first term, finite harmonic second term and convergent small-K tail. The redundant-frequency lift preserves the sixth-free core and unit. Hence the exact core-flat transfer is legitimate; it does not assume convergence of an unproved negative whole-probe bound.

Finally Q/Y'^{3/2} has exponent 11/96-d/2 and (ZP/X')^{1/3} has exponent 13/48. Their sum is 37/96-d/2. The stated normalization gives -1/32 after compensation. The full target -3/16 remains stronger by 5/32, and other dual types remain outside this certificate.

### Original-marked flat corollary

The same outer-scale argument also covers the user's original-marked flat definition in `MARKED_ROW_REFLECTION.md`, commit 56c6cf64, Section 7. The independent-T estimate already covers both original completed and core markings with all physical windows fixed. Its application at T=Z/q_d^6, weighted by q_d^{-2}, and the sixth-power redundant-frequency lift do not depend on which of these two markers was used. Thus the same complete nonprincipal quadratic contribution Z^{-1/32+epsilon} applies to both exact flat definitions. This is one corollary of the same uniform bound, not a new index estimate or a transfer of the full reflected theorem.

# Review of Part VI: complete cubic good-core

## Audit of the complete cubic good-core sector

The full note Part VI of the companion report passes with its stated scope and exponent. It treats all H=epsilon w^2 a^6 with w nonunit cube-free, every original physical n, both original/core markings and each marking's exact first Möbius scale transform. It does not include unit-only cores or genuine sextic good-core types.

### The family parameter and the two columns

The large-sieve row parameter is q_w, with w=v_1 v_2^2 genuinely cube-free. It is not the smaller conductor q_rad(w). The n=3 cube-free theorem therefore applies to the actual row family and squarefree reciprocal columns. The smooth all-power second column is decomposed into cube-free times cubes; its three norm sums have powers -3/2,-3,-5/2. The row restriction induced by the cube layer is removed only within a positive norm.

The actual primitive conductor c_w<=C q_w is enough for the two Poisson bounds. The global per-row bound sqrt(c_w) is at most C sqrt(M). For S>=C M and A>1/2, (S/sqrt(c_w))(S/c_w)^{-A} is at most a fixed multiple of (S/sqrt(M))(S/M)^{-A}. With O(M) rows, this proves the stated long-column norm. Thus the mixed cube-free family does not require a false conductor comparability assertion.

The finite e-sum keeps all three terms M, M^{11/10}(Y_f/C_*)^{1/2}, M^{6/5}(Y_f/C_*)^{1/6}. Splitting at Y_f/(GM) and Y_f/(GM^{4/5}) proves it without assuming C_*>=Y_f. The physical nonempty-annulus cutoff is retained.

### Exact arithmetic and odd branches

For n=n_0r^2, the original coefficient covariance and Möbius expansion of the r-mask are used without coprimality assumptions. The full-modulus lift is H=(r^6/k)L. Its lower valuation 6v_p(r)-1, combined with cubic residues 0,2,4 modulo six, forces r|a. The unit-covariance phases then cancel exactly, leaving q_r^{-2}q_k^{-1} and the Gaussian scale divided by q_r^6.

At a prime of squarefree n_0, the source local C table has exactly two cubic branches. For j'=2, (e_0,k_s)=(0,0), C=P^2G_3 and the normalized magnitude is P^{-3/2}. For j'=4, (e_0,k_s)=(1,1), C=omega^{-1}G_1P^3G_3 and the normalized magnitude is P^{-2}. Higher lifts 2+6m or 4+6m do not survive. Consequently n_0=F_2E_4 with F_2|v_1, E_4|v_2 and (n_0,a')=1. Only E_4 is forced into both c and s. It has no Ramanujan factor. Extracting the c divisor E_4 gives precisely q_{n_0}^{-3/2}.

The local rho^{-3} phases are fixed-unit factors because the remaining good core occurs as a square, and its sixth power disappears. They do not couple the moving row divisor to the free columns. The separate j primes are ordinary free-s branches, vanish if (j,H')>1, and must not be confused with the forced E_4 branches.

The common g has Ramanujan factor phi(g). Expanding the true gcd and sixth-power masks retains eta(e), the actual character zeros, the fixed c_2 masks, and only common smooth/ray coefficients in s_2. Actual slots split by priority among r,n_0,g,e,c_2, with r omitted for the core marker. The n_0,E_4,g divisor sums are inside the row coefficient; common-column mass remains L^{-1+epsilon}. The Gaussian's D dependence is separated on a zero-real-part Mellin line.

### Complete ranges and exponents

The true ratio Y_*/(C_*q_f)=Y'N^3/(U_l q_j^2 q_f), multiplied by N^{-3/2}, produces exactly the three terms in (21): N^{-3/2}, no N factor, and N^{-1}. The middle term therefore costs only a logarithmic number of dyadic ranges after divisor choices have already been pooled inside each row.

The fully weighted M and a' sums have powers K_l^{1/2}, K_l^{11/20}, K_l^{3/5}. The a' norm powers are -3,-33/10,-18/5 and converge. Small K_l is controlled by the retained arbitrary-order Fourier decay. Combining with the square-layer coefficient gives q_r^{-5}, q_r^{-23/10}, q_r^{-23/5}. Each is absolutely summable after the divisor-small losses. All Gaussian annuli remain included.

The exact outer Möbius scale sum has the same three summable powers and preserves the cubic core and original unit. Thus it applies separately to original-flat and core-flat without an unproved scale-covariance assumption.

At T=Z, the second and third terms relative to the first are Z^{-97/320} and Z^{-1/30}. The first gives S_cub bounded by Z^{25/48-d/2+epsilon}; the original normalization and signed compensation give Z^{5/48+epsilon}. This is a bound for a complete nonprincipal cubic type, remains 7/24 above the full low target, and proves no RH exclusion.

# Review of Part VII: conditional genuine-column density

## Audit of the quadratic-density estimate for true Möbius columns

### Verdict and external input

The revised Part VII of the companion report passes as a conditional consequence of the explicitly stated user input Q: the fixed finite-order Hecke functions over the Eisenstein field have no zeros with real part greater than 7/8. This certificate does not independently rebuild the formal Q artifact or claim a new unconditional zero-free theorem.

The resulting true Möbius-column estimates, with fixed finite ray twists, the stated coprimality mask M, common smooth annular weights and polynomial Mellin-parameter dependence, are

\[
 \sum_{v\asymp V}|A_v(L;M,t_0)|
 \ll \mathfrak X^\epsilon(1+|t_0|)^C V^{1/3}L^{-1/8},
 \qquad L\ge V^{64/27},
\]

and

\[
 \|A_v(L;M,t_0)\|_2
 \ll \mathfrak X^\epsilon(1+|t_0|)^C V^{1/6}L^{-1/8},
 \qquad L\ge V^{32/27}.
\]

These are not estimates for arbitrary inner coefficients or for an already summed full physical sector.

### Fourth moment and zero detection

Goldmakher–Louvel is applied only to genuine squarefree quadratic indices. Applying the degree-four approximate functional equation to the square of the actual twisted L-function gives polynomials of length B at most V times a fixed power of the height. The coefficients are eta(n)tau(n)n^{-1/2-it}; the conductor-dependent weights admit a common Mellin separation and the dual root number is a bounded row factor. Splitting n=b ell^2 gives the stated norm sum ell^{-1}sqrt(V+B/ell^2), hence the fourth moment has conductor power V^{1+epsilon}. The revised Sobolev step uses L^2 and its first derivative in row L^2; differentiating their approximate functional equation introduces only logarithms and smooth-weight derivatives. It does not assume an extra fourth moment for L'.

The BGL source, arXiv:1112.1650, proof of Corollary 1.6, especially (5.3), was read directly. The manuscript uses its detector mechanism, not its published higher-order density conclusion. For one zero from each exceptional row, retaining the restricted first term and applying Hölder with 4,2,4 genuinely preserves R^{1/4}. The Gamma-weighted height integrals are controlled by the polynomial-height moment bounds and exponential Gamma decay; varying real parts are handled by partial summation of common coefficients.

The detector's all-power b column has common coefficients a_b of divisor size. Splitting b=b_0 ell^2, then Minkowski and the quadratic sieve, gives the norm sqrt(VU)+U, up to small powers. The actual induced row masks are removed only inside a positive norm. Thus the second detector term is V X^{1-2sigma}+Y^{2-2sigma}.

With X=V and Y=V^{3/(4-2sigma)}, division of the first alternative by R^{1/4} gives exponent

\[
 d(\sigma)=3(1-\sigma)/(2-\sigma).
\]

The other alternative has the same or smaller conductor power. The fixed twist is a common coefficient throughout; no different character family is substituted. Polynomial height costs can later be absorbed by choosing the height exponent sufficiently small, after all desired losses and fixed buffers are chosen.

### Finite-height reciprocal estimate

The zero-free rectangle has height 4T, while the reciprocal bound is used only at height T and a fixed distance h to its right. Borel–Carathéodory discs centered on the Euler line stay inside that larger rectangle. They give a logarithmic bound for the analytic branch of log L. The two-constants argument for log|log L|, with the right Euler bound and exponentially small horizontal harmonic measure, yields |log L| bounded by a fixed power strictly below one of log(VT). This implies the stated subpower reciprocal bound. Zeros of log L itself are harmless for the subharmonic argument.

The corrected choice T>=4(1+|t_0|), with the Mellin contour truncated at height T/2, keeps every 1+s+it_0 strictly inside the reciprocal-height domain. Sufficiently many smooth derivatives control the horizontal joins and original Euler-line tails. Deleted factors caused by (c,M)=1 have product at most q_M^epsilon on Re s>=1/2+h; their local denominators cannot vanish there. A possible principal row is separated and its L pole becomes a reciprocal zero.

### Stratification and exact powers

Rows are classified using zeros in the larger finite-height box. Each bin is evaluated strictly to the right of its upper endpoint; zeros on Re s=7/8 are allowed and never crossed. The baseline count is O(V), corresponding to d(1/2)=1. Fixed-width bins and the height loss are absorbed only after choosing their parameters in the stated order.

Since d'(b)=-3/(2-b)^2, the first-moment exponent d(b)log V+(b-1)log L is increasing on [1/2,7/8] when log L/log V>=64/27. Its endpoint is V^{1/3}L^{-1/8}. For the squared moment the threshold is 32/27; taking its square root gives V^{1/6}L^{-1/8}. These endpoint powers are accurate only with the stated arbitrarily small losses.

The prescribed-column-prime identity is exact on its genuine unit support. For a fixed slot product D it introduces q_D^{-1} and length L/q_D, with the original squarefree/coprimality conditions. Summing fixed slots positively at the row estimate stage gives the effective length L/P_c, as stated. Divisor-boundedness alone would not establish this extension.

For the clean actual large-g block, V=Z^{13/48}, L=Z^{23/24}, S~V and pointwise smooth Poisson gives |B_v(S)| at most sqrt(V). Its bound V^{5/6}L^{-1/8} saves 95/576 relative to V, exceeding 5/32 by 5/576. This is a verified single-block consequence. Full moving e,g,odd/square layers, column slots and all other dual types still require their own complete budget.

Primary sources: https://arxiv.org/pdf/1112.1642 and https://arxiv.org/pdf/1112.1650 .

### Supplement: finite-divisor consequence, Section 7

Equations (24)–(31) of the added Section 7 also pass. Write x=P_c/R. If x>=V^{-1/3}, the old V+V/sqrt(R) bound is precisely the stated minimum branch. Otherwise S_*=xV^{32/27}<V is the exact threshold for the new selected-column second moment. Above it, the two norm products have powers V^{2/3}x^{1/8}S^{3/8} and V^{1/6}x^{1/8}S^{7/8}(S/V)^{-A}; each sums dyadically to V^{25/24}x^{1/8}. Below it, the old sqrt(VS) term is at most V^{59/54}x^{1/2}, whose ratio to the new term is V^{11/216}x^{3/8}<=V^{-2/27}. The constant V/sqrt(R) term is summed only over the actual finite e range. Fixed annular constants and logarithms are harmless.

The full bound is therefore min(V,V^{25/24}(P_c/R)^{1/8})+V/sqrt(R), with small ambient losses. Substitution of the actual odd-branch scales and multiplication by 1/(NB) gives exactly (NB)^{-3/4}q_j^{-1/4}f^{-1/8} times V^{25/24}P_c^{1/8}(Y'/U)^{1/8}. No full physical theorem is asserted merely from this substitution; its Fourier tails, square layers and compensation require the separate exact-interface argument.

The finalized domain also states that c is good and M is replaced by its S-outside part. This is the domain used for all Euler-mask factors in this certificate.

# Review of Part VIII: selected Euler multiplier moments

## Audit of moments of genuine selected-prime Euler multipliers

The revised Part VIII of the companion report passes. Its coefficients z_D are common to the rows, the slot prime sets are disjoint, and the number of slots J and moment order k are fixed. All c are good and the mask M is first replaced by its part outside the fixed deleted set S. No extra Euler factor at an already deleted bad prime is introduced.

For A_v=sum_D z_D psi_v(D)/q_D, the bound

\[
 \sum_{v\asymp V}|A_v|^{2k}
 \ll (VP)^\epsilon(1+V/P^k)
\]

is correct. Expanding A_v^k and partitioning the repeated primes by equality gives finitely many patterns. In slot i, r_i distinct primes and o_i odd multiplicities leave a squarefree common odd column of norm product P_i^{o_i}. Freeze the even-multiplicity primes, retain their row unit masks in the positive norm, and only then enlarge that norm. Their exclusions from the odd columns are common restrictions. The coefficient multiplicities are bounded solely in terms of fixed k,J.

The resulting row norm is bounded by sqrt(V+R) product P_i^{r_i-o_i/2-k}. The inequality k>=2r_i-o_i makes its sqrt(V) part at most sqrt(V)/P^{k/2}; r_i<=k makes its sqrt(R) part at most one. The constant-column case R=1 satisfies the same bound. Summing finitely many patterns and squaring proves the claim, without a prime-independence assumption.

For x in {0,1,-1}, the exact identity

\[
 \frac{\eta x q^{-s}}{1-\eta xq^{-s}}
 =\frac{\eta xq^{-s}+\eta^2x^2q^{-2s}}
 {1-\eta^2q^{-2s}}
\]

preserves x=0. The denominator is row-independent and uniformly nonzero for Re s>=1/2+delta. Expanding odd/even choices over the fixed slots and freezing even primes gives the factor P_even^{-Re s} after normalization. Applying the preceding moment bound to the odd slots yields the claimed norm 1+V^{1/(2k)}/sqrt(P), since Re s>=1/2. Raising it to 2k gives the stated Euler-multiplier moment uniformly in the imaginary part.

The selected Möbius Dirichlet-series identity in (8) is exact in its absolute region, with selected D coprime to the good part of M. Its nonunit zero masks remain exact. The normalized scalar length is (L/P)^{sigma-1}; the remaining multiplier is precisely E_v(s), rather than arbitrary extra coefficients. The displayed Hölder estimate over R exceptional rows is valid.

This certificate establishes the genuine selected multiplier moment. A density theorem, inverse-L control, the free-s moments and the complete physical divisor/slot budget must still be combined before asserting a bound for the full low probe.

# Review of Part IX: complete pure fifth-power sector

## Audit of the complete pure fifth-power sextic-core sector

Part IX of the companion report passes in its exact scope H=epsilon v^5 a^6, v nonunit squarefree, all physical n, original/core markings and both first-decompleted versions. It proves the claimed S exponent 133/480-d/2 and compensated exponent -67/480. It does not include mixed sextic cores, unit-only cores, or the full low target.

The sixth-order sieve's four reciprocal-column norm terms and the complete all-power smooth-column decomposition are correct. The sixth-power layer has summable norm powers -3,-6,-4,-11/2. Primitive Poisson applies to the actual nonprincipal character. The smooth norm transitions at S=V^{1/2}, V^{7/8}, V are the stated ones. Multiplying the four column terms and summing only the finite physical e range gives respectively V, V^{17/16}(Y_*/C_*f)^{1/2}, V^{9/8}(Y_*/C_*f)^{1/3}, V^{35/32}(Y_*/C_*f)^{1/12}. The borderline constant segment incurs only a finite logarithm.

The actual n=1 completion retains the true common c/s characters, eta(e), all reciprocal and gcd masks, and the marked-slot organization. No row-dependent inner coefficients are substituted.

The source local scalar table forces every physical n in this sector to be a square r^2. At p^b||r, no frequency valuation below 6b-1 survives. Above that boundary the exact comparison with the n=1 coefficient is P^{6b} times

\[
 M_p=1_{p^2\nmid s}\bigl(1-P^{-1}1_{p\nmid c,p\nmid s}\bigr).
\]

The cases e_0,k_s=(0,0),(0,1),(1,0),(1,1), and k_s>=2 agree individually with this formula. At the sole lower boundary j'=6b-1, e_0=k_s=0 and the scalar is exactly -P^{6b-1}. Thus the exceptional product h_0 divides both rad(r) and v, with a=(r/h_0)a' and (h_0,a'cs)=1. The coefficient is kappa(r)q_r^{-2}mu(h_0)q_{h_0}^{-1}.

The phase restoration is exact. Relative to H_eff=Hh_0/r^6, the unit factor chi_q^{k-t}(H/q^{j_q}) at other primes supplies chi_c(h_0) on the free c column and conjugate chi_s(h_0) on the free s column. Shared g factors cancel. Together with the ordinary sixth-power covariance these restore the full v character, including the original bad character; no character is evaluated at a forced nonunit.

The mask also has the exact expansion 1-1_{p^2|s}-P^{-1}1_{p\nmid c}1_{p\nmid s}. Hence only fixed c-unit conditions and fixed s-divisor extractions are needed. After splitting fixed-prime valuations in g,e,f, extracting a divisor from the free s variable reduces its scale. The outside Q/Y'^{3/2} normalization stays unchanged, and every term of the analytic bound is nondecreasing in that reduced scale. This justifies the common-column interface with at most C^{omega(r)} fixed choices.

Crucially, the actual Gaussian annulus q_c q_r^6~C_l implies q_r<=O(C_l^{1/6}). After the full Fourier moments and h_0<=r, the four r powers are -3,0,-1,-5/2. The second term therefore costs C_l^{1/6}, converting its apparent C_l^{-1/2} into C_l^{-1/3}; the third costs only logarithms. Empty subunit annuli stay empty. Gaussian summation preserves the resulting bound at every T>0 with the original windows fixed.

The four powers of C in the final positive envelope give exact outer Möbius exponents -16/5,-51/40,-27/20,-45/16. All are strictly below -1, so first decompletion is absolutely legitimate even with the exceptional fifth-power boundary. The redundant frequency lift preserves this pure core and unit.

The displayed original-scale exponent arithmetic is correct: the first envelope term dominates, gives S=133/480-d/2, and the original normalization/finite compensation gives -67/480. The remaining gap to -3/16 is 23/480 for this type, with other types still untreated.

The finalized square-layer normalization uses g=(c,rad(H_eff))=(c,rad(v a')), with H_eff=Hh_0/r^6. It need not equal (c,rad(H)) before removing ordinary sixth-power r primes. The latter primes are retained through the exact fixed multiplier M_p. This distinction is required by the common-column reduction and has been incorporated in the final text.

# Review of Part X: genuine smooth direct and dual moments

## Audit of the two-sided high moments of the true smooth quadratic column

Part X of the companion report passes on its stated domain: nonunit good squarefree rows q_v~V, actual nonprincipal fixed-ray twists with conductor comparable to V, 1<=S<=V, common smooth weights, and any fixed integer k>=1. No Q or Burgess input is required.

The k-th power of the original smooth column is a common polynomial of norm length O_k(S^k), with divisor-bounded coefficients. Its product indices are not assumed squarefree. Splitting n=b ell^2, retaining the induced row zero mask and enlarging only the positive norm, gives the exact bound sqrt(VN)+N up to small powers. Taking the k-th root yields V^{1/(2k)}sqrt(S)+S.

The actual primitive Poisson formula gives a unit-modulus root number times S/sqrt(q_f) and a conjugate common-character sum at scale q_f/S. Fixed deleted primes have a fixed finite decomposition. There is no zero Fourier term. Since q_f/V lies in a compact positive interval, a common cutoff in its logarithm and Fourier separation give integrable coefficient measures with uniform Schwartz seminorms. The root number and separated imaginary powers are row factors; no supremum over unrelated row-dependent dual weights is introduced.

The dual scale V/S is at least one. On its bounded main range the same moment proof applies even though the dual weight need not vanish at zero, because its coefficients remain bounded and supported in a polynomial of length O(V/S). Large dual annuli have arbitrarily rapid decay. Minkowski sums those tails and the common separation. Thus the dual bound is V^{1/(2k)}sqrt(S)+sqrt(V). Taking the minimum proves

\[
 \|B(S)\|_{2k}\ll (VS)^\epsilon
 \left[V^{1/(2k)}\sqrt S+\min(S,\sqrt V)\right].
\]

For nonradial weights the conductor-generator rotation is also separated by angular Fourier modes, with the corresponding unit phases absorbed into the row. Polynomial mode seminorm costs are summed against the original rapid angular decay. This preserves common dual columns.

Hölder over any R-row subset gives the displayed exceptional-set estimate, regardless of whether that subset depends on S. The alternative R min(S,sqrt(V)) is the genuine pointwise length/Poisson bound.

For the illustrative R<=V^{1/3} calculation, the fourth norm reduces to V^{1/4}sqrt(S) throughout 1<=S<=V. Combining fourth, sixth and pointwise bounds, then multiplying by S^{-1/8}, has maximum V^{53/72}, at S=V^{7/9}. The earlier intersection S=V^{5/9} gives only V^{17/24} and is not the global maximum. No complete marked physical exponent is inferred from this illustrative maximum alone.

# Review of Part XI: Q-conditional complete nonprincipal quadratic closure

## Independent referee: the complete nonprincipal quadratic sector

### Verdict

The theorem in Part XI of the companion report passes, conditional on its explicitly stated input Q and on the source-backed analytic inputs identified below. The complete nonprincipal quadratic type, with all physical indices and either original or core marking, has compensated bound

\[
 I_{\rm quad}=O_\epsilon(Z^{-439/2304+\epsilon}).
\]

The same conclusion holds for each exact first Möbius-flat operation. The margin below the required exponent \(-3/16\) is \(7/2304\). The statement concerns this complete dual type alone. It supplies neither a bound for the other dual types nor a proof of RH or of the full low comparison.

The proof does not use Burgess. In particular, no superseded pointwise-Burgess budget enters this verdict.

### 1. Inputs and quantifiers

The input Q is the user's fixed finite-order Hecke zero-free half-plane \(\Re s>7/8\), with the public provenance recorded in the accompanying density manuscript. This review does not claim an independent rerun of the user's Lean build. The true-column density theorem, its finite-height reciprocal estimate, the exact selected-prime Euler-multiplier moments, and the genuine direct/dual smooth quadratic moments have separate independent referee certificates.

After a fixed finite ray decomposition, the Möbius column really is the reciprocal of \(L(s,\eta\psi_v)\), with fixed finite-order \(\eta\). Common deleted Euler factors have only a small-power cost. The moving squarefree quadratic index remains the actual \(v\), and the smooth free column is not replaced by arbitrary coefficients before Poisson is used.

For density-bin endpoint \(b\), put \(a=1-b\) and \(d(a)=3a/(1+a)\). A bin contains at most a small-power factor times \(V^{d(a)}\). Contours lie strictly to the right of the upper bin endpoints. Consequently endpoints displaced by the fixed bin width change powers by \(O(h)\); the final positive margin permits choosing this width and every analytic epsilon loss sufficiently small. No estimate is asserted on a zero itself.

### 2. The full smooth-column scale

For \(R=V^{d(a)}\), the eighth moment and the pointwise bound give
\[
 \sum_{v\in\mathcal E}|B_v(S)|
 \ll Z^\epsilon\min\{R\min(S,\sqrt V),
 R^{7/8}\max(V^{1/8}\sqrt S,\min(S,\sqrt V))\}.
\]
The weighted expression \(S^{-a}\) times this bound has its first candidate maximum at \(S=V^{1/2}\), with exponent
\[
 F(a)=7d(a)/8+1/2-a/2.
\]
The second candidate maximum occurs at \(S=V^{(3+d(a))/4}\). Its difference from the first exponent is exactly
\[
 \frac{a(1-8a)}{8(1+a)}\le0
 \qquad(1/8\le a\le1/2).
\]
All smaller scales are covered by the increasing short-scale power pieces, and the genuine primitive-Poisson long-scale tail decreases rapidly. At \(a=1/8\) both maxima must be retained: they occur at \(V^{1/2}\) and \(V^{5/6}\), and both give \(F=35/48\). Thus the proof takes the maximum over the whole scale range.

### 3. Selected slots and actual common coefficients

Hölder with the selected multiplier's \(2k\)-moment applies to both terms of the preceding minimum. The remaining counting exponent is nonnegative because \(1/(2k)+1/8\le1\). Relative to the unweighted bound its factor is
\[
 R^{-1/(2k)}(1+V/P_c^k)^{1/(2k)}.
\]
For \(P_c\le\sqrt V\), write \(t=\log V/\log P_c\), \(m=\lfloor t\rfloor\ge2\). The choice \(k=m\) has no positive exponent if \(t\le m(1+a)\); the choice \(k=m+1\) has no positive exponent if \(t\ge2(m+1)(1+a)/3\). The intervals cover \([m,m+1]\), since \(m\ge2\). Tiny \(P_c\) is handled by its normalized pointwise bound. For \(P_c\ge\sqrt V\), \(k=2\) suffices. Therefore the total selected cost is
\[
 \ll V^\epsilon\{1+P_c^aV^{-d(a)/4}\}.
\]
Only finitely many fixed moments, depending on the chosen epsilon, are required.

The inherited priority assignment of original slots to \(r,n_0,g,e,c_2\) preserves common coefficients in the \(c_2\)-slot sum. The exclusions involving the variable divisors \(n_0\) and the \(v\)-part of \(g\) are already enforced by the original quadratic zero extension. The remaining exclusions involve fixed \(r,e,a'\) masks. Thus the selected multiplier in this argument is the genuine common-coefficient Euler multiplier, rather than a family of arbitrary row-dependent selected sums. Pooling the divisors \(n_0,E,g\) creates only a divisor-bounded row weight.

### 4. Odd physical branches and finite inclusion-exclusion

The inherited exact identities give the outside coefficient \((NB)^{-1}\) and the two lengths
\[
 L=\frac{U}{N^3BGq_e},\qquad
 S=\frac{Y'B}{NGq_j^2q_eq_f}.
\]
Hence \(L/S=Uq_j^2q_f/(Y'N^2B^2)\), independent of \(e\). The actual finite \(e\)-cutoff and reciprocal ideal mass reduce its dyadic summation to logarithms. The remaining bound is
\[
 V^{F(a)}(Y'/U)^a(NB)^{-1+2a}q_j^{-2a}q_f^{-a}
 \{1+P_c^aV^{-d(a)/4}\},
\]
up to small powers. Since \(-1+2a\le0\), all \(N,B\) dyads are harmless, including their logarithmic endpoint. The smooth \(s_2\) column retains the exact common smooth/ray form needed for the high-moment input. No signed mask was deleted inside a mixed product.

### 5. All Fourier, square, and flat tails

The two row exponents are
\[
 \kappa_0=F(a),\qquad \kappa_1=F(a)-d(a)/4.
\]
Their minima are respectively \(35/48\) and \(31/48\), both strictly greater than \(1/2\). The full Fourier envelope therefore gives a convergent \(a'\)-sum with weight \(q_{a'}^{-2\kappa}\), and a factor \((U/X')^{\kappa/3}\) for \(U/X'\ge1\). For \(U/X'\le1\), any prescribed sufficiently large positive power is available from the original Schwartz envelope. Gaussian annuli control both signs of the scale parameter.

Combining the physical square factor and an optional first flat factor as \(\rho=r\delta\) leaves coefficient \(q_\rho^{-2+\epsilon}\). At \(U_0=ZP\), the large-scale part is exactly bounded by
\[
 Y'^aU_0^{\kappa/3-a}X'^{-\kappa/3}
 \sum_{q_\rho\le(U_0/X')^{1/6}}
 q_\rho^{-2-2\kappa+6a+\epsilon}.
\]
For the first branch this exponent increases to \(-5/4\), so the series is genuinely absolutely summable. The second branch can reach \(-3/4\); its finite cutoff must be used. It contributes the boundary expression
\[
 P^aY'^aU_0^{-1/6}X'^{1/6-a}.
\]
Directly summing the complementary small-scale tail gives the same boundary bound: choosing \(M\) large in the small-scale Fourier bound gives a tail of \(q_\rho^{-2-6M+6a}\). Thus no divergent infinite series is suppressed. The core-preserving redundant-frequency lift for each exact flat operation is the already audited identity; it applies equally to original and core markings.

### 6. Exact normalization and exponents

After the original normalization and compensation, the two main exponents are
\[
 G_0(a)=-\frac{316a^2+107a+64}{384(a+1)},\qquad
 G_1(a)=-\frac{252a^2+121a+64}{384(a+1)}.
\]
Both are strictly decreasing:
\[
 G_0'=-\frac{316a^2+632a+43}{384(a+1)^2}<0,
 \qquad
 G_1'=-\frac{84a^2+168a+19}{128(a+1)^2}<0.
\]
The exact subset parameter adds \(-da\) to the second expression, so discarding it is safe. At \(a=1/8\),
\[
 G_0=-439/2304,\qquad G_1=-443/2304.
\]
The exact boundary exponent is \(-7/16+7a/24-da\le-7/24\). Restoring the unnormalized factor gives \(521/2304-d/2\) as stated. The final compensation removes the original subset's \(d/2\) exactly as in the previously audited normalization.

This verifies the claimed positive margin \(7/2304\), subject to the explicit Q input and only for the stated complete nonprincipal quadratic type.

### 7. Consistency with the user's new joint-Möbius interface

The user's commit `bbb8bba6f6a678848a270a4c950568a672cc975f`, `QUADRATIC_MOBIUS_GAIN.md` Sections 3--5, was independently read after the initial review. Its three structural requirements are consistent with this stronger mean proof and are now explicit in the revised manuscript:

1. Joint logarithmic Fourier separation retains fixed product cutoffs equal to one on the joint profile support. Each separated column is therefore still a compactly supported smooth sum. This justifies both the true Möbius Mellin shift and primitive smooth-column Poisson. Fourier constants must of course follow the chosen transform normalization.
2. Reciprocal estimates retain the actual imprimitive modulus, including every deleted prime, particularly h. The intrinsic character zero handles the v-supported factors; e,h,a' and the selected-slot restrictions are retained as their correct common masks or Euler factors. No arbitrarily large deleted modulus is hidden in a fixed primitive-conductor constant.
3. On compatible squarefree support, \(\mu(e)\mu(\operatorname{lcm}(e,D_0))=\mu(D_0/(D_0,e))\). In the priority assignment this is exactly the one-time cancellation producing the c_2 Möbius column and its selected Euler multiplier. There is no second free Möbius e sum; the proof bounds the actual finite e-sum in absolute value.

The added paragraph on the ambient size is also necessary and correct: before infinite sums it contains Z,V,q_rho,q_{a'},exp(|ell|), and separated heights. The initially arbitrary small powers of those labels are absorbed only afterward, using the strict a' margin, the first rho branch's -5/4 exponent, the second branch's actual finite cutoff and boundary term, and the full Schwartz/Gaussian tails.

These clarifications preserve the user's attribution and do not change the theorem or the exponent. The revised manuscript with SHA-256 `012219599c2e57a73cd1ab93e5b8e3a29d54d426d6271ecb2629bcfe9bd39705` was read back and passes with these explicit interpretations. The user's pointwise-column result and its warning about direct minimum bounds are not contradicted: the stronger argument additionally uses zero-density exceptional-row sizes and joint high moments, rather than multiplying two separate savings.

# Review of Part XII: Q-conditional complete cubic mean bound

## Independent referee: true Möbius mean for the complete cubic sector

### Verdict and scope

The revised Part XII of the companion report passes, conditional on the explicitly attributed Q input. For the complete nonprincipal cubic type, including all physical n, original or core marking, and either exact first flat operation, the compensated bound is
\[
 I_{\rm cub}(Z)\ll_\varepsilon Z^{2/45+\varepsilon}.
\]
It improves the preceding \(5/48\) exponent by \(43/720\). It remains \(167/720\) above the required \(-3/16\). This is an upper bound for this type alone, not a main-term asymptotic, a counterexample, a full low comparison, or an RH conclusion.

### Density input and actual characters

I checked the statement and proof of Corollary 1.5 in [de Faveri's original preprint](https://arxiv.org/html/2610.04045v1). At n=3 its middle interval collapses. Specialization gives precisely the two formulas D_* in the manuscript. The index is the norm of the actual cube-free ideal w, not the possibly smaller primitive conductor. The source allows cube-free outer rows and cube-free columns.

The fixed target twist can be inserted into the source proof: inverse-detector coefficients, its polynomial tail, and the approximate-functional-equation coefficients remain common coefficients. At the half-line the AFE length is at most \(M^{1/2}\) times a fixed height power. The cubic sieve's mixed term at that length is at most M. Cube layers have convergent weights; primitive root numbers are bounded row factors. Thus the required second moment and detector inequalities retain the cited M-exponents, with fixed-twist constants and polynomial height costs. This does not justify replacing a moving second character by a fixed twist.

The piecewise-linear majorant D in the draft is valid. On the last two intervals its differences from D_* are, with x=1-b,
\[
 \frac{(1-6x)^2}{3(1+6x)},\qquad
 \frac{(1-6x)^3}{6(1-12x^2)}.
\]
The first interval uses the trivial row count. The true-column finite-height inverse lemma is inherited with its strictly buffered contours, all actual deleted Euler factors, and explicit Q cap at 7/8. All c are good ideals and the common mask is replaced by its part outside the fixed excluded set. Q is an external user-supplied theorem with the previously recorded source-level and formal-verification scope; this review does not claim a new Lean build.

### Marked column and every free-column scale

Forcing the selected squarefree D_c gives its exact \(\mu(D_c)\eta(D_c)\overline{\psi_w(D_c)}/q_{D_c}\) factor and a true Möbius sum of length L/q_D. Summing the fixed slots gives the legitimate scalar \((L/P_c)^{b-1}\). Nonunit cases remain zero. This step is not valid for arbitrary divisor-bounded column coefficients; the manuscript uses the actual arithmetic column.

For R=M^D rows the positive restricted smooth-column norm yields
\[
 \sum|B_w(S)|\ll\min\{M^D\min(S,\sqrt M),M^{D/2}B_3(M,S)\}.
\]
Here the inherited genuine smooth B_3 has the three pieces \(\sqrt{MS}\), \(M^{1/3}S^{5/6}\), and M, with transitions \(M^{1/2}\) and \(M^{4/5}\); the actual long-column Poisson estimate controls the remaining scales.

After multiplication by \(S^{b-1}\), both short-scale pieces are nondecreasing. In the middle range the increasing moment bound meets the decreasing pointwise bound at
\[
 S_0=M^{(3D+1)/5}.
\]
Since \(1/2\le D\le1\), this point belongs to that middle range. The complete maximum is
\[
 M^{J(b,D)},\qquad J=\frac{D(2+3b)}5+\frac{3+2b}{10}.
\]
The capped range and long-column tail give no larger value. Consequently the actual finite reciprocal e-sum is bounded by this maximum times the fixed length-ratio factor and logarithms. This includes ranges where a formal transition would lie below the first nonempty ideal scale. No second free Möbius e cancellation is used.

### All physical branches and tails

The previously audited cubic identities give outside weight N^{-3/2}, lengths \(C_*=U/(N^3B)\), \(Y_*=Y'/(Bq_j^2)\), and hence
\[
 N^{-3/2}(C_*q_f/(Y_*P_c))^{b-1}
 =N^{3/2-3b}(U/(Y'P_c))^{b-1}(q_j^2q_f)^{b-1}.
\]
All variable divisors n_0,E_4,g are pooled as bounded row coefficients after the exact common-weight separation. The N exponent is nonpositive. The actual slot priority assignment preserves common column coefficients; replacing \(P_c\) by P is a safe upper bound and does not omit the marked-column cost.

The Fourier envelope depends on \(X'M^2q_{a'}^6/U\), so frequency summation gives \((U/X')^{J/2}\) and the convergent ideal weight \(q_{a'}^{-3J}\). Throughout the interval J>0.97. Combining the physical square coefficient with the scale dependence gives
\[
 q_r^{4-6b-3J(b)}\le q_r^{-23/10}.
\]
This is uniformly absolutely summable, and the same calculation applies to the first flat coefficient and sixth-power scale change. Arbitrary decay of the full Fourier envelope and Gaussian annuli handles every small scale. All unbounded labels must first enter the ambient modulus/height size; their arbitrarily small powers are then absorbed by these strict summability margins and the original tails, as the revised manuscript explicitly requires.

### Exact exponent maximization

The three J-polynomials in the manuscript were checked directly. The compensated exponent is
\[
 E(b)=-29/96+13J(b)/32+25(b-1)/48.
\]
On the first interval its derivative is 203/240. On the second it decreases from 47/240 to 1/30 and remains positive. On the third it is negative throughout, beginning at -319/960. Therefore the unique endpoint maximum is b=5/6, where D=2/3, J=16/15, and E=2/45. The residual subset term d(b-1) is nonpositive. The complete finite-e maximum here occurs at \(S=M^{3/5}\), not at the convenient clean scale S=M.

The stated improvement and remaining gap follow exactly. All Q, fixed-twist, nonprincipal-type, and full-tail qualifications must accompany the result.

# Review of Part XIII: complete mixed residues 3/5

## Independent referee: the complete mixed residues 3/5 sector

### Verdict and scope

The argument in Part XIII of the companion report passes with the explicit compact-support and ambient-size conventions stated below. It treats exactly
\[
 H=\varepsilon v^3w^5a^6,\qquad vw\text{ squarefree},\quad(v,w)=1,
 \quad v,w\ne1,
\]
with every physical n, all original slots, original or core marking, and either exact first Möbius-flat operation. Its normalized compensated bound is \(O_\epsilon(Z^{-1/32+\epsilon})\). It uses no Q input or zero-density assertion for a moving twist. The gap to \(-3/16\) remains \(5/32\), and other mixed residue types are outside its scope.

### Actual characters and the entire free-column scale

For fixed w, the v-family is genuinely quadratic, with the fixed w-symbol included in its common column coefficients. Thus the quadratic large sieve has no extra conductor-W cost in the direct column norm. The actual smooth character, however, has primitive conductor comparable to VW: disjoint good supports carry nontrivial orders 2 and 6. Its pointwise Poisson bound must use this full conductor. The draft does so.

Square decomposition of the smooth column preserves the w-symbol as a bounded common coefficient and removes only the v-dependent square mask inside a positive norm. Combining that direct estimate with actual primitive Poisson gives precisely the four ranges
\[
 \sqrt{VS},\quad S,\quad V\sqrt W,\quad
 S W^{-1/2}(S/(VW))^{-A}
\]
at the transitions V, \(V\sqrt W\), and VW. Root numbers and conductor-generator angular factors have modulus one as row factors; their separated smooth weights have uniform seminorms. This is not a Poisson assertion for arbitrary rough coefficients.

Writing L=RS, the first term of the c-column norm has maximum \(V\sqrt W\); the term \(\sqrt{V/L}\) has maximum \(VW^{1/4}/\sqrt R\), attained at \(S=V\sqrt W\). The long tail is smaller. The actual reciprocal e-sum therefore gives (10), including cases when transitions lie outside its nonempty support.

### Source local coefficients and square layers

I checked the source coefficientwise unit factor and the local C/P table. Odd physical valuation is possible only in dual residues 2,3,4; here it forces \(n_0\mid v\), with the two residue-3 branches already audited in the complete quadratic proof. They give the exact outside amplitude \((q_{n_0}q_E)^{-1}\). Their additional w-symbols are genuine unit row factors for fixed w; they are not fixed-ray constants and are not evaluated at a forced nonunit.

At p dividing n_0, increasing the physical valuation by 2b and lowering the frequency exponent by 6b gives the nonprincipal Gauss ratio \(P^{6b}\) without an extra boundary. At the other r-primes, the ordinary multiplier is exactly
\[
 1_{p^2\nmid s}\bigl(1-P^{-1}1_{p\nmid c,p\nmid s}\bigr).
\]
The only lower boundary has frequency exponent 6b-1, belongs to residue 5, and forces p not to divide cs. Hence \(h_0\mid w\), \(a=(r/h_0)a'\), and \((h_0,a'cs)=1\). The coefficient is \(\kappa(r)q_r^{-2}\mu(h_0)q_{h_0}^{-1}\).

The phase comparison is valid also at an odd base valuation: the change of the rho exponent is a multiple of six, and the omega change cancels the \(\gamma_3^{-2b}\) factor. The remaining factor is \(\kappa(p)^b\). Restoring h_0 from the effective frequency contributes the inverse pair of c/s symbols and recovers the full fixed w twist. The correct shared divisor is formed from the effective frequency after removing the forced E factor, not from the unreduced original H.

Expanding the ordinary multiplier creates only fixed c-unit masks and s-divisor extractions after the finite valuation splits. Such an extraction reduces the free smooth scale and introduces a bounded row character; it does not create a larger outside normalization. The number of splits is divisor-bounded. All selected-slot assignments and zero extensions are preserved before applying norm inequalities.

### Odd-branch scales and the decisive h_0 count

At \(q_cq_{n_0}^3q_r^6\asymp C_l\), the physical scales are
\[
 C_*=C_l/(q_r^6N^3B),\qquad Y_*=Y'B/N.
\]
Multiplying the two-column bound by \((NB)^{-1}\) gives
\[
 \frac{V\sqrt W}{NB}+VW^{1/4}q_r^3\sqrt{Y'/C_l}.
\]
Thus the N,B cost cancels in the second branch and is favorable in the first. The divisor choices n_0,E,g remain row coefficients with common free columns.

The complete Fourier envelope has argument
\(X'V^3W^5(q_r/q_{h_0})^6q_{a'}^6/C_l\).
Its V-sum gives \(K_l^{1/3}W^{-5/3}(q_{h_0}/q_r)^2q_{a'}^{-2}\). Crucially, there are only \(O(W/q_{h_0})\) admissible w in a W-interval because h_0 divides w; the interval is empty below the corresponding ideal scale. Combining this count with the exact boundary coefficient cancels the apparent positive h_0 power. The resulting two terms are
\[
 K_l^{1/3}q_{a'}^{-2}q_r^{-4}W^{-1/6},\qquad
 K_l^{1/3}\sqrt{Y'/C_l}\,q_{a'}^{-2}q_r^{-1}W^{-5/12}.
\]
The W-dyads converge, as does the a'-ideal sum. The first r-sum converges absolutely. The second is summed only to the actual nonempty Gaussian bound \(q_r\ll C_l^{1/6}\), so it costs logarithms. This finite cutoff is indispensable.

For \(K_l<1\), the actual frequency numerator is at least one, giving any additional fixed positive K_l power from the full Schwartz envelope. Gaussian annuli outside the small-scale range are absorbed by their Gaussian tails. These estimates yield the uniform two-case formula (22) for every positive T at most Z.

### Exact flattening, normalization, and needed conventions

The first flat coefficient has norm \(q_b^{-2}\) and scale \(T=Z/q_b^6\), preserving the residue type through the exact sixth-power full-modulus lift. The large-scale b-weights are \(b^{-4}\) and the finitely truncated \(b^{-1}\); the complementary small-scale tail has powers \(b^{-2-6M}\) and \(b^{1-6M}\). All are controlled as stated. This applies independently to the two marker choices.

At the original scales, \(K=Z^{13/16}\). Multiplication by \(Q/Y'^{3/2}\), then by the original \(Q^{-1/2}\) normalization and finite compensation, gives respectively \(37/96-d/2\) and \(-1/32\).

Joint logarithmic Fourier separation must retain fixed product cutoffs, so every separated mode remains compactly supported; this is the explicit convention emphasized in the user's `bbb8bba6` joint-Möbius note. The e-sum here remains absolute, with no extra free Möbius cancellation. Before infinite sums, ambient small powers include the actual V,W,r,a',Gaussian-scale and height labels. They are absorbed only afterward by the strict W exponents, the a' sum, the actual r cutoff, and the complete Schwartz/Gaussian tails. These qualifications preserve the uniformity asserted by the theorem.

The final compact-cutoff and ambient paragraphs were read back in the author manuscript with SHA-256 `a53ecdb4655155dfbdde417bc42280352160dacf9296ab27164958887b2a8d2e`. They implement the stated conventions, explicitly retain the actual eta(e)/q_e coefficient, and preserve the user's cutoff attribution. The final text therefore passes without a pending mathematical qualification beyond its stated inputs and scope.

# Review of Part XIV: Q-conditional complete pure-fifth closure

## Independent referee: the complete pure-fifth type below the low threshold

### Verdict and exact scope

The combined arguments in Parts XIV A and XIV B of the companion report pass, conditional on the explicitly attributed Q input. They prove
\[
 I_{\rm fifth}(Z)\ll_\epsilon Z^{-63/320+\epsilon}
\]
for the complete nonprincipal type \(H=\varepsilon w^5a^6\), w good squarefree and nonunit. All physical n, original or core marking, and each exact first Möbius-flat operation are included. The margin below \(-3/16\) is \(3/320\).

This is a statement for this complete pure type. It does not cover mixed frequencies or combine all types into a full low estimate. Q remains the user's external fixed finite-order Hecke zero-free input, with its recorded attribution; this review does not claim an independent rerun of the formal build.

### 1. Actual density and true-column inputs

The D(a) formulas are the n=6 specialization of [de Faveri's Corollary 1.5 and its proof](https://arxiv.org/html/2610.04045v1), restricted by positivity to squarefree rows. The fixed finite-order eta enters common coefficients. The AFE has length O(sqrt(W)) times a fixed height power, and each term of the sixth sieve at that length is O(W) up to small powers. Thus the source detector proof has the same W-exponents with the fixed twist. This is also the V=1 case of the separately audited explicit moving-conductor interface.

The finite-height reciprocal lemma is applied only on strictly buffered zero-free rectangles, with all common deleted Euler factors retained in the actual imprimitive modulus. The final Q bin is traversed strictly to the right of any zero at 7/8. The fixed bin widths and all analytic losses are chosen sufficiently small for the final margin.

The selected c-column is the actual Möbius column. Extracting D_c contributes exactly its sign, character value, reciprocal norm, and changed scale L/q_D. Summing the genuine fixed slots gives the safe scalar \((L/P_c)^{-a}\). No selected-slot high-moment saving is needed. The remaining e coefficient is still summed in absolute value after the single exact Möbius cancellation that produced the free c-column.

### 2. The full free-s scale and exact physical columns

The true free-s character has conductor comparable to W and is nonprincipal. Its pointwise smooth bound is \(\min(S,\sqrt W)\), with rapid long-S decay. Therefore the maximum of \(S^{-a}\min(S,\sqrt W)\) is exactly \(W^{(1-a)/2}\), at S=sqrt(W). This checks the whole scale range, not only a convenient physical dyad.

For the actual lengths \(L=C_l/(R^6Gq_e)\), \(S=Y_*/(Gq_eq_f)\), the ratio L/S is independent of e. Each nonempty reciprocal e-dyad has bounded ideal mass. With at most \(W^{D(a)}\) exceptional rows, the full e-sum is bounded by
\[
 W^{F(a)}(Y'P/C_l)^a R^{6a},\qquad F(a)=D(a)+(1-a)/2.
\]
The exact ordinary-r masks are expanded before this estimate. They create common column masks or decrease Y_*, never an unaccounted larger normalization. Joint log-Fourier separation retains fixed product cutoffs in each mode. The original selected slots are assigned to r,g,e,c_2, or g,e,c_2 for the core marker, so the surviving c_2 conditions genuinely form the true marked Möbius column.

### 3. The exceptional square boundary supplies the needed support

The audited local table forces every physical n to be r squared. At an exceptional prime p^b exactly the exponent 6b-1 survives, and its contribution has p absent from cs. With h the product of those exceptional primes,
\[
 h\mid\operatorname{rad}r,\quad h\mid w,\quad
 a=(r/h)a',\quad(h,a'cs)=1,
\]
and the coefficient is \(\kappa(r)R^{-2}\mu(h)H^{-1}\). The restored unit phases give the original full w-character. Ordinary and exceptional primes are exclusive; in particular a boundary prime with b>1 must still be excluded from the ordinary product even though it divides r/h.

The actual Fourier numerator satisfies
\[
 W^5(R/H)^6q_{a'}^6\gg R^5q_{a'}^6,
\]
because H is at most both a constant times W and R. This is the decisive support condition. It does not divide the exceptional zero-density count by H.

Splitting the original Schwartz exponent retains simultaneously the W-frequency decay and an independent factor \((1+R^5/K_l)^{-B}\). Weighted dyadic W summation then gives
\[
 K_l^{F/5}(H/R)^{6F/5}q_{a'}^{-6F/5}
 (1+R^5/K_l)^{-B}.
\]
After the exact coefficient and R^{6a} are restored, the h exponent is \(6F/5-1>0\). Bounding H by R, and counting its divisors with an arbitrary small power, leaves precisely
\[
 K_l^{F/5}\sum_r R^{-3+6a+\epsilon}(1+R^5/K_l)^{-B}.
\]
This is a true Schwartz-controlled sum with effective norm scale \(K_l^{1/5}\), not an unjustified hard cutoff at the earlier physical scale.

### 4. Uniform summation and rational checks

The inequality F>5/6 holds uniformly on the closed bin interval. On the first piece, the numerator in the manuscript has cubic Bernstein coefficients
\[
 199/64,\quad161/16,\quad83/8,\quad6,
\]
all positive; its denominator has the stated negative sign. On the second piece the displayed elementary factorization has the claimed sign. Thus \(6F/5>1\) gives a strict ideal-summability margin for a'.

Ideal counting bounds the r-sum by \(K_l^{(6a-2)_+/5}\) for K_l>=1, with a logarithm at a=1/3. For K_l<1, an arbitrarily strong Schwartz exponent gives the same upper bound. This controls every Gaussian annulus and all positive T at most Z. Ambient small powers first include the actual unbounded labels; strict a'-summability and the full Fourier/Gaussian tails absorb them only afterward.

For the compensated exponent
\[
 G(a)=-29/96+13[F(a)+(6a-2)_+]/80-25a/48,
\]
the derivative numerator on [1/8,1/3] has the independently recomputed Bernstein coefficients
\[
 240361/64,\quad220293/32,\quad54167/8,\quad15921/4,\quad1899.
\]
They are all positive, so G is strictly decreasing there. Its initial value is \(-16641/75520<-63/320\). On [1/3,1/2], the exact identity
\[
 G(a)+63/320=(2a-1)(1074a-101)/(960(6a-1))
\]
is nonpositive. The global maximum is \(-63/320\), attained at the limiting initial-bin endpoint a=1/2. The residual subset contribution is \(-\alpha a\le0\). Thus the worst bin is not the top 7/8 bin.

### 5. Both exact first flat operations

The uniform physical scale exponent is
\[
 \beta(a)=[F(a)+(6a-2)_+]/5-a\ge-1/10.
\]
I independently checked both factorizations used to prove this inequality; equality occurs at a=1/3. Hence substituting the true scale T=Z/q_delta^6 with its coefficient q_delta^-2 produces an absolute ideal weight at most \(q_\delta^{-7/5+\epsilon}\). This converges with a strict margin uniformly over the bins. The full-modulus sixth-power lift preserves the pure-fifth core and unit. The argument therefore transfers to both actual first-flat operators while keeping X',Y' and all slots fixed.

No unproved negative large-T estimate was summed outside its range: the physical estimate was first established uniformly for every positive T, with the full small-scale tail retained. These checks complete the stated conditional theorem for the complete pure-fifth type.

# Review of Part XV: genuine cubic rational-slot moments

## Independent referee: genuine cubic rational-slot moments

### Verdict

Part XV of the companion report passes as an analytic lemma, without input Q. For the stated cube-free cubic rows and common selected-prime coefficients, its exact rational multiplier satisfies
\[
 \sum_{w\asymp M}|E_w(s)|^{2k}
 \ll(MP)^\epsilon\left(1+M/P^k+M^{2/3}/P^{k/3}\right)
\]
for every fixed positive integer k, uniformly for \(1/2\le\Re s\le1\). The positive row sum may be restricted arbitrarily. This certificate supplies no full physical or all-density-bin low estimate.

### Exact masks and sparse columns

The three-cycle Euler identity is valid both for cubic roots of unity and for the zero-extended value x=0. Its denominator is row-independent and bounded away from zero throughout the stated closed real-part interval. The branch x^3 is a unit mask, not a row-independent constant. The elementary normalized pointwise bound \(\sup|E|\ll1\) also holds.

After raising to the k-th power, freeze residue-zero prime blocks and retain their masks in the positive row norm. The remaining column is truly cube-free: residue-two primes have norm P_i squared, while only O(P_i) such primes are available. The draft correctly uses both this norm and this sparse coefficient mass before applying the genuine cube-free cubic large sieve. Correlations in the original common z_D coefficients remain in the resulting common column coefficient. Representation multiplicities and equality patterns are bounded because k and the number of slots are fixed.

For each repeated-prime block with occurrence count m, total branch exponent n, and residue r modulo three, the worst exponent occurs at real part 1/2. With h_0=1 and h_1=h_2=1/2, direct verification gives
\[
 h_r-(m+n)/2\le-m/2,
\]
\[
 h_r+r/2-(m+n)/2\le0,
\]
\[
 h_r+r/3-(m+n)/2\le-m/6.
\]
Here m<=n, and residue zero forces n>=3. These inequalities pay separately for the square-root M term, the square-root column-length term, and the mixed cubic-sieve term. They yield the stated row norm of E^k; squaring proves the proposition. No prime-square branch was treated as a squarefree column at the smaller norm P_i.

The source is [de Faveri, Theorem 1.1](https://arxiv.org/html/2610.04045v1), whose definition permits cube-free ideals on both sides at n=3. The primary/ray identification is the previously audited cubic family. Common fixed twists and whole-kernel conjugation preserve the positive operator bound.

### Exceptional rows and the stated endpoint corollary

Hölder with a second 2l-th moment is legitimate when \(1/(2k)+1/(2l)\le1\). It uses the upper row count consistently and requires no independence between the selected slots and the exceptional set.

At a=1/6, D=2/3, p=log P/log M, the three exponents are exactly
\[
 p/6-1/(3k),\qquad1/(6k)-p/3,\qquad0.
\]
Thus the factor has no positive power for \(1/(2k)\le p\le2/k\). These intervals cover every fixed positive p using a finite collection of fixed moment orders after epsilon is chosen. Tiny P uses the actual pointwise bound. For p>=2, k=1 yields the remaining term \(P^{1/6}M^{-1/3}\). This proves the stated endpoint envelope.

The endpoint statement does not cover every zero-density bin automatically; any complete physical application must separately maximize all free-column scales and all bins, and retain its own n, square, selected-slot, and flat tails.

# Review of Part XVI: negative complete-cubic mean

## Independent referee: negative complete-cubic mean with exact slots

### Verdict and scope

The proof in Part XVI of the companion report passes with the explicit short-dual-length convention in Section 1 below. Conditional on the user's attributed Q input, it gives
\[
 I_{\rm cub}(Z)\ll_\epsilon Z^{-11/2304+\epsilon}
\]
for the complete nonprincipal cubic type, including all physical n, the original and core markers, and either exact first Möbius-flat operation. It remains \(421/2304\) above the required \(-3/16\). A negative exponent for this type does not establish the full low comparison or RH.

### 1. True primitive conductor and smooth eighth moments

The row index w is cube-free. Its primitive conductor is comparable to rad(w), not necessarily to w. The proof correctly first partitions the actual conductor norm into blocks C<=C_0M. The direct k-th-power convolution has common divisor-bounded coefficients; cube removal uses the genuine cube-free cubic sieve and its convergent layer weights. This gives the stated three direct moment terms.

Primitive Poisson has amplitude S/sqrt(C), a unit row root number, and dual length C/S. For C/S>=1, common conductor-ratio separation and the actual dual smooth polynomial give
\[
 M^{1/(2k)}\sqrt S+\sqrt C+M^{1/(3k)}C^{1/3}S^{1/6}.
\]
For C/S<1, one must instead retain the actual rapid Poisson tail. It bounds each row by O(sqrt(C)) after taking a sufficient tail order, hence its 2k-norm by \(M^{1/(2k)}\sqrt C\le M^{1/(2k)}\sqrt S\). This is already covered by the first displayed term. Thus no large-sieve estimate at a false positive length below one is needed.

Every displayed C power is nonnegative, so replacing C by C_0M afterward is safe. The positive restriction to the conductor block is retained until enlargement. Angular Fourier modes of nonradial common weights contribute only unit row factors from the conductor direction; their smooth mode decay absorbs the polynomial seminorm costs. Fixed product cutoffs remain outside each joint log-Fourier mode.

At k=4, taking the minimum of the complete direct and dual bounds yields exactly the four pieces with transitions \(M^{1/8},M^{1/2},M^{7/8}\). The original pointwise bound and genuine long-column tail are also valid with the upper conductor scale M.

### 2. Exact rational slots for every bin

The selected multiplier is the actual one from the Möbius Dirichlet series, including its cubic unit masks, prime-square branches, and all Euler denominators. The separately reviewed rational-slot moment is applicable after the original eta slot factors are incorporated into common coefficients. No arbitrary column coefficient is submitted to an inverse-L estimate.

With p=log(P_c)/log(M), a=1-b, the three Hölder exponents are
\[
 ap-D/(2k),\quad(1-D)/(2k)+(a-1/2)p,
 \quad(2/3-D)/(2k)+(a-1/6)p.
\]
For p<=1/2 the manuscript's choices work on every density interval:

- D=1: k=1 makes all three nonpositive.
- D=7/3-2b: choosing kp in [1/2,1] makes all three nonpositive.
- D=19/6-3b: choosing kp in [3/2,2] makes all three nonpositive.

The integer ceilings proposed in the proof hit those intervals. Tiny p uses the actual pointwise multiplier bound; after epsilon is fixed, only finitely many fixed moment orders are required. Hölder is valid with the eighth moment, and the same slot factor also applies to the pointwise smooth-column bound. This proves lossless slot control only in the stated range P_c<=C sqrt(M), not globally.

### 3. The complete free-s maximum

The restricted eighth-moment and pointwise bounds give the two candidate exponents
\[
 J_8(b)=\max\{7D/8+b/2,
 D(3+b)/4+(3b-1)/4\}.
\]
Below S=sqrt(M), all weighted power pieces are nondecreasing. In the next range the possible crossing with the pointwise bound would be at exponent \(1/2+3D/4\), which is beyond 7/8 because D>=13/24. The last interval contains the actual crossing \(S=M^{(3+D)/4}\); the remaining long tail decreases. Thus both peaks, and all intermediate and truncated scales, are covered. At b=5/6 the second peak wins, giving J_8=73/72 and S=M^{11/12}.

The actual finite reciprocal e-sum is controlled by this full maximum. Its length ratio is independent of e. After restoring N^{-3/2}, the odd-branch weight is \(N^{3/2-3b}\le1\). The n_0,E_4,g sums remain divisor-bounded row factors with true common free columns. Every common mask, especially h, remains in the actual deleted modulus.

### 4. High M and exact physical tails

When M>=Z^{1/3}, the original P_c<=C Z^{1/6} guarantees the needed slot range. The complete Fourier envelope then gives \((U_l/X')^{J_8/2}\), with a convergent a'-ideal weight \(q_{a'}^{-3J_8}\). The r weight is \(q_r^{4-6b-3J_8}\), uniformly below -1. The same scale exponent applies to the external first-flat divisor, so this part covers both flat operators. Enlarging the final positive frequency bound to all M occurs only after deriving it for the permitted high-M range; it does not invoke a slot estimate outside its domain.

The compensated exponent is
\[
 E_8(b)=-29/96+13J_8(b)/32+11(b-1)/16.
\]
It increases through the first two density intervals and decreases on the last one. At the right start of the last interval its derivative is -83/768. Its global maximum is therefore at b=5/6 and equals -11/2304. The residual subset parameter does not worsen this bound.

### 5. Low M: the multiplicities cannot be dropped

For M<=Z^{1/3}, the proof correctly returns to the previously reviewed absolute-slot mean. With q_r about R and q_{a'} about A, the actual dyadic counts and square coefficient produce
\[
 A R^{5-6b}(1+M^2A^6R^6/(e^lZ^{13/16}))^{-N}.
\]
The exponent 5-6b includes the number of r-ideals. Its omission would invalidate the small-M estimate. If an external flat divisor is present, it has the same exponent as R and enters the same product constraint; allocating product size between the equal exponents adds logarithms, not a new power.

Set C(b)=max(1,5-6b). Dyadic summation in A,R and the optional external divisor gives \((e^lZ^{13/16}/M^2)^{C(b)/6}\), with full rapid decay retained when this ratio is below one. Since \(J_0(b)-C(b)/3>0\), the M-sum is maximized at its actual upper endpoint Z^{1/3}. The resulting exponent is precisely
\[
 E_{\rm small}(b)=-29/96+J_0(b)/3+25(b-1)/48+7C(b)/288.
\]
Its three interval derivatives have the stated signs, including the transition where C becomes one. The maximum is at b=5/6 and equals -13/1440, strictly smaller than -11/2304. The subset correction d(b-1) is nonpositive.

All initially small losses must include the actual unbounded physical and Mellin labels before summation. The strict high-range margins, the low-range genuine product cutoff, and the original Schwartz/Gaussian tails absorb them. This completes the all-bin, all-physical, two-marker, two-flat estimate with the stated Q condition and remaining gap.

The explicit C/S<1 Poisson-tail paragraph was read back in the final author text with SHA-256 `d137da20dcf13ef19064d245c51059e9949d5d980105bb19216371056678a8c6`. It implements the required convention. The theorem therefore passes with no pending mathematical amendment beyond retaining its stated assumptions and scope.

# Review of Part XVII: Q-conditional complete mixed(3,5) bound

## A. Forward moving-conductor input

### Independent referee: quadratic detection with the actual moving sextic conductor

#### Verdict

Part XVII A of the companion report passes as an explicit-conductor analytic interface. It does not prove a complete physical mixed-sector bound. The variables v,w retain disjoint good squarefree nonunit supports; w is frozen while v is averaged. No constant depending arbitrarily on w is treated as fixed.

#### Density and true smooth moments

The actual primitive conductor is comparable to VW. The AFE for the square of the L-function has norm length O(VW) times a height power. The fixed w-symbol enters common coefficients, but does not shorten that length. Quadratic large sieve, square-layer decomposition, and common AFE differentiation therefore give the stated fourth-moment bound VW times small powers and a height polynomial.

The inverse detector has common coefficients with second moment V+X. Its first term is
\[
 Y^{a-1/2}R^{1/4}(VW)^{1/4}(V+X)^{1/2},
\]
and its squared-polynomial tail is \(VX^{2a-1}+Y^{2a}\). Taking X=V and \(Y=(V^3W)^{1/(2+2a)}\) is admissible for \(0<a\le1/2\). Balancing the first term after absorbing R^{1/4} gives
\[
 R\ll\min\{V,(V^3W)^{a/(1+a)}\}
\]
with the claimed height and small-power factors. The remaining \(V^{2a}\) tail is no larger. Q and the finite-height reciprocal argument apply to the actual finite-order product character, with all deleted factors in the ambient size.

For each fixed smooth 2l-th moment, direct quadratic expansion gives \(V^{1/(2l)}\sqrt S+S\). Primitive Poisson uses amplitude \(S/\sqrt{VW}\) and length VW/S. Applying the direct moment to that genuine conjugate dual column gives \(V^{1/(2l)}\sqrt S+\sqrt{VW}\). The minimum is the stated two-sided bound. Root numbers and angular/conductor-ratio factors remain bounded row factors after common smooth separation. These steps require genuine smooth columns and preserved compact cutoffs.

#### All free-column scales and slots

For \(R_0=\min(V,(V^3W)^{a/(1+a)})\), the left possible eighth-moment peak is at \(S=\sqrt{VW}\), giving
\[
 R_0^{7/8}(VW)^{(1-a)/2}.
\]
The right possible peak lies at \(S=R_0^{1/4}V^{3/4}W\). Its ratio to the left is \(R_0^{1/8-a/4}V^{-a/4}W^{-a/2}\). Substituting the uncapped upper bound for R_0 is legitimate because \(1/8-a/4\ge0\). The resulting V-exponent is \(a(1-8a)/(8(1+a))\le0\), and the W-exponent is negative. The short pieces and actual long-Poisson tail are also covered. Thus the full-scale maximum is correctly bounded, not merely one transition point.

The selected multiplier's local coefficient can include the fixed w-symbol and its zero. Its common-coefficient moments remain valid uniformly in w. Since \(R_0\ge V^{3a/(1+a)}\), the already audited floor/ceil selection of fixed moment orders gives the safe factor \(1+P_c^aR_0^{-1/4}\). No independence from the exceptional family is assumed.


## B. Reverse moving-conductor input

### Independent referee: reverse sixth-family moving-twist inputs

#### Verdict and quantifiers

The revised Part XVII B of the companion report passes as an analytic interface, including its density, true direct/dual smooth moments, and exact selected-Euler moments. It does not assert a full physical low bound.

The revised scope explicitly requires w to be nonunit, W>=2, with v allowed to be the unit ideal and V>=1. Good supports are disjoint, and the fixed excluded set contains the fixed eta/ray conductors. Thus a w-prime supplies a nontrivial sextic component and every product character used in Poisson is nonprincipal. No principal zero mode is inadvertently discarded. The density statement additionally requires V<=W.

#### Explicit conductor payment in the zero detector

The actual primitive conductor is comparable to VW. The half-line approximate functional equation has length B at most \((VW)^{1/2}\) times a fixed height power. Sixth-power decomposition and the genuine sixth-order large sieve give the four terms
\[
 W+B+W^{5/6}B^{1/3}+W^{1/3}B^{5/6}.
\]
At the indicated B they are bounded by \(M=WV^{1/6}\) when V<=W. In particular the fourth term is \(W^{3/4}V^{5/12}\), whose ratio to M is \((V/W)^{1/4}\le1\). Smooth AFE differentiation preserves this conductor power and supplies only a height polynomial.

The inverse-polynomial and detector-tail coefficients retain the moving v-character as a common coefficient, including its zeros. Their operator estimates at (W,X) and (W,U) are bounded by the corresponding estimates at (M,X) and (M,U), by monotonicity of each positive term. Thus the exact detector expression displayed in the manuscript is bounded by the source expression with effective parameter M. The actual conductor VW is at most M squared here, so its small powers and fixed polynomial-growth tail controls also fit this replacement; it is not silently assumed to be at most M.

I checked the specialization of [de Faveri's Corollary 1.5 and its proof](https://arxiv.org/html/2610.04045v1). The displayed D_6 formulas are correct on the stated interval; in particular D_6(7/8)=55/118. The source optimization therefore gives the claimed \(\min(W,M^{D_6(b)})\) bound. Q is needed only when this analytic density input is combined with the capped true-Möbius contour, not for the density calculation itself. Such a use must retain Q's attribution and the prior source/formal-verification distinction.

#### True direct and dual high moments

Expanding the k-th power of an actual common smooth character column gives a common divisor-bounded polynomial of length O(S^k). Sixth-power removal has four summable layer powers: -3,-6,-4,-11/2. The resulting row norm before taking the k-th root has terms
\[
 \sqrt{WN},\quad N,\quad W^{5/12}N^{2/3},\quad W^{1/6}N^{11/12}.
\]
These yield exactly the stated four direct 2k-moment terms.

For the dual estimate primitive Poisson has amplitude S/sqrt(C), C=VW, and dual norm length C/S. Substituting that length into the complete direct estimate gives the four stated dual terms, including \(C^{1/6}S^{1/3}\) and \(C^{5/12}S^{1/12}\). The minimum must be taken between the complete sums, as the manuscript explicitly says, not independently term by term. Actual conductor-ratio, angular and root-number factors admit the inherited common smooth separation, preserving compact cutoffs and rapidly decreasing tails. Arbitrary row-dependent rough columns are outside this statement.

#### Rational sixth-cycle selected multipliers

The exact six-cycle identity is valid also at the zero extension. Its denominator is row-independent and uniformly separated from zero for real part at least 1/2. The fixed v-symbol, including zero, is a common coefficient; it does not enter an unspecified v-dependent constant.

For the raw selected polynomial, freeze repeated-prime blocks with multiplicity divisible by six. Their masks remain in the positive norm before enlargement. The residual column is truly sixth-power-free with its actual norm and sparse coefficient count. For a nonzero residue t of a multiplicity-m prime block the four counting costs are
\[
 1/2,\quad(1+t)/2,\quad1/2+t/6,\quad1/2+5t/12.
\]
They are respectively bounded by m/2,m,2m/3,11m/12. A zero-residue block has cost one and m>=6. This proves all four exponents in (10).

For the rational multiplier, Minkowski first separates the finitely many Euler branches. Within each branch the same j is attached to a given slot before its k-th power is expanded. The coefficient exponent satisfies \(\kappa_j\ge(j+1)/2\). With residual t=jm mod six, the four local inequalities in the manuscript follow from t<=jm and m>=1; zero-residue blocks satisfy them as well. Therefore every branch obeys the same four moment powers, and finite summation proves (8). No mixed-exponent term in the k-th power was discarded, and no repeated-prime zero mask was set to one.

The two genuine sixth-sieve cross terms remain necessary. Subsequent exceptional-row Hölder estimates and physical n, slot, square-boundary, and flat summations require a new complete calculation; this certificate does not supply that calculation.

The revised true Möbius column ranges only over original good c, takes the common mask's S-exterior part, and retains every actual deleted Euler factor in the ambient imprimitive modulus. These final scope corrections were read back before issuing this verdict.

## C. Finite two-direction budget

### Independent referee: finite clean mixed dyadic certificate

#### Verdict and restriction

Part XVII C of the companion report passes as the stated clean, all-selected-slot analytic budget. Choosing between its two true moving-conductor directions bounds the positive dyadic majorants by \(Z^{-5/32+\epsilon}\). This certificate does not include all physical n, exceptional h_0, square layers, Gaussian-scale changes, or either flat operation. Those require a separate exact transfer. It is not an actual lower bound or an attainment claim.

#### Forward range

The positive bounds are nondecreasing in V,W before imposing the frequency boundary, so replacing v by \((13/16-5w)/3\) is safe. The uncapped density is an allowed upper row count even where it exceeds the trivial count. For each admissible Hölder choice the total a-derivative is bounded by
\[
 (13/48)(85/54)-11/16+1/6<0.
\]
The derivative of the selected negative row-count factor only improves this. Thus a=1/8 controls all bins in this majorant.

At that endpoint, the unselected exponent is \(-439/2304+(23/72)w\). The exact quadratic selected moments give the three additional candidates in (5). In the intermediate slot range the k=1 and k=2 lines meet at p=v-r/2, giving value \(av-(a/2+1/4)r\); in the long-slot range k=1 gives p/8-r/2. These reproduce (5), with the short-slot floor/ceil bound already audited. Each resulting affine branch increases with w on the stated interval. At w=5/48 the penalty vanishes and the exponent is exactly \(-1087/6912<-5/32\).

#### Reverse monotonicities and genuine sixth-slot terms

For w>=5/48, v<=7/72<w, so the reverse detector's V<=W hypothesis holds. The D_6 derivative formulas and the bound \(D_6'\le9816/3481\) are correct. They make every complete Hölder candidate decrease with a after including the selected scalar, so a=1/8 is again sufficient.

On the frequency boundary, the frozen-v count has derivative -5/3. The row-count exponent has derivative less than one; every direct or dual smooth moment term has derivative at most 1/(2l), and each selected-moment term at most 1/(2k). With the nonnegative Hölder counting coefficient, the whole derivative is at most -2/3. The available s-interval also shrinks. The reduction to v=7/72,w=5/48 is therefore valid for these clean bounds.

At that endpoint r/w=286/531. The floor and ceiling selected-moment choices retain all four sixth-sieve terms. Their coverage criterion is exactly r/w>=10/21. Tiny p can use one sufficiently large fixed moment for the desired epsilon; the order need not grow with Z. For p>=w, k=1 and p<=2w give the stated nonpositive remaining cost. These multiplier moments are compatible with every smooth moment used afterward, since the relevant Hölder reciprocal exponents sum to at most one.

#### Full s-interval check

At the endpoint, the complete dual moment is a maximum of four affine s-exponents. Hence each closed interval can be checked at its two endpoints. Independently recomputing with exact rational arithmetic gives:
\[
 -3619/22656,\quad-16183/101952,\quad-96539/611712,
 \quad-159979/1019520
\]
for the four intervals and choices stated in the manuscript. Every value is at most \(-321/2048<-5/32\). The pointwise final interval and genuine long-Poisson tail cover the remaining scales. No termwise minimum of separate direct/dual expressions was substituted for a valid complete norm estimate.

The resulting -5/32 clean budget is established as an intermediate analytic inequality. The full physical transfer is proved and reviewed separately in subsection D; it uses a restored-character positive extension and does not divide a density count by h_0.

## D. Complete physical transfer

### Independent referee: complete mixed (3,5) density transfer

#### Verdict and exact scope

Part XVII D of the companion report passes conditional on the user's explicitly attributed Q input and the separately audited analytic and arithmetic inputs. For precisely
\[
 H=\varepsilon v^3w^5a^6,\quad vw\text{ good squarefree},\quad
 (v,w)=1,\quad v,w\ne1,
\]
the complete normalized finite compensation satisfies
\[
 I_{3,5}(Z)\ll_\epsilon Z^{-5/32+\epsilon}.
\]
All physical n, both original and core markings, and each exact first Möbius-flat operation are included. This improves the earlier Q-free -1/32 bound for the same complete type by 1/8. It remains 1/32 above the required -3/16 and does not combine the remaining types into the full low comparison or prove RH.

The finite clean certificate alone did not establish this result. The new complete physical transfer is verified below.

#### 1. Exact physical coefficients and common columns in both directions

The inherited local identities give n=n_0r^2, n_0|v, outside weight (NB)^{-1}, and the ratio
\[
 L/S=C_lq_f/(R^6Y_*N^2B^2),\qquad Y_*\le Y'.
\]
The inverse-column scalar therefore produces \((NB)^{-1+2\alpha}\le1\). The complete n_0,E,g choices remain divisor-bounded row factors after the common norm separation. Their w-dependent unit phases are retained.

The exceptional boundary has h_0|rad(r), h_0|w and outside coefficient \(R^{-2}H_0^{-1}\). Ordinary primes exclude h_0 even when a boundary prime occurs to a higher power in r. Restored phases give the actual full v,w character pair. On the true support h_0|w, the additional h_0-unit masks on c and s are redundant because that restored character already vanishes there. One can therefore define the common smooth character column without that redundant rough mask, and only afterward enlarge its positive row norm. This order is essential: it avoids asserting primitive smooth Poisson for an arbitrary retained h_0-unit cutoff.

The same common-column structure is valid in the reverse direction. With v frozen, n_0,E are fixed v-divisors and their remaining w-symbols are bounded row factors. The w-part of g is handled by the varying character's zero; its v-part by the fixed v-character's zero; its a'-part by the fixed mask. Ordinary r restrictions are first expanded into fixed divisor extractions. The selected c_2 coefficients remain common for the family being averaged. All actual deleted Euler primes are retained in their imprimitive modulus.

The exact e coefficient remains eta(e)/q_e, with no second free Möbius cancellation. Fixed product cutoffs remain outside each joint logarithmic Fourier mode, as required by the user's joint-Möbius interface.

#### 2. Small bins: genuine positive-majorant homogeneity

For 1/8<=alpha<=1/4, consider the complete clean positive dyadic majorants after removing the explicit column-ratio scalar. Under
\[
 (V,W,S)\mapsto(tV,tW,t^2S),\qquad0<t\le1,
\]
with actual slots held fixed, the frozen-twist count contributes t. Every monomial of either complete direct/dual smooth moment contributes at least one further t power. This includes both sixth-sieve cross terms. The pointwise alternative also contracts by at least t, and the true long-S ratio S/(VW) stays unchanged.

Density majorants and selected positive moments are nondecreasing in their family sizes. Their remaining Hölder counting powers are nonnegative. Thus they cannot increase under contraction. The scalar S^{-alpha} supplies t^{-2alpha}. Every permitted complete Hölder bound therefore contracts by at least \(t^{2-2\alpha}\). Taking the permitted minimum does not invalidate this common contraction. The ratio V/W is unchanged, so any reverse-family V<=W requirement remains valid when a pair is inflated to the clean reference range.

Frequency norm contracts by t^8. Consequently the counting function below an effective cutoff U<=K_0 contracts by
\[
 (U/K_0)^{\gamma(\alpha)},\qquad
 \gamma(\alpha)=(1-\alpha)/4\ge3/16.
\]
Shifting dyadic grids creates only bounded overlap and logarithmic losses. No actual ideal is rescaled; this is an inequality between the explicit analytic majorants.

#### 3. The complete Schwartz and Gaussian tails

For U>=K_0, the clean algebra can be applied at the enlarged analytic reference \(Z_U=Z(U/K_0)^{16/13}\). Its hypotheses allow the unchanged slots because P_c<=Z_U^{1/6}. This is not a coupled-scale physical theorem. Explicitly, one may take the clean counting upper bound proportional to
\[
 B_\alpha=Z^{7/48+11\alpha/16}
\]
up to small powers after restoring the known normalized prefactor and column-ratio factor. Replacing Z by Z_U gives a uniform finite polynomial in U/K_0. This verifies the claimed large-U counting bound.

Let \(x=(T/Z)(H_0/R)^6q_{a'}^{-6}\le1\) and \(E=e^l xK_0\). Combining the small-U contraction and large-U polynomial bound, a dyadic Schwartz summation or Stieltjes integration gives
\[
 \int(1+U/E)^{-A}\,dA_\alpha(U)
 \ll Z^\epsilon B_\alpha e^{C|l|}x^{\gamma(\alpha)}.
\]
A is chosen larger than the polynomial exponent and gamma. The statement remains valid when E is below the first ideal scale, or above K_0; the latter excess is paid by \(e^{C|l|}\). The original Gaussian absorbs that factor. This checks the actual full frequency tail rather than only a hard truncated range.

The remaining small-bin weights are exactly
\[
 R^{6\alpha-2-6\gamma}H_0^{6\gamma-1}q_{a'}^{-6\gamma}.
\]
Since H_0<=R and 6gamma>=9/8, they are bounded by \(R^{6\alpha-3}q_{a'}^{-6\gamma}\). Thus the r-ideal exponent is at most -3/2 and the a'-ideal exponent at most -9/8. Both have strict summability margins. Divisor choices are absorbed by initially smaller epsilon powers.

An external first flat coefficient adds the ideal exponent
\[
 -2+6\alpha-6\gamma=-7/2+15\alpha/2\le-13/8.
\]
This is also absolutely summable. The exact sixth-power frequency lift preserves the mixed type while X',Y' and all slots stay fixed.

#### 4. Large bins: retain the actual frozen-twist divisibility count

For 1/4<=alpha<=1/2, the forward explicit-conductor density is bounded by \(V^D W^{D/3}\), where \(D=3\alpha/(1+\alpha)\). Combining it with the genuine pointwise smooth bound and the safe absolute selected-slot price gives
\[
 \kappa=D+(1-\alpha)/2,\qquad
 \lambda=D/3+(1-\alpha)/2.
\]
Here the number of frozen twists w satisfying h_0|w is truly O(W/H_0). This is ordinary ideal counting of the frozen variable, not division of a density row count by H_0.

After the weighted V-sum, the W exponent is
\[
 m=1+\lambda-5\kappa/3
   =(\alpha^2-9\alpha+2)/(3(1+\alpha))\le-1/20.
\]
The W-dyads start at H_0, so their sum supplies H_0^m. The residual boundary power is
\[
 2\kappa-2+m=(2D-1-2\alpha)/3\le0.
\]
The physical r and external flat exponents are both
\[
 6\alpha-2-2\kappa=7\alpha-3-2D\le-3/2.
\]
Moreover 2kappa>=39/20>1, so the a' sum converges. All relevant limits and infinite tails retain strict margins.

The complete all-scale large-bin expression is \((Y'/T)^\alpha(TP/X')^{\kappa/3}\). At T=Z its compensated exponent decreases with alpha and has maximum
\[
 -29/96+13\kappa(1/4)/48-25/(4\cdot48)
 =-323/1920<-5/32.
\]
The remaining subset term is nonpositive. Thus this part is smaller than the small-bin bound.

#### 5. Uniformity and conclusion

The ambient size contains the actual unbounded v,w,r,a',e,h_0,external-flat, Gaussian and Mellin labels before any infinite sum. Their arbitrarily small powers are absorbed only afterward by the strict exponents and the full original rapid decay. All bin contours are buffered and all Q provenance remains explicit; this review does not claim a new formal build.

These checks establish the complete two-marker, all-n, two-first-flat estimate. The earlier clean transfer warning is resolved by the present positive-extension and homogeneity proof, rather than by falsely replacing the reverse density count with that count divided by H_0.

#### 6. Final text readback

The final author text was read back with the explicit reverse common-column allocation: the w part of g is covered by chi_w zero extension, the v part by fixed chi_v zero extension, and the a' part by the original fixed mask; n_0,E are fixed v-divisors in the reverse family and their w-symbols are bounded row factors. The same text includes the explicit clean envelope B_alpha=Z^{7/48+11alpha/16} and its polynomial extension above K_0. These additions agree with the proof audited above.

Audited author SHA-256: 5273afbb8268424df9f9d46b94bea81c65a05284ad50b6f8c7412a16170bd867.

# Review of Part XVIII: joint exceptional rows and the complete mixed(3,5) bound

## A. Joint analytic theorem

### Independent referee: joint quadratic–sextic detector and moments

#### Verdict and scope

The analytic assertions in Part XVIII A of the companion report pass, with the selected multiplier's real part in a fixed compact interval starting at 1/2, and constants allowed to depend on the original fixed arithmetic data and that interval. In particular, the genuine joint family with V=W=N has exceptional-row count at b=7/8 bounded by N^(7/5+epsilon) times a polynomial in the height. No Q hypothesis is required for this zero-density result. Q enters only in a later inverse-column application. No complete physical mixed bound follows from the detector alone.

The family is the original product eta psi_v chi_w (or its sixth-factor conjugate), with v,w good, squarefree, nonunit and coprime. Its conductor has norm comparable to VW because the moving local components have different disjoint supports and are ramified there. The fixed bad conductor is partitioned into finitely many possibilities. The proof never absorbs a moving prime into fixed S.

#### 1. Common-coefficient joint sieve

Freezing w gives W(V+B); freezing v gives V Theta_6(W,B). The former uses Goldmakher–Louvel's squarefree quadratic large sieve; the latter uses the sixth-power-free large sieve, in which the actual squarefree rows and columns form permitted subfamilies. The two positive norms may each be enlarged after forming them. Taking their minimum is valid:

K(B)=min{W(V+B), V[W+B+W^(5/6)B^(1/3)+W^(1/3)B^(5/6)]}.

For bounded common full-column coefficients, n=c ell^2 with c squarefree is a valid reduction even though chi_w is sixth order: chi_w(ell^2) is retained as a modulus-at-most-one joint-row factor, not set equal to one. The psi_v square is the appropriate row unit mask. Minkowski gives sqrt(B K(B)) times the ideal harmonic sum in ell, which is logarithmic. This proves only the claimed bounded-coefficient consequence, not an arbitrary all-column operator bound.

#### 2. The actual L moments and detector

The AFE lengths for L and L^2 are respectively sqrt(VW) and VW up to polynomial height. In each square layer their coefficients have an ell^(-1) factor and squarefree harmonic mass. The layer sum is logarithmic and gives J_2=K(sqrt(VW)) and J_4=K(VW). Primitive dual root numbers are pure joint-row factors. The normalized conductor ratio lies in a compact interval, so one common Mellin separation retains common inner coefficients; angular modes are similarly pure row phases. Differentiating the AFE and applying Sobolev to L or L^2 yields the asserted finite-height suprema without assuming an independent fourth moment of L'. Fixed deleted Euler factors are harmless finite arithmetic factors on these lines; the primitive zero set in Re s>1/2 is the same for the corresponding incomplete function.

The truncated inverse is the actual squarefree Mobius polynomial, so its second moment is K(X). Its product with the original incomplete L-function has common divisor-bounded tail coefficients. The Gamma detector therefore has the two alternatives

Y^(1/2-b) (J_2 K(X))^(1/2),

Y^((2-4b)/3) J_4^(1/3) K(X)^(2/3),

and the same nonnegative tail sup_{X<=U<=Y} U^(1-2b) K(U). In the fourth-moment alternative the intermediate R^(1/4) is retained and only then eliminated from R<=A R^(1/4)+tail. It is not replaced by the full row count. Actual varying zero ordinates and real parts are handled by the height supremum and partial summation. The full Gamma tail is controlled by exponential decay against the established polynomial height losses.

For V=W=N, K(B)<=C(N^2+NB). Taking X=N, Y=N^(2/(3-2b)) in the second-moment alternative gives the exponent (7-6b)/(3-2b)=1+4(1-b)/(3-2b). The remaining term has exponent 3-2b, smaller by 2(2b-1)(1-b)/(3-2b). Thus the stated 7/5 at b=7/8 is exact.

#### 3. Smooth moments and exact selected multipliers

Expanding the k-th power of the common smooth sum creates a bounded-divisor common full-column polynomial at length S^k. The preceding full-column estimate and k-th root give sqrt(S) K(S^k)^(1/(2k)). Genuine primitive Poisson contributes S/sqrt(VW) and dual length VW/S, producing sqrt(S) K((VW/S)^k)^(1/(2k)). The minimum of these two complete expressions is legitimate. Conductor ratios, rotations, the bounded dual weight near zero and its full large-frequency tail are all retained through common Mellin/angular separation. No zero dual term survives the nonprincipal family. The stated range 1<=S<=VW avoids a subunit dual length; the actual long-Poisson tail handles S>VW.

For the normalized rational selected multiplier, freezing w uses the exact quadratic two-cycle identity including x=0; freezing v uses the exact sixth-cycle identity and all four sparse-column terms. Summing the positive row moments gives exactly the minimum in (13). This retains the true Euler denominators and zero masks. Constants are uniform only on the stated fixed real-part box. The exceptional-set Holder exponent is nonnegative by 1/(2k)+1/(2l)<=1. No density count is divided by V or W.

#### 4. Homogeneity of the analytic upper bounds

For B<=m=min(V,W), Q<=K(B)<=2Q. Hence in optimizing the detector, imposing X>=m loses at most an absolute constant. This is also valid when the original Y<m, by increasing both cutoffs to m and bounding the new decreasing-power tail by the previous one.

Under (V,W,S,X,Y)->(tV,tW,t^2 S,tX,tY), with nonempty row ranges and fixed actual slots, the two direct kernel inequalities in (16) hold term by term. The cross terms in K(tB) have degree 13/6>=2; in K(B) every term has degree at least one. J_2,J_4,K(X) therefore contract by at least t^2. The detector alternatives contract respectively by t^(3/2+a), t^(4/3+4a/3), and t^(1+2a), for a=1-b. The first two powers are at least the third for 0<a<1/2; the trivial cap has power two. Taking admissible optimized minima preserves the bound.

The selected moment contracts by at least t, and its 2k norm by t^(1/(2k)). The full smooth norm contracts by at least t^(1+1/(2l)), since its dual length ratio is unchanged and the direct length decreases. The weighted Holder expression thus contracts by

t^[2-2a(1/(2k)+1/(2l))] <= t^(2-2a).

This is a comparison of explicit positive analytic majorants. It is not an assertion that actual ideal or zero sets rescale, and it does not independently establish the required physical reindexing.

#### Sources and limits

Primary inputs were checked against Goldmakher–Louvel, Theorem 1.1 and primitive Poisson, https://arxiv.org/pdf/1112.1642 ; and de Faveri, Theorem 1.1 and the fixed-family definitions, https://arxiv.org/html/2610.04045v1 . The Gamma detector is the already audited BGL Section 5 construction. The author's fixed ray data, original masks and common-coefficient hypotheses are essential.

The balanced exceptional-row improvement and joint analytic contraction pass. Any complete signed or full physical mixed application requires a separate budget and arithmetic verification.

Final readback confirms the author now restricts (13) to 1/2<=Re(s)<=1 and explicitly permits dependence only on fixed eta/S/ray data and fixed smooth seminorms, not moving conductor sizes. Audited SHA-256: 754788a8b73771d8bb82e2e85848736cedffca4a56ab5a5612c3abee40b6d503.

## B. Complete physical transfer and finite rational certificate

### Independent referee: complete joint mixed (3,5) budget

#### Verdict

Part XVIII B of the companion report passes, conditional on the explicitly attributed Q input and the separately audited joint analytic theorem. The complete mixed type H=epsilon v^3 w^5 a^6, with v,w nonunit, good squarefree and coprime, satisfies the compensated bound Z^(-1/6+epsilon). All physical n, original and core marking, and each exact first Mobius-flat operation are included. The gain over the preceding complete -5/32 is 1/96; the remaining gap to -3/16 is 1/48. Other types and the complete signed probe are not included.

#### 1. Joint family and common arithmetic

The actual inverse-column family eta psi_v chi_w and smooth-column family psi_v conjugate(chi_w) need not be equal; Holder uses their moments on the same joint index set, which suffices. Each joint sieve is proved by freezing one coordinate, but the actual exceptional set is retained jointly afterward. The pooled n_0,E,g divisor choices are bounded joint-row factors after common norm separation. Their moving column unit masks are already in the original v,w zero extensions; r,a',e masks are fixed. The c_2 selected multiplier has common coefficients. The local restoration at h_0 takes place before the positive extension: its additional cs-unit mask is redundant on actual h_0|w support. It must not be retained as an arbitrary rough mask in a fictitious smooth Poisson theorem.

The user's fixed product cutoffs remain in every joint Fourier mode, all imprimitive deleted Euler primes are retained, and the e coefficient is the actual eta(e)/q_e after its one Mobius cancellation. The new joint moments therefore apply to the same common columns as the previously audited physical transfer.

#### 2. Explicit density choices, including the interior tail maximum

Set a=1/8 and v=(13/16-5w)/3. In the first range w<=13/128 one has w<=v. With X=V and Y=V^(8/5), the quadratic side gives J_2=K(X)=Z^(v+w), so the integral and terminal tail exponent equal w+2v/5. The initial tail w+v/4 is smaller.

In the second range v<=w<=12v/11, J_2 has exponent v/2+3w/2 and K(X) has exponent v+w. Choosing y=2(3v+w)/5 gives the exponent 3v/10+11w/10 for both the integral and terminal tail.

In the third range 12v/11<=w<=7v/5 choose y=2w-6v/11. The first integral is bounded by A=21v/22+w/2. For the entire tail u in [v,y], the quadratic term is w+u/4. The sixth-side decreasing cross term v+5w/6-5u/12 meets it at u=3v/2-w/4, with value B=3v/8+15w/16. The other increasing sixth cross term has terminal value A. The common initial term is at most w+v/4<=A on this range, and v+u/4 has terminal value below A. Thus the full tail is bounded by max(A,B); the genuine interior peak is included.

The fourth range uses the separately proved reverse-family density summed over frozen v: v+(55/118)(w+v/6). This is a legitimate joint row upper bound, not a division of a density count by either family size.

Keeping these admissible X,Y choices fixed for larger a, their detector slopes are at most 2y. The stated maxima 37/75, 13/40 and 403/1100 are each below 25/48. The reverse derivative is bounded by (9816/3481)(3/25+17/1440)<25/48. After adding the actual selected P_c^a, S^(-a) and column ratio, every complete Holder expression decreases with a. The remaining density exponent in Holder is nonnegative and at most one. The endpoint a=1/2 is used only as a continuous positive-envelope endpoint for buffered bins, not an extension of a b>1/2 zero detector to the critical line itself.

#### 3. Independent exact finite verification

I independently expanded the actual joint K kernel into the direct and dual smooth affine groups and the selected Euler affine groups. For each group the exponent formulas are exactly (7)–(8). A k,l pair always has 1/(2k)+1/(2l)<=1, including k=l=1, so independently minimizing the selected and smooth norms is allowed. Their remaining common row power is nonnegative.

The maximum of a finite minimum of finite affine maxima occurs at an interval endpoint or an intersection of constituent affine lines. A separate implementation was written and executed independently of the author's companion checker. It builds the groups directly from K, clears denominators, enumerates every rational intersection, and compares values by exact integers/Fractions.

It read the 23 intervals in [joint_mixed_rational_intervals.txt](joint_mixed_rational_intervals.txt), checked exact adjacency and coverage from 7/100 through 3/25, and independently reproduced every stated fraction. All 23 passed the -1/6 target; their exact maximum was -105837/634880. This is an exhaustive finite rational certificate, not a sampled grid or floating-point optimization.

For each interval the independent bound uses v at its left endpoint, w at its right endpoint and the maximum endpoint row exponent. In the third region the row bound is a maximum of affine functions, so this is still an upper bound everywhere. Each full Holder expression is nondecreasing in V,W,R because its net count power is nonnegative. The deliberate frequency-edge inflation is therefore valid.

The two complementary ranges also check exactly. The old forward all-slot bound at w=7/100 is -1607/9600 and is no larger below that endpoint. The old reverse monotonicity gives -321/2048-(2/3)(3/25-5/48)=-77089/460800 at w=3/25 and a smaller value afterward. Both lie strictly below -1/6. Long smooth scales are covered by the actual nonzero Poisson tail.

#### 4. Complete physical transfer

The joint analytic theorem permits optimizing with X>=min(V,W). Under (V,W,S,X,Y)->(tV,tW,t^2 S,tX,tY), its detector contracts by at least t^(1+2a). The reverse alternative allowed in the fourth range contracts by t^(1+7D_6/6), which is at least t^(1+2a) for a in [1/8,1/4]. Selected and smooth norms contract by t^(1/(2k)) and t^(1+1/(2l)); with S^(-a) and Holder, the full positive bound contracts by at least t^(2-2a). Pointwise alternatives have the same or stronger contraction. Actual ideal or zero sets are not being rescaled.

The clean CDF therefore gains (U/K_0)^gamma, gamma=(1-a)/4, for U<=K_0. With the new -1/6 clean bound one can explicitly take B_a=Z^(13/96+11a/16), up to small powers, after removing the common physical prefactor and ratio. For U>=K_0, replacing the analytic reference Z by Z(U/K_0)^(16/13) gives a finite polynomial continuation while leaving the actual selected slots fixed. The full Schwartz integral and Gaussian annuli are consequently justified exactly as in the preceding complete transfer, including effective scales below one and above K_0.

The inherited physical factor is (Y'/C_l)^a R^(6a-2) H_0^(-1), with full frequency V^3W^5(R/H_0)^6 q_a'^6. Odd n_0/E choices contribute at most (NB)^(-1+2a)<=1. The CDF bound gives strictly summable r, a' and external flat weights bounded by R^(-3/2), q_a'^(-9/8) and q_delta^(-13/8). No reverse density count is divided by H_0. All actual unbounded ambient labels are introduced before, and absorbed only after, these strict margins and the original rapid tails.

For a in [1/4,1/2] the already audited complete physical pointwise-density bound -323/1920 is stronger than -1/6. It covers those bins without a new endpoint summation. Both flat operations keep X',Y' and all slots fixed and preserve the numerator type under their exact sixth-power lift.

Audited author SHA-256: 916c4b27ceb34746565cd054a5f911631de13350fc8a847618b696667679c17d.

# Review of Part XIX: complete cubic–fifth mixed sector

## Independent referee: complete cubic–fifth mixed sector

### Verdict and exact scope

Part XIX of the companion report passes conditional on the user's attributed Q input and the previously audited arithmetic and analytic inputs. For H=epsilon u^2 w^5 a^6, u nonunit good cube-free, w nonunit good squarefree and (u,w)=1, the complete compensated bound is Z^(-133/34560+epsilon). All physical n, both original and core markings, and both exact first Mobius-flat operations are included. This covers the (2,4,5) type and remains 6347/34560 above -3/16; it is not a complete low comparison or an RH proof.

### 1. Exact local completion and common columns

Writing u=v_1 v_2^2, the actual local C table gives n=n_0 r^2 with n_0=F_2 E_4, F_2|v_1 and E_4|v_2. At the two odd branches one has respectively j=2, c and s units, or j=4, c and s each divisible once. The outside completed factor is the inherited q_n0^(-3/2). The extra rho^(-3) now contains a genuine fifth-twist residue symbol. It is kept as a bounded u-row factor at fixed w, not replaced by fixed ray data.

At a prime dividing n_0, increasing the physical square-layer exponent by b increases the relevant nonprincipal Gauss modulus by 6b and multiplies its exact value by P^(6b). There is no ordinary 1-P^(-1) term at such a prime. This independently checks the important j=2 case where c and s are units. Ordinary M_p factors occur only at p|r outside n_0 h_0. Boundary h_0 primes, including those dividing r to higher powers, are also excluded.

The lower boundary is only in the fifth part: h_0|rad(r), h_0|w, a=(r/h_0)a', (h_0,a'cs)=1, coefficient mu(h_0)/q_h0. The odd equality also forces (n_0,a')=1. The square factor is kappa(r)/q_r^2. The reduced frequency is H_eff=Hh_0/r^6, and the corrected shared divisor is g=(c/E_4,rad H_eff), with (g,n_0)=1. Removed square-layer primes cannot remain in g by fiat.

Restored covariance factors give the full mixed character pair; the redundant h_0-unit masks are then handled by its original zeros. Ordinary masks are expanded into fixed divisor extractions. The genuine free c_2 coefficient remains mu(c_2)eta(c_2)/q_c2, and the free s_2 column remains common smooth. The e coefficient is eta(e)/q_e with only its original one Mobius cancellation. Moving u,w column masks come from their actual zeros; all remaining deleted primes stay in the imprimitive modulus. Every logarithmically separated mode retains fixed compact product cutoffs.

The true ratio L/S=C_l q_f/(R^6 N^3 Y_*) with Y_*<=Y' gives the total odd factor N^(-3/2+3alpha)<=1. These choices can thus be pooled as divisor-bounded row weights while retaining the exact selected multiplier.

### 2. Moving-conductor density and moment transport

At fixed w, first split by the actual primitive conductor C<=C_0 MW. For W<=M^3, the AFE half-length is at most sqrt(MW) and

Theta_3(M,sqrt(MW)) <= small power * [M+sqrt(MW)+M W^(1/3)] <= small power * M',

where M'=M W^(1/3). The actual conductor also satisfies MW<=(M')^2 in precisely this range. Every other detector sieve input increases when M is replaced by M'. Hence the original cubic detector applies with this enlarged parameter and yields M^D W^(D/3). For W>=M^3 that expression exceeds M because D>=13/24>1/2, so the same capped statement follows from the actual trivial row count, without using an invalid AFE estimate there.

The piecewise convenient D is exactly the previously audited cubic density envelope. Finite heights, fixed twists and all deleted factors have their genuine ambient dependence; no W-dependent constant is hidden.

For smooth moments, the text now explicitly splits the actual conductor before enlarging C to MW. The common dual norm is used only when C/S>=1. For C/S<1 the genuine nonzero Poisson tail supplies the first positive monomial; no subunit dual large sieve is invoked. Nonprincipality follows from the nonunit fifth support, which fixed bad data cannot cancel. With S=W S_0, every direct monomial is at most W times the pure cubic monomial; every dual one is at most W^(1/2) times it. The pointwise and long-Poisson bounds have the same comparison. At S_0<1 this is merely a comparison of positive algebraic envelopes, not a fictitious arithmetic sum. The exact cubic rational-slot moments have unchanged bounds because the fixed fifth values enter common coefficients with all zero masks retained.

In the full reciprocal-e sum these facts cost at most W^(1-alpha+D/3). They preserve both the pointwise and eighth-moment alternatives before taking their minimum. The inherited full-e exponent is J=max(J_1,J_2) in (15). For P_c<=sqrt(M), the finite-choice selected moment has no power loss. For arbitrary P_c the actual k=1 moment gives all three factors (16); Holder remains legal because 1/2+1/8<1. The same factors may multiply the pointwise alternative as well, so the minimum still applies.

### 3. Normal column slots and complete tails

Actual frozen twists satisfying h_0|w are counted by O(W/H_0); no zero-density count is divided by H_0. The weighted M moment of the full Fourier envelope gives the stated K^(J/2) W^(-5J/2)(H_0/R)^(3J) q_a'^(-3J). Writing B=2-alpha+D/3, I independently recomputed the piecewise expressions in (17)–(18):

B-5J/2 <= -257/1152,

r exponent <= -95/48,

a' exponent <= -175/64,

external flat exponent <= -19/8.

For the r bound the expression is nonincreasing in J and the lower substitute J_1 has positive boundary correction, giving exactly the three rational affine expressions in the manuscript. All sums have strict margins. The remaining normalized exponent is at most the inherited -11/2304. The M range is enlarged only after applying its valid slot condition.

### 4. Oversized slots, the genuine finite harmonic range, and exact endpoints

If P_c>sqrt(M), then M<=O(Z^(1/3)). Summing W first against the full Schwartz envelope gives (20), including subunit effective cutoffs. Its H_0 exponent 6B/5-2 is positive. Using H_0<=R leaves r exponent 6alpha-4, at worst -1. This last endpoint is genuinely harmonic, not absolutely summable. The actual Gaussian annular decomposition imposes R^6<=O(C_l) on a nonempty c annulus; the remaining annuli retain their original rapid Gaussian decay. This yields only the permitted logarithmic/small-power loss. The a' exponent is at most -11/5, and the external flat exponent at most -6/5, both strict.

For m_0=log M/log Z and p=log P_c/log Z, the range is the triangle 0<=m_0<=1/3, m_0/2<=p<=1/6. Each of the three actual slot terms is affine in these two variables. Optimizing first in p, according to its sign, and then in m_0 leaves the two displayed endpoint functions E_0,E_1 or smaller values. This also retains negative slot powers; none is improperly enlarged by replacing its lower endpoint with P.

I independently recomputed all three E_0 formulas and all six E_1 formulas symbolically from (15)–(16), rather than relying on the author's checker. Each is decreasing on its stated alpha interval. The largest is the first interval's J_2 expression at alpha=1/8, exactly -133/34560. The other main endpoint, -11/2304, is smaller. Original subset-length terms are nonpositive with the correct selected endpoint choices.

### 5. Uniformity and final readback

All unbounded u,w,n_0,r,h_0,a',e, flat, Gaussian and Mellin labels enter the ambient size before summation. Strict summability and the genuinely finite harmonic r range absorb the small powers afterward. The complete original Fourier/Gaussian tails, fixed physical windows and exact sixth-power flat lift are retained. Boundary alpha endpoints are only positive-envelope limits of the buffered inverse bins.

Final readback confirmed the exact g=(c/E_4,rad H_eff), the odd (n_0,a') condition, and the C/S<1 branch. Audited author SHA-256: 70b127f3a7dd4185538c88162f8a76ef04bfc045347563c964a125dc58c72938.


# Supplement: explicit row tails, tuple ratios and boundary counts

The three clarifications in Parts XIV B, XVI 1 and XIX 5 have passed a separate mathematical review. They clarify the existing sector estimates and do not extend their scope to the full probe.

In XIV B, the needed long-column assertion is per row: primitive nonprincipal Poisson has no zero frequency and, after one extra Schwartz decay absorbs its S/sqrt(W) prefactor, gives C_A sqrt(W)(S/W)^(-A) for every A>0. Apply this to the genuine smooth column after fixed divisor extraction and compact common-weight separation, before taking the supremum over the e-dependent scale. A row-norm estimate alone would be insufficient at this step.

In XVI 1, compact prime windows give c<=q_D/P<=C uniformly before pooling tuples and divisor choices. Derivatives of the joint profile in this ratio and the normalized column variables have polynomial seminorms in the retained heights and Gaussian label. The Gaussian/Schwartz envelope absorbs these powers uniformly. A zero real Mellin part alone does not give this uniform tail.

In XIX 5, the frozen-w count O(W/H_0) and the physical boundary coefficient mu(h_0)/q_h0 supply two distinct H_0^(-1) factors. Formula (20) now displays the former; the latter is still outside. Thus the post-W boundary power is H_0^(6B/5-2), and H_0<=R gives R^(6alpha-4), with the stated finite harmonic endpoint. This correction leaves the exponent -133/34560 unchanged.
