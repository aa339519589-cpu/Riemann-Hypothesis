# Effective complete-Gamma tails for actual nonpositive eigenstates

For every 0<eta<=exp(-1), this theorem gives an explicit integer J(eta) such that

    beta_J[mv]<eta,   beta_J=b-b_J,

for EVERY normalized actual eigenvector Hv=lambda v with lambda<=0 of the original even theta/Gamma/complete-prime operator. The choice is uniform in the eigenvector and the depth of its eigenvalue. All constants are explicit, with

    log J(eta)<=C_Gamma eta^(-3)(log(1/eta)+2)^4.

The constructive proof is Part A. Part B separately proves qualitative uniform convergence on the entire genuine nonpositive spectral subspace. The effective rate in Part A is claimed only for eigenvectors or a single eigenspace; it is not asserted for arbitrary superpositions of different eigenvalues or for an expectation-energy cone.

This controls the omitted Gamma energy. The complete-prime edge defect after shorting and the remaining critical sign are still not estimated. The certified original gap 511/1024 is unchanged, and no zeta zero is excluded.

## Original normalization, necessary bounds, and attribution

The original closed realization is the user's [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). Work on complex even L2(R,dx), with Fourier transform fhat(t)=integral f(x)exp(-itx)dx and Plancherel measure dt/(2pi). The complete theta kernel, extended by its theta evenness, is

    Phi(x)=sum_(n>=1)[4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2)]
                              exp[-pi n^2 exp(2x)]  (x>=0),
    m(x)^2=Phi(x)/(2cosh(x/2)),
    b(t)=Re psi(1/4+it/2)-psi(1/4),
    C0=-psi(1/4)+log pi,  alpha_n=Lambda(n)/sqrt(n),
    B=M_m b(D)M_m,
    V=C0 m^2+sum_(n>=2)alpha_n M_m(tau_(log n)+tau_(-log n))M_m,
    H=B-V,   tau_d f(x)=f(x+d).

B is defined by its closed associated form b[mv]; its operator domain does not require global unweighted b(D)(mv) in L2. V is bounded and selfadjoint, so D(H)=D(B). The full original jump operator is H+I/2. Its constant direction becomes the normalized ground g0=Phi/m. The proofs below use the full even space; any actual eigenvector in the original mean-zero space is included.

For completeness, the scalar bounds inherited from [REPORT.md, Sections 1.1–1.2](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_adaptive_spectral_tail/REPORT.md) have a short direct verification. Put Astar=4pi^2(125/121)<49. Retaining the first positive theta term, and bounding the remaining positive series by a geometric majorant, gives

    (2pi^2-3pi) exp(4|x|-pi exp(2|x|))<=m(x)^2
                  <=Astar exp(4|x|-pi exp(2|x|)),

where 2pi^2-3pi>9. For the upper bound use n^4<=16^(n-1), n^2-1>=3(n-1), and 16exp(-9)<1/500. These estimates retain the full theta sum.

For d=log n, set r=exp(2|x|), s=exp(2|x+d|). Then rs>=n^2, r+s>=2sqrt(rs), and the decreasing function t^2 exp(-pi t), t>=1, give

    sup_x m(x)m(x+d)<=Astar n^2 exp(-pi n).

Thus, if V_N retains all n<=N shifts and the unchanged C0 m^2, then

    ||V-V_N||<=2Astar sum_(n>N)log(n)n^(3/2)exp(-pi n)
              <=(20Astar/9)(N+1)^2 exp[-pi(N+1)]=delta_N.

Indeed log n<=sqrt(n), and successive n^2 exp(-pi n) terms for n>=3 have ratio below 1/10. This proves the complete-prime norm tail used in both parts, without removing primes from the actual H. The exact value psi(1/4)=-EulerGamma-pi/2-3log 2 gives C0=EulerGamma+pi/2+3log 2+log pi, and hence 0<C0<8.

The user's [quantitative prime-two Gamma-depth theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_fixed_shortening_essential_band/QUANTITATIVE_PRIME_TWO_GAMMA_DEPTH.md) gives a necessary depth for its selected-space finite-prime lower comparator. The cutoff below is sufficient only for approximation of Gamma energy on genuine nonpositive eigenstates. It is not a sufficient depth for that comparator or a reversal of the user's obstruction. The full-prime/full-kernel fixed-J obstruction in [FIXED_GAMMA_FULL_KERNEL_BARRIER.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md) likewise remains valid: here J grows with the requested accuracy.

Both proofs and their exact domain restrictions have an [independent mathematical review](REFEREE_EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md). No numerical spectral certificate or experimental code is an input to this result.

## Part A. Constructive cutoff, uniform over actual nonpositive eigenstates

### 1. Original operators and scalar bounds

Use the actual even Hilbert space and its closed realization H=B-V, B=M_m b(D)M_m, D(H)=D(B). The complete weighted prime operator V is unchanged. Retain the proved theta bounds

 9 exp(4|x|-pi exp(2|x|)) <= m(x)^2
 <= Astar exp(4|x|-pi exp(2|x|)),  Astar<49.

The exponent decreases for x>=0. Thus M=2 bounds ||m||_infinity, and for r>=0 define

 m_tail(r)=7 exp(2r-(pi/2)exp(2r)),
 mu(r)=3 exp(2r-(pi/2)exp(2r)).                          (1)

Then m_tail(r)>=sup_(|x|>=r)m(x) and mu(r)<=inf_(|x|<=r)m(x). For integers N>=2 put

 c_N=C0+2 sum_(2<=n<=N) alpha_n,
 delta_N=(20 Astar/9)(N+1)^2 exp[-pi(N+1)],
 C=M^2 c_2+delta_2.

The established full-prime norm tail gives ||V-V_N||<=delta_N and ||V||<=C. In particular every actual eigenvalue lambda<=0 lies in [-C,0]. Elementary bounds C0<8, alpha_n<=log(n)/sqrt(n) imply

 c_N <= C0+4 sqrt(N)log N.                             (2)

The exact Gamma jump kernel is

 k(y)=sum_(j>=0)exp[-(2j+1/2)|y|]
     =exp(-|y|/2)/(1-exp(-2|y|)), y!=0,

with energy

 b[f]=(1/2) integral integral k(y)|f(x+y)-f(x)|^2 dxdy.  (3)

This follows from the finite Gamma convolution identity and monotone convergence. Direct integration and a first-term-plus-integral bound give

 M1:=integral |y|k(y)dy=(1/2)sum_(j>=0)(j+1/4)^(-2)<9,
 M2:=integral y^2k(y)dy=(1/2)sum_(j>=0)(j+1/4)^(-3)<36. (4)

The same decreasing-series comparison yields

 b(T)>=(1/2)log(1+4T^2).                               (5)

Indeed integrate T^2/[a(4a^2+T^2)] over a>=1/4.

### 2. Domain-safe localization, retaining the true theta weight

For a real bounded Lipschitz chi with Lipschitz constant L,

 ||[b(D),chi]||_(L2->L2) <= L M1.                       (6)

The kernel contains k(y)(chi(x)-chi(x+y)); its modulus is bounded by L|y|k(y), which is integrable. Young's inequality proves (6), first on smooth sources and then by density.

For f in Q(b), multiplication by chi preserves Q(b), and the exact jump identity gives

 b[chi f]=Re b(chi^2 f,f)+E_chi[f],
 E_chi[f]=(1/2) integral integral k(y)
       (chi(x+y)-chi(x))^2 Re(conjugate(f(x+y))f(x)) dxdy. (7)

The form convention is conjugate-linear in the first argument. The error integral is absolutely bounded by (M2 L^2/2)||f||^2. Consequently (7) passes from finite jump kernels and smooth sources to the stated form domain; global unweighted b(D)f in L2 is not assumed.

Fix R>=1 and 0<s<=1. Choose smooth even chi=chi_(R,s) with 0<=chi<=1, chi=0 on |x|<=R, chi=1 on |x|>=R+s, and Lip(chi)<=2/s. Let theta=1-chi. If chi(x+y)-chi(x) is nonzero, at least one of x,x+y has absolute value greater than R. Thus

 m(x)m(x+y)<=M m_tail(R)

on the support of the error kernel. Applying Young's inequality directly to v, rather than discarding its theta factors and estimating f=mv, proves

 |E_chi[mv]| <= (2 M2 M/s^2) m_tail(R)||v||^2
              <=(72 M/s^2) m_tail(R)||v||^2.            (8)

This weighted localization remainder is the useful improvement over a bare inverse-width-squared estimate.

### 3. Exterior Gamma energy of a true nonpositive eigenvector

Suppose Hv=lambda v, lambda<=0, ||v||=1, and f=mv. The test chi^2 v is in Q(B), because its source is chi^2 f. The original eigenvalue equation and (7) give

 b[chi f]=Re<chi^2 v,Vv>+lambda||chi v||^2+E_chi[f].

The eigenvalue term is nonpositive. The actual complete prime norm tail and the left theta multiplier imply, for any N>=2,

 ||chi V|| <=M m_tail(R)c_N+delta_N.

Therefore the explicit bound is

 b[chi f] <= h(R,s,N),
 h(R,s,N):=M m_tail(R)[c_N+72/s^2]+delta_N.              (9)

No prime has been removed from H. The delta term merely bounds a complete tail within this estimate. The favorable sign lambda||chi v||^2 is used only for a genuine eigenvector, not for arbitrary spectral superpositions or an expectation-energy cone.

### 4. Interior Gamma regularity from the original eigen-equation

The associated-form equation implies on compact intervals, in distributions,

 b(D)f=m^(-1)Bv=m^(-1)(Vv+lambda v).                    (10)

The right side is locally L2 because m is smooth positive. For g=theta f, the compact support of theta and (6) give a globally L2 expression

 b(D)g=theta m^(-1)Bv+[b(D),theta]f.

Thus g really belongs to D(b(D)), with

 ||g||<=M,
 ||b(D)g||<=2C/mu(R+s)+18M/s=:L(R,s).                  (11)

Here ||Bv||<=||Vv||+|lambda|<=2C. This proves the needed regularity instead of presupposing global b(D)f in L2.

### 5. Uniform complete-Gamma tail ledger

For beta_J=b-b_J and T>0, monotonicity gives

 beta_J[g] <= beta_J(T)||g||^2 + ||b(D)g||^2/b(T).

Since 0<=beta_J<=b and f=g+chi f, (9)-(11) prove

 beta_J[mv] <=2M^2 beta_J(T)+2L(R,s)^2/b(T)+2h(R,s,N).  (12)

This is uniform in every normalized actual eigenvector with lambda<=0 and in its eigenvalue depth. Also

 beta_J(T) <= (T^2/4)[(J+1/4)^(-3)
                             +(1/2)(J+1/4)^(-2)]
             <=3T^2/(8J^2), J>=1.                     (13)

The first inequality is the decreasing-series estimate for the tail of (j+1/4)^(-3).

### 6. Fully explicit joint selection and its growth order

Fix 0<eta<=exp(-1), set ell=log(1/eta), and define

 y=(2/pi)[ell+3log(ell+2)+40],
 R=(1/2)log y, s=1/y, N=ceil(y).                       (14)

These choices satisfy R>=1, y>=2, N>=2. From (2), log N<=sqrt N, N<=y+1 and C0<8 one gets c_N<=8y^2. Using (1) and (9),

 h(R,s,N)<=1200 y^3 exp(-pi y/2).                      (15)

Here the first term is at most 1120 y^3 exp(-pi y/2). The prime tail contributes at most one further copy: since N+1>=y+1, N+1<=y+2<=2y,

 delta_N <=(3920/9)y^2 exp[-pi(y+1)]
          <=y^3 exp(-pi y/2), y>=2.

For the last inequality it suffices to check the decreasing ratio at y=2. The slack constant 1200 in (15) is convenient.

Now y<47(ell+2), and exp(-pi y/2)=eta exp(-40)(ell+2)^(-3). Therefore

 2h(R,s,N) <=2400*47^3 exp(-40) eta <eta/3.             (16)

For example 7200*47^3<10^9<2^40<exp(40), so the strict last comparison is elementary.

Set L_*=L(R,s) using its explicit value (11), then choose

 T=exp(6 L_*^2/eta+1),
 J=ceil(4T/sqrt(eta)).                                 (17)

Equation (5) gives 2L_*^2/b(T)<eta/3, while M=2 and (13) give 2M^2 beta_J(T)<=3eta/16<eta/3. Combining with (12) and (16) proves the actual uniform bound

 beta_J[mv]<eta                                        (18)

for every normalized original eigenvector with lambda<=0.

Although enormous, the cutoff in (17) has a stated finite growth order. Because y>=2, exp(2/y)<=1+4/y and hence

 mu(R+s)^(-2) <=(1/9)y^(-2)exp[pi(y+4)].

It follows that

 L_*^2 <=K y^(-2) exp(pi y),
 K=(8 C^2/9)exp(4pi)+648 M^2.                          (19)

To absorb the second squared term use y^4<=exp(pi y), y>=2. Also y>=(2/pi)(ell+2) and exp(pi y)=exp(80) eta^(-2)(ell+2)^6. Thus

 L_*^2 <=(K pi^2/4)exp(80) eta^(-2)(ell+2)^4,
 log J <=C_Gamma eta^(-3)(ell+2)^4,
 C_Gamma=(3pi^2 K/2)exp(80)+4.                         (20)

For the last line, J<=5T/sqrt eta and the additive 1+(ell/2)+log5 are absorbed by 4 eta^(-3)(ell+2)^4. All constants are explicit. Arithmetic with these quantities can be performed through their logarithms; constructing the colossal integer J is unnecessary for the mathematical statement.

### 7. Exact scope at criticality

The result is an effective Gamma-tail budget for an unknown hypothetical negative eigenvector, independent of its depth. Part B below controls the whole nonpositive spectral subspace qualitatively, while (18)-(20) are only claimed for individual eigenvectors or a single eigenspace. No norm estimate on arbitrary superpositions of different eigenvalues is inferred.

This gives one honest input for J(epsilon) constructions: the omitted Gamma form on an actual negative state can be made smaller than epsilon with an explicit cutoff. It does not estimate the full-prime edge defect after shorting, establish a complementary sign, or prove a successful all-depth inertia test. The sufficient bound here is for Gamma approximation alone. It is not a sufficient Gamma-depth prescription for the user's selected-frame comparison, whose quantitative necessary depth condition has a different scope and remains the user's result.


## Part B. Qualitative uniform tail on the entire genuine nonpositive spectral subspace

### 1. Original operators

Work on the original even Hilbert space with its closed form realization

 H=B-V,  B=M_m b(D)M_m>=0,
 b(t)=Re psi(1/4+it/2)-psi(1/4),
 V=C0 m^2 + sum_(n>=2) alpha_n m(tau_(log n)+tau_(-log n))m.

Here m is the true positive theta multiplier, m belongs to L2 intersect L-infinity, b is nonnegative, even, increasing in |t| and tends to infinity. V is bounded selfadjoint. Its original finite-prime operators V_N satisfy V_N -> V in operator norm; one already established explicit bound is

 ||V-V_N|| <= (20 Astar/9)(N+1)^2 exp[-pi(N+1)].          (1)

All zeros, theta jets and their possible completeness are irrelevant to the proof below.

Let

 P=1_(-infinity,0](H).

Since H>=-||V||, the interval defining P has bounded intersection with the spectrum. Consequently P maps the full Hilbert space boundedly into D(H)=D(B), and HP is bounded. For v in range(P), the original form identity gives

 0<=B[v]=H[v]+<v,Vv><=<v,Vv><=||V||||v||^2.            (2)

This uses the actual spectral inequality H|range(P)<=0. It is not inferred from one expectation bound on one vector.

### 2. Compact source and compact Gamma energy

For the full Fourier projection Q_T to |t|<=T, (2) gives

 ||(I-Q_T)mP||^2 <= ||V||/b(T).                         (3)

The operator Q_T m on full L2 is Hilbert--Schmidt, with squared norm

 ||Q_T m||_HS^2=(T/pi)||m||_2^2.

Restriction to the even space or composition with P can only decrease this bound. Thus mP is compact.

For fixed N every summand of V_NP is a bounded operator times mP, so V_NP is compact. Equation (1) then proves VP compact, without requiring the unweighted infinite shift S to be bounded. In particular

 K=PVP|range(P)

is compact, selfadjoint and nonnegative, by (2). The bounded positive operator

 C=PBP|range(P)

is well-defined either by BP bounded or its bounded restricted form. Equation (2) says 0<=C<=K. Hence C is compact. One elementary proof uses finite-rank spectral projections E_r of K. Positivity and Cauchy--Schwarz give

 ||C-E_r C E_r|| <= ||(I-E_r)C(I-E_r)||
                  +2 sqrt(||C|| ||(I-E_r)C(I-E_r)||),

and the right side tends to zero because the diagonal remainder is at most ||(I-E_r)K(I-E_r)||.

Define the genuine Gamma energy map

 T=sqrt(b)(D) M_m

on Q(B), so T*T=B in the closed-form sense. Then TP is bounded and

 (TP)*(TP)=PBP.

Compactness of this positive Gram proves that TP is compact. Equivalently B^(1/2)P is compact. This last conclusion is stronger than compactness of mP; it controls the complete original Gamma energy, not only the source L2 norm.

### 3. Uniform disappearance of a growing Gamma tail

For an integer J>=1 set

 b_J(t)=sum_(0<=j<J) t^2/[(j+1/4)(4(j+1/4)^2+t^2)],
 beta_J=b-b_J.

Define a bounded measurable multiplier

 r_J(t)=sqrt(beta_J(t)/b(t)) for t!=0, r_J(0)=0.

For every real t, 0<=r_J(t)<=1 and r_J(t)->0 as J->infinity. Dominated convergence proves r_J(D)->0 strongly on source L2. A uniformly bounded strongly convergent family converges uniformly after composition with a compact operator. Applying this to TP proves

 eta_J := ||sqrt(beta_J)(D)mP||^2
        = ||r_J(D)TP||^2 -> 0.                         (4)

Thus a single J controls every normalized vector in the genuine nonpositive spectral subspace at once. In particular it controls any hypothetical sequence of actual negative eigenvectors with eigenvalues approaching zero. No relation to the eigenvalue depth epsilon is required for this qualitative statement.

For reference, on a fixed source frequency band |t|<=T one has the elementary explicit bound

 beta_J(t) <= (t^2/4)[(J+1/4)^(-3)+(1/2)(J+1/4)^(-2)], (5)

obtained by bounding the decreasing series sum_(j>=J)(j+1/4)^(-3) by its first term plus its integral. The unresolved issue in making (4) effective is the compact energy-image tail of TP, not the elementary fixed-band Gamma remainder.

### 4. Scope and remaining sign

Let P_* be the spectral subprojection of P orthogonal to the known ground vector. The already verified finite gap bound constrains the spectrum of HP_* on range(P_*) to [-1/1024,0]. The subspace still contains the known infinite-dimensional kernel, so P_* is not zero. Equations (3)-(4) also hold with P_* in place of P; they do not exclude any remaining strictly negative spectrum. All constants and convergence assertions retain their original domains.

The residual after retaining the whole Gamma symbol in the full-prime diagonal comparison is still the genuine prime-edge form

 e[v]=sum_(n>=2) alpha_n integral m(x)m(x+log n)
                             |v(x+log n)-v(x)|^2 dx.

It is not bounded by eta_J in (4), and shorting that residual against known or full kernel vectors requires a separate argument. No sign for the complementary block has been obtained.

The distinction between a spectral subspace and an energy cone is essential. A negative direction can compensate a small-norm high-frequency positive direction in an expectation inequality; those mixed vectors need not belong to range(P). Therefore (4) does not contradict the previously proved failures of uniform residual disappearance on fixed energy balls.

This result isolates a valid low-state compactness input for a joint J(epsilon) construction. It is qualitative and depends on the actual unknown spectral projection. It cannot, by itself, certify a cutoff or the critical positivity inequality.
