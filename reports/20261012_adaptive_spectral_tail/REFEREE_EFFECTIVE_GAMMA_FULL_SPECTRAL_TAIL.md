# Independent review: effective Gamma tails on the whole nonpositive spectral subspace

The complete [mathematical proof](EFFECTIVE_GAMMA_FULL_SPECTRAL_TAIL.md) has been independently reviewed, including the weighted original-domain commutator, the square-root estimate, the mixed-state energy term and every constant in the explicit cutoff. The effective operator-norm statement concerns the true projection P=1_(-infinity,0](H). The separate prime-edge residual and critical complementary sign remain unproved.

## Domain and original commutator

H>=-C makes HP and BP bounded and puts the entire range of P in D(H)=D(B). Bounded Lipschitz multiplication preserves the original source form domain. The bounded commutator m[b(D),q]m, justified from the integrable first jump moment, then proves qD(B) is contained in D(B) by the associated-form criterion. It is not necessary to assume global unweighted b(D)(mv) in L2. Thus the exact compression identity [A,X]=-P[H,q]P is legitimate on the full spectral subspace.

For q=chi^2 its Lipschitz constant is at most 4/s. A nonzero difference has an exterior endpoint, so the true product of theta factors is bounded by M*m_tail(R). This gives 36M*m_tail(R)/s for the Gamma commutator. The scalar C0m^2 commutes; each retained prime shift has difference at most one, and the omitted operator-norm tail pays 2delta_N. Therefore K(R,s,N) in (10) is a valid uniform bound without an unweighted bounded prime shift assumption.

## The genuinely new mixed-spectral payment

For bounded positive A and 0<=X<=I, the square-root integral is norm convergent. On t<=d=||[A,X]|| the commutator of A(A+t)^(-1) with X is at most two; on t>d the resolvent identity bounds it by d/t. The two integrals give (4+2)sqrt(d)/pi. The d=0 case follows from functional calculus, so a kernel of A causes no inverse problem.

The identity XA=sqrt(A)Xsqrt(A)+[X,sqrt(A)]sqrt(A) separates a positive quadratic form and a bounded remainder. It proves (13), with 2sqrt(CK), for arbitrary spectral superpositions. No unjustified sign is assigned to Re<chi^2v,Hv>. This is precisely what was missing from the earlier eigenvector-only argument.

The weighted jump localization remainder retains both theta multipliers and has the stated coefficient 72. Adding the true V contribution and the mixed-spectral payment yields (15). Locally, b(D)f=m^(-1)Bv and ||Bv||<=2C; the compact interior cutoff and the same source commutator prove actual D(b(D)) membership and the bound L(R,s). This supplies the interior regularity in the correct original domain.

## Complete explicit ledger

The low/high source-frequency split and the two-term energy inequality give exactly (17). The scalar series bound beta_J(T)<=3T^2/(8J^2) is the same complete-Gamma remainder already verified.

For the chosen y,R,s,N, the bounds c_N<=8y^2 and delta_N<=y^3 exp(-pi y/2) hold. Direct substitution gives h<=1121y^3E<1200y^3E and K<=114y^3E+504y^2E<=366y^3E<400y^3E. The explicit C<41 follows from c2<10, M=2, and delta2<1. The lower and upper bounds on y in (19) are valid for ell>=1.

Now E=eta^2 exp(-80)(ell+2)^(-3). The two elementary integer comparisons in (22) each pay less than eta/6, so the whole exterior budget is below eta/3. The selected T pays the interior high-frequency term below eta/3. The selected integer J pays the remaining low-frequency term by 3eta/16. Their sum is strictly below eta, uniformly for every unit vector of range(P).

For growth, exp(2/y)<=1+4/y and the actual inner theta lower bound yield (25). Squaring the two terms of L gives K0=(8C^2/9)exp(4pi)+648M^2. Since y^4<=exp(pi y), and exp(pi y)=exp(160)eta^(-4)(ell+2)^6, the stated L_* bound follows. Rounding J<=5T/sqrt(eta) proves the exact coefficient in (26), including the harmless additive 4. All constants are explicit and independent of computing P.

## Scope

The conclusion is stronger in domain than the earlier effective eigenvector-only result: it covers the whole actual nonpositive spectral subspace and all mixed spectral vectors there. It still does not cover a general expectation-energy cone. It does not construct a finite approximation to P, decide its strictly negative ground-perpendicular part, or control the prime-edge residual. The result is an effective Gamma approximation input only. No successful all-depth inertia test or zeta-zero exclusion is asserted.

## Appendix review: logarithmic mixed term and the stronger cutoff

The mathematical appendix has been independently checked. It sharpens the preceding sufficient whole-span rate from eta^(-5) to eta^(-3), with the same logarithmic fourth power and explicit constants. The earlier theorem remains correct.

### Weighted square-root lemma

For A_tau=A+tau I, the functional-calculus formula gives exactly

 [X,sqrt(A_tau)]sqrt(A_tau)
 =pi^-1 integral_0^infinity t^(1/2)(A_tau+t)^-1[X,A](A_tau+t)^-1 sqrt(A_tau)dt.

The integrand is norm integrable after tau>0 regularization. Below tau, the two resolvent factors give t^(1/2)/tau^(3/2), whose integral is 2/3. On [tau,C+tau], the bounds ||(A_tau+t)^-1||<=1/t and sup_lambda sqrt(lambda)/(lambda+t)<=1/(2sqrt(t)) give 1/(2t). Above C+tau, the bound sqrt(C+tau)t^(-3/2) integrates to 2. Thus (A.3) has constant 8/3 and the stated half logarithm.

The identity X A_tau=sqrt(A_tau) X sqrt(A_tau)+[X,sqrt(A_tau)]sqrt(A_tau) has the correct multiplication order. Positivity of its first term and 0<=X<=I give the unfavorable quadratic part at most tau plus the commutator norm. Setting tau to the chosen positive commutator upper bound K, and using pi>3, proves K[2+log(1+C/K)/6]. The lemma bounds the negative quadratic part only; no false norm bound on the whole Jordan product is used. Commuting A,X give the asserted K=0 endpoint directly.

### Original spectral application and domains

The unchanged full-spectrum proof supplies P=1_(-infinity,0](H), A=-H|range P in [0,41], X=P chi^2 P, qD(H) subset D(H), and [A,X]=-P[H,q]P. The displayed K retains the exterior theta product, the true first jump moment and complete omitted-prime norm tail. It is a bound on the actual compressed commutator even when the subspace contains different spectral values and the kernel. The new lemma replaces only the previous mixed-term estimate.

The weighted IMS error and interior multiplier localization therefore give (A.5)–(A.7) on the same domain. In particular b(D)(mv) is not assumed globally L2: the interior bound follows from the local original equation, division by the positive compact minimum mu(R+s), and a bounded source commutator. The source-band split retains 0<=beta_J<=b and the already verified explicit bound beta_J(T)<=3T^2/(8J^2).

### Exterior numerical ledger

For y>=2 and an integer y<=N<=y+2, log N<=sqrt N gives c_bar<=12y. The complete-prime delta bound divided by y^2 exp(-pi y/2) is at most (6125/9)exp[-pi(y/2+1)]<2. The stated proof at y=2 uses exp(6)>(8/3)^6>6125/18, and monotonicity covers larger y.

Consequently K<=676y^2 E_y<700y^2 E_y, while h<=1008y^3 E_y+170y^2 E_y<=1093y^3 E_y<1100y^3 E_y. Applying the operator lemma directly with K_bar is legitimate. Since K_bar>=E_y and C=41, log(1+C/K_bar)<=log 42+pi y/2<4y. Hence R_C(K_bar)<1200y^3 E_y and the total exterior payment is below 4600y^3 E_y. Every constant has sufficient slack at y=2.

### Joint selection and growth

With ell=log(1/eta)>=1, the chosen y=(2/pi)(ell+3log(ell+2)+40) satisfies R>=1 and (2/pi)(ell+2)<=y<12(ell+2). The exact exponential is E_y=eta exp(-40)(ell+2)^(-3), so the complete exterior budget is less than eta/3. The elementary numerical comparison 13800*12^3=23846400<2^25<exp(40) is correct.

The chosen T and J give interior high-frequency payment below eta/3 and low-frequency payment at most 3eta/16. An interval-certified integer N in the width-2 interval and J in the indicated much longer interval avoid any exact-real ceiling decision; such choices preserve every bound.

Finally, the inequality exp(2/y)<=1+4/y controls mu(R+s), and y^4<=exp(pi y) absorbs the commutator's polynomial term. The displayed K0 therefore satisfies L_*^2<=K0 y^-2 exp(pi y). Substituting y yields exactly eta^-2(ell+2)^4 with coefficient (K0 pi^2/4)exp(80). Multiplication by 6/eta in log T gives the leading coefficient (3pi^2 K0/2)exp(80) and exponent eta^-3. The remaining log 5+1+ell/2 is absorbed by the stated additive 4. Thus (A.15)–(A.16) hold uniformly on the whole true nonpositive spectral subspace.

### Scope

The gain is a better mixed-product estimate and a sharper sufficient cutoff. The actual projection is not computed, no prime-edge residual is removed, and neither a central/Schur inertia certificate nor critical positivity follows. The previously published eta^-5 estimate is correct and needs no erratum.
