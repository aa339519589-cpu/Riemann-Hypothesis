# Polynomial auxiliary ensembles on the same selected rows

Independently reviewed mathematical supplement. The finite-order Q hypothesis is explicit throughout the arithmetic bounds below. This is a new ensemble of admissible observations; the original fixed-auxiliary observation is not replaced by an identity with its average.

The main positive result is a uniform R₀^(-1/20) bound for the exact auxiliary multiplier on the SAME selected rows and common height box, including its full local Euler deletions. In the unrestricted good-prime ensemble, domains B and C cover every sixth-power-free row u≠1, including the five nontrivial units. The actual u=1 multiplier stays nonzero in C but depends on R₀. Separate physical arguments preserve the complete cubic and six other covered nonprincipal NONFLAT low bounds uniformly over the stated auxiliary moduli.

No matching whole-probe low theorem or fixed principal-signal comparison is established here. Unit cores, missing residue-1 types, the exclusive-s marker, and first-flat observations are outside the low-transfer conclusions. The finite/common-height high estimate extends to infinite sums only when their actual absolute majorant has been proved; it is not a conditional-contour interchange or an RH proof.

Parts A–D retain complete proofs of the high estimate, the necessary exact single-prime physical calculation, its direct many-prime extension, and the six other covered physical types. Equation numbers restart within each part.

## Sources and an exact signed-identity correction

The common original source is [the pinned September 30 QRH manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), equations local-F, local-full-coefficient and local-unit-factor. The complete sector estimates are in [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md); the genuinely new half-damped observation is defined in [HALF_DAMPED_PROBE.md](HALF_DAMPED_PROBE.md). The user's [finite-order Q input](FORMAL_INPUT_Q.md) and [GENERAL_SELECTED_Q_GAIN.md](GENERAL_SELECTED_Q_GAIN.md) are inherited with their stated finite-order and common norm-mode restrictions. No new Lean build or infinite-order Q assertion is claimed. The sharper pure-fifth exponent is the user's [PURE_FIFTH_SELECTED_Q_GAIN.md](PURE_FIFTH_SELECTED_Q_GAIN.md).

**Formal mathematical correction, first identified and supplied by the user in commit 3c92c606af566f64621e17e9533aaac9deab6719.** The previously published Part XXVII B §6, equation (13), omitted an outside moving-character phase. With its actual definitions, the correct signed identity is

\[
 R_{(u,M)}(s)=\sum_{d\mid M_0}\mu(d)G(d)\chi_0(d)\,
       \overline{\rho_u(d)}(Nd)^{-s}R_{ud}(s).
\]

Indeed inclusion–exclusion gives A=dB. Splitting the pre-existing coefficient \(\bar\rho_u(dB)\) produces the outside \(\bar\rho_u(d)\), whereas the Gauss CRT factor in \(G(dB)=G(d)G(B)\bar\rho_d(B)\) changes the remaining moving parameter to ud. These are distinct phases. The zero masks extend the identity to nonsquarefree dB. The omitted-phase identity is false and must not be used in a signed argument. Since (d,u)=1, the new outside phase has modulus one; the stated absolute U^(1/4) and common-hole M^ε bounds are unchanged. See the user's [full coefficientwise correction and norm-7/norm-31 counterexample](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c191be4053479df9bc44f8c5e583fdf041ddcd44/reports/20261011_qrh_selection_bridge/REFEREE_MOVING_HOLE_PHASE.md).

This correction is preserved in the user's original files. The high identity in Part A below is derived directly from the original first-Poisson CRT and deletion of P_p, not from the erroneous moving-Gauss-hole rearrangement. The ordinary smooth-column hole identities in Parts B–D explicitly retain their factors μ(d)ψ_row(d), and their reciprocal Euler corrections retain the corresponding moving-character values. Thus the old omitted phase is not used to obtain this ensemble theorem.

## Part A. Exact auxiliary averaging and the unrestricted prime pool

### 1. Fixed data, exact objects, and scope

Keep the original field K=Q(sqrt(-3)), target eta, excluded set S0, auxiliary xi0 modulo b0, and fixed finite reciprocity ray group. Fix a prime ray class in a fixed refinement carrying all these data. Fix 0<=W<=1, smooth, nonzero and supported in [1,2]. All constants below may depend on this fixed data and on the fixed compact real-part domains specified below.

Assume the user's finite-order Q input: every nonprincipal finite-order Hecke L-function has no zero in Re s>7/8, with the standard uniform fixed-field growth used in the already reviewed user [GENERAL_SELECTED_Q_GAIN](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/113702dd9ff055b343a89d2667fb9ff72783de97/reports/20261011_qrh_selection_bridge/GENERAL_SELECTED_Q_GAIN.md). No infinite-order twist is assumed to satisfy Q.

Let R0 tend to infinity, and fix A0,A1,A2. Every retained original row u has Nu<=R0^A0, every additional common hole has norm at most R0^A1, and the COMMON contour heights obey |Im x|+|Im w|+|Im z|<=R0^A2. The row set E can be any finite subset of the original bad set, defined using its original primitive characters and selected zeros. No zero is moved to a different row.

For the first real-part domain below require that both chi_bullet(u) and its square have nonempty GOOD ramification disjoint from S0. This includes every nonunit complete cubic row u=epsilon v^2 and genuinely cubic-containing mixed rows. It excludes pure quadratic good cores and unit cores. On the second, positive-w domain, only chi_bullet(u) needs nonempty good ramification.

The two domains are fixed compact subsets of the original normal-convergence regions:

 A: Re x>=51/100, Re z>=17/50, Re w>=-1/100,
    Re(x+w)>=1+epsilon0, epsilon0>0 fixed;

 B: Re x>=7/8, Re z>=33/200, Re w>=19/20.

These are domains for an actually resummed original Euler row. An open contour outside these regions is not included by assertion.

### 2. The actual auxiliary ensemble has polynomial total modulus

Set L=log R0, ell=log log R0,

   P=L^64,       k=floor(L/(65 ell)).                        (1)

Let the pool consist of the good primes in the fixed prime ray class with W(Np/P)>0, and write w_p=W(Np/P), N=sum_p w_p. The fixed-ray prime normalizer from the original source gives N asymptotic to c_W P/log P, with c_W>0. In particular k=o(N).

Choose an UNORDERED k-element subset J of DISTINCT pool primes with probability

   Prob(J) = product_(p in J) w_p / e_k((w_p)_p),            (2)

where e_k is the k-th elementary symmetric coefficient. This is a genuine positive normalized finite probability law; no replacement samples or collision error are discarded.

For each J set B_J=product_(p in J)p, S_J=S0 union J, and at the new p use xi_p=bar chi_p. Every xi_p has exact order six and is nonprincipal, so this is allowed by the original definition. Moreover

   NB_J <= (2P)^k <= R0                                     (3)

for all sufficiently large R0. The original literal sharp inverse and physical windows remain the ones attached to this actual S_J observation. They are not replaced by a smooth inverse. The added completed-row Xi factor is a product of fixed reciprocity-ray characters, by the exact identity bar chi_p(A)chi_A(p)=R(A,p)^(-1).

### 3. The removed local Euler factors are retained, not dropped

For p not dividing u put chi=chi_p(u) and use the original notation

 V=Pp^(-6z), Wloc=chi Pp^(-w), D=eta(p)bar chi Pp^(-x),
 H_p=P_p(1-V)(1-Wloc)/(1-D),       Pp=Np.

Define the exact resummed auxiliary multiplier

   Z_p(u;x,w,z)
     = (1-V)[chi-chi^2 Pp^(-w)]/[(1-D)H_p].                 (4)

At a prime dividing the original row or a stipulated common hole define it as zero. On units (4) is exactly chi_p(u)/P_p, with meromorphic continuation understood after clearing denominators. For sufficiently large pool primes H_p stays uniformly away from zero in A and B, so the displayed right side is directly defined, even where an unextracted P_p has a pole.

Thus the complete original row with all primes J deleted, multiplied by its new auxiliary phase, is exactly the original S0 row multiplied by

                       product_(p in J) Z_p.              (5)

This includes removal of the scalar zeta local factor, the numerator L local factor, the reciprocal-L local factor, and the full local correction. It is not merely a product of bare residue characters.

For completeness the needed elementary local estimate follows from the original j=0 formula. Put Rloc=a_p^2 Pp^(4-6x-6z). Writing
H_p=N_p/[(1-Rloc)(1-D)], direct expansion gives

 N_p-(1-Rloc)(1-D)
 = D Wloc
   +Rloc[-D+V Wloc^2-Wloc^2+Wloc/Pp+1-1/Pp]
   +V[D Wloc^2 Pp-D Wloc^2-D Wloc Pp+D-Wloc].               (6)

In A the right side is O(Pp^(-1-delta)), for any fixed
0<delta<min(epsilon0,1/25). For example the least Rloc Wloc^2 exponent is 1.08 and the D Wloc exponent is at least 1+epsilon0. In B all terms also have exponent strictly greater than one. The two denominators are uniformly bounded away from zero. Consequently, uniformly in ALL imaginary parts,

 A: Z_p=chi-chi^2 Pp^(-w)+O(Pp^(-1/2)), |Z_p|<<Pp^(1/100);
 B: Z_p=chi+O(Pp^(-7/8)),                 |Z_p|<<1.        (7)

The first estimate keeps the second oscillating branch. If chi^2 has no good ramification, that branch cannot in general be estimated by the same nonprincipal prime theorem; this is the reason for the explicit exception in section 1.

### 4. A logarithmic-height form of the actual prime-Q input

We record the height cost rather than raising an unspecified polynomial seminorm to k. For a finite-order nonprincipal character theta whose good ramification cannot be cancelled by the fixed prime-ray restriction, Q gives an analytic log L on Re s>7/8. Borel--Caratheodory from a fixed Euler line and standard fixed-field Hecke growth give

 |log L(29/32+it,theta)| << log(C_theta(3+|t|)).             (8)

This is the same buffered log-L step as in the user's reviewed prime-slot proof. With the FIXED norm weight W, Mellin inversion and shifting only the log-L integral to Re(s)=29/32 give, uniformly for v in a fixed compact real strip,

 |sum_p w_p theta(p)(Np)^(-v)|
 << P^(29/32-Re v) log(C_theta(3+|Im v|))
       + P^(1/2-Re v) log(2P).                            (9)

The finite fixed ray expansion is included in this formula. In the integral the Mellin transform is that of W itself. The imaginary part of v enters log L, not derivatives of W; integrating its logarithmic growth against the fixed rapidly decreasing Mellin transform gives the displayed logarithm. The prime-power correction uses absolute values, so introduces no height power. Constants remain uniform on the specified compact real-part strip.

For the characters chi_bullet(u) and, in A, chi_bullet(u)^2, their actual inducing conductors are bounded by a fixed power of Nu times fixed data. Their good ramification proves nonprincipality after every fixed prime-ray twist. The full zero extension at ramified primes is retained. Since log(C_theta(3+|Im w|))=O(log R0), dividing (9) by N and using (7) gives

   |N^(-1) sum_p w_p Z_p| <= L^(-4)                       (10)

for all sufficiently large R0, uniformly in u and in the complete common-height window. Indeed the worst exponent in A before harmless log log factors is

 64(3/32-1/100)-1 = 109/25 > 4.

Also |Z_p|<=C L^(16/25). Removing p dividing a common hole of norm<=R0^A1 costs at most
O(P^(1/100-1) log R0), smaller than (10). On B the same conclusion is stronger and needs only the original character to be nonprincipal.

### 5. Exact no-replacement estimate

Here is the finite elementary-symmetric lemma used to keep the normalization and all collisions exact. Let 0<=w_i<=1, N=sum_i w_i, and |z_i|<=B. Put

   mu = |sum_i w_i z_i|/N,
   A = mu+B sqrt(k/N).

If 1<=k<=N/4, then

 |e_k((w_i z_i)_i)|/e_k((w_i)_i) <= [C A]^k               (11)

for an absolute C. Proof: the ordered distinct-tuple denominator is at least
N(N-1)...(N-k+1), because after j distinct indices the total removed weight is at most j. Thus e_k(w)>= (N-k)^k/k!. For |t|B<1,

 log |product_i(1+t w_i z_i)|
 <= N mu |t|+N B^2|t|^2/[2(1-B|t|)].

Choose |t|=k/(N A). Then B|t|<=sqrt(k/N)<=1/2. Both terms in the last bound are O(k). Cauchy's coefficient bound, k!<=k^k, and N/(N-k)<=4/3 give (11). No unweighted sampling approximation is used.

For (10), B<<L^(16/25) and N comparable to L^64/log L, whereas k comparable to L/log L. Hence

 B sqrt(k/N) << L^(-1543/50) = o(L^(-4)).

Equations (10)--(11) prove the following uniform power estimate for the ACTUAL resummed multiplier:

  |E_J product_(p in J) Z_p(u;x,w,z)| <= R0^(-1/20).        (12)

Indeed the exponent is 4/65-o(1), and 4/65>1/20. The implied threshold is uniform over all the stated rows, holes and heights. No density hypothesis on E is used.

### 6. Same-E consequence and exact limitations

At any one common point (x,w,z) in the specified domains where the original S0 row amplitudes A_u are finite, and for ANY finite fixed selected set E satisfying section 1,

 |E_J sum_(u in E) A_u product_(p in J) Z_p|
       <= R0^(-1/20) sum_(u in E)|A_u|.                   (13)

In particular every primitive conductor, root, original sharp cutoff, selected-zero indicator and original outside coefficient can remain inside A_u. The chosen ensemble is independent of the row and of the common height within the prescribed window. An actually absolutely convergent row sum can be passed through (13) with its real majorant. A conditionally continued infinite row sum or an open contour outside A/B requires further proof.

For bare finite post-Poisson blocks, the identical argument with z_p=chi_p(u) gives the same bound without local resummation. For the unit row the bare phase is 1, but its RESUMMED row is still changed by the full product of removed P_p factors. This note does not assume its principal analytic normalizer is identically one.

This construction averages many different admissible bad moduli, each of norm at most R0. It therefore does not contradict the earlier fixed-modulus bound 3^omega(B)=B^o(1), and it cannot be quoted as a saving for any one original fixed auxiliary observation.

A complete use still needs a matching uniform WHOLE-probe low estimate and principal signal on the same ensemble. Parts B–C below prove the direct complete-cubic many-prime extension, and Part D handles the six other explicitly listed nonprincipal types. They do not supply the missing unit and residue-1 low estimates or the complete principal comparison. Their direct whole-modulus arguments, rather than k iterations of a fixed-prime theorem with untracked constants, are essential.

### 7. The reviewed half-damped observation admits a critical high window

This additional domain is specific to the already reviewed half-damped observation at eta=1, published as [HALF_DAMPED_PROBE.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c541a15554733bb4d71a08dc6d84d19d3e73433f/reports/20261011_qrh_selection_bridge/HALF_DAMPED_PROBE.md). Its exact local equation (1), state j=0, changes ONLY Rloc to Rloc/Pp in the original unramified formula; V, Wloc, D are unchanged. We use no such simplification at ramified states j>=1.

Fix delta>0 and 0<epsilon<min(delta/8,1/200). On a fixed compact real domain

 C: Re x>=1/2+delta, Re w>=1-epsilon,
    Re z>=1/6-epsilon,

the same polynomial identity (6), now with Rloc'=a_p^2 Pp^(3-6x-6z), gives

   H_(p,half)=1+O_delta(Pp^(-1-c_delta)), c_delta>0.

For example the bare Rloc' exponent is at least 1+6delta-6epsilon, while the potentially larger DVWloc Pp term has exponent at least 3/2+delta-7epsilon. The other terms have strict margins as well. The exact half auxiliary multiplier is therefore

   Z_(p,half)=chi_p(u)+O_delta(Pp^(-1/2)),                 (14)

uniformly in all imaginary parts. Repeating sections 4--5 proves (12)--(13) on C for EVERY nonunit row with nonempty good ramification; no extra nonprincipality of chi^2 is needed because the second branch has the absolute factor Pp^(-Re w). Thus this extension really reaches an arbitrary fixed distance delta>0 to the right of 1/2 at the scalar residue window, with the full local deletions paid.

For the unit row the raw auxiliary character is 1, and (14) instead gives

  product_(p in J) Z_(p,half)(1)=1+O_delta(kP^(-1/2))
                              =1+O_delta(L^(-31)/ell).   (15)

The same holds after the ensemble average, uniformly in the stated domain, so this factor is nonzero for all sufficiently large R0. It is nevertheless a function of R0. If R0 is tied to the physical scale Z, (15) is only logarithmically small, not a power-small error relative to a fixed principal Mellin signal. A continuation theorem requiring a FIXED principal multiplier cannot simply be quoted for it. One must either prove a suitable uniform varying-multiplier version, or realize and price an exact principal Euler normalization. Neither step is supplied by (15), and no complete high/low comparison follows here.

### 8. Unrestricted good-prime pool: all nonprincipal sixth-power-free rows

There is a useful separate version of sections 2--7 in which the pool is ALL good primes outside S0, with the same norm weight W, rather than a single fixed prime ray class. Keep this unrestricted ensemble through the signed high average. On domains B and C, conclusions (12)--(13) then hold for every original sixth-power-free element u other than u=1, including the five nontrivial unit rows.

Here is the exact nonprincipality and conductor verification. The original fixed-numerator lemma identifies theta_u(p)=chi_p(u) with the faithful character

 Gal(K(u^(1/6))/K) -> mu_6,  sigma -> sigma(u^(1/6))/u^(1/6).

It is principal precisely when u is a sixth power in K. For a sixth-power-free integral u, a root v in K with v^6=u must have zero valuation at every finite prime: the valuations of u lie in {0,...,5} and are divisible by six. Thus v is a unit of the Eisenstein integers. Its unit group is mu_6, so v^6=1 and u=1. In particular a nontrivial unit does define a nonprincipal finite-order character on the FULL good-prime monoid; no claim is made that it stays nonprincipal on a restricted bad ray.

A polynomial conductor bound, including the bad primes, can be made explicit. If g is the minimal polynomial of u^(1/6), then g is a monic integral factor of X^6-u. The polynomial discriminant factorization and the order/field discriminant relation imply

 disc(K(u^(1/6))/K) divides disc(X^6-u) = (+/-)6^6 u^5.

The conductor-discriminant formula for this abelian extension implies that the finite conductor of theta_u divides this field discriminant. Hence

                  C_(theta_u) <= 6^12 (Nu)^5.             (16)

This also handles reducible X^6-u: use the integral complementary monic factor and its resultant in the discriminant product. The same bound applies to powers of theta_u by the conductor-discriminant formula. Primary reference actually checked: Milne, Class Field Theory, Chapter V, Theorem 3.27, https://www.jmilne.org/math/CourseNotes/CFT.pdf . The Kummer identification itself is the original source's fixed-numerator lemma.

Thus the logarithm in (8)--(10) is still O(log R0) for every u in the stated full norm range, with all heights retained. In B and C the second branch was paid absolutely, so theta_u squared need not be nonprincipal. The elementary-symmetric proof is unchanged. The only principal exception is u=1, whose full deleted multiplier was explicitly kept in (15).

On the physical side, no prime-ray restriction is needed to define the original probe. For any subset J, the product of supplementary factors from (1) is R(A,B_J)^(-1). As a character of A it lies in the SAME fixed finite reciprocity group T, independently of k and NB_J. For a uniform positive low bound one may partition by this finite total T option, or use the already bounded row phase directly. There is no expansion into a number of options growing with k. This does not authorize conditioning the signed HIGH prime average on that total T option: doing so can precisely destroy the cancellation of a bad-supported unit character. The high average in this corollary remains the single unrestricted ensemble (2).

## Part B. Exact single-prime complete-cubic physical uniformity

### 1. Objects and conclusion

Fix the original target eta=1, original bad set S0, ray group T, primitive auxiliary xi0 modulo b0, original finite disjoint positive prime slots, physical windows, and original sharp inverse. Let p be a good prime outside S0 and the actual selected slot supports. Write P=Np. Put S=S0 union {p}, b*=b0 p and xi=xi0 xi_p, where xi_p is any nonprincipal residue character modulo p of order dividing six. All original frequency units epsilon are retained.

At a fixed p this is precisely an admissible original probe. Its c,n,s,a variables avoid p, and its first Poisson frequency avoids p. In particular the original/core marker and finite scale compensation are defined with this same enlarged bad set. The optional half-damping multiplies each physical n by Nn^(-1/2). Only nonflat observations are asserted here.

The reviewed uniform conclusion is that the already reviewed complete nonprincipal cubic estimate remains valid with cost (PZ)^epsilon, uniformly for P<=Z^C for every preassigned fixed C:

 |I_cubic,S,xi(Z)| <<_(epsilon,C,S0,profiles) (PZ)^epsilon Z^(-271/32256-c0).

Here c0>0 is the same fixed strictly improved exponent available in the reviewed all-physical cubic estimate, after its preliminary small losses are chosen. Equivalently one may decrease c0 slightly and absorb P^epsilon into a requested Z^epsilon. The fixed arithmetic constants depend on S0, not on p or xi_p. The conclusion holds for both original/core markers, for the original physical n weight and for its reviewed half-damping. It preserves the same finite-order Q uses and is not an unconditional new density estimate.

### 2. The exact first Poisson formula removes the auxiliary norm

The source is the fixed public fd4aeeb2 paper.tex, equations local-F, local-full-coefficient and local-unit-factor, particularly its bad CRT paragraph. The finite transform has outside factor sqrt(X)/(sqrt(Nb*) NA), where A=c n^3, apart from Y^(-1). Its bad Gauss factor is exactly

 sqrt(Nb*) tau xi(A) overline{xi(H/s)}.

After multiplication by the original corrections, every auxiliary factor cancels except overline{xi(u)}, where H=u a^6. This uses xi(a)^6=1 and holds coefficientwise, including all physical n and all six units. The common radial Fourier argument is exactly X NH/NA and has no b*. Thus the fully reassembled first-Poisson expression has outside sqrt(X)/Y, not a positive power of P, and unchanged Gaussian and Fourier profiles.

For the n=1 cubic layer the same identity is included in the published [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XXIV. For all n the same source cancellation precedes the square-layer and odd n0 decompositions. Therefore changing b0 to b0 p does only the following in the cubic first-Poisson formula:

1. multiply its frequency row by overline{xi_p(epsilon w^2)};
2. require p not dividing epsilon w^2 (a')^6, c, n0, r_phys or s;
3. retain all original S0 data and all original good-prime local coefficients elsewhere.

The first is a modulus-one row coefficient on its retained rows. It must not be moved into either free column or used to create a moving good conductor for those columns. The finite source ray group T, which handles the original supplementary phases at 2 and 3, is unchanged. No character expansion modulo p is needed.

In older fixed-Q bookkeeping, Q=Nb* X'Y' and a positive bound was written with prefactor Q/Y'^(3/2), followed by Q^(-1/2). That fixed-b* presentation is not a uniform lower bound on the cost of changing b*. The uniform proof starts from the exact cancellation just displayed, before those fixed constants were absorbed.

### 3. All physical labels and true inverse rows

Use the exact reviewed all-n organization

 n=n0 r_phys^2, n0=F2 E4,
 c=E4 g e0 c2, s=E4 g j^2 e0 f s2,
 L=U_l/(N^3 B G Ne0),
 S=Y'/(B G Nj^2 Ne0 Nf).

Here N~Nn0, B~NE4, G~Ng, U_l=e^l T P_slots/Nr_phys^6; P_slots is the product scale of the original marked primes and is unrelated to the new norm P. Keep this distinction in all budgets.

The new p restrictions on w,a',n0,r_phys,g,e0 are retained as bounded row restrictions or restrictions in outer positive sums. Since p does not divide r_phys or a', it also does not divide their square-layer mask h, its factors j,k, or the old f|rad(k a'). The reciprocal c2 column acquires exactly the common unit mask (c2,p)=1. Its Dirichlet series is the old inverse divided by the one local factor 1-eta(p) overline{psi_w(p)}P^(-v). On the actual shifted contour sigma=Re v>=1/2+fixed buffer this reciprocal factor is uniformly bounded by (1-P^(-sigma))^(-1). Its fixed-order v derivatives have costs (log P)^J, which are absorbed by ambient small powers. No additional zero with positive real part is introduced.

Accordingly the original selected row set E_b and its buffered zero-height condition are unchanged, apart from its positive restriction p not dividing w and the other actual labels. The underlying finite-order characters in the inverse proof retain their original S0 presentations. Their deleted p factor is handled by the displayed finite correction, rather than declared to be a new uniformly bounded fixed conductor.

Every original prime-slot rational moment remains applicable: p is a common column hole, and the outer xi_p(epsilon w^2) is an allowed bounded row weight. All original zero masks and moving primitive conductors of psi_w are retained.

### 4. The only new smooth-column mask and its whole-scale payment

After the fixed factors above are p-units, the remaining restriction is exactly (s2,p)=1. On each genuinely compact separated spatial mode, its finite identity is

 B_w(S;p-unit)=B_w(S)-psi_w(p) B_w(S/P),

with the original radial profile rescaled by P and the original complex dilation rotation kept. A common smooth angular decomposition makes the rotation a modulus-one row scalar; its seminorms have no positive P power. If the rescaled physical annulus is empty it stays empty. No artificial short column is added.

The first term is the original bound. For the second, freeze p and put S'=S/P before applying the complete positive e0 estimate. The exact inverse-column scale ratio is

 L/S=U_l Nj^2 Nf/(N^3Y').

Consequently on the same actual reciprocal contour

 L^(sigma-1)=(L/S)^(sigma-1) P^(sigma-1) (S')^(sigma-1).

The old proof bounds the entire finite e0 sum by its positive all-scale integral dS/S. Under this substitution dS/S=dS'/S'. The common reciprocal e0 measure and its true finite support are retained first; only afterward may the positive bound be enlarged. Thus the complete pointwise/eighth-moment minimum and genuine long-Poisson tail give exactly the old M^J(b) envelope, multiplied by P^(sigma-1)<=1. This is uniform since all actual shifted contours have sigma<1 by a fixed margin after Q and the bin buffers are fixed.

Equivalently the new p hole can be merged with the ordinary f mask and expanded once. Its p-divisor term contributes f^(sigma-1), the same nonpositive weight. The fact that p is moving does not create P possible divisors: there are two. This argument relies on the whole e0 sum, not on an unproved monotonicity of a single signed smooth column under deleting multiples of p.

The same calculation applies in the small-M range where the old proof uses the pointwise slot price. It only replaces S by S/P in the same full-scale envelope. The actual outer counts of r_phys and a', the n0 pooling, and all Gaussian/Fourier tails retain their previously strictly summable powers. The optional half-damping adds n0^(-1/2) r_phys^(-1) at the already reviewed positive stages.

### 5. Precise limits

This reviewed statement concerns the complete nonprincipal cubic good-core sector only. It does not provide a uniform original completed-theta R2 estimate as b* grows, and it says nothing about principal/unit-core or genuine sextic sectors. It does not identify a small family-density bound with a coherent signed sum. The high auxiliary-prime average needs its own source identity, primitive character check and complete bad-row budget.

The prime p is fixed during every exact physical identity and only later allowed to vary in the stated uniform bounds. All norm-mode and height seminorms are paid before such averaging. The sharp inverse cutoff is unchanged; no smoothing of its endpoint is used here.

## Part C. Simultaneous many-prime complete-cubic uniformity

Fix all the original S0, eta=1, windows, prime slots, inverse family and physical geometry of Part B. Fix C>0 and let R tend to infinity with R<=Z^C. Put

 P=(log R)^64,
 k=floor(log R/(65 log log R)).

Let b be a squarefree product of k distinct good primes, each with norm in [P,2P], outside S0. For sufficiently large Z these primes are outside every original marked slot support, whose norm scale is a fixed positive power of Z. More generally retain this disjointness as an explicit condition. Then Nb<=(2P)^k<=R for all sufficiently large R.

At each p|b choose any nonprincipal xi_p of order dividing six, including the choice xi_p=bar chi_p. Form the admissible auxiliary xi=xi0 product xi_p, modulus b0 b, and enlarged bad set S0 union supp(b). The claim is uniform over every such b and all these choices:

 |I_cubic,b(Z)| <<_(epsilon,C,S0,profiles) (RZ)^epsilon
                                      Z^(-271/32256-c0).       (1)

The already reviewed original/half physical n weights and original/core nonflat markers are included, with the same finite-order Q assumptions and same strictly improved c0 after preliminary losses. There is no full-probe, principal/unit-core, genuine-sextic or first-flat claim.

### One simultaneous exact transformation

Apply the first-Poisson CRT cancellation once for the whole modulus b0 b. Its auxiliary Gauss norm sqrt(Nb0 Nb) cancels exactly against the original normalization. The profiles retain their original radial argument X NH/NA. The extra multiplier is simply overline{product_(p|b) xi_p(epsilon w^2)}, of modulus one on the retained rows. There is no expansion into a number of ray characters depending on Nb, and no repeated invocation of a fixed-data theorem with an untracked constant to the power k. The old ray group T is unchanged.

Every new b-unit restriction on w,a',n0,r_phys,g,e0 is retained as a positive row/outer restriction. The inverse column has the one explicit correction

 J_b(v,w)=product_(p|b)[1-eta(p)overline{psi_w(p)}(Np)^(-v)]^(-1).

Fix the actual buffered reciprocal contours inside

 1/2+delta <= sigma=Re v <= 9/10,                    (2)

with delta>0 fixed before the application. This is allowed in the existing Q-capped bins, whose old top is 7/8, by choosing all bin and contour buffers beforehand. The denominator in J_b has no positive-real-part zero. The underlying primitive inverse family and the same selected zero rows E_b remain unchanged apart from the explicit b-unit restriction.

The smooth column has its simultaneous finite mask identity

 B_w(S; b-unit)=sum_(d|b) mu(d)psi_w(d) B_w(S/Nd).     (3)

Keep each actual compact common profile, norm dilation and complex rotation. After the complete true finite e0 sum, the same change S'=S/Nd as in Part B pays exactly (Nd)^(sigma-1). The true reciprocal e0 measure is unchanged, and only the final positive all-scale integral is enlarged. Thus the total new positive price is bounded by

 product_(p|b)(1-(Np)^(-sigma))^(-1)
                 times product_(p|b)(1+(Np)^(sigma-1)).       (4)

This is an exact simultaneous local-cost bound. In particular no factor 2^k is substituted for the second product before its decay is used. The common sharp inverse cutoff and all masks are preserved.

### Uniform product and seminorm bounds

Since Np>=P, (2) gives

 log of the first product in (4) << k P^(-1/2-delta),
 log of the second product in (4) <= k P^(-1/10).

Both tend to zero because k<<log R/log log R and P=(log R)^64. Hence (4) is bounded by an absolute fixed constant for all sufficiently large R, uniformly in every admissible b, sigma and character phase.

For each predetermined derivative order J, logarithmic differentiation of the first product contributes finite polynomials in sums

 sum_(p|b) (log Np)^j (Np)^(-sigma)/(1-(Np)^(-sigma))^j,
 1<=j<=J.

These are bounded by fixed powers of log R, uniformly on (2); the same conclusion follows directly by finite differentiation. For the second product, every log-scale derivative of a d dilation has at most (1+log Nd)^J<=(1+log R)^J. Therefore the weighted finite sum in (3), including its common-mode seminorms, is at most

 (1+log R)^J product_(p|b)(1+(Np)^(sigma-1)),

which is still ambient-subpower. Angular rotations retain unit row factors and do not add a power of Nd.

The old rational selected-slot moments accept the unchanged common b-hole, their explicit inverse correction J_b, and the bounded new row phase. The genuine complete e0 envelope, small-M branch, n0 pooling, actual primitive conductor blocks, all r_phys/a' multiplicities and Gaussian/Fourier tails remain the ones in the reviewed single-prime proof. Their strict summability pays the same ambient small powers, proving (1).

Any normalized finite average over this ensemble also satisfies (1) by triangle, since the bound is uniform for each b. This last statement is only a low bound for this specified core type; it does not replace the signed high average or assert that the principal/unit frequency is suppressed.

## Part D. Uniform transfer for the six other covered nonflat types

### 1. Exact observation and claim

Use target eta=1, the original fixed bad data (S0,b0,xi0), the fixed ray group and profiles, and the original fixed number of disjoint positive prime slots. Let b_aux be a squarefree good ideal outside S0 and all selected slot supports. For every p|b_aux choose a nonprincipal residue character xi_p of order dividing six. Enlarge the physical bad set to S0 union supp(b_aux), and replace the primitive auxiliary character by xi0 product xi_p. All physical variables and the first Poisson frequency retain the resulting unit masks. Each original/core marker and its original finite compensation uses that SAME enlarged bad set. Allow either the original physical n weight or the already reviewed additional q_n^(-1/2). No first-flat operation and no exclusive s-unit marker is included in this claim.

For every fixed C>0, uniformly for q_b_aux<=Z^C and these characters, the six already covered nonprincipal types retain their complete normalized bounds with only an ambient (q_b_aux Z)^epsilon loss:

- quadratic H=epsilon v^3 a^6: exponent -439/2304;
- pure fifth H=epsilon w^5 a^6: USER exponent -209/960;
- mixed (3,5) H=epsilon v^3w^5a^6: exponent -3073/16384;
- mixed (2,4,5) H=epsilon u^2w^5a^6: exponent -133/34560;
- mixed (2,3,4) H=epsilon u^2v^3a^6: exponent -1/512;
- mixed (2,3,4,5) H=epsilon u^2v^3w^5a^6: exponent -1/512.

Here u is nonunit cube-free, v,w are nonunit squarefree, their indicated supports are pairwise disjoint, and the original frequency unit epsilon ranges over all six units. Preserve every preexisting finite-order Q assumption and the common radial/norm-mode restrictions. No angular Q statement is added. Constants may depend on C,S0,profiles and the final loss, not on b_aux or its characters. The pure-fifth exponent and selected-Q input remain the user's contributions.

The supplied single-prime cubic theorem is not used as a black-box theorem about the whole completed row. Its underlying exact CRT identity, before ANY core decomposition, is the common starting point below.

### 2. Type-independent first-Poisson cancellation

In the pinned original source equations local-F, local-full-coefficient and local-unit-factor, put A=c n^3 and b*=b0 b_aux. The first-Poisson prefactor is sqrt(X)/(sqrt(Nb*) NA), with Y^(-1) separate. The primitive bad Gauss factor is

    sqrt(Nb*) tau xi(A) conjugate(xi(H/s)).

Its product with the original arithmetic corrections leaves precisely conjugate(xi(u6)), where H=u6 a^6 is the sixth-power-free decomposition, because xi(a)^6=1. The radial Fourier argument is X NH/NA. Thus no positive norm power of b_aux remains and no b_aux enters that radial scale. This exact cancellation is prior to deciding whether u6 has type 3,5,35,245,234 or2345. Product xi remains primitive since its coprime local factors are all nonprincipal; its normalized bad Gauss root has modulus one and is not expanded into q_b_aux residue classes.

After this step the only new data are (i) the bounded joint-row scalar conjugate(xi_aux(u6)), and (ii) unit restrictions at b_aux in every actual row, square layer, odd branch and common free column. The original ray group at 2 and 3 stays fixed. No primitive good-conductor factor is assigned to xi_aux in a free inverse or smooth column.

### 3. Common inverse holes and exact smooth-hole expansion

Fix all actual outer labels and ordinary mask branches before applying the analytic bounds. The new outer unit restrictions are restrictions in positive norms/sums. In particular the r,a',n0,g,e restrictions imply that their extracted ordinary mask factors are b_aux-units. The free reciprocal c2 column has precisely the extra common hole (c2,b_aux)=1. Its Dirichlet series is multiplied by

    product_(p|b_aux) (1-eta(p) psi_row(p) P^(-v))^(-1),

with the appropriate original conjugation of psi_row. On the genuine contour sigma=Re v in a fixed compact subinterval of (1/2,1), this and every fixed-order height derivative are bounded by q_b_aux^epsilon times a constant depending on that compact set and derivative order. To see uniformity, the absolute undifferentiated product is at most product(1-P^(-sigma_min))^(-1), which is O_epsilon(q_b_aux^epsilon); the logarithmic derivatives have at most fixed powers of 1+log q_b_aux, absorbed by decreasing the initial epsilon. Local zeros have Re v=0, so no extra positive-real-part zeros or new exceptional-row density family is introduced.

The remaining smooth s2-hole has the EXACT finite identity, at each compact physical block,

    B_row(S;b_aux-unit)=sum_(d|b_aux) mu(d) psi_row(d) B_row(S/Nd).

All original source phases and the complex rotation of the common test under s2=d t are retained. Such normalized rotations have the same compact smooth seminorm class. No derivative falls on a row character or on an auxiliary residue-class expansion. The inverse/smooth characters themselves remain the original ones.

For every type in the claim, the actual common-divisor e has outside weight 1/q_e and multiplies BOTH free-column denominators. Consequently L/S is independent of e. On the reciprocal contour the inverse scalar is L^(sigma-1). Fix d|b_aux, set S'=S/Nd, and write exactly

    L^(sigma-1)=(L/S)^(sigma-1)(Nd)^(sigma-1)(S')^(sigma-1),
    dS/S=dS'/S'.

The old full e estimate retains its true finite support first and only then enlarges a POSITIVE all-scale envelope. Apply it after this substitution. Its entire pointwise/moment minimum, actual-row long-Poisson tail and empty/subunit ranges therefore give the same bound, times (Nd)^(sigma-1). This does not assert monotonicity for any signed single-scale column. Since sigma<=sigma_max<1,

    sum_(d|b_aux) (Nd)^(sigma-1)
       <=product_(p|b_aux)(1+P^(-(1-sigma_max)))
       <<_epsilon q_b_aux^epsilon.

All boundary bin buffers are fixed before this assertion. Thus both holes cost only an ambient small power, uniformly for arbitrarily many auxiliary primes. There is no iteration of a fixed-prime unspecified constant.

### 4. Verification of the all-e interface in the six actual proofs

Quadratic: in [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XI §4 equations (11)–(13), c=E g e c2 and s=F g j^2 e f s2. The exact ratio is U q_j^2 q_f/(Y' N^2 B^2). Its full e result has factors (NB)^(-1+2a) q_j^(-2a) q_f^(-a), with a=1-sigma. Replacing f by a new coprime divisor d f yields exactly the factor (Nd)^(-a) above. The n0/E/g pooled coefficients remain in the original divisor-bounded class under the extra joint-row phase and unit restrictions. The frequency and all square tails are unchanged.

Pure fifth: Part XIV B of the published physical proof fixes r,h0,a', the ordinary mask and actual s-divisor extractions; n=r^2. Its c2 inverse and s2 smooth columns have L/S=C_l q_f/(q_r^6Y_*), and its true e coefficient is eta(e)/q_e. The complete density estimate gives the same factor q_f^(sigma-1). The user's PURE_FIFTH_SELECTED_Q_GAIN equation(0) already treats arbitrary frozen common holes in the actual Euler product; adding b_aux leaves exactly that identity. Since auxiliary primes are outside selected slots and xi_aux is only an OUTER frequency-row phase after the CRT cancellation, it never becomes an illegal moving character in a slot weight nu_i. The selected prime tests stay factorable mode by mode. Equation(A)'s common-hole loss is charged to q_b_aux in the ambient before any infinite row sum. Hence the USER's -209/960 envelope is unchanged.

Mixed(3,5): the exact odd interface is the quadratic one, with fifth boundary h0|w and the original true r/h0 frequency reduction. The complete 35 proof takes the full finite e integral before its restricted pair-Gram/smooth contraction and before the rational 4351-box budget. The extra bounded joint-row scalar does not affect these positive norms, and common b_aux holes are removed/expanded at the free-column stage just proved. The user's selected-Q pointwise estimate retains the same frozen-product slot coefficients, and every true long-S tail is applied before row enlargement. Thus no extra factor enters its verified exponent ledger, low or high bins.

Mixed(2,4,5): the actual identity (7) in [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XIX is L/S=C_l q_f/(q_r^6 N^3Y_*); the outside odd factor after inversion is N^(-3/2+3a)<=1. The finite e sum is the same positive all-scale sum. The moving fifth character is already paid by the old conductor enlargement; no auxiliary character is added to it. Its physical r-boundary cases and all original finite cutoffs remain intact.

Mixed(2,3,4): the exact all-n formula (14) in [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XX is L/S=C_l f tau/(R^6 A^3 N^2 B^2Y'), with outside scalar A^(-3/2)/(NB). The reciprocal-e measure and the whole smooth envelope are retained in its low-bin bound; Section4 high bins use the same full e integral and pointwise/specified moment alternatives. Its odd factor A^(-3/2+3a)(NB)^(-1+2a)<=1 is unchanged. The 489-rational-box certificate therefore still bounds the identical positive upper envelope.

Mixed(2,3,4,5): [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XXII Section3 inherits precisely that full physical interface and complete reciprocal-e integral. Section4 likewise integrates the full positive envelope, with actual w shell count W/H0. The fifth conductor, primitive-Poisson support and true row masks are fixed before positive enlargement. Adding b_aux only restricts those positive families, and its holes receive the common calculation above. The strict W,R,a' summability margins remain.

In all six proofs, a square-layer or a' sum is performed against the same full Schwartz/Gaussian envelope after fixing the ambient parameter to include q_b_aux as well as all original labels. The preexisting strict margins absorb the original label losses; q_b_aux is external and polynomially bounded in Z. Reserve its required losses at the start, so no claimed exponent is consumed. Optional half-damping is inserted solely at the already reviewed positive n0/r stages, not by comparing signed completed sums.

### 5. Boundary and sources

This is a uniform statement for the listed nonprincipal types. It supplies no uniform estimate of original completed-theta R2, no unit-core estimate, no missing residue-1 type, no exclusive-s observation transfer, no first-flat assertion, and no whole-probe high or low bound. It changes the finite auxiliary data with Z only through the explicitly defined observations above; it is not a signed estimate for the unaveraged original E_b sum.

The exact common source is fd4aeeb2 Sep30 paper.tex, local-F/local-full-coefficient/local-unit-factor before the all-n decomposition. Supporting public mathematics is QUADRATIC_DUAL_N1.md Parts XI,XIV,XIX,XX,XXII,XXIII plus the user's PURE_FIFTH_SELECTED_Q_GAIN.md at92d2d98. The previously reviewed half-damping transfer is HALF_DAMPED_PROBE.md §§7-8. The fixed single-prime cubic uniformity theorem is used only to locate the already audited type-independent CRT source calculation; none of its cubic positive estimates is silently substituted for a six-type proof.
