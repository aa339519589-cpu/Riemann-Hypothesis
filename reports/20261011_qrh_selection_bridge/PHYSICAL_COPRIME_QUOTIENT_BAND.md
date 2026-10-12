# A growing coprime-quotient band of the physical signed cross sum

Use the same exponentially large single-prime observation as in [UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md): eta=1, positive auxiliary xi=xi0 chi_p, the half-damped physical n weight, both original/core nonflat markers, all original compensation, the actual c_(S_p), the fixed ambient A_T(Z), and the OLD Gaussian-T restorer. Primes are sampled with that report's probability law at norm comparable to exp(Z), without restricting the prime pool to a ray. The new estimate is unconditional for this observation.

At each finite sector gamma, original squarefree physical c and actual element Kummer class h=[m/c^2], average the complete physical column first:

    V_(gamma,c,h)=sum_p omega_p J_(p,gamma,c,h).

The two copies in its squared norm use independent sampled primes. Define g=(c,c'), and retain the quotient band

    N(c/g) N(c'/g)<=R^2.

For every fixed 0<eta_band<1/18, taking R=Z^(1/18-eta_band) gives the actual mean-before-square off-class estimate

    |sum_gamma sum_(c,c': N(cc'/g^2)<=Z^(1/9-2eta_band))
               sum_(h!=h') V_(gamma,c,h) conjugate(V_(gamma,c',h'))|
       <=C_epsilon Z^(-3/8-eta_band+epsilon).

This includes genuinely different c,c' with growing coprime quotients, and remains valid after removing c=c'. The proof retains the same-class subtraction and pays both of its terms. The remaining larger-quotient Mobius correlation is unestimated; this theorem does not bound the whole cross sum or exclude a zeta zero.

## Exact dependencies and normalization

Part A proves the necessary new all-s literal-unit reduction and divisor-weighted fixed-c estimate, including every original compensation scale. Its fixed-c off-class conclusion alone is a ONE-SIDED upper bound. Part B uses the proof-level bounded-c-phase and small-c-weight version of the already published positive class estimate, plus an exact weighted Schur bound, to obtain the displayed ABSOLUTE band bound. No scalar norm of a whole c-sum is mistaken for a sum of fixed-c norms.

All physical factors, in particular chi_(c n^3)(m), the exact Gauss roots, the scale B Ns X, the sector gamma, common windows and zero masks, are as explicitly defined in the [unconditional single-prime report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md), its introductory physical display and Parts A–B. The raw column-level auxiliary projection is that report's Part B, before summing c into Euler factors. The all-s unit identities use the published [PHYSICAL_KUMMER_BLOCKS.md, Part I A–B](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261011_qrh_selection_bridge/PHYSICAL_KUMMER_BLOCKS.md) and [PHYSICAL_SHORT_CONDUCTOR.md, Part I (12)–(17)](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261011_qrh_selection_bridge/PHYSICAL_SHORT_CONDUCTOR.md). These pinned files have the same exact blobs as the source versions checked for the present proof.

The user's original source, principal-contraction work and phase correction retain their attribution through those public dependencies. This proof uses no conditional finite-order Q input. It concerns the old single-prime T-restorer; it does not claim preservation under a further infinite-prime inverse-H normalization, a first-flat operation or a different observation. No near-fibre cutoff is imposed inside a completed physical column. The [independent mathematical review](REFEREE_PHYSICAL_COPRIME_QUOTIENT_BAND.md) checks both parts and their common original labels. Equation numbers restart in each part.

## Part A. The complete all-s unit column and weighted fixed-c estimate

### 1. Exact object and intended one-sided estimate

Use eta=1, the half-damped physical n weight, the positive auxiliary choice xi=xi0 chi_p with Np comparable to exp(Z), the original/core nonflat marker, all original finite-compensation terms, c_(S_p), and the OLD T-restorer. Keep all slot labels and normalizations fixed at the original ambient Z. Let

 V_(gamma,c,h)=sum_p omega_p J_(p,gamma,c,h),

where c is the ORIGINAL squarefree physical c variable, gamma=A/s is the original finite ray sector, and h=[m/c^2] is the physical Kummer class. The primes in the two copies of this mean are independent.

The fixed-c part of the actual cross-class expression is exactly

 C_= =sum_(gamma,c) sum_(h!=h') V_(gamma,c,h) conjugate(V_(gamma,c,h'))
     =sum_(gamma,c) { |sum_h V_(gamma,c,h)|^2
                                  -sum_h |V_(gamma,c,h)|^2 }.

In particular it is real and has the ONE-SIDED upper bound

                  C_= <= sum_(gamma,c)|sum_h V_(gamma,c,h)|^2.       (1)

No absolute-value bound for C_= is needed or asserted. Completing m on the right of (1) is legitimate; doing so has not removed the negative same-class term with the wrong sign.

The intended conclusion in the original geometry X=Z^(17/48), Y=Z^(23/48), T=Z is

               C_= <= C_epsilon Z^(-31/72+epsilon).                  (2)

Since -31/72=-3/8-1/18, this pays this particular degeneracy with a fixed margin. It does not pay any pair with different physical c, including pairs with a common large divisor.

### 2. The published squarefree-s unit formula

The exact source input is [PHYSICAL_SHORT_CONDUCTOR.md, Part I (12)–(17)](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261011_qrh_selection_bridge/PHYSICAL_SHORT_CONDUCTOR.md), whose unchanged source version was published at commit 5f38092b8d270aec72a68d989e05f5620141452c. It is in the original additive, primary, unit and ray conventions.

For squarefree s the literal original dual unit H=a^6 forces n=r^2. Write c=g c1, s=g s1 with g,c1,s1 squarefree and pairwise coprime. Its full root is precisely

                         mu(c) kappa(r),  kappa=bar(alpha)^6.

In one unmarked row the resulting unit contribution is

 sqrt(X)/Y sum_(g,c1,s1;r)
  mu(g c1)kappa(r)/(Nc1 (Nr)^3) W1(Ng Ns1/Y)
  V_G(Ng Nc1 (Nr)^6/T) phi(D)/ND
  *sum_(z,(z,b*c1*s1)=1) Wtilde0(X (Ng)^5 (Nz)^6/Nc1),                (3)

where D=rad(gr) outside c1s1. In particular z may share primes with g and r. Every marked test and original hole remains attached to (3); the estimates below drop them only in a positive majorant. A fixed gamma-sector indicator is retained as well.

### 3. Higher s valuations on the SAME literal unit frequency

Write the original s=s0 t, with s0 squarefree, t powerful and (s0,t)=1. At each p^k exactly dividing t, k>=2, the original Gauss support together with chi_A(m) forces p not dividing A=c n^3.

For k not divisible by six, the published exact absorption identity gives P^(-k) times a squarefree-residual-s column with the auxiliary character enlarged by chi_p^(-k), Y replaced by Y/P^k, and X,T,c,n unchanged. The substitution m=p^(k-1)m0 and the new auxiliary modulus b*p show that the full-modulus frequency H is unchanged. Hence its literal H=a^6 component is again (3), with the extra true p-unit masks on c,n,s0,z. Its auxiliary root still cancels completely in (3).

For 6|k, use the published TWO complete columns, not a spurious principal auxiliary. Their exact identity is

 P^(-k)[ J_p(X,Y/P^k,T)
       -P^(-1/2) J_p^omega(PX,Y/P^k,T) ],
 omega=bar(xi(p)) chi_s0(p) bar(chi_A(p)).                            (4)

Both complete m columns retain p not dividing A s0. In the first column the old H is its new H. In the second column the substitution m=p^(k-1)m0 makes the new frequency H'=H/p. Thus its contribution to OLD H=a^6 exists only for p|a and has H'=p^5 a1^6.

At p the residual primitive good character is theta=chi_A bar(chi_s0), with p a unit. The second column's factor omega=bar(xi(p))bar(theta(p)) cancels exactly

                 bar(xi(p^5)) bar(theta(p^5))=xi(p)theta(p).

The remaining full root is the same mu(c)kappa(r). Its factor P^(-1/2)sqrt(PX) equals sqrt(X), and its Fourier argument is

        PX * N(p^5 a1^6)/NA = X * N((p a1)^6)/NA.

Consequently the second column in (4) subtracts precisely the p|z terms of the first column, with all phases and zero masks retained. It leaves the single condition p not dividing z. The character at p has not been omitted; its complete boundary/bulk transform has imposed this unit condition.

This also agrees with finite Fourier inversion of the original local Gauss sum at p^k: its complete m transform is proportional to chi_(p^k)(H), which is zero for p|H and equals one when H is a sixth power prime to p.

Applying these exact identities for every p|t gives (3) with

 W1(Ng Ns1/Y) replaced by W1(Nt Ng Ns1/Y),
 (t,c r g s1)=1, and an additional (z,t)=1 mask.                     (5)

There is no additional t-dependent Gauss root or angular character. Equivalently, this is (Nt)^(-1) times (3) at Y/Nt with its genuine added holes. The n-square support is still exact: the squarefree-s primitive argument excludes every prime of n0, while the high-s primes are prime to A. All operations preserve the original c label. For core marked tests this identity is used with the original tests retained, not with a redefined mark.

### 4. A divisor-weighted square estimate in the original c coordinate

Let U_c(X,Y,T) denote the complete unmarked unit column at fixed original c, summed over every physical s and n with (5), in one fixed gamma sector. Put C=Nc. The Schwartz profile satisfies for all v>0

                    sum_(z!=0)|Wtilde0(v (Nz)^6)| << v^(-1/6).       (6)

The bound is uniform below the unit threshold, since then the actual nonzero lattice support and Schwartz tail only improve it. At fixed g|c the argument v is X(Ng)^6/C, so the z sum is at most (C/X)^(1/6)/Ng. The annular s1 count is at most Y/(Nt Ng); this remains a valid bound on every nonempty annulus below one. Therefore (3)-(5) give

 |U_c| <= C X^(1/3) C^(-5/6)
       [sum_(g|c) 1/Ng]
       [sum_(t powerful)1/Nt]
       sum_r (Nr)^(-3)V_G(C(Nr)^6/T).                               (7)

The powerful-ideal series is absolutely convergent, with local nonconstant term beginning at P^(-2). The divisor factor is C^epsilon. Define

 H(V)=sum_r (Nr)^(-3)V_G((Nr)^6/V).

Ordinary ideal counting and the same fixed log-Gaussian give

 H(V)<<V^(-1/3) for V>=1, and H(V)<<_L V^L for 0<V<1.               (8)

Hence for V>0,

 sum_(c!=0) (Nc)^(-5/3)H(V/Nc)^2
                  << V^(-2/3) log(2+V).                             (9)

For Nc<=V the summand is bounded by V^(-2/3)(Nc)^(-1), which gives the logarithm; for Nc>V the small-V branch of (8) is summable. The case V<1 follows directly from the latter branch. The same argument with any prescribed fixed divisor power, or a sufficiently small positive power (Nc)^epsilon, costs only (1+V)^epsilon. Thus

           sum_c d(c)^K |U_c(X,Y,T)|^2
                <<_(K,epsilon) X^(2/3)T^(-2/3)(1+T)^epsilon,        (10)

for each fixed K. This estimate is independent of Y and of the auxiliary norm. The original mu(c) and kappa(r) were not changed, even though their moduli suffice in this diagonal estimate.

### 5. Original finite compensation, with the actual c label retained

In a compensation summand D,E keep the original scalar (ND)^(-3/2), X'=X/ND, Y'=Y/ND, and completed scale T NE. On the true unit support n=r^2, E|c r^6. Split E=Ec Er according as a marked prime divides c or does not; the latter then divides r. The core test is a subset of this support. Keep the original prime distinctness and all shared masks.

Fix Er and its slot assignment. In the r sum put r=Er v. Its factor is (NEr)^(-3) and its Gaussian argument is

                  Nc (NEr)^5 (Nv)^6/(T NEc).

For each c, take Cauchy in the actual marked Ec divisors of c, retaining squared slot weights. Its multiplicity is divisor-bounded in c and is paid by (10). Then set c=Ec c0 in the resulting positive square sum. Equations (8)-(9) give the precise squared costs

                  (NEc)^(-5/3) (NEr)^(-8/3) T^(-2/3),              (11)

apart from X'^(2/3), fixed logarithms and ambient small powers. Thus a fixed Er has norm price (NEr)^(-4/3); the marked-c square sum contains (NEc)^(-5/3).

The original slot sums are consequently all nonincreasing in their scale:

 sum_(p in one marked-c slot) |W_i(Np)|^2 (Np)^(-5/3) << 1,
 sum_(p in one marked-r slot) |W_i(Np)| (Np)^(-4/3) << 1,
 sum_(p in one rescaled slot) |W_i(Np)| (Np)^(-11/6) << 1.          (12)

The last exponent is the exact product of (ND)^(-3/2) and X'^(1/3). No unrestricted l1 sum of c-marked slots was taken. Only finitely many original slot assignments occur. It follows that the whole compensated unit vector, including divisor weights d(c)^K, has

                    ||U||_l2(c) << Z^epsilon (X/T)^(1/3).           (13)

The fixed ambient A_T(Z)^(-1) costs the previously reviewed logarithmic factors. It is not re-evaluated at each smaller Gaussian scale.

On this T^(-1/3) envelope, the OLD restoring D_p=P^(-5/6)[T->T/P] has norm P^(-1/2). Its geometric denominator P^2 D_p^6 consequently has norm P^(-1), and its finite numerator is bounded. For the SINGLE auxiliary p comparable to exp(Z), its complete norm is 1+O(P^(-1/2)), uniformly. The c_(S_p) normalization is 1+O(P^(-1)) relative to c_(S0). Thus the old restored unit vector satisfies the same estimate. No unproved all-prime inverse-H operator estimate in this stronger norm is used.

### 6. Passing from the actual auxiliary mean to this unit vector

Use the coefficient-level original first Poisson identity BEFORE summing c,n,s,a into Euler products. The positive auxiliary multiplier is exactly bar(chi_p(u)) times all original p-unit masks, with c still its original physical variable. On an absolute five-variable box of polynomial size in Z, the conductor of this Kummer character is polynomial in Z, the pool p has norm comparable to exp(Z), and the actual fixed-field prime mean annihilates every nonprincipal u, including the nontrivial unit labels, by any prescribed power of Z. Only literal u=1 remains.

Crucially, the reviewed high proof bounds the error by the SUM OF ABSOLUTE VALUES of the raw coefficients. It therefore also bounds the l1 sum of the error over the retained c labels and finite gamma sectors. The complete original (3,3,2) majorant has five weights c^(-5/2), n^(-7), s^(-2), a^(-12), u^(-2), with exterior X^(-3/2)T^4Y^2 and no auxiliary norm cost. Choosing a sufficiently large fixed polynomial box pays its complement to any desired Z-power. The same argument permits each fixed divisor weight d(c)^K by slightly larger Gaussian/absolute moments. It does not apply prime averaging to an individual long physical m or Kummer-h column.

Define U_(gamma,c) to be the literal unit column for the FIXED base bad set S0, with no moving p-unit hole, and with the original ambient slot normalization; its exact all-s expression is (3)-(5) with b=b0. Removing the moving p-unit holes changes no term in the raw polynomial box, because p is larger than every variable in that box. The difference is entirely in its complement and is therefore O(Z^(-N)) in l1(c), also with each fixed divisor weight, by the same complete absolute tail just described. Thus U_(gamma,c) is independent of the averaged prime p.

The true c_(S_p) scalar and OLD restorer differ from their limiting base unit factors by O(P^(-1)) on these absolute lines; their complete finite numerators and denominators are retained. Their l1(c) error is exponentially small. Hence, after normalization and restoration,

 sum_(gamma,c) d(c)^K |sum_h V_(gamma,c,h)-U_(gamma,c)|
                                                 <<_(K,N) Z^(-N)  (14)

for every fixed N, with the same original c, gamma, slot and window labels. This is the raw coefficient-level form of the already reviewed unconditional single-prime high projection, not a new columnwise Siegel--Walfisz assertion at a conductor of size exp(Z).

Combining (1), (13), and (14) proves the proposed upper bound (2). The same argument gives the corresponding d(c)^K-weighted diagonal envelope. The different-c term retains the genuine mu(c)mu(c') correlation and has not been bounded.

## Part B. Weighted Schur control of the growing quotient band

### 1. Actual c labels and the retained band

Keep the exponential-prime observation, old restorer, all original compensation and common windows, and the original Möbius-bearing coefficient. After prime averaging let V_(gamma,c,h) be its class contribution with its ORIGINAL physical c retained; put S_(gamma,c)=sum_h V_(gamma,c,h). Different compensation terms all use the same original physical c label. Set g=(c,c') and

 A_R(c,c')=1_(N(c/g) N(c'/g)<=R^2), R>=1.

The retained part of the mean-before-square cross expression is

 C_R=sum_gamma sum_(c,c') A_R(c,c')
               sum_(h!=h') V_(gamma,c,h) conjugate(V_(gamma,c',h')). (1)

One may additionally remove c=c', since the same estimate below holds with that diagonal removed. This is a mask on the complete c,c' columns. No restriction on the physical m/m' variables is imposed before completing a column.

### 2. Exact weighted Schur bound

For fixed c, every c' counted in A_R has c=g a, c'=g a', where a|c and Na Na'<=R^2. Use the positive Schur weight w(c)=(Nc)^(-1/2). Elementary ideal counting and partial summation give sum_(Nb<=H) (Nb)^(-1/2)<=C sqrt(H), uniformly for H>=1. Therefore

 sum_c' A_R(c,c') w(c')/w(c)
  <= sum_(a|c,Na<=R^2) (Na)^(1/2)
                  sum_(Na'<=R^2/Na) (Na')^(-1/2)
  <= C R d(c).                                         (2)

Original squarefree/coprimality restrictions can be omitted in this positive majorant. Since A_R is symmetric, weighted arithmetic-geometric mean gives, for any scalar or Hilbert-space family v_c,

 sum_(c,c') A_R(c,c') |<v_c,v_c'>|
  <= (1/2)sum_(c,c') A_R(c,c')
      [(w(c')/w(c))||v_c||^2+(w(c)/w(c'))||v_c'||^2]
  <= C R sum_c d(c)||v_c||^2.                            (3)

The finite-sum inequality passes to infinite families by monotone convergence of the nonnegative majorant. This is a weighted Schur estimate, not an assertion that the unweighted row degree is O(R). The product band contains the rectangle Na,Na'<=R and can include one quotient as large as R^2.

### 3. Verified input and the additional weighted class estimate

Part A proves for its actual fixed base unit projection U_(gamma,c) the all-s, all-marks, old-restorer estimate

 sum_(gamma,c) d(c)|U_(gamma,c)|^2
                    <= C_epsilon Z^epsilon (X/T)^(2/3). (4)

This is the divisor-weighted form of Part A, Sections 3–6, checked in the corresponding part of the [independent review](REFEREE_PHYSICAL_COPRIME_QUOTIENT_BAND.md). It comes from the exact half-damped r^-3 column and the complete-s unit reduction, rather than from a scalar whole-high formula. The fixed base U has no moving auxiliary-prime hole.

The published [uniform-large-B positive class proof, Part A](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md) extends, at the proof level, to independent bounded phases in the ORIGINAL c label: these phases are independent of the common sixth-power-free h0 variable, and the proof takes absolute values of their products in its principal pair majorant and nonprincipal remainder. Its exact h0 character, holes, lattice density and all marked Gaussian scales are unchanged.

For the required divisor weight, use d(c)<=C_eta (Nc)^eta. Insert (Nc)^(eta/2) in each physical c coefficient before running that proof. In the common pair c=g a,c'=g a', the new factor is (Ng)^eta (Na Na')^(eta/2). The harmonic Gaussian g bound gains at most a fixed small power of its real scale; all a/a' sums remain convergent for sufficiently small eta. At marked c slots the new factors are fixed small powers of the actual slot norms, so their total cost is Z^(C eta). The n sums retain strict convergence after these small shifts. The full nonprincipal error remains B^(-1/4)Z^C. Powerful-s branches and the old T-only restorer preserve the original c label; their strict convergence margins also permit a sufficiently small eta. Taking eta after the final epsilon pays the divisor weight with Z^epsilon and introduces no B^epsilon.

Apply the thus-weighted positive bound first with independent Rademacher phases in finite c cutoffs and average the signs. Only equal ORIGINAL c labels survive. Then use Jensen for the auxiliary prime mean and pass to the full Gaussian sums by their absolute domination. The resulting needed class estimate is

 sum_(gamma,c,h) d(c)|V_(gamma,c,h)|^2
                      <= C_epsilon Z^epsilon Y^(-1)+exp(-c Z)Z^C. (5)

The preceding argument uses the full marked and all-s steps of the published Part A pair proof; it does not differentiate its final estimate. This phase/weight extension has been independently checked against that proof.

Finally the raw complete-m first-Poisson proof, with each c label kept outside the sums, gives

 sum_(gamma,c) |S_(gamma,c)-U_(gamma,c)|=O_N(Z^(-N))       (6)

for every fixed N, provided U has its true original normalization and fully restored unit contribution. On the absolute high lines the c-labelled l1 estimate has precisely the old total majorant. Truncate all raw labels at Z^L, apply the independent p and p' laws (not a same-p ratio mean), and pay full raw tails; choosing L after N gives (6). The finitely many sectors are retained row restrictions. The original Gauss roots cancel only through that complete-column identity. Equation (6) is a vector refinement of the existing raw-coefficient high argument; it is not a bound on U.

### 4. Deduction for the band

The exact class algebra in (1) is

 C_R=sum_gamma sum_(c,c') A_R(c,c')
     [S_(gamma,c) conjugate(S_(gamma,c'))
       -sum_h V_(gamma,c,h) conjugate(V_(gamma,c',h))].    (7)

Use (6) and the polynomial absolute mass of the complete principal source to replace S by U at O_N(Z^-N) cost. For completeness, the fixed-c pointwise bound and its Gaussian H estimate give directly

 sum_c |U_c(X,Y,T)| <= C_epsilon X^(1/3)T^(1/6)(1+T)^epsilon.

Indeed c<=T contributes X^(1/3)T^(-1/3)sum_(Nc<=T)(Nc)^(-1/2+epsilon), and c>T is paid by the arbitrary Gaussian tail; the same bound is valid for T<1 with a fixed constant. The finite slots and their fixed normalizers cost only a polynomial in Z here. The old restorer is bounded on a T^(1/6) envelope. Thus the full compensated sum over the finite sectors has sum_(gamma,c)|U_(gamma,c)|<=Z^C for some fixed C. The mask A_R has modulus at most one, so no pair-count factor is needed in this l1 error step.

Applying (3) to the scalar U and separately to the Hilbert vector (V_(gamma,c,h))_(gamma,h), then using (4)--(5), gives

 |C_R| <= C_epsilon R Z^epsilon [(X/T)^(2/3)+Y^-1]
                                           +O_N(Z^-N). (8)

Here R may be any fixed polynomial in Z, and the exponentially small term in (5) is absorbed. Original Möbius signs and Gauss phases have not been changed; the estimate is obtained only for the indicated restricted pair set.

At X=Z^(17/48),T=Z,Y=Z^(23/48), equation (8) becomes

 |C_R| <= C_epsilon R Z^(-31/72+epsilon)+O_N(Z^-N),       (9)

since -23/48<-31/72. Therefore for each fixed 0<eta<1/18, the growing band

 R=Z^(1/18-eta)

obeys |C_R|<=C_epsilon Z^(-3/8-eta+epsilon). It includes genuinely different c,c' whose coprime quotients grow with Z. Equivalently the retained band is N(cc'/(c,c')^2)<=Z^(1/9-2 eta). Its complement remains unestimated. The exact arithmetic coefficient on that complement is still the original long Möbius correlation.
