# Pure prime-edge source evaluations and a full-kernel residual

The complete positive prime-edge energy E controls each real source evaluation after the actual ground moment is removed. More precisely, the explicit constants C_gamma in Section 1 satisfy, for every original even v in L2 and every real gamma,

    |F_v(gamma)-c_gamma<g0,v>|^2
        <=C_gamma(e_2[v]+e_3[v])<=C_gamma e[v],
    F_v(gamma)=integral m(x)v(x)exp(-i gamma x)dx.

Only the actual prime-two and prime-three edge energies are needed. The proof builds two weighted currents, using a zero-free strip of the complete theta multiplier and an elementary small-divisor estimate for log 3/log 2. It uses no Gamma remainder or assumed source spectral gap.

At an actual simple critical-line zero gamma0, the already proved full-kernel evaluation identity gives the consequence

    inf_(w in Z) e[v-w]>=|F_v(gamma0)|^2/C_gamma0

for every v perpendicular to g0 and every subspace Z of the entire true ker H. Compact original-domain witnesses make this lower bound positive, including a fixed witness in every original unit-norm energy ball with upper level greater than 1/2. This does not put such a witness in an unknown strictly subcritical spectral space, compare its residual against its H-energy, or prove negative inertia of the kernel-corrected comparator.

The optimal pure-edge evaluation constant has a POSITIVE large-height lower limit:

    liminf_(gamma->infinity)d_E(gamma)>=||m||_2^2/36.

Thus the vanishing-dual-norm argument for a defect with a fixed positive Gamma remainder cannot be transferred to this pure-edge form. These are continuity and residual theorems. They give no new spectral gap or zeta-zero exclusion, and the known 511/1024 bound is unchanged.

## Original realization and the exact public dependencies

Use the user's [original closed-form foundation](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/ca7be214e825dab063ea332a27e833b601d109e5/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), on complex even L2(R,dx):

    H=B-V, B=M_m b(D)M_m,
    V=C0m^2+M_m S M_m,
    S f(x)=sum_(n>=2)alpha_n[f(x+log n)+f(x-log n)],
    b(t)=Re psi(1/4+it/2)-psi(1/4),
    C0=EulerGamma+pi/2+3log 2+log pi.

B is defined by its closed associated form b[mv], and D(H)=D(B). The Fourier transform is integral f(x)exp(-itx)dx, with Plancherel measure dt/(2pi). The true normalized ground is g0=2cosh(x/2)m, with H g0=-g0/2. The complete-prime edge used below is the bounded positive operator

    E=M_p-M_m S M_m,
    p(x)=sum_(n>=2)alpha_n m(x)[m(x+log n)+m(x-log n)].

Its full row tail, positivity and bound E<18I are proved in [EXACT_PRIME_EDGE_CORRECTION.md, Appendix A](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/ca7be214e825dab063ea332a27e833b601d109e5/reports/20261012_adaptive_spectral_tail/EXACT_PRIME_EDGE_CORRECTION.md). The proof below does not use that report's finite-rank approximation. The original scalar envelopes

    9exp(4|x|-pi exp(2|x|))<=m(x)^2
        <=49exp(4|x|-pi exp(2|x|))

follow from the complete theta series as shown in [EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md, original normalization](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/ca7be214e825dab063ea332a27e833b601d109e5/reports/20261012_adaptive_spectral_tail/EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md). These are used only as theta bounds, not as a Gamma-energy estimate. The complex strip needed here is separately proved in full in Section 2.

Section 6 uses exactly the actual-domain simple-real-zero construction and self-adjointness implication in the publicly proved fixed-Gamma theorem's Appendices C–D, linked there. It does not import that theorem's finite-Gamma dual decay or its comparator conclusion. The user's original operator and theta constructions retain their attribution. The [independent mathematical review](REFEREE_PURE_PRIME_EDGE_EVALUATIONS.md) checks the entire current construction, domain, constants, full-kernel implication and positive large-height lower limit.

## 1. Original objects and the claimed estimate

Use the unchanged original even L2(dx) space and theta functions

 Phi(z)=sum_(n>=1)(4pi^2 n^4 exp(9z/2)-6pi n^2 exp(5z/2))
                         exp[-pi n^2 exp(2z)],
 m(x)=sqrt(Phi(x)/(2cosh(x/2))),
 g0(x)=2cosh(x/2)m(x).

The established even theta identity is retained. The positive original ground vector is g0; its normalization has no effect on the orthogonality condition below. The exact complete edge energy is

 e[v]=sum_(n>=2)alpha_n integral m(x)m(x+log n)
                              |v(x+log n)-v(x)|^2 dx,
 alpha_n=Lambda(n)/sqrt(n).

It is the bounded positive form already established on original L2. Write e_2 and e_3 for its prime-2 and prime-3 summands. They satisfy e_2+e_3<=e. Define the source transform

 F_v(gamma)=integral m(x)v(x)exp(-i gamma x)dx.

All such integrals are well-defined for v in L2. For real gamma, set

 c_gamma=(integral m(x)cos(gamma x)dx)/(integral g0(x)dx),
 B_gamma=18(exp(|gamma|/6)+1),
 mu(R)=3 exp(2R-(pi/2)exp(2R)),
 C_gamma=5000+12(24+8B_gamma)^2/mu(3)^2
                      +32B_gamma^2/mu(2)^2.           (1)

The conclusion is the completely explicit bound

 |F_v(gamma)-c_gamma<g0,v>|^2<=C_gamma e[v]             (2)

for every original even v in L2 and every real gamma. In particular, on the ground-perpendicular space,

 |F_v(gamma)|^2<=C_gamma e[v].                         (3)

The inner product is conjugate-linear in its first entry. Since g0 is real, <g0,v>=integral g0 v. Evenness replaces exp(-i gamma x) by cos(gamma x) in F_v.

## 2. A zero-free theta strip and a uniform Fourier bound

We first verify the analytic input instead of assuming that the real square root m has a global complex branch. The original Phi series converges normally on compact subsets of |Im z|<pi/4. Its real even identity extends there by analytic continuation.

Let z=x+iy, x>=0, |y|<=1/6, and u=exp(2z). Then |u|>=1 and cos(2y)>=17/18. The first theta term is

 Phi_1(z)=2pi exp(5z/2)(2pi u-3)exp(-pi u),

which is nonzero, since

 |2pi u-3|>=2pi Re u-3>=(8/3)|u|.

For n>=2 the ratio of the nth term to the first therefore satisfies

 |Phi_n/Phi_1|<=4n^4 exp[-(8/3)(n^2-1)].              (4)

Here pi>3, 2pi<7, |2pi n^2u-3|<8n^2|u|, and pi cos(1/3)>8/3 suffice. The first majorant term is 64exp(-8)<1/32: e>8/3 gives e^8>(8/3)^8>2^11. Successive majorant ratios for n>=2 are at most

 (3/2)^4 exp(-40/3)<1/100.

Hence the full relative tail in (4) is less than 1/16. Phi has no zero on this half-strip, and evenness proves the same on the other half. Also 2cosh(z/2) has no zero there. The simply connected strip therefore admits the analytic branch of m agreeing with its positive real values.

The first-term estimate and the same tail bound give

 |Phi(x+iy)|<=75 exp(9|x|/2)
                    exp[-pi cos(1/3)exp(2|x|)],
 |m(x+iy)|<=9 exp(2|x|)
                    exp[-(pi/2)cos(1/3)exp(2|x|)].    (5)

For the second inequality use |2cosh((x+iy)/2)|>=exp(|x|/2). The margin in (4) also permits a neighborhood of the closed strip, so contour shifts at |y|=1/6 are legitimate.

Put

 q_gamma(x)=m(x)cos(gamma x)-c_gamma g0(x).

Since g0(x)>=2m(x)>0, |c_gamma|<=1/2, and by definition integral q_gamma=0. With a=17pi/36>1, (5) gives on the shifted contours

 |q_gamma(x+iy)|
 <=9(exp(|gamma|/6)+1)exp(5|x|/2)exp[-a exp(2|x|)].

The integral of the last profile on R is at most 2. Indeed, putting s=exp(2x) on the positive half-axis bounds it by

 integral_1^infinity s^(1/4)exp(-a s)ds
 <=exp(-a)(1/a+1/a^2)<2.

Contour shifting in the Fourier integral therefore proves

 |qhat_gamma(t)|<=B_gamma exp(-|t|/6).                (6)

All normal convergence, contour-end errors and integrability here are paid by the displayed double-exponential envelope.

## 3. An elementary circle cohomology equation for log 2 and log 3

Set

 d=log 2, a=log 3,
 h(s)=sum_(k in Z)q_gamma(s+kd), 0<=s<d.

The sum and its holomorphic extension on the strip converge normally. It is d-periodic and has mean zero. Its Fourier coefficients are

 hhat_k=(1/d)qhat_gamma(2pi k/d), hhat_0=0.

We solve on this circle

 j(s-a)-j(s)=h(s),
 jhat_0=0,
 jhat_k=hhat_k/[exp(-2pi i k a/d)-1], k!=0.           (7)

No unproved Diophantine estimate is needed. For k>=1 choose an integer l nearest ka/d and let s=ka-ld. Then |s|<=d/2 and unique prime factorization gives |3^k-2^l|>=1. Since

 |3^k-2^l|=2^l|exp(s)-1|<=2*3^k|s|,

we obtain ||ka/d||>=1/(2d3^k), where ||.|| denotes distance to an integer. Therefore

 |exp(-2pi i k a/d)-1|>=2/(d3^k).                    (8)

Negative k follow by conjugation. Combining (6) and (8),

 |jhat_k|<=(B_gamma/2)
             exp[-(pi/(3d)-log 3)|k|].

The exponent is greater than 1/4: for example d<7/10, log 3<11/10 and pi>3 give pi/(3d)-log 3>23/70. Thus the series in (7) converges absolutely and defines a real periodic function, with

 ||j||_infinity<=B_gamma/(exp(1/4)-1)<4B_gamma.        (9)

Its Fourier series verifies (7) pointwise. This small-divisor step uses only two actual primes and the actual source analyticity from Section 2.

## 4. Lifting the circle solution to real weighted edge currents

Define the compactly supported prime-3 current

 J3(x)=j(x)1_[0,d)(x),
 q3(x)=J3(x-a)-J3(x),
 r(x)=q_gamma(x)-q3(x).

By (7), the d-periodization of r is zero. Define the prime-2 current

 J2(x)=sum_(k>=1)r(x+kd)
      =-sum_(k<=0)r(x+kd).                            (10)

Both sums converge absolutely; the equality follows from zero periodization. Direct telescoping gives

 q_gamma(x)=J2(x-d)-J2(x)+J3(x-a)-J3(x).              (11)

These are actual L2 currents. To prove their finite weighted energy and the constant in (1), we give both the compact and tail ledgers.

The real theta bound implies exp(|x|)m(x)<2: the upper envelope 7exp(3|x|-(pi/2)exp(2|x|)) decreases for |x|>=0 and is less than 2 at zero. Thus

 |q_gamma(x)|<=2exp(|x|/2)m(x)<=4exp(-|x|/2).

The maximum over a residue class of sum_(k in Z)exp(-|x+kd|/2) equals (sqrt(2)+1)/(sqrt(2)-1)<6. Hence the absolute periodized q sum is less than 24. A one-sided sum in (10) contains at most one contribution from each of the two length-d support intervals of q3, apart from irrelevant endpoints. Equations (9)-(10) therefore give

 |J2(x)|<=24+8B_gamma.                               (12)

On the central interval [-d,a+d], both endpoints x,x+d lie in [-3,3], and its length a+2d is less than 3. With alpha_2>1/4, its contribution to the prime-2 current cost is bounded by

 integral_[-d,a+d] |J2(x)|^2/[alpha_2 m(x)m(x+d)]dx
 <=12(24+8B_gamma)^2/mu(3)^2.                         (13)

Since J3 is supported in [0,d], its endpoints x,x+a lie in [0,2]. The inequalities d<1 and alpha_3>1/2 give

 integral |J3(x)|^2/[alpha_3 m(x)m(x+a)]dx
 <=32B_gamma^2/mu(2)^2.                              (14)

For the tails, put

 Q(t)=14exp(5t/2)exp[-(pi/2)exp(2t)], t>=0.

The real theta envelope and |c_gamma|<=1/2 give |q_gamma(x)|<=Q(|x|). For t>=d,

 Q(t+d)/Q(t)=2^(5/2)exp[-(3pi/2)exp(2t)]<1/2.

If x>=a+d, q3 is absent from the right-hand sum in (10), and

 |J2(x)|<=2Q(x+d).

Using the real lower theta envelope on both endpoints yields

 |J2(x)|^2/[alpha_2 m(x)m(x+d)]
 <=2800 exp(x)exp[-(9/2)exp(2x)].                     (15)

If x<=-d, write t=-x>=d and use the left-hand sum in (10). Again q3 is absent, and |J2(x)|<=2Q(t). The corresponding bound is

 |J2(x)|^2/[alpha_2 m(x)m(x+d)]
 <=1400 exp(t)exp[-(9/8)exp(2t)].                     (16)

For clarity, before relaxing constants in (15) the factor is (3136/9)exp(3d) exp(x)exp[-(3pi/2)exp(2x)]; in (16) it is (3136/9)exp(2d) exp(t)exp[-(3pi/8)exp(2t)]. Thus the stated factors follow from exp(d)=2 and pi>3. Each displayed exponential profile integrates to less than 1 on the relevant half-line, already if its lower endpoint is replaced by zero. The sum of both tail costs is less than 4200, and hence less than the allowance 5000 in (1).

Combining (13)-(16), the genuine current cost satisfies

 integral |J2|^2/[alpha_2 m(x)m(x+d)]dx
 +integral |J3|^2/[alpha_3 m(x)m(x+a)]dx<=C_gamma.     (17)

No prime Fourier multiplier has been declared positive, and no source-to-original-domain substitution is used. The currents are explicit functions with the correct one-sided theta tails.

## 5. Weighted summation by parts proves the evaluation estimate

For every v in original L2, equation (11) and ordinary L2 change of variables give

 integral q_gamma(x)v(x)dx
 =integral J2(x)[v(x+d)-v(x)]dx
   +integral J3(x)[v(x+a)-v(x)]dx.

Both pairings are absolutely controlled by (17) and their corresponding edge energies. Cauchy--Schwarz on the direct sum of the two edge spaces proves

 |integral q_gamma v|^2<=C_gamma(e_2[v]+e_3[v])
                        <=C_gamma e[v].             (18)

For even v, the left side is exactly the left side of (2). This proves (2)-(3) on the entire original even Hilbert space. No Gamma term, finite or complete, is needed for this continuity statement.

As an optional norm reformulation, B_gamma<=36exp(|gamma|/6), so C_gamma<=D exp(|gamma|/3), with the explicit constant

 D=5000+1168128/mu(3)^2+41472/mu(2)^2.

For ground-perpendicular v, integration of (3) gives

 ||exp(-|D_x|/3)(mv)||_2^2<=(3D/pi)e[v].              (19)

Here D_x is the source Fourier variable operator, and Parseval uses measure dt/(2pi). This is an exponentially smoothed source norm, not a source L2 spectral gap.

## 6. A genuine pure-edge residual that full-kernel shorting cannot erase

Let gamma0 be any actual positive SIMPLE critical-line zero ordinate. Such zeros exist unconditionally; the original primary source and its exact simple-zero hypothesis are recorded in Section 3 of the published [fixed-Gamma full-kernel theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md). Appendices C and D of that same source provide the precise full-kernel fact needed here. They construct an actual w_gamma0 in D(H) with H w_gamma0=2m cos(gamma0 x). Selfadjointness then gives, for every w in the entire actual ker H,

 0=<H w_gamma0,w>=2F_w(gamma0).

This includes any unknown additional kernel vectors. No exhaustion by theta jets or general multiple-zero kernel classification is assumed.

Such w are also ground-perpendicular. Let Z be any subspace of ker H, including its full closed kernel, and define the pure-edge residual variationally by

 r_Z[v]=inf_(w in Z)e[v-w].

No invertibility of the infinite kernel Gram is assumed. Equation (3) proves, for ground-perpendicular v,

 r_Z[v]>=|F_v(gamma0)|^2/C_(gamma0).                  (20)

This lower bound survives even after all Gamma tails have been removed.

It has concrete original-domain witnesses. Choose a nonnegative real even smooth bump psi of integral one, supported in |x|<r0 with r0<1/[4(1+gamma0)]. Set

 f0=(-partial_x^2+1/4)psi,
 v0=f0/m.

The compact support and positivity of m put v0 in the original operator domain. Integration by parts against g0/m=2cosh(x/2) gives <g0,v0>=0. Its source value is

 F_v0(gamma0)=(gamma0^2+1/4)psihat(gamma0)>0,

since psihat(gamma0)>31/32. Thus r_Z[v0] has a fixed strictly positive lower bound from (20), even for Z=ker H.

This can also be put into every original unit-norm energy ball strictly above the threshold. Write L0=H+I/2 and fix E0>1/2. For any nonzero actual k in ker H, let v_s=v0+s k. Then H[v_s]=H[v0], and for sufficiently large |s| the unit vector u=v_s/||v_s|| satisfies

 <u,L0u>=1/2+H[v0]/||v_s||^2<=E0,
 r_Z[u]>=|F_v0(gamma0)|^2/[C_(gamma0)||v_s||^2]>0.    (21)

Choose one such finite s; the bound is then independent of Z. This is a nonvanishing residual statement. It neither constructs a negative vector for H nor settles the actual strictly subcritical spectral subspace.

## 7. Precise scope

The result extends evaluation continuity from a defect containing a positive Gamma remainder to the pure complete prime-edge form on the ground-perpendicular space. The ground correction in q_gamma is essential: without it, approximately constant original vectors can have vanishing edge energy while a source evaluation need not vanish.

There is a further exact distinction from the finite-Gamma mechanism. Define the optimal ground-perpendicular evaluation constant

 d_E(gamma)=sup{ |F_v(gamma)|^2 : v perpendicular g0, e[v]<=1 }.

It is finite by (3), but cannot tend to zero at large real height. Let u_gamma be the original orthogonal projection of m cos(gamma x) onto g0-perp. Since E<=18I, testing with u_gamma/(sqrt(18)||u_gamma||), when it is nonzero, gives

 d_E(gamma)>=||u_gamma||^2/18,
 liminf_(gamma->infinity)d_E(gamma)>=||m||_2^2/36>0.  (22)

The limit follows from Riemann--Lebesgue applied to m^2 and m g0: ||m cos(gamma x)||^2 tends to ||m||^2/2 and its ground projection tends to zero. These products are integrable by the theta bounds. Thus one cannot transfer a finite-Gamma argument based on a vanishing evaluation dual norm to this pure-edge form.

The full-kernel pure-edge residual cannot disappear on all ground-perpendicular bounded-energy tests by a density argument alone. However, (20)-(21) do not prove negative inertia of the full-kernel-shorted critical comparison, do not show any actual negative spectral vector exists, and do not exclude a zero. In particular a nonzero residual on a positive-energy witness is not itself a failure of critical positivity. The remaining complementary sign is still open.
