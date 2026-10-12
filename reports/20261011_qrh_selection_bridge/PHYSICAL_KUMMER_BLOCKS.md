# Full physical Kummer blocks and powerful-s signed cancellation

Two complementary unconditional statements are proved for the actual physical columns, with the original primary conventions, finite ray data, and zero-extended characters retained.

1. On the literal family c squarefree, n=r^2, s=c t with t powerful and (c,t)=1, summing the complete m column first gives arbitrary fixed power decay Z^(-A), uniformly in the primitive auxiliary modulus and all Gaussian scales 0<T<=Z. This holds for both original and half-damped n weights. The Gaussian-restoring operation is asserted only for the half-damped observation.
2. For the half-damped observation with the published inverse-sextic auxiliary choice xi=xi0 conjugate(chi_b), and every physical n and s, the square root of the complete positive within-Kummer-class energy is at most Z^(-5/32+epsilon), after the actual finite compensation, original/core marks, original normalization and Gaussian restoration. No Q is used. This is still weaker than Z^(-3/16) by 1/32; the cross-class contribution remains unestimated.

The first theorem is a signed physical subtraction before forming positive class energies. It does not permit removing entries from an already-positive class norm. The second theorem does not bound the whole observation. Neither supplies the missing whole-low comparison or proves RH.

## Original physical object and public dependencies

Use K=Q(sqrt(-3)), its original primary generators, N for the ideal norm, and the same primitive auxiliary character xi modulo b*, with B=N(b*). Let

    g_psi(s,k)=sum_(d mod s) psi(d)e(kd/s),
    tau=B^(-1/2)g_xi(b*,1),   Xi(A)=xi(A)chi_A(b*),
    V_G(u)=(2 sqrt(pi))^(-1)exp[-(log u)^2/4].

Every local component of xi is nonprincipal and has order dividing six; all residue characters are zero on nonunits. In the notation of the original source, for A=c n^3 the actual half-damped summand is

    [W1(Ns/Y)/Y] [chi_s(b*)/(tau xi(s))] xi(m)
    [g_(chi_s)(s,-m)/(Ns)^(1/2)]
    gamma_2(c) conjugate(alpha(A)) conjugate(G(A)) eta(A)
    Xi(A)^(-1) R(A,s) chi_A(m) (Nc)^(-1/2)(Nn)^(-3/2)
    (B Ns X)^(-1/2) W0(Nm/(B Ns X)) V_G(NA/T).

Here eta=1; c is squarefree and the ideals retain their original S-unit restrictions. The original observation replaces (Nn)^(-3/2) by (Nn)^(-1). This is obtained directly by Gaussian Mellin inversion of the source's general-probe definition and its corrected row. In particular, the true chi_A(m) phase and its shared-prime zero mask remain present; the auxiliary phase never replaces it. All normalized primitive Gauss roots include their full CRT factors.

A physical Kummer coordinate is the element class [m/s^2] in K^times/K^(times 6), including its unit component. When relating this partition to the auxiliary second moment, retain a fixed finite-ray sector gamma=A/s first. This is a finite positive decomposition, not conditioning the auxiliary prime pool. Additional such bounded row restrictions are permitted by the positive proof below.

The [pinned original source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) fixes general-probe/Psi, the primary and Gauss conventions and all finite-compensation coefficients. The [half-damped observation](HALF_DAMPED_PROBE.md), [auxiliary ensemble](POLYNOMIAL_AUXILIARY_ENSEMBLE.md) and [Gaussian-restored comparison](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261011_qrh_selection_bridge/RESTORED_AUXILIARY_COMPARISON.md) fix the unchanged data used here. The precise complete-m base cancellation is [PHYSICAL_SQUARE_RESONANCE.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/dde3bf1526f28311f4cd6f527c1cc7c80bf6f4a6/reports/20261011_qrh_selection_bridge/PHYSICAL_SQUARE_RESONANCE.md).

The classical all-primitive-character large sieve used in Part III has a complete proof in [QUADRATIC_DUAL_N1.md, Part XXIII A, Section 1](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d74308ed56639ddf0505f1e50007f79337d367da/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md). Its full-column dual kernel is D+Q^2; no unproved fixed-order or moving-conductor strengthening is used. [The accompanying independent review](REFEREE_PHYSICAL_KUMMER_BLOCKS.md) records the exact phase, domain of summation and scale checks. Formula numbers are local to each part.

# Part I. Exact complete-column reductions

## A. Nonprincipal s valuations

### 1. The identity with all scalar normalizations

Let I_(S,xi)(X,Y,T) be the original unmarked physical probe, with fixed target eta and either the original or half-damped physical n weight. Write b* for its genuine primitive auxiliary modulus, tau_xi for its full normalized Gauss sum, and Xi(A)=xi(A)chi_A(b*). Fix a good prime p outside S and put P=Np. Let k>=1 with j=k mod6 in {1,2,3,4,5}. On the original physical sum, select

                  v_p(s)=k,  (p,A)=1,  A=c n^3.           (1)

Define new admissible data

 S+=S union {p}, b*+=b* p, xi+=xi chi_p^(-j),
 Xi+(A)=xi+(A)chi_A(b* p),
 tau+=tau_xi tau_(chi_p^(-j)) xi(p)chi_p^(-j)(b*).

Every character remains zero-extended at its true modulus; the new local auxiliary character is nonprincipal and has order dividing six. The finite reciprocity ray group is unchanged. Then the contribution selected by (1) is exactly

                  P^(-k) I_(S+,xi+)(X,Y/P^k,T).           (2)

No Gauss root, norm factor or external unit phase is suppressed in (2). For k>=2, the condition (p,A)=1 in (1) is automatic on the original nonzero support, so the formula applies to the entire v_p(s)=k branch. For k=1 it must be retained: the possible common p|A,s branch is not covered by (2).

### 2. Prime-power support and the normalized finite transform

Write s=p^k s0 with p not dividing s0. The local character at p is chi_p^j. Its primitive Gauss lift vanishes unless

                      m=p^(k-1)m0, (p,m0)=1.              (3)

This is an exact valuation condition, not only a congruence modulo six. The original completed coefficient contains chi_A(m), including the zero condition (A,m)=1. Thus k>=2 in (3) indeed implies p not dividing A.

For gamma_j(p)=g_(chi_p^j)(p,1)/sqrt(P), the full CRT formula and scaling by a unit at s0 give

 g_(chi_s)(s,-m)/sqrt(Ns)
   =P^((k-1)/2) gamma_j(p)
      chi_p(s0)^j chi_(s0)(p) conjugate(chi_p^j(-m0))
                         g_(chi_(s0))(s0,-m0)/sqrt(Ns0).  (4)

In particular every reciprocity factor linking p and s0 remains. Formula (4) is valid even when the residual character at s0 is imprimitive. Its scaling covariance uses only that p is a unit modulo s0.

### 3. Coefficientwise verification of (2)

Set rho=chi_p^(-j). The primitive Gauss conjugation formula gives

       gamma_j(p) conjugate(chi_p^j(-1))=tau_rho^(-1).

The extra factors from xi(m)/xi(s) and chi_s(b*) are respectively conjugate(xi(p)) and chi_p^j(b*). Together with the preceding Gauss root they are exactly the ratio of tau+^(-1) to tau_xi^(-1). The factor in m0 from (4) is rho(m0), exactly the added auxiliary character.

The s0 cross factor is

 chi_p(s0)^j chi_(s0)(p)=chi_(s0)(p)/rho(s0),

which is the required change in chi_(s0)(b*)/xi(s0).

For the completed row, reciprocity in the original convention is
chi_A(p)=R(A,p)^(-1)chi_p(A). On (1), all terms are units at p, and

 R(A,p)^k chi_A(p)^(k-1)
      =R(A,p)chi_p(A)^(j-1)
      =[Xi+(A)/Xi(A)]^(-1).                              (5)

Thus the original R(A,s)chi_A(m) becomes exactly the new completed-row correction R(A,s0)chi_A(m0)Xi+(A)^(-1). The factors involving eta, alpha, G and gamma_2(c) are unchanged, because c,n and A are unchanged and p-units. This proves the entire phase identity, rather than only an equality of absolute values.

Finally the original radial factor and its square-root normalization become

 P^((k-1)/2)/(B P^k (Ns0) X)^(1/2)
       =1/(B P (Ns0) X)^(1/2),
 W0(P^(k-1)Nm0/(B P^k (Ns0)X))
       =W0(Nm0/(B P (Ns0)X)),

where B=N(b*). These are exactly the new b* p factors. The smooth s normalization is

 Y^(-1) W1(P^k Ns0/Y)
      =P^(-k)(Y/P^k)^(-1)W1(Ns0/(Y/P^k)).

The Gaussian has the same A and T. Every zero mask in the new probe is already forced by (1) and (3). This proves (2).

### 4. The genuinely hidden k=5 mod6 layer

For k=5+6a, the new auxiliary factor is rho=chi_p, not conjugate(chi_p). This opposite orientation must not be replaced by the optimized auxiliary choice used in the separate prime ensemble. The physical substitution is

 s=p^(5+6a)s0, m=p^(4+6a)m0,
 X unchanged, Y replaced by Y/P^(5+6a),
 b* replaced by b* p, and outside coefficient P^(-5-6a).

For any other auxiliary prime q, its exact pair-label phase sees the factor
chi_q(p^(k+1))=1. Thus this layer is truly invisible in the Kummer class of m/s^2. Identity (2) retains it as an actual rescaled observation with its full new primitive auxiliary root and mask; it does not call that layer small merely because the pair character is principal.

Several prescribed hidden primes may be extracted successively using (2). Each step uses the current full tau and xi, so the final tau includes every internal CRT factor. For a squarefree product d of those primes and k_p=5+6a_p, the scalar is product P^(-k_p), the new auxiliary character is xi chi_d, and Y is divided by product P^(k_p). This is an exact finite reorganization. A uniform estimate or an infinite sum over such data still needs the actual scale, masks and coefficient budget.

### 5. Outer operations and excluded branches

The formula is first an identity for a base physical observation or a fixed existing compensation summand. A marked condition involving A may be retained coefficientwise. If its selected prime is p, that positive marked branch is zero because (p,A)=1. If p is one of the already rescaled primes, the original outside coefficient and slot label stay where they were; (2) does not authorize redefining the entire slot system with p deleted from it.

Likewise an already chosen restoring operator A_b retains its OLD set of dilation primes after applying (2). No new A_p is silently inserted. If the old normalized row is I/c_S, expressing it through the new normalized I+/c_S+ introduces the exact scalar c_S+/c_S=(1-P^-1)^2. One cannot relabel this as a fully restored enlarged ensemble without paying those changes.

The principal local characters k=0 mod6 are not covered: their Gauss transform is Ramanujan, with both the boundary v_p(m)=k-1 and the full bulk v_p(m)>=k. The branch k=1 with p|A also stays explicit. These are the true remaining local cases.

All identities begin with finite physical cutoffs or original absolute convergence and may then be passed through the original Gaussian tails. They do not invoke Q or the phase-defective moving Gauss-hole identity. The source is the pinned general-probe and its Xi/Psi definitions, with the unchanged positive additive convention.

## B. Principal s valuations

### 1. Definitions and the precise identity

Use the original physical probe with its genuine primitive auxiliary xi modulo b*, full normalized root tau, and either original or half-damped n weight. Fix a good prime p outside S, P=Np, and k>=6 divisible by six. In the original sum select v_p(s)=k. Its nonzero Gauss support has v_p(m)>=k-1, so the completed coefficient chi_A(m) forces p not dividing A=cn^3.

For the SAME original auxiliary data, define J_p(X,Y0,T) to be the complete physical probe with the additional restrictions p not dividing A and p not dividing s0, using s0 as its physical s variable. Its m sum is complete. Define J_p^omega by additionally multiplying each c,n,s0 row by the unit scalar

             omega_p(A,s0)=conjugate(xi(p))
                             chi_(s0)(p)conjugate(chi_A(p)). (1)

The additional restrictions ensure these character values are units. No new character is inserted into the m column. Then the original valuation-k branch is exactly

 P^(-k) [ J_p(X,Y/P^k,T)
             -P^(-1/2) J_p^omega(PX,Y/P^k,T) ].           (2)

All original eta, finite-ray, unit, c/n coefficient, and Gaussian factors remain. Both columns on the right have complete m sums, not unit-truncated m sums. In particular (2) must not be replaced by a single term with a principal auxiliary character added at p.

### 2. Boundary and bulk calculation

Write s=p^k s0 with p not dividing s0. The local s character at p is principal. Its Gauss transform is

        -P^(k-1)          if v_p(m)=k-1,
         P^(k-1)(P-1)    if v_p(m)>=k,
         0               otherwise.

The residual s0 Gauss transform retains its exact CRT factor chi_(s0)(p)^k. Since k is divisible by six, every k-th power of xi(p), chi_A(p), chi_p(b*), and the reciprocity phase R(A,p) is one.

On the bulk set put m=p^k m1. Scaling the residual Gauss transform cancels its entire chi_(s0)(p)^k factor. The completed character and xi factors also cancel their k-th powers. The normalized bulk column is therefore

 (1-P^(-1)) times the original complete m1 column
                   at the scales (X,Y/P^k,T),            (3)

after factoring out the common P^(-k) from the original Y normalization.

On the boundary put m=p^(k-1)m0 with p not dividing m0. The Gauss scaling leaves exactly one chi_(s0)(p), while xi(m)/xi(s) leaves conjugate(xi(p)) and the completed correction leaves conjugate(chi_A(p)). These are precisely (1). The normalized boundary is

 -P^(-1/2) omega_p(A,s0) times the m0 column
                  at (PX,Y/P^k,T), restricted to p-units. (4)

To verify the norm, its old factor is -P^(-1)/sqrt(B Ns0 X); this is -P^(-1/2)/sqrt(B Ns0 PX). Its radial window is W0(Nm0/(B Ns0 PX)), as required.

Expand the unit restriction in (4) as all m0 minus p times all m1. Under m0=p m1, the remaining complete row picks up

             xi(p)chi_A(p)conjugate(chi_(s0)(p))

from the auxiliary factor, completed character and Gauss scaling. It cancels omega_p exactly. The sqrt(P) change between the two radial normalizations makes this removed part contribute +P^(-1) times the original column at X. Adding it to (3) gives coefficient one. This proves (2), including every mask and phase.

### 3. Exact Kummer-class map

Let square brackets denote classes in K^times/K^(times 6), including their original unit component. On the bulk,

          [m/s^2]=[p^(-k)m1/s0^2]=[m1/s0^2].

On the boundary,

          [m/s^2]=[p^(-k-1)m0/s0^2]=[p^(-1)m0/s0^2].

Thus (2) is also an identity of Kummer-class vectors: its first column uses the identity class permutation, and its second uses multiplication by the fixed class [p^(-1)]. In the removed p-multiple part of the second column, this permutation agrees exactly with the first, which is why their bulk cancellation remains coefficientwise valid within the original class space.

The original finite ray label A/s similarly changes only by the fixed factor p^(-k); a complete fixed-ray partition is merely permuted. If a positive proof instead fixes s0 first, the multiplier (1) is a fixed s0 scalar times the row phase conjugate(chi_A(p)). It is independent of the free m variable and of any further d,z parametrization of m. It may therefore be incorporated into an arbitrary-coefficient conductor large-sieve row without changing that family's primitive characters or its coefficient absolute values. A proof requiring special signed row coefficients rather than arbitrary coefficients would need to check this separately.

### 4. Outer labels and iterative use

The identity is applied first at a fixed original compensation summand. Its old slot coefficient and all marked tests are kept. If a marked test forces p into A, the selected branch is zero. If p is already an external rescaled slot, it is not removed from that slot system. The old normalization c_S and restoring operator retain their original auxiliary primes; no new A_p is inserted.

Several principal higher valuations can be reduced successively. Their powers P^(-k) and shifted X scales are real and must be paid. The phase in each step uses the current actual auxiliary data. For norm estimates allowing arbitrary bounded row coefficients, the triangle cost of one such step is at most the sum of the corresponding X and PX column norms with weights 1 and P^(-1/2), respectively. This is not an assertion of signed monotonicity.

Nonprincipal higher valuations use the separately reviewed identity with new auxiliary factor chi_p^(-j), outside P^(-k), and Y/P^k. Their original class is multiplied by [p^(-k-1)], again a fixed permutation. The k=1 branch sharing p with A is not reduced by either higher-valuation rule and remains part of the final squarefree-s problem.

The sole source input is the original general-probe/Psi definition at fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, its positive Gauss convention, and exact primitive/Ramanujan CRT. No Q, completion shift, or auxiliary prime-average estimate is invoked.

# Part II. Powerful-s signed cancellation

## 1. Precise subfamily and uniform assertion

Work with the original eta=1 physical probe and its half-damped n weight, fixed original primary conventions, and an arbitrary admissible primitive auxiliary character xi modulo b*. Put B=N(b*). A powerful ideal means an ideal all of whose nonzero prime valuations are at least two; the unit ideal is included. In each actual compensation summand select the literal tuples

        c squarefree, n=r^2, s=c t,
        t powerful, (c,t)=1.                              (1)

All original unit and finite-ray factors are retained. On the nonzero support of (1), one moreover has

                            (r,t)=1.                      (2)

If p divides t, the s Gauss transform is supported on v_p(m)>=v_p(s)-1>=1, whether its local character is principal or not. The original completed coefficient chi_(cr^6)(m) vanishes when p divides r. This proves (2) without deleting a nonzero term.

Thus c is exactly the product of the valuation-one primes of s on this family. No claim is made about an additional unit orbit that is not a literal tuple in (1).

Freeze the ambient Z, all original slot windows and auxiliary data. For each compensation subset with size parameter d in [0,1/6], the actual scales are

 X'=Z^(17/48-d), Y'=Z^(23/48-d),
 T_eff=T N(p_(J^c)) << Z^(7/6-d), 0<T<=Z,                 (3)

up to fixed compact ratios. Let I_pow,b(T) be the contribution of (1) to the full finite compensation, with original or core nonflat marks. Then for every prescribed A0>0,

                  |I_pow,b(T)| <<_(A0) Z^(-A0)            (4)

uniformly in all 0<T<=Z and all admissible auxiliary moduli and characters. No Q is used. The published Gaussian restorer A_b, the original normalization c_Sb^(-1), the positive finite auxiliary ensemble, and the ambient slot normalization A_T(Z)^(-1) preserve (4).

## 2. Absorb every nonprincipal higher s valuation exactly

Factor t=t_* v^6, with disjoint prime supports, by placing into v^6 precisely those prime powers of t whose exponent is divisible by six. Thus if p^k exactly divides t_*, then k>=2 and j=k mod6 lies in {1,2,3,4,5}. The exact absorption identity proved in Part I A for such a prime is

 I_(S,xi)(X,Y,T)|_(v_p(s)=k, p not dividing A)
      =P^(-k) I_(S union p, xi chi_p^(-j))(X,Y/P^k,T),    (5)

where A=cn^3 and every mask and full primitive Gauss root changes according to the actual CRT. Here p not dividing A follows from (1)--(2). This is an identity before any absolute values, not a smooth reweighting of the s cutoff.

Apply (5) for all primes of t_*, always with the current full auxiliary modulus and Gauss root. Write K=N(t_*). The exact outside coefficient is K^(-1), the s scale becomes Y'/K, and the new auxiliary character xi_* modulo

                       b_* rad(t_*)

has local factor chi_p^(-j) at every new prime. Each local factor is nonprincipal, hence the whole character remains primitive. In particular, at k=5 mod6 the factor is chi_p, not conjugate(chi_p). All internal CRT phases are included in the new normalized tau.

The remaining physical s variable is c v^6, while c,r,T_eff and X' are unchanged. The exact physical s normalization satisfies

                  K^(-1)(Y'/K)^(-1)=(Y')^(-1).           (6)

The original marked tests and outside slot coefficients are kept. A test forcing a prime of t_* into A gives zero. Even when a prime of t_* is an existing rescaled slot prime, no slot is removed or redefined. The old c_Sb normalization and old restorer prime set also remain in force; neither is silently enlarged.

## 3. Keep all principal Ramanujan boundary and bulk terms

Temporarily write xi_* as xi and its full modulus norm as B_*; all ensuing estimates are uniform in that modulus. Put C=Nc, R=Nr, V=Nv, and D=rad(cr). The supports give (v,cr b_*)=1.

For s=c v^6, primitive Gauss CRT is exactly

 g_(chi_s)(s,-m)/sqrt(Ns)
       =gamma_1(c)conjugate(chi_c(-m))c_(v^6)(m)/V^3.

The possible CRT factor chi_c(v^6) is one, and the principal local Ramanujan sum is invariant under all unit rescalings. Multiplication by the original chi_(cr^6)(m) gives

 gamma_1(c)conjugate(chi_c(-1))
                          1_((m,cr)=1)c_(v^6)(m)/V^3.    (7)

Define the normalized full auxiliary column

 C_xi(U;D)=U^(-1/2) sum_m xi(m)1_((m,D)=1)W0(Nm/U).

The exact Ramanujan identity

 c_(v^6)(m)=sum_(e|rad(v), v^6/e|m) mu(e)V^6/Ne

and the substitution m=(v^6/e)k show that, with M=B_* C V^6 X', the complete normalized m factor is

 M^(-1/2) sum_m xi(m)1_((m,D)=1)c_(v^6)(m)V^(-3)W0(Nm/M)
   =sum_(e|rad(v))mu(e)conjugate(xi(e))(Ne)^(-1/2)
                                  C_xi(B_* C Ne X';D).   (8)

Here xi(v^6)=1. There is no additional v-unit condition on k in (8). Keeping such a condition would incorrectly discard the Ramanujan bulk. The phase conjugate(xi(e)) is retained.

## 4. Uniform primitive Poisson estimate

For every U>0 and fixed L>=0, the complete primitive character Poisson formula gives

 |sum_m xi(m)W0(Nm/U)| <<_L sqrt(B_*)(B_*/U)^L.            (9)

For U>=B_*, its dual zero vanishes and the whole nonzero Schwartz tail proves (9). For U<=B_*, the entire two-dimensional dual lattice is O(sqrt(B_*)), which is sufficient for the same bound. The constants are uniform in the modulus, character, and generator rotation.

Expand the original D-unit mask once, preserving its character factors. Since each mask divisor has norm at most CR, equation (9) yields

 |C_xi(B_* C Ne X';D)|
 <<_(L,epsilon) (C Ne X')^(-1/2)(CR)^epsilon
                                         [R/(Ne X')]^L. (10)

The entire norm B_* cancels exactly. Equations (8)--(10), for L>0, give

 |complete normalized m column|
 <<_(L,epsilon) (C X')^(-1/2)(CR)^epsilon(R/X')^L
                          sum_(e|rad(v))(Ne)^(-1-L)
 <<_(L,epsilon) (C X')^(-1/2)(CR)^epsilon(R/X')^L.         (11)

The divisor sum is bounded by zeta_K(1+L). In particular there is no hidden t_*,v, auxiliary norm, or number-of-new-primes factor. This also proves (11) when R>X', as a permitted larger upper bound. Combining with (6) transfers (11) back to the exact original observation with its original s window.

## 5. Powerful-ideal count and every actual scale

The half-damped c,n coefficient has absolute value C^(-1/2)R^(-3). The original Gaussian is V_G(C R^6/T_eff). Equations (6) and (11) give

 |I_pow,b,subset(T)|
 << (Y')^(-1)(X')^(-1/2-L)
       sum_(C Nt~Y', t powerful) C^(-1+epsilon)
       sum_r R^(L-3+epsilon)V_G(C R^6/T_eff).             (12)

The other masks and marked divisibility tests can be kept before enlarging this positive upper bound. For each fixed L>2, the full Gaussian moment is

 sum_r R^(L-3+epsilon)V_G(C R^6/T_eff)
                  <<_(L,epsilon)(T_eff/C)^((L-2+epsilon)/6).

It includes T_eff/C<1 and retains its original rapid tail. Since C>=1, drop its negative power on the right. Every powerful ideal t has a unique expression a^2 b^3 with b squarefree, so the number with Nt<=H is O(H^(1/2)); ideal counting and the convergent sum over b of Nb^(-3/2) suffice. For each t, the annular sum of C^(-1+epsilon) is O((Y')^epsilon). Thus

 |I_pow,b,subset(T)|
 << Z^epsilon (Y')^(-1/2)(X')^(-1/2-L)
                                        T_eff^((L-2)/6). (13)

Preserve the SAME subset parameter d in (3). The coefficient of L in the exponent in (13) is

       -(17/48-d)+(7/6-d)/6 = -23/144+5d/6 <= -1/48.

Its constant part is

       -(23/48-d)/2-(17/48-d)/2-(7/6-d)/3
                           =-29/36+4d/3 <= -7/12.

Consequently the subset is O(Z^(-7/12-L/48+epsilon)). The total original fixed-slot tuple mass costs at most Z^(1/6), while each original coefficient (N p_J)^(-3/2) has absolute value at most one. Hence

                   |I_pow,b(T)| << Z^(-5/12-L/48+epsilon). (14)

Choosing L as a fixed number after A0 proves (4), with every powerful t, all physical r, all original subsets, and all 0<T<=Z. No derivative or Schwartz order grows with Z.

## 6. Restored observation and allowed subtraction

The original restoring operator only dilates T, and therefore preserves the selected literal support (1). On sup_(0<T<=Z), each factor has norm at most 1+O(P^(-5/6)); the original prescribed polylogarithmic-pool product is O(1). The ORIGINAL c_Sb^(-1) is O(1). The auxiliary absorption used inside the proof does not alter that normalization or introduce restoring factors for its new primes. Positive finite ensemble averaging preserves (14), and A_T(Z)^(-1) costs only a fixed logarithmic power.

The complete m column is summed before any positive Kummer-class decomposition. Thus this theorem permits subtracting I_pow,b from the exact signed observation before squaring. It cannot be applied separately to each already-positive within-class energy. The complementary tuples, including unmatched valuation-one s primes and nonsquare physical n, remain to be estimated.

## 7. The original n weight: a separate physical corollary

The same signed subtraction also holds for the original physical n^(-1) weight, without introducing a new restoring operator. On n=r^2 its coefficient is R^(-2) instead of R^(-3). For fixed L>1 the full r-Gaussian moment is consequently (T_eff/C)^((L-1+epsilon)/6), so (13) is replaced by

 Z^epsilon (Y')^(-1/2)(X')^(-1/2-L) T_eff^((L-1)/6).

Keeping the same subset parameter d gives subset exponent at most -5/12-L/48, and the complete slot mass gives -1/4-L/48. Hence arbitrary fixed power decay follows for the ORIGINAL n-weight physical signed family (1), uniformly in all admissible auxiliary data and T<=Z. The original c_S normalization and positive finite auxiliary average may also be taken. The previously reviewed Gaussian restorer and its claim in Section 6 remain statements about the half-damped observation; this corollary does not assert that the same restoration formula is a principal restorer for the original n weight.

# Part III. Squarefree-s positive norm

## 1. Original object and assertion

Use the original half-damped physical probe, with its exact factor chi_A(m), A=c n^3, c squarefree, and n weight (Nn)^(-3/2). Keep the original primitive finite-order auxiliary xi modulo b*, B=N(b*), including all its CRT phases, all original fixed data, all zero extensions and the actual radial window

                 M_s=B (Ns) X.

Let E be the squarefree marked ideal, coprime to b*. Either original marking E|c n^3 or the more restrictive core marking is permitted. In this note retain only SQUAREFREE physical s. For every sixth-power class h in K^times/K^(times 6), let I_(b,E,h)^sf(X,Y,T) be the contribution of this s-subfamily whose m/s^2 belongs to h, with the entire original c,n,m sums and Gaussian retained. The class includes the original unit component. Define

       N_(b,E)^sf(X,Y,T)=(sum_h |I_(b,E,h)^sf(X,Y,T)|^2)^(1/2).

For X,Y>=1, BXY>=1 and T>0, the assertion is

 N_(b,E)^sf(X,Y,T)
   <<_epsilon (BXY(1+T)NE)^epsilon
       Y^(-1/2) (NE)^(-1/2)
       [1+T (BXY)^(-1/3)].                              (1)

The constants depend on the fixed profiles, field and fixed bad conventions, and not on B or the particular primitive admissible xi. No Q or zero-density theorem is used. Fixed compact ratios in the X,Y windows are permitted. A finite number of unit/ray components only changes the fixed constant.

## 2. The true class support; no false character factorization

For squarefree s, primitive Gauss support forces (m,s)=1. Choose the sixth-power-free representative h of the element class m/s^2, with all original unit conventions retained. Prime valuations give EXACTLY

 s | h_4,       h=s^4 d,       m=d z^6,       (s,dz)=1,   (2)

where h_4 is the squarefree product of primes having valuation four in h. The element d is sixth-power-free and (d,s)=1. There are at most divisor-many possible s for one h, up to fixed units. The norm support gives Nh << B X Y^5, since Nz>=1.

For each fixed h apply Cauchy only to its finite set of possible s. Thus, with an ambient small-power loss,

 sum_h |I_h^sf|^2
       << (BXY)^epsilon sum_(s squarefree,Ns~Y)
                                  sum_d |I_(s,d)|^2.     (3)

The original masks are retained. In particular chi_A(d z^6) equals chi_A(d) times its genuine z-unit mask. It is NEVER replaced by chi_A(h)chi_A(s)^(-4); that invalid replacement would create false zeros when A and s share a prime.

The primitive s Gauss factor is gamma_1(s) conjugate(chi_s(-d)); xi(d z^6)=xi(d) on the true unit support. These factors have modulus at most one and are independent of the c,n row inside the squared sum over d. They may be removed only at that point in the positive norm. The b-dependent reciprocal-ray phase remains a bounded row coefficient. The auxiliary normalization is exactly M_s^(-1/2).

## 3. Full c,n rows and a legitimate dual large sieve

Write n=n0 r^2, with n0 squarefree. Then

 A=c n0^3 r^6,    a=c n0^3,
 chi_A(d z^6)=chi_a(d) 1_((r,d)=1) 1_((c n0 r,z)=1).

For fixed r,z the first extra factor is a COMMON d-column hole, and the second is a bounded row coefficient. Neither is converted to a new primitive character. The fixed common hole can be discarded only after taking the positive squared norm.

The canonical index a has local exponents 0,1,3,4, even when c and n0 share primes. The pair (c,n0) is recovered uniquely from these exponents. The primitive good conductor of chi_a is rad(a), of norm at most Na. A finite fixed bad/ray partition makes these a bounded-multiplicity family of primitive finite-order Hecke characters. The reviewed general conductor large sieve and duality therefore give, for every finite common coefficient vector alpha and every Q,D>=1,

 sum_(Nd<=D) |sum_(Na<=Q) alpha_a chi_a(d)|^2
             << (D+Q^2)(QD)^epsilon sum_a |alpha_a|^2.   (4)

One may restrict d to its actual sixth-power-free, ray and common-hole support after this positive estimate. This is the full-column conductor inequality, not a replacement of canonical a by rad(a) inside a fixed-order theorem.

On a dyad Na comparable to Q, the row coefficient before its Gaussian and r^(-3) has squared mass bounded by

 sum_(c,n0 squarefree;Nc(Nn0)^3~Q;
       E|c n0 r) 1/[Nc(Nn0)^3]
       <<_epsilon (Q NE)^epsilon / NE0,
                  E0=E/(E,rad r).                       (5)

To see this, fix n0 and require c to be a multiple of E0/(E0,n0). The harmonic c-sum in its actual annulus is O((E0,n0)/NE0), with a harmless small-power loss. The remaining n0 sum is bounded by

 sum_n0 (Nn0)^(-3) N(E0,n0) << 1,

uniformly in E0, by its absolutely convergent Euler product. This proves (5). The core marker only restricts the same positive mass further.

The original Gaussian is V_G(Na (Nr)^6/T). Minkowski in the row dyads and (4)-(5) yield, for fixed r,z and a d-dyad of length D,

 ||sum_(c,n0) alpha_(c,n0,r,z) chi_a(d)||_(ell2(d))
 << ambient^epsilon (NE0)^(-1/2) (Nr)^(-3)
                                 [sqrt(D)+T/(Nr)^6].     (6)

Indeed sum_Q V_G(Q/R) is uniformly bounded for R>=1 and rapidly small for R<1, while sum_Q Q V_G(Q/R)<<R for every R>0. This explicitly retains the full log-Gaussian; no hard completed-index cutoff is substituted.

Now sum r by Minkowski. Since

 (NE0)^(-1/2)=(NE)^(-1/2) N(E,r)^(1/2),
 sum_r (Nr)^(-3) N(E,r)^(1/2) << 1,

and the analogous exponent-nine series also converges uniformly, (6) becomes

 ||the complete c,n row at fixed z||_(ell2(d,Nd<<D))
       << ambient^epsilon (NE)^(-1/2)[sqrt(D)+T].         (7)

Thus all square factors of n, their actual missing-unit holes and all completed scales have been paid before the next summation.

## 4. The sixth-power column and the B-dependent window

For fixed s and z the actual compact radial weight requires

                       Nd comparable to M_s/(Nz)^6.

It is a COMMON d weight, bounded independently of B,s,z and every row. Multiplication by that weight in (7) is harmless. Only Nz<<M_s^(1/6) can occur. Apply Minkowski in z, preserving all its original unit restrictions, and then use

 sum_z (Nz)^(-3)<<1,      #{z:Nz<=V}<<V.

After the original M_s^(-1/2) normalization this gives

 (sum_d |I_(s,d)|^2)^(1/2)
 << ambient^epsilon Y^(-1)(NE)^(-1/2)
                                [1+T M_s^(-1/3)].       (8)

The constants in the primary-generator counts are fixed. There is no free sixth-power multiplicity omitted. Since Ns is comparable to Y and there are O(Y) such s, (3) and (8) prove (1).

This proof applies to each actual b separately. Averaging its squared bound over the positive auxiliary law does not add any factor for the number of b's. It uses their full changing m windows; the B factor has not been frozen or discarded.

## 5. Actual finite compensation and Gaussian restoration

For one slot tuple put D=p_J and E=p_(J^c). The actual summand has coefficient (ND)^(-3/2) and scales (X/ND,Y/ND,T NE). Its squarefree-s class vector is indexed by the same rational element classes m/s^2 as every other summand. The triangle inequality in that common class space, followed by (1), gives

 Y^(-1/2) (ND)^(-1)(NE)^(-1/2)
        [1+T (NE)(ND)^(2/3)/(BXY)^(1/3)]                 (9)

times the small-power factor. This is an upper bound; it does not assert coefficientwise cancellation between marked and rescaled local states.

The nonnegative fixed slot weights and ideal counting imply

 sum_(tuple,J) prod_i W_i (ND)^(-1)(NE)^(-1/2)
                                                  << Z^(ell/2),
 sum_(tuple,J) prod_i W_i (ND)^(-1/3)(NE)^(1/2)
                                                  << Z^(3ell/2).

Consequently the entire finite-compensated squarefree-s within-class norm obeys

 N_modified^sf
 << ambient^epsilon Y^(-1/2)
       [Z^(ell/2)+T(BXY)^(-1/3)Z^(3ell/2)].              (10)

In the original geometry X=Z^(17/48),Y=Z^(23/48),ell=1/6,T<=Z,

 N_modified^sf << ambient^epsilon
                     [Z^(-5/32)+B^(-1/3)Z^(211/288)].  (11)

For the actual polylog pool with R0=Z^128, every b has
Nb >= R0^(64/65-o(1)); the fixed factor b0 is harmless. The second term is smaller than the first by a fixed large power of Z. The original A_T normalizer costs only logarithms, c_Sb^(-1)=O(1), and the Gaussian-restoring operator changes only T. On the two terms in (10), its coefficient norms are bounded by the reviewed products 1+O(P^(-5/6)); shifting T down only improves the linear-T term. Thus (11), with only an additional small-power loss, also holds for the actual normalized restored positive within-class piece.

## 6. Exact scope of the gain and remaining problem

The bound Z^(-5/32+epsilon) controls the square root of the positive within-class contribution for SQUAREFREE physical s. It leaves a fixed 1/32 exponent gap from Z^(-3/16), for this squarefree-s intermediate statement; Part IV treats every physical s. It is not a lower bound: the triangle and large-sieve steps may be lossy.

The cross-class terms in the ensemble second moment remain outside this estimate. The reviewed entrywise R0^(-1/20) estimate does not control their full sum independently of the long physical m support. Nothing in (1)-(11) removes that difficulty or substitutes the already proved full-high Poisson projection as a low input.

The reviewed complete-m cancellation of literal c=s,n=r^2 may be subtracted from the signed observation before this construction. This subtraction does not license deleting selected positive entries from a class energy already formed. The present upper bound does not require that subtraction and does not claim an extra saving from it.

# Part IV. The complete physical s support

## 1. Exact norm to be controlled

Use the entire half-damped original physical column, including chi_A(m), A=c n^3, the genuine b-dependent window B Ns X, the full Gaussian, all unit masks and either actual marker E. For each element class h=[m/s^2] in K^times/K^(times 6), let I_(b,E,h)(X,Y,T) be its complete signed contribution, and put

             N_(b,E)(X,Y,T)=(sum_h |I_(b,E,h)|^2)^(1/2).

The claim is, uniformly in the primitive admissible auxiliary xi of full modulus norm B,

 N_(b,E)(X,Y,T)
 <<_epsilon (BXY(1+T)NE)^epsilon
       Y^(-1/2)(NE)^(-1/2)[1+T(BX)^(-1/3)].             (1)

Here X,Y>=1, T>0 and the original windows have fixed compact ratios. The same harmless adjustment covers a reduced Y in a fixed compact interval below one. This is a statement about the positive within-class norm, not |I_b| or its ensemble mean.

The input is Part III: it proves the corresponding squarefree-s norm with the stronger last factor (BXY)^(-1/3). Its proof in fact permits arbitrary modulus-one c,n row factors, modulus-one factors depending only on s, and additional positive row restrictions and common column unit masks. All such permissions are used below at exactly the squared-norm steps of that proof, never by deleting a summand inside a signed sum.

## 2. Physical high valuations and the two exact reductions

Write uniquely s=s1 t, where s1 is squarefree, every prime valuation of t is at least two, and (s1,t)=1. Every prime p|t is prime to A on the genuine support. Indeed the local Gauss sum requires v_p(m)>=v_p(s)-1>=1; the original chi_A(m) then forces p not dividing A. If p also divides E the marked contribution is zero and can be omitted.

The following are exact complete-m identities, with the original primary unit phases retained.

(a) If v_p(s)=k>=2 with j=k mod 6 in {1,2,3,4,5}, the nonzero Gauss support has v_p(m)=k-1. Substituting s=p^k s0,m=p^(k-1)m0 transforms the entire branch into

 P^(-k) times the same physical column with
   b* replaced by b*p,
   xi replaced by xi chi_p^(-j),
   Y replaced by Y/P^k,
   X,T unchanged,                                      (2)

and all genuine p-unit masks included. The new local character is nonprincipal and primitive. This is the exact CRT identity in Part I A; the full normalized auxiliary Gauss sum, rather than a product with discarded CRT phases, is used. The old Kummer label equals [p^(-k-1)] times the new label [m0/s0^2]. Thus (2) only permutes the class coordinates by one fixed bijection.

(b) If k>=6 and 6 divides k, let J_p denote the same old auxiliary column with p excluded from A and s0, and put

 omega_p(A,s0)=conjugate(xi(p)) chi_s0(p) conjugate(chi_A(p)).

The principal local Ramanujan factor gives

 branch =P^(-k)[J_p(X,Y/P^k,T)
               -P^(-1/2)J_p^(omega_p)(PX,Y/P^k,T)].      (3)

Both m columns on the right are COMPLETE. To check (3), write m=p^(k-1)m0. The normalized local Ramanujan sum is P^(k/2-1)c_p(m0), with c_p(m0)=P 1_(p|m0)-1. In its first term put m0=p l. The original xi and good character phases have sixth powers one, so that term has coefficient one and radial scale X. The second term has precisely the phase omega_p and radial scale PX, together with the displayed P^(-1/2). Its original class is [p^(-1)] times its new class; the first term's class is unchanged. The coefficient omega_p is a product of a scalar, an s0 factor and an A-row factor. It does not depend on m,d or the sixth-power column variable z.

In both identities the coefficient P^(-k) includes the change of the ORIGINAL outer Y^(-1) and the exact radial square-root normalization. We do not re-normalize by a new c_S. Formula (3) also follows by retaining the unit boundary m0 and then combining its missing p multiples with the Ramanujan bulk; it must not be replaced by the boundary term alone.

## 3. One simultaneous reduction and its uniform cost

Fix t before applying (2)-(3) at its primes. The exact result is a sum of class-coordinate permutations of squarefree-s1 columns. Every resulting column has

 Y_t=Y/Nt,
 B_t=B product_(p|t,6 does not divide v_p(t)) Np >=B,
 X_t>=X,
 T_t=T.

The common outside coefficient is (Nt)^(-1). For primes with 6|v_p(t), the two alternatives in (3) have additional absolute coefficient 1 and P^(-1/2). Thus their total absolute coefficient is

 C(t)=product_(p|t,6|v_p(t))(1+P^(-1/2)) <<_epsilon (Nt)^epsilon. (4)

There is no unaccounted constant raised to omega(t). The fixed-modulus character phases and cross-prime CRT phases remain exact bounded row/scalar factors. The squarefree-s bound is uniform over all the resulting primitive xi's; its large sieve family remains chi_a with the original fixed field/bad convention, while each new auxiliary phase is outside the positive d norm or inside its permissible row coefficients.

All original marked primes remain marked. Since (E,t)=1 on every nonzero branch, the marked mass factor (NE)^(-1/2) is unchanged. Old slot supports and coefficients are frozen. If a prime of t was in an already-rescaled slot, it is still just a fixed label in that summand; no new slot pool is selected.

Each class permutation is an isometry on ell2(h). Apply its triangle inequality, then the squarefree-s estimate, to obtain for this fixed t

 N_t << ambient^epsilon Y^(-1/2)(NE)^(-1/2)
       (Nt)^(-1/2) C(t)
          [1+T (Nt)^(1/3)(BXY)^(-1/3)].                (5)

Keeping B_t and X_t could improve the second term. The displayed enlargement uses only B_t>=B and X_t>=X and is valid in every branch. The compact s-window forces Nt<<Y, and then Y_t is bounded below by a positive constant depending only on the fixed W1 support.

## 4. Sum every powerful layer

The standard ideal factorization t=a^2 b^3, b squarefree, gives uniformly for V>=1

 sum_(t powerful,Nt<=V) (Nt)^(-1/2+epsilon) << V^(2epsilon),
 sum_(t powerful,Nt<=V) (Nt)^(-1/6+epsilon) << V^(1/3+2epsilon). (6)

For example the first is bounded by sum_b (Nb)^(-3/2+3epsilon) times a harmonic a-sum. The second follows from the same factorization or the O(V^(1/2)) powerful-ideal count. All finite unit multiplicities are fixed constants. Use a smaller preliminary epsilon to absorb (4) into (6).

Summing (5) over every genuine t by Minkowski now proves (1). The main term does not incur any positive power of Y from non-squarefree s; the second term pays at most Y^(1/3), converting (BXY)^(-1/3) into (BX)^(-1/3). This is the full original s support, including the k=5 invisible Kummer layer and all principal Ramanujan boundary/bulk branches.

## 5. Actual compensation, all b and restoration

For a compensation subset D=p_J,E=p_(J^c), apply (1) at scales (X/ND,Y/ND,T NE), with its actual outside factor (ND)^(-3/2). The class norm is bounded by

 Y^(-1/2)(ND)^(-1)(NE)^(-1/2)
       [1+T(NE)(ND)^(1/3)(BX)^(-1/3)].                (7)

Summing the original nonnegative slot weights over all tuples and subsets, without discarding any mark, gives

 N_modified
 << ambient^epsilon Y^(-1/2)
       [Z^(ell/2)+T(BX)^(-1/3)Z^(3ell/2)].             (8)

The main slot product is sum_p W_i(P)(P^-1+P^-1/2); the second is sum_p W_i(P)(P^-2/3+P^1/2). These are at most constant times P_i^(1/2) and P_i^(3/2), respectively. No auxiliary prime is included in a new physical slot.

In the actual geometry and for every 0<T<=Z, (8) reads

 N_modified << ambient^epsilon
                 [Z^(-5/32)+B^(-1/3)Z^(257/288)].     (9)

For the reviewed ensemble R0=Z^128 and k=floor(logR0/(65loglogR0)), every Nb is at least R0^(64/65-o(1)). Hence the second term is much smaller than Z^(-5/32). The harmless original c_Sb^(-1) and A_T(Z)^(-1) costs are exactly those already reviewed, O(1) and a fixed logarithmic power.

The restoring operator acts only on T and leaves the actual class [m/s^2] unchanged. On the norm in (8), its constant term and positive T term are bounded by its unweighted sup_(0<T<=Z) norm, with products 1+O(P^-5/6). It is the OLD restoring operator at the original b, not a newly enlarged operator at the temporary auxiliary conductor B_t. Thus the full normalized restored within-class energy has square root at most

                           Z^(-5/32+epsilon).           (10)

This conclusion holds for each actual b and then for their positive average. Every cut in physical variables may first be finite; the bounds above, Gaussian tails and absolute convergence of the original column justify the indicated limits. The newly introduced t reductions are identities for complete m columns. Since their Kummer coordinate maps are explicit bijections, they also define identities of the class vectors before taking the displayed norms.

## 6. Remaining low burden

Equation (10) controls the ENTIRE sixth-power-ratio resonant positive block of the physical second moment, including all n and s layers and all true marks. The corresponding cross-class signed kernel remains to be estimated. Even the stated positive bound is weaker than Z^(-3/16) by 1/32; it is only an upper bound and does not rule out a sharper estimate.

The separate reviewed powerful-s complete-m resonance cancellation may be performed on the signed observation before this decomposition. It does not justify deleting entries from positive class energies that have already been formed. Neither (10) nor that cancellation is a whole-probe low estimate, and no already established Poisson high projection has been used as a low input.
