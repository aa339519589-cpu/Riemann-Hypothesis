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
