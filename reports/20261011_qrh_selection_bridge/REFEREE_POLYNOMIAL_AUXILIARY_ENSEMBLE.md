# Independent mathematical review: polynomial auxiliary ensemble and covered low types

This review accompanies [POLYNOMIAL_AUXILIARY_ENSEMBLE.md](POLYNOMIAL_AUXILIARY_ENSEMBLE.md). It preserves the conditional finite-order Q assumption, the exact common-row/height scope and the open whole-probe/principal issues. Source-level proof checks are described below; no new formal-assistant build is claimed.

## Part A. High ensemble and complete local factors

### Verdict

Approved under the explicitly attributed user finite-order Q assumption, for the fixed compact A/B domains, polynomial norm/height/common-hole windows, and finite or genuinely absolutely convergent original selected-row sums stated in the note. This is an average of different admissible auxiliary observations. It is not an estimate for a previously fixed auxiliary observation and supplies neither a whole-probe low bound nor a common principal-signal theorem.

### Exact arithmetic and local domains

The original source's local family table and complete Euler identity were actually reread at pinned source lines 3995–4175. At each new prime xi_p=bar-chi_p is primitive and nonprincipal of order six. Reciprocity makes bar-chi_p(A)chi_A(p) a fixed bad-ray character on the retained domain. The prime-unit restriction is still present. The exact first-Poisson normalization, not a size inequality, removes the auxiliary Gauss norm. Consequently the complete resummed row multiplier is chi_p(u)/P_p, equivalently (4), including all scalar zeta, numerator-L, reciprocal-L and correction factors.

Independently expanding the source j=0 factor with SymPy gives exactly (6): the difference between the reconstructed numerator and the displayed polynomial is identically zero. On A, Rloc has size at most P^(-11/10), W at most P^(1/100), and the least Rloc W^2 term is P^(-27/25). DW uses x+w>=1+epsilon0. The other terms are smaller, so H-1=O(P^(-1-delta)) with the stated conservative delta. The corresponding B-domain estimates are stronger. The denominators 1-Rloc and 1-D are uniformly bounded away from zero for large P; so is H. The meromorphic identity defining the unextracted P_p is never used to divide by an uncontrolled zero.

On A, multiplication by (1-D)^(-1) costs at worst P^(-x)(1+P^(1/100))=O(P^(-1/2)), giving the two oscillating terms chi-chi^2 P^(-w). On B the error is O(P^(-7/8)). The A-domain exclusion of characters whose square has no good ramification is necessary and is explicitly retained. The second branch cannot be discarded or estimated by the nonprincipal prime theorem for a pure quadratic row.

### Q prime input and full common-height uniformity

The user's GENERAL_SELECTED_Q_GAIN source, especially its analytic-log estimate and prime-power correction, was actually reread. Nonempty good ramification survives every fixed bad-ray character used to restrict the prime pool. Q supplies an analytic logarithm on Re s>7/8. A fixed buffered Borel--Caratheodory argument from the Euler line gives the logarithmic conductor-height bound on Re s=29/32.

For a fixed smooth W, use Mellin inversion with its unchanged transform. Only the log-L integral is shifted. The norm exponent v enters the argument of log L; its imaginary part does not enter derivatives of W. Thus the integral costs log(C_theta(3+|Im v|)), with the displayed P^(29/32-Re v) factor, throughout the prescribed polynomial common-height window. Prime powers are separately estimated absolutely; the stated P^(1/2-Re v) log P bound is more than sufficient. This avoids raising an unspecified polynomial-height seminorm to the number of chosen primes.

With P=(log R0)^64 and N asymptotic to c P/log P, the worst A-domain prime saving has log-R0 exponent

64(3/32-1/100)-1=109/25>4.

All remaining log-log factors are absorbed in its strict margin. Restoring primes dividing the common hole or the row costs at most the number of such primes, O(log R0/log P), times P^(1/100), divided by N. This is negligible. All actual character zero values remain. Thus (10) is uniform over the same selected rows, common heights and allowed holes.

### Exact without-replacement averaging

For weights 0<=w_i<=1, the ordered distinct-tuple denominator is at least product_(j=0)^(k-1)(N-j), since each previously chosen index removes weight at most one. Hence e_k(w)>=(N-k)^k/k!. The logarithm estimate for product(1+t w_i z_i) follows from its linear term and the absolute quadratic remainder; sum w_i^2<=N. With A=mu+B sqrt(k/N) and |t|=k/(NA), the quadratic term is O(k), as is the linear term, and |t|B<=sqrt(k/N)<=1/2. Cauchy's coefficient estimate proves (11). The degenerate A=0 case has every weighted z_i zero and is immediate. This derivation keeps the exact positive weighted-subset normalization, rather than silently sampling with replacement.

The exact exponent calculations were independently checked with Fraction arithmetic:

16/25+(1-64)/2=-1543/50,

4/65-1/20=3/260>0.

Thus the collision term in A is smaller than (log R0)^(-4), and [C A]^k<=R0^(-1/20) for all sufficiently large R0. The threshold may depend on the fixed polynomial-window exponents and compact domains, as allowed. Also k log(2P)<=log R0 for all sufficiently large R0, proving the true polynomial total-modulus restriction for every sampled observation.

### What is and is not estimated

The ensemble law is independent of the chosen row and common height, so finite linearity proves (13) with arbitrary original amplitudes, masks, primitive labels and sharp cutoffs retained in A_u. A truly absolutely convergent infinite row sum is permitted only with its actual majorant. An open contour outside A/B, a conditional continuation or a row-dependent ensemble is not covered.

The unit resummed multiplier includes its deleted local P_p factors and is not one. A corresponding averaged principal signal must be proved separately. The growing ensemble does not contradict the fixed-modulus subpower number of residue-pattern projectors. No new conclusion about the original unaveraged same-E_b sum, the whole physical estimate or RH is drawn.

### Additional half-damped domain

Part A §7 is also approved. In the actual half-damped j=0 table, the only change is Rloc to Rloc/P. Thus the exact numerator identity (6) applies with this substitution. On C the new Rloc has decay exponent at least 1+6delta-6epsilon; the potentially costly D V W P term has exponent at least 3/2+delta-7epsilon. DW, VW and every other term also have a fixed margin beyond one. The assumptions epsilon<delta/8 and epsilon<1/200 ensure all denominators remain safe and Hhalf=1+O(P^(-1-c_delta)). This uses the true half-damped local identity, not the original local domain asserted on a lower line.

In Zhalf the D correction is O(P^(-1/2-delta)), the V correction O(P^(-1+6epsilon)), and the W branch O(P^(-1+epsilon)). All are O(P^(-1/2)). The mean of the leading chi term needs only nonempty good ramification, so the same exact ensemble proof applies to all these nonunit rows without imposing nonprincipality of chi squared. The finite/common-height/absolute-convergence limitations are unchanged.

At u=1 the full deleted multiplier is 1+O(kP^(-1/2)), uniformly in C; expansion of the finite product is valid because this sum of errors tends to zero. Its ensemble average is nonzero for sufficiently large R0. The explicit R0 dependence remains. This logarithmic closeness does not justify a fixed-principal Mellin continuation or a power-small physical comparison, and Section 7 correctly leaves that task open.

### Unrestricted-prime extension in Section 8

Section 8 was separately read and its source-level nonprincipality checked. The pinned source's fixed-numerator lemma, lines 646–690, identifies chi_bullet(u) on all good primes with the faithful Kummer character of K(u^(1/6))/K. For an integral sixth-power-free u, being a sixth power in K forces all finite valuations to be zero; its sixth root is then an Eisenstein unit, whose sixth power is 1. Thus only u=1 is principal. This includes, without discarding, the five other unit rows.

The conductor estimate is valid also when X^6-u is reducible. Its minimal polynomial is a monic integral factor; the discriminant factorization with the monic complementary factor and resultant shows that the minimal-polynomial discriminant divides the full polynomial discriminant. The field discriminant divides the order discriminant. Milne, Class Field Theory, Chapter V Theorem 3.27, was actually opened and read at https://www.jmilne.org/math/CourseNotes/CFT.pdf ; its conductor-discriminant product makes each character conductor divide the field discriminant. Taking norms of 6^6u^5 gives the displayed upper bound 6^12(Nu)^5. Character powers have no larger required discriminant bound.

The log-conductor input is therefore still O(log R0). In domains B and C the square-character branch is bounded absolutely, so no good-ramification or nonprincipality condition on that square is needed. Equations (12)–(13) consequently hold for every sixth-power-free u other than 1 in the single unrestricted good-prime ensemble, under the same finite/absolute convergence and common-height limitations.

This extension would be false if one silently conditioned the high average on a ray on which a bad-supported unit character becomes constant. The text explicitly does not do this. For uniform positive low bounds the supplementary product belongs to the same fixed finite total reciprocity group, which can be handled without a k-growing packet. The high average retains its original unrestricted law. The principal row remains an R0-dependent deleted multiplier, with the same unresolved full-signal comparison described above.

## Part B. Exact single-prime physical input

Status: approved for the stated complete nonprincipal cubic sector and polynomially bounded single moving auxiliary prime. No whole-probe uniform estimate is obtained.

I read the full manuscript, the pinned source's local-F prefactor, radial argument and bad CRT cancellation, and the actual all-n/marked-dual scale identities used in its transfer.

### 1. The auxiliary norm is canceled in the true expression

The source explicitly gives the outside first-Poisson factor sqrt(X)/(sqrt(Nb*) NA), with Y^{-1} separate. The primitive bad Gauss factor supplies sqrt(Nb*) tau xi(A) conjugate(xi(H/s)). All accompanying corrections cancel coefficientwise, using xi(a)^6=1, leaving only conjugate(xi(u)). The true radial argument is X NH/NA and has no auxiliary modulus. Thus the reassembled expression really has outside sqrt(X)/Y and no positive power of the new P. This holds before square-layer or odd-branch decompositions and is not inferred by dropping a fixed-data factor in an inequality.

Changing b0 to b0 p inserts a bounded frequency-row phase and the stated p-unit restrictions. It does not add a p-conductor to the free inverse or smooth character family. The original small bad-ray group remains fixed. All six units are retained; the auxiliary phase need not be trivial on them because it is only a bounded row scalar here.

### 2. Inverse and smooth holes are separately paid

All outer p restrictions are retained in positive sums. The c2-hole changes its true inverse Dirichlet series by division by one Euler factor. On the buffered positive reciprocal contour that factor is uniformly bounded; fixed-order derivatives cost only powers of log P. Its local zeros lie on real part zero and therefore introduce no new positive-real-part zero condition. The underlying zero-bin density input remains the original S0 family, positively restricted, rather than an asserted uniform theorem for a new large fixed conductor.

The smooth-column hole has the exact finite identity B(S)-psi_w(p)B(S/P), with the actual rotation and compact norm test. The common coefficient seminorms are uniformly preserved under the normalized rotation. The whole reciprocal e0 sum, not a single S block, is then used. Since L/S is independent of e0, setting S'=S/P gives the exact factor P^{sigma-1}. The genuine contours are below one by a fixed margin, so this costs no positive power. The measure dS/S and its true finite support are handled in the same order as in the reviewed marked proof, including the long-Poisson tail and subunit/empty annuli.

Equivalently merging the new prime with the ordinary f mask gives exactly two terms and the same nonpositive f exponent. There is no count of P possible divisors. The original selected primes are assumed outside p, so their rational moments remain in the same coefficient class. The extra inverse factor and the auxiliary phase are bounded row weights, while the new smooth hole is explicitly expanded before the moment estimate.

### 3. Complete scope and constants

These operations preserve the original high-M and small-M all-scale cubic envelopes, the n0 pooling and the strict r_phys/a' tails. Optional half-damping is applied only at its previously reviewed positive stages. For every preassigned P<=Z^C, logarithmic derivative and divisor-small losses are absorbed by the displayed ambient epsilon powers with constants depending on C and fixed S0/profiles. The preexisting existential cubic gain may be slightly decreased when reserving these losses, as the statement permits.

The conclusion is for eta=1, one prime outside S0 and the actual selected slot supports, any admissible nonprincipal local character of order dividing six, both original/core nonflat markers, and either the original n weight or its reviewed half-damping. It retains the existing finite-order Q assumptions. It does not supply uniform completed-row R2, other core sectors, principal high comparisons, a bound for the unaveraged same-E sum, or a scale-dependent many-prime extension.

## Part C. Direct simultaneous cubic low bound

Approved as the stated extension of the independently reviewed single-prime full cubic bound. The scope is eta=1, the original or half-damped physical weights, the original/core nonflat markers, and the complete nonprincipal cubic sector under its existing Q assumptions. No whole-probe, unit-core, other local type, first-flat or high-side principal theorem is supplied.

The proof correctly performs one simultaneous CRT/first-Poisson transformation for b0*b. The auxiliary Gauss norm cancels its literal normalization, leaving the fixed radial scales and a unit-modulus row phase. It does not iterate a theorem with an unknown constant once per prime. The original fixed ray group is retained; no unbounded character-packet expansion is inserted.

Every added b-unit restriction on an outer variable or row remains a positive restriction. On the inverse column, the actual correction is the product J_b over p|b. Its denominator has no zero at positive real part. On the fixed buffered contours 1/2+delta<=sigma<=9/10, its absolute product is bounded by exp(O(k P^(-1/2-delta))). The underlying primitive family and original selected zero labels are unchanged apart from genuine b-unit restriction.

The smooth-column mask is expanded once over all d|b, preserving the actual profile, norm dilation and rotation. The complete physical e0 sum has reciprocal measure dS/S and the exact same ratio of its two true scales as in the single-prime proof. Substituting S'=S/Nd therefore contributes (Nd)^(sigma-1) before the final positive all-scale enlargement. Summing these genuine weights gives product(1+Pp^(sigma-1)), not 2^k. Its logarithm is at most kP^(-1/10). With P=(log R)^64 and k<=log R/(65 log log R), both product costs tend to zero in the exponent and are uniformly O(1).

For each fixed needed derivative order, differentiation of J_b produces finite polynomials in sums of decaying prime terms times powers of log Pp; these are bounded by fixed powers of log R. The d-dilation derivatives cost at most (1+log Nd)^J<=(1+log R)^J and the same already summed positive d weights. Thus the required common-mode seminorms are ambient-subpower, without an untracked C^k factor. Rotations retain bounded phases.

The old rational selected-slot proof accepts these common holes and bounded row phases. The same all-e0 envelope, small-conductor case, primitive conductor blocks, n0 pooling, r/a-prime strict tails and Gaussian/Fourier tails apply. The buffers can be chosen inside the stated sigma range because the old Q-capped upper endpoint is 7/8; the gap to 9/10 is positive. Any small powers are paid after reserving a fixed positive amount of the old existential cubic saving. This proves the stated bound uniformly for each b, and hence for any normalized finite ensemble by triangle.

The prime-pool disjointness from original selected slots is explicitly required (and holds for sufficiently large Z in the stated polylogarithmic construction with fixed positive slot exponents). This extension does not by itself cover other core types or establish the matching principal normalization needed for a full ensemble argument.

## Part D. Six other covered physical types

### Verdict and hypotheses

Approved for eta=1 and the six listed already covered nonprincipal core types, original/core nonflat markings, original or half-damped physical n weights, and squarefree auxiliary b of norm at most Z^C disjoint from the fixed bad set and selected slots. Every new local auxiliary character must be nonprincipal of order dividing six. All original Q hypotheses and norm/common-mode restrictions remain. This is a uniform transfer of the already proved positive upper envelopes, with an ambient (Nb Z)^epsilon loss, not a new exponent calculation or a whole-probe theorem.

The source-level identities and actual all-e interfaces were read again, rather than substituting the cubic-sector estimate for the other types. The original first-Poisson source at lines 3742–3845 was previously checked for its exact normalization; its cancellation is independent of the frequency core type. The current readback includes the full quadratic-density physical equations (11)–(13), the pure-fifth physical bridge (1)–(5), the user's 92d2 pure-fifth selected-Q proof and multiplier (0)/(A), the complete pair-Q-slot proof Sections 1–2, complete cubic-fifth mixed Sections 1–3, complete joint 234 Sections 3–4, and complete three-core mixed (8)–(11) and its actual-row long-tail explanation.

### Common exact transformation

Before any type decomposition, the first-Poisson factor sqrt(X)/(sqrt(Nb*)NA) is multiplied by the literal primitive bad Gauss magnitude sqrt(Nb*). The remaining character calculation leaves bar-xi(u6), because xi(a)^6=1. All auxiliary conductor size cancels at this step; the radial argument is unchanged. The product auxiliary is primitive since its coprime local factors are nonprincipal. Its normalized root is kept, not expanded into a large residue-class packet.

Thus the new data consist of a bounded joint-row phase and genuine unit restrictions. There is no new free-column moving auxiliary character. These restrictions must be imposed before any positive enlargement, including on odd branches, square layers and extracted ordinary mask factors. The original fixed reciprocity group has only its fixed finite options.

On the common inverse column, deleting b multiplies its true inverse series by product_(p|b)(1-eta(p)psi(p)P^(-v))^(-1), with the original conjugation convention. On any preselected compact interval 1/2<sigma_min<=Re v<=sigma_max<1, this product and every required fixed derivative are O_epsilon((Nb)^epsilon). This follows by separating finitely many small primes and bounding each remaining local contribution by an arbitrarily small prime-norm power; logarithmic derivatives add only fixed powers of log Nb. It neither changes the primitive zero family nor adds a positive-real-part local zero.

The smooth-column hole has the exact finite divisor expansion in Section 3. Its original rotations and compact weights stay attached to each d term. Every relevant all-e interface has reciprocal e measure and L/S independent of e. For fixed d, setting S'=S/Nd gives the exact scalar (Nd)^(sigma-1), before enlarging the true finite range into the complete positive all-scale envelope. The divisor sum is product_(p|b)(1+P^(sigma-1))=O_epsilon((Nb)^epsilon), uniformly for arbitrarily many primes. No iteration of unspecified fixed-prime constants, nor a replacement by 2^omega(b), is used.

### Actual sector interfaces

For the quadratic type the readback gives L/S=U q_j^2 q_f/(Y' N^2 B^2), and its full finite-e result contains q_f^(-a), a=1-sigma. Replacing f by the added coprime d f is exactly the preceding d^(-a) price; the existing (NB)^(-1+2a) and q_j^(-2a) weights remain.

For the pure-fifth type the original exact interface is L=C_l/(q_r^6Gq_e), S=Y*/(Gq_eq_f), with unchanged eta(e)/q_e. Its all-scale envelope therefore gives the same d^(-a) factor and retains the actual fifth boundary h0|w, physical square cutoff and full Schwartz tail. The user's selected-Q identity (0) already includes arbitrary common holes. The new auxiliary phase is outside the selected prime column; it is not inserted into the fixed ray factor of a slot. Consequently the user's sharper -209/960 exponent, rather than the superseded -63/320, is retained.

For mixed (3,5), the physical odd/square interface is the same genuine quadratic one with the fifth boundary and its restored character. The restricted pair-Gram and smooth alternatives accept bounded joint-row coefficients; the true long-S tail is paid per actual row before integration. The rational 4351-box envelope is unchanged.

For mixed (2,4,5), the source ratio C_l q_f/(R^6N^3Y*) and outside N^(-3/2+3a) remain. The already paid moving-fifth conductor is unchanged; no auxiliary conductor enters it. The same all-e comparison and true physical boundary cases apply.

For mixed (2,3,4) and (2,3,4,5), the displayed ratios are C_l f tau/(R^6 A^3 N^2 B^2Y'), with outside A^(-3/2)/(NB). The source explicitly retains the reciprocal-e integral and both actual free columns. The resulting A^(-3/2+3a)(NB)^(-1+2a) is unchanged. Their pointwise/moment alternatives, actual primitive conductor blocks, selected-slot masks, fifth shell W/H0 where present, and complete long-Poisson tails are the original ones. Thus the verified rational envelope and strict outer summability margins survive.

All six arguments include the new external Nb in the ambient before infinite outer sums. The preexisting strict label exponents absorb their own small powers; the externally polynomial Nb loss is reserved when choosing the initial epsilon. Optional half-damping is inserted at the fixed n0/r positive stage already reviewed, not by comparing signed completed sums.

### Preserved numerical and logical scope

The retained normalized exponents are -439/2304, the user's -209/960, -3073/16384, -133/34560, -1/512 and -1/512 for the six types in the stated order. The transfer excludes unit cores, residue-1 missing types, the exclusive-s observation, first-flat operations, full completed-theta R2, and any whole-probe high/low comparison. A normalized auxiliary ensemble inherits these uniform low bounds by triangle, but no signed high estimate follows from that triangle step.

## Exact moving-hole phase correction

The user’s correction in commit 3c92c606 is mathematically required: the former Part XXVII B (13) must include the outside conjugate moving phase barρ_u(d). Splitting the original moving coefficient and applying Gauss CRT give two distinct factors, so the phase-free signed identity is not valid. The norm-7/norm-31 coefficient example supplied by the user demonstrates the mismatch. The corrected outside phase has modulus one on the actual support, and the old absolute bounds survive.

The current high ensemble is instead derived from the original first-Poisson bad CRT and the full local P_p deletion. Its low-transfer proofs use the explicitly phased smooth mask and the actual inverse Euler correction; they do not use the faulty rearrangement. The user's corrected proof and attribution are retained in [REFEREE_MOVING_HOLE_PHASE.md](REFEREE_MOVING_HOLE_PHASE.md).
