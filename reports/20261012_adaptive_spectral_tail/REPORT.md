# Sharp global source-resolvent growth and an adaptive full-operator norm tail

Status: independently reviewed mathematical result. This is a positive full-space error-control theorem for the unchanged original theta/Gamma/prime operator. It is not a spectral positivity certificate or an RH proof. No finite matrix is asserted to have passed a second-eigenvalue test.

## 1. Exact original operator, domains and complete prime tail

Work on the full even subspace of L2(R,dx), complexified when needed. The Fourier convention is fhat(t)=integral f(x)exp(itx)dx, with Plancherel measure dt/(2pi). Retain the complete original theta kernel

    Phi(x)=sum_(n>=1) (4pi²n⁴e^(9x/2)−6pi n²e^(5x/2))
                         exp(−pi n²e^(2x)),
    h(x)=cosh(x/2), p(x)=2Phi(x)h(x), dnu=p dx,
    Uq=sqrt(p)q, m=sqrt(Phi/(2h)).

The theta identity makes Phi even and strictly positive, and integral p=1. Thus U is the original unitary map, and mUq=Phi q. Let

    C0=EulerGamma+pi/2+3log 2+log pi>0,
    b(t)=Re psi(1/4+it/2)−psi(1/4),
    bform[v]=integral b(t)|hat(mv)(t)|² dt/(2pi),
    D(bform)={v in L2_even:mv in H_log},
    H_log={f:integral log(2+|t|)|fhat(t)|²dt<infinity}.

The nonnegative selfadjoint B is the associated operator of this closed form. The notation B=M_m b(D)M_m means this realization. Its operator domain consists of the form-domain v for which the distribution m b(D)(mv) is represented by an L2 vector. It does not assert that b(D)(mv) is in L2 for every v in D(B). Closedness follows from the boundedness of m and consistency of the L2 and H_log limits; even compact smooth functions are a form core by cutoffs and smoothing on compact sets where m is bounded above and below.

With tau_d f(x)=f(x+d), define the full bounded selfadjoint potential

    V=C0 M_(m²)+sum_(n>=2) alpha_n M_m(tau_(log n)+tau_(−log n))M_m,
    alpha_n=Lambda(n)/sqrt(n).

The exact original maximal jump operator has

    U L U^(-1)=1/2+B−V,    H=B−V,    D(H)=D(B).

This is the original theta/Gamma/prime operator identity. The corresponding nonnegative jump form is

    E(q)=1/2 integral integral Phi(x)Phi(y) k(x−y)|q(x)−q(y)|²dxdy
         +sum_(n>=2) alpha_n integral Phi(x)Phi(x+log n)
                                      |q(x)−q(x+log n)|²dx,
    k(a)=e^(−|a|/2)/(1−e^(−2|a|)).

Its domain is the maximal finite-energy domain in L2(nu). The original explicit-formula source identity, applied to the complete Phi, gives the displayed transformed operator; it does not require RH. The positive continuous jump kernel shows that E(q)=0 only for constant q. Thus the normalized original constant direction g0=sqrt(p) is the unique H eigenvector at −1/2. The original even mean-zero space is g0-perp. B and V separately need not preserve that space; all constructions below are on the full even space.

The source identity and the complete-domain identification are derived explicitly in [ORIGINAL_FORM_FOUNDATION.md](ORIGINAL_FORM_FOUNDATION.md). Its contour proof cancels zeta-zero poles algebraically before shifting and includes the two pole residues giving cosh(x/2); its core proof starts from the maximal finite-energy domain, retains every prime power, and identifies the two closed forms on a common compact smooth core. The identity is a quadratic-form identity on the full form domain, with the ordinary operator inner product used only on D(B). Separate analytic and domain reviews are supplied there.

[ESSENTIAL_SPECTRUM.md](ESSENTIAL_SPECTRUM.md) proves unconditionally that the full even operators have sigma_ess(B)=sigma_ess(H)=[0,infinity) and sigma_ess(L)=[1/2,infinity), using complete-prime relative compactness and even escaping Weyl packets. This confines the remaining critical problem to discrete negative eigenvalues of H on g0-perp; it does not exclude those eigenvalues.

### 1.1 Theta and symbol bounds

Put Astar=4pi²(125/121). The exact estimates needed below are

    pi² exp(4|x|−pi exp(2|x|)) <= m²(x)
                   <= Astar exp(4|x|−pi exp(2|x|)),
    (16/5)min(t²,1) <= b(t) <= 18t².                         (1)

Here is a direct check of these constants. For x>=0, every theta summand is positive. Its first summand is at least 2pi² exp(9x/2−pi e^(2x)), since pi>3. Dividing by 2h<=2e^(x/2) proves the lower bound. For the upper bound, use 2h>=e^(x/2) and omit the negative term of every summand. The normalized theta sum sum_n n⁴ exp[−pi(n²−1)e^(2x)] is at most 125/121: successive summands have ratio at most 16e^(−3pi)<4/125. Summing the geometric majorant proves the upper bound; evenness handles x<0.

The exact positive expansion is

    b(t)=sum_(j>=0) (t/2)²/
               [(j+1/4)((j+1/4)²+(t/2)²)].

Its j=0 term is 16t²/(1+4t²), which implies the lower bound in (1). For the upper bound, the j=0 inverse-cube denominator contributes 64, and the remaining inverse-cube sum is at most integral_0^infinity(x+1/4)^(-3)dx=8. Multiplication by t²/4 gives 18t². The exact b is even, strictly increasing for t>0, and b(t)=log(1+|t|)+O(1). No differential operator replaces it.

### 1.2 Every omitted prime power has an explicit operator error

For d=log n put r=e^(2|x|), s=e^(2|x+d|). Then rs>=n² and r+s>=2sqrt(rs). The theta bound and monotonicity of t²e^(−pi t) for t>=1 give

    sup_x m(x)m(x+d) <= Astar n²e^(−pi n).

Consequently, for N>=2,

    ||V−V_N|| <= 2Astar sum_(n>N) log n n^(3/2)e^(−pi n)
              <= (20Astar/9)(N+1)²e^(−pi(N+1))=:delta_N,

where V_N keeps exactly the n<=N shifts and the unchanged C0m². Indeed log n<=sqrt(n), and successive n²e^(−pi n) terms for n>=3 have ratio below 1/10. This proves norm convergence of the full weighted prime series and the asserted bound. It also gives

    m_tail(R):=sup_(|x|>R)m(x)
       <=sqrt(Astar)exp(2R−(pi/2)exp(2R)), R>=0,
    ||m||_infinity<=sqrt(Astar)e^(−pi/2).

### 1.3 The actual source inverse and its form domain

For 0<epsilon<1/2 define

    A_epsilon=B+epsilon,
    J_epsilon=M_m A_epsilon^(-1/2),
    S_epsilon=J_epsilon J_epsilon^*=M_m A_epsilon^(-1)M_m,
    K_epsilon=A_epsilon^(-1/2)V A_epsilon^(-1/2).

On source L2 use the closed form

    a_epsilon[f]=integral b(t)|fhat(t)|²dt/(2pi)
                  +epsilon integral |f(x)|²/m²(x)dx,
    D(a_epsilon)={f in H_log,even:f/m in L2}.

For a source f, write b[f]=integral b(t)|fhat(t)|²dt/(2pi); this is distinct from bform[v]=b[mv]. Its associated operator C_epsilon is coercive, since m is bounded, and

    S_epsilon=C_epsilon^(-1).

This identity is not formal bounded conjugation by the unbounded m^(-1). For g in L2 set v=A_epsilon^(-1)mg and f=mv. Testing the B+epsilon equation against phi/m for compact smooth phi gives a_epsilon[f,phi]=<g,phi>. The common compact smooth form core, obtained by spatial cutoffs in H_log and the weighted L2 term followed by local smoothing, extends this identity to the full form domain. Hence f=C_epsilon^(-1)g. This also supplies the usual inverse variational formula used below.

## 2. A global upper bound of order (log log(1/epsilon))²

Let

    L_epsilon=log(Astar/epsilon),
    R_epsilon=max{1, (1/2)log[(2/pi)L_epsilon]},
    M_epsilon=min{sqrt(Astar)e^(−pi/2)/sqrt(epsilon),
                  sqrt(10)R_epsilon}.                        (2)

Then on the ENTIRE source space,

    ||S_epsilon||<=10R_epsilon²,
    ||J_epsilon||<=M_epsilon.                                (3)

This does not require source-mass cancellation or the original mean-zero constraint.

### 2.1 The actual theta potential supplies an exterior anchor

For R=R_epsilon,

    epsilon/m²(x)>=1 for |x|>=R.                              (4)

Indeed t=(2/pi)L_epsilon>=1, and the theta envelope at exp(2R)=t gives

    m²(R)<=Astar t²e^(−pi t)
           =epsilon t²e^(−L_epsilon)<=epsilon.

The last inequality follows from

    sup_(L>0) [(2L/pi)²e^(−L)]=16/(pi²e²)<1.

The theta envelope is decreasing on [0,infinity), and increasing R to 1 if needed preserves (4).

### 2.2 A quantitative anchored one-dimensional estimate

For any g in H1(R), any R>=1, and x in [−R,R], average the estimate

    |g(x)|²<=2|g(y)|²+2(y−x)||g'||²

over y in [R,R+1], then integrate over x in [−R,R]. This gives

    ||g||²<=(4R+1)||g||_(|x|>R)²+(4R²+2R)||g'||².             (5)

In particular the weaker coefficient 4R(2R+1) would also suffice. The displayed sharper coefficient is obtained by integrating y−x, rather than replacing it by its maximum.

For f in the source form domain split it into the orthogonal Fourier pieces

    g=1_(|D|<=1)f,  h=f−g.

Write E=b[f] and P=epsilon integral |f|²/m². From (1) and (4),

    ||g'||²<=5E/16,  ||h||²<=5E/16,
    ||g||_(|x|>R)²<=2P+2||h||²<=2P+5E/8.

Using ||f||²=||g||²+||h||² and (5),

    ||f||² <= [(5/4)R²+(25/8)R+15/16]E+(8R+2)P
            <=10R²(E+P).                                    (6)

Both final coefficients are at most 10R² for R>=1. Thus C_epsilon>=1/(10R²), proving the first assertion in (3). The second follows from ||J_epsilon||²=||S_epsilon||, together with the earlier elementary bound ||J_epsilon||<=||m||_infinity/sqrt(epsilon).

## 3. Matching growth from an actual source trial

For sufficiently small epsilon, put

    r_epsilon=(1/2)log[log(1/epsilon)/(2pi)],
    chi(x)=cos(pi x/2) for |x|<=1, and zero otherwise,
    f_r(x)=r^(−1/2)chi(x/r).

This is a genuine even compact H1 source with ||f_r||=1 and ||f_r'||²=pi²/(4r²). For r=r_epsilon large enough, the actual lower theta bound in (1) gives m²>=2pi² sqrt(epsilon) on its support. Hence

    a_epsilon[f_r]<=18pi²/(4r²)+sqrt(epsilon)/(2pi²)
                  <=19pi²/(4r²)                             (7)

once the explicitly stated last inequality holds. The inverse variational formula gives

    ||S_epsilon||>=4r_epsilon²/(19pi²).                       (8)

Thus the upper bound (3) matches the true global order:

    ||S_epsilon|| is of order [log log(1/epsilon)]²
    as epsilon tends to zero.                                (9)

No uniform bound at epsilon=0 is claimed. The fixed-window cancellation results and the original-ground-state source constraint remain distinct from this global norm statement.

## 4. An explicit finite prime cutoff and an exact frequency cancellation

Let

    alpha_n=Lambda(n)/sqrt(n),
    C_N=C0 I+sum_(2<=n<=N) alpha_n(tau_(log n)+tau_(−log n)),
    c_N=C0+2sum_(2<=n<=N)alpha_n,
    V_N=M_m C_N M_m,
    delta_N=(20Astar/9)(N+1)²e^(−pi(N+1)).

The inherited full-prime operator bound is ||V−V_N||<=delta_N. All omitted prime powers are therefore retained through an explicit error, not dropped.

Define the even trapezoidal Fourier multiplier

    rho_T(t)=1                         if |t|<=T,
             2−|t|/T                  if T<|t|<2T,
             0                        if |t|>=2T,
    Q=rho_T(D).

It is a selfadjoint contraction and commutes EXACTLY with C_N. It need not be smooth in frequency. Put G=Q J_epsilon. Then

    ||J_epsilon^* C_N J_epsilon−G^*C_NG||<=c_N/b(T).           (10)

Indeed their difference is J_epsilon^* C_N(1−Q²)J_epsilon. The middle multiplier has modulus at most c_N, and vanishes on |t|<=T. The original source energy satisfies b[J_epsilon u]<=||u||². Consequently

    |<J_epsilon u,C_N(1−Q²)J_epsilon u>|
       <=c_N ||1_(|D|>T)J_epsilon u||²
       <=[c_N/b(T)]||u||².

The difference is selfadjoint, so this quadratic bound proves (10). Signed C_N is allowed. The crucial error has no cross term of size ||J_epsilon||/sqrt(b(T)).

## 5. Spatial leakage and cells without sacrificing the frequency gain

The convolution kernel of Q is explicit:

    k_T(x)=[cos(Tx)−cos(2Tx)]/(pi T x²),
    k_T(0)=3T/(2pi).

It is integrable, and for d>0,

    integral_(|x|>d)|k_T(x)|dx<=4/(pi T d).                  (11)

Fix R0>=0, d>0, R=R0+d. Let P_R multiply by 1_[-R,R]. Splitting the input source at R0, using Q as a contraction on the outer input, and applying Young's inequality to the inner-to-outer kernel yields

    ||(1−P_R)G||
      <=m_tail(R0)/sqrt(epsilon)+4M_epsilon/(pi T d),          (12)

where

    m_tail(R0)<=sqrt(Astar)exp(2R0−(pi/2)exp(2R0)).

For the leakage term, if |x|>R and |y|<=R0 then |x−y|>d, so the integral kernel is bounded by the corresponding tail in (11). No locality of a hard Fourier cutoff is assumed.

Let Pi be orthogonal projection onto n equal even cells on [−R,R], with Delta=R/n. Since G is band limited to |t|<=2T,

    ||(P_R−Pi)G||<=(Delta/pi)||(G)'||
                  <=2Delta T M_epsilon/pi.

Therefore the rank-at-most-n map F=Pi Q J_epsilon satisfies

    ||G−F||<=a_new,
    a_new=m_tail(R0)/sqrt(epsilon)
            +4M_epsilon/(pi T d)
            +2Delta T M_epsilon/pi.                          (13)

All three terms are actual full-source norms. The second is a paid spatial leakage; the earlier unwanted 1/sqrt(b(T)) term has not reappeared here.

## 6. Full original Birman–Schwinger operator norm certificate

Combining the full-prime tail, (10), and the signed product estimate with ||G||,||F||<=M_epsilon gives

    ||K_epsilon−F^* C_N F||<=tau_new,

    tau_new=delta_N/epsilon+c_N/b(T)
             +2c_N M_epsilon[
                 m_tail(R0)/sqrt(epsilon)
                 +4M_epsilon/(pi T d)
                 +2R T M_epsilon/(pi n)].                    (14)

This is an operator-norm bound on the ENTIRE original even Hilbert space. It controls all primes, the full Gamma symbol, the original theta weight, the frequency window, the spatial leakage, and the finite-cell approximation.

For any target eta>0, the following explicit choices suffice for tau_new<=eta:

    delta_N<=eta epsilon/4,
    b(T)>=4c_N/eta,
    m_tail(R0)<=eta sqrt(epsilon)/(12c_N M_epsilon),
    T d>=48c_N M_epsilon²/(pi eta),
    n>=24c_N R T M_epsilon²/(pi eta),   R=R0+d.                (15)

The prime and frequency terms each cost at most eta/4. Each of the three terms in brackets in (14) is at most eta/(12c_N M_epsilon), so their total product cost is at most eta/2.

All requirements can be imposed with d=1. The symbol requirement also has an explicit elementary inversion. From its exact positive expansion

    b(t)=sum_(j>=0) (t/2)²/
          [(j+1/4)((j+1/4)²+(t/2)²)],

comparison with the integral of its decreasing summand gives

    b(t)>=(1/2)log(1+4t²).                                   (16)

Thus it suffices to take

    T>=max{(1/2)sqrt(exp(8c_N/eta)−1),
            48c_N M_epsilon²/(pi eta)}.                      (17)

The choices of N and R0 use the monotone explicit exponential envelopes displayed above. The exact full source inverse is still present in F; (14) is not a claim that its finite resolvent Gram has already been computed.

## 7. An epsilon-dependent rank bound that survives the fixed-rank obstruction

Fix eta>0 and let epsilon tend to zero. Write L=log(1/epsilon). One can choose parameters in (15) with

    N=O_eta(L),
    c_N=O_eta(sqrt(L)log L),
    M_epsilon=O(log L),
    R0=O_eta(log L),  d=1,
    log T=O_eta(sqrt(L)log L),
    log n=O_eta(sqrt(L)log L).                                (18)

For c_N, no prime-density theorem is needed: Lambda(k)<=log k and sum_(k<=N)k^(−1/2)<=2sqrt(N) give c_N<=C0+4sqrt(N)log N. The theta tail makes the required R0 of logarithmic-logarithmic size. Equation (17) gives the frequency bound, and the remaining factors in n from (15) have logarithms O_eta(log L).

Consequently there exists an explicitly parameterized rank-n(epsilon) approximation in the original norm with

    ||K_epsilon−F_epsilon^* C_(N(epsilon))F_epsilon||<=eta,
    n(epsilon)<=exp[O_eta(sqrt(log(1/epsilon))log log(1/epsilon))]
               =epsilon^(−o(1)).                            (19)

This is a rank bound for the defined approximation, not a bound on the time or precision needed to rigorously evaluate its resolvent Gram. The rank tends to infinity, consistently with the already proved true-threshold obstruction to every fixed-rank critical approximation. Neither (14) nor (19) asserts that the finite signed matrix has second eigenvalue at most 1−eta.

## 8. The exact finite matrix and the signed spectral criterion

Let e_1,...,e_n be the normalized even-cell basis for Ran Pi. The nonzero spectrum of the finite-rank comparison F^* C_N F is exactly that of

    Z_cell=G_cell^(1/2) D G_cell^(1/2),
    D=Pi C_N Pi on Ran Pi,
    G_cell=F F^*=Pi Q S_epsilon Q Pi on Ran Pi.

This is the polar decomposition of F, so includes singular G_cell. D is signed; no positivity of C_N or V is assumed. The entries of D are finite weighted overlaps of shifted cells. The ACTUAL remaining Gram entries are

    (G_cell)_ij=<f_i,A_epsilon^(-1)f_j>,  f_i=m Q e_i.

They are not the already known finite jump-energy moments. Section 9 provides two-sided residual bounds for these exact inputs, without pretending they have already been numerically evaluated.

Write lambda_2^+(Z_cell) for the second largest eigenvalue after adjoining an infinite zero tail. The sufficient finite-depth condition is

    lambda_2^+(Z_cell)+tau_new<=1.                            (20)

It implies the original mean-zero form inequality

    E(q)>=(1/2−epsilon)||q||_nu²
    for every even q in the original form domain with nu(q)=0.

For completeness, (14) and min--max permit at most one eigenvalue of K_epsilon strictly above one when (20) holds. K_epsilon is compact: for fixed epsilon, (14)--(15) give finite-rank approximants with arbitrarily small error. The form identity

    H+epsilon=A_epsilon^(1/2)(I−K_epsilon)A_epsilon^(1/2)

is a congruence on the original form domain. A_epsilon^(-1/2) maps the full even Hilbert space bijectively onto that domain, so the negative index equals the number of K_epsilon eigenvalues above one. The known g0 eigenvector at −1/2 supplies one such direction for epsilon<1/2. If a second negative direction existed on g0-perp, it and g0 would contradict the index bound. Since g0-perp reduces H, the asserted form inequality follows. Equality at −epsilon is not excluded.

No matrix has been proved to satisfy (20) here. A certificate at one positive epsilon excludes only that depth; a critical result would require actual valid certificates at depths tending to zero or a further structural argument. The adaptive rank bound is not a numerical spectral certificate.

## 9. A domain-safe two-sided computation of the actual Gram

### 9.1 A genuine operator core

Even C_c-infinity vectors form an OPERATOR graph core for B, not merely an L2 or form-dense family. The exact jump multiplier is

    b(D)f=integral k(a)[f(x)−f(x+a)]da,
    integral |a|k(a)da<infinity.

For an even cutoff chi_R with ||chi_R'||=O(1/R), Young's inequality gives

    ||[b(D),chi_R]||_(2->2)
       <=||chi_R'||_infinity integral |a|k(a)da.

If v in D(B), f=mv, the distributional identity is

    B(chi_R v)=chi_R Bv+m[b(D),chi_R]f.

The usual product-difference estimate first puts chi_R v in the form domain; the displayed L2 right side then puts it in D(B). It converges to v in graph norm. For compactly supported v, local positivity of m implies b(D)f is L2 on an enlarged compact set. Outside that set, separated supports give b(D)f=−k*f, with an exponentially decreasing L2 tail. Hence f belongs to D(b(D)) globally. Even compact mollification commutes with b(D) and converges in its graph norm. Dividing the mollified sources by m on their common compact support produces even C_c-infinity approximations in the graph norm of B.

One can therefore choose nested finite-dimensional spaces of genuine compact smooth trials whose union is a B graph core. For such a trial y,

    A_epsilon y=m b(D)(my)+epsilon y

is an actual L2 vector. No second derivative of a nonsmooth moment coordinate or unverified operator-domain inclusion is used.

### 9.2 Actual least-residual matrices

Fix epsilon>0 and the finite cell parameters. Use the exact inputs f_i=mQe_i from Section 8. Choose independent even compact smooth trials y_j, and use an inner product conjugate-linear in its first argument. Form

    S_jk=<y_j,A_epsilon y_k>, C_ji=<y_j,f_i>,
    T_ji=<A_epsilon y_j,f_i>, D_trial,jk=<A_epsilon y_j,A_epsilon y_k>,
    F_input,ij=<f_i,f_j>.

All entries are defined in the original L2 norm and exact operator. D_trial is positive definite because A_epsilon is injective. Let

    W=D_trial^(-1)T,  Y_i=sum_j y_j W_ji,
    R_i=f_i−A_epsilon Y_i,
    R^*R=F_input−T^*D_trial^(-1)T,
    L_Y=C^*W+W^*C−W^*S W.

Expansion of the genuine residual gives the exact identity and Loewner bounds

    G_cell−L_Y=(<R_i,A_epsilon^(-1)R_j>),
    L_Y<=G_cell<=L_Y+epsilon^(-1)R^*R.                       (21)

L_Y need not be positive. These are two-sided bounds, not an energy-Galerkin lower matrix incorrectly used as an upper one. The coefficients W minimize the actual L2 residual for each input. The graph-core result and surjectivity of A_epsilon:D(B)->L2 imply that these residuals tend to zero as the nested spaces exhaust the core. Hence (21) converges to the true finite Gram for each fixed epsilon and fixed cell family. This does not assert L2-residual convergence of arbitrary energy-Galerkin approximants.

Rigorous numerical enclosures of S,C,T,D_trial,F_input and the actual finite eigenvalues are still required for a specific implementation of (20). No such enclosures, runtime or precision bounds are supplied. In particular (21) has no claimed rate uniform as epsilon decreases, and no source-mass-zero assumption is silently imposed on the full cell family.

## 10. Provenance and exact scope

The original full theta/Gamma/prime normalization, maximal jump form and explicit-formula identity are inherited from the user's fifth-round report and continuation at fixed [74add2e](https://github.com/aa339519589-cpu/Riemann-Hypothesis/tree/74add2e1350dd4414d83dd46a4e10be8aeb7b42f), especially rounds/05 and history/source-materials/RH_研究续篇_20261011.md. The complete theta realization is also fixed in the public [lowstate report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d74308ed56639ddf0505f1e50007f79337d367da/reports/20261011_lowstate_subexponential_decay/REPORT.md). Section 1 states the exact realization and proves the quantitative bounds needed here; Sections 8--9 include the signed finite-spectrum and operator-domain steps rather than treating unavailable computations as inputs.

The new positive content is the matching GLOBAL source norm estimate (3), the exact commuting-frequency gain (10), and the full original adaptive norm tail (14)--(19), with a legitimate two-sided method for the remaining resolvent Gram. The statements concern the unchanged full even operator at positive epsilon, with fixed-error constants allowed to depend on eta. The rank bound is not a complexity bound. No actual second-eigenvalue certificate, exclusion of an unknown low eigenvalue, or RH proof follows without the remaining finite/limiting sign estimate. Independent mathematical verification is in [REFEREE.md](REFEREE.md).
