# Depth-free source regularity and full-zero sampling for individual negative eigenstates

For every normalized individual negative eigenstate of the original even operator, the source has a depth-independent H^s bound for every s<1, a dyadic frequency-mass bound C/(N^2 log N), and a logarithmically weakened H^1 endpoint. Spatial interpolation then gives uniform sampling bounds over all genuine zeros, with their multiplicities. The conclusions concern individual eigenstates, rather than arbitrary mixtures in the negative spectral subspace; the inverse-depth factors in the actual zero expansion remain explicit.

The original closed form, complete weighted prime operator, theta bounds and operator domain are those of [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md) and [ACTUAL_NEGATIVE_BAND_COVERAGE.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bf5ee119d3b6687d34cd708f1a755aea9efd9679/reports/20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md). The localization and source-frequency arguments needed here are proved below.

## 1. Setting and theorem

Use the original closed even form

 h[v]=b[mv]-C0||mv||_2^2-<mv,S mv>,
 S=sum_(n>=2) alpha_n(tau_(log n)+tau_(-log n)),
 alpha_n=Lambda(n)/sqrt(n),
 b(t)=Re digamma(1/4+it/2)-digamma(1/4)
      >= (1/2)log(1+4t^2),
 C0=EulerGamma+pi/2+3log 2+log pi.

Use Fourier transform fhat(t)=int f(x)exp(itx)dx, measure dt/(2pi), and b[f]=int b(t)|fhat(t)|^2dt/(2pi). Inner products are conjugate-linear in their first slot. The physical operator H=M_m b(D)M_m-V has complete bounded V. Its form domain is precisely the original L2 vectors whose source mv belongs to Q(b). All infinite-prime expressions below are limits of the original norm-convergent weighted physical operator; no unweighted bounded full S is asserted.

Let Hu=-kappa u, 0<kappa<=1/2, with u in the original even operator domain and ||u||_2=1. Put f=mu and rho=m^(-2). The conclusion is

  ||f||_(H^s(R)) <= C_s,                 0<=s<1,                 (1)

with C_s independent of u and kappa. The proof below also gives the dyadic estimate

  integral_(N<=|t|<=2N) |fhat(t)|^2 dt/(2pi)
        <= C/(N^2 log N),               N sufficiently large.   (2)

The known ground-orthogonality condition can be retained throughout, but the proof only uses the eigen-equation and positive physical kappa term, not a variational assertion about other eigenvalues.

## 2. A kappa-weighted double-exponential physical moment

Write V=C0 m^2+V_prime, and define M=||m||_infinity<=2. The original theta envelope and complete weighted prime norm tail give

 m_tail(R)=7 exp(2R-(pi/2)e^(2R)),
 c_K=C0+2 sum_(2<=n<=K)alpha_n,
 ||V_prime-(V_prime)_K||<=delta_K
             <=(980/9)(K+1)^2 exp(-pi(K+1)), K>=2.

The complete Gamma jump kernel is k(y)=exp(-|y|/2)/(1-exp(-2|y|)), with integral y^2 k(y)dy=4 sum_(j>=0)(2j+1/2)^(-3)<36.

Let chi_R be smooth and even, 0<=chi_R<=1, zero for |x|<=R, one for |x|>=R+1, and Lip(chi_R)<=2. A bounded Lipschitz multiplier preserves Q(b): expand the source increment and use the integrability of k(y)min(1,y^2). Hence chi_R^2 u is in the original form domain and is a legal test of the scalar eigen-equation. In particular

 Re h(chi_R^2u,u)=-kappa||chi_R u||^2.

The exact Gamma source localization formula is

 b[chi_R f]=Re b(chi_R^2f,f)+E_R,
 E_R=(1/2) integral integral k(y)(chi_R(x+y)-chi_R(x))^2
                           Re(conjugate(f(x+y))f(x)) dxdy.

It follows first for truncated kernels and then by the integrable difference bound. On the support of the chi difference at least one endpoint has absolute value greater than R, so its two theta factors have product at most M m_tail(R). Since integral y^2 k(y)dy<36 and |chi_R(x+y)-chi_R(x)|<=2|y|,

 |E_R|<=72 M m_tail(R)||u||^2.

Testing the full eigen-equation therefore gives the exact identity

 kappa||chi_R u||^2+b[chi_R f]
 =C0||chi_R f||^2+Re<chi_R^2u,V_prime u>+E_R.

The constant term is at most C0 M m_tail(R)||u||^2. For each of the two shifts with n<=K, the chi-supported physical multiplier has norm at most M m_tail(R). The complete remaining physical prime operator has norm at most delta_K. As ||u||=1, this proves

 kappa||chi_R u||^2+b[chi_R f]
 <= M m_tail(R)[c_K+72]+delta_K.                                (3)

This is the full original H, with the finite label K used only to estimate its complete prime norm tail. The elementary Chebyshev estimate Psi(X)<=3X, whose complete-label proof is also included in [INFINITE_HIGH_TAIL.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6d1e0faa41303572069083f398c477f44660467a/reports/20261013_growing_rank_source_estimates/INFINITE_HIGH_TAIL.md), gives

 sum_(n<=K) alpha_n <=6 sqrt(K),   c_K<=C0+12 sqrt(K).

Take K=ceil(e^(2R)). Equation (3) implies, for R>=1,

 kappa integral_(|x|>=R+1)|u(x)|^2 dx
       <= C exp(3R-(pi/2)e^(2R)).                               (4)

In particular, writing beta=pi/(2e^2),

 kappa integral_(|x|>=t)|u(x)|^2 dx
       <= C exp(3t-beta e^(2t)),   t>=2.                        (5)

The shift by one in this statement is essential. By layer integration of the increasing weight, (5) and kappa<=1/2 imply

 kappa integral exp(b0 e^(2|x|)) |u(x)|^2 dx <= C_(b0),
                          0<b0<beta.                           (6)

Indeed the derivative of that weight is 2b0 e^(2t)exp(b0 e^(2t)); multiplying (5) leaves an integrable C exp(5t-(beta-b0)e^(2t)). The bounded interval is paid by kappa<=1/2. Thus (6) is stronger than merely all fixed exponential moments.

## 3. Theta logarithmic derivatives and a fixed translation radius

The full theta series and its positive lower bound give constants L>=1 such that, on the whole real line,

 |(log m)'(x)|<=L e^(2|x|),
 |rho''(x)|<=L e^(4|x|)rho(x).                                  (7)

Here is a direct justification. For x>=0 write q=e^(2x). The defining theta series is

 Phi(x)=sum_(n>=1)(4pi^2 n^4 e^(9x/2)-6pi n^2 e^(5x/2))
                                      exp(-pi n^2 q),
 w(x)=m(x)^2=Phi(x)/(2cosh(x/2)).

Differentiating zero, one or two times shows

 |w^(j)(x)|<=C_j e^((4+2j)x)exp(-pi q), j=0,1,2.

To see uniformity, after extracting exp(-pi q), the remaining sums are bounded by constants times sum n^(4+2j)exp[-pi(n^2-1)], since q>=1; powers of q from differentiation are included in e^(2jx). The denominator and its derivatives contribute only bounded logarithmic factors. Combine with w>=9e^(4x-pi q) and use evenness. Then (log m)'=w'/(2w) and rho''/rho=2(w'/w)^2-w''/w prove (7).

Choose a fixed 0<delta<1/100 so small that

 16 L delta exp(8delta) <= beta.                                (8)

This radius is independent of kappa and of the frequency parameter. All kernel shifts below have |s|<=delta, and twofold propagation has radius at most 2delta.

For |h|<=2delta, the mean value bound in (7) gives

 w(y)/w(y+h) <= exp[4 L delta exp(4delta)e^(2|y|)].                (9)

Equations (6), (8), and (9) imply the legitimate physical-space translation bound

 || f(.-h)/m ||_2 <= C kappa^(-1/2),       |h|<=2delta.           (10)

This bound is used only to pay domains. It is not inserted into the frequency estimates as an error term.

A second consequence, for |s|,|t|<=delta, h=s+t and a=theta s+eta t with theta,eta in [0,1], is

 kappa integral |f(x)f(x-h)| sup_(theta,eta in [0,1])
                                   |rho''(x-a)| dx <= C.        (11)

For detail, |a|+|h-a|<=|s|+|t|<=2delta. Hence (7) yields

 m(x)m(x-h)|rho''(x-a)|
 <= C exp(4|x|)exp[2L delta exp(4delta)e^(2|x|)].

Apply Cauchy--Schwarz to the two u factors. In the translated factor change variables by h; its double-exponential coefficient is at most 2L delta exp(8delta)<=beta/8. The factor exp(4|x|) can be absorbed into exp[(beta/8)e^(2|x|)] with an absolute constant, also after translation. Both resulting coefficients are strictly below beta/2, so (6) pays them. This proves (11) with uniform constants.

## 4. A compact-propagation bandpass

Fix an even real p in C_c^infinity(R) with p=1 on 1<=|t|<=2, supported in 1/2<|t|<3. Let k be its inverse Fourier kernel, so p(D)g=k*g. Then k is real, even and Schwartz. Choose an even real eta in C_c^infinity((-delta,delta)), eta=1 on [-delta/2,delta/2]. Define

 k_N(s)=N k(Ns)eta(s),  C_N g=k_N*g,  c_N(t)=khat_N(t).

No Gevrey assertion is needed. For every integer M>=1,

 ||k_N||_1<=C,
 integral |s||k_N(s)|ds<=C/N,
 sup_t |c_N(t)-p(t/N)|<=C_M N^(-M).                             (12)

The last bound is just the L1 tail of the Schwartz kernel outside |Ns|>=Ndelta/2. Thus |c_N|>=1/2 on N<=|t|<=2N for large N, and |c_N|<=C_M N^(-M) on |t|<=N/4.

Put g_N=C_N f. Equation (10) and Minkowski show that g_N/m and C_N^2 f/m belong to physical L2. They are even. Since f is in Q(b) and C_N is a bounded Fourier multiplier commuting with b(D), both sources belong to Q(b). Therefore both quotients lie in the original closed form domain. This form-domain statement is sufficient to test the eigen-equation; an operator-domain assertion is unnecessary.

If u is ground-perpendicular, its two source pole moments vanish. Compact translations multiply each exponential moment by exp(+-s/2), so the same is true of C_N f and C_N^2 f. No ground or pole term is created.

## 5. Exact full-form identity and its uniform upper bound

For a finite prime sum S_K, translation invariance and selfadjointness give

 b[C_N f]=b(f,C_N^2 f),
 <C_N f,S_K C_N f>=<f,S_K C_N^2 f>,
 ||C_N f||^2=<f,C_N^2 f>.

Pass to the full original prime form using its physical norm convergence and the just-proved physical L2 domains. Testing Hu=-kappa u against C_N^2 f/m then gives

 h[g_N/m]+kappa||g_N/m||^2
 =kappa ( integral rho |C_N f|^2
                    -Re integral rho conjugate(f) C_N^2 f )
 =(kappa/2)<f,[C_N,[rho,C_N]]f>.                                (13)

The last expression denotes the absolutely convergent quadratic kernel, not a globally bounded double commutator on unweighted L2.

Since k_N is real and even, symmetrizing the two convolution shifts writes its kernel factor as

 rho(x-s)+rho(x-t)-rho(x)-rho(x-s-t).

The mixed fundamental theorem of calculus bounds its absolute value by

 |st| sup_(theta,eta in [0,1]) |rho''(x-theta s-eta t)|.

Thus (11), (12), and Fubini imply

 h[g_N/m]+kappa||g_N/m||^2
              <= C (integral |s||k_N(s)|ds)^2 <= C/N^2.         (14)

No sign is assigned to the four-point kernel. The upper bound uses its absolute value. All constants here are independent of kappa.

## 6. The complete prime bound for the filtered source

Choose 0<a<(pi/2)exp(-2delta), and set m_a(x)=exp(-a e^(2|x|)). The theta upper bound implies

 sup_(x,|s|<=delta) m(x-s)/m_a(x) <= C_a.

Consequently, directly from f=mu and Minkowski,

 ||g_N/m_a||_2<=C_a||k_N||_1||u||_2<=C_a.                       (15)

This estimate is independent of kappa. Unlike g_N/m, it requires no eigenstate tail input.

For d=log n,

 sup_x m_a(x)m_a(x+d)<=exp(-2an),

because e^(2|x|)+e^(2|x+d|)>=2n. Therefore the COMPLETE prime tail, in the auxiliary weight, obeys

 || M_(m_a)(S-S_K)M_(m_a) ||
 <=2 sum_(n>K) alpha_n exp(-2an) <= C_a exp(-aK).                (16)

The final inequality follows even from alpha_n<=log n/sqrt(n). The finite initial part uses the true Chebyshev estimate:

 |<g_N,S_Kg_N>|<=12 sqrt(K)||g_N||^2.

Combining with (15)-(16) gives

 |<g_N,Sg_N>|<=12 sqrt(K)||g_N||^2+C_a exp(-aK).                 (17)

This is the full original source prime form, identified either by its absolutely convergent weighted sum or by the original physical norm limit. No finite-prime operator replaces H.

## 7. High-frequency coercivity and the conclusion

The low-frequency leakage in (12) and b(t)>=(1/2)log(1+4t^2) give

 b[g_N]>= (log N-C)||g_N||^2-C_M log(N)N^(-2M).                 (18)

Choose a fixed sufficiently small epsilon>0, for example epsilon=1/2304, and K=floor(epsilon(log N)^2). For all sufficiently large N, K>=2 and 12sqrt(K)<=log(N)/4. Equations (17)-(18), with C0 absorbed for large N, yield

 h[g_N/m]+kappa||g_N/m||^2
 >= (1/2)log(N)||g_N||^2
           -C_M log(N)N^(-2M)-C exp[-c(log N)^2].               (19)

Here the positive kappa mass is simply retained or discarded; there is no inverse-depth cost. Combining (14) and (19), taking M=2 and increasing the lower N threshold, proves

 ||g_N||^2<=C/(N^2 log N).

Since |c_N(t)|>=1/2 on N<=|t|<=2N, this proves (2). Summation over dyadic N proves (1) for every s<1. More precisely, the same argument yields the endpoint logarithmically weakened bound

 integral ((1+t^2)/(log(2+|t|))^epsilon) |fhat(t)|^2 dt
       <= C_epsilon,                       epsilon>0.          (20)

Indeed the dyadic high-frequency terms are bounded by C k^(-1-epsilon). The unweighted H^1 endpoint is not obtained by this summation.

## 8. Whole-strip weighted source estimates

Let Hu=-kappa u be an individual normalized real even original negative eigenstate, 0<kappa<=1/2, and set f=mu. The theorem proved in Sections 1–7 gives

 ||f||_(H^s)<=C_s,                       0<=s<1,                (S1)

uniformly in kappa and u. In addition the theta multiplier gives

 ||1_(|x-k|<=2) f||_2
       <= sup_(|x-k|<=2) m(x),                                 (S2)

and the right side decreases double exponentially as |k| tends to infinity.

For any finite A>=0, integer q>=0 and 0<=t<1, we claim

 sup_(|eta|<=A) ||x^q exp(eta x)f||_(H^t)<=C_(A,q,t).             (S3)

Fix t<s<1 and a smooth unit-scale partition of unity chi_k with uniformly bounded derivatives and support |x-k|<=2. Multiplication by chi_k is uniformly bounded on H^s. Interpolating its global H^s bound with (S2) yields

 ||chi_k f||_(H^t)
       <=C_s [sup_(|x-k|<=2)m(x)]^(1-t/s).                      (S4)

For the finitely many central cells replace this supremum by a fixed upper bound; all constants remain uniform. On the k-th cell, multiplication by x^q exp(eta x) is bounded on H^t with norm at most

 C_(A,q,t)(1+|k|)^q exp(A|k|),

using a smooth extension supported in a slightly larger cell. This follows, for example, from the L2 and H1 multiplication bounds followed by interpolation; all required first derivatives have the displayed size up to a fixed constant. The double-exponential decay in (S4) makes the resulting H^t norms summable over k. The series reconstructs x^q exp(eta x)f in L2 and converges absolutely in H^t, proving (S3).

Thus the source estimates cover any fixed finite vertical Fourier strip, with an arbitrarily small loss from s to t. No conjugated infinite-prime operator or additional eigenstate equation is needed. In particular one may take A=1, which covers the entire nontrivial zero strip with a positive margin.

## 9. Complete genuine-zero sampling

Define the actual entire transform

 B(z)=integral f(x)cos(zx)dx=integral f(x)exp(izx)dx.

Evenness gives the second equality. Entire continuation follows from the theta multiplier and Cauchy--Schwarz. With the Fourier convention fhat(t)=integral f(x)exp(itx)dx,

 B(t+i eta)=(exp(-eta x)f)hat(t).

Let Z_+ be all distinct genuine Xi zeros with gamma_z=Re z>0 and |Im z|<1/2, with their true multiplicities j_z. This is the standard nontrivial zero strip; the argument needs no narrower zero-containment claim. Use the unconditional unit-height zero count, obtained from [Hasanalizade, Shen and Wong, Corollary 1.2](https://arxiv.org/abs/2107.06506) by subtracting the counting bounds at unit separation,

 sum_(z: r<=gamma_z<r+1) j_z <=C_Z log(2+r),   r>=0,             (S5)

with a larger fixed constant on the bounded initial range.

For every 0<=t<1,

 sum_(z in Z_+) j_z (1+gamma_z)^(2t)|B(z)|^2 <= C_t.             (S6)

To prove this, choose t<r<1 and use (S3) with Sobolev exponent r and A=1. It gives

 integral_(-1)^1 integral_R (1+|x|)^(2r)|B(x+i y)|^2 dxdy <=C_r. (S7)

Use disks of fixed radius 1/8 about every z in Z_+. They lie inside |Im w|<1 and satisfy 1+|Re w| comparable to 1+gamma_z. The analytic mean-value inequality bounds |B(z)|^2 by the disk area integral divided by pi/64. At any point of the strip, the sum of the true multiplicities of disks covering it is at most C log(2+|Re w|), by (S5). Therefore the left side of (S6) is bounded by

 C integral_(|Im w|<1) (1+|Re w|)^(2t)
                       log(2+|Re w|)|B(w)|^2 dA(w),

which is at most C_(r,t) times (S7). This proves (S6), with no separation or simplicity assumption and both conjugate members retained.

For fixed derivative order q, the same proof applied to B^(q), using the x^q case of (S3), gives

 sum_(z in Z_+) j_z (1+gamma_z)^(2t)|B^(q)(z)|^2 <= C_(t,q).      (S8)

This statement concerns derivatives of the actual sampling function, not vanishing to the multiplicity order at a zero.

## 10. Actual all-zero tail budgets

Fix 1/2<t<1 and T>=2. Equation (S6) gives

 E_1(T):=sum_(gamma_z>=T) j_z log(2+gamma_z)|B(z)|^2
                 <= C_t T^(-2t)log(2+T).                       (S9)

For the absolute sampling sum, apply Cauchy--Schwarz with the weight (1+gamma_z)^(2t). The zero-count bound (S5) implies

 sum_(gamma_z>=T) j_z(1+gamma_z)^(-2t)
                 <=C_t T^(1-2t)log(2+T).

Hence

 sum_(gamma_z>=T)j_z|B(z)|
                 <= C_t T^(1/2-t)sqrt(log(2+T)).                (S10)

Assume now additionally that u is perpendicular to the distinguished ground state. Only for this nonground negative state do we invoke the actual complete expansion proved in [INFINITE_HIGH_TAIL.md, Section 5](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6d1e0faa41303572069083f398c477f44660467a/reports/20261013_growing_rank_source_estimates/INFINITE_HIGH_TAIL.md), a_z=-2j_zB(z)/kappa. Equations (S9)-(S10) then imply

 J_T^2:=sum_(gamma_z>=T)|a_z|^2 log(2+gamma_z)/j_z
                 <= C_t kappa^(-2)T^(-2t)log(2+T),              (S11)

 M_T:=sum_(gamma_z>=T)|a_z|
                 <= C_t kappa^(-1)T^(1/2-t)sqrt(log(2+T)).       (S12)

All constants are independent of the normalized individual negative eigenstate and its depth kappa. The inequalities cover all genuine zeros, including the complete off-line conjugate pairs. The inverse-depth factors in (S11)-(S12) remain explicit.

The centered boundary estimate is in [CENTERED_BOUNDARY_COUPLING.md, Sections 5–6](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6d1e0faa41303572069083f398c477f44660467a/reports/20261013_growing_rank_source_estimates/CENTERED_BOUNDARY_COUPLING.md). Its sampling budget obeys the corresponding absolute estimate

 sum_z j_z log(2+gamma_z)|B(z)|^2 exp(-|gamma_z-T|/8)
                 <=C_t T^(-2t)log(2+T),                        (S13)

since the ratio of its weight to (1+gamma_z)^(2t) is bounded by the displayed right-hand factor, with exponentially small distant low-height terms. More generally any fixed power of the logarithm can be included at the cost of that logarithmic power on the right.

## 11. Scope of the uniform estimates

These estimates replace depth-dependent sampling regularity constants by uniform polynomial tail bounds for each actual eigenstate. They do not extend (S1) to an operator norm bound for mP_- or to arbitrary mixed eigenvalues. They do not turn the Hermitian sampling budgets into the complete signed zero-pair comparison.

In particular, the low/high boundary residual still carries kappa^(-2); its comparison with the actual low/high source Gram or physical tail mass has not been made relative. Selecting T so that (S11) is absolutely small does not provide that missing comparison.

No unweighted H^1 endpoint or fixed-strip exponential frequency decay is asserted. The constants may deteriorate as the Sobolev exponent approaches 1 or as a weight parameter increases. No new zero exclusion or RH conclusion follows.


---

The following continuation refines the same proof by shrinking the source convolution radius as the eigenvalue approaches zero. It gives a genuine relative bound for the high negative sampling squares of an actual eigenstate, while keeping the entire low-height signed comparison unresolved. Equation labels (D1)–(D19) refer only to this continuation.

## 12. A depth-adapted filter and the actual all-zero tail

Let Hu=-kappa u be a normalized real even original negative eigenstate, 0<kappa<=1/2. Write f=mu, B(z)=integral f(x)cos(zx)dx, and ell_kappa=log(e/kappa). For every fixed sigma>0 the conclusion is that, for

 T>=C_sigma kappa^(-sigma),

one has, over ALL genuine positive-height zeros and their true multiplicities,

 sum_(gamma_z>=T) j_z log(2+gamma_z)|B(z)|^2
                 <= C_sigma kappa log^4(2+T)/T^2,               (D1)

 sum_(gamma_z>=T) j_z |B(z)|
                 <= C_sigma sqrt(kappa) log^2(2+T)/sqrt(T).    (D2)

The constants depend on sigma and the fixed original operator, not on kappa or u. For the ground-perpendicular state with actual expansion a_z=-2j_zB(z)/kappa these give

 J_T^2 <= C_sigma kappa^(-1)log^4(2+T)/T^2,
 M_T   <= C_sigma kappa^(-1/2)log^2(2+T)/sqrt(T).                 (D3)

The inverse-depth powers improve, but do not disappear. The stated height threshold is an essential part of the claim.

## 13. A sharper use of the actual kappa-weighted physical tail

Use the scalar localization estimate (5) proved above, with beta=pi/(2e^2),

 kappa integral_(|x|>=r)|u(x)|^2dx
                <= C exp(3r-beta e^(2r)),       r>=2.

Put q(x)=e^(2|x|) and let dnu_kappa(x)=kappa|u(x)|^2dx, of total mass kappa. Then, for Q>=e^4,

 nu_kappa(q>=Q)<=min(kappa,C Q^(3/2)exp(-beta Q)).                (D4)

For each fixed c>=0, if delta_kappa=delta_*/ell_kappa with delta_*>0 sufficiently small, (D4) implies

 integral q^2 exp(c delta_kappa q)dnu_kappa
                              <= C_c kappa ell_kappa^2.        (D5)

A direct proof is as follows. Choose delta_* so that c delta_*<=beta/4. Set Q0=A ell_kappa+B, with fixed A>=8/beta and sufficiently large B. On q<=Q0 the integrand is at most C ell_kappa^2, so the contribution is at most C kappa ell_kappa^2. Above Q0 use layer integration and the second bound in (D4). The derivative of q^2 exp(c delta_kappa q) is at most C(q+q^2)exp(c delta_kappa q). The resulting integrand is a fixed polynomial times exp(-3beta q/4). By increasing A,B its tail is bounded by C kappa^2, which is at most C kappa ell_kappa^2. This proves (D5). The same proof with q^2 replaced by 1 gives integral exp(c delta_kappa q)dnu_kappa<=C kappa.

The true theta derivative estimates

 |(log m)'(x)|<=L_m q(x),  |rho''(x)|<=L_m q(x)^2 rho(x),
 rho=m^(-2),

therefore yield the improved four-point estimate

 kappa integral |f(x)f(x-s-t)|
       sup_(theta,eta in [0,1])|rho''(x-theta s-eta t)|dx
          <=C kappa ell_kappa^2,       |s|,|t|<=delta_kappa.     (D6)

Indeed the same logarithmic ratio comparison as in the fixed-radius proof in Section 3 bounds the integrand by C q(x)^2 exp(C delta_kappa q(x))|u(x)u(x-s-t)|. After Cauchy--Schwarz and shifting the second factor, the fixed small delta_* keeps the coefficient in (D5) uniformly bounded. A single choice of delta_* pays every constant in this calculation. It also gives

 ||f(.-h)/m||_2<=C,                       |h|<=2delta_kappa,     (D7)

by the q^0 version of (D5), after dividing the resulting bound by kappa. As before, these translation bounds pay the original physical form domains of the convolution tests.

## 14. Shrinking compact convolution and a real-axis frequency estimate

Fix a real even compact-frequency bandpass p, equal to 1 on 1<=|t|<=2 and supported in 1/2<|t|<3, with Schwartz convolution kernel k. Choose a fixed smooth even cutoff eta, supported in (-1,1) and equal to 1 on [-1/2,1/2]. Define

 k_(N,kappa)(s)=N k(Ns)eta(s/delta_kappa),
 C_(N,kappa)g=k_(N,kappa)*g.

Uniformly in N,kappa,

 ||k_(N,kappa)||_1<=C,
 integral |s||k_(N,kappa)(s)|ds<=C/N,
 ||chat_(N,kappa)-p(./N)||_infinity
                    <=C_M(ell_kappa/N)^M                     (D8)

for every fixed M, provided N delta_kappa>=1. In the last line chat denotes the Fourier multiplier of this kernel, not the transform of the operator.

For g=C_(N,kappa)f the same exact full-source identity and (D6) give

 h[g/m]+kappa||g/m||^2
 = (kappa/2)<f,[C_(N,kappa),[rho,C_(N,kappa)]]f>
                    <=C kappa ell_kappa^2/N^2.                (D9)

All quotient domains are paid by (D7), and the complete source form commutes with the convolution exactly as in Section 5. No bounded bare full S is used.

The auxiliary wider-theta weight m_a can now be chosen once for the maximum radius delta_*. Its source norm and full prime-tail constants are uniform as delta_kappa shrinks. Thus, with K=floor((log N)^2/2304), the complete high-frequency lower bound is

 h[g/m]+kappa||g/m||^2
 >=(1/2)log(N)||g||^2
       -C_M log(N)(ell_kappa/N)^(2M)-C exp[-c(log N)^2].         (D10)

Fix sigma>0. For N>=C_sigma kappa^(-sigma), one has kappa^(-1)<=C_sigma N^(1/sigma) and ell_kappa<=C_sigma log N. Choose a fixed M with 2M>3+1/sigma. Increasing C_sigma then makes both errors in (D10) at most C_sigma kappa ell_kappa^2/N^2: the first follows by comparing fixed powers of N and log N, and the Gaussian-in-log error beats every required power of N. Equations (D8)-(D10) imply

 integral_(N<=|t|<=2N)|fhat(t)|^2dt/(2pi)
       <= C_sigma kappa ell_kappa^2/(N^2 log N),
                       N>=C_sigma kappa^(-sigma).             (D11)

By dyadic summation, the same bound holds with the integration region |t|>=N, after a change of constant. There is no assertion here about the complementary lower frequencies.

## 15. Finite-strip transfer with only logarithmic losses

We need the estimate on |Im z|<=1, rather than just the real Fourier line. Fix a finite A>=0. For |eta|<=A, the source multiplier e^(eta x) is handled by a spatial cutoff and a Fourier low/high split, with no conjugated operator.

For N above a larger constant times kappa^(-sigma), set

 R=(1/2)log[D(ell_kappa+log N)],

where D is a fixed sufficiently large constant, depending only on A. Let chi_R be 1 on |x|<=R, zero on |x|>=R+1, with uniformly bounded derivatives of every fixed order. The theta envelope and ||u||=1 give

 ||e^(eta x)(1-chi_R)f||^2<=C_A kappa N^(-4),
                                             |eta|<=A,        (D12)

by taking D large: its upper bound is C_A exp[(4+2A)R-pi e^(2R)], and any fixed power of ell_kappa+log N can be absorbed into half of that double-exponential exponent.

Put a_R(x)=e^(eta x)chi_R(x). Then

 ||a_R||_infinity^2<=C_A(ell_kappa+log N)^A,
 ||a_Rhat 1_(|xi|>=N/2)||_1
 <=C_(A,M)(R+1)e^(A(R+1))N^(-M).                              (D13)

The latter follows by integrating by parts a fixed sufficiently large number of times. All derivatives of chi_R are uniformly bounded, its support has length O(R+1), and every derivative of e^(eta x) is uniformly bounded by C_(A,M)e^(A(R+1)) there.

Let P_N denote the sharp frequency projection N<=|t|<=2N. Split f at input frequency N/4. The high-input term is bounded by ||a_R||_infinity times the tail version of (D11); ensure N/4 is above its threshold by enlarging C_sigma. In the low-input term the multiplier convolution has frequency separation at least 3N/4, so (D13) and Young's inequality apply. With fixed M sufficiently large in terms of sigma and A, its square is at most C_(sigma,A)kappa N^(-2). Finally add (D12). Since ell_kappa<=C_sigma log N, the result is

 ||P_N(e^(eta x)f)||^2
 <=C_(sigma,A) kappa (log N)^(A+1)/N^2,
 |eta|<=A,                N>=C_(sigma,A)kappa^(-sigma).         (D14)

The factor (log N)^(A+1) comes from (ell_kappa+log N)^A times ell_kappa^2/log N. All source Fourier projections in this section act in unweighted L2; none is divided by m or used as an original variational test.

## 16. Full genuine-zero sampling and the actual budgets

Take A=1 in (D14), and integrate in eta. Since B(t+i eta)=(e^(-eta x)f)hat(t), the squared analytic area mass in an enlarged dyadic rectangle is at most C_sigma kappa(log N)^2/N^2. The fixed-disk analytic mean-value inequality and the unconditional unit-height zero count give, with true multiplicities and no separation assumption,

 sum_(N<=gamma_z<2N) j_z|B(z)|^2
       <=C_sigma kappa(log N)^3/N^2,
                         N>=C_sigma kappa^(-sigma).            (D15)

The disks about all nontrivial zeros, |Im z|<1/2, are inside |Im z|<1. Enlarging the rectangle by a fixed amount is harmless after enlarging the threshold constant.

Dyadic summation of (D15), with one logarithmic factor, proves (D1). For (D2), Cauchy--Schwarz in each dyadic block uses its total zero multiplicity O(N log N): its absolute sampling sum is at most C_sigma sqrt(kappa)(log N)^2/sqrt(N). Sum the geometric tail.

The centered boundary sampling budget obeys the same improved absolute bound

 sum_z j_z log(2+gamma_z)|B(z)|^2 exp(-|gamma_z-T|/8)
                  <=C_sigma kappa log^4(2+T)/T^2,              (D16)

for T>=C_sigma kappa^(-sigma), with a sufficiently enlarged constant. To see this, split at gamma=T/2. Above this point use (D1); below it, the earlier depth-free global weighted sampling bound gives at most C exp(-T/16). Since kappa^(-1)<=C_sigma T^(1/sigma), that exponential remainder is absorbed into (D16).

Let S_low(T) and S_high(T) be the sum on the left of (D16), restricted respectively to gamma_z<T and gamma_z>=T. For the original centered boundary residual D_T, the complete estimate from CENTERED_BOUNDARY_COUPLING.md is still

 |D_T|<=C kappa^(-2)sqrt(S_low(T)S_high(T)).

Using (D16) gives |D_T|<=C_sigma kappa^(-1)log^4(2+T)/T^2. This genuinely saves one inverse-depth power in the absolute residual budget, but there is still no comparison to the actual mixed source Gram or actual tail mass. In particular a normalized low/high tail can be much smaller than this absolute bound; no relative absorption follows.

## 17. Relative control of the actual high negative sampling squares

Assume again that u is a normalized real ground-perpendicular negative eigenstate. For each off-line pair choose z=gamma+i eta with eta>0 and write B(z)=b_z-i c_z, with real b_z,c_z. Both members of the pair have multiplicity j_z. The actual complete source expansion gives the exact signed identity

 kappa+P(u)=N_low(T)+N_high(T),
 P(u)=sum_critical 2j|B(gamma)|^2+sum_off_pairs 4j b_z^2,
 N_low(T)=sum_(off_pairs,gamma<T)4j c_z^2,
 N_high(T)=sum_(off_pairs,gamma>=T)4j c_z^2.                     (D17)

For every pair its contribution to the full Hermitian sum is 2j(b_z^2+c_z^2). Therefore (D15) and dyadic summation give

 N_high(T)<=2 sum_(all z,gamma>=T) j_z|B(z)|^2
          <=C_sigma kappa log^3(2+T)/T^2,
                         T>=C_sigma kappa^(-sigma).            (D18)

Increasing C_sigma if necessary makes the final multiplier at most 1/2 throughout the stated range. Subtracting this tail from the exact identity, while retaining EVERY positive sampling term, gives

 kappa/2+sum_critical 2j|B(gamma)|^2+sum_off_pairs 4j b_z^2
                  <=sum_(off_pairs,gamma<T)4j c_z^2.            (D19)

This is a genuine relative estimate for the high negative-square part of the actual original coupling. It is distinct from the low/high form-boundary estimate, whose source Gram comparison is still missing. Equation (D19) forces at least one active off-line pair below this depth-dependent finite height. It does not bound the remaining low-height imaginary squares by the retained positive sampling terms, and does not prove their coefficient-one comparison.


---

A fixed Gevrey-two choice of the source filter makes the finite-height threshold explicit in scale. The proof below replaces the family of bounds T>=C_sigma kappa^(-sigma) by one bound T>=exp(C sqrt(log(e/kappa))). No numerical value of C or new finite-height zero verification is supplied. Equation labels (G1)–(G13) refer only to this continuation.

## 18. Fixed Gevrey cutoffs, with their elementary kernel bound

A compact Gevrey-2 cutoff can be constructed without any spectral assumption. For example take phi(x)=exp[-1/(1-x^2)] on |x|<1 and zero elsewhere. If d=1-|x|, Cauchy's estimate on a complex circle of radius c d, with c a sufficiently small fixed constant, gives

 |phi^(n)(x)|<=n!(c d)^(-n)exp(-c'/d).

Indeed the denominator 1-z^2 has size comparable to d and argument uniformly separated from +-pi/2 on that circle. Maximizing d^(-n)exp(-c'/d) and using n!>=(n/e)^n yields

 ||phi^(n)||_infinity<=C^(n+1)(n!)^2.

The function and all derivatives vanish at the endpoints. Integrating and normalizing phi gives a step cutoff. Translating, dilating by fixed constants and multiplying finitely many such steps gives the real even bandpass p used in the source proof, with p=1 on 1<=|t|<=2 and support in 1/2<|t|<3. Its compact support and derivative bounds give

 ||p^(n)||_1<=C^(n+1)(n!)^2.

If k is its inverse Fourier kernel, integration by parts and n=floor(c sqrt(|x|)) imply

 |k(x)|<=C exp(-c sqrt(|x|)),
 integral_(|x|>=R)|k(x)|dx<=C exp(-c sqrt(R)).                   (G1)

The polynomial prefactor from integrating the pointwise bound is absorbed by decreasing c.

Similarly choose the spatial cutoff chi_R, equal to 1 on [-R,R] and zero outside [-R-1,R+1], so that

 ||chi_R^(n)||_infinity<=C^(n+1)(n!)^2

with constants independent of R>=1. For a_R(x)=exp(eta x)chi_R(x), |eta|<=A fixed, Leibniz' rule gives

 ||a_R^(n)||_1
 <=C_A(R+1)exp(A(R+1))C_A^n(n!)^2.

The same integration-by-parts optimization gives

 ||ahat_R 1_(|xi|>=N/2)||_1
 <=C_A(R+1)exp(A(R+1))exp(-c_A sqrt(N)).                         (G2)

These are ordinary unweighted source Fourier estimates.

## 19. Error absorption at a single explicit scale

Retain ell=log(e/kappa), delta_kappa=delta_*/ell, and the actual four-point bound (D6) C kappa ell^2. Cut the fixed kernel in (G1) off at |s|<=delta_kappa, exactly as before. Its multiplier leakage is now

 ||chat_(N,kappa)-p(./N)||_infinity
                    <=C exp[-c sqrt(N/ell)],                  (G3)

while its first absolute kernel moment remains at most C/N. The full source identity consequently still has the upper bound C kappa ell^2/N^2. The complete high-frequency lower bound has errors

 C log(N)exp[-c sqrt(N/ell)] +C exp[-c_0(log N)^2].              (G4)

There is a fixed C_*>0 such that both errors in (G4) are at most C kappa ell^2/N^2 for every

 N>=exp(C_* sqrt(ell)).                                        (G5)

For the second error, enlarge C_* so c_0(logN)^2>=ell+3logN+O(1). For the first, put X=logN. In the stated range ell<=X^2/C_*^2 and

 sqrt(N/ell)>=C_* exp(X/2)/X.

After enlarging C_*, this quantity times c dominates ell+3X+O(logell) for every X>=C_*sqrt(ell). The exponential dominates the required fixed polynomial uniformly after the lower X threshold is increased. This proves the first absorption as well.

Hence the real-axis estimate (D11) becomes

 integral_(|t|>=N)|fhat(t)|^2dt/(2pi)
       <=C kappa ell^2/(N^2 logN),
                      N>=exp(C_*sqrt(ell)),                    (G6)

including the dyadically summed tail. The original form domains are the same as in the shrinking-radius proof; replacing a smooth bandpass by the specified smoother one changes no domain assertion.

## 20. Finite-strip transfer without losing the explicit scale

Choose R by exp(2R)=D(ell+logN), as in Section 15. The theta envelope gives an outside weighted-source error at most C_A kappa N^(-4). For the low-input-frequency term use (G2), rather than an unspecified fixed inverse power. In the range (G5), exp(-c_A sqrtN) dominates kappa times every fixed power of N, ell and R after increasing C_* depending on A. Thus all low-input and exterior errors can be absorbed into

 C_A kappa ell^2/[N^2 logN].

The high-input term is still bounded by exp(2A(R+1)) times (G6). Retaining the dependence on ell rather than replacing it by a power of logN gives

 integral_(N<=|t|<=2N)|(exp(eta x)f)hat(t)|^2dt/(2pi)
 <=C_A kappa ell^2(ell+logN)^A/[N^2 logN],
 |eta|<=A,              N>=exp(C_A sqrt(ell)).                  (G7)

A fixed enlargement of the threshold handles the input N/4 and the finitely enlarged dyadic intervals used in the sampling argument.

## 21. Full actual samples and the signed reduction

Take A=1 and use the same analytic disks and unconditional unit-height multiplicity count as in Section 16. The extra factor logN from the count cancels the denominator in (G7), giving

 sum_(N<=gamma_z<2N)j_z|B(z)|^2
 <=C kappa ell^2(ell+logN)/N^2,
                         N>=exp(C sqrt(ell)).                  (G8)

The sum runs over the entire genuine positive-height zero set, including both conjugate members. Consequently

 sum_(gamma_z>=T)j_z|B(z)|^2
 <=C kappa ell^2(ell+logT)/T^2,                                 (G9)

 sum_(gamma_z>=T)j_z log(2+gamma_z)|B(z)|^2
 <=C kappa ell^2(ell+logT)logT/T^2,                            (G10)

 sum_(gamma_z>=T)j_z|B(z)|
 <=C sqrt(kappa)ell sqrt((ell+logT)logT)/sqrt(T),                (G11)

for T>=exp(C sqrt(ell)). The dyadic sums are geometric with only fixed polynomial/logarithmic factors.

For a real ground-perpendicular negative state, the high off-line imaginary sampling squares therefore satisfy

 N_high(T)<=C kappa ell^2(ell+logT)/T^2.

In the range T>=exp(C sqrt(ell)), enlarging the same fixed C makes the factor multiplying kappa at most 1/2: with X=logT, ell<=X^2/C^2 and the remaining factor is bounded by a fixed polynomial in X times exp(-2X). Thus the complete actual identity gives

 kappa/2+P_all(u)<=N_off,gamma<T(u),
                   T>=exp(C sqrt(log(e/kappa))).               (G12)

This is an explicit subpower height, not a fixed height independent of depth. It still leaves exactly the low-height signed comparison unresolved.

A precise depth/height consequence is: if there is no off-line zero below a height G large enough for the constants, any nonground negative eigenvalue -kappa must obey

 kappa<=e exp[-c(log G)^2].                                    (G13)

Indeed (G12) would otherwise force an active off-line zero below G. This is only a quantitative implication; it neither supplies a zero-free height nor contradicts the possible existence of arbitrarily shallow negative eigenvalues.


---

The same depth-free source estimates also control the whole near-critical strip. Combining that bound with the high-tail reduction leaves the actual signed inequality on a finite region bounded away from the critical line by a depth-dependent distance. Equation labels (R1)–(R8) refer only to the following final continuation.

## 22. Original single-state setting and inputs

Let Hu=-kappa u be an original real even negative eigenstate, normalized by ||u||_2=1, with 0<kappa<=1/2 and orthogonal to the distinguished ground. Let f=mu and

 B(z)=integral_R f(x)cos(zx) dx.

The actual signed identity is

 kappa+P_all(u)=N_off(u),
 P_all=sum_critical 2j_z|B(gamma_z)|^2+sum_off-pair 4j_z b_z^2,
 N_off=sum_off-pair 4j_z c_z^2,
 B(gamma_z+i eta_z)=b_z-i c_z, 0<eta_z<1/2.

There is one representative with eta_z>0 per positive-height conjugate pair, with its true multiplicity j_z. All sums retain all genuine zeros; no arbitrary interpolation family is substituted.

The depth-free theorem and unit-cell interpolation in Sections 1–9 give, for every fixed A,q and s<1,

 sup_(|eta|<=A)||exp(eta x)x^q f||_(H^s)<=C_(A,q,s).             (R1)

The genuine unit-height zero count including multiplicity is O(log(2+gamma)). The shrinking-propagation and Gevrey theorem in Sections 12–21 gives, with ell=log(e/kappa),

 sum_(all genuine z,gamma_z>=T)j_z|B(z)|^2
 <=C kappa ell^2(ell+log T)/T^2,
                     T>=exp(C_G sqrt(ell)).                  (R2)

By enlarging the fixed C_G, the high off-pair contribution is therefore <=kappa/4. This only changes the fixed constant in the existing threshold; no dependence on the eigenstate or depth is introduced.

## 23. A vertical-supremum sampling bound

For every fixed 0<=t<1,

 D_t(u):=sum_(off-pair reps) j_z(1+gamma_z)^(2t)
          sup_(|eta|<=1/2)|B'(gamma_z+i eta)|^2 <=C_t.          (R3)

This is slightly stronger than evaluation at the original zero points and pays the moving vertical points needed below.

Choose t<s<1. Since f is real and even, B is its entire Fourier transform in the +it convention used throughout. B' is the transform of i x f. For any center gamma+i eta with |eta|<=1/2, the analytic disk mean-value inequality at fixed radius 1/4 gives

 |B'(gamma+i eta)|^2
 <=C integral_(gamma-1/4)^(gamma+1/4)
       integral_(-3/4)^(3/4)|B'(xi+i v)|^2 dv dxi.             (R4)

The right-hand side is independent of eta, so it also bounds the vertical supremum. Upon multiplying by j_z(1+gamma_z)^(2t) and summing, the genuine unit-height multiplicity count bounds the overlap at any real xi by C log(2+|xi|). On the corresponding interval, 1+gamma_z is comparable to 1+|xi|; bounded heights are covered by the same constant. Thus the left side of (R3) is at most

 C integral_(-3/4)^(3/4) integral_R
        (1+|xi|)^(2t)log(2+|xi|)|B'(xi+i v)|^2 dxi dv.

The pointwise scalar bound

 (1+|xi|)^(2t)log(2+|xi|)<=C_(s-t)(1+xi^2)^s

and Plancherel reduce this to (R1) with q=1, A=3/4. This proves (R3). The proof makes no simplicity, spacing, or derivative-vanishing assumption. If eta=1/2 is included in the harmless supremum, the entire source transform is still defined there.

## 24. True imaginary squares in a narrow or height-weighted strip

Reality gives B(gamma) real. Hence, for 0<eta<=1/2,

 Im B(gamma+i eta)=integral_0^eta Re B'(gamma+i v) dv,
 |Im B(gamma+i eta)|^2
 <=eta^2 sup_(|v|<=1/2)|B'(gamma+i v)|^2.                      (R5)

For any d>0 define the actual near-line set

 A_t(d)={off-pair representatives: eta_z<=d(1+gamma_z)^t}.

Equations (R3)--(R5) imply the fully summed inequality

 N_(A_t(d))(u):=4sum_(z in A_t(d))j_z c_z^2
 <=4d^2 D_t(u)<=C_t d^2.                                    (R6)

The definition remains valid when d(1+gamma)^t exceeds 1/2; in that region every off-line pair simply belongs to A_t(d). There is no maximum-height restriction in (R6). The unweighted case t=0 gives the simpler whole-height narrow-strip estimate N_(eta<=d)<=C d^2.

Choose a fixed c_t>0 so small that C_t c_t^2<=1/4 and put

 d_kappa=c_t sqrt(kappa).

Then the complete near-line imaginary-square contribution is <=kappa/4.

## 25. Simultaneous actual signed absorption

Take

 T_kappa=exp(C_*sqrt(log(e/kappa))),

where the fixed C_* is large enough for the high-tail contribution in Section 22 to be <=kappa/4. Let

 R_(kappa,t)={off-pair reps: gamma_z<T_kappa,
              eta_z>c_t sqrt(kappa)(1+gamma_z)^t}.

The complement of R_(kappa,t) is contained in the union of the full high tail and A_t(d_kappa). Counting an intersection twice only enlarges this nonnegative upper bound. Therefore (R2) and (R6), applied to the SAME actual eigenstate, give

 kappa/2+P_all(u)
 <=sum_(z in R_(kappa,t))4j_z c_z^2.                          (R7)

Every positive square in the original identity is preserved. In particular R_(kappa,t) contains at least one genuine off-line zero with a nonzero imaginary sample.

For t=0 this is the finite rectangle

 0<gamma_z<exp(C_*sqrt(log(e/kappa))),
 c_0 sqrt(kappa)<eta_z<1/2.                                  (R8)

For t>0 the stronger curved lower boundary retains the same upper height. Both constants are uniform over the normalized scalar negative eigenstates. Formula (R7) is not a uniform source estimate on mixtures of different eigenvalues; normalization and the scalar Hu=-kappa u input remain essential.

## 26. Exact scope of the remaining comparison

This removes two nonnegative portions of the actual negative-square sum relative to the existing kappa: the full high-height piece and the complete near-critical-line piece. It does not sign the remaining finite rectangle or control the actual low--high mixed source Gram. The original reconstruction coefficients remain a_z=-2j_z B(z)/kappa, and no inverse-depth factor has been discarded.

A sufficient still-unproved comparison would be

 sum_(z in R_(kappa,t))4j_z c_z^2<=P_all(u)

for every such actual state; (R7) would then be contradictory. No such inequality is obtained here. The active region depends on the unknown depth. As kappa tends to zero, the excluded near-line strip becomes thinner, so the active region approaches the critical line while its upper height grows. In particular this theorem does not exclude arbitrarily shallow negative spectrum or prove RH.
