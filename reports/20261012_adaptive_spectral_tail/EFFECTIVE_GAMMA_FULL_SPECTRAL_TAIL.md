# Effective complete-Gamma tails for the entire true nonpositive spectral subspace

Let P=1_(-infinity,0](H) be the actual spectral projection of the original even theta/Gamma/complete-prime operator. For every 0<eta<=exp(-1), this theorem supplies an explicit integer J(eta) such that

    ||sqrt(beta_J)(D)mP||^2<eta,  beta_J=b-b_J,
    log J(eta)<=C_fullGamma eta^(-5)(log(1/eta)+2)^4.

The estimate is uniform over all normalized vectors in range(P), including arbitrary superpositions of different nonpositive spectral values and kernel vectors. It does not require computation of P. The constants and parameter prescription are explicit below.

The earlier [effective eigenstate theorem and qualitative spectral-span theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/b964dea922c9ec87a572b812a651525e591dfaa9/reports/20261012_adaptive_spectral_tail/EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md) retain their original scopes. The new step here is the weighted compressed commutator together with a square-root commutator estimate. It controls the previously unpaid mixed spectral term instead of incorrectly assigning that term a sign. The effective whole-span rate is weaker than the earlier eigenvector-only rate.

The full-prime edge defect after shorting remains unestimated. This Gamma-tail theorem does not establish a complementary sign, an all-depth inertia certificate, a new spectral gap, or any zeta-zero exclusion. The existing original gap 511/1024 is unchanged.

## Original normalization and complete published inputs

Use the user's [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/b964dea922c9ec87a572b812a651525e591dfaa9/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), on complex even L2(R,dx), with fhat(t)=integral f(x)exp(-itx)dx and Plancherel measure dt/(2pi). The actual theta multiplier and coefficients are

    Phi(x)=sum_(n>=1)[4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2)]
                               exp[-pi n^2 exp(2x)]  (x>=0),
    m^2=Phi/(2cosh(x/2)),  alpha_n=Lambda(n)/sqrt(n),
    b(t)=Re psi(1/4+it/2)-psi(1/4),
    C0=-psi(1/4)+log pi
      =EulerGamma+pi/2+3log 2+log pi.

Phi is extended by its true theta evenness. B is the operator of the closed form b[mv], and H=B-V with the complete bounded V below. The operator-domain condition is that m b(D)(mv) is represented by an L2 vector; global unweighted b(D)(mv) in L2 is not assumed.

The elementary theta bounds, full-prime operator-norm tail delta_N, exact Gamma jump identity and its two moments are proved in the [published normalization and Part A Sections 1–2](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/b964dea922c9ec87a572b812a651525e591dfaa9/reports/20261012_adaptive_spectral_tail/EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md). Section 1 below states all of those inputs with their constants. The new weighted commutator, domain-invariance proof, square-root estimate, mixed term and effective whole-span ledger are proved here in full. No unknown kernel characterization, source-domain replacement or unproved projection computation is used.

The user's [quantitative prime-two depth obstruction](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/b964dea922c9ec87a572b812a651525e591dfaa9/reports/20261012_fixed_shortening_essential_band/QUANTITATIVE_PRIME_TWO_GAMMA_DEPTH.md) concerns a different sufficient-sign problem for a selected-space comparator. Its necessary-depth conclusion retains its user attribution. The present J is sufficient only for Gamma approximation on the actual nonpositive spectral subspace. It does not make that comparator successful or control its remaining prime-edge residual.

An [independent review](REFEREE_EFFECTIVE_GAMMA_FULL_SPECTRAL_TAIL.md) checks the complete mixed-state argument and the precise domain restrictions.

## 1. Original operators and already established scalar bounds

Work on the original even Hilbert space with its closed form realization

 H=B-V,  B=M_m b(D)M_m>=0,  D(H)=D(B).

The original complete prime operator V is bounded and selfadjoint. Its finite-prime approximation is

 V_N=C0 m^2 + sum_(2<=n<=N) alpha_n m(tau_(log n)+tau_(-log n))m,

where alpha_n>=0. All operators H, B and V in the conclusion remain the complete original operators. Retain the established bounds

 9 exp(4|x|-pi exp(2|x|)) <= m(x)^2
 <= Astar exp(4|x|-pi exp(2|x|)),  Astar<49.

For r>=0 set

 M=2,
 m_tail(r)=7 exp(2r-(pi/2)exp(2r)),
 mu(r)=3 exp(2r-(pi/2)exp(2r)).                         (1)

They give ||m||_infinity<=M, sup_(|x|>=r)m(x)<=m_tail(r), and inf_(|x|<=r)m(x)>=mu(r). For N>=2 put

 c_N=C0+2 sum_(2<=n<=N) alpha_n,
 delta_N=(20 Astar/9)(N+1)^2 exp[-pi(N+1)],
 C=M^2 c_2+delta_2.                                   (2)

The established complete-prime norm tail gives ||V-V_N||<=delta_N and ||V||<=C. We use C0<8 and alpha_n<=log(n)/sqrt(n), so

 c_N<=C0+4sqrt(N)log N.                               (3)

In particular alpha_2<1 gives c_2<10, and delta_2<980 exp(-3pi)<1. Hence C<41.

The complete Gamma jump kernel and its form are

 k(y)=exp(-|y|/2)/(1-exp(-2|y|)), y!=0,
 b[f]=(1/2) integral integral k(y)|f(x+y)-f(x)|^2 dxdy.

The verified moments and scalar symbol bound are

 M1=integral |y|k(y)dy<9,
 M2=integral y^2k(y)dy<36,
 b(T)>=(1/2)log(1+4T^2), T>0.                         (4)

For b_J(t)=sum_(0<=j<J)t^2/[(j+1/4)(4(j+1/4)^2+t^2)] and beta_J=b-b_J,

 0<=beta_J(t)<=b(t),
 sup_(|t|<=T)beta_J(t)=beta_J(T)<=3T^2/(8J^2), J>=1.   (5)

These are scalar estimates for the complete symbol, not finite-prime changes to H.

## 2. Spectral subspace and domain-safe weighted commutator

Let

 P=1_(-infinity,0](H),  Kspace=range(P).

Since H>=-C, P maps the Hilbert space boundedly into D(H)=D(B). In particular HP and BP are bounded, and on Kspace

 A=-H|Kspace is bounded selfadjoint, 0<=A<=C I.         (6)

Fix R>=1 and 0<s<=1. Choose a smooth even function chi with 0<=chi<=1, chi=0 on |x|<=R, chi=1 on |x|>=R+s, and Lip(chi)<=2/s. Put q=chi^2. Then Lip(q)<=4/s.

For any bounded Lipschitz multiplier a, the jump kernel gives

 ||[b(D),a]||<=M1 Lip(a).                             (7)

Multiplication by a preserves Q(b); this follows by expanding the source increment and using integral min(4||a||_infinity^2,Lip(a)^2 y^2)k(y)dy<infinity. The kernel expression in (7) first holds for truncated jump kernels and extends by its integrable bound.

Consequently multiplication by q preserves Q(B). The bounded commutator of B with q is

 [B,q]=m[b(D),q]m.                                   (8)

For completeness, the associated-form criterion proves qD(B) is contained in D(B): for v in D(B), the form against a test w in Q(B) equals the form against qw plus the bounded term represented by (8). The representing vector is qBv+[B,q]v in L2. Thus Bqv=qBv+[B,q]v, and the same domain inclusion holds for H. This does not assume b(D)mv belongs globally to L2.

Whenever q(x+y)-q(x) is nonzero, at least one of |x| and |x+y| is greater than R. Therefore m(x)m(x+y)<=M m_tail(R). The kernel Schur/Young bound proves

 ||[B,q]||<=36 M m_tail(R)/s.                         (9)

For a finite-prime shift, the commutator is a shift times the multiplier

 m(x)m(x+a)(q(x+a)-q(x)), a=log n or -log n.

Its norm is at most M m_tail(R), because |q(x+a)-q(x)|<=1 and a nonzero difference again has an exterior endpoint. The C0m^2 term commutes with q. Finally ||[V-V_N,q]||<=2delta_N. Therefore

 ||[V,q]||<=M m_tail(R)c_N+2delta_N,
 ||[H,q]||<=K(R,s,N),
 K(R,s,N):=M m_tail(R)[c_N+36/s]+2delta_N.             (10)

Here c_N is a convenient upper bound for the sum of the nonconstant shift coefficients. No bounded unweighted infinite shift operator is assumed.

The compression

 X=PqP|Kspace

satisfies 0<=X<=I. Domain invariance and commutation of the spectral projection P with H imply the exact identity

 [A,X]=-P[H,q]P|Kspace.                               (11)

For example H Pqv=P Hqv is valid because qv is in D(H); the other term uses Hv in Kspace. Hence ||[A,X]||<=K(R,s,N), uniformly without constructing P.

## 3. Square-root commutator pays the mixed spectral term

We use the following elementary bounded-operator lemma. If 0<=A<=C I, 0<=X<=I and d=||[A,X]||, then

 ||[sqrt(A),X]||<=(6/pi)sqrt(d)<=2sqrt(d).             (12)

If d=0, the conclusion follows from continuous functional calculus. If d>0, the norm-convergent integral representation gives

 [sqrt(A),X]=(1/pi) integral_0^infinity
                    t^(-1/2)[A(A+t)^(-1),X] dt.

For small t the commutator norm is at most 2, because ||A(A+t)^(-1)||<=1 and ||X||<=1. For large t, the resolvent identity gives

 [A(A+t)^(-1),X]=t(A+t)^(-1)[A,X](A+t)^(-1),

whose norm is at most d/t. Split at t=d. The two integrals are respectively at most 4sqrt(d) and 2sqrt(d), proving (12). The integral also converges at both endpoints by these bounds, so a possible kernel of A causes no domain or invertibility problem.

For any unit vector v in Kspace,

 XA=sqrt(A)Xsqrt(A)+[X,sqrt(A)]sqrt(A).

The first term has nonnegative quadratic form. Since the inner product convention is conjugate-linear in its first entry, taking real parts in either adjoint ordering gives

 Re<qv,Hv>=-Re<Xv,Av>
             <=||[sqrt(A),X]|| ||sqrt(A)||
             <=2sqrt(C K(R,s,N)).                    (13)

This is the additional term needed for genuine spectral superpositions. It is not obtained by assigning a sign to Re<qv,Hv>.

## 4. Weighted exterior energy and interior regularity

Let v be any unit vector of Kspace and f=mv. The exact Gamma localization identity is

 b[chi f]=Re b(qf,f)+E_chi[f],
 E_chi[f]=(1/2) integral integral k(y)(chi(x+y)-chi(x))^2
                    Re(conjugate(f(x+y))f(x)) dxdy.

The error integral is absolutely convergent. Retaining both theta multipliers on its support gives

 |E_chi[mv]|<=(72M/s^2)m_tail(R).                     (14)

Indeed |chi(x+y)-chi(x)|<=2|y|/s, a nonzero difference has an exterior endpoint, and the remaining convolution integral is bounded by M2||v||^2. This identity is justified first with truncated kernels and then on Q(b), using that absolute bound and form-domain continuity.

Because ||chi V||<=M m_tail(R)c_N+delta_N, the original form equation B=H+V, (13) and (14) yield

 b[chi f]<=h(R,s,N)+2sqrt(C K(R,s,N)),
 h(R,s,N):=M m_tail(R)[c_N+72/s^2]+delta_N.            (15)

For the interior source put theta=1-chi and g=theta f. Since ||Hv||<=C and ||Vv||<=C, ||Bv||<=2C. The associated-form equation implies locally in distributions

 b(D)f=m^(-1)Bv.

The compact support of theta and the commutator bound (7) therefore give the globally L2 expression

 b(D)g=theta m^(-1)Bv+[b(D),theta]f.

In particular g belongs to D(b(D)), with

 ||g||<=M,
 ||b(D)g||<=L(R,s),
 L(R,s):=2C/mu(R+s)+18M/s.                            (16)

This derives local Gamma regularity from the original operator equation; it does not presume global unweighted Gamma regularity of f.

## 5. Effective uniform Gamma-tail ledger

Splitting the interior source at source frequency T gives

 beta_J[g]<=beta_J(T)||g||^2+||b(D)g||^2/b(T).

Since f=g+chi f and 0<=beta_J<=b, (15)-(16) imply, for every unit v in Kspace,

 beta_J[mv]<=2M^2 beta_J(T)+2L(R,s)^2/b(T)
                 +2h(R,s,N)+4sqrt(C K(R,s,N)).        (17)

Every entry on the right is explicit and independent of v and P.

## 6. Explicit parameter choice and growth

Fix 0<eta<=exp(-1), let ell=log(1/eta), and choose

 y=(4/pi)[ell+(3/2)log(ell+2)+40],
 R=(1/2)log y,  s=1/y,  N=ceil(y).                   (18)

These choices have R>=1, y>=2 and 0<s<=1. For ell>=1, log(ell+2)<=ell+2 implies

 (4/pi)(ell+2)<=y<22(ell+2).                          (19)

For the upper bound, ell+(3/2)log(ell+2)+40<=2.5ell+43<=16(ell+2), and 64/pi<22.

Since N<=y+1, (3) and log N<=sqrt(N) give c_N<=8y^2. Also

 delta_N<=y^3 exp(-pi y/2), y>=2.                     (20)

To verify (20), use N+1>=y+1, N+1<=y+2<=2y, and Astar<49 to bound delta_N by (3920/9)y^2 exp[-pi(y+1)]. The ratio to the right side is decreasing in y>=2 and already less than 1 at y=2.

Writing E=exp(-pi y/2), equations (10) and (15) now give

 h<=1200 y^3 E,
 K<=400 y^3 E.                                       (21)

More precisely, h<=(1120+1)y^3E; and K<=(114y^3+504y^2)E<=366y^3E, since y>=2.

The parameter choice makes

 E=eta^2 exp(-80)(ell+2)^(-3).

Using C<41 and (19), the exterior budget is bounded by

 2h+4sqrt(CK)
 <=2400*22^3 exp(-80)eta^2
       +80sqrt(41)*22^(3/2)exp(-40)eta
 <eta/3.                                            (22)

Each term is less than eta/6: 14400*22^3<2^28<exp(80), while 480sqrt(41)*22^(3/2)<480*7*22*5<2^19<exp(40); also eta<=1. These elementary comparisons leave substantial slack.

Set L_*=L(R,s) from (16), and take

 T=exp(6L_*^2/eta+1),
 J=ceil(4T/sqrt(eta)).                                (23)

Equation (4) gives 2L_*^2/b(T)<eta/3. Since M=2, (5) gives 2M^2 beta_J(T)<=3eta/16<eta/3. Combining these with (17) and (22) proves

 sup_(v in range(P), ||v||=1) beta_J[mv]<eta,
 equivalently ||sqrt(beta_J)(D)mP||^2<eta.             (24)

The supremum over the zero subspace is understood through the equivalent operator-norm statement. The same bound applies to any spectral subprojection of P.

For a fully explicit growth estimate, define

 K0=(8C^2/9)exp(4pi)+648M^2.

Since exp(2/y)<=1+4/y for y>=2,

 mu(R+s)^(-2)<=(1/9)y^(-2)exp[pi(y+4)],
 L_*^2<=K0 y^(-2)exp(pi y).                           (25)

The second estimate uses (a+b)^2<=2a^2+2b^2 and y^4<=exp(pi y), y>=2. From (18)-(19),

 exp(pi y)=exp(160)eta^(-4)(ell+2)^6,
 L_*^2<=(K0 pi^2/16)exp(160)eta^(-4)(ell+2)^4.

Also J<=5T/sqrt(eta). Thus

 log J<=C_fullGamma eta^(-5)(ell+2)^4,
 C_fullGamma=(3pi^2 K0/8)exp(160)+4.                  (26)

The additive 1+ell/2+log 5 is absorbed by 4eta^(-5)(ell+2)^4. If desired every occurrence of C can be replaced by the explicit universal upper bound 41, including in L_*, making the prescription independent even of evaluating the original scalar coefficients. Parameters can be represented through their logarithms; writing the enormous integer J in full is not required.

## 7. Exact scope and remaining obstruction

Unlike the earlier individual-eigenvector estimate, (24) controls arbitrary unit vectors in the actual nonpositive spectral subspace, including mixtures of different spectral values and kernel vectors. The square-root commutator in Section 3 pays for the mixed spectral term. The use of the true spectral projection is essential; no such conclusion is inferred for the larger set of vectors with merely nonpositive expectation energy.

The formula (23) is a computable sufficient cutoff for the complete Gamma tail on that unknown subspace. It does not construct P, decide whether its strictly negative ground-perpendicular part vanishes, or provide a computable finite-dimensional approximation to P itself. In particular, it does not make an all-depth inertia certificate successful.

The independent residual after retaining the complete Gamma symbol in the full-prime diagonal comparison remains

 e[v]=sum_(n>=2)alpha_n integral m(x)m(x+log n)
                              |v(x+log n)-v(x)|^2 dx.

No smallness or required sign for this prime-edge residual, or its shorting against the known or full kernel, follows from (24). Critical complementary positivity and RH remain unproved.

## Appendix. A logarithmic mixed-term estimate sharpens the whole-span rate

The preceding theorem and its original eta^(-5) rate remain valid. The following complete strengthening replaces the square-root loss in the mixed spectral term by K log(1/K). On exactly the same entire true nonpositive spectral subspace, it gives an explicit cutoff with

    ||sqrt(beta_J)(D)mP||^2<eta,
    log J<=C_sharp eta^(-3)(log(1/eta)+2)^4.

The operator lemma, sharper exterior ledger and explicit constant are proved below. Domain invariance, weighted localization and interior regularity are the unchanged proofs in Sections 1–5 above. This improves only the sufficient Gamma approximation rate; no central sign or prime-edge residual estimate follows.

### A.1. A bounded positive-operator lemma

Let A and X be bounded selfadjoint operators on a Hilbert space with

 0<=A<=C I, 0<=X<=I,
 ||[A,X]||<=K, K>0.

For every unit vector v,

 -Re<v,XA v><=R_C(K),
 R_C(K)=K[2+(1/6)log(1+C/K)].                        (A.1)

If K=0 the left side is nonpositive, so R_C(0)=0 is the continuous extension. This estimate concerns the negative part of the real quadratic form, not the entire Jordan product's norm.

To prove it, fix tau>0, set A_tau=A+tau I and Q=sqrt(A_tau), and use the norm-convergent functional-calculus commutator integral

 [X,Q]Q=(1/pi) integral_0^infinity
        t^(1/2)(A_tau+t)^(-1)[X,A](A_tau+t)^(-1)Q dt.  (A.2)

Since the spectrum of A_tau lies in [tau,C+tau], the norm of the integrand without [X,A] is bounded by

 t^(1/2)/tau^(3/2),            0<t<tau,
 1/(2t),                       tau<=t<=C+tau,
 sqrt(C+tau)t^(-3/2),           t>C+tau.

For the middle estimate use sup_(lambda>0)sqrt(lambda)/(lambda+t)=1/(2sqrt(t)). Integrating the three ranges proves

 ||[X,Q]Q||<=(K/pi)[8/3+(1/2)log(1+C/tau)].           (A.3)

The identity

 X A_tau=Q X Q+[X,Q]Q

and positivity of QXQ imply

 -Re<v,XA v><=tau+(K/pi)[8/3+(1/2)log(1+C/tau)].

Take tau=K and use pi>3. This gives (A.1). When the actual commutator is smaller than the chosen explicit K, the same calculation remains valid with that upper bound. No computability or spectral gap of A is assumed, and a kernel of A causes no difficulty because the regularization is used only inside the proof.

### A.2. Application on the same original domain

In this appendix use the explicit upper bounds M=2 and C=41, and keep the unchanged actual P=1_(-infinity,0](H). Sections 1–2 of this report prove that A=-H restricted to range(P) is bounded in [0,C], that X=P chi^2 P lies in [0,I], and that q=chi^2 preserves D(H) with [A,X]=-P[H,q]P. Retain m_tail and mu from equation (1) of the main report, and set

 c_bar(N)=8+4sqrt(N)log N,
 delta_bar(N)=(980/9)(N+1)^2 exp[-pi(N+1)],
 K(R,s,N)=M m_tail(R)[c_bar(N)+36/s]+2delta_bar(N),
 h(R,s,N)=M m_tail(R)[c_bar(N)+72/s^2]+delta_bar(N),
 L(R,s)=2C/mu(R+s)+18M/s.

The original weighted commutator (main equations (9)–(11)) is bounded by this K: both theta factors, the first Gamma jump moment and the full omitted-prime norm tail remain present. The new lemma therefore gives, for every unit v in range(P),

 Re<qv,Hv><=R_C(K(R,s,N)).                            (A.4)

Use f=mv and g=(1-chi)f. The already proved domain-safe localization and local regularity in Section 4 give, with only its mixed term replaced,

 b[chi f]<=h(R,s,N)+R_C(K(R,s,N)),                    (A.5)
 g in D(b(D)), ||g||<=M, ||b(D)g||<=L(R,s).           (A.6)

In particular, global unweighted b(D)f in L2 is not assumed: (A.6) follows from the local original equation b(D)f=m^(-1)Bv, ||Bv||<=2C, and the bounded compact-multiplier commutator. The full weighted IMS error is still 72M m_tail(R)/s^2. Section 5's exact source-frequency split now becomes

 beta_J[mv]<=2M^2 beta_J(T)+2L(R,s)^2/b(T)
                 +2h(R,s,N)+2R_C(K(R,s,N)).          (A.7)

The unchanged scalar estimates are beta_J(T)<=3T^2/(8J^2), 0<=beta_J<=b and b(T)>=log(1+4T^2)/2. These statements cover all mixed spectral vectors in range(P). P is not computed or replaced.

### A.3. Sharper polynomial prefactors in the exterior budget

Put y=exp(2R)>=2, s=1/y, and choose an integer N with

 y<=N<=y+2.

Such an integer can be found by interval bounds without an exact ceiling-equality test. Since log N<=sqrt(N),

 c_bar(N)<=8+4N<=4y+16<=12y.                         (A.8)

Writing E_y=exp(-pi y/2), one also has

 delta_bar(N)<=2y^2 E_y.                             (A.9)

Indeed N+1>=y+1 and N+1<=y+3<=(5/2)y, so the ratio of the left side to y^2 E_y is at most

 (6125/9)exp[-pi(y/2+1)]<2, y>=2.

The last ratio decreases with y, and at y=2 the comparison follows from exp(2pi)>exp(6)>(8/3)^6>6125/18.

Equations (A.8)-(A.9) give

 K(R,s,N)<=676y^2E_y<700y^2E_y=:K_bar,
 h(R,s,N)<=1008y^3E_y+170y^2E_y<=1093y^3E_y
                                             <1100y^3E_y. (A.10)

Apply the operator lemma directly with the upper commutator bound K_bar. Since K_bar>=E_y and C=41,

 log(1+C/K_bar)<=log(42)+pi y/2<4+2y<=4y.

Thus

 R_C(K_bar)<=700y^2E_y(2+2y/3)<1200y^3E_y,
 2h+2R_C(K_bar)<4600y^3E_y.                         (A.11)

The mixed spectral term now has the same y^3E_y scale as the weighted Gamma localization error.

### A.4. Explicit joint cutoff and its improved growth order

Fix 0<eta<=exp(-1), put ell=log(1/eta), and choose

 y=(2/pi)[ell+3log(ell+2)+40],
 R=(1/2)log y, s=1/y,
 y<=N<=y+2, N an integer.                           (A.12)

Then R>=1, y>=2, and

 (2/pi)(ell+2)<=y<12(ell+2),
 E_y=eta exp(-40)(ell+2)^(-3).

For the upper bound use log(ell+2)<=ell+2 and
ell+3log(ell+2)+40<=4ell+46<=17(ell+2). Therefore (A.11) gives

 2h+2R_C(K_bar)<4600*12^3exp(-40)eta<eta/3.           (A.13)

The last comparison is purely elementary:
13800*12^3=23846400<2^25<exp(40).

Let L_*=L(R,s) as in (A.6), and choose

 T=exp(6L_*^2/eta+1),
 J=ceil(4T/sqrt(eta)).                               (A.14)

Equivalently, choose any interval-certified integer J between 4T/sqrt(eta) and 5T/sqrt(eta); this interval is sufficiently long. The same two source estimates as before give

 2L_*^2/b(T)<eta/3,
 2M^2 beta_J(T)<=3eta/16<eta/3.

Combining these with (A.7) and (A.13), uniformly on the entire original nonpositive spectral subspace,

 ||sqrt(beta_J)(D)mP||^2<eta.                         (A.15)

Finally set

 K0=(8C^2/9)exp(4pi)+648M^2,
 C_sharp=(3pi^2 K0/2)exp(80)+4.

The elementary estimates exp(2/y)<=1+4/y and y^4<=exp(pi y), y>=2, imply

 L_*^2<=K0 y^(-2)exp(pi y)
      <=(K0 pi^2/4)exp(80)eta^(-2)(ell+2)^4.

Since J<=5T/sqrt(eta),

 log J<=C_sharp eta^(-3)(ell+2)^4.                   (A.16)

Every constant is explicit; C=41 and M=2 were fixed throughout. The construction is uniform over arbitrary superpositions of distinct nonpositive spectral values and kernel vectors. It matches the eta-power and logarithmic order of the earlier individual-eigenvector bound, without computing P.

### A.5. What changes, and what does not

The new ingredient is (A.1), a K log(1/K) control of the unfavorable mixed spectral product. The old square-root estimate and eta^(-5) cutoff were valid but less efficient. The present result strengthens their rate without changing H, its domain, the complete prime operator, the theta multiplier, or the unknown spectral subspace.

This is still only a sufficient complete-Gamma-tail cutoff. It does not construct P, prove that any comparison has the correct inertia, make the pure prime-edge shorted residual disappear, establish critical complementary positivity, or prove RH. Those separate sign questions remain open.
