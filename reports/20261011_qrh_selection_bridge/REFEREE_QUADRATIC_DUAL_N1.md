# Independent review: complete physical quadratic dual sector

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
