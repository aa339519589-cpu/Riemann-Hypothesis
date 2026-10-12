# Independent review: physical Kummer blocks and signed powerful-s subtraction

This review accompanies [PHYSICAL_KUMMER_BLOCKS.md](PHYSICAL_KUMMER_BLOCKS.md). It covers the two exact higher-valuation identities, the complete powerful-s signed cancellation and the full physical within-class positive norm. The first requires complete m summation before positive decomposition; the second leaves the cross-class term and a 1/32 exponent deficit. Neither uses Q.

## Part I A

Approved as an exact finite physical identity, with no new estimate asserted. The corresponding proof in the accompanying report was reviewed.

### 1. The prime-power Gauss transform

For s=p^k s0, j=k mod 6 nonzero, the p-primary character is the lift of primitive chi_p^j. Its Gauss transform is zero unless v_p(m)=k-1 exactly. Writing m=p^(k-1)m0, its normalized magnitude factor is P^((k-1)/2) gamma_j(p) conjugate(chi_p^j(-m0)). The full CRT initially contributes chi_p(s0)^j chi_s0(p)^k. Scaling the residual s0 Gauss sum by the unit p^(k-1) contributes conjugate(chi_s0(p))^(k-1), leaving exactly chi_p(s0)^j chi_s0(p). This proves (4), including imprimitive residual s0 characters.

The original chi_A(m) zero mask forces (p,A)=1 when k>=2. At k=1 that condition is additional and cannot be omitted. No principal j=0 lift is covered by this argument.

### 2. Full auxiliary root and completed-row phase

With rho=chi_p^(-j), normalized primitive Gauss conjugation gives gamma_j(p) conjugate(chi_p^j(-1))=tau_rho^-1. The changes xi(m)/xi(s) and chi_s(b*) supply xi(p)^-1 and chi_p(b*)^j. Their product is precisely the full-root ratio tau_plus^-1/tau_xi^-1, including both CRT characters xi(p) and rho(b*).

The remaining s0 factor is chi_s0(p)/rho(s0), exactly the new chi_s0(b*)/xi(s0) factor. For A, the source convention chi_A(p)=R(A,p)^-1 chi_p(A) yields
R(A,p)^k chi_A(p)^(k-1)=R(A,p)chi_p(A)^(j-1)=[Xi_plus(A)/Xi(A)]^-1.
Thus the original completed-row correction, including chi_A(m), becomes the stated enlarged-auxiliary correction with no omitted phase. Target eta, alpha, G and gamma_2(c) are unchanged.

### 3. Physical scales and zero extensions

The Gauss lift P^((k-1)/2) converts the original square-root radial normalization with s=p^k s0 into the new normalization with auxiliary norm BP and the same X. The argument of W0 similarly becomes Nm0/(BP Ns0 X). The original s average changes to P^-k times the average at Y/P^k. The Gaussian index A and T are unchanged. All new p-unit masks for m0,s0,A are exactly supplied by the selected branch and its primitive Gauss support. Therefore the identity P^-k I_(S+p,xi rho)(X,Y/P^k,T) is coefficientwise exact.

For k=5 mod 6, rho=chi_p, not its conjugate. Its contribution to s^2/m has p-exponent k+1 divisible by six, explaining the invisibility to the separate auxiliary pair label. Repeated extraction is valid only with the current complete auxiliary root at each step; the manuscript correctly retains this and does not replace it by independent scalar roots.

### 4. Scope of outer operations

Existing marked A conditions and compensation coefficients remain literal. A p-marked positive term is zero on this A-unit branch. Existing rescaled slot labels are not redefined. The already chosen restoring operator retains its old dilation-prime set. Converting the old normalized observation into the new normalized one costs the exact factor c_(S+p)/c_S=(1-P^-1)^2. The principal j=0 Ramanujan layers and the k=1 common-A branch stay open. Neither uniform scale estimates nor any infinite-sum interchange beyond the original absolute convergence follows solely from this identity.

## Part I B

Approved as an exact identity. The corresponding proof in the accompanying report was reviewed.

For k>=6 divisible by six, the complete principal p^k Gauss transform has the stated boundary -P^(k-1), bulk P^(k-1)(P-1), and zero elsewhere. Its support and the original chi_A(m) imply p not dividing A. At m=p^k m1 all k-th power phases cancel, leaving (1-P^-1) times the old complete column at X after the common P^-k Y factor. At m=p^(k-1)m0, the residual Gauss scaling contributes chi_s0(p), the auxiliary factor contributes conjugate(xi(p)), and the completed row contributes conjugate(chi_A(p)). These give exactly omega_p in (1).

The boundary normalization is -P^-1/2 times the column at PX, with the genuine p-unit mask on m0. Expanding that mask as all m0 minus p multiples, the latter's row factor is the exact inverse of omega_p. Its radial square-root change supplies another P^-1/2. It therefore returns +P^-1 times the complete X column, restoring its coefficient from 1-P^-1 to one. This proves the full signed two-column identity (2), with no new m-character or artificial p-unit condition.

The bulk Kummer class is unchanged because p^-k is a sixth power. The second column uses the fixed permutation by [p^-1]. Its removed p-multiple part has the first column's class, so the identity holds coefficientwise in the common original class space, including the unit component. The nonprincipal higher-valuation identity analogously has the fixed class permutation by [p^(-k-1)].

Omega_p is a fixed-s0 scalar times a bounded A-row phase. It is independent of the free m column and any subsequent d,z parametrization, so an arbitrary-common-coefficient conductor large sieve can absorb it without changing its characters. Original marks, slot labels, c_S and restoring-prime sets must remain literal; the manuscript correctly does so. Iterated use entails its actual P^-k and changed X scales, and does not itself prove a uniform or cross-class estimate. No Q is used.

## Part II

Approved within the stated signed-subfamily scope. The corresponding proof in the accompanying report was reviewed.

### 1. Exact support and nonprincipal higher valuations

Every prime of t has s-valuation at least two. Both primitive and principal local Gauss transforms require v_p(m)>=v_p(s)-1>=1. The actual chi_(cr^6)(m) zero extension therefore forces (r,t)=1; this is not an additional deletion. The unique division of t into non-six-divisible prime powers t_* and a disjoint sixth-power v^6 is legitimate.

The separately reviewed nonprincipal-valuation identity applies coefficientwise to every prime of t_*. Each step retains the current full normalized auxiliary Gauss root and replaces xi by the genuine nonprincipal local factor chi_p^(-j). The resulting primitive auxiliary modulus has no uncontrolled multiplicity factor. The product K^-1 from these steps cancels exactly with (Y'/K)^-1, leaving the original outer Y'^-1. Existing marks, compensation coefficients, old c_S normalization and the old restoring-prime set stay fixed.

### 2. Full principal Ramanujan identity

For the remaining s=c v^6, coprimality (v,cr b*)=1 makes the CRT factor chi_c(v^6) equal to one. The principal Gauss component is the entire Ramanujan sum c_(v^6)(m), including its bulk. Multiplication by the genuine completed chi_(cr^6)(m) cancels the primitive c-Gauss character and retains exactly the cr-unit mask.

Expand c_(v^6)(m) as sum over e|rad(v), v^6/e|m, with coefficient mu(e)Nv^6/Ne. The substitution m=(v^6/e)k is a discrete bijection, not a continuum change of variable. Since xi(v^6)=1, its phase is conjugate(xi(e)). The old radial square-root normalization, Ramanujan normalization and the new radial scale B_* C Ne X' combine to precisely (Ne)^-1/2. This proves (8), with no additional v-unit mask on k.

The primitive Poisson estimate holds for all positive radial scales and uniformly in the enlarged modulus. Expanding only the cr-hole gives (10). Multiplication by the factor in (8) leaves sum_e (Ne)^(-1-L), bounded by zeta_K(1+L) for fixed L>0. Thus (11) has no power of B_*, t_* or v, and no constant raised to the number of absorbed primes.

### 3. Complete powerful count and actual compensated scales

Every powerful ideal has a unique representation a^2 b^3 with b squarefree. Ideal counting and the convergent b^-3/2 sum give O(H^1/2) ideals up to H. The actual annular c sum weighted by C^-1+epsilon is divisor-small. The entire log-Gaussian moment for r is (T_eff/C)^((L-2+epsilon)/6), valid also at subunit T_eff/C through its rapid tail. For L>2 its negative C-power can be discarded, yielding (13).

It is essential to keep the same subset parameter d in X',Y',T_eff. The coefficient of L is -23/144+5d/6<=-1/48, and the constant part is -29/36+4d/3<=-7/12. The whole fixed-slot mass contributes at most Z^(1/6), giving exactly -5/12-L/48. The Gaussian order L is fixed after the desired final power. This proves uniform arbitrary fixed power decay over all original subsets, powerful t, r and 0<T<=Z.

The original n^-1 corollary changes only r^-3 to r^-2. Its Gaussian exponent is (L-1)/6; the same subset calculation gives -5/12-L/48 before the slot mass and -1/4-L/48 afterwards. That separate physical assertion is valid. The restoring statement remains restricted to the half-damped observation, as expressly stated.

### 4. Restoration and scope

The previously reviewed restoring operator only dilates T and preserves this literal selected support. Its norm on the uniform T<=Z bound is the prescribed O(1) product, as is the old c_Sb^-1 on the polylogarithmic pool. Internal auxiliary absorption does not insert new restoring factors or enlarge that normalization. Positive finite averaging and the logarithmic slot normalizer preserve arbitrary power decay.

This is a cancellation of an entire signed m column, before squaring or positive Kummer-class decomposition. It does not bound each positive class energy or the complementary physical family. The unreviewed intermediate sixth-power-only draft is not needed as a separate hypothesis: the full Ramanujan calculation was checked directly here. No Q or whole-low/RH conclusion is used or obtained.

## Part III

Approved as a positive-block estimate. The squarefree-s proof was reviewed.

### 1. True class parametrization and legitimate common coefficients

Primitive squarefree-s Gauss support gives (m,s)=1. The actual class [m/s^2] therefore has valuation four at every prime of s. With all unit components retained, its sixth-power-free representative satisfies h=s^4 d, m=d z^6, (s,dz)=1. For a fixed h there are only divisor-many possible s. Cauchy in precisely that finite set gives (3), with Nh bounded by a constant times B X Y^5. No independent free s multiplicity is omitted.

The original chi_A(m) remains chi_A(d) times its z-unit mask; it cannot be replaced by chi_A(h)chi_A(s)^-4 when A and s share primes. The manuscript avoids that false factorization. After taking the fixed-s squared norm, xi(d) and the primitive s-Gauss d-character are legitimate common column factors of modulus at most one. The remaining correction is a bounded row coefficient.

Writing n=n0 r^2 gives a=c n0^3 with local exponents 0,1,3,4. They uniquely recover (c,n0) and distinguish the primitive good local characters; fixed bad/ray components give only bounded multiplicity. The genuine conductor has norm at most a fixed multiple of Na. The earlier all-primitive-character large sieve in QUADRATIC_DUAL_N1.md, Part XXIII A, Section 1 was read back: it has the arbitrary-full-column kernel D+Q^2. Its dual therefore applies to this actual family. New auxiliary phases remain coefficients and masks, rather than moving conductors concealed in the family constant.

### 2. Marker mass and complete n/Gaussian sums

For fixed n0, the marked c must be divisible by E0/(E0,n0). Its harmonic annular sum is at most the reciprocal norm of that divisor, with divisor-small loss. Summing n0^-3 N(E0,n0) is uniformly bounded: marked Euler factors have size 1+O(P^-2), so their total converges. This proves the precise marker factor (NE0)^-1 in squared mass.

For fixed r,z, the (r,d) condition is a common column mask, while the z-unit condition is a bounded row mask. Positive enlargement is made only after the relevant norm. The Gaussian dyad sums of 1 and Q cost respectively O(1) and O(T/(Nr)^6), including their subunit rapid tails. This proves (6) with the true full Gaussian, not a hard cutoff.

Minkowski in r is summable uniformly in E because r^-3 N(E,r)^1/2 and its exponent-nine version have convergent Euler products. All square factors of n and their masks are thus retained. For fixed z the common radial d weight has length M_s/(Nz)^6. Summing its square-root term uses the convergent z^-3 series, and summing its constant T term uses the actual count Nz<=O(M_s^1/6). After M_s^-1/2 normalization these are exactly 1 and T M_s^-1/3. Unit-scale end dyads are harmless fixed compact cases. The annular O(Y) physical s count and the previous class-divisor Cauchy give (1).

### 3. Original compensation and restoring operation

The original summand has coefficient (ND)^-3/2, scales X/ND,Y/ND,T NE, and the same abstract class labels [m/s^2]. Its triangle-norm bound is exactly (9), not a coefficientwise cancellation. The positive slot sums cost at most Z^(ell/2) and Z^(3ell/2). At the original geometry these give -5/32 and 211/288 minus the B^(1/3) suppression, respectively.

Every actual auxiliary modulus in the stated R0=Z^128 pool has the supplied lower norm bound, so the second term is smaller by a fixed large power. The auxiliary small-power losses can be chosen after the fixed polynomial ambient relation. The old c_Sb, A_T and T-only restoring costs are the reviewed ones, and the physical class labels remain unchanged. Averaging the squared per-b bound with the positive law adds no number-of-moduli cost.

No Q is needed for this positive estimate. It remains short of Z^-3/16 by 1/32, and the long-support cross-class sum remains unestimated. The separate signed complete-m cancellation cannot be assigned to already-positive class entries.

## Part IV

Approved as an extension of the reviewed squarefree-s estimate. The corresponding proof in the accompanying report was reviewed.

### 1. Exact higher-valuation reductions and class coordinates

The unique splitting s=s1 t with s1 squarefree and t powerful is correct. Gauss support at every prime of t, together with the genuine chi_A(m) zero extension, forces (t,A)=1. In particular (t,E)=1 on nonzero marked branches.

For nonprincipal local exponents, the already independently reviewed complete-column absorption replaces xi by its genuine primitive local extension, scales Y by P^-k, and contributes the exact P^-k outside factor. The old class is [p^(-k-1)] times the new class, a fixed bijection. Full auxiliary roots and masks are retained.

For principal exponents k divisible by six, the separately checked two-column formula contains both the complete X column and -P^-1/2 times the complete PX column. Its row phase is exactly conjugate(xi(p)) chi_s0(p) conjugate(chi_A(p)). It is a scalar times an s0 coefficient times an A-row coefficient, with no dependence on the free d,z column. The first class permutation is identity and the second multiplication by [p^-1]. The missing p multiples combine with the Ramanujan bulk in the first class exactly. Neither branch is reduced to a false principal auxiliary character.

These formulas remain legal in the squarefree-s proof because that proof uses arbitrary bounded row factors at its actual large-sieve steps, with additional row restrictions and common column masks retained. The actual character family chi_a and its conductor remain unchanged. Temporary auxiliary data only change allowed coefficients and masks.

### 2. Summing every powerful ideal

For fixed t the total absolute branch coefficient is (Nt)^-1 times product_(6|v_p(t))(1+P^-1/2), which is divisor-small without an unbounded C^omega factor. The new B_t>=B and X_t>=X, while Y_t=Y/Nt. Each fixed class permutation is an ell2 isometry. Applying triangle and the squarefree-s bound yields exactly (5), including (Nt)^-1/2 and the secondary (Nt)^1/3.

The compact physical window forces Nt<=O(Y), so any surviving reduced Y_t is bounded below by a fixed positive constant. The powerful factorization a^2 b^3 gives the two stated weighted sums: a harmonic endpoint for t^-1/2, and Y^1/3 for t^-1/6. A smaller preliminary epsilon absorbs all divisor factors and temporary-modulus polynomial changes. Their Minkowski sum proves Y^-1/2 (NE)^-1/2 [1+T(BX)^-1/3] with no positive power of Y in its main term.

### 3. Exact outer scale budget

With the original compensation coefficient D^-3/2 and scales X/D,Y/D,T E, the first outer factor is Y^-1/2 D^-1 E^-1/2. The secondary factor is T E D^1/3 (BX)^-1/3. Thus the per-slot positive masses are P^-1+P^-1/2 and P^-2/3+P^1/2, with total costs Z^(ell/2) and Z^(3ell/2). This gives exactly the exponents -5/32 and 257/288 in the original geometry.

The large actual auxiliary norm in the prescribed polylogarithmic pool suppresses the second term. The old c_S normalization, old T-only restorer and logarithmic A_T normalization remain those of the original b, not of B_t introduced within the proof. Restoring dilations preserve the class coordinates. The complete per-b positive norm and then its positive average are therefore at most Z^(-5/32+epsilon).

All transformations are actual complete-column identities before norms, with finite class-coordinate permutations. Gaussian tails and the displayed convergent estimates justify the indicated limits. This result estimates the entire within-Kummer-class block, but it neither proves that the signed cross-class contribution is small nor bounds the full observation. It still has a 1/32 exponent deficit from Z^-3/16. No Q, full-high estimate or unproved cancellation is inserted into the low proof.

