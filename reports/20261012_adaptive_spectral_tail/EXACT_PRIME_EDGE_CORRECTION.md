# Computable finite-rank corrections below the complete prime-edge operator

For every rational 0<epsilon<=1, this theorem constructs an explicit positive finite-rank operator Fhat from even spatial cells, the original theta function, finitely many prime powers and a certified rational inverse Gram matrix. It satisfies the exact global operator order

    0<=Fhat<=E,

where E is the complete positive prime-edge operator of the original H. Its positive residual has the full form-domain bound

    0<=<v,(E-Fhat)v>
      <=epsilon max{||v||^2,B[v]/41}.

In particular, 0<=P(E-Fhat)P<=epsilon P for the true P=1_(-infinity,0](H). Neither the construction nor its terminating scalar prescriptions require computing P. All omitted primes and the inverse-Gram rounding are paid in the displayed residual.

The resulting globally ordered comparator

    Lhat=B-C0m^2-M_p+Fhat<=H

retains the complete Gamma coefficient and complete prime diagonal p, without a scalar penalty. The explicit positive Gram lower bound comes from the actual prime-two edge. This is a finite construction and error theorem, not a numerical inertia certificate. Every fixed finite-rank comparator here still has infinite negative index on the known threshold kernel, as proved in Section 7. The central sign remains unresolved; the original certified gap 511/1024 and the status of zero exclusion are unchanged.

## Original inputs, complete tails and attribution

The original closed realization is the user's [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). The full theta normalization and scalar estimates are proved in the [effective Gamma-tail report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261012_adaptive_spectral_tail/EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md). Explicitly, on the complex even L2(dx) space,

    Phi(x)=sum_(n>=1)[4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2)]
                              exp[-pi n^2 exp(2x)]  (x>=0),
    m^2=Phi/(2cosh(x/2)),
    b(t)=Re psi(1/4+it/2)-psi(1/4),
    C0=EulerGamma+pi/2+3log 2+log pi,
    alpha_n=Lambda(n)/sqrt(n).

Phi has its genuine even extension. The Fourier transform is integral f(x)exp(-itx)dx, with Plancherel measure dt/(2pi). B is the operator of the closed associated form b[mv]; its domain does not impose a global unweighted b(D)(mv) condition. H=B-V has D(H)=D(B). The bounds

    9exp(4|x|-pi exp(2|x|))<=m(x)^2
        <=49exp(4|x|-pi exp(2|x|)),
    0<C0<8, ||m||_infinity<2,
    b(T)>=(1/2)log(1+4T^2)

keep the whole theta and Gamma series. Appendix A below includes the complete-prime row-tail proof needed for the new correction, rather than assuming that an operator tail automatically bounds a diagonal tail. It also proves the constants ||E||<18 and ||V||<41 used by the construction.

The user's [true boundary-frame theorem, Sections 1 and 3](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261012_theta_boundary_frame/REPORT.md) supplies the known infinite-dimensional subspace of ker H used only for the limitation in Section 7. No completeness of that frame is assumed. The positive Gram shorting identity is classical linear algebra; the content here is its explicit original-domain columns, prime-two inverse bound, complete-prime residual and order-safe computable realization for this operator.

The separately proved [effective entire-spectral-span Gamma tail](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/c2207e8e73bdfdcac47a4c786418f50c49b901a8/reports/20261012_adaptive_spectral_tail/EFFECTIVE_GAMMA_FULL_SPECTRAL_TAIL.md) concerns the Gamma remainder on P. It is not used to assume the sign of the prime-edge core. The [independent review](REFEREE_EXACT_PRIME_EDGE_CORRECTION.md) covers all the construction and its domain and threshold restrictions. No experimental code or floating-point matrix is a proof input.

## 1. Original objects and the retained reconstruction estimate

Work on the original even Hilbert space, with

 H=B-V, B=m b(D)m>=0, V=C0m^2+m S m,
 P=1_(-infinity,0](H).

Let E be the complete bounded positive prime-edge operator, with form

 e[v]=sum_(n>=2) alpha_n integral m(x)m(x+log n)
                         |v(x+log n)-v(x)|^2 dx,
 alpha_n=Lambda(n)/sqrt(n).

Its exact diagonal is p(x)=sum_(n>=2)alpha_n m(x)[m(x+log n)+m(x-log n)], so

 H=B-C0m^2-M_p+E.                                     (1)

All complete-prime terms and the original theta multiplier are unchanged. We use the previously proved explicit bounds

 M=2, ||m||_infinity<=M, ||V||<=41, ||E||<18,
 m_tail(R)=7 exp(2R-(pi/2)exp(2R)),
 mu(R)=3 exp(2R-(pi/2)exp(2R)),
 inf_(|x|<=R)m(x)>=mu(R),
 b(T)>=(1/2)log(1+4T^2),
 delta_bar(N)=(980/9)(N+1)^2 exp[-pi(N+1)],
 c_bar(N)=8+4sqrt(N)log N.

For the finite-prime edge E_N and diagonal p_N,

 0<=E-E_N<=2M_(p-p_N),
 ||p-p_N||_infinity<=delta_bar(N),
 ||E-E_N||<=2delta_bar(N),
 p_out(R):=sup_(|x|>R)p(x)
 <=M m_tail(R)c_bar(N)+delta_bar(N).                   (2)

These are the full row-sum tail bounds, not a discarded-prime change to H.

Here is the explicit cell reconstruction that will be used. Fix a rational 0<epsilon<=1. Choose N>=2 and an integer R>=1 such that

 delta_bar(N)<epsilon^2/6400,
 M m_tail(R)c_bar(N)<epsilon^2/6400.

Put mu=mu(R), choose

 T=exp[41(80sqrt(18)/(mu epsilon))^2+1],
 L>=80sqrt(18)MTR/(pi mu epsilon),                     (3)

where L is any positive integer certified to exceed the real bound. Partition [-R,R] into 2L reflected cells I_j of length h=R/L, and put

 phi_j=h^(-1/2)1_(I_j),
 S_cell f=sum_(j=1)^(2L) phi_j<phi_j,f>,
 phi_j^+=(phi_j+phi_(2L+1-j))/sqrt(2), 1<=j<=L,
 psi_j=phi_j^+/m,
 Psi c=sum_(j=1)^L c_j psi_j,
 Z=m^(-1)S_cell m.

The coefficient inner product is conjugate-linear in its first argument. The phi_j^+ are an orthonormal even source-cell basis. All Psi columns are thus in the original even space. On even inputs S_cell is exactly projection onto their span, so Zv belongs to range(Psi).

For every v in Q(B) with ||v||<=1 and B[v]<=41,

 ||sqrt(E)(v-Zv)||<=rho<epsilon/20.                   (4)

For completeness, if f=mv and Q_T is the source Fourier projection, then

 ||(1-Q_T)f||<=sqrt(41/b(T)), ||(Q_Tf)'||<=TM.

Writing D_R=1_[-R,R], the difference D_R-S_cell is an orthogonal projection. Cell Poincare therefore gives

 ||D_Rf-S_cell f||<=sqrt(41/b(T))+hTM/pi=:a.

Since E<=2M_p and ||E||<18,

 rho=sqrt(2p_out(R))+sqrt(18)a/mu(R).

The parameter choices (3) make each summand less than epsilon/40, proving (4). Only ordinary L2 source estimates are used here; the sharp cells are not commuted through the Gamma operator.

## 2. Cell columns really lie in the original operator domain

Each source phi_j has Fourier transform

 phihat_j(t)=h^(-1/2)(exp(-it a_j)-exp(-it b_j))/(it),

with the continuous value at zero. In particular

 |phihat_j(t)|<=min(sqrt(h),2/(sqrt(h)|t|)).

The original Gamma series gives b(t)=O(log(2+|t|)): split the terms at j=ceil(|t|), bound the first group by the harmonic sum of (j+1/4)^(-1), and the remaining group by (t^2/4)sum(j+1/4)^(-3). It follows that integral b(t)^2|phihat_j(t)|^2dt is finite. Thus each single-cell phi_j belongs to the full-line domain D(b(D)), and its even combination phi_j^+ belongs to that domain in the original even space.

Since m is bounded and bounded away from zero on the cell support, psi_j belongs to original L2 and

 B psi_j=m b(D)phi_j^+ in L2.

The associated-form criterion therefore puts every psi_j in D(B)=D(H), not merely in an abstract source completion. Moreover

 ||Psi||<=1/mu(R),
 ||Psi c||>=||c||/M.                                 (5)

No inverse theta multiplier is used outside a compact interval.

## 3. An explicit positive Gram bound from prime 2

Put d=log 2 and alpha=log 2/sqrt(2)>1/4. Choose an integer K with Kd>2R. For any u supported in [-R,R], its translate by Kd has disjoint support. Telescoping the K unitary translations gives

 2||u||^2=||tau_(Kd)u-u||^2
             <=K^2||tau_d u-u||^2.

The support of the difference involves only endpoints in [-R-d,R+d], where both theta factors are at least mu(R+d). Therefore

 e_2[u]>=2alpha mu(R+d)^2||u||^2/K^2.

Combining this with (5), the finite Gram matrix

 G_Q=Psi* E_Q Psi, Q>=2,

satisfies the explicit uniform lower bound

 G_Q>=g_R I,
 g_R=mu(R+d)^2/(2K^2M^2)>0.                          (6)

The same lower bound holds for G=Psi*E Psi. This supplies a certified inverse bound ||G_Q^(-1)||<=1/g_R, independent of any unknown spectral projector or computed eigenvalue. In the even cell coordinates, the same estimate follows by restriction to an orthonormal coefficient subspace.

## 4. Exact finite-rank order and a complete-prime residual bound

Choose a further Q>=2 so

 delta_bar(Q)<epsilon/8.                             (7)

Define the finite-prime column map and its exact Gram correction by

 C_Q=E_Q Psi,
 F_Q=C_Q G_Q^(-1) C_Q*.

The operator F_Q is bounded, positive, finite rank, and

 0<=F_Q<=E_Q<=E.                                     (8)

Indeed, sqrt(E_Q)Psi has Gram G_Q; the middle operator
sqrt(E_Q)Psi G_Q^(-1)Psi*sqrt(E_Q) is the orthogonal projection onto its finite-dimensional range. Equivalently, for every original v,

 <v,(E_Q-F_Q)v>=inf_c e_Q[v-Psi c].                  (9)

Taking the specific cell reconstruction Zv in this variational formula and using (2),

 0<=<v,(E-F_Q)v>
 <=2delta_bar(Q)||v||^2+e[v-Zv].                     (10)

Thus for the full class ||v||<=1, B[v]<=41, equations (4) and (7) give

 <v,(E-F_Q)v><epsilon/4+epsilon^2/400.                (11)

In particular this estimate holds uniformly on the unit ball of range(P), since B[v]<=41||v||^2 there. Unlike simply substituting e_Q[Zv], the variational formula avoids multiplying the omitted-prime norm error by mu(R)^(-2).

## 5. Computability of all columns, the full-prime limit, and order-safe rational inversion

Every even column C_Q e_j is an explicit finite sum:

 E_Q psi_j=p_Q psi_j
       -sum_(2<=n<=Q)alpha_n m(x)
          [m(x+log n)psi_j(x+log n)
                     +m(x-log n)psi_j(x-log n)].      (12)

It is supported in [-R-log Q,R+log Q] and is square-integrable. It consists of known smooth theta factors and finitely many step functions. Its scalar products can be integrated by splitting at the finitely many cell endpoints and their translates. Uniform theta-series tails and the positive lower theta envelope on this compact set permit certified quadrature to arbitrary accuracy. The finite construction is therefore computable in the original Hilbert norm.

For clarity, even the complete E Psi columns have a fully paid norm approximation:

 ||E Psi-C_Q||<=2delta_bar(Q)/mu(R),
 ||Psi*E Psi-G_Q||<=2delta_bar(Q)/mu(R)^2.             (13)

Both follow directly from (2) and (5). Hence an alternative exact full-edge correction E Psi G^(-1)Psi*E is also computable. It is not needed for (8)-(11), where the finite-prime correction already sits below the actual complete edge. All omitted primes are retained in the residual (10).

The inverse in F_Q can be replaced by rational matrix data while preserving (8). Let delta>0 be rational and choose a rational Hermitian G_tilde on the even coefficient space such that

 ||G_tilde-G_Q||<=delta,
 delta<=epsilon mu(R)^2 g_R^2/2592.                 (14)

A positive rational delta below this explicit bound can be found by interval-enclosed scalar comparisons. Entrywise accuracy delta/L with Hermitian symmetry in the even L-dimensional basis suffices. Put

 G_plus=G_tilde+delta I,
 R_Q=G_plus^(-1),
 Fhat=C_Q R_Q C_Q*.

Then G_plus>=G_Q>=g_R I. Thus R_Q is a well-defined positive rational matrix and

 0<=Fhat<=F_Q<=E_Q<=E.                              (15)

Since 0<=G_plus-G_Q<=2delta I, the inverse identity and (6) imply

 ||G_Q^(-1)-R_Q||<=2delta/g_R^2.

Using ||C_Q||<=18/mu(R),

 0<=F_Q-Fhat,
 ||F_Q-Fhat||<=648delta/(mu(R)^2g_R^2)<=epsilon/4.    (16)

The finite column functions in (12) are retained by their exact computable theta formulas; an uncontrolled floating-point replacement of those columns is not part of the order claim. Formula (13) gives the explicit full-prime column error if that variant is used.

## 6. Final global comparison and actual low-state error

Let Rhat=E-Fhat. Combining (10)-(16),

 Rhat>=0,
 <v,Rhat v><epsilon/2+epsilon^2/400<epsilon
       when ||v||<=1 and B[v]<=41.                  (17)

By homogeneity, for all nonzero v in Q(B),

 0<=<v,Rhat v>
 <epsilon max{||v||^2,B[v]/41}
 <=epsilon(||v||^2+B[v]/41).                         (18)

At v=0 all terms vanish. In particular the actual spectral compression satisfies

 0<=P(E-Fhat)P<=epsilon P.                           (19)

Define the genuine globally ordered comparison

 Lhat_epsilon=B-C0m^2-M_p+Fhat.

Then

 Lhat_epsilon<=H,
 H-Lhat_epsilon=Rhat>=0.                             (20)

Both are selfadjoint on D(B) with form domain Q(B): the Gamma coefficient is exactly one, and all other terms are bounded selfadjoint. There is no added scalar penalty in Lhat_epsilon and no replacement of the complete Gamma symbol. On the true low-state subspace,

 HP-epsilon P<=P Lhat_epsilon P<=HP.                (21)

This is an explicit approximation with exact global order. It remains valid for any spectral subprojection of P.

## 7. Scope at the infinite threshold kernel

The range used for shorting here is the explicit compact cell space, not the true kernel and not an unknown spectral basis. Formula (20) is a valid comparison, but no critical positivity has been proved.

There is an exact reason not to mistake this finite-rank construction for a complete critical certificate. The actual known threshold kernel of H is infinite-dimensional. Intersect it with the finite-codimensional kernel of Fhat. On every nonzero vector in that intersection,

 Lhat_epsilon[v]=-e[v]<0.

The strict inequality follows already from prime 2: e_2[v]=0 would force v(x+log2)=v(x) almost everywhere, and a nonzero periodic function cannot belong to original L2(R). Therefore each fixed finite-rank comparison still has infinite negative index on the ground-perpendicular space, compatible with those negative values tending to zero as the correction is refined. The absence of a scalar penalty does not remove this separate threshold-kernel issue.

The useful conclusion is exact global order together with a computable, uniformly small residual on actual low states. Positive-depth or correctly restricted central-block applications may use that error budget. Their remaining inertia or complementary sign must still be established. No new zero exclusion or RH conclusion follows from this construction.

## Appendix A. The full-prime row tail and the scalar bounds

These elementary estimates are included to close the dependencies of Section 1. For d=log n, put r=exp(2|x|), s=exp(2|x+d|). Then rs>=n^2 and r+s>=2sqrt(rs). The two-sided theta upper envelope therefore gives

    m(x)m(x+d)<=49rs exp[-pi(r+s)/2]
                 <=49n^2 exp(-pi n),  n>=2,

because z^2 exp(-pi z) decreases for z>=n>=2. Moreover alpha_n<=log(n)/sqrt(n)<=1. For n>=3, successive terms n^2 exp(-pi n) have ratio at most (4/3)^2 exp(-pi)<1/10. Summing both shifts proves, for every integer N>=2,

    ||p-p_N||_infinity
      <=98 sum_(n>N)n^2exp(-pi n)
      <=(980/9)(N+1)^2exp[-pi(N+1)]=delta_bar(N).

Expansion of |v(x+d)-v(x)|^2 and the inequality |a-b|^2<=2|a|^2+2|b|^2 give the bounded positive even-space operators

    E=M_p-mSm, 0<=E<=2M_p,
    0<=E-E_N<=2M_(p-p_N),
    ||E-E_N||<=2delta_bar(N).

Thus no prime is removed from the actual H. Since alpha_2<1 and delta_bar(2)<1,

    ||p||_infinity<=2M^2alpha_2+delta_bar(2)<9,
    ||E||<18,
    ||V||<=M^2(C0+2alpha_2)+delta_bar(2)<41.

For |x|>R, the finite part is at most M m_tail(R) times 2 sum_(2<=n<=N)alpha_n. The elementary bound sum_(n<=N)n^(-1/2)<=2sqrt(N) therefore implies

    p_out(R)<=M m_tail(R)[8+4sqrt(N)log N]+delta_bar(N).

The added constant eight is harmless. These estimates prove all row, spatial and operator tails used in the parameter searches. They apply before any spectral compression and use no prime-number theorem.
