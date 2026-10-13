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
