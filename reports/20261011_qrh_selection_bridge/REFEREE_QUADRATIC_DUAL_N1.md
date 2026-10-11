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

# Review of Part XX: complete mixed cubic–quadratic type

## Independent referee: complete mixed (2,3,4) bound

### Verdict and scope

Part XX of the companion report, including its exact all-n arithmetic, full joint budget, verifier and 489 rational rectangles, passes independent review.

Subject to the user's explicitly attributed Q input, the complete normalized contribution of H=epsilon u^2 v^3 a^6, with nonunit good cube-free u, nonunit good squarefree v and disjoint supports, is O(Z^(-1/512+epsilon)). The statement covers all physical n, original and core marking, and each exact first Mobius-flat operation. The 95/512 gap to the required -3/16 remains. This certificate does not supply a new verification of the user's Lean build or a claim about other frequency types.

### 1. Exact arithmetic and common columns

The four odd physical branches are exactly F2 with c=s=0, F3 with c=0,s=1, E3 with c=1,s=0, and E4 with c=s=1. Their remaining frequency valuations are respectively 2,3,3,4. Thus the odd physical factor is coprime to the remaining sixth-power frequency factor. The local square lift is exactly P^(6b) at an odd physical prime. At other square-layer primes it has the stated ordinary factor M_p; in particular the odd residue-two unit--unit branch does not acquire an extra 1-P^(-1).

There is no residue-five boundary in this type. Hence r divides the sixth-power factor a, and H/r^6 preserves the displayed mixed type. No artificial coprimality of r with the odd factor or c is introduced. The local comparison retains the original rho, gamma_3 and omega phases; only kappa(r)/q_r^2 remains from the square shift.

The mixed odd rho values are genuine joint (u,v) row coefficients. They are not fixed-ray constants and are not replaced by characters evaluated at forced nonunits. The correct shared divisor is g=(c/(E4 E3),rad(H/r^6)), coprime to the odd factor. Only this g contributes its Ramanujan factor phi(g). The actual e coefficient is eta(e)/q_e after one Mobius cancellation. All fixed and moving zero masks are retained before taking a positive norm. Original/core slot priority and common compact cutoffs survive the joint log-Fourier separation.

Writing A=q_Nc, N=q_Nq, B=q_E3 and E=q_E4, the exact outside odd factor and free-column ratio are

    A^(-3/2)/(N B),
    L/S = C_l q_f q_tau/(R^6 A^3 N^2 B^2 Y').

The inverse-column bin therefore leaves A^(3a-3/2)(N B)^(2a-1)<=1 for a<=1/2. This explicitly pays all four odd branches and justifies absorbing their remaining divisor counts and cross phases into the joint-row coefficients.

### 2. Joint analytic estimates

For common squarefree columns the kernel is

    K(M,V;B)=min{V[M+B+(MB)^(2/3)], M(V+B)}.

Freezing either row parameter makes its actual twist a common column coefficient for the other sieve. For genuinely bounded full coefficients, the decomposition n=c ell^2 and Minkowski gives B K(M,V;B) with only a small-power loss; the ell character is a bounded joint-row factor, including its zero mask. This is not an arbitrary full-column operator bound with unchanged coefficient mass.

The actual conductor is rad(u)v times fixed data, not the cube-free index uv. Splitting actual conductor blocks before AFE and Poisson, then enlarging positive quantities, gives J2=K(sqrt(MV)) and J4=K(MV). The previous true Gamma-detector argument therefore supplies (5) with its full tail supremum and its intermediate restricted fourth-moment count power retained. The selected moments use the separately established genuine rational Euler identities, not the bounded-full-column shortcut.

For the smooth column the direct and dual moments use actual conductor blocks and common Mellin/angular separation. If C/S<1, the nonzero dual Schwartz tail is used separately, yielding the indicated row bound O(sqrt(C)); it is covered by the positive first moment term before C is enlarged to MV. No subunit-length sieve is invoked. In the clean range S<=MV, K(M,V;MV/S)>=MV. The actual long-S tail is handled by nonprincipal Poisson.

The common-column identities, original imprimitive Euler factors and restored compact product cutoffs agree with the inherited user source. All initial small powers include the moving and unbounded physical labels, rather than treating them prematurely as fixed powers of Z.

### 3. Independent verification of the finite rational certificate

Every affine constituent in (9)--(11) was checked against the complete detector, cubic/quadratic selected moments, and direct/dual smooth moments. In particular:

- The detector tail is maximized over its whole interval, including internal affine intersections.
- The cubic direct smooth third term has slope 5/6-a and the dual third term slope 1/6-a, with the displayed conductor contribution in its intercept.
- Slot and smooth moment orders may be chosen independently: their reciprocal Holder exponents sum to at most one, so the remaining count power is nonnegative.
- On each rectangle, increasing the family sizes and using the upper endpoint a1 in the density gives a valid upper row count. With this count fixed, the rest of each full Holder bound has derivative -11/16+p-s<=-25/48, so evaluation at a0 has the correct upper-bound direction.

The author's exact verifier was actually rerun and returned:

    ALL_PASS 489 rectangles; complete rational coverage;
    maximum -297139/151879680.

An independent verifier was also written and executed. It does not use the author's envelope-intersection algorithm. For a proposed rational level, each complete Holder bound has an interval where all of its affine constituents lie below that level. Taking the exact union of these sublevel intervals proves a uniform bound on the minimum envelope. Rational bisection supplies a slightly weaker rigorous upper bound. This independent method also checks the full detector tail by sublevel covers and verifies the rectangular covering by exact subdivision in both coordinates. It returned:

    INDEPENDENT_SUBLEVEL_COVER_PASS 489 rectangles;
    upper bound -405692699/207366389760 < -1/512.

The independent verification uses a separately implemented sublevel-cover algorithm. All its arithmetic is integer or Fraction arithmetic. No numerical optimizer or floating-point comparison is an input to acceptance. The strict margin permits the required sufficiently small contour buffers and ambient epsilon losses.

### 4. Low-bin all-physical transfer

For a in [1/8,3/8], the explicit joint analytic bounds contract under (M,V,S,X,Y)->(tM,tV,t^2S,tX,tY) by the claimed powers. The restriction X>=min(M,V) is admissible because MV<=K(B)<=2MV below that minimum. The detector contracts by at least t^(1+2a), the selected norm by t^(1/(2k)), and the smooth norm by t^(1+1/(2l)). With Holder, the complete positive expression contracts by at least t^(2-2a).

This is a scaling assertion for the upper bounds, not for actual zeros or ideals. Since M^2V^3 has degree five, its positive cumulative bound gains gamma=(2-2a)/5, at least 1/4 on the stated interval. The polynomial upper continuation and full Stieltjes/Schwartz integration retain this gain for both small and large effective cutoff, including every Gaussian annulus.

The remaining ideal powers are

    r and first-flat: -2+6a-6gamma=(42a-22)/5 <= -5/4,
    a': -6gamma <= -3/2.

They have strict convergence margins. The first-flat change is only T=Z/q_delta^6 with the original q_delta^(-2) coefficient; X',Y' and all original slots remain fixed. The full-modulus lift preserves the frequency type. No coupled-window scaling is inserted. The exact odd weights already paid in Section 1 remain nonpositive throughout.

### 5. High-bin bound without a new density estimate

For a in [3/8,1/2], Cauchy using the full joint count, true cubic-side selected second moment, and pointwise smooth bound produces exactly the three row monomials (17). The full reciprocal-e integral peaks at S=sqrt(MV), rather than at an arbitrarily selected scale.

For the first monomial integrate V first against the complete frequency envelope; for the other two integrate M first. The frequency powers are

    1/2-a/6, 3/4-a/4, 2/3-a/4.

The remaining family's dyadic exponents are respectively -a/6, -(3-a)/4 and -1/2+a/4, all negative. The actual r/first-flat powers are

    7a-5, (15a-13)/2, (15a-12)/2,

all at most -3/2. The a' powers are at most -5/2. Thus these are complete physical estimates, including small effective cutoffs through the nonzero Schwartz tail.

For selected-prime powers, positive exponents use P_c<=P<=O(Z^(1/6)), and negative exponents use P_c>=1. Independent simplification gives exactly

    (10-63a)/96,
    (59-171a)/192,
    61/288-139a/192.

All decrease with a. Their maximum on the whole high-bin interval is -41/1536, stronger than -1/512. The original subset-length contributions are nonpositive with these choices.

### Conclusion

The low-bin rational certificate and both complete physical-transfer arguments jointly establish the stated Q-conditional complete-type bound. The proof retains all original local branches, actual conductors, masks, common coefficients, physical and flat tails. It does not use either newly proposed general-conductor detector or the primitive-pair Halasz--Montgomery improvement, so its conclusion does not depend on their subsequent applications.

# Review of Part XXI: exact signed unit-one two-polar annihilation

## Independent referee: the original signed cubic two-polar contribution vanishes

### Verdict

The self-contained Part XXI of the companion report has been independently read and checked against all component identities. Its precise unit component is epsilon=1, H=w^2.

The conclusion is unconditional: in the original physical epsilon=1, H=w^2, n=g=a=1 sector with squarefree nonunit cubic row w, the explicitly iterated two-polar contribution is exactly zero after summing all actual good and bad dual valuations, the original e convolution, windows and marks. This conclusion does not use the user's zero-free input Q and does not change the probe. Both genuine nonpolar contributions remain.

### 1. Primary-class Poisson and source conventions

The field, primary generators, original additive character and self-dual measure are kept. Poisson on the primary class modulo 3w contributes S/(9 q_w). Its finite Fourier transform is exactly

    e(h/3) theta_w(3) conjugate(theta_w(h)) sqrt(q_w) gamma_original(w).

Thus the amplitude is S/(9 sqrt(q_w)), with the nonprincipal zero dual frequency absent. The finite original bad-prime mask d|B changes this to S/(9 q_d sqrt(q_w)), and changes the radial Fourier argument to S q_h/(9 q_d q_w). Both changes are essential.

The source convention is not silently identified with the original convention. DDDS uses exp(2 pi i Tr z), while the original source uses exp(2 pi i Tr(z/lambda)). Finite Gauss rescaling gives gamma_original(w)=theta_w(lambda) gamma_DDDS(w). Since theta_w(3)=conjugate(theta_w(lambda)), these factors cancel. The actual DDDS numerator is consequently kappa d^2 c h (eB)^3, with no extra lambda.

The fixed character identity conjugate(xi(w^2))=conjugate(theta_w(kappa)) follows from cubic reciprocity and the original local xi data. Primes with zero kappa exponent remain in B and its masks. Positive cube exponents in a numerator remain unit masks after reduction; they are never replaced by the constant one.

After this conversion the row is gamma_DDDS(w)/sqrt(q_w), so DDDS Lemma 6.7 applies with sigma=1 and its original compact radial test. Its exponent-two obstruction, unit/lambda residue constant, finite Euler ratio P/(P+1), w=1 subtraction and remainder are retained. This establishes the claimed source match, not a bound on that remainder.

### 2. Weighted second residue and signed Gauss cancellation

Write A(j)=product_{p|j} P/(P+1) and H_j=product_{p not dividing 3j}(1-(P+1)^(-2)). In the thin channel the second-row weight satisfies A(ell)=sum_{f|ell} lambda_0(f), where lambda_0(p)=-1/(P+1). Extracting ell=f t retains both the squarefree coprimality and the Gauss CRT phase. The signed identity

    conjugate(gamma(f)) theta_f(zeta a0 c) gtilde(zeta,a0 c f)
       = gtilde(zeta,a0 c)

is exact. At the pole, q_f^(-5/6) combines with the numerator factor q_f^(-1/6); the remaining Euler sum is H_{mc}. This gives the stated weighted residue, rather than the residue obtained after taking absolute values.

The residue exchange is justified locally. For fixed remaining parameters, the source's coprimality-removal and convexity bounds give a cost at most q_f^(1/4+epsilon) for the pole-subtracted series in a small neighborhood of normalized s=5/6. Together with |lambda_0(f)|<=q_f^(-1), the outer series is normally convergent there. Cauchy's formula then permits extracting the residue termwise. This assertion does not require, or supply, a uniform bound on all nonpolar terms as c and the physical parameters vary.

The first pole contributes the additional q_ell^(-1/6). Therefore the second pole is at 2/3 in the original ell Mellin coordinate. The two coordinates are (1/3,2/3). The two Gauss phases cancel, giving the exact remaining c weight

    |C_zeta|^2 q_a0^(-1/3) A(m)^2 H_m
       mu(c) eta(c) q_c^(-4/3) product_{p|c} P/(P+2).

### 3. Recombining the actual radial windows

The true joint test is retained rather than replaced by a product. Its Mellin integral at (1/3,2/3) is

    (1/2) (q_e q_c/X)^(1/2)
      (9 q_e q_d/(Y q_tau))^(2/3) MF(1/2) MG(2/3).

The original sqrt(X) cancels. Both e and c acquire norm exponent -5/6; the d exponent is -1/3. The finite support factor A(eB)^2 H_{eB} becomes A(B)^2 H_B product_{p|e} P/(P+2). Hence the thin-channel allocation at fixed k=ec has the genuine sum sum_{e|k} mu(k/e), retaining D|k and the original Gaussian V_G(q_k/U_D).

These identities use the exact full e-series after Poisson. A physical large-e vanishing statement is not imported as a separate cutoff into a partial dual or polar term. The original norm partitions are recombined, and the Gaussian supplies absolute convergence of the extracted polar e/c sum. The nonpolar terms remain in the original decomposition.

### 4. All good h valuations

The unique decomposition h=tau u v^2 t^3 has u,v squarefree and coprime, with t arbitrary. First-pole support forces v|c and (u,c)=1, so c=v c0. The variable u may share primes with e and t. After extracting A(B e v c0 t), its remaining prime weight is one at p|et and P/(P+1) elsewhere. Its true mask is K=B v c0, not B e v c0 t.

The weighted second residue is therefore exactly

    conjugate(C_zeta) gtilde(zeta,a0 c0) q_(a0 c0)^(-1/6)
        A(K) H_(B e v c0 t).

Applying the actual joint-window integral leaves e and c0 with exponent -5/6, v with exponent -11/6, and t with exponent -2. At fixed squarefree k=e v c0 the remaining signed allocations have local sum

    1 - P/(P+1) - (1/P) P/(P+1) = 0.

All three allocations are actual original branches. In particular the branch where u shares e is accounted for by its prime weight one. All marks D|k and their original Gaussian depend only on k, not the allocation. Thus every nonunit k vanishes. The remaining t-series is absolutely convergent, with the stated Euler factor 1+[(P+1)/(P+2)] P^(-2)/(1-P^(-2)).

### 5. The mandatory bad prime kills the last unit

It remains to sum the original d|B and bad-supported tau. Their exact norm factors are q_d^(-1/3) q_tau^(-2/3), with q_a0^(-1/3), the first-pole support, e(tau/3) and |C_zeta|^2 retained.

Every B-prime has its primary generator congruent to one modulo three. Its tau valuation therefore changes neither the additive phase e(tau/3) nor the unit/lambda datum zeta. At a B-prime set x=P^(-1/3), j=v_p(kappa) modulo three, and f=(1,x,0). The local sum is

    T_j = sum_{delta=0,1} (-x)^delta sum_{a>=0} x^(2a) f_(j+2delta+a),

and direct geometric summation gives T_0=1, T_1=T_2=0. This combines the original mask sign and the original dual-window scaling; no contour relation is imposed.

At the mandatory prime (2), the residue field has four elements. The original xi is nonprincipal there, hence has order three; its square is still nonprincipal. Thus j is one or two, and this local factor is zero. The finite d sum and the bad-supported norm-geometric tau sum converge absolutely, so this cancellation annihilates the last unmarked unit term as well.

### 6. Precise boundary of the conclusion

The calculation concerns the specified order of two polar extractions. It does not identify those residues with the whole finite probe, exchange arbitrary contour orders, eliminate either nonpolar integral, or establish a bound for g>1, a>1, n>1 or mixed cube-free w.

### Sources checked

- [Original arithmetic source fixed at openai/math commit fd4aeeb2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), especially field/primary/Gauss conventions, the original xi construction and full-modulus local tables.
- David, de Faveri, Dunn and Stucky, arXiv:2410.03048v2, Sections 3.3 and 6, including (3.5), (6.8), the coprimality-removal formulas, convexity estimate and Lemma 6.7: https://arxiv.org/html/2410.03048v2 .


The complete publication text preserves the original unit-one restriction, full-e qualification, all good/bad dual valuations, source-convention conversion, weighted second residue, original radial Mellin integral, actual three prime allocations and the norm-four bad-prime cancellation. The two nonpolar remainders and every other physical/unit/core sector remain outside the conclusion.

### Extension retaining every original shared divisor g


The appendix to Part XXI also passes independent review. It extends the exact vanishing to every original shared g while still fixing the unit component epsilon=1, n=a=1 and squarefree nonunit w.

The original coefficient is mu(g)eta(g)phi(g)/q_g. With the actual free-column scale S=Y/(q_g q_e), primary Poisson gives the displayed outside q_g^(-2). Writing w=g r retains (r,g)=1 and the original zero forces (h,g)=1. Cubic Gauss CRT supplies conjugate(theta_r(g)), so the first numerator is g kappa d^2 c h. The exact signed identity (7) cancels the original g Gauss factor and every g-dependent character of that numerator. It leaves q_g^(-1/2-1/6)=q_g^(-2/3), not a new oscillating d/tau factor.

The remaining u mask is B g v c0; u still may meet e and the cube factor t. The same weighted-residue argument therefore applies with g genuinely retained in its finite masks. The actual two radial windows are those in (9). Their joint Mellin value contributes q_g^(5/6), hence the final shared-divisor coefficient is precisely mu(g)eta(g)phi(g)q_g^(-11/6).

For each fixed allowed good configuration, all d/tau dependence is now exactly the previously proved bad-prime scalar. The norm-four factor is zero, independently of the original D|g e c mark and its unchanged Gaussian scale. The bad-supported tau geometric sum, the t^(-2) good cube sum and the Gaussian in q_(g e c)/U_D justify the regrouping. No absolute convergence of an unsmoothed q_g^(-5/6) sum is asserted or needed.

The enhanced conclusion covers all shared g in this unit-one, n=a=1, squarefree-w sector. It still concerns only the specified iterated polar contribution; neither nonpolar remainder, any n>1 or a>1 layer, other unit components, nor mixed cube-free w is added by this extension.

The all-g appendix was subsequently frozen by a status-only change; its final SHA-256 is `a72868889558b0a422702a28ba8779f0d42e852f117a6af0058128c39b7c1a9c`. The mathematical content is the audited extension above.

# Review of Part XXII: complete three-core transfer

## Independent referee: complete three-core (2,3,4,5) transfer

### Verdict and scope

The argument in Part XXII of the companion report passes independent mathematical review, with the explicit uniformity and equation-format clarification recorded at the end of this certificate. It establishes, subject to the user's Q input, the complete bound O(Z^(-1/512+epsilon)) for

    H=epsilon u^2 v^3 w^5 a^6,

where u is nonunit good cube-free, v,w are nonunit good squarefree, and their supports are pairwise disjoint. All physical n, original/core marking and each exact first-flat operation are included. The bound retains the 95/512 gap to -3/16 and excludes residue one. It uses the independently verified complete (2,3,4) clean certificate; it does not rely on a new numerical optimization.

### 1. Exact physical interface

The four odd branches from (2,3,4) are unchanged, and the fifth support has no odd branch. At every odd prime, including a prime also dividing the square layer r, the Gauss lift is exactly P^(6b). The ordinary multiplier must exclude both n0 and the lower-boundary h0, even when a boundary prime divides r to order greater than one.

The only lower boundary is h0|rad(r), h0|w, a=(r/h0)a', with (h0,a'cs)=1 and coefficient mu(h0)/q_h0. The full effective frequency is H h0/r^6. The genuine g=(c/(E4 E3),rad(H_eff)) is coprime to n0. Only g contributes phi(g); no forced odd prime is counted twice. Restoring the h0 character factors recovers the actual full mixed character pair. Its redundant h0-unit condition is removed before positive row enlargement.

All cubic/quadratic/fifth crossing symbols remain bounded joint row factors. They are not declared fixed-ray phases, and no nonzero forced Gauss branch is represented by a character at a nonunit. The actual free e coefficient has exactly one Mobius cancellation. Common columns, original/core slot priority and all original imprimitive deleted primes are retained.

The exact odd weights are A^(-3/2)/(NB) and L/S=C_l f tau/(R^6 A^3 N^2 B^2Y'). Consequently the inverse-bin powers A^(3a-3/2)(NB)^(2a-1) are nonpositive. The remaining physical factor is (Y'/C_l)^a R^(6a-2) H0^(-1), with the full Fourier envelope stated in (12).

### 2. Moving fifth twist: the common factor t^(-1)

Fix the actual w and set t=sqrt(W), M'=tM, V'=tV. These are numerical parameters for upper bounds, not rescaled ideal indices. Direct monomial comparison gives

    K(M,V;B)<=t^(-1)K(M',V';B)

on both branches. The exponents in the cubic branch are 2,1,5/3; those in the quadratic branch are 2,1, all at least one.

The fixed w-character is a common coefficient in either original sieve. The actual conductor C is at most M'V'=MVW, with actual conductor blocks taken first. The bounded-full-column decomposition, AFE second/fourth moments, inverse polynomial and complete Gamma-detector tail retain the same t^(-1). Both first-integral alternatives are homogeneous of total degree one in these moment kernels. The actual row count MV=t^(-2)M'V' is even smaller. Thus the stated exceptional-row bound R_w<=t^(-1)R_234 is valid, including the row-count cap.

The genuine rational slot 2k moments likewise have the factor t^(-1) before taking roots. The fixed w phase remains in their common coefficients; their denominators and zero masks are retained. Smooth direct and dual 2l moments have the same factor after using actual conductor blocks. For C/S<1, the individual nonzero Poisson tail and the actual row count t^(-2)M'V' cover the first positive moment term without applying a sieve at a subunit length.

Holder therefore produces exactly

    t^(-theta) t^(-1/(2k)) t^(-1/(2l))=t^(-1),
    theta=1-1/(2k)-1/(2l)>=0.

This includes theta=0. Pointwise alternatives correspond to an infinite moment order and also preserve the equality. The proof pays the moving fifth conductor explicitly; it must not hide w among fixed bad-prime constants.

### 3. Complete low-bin tails

For a in [1/8,3/8], the previously proved clean positive CDF has gamma=(2-2a)/5>=1/4. Since M'^2 V'^3=W^(5/2) M^2V^3, the physical envelope and the t^(-1) payment give W^(-1/2-5gamma/2) before summing the actual w rows.

The genuine count of squarefree w with h0|w is O(W/H0), with W>=H0. This is ordinary frozen-ideal counting, not an exceptional-row density divided by H0. Its H0^(-1) is distinct from the physical boundary coefficient. The W shell exponent becomes a-1/2<=-1/8, so its tail contributes H0^(a-1/2). The remaining powers are exactly

    R^(6a-2-6gamma) H0^(6gamma+a-5/2) q_a'^(-6gamma),

with R exponent at most -5/4, H0 exponent -1/10-7a/5<0, and a' exponent at most -3/2. Divisor-small h0 sums and all initial ambient losses fit these strict margins.

The CDF is integrated against the entire Schwartz envelope. For a small effective cutoff the subunit nonzero-frequency tail is retained; above the reference range, the same polynomial continuation is absorbed by a higher Schwartz order. The actual Gaussian absorbs fixed exponential losses in its annulus label. This is not a hard-cutoff argument.

The exact first-flat coefficient changes only T=Z/q_delta^6 and adds q_delta^(-2). It leaves X',Y' and all slots fixed. Its exponent is the same -2+6a-6gamma<=-5/4. Thus both markings and both first-flat operations are fully covered.

### 4. Complete high bins

For a in [3/8,1/2], the full family count and true cubic-side selected second moment give the three monomials (24). The count restriction h0|w appears in both Cauchy factors and yields exactly one H0^(-1); the physical boundary supplies the second.

The full reciprocal-e maximum is at S=sqrt(MVW), not at an arbitrarily selected column length. Frequency integration yields gamma1=1/2-a/6, gamma2=3/4-a/4 and gamma3=2/3-a/4. The other M or V shell exponent is strictly negative in each case. The W exponent p-5gamma_i is also negative. After summing W>=H0, the remaining boundary exponents are

    -2a/3, (1-3a)/4, 1/6-3a/4,

all nonpositive on this entire high-bin interval. The R/flat exponents are 7a-5, (15a-13)/2 and (15a-12)/2, at most -3/2; all a' exponents are at most -5/2.

No positive W power remains. The normalized exponents reduce exactly to the reviewed (2,3,4) values, whose maximum is -41/1536. Independent algebra checks these linear endpoint inequalities; the accompanying exact affine checker was also actually run and returned ALL_PASS. Thus the high bins are stronger than the stated complete exponent.

### 5. Uniformity and inherited user corrections

The original tuple ratio q_D/P must be in its fixed compact interval before joint differentiation and row pooling. Gaussian/Schwartz envelopes are uniform in that ratio, not merely in a zero-real-part Mellin variable. The actual e-dependent long-S tail must first be bounded on each primitive row and actual conductor block, retaining its compact common cutoffs, and only then summed over e. These are the user's explicit clarifications in commit 782137 and are validly inherited here.

All constants depend only on fixed original data, buffers and the stated smooth seminorms. Moving w and every actual deleted Euler factor enter the explicit conductor or ambient parameter, not a newly enlarged fixed S. Strict physical powers and full rapid tails absorb the initial small losses only after these parameters are introduced.

The combined proof establishes exactly the displayed complete-type theorem. It supplies no residue-one bound or full low/high comparison.

### Final readback

The explicit moving-w-not-fixed-S paragraph, the user's two uniformity clarifications, and the repaired right parenthesis in (21) have been read back. The audited mathematical SHA-256 is `54a4c18cb0071d8649aabde52b17474a0e9e75802991631f32baa5fb328a11b2`. The accompanying exact affine endpoint checker was run and passed. Status-only changes after this version do not change the mathematical verdict.

# Review of Part XXIII: complete mixed (3,5) estimate


## A. Genuine-conductor detector

### Independent referee: genuine-conductor long detector

The retained detector and arbitrary-full-column large-sieve arguments pass independent review. The K_0 branch retains its original common-column or bounded-coefficient hypotheses; the Q^2+B branch is the arbitrary-full-column operator. The balanced density bound is unconditional, while the later full physical theorem has the user's stated Q hypothesis.

#### 1. Direct verification of the full-column large sieve

In the Eisenstein PID choose one generator of each modulus and each ideal column. A column of norm at most B lies in a fixed lattice disk of radius O(sqrt(B)); arbitrary coefficients are zero-extended to the other lattice points. Characters trivial on units evaluate these chosen generators exactly as their ideal values.

Reduced fractions a/f of denominator norm at most Q are distinct modulo the relevant fixed lattice after the associate choice. Equality would force the two denominator ideals to coincide by coprimality. A nonzero difference has numerator a nonzero Eisenstein integer and denominator fg, so its distance on the torus is at least c/Q, not Q^(-1/2). The different and the trace pairing only change a fixed linear lattice map and constants.

The manuscript's Gaussian duality proof of the two-dimensional additive large sieve is complete. A Gaussian majorant bounds the column-disk indicator. Poisson turns the dual Gram kernel into a positive periodic Gaussian of mass scale R^2, R comparable to sqrt(B). Delta-separated packing in planar annuli bounds its absolute row sum by O(R^2+Delta^(-2)). Schur and duality give B+Q^2.

For each primitive multiplicative character modulo f, the genuine Gauss expansion has amplitude q_f^(-1/2). After taking the squared norm, enlarging the positive sum from primitive characters to all unit-group characters and using their exact orthogonality produces phi(f)/q_f times the sum over reduced additive fractions. This factor is at most one. Thus the claimed all-primitive-character inequality holds for arbitrary full common columns. It does not use a sixth-power-free index reduction.

The actual joint character determines its good v support from local order two and w support from local order six. Fixed bad/ray pieces give only bounded repetition. Thus the all-character inequality applies to the original family; the larger family is used only in a positive norm. All common primary, fixed angular and norm-twist coefficients remain legal.

#### 2. True inverse, complete detector tail and explicit gains

The inverse polynomial is the original mu-weighted polynomial. Its product with L has coefficients sum_{d|n,q_d<=X}mu(d), vanishing on 1<q_n<=X and divisor-bounded elsewhere. The new full-column inequality applies to this actual tail with its original unit masks. The prior finite-height Sobolev, Gamma tail and common-conductor separation arguments are unchanged.

For the fourth-moment branch take J=K_0(Q), X=Q^2 and Y=(JQ^4)^(1/(2(1+a))). Since J>=Q and a<=1/4, this has Y>=X. Throughout U>=X the global kernel is at most 2U, so the full detector tail, including its initial endpoint, is at most 2Y^(2a). The first integral balances that quantity. This gives min(Q,(JQ^4)^(a/(1+a))).

For the second-moment branch take J_2=K_0(sqrt(Q)), X=Q^2 and Y=(Q^2 J_2)^(1/(1+2a)). Again J_2>=Q>=Q^(4a) guarantees Y>=X. Its first term Y^(a-1/2)Q sqrt(J_2) balances the same complete tail Y^(2a), giving min(Q,(Q^2 J_2)^(2a/(1+2a))).

At V=W=N one has Q=N^2, J_2<=C N^2 and J<=C N^3. The respective exponents are 12a/(1+2a) and 11a/(1+a). At a=1/8 these are exactly 6/5 and 11/9. These are upper bounds for exceptional joint rows, not asymptotic counts.

The explicit homogeneous J upper bounds in (8) are also correct. For V>=W the quadratic side gives O(VW^2). For V<=W each term in V Theta_6(W,VW) is bounded by V^(11/6)W^(7/6). No moving conductor has been put into a constant.

#### 4. Combined homogeneity and its necessary restrictions

Scale (V,W,S) to (tV,tW,t^2S), and use X,Y scaled by t^4 in the long detector. Since X=Q^2, the new cutoff equals the square of the new conductor range and stays admissible on nonempty rows. The global kernel at these cutoffs gains t^4, whereas J_2 and J gain at least t^2. The second first-term, fourth first-term and complete tail therefore gain respectively

t^(1+4a), t^((16a+2)/3), and t^(8a).

For a in [1/8,1/4] the first two exponents and the trivial-cap exponent two are all at least 8a. Thus the positive density majorant contracts by at least t^(8a). This is a comparison of admissible analytic bounds, not a literal rescaling of zeros.


## B. Pair-Gram and true tail

### Independent referee: true pair-Gram, smooth norms and detector tail

The retained statements for the genuine finite-order Eisenstein family, original zero extensions and actual conductors pass independent review.

#### 1. Exact fixed-row arithmetic

For each prime of a fixed row, the varying row has three states: absent, quadratic, or sixth-order. The assignment count is divisor-small. Equal types cancel as characters but retain a unit mask. Crossed types have exponent +2 or -2 and remain primitive cubic characters. The fixed-only components form a fixed character; the free varying components remain precisely the conjugate original quadratic--sixth family. After a finite bad/ray partition, no off-diagonal principal ratio remains.

Let g be the cancellation support and f the actual primitive ratio conductor. Prime-by-prime comparison gives q_f q_g^2<=C Q^2. The crossed primes do not incorrectly disappear from this comparison. Expanding the original zero mask over d|g, and dilating n=d x, retains a genuine modulus-one varying-row scalar. The remaining scale is U/q_d. No d-dependent moving phase is put into the common frequency coefficients.

#### 2. Poisson, bounded-full columns, and varying detector weights

Primitive Poisson has amplitude (U/q_d)/sqrt(q_f) and dual norm scale J0=q_f q_d/U. The nonprincipal zero frequency vanishes. Its complete Gauss/root factor is a pure row scalar; the fixed conductor character is a common frequency coefficient, including its zeros. The free frequency character is the actual original joint family. This is the necessary common-column property, not just a conductor-size comparison.

Actual conductor ratios are separated on compact dyadic row blocks. For the annular detector weights, beta_j and t_j/T can additionally be separated on fixed compact boxes after a smooth extension. All separating Fourier factors are pure row scalars. Uniform Schwartz and Fourier seminorms cost a polynomial in T. This deals with arbitrarily selected beta_j and t_j; it does not replace the inner weight by an unjustified row-dependent supremum.

On a frequency dyad J the previously established bounded-full-column inequality gives amplitude squared times J K_(V0,W0)(J), with its full rapid tail. Summing by Minkowski at J0>=1 yields exactly

    (U/q_d) K_(V0,W0)(J0),

because amplitude squared times J0=U/q_d. When J0<1, the nonzero Schwartz tail gives an arbitrary positive power of J0 before enlarging to K_(V0,W0)(1). The inequalities V0<=C V, W0<=C W and q_f q_d<=C Q^2 therefore prove

    sum_(j!=i) |G_ij(U)|^2
       <= ambient^epsilon (1+T)^C U K(max(1,Q^2/U)).

Unit free factors are permitted by the elementary one-row bound. All divisor-small assignments and mask divisors are summed with a smaller initial loss. The proof is a true fixed-row squared-Gram bound, with the original full zero masks.

#### 3. Restricted arbitrary-full-column operator

A positive radial Gaussian majorant and ideal/full-lattice unit normalization give diagonal O(B). On a subset of at most R rows, Cauchy in the off-diagonal columns and Schur bound the Gram norm by

    D_R(B)=B+sqrt(R B K(max(1,Q^2/B))).

Duality proves the claimed arbitrary-full-column inequality. This use does not confuse the original squarefree-column K theorem with a full-column operator theorem; the latter is newly obtained through the Gram argument.

The upper logarithmic slope assertion is correct. Before clamping, B K(Q^2/B) is the minimum of sums of nonnegative monomials in B with exponents in [0,1]. After clamping it is linear. Hence it is nondecreasing and at most linear under dilation; taking the square root and adding B preserves D_R(cB)<=c D_R(B).

#### 4. True restricted smooth moments

For the common smooth sum, the direct power coefficients have divisor-bounded squared mass. The primitive dual is treated with actual conductor blocks, its row root number, common ratio separation, nonzero near-origin terms and full Schwartz tails. In the genuine disjoint squarefree joint family C is comparable to Q up to fixed data. This gives (11) on 1<=S<=Q. These norms concern the very same subset of R rows; no artificial ratio R/V or R/W is inserted.

#### 5. Genuine detector tail

With the original common divisor-bounded coefficient mass, the annular Gram estimate gives

    R U^(2b) <= U^(1+epsilon)
       [U+sqrt(R U K(max(1,Q^2/U)))].

Solving the quadratic inequality in sqrt(R) gives precisely

    R <= U^(2a+epsilon)+U^(4a-1+epsilon)K(max(1,Q^2/U)).

For a in [1/8,1/4], the second summand decreases with U, including the clamped range. After the actual smooth dyadic selection and exponential far-tail treatment, the complete tail is bounded by the stated Y term plus the value of the second term at X. The original Gamma-integral term and its genuine second/fourth moments remain unchanged.


## C. Explicit density contraction

### Independent referee: explicit pair density and contraction

The certified domain is all V,W>=1, with 1/8<=a<=1/4.

#### Detector choices

For X>=V, the displayed kernel bounds give precisely the four terms in (2). Balancing the fourth-moment first term with Y^(2a) yields R(X)=(V W^4 X^2)^(a/(1+a)). Solving against each of the two genuine tail monomials gives the stated XA and XB. Choosing their maximum, rather than their minimum, pays both tails. Both choices have X>=V, and their individual coefficient inequalities give Y>=X. Since the logarithm of max(XA,XB) is one of the two logarithms, the same admissibility holds for the chosen X.

The RA and RB exponents and simultaneous degrees were independently simplified. The identities in (9) are exact, with positive denominators throughout the stated interval. They prove 1<=delta_A<=2 and delta_B>=delta_A. The trivial count degree is two. Hence the minimum with VW and the maximum of the two detector alternatives both retain the degree-delta_A contraction.

The additional exact identity delta_A-(4a+1/2)=(8a-1)(4a^2-3a+1)/(2D) is nonnegative on this interval. It is independently verified with rational algebra.

Indeed J4<=W(V+VW)<=2VW^2 uses only W>=1, and K(X)<=2WX uses only X>=V. The XA/XB admissibility inequalities were already proved separately for the positive V and W exponents, so require no ordering. All subsequent homogeneous kernel and moment arguments are also shape-independent. The contraction explicitly requires tV,tW>=1 and the actual smooth-range conditions. This removes only an unnecessary hypothesis; it does not extend the a interval or certify a complete physical bound.

## D. Complete physical estimate and exact verification

### Independent referee: complete mixed (3,5) estimate with the user's selected-slot gain

#### Verdict

The proof in Section D of the companion Part XXIII passes independent review. Subject to the user's genuine finite-order Hecke Q input and its separately audited selected-slot consequence, the exact original/core, all-physical-n, two-first-flat mixed type

    H = epsilon v^3 w^5 a^6,
    v,w good, squarefree, nonunit, and coprime

satisfies the stated normalized bound

    I_(3,5)(Z) << Z^(-3073/16384+epsilon).

This is a saving of 1/16384 beyond -3/16 for this complete frequency type. It does not settle the other types or the complete signed low/high comparison. No independent Lean rebuild is claimed. The user's commits 113702dd9ff055b343a89d2667fb9ff72783de97 and 7821372494c3cc9b675f694549ca2550db0ff423 retain their attribution.

#### 1. Actual physical and selected-column interface

The exact two odd branches n0|v, their crossing phases, and their common-column reconstruction agree with the independently checked all-n mixed interface. Their residual weight (NB)^(-1+2alpha) is at most one. The fifth-boundary condition is h0|rad(r), h0|w, including the possibility that p^2|r. The ordinary local factors exclude boundary and odd primes in the established manner. The physical outside factor and complete Fourier envelope are precisely (2).

On the actual restricted family h0|w, restoration of the genuine mixed character already supplies its h0-unit zero. Removing a redundant copy before positive enlargement is legitimate; dividing an exceptional-row density by H0 would not be. The low-bin proof does not make that division.

The new pointwise selected theorem applies after every physical divisor, unit/ray and common compact log-Fourier mode has been fixed. The remaining coefficients factor over the actual disjoint slots. Fixed factors have only the allowed fixed finite-order bad-ray characters; the moving good factors remain in the true row character. Its nonempty good ramification prevents the principal exception. The bound is not asserted for arbitrary arrays or an angular infinite-type twist.

Thus the actual extraction cost is P_c^(alpha-1/8), with P_c=1 allowed. It is bounded by P^(alpha-1/8) because alpha>=1/8. No spurious contraction power is assigned to this fixed P_c factor. All imprimitive holes remain in the actual modulus.

The user's two uniformity requirements are necessary and explicitly retained: common differentiated compact q_D/P envelopes before tuple pooling, and primitive Poisson on each actual row before the e-dependent long-S tail is summed. The modes keep their compact product cutoffs.

#### 2. Density and moment inputs

The joint kernel K is used for its genuine common squarefree-column estimate and its separately proved bounded-full-column consequence. The arbitrary-full-column restricted kernel instead comes from the actual pair-Gram theorem:

    D_R(B)=B+sqrt(R B K(max(1,Q_c^2/B))).

The full direct/dual smooth alternatives, actual conductor blocks, Gauss root numbers and zero masks are preserved. New general/restricted alternatives are used only at moment index j>=2. The proof does not use the separate new coupled-product or raw-slot estimates.

Every branch in (7) is a valid bound on the same exceptional set. The explicit branch is max(R_A,R_B), not their minimum: both genuine tail requirements must be paid. Its admissibility and homogeneity hold for all V,W>=1. The fourth-moment envelope min(VW^2,V^(11/6)W^(7/6)) is valid with the stated shape split; it is not an unsupported extension from V>=W.

The nested zero-set argument permits evaluating density at the upper alpha edge while using the lower alpha edge in the remaining cost. With density fixed, the latter derivative is exactly -25/48-s. Every Holder dependence on row count is nonnegative, including D_R's own dependence on R. Positive family enlargement to v+ and w+ is therefore safe.

#### 3. Independent exact rational verification

The author's standalone verifier was actually run to completion. It returned:

    ALL_PASS 4351 rational rectangles; complete S sublevel covers; goal -3073/16384

A second verifier was written independently from the displayed operator definitions. It constructs an exact min/max expression tree for K and D_R, explicitly includes max(1,Q_c^2/B), computes affine sublevel sets by unions and intersections, and checks the rectangular domain by an independent vertical coverage sweep. It neither imports the author's affine-group enumeration nor samples floating-point grids. Its actual completed result was:

    INDEPENDENT_OPERATOR_AST_PASS 4351 rectangles; actual clamped D_R; goal -3073/16384

The entire S interval is covered on every rectangle, not merely selected values or endpoints. The 4351 fixed boxes cover [1/8,1/4] x [0,13/80]. All arithmetic in both verification steps is integer/rational.

Although the author's affine implementation does not explicitly clamp a negative logarithm of Q_c^2/B, this does not understate its envelope: at negative column logarithm, each branch of K is dominated by its constant VW term and equals the value at logarithm zero. The independent verifier nevertheless retains the clamp literally.

Constants hidden by finite positive sums, moment orders, and the fixed box covering are absorbed by the allotted epsilon loss, with the stated strict exponent margin. The numerical discovery or generation process is not a proof input.

#### 4. Low-bin contraction and all physical tails

For 1/8<=alpha<=1/4 every allowed density envelope contracts with degree at least 4alpha+1/2. In particular the explicit minimum degree is

    delta_A=alpha(9-20alpha)/(1-alpha-4alpha^2),

and the second degree is no smaller. The requisite exact rational inequalities were checked independently in the contraction certificate. The frozen quadratic branch, total count and genuine-conductor branches also meet this lower degree.

Under (V,W,S)->(tV,tW,t^2S), the old smooth norm contributes at least t^(1+1/(2j)), and each permitted new norm contributes at least t. For a new direct restricted norm it is essential first to expand B K(Q_c^2/B), or to use monotonicity in the full column operator. The quotient Q_c^2/B alone can increase when j>2. The manuscript's latest clarification correctly retains all positive expanded monomials. The dual ratio Q_c/S is fixed.

With the nonnegative Holder row-count power, all allowed complete expressions have degree at least 3/2. This gives frequency CDF exponent gamma=3/16. The argument concerns explicit positive analytic envelopes, not a dilation of actual zero sets.

Full Stieltjes integration against the Fourier/Schwartz envelope, including effective subunit cutoffs and all Gaussian annuli, supplies (T/Z)^gamma (H0/R0)^(6gamma) q_a'^(-6gamma). Combining the exact outside factor yields

    R0^(6alpha-2-6gamma) H0^(6gamma-1) q_a'^(-6gamma)
       <= R0^(6alpha-3) q_a'^(-9/8).

Here H0<=R0 is used because 6gamma-1=1/8. The square exponent is at most -3/2. The exact first-flat sum has exponent -2+6alpha-6gamma<=-13/8. These are strict ideal-summation margins. Actual divisor counts and all moving modulus/height small powers are paid before the sums are collapsed into Z^epsilon. No hard Fourier cutoff or jointly rescaled physical-window theorem is assumed.

#### 5. High bins and the full subset ledger

For 1/4<=alpha<=1/2 the previously checked complete pointwise proof remains applicable, with the one justified replacement P_c^alpha by P_c^(alpha-1/8). Its maximization is valid even when the column slots are empty. The resulting complete all-scale expression is (12).

The actual frozen-w count W/H0 is legitimate here and is separate from the boundary H0^(-1); it is not imposed on a density estimate. The original W-shell exponent remains at most -1/20, the final H0 exponent is nonpositive, and square/flat exponents remain at most -3/2. The full small-T Fourier bound is retained.

Writing kappa=3alpha/(1+alpha)+(1-alpha)/2, the normalized exponent is

    -29/96+13kappa/48-25alpha/48-1/48.

Its derivative is 13/[16(1+alpha)^2]-63/96<0 on this interval. Its exact maximum is -121/640, strictly below -3073/16384.

For every original subset of exponent d_slot, the extra term is exactly -d_slot(alpha-1/8)<=0. Thus the selected gain is reconciled with the actual compensated probe scales; it is not simply subtracted from a leading-only exponent. The theorem follows in the full scope stated above.


# Review of Part XXIV: signed secondary remainder

## Independent referee: specified secondary cubic remainder

The four-part base theorem passes independent review for η=ε=1, squarefree nonunit w in H=w²a⁶, every physical n/a/g/h, the original finite compensation, and separately the original/core markers and each exact first Möbius scale transform. The specified secondary nonpolar term is O(Z^(−19/480+ε)), without Q. Its finite-physical-e-first decomposition is part of the assertion. The first nonpolar contribution, other units and mixed cube-free w remain unestimated. The following base calculations and successive extensions certify that scope. The separately audited cube-free extension below adds the complete nonunit cube-free w range, still only for the specified secondary contribution.

### Base calculation: signed column and n=a=1

#### 1. The true Mobius--Gauss estimate

The finite convolution identity (2) is exact: its error is mu*(1-1*mu_z)^(star J), supported above z^J. On squarefree c every factorization is into pairwise coprime squarefree factors. The actual Gauss CRT gives the displayed cubic kernel; it retains the coprimality zero and separates the u-dependent phases into common row or column coefficients.

For delta<=1/3 and fixed sufficiently large J, a factor longer than C^(1-delta) can only be an unrestricted 1-factor. Otherwise grouping the bounded factors produces a genuine Type II split with both lengths between C^delta and C^(1-delta), up to fixed annular constants. Smooth norm partitions and common Mellin separation retain divisor-bounded coefficients. The cubic sieve and Cauchy give exactly C^(1-delta/2)+C^(5/6), with no numerator-size factor in Type II.

For Type I, the moving numerator ua is squarefree and coprime to the long variable. The actual DDDS convention is retained. The published coprimality formula and convexity estimate were independently reread in the primary source. On the unnormalized line 1+epsilon, their divisor terms have costs at most d^(-3/4) for d|ua and e^(-1/4) for the extra mask; the local Delta inverse is uniformly bounded there. Consequently the stated normalized long-row bound

    B^(5/6)(q_a q_u)^(-1/6)+B^(1/2)(q_a q_u)^(1/4)

is valid with the displayed small losses. This uses the source's exact squarefree numerator and stated character family.

Summing the short a-variable gives a harmonic first term and the second term C^(1/2+3delta/4)q_u^(1/4). For q_u<=C^(1/3), delta=1/3 yields C^(5/6). Otherwise balancing at delta=(2-log(q_u)/log(C))/5 gives C^(4/5)q_u^(1/10); q_u>=C^2 is covered by the trivial bound. A finite sufficiently fine delta grid, followed by the allotted epsilon loss, keeps J fixed independently of C and u. This proves (1).

The A_* weight and its local-one variant are compatible with the factorization. In Type I their divisor expansion yields absolutely convergent f^(-2) and f^(-5/4) series. The variant is important because c0 may meet the cube factor t; imposing an extra coprimality would be wrong.

#### 2. Marked columns

The selected primes remain explicit factor variables in the finite Mobius decomposition. Their original smooth coefficients are common after the legitimate compact norm separation, and the number of their assignments to a fixed product is divisor-bounded. If every selected prime is at most C^(1-delta), a Type I long factor is still necessarily unrestricted. Type II may include selected variables in either grouped coefficient. Thus the stated marked estimate does not lose an extra power from first bounding each tuple separately.

The manuscript correctly restricts this use to C>=C0 P^(3/2), which suffices for all delta<=1/3. The complementary short c0 range is estimated separately. No theorem for an arbitrary prime-restricted long Type I row is assumed.

#### 3. Exact order of the finite-e decomposition

The original physical W1 support implies q_g q_e<=C1 Y. Restricting the whole physical column by this condition before Poisson is an exact finite reorganization. The ensuing first and secondary remainder pieces need not equal the corresponding pieces obtained by first extracting poles from the untruncated-e representation.

The final bad-prime cancellation from the previously audited all-g proof holds for every fixed allowed good configuration. The physical e indicator depends only on g,e and is constant throughout that configuration's complete bad-mask and bad-dual sum. It therefore preserves the second-pole zero. This step uses that local bad-prime cancellation, not the earlier sum over every allocation e|k. It is consistent with the prohibition on imposing a physical cutoff on an already extracted old polar piece.

Thus the first polar contribution of this finite-e representation equals its secondary nonpolar contribution, with the first nonpolar and unit-row terms retained. No cutoff is imposed on h.

#### 4. Complete scale calculation for the stated secondary term

With C approximately U_l/(GEV), M=sqrt(U_l/X), radial residue scale R=M/G and actual u scale H=GEM/(Y q_tau V^2 T^3), the original first residue has exactly the c0 weight q_c0^(-7/6), the u weight q_u^(-1/6), and the displayed outside g/e/v factors. Its g phase is the already checked all-g cancellation. The normalized residue scale R is a continuous Mellin scale and is not treated as an integer count when below one.

Applying the signed column lemma gives C^(-1/3)+C^(-11/30)q_u^(1/10). Actual u summation with the original nonzero Schwartz envelope yields H^(5/6) and H^(14/15), also for H<1 by rapid decay. The two positive block expressions in (13) were independently recomputed, including all powers of G,E,V,T and q_tau.

The genuine finite bound E<=C1 Y/G pays the positive E powers. In both resulting terms the g coefficient becomes exactly phi(g)/G^2, whose sum through the physical range is logarithmic. The v and cube-factor t sums are absolutely convergent; the bad-supported tau sums are geometric. This gives precisely

    X^(-1/12) U^(1/4) Y^(-2/3)
       +X^(-2/15) U^(4/15) Y^(-19/30).

Marks in positive variables remain divisor weights, and marks in c0 were kept inside the signed lemma. The original tuple norm ratio and compact common-mode seminorms must be uniform before pooling, with their Gaussian/Fourier tails retained.

#### 5. The short-column complement

When C<C0 P^(3/2), the physical e bound forces V much larger than U_l/(Y P^(3/2)). The trivial signed c0 bound is C^(-1/6), not the stronger marked Type I/II estimate. Its ideal V tail has exponent -5/2 and therefore contributes the cutoff to power -3/2. The resulting term is exactly

    X^(-1/12) U^(-13/12) Y^(2/3) P^(9/4).

It is a safe overestimate when the threshold is below one. Full Gaussian annuli absorb every fixed resulting power of exp(l); no false hard Fourier cutoff is used.

At the stated leading scales, the three exponents are -11/192, -19/480 and -115/192. The second is the largest. The complete bound claimed for this specifically defined secondary term follows.

#### Source and remaining boundary

The source checks use DDDS, *Non-vanishing for cubic Hecke L-functions*, arXiv:2410.03048v2, Corollary 6.2 and Lemmas 6.3, 6.7, with its actual additive-character normalization: https://arxiv.org/html/2410.03048v2 . The finite identity, signed bilinear reduction, parameter balance and physical bookkeeping above are the independent steps needed to use that source.

The original pinned source and already audited all-g signed calculation supply the exact physical starting identity. This base calculation remains eta=1. The subsequent sections supply the actual a, n and first-flat extensions. Additional ray or angular Gauss-row twists, other units, mixed cube-free w, the first remainder and the complete low/high comparison are not inferred from it.


### Complete a range and original finite compensation

#### A. Exact arithmetic of the additional a layer

The original signed n=1 identity was reread. Its free-column a mask expands as mu(f)vartheta_w(f), f|rad(a), with terms meeting w zero. Primary Poisson therefore supplies f^2 in the conjugated numerator and the exact physical column scale Y/(q_g q_e q_f), not an artificial extra phase.

The decomposition g=g_w g_a, g_w=(g,w), g_a|rad(a), (g_a,w)=1 is exact even when a and w meet. It imposes the displayed true r mask. No false condition (a,w)=1 is introduced. The original g_w zero requires h coprime to g_w; the f zero requires f coprime to w.

At a prime of f, first-pole support excludes h valuation zero modulo three and gives exactly the f1/f2 allocation in (4). The f1 numerator becomes a cube; the f2 numerator retains its squarefree factor. The moving signed-column numerator f2 u0 is squarefree and coprime to c0. The original masks, including a, are preserved. Its c0/t local-weight variant is exactly the one already proved admissible in the signed lemma.

The g_w phase cancellation is the same source-normalized Gauss CRT calculation as before. The additional f2 Gauss phase is retained until the second residue, where it cancels against its paired numerator factor. It is not discarded as a harmless bad-prime phase.

The second row has K=B g_w f v0 c0 and J=B g e f v0 c0 t. In particular u0 can meet g_a,e,t; excluding these primes would be an incorrect strengthening. Its weights are one on J outside the actual mask and P/(P+1) elsewhere. Thus the same normally convergent weighted-residue calculation applies. After both residues, the entire bad dependence remains exactly (8). The norm-four bad-prime cancellation still occurs for each fixed allowed good configuration. The whole physical truncation GE<=C1Y was imposed before Poisson and remains constant through that bad-prime sum.

#### B. Exact positive bounds and full a summation

The actual continuous first-residue scale is R=M/G_w, with M=sqrt(U_l/X) A^(-3). The dual u0 scale is H=GEM/(Y q_tau F2 V^2 q_t^3). Its f1 cancellation and remaining F2^(-1) were checked directly against both original windows.

Combining the displayed outside factor with the signed column and actual u0 summation gives the same factor F1^(-1)F2^(-2) in both terms. The g/e factors before e summation are respectively

    phi(g) G^(-5/6) G_w^(-1) E^(1/6),
    phi(g) G^(-7/10) G_w^(-1) E^(3/10).

The true physical bound E<=C1Y/G makes both equal to phi(g)/(G G_w) times their stated scale factors. This splits into phi(g_w)/G_w^2 and phi(g_a)/G_a. The first is logarithmically summable through its physical range; the second is summed only over divisors of rad(a).

The f-allocation product is exactly the finite positive Euler product in (13). All these counts have divisor-small cost. The M powers give A^(-7/2) and A^(-19/5), so the unrestricted original a sums converge absolutely with strict margins.

The trivial short-c0 branch must also be retained. Here the E power is zero, giving a logarithmic sum rather than the positive E endpoint used above. Its g factor is still phi(g)/(G G_w); its f factor remains F1^(-1)F2^(-2), and its A power is A^(-7/2). The genuine V lower bound and tail are unchanged. Thus the same three geometric expressions from the leading proof remain valid after all a are summed. Full Gaussian annuli and nonzero Schwartz tails handle all subunit effective scales.

#### C. Original compensated rescalings

Section 5 defines the projection inside each actual original rescaled probe before forming its signed finite combination. It does not assert that a new projection commutes with an unrelated change of full-modulus labels. The remaining marker, original U_D, actual removed slots, physical e cutoff with Y', and all original masks are explicitly preserved.

At X'=Z^(17/48-d), Y'=Z^(23/48-d), U=ZP with P=Z^(1/6-d), the independently recomputed powers of the two main terms are -11/192+d/2 and -19/480+d/2. The short-column term is -115/192-7d/4. The actual original coefficient q_rho^(-3/2) and O(Z^(d+epsilon)) tuple count together supply -d/2. Consequently the two main powers return exactly to their leading values, and the short-column power improves. There are only the original finitely many subset patterns.

The final theorem is therefore O(Z^(-19/480+epsilon)) for this complete-a secondary contribution in the original finite compensation, with eta=epsilon=1 and n=1. It remains one rigorously defined remainder term, not the complete cubic sector. The separate first-flat proof is given below.


### Complete physical n range

#### D. Actual square covariance, odd branch and signed numerator

The exact original covariance for n=n0 r^2 keeps mu(h0)kappa(r) q_r^(-2) q_k^(-1), with j=(h0,rad(s)), k=h0/j and j^2|s. The full-modulus lift forces r|a in this cubic sector. Its unit covariance cancels only the k multiplier. It does not cancel the free-s character at j^2.

In particular the surviving j phase is psi_w(j^2)=conjugate(vartheta_w(j)). It is harmless as a modulus-one row coefficient in the previously proved absolute estimates, but a signed source-row calculation must retain it. The new note does so: its first source numerator is j kappa d^2 f^2 c2 h. The original condition (j,H')=1, with all other masks, is preserved.

The pinned source's local-P expression and complete local family table were actually reread. For squarefree w the only odd branch is j'=2, with n0|w, (n0,a')=1 and neither c nor s divisible by n0. Its local factor has the fixed phase a_p rho^(-3). At epsilon=1 the moving squarefree-w component has rho^(-3)=1. Thus this is a scalar depending only on n0, not a new moving twist in the cubic Gauss row. Its already established physical norm factor is N^(-3/2).

Writing w=n0 g_w rho retains the genuine inducing conductor and masks. The original n0 g_w Gauss factor cancels precisely its paired first-residue numerator factor, leaving (N G_w)^(-2/3); no d/tau-dependent phase remains there.

At j, first-pole support allows dual h exponents zero or two modulo three and kills exponent one. Hence the exact j=j0 j2 allocation in (9) is necessary. The first squarefree numerator becomes a0 n0 g_w j0 f2 c0 u. Its remaining moving numerator j0 f2 u is genuinely squarefree and coprime to c0, so the signed-column theorem applies without a new source theorem. The j0^(1/10) cost in its second term is explicitly paid.

The second row's true mask K and finite-weight support J in (12) are distinct; u may meet J outside K, including g_a,e,t. The paired numerator Gauss phases cancel as in the previously certified weighted residue. All retained mu(h0), kappa(r), odd-n0 phases and j/f choices are good-variable factors. The bad dependence is exactly the already proved norm-four zero, for each fixed good configuration. The whole-column cutoff G q_j^2 E<=C1Y is imposed before either residue and is constant through that bad-prime sum.

#### E. Independent full norm calculation

The actual first-residue scale is M/(N G_w), with M=sqrt(U_l/X) A^(-3) and U=ZP/q_r^6. The dual u scale is GEM J0^2/(Y q_tau F2 V^2 q_t^3). These were checked directly from both original windows: j2 and f1 cancel their own dual valuations, while j0 and f2 leave the displayed factors.

Before the signed column, the N powers total -3/2-2/3-1/3=-5/2. The two column bounds therefore give N^(-3/2) and N^(-7/5); the trivial column gives N^(-2). These are actual ideal sums, not counts of at most divisor-many n0 after a residue has removed w.

After the real E cutoff, the exact j weights are

    J0^(-5/6) J2^(-7/3),
    J0^(-4/5) J2^(-13/5).

They follow from q_j^(-2), the numerator residue q_j0^(-1/6), the two H powers, the second-column numerator J0^(1/10), and the j^2 in the E endpoint. All are nonpositive, so the fact that j divides rad(r) permits the final divisor-small bound without a hidden growth factor. The f weights remain F1^(-1)F2^(-2); the g factors and A powers remain those certified above.

The two net physical-square weights are q_r^(-7/2) and q_r^(-18/5). All h0/j/k choices and original mark assignments have divisor-small cost. The original signs and angular kappa(r) are retained until this positive estimate, and no angular source theorem has been used.

#### F. Necessary joint short-column tail

The small-c0 complement cannot first be summed in V and then bounded by a divergent N series. The new note correctly keeps the joint restriction V>>U_l q_j^2/(N^3 YP^(3/2)). With L=U_l q_j^2/(YP^(3/2)), ideal counting gives

    sum_(n0) q_n0^(-2+epsilon) min(1,(q_n0^3/L)^(3/2))
       << L^(-1/3+epsilon).

For L>=1, splitting at q_n0=L^(1/3) verifies both parts separately; for L<1 it is an overestimate. The remaining j powers only improve. This yields exactly

    X^(-1/12) U^(1/12) Y^(-1/2) P^(1/2).

Its physical r weight is q_r^(-5/2), strictly summable. Its leading exponent is -17/192, below the main -19/480. All Gaussian annuli are retained.

The three expressions in (20) consequently have leading powers -11/192, -19/480 and -17/192. In an original subset of exponent d, the first two acquire +d/2 and the third acquires zero. The original coefficient and tuple count supply -d/2. The same main exponent follows for the actual original finite compensation, with the sector defined inside each rescaled full-modulus expansion.

This extension is specific to the newly restored signed j arithmetic. It does not obtain an all-n result merely by quoting an earlier absolute common-column formula.


### Exact core-marker and first-flat interface

The all-n proof retains every positive Gaussian scale T. Its three final U=TP powers are 1/4, 4/15 and 1/12. The formerly negative U power belonged only to the n=1 short-column shortcut; the actual joint n0,V bound replaces it. Full Gaussian annuli, continuous first-residue scales, nonzero dual tails at subunit H and the all-L positive joint-tail estimate give the same bound with arbitrarily small prescribed scale losses. In particular at T=Z/q_b^6 those losses are Z^epsilon q_b^epsilon after choosing the initial exponents sufficiently small. The revised statement uses a prescribed positive delta, not an undefined uniform o(1).

Core marking is handled with its own exact priority list. A prime dividing r alone is excluded; a prime dividing both r and c n0 remains and is reassigned in the shorter list. One must not delete every tuple formerly assigned to r. The signed c0-column proof and the other convergent positive assignments consequently remain applicable without an inequality between oscillating markers.

The original first scale operation is precisely the sum with coefficient mu(b)kappa(b)/q_b^2 at Gaussian parameter Z/q_b^6. Its full-modulus lift multiplies H by b^6, preserving the actual unit and squarefree w. For finite b truncations, perform the whole physical-e restriction and successive residue decompositions separately in each inner sector. This gives an exact finite decomposition. The secondary sum then converges absolutely with weights q_b^(-7/2+epsilon), q_b^(-18/5+epsilon), q_b^(-5/2+epsilon).

The original projected flat sector also has its defining limit. Therefore its remaining first term can be defined as the limit of the finite decompositions, equivalently sector minus secondary. No bound for that first term, or exchange of an uncontrolled first-remainder contour, is required for this conclusion. It is not claimed that a differently regrouped flat physical expression has termwise identical intermediate residues.

The norm-four second-pole zero holds separately for each b, since the physical-e cutoff and all good configurations remain independent of its bad allocations. Applying the calculation inside each original compensated rescaling retains the already checked d ledger. Thus both the original-marked and core-marked specified first-flat secondary pieces also satisfy O(Z^(-19/480+epsilon)). The first nonpolar remainder is still uncontrolled. This remains eta=epsilon=1 and squarefree nonunit w, with all physical n/a, rather than a theorem for all cubic types or all units.


The final self-contained Parts I–IV were read back together. Their conventions, finite-e ordering, true j phase, joint short-column tail, core-prime reassignment and convergent external sum agree with the separately checked calculations above. No interchange of an uncontrolled first-remainder integral is required.


## Complete cube-free extension of the specified secondary term

### Independent audit: the unit-one complete cube-free cubic secondary term

The cube-free extension in internal Part V of the companion Part XXIV passes independent review as an extension of the specified secondary contribution. Its target and original unit remain eta=epsilon=1. It includes w=v1 v2^2 with v1,v2 coprime squarefree and w nonunit, every original physical n and sixth-power factor, both exact markings, their first-flat operations and the original finite compensation. The first nonpolar contribution is still unestimated. In particular this is not a stronger bound for the whole cubic probe.

#### 1. Primitive and odd local arithmetic

The two primitive cubic CRT cross factors cancel by reciprocity, giving gamma_D(v1)bar(gamma_D(v2)). The primitive conductor is v1v2, not the cube-free index v1v2^2. The conversion from the original additive Gauss convention and the primary Poisson factor at 3 cancel componentwise. The Poisson factor in (1) is therefore correct, including its square-root norm.

The original local-P table was independently reread at j'=2 and j'=4. For the latter, e0=l=k=1 gives the exact coefficient -a_p rho^(-3)P^4 before the original norm weight. Its product with P^(-3/2)P^(-4) is -a_p rho^(-3)P^(-3/2). The j'=2 branch gives the positive counterpart. For unit epsilon=1 the moving good part of rho^(-3) equals one, since the actual cubic-core exponents are even. Thus the remaining phases depend on the fixed odd factors, not on the later source variables. The n_- divisor is present in both c and s; its additional inverse norm from the second Poisson is mandatory and retained.

The earlier exact square reduction retains its j character and cancels only the k unit multiplier. It yields precisely (2)--(4), including the physical-e cutoff. No ordinary square-layer mask has been replaced by a forced odd-prime character value.

#### 2. The two source residues

At fixed v2 the first source is the actual v1 family. v2 is a coprimality hole, not an exponent-two numerator in that first source. The added fixed conjugate Gauss factor and character remain outside it. The first residue's j/f/h allocation is unchanged. Its c0 column acquires exactly the squarefree, disjoint numerator v2 j0 f2 u; (8) is the signed column to which the proved lemma applies. Its second bound must carry the factor L^(1/10).

For the second u residue, the genuine zero mask is K in (9); J controls the different finite weight. The new numerator v2 is squarefree and lies in K. The extra gamma_D(v2) from that residue cancels the outside conjugate Gauss sum. The CRT factor cancels theta_v2(zeta a0 j0 f2 c0), with its actual conjugate direction. All remaining new factors are good. Consequently the bad-prime d/tau scalar has precisely the previously proved local norm-four zero. The physical-e cutoff is fixed before these operations and independent of those bad allocations.

Only v2=1 requires the old entire unit-row subtraction. When v2 is nonunit, rho=1 is a genuine allowed term and is retained. The revised manuscript makes this distinction explicit.

#### 3. Independent norm check

The three actual scales in (10) follow respectively from the original c n^3 Gaussian, q_H=q_v1^2 q_v2^4 q_a'^6, and the primitive conductor in the second Poisson. In particular the first-residue scale contains L^(-2), whereas the u scale contains L^(-1).

Before the signed estimate the n_- power is -5/2. In the first term it receives +4/3 from C^(-1/3), +5/6 from the u sum and -1/6 from the finite E endpoint, giving -1/2. In the second term the corresponding additions are +22/15,+14/15,-3/10, giving -2/5. The n_+ powers remain -3/2 and -7/5.

The L exponents are respectively -1/2-2/3-5/6=-2 and -1/2-2/3-14/15+1/10=-2. Thus the stated uniform L^(-2) is exact. Omitting the moving-numerator loss would be incorrect. The residual g coefficient is phi(g)/(G G_+); its g_- part and the n_- choices are true divisors of v2 and have only divisor-small cost. This leaves a strictly summable v2 norm series. The earlier a', physical-r and n_+ margins remain unchanged.

In the short selected-column range, the E cutoff gives (13). The exact trivial weights are N_+^(-2)N_-^(-1)L^(-2). Summing N_+ jointly with its V tail, rather than summing a divergent isolated N_+ power, gives (14). Its N_- factor cancels the preceding inverse power. The resulting geometric error is therefore exactly (15), and its r power remains -5/2.

#### 4. Complete scope and limits

The revised common-mode paragraph charges the moving v2 holes and scales to the ambient parameter first. Actual joint compact q_D/P derivatives and individual long-column tails are retained before pooling. The new small powers are absorbed by L^(-2) and the existing strictly convergent tails. The original marker is redistributed only among its actual factors; no unmarked v2 prime is turned into a selected slot. The core priority list retains primes shared with r and c n0 by their later allowed assignment.

The three positive-scale geometric terms are unchanged. Therefore the original compensation still gives the exponent -19/480, and the same exact inner-physical-e-first definition followed by the absolutely convergent first-scale sum gives both first-flat secondary pieces. Their first remainders are defined by subtracting this convergent contribution from the corresponding full sectors; no interchange of an unestimated first remainder is invoked. Other original units remain outside this theorem.


The final self-contained five-part report was read back. Its original four-part mathematical proof is retained, with local scope sentences referring to the new Part V. The introduction defines the first v1 pole at fixed v2; the same positive-scale estimates and exact first-flat decomposition remain. The first nonpolar term and other units are still excluded.


## Square-unit extension of the specified secondary contribution

### Independent review: all square-unit cubic secondary components

#### Decision

The square-unit argument in internal Part VI of Part XXIV passes independent review. It extends the already audited eta=1 secondary-remainder theorem from epsilon=1 to every epsilon in {1,omega,omega^2}. The full cube-free core, physical n/a layers, both actual marker conventions, both first-scale transforms, and original finite compensation remain included. The specified secondary contribution retains the bound Z^(-19/480+epsilon_loss). The first nonpolar contribution and the three nonsquare units are not covered.

#### 1. Genuine primary Poisson vector

For epsilon of order three, tau(c)=chi_c(epsilon)=theta_c(epsilon^2). The equality uses the order-three image on epsilon and theta=chi^2. The supplementary character is nontrivial on the primary subgroup and therefore has lambda conductor strictly beyond lambda^2. The six global units give the six distinct invertible classes modulo 3; consequently tau extends trivially on global units, and every product with a mod-3 character remains primitive at the same larger lambda conductor.

The primary indicator is exactly the average of the six mod-3 characters. Applying the primitive Gauss transform to each product tau*kappa_0*chi gives its amplitude S/(sqrt(q_m)*sqrt(q_q)). In Gauss CRT the factors are tau(q), chi(m), and the two normalized Gauss sums; kappa_0(q)=1 since q is primary. The original-to-DDDS conversion contributes the additional chi(lambda). This proves (4), with chi(m lambda) and exactly one factor 1/6, already included in Phi_tau. The Fourier norm argument is S q_h/(q_m q_q). Primitivity makes each Phi component zero on lambda nonunits, and the original good-character zeros remain present.

For a primary x, the mod-3 characters equal one on x, proving Phi_tau(xh)=bar(tau(x)) Phi_tau(h). In particular this covariance must be used, rather than treating the primary norm-four generator as trivial at the higher lambda conductor. Expanding the fixed bad mask contributes mu(d) tau(d) chi(d)/q_d with the actual radial scale S/q_d.

#### 2. Restored phases at both source residues

The original square-unit factor is tau(s)bar(tau(c)). Its common e/g factors cancel, while the physical j/f/c2 factor remains tau(j^2 f)bar(tau(c2)). The odd n0 phases have tau(p)^(-3)=1, so their previously established local identities persist.

Multiplying tau(v1 v2) and chi(m lambda) into the original two Gauss characters yields exactly the two numerators in (5). The first numerator is Z/(m lambda L), while the second has the extra L^2. Here L=epsilon^2. All lambda fractions are evaluated at good units and can be reduced modulo cubes within the published source family.

Insert j=j0 j2, f=f1 f2, c2=v c0 and h=tau_h f1 u j2^2 f2^2 v^2 t^3 into the covariance. The f1, j2 and v factors cancel exactly; the remaining character is bar(tau(j0 f2 c0 u)), as asserted in (6). This changes the fixed bad numerator for the actual signed c0 column and subsequent u residue from zeta0 to zeta1=zeta0/L. The moving squarefree numerator and all its holes are unchanged.

The finite Gauss rescaling identity gives

    bar(g3(zeta0,a0))*g3(zeta1,a0)/q_a0 = theta_a0(zeta0/zeta1)=tau(a0).

The same identity on the good moving factors cancels their restored tau weights. In the mixed core, the extra tau(v2) cancels the conjugate tau(v2) from L^2 in the original second Gauss factor. Thus (9) retains precisely the indicated bad-prime dependence.

#### 3. Bad-prime local cancellation

At a primary bad prime p, let delta in {0,1} be its d-valuation, b its frequency valuation, and e in {0,1} its surviving squarefree numerator valuation. The source support imposes e=j+2delta+b modulo 3. Phi covariance supplies tau(p)^(-b), the mask supplies tau(p)^delta, and the Gauss ratio supplies tau(p)^e. Their product is tau(p)^(delta-b+e)=tau(p)^j because tau(p)^3=1.

This scalar is independent of both local summation variables. The complete local sum is therefore tau(p)^j times the previously verified T_j=(1,0,0). At the original norm-four prime, j is 1 or 2 by the original nonprincipal order-three bad character. The specified second pole vanishes. The constants depending on reduced unit/lambda classes do not change with primary bad-prime allocations away from lambda, so no such dependence has been suppressed.

#### 4. Analytic and scope transfer

Every newly introduced conductor and finite Gauss coefficient depends only on the original fixed unit component. The actual signed c0 family still has a reduced fixed bad numerator and the same squarefree moving good numerator. Fixed norm dilations leave the joint compact modes, physical-e-first cutoff, individual long tails and weight-seminorm class valid. All three positive-scale estimates, the strict n/a/v2 sums and the exact first-flat construction therefore carry over with unchanged powers.

This argument does not invoke finite-order Q, extend it to an angular character, or identify a complex diagonal with a contour shift. It also does not treat the nonsquare units, whose additional bad character requires a separate source matching.


The six-part unified report was compared with its five-part base and read back. Parts I–V retain their ε=1 proofs; Part VI supplies the reviewed extension. The top-level frequency is H=εw²a⁶, with η=1 and ε∈{1,ω,ω²}. Both exact marker conventions, both first-scale transforms and the full cube-free core remain included; the three nonsquare units and first remainder remain excluded.


## All-six-unit extension: the negative-unit polar functional

### Independent audit: the first polar functional for the actual negative units

#### Decision and precise consequence

The negative-unit proof in internal Part VII of Part XXIV passes independent review, using the fixed all-lambda-cusps noncubic theorem proved in Part XXVII A and the already audited exact physical decomposition. For eta=1 and each of the three negative original frequency units, the specified first Gauss residue is zero for every fixed admissible outer configuration. Its ordered first-polar-then-second-remainder functional is therefore zero. Combined with the positive-unit proof this extends the specified secondary estimate to all six units. It does not bound the first nonpolar contribution or identify this decomposition with the coupled Mellin wall.

#### 1. Actual finite bad vector and normalization

The factor chi_c(epsilon) splits as the primitive norm-four quadratic psi_4 times the positive-unit cubic lambda character. The full finite period retains its 2-part equal to 4, all lambda data, primary selection and genuine holes. The bad vector obeys A(qv)=tau_epsilon(q)A(v) for good primary q. CRT modulo Mq, with residues qb+Mr, gives exactly S/(q_M sqrt(q_q)), tau_epsilon(q), chi(M lambda), and the normalized DR Gauss factor in (4). The positive-additive conversion contributes the displayed chi(lambda); the primary mask appears exactly once. Primitive norm-four Fourier support is on 2-units, not a fictitious primitive modulus-two character.

#### 2. The noncubic factor survives every physical phase

Both moving Gauss chiralities in (5) retain psi_4(v_i). Splitting v1=n_+g_+r leaves the genuine moving factor psi_4(r). Gauss CRT, the actual j phase, the original xi contribution and the good numerator supply cubic factors only. At the two odd physical branches j'=2 and 4, the free core enters rho_p^(-3) as r^2, producing chi_p(r)^(-6)=1. Thus no unrecorded physical factor cancels psi_4(r).

The extra q_r^(-1/2) beside normalized gamma_D is absorbed by s=z+1/2. The pole z=1/3 is consequently s=5/6 in the normalized row, not an incorrectly shifted pole. All actual support exclusions remain fixed holes of that row. Its norm-four character is psi_4 times a cubic character factoring through modulo 2, and hence remains nontrivial on 1+2O modulo 4. The separately proved all-lambda-cusp result applies even with the actual fixed lambda-ray factor. If an entire unit-row subtraction is required by the nonunit-core convention, it contributes no residue.

The corrected bad-prime symbol is theta_w(4)=(w/(-2))_3^2. The proof retains this value rather than squaring the Jacobi symbol modulo 4.

#### 3. Quantifiers and the remaining integral

The holomorphic germ at 5/6 is used only after each original outer configuration is fixed. Hence the polar functional is identically zero before summing physical layers, slots or scale transforms. No uniform level estimate or exchange of an uncontrolled infinite first-remainder contour integral is asserted or needed for this zero functional. The first remainder is retained as the actual original sector minus that functional, and the first-flat convention applies this definition to each inner physical sector before its exact scale operator.

The all-six-unit secondary statement inherits the positive-unit exponent -19/480 and its established full-n, full-a, two-marker, two-first-flat and finite-compensation scope. The negative-unit contribution to this particular functional is exactly zero. The complete cubic sector and the first nonpolar term remain open.

Ownership of the prime-to-three noncubic input remains with the user's d4f8dfe theorem. The extra lambda compatibility is the separately audited translated-theta result; it is not inferred by applying DR's prime-to-three theorem outside its domain.


# Review of Part XXV: genuine truncated-inverse results

## A. Exact inverse Gauss projection

### Independent referee: genuine truncated-inverse Gauss projection

#### Verdict

The corresponding section of Part XXV passes review. The result keeps the actual coefficient a_n(X)=sum_(d|n,Nd<=X)mu(d). Its residue factorization is unconditional; the sharp decay uses only the user's Q for the fixed Dedekind zeta function. Its moving-level assertion concerns the residue only. The smooth signed-sum theorem retains fixed r,S and 2<=X<=U^(51/100).

It does not provide a corrected Gram theorem, a full detector-tail saving, an arbitrary-coefficient sieve improvement, or an estimate for the separate physical mu(c)psi(ch,s) sum.

#### 1. Source and exact level residue

The pinned September 25 source was actually read, including its definition of G, metaplectic level series, equation typeI-residue and full Proposition typeI proof. Its G is normalized in the stated original additive convention and vanishes on nonsquarefree moduli. Thus f_l automatically omits m meeting squarefree l.

Factoring the exact source residue gives rho_l=C0 (Nl)^(-1/6) product_(p|l)(1+1/Np)^(-1). The extra S mask is a finite inclusion-exclusion over primes not already dividing l, with the prime above 3 omitted from that reinsertion. Its residue multiplier at a new excluded prime is P/(P+1). Consequently (7) is exact for every d coprime to S.

The original inverse expansion has only finitely many d for each fixed X. In its initial absolute domain it is exactly (8), so its meromorphic continuation and residue extraction require no infinite interchange. Multiplication by (Nd)^(-5/6) converts the extra level factor into 1/product_(p|d)(P+1). This proves the precise signed residue identity (1).

#### 2. Sharp cutoff and Q

The Euler correction E_S has the nonnegative local coefficients P^(-j)/(P+1), j>=1. They give an absolutely convergent coefficient series in Re z>-1, uniformly bounded above by the series with only the original prime above 3 deleted. Its moment at 1/8-epsilon is finite. This is stronger than a merely meromorphic factorization and permits the required sharp coefficient convolution.

The revised reciprocal-zeta argument correctly contains both steps. Borel--Caratheodory gives log zeta=O(log T) on a buffered zero-free left line. Interpolation with the bounded Euler right line, on buffered rectangles, then bounds log zeta by a power of log T strictly below one at an interior line. Hence the reciprocal is O(T^epsilon). This implication does not follow from Borel--Caratheodory alone.

Truncated Perron at a half-integral norm cutoff, with a sufficiently large power height and initially smaller losses, therefore gives M_S(t)<<t^(7/8+epsilon). The integer-norm coefficients are divisor-bounded. Vertical and horizontal contributions and the truncation error fit within this exponent. Partial summation gives the convergent weighted sum with total zero and the sharp bound M_1,S(t)<<t^(-1/8+epsilon). The zero total agrees with the zero of reciprocal zeta at one.

Convolution with the positive E_S coefficients now proves (2), including its actual sharp d cutoff. No smoothing substitute or coefficient modification is introduced.

#### 3. Moving deleted primes: residue only

For S0 consisting just of the prime above 3, the exact reciprocal finite Euler product gives

    M_1,S(t)=sum_(e supported on M,Ne<=t) (Ne)^(-1) M_1,S0(t/Ne).

Its positive majorant is the convergent product of (1-P^(-7/8-epsilon))^(-1). Splitting off the finitely many primes below a threshold depending only on epsilon proves an O_epsilon((NM)^epsilon) bound, uniformly in the set of deleted primes. The E_S moment is bounded by E_S0's positive moment. Finally |rho_r,S|<=C(Nr)^(-1/6). These prove (2a), with M the full extra deleted-prime product, including the support of r. They do not make the later Type I constants uniform in moving r,S.

#### 4. Actual smooth signed projection

The source Type I comparison permits arbitrary divisor-bounded level coefficients, including the original sharp d cutoff and its signs, and level-dependent common compact smooth tests with uniformly bounded derivatives. For fixed r and the finitely many fixed S-mask divisors, the new level is a fixed multiple of d. In each d dyad the total norm scale is a fixed multiple of U, and the level is O(U^(51/100)). The original W(dm/U) has exactly the required uniform rescaled derivatives. Thus the source comparison is applicable, including its endpoint convention; dyadic summation costs only a logarithm.

The squarefree model count with the original coprimality mask gives the local density product (1+1/P)^(-1). Inserting the n^(-1/6) weight yields the main term c_S U^(5/6)H_S(X), with the stated fixed r factor. Its error is U^(1/3+epsilon)sum_(Nd<=X)(Nd)^(-1/2+epsilon), hence U^(1/3+epsilon)X^(1/2). The actual inner lengths are at least U^(49/100), so no subunit counting estimate has been invoked.

Combining these facts gives precisely the three terms in (3). The third is well below U^(5/6-1/100) throughout X<=U^(51/100); the asserted kappa=min(delta/8,1/100) for X>=U^delta follows. No unproved moving-level uniformity has been inserted.

The source is the fixed OpenAI September 25 text at:
https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/background-type1.tex .
The user's Q attribution is retained; no formal build was rerun in this audit.

## B. All-cutoff SW for the actual Gauss column

### Independent referee: all-cutoff SW for the actual inverse Gauss column

#### Verdict

The corresponding proof in Part XXV passes review. It proves the stated unconditional Siegel--Walfisz property for beta_n=a_n(X)conjugate(G(n)), uniformly in 1<=X<=2U, finite-order cubic twists of logarithmic conductor, norm-twist heights of logarithmic size and the stated polynomial-size original masks. All A,B,C,D are fixed before the implied constant is chosen. No angular-character or Q assertion is used.

It verifies only this precise SW property. Rough support, prime-convolution structure, a corrected full Gram estimate and a complete detector tail do not follow from it.

#### 1. Actual finite-conductor extension of the Gauss inputs

A cubic finite-order Hecke character over the Eisenstein field has a Kummer representative R that is cube-free after removing cubes. Away from 3 its nonzero valuations are 1 or 2 at ramified primes. The class number is one, and the ramified 3-adic/unit alternatives form a fixed finite collection. Consequently NR is at most a fixed multiple of the square of the conductor norm. This is a finite-order statement; it does not concern arbitrary angular modes.

The source's exact residue and convexity estimates permit this R. The moving squarefree part ua remains disjoint from R after the actual character zeros are imposed. An exponent-two part in R may kill the pole, which only improves its bound. All remaining factors from R, its coprimality removal and its Gauss norms have a fixed polynomial cost in NR. The Type II CRT character and common coefficients do not change. Thus the extension (2) and unweighted estimate (3) are valid with a logarithmic cost in the stated conductor range. Their constants have fixed polynomial seminorm dependence. Norm twists with logarithmic height and the later logarithmic smoothing widths preserve that class.

#### 2. Small cutoff

The actual vanishing of G(n) off squarefree n forces d,m squarefree and coprime in the divisor expansion. Conjugating its exact CRT formula gives (4), including the essential cubic cross character. Freezing d leaves the source's genuine long-row sum with numerator Rd and its original mask.

The two d weights are respectively (Nd)^(-1) and (Nd)^(-1/4). Ideal counting gives the logarithmic first sum and X^(3/4) second sum. This proves U^(5/6)+U^(1/2)X^(3/4), up to the inherited small and logarithmic losses. For X<=U^(1/2) its exponent is at most 7/8 plus a sufficiently small loss. All ramified and K zero extensions remain intact.

#### 3. Large cutoff and exact boundary

On the actual test support n>1, the full divisor sum of mu is zero. The complementary formula (6) is therefore exact. After freezing m, its squarefree support supplies precisely the squarefree moving numerator required by the signed Mobius--Gauss bound; the true mu(d) sign has not been discarded.

Summing m up to 2U/X gives the two expressions U X^(-1/6) and U^(11/10)X^(-3/10). Throughout X>=U^(1/2) their largest exponent is 19/20. The fixed masks of norm at most U^C are paid by choosing the initial epsilon sufficiently small in terms of C.

The sharp d boundary cannot simply be treated as a fixed smooth test. The manuscript correctly smooths only a relative logarithmic-width band at d about X. Per m, elementary lattice counting bounds its number of d by O(delta X+sqrt(X)). Counting the actual (d,m) pairs, rather than asserting a false bounded divisor multiplicity for n, gives O(delta U log U+U X^(-1/2)log U). Coprimality restrictions only reduce this absolute discrepancy. This establishes (8).

Choose the logarithmic-width exponent after D. Its derivative costs remain logarithmic. Both strict power margins absorb every resulting fixed log loss; the boundary main error is made smaller than U(log U)^(-D). This proves the uniform sharp-cutoff assertion. If the cutoff passes the support endpoint, the coefficient vanishes for all supported n>1.

#### Exact remaining boundary

The two representations used are the original a_n(X) and its exact complementary divisor sum. The result therefore concerns the unchanged detector column, not an optimized replacement. The source's additional roughness and prime-convolution hypotheses have not been established by this argument. No corresponding gain for its full corrected dispersion form is certified here.


## C. Genuine inverse off-balanced cubic quadratic form

### Independent audit: the genuine inverse's off-balanced cubic quadratic form

The corresponding off-balanced proof in Part XXV C passes independent review. The relevant complete paragraphs of the pinned September 25 `dispersion.tex`, and its actual `outer-extension` bound in `background-type1.tex`, were reread.

For each fixed 0<delta<1/2 it gives some kappa>0 in the stated range B^(1+delta)<=A<=B^(2-delta), uniformly in the genuine inverse cutoff 1<=X<=2B:

    sum_a W(a/sqrt A) |sum_n,sf a_n(X)w(Nn/B)bar(chi_n(a))|^2
      << A B^(1+epsilon)+A^(2/3)B^(5/3-kappa).

Here chi is the source's cubic symbol. The n column is squarefree; the a sum is not assumed squarefree. Fixed cubic column twists are allowed. No Q assumption is used. The full detector's other power classes, balanced range and noncubic target twists are outside this assertion.

#### 1. True-coefficient power cancellation

The already checked all-cutoff proof has strict 7/8 and 19/20 smooth exponents. All its finite decomposition, test and fixed finite-conductor dependencies are polynomial in finitely many seminorms and parameters. Taking the boundary smoothing width to be V^(-eta), rather than a log-power, yields the displayed discrepancy V^(1-eta)log V+V^(3/4)log V. Choosing eta against every polynomial cost, then a smaller conductor/height window and sufficiently small initial mask losses, gives (2) with positive constants. This is an existence assertion and does not provide their numerical values.

On (n,q)=1 with q squarefree, both identities in (3) are exact. They preserve the actual sharp cutoff and Gauss CRT factor. The new character is cubic and its conductor is bounded by the stated small product. A cutoff outside the surviving norm support contributes zero and creates no missing endpoint case. Thus the forced-divisor version applies uniformly to the genuine beta_(fln), including a principal frequency twist.

#### 2. Source restrictions and the large divisors

With beta_b=a_b(X)bar(G(b))w(Nb/B), the identity beta_b G(b)=a_b(X)w(Nb/B) holds exactly on squarefree support. The source's Poisson formula with d=1 therefore applies to this unchanged coefficient. Its common-divisor CRT and zero-frequency cancellation do not use roughness, a prime convolution or SW.

The large-f paragraph uses positive divisor inversion, divisor bounds and the actual outer cubic sieve only. It bounds each divisor dyad by AB plus Q0 F^(-2/3), up to arbitrarily small powers. In this application H=B^2/A>=B^delta, so the AB term is smaller than Q0 by H^(-1/3). Its removed artificial diagonal has the same margin. The extra fixed exclusions can be retained in the coefficients or treated by their finite masks; they do not introduce a coefficient hypothesis.

For small f, the finite l inversion is applied to the displayed Poisson expression, not to a false Poisson identity on artificial noncoprime pairs. Mellin separation produces precisely (6). Its benchmark ratio (7) was recomputed from amplitude AF/(MB), J=kHM/F^2 and B'=B/(FL). The resulting f,m weights are summable.

The source outer-extension bound is valid for full nonzero frequency rows and squarefree n coefficients. Its three ratios to J^(1/3)B'^2 are exactly those stated. Summing the l dyad gives the three claimed saving factors. Here A>=B^(1+delta) and H<=B^(1-delta) are stronger than the coarse inequalities used in that source reduction. No use of the source's restricted final dispersion theorem is required.

#### 3. Every large primitive frequency

The actual factorization h=zeta lambda^i p q^2 j^3 has bounded multiplicity, with coprime squarefree p,q. The cube part is kept as a common unit mask. Fixing q or p and applying the ordinary cubic sieve gives the respective three ratios in Section 3.

When P dominates Q, the strict PQ^2<=(B')^(1-delta/2) range and the fixed exponent separation give a positive gap in each ratio. The reversed case is analogous. Near equality, the ordinary all-character sieve is applicable to the true primitive characters, with conductor O(PQ) and bounded multiplicity. Its second ratio is

    (PQ^2)/B' * (P/Q)^(2/3),

so it has a fixed gap when the near-equality width is chosen below the delta margin. Its first ratio saves on the chosen positive primitive-frequency threshold. Hence neither exceptional limiting configuration requiring prime-convolution input occurs here.

#### 4. Small primitive frequencies, including cube rows

In the remaining actual separated form the twist conductor is bounded by O(FLPQ). The inverse fm has the same radical support as f and does not cost F^2 in the conductor; the two possible cubic exponents simply distinguish the f and m portions. The cube divisor and other unit masks have polynomial norm and remain within the already fixed mask range.

The forced true-coefficient bound applies to every inner sum. It remains valid at p=q=1, since beta retains its Gauss phase; those cube rows are not discarded as a main term. Their dyadic ratio is exactly (B')^(-2c2)P^(2/3)Q^(1/3), bounded by (B')^(-2c2+2theta/3). Counting the genuine cube parts restores the benchmark with the already summable weights (7).

The revised order of constants is noncircular: first fix the power-cancellation window and its saving, next its forced-divisor saving, then the primitive threshold and the small f/l/transform ranges within that fixed window, and finally the original sieve losses. All transform tails retain their arbitrarily rapid decay. Taking kappa below the resulting finite list of positive gaps proves the asserted bound.

#### Exact bearing

This is a positive quadratic-form gain for the genuine finite inverse, not only a separate linear Gauss projection. It does not give an arbitrary-coefficient large sieve, a balanced estimate, or the missing full detector decomposition. The squarefree column and the cubic nature of the allowed fixed twists are indispensable in the proof as stated.

Pinned source:
https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dispersion.tex .

## D. Complete-column true-inverse off-balanced form

### Independent review: all-column true-inverse off-balanced form

#### Decision and scope

The proof in Part XXV D passes independent mathematical review, using the already audited squarefree-column theorem and its actual inverse-Gauss input. For the original finite inverse a_n(X), the cubic residue symbol, a fixed finite cubic column twist, smooth annular weights, and any fixed 0<delta<1/2, there exists kappa>0 such that the full-column quadratic form is bounded by

    A U^(1+epsilon) + A^(2/3) U^(5/3-kappa),

uniformly for U^(1+delta)<=A<=U^(2-delta), U>=2 and 1<=X<=2U. All exponent-two and cube layers are included. No Q input is used. The strict off-balanced range and the cubic twist restriction remain.

#### 1. Necessary uniformity is proved, not assumed

The squarefree theorem is extended explicitly to a common hole ideal K of norm at most V^C, with C fixed before the proof constants. In the original exact pair decomposition, a common hole only forces (fl,K)=1 and leaves a common (n,K)=1 column mask. It changes neither the primitive pair character nor its Poisson modulus. The large-f/l and large primitive-frequency bounds allow those masked coefficients. In the small primitive-frequency part, the previously established genuine inverse-Gauss power bound already allows a polynomial common mask, with the exponent range fixed before its saving. Since B'=V/(FL)>=V^(1-2eta), the combined masks still have a fixed polynomial norm in B'. This proves the uniformity required in (2), without introducing a moving conductor into a formerly fixed constant.

#### 2. Exact complete-column decomposition

The decomposition n=a b^2 c^3 with squarefree coprime a,b is unique, even when c shares their primes. Writing q=rad(bc), g=(a,q), and a=g v gives g|q, (g,b)=1, v squarefree and (v,q)=1. Conversely these conditions reconstruct the original columns. Hence rad(n)=qv and the finite inverse identity

    a_n(X)=sum_(e|q) mu(e) a_v(X/Ne)

is exact for every cutoff. There is no truncated-convolution approximation.

The cubic character factorization retains the actual zero mask:

    chi_n(a_row)=chi_v(a_row) chi_g(a_row) chi_b(a_row)^2 1_(c,a_row)=1.

After freezing b,c,g this extra row factor has modulus at most one and may be discarded in the positive norm. It is not dropped from a signed identity. The fixed cubic twist factors similarly; the smooth test remains exactly w(Nv/V), with V=U/(Ng Nb^2 Nc^3). Minkowski therefore applies to genuine complete blocks. The common hole satisfies Nq<=Nb Nc<=sqrt(2U).

#### 3. Long free columns and summability

For V>=U^(1-delta/4), the squarefree theorem applies with buffer delta/4 and a fixed polynomial hole range. The upper range inequality follows from

    (1-delta/4)(2-delta/4)>=2-delta;

the lower one is immediate. The diagonal norm sums with b-power -1 and c-power -3/2; the former is logarithmic and the divisor choices cost arbitrarily small powers. The saving terms have b-power -5/3+kappa_sf and c-power -5/2+3kappa_sf/2. Shrinking kappa_sf below 1/6 leaves both strictly summable, including all divisor-small perturbations. Their total is at most A^(1/3) U^(5/6-kappa_sf/2+epsilon).

#### 4. Short columns and the unit

For V below V0=U^(1-delta/4), the ordinary squarefree-column/full-row cubic bound gives the norm terms sqrt(A V) and A^(1/3)V^(5/6). Its extra A^(1/3)V^2 squared term is absorbed when A>=V, which holds here. The inequality V^(5/6)<=V0^(1/4)V^(7/12) yields convergent b- and c-powers -7/6 and -7/4. The resulting cross norm is at most A^(1/3)U^(5/6-delta/16+epsilon).

The scales V in [1/2,2], including v=1, are treated directly by the finite column count and the O(A) weighted row count. The false large-cutoff vanishing assertion for the unit is never used. Combining all positive norms and squaring gives any sufficiently smaller kappa than min(kappa_sf,delta/8). The sieve and divisor epsilons are chosen last, so the gain is strict.

#### Consequence

The former squarefree-column restriction is removed for this specific true inverse coefficient. This is not an arbitrary-coefficient saving or a balanced detector-tail estimate. The character throughout is the source cubic residue symbol; a general fixed sextic or quadratic target twist has not been included.


# Review of Part XXVI: the actual coupled residue

## Independent review: the actual coupled pole of the complete cubic core

### Decision and exact object

The coupled-wall proof in Part XXVI passes independent review. For eta=1 and the actual nonunit cubic good core u=epsilon v1^2 v2^4, it extracts the genuine pole q=x+y=1 from the original triple Mellin identity. All six units, all physical n/a, the two actual marker conventions, both first-scale transforms and the original finite compensated slot operator are retained. The resulting coupled residue satisfies O(Z^(-37/192+epsilon_loss)) at the original leading geometry, with no Q input. The entire shifted q contour remains in the exact identity. This residue is not identified with the previously defined first nonpolar remainder, and the bound gives no complete-cubic improvement by itself.

### 1. Genuine extraction and complete convergence

The pinned original source's exact Poisson identity supplies the three Mellin weights, q_u^(-t), and the full scalar Euler identity. At an unramified prime the numerator (3) is the original complete local polynomial. Removing (1-P^(-q)) cancels its genuine leading D W=P^(-q). The remaining term from this cancellation is bounded by P^(-q-x)+P^(-2q); the other monomials and R are strictly summable in the stated box. The denominators 1-D and 1-R are nonzero there. The finite selected factors are treated without any H_p or G_p division.

At x=3,t=2, moving q from 6 to 1-delta0 with 0<delta0<1/4 is legitimate. The local product after the zeta(q) extraction remains normally convergent along the shift. Since v1v2 is nonunit, every character has a genuinely ramified good prime and is nonprincipal, so no y=1 pole is crossed. The inverse L(x) is on its absolute line. On the new q line, the functional equation and the complete ramified table give a v1 prime weight O(P^(-3/2+2delta0)); the v2 weight is smaller. Hence the u sum is normally convergent, including small divisor losses. Original Mellin decay handles all heights and the horizontal contour sides. This establishes a residue plus the full remaining contour, rather than imposing a diagonal equality on independent height variables.

### 2. Exact functional equation on the residue

On q=1 the equality y=1-x is a complex equality. Applying the genuine finite-order Hecke functional equation, with the fixed S factors restored and removed explicitly, cancels the displayed L(x,bar chi_u) denominator exactly. The remaining conductor power has exponent x-1/2, with good conductor v1v2 and only finitely many bad conductor possibilities. The root number is retained; taking its modulus later costs one. The gamma ratio is holomorphic for positive real part of x, including its harmless zeros at positive integers. The deleted factors have nonzero denominators on this positive strip and only fixed height costs. Thus moving this two-dimensional residue through the former L zeros is justified by an actual identity, not a reciprocal-L bound.

### 3. Full ramified arithmetic and both markers

The original local family table was reread. For j=2,4 the zero extension sets D=W=0. The shared-divisor term on q=1 combines with 1-R/P to give (1-R)/P, while the odd entries are respectively plus and minus a_p rho^(-3)P^(3/2-3x). This proves (7) and its first-flat version (8), without deleting physical odd layers.

In the original marked operation, the t_completed=0 family is (1-V)^(-1), whose contribution after the ramified normalization is exactly one. The compensated operation therefore gives P^x[(1-P^(-1))H_p-1], including its rescaled term. The core operation removes precisely R(1-P^(-1))/[(1-R)(1-V)] from the raw marked local factor. After normalization this is the subtraction in (10). These formulas hold through zeros of H_p and use no ratio by it. At unramified selected primes the raw leading term -D becomes bounded after multiplication by P^x; all the remaining table monomials are smaller in the final box. The first-flat multiplier 1-R preserves these conclusions.

### 4. Residue contours and all prime rows

The exact unselected ramified convergence conditions are 2 Re(t)-Re(x)>-1/2 and Re(x)+Re(t)>1. The prescribed path first lowers x at t=2 and then lowers t at fixed x=5/8+delta; both conditions hold throughout. The unramified corrected product is normally convergent along this path, and t stays strictly above the zeta(6t) pole. At the final box the v1 local absolute weight is O(P^(-1-4delta)) and the v2 weight O(P^(-7/4-6delta)). Fixed constants per prime are harmless with this strict room. All six original unit factors retain their actual character phases.

### 5. Every forced slot is paid

The slot supports are disjoint and finite in number. For a slot prime not dividing u, the local selected factor is bounded and elementary prime-ideal counting costs P_i^t. For a slot forced into v1, use G_p=O(P^x), not H_p or a divided quotient. Including q_u^(-t), the conductor power, and P^(t-1), the summed cost is P_i^(2 sigma-zeta-1/2)=P_i^(3/8+delta). For a prime forced into v2 it is P_i^(2 sigma-3 zeta-1/2)=P_i^(-3/8-delta). Hence the full compensated slot operator costs at most P^(3/8+delta), while the remaining row primes still have the convergent products above. No ramified selected prime has been treated as unramified.

The residue scale is exactly X^(1/2-t) Z^(x+t-1)Y^(-x). At sigma=5/8+delta,zeta=3/8+delta this gives the displayed bound X^(1/8)Y^(-5/8)P^(3/8), with the explicit delta loss absorbed after choosing delta against the final epsilon. Substituting 17/48,23/48,1/6 gives -37/192 and margin 1/192 below -3/16. For each first-scale transform, its reciprocal angular Euler factor is absolutely convergent throughout the path, since 6 Re(x+t)-4>1; this uses no zero-free assertion for an angular L-function.

Pinned source: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex , the labelled exact Poisson identity, local family table, scalar Euler factorization and quotient-free selected operation. The shifted surface is an essential remaining part of the original probe.


# Supplementary source review: the user’s noncubic-twist theorem

## Independent audit of the user's noncubic cubic-Gauss twist result

### Verdict and attribution

The main qualitative theorem in the user's [fixed source](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d4f8dfe5b487cfa2cafb606bb067b7e8bfe39e66/reports/20261011_qrh_selection_bridge/CUBIC_NONCUBIC_TWIST.md) is correct: a primitive finite residue character phi modulo a primary r prime to 3, with phi cubed nonprincipal, gives a normalized cubic-Gauss Dirichlet series holomorphic throughout Re(s)>1/2. Fixed common holes and the conjugated coefficient version are also valid. This is the user's mathematical input. It does not settle a row with an additional lambda-ray multiplier, supply moving-conductor/height bounds, or prove a full negative-unit ordered residue assertion.

One cubic-symbol notation correction is necessary in the introduction and the corresponding final paragraph of the user's referee file. Under the standard Jacobi-symbol convention used in the cited source,

    theta_w(4)=(4/w)_3=(w/4)_3=(w/(-2))_3^2,

not (w/4)_3 squared. The later actual CRT formula written with theta_w(4), and its expression in terms of the chosen xi at the norm-four prime, are correct. This correction does not alter the qualitative no-pole result because all the indicated fixed factors are cubic.

### 1. Source hypotheses and finite transform

Dunn--Radziwill, arXiv:2109.07463v3, Section 5.3, Corollary 5.1 and Proposition 5.1 were independently read. Their input is a periodic sequence at a primary modulus r prime to 3, with finite Fourier transform supported on units. A primitive multiplicative residue character satisfies this condition, including at nonsquarefree r. This does not assert that the character induced on primary ideal generators has exactly the same Hecke conductor.

Use the general finite transform (5.42), not the later cubic-only formula. At zero it gives a nonzero fixed scalar times the sum of phi-hat(d) times the conjugate cubic Jacobi character rho_r(d). Primitive Gauss scaling makes this proportional to the group sum of the conjugate of phi*rho_r. Since rho_r cubed is principal, this group sum vanishes whenever phi cubed is nonprincipal.

The completed source series consequently has its only possible pole removed. Lemma 5.3 expresses the uncompleted source series as that entire completion times reciprocal Gamma factors, which are entire. There is no additional independent zero-index term in the nonzero S-supported Dirichlet series.

### 2. The denominator is retained correctly

Expanding the actual source indices mu=lambda^(-3)e f^3 gives

    D(s)=3^(5/2+3s) phi(lambda) R_phi(s)
                    L_(3r)(3s-1/2,phi^3).

The squarefree e coefficient and unrestricted f factor are exactly those in the source theta expansion. Their multiplicativity does not require (e,f)=1. The direct factorization is initially absolutely convergent for Re(s)>1. The partial L-series is defined by its primary-generator values and deleted primes, without an incorrect exact-conductor identification. For Re(s)>1/2 its argument has real part greater than one, so its Euler product is holomorphic and nonzero. Also phi(lambda) is nonzero. Dividing proves the claimed continuation in that open half-plane. Replacing s by u-1/2 gives the unnormalized region Re(u)>1 and removes its candidate at 4/3.

### 3. Fixed holes and conjugation

For d squarefree dividing a fixed hole radical and coprime to 3r, the exact Gauss CRT relation inserts bar(chi_d) in the residual normalized series. Its zero extension is precisely the necessary (c0,d)=1 mask. The product phi*bar(chi_d) is primitive modulo rd, and its cube remains nonprincipal on the original r-component. The finite inclusion-exclusion therefore proves the hole version. Conjugating the Gauss coefficient reverses this cubic factor to chi_d, as stated. No uniform estimate in the hole or conductor follows just from this finite identity.

### 4. The norm-four calculation and its orientation

The script was inspected and independently executed. All sixteen residue classes, multiplicativity, primitive support, both additive conventions, all three cubic character projections and fixed-mod-2 fiber cancellations passed with integer arithmetic. Its original-character Gauss sum is 4 psi(h); the literal trace-character sum is -4 psi(h). The prime norm is four, the residue modulus (4) has norm sixteen, and the distinction is maintained.

CRT with a good squarefree w gives exactly the displayed factor psi(w)*theta_w(4) and the corresponding h characters. The bad quadratic character remains after either possible cubic factor. This is a finite identity and does not remove a separate lambda-ray dependence.

For a concrete check of the notation correction, take the primary prime w=-2-3 omega of norm seven. In O/(w), omega=4 modulo 7, so (4/w)_3=4^2=2=omega^2. In O/(-2), w=omega and (w/(-2))_3=omega. Therefore (w/4)_3=omega^2, while its square is omega. Thus the extra square in the introduction cannot be used with the standard denominator-Jacobi convention. If a different primitive cubic character modulo 4 were intended, it would have to be separately defined; the unambiguous correct expression is theta_w(4) or (w/(-2))_3^2.

Primary source: https://arxiv.org/html/2109.07463v3 , equations (5.7), (5.42), (5.44)--(5.52), and Lemma 5.3. The argument avoids extending the cubic-only hypothesis of Lemma 5.4.


# Review of Part XXVII: actual lambda cusps and moving cubic levels


## A. Independent mathematical review

### Independent audit: norm-four noncubic twists across all fixed lambda cusps

#### Decision and attribution

The proof in Part XXVII A passes independent review. It extends the user's d4f8dfe prime-to-three noncubic result by a new finite translated-theta constant-term calculation. For the primitive norm-four character psi times any cubic character modulo 4, any fixed odd multiplicative residue factor, and an arbitrary fixed multiplicative lambda-ray factor on primary generators, the normalized cubic-Gauss series is holomorphic for Re(s)>1/2. The conjugated version and the stated fixed finite lambda-function corollary also hold. This is qualitative for fixed data; no moving-level, height-uniform or complete signed-row estimate is proved.

#### 1. Exact periodic theta construction

The multiplier Phi is supported on the primary coset and retains the original zero extensions. Its 2-part is primitive modulo 4, so its finite Fourier transform is supported on 2-units and proportional there to the conjugate character. Additive CRT fixes the other components independently. The translated theta sum uses the shift lambda^2 t/L with the original additive convention. Thus Fourier inversion multiplies the source coefficient at mu by Phi(lambda^3 mu), not Phi(lambda^4 mu). Primary support selects exactly mu=lambda^(-3)e f^3 with e,f primary and e squarefree. The source coefficients give 3^(5/2)tilde_g(e)|f|. The infinity constant is killed by Phi(0)=0.

#### 2. Every lambda-cusp constant term vanishes

For fixed non-2 Fourier coordinates the reduced denominator has 2-valuation two and fixed norm. Its normalizing unit and lambda cusp are fixed. At a rational cusp the inverse group action gives height 1/(q_cF v); a constant term has no horizontal additive phase.

The source's three exact cubic multiplier formulas have only cubic dependence on the 2-unit variable. Such dependence factors through modulo 2. In the middle cusp, the actual source congruence b=0 modulo its auxiliary modulus makes a-u0 b agree locally with a, so no extra norm-four character is introduced.

The revised lift argument resolves the higher-lambda issue explicitly. When e=v_lambda(c_F)>=2, the fixed Fourier coordinate fixes a modulo lambda^(e+2), sufficient for the supplementary factors modulo lambda^4. When e=1, it fixes modulo lambda^3 and a permitted lift t -> t+Lk supplies the missing lambda^3 coefficient modulo lambda^4; CRT can keep the other required residues fixed. This changes the theta argument by its genuine period lambda^2 k. The source b congruence then fixes the middle-cusp numerator as well. At e=0 the denominator has no lambda factor and the remaining source cusp and odd residues are already fixed. No circular assumption about an ever-enlarging source modulus is used.

The complete constant contribution on each fixed non-2 fiber is therefore a common cusp constant times sum_(t2 unit mod4) bar(chi2(t2)) K(t2 mod2). Its sums over the four-element fibers above each unit modulo 2 vanish, because the quadratic norm character is nontrivial on 1+2O modulo 4 and the cubic character is trivial there. Every cusp constant is thus killed independently. With finitely many cusps, the remaining Fourier terms decay exponentially in 1/v, while the infinity expansion decays exponentially in v.

#### 3. Entire Mellin numerator and exact quotient

The Mellin transform of the translated sum is entire. The Bessel Mellin identity expresses its Dirichlet numerator through reciprocal Gamma factors, again entire. In the original absolute half-plane its exact factorization is

    D_Phi(s)=3^(5/2+3s) R_chi(s) L_deleted(3s-1/2,chi^3).

There is no evaluation of a lambda-ray character at lambda. The multiplier was applied to the integral primary index e f^3, so multiplicativity gives chi(e)chi(f)^3 directly, without requiring coprimality between e and f. For Re(s)>1/2 the final partial Euler product converges absolutely and is nonzero. Division proves the claimed continuation and agrees with the initial series.

A fixed arbitrary function on the finite primary lambda-unit group can be expanded in its multiplicative character basis. Each character has its own Euler quotient; taking their finite sum gives the additional corollary. A nonmultiplicative finite function is not itself inserted into a putative Euler product.

#### 4. Exact finite check and limitations

The norm-four fiber checker was inspected and independently run. It returned ALL_PASS for all three psi*rho^j characters, nonunit Fourier support and all three unit-fiber sums, using integer arithmetic in Z[zeta_12]. This verifies the finite orthogonality, while the cusp identification and continuation follow from the separate proof above. The result does not apply the source's prime-to-three Proposition 5.1 at an illegal lambda-divisible modulus.

The input being continued is a specified one-variable Gauss series. Identifying a complete physical signed row with it, obtaining conductor/height-uniform estimates, and justifying other infinite contour operations remain separate tasks. The user's original prime-to-three result and its exact coefficient-factorization insight retain their attribution.

Sources: the user's commit d4f8dfe5b487cfa2cafb606bb067b7e8bfe39e66, and the original pinned QRH source's translated theta construction, three cusp multipliers and coefficient expansion. The source theta coefficients and Bessel normalization are those of https://arxiv.org/html/2109.07463v3 , Section 5.

#### Frozen publication snapshot

The self-contained qualitative snapshot is `noncubic_twist_all_lambda_cusps_qualitative_frozen.md`, SHA-256 5206c71a1d9cc175437247287316bce28ce8fd92010c1fbaea4372f9319d5b78. It contains exactly the reviewed Sections 1--6 and their unchanged proof, with the initial status updated. The later exploratory Section 7 in the older working file is not part of this certificate or the publication snapshot. Quantitative polynomial-height control is supplied instead by the separately audited moving-cubic theorem.

## B. Independent mathematical review

### Independent audit: quantitative moving-cubic control through the actual lambda cusps

#### Decision and precise theorem

The proof in Part XXVII B passes independent review. For a fixed defining period L whose 2-part is exactly 4 and whose norm-four character is primitive quadratic times cubic, arbitrary fixed odd and multiplicative lambda-ray factors, and moving good squarefree u coprime to 6L, it proves
|R_u(sigma+it)| <<_epsilon (NL)^(3/4)U^(1/4)(1+|t|)^3,
sigma>=1/2+epsilon.
The moving cubic chirality beside normalized G is bar(rho_u); the conjugated theorem reverses both. Smooth norm sums have B^(1/2+epsilon), common moving holes cost M^epsilon, and a fixed nonmultiplicative lambda function costs its finite character-expansion l1 norm. The actual full period NL is paid explicitly. No Q is used and no whole-sector estimate follows from this lemma alone.

#### 1. Original finite theta source, not an out-of-domain functional equation

The theta multiplier is Phi_u(lambda^3 mu), with all primary and original zero masks. Its infinity coefficients are therefore the actual lambda^(-3)*a*b^3 coefficients. The norm-four primitive Fourier fibers cancel every constant term at every lambda cusp by the separately audited qualitative proof. Adding moving nonzero good Fourier coordinates does not change that fiber argument because the other CRT coordinates are held fixed. Constants are removed only after the common-denominator fiber sums, not individually at each h0.

The original fixed-source cusp construction and local table were reread directly. For fixed h0 and the actual sector of u, the reduced denominator is c0*u, Nc0<=NL. The source congruences fix the bad multiplier and additive phase independently of the moving hp. Its conjugate multiplier contributes chi_p(a)^(-2), with a=sigma_p hp. The Fourier coefficient of bar(rho_p)=chi_p^4 contributes P^(-1/2)gamma_4(p)chi_p(hp)^(-4). These exponents cancel. The inverse-variable sum is exactly c_p(lambda^4 mu), so each moving prime contributes P^(-1/2)c_p, retaining every unit-modulus scalar. This holds in all three actual bad cusp cases. There is no extra choice of inactive primes or exponential-in-omega(u) summation.

#### 2. Exact Mellin level powers and the full dual majorant

Reflection sends height v to 1/(Nc0 U v). Its undifferentiated Mellin transform therefore contributes (Nc0)^(1-2s)U^(1-2s), multiplied by the Fourier factor U^(-1/2). The resulting U^(1/2-2s) in (9) is correct. The matched two Bessel gamma pairs have polynomial vertical ratio; this is not the differentiated angular reflection formula.

For each of the three true cusp coefficient series, the complete squarefree/cube local majorant at z=1+h is (1+P^(-z))/(1-P^(1/2-3z)). A moving prime replaces it by at most 1+P(T_p-1)=1+O_h(P^(-h)). Its product is U^eta for any prescribed eta>0, with the appropriate parameter-dependent constant. The lambda progression and every cube layer converge absolutely. The fixed additive phase has modulus one. Normalized Parseval bounds the bad Fourier l1 mass by sqrt(NL), and Nc0<=NL supplies the remaining period power. This proves the uniform left boundary (NL)^(3/2+2h)U^(1/2+2h+eta). The original right line is uniformly absolutely bounded.

#### 3. Uniform interpolation and attribution

The entire split Mellin representation gives fixed-data finite exponential strip growth, sufficient for the maximum principle. The proof correctly uses the user's 7a7c2dec conductor-balanced argument with denominator (s-2)^3 and the cosine barrier. The barrier controls horizontal sides and does not enlarge vertical bounds, so fixed-data interior constants do not pollute the uniform final estimate.

With h=eta=epsilon/4, the exact deficits at sigma=1/2+epsilon are
(5epsilon/4+3epsilon^2/8)/(1+epsilon/2)
and
(epsilon/8+9epsilon^2/16)/(1+epsilon/2)
below the desired bad-period exponent 3/4 and moving-cubic exponent 1/4. Both are strictly positive. The left height degree is 2+epsilon<3. The independently inspected and rerun exact checker returned ALL_PASS for these identities. This computation verifies the rational ledger; the source and analytic arguments were separately checked.

The user's general-character growth theorem remains their result, with its own A(M) mask cost. The improved U exponent here comes from the additional actual j=4 Ramanujan transform, and the lambda extension comes from the separate original-cusp construction. Those distinct inputs are accurately attributed.

#### 4. Correct Euler quotient and moving masks

The infinity coefficient identity retains L_deleted(3s-1/2,chi_0^3). There is no chi_0(lambda), since Phi is evaluated at lambda^3 mu. The Euler product and its inverse are uniformly absolutely bounded in the target half-plane. For larger real parts the proof returns to the original R_u series, whose norms are at least one, rather than incorrectly extending a D_u boundary estimate.

Finite lambda functions are first decomposed into multiplicative characters, each with its own Euler quotient. Their l1 coefficients are paid. For common moving holes, the exact finite CRT identity replaces u by ud and contributes d^(-s); its net d exponent is 1/4-sigma<=-1/4-epsilon, giving M^epsilon. These steps do not assume an unproved uniform bound for arbitrary moving noncubic characters or reverse the moving chirality.

Primary sources: the pinned original QRH cusp matrix/multiplier and local j=4 reflection table; https://arxiv.org/html/2109.07463v3 , Section 5 and Appendix A; the user's d4f8dfe qualitative noncubic theorem and 7a7c2dec quantitative interpolation argument. Only unconditional theta and finite-transform identities are used.



# Review of Part XXVIII: genuine cubic density and complete transfer


## A. Independent mathematical review

### Independent audit: the cube-free cubic pair Gram and genuine inverse detector

#### Decision

The true inverse detector in Part XXVIII A passes independent review. For the stated fixed finite-order twist of the canonical cube-free cubic family Na<=M, it proves the actual off-diagonal fixed-row Gram bound
sum_(j!=i)|G_ij(U)|^2 << (MU)^epsilon (1+T)^C [UM+M^2 U^(1/3)]
and the genuine zero-detector consequence R(M,T;5/6)<<M^(9/14+epsilon)(1+T)^C. No Q is used. The family remains ordered by its canonical cube-free index, not its radical conductor. Only bounded smooth full-frequency coefficients are used in the Poisson step; no arbitrary full-column sieve operator is asserted.

#### Local quotient and conductor verification

At each prime of the fixed row, the varying exponents 0,1,2 give only divisor-small many assignments. Equal nonzero states cancel as characters but retain their original unit mask. Opposite nonzero states give primitive cubic differences, not cancellation. Once these fixed primes are removed, the free varying index is still cube-free with its actual canonical norm at most M, and its primitive support is disjoint from the remaining fixed conductor. Bounded primitive multiplicity follows from the recoverable good-prime exponents; the diagonal and the fixed possible principal row are treated separately.

The local conductor inequality f*g^2 <= constant*f_i*f_j <= constant*M^2 is correct: cancellation pays two conductor powers through g^2, a crossed prime pays one through f, and disjoint support matches. A further block in the true primitive conductor is necessary and is explicitly retained. It never changes the cube-free index used in the sieve.

#### Poisson, common coefficients and all frequency powers

After the genuine common-unit mask is expanded at d|g, primitive Poisson has amplitude (U/Nd)/sqrt(Nf), dual norm scale J=Nf Nd/U, and exact amplitude squared times J equal to U/Nd. The zero frequency vanishes for the nonprincipal quotient. All normalized Gauss factors and fixed CRT phases are pure row scalars; the fixed dual character is a common frequency coefficient. The conductor ratio, chosen real parts of zeros, and normalized heights are separated by common compact-parameter Mellin/Fourier transforms with polynomial height seminorms.

Theorem 1.1 of de Faveri applies to both canonical cube-free ideal indices, giving K3(M,J)=M+J+(MJ)^(2/3). For the full bounded frequency column, h=h0*l^3 gives a real row zero mask, removable only inside the positive norm after freezing l. Its three Minkowski weights are l^(-3/2), l^(-3) and l^(-5/2), all summable. Thus the squared dual norm is J*K3(M,J), with only small losses. J<1 is handled by the actual nonzero Schwartz tail before clamping, not by invoking a sieve at subunit length. Complete dyad and divisor summation gives U*K3(M,max(1,M^2/U)); its middle M^2 term is absorbed into M^2 U^(1/3) for U>=1. This proves the announced Gram bound, including independently chosen bounded beta/height row parameters.

#### The real inverse coefficient and the detector

The coefficient remains a_n(X)=sum_(d|n,Nd<=X)mu(d). The Gamma-integral identity at an actual zero cancels the s=0 residue and detects a critical-line integral or one of its genuine n>X tail dyads. On a tail dyad, the common coefficient mass is O(U^(1+epsilon)). With the actual beta/height row weights, Halasz--Montgomery and Cauchy on each row's off-diagonal entries give
R U^(2b) << U^(1+epsilon)[U+sqrt(R U K3(M,max(1,M^2/U)))].
Solving this inequality gives U^(2a)+U^(4a-1)K3, where a=1-b; no inverse coefficient is replaced or chosen differently on different rows.

At b=5/6 the resulting tail is bounded by Y^(1/3)+M X^(-1/3)+M^2/X. The additional M^2 X^(-4/3) is smaller. Actual conductors are at most a fixed multiple of M, so the ordinary AFE, the same cube-free sieve and complete cube-layer separation give the critical-line L second moment O(M^(1+epsilon)(1+T)^C). Cauchy with the true inverse polynomial gives the unchanged first term Y^(-1/3)sqrt(M K3(M,X)).

At X=M^(19/14), Y=M^(27/14), the cross term gives K3(M,X)<<M^(11/7). The first term, Y^(1/3), and M^2/X are all M^(9/14); M X^(-1/3)=M^(23/42) is smaller. Dyad and height losses have the advertised epsilon and polynomial dependence. Counting one chosen zero per bad primitive row is legitimate; a total count may add the ordinary per-character height/logarithm factor.

Primary source independently checked: https://arxiv.org/html/2610.04045v1 , Theorem 1.1 and its definition of the n-th-power-free ideal family, with n=3. The new fixed-row argument uses its upper bound, not the source's final density corollary. This result alone does not establish a complete physical-probe estimate or exclude individual off-line zeros.


## B. Independent mathematical review

### Independent audit: complete cubic gain from the genuine pair-Gram density

#### Decision and retained scope

The proof in Part XXVIII B passes independent review as a full application of the separately audited cube-free cubic pair-Gram detector. It improves the previously defined complete nonprincipal cubic contribution to O(Z^(-271/32256+epsilon)). It retains every original unit, physical n and sixth-power layer, actual selected slot, original/core marker, both exact first flat operations and original finite compensation. The new density input is unconditional, while the physical buffered reciprocal-L step still assumes the user's finite-order Q with its original attribution. It does not reach -3/16 or control the whole probe.

#### Detector interval and exact exponents

On 1/8<=a<=9/50 the proposed X=M^x,Y=M^y satisfy 1<=x<=3/2 and Y>=X. The canonical cubic sieve is dominated by its cross term there. Substitution into the actual first-integral and tail expressions makes the first term, Y^(2a), and M^2 X^(4a-5/3) exactly M^Dp. The remaining M X^(4a-1) term is smaller by 1-2x/3. The original clamping and exponential tail remain legitimate for U>M^2.

The two D0-Dp identities in (7) were independently recomputed. The second numerator has the stated strictly positive Bernstein coefficients; the first factors into (1-4a)(108a^2-36a+5), positive on its interval. At a=1/6, Dp=9/14. No Q-free statement about an individual zero is inferred from this density bound.

#### Every slot and every smooth-column scale

The old proof's actual moment choices and its row exponent D0 are retained in the slot estimate. They are not silently replaced by Dp. For each genuine k>=1, the two restricted-row Holder powers are 1-1/(2k) and 1-1/(2k)-1/8, hence at least 1/2 and 3/8. Replacing only the real bad-row count by M^Dp therefore improves each old envelope by at least M^(-3Delta/8). Empty and tiny slots have no smaller row power. Fixed moments, prime-square branches, repeated-prime masks and common coefficients are unchanged.

This factor is uniform in the actual smooth s-scale, so it may be applied before the complete finite e integration and the genuine rowwise long-S Poisson tail. It improves the already proved all-S exponent J8 by 3Delta/8 without moving a convenient peak or changing the slot lemma's domain. The common compact c/s cutoffs and normalized q_D/P ratios are explicitly retained before pooling.

#### Complete physical transfer and tails

On the new interval, Delta<=1/20 and the stated lower bound on J8 give J8-3Delta/8>9/10. The bound Delta<=1/20 can also be checked directly after clearing its positive denominator: on the second interval the resulting cubic has Bernstein coefficients 22/3, 664/75, 6454/625, 36748/3125, all positive. The first interval reduces to a positive quadratic times 10a-1.

Consequently the full sixth-power a' sum remains strictly convergent, and the physical-square and external-flat exponents 4-6b-3(J8-3Delta/8) remain below -1 with large room. The original n0 factor, fixed divisor assignments and proper-subset compensation do not change. Actual unbounded ambient losses are absorbed by these strict powers and the original Gaussian/Schwartz envelopes. The high-M positive-frequency enlargement is made only after the valid high-M slot estimate; the small-M argument is left intact.

#### Exact maximum

The cutoffs, three balanced detector exponents, both rational differences in (14), and every displayed Bernstein coefficient were independently recomputed using exact rational symbolic arithmetic. The coefficients of PL and -PR are exactly those listed in the proof and positive on the specified intervals. Thus the new high-M maximum is -271/32256 at a=1/6. The inherited decreasing tail beyond a=9/50 is at most -4109/480000, smaller by 3203/20160000. The unchanged complete small-M bound -13/1440 is smaller by 101/161280. These calculations prove the global claimed exponent; no floating grid is used.

The actual balanced cube-completion-tail lemma is not an input here. No unsigned completion, angular Q, or unproved low-k estimate has entered this application.

#### Frozen proof

The mathematical version was read at SHA-256 0b77320539adf198d63977170342248b32342eac5276e02d3a0177f558f9dddc. Its status-only final version is SHA-256 4442e8b60a4adfda9a56a27afc246e75834d958b960494ab598d0c33da47f6d2. The proof, bounds and complete physical scope are unchanged.


# Review of Part XXIX: actual balanced inverse columns


## A. Independent mathematical review

### Independent mathematical review: the genuine shifted inverse on squarefree columns

The proof in `Section A of this Part` passes independent review in its stated finite-order Q, fixed positive real-delta interval, common-hole, norm-height and buffered-zero-box domains. It is an analytic input for the actual coefficient, not a matched coupled-contour or complete balanced estimate.

#### Exact squarefree Euler correction

The full ratio coefficient is b_delta=mu*N^(-delta), and restricting it to squarefree ideals changes its Euler factor to 1+(P^(-delta)-1)psi(p)P^(-s). Multiplying by (1-rz)/(1-z) produces exactly H_p=1+r(1-r)z^2/(1-z). Thus the displayed SF series is L(s+delta)/L(s) times H, not the bare quotient. H is normally convergent and bounded on every sigma>=1/2+h, uniformly in Im(delta); no nonvanishing of H is needed.

The removed actual SF local factor has magnitude at least 1-2P^(-1/2-h)>0, since good Eisenstein prime norms are at least 4 and the ramified norm-three prime is excluded. Its finite divisor product and reciprocal cost K^epsilon with constants depending on the chosen positive buffer. Forced squarefree divisors factor the actual coefficient exactly, retain the enlarged hole dK, and add at most d^epsilon. Nonsquarefree or excluded forced divisors give zero.

#### Global Q bound, including the principal row

The contour sigma=max(7/8,1-Re(delta))+rho is to the right of both possible numerator poles and denominator zeros. Principal reciprocal-L zeros at the denominator's pole are harmless, and the numerator pole at 1-delta is never crossed. The previously audited buffered log-L and two-constants argument supplies the subpower reciprocal estimate; the proof does not infer it from Borel--Caratheodory alone. On this contour the numerator is absolutely convergent. Mellin inversion proves the stated B^(max(7/8,1-delta0)+epsilon) estimate, with the genuine conductor/hole small powers and polynomial height costs.

The resulting logarithmic-window SW bound and sufficiently small polynomial-window power saving are valid only after the fixed mask exponent and all seminorm degrees are chosen. They are not uniform as Re(delta) decreases to zero. The forced-divisor version is at the real length B/Nd, with its explicit outside coefficient; a useful long length must be imposed when the application needs one.

#### Finite-height zero bins and the numerator conductor

For a nonprincipal row, the buffered reciprocal bound for the denominator at b+O(h) combines with degree-two convexity for the numerator. This gives the actual extra conductor exponent ((1-b-Re(delta))_+)/2+O(h), not zero in every bin. A bin starting at b=1/2 still needs its positive buffer for H. The height box includes all center shifts; truncation and rapid Mellin tails are treated separately. A principal row is not passed through this finite-box argument and is explicitly left to the preceding global bound.

The identity 1-P^delta=P^delta*b_delta(p) is correct but purely local. It neither erases the Gauss factor in a corrected column nor verifies the rest of the physical Euler product, root numbers, selected marks or remaining contour. No angular use of Q is authorized by this lemma.


## B. Independent mathematical review

### Independent audit: the balanced shifted-inverse Gauss quadratic form

The complete theorem in `Section B of this Part` passes review, conditional on the user's finite-order Hecke input Q in its recorded scope. The review includes the explicit short cubic numerator window.

The conclusion is a positive quadratic-form estimate for the actual squarefree column b_delta(n) G(n), Re(delta)=15/64, including A comparable to B. It is not an estimate for arbitrary divisor-bounded coefficients, the raw finite inverse a_n(X), or the full coupled physical remainder. Its small polynomial height and short-numerator windows are part of the theorem.

#### 1. Coefficient and zero-bin input

The squarefree series is exactly L(s+delta,psi)/L(s,psi) times H, with H_p=1+r(1-r)z^2/(1-z). I retained this correction, the exact deleted squarefree local factors, and the actual forced-divisor factor b_delta(fl). The latter is divisor-bounded; a nonsquarefree forced product vanishes. Every remaining free column has length B/N(fl), and retains its enlarged hole. No Gauss sum is erased from the theorem's column: the September-25 corrected Poisson formula cancels the Gauss sums itself and leaves beta=b_delta times the stated common twist and smooth weight.

The previously audited shifted-inverse lemma applies on buffered finite-height boxes. The numerator's convexity cost is C(psi)^((a-15/64)_+/2), where a=1-b. This cost has been preserved before squaring. Principal rows are excluded from the zero-bin argument and handled by the global Q contour to the right of 7/8. The numerator pole at 1-delta lies to its left; no principal residue is silently discarded.

The density parameter is the canonical cube-free index bound M, not the smaller radical conductor. The exact de Faveri curve 8a/(1+6a), on a>=1/6, is used with its already checked fixed-twist detector argument. The new true pair-Gram curve Dp is used only inside its audited interval. Both have the required polynomial height dependence. Common holes enter the reciprocal estimate, not a falsely hole-dependent zero-density family.

#### 2. Exact all-index gap

The original exact gap checker was rerun and independently checked the reductions. Both displayed Bernstein lists are positive and agree exactly. For a between 7/40 and 15/64 the gap is (6a-1)^2/[3(6a+1)], increasing there, with value 1/2460 at 7/40. Above 15/64 the minimum gap is 15/64-(7-4 sqrt(2))/6, and sqrt(2)>140/99 gives the stated positive rational lower bound. The Dp intervals have the stronger 1/200 margin.

Thus D(a)+2-2a+(a-15/64)_+ is uniformly at most 7/3-1/2460. For M=L^m, the gap relative to L^2 M^(1/3) is affine in m. Its two endpoint lower bounds are 2a>=1/4 and 1/2460. This proves a fixed positive power margin on the whole range M<=L, with a small enlargement M<=L^(1+eta_1) after paying buffers, density height costs, common-hole losses and Mellin heights. Unit-size families are handled separately by the global Q bound.

A short cubic numerator can be incorporated into the canonical index. At its finitely many prime factors, partition the exact local exponent states modulo three, retaining every unit mask when a component cancels. The reindexing is injective up to divisor-small finite states and enlarges the index by at most a fixed power of the short numerator norm. Taking its exponent small enough fits the same enlarged window. This verifies the additional xi=xi_0 chi_v assertion; it does not give an arbitrary moving finite-order twist theorem.

#### 3. Source Poisson and the near-balanced geometry

I directly reread the pinned September-25 `dispersion.tex` paragraphs from the exact Poisson formula through the large-common-divisor and large-l reductions. Their use here is restriction-free: these steps require coefficient divisor bounds and the ordinary cubic large sieve, rather than the source's separate roughness or prime-convolution hypotheses.

With the outer sieve divisor set to one, the exact scales are H=B^2/A, H'=H Nm/(Nf)^2 and amplitude A Nf/(Nm B). The fixed additive factor, reciprocal cubic argument h/(fm), common masks and finite Mobius inversion are retained. The unequal-pair zero frequency vanishes. The artificial equal pairs introduced during finite inversion are not assigned an unjustified Poisson identity.

Allowing A down to B^(1-eta) is legitimate in the large-f step: every removed divisor E>=B^lambda satisfies A>=B/E when eta<lambda. The two source costs relative to Q0=A^(2/3)B^(5/3) retain the gaps H^(-1/3) and E^(-2/3), since H>=B^d_0. In the large-l step the source upper bound on J acquires only B^O(eta). Its first cost still has a B^(-1/3+O(lambda+eta)) gap, and the other two retain the l^(-2/3) and l^(-1) gains. The stated order of small constants pays all of them.

After both removals, L>=B^(1-2lambda), while the genuine retained Fourier frequency is at most B^(1+eta+small truncation)/Nf. This fits L^(1+eta_1) once the widths are chosen in the stated order. The short reciprocal numerator fm is included in the same allowance, rather than placed in an unproved fixed-twist constant.

#### 4. Cubes, weights and complete positive form

For a true frequency, keep its actual fixed bad/unit alternatives, canonical cube-free part and cube factor j^3. For each fixed j, the mask (n,j)=1 remains common. Applying the all-index mean on a canonical dyad M and counting the cube factors gives J^(1/3)L^(2-kappa_1), up to harmless dyads. Principal primitive labels, including genuine cubes and labels created by a short twist, instead use the stronger L^(7/4+epsilon) squared bound with the same cube multiplicity. No cube contribution is declared zero.

I independently restored the source prefactor. Relative to Q0 it is exactly k^(1/3)(Nm)^(-2/3)(Nf)^(-5/3)(Nl)^(-2), k=J/H'. The f sum with m|f and the l sum converge after small divisor losses. The actual rapid Fourier and two common Mellin envelopes pay the transform tails; no uniform power saving at an independently imposed height B^0.36 is asserted. The exact diagonal is O(AB^(1+epsilon)). This yields the claimed complete quadratic form with some fixed kappa>0.

#### 5. Physical interpretation and limits

The displayed ramified identity follows from 1-R/P-(P-1)P^(-q) at q=1-delta and the original j=2,4 odd entries. The pure first-orientation branch has the true b_delta factor and primitive cubic Gauss root; the corresponding shifted Hecke quotient has the other actual b_delta column. All defect alternatives, fixed bad factors, mixed orientations, selected operators, norm powers and full length/contour summations still require their own physical bookkeeping. The present theorem is a genuine new balanced input, not a completed bound for that remainder or an RH conclusion.

This certificate does not claim a new independent Lean run for Q. It verifies the mathematics conditional on the user's stated finite-order input and preserves that attribution.


The publication's standard-library `check_balanced_shifted_inverse_gap.py` was also read and independently executed. Its Fraction polynomial arithmetic reproduces both exact Bernstein lists and the remaining rational margins, and returned ALL_EXACT_GAPS_PASS. It is equivalent to the author's symbolic gap ledger and carries no analytic/source-verification claim.

## C. Independent mathematical review

### Independent audit: direct Mobius--Gauss quadratic-form corollary

The complete direct corollary in `mobius_gauss_direct_density_corollary.md` passes independent review.

The result is conditional on the user's finite-order input Q and the independently checked density and source-transfer arguments in the balanced shifted-inverse theorem. It proves the same full range B^(1-eta)<=A<=B^(2-d_0), including A comparable to B, for the actual mu(n)G(n) column, with the explicit uniform short cubic numerator, common polynomial-size holes and sufficiently small polynomial norm-height windows.

The transfer is legitimate because it verifies the proof's actual coefficient inputs anew. It does not infer an inequality for arbitrary coefficients from the theorem for b_delta. The exact Dirichlet series of mu is 1/L^S, and removing its local factor multiplies by (1-psi(p)P^(-s))^(-1). On every positive buffered strip used here, the finite product costs the prescribed arbitrarily small mask power. A forced squarefree divisor extracts mu(d), the original norm/character factors, and the enlarged hole dK; incompatible and nonsquarefree divisors vanish. The actual free length remains B/Nd.

The global Q smooth bound includes the principal character, whose reciprocal has a zero at s=1. For a nonprincipal zero bin the reciprocal bound gives L^(b+O(h)) without the shifted-inverse numerator's conductor cost. Thus every bin is bounded at least as strongly as in the main theorem. The proved all-a inequality with margin 1/2460 still holds after dropping its nonnegative numerator term. The same affine comparison in log M/log L therefore provides a strict canonical-index mean for all M<=L^(1+eta_1). The canonical index is not replaced by the radical conductor. Short moving cubic twists are reindexed using the exact finite local-state and zero-mask decomposition already audited in the main theorem.

I checked that all remaining steps really use only these inputs: the exact Gauss-corrected Poisson identity, the diagonal, the restriction-free large-f and large-l reductions, the actual forced subsequences, separate principal/cube treatment, cube multiplicities, the convergent restoration weights, and the rapid Fourier and common Mellin tails. None requires the particular shifted-inverse Euler correction. Consequently they apply unchanged to beta=mu and prove the full stated quadratic form.

This argument does not prove a pointwise C^(5/6-kappa) Mobius--Gauss bound, a theorem for angular use of Q, or a complete physical remainder bound. A further application must still match its true row product, twists, common coefficients, holes and norm heights.

Status-only frozen direct version: SHA-256 `ff58ea1a7ce1552c66e6c4f5dae2d91a0e56caf53ff98a4658695f746ffc88f0`. Mathematical statements and proof are unchanged.



## D. Independent mathematical review

### Independent mathematical review: the fixed norm-four noncubic twist in the actual inverse column

#### Decision and application boundary

The proof in `Section D of this Part`, passes independent review. Its mathematical conclusion is an all-cutoff positive power saving for the unchanged a_n(X)*bar(G(n)) column with the fixed primitive norm-four noncubic target, any fixed lambda-ray component, sufficiently small moving cubic conductor/height window, and polynomial-sized common holes. It also legitimately removes the former fixed-cubic-target restriction from the separately audited off-balanced and full-column quadratic-form argument. No Q is used. The balanced boundary, arbitrary moving opposite cubic twists and complete first-nonpolar estimate remain outside the theorem.

#### Noncubic long rows and exact signed decomposition

The newly audited quantitative lambda theorem applies in precisely the conjugated chirality bar(G(n))*rho_u(n). The fixed tau*xi period costs a fixed power of its actual norm; the primitive norm-four component persists and removes the pole. Its smooth input is B^(1/2+epsilon)u^(1/4), with every true zero mask and common hole retained.

For coprime squarefree a,b, cubic reciprocity gives bar(G(ab))=bar(G(a))*bar(G(b))*rho_a(b). The fixed noncubic twist remains multiplicative and therefore splits into the two actual coefficient families without changing the cubic Type II kernel. The ordinary cubic sieve has exactly the same common-column applicability as in the audited signed Mobius proof. In Type I, the genuine long row retains tau*xi and the moving parameter ua. Summing the short a gives B^(1/2+3delta/4+epsilon)u^(1/4), with no residue term. Balancing against B^(1-delta/2)+B^(5/6) yields the claimed conservative signed estimate B^(5/6)+B^(4/5)u^(1/10). The two stated choices of delta and the trivial bound beyond u>=B^2 are correct; a finite epsilon-dependent grid keeps the seminorm costs uniform.

#### Every inverse cutoff and the parameter order

For X<=sqrt(V), the original divisor expansion and the exact Gauss phase leave d^(-1/4), whose ideal sum is X^(3/4). The resulting unperturbed bound V^(1/2)X^(3/4) is at most V^(7/8). For X>=sqrt(V), the exact nonunit complementary identity retains mu(d); the signed input yields VX^(-1/6)+V^(11/10)X^(-3/10), at most V^(19/20) before smoothing.

The sharp boundary affects only actual pairs (d,m), each of modulus at most one. The norm-annulus discrepancy is delta V log(V)+V X^(-1/2)log(V), with no extra divisor coefficient. First choose the smoothing power against all fixed seminorm degrees and the 1/20 margin; then choose the moving conductor and height window smaller; finally choose epsilon after the fixed polynomial-hole exponent. This yields noncircular positive eta_0 and kappa_0. Unit and empty-cutoff cases are treated separately.

#### Forced divisors and the inherited quadratic form

The forced-subsequence identities a_(qn)(X)=sum_(e|q)mu(e)a_n(X/Ne) and bar(G(qn))=bar(G(q))*bar(G(n))*rho_q(n) are exact with (n,q)=1. A zero of the original character kills the block, and otherwise the new twist is still fixed noncubic times a small cubic character. The cutoff and hole uniformity therefore apply after a smaller forced-divisor window is chosen.

The previously audited off-balanced proof was checked by dependency: its coefficientwise Poisson identity, diagonal, large common-divisor removal, large primitive-frequency sieves and full transform tails require divisor-bounded beta and the real Gauss rephasing, not cubic order of its fixed coefficient twist. Its only additional cancellation input is the small-primitive-frequency and forced-divisor estimate, now supplied here. The strict off-balanced geometry and its ordering of small constants remain intact. The fixed noncubic period is a paid implied constant, not an unrestricted moving v2 parameter.

The full-column decomposition uses multiplicativity of tau(gb^2c^3v), not the condition tau^3=1. Its frozen factors are bounded common scalars; the original character's cube/exponent-two row masks and rad(n) inverse identity remain unchanged. Thus the existing positive Minkowski and short/long free-column estimates extend as stated, with possibly smaller kappa. This does not extend to A comparable to B.


## E. Independent mathematical review

### Independent audit: the original large-cutoff inverse at balanced scales

The complete proof in `true_inverse_large_cutoff_balanced.md` passes independent review, conditional on the user's finite-order input Q and the explicitly cited, previously reviewed coefficient estimates. This certificate covers the actual sharp inverse a_n(X), all original column layers, and the finite-integral raw b_delta consequence. The author's final clarifications on the short-column diagonal and the combined complex-height window are recorded with the final version below.

#### 1. Scope and sharp Mobius--Gauss input

The main range is X>=U^(2/3+rho), with fixed rho in (0,1/3), A in a sufficiently small power neighborhood of U, common column holes of fixed polynomial norm, and norm height in a sufficiently small polynomial window. The target twist is fixed cubic, or the particular already audited primitive norm-four noncubic family with its fixed bad/lambda factors. A finite bad vector must first be expanded in the actual permitted characters. The proof does not establish a general finite-order or angular extension of the raw inverse's small-frequency input.

The Mobius--Gauss theorem may be conjugated in its entirety, giving the orientation in (2). It permits a common sharp norm cutoff after the following legitimate argument. On a D-annulus, smooth the step in log norm on width D^(-theta); its common Mellin transform has logarithmic L1 cost. Apply the fixed-test theorem to its norm-height modes, inside its proved small height window. Large modes have rapid tails paid against a trivial polynomial bound. This does not feed a test with D-dependent large seminorms into a fixed-seminorm theorem.

The remaining thin band has O(D^(1-theta)+D^(1/2)) lattice points. The ordinary full-row cubic sieve controls its coefficient square mass. Relative to the desired cross term, the potentially dangerous middle term is bounded by D^(eta'/3-theta+small loss) when A1>=D^(1-eta'). Choosing eta' and the new saving below theta handles it; the diagonal stays within A1D. Thus the sharp cutoff is covered uniformly in its position.

#### 2. The actual row product mh

The identity a_n(X)=-sum_{d|n,Nd>X} mu(d) is exact for n>1. On squarefree n=dm, the conjugate Gauss CRT gives bar G(d) bar G(m) chi_d(m). Multiplication by the actual frequency character produces the common d-column mu(d) bar G(d) xi(d) chi_d(mh). The original zero at (d,m)>1 is already encoded by chi_d(mh); no m-dependent internal coefficient or extra m-hole remains in this common column.

On fixed d,m norm dyads, separate the common product weight with compact cutoffs retained. Cauchy in m costs B/D. Replacing a=mh then costs only the ideal divisor multiplicity, and all products lie in an actual row annulus of scale A1=BJ/D. A fixed radial positive majorant gives the complete-row norm from the Mobius--Gauss theorem. This is not an invocation of uniformity for a long moving character.

I recomputed the resulting terms: they are B^2 J/D and B^(5/3)J^(2/3)D^(-kappa_mu). At J in a small power neighborhood of B and D>=B^(2/3+rho), the actual A1 interval lies inside the input's lower and upper aspect-ratio windows. The upper condition follows from B^(2+zeta)<=D^(3-d_0) with d_0 chosen in terms of rho. The two ratios to J^(1/3)B^2 are J^(2/3)/D and (J/B)^(1/3)D^(-kappa_mu), both strictly saving. Dyadic Minkowski introduces only logarithms. The genuine sharp boundary has its independent sieve saving.

#### 3. Restore every true frequency and the squarefree form

The source coefficient is exactly beta=a_n(X) bar G(n), so multiplication by G(n) recovers the original squarefree polynomial, rather than a different mollifier. I checked the pinned Poisson and positive large-f/l reductions against the previously audited complete proof. Their near-balanced extension pays A>=B/E in the large-common-divisor removal and the small B^O(eta) enlargement in the large-l costs.

For retained f,l, the forced identity a_(fln)(X)=sum_{e|fl} mu(e)a_n(X/Ne) is used with its true free length L=B/N(fl), its coprimality and enlarged holes. Taking the removal width sufficiently small in terms of rho ensures X/Ne>=L^(2/3+rho/2). No forced cutoff is replaced by X without its divisor.

Near-frequency blocks use the new mh estimate. For J<=L^(1-zeta), the original restriction-free primitive-frequency sieve proof applies precisely because its canonical frequency index is smaller than L by a fixed power. Its small primitive frequencies, including genuine cubes, use the previously proved true all-cutoff inverse--Gauss power estimate in the stated cubic or particular noncubic family. This input retains polynomial holes, short twists and a small height window; no unrestricted source height B^0.36 is imported.

The exact restoring weight is k^(1/3)(Nm)^(-2/3)(Nf)^(-5/3)(Nl)^(-2). Its divisor sums and the actual rapid Fourier/common Mellin envelopes preserve the power margin. The diagonal remains O(AB^(1+epsilon)). Constants can be chosen in the stated noncircular order.

#### 4. All columns, including exponent two and cubes

The factorization n=a b^2 c^3, q=rad(bc), g=(a,q), a=g v is exact. It preserves (g,b)=1, (v,q)=1, rad(n)=qv, the true cutoff identity sum_{e|q}mu(e)a_v(X/Ne), and the row-only character factor. The latter is removed only after freezing b,c,g inside a positive norm. The real free length is V=U/[Ng(Nb)^2(Nc)^3].

For V>=U^(1-tau), Nq<=Nb Nc<=sqrt(U/V) is small. Therefore X/Ne remains above V^(2/3+rho/2), and A remains in the squarefree theorem's near-balanced window after tau and the final eta are chosen sufficiently small. A cutoff above the free support endpoint vanishes on nonunits. Common holes remain in a fixed polynomial range in V.

The saving cross norms sum with the strict b,c exponents -5/3+kappa_sf and -5/2+3kappa_sf/2. The total diagonal norm over both long and short blocks is O(sqrt(AU) U^epsilon). For short V, A>=V allows the ordinary sieve's middle term to be absorbed into its cross term. The inequality V^(5/6)<=U^((1-tau)/4)V^(7/12), followed by the summable b,c exponents -7/6,-7/4, gives the extra tau/4 norm saving. Unit-scale blocks are bounded directly. No invalid vanishing assertion for a_1 is used. This proves the displayed all-column theorem after squaring and shrinking the saving.

#### 5. Raw complete shifted inverse

For n>1, direct finite partial summation gives b_delta(n)=-delta (Nn)^(-delta) integral_1^(Nn) a_n(X) X^(delta-1) dX. On the actual annulus the upper limit may be replaced by 2U because a_n(X)=0 beyond Nn. This is an exact finite identity, not a contour passage through zeros.

Split at U^theta, 2/3<theta<1. The high-cutoff part uses the proved all-column theorem and has bounded absolute integral mass, with its genuine complex-height cost. The low-cutoff mass has the factor U^(-r(1-theta)), uniformly for r=Re(delta) in a fixed positive compact interval. The ordinary complete-row/full-column bound is exactly the three terms AU, A^(1/3)U^2 and A^(2/3)U^(5/3); it follows by the same column-layer decomposition and its convergent norm sums. The middle term is at most U^(eta/3) times the cross term near balance, so the low-cutoff mass pays it with a strict margin. It is estimated, not discarded.

The imaginary part of delta joins the norm-height variable, and all resulting polynomial factors are paid inside a further reduced small polynomial window. The n=1 coefficient is outside this annulus or is separated explicitly. Thus the complete raw b_delta column has its stated improved balanced quadratic form. It is distinct from the squarefree Gauss-weighted b_delta theorem.

#### Limits

These are genuine complete positive quadratic-form estimates for the specified coefficient families. They do not establish the entire zero-detector tail at arbitrary small cutoff, remove all physical ramified/selected alternatives, or bound the whole coupled q-surface. No final physical Z exponent or new zero-free region is claimed.

The final version explicitly retains the short-V diagonal norm, tau<=eta_sf/4 and final eta<=tau/4, the retained-frequency neighborhood, and the combined Im(delta)/norm-height window. These clarifications were read back and agree with this audit.

Status-only frozen manuscript SHA-256: `f819f9fb05dc244c62dfaaae6bad7b12f0f8ccfadcf9fa2eb545e3f1e304a3ee`. Mathematical contents are unchanged from the final reviewed version above.

# Supplementary source review: the user’s nine lambda-ray theorem

## Independent source audit of the user's nine lambda-ray theorem

The main theorem in user commit bed10bb2cf3f55ce5b66233614733a9acbbf0ac4 passes independent review. I read the complete main manuscript and both accompanying audits, directly checked the cited Dunn--Radziwill source sections, and ran the exact finite checker. The new general primitive residue-character range is retained: phi cubed is nonprincipal, the modulus is prime to three, and all nine specified primary modulo-nine ray characters are allowed. This is not restricted to the norm-four character used in our other local argument.


### Nine labels and one ancillary sign correction

For lambda=1+2 omega and T=A+B omega, Tr(lambda T)=-3B and Tr(T)=2A-B. Substitution into the actual definition of alpha_T gives exactly the main manuscript's formula (3): its two exponents are (+B,2A-B). The cross term for two primary generators lies in the trace-dual lattice, and cubing a primary generator gives one modulo nine. Thus these are precisely the nine multiplicative cubic characters of that primary subgroup.

There is a minor sign mismatch in the accompanying audit's description of the label map and in the checker's unused label-set coordinate: they write (-B,2A-B). The main formula and the checker's actual trace assertion use +B correctly. Both coordinate maps are bijective and this does not affect the cusp classification, matrix checks, or theorem. For exact alignment with formula (3), that ancillary coordinate should read +B. The checker should not be described as checking the incorrect signed coordinate against the formula.

### Finite Fourier and the true cusps

The finite Fourier inversion uses the original positive trace character, hence the primal theta argument is t-9d/r. The source projection has the three translations 0, omega, -omega with their stated weights and normalization 1/(3Q). Primitivity gives Fourier support on units, magnitude sqrt(Q), and transform equal to its value at one times conjugate(phi(d)). These facts hold for general primitive residue characters, including moduli with prime-power factors.

For a unit label T, the reduced cusp matrix belongs to the full principal subgroup modulo three. Its primary-normalizing unit is independent of d and the numerator modulo nine is independent of d. Cubic reciprocity therefore makes the Kubota multiplier a fixed constant times rho_r(d). Because the theta function is conjugated, its cusp coefficient uses the conjugate multiplier. The complete constant is proportional to the sum of conjugate(phi rho_r), which is zero since rho_r cubed is principal while phi cubed is not. This is a general character orthogonality argument, not a norm-four calculation.

For the two nonzero lambda-divisible labels, dividing numerator and denominator by lambda gives a genuine coprime matrix with lower-left residue plus or minus lambda modulo three. The source defines left Gamma_2 cosets. The two displayed lower-translation identities identify these cosets with indices 19 and 10, respectively; the rational lower translations and principal-level-three translations used on the left belong to Gamma_2. The source's Fourier expansion gives zero constant term at both indices individually. No unproved replacement by an untwisted bad-prime matrix is involved.

Direct use of the hyperbolic action gives the exact inverse image (-D/c,1/(N(c)v)). In particular there is no unaccounted horizontal error. The common transformed norm is 9Q in a unit channel and 3Q in either of the other channels.

The supplied checker was executed and returned ALL_PASS for the nine classifications, 288 exact matrices and the 19/10 coset words. Its finite quadratic projections are auxiliary checks; they do not replace the preceding general-phi orthogonality proof.

### Completion and uniform bound

The original support contains no zero Fourier frequency. At the other end, the actual transformed constants vanish by the preceding calculation. The fixed transformed theta expansions therefore give exponential decay at both endpoints. At their fixed horizontal coordinates, the Fourier factors have modulus one; the usual Bessel Mellin integral retains the same two Gamma factors. In a unit channel, subtract the individual constant parts only after noting that their aggregate coefficient is zero.

The undifferentiated change of variable gives the exact completion relation Lambda_T(s)=L_T^(1-2s) Lambda_H(1-s). The transformed coefficient mass is at most sqrt(Q). Absolute convergence at 1+delta and the Gamma quotient consequently give the left-edge cost Q^(3/2+2delta)(1+|t|)^(2+4delta), while the original coefficient factorization gives a uniform right edge. The user's previous conductor-balanced strip argument, with delta=epsilon/4, then gives Q^(3/4)(1+|t|)^3. To the far right one uses the original R series, rather than extrapolating the completed coefficient series with norms below one.

The initial Euler factorization retains phi(lambda), the ray phase, and L_(3r)(3s-1/2,phi^3). That reciprocal Euler product is absolutely convergent on every closed half-plane Re(s)>1/2. It follows that the normalized Gauss series is holomorphic there with the stated uniform bound. No Q or GRH input is used.

### Masks, conjugation and scope

For a squarefree extracted hole d prime to 3r, the residual character phi conjugate(theta_d) is primitive modulo rd and still has nonprincipal cube. The same ray alpha_T remains, by its true multiplicativity. The new modulus cost is (Q Nd)^(3/4), multiplied by Nd^(-sigma), which gives at most Nd^(1/4). Thus the explicit factor sum_{d|rad(M)} Nd^(1/4) is necessary in this proof and is retained. It is not replaced by M^epsilon. The conjugated-Gauss statement follows by conjugating the character, ray label and complex argument together.

The result is the user's general nine-channel theorem, with its original attribution. It does not by itself identify a complete physical row, prove uniformity for arbitrary additional lambda conductors or angular types, or bound an entire ordered physical remainder. The only correction above is the ancillary sign-coordinate mismatch; the main mathematics and exponents stand.

Primary source checked: Dunn--Radziwill, arXiv:2109.07463v3, Sections 5.1--5.4, including the full principal subgroup, left cosets, the 10/19 expansions, finite Fourier projection and two-Gamma Mellin formula: https://arxiv.org/html/2109.07463v3.

### Independent exact alignment check

I additionally read and executed `check_actual_ray_labels.py` from the independent local-arithmetic review, SHA-256 `69cbc3973f5cec0b9ba162a71157ee283aa2fc9b5e45046f6170c5fa53b3bd89`. It returned ALL_PASS for the actual +B trace formula in 81 evaluations, the 729 multiplicativity/source-phase identities, primary cube congruence, and both exact lower-translation words. This verifies the corrected coordinate directly without modifying the user's supplied files. The companion independent pressure audit, SHA-256 `91561a5ad1a1c778e5107139699ac41ebe95ae6feede4c8e8af9d77348fbdcde`, agrees on the complete general-phi analytic scope.
