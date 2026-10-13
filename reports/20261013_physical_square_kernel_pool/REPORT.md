# A growing squarefree-kernel pool in the complete physical two-column sum

The new estimate pays every Poisson frequency of a square-class stratum in the original balanced physical branch. A direct Eisenstein mixed-character theorem gives cancellation with both original cubic factors and an arbitrary harmonic quadratic phase. The physical proof retains the full fixed source, the actual radial normalizations and the old Gaussian-T restorer.

For P_aux=exp(Z), the complete scalar contribution from one squarefree kernel u is O_epsilon(P_aux^(-1/64+epsilon) Z^C), uniformly for Nu<=P_aux^theta0 with any fixed theta0<1. The disjoint pool Nu<=U costs at most U times this bound. In particular U=P_aux^(1/128) gives O_epsilon(exp((-1/128+epsilon)Z) Z^C). These are unconditional estimates: the character input is proved in Part I using only the classical complete finite-field Weil bound, and the independent auxiliary prime probabilities are used only through their total mass one.

The physical branch is precise: positive auxiliary orientation, half-damping, n=n'=1, the same compensation tuple E and squarefree row label a, c=E a varpi b and c'=E a varpi b', coprime b,b' of the specified balanced sizes, and distinct auxiliary primes. The scalar estimate is taken before the original Kummer-class inequality h!=h'. To recover that cross-class part, subtract the exact same-class term once for the whole kernel pool. Its already proved raw price is Z^(-49/48+epsilon), or Z^(-25/48+epsilon) with the additional actual Na row weight; the corresponding outside-normalized prices are Z^(-31/48+epsilon) and Z^(-7/48+epsilon). No factor U is added to this single masked same-class estimate.

The large squarefree-kernel complement, other compensation/row or n branches, and the complete original Mobius cross sum remain unestimated. The scalar cancellation estimate does not permit arbitrary additional v-dependent masks. This result gives no new spectral gap or zeta-zero exclusion.

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

The [original source realization](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md) gives m_theta(x)^2=Phi(x)/(2cosh(x/2)), e0(x)=2m_theta(x)cosh(x/2), dnu=e0^2 dx. For a fixed source q_0 in L2(nu), v=e0 q_0 and f_q=Phi q_0=m_theta v. The subscript in f_q is this fixed source label; q,q' elsewhere denote the auxiliary primes. For every fixed L>=0, the theta decay implies

    integral |f_q(x)| exp(L|x|) dx
       <= ||v||_2 ||m_theta exp(L|x|)||_2 < infinity.

No negative-state assumption or source cutoff is needed. In particular its unweighted L1 norm is finite.

For a prime of norm Q, the exact old restorer of [Part B, Section 2](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md) is

    D_q I(T)=Q^(-5/6) I(T/Q),
    (1-Q^(-2))[I-(1-Q^(-1))D_q-kappa(q)Q D_q^6]
                sum_(j>=0) kappa(q)^j Q^(-3j) I(T/Q^(6j)),

where |kappa(q)|=1. On the supremum norm in the Gaussian scale its coefficient sum is bounded uniformly: the two extra numerator weights are O(Q^(-5/6)) and O(Q^(-4)), and the denominator sum is geometric. It changes no radial disk, source parameter, slot, class or physical mask used below. The true c_S inverse is bounded uniformly in the auxiliary prime, while A_T inverse costs only a fixed logarithmic factor.

The marked tuple weight has the original diagonal price

    sum_E |W_E|^2/NE <<_epsilon Z^epsilon.

For each of the fixed number of slots this is the elementary bounded annular sum sum_p |W_i(p)|^2/Np; finite slot assignments and permutations only cost constants. This is also the diagonal term of [Part A, Section 5, equation (13)](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md). Both physical parts below use the SAME tuple in both columns; no independent E,E' summation is granted by this estimate.

For completeness, the mixed phase used in Part II is an exact CRT identity. Let psi=chi_q conjugate(chi_q'), ell_0=C0 b b', and let tau_q,tau_q' be the normalized good-prime roots. On the common-unit support,

    tau_psi=chi_q(q') conjugate(chi_q'(q)) tau_q tau_(bar chi_q'),
    tau_(bar chi_q')=chi_q'(-1) conjugate(tau_q'),
    w=q'(b')^2 m mod q,     w=-q b^2 m' mod q'.

Substituting these identities gives

    tau_q^(-1) conjugate(tau_q'^(-1))
       chi_q(m/c^2) conjugate(chi_q'(m'/(c')^2))
            =tau_psi^(-1) psi(w/ell_0^2).

The original b0, xi0 and sector reciprocity factors supply the remaining original bounded coefficients and small-period factors. On w=u2 v^2, put theta=psi^2. The exact square-class identity is

    psi(w/(b0 ell_0^2))=psi(u2/b0) theta(v/ell_0).

Its two local v factors are opposite nonprincipal primitive cubic characters. The original normalized root tau_psi^(-1), of modulus one, remains outside the v sum unchanged, together with psi(u2/b0) and theta(ell_0)^(-1). No change to a canonically rephased cubic Gauss root is required. This is the exact input to Part II. Fractions here are character evaluations on units, not integral-divisibility assertions. Both roots and all original phases remain present. Part II retains these characters and applies Part I only after the full small-period and Poisson decomposition. No smooth pushforward distribution of w is assumed.

The branch definitions and the masked same-class estimates are the proved ones in the [balanced physical-strata report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a4d31fa2778d55eb21ebfeb09f01578ee47e2157/reports/20261013_balanced_physical_strata/REPORT.md), especially its exact-object section and Part II. The latter proof is an absolute masked count and therefore applies to the union of square classes as one bounded mask. Its label restrictions and four raw/normalized exponents are retained here.

Part I contains the complete five-section character proof. Part II proves the complete fixed-class physical application, including all frequencies and both full source integrals. Part III supplies the uniform growing-kernel extension and its disjoint counting cost. Equation numbering restarts in each part. [Independent mathematical reviews](REFEREE.md) cover each complete argument and the original-source matching.

## Part I. A direct mixed-character bound

### 1. Statement

Let O=Z[omega]. Let mathfrak q,mathfrak q' be distinct good prime ideals with comparable norms, and put mathfrak Q=mathfrak q mathfrak q', Q=Nmathfrak Q. Thus each prime norm is comparable to Q^(1/2). Let chi be a character modulo mathfrak Q whose two local factors are nonprincipal cubic characters, possibly of opposite orientation, extended by zero on nonunits.

Let J=(j) be an ideal prime to mathfrak Q. For E>=1 assume NJ<=E. Let mathcal R be any coordinate rectangle in O, contained in the disk Nv<=C Q^(1/2) E, where C is fixed. Retain an arbitrary fixed coset v0 modulo J. Let

                    f(v)=Tr(eta v^2+lambda v)+c

be any real-valued harmonic quadratic polynomial, with completely arbitrary real coefficients in the fixed basis 1,omega. There is no restriction on the sizes or denominators of those coefficients. Then the bound is

 |sum_(v in mathcal R, v=v0 mod J) chi(v)e(f(v))|
                  <<_epsilon Q^(63/128+epsilon) E^2.       (1)

The constant is uniform in the two primes, J, the coset, the rectangle and f, subject to the displayed conditions. The only ambient fixed data are K and the fixed enclosing-disk constant. At E polynomial in log Q this saves Q^(1/128-epsilon) against the norm-area length Q^(1/2).

For a compactly supported smooth weight in the same enclosing coordinate box, the same bound holds multiplied by its two-dimensional Abel variation, for example the integral of |partial_x partial_y W| after extending W by zero with smooth compact boundaries. This last statement is ordinary two-dimensional partial summation using (1) for all partial rectangles. An arbitrary bounded nonseparable weight is not covered.

### 2. Translation average and its boundary

Write M=Q^(1/2)E. It is enough first to treat E<=Q^(1/8); if E is larger, the elementary count O(M) already obeys(1), since Q^(1/2)E<=Q^(63/128)E^2 in that range. For the first range set

                 A=Q^(5/16), B=Q^(1/16), r=8.

Take mathcal A and mathcal B to be fixed rectangular sets of nonzero Eisenstein elements, with coordinate side lengths comparable to sqrt(A),sqrt(B), and with norms at most fixed constants times A,B. Their cardinalities are comparable to A,B. For sufficiently large Q, every a in mathcal A is a unit modulo both primes, since Na<<Q^(5/16)<Nmathfrak q,Nmathfrak q'. The finitely bounded Q range is absorbed in the constant.

For each a,b replace v by v+jab. This preserves the selected J coset. Comparing a rectangle with its translate, and bounding lattice points by the full O lattice rather than requiring a density in the coset, gives boundary error

 O(sqrt(M NJ A B)+NJ A B+sqrt(M)+sqrt(NJ A B)+1)
          << Q^(7/16)E+Q^(3/8)E+Q^(1/4)sqrt(E)+1.         (2)

This is smaller than the right side of(1). The estimate follows from the fixed-lattice point count in boundary strips: the rectangle's side lengths are O(sqrt(M)), and the shift length is O(sqrt(NJ A B)). It remains valid for shorter or degenerate subrectangles.

Consequently the original sum is bounded, up to(2), by

  C/(A B) sum_(v in mathcal R, v=v0 mod J)
                sum_(a in mathcal A)
       |sum_(b in mathcal B) chi(v+jab)e(f(v+jab))|.        (3)

This is the average of the translated complete sums, followed by the triangle inequality. The v box in(3) is the original box; boundary comparison was performed before taking that absolute value.

Put x=v/(ja) modulo mathfrak Q. Multiplicativity gives chi(v+jab)=chi(ja)chi(x+b), including all zero values. The polynomial f(v+jab), as a function of b, is another arbitrary real harmonic quadratic polynomial. Its coefficients can depend on v,a, but its degree and four nonconstant real coefficient coordinates do not change.

Define

  nu(x)=# {(v,a) in the ranges in(3): v/(ja)=x mod mathfrak Q},
  T(x)=sup_F |sum_(b in mathcal B) chi(x+b)e(F(b))|,

where the supremum is over all such harmonic quadratics F. Thus(3) is at most C(AB)^(-1) sum_x nu(x)T(x).

### 3. The actual ratio energy is an integral equality count

One has sum_x nu(x)<<MA. For two represented pairs with the same x,

                    v1 a2-v2 a1 in mathfrak Q.

The norm of the left side is at most C M A. In the present range E<=Q^(1/8), this is O(Q^(15/16)), strictly less than Q for sufficiently large Q. A nonzero element of mathfrak Q has norm at least Q. Hence the congruence forces the literal equality

                         v1 a2=v2 a1.                     (4)

The fixed J cancels from this congruence because it is prime to mathfrak Q. No geometry of a large modular inverse is used.

For a nonzero product w, the number of factorizations w=v a into elements in O is at most a fixed unit factor times the ideal divisor function of(w). The standard elementary bound d((w))<<_epsilon (Nw)^epsilon and the norm-disk count O(V) therefore bound the quadruples in(4) by O_epsilon((MA)^(1+epsilon)). The possible v1=v2=0 pairs cost at most O(A^2), which is smaller than MA because M>=Q^(1/2)>A. Thus

                 sum_x nu(x)^2 <<_epsilon MA Q^epsilon,   (5)

after renaming epsilon; here E<=Q^(1/8). Restricting the v coset only decreases this upper bound. In particular (5) is not the energy estimate for arbitrary coefficients on a long residue sequence.

### 4. A finite coefficient grid controls the polynomial-phase supremum

Write b=k+l omega. Its coordinates are O(sqrt(B)), and

                 b^2=(k^2-l^2)+(2kl-l^2)omega.

Apart from an irrelevant constant, every F(b) is therefore

     theta1 k+theta2 l+theta3(k^2-l^2)+theta4(2kl-l^2).

The theta coordinates may be taken modulo1. For fixed x, the corresponding sum over b is a trigonometric polynomial on a four-dimensional torus. Its degrees in the first two coordinates are O(sqrt(B)), and those in the last two are O(B). Multivariable Bernstein's inequality, followed one coordinate at a time, implies that its supremum is at most twice the maximum over an oversampled rectangular grid of cardinality O(B^3): choose each mesh at most a sufficiently small fixed multiple of the reciprocal degree and compare a maximum point to its nearest grid point. The derivative bounds are in terms of the supremum itself, so this introduces no additive O(B) approximation error.

It follows that

 sum_(x mod mathfrak Q) T(x)^(2r)
       <<_r B^3 max_theta sum_(x mod mathfrak Q)
                    |sum_b chi(x+b)e(F_theta(b))|^(2r).    (6)

For each fixed theta, expand the power. The phase coefficients in every tuple have absolute value one. Since the characters have order3, the complete character factor is the product of the two finite-field complete sums of chi_local(P(X)), where

        P(X)=product_(i<=r)(X+b_i)
                         product_(r<i<=2r)(X+b_i)^2.

This polynomial expression is exact also at every root, since both chi(0) and conjugate(chi(0)) are zero. No denominator-zero convention or discarded root correction is needed.

Two different b_i have norm difference O(B), below either prime norm for large Q. Thus their roots coincide modulo either prime exactly when they are the same element of O. The polynomial is a cube at either local field precisely when every signed multiplicity of a distinct literal root is divisible by3: its polynomial multiplicity is the positive count plus twice the negative count, congruent to their difference modulo3. In a tuple satisfying that condition, every distinct root occurs at least twice, so there are at most r distinct roots. Such tuples number O_r(B^r).

For these exceptional tuples use the trivial complete bound Q. For every other tuple the finite-field Weil bound for a noncube polynomial and a nonprincipal cubic character gives O_r(sqrt(Nmathfrak q)) and O_r(sqrt(Nmathfrak q')) at the two primes. One precise primary reference is Iwaniec--Kowalski, *Analytic Number Theory*, Chapter11, Theorem11.23 and Corollary11.24, in the authors' chapter file https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf. With r=8 the polynomial has at most16 distinct roots, so15 times the square root of the field size is a sufficient local bound. This theorem applies over the full residue field, including inert prime ideals. Their product is O_r(sqrt(Q)). The exact zero extensions are retained by the polynomial formula. The two local orientations do not change the cube criterion. Therefore

 sum_x T(x)^(2r)
             <<_r B^3[Q B^r+Q^(1/2) B^(2r)].             (7)

Only the classical complete finite-field character estimate is used here. No bound for an incomplete mixed sum has been invoked.

### 5. Holder, the explicit exponent, and the smooth-weight range

Holder followed by Cauchy gives the exact inequality

 sum_x nu(x)T(x)
  <= (sum nu)^(1-1/r) (sum nu^2)^(1/(2r))
                                   (sum T^(2r))^(1/(2r)). (8)

Insert(5),(7), divide by AB as in(3), and take r=8. Since B=Q^(1/16), the two terms in(7) are of the same size. The resulting main bound is

             <<_epsilon M^(15/16) Q^(3/128+epsilon)
              =Q^(63/128+epsilon) E^(15/16).               (9)

For a direct exponent check at E=1, MA=Q^(13/16), the moment in(7) is O(Q^(27/16)), and(8) divided by AB gives

       (13/16)(15/16)+(27/16)/16-3/8=63/128.

The boundary(2) is smaller than Q^(63/128)E^2. This proves(1) for E<=Q^(1/8); the earlier trivial estimate handles the rest. Powers of Q^epsilon can be made arbitrarily small by using the elementary divisor bound with a correspondingly smaller epsilon. Constants are allowed to depend on that choice, but not on the phase coefficients.

For a smooth compact weight, represent its weighted sum by two-dimensional Abel integration of rectangular partial sums. The right side is multiplied by a genuine fixed-order variation seminorm of the weight. If the original parameter-dependent weight has seminorm Z^C exp(CA_source), and E has the same kind of bound, this still has only a fixed exponential moment cost for the original source. The amplitude derivatives and summable full Poisson-frequency envelope required for the physical application are proved in Part II below.

The physical application in Part II keeps both cubic local factors and the entire quadratic reciprocal phase. Its product modulus has norm comparable to P_aux^2, and v has norm-area scale comparable to P_aux up to the stated polynomial/source factors. Part II supplies the exact smooth and small-period decomposition and its complete frequency sum, yielding the P_aux^(-1/64+epsilon) saving after the actual radial normalization.

## Part II. The complete fixed square-class contribution

### 1. Exact branch and conclusion

Use the same balanced original physical branch defined in the exact-object section above and the linked balanced physical-strata report: positive orientation, old T-only restorer, n=n'=1, all-Ec, common E and a,

 c=C0 b, c'=C0 b', C0=E a varpi,
 NE~Z^(1/6), Na,Nb,Nb'~sqrt(Z/P), P=Nvarpi fixed,
 (b,b')=(bb',C0)=1.

The auxiliary primes are DISTINCT and have norm comparable to P_aux=exp(Z). Keep all original physical phases, true own-prime zeros, complete s valuations, original finite sectors, and the full fixed source activation. Fix a nonzero squarefree element u2 independently of Z and select

         w=q'b'^2 m-q b^2 m'=u2 v^2,       v!=0.                 (1)

The two square roots are counted with factor1/2. This avoids introducing a nonsmooth choice of their arguments. There is no arbitrary additional v- or w-dependent mask in the claimed scalar bound. The original smooth radial windows and finite residue masks remain. Fixed physical-label restrictions, with polynomially bounded multiplicity or weight, may remain.

Let C_square,total be this scalar physical two-column sum with no h-class restriction. Using the character theorem of Part I, we prove that for every fixed epsilon>0,

           |C_square,total| <<_epsilon
                       P_aux^(-1/64+epsilon) Z^C.                (2)

The constants may depend on the fixed u2, fixed original profiles/source and original bad data. The exponent C is fixed independently of the auxiliary primes and source variables.

For the actual h!=h' sum, subtract its exact restricted same-class term. That term has already been paid absolutely on this branch, including after (1): raw Z^(-49/48+epsilon), or raw Z^(-25/48+epsilon) if the actual additional row weight Na is included. Thus the corresponding cross-class bounds are the sum of those explicit prices and (2). Their original outside squared normalization multiplies them by Z^(3/8), giving -31/48 and -7/48 respectively. No further unpriced polynomial multiplicity is granted in these same-class exponents.

Previously removed cross-prime holes may be restored before Poisson. On (1), m=q'k implies u2 v^2=(q'b')^2 k mod q, with at most two v roots; the actual k/v disks give only Z^C exp(C(|alpha|+|alpha'|)) possibilities. Both true radial normalizers give P_aux^(-1)Z^C exp(C(|alpha|+|alpha'|)). The symmetric hole is identical. Full source integration therefore pays these changes by P_aux^(-1)Z^C, by the following direct count. Writing A_source=|alpha|+|alpha'|, the physical disk gives Nk<=Z^C exp(A_source). For each k the at most two q residue classes for v contain O(1+Nv/Nq)<=Z^C exp(C A_source) lattice points, because Nv<=P_aux Z^C exp(A_source/2) and Nq is comparable to P_aux. Each (k,v) fixes m' if it is integral. The original pair normalization is P_aux^(-1) times the stated polynomial/source factor. This proves the asserted restoration price directly; the full source moments above pay its fixed exponential cost. The own-prime zeros are not restored: they are exactly the primitive cubic character zeros below.

### 2. Every fibre frequency has an actual harmonic quadratic phase

Freeze q,q' and the original small labels. Put Acoef=q'b'^2, Bcoef=q b^2, and take a principal small-period ideal J=(j), prime to qq', large enough for all the remaining original m,m' periodic factors. Its norm is at most Z^C. This uses the exact mixed two-Gauss-root identity before estimates; the original auxiliary m characters have been moved to w, while the physical chi_c(m), xi0(m), s Gauss functions, zero extensions and finite ray data are all retained in the small-period table P(x,y). All remaining factors independent of v, including the original normalized Gauss roots, keep their phases.

Partition v modulo J. At v=v0 mod J enumerate the original small residue pairs x,y modulo J satisfying

                Acoef x-Bcoef y=u2 v0^2 mod J.                   (3)

There are exactly NJ such pairs because Acoef,Bcoef are coprime. Write

 m=x+jz, m'=y+jz',
 t(v)=(u2 v^2-Acoef x+Bcoef y)/j in O_K.

Then Acoef z-Bcoef z'=t(v). Choose a fixed inverse Abar of Acoef modulo Bcoef, and set z0(v)=Abar t(v) modulo Bcoef. The integral m solutions form the coset

                   m=x+j z0(v)+j Bcoef O_K.

Poisson summation on this actual coset, using the original trace-dual lattice O_K^vee and normalized plane measure, gives for each dual element ell a factor

 exp(2pi i Tr(ell(x+j z0(v))/(j Bcoef)))
   =constant_(q,q',ell,x,y)
        exp(2pi i Tr(eta_ell v^2)),
                  eta_ell=ell Abar u2/(j Bcoef).                  (4)

The equality is on the selected v residue class. Changes of representatives alter the phase only by an integral trace. Thus the entire v-dependent arithmetic phase is genuinely harmonic quadratic with an unrestricted real coefficient. No assertion that its denominator is small is needed.

The two original roots on the square class leave, up to a bounded factor independent of v,

                chi(v)=chi_cubic,q(v) conjugate(chi_cubic,q'(v)). (5)

It has two nonprincipal primitive cubic local factors modulo the ideal qq'. Original unit zeros at q,q' are exactly its zeros. The physical b/b' character factors have not disappeared: they remain in the table for the v residue class modulo J. The finite q-ray factors and all original scalar/root phases multiply the estimate by bounded or polynomial-label factors only.

The continuous coefficient for (4) is

 W_ell(v)=1/N(j Bcoef)
     integral_C W0(Nz/M)
          W0(N((Acoef z-u2 v^2)/Bcoef)/M')
                  exp(-2pi i Tr(ell z/(j Bcoef))) dmathfrak m(z), (6)

where M=N(b0q)X exp(-alpha)Ns and M'=N(b0q')X exp(-alpha')Ns'. The periodic table coefficient and the original two M^(-1/2) factors are outside (6). Formula(6), including ell=0, is the actual full Poisson decomposition of the physical fibre. No truncation of ell or replacement by its zero mode has been made.

### 3. The whole frequency sum has a paid smooth-variation envelope

Write A_source=|alpha|+|alpha'|. The two original radial disks imply

                   Nv <= P_aux Z^C exp(A_source/2).              (7)

Every W_ell is a smooth compactly supported function of the two real coordinates of v. Substitute z=sqrt(M)y in(6). The first W0 restricts y to a fixed compact set. The second depends smoothly on

 (Acoef/Bcoef)sqrt(M/M')y-u2 v^2/(Bcoef sqrt(M')).

The Fourier phase in y has frequency ell sqrt(M)/(j Bcoef), independent of v. Let

                         H_freq=N(j Bcoef)/M.

At any fixed derivative order and any fixed K, integration by parts in y, followed by two-dimensional variation in v, gives

 ||W_ell||_Abel
   <= [M/N(j Bcoef)] Z^C exp(C A_source)
                     (1+Nell/H_freq)^(-K).                      (8)

Here ||W||_Abel may be taken as the integral of the absolute mixed coordinate derivative after extension by zero. The fixed-order derivative estimates needed for this bound contain no positive P_aux power. To check this directly, put q=sqrt(P_aux)Q, q'=sqrt(P_aux)Q', and v=sqrt(P_aux)R_V V, with R_V=Z^C exp(C A_source) covering(7). The Q,Q' variables stay in fixed annuli away from zero, and all P_aux powers cancel in the second window. The area factor from v differentiation cancels its two derivative-scale factors in the Abel seminorm. Integration by parts in y differentiates only fixed smooth profiles with polynomial-Z/fixed-exponential-source costs. Choosing twice as many integrations proves the squared-norm envelope in(8).

Both M/N(j Bcoef) and H_freq, or 1+H_freq, are bounded by Z^C exp(C A_source). The fixed two-dimensional dual-lattice count gives

       sum_ell (1+Nell/H_freq)^(-K) << 1+H_freq,   K>1.

Consequently

                  sum_ell ||W_ell||_Abel
                              << Z^C exp(C A_source).            (9)

This includes every frequency, even one divisible by an auxiliary prime. There is no need to assert that all ell are smaller than q: the reviewed mixed-character theorem is uniform in the quadratic coefficient in(4).

The NJ v classes and NJ residue pairs in(3), and their table values, have only polynomial total cost. All compensation/s labels in this branch also have only polynomial count. The old restoring operator changes only single-column Gaussian T scales; taking the Gaussian supremum and summing its actual coefficient l1 series leaves(8)-(9) unchanged. It does not change M, the coset, or the fibre frequency.

### 4. Exact application of the mixed-character lemma

Let Q_mod=N(qq'), so Q_mod is comparable to P_aux^2. Choose E0=Z^C exp(C A_source)>=1 to cover NJ and the ratio of the enclosing v disk in(7) to Q_mod^(1/2). Part I's two-prime Eisenstein mixed-character theorem gives, uniformly in ell and in the chosen v residue class,

 |sum_(v=v0 mod J) chi(v) exp(2pi i Tr(eta_ell v^2)) W_ell(v)|
   <<_epsilon Q_mod^(63/128+epsilon) E0^2 ||W_ell||_Abel.          (10)

All its hypotheses are actual ones here: q and q' are distinct good primes of comparable norms, (J,qq')=1, both local cubic characters are nonprincipal, the additive polynomial is harmonic quadratic with arbitrary coefficient, and the weight is smooth with the paid variation envelope. Values v=0 contribute zero by the character's own zero extension. No squarefree condition on v is imposed. The lemma allows every coordinate partial rectangle inside the enclosing disk, as required by Abel integration.

Sum(10) over ell by(9), then over the finite small residue tables and all selected labels. The original M^(-1/2)(M')^(-1/2) contributes P_aux^(-1) Z^C exp(C A_source). Since Q_mod^(63/128)=P_aux^(63/64) times a bounded factor, the result is

 |C_square,total(alpha,alpha')|
       <<_epsilon P_aux^(-1/64+epsilon) Z^C exp(C A_source),       (11)

after renaming epsilon. Both original auxiliary probability laws have total mass one; this step is a uniform bound at each prime pair and does not need a new prime-distribution theorem or a conditional renormalization. Integrating(11) against |f_q(alpha)f_q(alpha')| is legal because the fixed actual source has every fixed exponential L1 moment. This proves(2) using the independently reviewed character lemma and the source/Poisson estimates proved here.

### 5. Restrictions on the conclusion and further subtractions

The scalar bound does not permit an arbitrary bounded v mask: such a mask could destroy the character cancellation in(10). Fixed finite residue restrictions and the actual smooth radial weights are explicitly paid. If one wishes to return to a far-w restriction after estimating the complete fixed square class, the omitted near-w part can instead be counted absolutely. For example Nw<=P_aux^(1-delta) gives Nv<=P_aux^((1-delta)/2)/sqrt(Nu2), so the earlier fibre count and true radial normalization give at most P_aux^(-1/2-delta/2) Z^C exp(C A_source). This integrates over the full source. No partial-summation estimate for an arbitrary sharp curved mask is asserted.

All bounds in this report keep u2 fixed. Summing over a growing or unrestricted set of square classes requires a separate uniform bound and its actual counting cost. It is not supplied by(2) alone; Part III proves the needed uniformity for the explicitly bounded pool. Likewise no change of E/a branch, n-range, observation, source, or original Mobius coefficient is made. The result pays an entire actual fixed square-class contribution and its already priced same-class subtraction, not the remaining large-squarefree-kernel or whole-cross problem.

## Part III. A uniform growing squarefree-kernel pool

### 1. Exact square-class selection and statement

Retain the original branch and notation of Part II: P_aux=exp(Z), distinct auxiliary primes q,q' of comparable norms P_aux, n=n'=1, all-Ec, common E and a, c=C0 b and c'=C0 b', C0=E a varpi. All original physical zero masks, finite sectors, s valuations, Gaussian factors and the complete old T-only restoring operator remain. The unrestricted scalar still means that the original h-class inequality has not yet been imposed.

Choose once and for all one generator for every integral ideal of the Eisenstein ring O, and two representatives for O^*/(O^*)^2. For every squarefree ideal choose the two resulting squarefree element representatives. Denote this set by U_2. Every nonzero w has a unique expression

                    w=u v^2,  u in U_2,

up to v -> -v. Count both v with factor1/2. This is a partition of the original nonzero w, not an additional coefficient weight. There are O(U) representatives u with Nu<=U, by the fixed-field ideal count.

Fix theta0<1. For all sufficiently large Z and every u in U_2 with

                         1<=Nu<=P_aux^theta0,                (1)

the fixed-class scalar estimate is uniform:

       |C_u,total| <<_(epsilon,theta0,fixed data)
                          P_aux^(-1/64+epsilon) Z^C.          (2)

In particular for 1<=U<=P_aux^theta0, retaining all square classes Nu<=U gives

       |C_(Nu<=U),total| <<_epsilon
                          U P_aux^(-1/64+epsilon) Z^C.        (3)

For the concrete choice U=P_aux^(1/128), every fixed epsilon<1/128 gives an exponential saving P_aux^(-1/128+epsilon) Z^C. An arbitrarily small adjustment of epsilon permits any fixed smaller saving constant to absorb the polynomial in Z.

The corresponding h!=h' contribution is (3) minus the exact restricted same-class contribution. The latter is bounded ONCE by the already reviewed absolute same-class bound for the entire original branch, since the union Nu<=U is one mask bounded by one. It incurs no U factor. Thus add raw Z^(-49/48+epsilon), or raw Z^(-25/48+epsilon) when the specified additional Na row weight is present. The original Z^(3/8) squared normalization gives -31/48 and -7/48 respectively. All original restrictions on the label counts for those prices remain.

### 2. Uniform arithmetic factors and restored cross holes

Every auxiliary prime norm is at least c P_aux with fixed c>0. In(1), for large Z no such prime divides u. The two original own-prime zero masks consequently remain exactly the zeros of the two primitive cubic factors in v. The mixed-root factor psi(u/b0) has modulus one, regardless of Nu or its argument, and introduces no growth. Its finite-ray factors are unchanged.

The small period J is formed from the original c,c',s,s',b0 and original fixed character periods. It does not acquire the prime divisors of u. The small residue table merely reads u modulo J. For every selected v class the equation Acoef x-Bcoef y=u v0^2 modulo J still has exactly NJ solutions, because Acoef=q'b'^2 and Bcoef=q b^2 are coprime. The number and absolute bounds of all table entries are the same polynomial in Z as before.

For a previously removed cross hole m=q'k, the congruence u v^2=(q'b')^2k modulo q has at most two roots, uniformly in u in(1). The real v disk can only shrink as Nu grows. The existing disk/coset counting bound therefore gives the same P_aux^(-1) Z^C exp(C(|alpha|+|alpha'|)) absolute cost for each u. The symmetric hole is identical. Its pool cost is at most U P_aux^(-1) Z^C after source integration, smaller than(3). This argument restores no own-prime zero and invokes no arbitrary-mask character estimate.

### 3. Uniform full-frequency smooth variation

Write U0=Nu and A_source=|alpha|+|alpha'|. The exact physical windows give Nw<=P_aux^2 Z^C exp(A_source), hence

             Nv<=P_aux U0^(-1/2) Z^C exp(A_source/2).       (4)

For every original Poisson frequency ell, the smooth weight remains exactly

 W_(ell,u)(v)=1/N(j Bcoef) integral_C
   W0(Nz/M) W0(N((Acoef z-u v^2)/Bcoef)/M')
          e(-Tr(ell z/(j Bcoef))) dmathfrak m(z).

The exact accompanying phase is e(Tr(ell Abar u v^2/(j Bcoef))), with Abar inverse Acoef modulo Bcoef. No restriction on this coefficient is imposed by Part I.

To verify uniformity of the weight, put z=sqrt(M)y and use the positive real scaling

               v=sqrt(P_aux) U0^(-1/4) R_V V,
                R_V=Z^C exp(C A_source).

The second archimedean window becomes a function of

 (Acoef/Bcoef)sqrt(M/M') y
      - [u/|u|] P_aux R_V^2 V^2/(Bcoef sqrt(M')).

All positive powers of U0 cancel exactly. The remaining u/|u| lies on the fixed unit circle, so every required fixed derivative is uniformly bounded in this parameter. The auxiliary P_aux powers cancel exactly as in the fixed-u proof. The enclosing support in V, coefficient ratios, and inverse scale factors have at most polynomial-Z and fixed-exponential-source costs.

The two coordinate derivatives in the genuine Abel seminorm contribute the inverse square of the positive v scaling; the v area element contributes its square. They cancel, including the entire U0 dependence. With H_freq=N(j Bcoef)/M, the identical integration-by-parts proof therefore gives uniformly for every ell

 ||W_(ell,u)||_Abel
  <= [M/N(j Bcoef)] Z^C exp(C A_source)
                          (1+Nell/H_freq)^(-K),            (5)

for any fixed K, with constants independent of u satisfying(1). H_freq does not depend on u. Summing all ell, including frequencies divisible by either auxiliary prime, gives

                 sum_ell ||W_(ell,u)||_Abel
                            <<Z^C exp(C A_source).         (6)

The old restoring operator only changes the single-column Gaussian T scales. Its actual absolute coefficient series remains bounded, uniformly in u, when those Gaussians are bounded by their supremum. No derivative of that series is needed.

### 4. Application, source integration and limits of scope

Part I can use the SAME enclosing-disk parameter E0=Z^C exp(C A_source) for every u in(1): (4) is contained in its original P_aux E0 disk, and NJ<=E0. It is uniform in the arbitrarily large coefficient ell Abar u/(j Bcoef), in the coset, and in the two prime characters. Apply it with the variation envelope(5), sum by(6), and retain the original two M^(-1/2) normalizers. This gives

 |C_u,total(alpha,alpha')|
        <<P_aux^(-1/64+epsilon) Z^C exp(C A_source)

with C independent of u. All finite tables and original label sums have exactly the previous costs. The original fixed source has every fixed exponential L1 moment, so integration is uniform in u and proves(2). The elementary O(U) ideal count then proves(3).

No growing-source constants, new q-dependent source, character-conductor theorem, or source-tail truncation is used. The pool selection is performed by the unique squarefree-kernel partition before estimates. The scalar proof does not cover an additional arbitrary bounded v mask. A near-w restriction may be subtracted absolutely as in the fixed-class proof, with its actual pool count paid separately; this is not needed for(3).

The estimate controls a growing but small squarefree-kernel pool in this one original balanced branch. It does not control its large-kernel complement, different E/a compensation pairs, other n branches or the full different-free-norm Mobius cross sum. The same-class subtraction keeps its separately stated polynomial cost, rather than being silently folded into an exponential scalar claim.
