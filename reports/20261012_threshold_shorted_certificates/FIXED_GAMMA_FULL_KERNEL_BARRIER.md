# Fixed finite-Gamma comparison: an obstruction even after shorting on the entire true kernel

For every fixed finite Gamma index J, the complete-prime diagonal lower comparison retains infinite negative inertia after exact shorting on ANY closed subspace of the actual original ker H, including the whole kernel. The conclusion allows arbitrary rank and also zero scalar penalty, interpreted by the exact variational infimum. Its finite-dimensional witnesses have strictly POSITIVE original-H energy. Thus the theorem obstructs this lower-comparison method; it does not produce a negative vector for H.

More precisely, for each k there is one k-dimensional original, ground-perpendicular subspace on which every such corrected comparison is strictly negative, simultaneously for all scalar penalties delta>=0 and every closed Z contained in ker H. The same subspace remains negative after adding epsilon I for all sufficiently small positive epsilon, with a bound depending on its actual Hilbert Gram. All primes and prime powers are retained throughout.

The finite-Gamma index is fixed. This theorem does not rule out J=J(epsilon) tending to infinity or a reference operator retaining the full Gamma multiplier. The certified original gap 511/1024 is unchanged. No zeta zero is excluded, and no RH conclusion is asserted.

## Provenance and exact scope relative to prior shorting results

The shorting construction is the user's [threshold-defect correction](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a3720b966577d0f7d23332eafe884ea69eaf8569/reports/20261012_threshold_shorted_certificates/REPORT.md), extended by the user's [countable correction](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a3720b966577d0f7d23332eafe884ea69eaf8569/reports/20261012_threshold_shorted_certificates/COUNTABLE_CORRECTION.md). The user's new [exact essential-band theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a3720b966577d0f7d23332eafe884ea69eaf8569/reports/20261012_fixed_shortening_essential_band/ESSENTIAL_SPECTRUM_COUNTABLE_SHORTING.md) treats its selected infinite theta space at fixed finite J,N and positive omitted-prime allowance. That exact band and trace-class conclusion retain their user attribution.

The user's subsequent [quantitative prime-two depth theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/b719cc94ad14b9b09f914f892a08d96565236d8a/reports/20261012_fixed_shortening_essential_band/QUANTITATIVE_PRIME_TWO_GAMMA_DEPTH.md) gives a necessary superpolynomial Gamma-depth policy for that selected-space, finite-prime comparator, uniformly in its finite prime cutoff. This separate quantitative result retains its user attribution; the theorem below concerns fixed J and makes no quantitative claim for J(epsilon).

The present theorem concerns a different, stronger correction class for a different complete-prime comparison: no omitted-prime penalty is necessary, the correcting space may be the ENTIRE true kernel, and even the delta=0 variational correction still leaves arbitrarily many negative directions. It does not repackage the fixed positive-penalty essential-spectrum argument, and it does not assert an essential-spectrum formula for the zero-penalty form.

The original Hilbert/form realization and the theta, Gamma and complete-prime conventions are those in the user's [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a3720b966577d0f7d23332eafe884ea69eaf8569/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). All additional source coercivity, Fourier evaluation, division-vector and shorting lemmas needed here are proved in Appendices A–D below. In particular no claim that the known theta derivatives exhaust ker H is assumed. The only zero-existence input is the unconditional infinitude of simple critical-line zeros, cited from Conrey's original theorem in Section 3. The [independent review](REFEREE_FIXED_GAMMA_FULL_KERNEL_BARRIER.md) checks this precise domain and scope.

## 1. Original objects and exact correction

Retain the actual original even Hilbert space, H=B-V, normalized ground g0, and Lhat=H+I/2. Fix one finite J>=1. Use the complete, untruncated prime defect and bounded comparator constructed in Appendix A:

 A0=(c_J-C0)m^2-p_infinity-m R_J m,
 D0=H-A0>=0,
 d0[v]=beta_J[mv]+sum_(n>=2) alpha_n integral m(x)m(x+log n)
                            |v(x+log n)-v(x)|^2 dx,
 beta_J=b-b_J, c_J=sum_(j<J)1/(j+1/4).

All primes and prime powers are retained. The reviewed full-prime bound Sm(x)<=C(1+|x|)exp(|x|/2), together with the actual theta tail, gives p_infinity in C0 intersect L-infinity. Each R_J kernel is integrable, m is bounded, and hence A0 is bounded selfadjoint. Therefore D0=H-A0 has the same operator domain as H, is selfadjoint, and its nonnegative closed form has the same form domain as B. These boundedness facts do not require Sm itself to be bounded. Fourier transform is F_v(z)=integral mv exp(-izx)dx, with inverse factor 1/(2pi).

Let Z be ANY closed original-Hilbert subspace of ker H, including Z=ker H itself. For delta>0 the actual bounded shorting correction F_(delta,Z) is defined by the compressed positive defect D_delta=D0+delta I. The exact residual is

 r_(delta,Z)[v]=d_delta[v]-<v,F_(delta,Z)v>
              =inf_(w in Z){d0[v-w]+delta||v-w||^2}.       (1)

Here D_delta w=(-A0+delta I)w on Z, so its column map is bounded and its compressed Gram is >=delta I. In particular ||F_(delta,Z)||<=(||A0||+delta)^2/delta; this is a genuine bounded selfadjoint correction on the full original Hilbert space. The corrected comparison is

 a_(delta,Z)[v]=<v,(A0-delta I+F_(delta,Z))v>
              =H[v]-r_(delta,Z)[v].                       (2)

At delta=0 define r_(0,Z) directly by the infimum in (1), and define a_(0,Z)=H-r_(0,Z) on Q(H). This is a legitimate variational form statement even if an unregularized correction has no bounded-operator realization. Any claimed operator realization with this variational shorting has the same finite-dimensional negative directions below.

## 2. Actual defect-energy Fourier evaluations become small at large real height

Write alpha=log2/sqrt2 and W2(x)=alpha[m(x+log2)+m(x-log2)]/m(x). The explicit source coercivity and spatial-tail bounds proved in Appendix B are

 beta_J[f]<=d0[v],
 ||f||_2^2<=d0[v]/lambda,
 integral W2|f|^2<=(1+2alpha/lambda)d0[v], f=mv,             (3)

where a=J+1/4 and lambda=1/[16a(1024a^2+1)]. For |x|>=1,

 W2(x)>=64alpha exp[15(|x|-1)].                            (4)

For gamma>0 define the genuine evaluation dual norm

 e_J(gamma)=sup { |F_v(gamma)|^2 : v in Q(D0), d0[v]<=1 }.

It is finite and tends to zero as gamma tends to infinity. Here is an explicit proof with all three terms. For R>=1 set g(x)=1_(|x|<=R) exp(i gamma x), and split its Fourier transform into |t|<=gamma/2 and the complement. On the first region

 |ghat(t)|<=2/|gamma-t|,
 integral_(|t|<=gamma/2) |ghat(t)|^2 dt/(2pi)
 <=8/(3pi gamma).

Use the source L2 bound in (3) for this low-frequency term and the beta_J bound for the high-frequency term. The latter has ||g||_2^2=2R. The omitted spatial integral is bounded by (3)-(4). Consequently

 sqrt(e_J(gamma))
 <=sqrt[8/(3pi lambda gamma)]
   +sqrt[2R/beta_J(gamma/2)]
   +sqrt[(1+2alpha/lambda) exp(-15(R-1))/(480alpha)].       (5)

This statement initially uses beta_J(gamma/2)>0, which holds for every gamma>0. To display convergence explicitly, put

 ell_gamma=(1/2)log(1+gamma^2)-c_J,
 R_gamma=1+(1/15)log(1+ell_gamma)

when ell_gamma>0. The original b lower bound and b_J<=c_J imply beta_J(gamma/2)>=ell_gamma. Squaring (5) using (x+y+z)^2<=3(x^2+y^2+z^2) gives

 e_J(gamma)<=3[8/(3pi lambda gamma)
               +2R_gamma/ell_gamma
               +(1+2alpha/lambda)/(480alpha(1+ell_gamma))]
            =O_J(log log gamma/log gamma) ->0.            (6)

The scalar c_J in ell_gamma remains the finite Gamma sum; e_J(gamma) is the distinct evaluation dual norm. These estimates concern actual original inputs, not a formal source domain substitution.

For every simple critical-line ordinate used below, Appendix C first constructs an actual domain vector w_gamma with H w_gamma=2m cos(gamma x). Appendix D then uses self-adjointness to prove F_w(gamma)=0 for EVERY w in the actual ker H. This argument does not use a prior full-kernel classification. Thus for any finite list of these simple ordinates gamma_1,...,gamma_k and every v in Q(D0),

 sum_(j=1)^k |F_v(gamma_j)|^2
 <=[sum_(j=1)^k e_J(gamma_j)] d0[v-w]  for every w in Z.   (7)

No original-norm or energy completeness of theta jets is assumed here.

## 3. Exact positive original-H witnesses supported on simple real zeros

There exist unconditionally infinitely many SIMPLE critical-line zeros. Only this classical existence is used, not a numerical certificate or RH. A primary source is J. B. Conrey, More than two fifths of the zeros of the Riemann zeta function are on the critical line, J. reine angew. Math. 399 (1989), Theorem 1, with the simple-zero count defined in equation (11): https://aimath.org/~kaur/publications/24.pdf . The PDF explicitly distinguishes simple critical zeros. Its existence consequence suffices here.

For a positive simple real zero gamma of Xi(z)=xi(1/2+iz), set

 A_gamma=2gamma/[(gamma^2+1/4) Xi'(gamma)],
 F_gamma(z)=A_gamma (z^2+1/4) Xi(z)/(z^2-gamma^2).          (8)

The singularities at +/-gamma are removable. This transform is real-even, F_gamma(gamma)=F_gamma(-gamma)=1, vanishes at every other actual Xi zero, and vanishes at +/-i/2.

These are genuine original operator-domain sources, not arbitrary entire interpolants. For x>=0 define

 g_gamma(x)=gamma^(-1) integral_x^infinity
                 sin(gamma(y-x)) Phi(y)dy.

Then g_gamma''+gamma^2 g_gamma=Phi, and g_gamma'(0)=-Xi(gamma)/2=0. Its even extension is smooth, and all derivatives have the true theta double-exponential tail. Fourier transformation gives ghat_gamma=-Xi(z)/(z^2-gamma^2). Thus

 f_gamma=-A_gamma(-partial_x^2+1/4)g_gamma,
 w_gamma=f_gamma/m

realizes (8). The complete original weighted-domain proof is given in Appendix C: f_gamma is H2 with weighted derivative bounds, f_gamma/m is original L2, b(D)f_gamma is L2, and w_gamma belongs to D(B)=D(H). The zero at +/-i/2 gives w_gamma perpendicular to g0.

The complete source explicit formula proved for this input in Appendix C, retaining multiplicities and both signs, now reduces exactly to

 H w_gamma=2m cos(gamma x).                               (9)

Therefore, for distinct chosen simple critical ordinates,

 <w_(gamma_i),H w_(gamma_j)>=2 delta_(i,j),
 F_(w_(gamma_i))(gamma_j)=delta_(i,j).                    (10)

In particular every nonzero vector in their finite span has STRICTLY POSITIVE original H energy. These are not negative witnesses for H.

## 4. Infinite negative inertia of every such fixed-J corrected comparison

Fix an arbitrary positive integer k. By (6) and the existence of arbitrarily large simple critical ordinates, choose distinct gamma_1,...,gamma_k so that

 sum_(j=1)^k e_J(gamma_j)<1/4.

For v=sum_j a_j w_(gamma_j), (7) and the variational formula imply, simultaneously for every closed Z subset ker H and every delta>=0,

 r_(delta,Z)[v]>=4 sum_j |a_j|^2,
 H[v]=2 sum_j |a_j|^2,
 a_(delta,Z)[v]<=-2 sum_j |a_j|^2.                       (11)

The vectors are linearly independent by their interpolation values and are all ground-perpendicular. Since k was arbitrary, the corrected comparison has infinite negative inertia on the original ground-perpendicular form domain. For delta>0 it is a bounded selfadjoint operator and the statement has its ordinary operator meaning. For delta=0 it is a finite-dimensional form conclusion, not an assertion of an unproved operator realization.

There is also a uniform positive-epsilon statement. Let G_k be the finite positive original Hilbert Gram of the w_(gamma_j). If

 0<epsilon<2/||G_k||,

then a_(delta,Z)+epsilon I is strictly negative on their k-dimensional span, for ALL delta>=0 and ALL such Z, including the entire actual kernel. Thus choosing a growing number of kernel columns, or even the full kernel from the start, does not permit a fixed finite Gamma J to certify all epsilon>0 through this comparison.

The bound depends on J and k. This does not rule out J=J(epsilon) tending to infinity, a different threshold-preserving full-Gamma base, or the previously published exact-full-Gamma finite certificates. It is independent of a fixed scalar-penalty negative-essential-spectrum argument and applies even at zero penalty. The obstruction uses actual positive-H vectors at known real zeros, so it is compatible with RH being true.


## Definitions used in the self-contained appendices

We use the original realization proved in ORIGINAL_FORM_FOUNDATION.md, cited above: B=M_m b(D)M_m>=0, bounded selfadjoint V=C0 m^2+m S m, H=B-V, and its closed associated form. Here the even positive theta source is

 Phi(x)=sum_(n>=1)[4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2)]
                         exp[-pi n^2 exp(2x)]  (x>=0),
 omega=2cosh(x/2), m^2=Phi/omega,
 b(t)=Re psi(1/4+it/2)-psi(1/4), C0=-psi(1/4)+log pi,
 (Sf)(x)=sum_(n>=2) alpha_n[f(x+log n)+f(x-log n)],
 alpha_n=Lambda(n)/sqrt(n).

Phi is extended by its genuine theta evenness. Fourier transform is hat f(t)=integral f(x)exp(-itx)dx; the inverse has factor 1/(2pi). The original ground vector is g0=Phi/m=m omega. Hilbert inner products are conjugate-linear in the first argument.

## Appendix A. Full-prime comparison and closed form

The elementary theta bounds on both half-axes are

 c exp(4|x|-pi exp(2|x|))<=m(x)^2
 <=Astar exp(4|x|-pi exp(2|x|)),
 c=2pi^2-3pi>9, Astar=4pi^2(125/121)<49.                 (A1)

For the lower bound retain the n=1 positive summand and use omega<=2exp(|x|/2). For the upper bound drop the negative theta summands, use omega>=exp(|x|/2), and bound sum n^4 exp[-pi(n^2-1)]<125/121. One elementary check is n^4<=16^(n-1), n^2-1>=3(n-1), and 16exp(-9)<1/500; the resulting geometric sum is below 500/499<125/121.

No prime-number theorem is needed to see

 Sm(x)<=C(1+|x|)exp(|x|/2).                              (A2)

Indeed alpha_n<=log n/sqrt n. In each group k<=log n<k+1 the sum of these upper bounds is at most C(k+1)exp(k/2). For x>=0 the negative shifts are therefore bounded by

 C exp(x/2) sum_(k>=0)(1+x+|k-x|) exp((k-x)/2)
                       sup_(z in [k-x,k+1-x])m(z).

The unit-lattice sum and its |k-x| weighted version are uniformly bounded in the fractional part of x by (A1). Positive shifts satisfy the same bound; evenness gives x<0. Local uniform convergence follows from the same estimates. Thus p_infinity=m Sm belongs to C0(R) intersect L-infinity.

For fixed finite J put

 c_J=sum_(j=0)^(J-1)1/(j+1/4),
 R_J(x)=sum_(j=0)^(J-1)exp[-(2j+1/2)|x|],
 b_J(D)=c_J I-R_J*, beta_J=b-b_J.

The digamma series gives

 beta_J(t)=sum_(j>=J) t^2/[(j+1/4)(4(j+1/4)^2+t^2)]>=0.  (A3)

The same series with J=0 gives b. For fixed t, its summand decreases in a=j+1/4, so comparison with the integral from a=1/4 to infinity gives b(t)>=log(1+4t^2)/2. Also b_J(t)<=c_J because the Fourier transform of every summand of R_J is nonnegative. Each summand of beta_J increases with |t|. These facts justify the frequency-tail lower bounds used in Section 2.

R_J is integrable and m is bounded. Hence

 A0=(c_J-C0)m^2-p_infinity-m(R_J*)m

is bounded selfadjoint. Expanding the prime squares, with the absolute bound by 2 integral p_infinity|v|^2, gives on the original form domain

 H[v]-<v,A0v>
 =beta_J[mv]+sum_(n>=2)alpha_n integral m(x)m(x+log n)
                                |v(x+log n)-v(x)|^2 dx.  (A4)

The full prime-edge form is bounded nonnegative on original L2. Since m b_J(D)m is bounded, the right side is a closed nonnegative form on Q(B). Its operator is D0=H-A0 with D(D0)=D(H)=D(B). This supplies both the complete-prime domain and the bounded comparison used by the main theorem.

For any closed Z subset ker H and delta>0, C_delta=(D0+delta I)|Z=(-A0+delta I)|Z is bounded, and E_delta=P_Z C_delta>=delta I_Z. Thus

 F_(delta,Z)=C_delta E_delta^(-1) C_delta*,
 ||F_(delta,Z)||<=(||A0||+delta)^2/delta.

Completing the positive quadratic form gives exactly

 d0[v]+delta||v||^2-<v,F_(delta,Z)v>
 =inf_(w in Z){d0[v-w]+delta||v-w||^2}.                  (A5)

This proof works for infinite-dimensional Z; it uses no basis completeness claim.

## Appendix B. Explicit source coercivity and spatial tail

Let alpha=log2/sqrt2 and W2(x)=alpha[m(x+log2)+m(x-log2)]/m(x). For f=mv, the source form consisting of beta_J and just the prime-2 square is

 t_J[f]=beta_J[f]+integral W2|f|^2
                    -2alpha Re integral conjugate(f(x))f(x+log2)dx.

It is nonnegative and at most d0[v]. From (A1), for x>=1>log2,

 W2(x)>=alpha (3/28)exp[(9/8)exp(2x)]
        >64alpha exp[15(x-1)].                         (B1)

Indeed sqrt(c/Astar)>3/7 and the shift contributes exp(-2log2)=1/4. The exponent is (3pi/8)exp(2x)>(9/8)exp(2x). At x=1, use e^2>7, e>8/3 and (3/28)(8/3)^7>64. The logarithmic derivative is (9/4)exp(2x)>15. Evenness gives the same bound with |x|.

Write a=J+1/4 and lambda=1/[16a(1024a^2+1)]. The j=J term of (A3) at t=1/16 is exactly 16lambda. Suppose ||f||_2=1 and t_J[f]<lambda. Since the prime square is nonnegative, beta_J[f]<lambda, and the Fourier mass beyond |t|=1/16 is less than 1/16. Also

 integral W2|f|^2<=t_J[f]+2alpha<lambda+2alpha<4alpha,

because lambda<2alpha. By (B1) the spatial mass outside [-1,1] is less than 1/16. Let P=1_[-1,1] and Q be the Fourier projection to [-1/16,1/16]. The exact bound

 ||PQ||^2<=||PQ||_HS^2=1/(8pi)<1/16

implies ||Pf||<1/4+1/4=1/2, whereas the spatial mass bound implies ||Pf||>=sqrt(15/16)>1/2. This contradiction proves

 ||mv||_2^2<=d0[v]/lambda,
 beta_J[mv]<=d0[v],
 integral W2|mv|^2<=(1+2alpha/lambda)d0[v].               (B2)

Integrating (B1) on both tails gives, for R>=1,

 integral_(|x|>R) 1/W2(x) dx
 <=exp[-15(R-1)]/(480alpha).                            (B3)

These are precisely the estimates used in the main theorem. The two positive terms of t_J were not both bounded directly by t_J: the spatial estimate separately pays the bounded shift term.

## Appendix C. Genuine division sources and their full original operator value

Let gamma>0 be any simple real zero of Xi(z)=xi(1/2+iz)=hat Phi(z). On x>=0 define

 g(x)=gamma^(-1) integral_x^infinity sin(gamma(y-x))Phi(y)dy.

Then g''+gamma^2 g=Phi and g'(0)=-Xi(gamma)/2=0. The even extension is smooth, including all odd derivatives at zero. Its transform satisfies

 ghat(z)=-Xi(z)/(z^2-gamma^2).                           (C1)

For domain control put a_x=2pi exp(2x)-9/2. The theta upper bound is Phi(x)<=2Astar exp(9x/2-pi exp(2x)). Its logarithmic derivative is at most -a_x on y>=x. Since |sin(gamma s)/gamma|<=s and |cos(gamma s)|<=1,

 |g(x)|<=2Astar exp(9x/2-pi exp(2x))/a_x^2,
 |g'(x)|<=2Astar exp(9x/2-pi exp(2x))/a_x                (C2)

for all sufficiently large x. The ODE and its derivatives control every higher derivative; the same holds on the negative half-axis. Set

 A_gamma=2gamma/[(gamma^2+1/4)Xi'(gamma)],
 f_gamma=A_gamma[Phi-(gamma^2+1/4)g], w_gamma=f_gamma/m.

Then (C1) gives

 F_gamma(z)=hat f_gamma(z)
          =A_gamma(z^2+1/4)Xi(z)/(z^2-gamma^2).           (C3)

It equals 1 at +/-gamma and 0 at every other actual Xi zero and at +/-i/2. By (A1)-(C2), |w_gamma|^2 is bounded at infinity by a fixed constant times exp(5|x|-pi exp(2|x|)), so w_gamma is in original L2. Also f_gamma is H2 and has every exponentially weighted derivative in L1. Thus b(D)f_gamma belongs to L2, and the original associated-form definition gives w_gamma in D(B)=D(H). No formal entire function has been assigned an unjustified original norm.

For completeness the additive-coordinate Guinand--Weil identity, with this normalization, is

 sum_rho integral h(y)exp[(rho-1/2)y]dy
 =integral h(y)[exp(y/2)+exp(-y/2)]dy
  +integral [b(t)-C0] hat h(t)dt/(2pi)
  -sum_(n>=2)alpha_n[h(log n)+h(-log n)].                 (C4)

It holds for compact smooth h, with every nontrivial zero counted with multiplicity. This is the ordinary explicit formula after the change from multiplicative to additive coordinates; a primary reference is J.-F. Burnol, The Explicit Formula in Simple Terms, sections 1 and 3, https://arxiv.org/pdf/math/9810169 . Formula (C4), including its actual Gamma and prime constants, also underlies the published original form realization.

To apply it to h(y)=f_gamma(x-y), first multiply that function by expanding even smooth cutoffs. All derivatives of f_gamma have exponentially weighted integrable tails by (C2) and the ODE, so these cutoffs converge in H1 and in every fixed exponentially weighted derivative norm. Two integrations by parts bound the zero transforms uniformly by C/(1+|Im rho|)^2 in the critical strip. The unconditional count N(T)=O(T log(2+T)) makes their full zero sum absolutely convergent and permits dominated passage to the limit on compact x intervals. The prime tails converge there by the actual double-exponential envelope. The Gamma term converges distributionally, or in L2 through b(D):H1->L2.

Substituting h(y)=f_gamma(x-y) into (C4) and rearranging therefore proves the genuine distributional identity

 C f_gamma=b(D)f_gamma+P_gamma-Z_gamma,
 C=C0 I+S,
 P_gamma(x)=exp(x/2)F_gamma(-i/2)+exp(-x/2)F_gamma(i/2)=0,
 Z_gamma(x)=sum_rho F_gamma(-i(rho-1/2))exp[(rho-1/2)x]
          =2cos(gamma x).                               (C5)

Evenness makes the sign choice in the transform coordinates harmless; both +/-gamma appear. All other zero values vanish, and the chosen pair is simple. Multiplying by m, using the actual V and the just-proved original domain, yields exactly

 H w_gamma=2m cos(gamma x).                             (C6)

Consequently <w_(gamma_i),H w_(gamma_j)>=2delta_ij for distinct such zeros, and the pole values give <g0,w_gamma>=0.

## Appendix D. Why the evaluation vanishes on the entire unknown kernel

The main theorem needs only the chosen simple real-zero evaluations, not a full characterization of ker H. For ANY w in the actual ker H, including possible unknown multiple-zero-derived vectors, selfadjointness and (C6) give

 0=<H w_gamma,w>=2 integral m(x)cos(gamma x)w(x)dx
               =2F_w(gamma).                           (D1)

The last equality uses evenness. The integral is well-defined by Cauchy--Schwarz and m in L2. Thus no assertion that theta jets exhaust ker H, and no assumption about other zero multiplicities, is needed anywhere in the full-kernel shorting obstruction.
