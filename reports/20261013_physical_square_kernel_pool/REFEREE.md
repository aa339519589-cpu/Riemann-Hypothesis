# Independent mathematical reviews of the physical square-kernel pool

These reviews cover the complete character theorem, its full-frequency physical application, and the growing-kernel uniformity argument in [the report](REPORT.md). Each main proof received a full independent review. A second reviewer checked the character theorem independently of its author; the character theorem's author separately checked the physical/source bridge and the growing-pool argument. That latter contribution does not substitute for independent review of the character theorem itself.

The conclusions remain restricted to the exact displayed physical branch. The scalar pool saving and the separately bounded same-class subtraction are distinct terms. No whole Mobius estimate, new spectral gap or zeta-zero exclusion is certified.

## A. Character theorem: complete independent review

### 1. Translation and original finite lattice

Let M=Q^(1/2)E. In the range E<=Q^(1/8), the nonzero averaging elements have norm lengths A=Q^(5/16), B=Q^(1/16) and cardinalities comparable to those lengths. Their elements are invertible modulo both primes for sufficiently large Q. The shift jab preserves the original coset modulo J. Its coordinate size is O(sqrt(NJ AB)), while rectangle side lengths are O(sqrt M). Bounding the symmetric difference by strips of the full fixed Eisenstein lattice gives exactly the stated perimeter, area and endpoint error, including short or degenerate rectangles. No coset-density estimate is assumed.

The comparison is performed for each entire translated sum before taking its absolute value. Multiplicativity then gives chi(v+jab)=chi(ja)chi(v/(ja)+b), retaining zeros even for nonunit v. Precomposing a harmonic quadratic with the complex affine map b -> v+jab remains a harmonic quadratic, so its four nonconstant real parameters are covered by the phase supremum.

For E>Q^(1/8), the trivial O(M) count is smaller than the claimed Q^(63/128)E^2; this includes all larger source/support parameters without an unproved uniformity continuation.

### 2. Ratio energy, including nonunits and zero

Equality of two residue ratios forces v1a2-v2a1 in the product ideal. Its norm is O(MA)<=O(Q^(15/16)), below Q for sufficiently large Q uniformly in this E range. Thus the residue relation is an exact element equality. j cancels because it is invertible modulo the product ideal; no inverse-size estimate is used.

For each nonzero common product w=v1a2=v2a1, both representations are counted by at most a fixed unit factor times the ideal divisor function. There are O(MA) possible elements w, each with divisor count O_epsilon((MA)^epsilon). Renaming epsilon gives the stated energy O(MA Q^epsilon). The zero product requires v1=v2=0 because all a are nonzero; its A^2 cost is <=MA. Hence the energy estimate includes nonunit v and all cosets.

### 3. Uniform phase supremum and complete moment

In coordinates b=k+l omega, harmonic quadratics have frequencies k,l,k^2-l^2,2kl-l^2. Their coordinate degrees are O(sqrt B), O(sqrt B), O(B), O(B). The tensor oversampling grid therefore has O(B^3) points. Bernstein bounds each derivative by its coordinate degree times the global supremum, so a sufficiently fine nearest grid point has value at least half the supremum. This is a multiplicative supremum estimate, not an additive approximation error. Summing over all residue x then costs B^3 times the largest complete sixteenth moment over fixed grid phases.

After expanding that moment, each phase coefficient has modulus one and is independent of x. The complete character expression factors by CRT into its two local field sums. Distinct b values have norm difference O(B), below either prime norm, so root collisions modulo either prime occur exactly for the same literal elements. Both local cubic orientations therefore have the same bad-tuple criterion.

For each local cubic character the exact product, including zero values, equals chi(P(X)), where P=product_plus(X+b_i) product_minus(X+b_i)^2. It is monic and a cube precisely when each signed multiplicity is divisible by three. A bad tuple has at most eight distinct roots, hence there are O(B^8) bad tuples. For any other tuple the finite-field multiplicative Weil bound applies at both primes, giving O(sqrt Q) after CRT. I directly read Theorem 11.23 and Corollary 11.24 in the authors' official Chapter 11 PDF: https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf . The polynomial has at most sixteen distinct roots, so the constant is fixed independently of all phase coefficients and primes. This explicitly checks the nonprime residue-field case as well.

Thus the complete phase-supremum moment is O(B^3[Q B^8+sqrt(Q) B^16]), with no intermediate one-prime-degenerate contribution omitted.

### 4. Exponent and smooth range

The stated Holder inequality has factors (sum nu)^(7/8), (sum nu^2)^(1/16) and (sum T^16)^(1/16). Inserting the two energy estimates, then dividing by AB, gives M^(15/16) Q^(3/128+epsilon), equal to Q^(63/128+epsilon) E^(15/16). At E=1 the exponent also checks as (13/16)(15/16)+(27/16)/16-3/8=63/128. The boundary error is smaller than the claimed Q^(63/128)E^2 throughout the range.

All partial rectangles satisfy the same enclosing-disk estimate, so two-dimensional Abel integration gives the stated compact smooth-weight consequence with its genuine variation seminorm. It does not give arbitrary bounded-mask uniformity. The local theorem is uniform in completely arbitrary harmonic quadratic coefficients, and thus can retain a reciprocal quadratic phase if the later physical decomposition supplies the remaining smooth seminorm and summable-frequency bounds.

This review certifies Part I. Its physical application is independently checked in the reviews of Parts II and III below; the character theorem alone does not supply those steps.

## B. Character theorem: second independent check

All five sections pass. The shift average compares entire translated sums before the triangle inequality, so the arbitrary harmonic quadratic remains legitimate. The coset is invariant under jab, and the displayed full-lattice boundary error covers short rectangles. In the nontrivial E range the ratio congruence has a difference of norm less than Q and is a literal equality; its divisor-square count includes nonunit v, with v=0 costing A^2<=MA. No modular-inverse regularity is assumed.

The four coefficient coordinates of a harmonic quadratic have trigonometric degrees sqrt(B),sqrt(B),B,B. Bernstein oversampling gives the multiplicative supremum grid with B^3 points. The exact complete-moment polynomial product_plus(X+b) product_minus(X+b)^2 retains all zero values. Distinct b values cannot collide at either auxiliary prime, because their difference norm is below both prime norms. Consequently the two local cube exceptions coincide, have at most eight distinct roots and cost O(B^8); no one-prime-degenerate family is missing.

I personally opened Theorem 11.23 and Corollary 11.24 in Iwaniec–Kowalski's official Chapter 11 PDF, https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf . The finite-field theorem covers both split and inert prime ideals here. The monic noncube polynomial with at most sixteen distinct roots has a fixed square-root bound; CRT gives sqrt(Q) for every nonexceptional tuple. The resulting sixteenth moment is B^3[Q B^8+sqrt(Q)B^16].

With A=Q^(5/16), B=Q^(1/16), r=8, Holder and the actual ratio energy give M^(15/16)Q^(3/128+epsilon)=Q^(63/128+epsilon)E^(15/16). The exact exponent at E=1 is (13/16)(15/16)+(27/16)/16-3/8=63/128. The boundary and the large-E trivial range are both paid by Q^(63/128+epsilon)E^2. Arbitrary harmonic-quadratic coefficients and all rectangular partial sums are covered. The smooth consequence costs the actual two-dimensional Abel variation and does not allow arbitrary bounded masks.

This is a character-sum theorem with its stated two-prime, short-disk and coset hypotheses. Its physical use requires the original root identity, full Poisson-frequency summation and uniform source-weight variation; those are separate from the argument certified here.

## C. Fixed-class physical application: complete review

### 1. Physical scope and original holes

The branch retains n=n'=1, all-Ec, c=C0b, c'=C0b', C0=Ea varpi, the original s labels/valuations, root factors, positive auxiliary orientation and complete old T-only restorer. The original raw normalization is unchanged. On w=u2v^2, counting both v roots with factor one half implements the physical selection without introducing an angular discontinuity. No arbitrary additional v/w mask is used in the scalar estimate.

The explicit square-class cross-hole count in Part II, Section 1 restores m divisible by q' or m' divisible by q at absolute cost P_aux^(-1) times polynomial-Z and fixed-exponential-source factors. It retains the original own-prime zeros. Since u2 is fixed and all other relevant labels are polynomial in Z, the distinct exponentially large primes avoid them for sufficiently large Z. On this support the own zeros are exactly the two cubic character zeros in v. The restricted same-class theorem was proved by an absolute masked count and therefore applies to this square-class mask with precisely its original raw exponents; these exponents do not absorb an arbitrary new polynomial multiplicity.

### 2. Complete small-period Poisson formula

After the exact mixed Gauss-root identity, all remaining m,m' arithmetic dependence is periodic modulo a polynomial-norm ideal J prime to qq'. For each v class modulo J, the residue equation Acoef x-Bcoef y=u2v0^2 has exactly NJ solutions, because Acoef=q'b'^2 and Bcoef=q b^2 are coprime. Writing m=x+jz and m'=y+jz' gives the exact integral equation Acoef z-Bcoef z'=t(v).

An inverse Abar modulo Bcoef yields the m coset x+j Abar t(v)+j Bcoef O. With ell in the original trace-dual lattice, its Poisson phase is constant times exp(2pi i Tr(ell Abar u2 v^2/(j Bcoef))). Replacing representatives changes the trace by an integer. In particular there is no unaccounted discontinuous large-inverse dependence in v: its entire dependence is a harmonic quadratic, on the selected small residue class.

The actual Fourier integral has covolume factor 1/N(j Bcoef) and the two original radial windows exactly as in (6). The roots leave opposite primitive cubic characters modulo q and q'. Remaining b/b' characters and zero masks are retained in the small-period table. No artificial same-orientation composite root or missing Gauss factor is introduced. Every ell, including those divisible by an auxiliary prime, remains in the decomposition.

### 3. Summable full-frequency variation

In the Fourier integral set z=sqrt(M)y. The first profile fixes y in a compact set; the other profile depends on (Acoef/Bcoef)sqrt(M/M')y-u2v^2/(Bcoef sqrt(M')). Normalizing q,q' by sqrt(P_aux) and v by sqrt(P_aux)R_V cancels every P_aux power in this expression. Fixed-order derivatives therefore have only polynomial-Z and fixed-exponential-source costs. For this fixed u2 its size is an allowed fixed constant.

The Fourier frequency in y is ell sqrt(M)/(j Bcoef), independent of v. Repeated integration by parts in y commutes with the two fixed v derivatives needed for Abel variation. Scaling the two real v coordinates contributes two derivative factors exactly cancelled by the variation integral's area Jacobian. Thus the stated bound with prefactor M/N(j Bcoef) and decay (1+Nell/H_freq)^(-K), H_freq=N(j Bcoef)/M, is valid. Choosing sufficiently many integrations gives any fixed K>1.

The complete dual-lattice sum is O(1+H_freq), including the zero frequency and all large frequencies. Both H_freq and its reciprocal have the allowed polynomial-Z/fixed-exponential-source bounds. Hence the entire frequency sum of Abel seminorms is of that type, with no positive P_aux power. The original restoring series is not differentiated: it changes only a single-column Gaussian T scale and is paid by its absolute coefficient sum and supremum. It changes neither the radial disks nor the Poisson lattice.

### 4. Applying the actual mixed-character theorem

For each fixed q,q', ell and small residue class, the product ideal has norm comparable to P_aux^2 and both local characters are nonprincipal cubic. The quadratic coefficient is arbitrary, exactly the domain allowed by the proved character theorem. Choose E0>=1 to cover NJ and the enclosing v norm disk divided by Q_mod^(1/2); E0 is at most polynomial-Z times exp(CA_source). This includes all source values through the theorem's large-E trivial branch. Every partial rectangle needed for two-dimensional Abel summation lies in a fixed comparable enclosing disk.

The character theorem gives Q_mod^(63/128+epsilon)E0^2 times the actual Abel seminorm. Summing all ell, the small residue table and all stated polynomially many labels preserves the allowed source factor. The two original M radial normalizers give P_aux^(-1). Since Q_mod^(63/128) is comparable to P_aux^(63/64), the result is P_aux^(-1/64+epsilon)Z^C exp(CA_source), after renaming epsilon.

This is uniform at each distinct auxiliary pair, so the original positive prime probability laws, of total mass one, require no extra distribution input or conditional renormalization. The fixed original source has every fixed exponential L1 moment by its theta weight and physical L2 normalization. Full source integration is therefore justified without a truncation.

### 5. Exact conclusion and remaining scope

The whole fixed-square-class scalar is now bounded, rather than only its fibre zero mode. Subtracting the exact same-class part gives the separately stated raw -49/48 price, or -25/48 with the actual row Na weight; multiplying by the original outside Z^(3/8) yields -31/48 and -7/48. The additional scalar error remains exponentially small. A further near-w removal may be paid by its explicit absolute v count as stated, rather than by an unsupported curved-mask partial-summation argument.

Part II alone does not provide uniformity over growing u2 or a sum over square classes; that extension is proved and reviewed in Part III. It does not estimate unrestricted different-free-norm Mobius pairs, change the observation, or imply a new spectral gap or zero exclusion. Those limitations are preserved by the final manuscript.

## D. Fixed-class physical application: independent source and frequency check

### 1. Exact physical source and period

I read all five bridge sections and returned to the complete raw summand in the publicly linked UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md. Once the actual two auxiliary Gauss factors have been combined, every remaining m-dependent character, original zero mask, and s-Gauss function is periodic modulo an ideal J of polynomial norm on this finite balanced branch. The b and b-prime characters are retained in this table, not deleted. The original finite ray choices also have fixed or polynomial period. The single-prime angular, root and restoring factors remain outside the v sum as actual bounded coefficients.

For A=q'b'^2 and B=qb^2, the branch hypotheses give (A,B)=1. For each v class modulo J, the map (x,y) to Ax-By modulo J is surjective, so there are exactly NJ compatible pairs. Writing m=x+jz and m'=y+jz' makes the remaining equation Az-Bz'=(u2 v^2-Ax+By)/j an integral equation. The inverse used in its parametrization is only A inverse modulo B. No inverse modulo BJ is assumed when b or b' intersects J.

The resulting m lattice is x+j z0(v)+jB O. Its Poisson phase is exactly the displayed constant times exp(2 pi i Tr(ell Abar u2 v^2/(jB))). The equality is on the fixed v residue class, and changes of representatives have integral dual trace. Thus every frequency, not merely zero frequency, gives a genuine harmonic quadratic in v. The two auxiliary cubic factors are primitive and nonprincipal at the two distinct primes. On fixed u2 and sufficiently large auxiliary primes, their zero values coincide with the true own-prime m and m-prime zero masks by reduction of the original equation at each prime.

The cross-prime holes can be restored with the independently checked absolute root count: m=q'k yields at most two roots for v modulo q, polynomially many k and v lifts in the actual disks, and the true pair radial normalization contributes P_aux^(-1). The full fixed source moments pay the fixed exponential dependence on its two parameters. This restoration is valid on the square stratum itself and does not borrow a bound for arbitrarily restricted complete columns.

### 2. The continuous Fourier coefficients and all-frequency sum

The covolume factor in (6) is 1/N(jB), with the two physical radial normalizers left outside. The Fourier kernel uses the original complete product of smooth radial windows. Substituting z=sqrt(M)y leaves the first window on a fixed compact set. In the second window, q=sqrt(P_aux)Q, q'=sqrt(P_aux)Q' and v=sqrt(P_aux)R_V V cancel every positive auxiliary scale: Q,Q' remain in fixed annuli and all residual ratios cost a fixed power of Z and a fixed exponential of A_source.

After this substitution the Fourier frequency is ell sqrt(M)/(jB), independent of v. Repeated integration by parts therefore gives the displayed norm-frequency decay, with H_freq=N(jB)/M. Differentiation in both real V coordinates and integration for the Abel seminorm only adds fixed profile seminorms and polynomial/source-exponential factors. Its area scaling cancels its two first-coordinate derivative scales. The coefficients are genuinely smooth and compactly supported, including at v=0; no square-root argument selection or sharp curved mask has been inserted.

Both the prefactor M/N(jB) and 1+H_freq have the claimed polynomial/source-exponential bounds. The fixed two-dimensional dual-lattice estimate sums the decay as O(1+H_freq). Consequently the entire frequency sum has the stated paid Abel-variation norm. This argument does not differentiate single-q roots or the restoring operator and does not require a small-frequency cutoff. Frequencies divisible by an auxiliary prime are included because the independently reviewed mixed theorem allows arbitrary quadratic coefficients.

### 3. Final application, source integration and scope

The v disk and NJ are covered by E0=Z^C exp(C A_source), so the character theorem applies to every partial coordinate rectangle used in Abel summation. Its uniform all-E0 statement is essential for full source integration. Summing the paid Fourier coefficients and residue tables gives Q_mod^(63/128+epsilon) times polynomial/source-exponential factors. The actual two radial normalizers contribute P_aux^(-1), while Q_mod is comparable to P_aux^2. The resulting scalar estimate is therefore P_aux^(-1/64+epsilon) Z^C exp(C A_source), and all fixed source exponential L1 moments make the last integration legitimate.

The two independent auxiliary laws are used only through their total probability one. Both roots and all original phases were retained until the uniform estimate. The old T-only restoring series has bounded coefficient l1 and changes none of the m lattice or frequency scales; its true Gaussian supremum is sufficient here.

The separately reviewed absolute same-class estimate permits its exact subtraction on this branch, with the raw and outside-normalized exponents distinguished in section 1. Those prices do not grant new unpriced label multiplicities. The scalar cancellation estimate permits no arbitrary bounded v mask. The optional near-w removal in section 5 instead uses its own absolute count, yielding P_aux^(-1/2-delta/2) times polynomial/source-exponential factors, so it does not misuse Abel summation on a curved sharp cutoff.

Conclusion: the complete fixed-square-class physical bridge passes this independent source, phase, full-frequency and source-tail review, using the independently proved character theorem in Part I. The result retains its same-E/common-a, n=1, all-Ec, fixed-u2 scope. It supplies no estimate for unrestricted squarefree u2, other branches, or the complete signed Mobius cross.

## E. Growing squarefree-kernel pool: complete review

### 1. Partition and original arithmetic support

The squarefree ideal factor of each nonzero (w) is unique. Choosing one generator per ideal and two unit representatives modulo unit squares gives a unique selected squarefree element u and v up to sign. The factor one half for the two roots therefore implements a disjoint partition. This does not require the chosen ideal generators to be multiplicative. The number of selected u of norm at most U is O(U), including units.

For fixed theta0<1, Nu<=P_aux^theta0 is smaller than both auxiliary prime norms uniformly once Z is sufficiently large. Thus the own-prime zero extensions are still exactly the two primitive cubic zeros in v. The additional psi(u/b0) is a unit-modulus scalar. Small-period data only read u modulo the existing J; no prime factor of u is inserted into the period. The map Acoef x-Bcoef y remains surjective modulo J for every u and retains exactly NJ solutions.

The cross-hole congruence still has at most two v roots modulo the relevant auxiliary prime. Its physical disk only shrinks with Nu, so its existing P_aux^(-1) absolute price is uniform. Its O(U) pool total is smaller than the stated scalar pool bound. Every other original hole remains in the finite table, including configurations where it makes the selected branch empty.

### 2. Full-frequency uniformity

Let U0=Nu. The actual support satisfies Nv<=P_aux U0^(-1/2) times the prior polynomial-Z/source factor. In the exact Fourier coefficient put z=sqrt(M)y and v=sqrt(P_aux)U0^(-1/4)R_V V. Then uU0^(-1/2)=u/|u|, so every size factor of u cancels from the second radial window. The remaining angular parameter lies on a fixed compact unit circle and does not enlarge any fixed smooth derivative bound.

The two real derivatives in the Abel seminorm contribute the inverse square of this positive v scale, while the area element contributes its square. They cancel exactly. The frequency ell sqrt(M)/(j Bcoef), its norm scale H_freq and its covolume prefactor are independent of u. The complete frequency decay and lattice summation from the fixed-class bridge therefore retain one polynomial-Z/fixed-exponential-source bound uniformly throughout the pool.

The harmonic quadratic phase coefficient may grow with u, but the proved character estimate is uniform in that coefficient. The same larger enclosing-disk parameter E0 applies to the now smaller v support and the unchanged NJ. The actual two radial normalizers and old restoring series have precisely their earlier costs. No source, period or derivative order is allowed to depend on u.

### 3. Summation and same-class bookkeeping

The preceding uniformity proves the same P_aux^(-1/64+epsilon) scalar bound for each class with one constant. The fixed original source has the required moments uniformly because the exponential-source exponent is fixed. Summing the disjoint O(U) classes gives U P_aux^(-1/64+epsilon)Z^C. The choice U=P_aux^(1/128) yields P_aux^(-1/128+epsilon)Z^C.

The same-class subtraction is a single previously proved absolute estimate with the union of classes as one bounded mask. It is not summed U times. Its raw -49/48 exponent, or -25/48 with the actual Na row weight, and the outside-normalized -31/48 or -7/48 exponents remain unchanged. Their original label-count restrictions are still required.

### 4. Verdict

All four sections are accepted with the independent full-source check below. This is a genuine estimate for a growing small squarefree-kernel pool in the specified original balanced branch. It does not grant arbitrary additional v masks, price the large-kernel complement or other compensation/n branches, or bound the complete signed Mobius cross term. No RH or new spectral-gap conclusion follows.

## F. Growing squarefree-kernel pool: independent full-source check

### 1. Partition, own-prime units and the remaining holes

Class number one and the two unit classes modulo squares give the stated partition: the squarefree ideal factor of (w) is unique; after choosing its generator, the remaining unit has a unique class modulo unit squares. The two square roots then differ by sign. Arbitrary fixed choices of ideal generators do not require multiplicativity for this argument. There are O(U) chosen representatives of norm at most U, including their finite unit choices.

For fixed theta0<1 and sufficiently large Z, Nu<=P_aux^theta0 is strictly smaller than each auxiliary prime norm. Thus both auxiliary primes are units for u, uniformly throughout the pool. The primitive cubic zero extensions continue to encode the original own-prime m and m-prime conditions. The factor psi(u/b0) is a unit-modulus coefficient, not a new v character of growing conductor.

Every other original hole stays in the same small-period table. Reading u modulo J does not require adding its prime divisors to J. If u shares a factor that the original physical support excludes, that table simply contributes zero. The residue map remains surjective with exactly NJ solutions regardless of the value of u modulo J. For the restored cross holes the quadratic congruence has at most two roots since u is an auxiliary unit; its real v disk decreases as Nu increases. Its P_aux^(-1) cost is therefore uniform, and summing it over O(U) classes remains smaller than the claimed pool bound.

### 2. Uniform full-frequency amplitude

Set U0=Nu. In the exact Fourier integral use z=sqrt(M)y and v=sqrt(P_aux) U0^(-1/4) R_V V. The identity u U0^(-1/2)=u/|u| cancels every size factor of u in the second physical window. The remaining angular parameter ranges over a compact unit circle. No angular derivatives of the arithmetic coefficients are needed. Fixed derivatives of the smooth amplitude are uniform in that parameter.

The Abel seminorm uses two real v-coordinate derivatives and the two-dimensional area measure. The derivative scaling is exactly the inverse of the area Jacobian, so no positive or negative U0 power is introduced. The Fourier frequency ell sqrt(M)/(jBcoef) and H_freq=N(jBcoef)/M are unchanged. The previously proved integration-by-parts and dual-lattice summation therefore give (5)-(6) uniformly in every u in the pool, with the same fixed source-exponential cost.

The actual quadratic coefficient contains u, but the approved character theorem is uniform in all such coefficients. It applies in the same larger enclosing disk E0 as before; using that disk only weakens the estimate. The old restoring operation and the original radial normalizers retain exactly their previous bounds.

### 3. Full source and the pool price

All source-exponential exponents in the uniform amplitude bounds are fixed independently of u. The fixed actual source's exponential L1 moments therefore justify integration with one uniform constant, including arbitrarily large source parameters. The scalar estimate for each class is P_aux^(-1/64+epsilon) Z^C. Summing the O(U) disjoint classes gives U P_aux^(-1/64+epsilon) Z^C. At U=P_aux^(1/128) the exponent is -1/128+epsilon; any remaining fixed polynomial Z is absorbed by a smaller fixed exponential saving.

The exact same-class subtraction is a single absolute masked count over the union of these classes. It incurs no factor U. Its raw and normalized prices, and the additional actual Na row-weight price, remain those of the separately approved theorem. No extra polynomial label multiplicity is silently absorbed in these polynomial exponents.

### 4. Scope

The result preserves the same E/common-a, n=n'=1, all-Ec branch and all original phases, periods and zero masks. No arbitrary additional v mask is permitted in the scalar estimate. The large squarefree-kernel complement and other physical branches remain unestimated. In particular the result does not estimate the complete coherent Mobius cross or imply a zero exclusion.

