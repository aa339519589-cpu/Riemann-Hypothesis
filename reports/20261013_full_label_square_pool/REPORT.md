# Complete-label physical square and higher-power kernel estimates

This report extends the [complete mixed-character and square-pool theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d4b0cb4460dc111f7737127a60bf599c8b11cd55/reports/20261013_physical_square_kernel_pool/REPORT.md) from its balanced same-E/common-a, n=n'=1 branch to all original c,n,s labels and both independent finite compensation tuples of the SAME half-damped, positive-auxiliary, Gaussian-T-restored observation. No polynomial label cutoff is imposed. The full source and the complete restoring series are retained.

Write P=exp(Z). For distinct auxiliary primes and the actual pair element w defined in Part I, Section 1, the scalar pool Nu<=U has the unconditional bound

    |C_full-label,pool,total|
      <<_epsilon U P^(-1/64+epsilon) Z^C + O_H(P^(-H) Z^(C_H)),
          1<=U<=P^theta0, fixed theta0<1,

for every prescribed fixed H>0. At U=P^(1/128), with theta0 chosen above 1/128, this is exponentially small. The new steps are the uniform polynomial-label Poisson envelope, complete all-scale Gaussian moments, and the arbitrarily small full-source auxiliary-label collision tail. The character theorem itself is the already proved one in the linked report, with no new arithmetic hypothesis.

The whole-cross consequence keeps the complete original positive class energy Q_full intact. Remove the complete equal-prime scalar before making a w partition, and then partition only the remaining scalar. This gives

    C_cross=Re L_large-Q_full+O_epsilon(P^(-1/128+epsilon) Z^C),
    Q_full>=0.

Here L_large is the exact unestimated large-squarefree-kernel scalar on the original remaining support. No positive-class estimate is transferred to a w-dependent mask. The same-pool full-label h!=h' estimate would require its own masked same-class subtraction and is not asserted. The report does not estimate L_large or prove the original whole-signal bound, a new spectral gap, a zeta-zero exclusion, or RH.

Part II independently extends the absolute small kth-power-free count to ALL original labels. For each fixed integer k>=3 and U>=1 it gives

    |C_(k,U)| << P^(2/k-1) U^(1-1/k) Z^C + O_H(P^(-H) Z^(C_H)).

Because this proof is absolute, it permits every additional physical pair mask bounded by one, including h!=h'. For k=6 and U=P^(4/5-eta), 0<eta<=4/5, it gives P^(-5eta/6)Z^C; literal physical cubes give P^(-1/3)Z^C. This arbitrary-mask permission belongs to Part II, not to the square-class cancellation estimate in Part I. Both parts use distinct auxiliary primes and share the complete Gaussian/source/restoring estimates in Appendix A. Their large-kernel complements remain unestimated.

## Original object and public dependencies

The [original exponential-prime observation](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d4b0cb4460dc111f7737127a60bf599c8b11cd55/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md), its opening raw summand and Parts A and B, fixes all primary-generator, bad-data, zero-extension, finite-sector and marker conventions. In K=Q(omega), write A=c n^3 with c squarefree. With b*=b0 q, B=N(b*), primitive xi=xi0 chi_q, eta=1, tau=B^(-1/2)g_xi(b*,1), and Xi(A)=xi(A)chi_A(b*), the half-damped raw summand at positive scales x,y,t is

    [W1(Ns/y)/y] [chi_s(b*)/(tau xi(s))] xi(m)
    [g_(chi_s)(s,-m)/(Ns)^(1/2)]
    gamma_2(c) conjugate(alpha_0(A)) conjugate(G(A))
    Xi(A)^(-1) R(A,s) chi_A(m) (Nc)^(-1/2)(Nn)^(-3/2)
    (B Ns x)^(-1/2) W0(Nm/(B Ns x)) V_G(NA/t),

where V_G(v)=(2sqrt(pi))^(-1)exp[-(log v)^2/4]. The subscript alpha_0 distinguishes the fixed character from the real activation variable. Original S-unit restrictions, all s valuations, bad-prime CRT factors, shared-prime zeros and ordinary/core nonflat markers remain. Every original finite compensation coefficient is retained; a term has the outside (ND)^(-3/2) factor and the actual scales

    x=X/(ND) exp(-alpha), y=Y/(ND), t=T NE exp(-alpha).

The original slot weights, their assignments and signs, the true c_(S0+q) inverse and the ambient A_T(Z) inverse are unchanged. In particular A_T is not redefined when t alone changes. The supports and total absolute prices of these finite compensation data are fixed powers of Z. The complete old T-only restorer is displayed and bounded on the required scale powers in Appendix A, Section 3.

The [original source realization](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d4b0cb4460dc111f7737127a60bf599c8b11cd55/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md) gives m_theta^2=Phi/(2cosh(x/2)), e0=2m_theta cosh(x/2), dnu=e0^2 dx. For the fixed source q_0 in L2(nu), v=e0 q_0 and f_q=Phi q_0=m_theta v. The subscript q here is the fixed source label, not an auxiliary prime. For every fixed L>=0,

    integral |f_q(alpha)| exp(L|alpha|) d alpha
       <=||v||_2 ||m_theta exp(L|x|)||_2 < infinity.

These are fixed-source constants; neither a source depending on the auxiliary prime nor a source truncation is introduced. Simultaneous activation of x and t has no extra scalar multiplier and leaves y, the auxiliary law, slots and ambient normalizers fixed.

The pure character theorem in [Part I of the square-pool report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d4b0cb4460dc111f7737127a60bf599c8b11cd55/reports/20261013_physical_square_kernel_pool/REPORT.md) is uniform for ALL E>=1, arbitrary harmonic quadratic coefficients, every stated small-period coset and the genuine two-dimensional Abel variation. Parts II and III there prove the original exact Poisson/source construction and uniform squarefree-kernel scaling. The present Part I, Sections 2--4 recheck their actual hypotheses for unbounded and unbalanced original labels, rather than presuming that a finite-label theorem is automatically uniform.

Part I contains the complete five-section square-kernel proof and whole-cross reduction. Part II contains the complete five-section absolute k>=3 proof. Appendix A supplies the shared three-section Gaussian, collision and restoring estimates. Part I, Section 5, gives the complete equal-prime argument directly from the public absolute lines of the linked single-prime comparison, Part B, Section 2. [Independent mathematical reviews](REFEREE.md) accompany all three proofs. Equation numbering restarts in each part and in Appendix A.

## Part I. Complete-label square-kernel cancellation and the whole-cross reduction

### 1. The full original scalar and its restricted scope

Use the original positive auxiliary law q,q' of norms comparable to P_aux=exp(Z), half n damping, finite compensation and the old T-only restorer. Keep the actual original c,n,s,m columns, with c squarefree, A=c n^3, every original/core marker and all finite sector labels. The two compensation tuples and the c,n labels need not coincide. The auxiliary primes are distinct. Retain the original finite-sector bilinear pairing, or any fixed bounded matrix between its finitely many coordinates; no scalar replacement of the sector energy is made.

For each original pair put

 g=gcd(c,c'), a=c/g, a'=c'/g, (a,a')=1,
 L0=g a a',
              w=q'(a')^2 m-q a^2 m'.                       (1)

Select the disjoint physical squarefree-kernel pool w=u v^2 with u in the fixed element representative set U_2 of Part III of the linked square-pool theorem, Nu<=U. The two roots v are counted with1/2. This scalar is taken directly from the original FULL m,m' columns, with only their original zero extensions: it has no previously inserted cross-prime m holes, no near/far-w cut, and no h!=h' restriction. Thus no estimate for restoring an artificially deleted m subset is being assumed. The selection w=u v^2 is its only new physical pair mask. The full-label bound is

 |C_full-label,pool,total|
       <<_epsilon U P_aux^(-1/64+epsilon) Z^C+O_B(P_aux^(-B) Z^C),
       1<=U<=P_aux^theta0,   fixed theta0<1.                (2)

All constants may depend on the fixed source, fixed profiles, original bad data and the displayed fixed exponents. For U=P_aux^(1/128) this gives an exponential scalar saving.

Unlike the balanced theorem, (2) does NOT by itself bound the h!=h' sum restricted to this same w pool. That masked same-class contribution remains unestimated. Section5 instead preserves the complete, unmasked class term and partitions only the complete scalar, giving a legitimate reduction of the original whole cross target. No unrestricted positive-class estimate is assigned to a w-dependent mask.

### 2. Original full-n phase and the exceptional auxiliary-label collisions

The exact original raw summand has A=c n^3 and outside c,n weight

                  (Nc)^(-1/2)(Nn)^(-3/2)=(NA)^(-1/2).

Its auxiliary-dependent character part before estimating is

 chi_q(m) chi_q(s)^(-1) chi_s(q)
                     chi_q(A)^(-1) chi_A(q)^(-1).

Original reciprocity gives the fixed finite-sector factor times chi_q(m/A^2). On the true q-unit support, A^2=c^2 n^6 and the sixth-power factor drops, giving exactly the original class chi_q(m/c^2). It does not remove chi_A(m), any zero extension or the n-dependent small-period factors. They remain in the physical coefficient.

First remove pairs where either auxiliary prime divides the opposite column's c n s. The own-column versions are already zero by the original restrictions. Since the original s scale is at most a fixed power of Z, no such prime divides s for sufficiently large Z. A remaining exceptional pair has Nc>=c P_aux or Nn>=c P_aux in at least one column. The raw absolute m sum in one column costs at most P_aux^(1/2) times a fixed polynomial in the remaining labels and exp(C|alpha|), since the annulus has O(M) points and its normalizer is M^(-1/2), where M=N(b0q) X_lambda Ns exp(-alpha). For M below the lower annular threshold there are no nonzero lattice points. In two columns the total auxiliary loss is at most P_aux times the corresponding polynomial/source bound.

For any fixed R, the exceptional-label indicator is bounded by (Nc/(c P_aux))^R or (Nn/(c P_aux))^R. High positive Gaussian moments then absorb that label power and pay P_aux^(-R). Taking R arbitrarily large proves O_B(P_aux^(-B) Z^C) after the full source integrals. This absolute estimate covers the whole exceptional pair set at once, with no factor U or dependence on the chosen w mask. The detailed positive moment and raw collision estimates are given in Section 4 and Appendix A, Sections 1--2.

On the remaining pairs, (c n s c'n's',qq')=1. Consequently Acoef=q'(a')^2 and Bcoef=q a^2 are coprime. The same exact two-root CRT identity used in the fixed-class bridge applies with L0 in place of C0bb':

 tau_q^(-1) conjugate(tau_q'^(-1))
  chi_q(m/c^2) conjugate(chi_q'(m'/(c')^2))
           =tau_psi^(-1) psi(w/L0^2),
              psi=chi_q conjugate(chi_q').                 (3)

All original fixed b0, xi0 and sector factors remain. On w=u v^2,

 psi(w/(b0 L0^2))=psi(u/b0) psi^2(v/L0).                    (4)

Nu<=P_aux^theta0 makes u an auxiliary unit for large Z. The v character therefore has two primitive cubic local factors. Both original normalized roots remain as the original v-independent phase; no new root normalization is needed.

### 3. General labels only introduce fixed polynomial costs

Let

 D_label=2+Nc+Nn+Nc'+Nn'+Ns+Ns'.

All other original compensation parameters, their reciprocals, finite tuple counts and coefficient sizes are bounded by fixed powers of Z. The s annuli are still bounded by fixed powers of Z. An admissible remaining period can be taken as a fixed multiple of A A' s s' and the fixed bad periods. Its norm obeys NJ<=Z^C D_label^C and it is prime to qq'. This period retains chi_A(m), chi_A'(m'), the complete s Gauss functions, xi0, all shared-prime zeros and every original finite ray condition.

At a fixed v class modulo J, the residue equation Acoef x-Bcoef y=u v0^2 modulo J has exactly NJ solutions. Poisson on m=x+j z0(v)+j Bcoef O gives exactly the reviewed all-frequency formula

 W_(ell,u)(v)=1/N(j Bcoef) integral_C
  W0(Nz/M) W0(N((Acoef z-u v^2)/Bcoef)/M')
                 e(-Tr(ell z/(j Bcoef))) dmathfrak m(z),

with accompanying harmonic quadratic e(Tr(ell Abar u v^2/(j Bcoef))). Abar is an inverse of Acoef modulo Bcoef, and ell runs over the original full trace-dual lattice. Nothing in this identity requires the labels to be balanced or bounded by a chosen polynomial cutoff. The finite table values cost at most a fixed polynomial in D_label and Z; for example the original unnormalized s Gauss sum is at most Ns.

Write A_source=|alpha|+|alpha'|. The support is contained in

 Nv<=P_aux (Nu)^(-1/2) Z^C D_label^C exp(C A_source).

With v=sqrt(P_aux)(Nu)^(-1/4)R_V V, R_V=Z^C D_label^C exp(C A_source), the same rescaling makes u enter the continuous weight only through u/|u|. Every fixed derivative has polynomial label and source-exponential cost. The ratios Acoef/Bcoef and its inverse are bounded by fixed powers of D_label because Na,Na'>=1; the auxiliary prime norm ratios stay in fixed compact annuli. Put H_freq=N(jBcoef)/M. For sufficiently large fixed K,

 sum_ell ||W_(ell,u)||_Abel
                  <<Z^C D_label^C exp(C A_source).          (5)

Indeed the individual envelope has M/N(jBcoef) times that bound and (1+Nell/H_freq)^(-K), and both H_freq and its reciprocal have only polynomial label/source cost. The exponent C is fixed, independent of q,q', u and the labels themselves. This is a fixed-order smooth estimate, not a finite-label counting assertion.

Choose the character lemma's E0=Z^C D_label^C exp(C A_source) large enough for NJ and the enclosing disk. Its theorem holds also when E0 is large; its large-E proof uses a uniform trivial bound rather than assuming E0 is logarithmic in Q_mod. Applying it to every frequency, summing(5), and multiplying both true radial normalizers gives, for each fixed original label pair,

 |C_(labels,u)(alpha,alpha')|
       <<P_aux^(-1/64+epsilon) Z^C D_label^C exp(C A_source)
                V_G(NA/T_eff) V_G(NA'/T_eff'),              (6)

up to the original compensation scalars and restoring coefficients. We have harmlessly bounded other negative label powers by one; keeping them would only improve convergence. T_eff and T_eff' include their original source and restoring shifts. Equation(6) is uniform in u in the stated pool. Both independent prime probability sums retain total mass at most one after the exceptional-pair restriction; no conditional renormalization is made.

### 4. Summing every label and every source shift

For every fixed K, choose a fixed B>K+2. The actual log-Gaussian has V_G(t)<=C_B t^(-B) for all t>0. Since Nc,Nn>=1, any fixed polynomial in Nc,Nn is bounded by a power of NA=Nc(Nn)^3. Consequently

 sum_(c squarefree,n) (NA)^K V_G(NA/T_eff)
  <= C_B T_eff^B
           sum_c (Nc)^(K-B) sum_n (Nn)^(3K-3B)
  <<_(K,B) T_eff^B.                                      (7)

The ideal sums converge absolutely; original holes and markers only decrease this positive majorant. The same estimate holds in the other column. The finite s annulus sum and every actual compensation tuple have polynomial-Z total cost. The largest unshifted Gaussian scale is at most Z^C exp(|alpha|). Every old restoring shift decreases this scale, and its absolute coefficients already form a uniformly bounded series, so (7) applies uniformly and is summable term by term. This also proves the high-label collision estimate used in Section2 by increasing K and B.

Integrating (6) with (7) costs only a fixed exponential moment of each original f_q. Thus the full, infinite c,n sums are paid without a polynomial cutoff whose discarded tail might be multiplied by the exponentially large pool count. This gives (2) for each u with a constant independent of u. The O(U) disjoint square-class count supplies the displayed U factor. The exceptional auxiliary-label contribution was already paid absolutely on the whole set.

The proof is confined to the scalar pool. To bound h!=h' INSIDE THAT SAME POOL directly, one must subtract its exact full-label restricted same-class term. No positivity or absolute estimate for that term is proved by (2), and no balanced-label certificate is applied outside its label range.


### 5. The whole-cross endpoint keeps the complete class term intact

Let I_(q,gamma,h) denote the full original fixed-source column, including all original compensation terms and the old restorer. Set I_(q,gamma)=sum_h I_(q,gamma,h) and V_(gamma,h)=sum_q omega_q I_(q,gamma,h). With the original finite-sector inner product, define

 S_full=sum_gamma |sum_h V_(gamma,h)|^2,
 Q_full=sum_(gamma,h) |V_(gamma,h)|^2,
 C_cross=sum_gamma sum_(h!=h') V_(gamma,h) conjugate(V_(gamma,h')).

Then the exact identity is C_cross=S_full-Q_full, with Q_full>=0. There is no w partition of Q_full. In particular this statement does not assert that a masked same-class expression is positive.

Remove the q=q' contribution from S_full BEFORE any w restriction. It is

 D_aux=sum_(q,gamma) omega_q^2 |I_(q,gamma)|^2.

The complete first-Poisson identity of the publicly linked single-prime comparison, Part B, Section 2, has absolute lines (3,3,2), summable ideal weights

    c^(-5/2) n^(-7) s^(-2) a^(-12) u^(-2),

and a jointly integrable fixed Schwartz majorant in all independent heights. Its prefactor is X^(-3/2)T^4Y^2, independently of the auxiliary norm B: the original bad sqrt(B) Gauss factor cancels exactly. Taking the surviving auxiliary character's modulus at most one, rather than taking a prime mean, bounds the COMPLETE column by a fixed polynomial in Z uniformly at each q. The original finite-sector indicator is independent of m and is kept through this complete-m bound. Actual compensation, the ambient normalizers and the full old restoring operation have their already proved polynomial or bounded costs; simultaneous source shifts have only exp(C|alpha|) cost, paid by the displayed source moments. Thus

    sum_gamma |I_(q,gamma)|<=Z^C

uniformly in q. The original positive prime law has max_q omega_q<<Z/P_aux and sum_q omega_q=1. Hence

                         D_aux<<P_aux^(-1)Z^C.              (8)

This argument uses the uncut complete column BEFORE any w-dependent mask. It does not claim a corresponding estimate for an arbitrarily masked raw m sum.

On distinct q,q' remove the exceptional auxiliary-label pairs of Section2. In this remaining domain w=0 is impossible: q'a'^2 m=q a^2 m' would force q|m because q does not divide q'a', contradicting the original own-prime unit support. Thus the nonzero squarefree-kernel partition omits no scalar term. Partition the resulting COMPLETE scalar into its small pool and its complementary large squarefree-kernel part L_large. All labels, original phases and the independent auxiliary laws remain in L_large. Equations(2),(8) give the exact signed reduction

 C_cross=Re L_large-Q_full
       +O_epsilon(U P_aux^(-1/64+epsilon)Z^C
                         +P_aux^(-1)Z^C+P_aux^(-B)Z^C).     (9)

In particular, for U=P_aux^(1/128),

       C_cross<=Re L_large+O_epsilon(P_aux^(-1/128+epsilon)Z^C).

This is a reduction of the ORIGINAL whole one-sided cross target to a large-kernel scalar target. It does not require a restricted-class estimate on the small pool, because Q_full has never been split and its sign is known. If a two-sided comparison is wanted, the original full positive-class estimate and Jensen, with the fixed-source moments paid, give Q_full<<Z^(-23/48+epsilon). That optional extra error retains the original normalization and is not an exponential masked-class bound.

Thus the full-label result removes a genuine physical small squarefree-kernel pool from the whole target while preserving its exact complete-class subtraction. It supplies no estimate for L_large itself and does not transfer already paid label or w submasks onto it without their own compatibility proof.

## Part II. Absolute complete-label small power-kernel pruning

### 1. The original physical selection and theorem

Use the same original half-damped positive-orientation observation, its fixed source f, original scalar normalizers, finite compensation, finite ray sectors, all zero extensions, and the complete old T-only restoring operator. At ambient Z take two DISTINCT independent auxiliary primes q,q' of norms comparable to P=exp(Z), with their original positive probability weights. No condition relates the two copies' compensation tuples or their original c,n labels. In particular this is not limited to n=n'=1, equal E/a, all-Ec, or a balanced dyad.

For every original pair write

 g=gcd(c,c'), a=c/g, a'=c'/g,
                 w=q'(a')^2 m-q a^2 m'.                    (1)

For a fixed integer k>=3, choose the standard kth-power-free ELEMENT representatives: the exponent of every prime ideal is between0 and k-1, and its unit component is selected modulo kth powers of units. Then every nonzero w has a unique such representative u_k in w=u_k v^k, with v determined up to the finite group of kth roots of unity in the Eisenstein field. Define the small-kernel set by Nu_k<=U, U>=1.

Let C_(k,U) be the original physical pair sum on this set, with any additional multiplier of absolute value at most1. It may include h!=h', h=h', arbitrary w or label masks, fixed finite-sector restrictions, or a bounded central-source restriction. The claimed bound, for each fixed H>0, is

 |C_(k,U)| <= C_(k,H,f) P^(2/k-1) U^(1-1/k) Z^C
                       +C_(H,f) P^(-H) Z^(C_H).          (2)

The constants and polynomial exponents are independent of U, the auxiliary primes and every original label. The second term pays cross-auxiliary c,n collisions as a whole and therefore has no U factor. The bound applies both before and after the original fixed polynomial outside normalization, by enlarging C.

For example, with any fixed 0<eta<=(k-2)/(k-1) and U=P^((k-2)/(k-1)-eta)>=1, the main term is

                          P^(-(1-1/k)eta) Z^C.           (3)

In particular k=6, for fixed 0<eta<=4/5, U=P^(4/5-eta) gives P^(-5eta/6)Z^C. The literal cube set w=v^3 is a subset of the finitely many unit-kernel k=3 classes and has bound P^(-1/3)Z^C. These assertions now hold on the complete original label support and under arbitrary further bounded masks. They do not address the full k=2 boundary, where absolute counting gives no saving.

### 2. Common-label units and the exact fibre

Pairs on which q or q' divides the opposite column's c n s have the mask-uniform total bound P^(-H)Z^(C_H) for any fixed H, by Appendix A, Section 2. Its proof includes the two raw m absolute costs, every Gaussian tail, the original fixed source and the full restoring series. Own-column divisibility was already zero; the compact polynomial s support excludes opposite-auxiliary s divisibility for large Z.

On the remaining pairs, g,a,a' are pairwise coprime and prime to qq'. Thus Acoef=q'(a')^2 and Bcoef=q a^2 are coprime. All integral solutions of Acoef m-Bcoef m'=w form a translate of

                      m=Bcoef t_f,
                      m'=Acoef t_f,       t_f in O.       (4)

The original own-prime zeros imply q does not divide m and q' does not divide m'. Reducing(1) modulo q and q' therefore shows (w,qq')=1, in particular w!=0. No artificial cross-prime m-hole has been imposed. All remaining original holes merely reduce the absolute counts below.

Freeze two actual compensation tuples and source parameters alpha,alpha'. Put

 x=X/(ND) exp(-alpha),       y=Y/(ND),
 t=T(NE) exp(-alpha),
 x'=X/(ND') exp(-alpha'),    y'=Y/(ND'),
 t'=T(NE') exp(-alpha').

The original outside compensation coefficient is (ND ND')^(-3/2). Set A_norm=Nc(Nn)^3 and A_norm'=Nc'(Nn')^3. For fixed s,s' in their genuine annuli, the original m windows satisfy

 Nm<=C P x Ns,             Nm'<=C P x' Ns'.               (5)

The lattice spacing in(4) gives at most

 C[1+min(x Ns/(Na)^2, x' Ns'/(Na')^2)]
                       <=C(1+xy+x'y')                    (6)

pairs for one w. This holds also at subunit physical scales: a disk in a translated scaled hexagonal lattice has at most C(1+radius^2/lattice-area) points. No smooth fibre approximation is used.

The squared triangle inequality in(1),(5) gives

 Nw<=C P^2[(Na')^2 x Ns+(Na)^2 x' Ns']
     <=C P^2[(A_norm')^2 xy+(A_norm)^2 x'y'] =:W.          (7)

All actual c,n labels are still unrestricted in this formula.

### 3. Counting the selected w and restoring both true radial normalizers

For W>=1 the elementary fixed-field ideal count, with the finite unit choices, gives

 #{w!=0:Nw<=W, N ker_k(w)<=U}
  <=C_k sum_(Nu<=min(U,W)) (W/Nu)^(1/k)
  <=C_k W^(1/k) U^(1-1/k).                               (8)

Here every nonempty v disk has norm radius at least1; all finite root multiplicities only change C_k. If W<1 there are no nonzero w, so the same upper bound is valid. No cancellation or smoothness of the selected physical mask is required.

The original s Gauss sum has the uniform bound |g_(chi_s)(s,-m)|<=Ns, valid for ALL physical s valuations. After dividing by sqrt(Ns) and by the TRUE radial normalizer sqrt(B x Ns), with B=N(b0q) comparable to P, its contribution is at most C(Px)^(-1/2). Therefore, apart from the two c,n Gaussian factors and the compensation coefficients, each m,m' pair has absolute coefficient at most

                        C/[P sqrt(xx') yy'].             (9)

Every original other phase has modulus at most a fixed constant. The actual s,s' annuli contain O(y),O(y') ideals when nonempty, respectively. Their counts cancel yy' in(9). This remains valid below scale1: a nonempty annulus has scale bounded below by a fixed positive constant.

Combine(6)--(9), and use (r+s)^(1/k)<=r^(1/k)+s^(1/k), to obtain a positive bound for the fixed compensation pair and source parameters of

 C_k P^(2/k-1) U^(1-1/k) (xx')^(-1/2)(1+xy+x'y')
  *sum_(c,n,c',n') A_norm^(-1/2)(A_norm')^(-1/2)
       V_G(A_norm/t)V_G(A_norm'/t')
       [(A_norm')^(2/k)(xy)^(1/k)
                        +A_norm^(2/k)(x'y')^(1/k)].        (10)

This is a complete original-label majorant; it has no hidden label count or truncated Gaussian support.

### 4. Complete Gaussian, source and restoring sums

Appendix A proves the all-scale moment

 sum_(c,n) A_norm^(r-1/2)V_G(A_norm/t)<=C_r t^(r+1/2),
                      r>=0, t>0.                         (11)

Apply it at r=0 and r=2/k to(10). The resulting exact scale upper bound is

 C_k P^(2/k-1) U^(1-1/k)
 * (xx')^(-1/2)(1+xy+x'y')
 * [(xy)^(1/k)t^(1/2)(t')^(1/2+2/k)
             +(x'y')^(1/k)t^(1/2+2/k)(t')^(1/2)],          (12)

times the original factor (ND ND')^(-3/2). This explicitly pays every unbalanced c,n label using the original Gaussian, and not a hard polynomial cutoff.

The source dependence of (xx')^(-1/2)t^(1/2)(t')^(1/2) cancels exactly. All remaining unshifted physical and slot scales have fixed polynomial-Z size. Since

 1+xy+x'y'<=Z^C exp(|alpha|+|alpha'|),

and the extra terms in(12) contain respectively exp(-alpha/k-2alpha'/k) and exp(-2alpha/k-alpha'/k), their total source cost is at most

                   Z^C exp((1+2/k)(|alpha|+|alpha'|)).    (13)

For k>=3 this is bounded by Z^C exp(2(|alpha|+|alpha'|)), so the original fixed second exponential L1 source moment already pays the main term. The exceptional-label remainder uses the higher fixed moments already proved in its separate lemma. No source tail has been discarded.

The full old restorer changes only t,t', leaving x,y,alpha, the slots, q,q', w and every physical mask fixed. The two Gaussian powers in(12) are b=1/2 and b=1/2+2/k, both nonnegative. Its independently verified absolute coefficient norm on t^b is at most

 (1+Q^(-b-5/6)+Q^(-6b-4))/(1-Q^(-6b-3)),

uniformly bounded for each auxiliary prime norm Q. Hence its entire numerator and denominator series preserve(12), term by term. This is the old restorer, without a new auxiliary choice or a new label-dependent normalization.

Finally sum the original fixed number of compensation patterns and their actual prime tuples with their bounded profile weights. All such sums and reciprocal physical scales cost only a fixed polynomial in Z. The original c_(S0+q)^(-1) is bounded and A_T(Z)^(-1) costs only a fixed logarithmic power. The two positive auxiliary laws have total mass one; restricting to distinct primes costs no extra factor. Integration against the complete fixed sources and addition of the mask-uniform collision remainder prove(2).

### 5. Exact scope

This is an ABSOLUTE estimate for the selected original physical pair stratum. It can consequently retain h=h', h!=h' or other arbitrary bounded pair masks without invoking an unmasked positive-class theorem. It also permits taking a disjoint union of the allowed k-free classes as a single mask; its entire U dependence is already in(8).

The theorem applies to distinct auxiliary primes. The complete q=q' scalar may separately be removed before any w mask by the existing complete-column bound, but no arbitrary-masked equal-prime estimate is asserted here. The selected full-label small-kernel set is still only part of the original whole target. Its large-kernel complement, the general large-squarefree-kernel scalar and the signed Mobius obstruction remain open.

## Appendix A. Complete Gaussian moments, collisions and restoration

### 1. An all-scale weighted Gaussian identity in inequality form

Write A=Nc(Nn)^3>=1 and

 V_G(x)=(2 sqrt(pi))^(-1) exp(-(log x)^2/4).

For every fixed real r>=0 and every t>0,

 M_r(t):=sum_(c squarefree,n) (Nc)^(-1/2)(Nn)^(-3/2) A^r V_G(A/t)
        <=C_r t^(r+1/2).                                      (1)

This is uniform over original restrictions on c,n, because the majorant is positive. To prove it, the fixed-field ideal count #{c:Nc<=R}<=C R gives, by dyadic summation,

 sum_c (Nc)^(r-1/2) V_G(Nc/u)<=C_r u^(r+1/2),    u>0.          (2)

For completeness, on the norm dyad 2^j<=Nc<2^(j+1), j>=0, the sum is bounded by a constant times 2^(j(r+1/2)) times the supremum of V_G(x/u) on that dyad. Divide by u^(r+1/2) and extend j to all integers. The resulting translates of a Gaussian times exp((r+1/2)x) have a uniformly bounded sum on the fixed logarithmic lattice. This proves (2), including u<1, with no hard cutoff or missing constant term. At u=t/(Nn)^3 the remaining n power in (1) is exactly

 (Nn)^(3r-3/2) (Nn)^(-3(r+1/2))=(Nn)^(-3).

The ideal series sum_n(Nn)^(-3) converges. This proves (1).

Every fixed polynomial in Nc,Nn is bounded by a fixed power of A, since Nc,Nn>=1 and each is at most A. Likewise, for a pair, the working D_label=2+Nc+Nn+Nc'+Nn'+Ns+Ns' obeys D_label^K<=Z^C A^K(A')^K, because the original s,s' annuli have polynomial-Z scales. Thus any fixed polynomial period, residue-table, frequency-envelope or smooth-variation price can be summed against the TWO original Gaussian factors with a fixed power of their true scales. It is preferable to retain the original outside A^(-1/2) and (A')^(-1/2); if they are dropped, (1) with r increased by 1/2 gives the same needed conclusion.

### 2. The exact raw absolute cost and a genuinely exponential collision tail

Let P=exp(Z); both auxiliary prime norms lie in fixed comparable annuli about P. Freeze any two actual compensation tuples. In one column use

 x=X/(ND) exp(-alpha),  y=Y/(ND),  t=T (NE) exp(-alpha),

with original outside factor (ND)^(-3/2). Put B=N(b0 q), so B is comparable to P, and M=B x Ns. The source activation has no additional scalar factor. It leaves y, slots, the auxiliary law and ambient normalizers fixed.

For every M>0 the original smooth annular profile satisfies

 sum_(m!=0) M^(-1/2)|W0(Nm/M)|<=C sqrt(M).                    (3)

Indeed a nonempty annulus requires M bounded below by a positive profile-dependent constant; on that range its lattice count is O(M). Below that threshold its nonzero lattice sum is empty. This handles arbitrarily large positive alpha without inserting a spurious M^(-1/2) term.

Use the genuine trivial complete Gauss bound |g_(chi_s)(s,-m)|<=Ns. Multiplying (3) by the original 1/sqrt(Ns) yields at most sqrt(Bx) Ns before the original y^(-1)W1(Ns/y). Its annular s sum is O(y), so the entire raw absolute physical column with an additional A^r weight is at most

 C_r sqrt(Bx) y t^(r+1/2) (ND)^(-3/2).                       (4)

If the s annulus is empty the expression is zero; otherwise its scale is bounded below by a fixed positive constant and the same O(y) estimate applies. All character, Gauss-root, angular and finite-ray factors outside the s Gauss sum have modulus at most a fixed constant, while every original unit hole and marker only reduces this positive bound. In particular |gamma_2(c)|=1 on the original squarefree support. The two-column raw absolute auxiliary cost in (4) is P, and no higher power of P is hidden in the remaining factors.

Consider pairs for which either auxiliary prime divides the opposite column's c n s. Own-column divisibility is already excluded by the original zero masks. Because Ns,Ns'<=Z^C and P=exp(Z), cross divisibility of s or s' is impossible for sufficiently large Z. For any remaining collision, one completed norm A or A' is at least c0 P, for a fixed c0>0. Indeed q|c' forces Nc'>=c0P; q|n' even forces A'>=(c0P)^3. The weaker common threshold suffices.

For every fixed r>=0,

 1_(A>=c0P or A'>=c0P) <=(A/(c0P))^r+(A'/(c0P))^r.          (5)

Apply (4) with r in one column and zero in the other. Sum the original finite compensation patterns and prime tuples, all of whose supports, reciprocal scales, count and coefficients have only fixed polynomial-Z cost. Include the original bounded c_(S0+q)^(-1) and the fixed logarithmic A_T(Z)^(-1). Before source integration the resulting bound is

 C_r P^(1-r) Z^C exp(C_r(|alpha|+|alpha'|)).                  (6)

The fixed original source satisfies int |f_q(alpha)| exp(L|alpha|) d alpha<infinity for every fixed L. Hence, for every prescribed fixed H>0, choosing the FIXED r>H+1 proves

 absolute complete collision-pair contribution
                    <=C_H P^(-H) Z^(C_H).                  (7)

The order r does not grow with Z. The constants are allowed to depend on H and on the fixed source. This estimate holds on the entire collision set at once, even with any additional bounded physical mask, including a union of square classes, h=h', or h!=h'. There is therefore no extra U factor for (7). It is a direct exponentially small physical tail, not a reuse of a polynomial-Z tail after exponential losses have been incurred.

### 3. The full old T-only restoring series remains summable

For a prime norm Q, the exact old restoring operator is

 (1-Q^(-2))[I-(1-Q^(-1))D_q-kappa(q)Q D_q^6]
       sum_(j>=0) kappa(q)^j Q^(-3j) S_(6j),

where D_q F(t)=Q^(-5/6)F(t/Q), S_j F(t)=F(t/Q^j), and |kappa(q)|=1. It keeps c,n,s,m, the source variable, original slots and all masks fixed. It only decreases the Gaussian scale t.

On an absolute bound proportional to t^b, b>=0, its coefficient norm is at most

 (1+Q^(-b-5/6)+Q^(-6b-4))/(1-Q^(-6b-3)).                    (8)

This is uniformly bounded for all auxiliary primes under consideration. All powers b from (1), (4) and (6) are nonnegative. Thus every argument above survives the COMPLETE finite numerator and infinite denominator series in each column, term by term. The same proof applies to a fixed polynomial-label estimate at each original label pair: summing labels first by (1) produces a nonnegative power of t on which (8) applies. No Gaussian supremum over c,n is substituted before their summation.

Consequently Sections 1--3 rigorously validate the general polynomial-label/source/restorer summation strategy and its cross-auxiliary label-tail input. The fixed polynomial-label price of the Fourier decomposition is proved separately in Part I, Section 3.
