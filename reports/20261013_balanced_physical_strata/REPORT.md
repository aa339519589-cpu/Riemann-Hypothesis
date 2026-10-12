# Two absolute estimates on a balanced physical two-column branch

This report gives two unconditional estimates on the SAME restricted branch of the exponentially large-prime observation. The independent prime laws have norm P_aux=exp(Z), the auxiliary orientation is positive, the damping is the original half-damping, and the complete old Gaussian-T restorer is retained. The two columns have the same compensation tuple E, the same squarefree row label a, n=n'=1, and c=E a varpi b, c'=E a varpi b', with a fixed good varpi and coprime b,b' of norms comparable to sqrt(Z/Nvarpi). Every original source variable is integrated over the whole real line.

* Part I pays small power-free parts of the actual element w=q'(b')^2 m-q b^2 m', even when Nw itself is as large as exp(2Z) times a polynomial. For w=u_k v^k, fixed k>=3, the absolute bound is P_aux^(2/k-1) U^(1-1/k) Z^C on Nu_k<=U. For k=6 and U=P_aux^(4/5-eta), this is exp(-5eta Z/6) Z^C. Literal physical cubes have exp(-Z/3) Z^C. These are physical element restrictions, not cube frequencies in another Poisson model.
* Part II pays the actual same-Kummer-class part of this branch AFTER ANY bounded physical pair mask. The raw estimate is Z^(-49/48+epsilon); the original outside squared normalization gives Z^(-31/48+epsilon). If an additional common-row Gram weight Na is present, the respective exponents are -25/48 and -7/48. That weighted bound is weaker and is not represented as meeting the whole-cross target.

The proofs use direct absolute counting with the exact radial normalizations. They do not assume that a masked class kernel is positive semidefinite. The remaining large power-free part and the full physical square scalar sum are unestimated. Different compensation/row branches and the complete original Mobius cross-class signal are also unestimated. These results do not improve the original spectral gap or exclude a zeta zero.

## Exact original object and self-contained inputs

The [original physical summand and exponential auxiliary law](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md), opening definition and Part B, fix the conventions. Work in K=Q(omega) with its original primary generators, zero-extended residue characters and finite reciprocity sectors. For primitive xi modulo b*=b0 q, put B=N(b*), tau=B^(-1/2)g_xi(b*,1), Xi(c)=xi(c)chi_c(b*), and

    V_G(v)=(2sqrt(pi))^(-1) exp[-(log v)^2/4].

In the n=1, all-Ec compensation term used here, X=Z^(17/48), Y_s=Z^(23/48), the Gaussian T scale is T NE, and the coefficient has weight W_E/(c_S A_T), where c_S is the actual c_(S0+q), not c_S0. The ambient slot normalizer A_T is frozen when the Gaussian T scale changes. At activation alpha, set M=B Ns X exp(-alpha). Apart from this displayed compensation scalar, the exact raw summand is

    [W1(Ns/Y_s)/Y_s] [chi_s(b*)/(tau xi(s))] xi(m)
    [g_(chi_s)(s,-m)/(Ns)^(1/2)]
    gamma_2(c) conjugate(alpha_0(c)) conjugate(G(c))
    Xi(c)^(-1) R(c,s) chi_c(m) (Nc)^(-1/2)
    M^(-1/2) W0(Nm/M) V_G(Nc/(T NE exp(-alpha))).

Here alpha_0 denotes the original fixed unitary character, to distinguish it from the real activation variable alpha. The choice is eta=1, xi=xi0 chi_q. All original zero extensions, sector masks, bad data and ordinary/core nonflat marker restrictions are kept. The normalized primitive root tau has modulus one; the elementary finite s Gauss bound is |g_(chi_s)(s,-m)|<=Ns. W0,W1 have their original fixed compact norm supports. All s valuations are allowed. The class is the original ELEMENT class h=[m/c^2] in K*/K*6, with its finite unit choices, as in the [positive-orientation derivation](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261011_qrh_selection_bridge/OPPOSITE_AUXILIARY_KUMMER.md).

The [original source realization](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md) gives m_theta(x)^2=Phi(x)/(2cosh(x/2)), e0(x)=2m_theta(x)cosh(x/2), dnu=e0^2 dx. For a fixed source q_0 in L2(nu), v=e0 q_0 and f_q=Phi q_0=m_theta v. The subscript in f_q is this fixed source label; q,q' elsewhere denote the auxiliary primes. The theta decay implies

    integral |f_q(x)| exp(2|x|) dx
       <= ||v||_2 ||m_theta exp(2|x|)||_2 < infinity.

No negative-state assumption or source cutoff is needed. In particular its unweighted L1 norm is finite.

For a prime of norm Q, the exact old restorer of [Part B, Section 2](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md) is

    D_q I(T)=Q^(-5/6) I(T/Q),
    (1-Q^(-2))[I-(1-Q^(-1))D_q-kappa(q)Q D_q^6]
                sum_(j>=0) kappa(q)^j Q^(-3j) I(T/Q^(6j)),

where |kappa(q)|=1. On the supremum norm in the Gaussian scale its coefficient sum is bounded uniformly: the two extra numerator weights are O(Q^(-5/6)) and O(Q^(-4)), and the denominator sum is geometric. It changes no radial disk, source parameter, slot, class or physical mask used below. The true c_S inverse is bounded uniformly in the auxiliary prime, while A_T inverse costs only a fixed logarithmic factor.

The marked tuple weight has the original diagonal price

    sum_E |W_E|^2/NE <<_epsilon Z^epsilon.

For each of the fixed number of slots this is the elementary bounded annular sum sum_p |W_i(p)|^2/Np; finite slot assignments and permutations only cost constants. This is also the diagonal term of [Part A, Section 5, equation (13)](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md). Part II uses the SAME tuple in both columns; no independent E,E' summation is granted by this estimate.

For completeness, the mixed phase in Part I is an exact CRT identity. Let psi=chi_q conjugate(chi_q'), ell=C0 b b', and let tau_q,tau_q' be the normalized good-prime roots. On the common-unit support,

    tau_psi=chi_q(q') conjugate(chi_q'(q)) tau_q tau_(bar chi_q'),
    tau_(bar chi_q')=chi_q'(-1) conjugate(tau_q'),
    w=q'(b')^2 m mod q,     w=-q b^2 m' mod q'.

Substituting these identities gives

    tau_q^(-1) conjugate(tau_q'^(-1))
       chi_q(m/c^2) conjugate(chi_q'(m'/(c')^2))
            =tau_psi^(-1) psi(w/ell^2).

The original b0, xi0 and sector reciprocity factors then give exactly Part I equation (3). Fractions here are character evaluations on units, not integral-divisibility assertions. Both roots and all original phases remain present. The estimates below would also follow directly from their unit modulus; they do not rely on an unproved smooth pushforward distribution of w.

[Mathematical reviews](REFEREE.md) verify both complete proofs and independently check the full-source and fixed-k increments. Equation numbering restarts in each part.

## Part I. Small power-free physical elements

### 1. Exact branch and order of the restrictions

Put P_aux=exp(Z), and take the same two independent positive auxiliary prime laws Nq,Nq' in [P_aux,2P_aux]. Work in the original half-damped positive-orientation observation, with its original normalizers and old T-only restorer. Use all-Ec terms and n=n'=1. Retain the actual compensation labels and genuine zero masks.

Fix a good prime ideal varpi of fixed norm P, a shared squarefree a, and two coprime b,b' in the following explicitly specified balanced branch:

 c=C0 b, c'=C0 b', C0=E a varpi,
 Na,Nb,Nb'~sqrt(Z/P), NE~Z^(1/6), (b,b')=1.

The implied windows have fixed ratios, and all original coprimality conditions are retained. The primes q,q' are distinct and the two columns have the original common-unit support (cc',qq')=1, in addition to their own zero masks. Define the original ELEMENT, not its norm difference,

              w=q'(b')^2 m-q b^2 m'.                         (1)

All original finite sectors, the h!=h' condition and any additional restrictions may be retained when they only decrease the absolute sum below. Original row or tag multiplicities bounded by a fixed power of Z may be included. There are at most a fixed polynomial number of the selected physical labels; the s and s' windows satisfy Ns,Ns'~Y_s=Z^(23/48).

Keep the full original activation variables alpha,alpha' in R and integrate against the original fixed source f_q(alpha),f_q(alpha'). We use its established finite moment

                  integral |f_q(alpha)|exp(2|alpha|)d alpha<infinity.   (2)

No source tail is discarded by appeal to a complete-column theorem. The new sparse count below bounds this particular w stratum directly at all activation parameters, before integrating. A central source restriction, or any other additional restriction, may of course be retained in its absolute majorant.

### 2. The physical counting and normalization

The exact mixed-Gauss kernel is still

 xi0(q'/q) R(gamma,q) conjugate(R(gamma',q'))
       tau_(chi_q conjugate(chi_q'))^(-1)
       (chi_q conjugate(chi_q'))(w/(b0(C0 b b')^2)).         (3)

It is obtained from both original roots by CRT, not by changing their phases. Its modulus on genuine units is one. In particular (w,qq')=1 and w=0 is absent.

The original m disks have norm radii bounded by

 Nm<=C P_aux X exp(-alpha) Ns,
 Nm'<=C P_aux X exp(-alpha') Ns',
                     X=Z^(17/48).

Put A_alpha=|alpha|+|alpha'|. Since Nb,Nb'~sqrt(Z/P), the squared triangle inequality in (1) gives

 Nw<=C P_aux^2 Z^(11/6)(exp(-alpha)+exp(-alpha'))
                   <=P_aux^2 Z^C exp(A_alpha)=:W.           (4)

For each fixed q,q' and w the integral solutions are a translate of

        m=m0+q b^2 t_f, m'=m0'+q'(b')^2 t_f.

The ideals q b^2 and q'(b')^2 are coprime. The exact lattice spacing and the original disk scales give at most

 C[1+min(X exp(-alpha) Ns/(Nb)^2,
         X exp(-alpha') Ns'/(Nb')^2)]
 <= C_P exp(A_alpha/2).                                  (5)

solutions; here min(exp(-alpha),exp(-alpha'))<=exp(A_alpha/2), and exp(A_alpha/2)>=1. In a fixed bounded source window it is O(1), but this is not assumed for the full-source estimate. All further zero masks or Kummer restrictions only reduce the count.

The actual physical radial normalization of each column is M^(-1/2), where M=N(b0q) X exp(-alpha) Ns; similarly for the other column. Thus each pair of raw summands, including all other factors at the stated polynomial labels, is bounded by

                    P_aux^(-1) Z^C exp(A_alpha/2).          (6)

Indeed the original auxiliary tau is already a normalized unit Gauss root, and supplies no further positive or negative P_aux power. Characters have modulus at most one; the finite physical s Gauss sum is bounded by Ns; and all remaining powers, fixed bad factors, normalizers and slot data cost only Z^C on these labels. The two M^(-1/2) factors are the only unbounded activation factors after taking the supremum of the Gaussian, and their product contributes exp((alpha+alpha')/2)<=exp(A_alpha/2). The original log-Gaussian is bounded uniformly. The old T-only operator has an absolutely bounded coefficient sum on this finite branch: its denominator gives sum_j (Nq)^(-3j), and its two numerator shifts have coefficient sizes O((Nq)^(-5/6)) and O((Nq)^(-4)). It changes neither m disk nor (5). Hence (6) also pays the restored columns, uniformly over all alpha,alpha'.

### 3. Sixth-power-free count and the resulting saving

Write every nonzero Eisenstein element uniquely up to a bounded unit convention as

                       w=u_w v^6,

where u_w is sixth-power-free; retain its unit rather than replacing it by a norm representative. All bad-prime valuations may be included. For U>=1, the elementary two-dimensional ideal/element count yields

 #{w:0<Nw<=W, Nu_w<=U}
 <= C sum_(Nu_w<=min(U,W)) (W/Nu_w)^(1/6)
 <= C W^(1/6) U^(5/6).                                    (7)

No distribution theorem, smoothness of the w pushforward, or cancellation in a Gauss root is used here. The same bound remains valid with the actual q-dependent attainable-w set and any further masks.

At fixed alpha,alpha', combining (4)-(7) gives

 P_aux^(-2/3) U^(5/6) Z^C exp((1/2+1/6+1/2)A_alpha)
       =P_aux^(-2/3) U^(5/6) Z^C exp(7 A_alpha/6).

The three activation exponents come respectively from the fiber count, the sixth-root of the w radius, and the two actual radial normalizations. They total less than2. Integrating against |f_q(alpha)f_q(alpha')| is therefore paid by (2), without any auxiliary cost. Summing the polynomial labels and using sum_q omega_q=sum_q' omega_q'=1 gives the bound for the ORIGINAL signed contribution of this restricted physical branch with its FULL source activation:

 |C_(Nu_w<=U)|
             <= P_aux^(-2/3) U^(5/6) Z^C.                  (8)

The exponent C is fixed after the branch, fixed profiles/source and polynomial row weights are fixed; it is independent of q,q',U and Z. The estimate is an absolute bound, so it preserves the original phases without needing a claim about their signs. It applies equally to the far-w part by imposing the extra lower bound on Nw.

In particular, for any fixed 0<eta<4/5, choosing

                   U=P_aux^(4/5-eta)

gives

                    |C_(Nu_w<=U)|
                     <= exp(-5eta Z/6) Z^C.                (9)

For U any fixed polynomial in Z, the bound is exp(-2Z/3) times a polynomial. The original power normalization of the target is also absorbed by Z^C. This pays a real physical stratum, even when Nw itself is large; it is not a small-Nw estimate relabelled.

The same proof has the following direct extension. For any fixed integer k>=3, write the actual physical element w=u_k v^k with u_k k-th-power-free, including its unit. Replace (7) by C W^(1/k) U^(1-1/k). The resulting FULL-source estimate is

 |C_(Nu_k<=U)|<=P_aux^(2/k-1) U^(1-1/k) Z^C.                (10)

Its activation factor is exp((1+1/k)A_alpha), still paid by (2). In particular the literal physical cube subset w=v^3 has bound exp(-Z/3) Z^C, even though its sixth-power-free part need not be small. This is a restriction on the physical element w, not a statement about the cube frequencies or the model in a different Poisson formula. For k=2 the auxiliary exponent in (10) would be zero, which is precisely the counting threshold; no positive auxiliary saving for the square stratum is obtained.

The remaining large-u_w contribution is not bounded by this argument. In particular a square w=v^2 typically has sixth-power-free part of large norm: square-power counting alone gives O(W^(1/2))~P_aux Z^C choices and loses the auxiliary exponential saving against (6). No conclusion about the full square stratum, or a fixed-power bound for the whole coherent middle, is asserted.

## Part II. Same-class subtraction with arbitrary physical masks

### 1. Exact observation and scope

Use the original positive auxiliary orientation, the two independent positive prime laws Nq,Nq'~P_aux=exp(Z), the half-damped observation, its finite compensation, and its old T-only restorer. Set X=Z^(17/48), Y_s=Z^(23/48), T=Z. Restrict to n=n'=1 and all-Ec terms. In the two copies use the same compensation product E, the same squarefree row label a, and a fixed good prime ideal varpi of fixed norm P. Put

  C0=E a varpi, c=C0 b, c'=C0 b',
  Na,Nb,Nb'~B0=sqrt(Z/P), NE~Z^(1/6),
  (b,b')=(bb',C0)=1.

All c,c' are squarefree and all genuine physical zero masks are retained. If these conditions or a fixed hole exclude varpi, the block is empty. The dyads have fixed ratios and P is fixed. The physical label h is the actual element class [m/c^2] in K*/K*6, including the original finite unit/ray choices.

Let C_=,B be the contribution with h=h', with all physical phases and both Gauss roots retained, and with any additional mask B of modulus at most one. Such a mask may depend on q,q',m,m', the exact mixed element w, sectors, and the other original labels. In particular it may impose a square-w stratum or its complement. The argument bounds the sum of absolute physical summands, so it does not require positivity or separability of B. We may retain q!=q' and all common-unit restrictions, or omit them in the positive majorant.

Keep the complete original source activation alpha,alpha' and integrate against f_q(alpha), conjugate(f_q(alpha')). No source cutoff is imposed. Constants can depend on this fixed source, P, the fixed profiles, and original bad data.

The claim, before the target's outside squared normalization Z^(3/8), is

                 |C_=,B| <<_epsilon Z^(-49/48+epsilon).       (1)

After that normalization it is O(Z^(-31/48+epsilon)). If the common a-row Gram additionally weights the pair by Na, the corresponding raw bound is O(Z^(-25/48+epsilon)), and the normalized bound is O(Z^(-7/48+epsilon)). No other unpriced polynomial multiplicity is included in these exponents.

### 2. Actual same-class support and uniform pair count

The original chi_c(m), chi_c'(m') zero extensions imply (m,c)=(m',c')=1. The equality of the actual h classes gives

                     m(b')^2/(m' b^2) in K*6.

At a prime dividing b, the valuation of m is zero, so the valuation of m' is congruent to4 modulo6; the reverse holds at primes dividing b'. Consequently, with a bounded choice of units, the full pair has the form

               m=(b')^4 H u^6,  m'=b^4 H v^6,               (2)

where H is a common sixth-power-free element. Other original masks impose additional holes, which may be ignored only in the counting upper bound. Formula (2) is a relation between the original element classes, not an assertion that different ideal directions have the same phase.

For fixed q,q',s,s',alpha,alpha', let

  M=N(b0 q) X exp(-alpha) Ns,
  M'=N(b0 q') X exp(-alpha') Ns',
  L1=M/(Nb')^4, L2=M'/(Nb)^4.

The radial profiles have a fixed compact annular support. Counting (2) inside their enclosing norm disks gives

  # pairs << L1^(1/6) L2^(1/6)
                 sum_(NH<=C min(L1,L2)) (NH)^(-1/3)
          << (L1 L2)^(1/6) min(L1,L2)^(2/3)
          <= C sqrt(L1 L2)
          = C sqrt(M M')/(Nb Nb')^2.                       (3)

The ideal/element count O(V) for norm<=V and partial summation prove the middle bound; fixed support constants are absorbed. If either enlarged L_i is below the minimum nonzero norm there are no pairs. Thus (3) is uniform at every positive M,M', including small shifted scales. Squarefreeness of H can be omitted in this upper bound. Finite unit conventions contribute only a fixed factor.

### 3. Exact radial cancellation and the remaining physical sums

The actual raw summand, with n=1, has absolute size at most

  C |W_E|/(|cS A_T|) * |W1(Ns/Y_s)|/Y_s
             * (Ns)^(1/2) (Nc)^(-1/2) M^(-1/2)
             * |W0(Nm/M)| |V_G(Nc/(T NE exp(-alpha)))|.     (4)

This follows from |g_(chi_s)(s,-m)|<=Ns and the source's division by sqrt(Ns). All normalized auxiliary roots, gamma_2(c), characters and reciprocity factors have modulus at most a fixed constant. In particular no extra power P_aux^(-1/2) is assigned to a normalized root. The fixed scalar normalizers and A_T^(-1) have at most logarithmic cost, which is included in Z^epsilon below.

Bound V_G uniformly, then multiply the two copies of (4) and use (3). The two M^(-1/2) factors cancel the sqrt(M M') exactly. For fixed E,a,b,b', the two s windows contribute

  Y_s^(-2) (sum_(Ns~Y_s) sqrt(Ns))^2 << Y_s.

This counts all s, including powerful factors, rather than making a squarefree-s simplification. Finite sector restrictions only remove summands. Since sqrt(Nc Nc')=NC0 sqrt(Nb Nb'), the resulting absolute bound is

                 C |W_E|^2 Y_s /
                    [NC0 (Nb Nb')^(5/2)],                (5)

apart from the stated logarithmic normalizers. It is independent of alpha,alpha'. Hence the complete source integrals cost only (integral |f_q|)^2. The independent positive auxiliary laws have total mass one, and incur no further cost.

The old restoring operator changes only Gaussian T scales on this branch. Its coefficient l1 norm is uniformly bounded: the denominator series has weights (Nq)^(-3j), and the two numerator shifts have weights O((Nq)^(-5/6)) and O((Nq)^(-4)). Taking the Gaussian supremum therefore preserves (5) in both copies. This uses the actual coefficient series, not an inverse operator norm on an unspecified function space.

### 4. Sum the common labels at their actual prices

For a fixed-ratio ideal dyad of scale B0,

  sum_(Nb~B0) (Nb)^(-5/2) << B0^(-3/2),
  sum_(Na~B0) (Na)^(-1) <<1.

The two b sums in (5) therefore cost B0^(-3)<<_P Z^(-3/2). The remaining common-E price is

                    sum_E |W_E|^2/NE <<_epsilon Z^epsilon. (6)

This is the original marked-slot diagonal price: for each fixed slot, sum_p |W_i(p)|^2/Np is bounded by a fixed power of log Z (the stronger bounded version is also available in the public positive-pair proof). The fixed number of slot assignments factors at this upper-bound stage; any repeated representation of the same squarefree E has only a bounded permutation multiplicity. All original cross-slot holes may be dropped in this positive sum. No unrestricted E-count is used.

Combining (5)-(6) gives

            Y_s Z^(-3/2+epsilon)=Z^(-49/48+epsilon),

which proves (1). Multiplication by Z^(3/8) gives -31/48. If the actual a-row Gram has the extra weight Na, then Na<<_P Z^(1/2), giving respectively -25/48 and -7/48 as claimed.

This estimate permits subtraction of the restricted same-class term from a scalar two-column expression on this branch, including after a square-w or far-w restriction. It does not estimate that scalar expression, make its weight positive semidefinite, or control different E/a branches.
