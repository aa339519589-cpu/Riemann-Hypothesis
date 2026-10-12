# Actual negative-band regularity, finite coverage and spectral summability

For the original complete-Gamma, signed full-prime even operator H=B-V, fix a positive depth 0<kappa<=1/2. The entire true spectral band Q_kappa=1_[-1/2,-kappa](H) has the explicit global regularity bound

    ||(1+D²)^(r/2)Q_kappa|| <= kappa^(-r/2-o(1))

for each fixed r>=0 as kappa tends to zero. The recursion below gives actual finite constants at each depth, without computing the unknown projection. The result includes arbitrary mixtures of different spectral parameters. It follows from weighted Fourier moments of the complete paired prime coefficients, a domain-safe quadratic commutator, and a positive Lyapunov inverse.

After removing the known ground, the same actual band localizes in one explicitly chosen central interval. A continuous even piecewise-polynomial space of any fixed degree p-1 covers every localized band vector to the required original Gamma-form accuracy, with

    rank <= kappa^(-1/2-1/p-o(1)), p>=2 fixed.

Equivalently, for every fixed epsilon>0 one may choose a fixed p and obtain rank <= C_epsilon kappa^(-1/2-epsilon) for sufficiently small positive depth. Constants, integer rounding, endpoint jumps and all source-domain conditions are paid explicitly. This is an upper cost for covering the actual negative band, rather than for covering every vector in a central energy ball.

The remaining sufficient test is the sign of the ENTIRE original signed finite matrix on this same growing space and at this same depth. That sign is not proved or computed here. A previously positive finite span cannot be substituted for it. The result gives no new spectral gap or zeta-zero exclusion and no uniform critical-depth sign.

The fixed-error version also yields an actual spectral counting bound and summability theorem, proved in Appendix A:

    dim Ran Q_kappa <= kappa^(-1/2-o(1)),
    (-Acrit)_+ belongs to S_a for every a>1/2.

Here Q_kappa has its known ground removed, Acrit=H+(1/2)|e0><e0|, and S_a has its usual quasi-norm interpretation for a<1. These statements permit nonzero negative spectrum; no endpoint S_(1/2) claim is made.

## Original realization and published inputs

The original closed form and normalization are the user's [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). We retain complex even L2(dx), Fourier measure dt/(2pi), the genuine theta multiplier, all prime powers, and the exact pole correction. The known normalized ground is e0=2m cosh(x/2), with H e0=-e0/2. The graph core and prime norm tail are in [REPORT.md, Sections 1 and 9](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/REPORT.md); the actual holomorphic theta strip is [ACTUAL_FULL_GAMMA_CERTIFICATE.md, Appendix B](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/ACTUAL_FULL_GAMMA_CERTIFICATE.md). The full-space D(R) and sharp Gamma cross E(R), including discontinuous-cutoff domain control, are proved in [SIGNED_PRIME_LOW_SPECTRUM.md, Sections 4–5](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/SIGNED_PRIME_LOW_SPECTRUM.md). Part II supplies the necessary new whole-band argument instead of inferring it from individual eigenvectors.

Parts I–III contain the complete new regularity, localization and approximation chain. Equation numbers and section numbers are local to each Part. The [independent review](REFEREE_ACTUAL_NEGATIVE_BAND_COVERAGE.md) covers the exact operator domain, whole-band mixing, and conditional finite-matrix criterion.

# Part I. Complete-prime Sobolev regularity on an actual negative band

## 1. Original objects and the result

Use the original even complex L2(R,dx) space, with Fourier transform fhat(t)=integral f(x) exp(-itx) dx and measure dt/(2pi). Let

    H=B-V, B=m b(D)m,
    b(t)=Re psi(1/4+it/2)-psi(1/4),
    V=C0 m² + sum_(n>=2) alpha_n m(tau_log n+tau_-log n)m,
    alpha_n=Lambda(n)/sqrt(n), C0=EulerGamma+pi/2+3log2+log pi<6.

All operators and forms have their original closed realizations; D(H)=D(B), and H>=-1/2. The original closed realization and even C_c^infinity graph core are proved in [REPORT.md, Sections 1 and 9](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/REPORT.md). The original full-prime norm tail is bounded by

    delta_N=(980/9)(N+1)² exp(-pi(N+1)), N>=2.

This is a harmless upward version of its sharper theta constant. Also

    c_N=C0+2 sum_(2<=n<=N) alpha_n <=6+4sqrt(N)log N,
    b(t)>= (1/2)log(1+4t²), ||m||_infinity<=2.

The holomorphic theta square root in [ACTUAL_FULL_GAMMA_CERTIFICATE.md, Appendix B](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/ACTUAL_FULL_GAMMA_CERTIFICATE.md) gives

    |m(x+iy)|² <=100 exp(4|x|-(3/2)exp(2|x|)), |y|<=1/2.

Fix 0<kappa<=1/2, and put Q=1_[-1/2,-kappa](H). One can also restrict Q by the original ground-state orthogonal projection. Let K=-H restricted to Ran Q, so kappa<=K<=1/2. Choose any integer N>=2 with delta_N<=kappa/2, and any T>=1 with b(T)>=c_N, for instance T=exp(c_N). Neither choice uses unknown spectral data.

For every fixed real s>=0 there is an explicit finite M_s(kappa), defined by the recursion and interpolation in Section 5 below, such that

    ||(1+D²)^(s/2) Q|| <= M_s(kappa).                    (1)

Thus each actual negative-depth spectral band maps L2 into every global Sobolev space, uniformly on its entire span. The result is not limited to single eigenvectors and does not choose or compute a basis of Q.

## 2. Completely explicit Fourier coefficient moments

Write <t>=sqrt(1+t²), and for a scalar coefficient a put

    a_p(a)=(1/(2pi)) integral <t>^p |ahat(t)| dt, p>=0.

For p>=0 define

    k(p)=ceil(p)+2,
    B_p=2^(p/2) [1+k(p)! 4^k(p)],
    A_p=14 B_p, P_p=800 B_p.

Then

    a_p(m)<=A_p,
    C0 a_p(m²)+2 sum_(n>=2) alpha_n a_p(m(x)m(x+log n))<=P_p. (2)

Here is a direct proof. The strip envelope gives integral |m(x+iy)|dx<40/3 and integral |m(x+iy)|²dx<25, uniformly for |y|<=1/2. For d=log n, n>=2, it gives

    integral |m(x+iy)m(x+d+iy)|dx
       <=100 n²(log n+1) exp(-3n/2)=:S_n.               (3)

On [-d,0], the product envelope is at most 100 n² exp(-3n/2). On the two exterior rays its integral is

    <=100 n² exp(-c)(1/c+1/c²), c=(3/4)(1+n²)>=3,

which is at most 100 n² exp(-3n/2). This proves (3). Cauchy's formula on radius 1/4 circles, followed by integration in x, bounds the L1 norm of the kth derivative of any of these coefficients by k!4^k times its respective strip L1 bound. Splitting the Fourier integral at |t|=1 and using |ahat(t)|<=min{||a||1,|t|^-k||a^(k)||1} gives

    a_p(a) <=(2^(p/2)/pi)[||a||1+||a^(k)||1], k=k(p).

Finally alpha_n<=log n/sqrt n and log n<=sqrt n imply

    2 sum alpha_n S_n <=400 sum_(n>=2) n³ exp(-3n/2)
                       <400 sum_(n>=2) n³/4^n
                       =400(149/108).

Adding 25 C0<150 gives a quantity below 800; 40/3<14. This proves (2), with deliberately coarse rational constants. The sum includes every prime power, not just a finite-prime approximation.

## 3. A uniform regularized commutator bound

For s>=1/2 and h>0 let L_(s,h) be the bounded even Fourier multiplier

    l_(s,h)(t)=<t>^s/(1+h<t>)^s.

Set q=s-1/2, p0=|s-1|+1, p1=p0+1/2, and

    c_s=s 2^(|s-1|/2),
    C_s=c_s [7 A_p0 2^(q/2) A_q
                    +14 2^(1/4) A_p1 +P_p0].          (4)

Uniformly in h>0,

    ||[H,L_(s,h)]v|| <= C_s ||v||_(H^q).               (5)

First, differentiation and the two-sided Peetre inequality give

    |l(t)-l(u)|
      <=c_s |t-u| <t-u>^|s-1| <u>^(s-1).             (6)

The positive digamma series gives b(t)<=4+(1/2)log(1+4t²)<=7<t>^(1/2). The first inequality follows by bounding the first summand by 4 and the rest by the decreasing-summand integral; the final bound follows from log(1+x)<=2sqrt x.

For the Gamma part, write

    [L,B]=[L,m]b(D)m +m b(D)[L,m].

Use (6), b(u)<=7<u>^(1/2), <t>^(1/2)<=2^(1/4)<t-u>^(1/2)<u>^(1/2), and Young's convolution inequality in the normalized Fourier convention. Multiplication by m on H^q has norm at most 2^(q/2)A_q. The two terms are consequently bounded by the first and second terms inside (4). For V, write each shifted term as a(x)tau_d. Since L commutes with translations, (6) bounds [L,a]tau_d from H^(s-1) to L2 by c_s a_p0(a). The embedding H^q into H^(s-1) and (2) prove the last term in (4), with absolute convergence over the complete prime series.

For each fixed h, these commutators are also bounded L2 to L2, with an h-dependent constant. Indeed |l'(t)|<=s h^(-s-1)<t>^-2, so the explicit difference bound is |l(t)-l(u)|<=2s h^(-s-1)|t-u|<t-u>²<u>^-2. The same convolution argument then absorbs the logarithmic symbol into a decaying power. L_(s,h) maps Schwartz functions to Schwartz functions. In particular it maps the original compact smooth graph core into D(H). The bounded commutator on that core, closedness of H, and graph-core approximation imply

    L_(s,h)D(H) subset D(H),
    H L_(s,h)v=L_(s,h)Hv+[H,L_(s,h)]v.                 (7)

Thus (5) is used only on a rigorously valid operator identity. It is not an unlicensed application of b(D) to an arbitrary original operator-domain source.

## 4. A low-frequency bound with no unknown regularity

For P_T=1_|D|<=T, define

    L_s(T)=2^(s/2)<T>^s A_s.

For every h>0,

    ||P_T m L_(s,h)||_(2->2)<=L_s(T).                  (8)

Indeed l(u)<=<u>^s and, on |t|<=T, <u>^s<=2^(s/2)<T>^s<t-u>^s. The weighted Fourier convolution kernel and Young's inequality give (8). This bound is on the entire original L2 space. In particular it does not assume that Q is already Sobolev regular.

The exact signed finite-prime terms, together with the norm of the complete omitted-prime tail, give for every w in the original form domain

    H[w]>=integral (b(t)-c_N)|hat(mw)(t)|² dt/(2pi)
                    -delta_N||w||²
          >=-c_N||P_T mw||²-delta_N||w||².             (9)

Here b(T)>=c_N and b is increasing. The inequality retains the positive full-Gamma high-frequency term; it does not discard the positive part of the entire finite-prime symbol.

## 5. Double-commutator bootstrap on the entire actual band

The exact quadratic commutator gives the sharp stated upper-cost scale while preserving the original operator domains. Every bounded regularized multiplier is first used on that domain, before any new regularity of the band is inferred.

Fix 1/2<=rho<1 and put beta=2(1-rho), so 0<beta<=1. The positive symbol bound can be sharpened in scale to

    b(t)<=G_beta <t>^beta,
    G_beta=4+2^beta/beta.                               (10)

Indeed b(t)<=4+log(1+2|t|), and log(1+x)<=x^beta/beta follows by integrating (1+x)^-1<=x^(beta-1). For s>=rho put q=s-rho>=0 and

    p=2+2|s-1|+q,
    D_(s,rho)=c_s² 2^(q/2)
       [G_beta 2^((beta+p)/2) A_p A_(p+beta)+P_p].       (11)

Then for every h>0 and v in H^q,

    |<v,[L_(s,h),[L_(s,h),H]]v>|
                         <=D_(s,rho)||v||_(H^q)².     (12)

This is a quadratic-form estimate, not an assertion that the double commutator has a uniform L2 operator norm for large s. For fixed h its operator is bounded on L2, as already proved in Section 3.

Here is the complete Fourier calculation. The double commutator multiplies the Fourier kernel of H between output t and input u by [l(t)-l(u)]². Divide the absolute kernel by <t>^q<u>^q and use (6). The two-sided Peetre inequality gives

    <t>^-q<=2^(q/2)<t-u>^q<u>^-q.

For a weighted prime coefficient the remaining power of <u> is 2s-2-2q=-beta<=0. The normalized L1 kernel bound is therefore c_s²2^(q/2)P_p, by (2). Translation phases have modulus one and are retained in the actual operator; only this commutator error estimate uses their absolute values.

For B, its exact Fourier kernel is the normalized convolution integral

    integral mhat(t-z)b(z)mhat(z-u) dz/(2pi).

Put k1=t-z and k2=z-u. By (10), b(z)<=G_beta 2^(beta/2)<u>^beta<k2>^beta. Now the remaining power of <u> is

    2s-2+beta-2q=0.

The residual <k1+k2>^p factor is at most 2^(p/2)<k1>^p<k2>^p. Two normalized Young inequalities yield the first term in (11). This proves (12), first on Schwartz vectors and then on H^q by density and the continuous bound. Absolute summability (2) justifies the complete prime-series passage.

Put a=kappa-delta_N>=kappa/2, W=L_(s,h)Q and X=W*W. Recall K=-H restricted to Ran Q, so kappa I<=K<=I/2. All these maps are bounded for fixed h. The actual operator-domain identity is

    2W*HW=-XK-KX-Q[L_(s,h),[L_(s,h),H]]Q.

Consequently (9) and (12) imply, whenever ||<D>^qQ||<=M_q,

    (K-delta_N)X+X(K-delta_N)
                   <=[2c_N L_s(T)²+D_(s,rho)M_q²]I.

Since K-delta_N>=a>0, the order-preserving Lyapunov inverse is

    Y -> integral_0^infinity exp[-t(K-delta_N)] Y exp[-t(K-delta_N)] dt.

Its norm is at most 1/(2a). Applying it to the preceding inequality and using ||X||=||W||^2 gives the explicit recursion

    M_0=1,
    M_s=sqrt{[c_N L_s(T)²+(D_(s,rho)/2)M_(s-rho)²]/a},
                       s=rho,2rho,3rho,... .           (13)

For each Qv, as h decreases to zero the squared Fourier multiplier l_(s,h)(t)^2 increases pointwise to <t>^(2s). Monotone convergence and the uniform-in-h bound therefore prove ||<D>^sQ||<=M_s at these exponents. Intermediate Sobolev orders follow by the elementary Fourier Holder inequality: if r=(1-theta)s0+theta s1, then

    ||<D>^r Q||<=M_s0^(1-theta) M_s1^theta.             (14)

For fixed rho and fixed r this gives M_r<=kappa^(-r/(2rho)-o(1)). For example rho=2/3 yields an H² bound after three steps with cost kappa^(-3/2-o(1)). The depth-dependent choice below improves this to kappa^(-1-o(1)).

For the asymptotic cost, choose the least integer N>=2 satisfying delta_N<=kappa/2, and T=exp(c_N). The displayed exponential prime tail gives N=O(log(1/kappa)+1), hence c_N=O(sqrt(log(1/kappa))loglog(1/kappa)) as kappa tends to zero. All remaining constants are the finite explicit expressions above.

Choose rho as an explicit function of the target depth:

    L=log(1/kappa), rho=1-1/(2+sqrt L).

This lies in [1/2,1). For any fixed target r the number of steps in (13),(14) remains bounded as kappa tends to zero. The moment indices in (11) stay in a fixed bounded interval, so their displayed factorial bounds remain bounded; the only additional growing symbol constant is G_beta=O(sqrt L). Since T=exp[O(sqrt L log L)], these factors are all kappa^(-o(1)). Hence the sharper actual-band result is

    ||<D>^r Q|| <= kappa^(-r/2-o(1))
                 for each fixed r>=0.                 (15)

This notation describes an explicit family of upper bounds from (11),(13),(14), not an assertion of a lower asymptotic or a new spectral gap. The depth must remain strictly positive. This proves no uniform Sobolev bound at kappa=0, no finite signed matrix sign, no absence of negative spectrum, and no new zero exclusion.

# Part II. Whole-band localization in one common central interval

## 1. Original domain and constants

Keep the original even Hilbert space and its reviewed realization

 H=B-V, B=m b(D)m>=0, H>=-1/2,
 He0=-e0/2, ||e0||=1.

The critical, pole-corrected operator is

 Acrit=H+(1/2)|e0><e0|.

All primes and the complete Gamma symbol are retained. For R>=2 write

 chi=1_(|x|>=R), t(R)=7 exp(2R-(pi/2)exp(2R)),
 D(R)=10000 t(R) exp(R/2), E(R)=10 t(R) exp(-R/2),
 g(R)=||chi e0||^2<=4t(R)^2 exp(R).

[SIGNED_PRIME_LOW_SPECTRUM.md, Sections 4–5](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/SIGNED_PRIME_LOW_SPECTRUM.md) proves the full-space bound ||chi V||<=D(R), the cross-Gamma bound E(R), and that this sharp cutoff preserves the original form domain. More explicitly, the bounded cross operator between the central and exterior source supports, after inserting the two original m multipliers, has norm at most E(R). Its quadratic pairing is

 E_R[mv]=Re integral_(|x|>=R,|y|<R) k(x-y)mv(x)conj(mv(y)) dxdy,
 k(h)=exp(-|h|/2)/(1-exp(-2|h|)).

These are full-space/domain assertions, not assumptions on an unknown spectral basis. In particular all sharp-cutoff identities below are legal closed-form identities.

## 2. The whole negative-depth subspace

Fix 0<kappa<=1/2 and let Q be the spectral projection of H on [-1/2,-kappa], with the known ground direction removed. If Q=0 there is nothing to prove. On range(Q), put

 K=-H|_(range Q), kappa I<=K<=(1/2)I,
 A=Q chi Q, z=||chi Q||, so A>=0 and ||A||=z^2,
 Dq=Herm(Q chi V Q),
 Bchi[v]=b[chi mv], v in range(Q).

Let Egamma denote the bounded selfadjoint compression of E_R[mv] to range(Q). Then ||Egamma||<=E(R). Since range(Q) is a bounded spectral subspace, all its vectors belong to D(H)=D(B). The cutoff-domain identity gives

 Bchi=Dq-(AK+KA)/2+Egamma.                            (1)

In particular Bchi is a bounded positive form on range(Q). No common eigenvalue is assigned to vectors in this subspace.

Write d=||chi VQ||<=D(R). Since chi is a projection,

 ||Dq||<=||Q chi|| ||chi VQ||<=zd.

Positivity in (1) yields

 AK+KA<=2(zd+E(R))I.

The Lyapunov inverse is order-preserving:

 L_K^{-1}(X)=integral_0^infinity exp(-sK)X exp(-sK) ds.

The integral converges in operator norm because kappa>0. Also L_K^{-1}(AK+KA)=A and 2L_K^{-1}(I)=K^{-1}. Therefore

 A<=(zd+E(R))K^{-1},
 z^2<=(zd+E(R))/kappa,
 z^2<=d^2/kappa^2+2E(R)/kappa.                        (2)

The last line uses dz<=kappa z^2/2+d^2/(2kappa). This is a uniform bound on all columns of the actual negative-depth subspace, not a sum of separately localized eigenvectors.

## 3. A common central negative subspace

Choose 0<eta<=1/16 and an explicitly searchable R>=2 for which

 D(R)<=kappa sqrt(eta kappa)/4,
 E(R)<=eta kappa^2/8.                                 (3)

Then (2) gives z^2<=5eta kappa/16<1, so the map J=(1-chi)|_(range Q) is injective and has closed range. Every image is supported in [-R,R] and remains in the original form domain.

For unit v in range(Q), exact expansion of the critical form and (1) gives

 Acrit[Jv]
 =-<v,Kv>+Re<v,AKv>+<v,Dq v>+<v,Egamma v>
   -<chi v,V chi v>+(1/2)|<Jv,e0>|^2.                 (4)

Here <v,e0>=0, hence the last term is bounded by g(R)z^2/2. The complete exterior multiplier estimate also gives

 |<chi v,V chi v>|<=D(R)z^2.

Consequently

 Acrit[Jv]<=-kappa+[1/2+D(R)+g(R)/2]z^2+dz+E(R).

Under (3), D(R)<1/8, g(R)<=1 and z^2<=5eta kappa/16. The square bracket is at most 9/8. Moreover

 dz<=d^2/(2kappa)+kappa z^2/2<=3eta kappa/32,
 E(R)<=eta kappa/16.

The total error is at most (45/128+12/128+8/128)eta kappa<eta kappa. Thus

 Acrit[Jv]<=-(1-eta)kappa||v||^2.                    (5)

This keeps the negative index of the entire band inside one explicit central window. It does not show that this central compression is nonnegative. The location scale depends on kappa, and no positive lower bound for kappa is asserted.


The same bounded Gamma cross and the bounded complete-prime and pole crosses also give operator-domain localization. For v in D(Acrit), test its equation against central form-domain vectors. The cross term is a bounded L2 functional, so the associated-operator criterion places (1-chi)v in the domain of the central diagonal operator A_c. Its B_c domain is the same, since its other terms are bounded. This proves the sharp central domain assertion used in Part III.

The radius in (3) can be found from scalar constants alone. Setting y=exp(2R), D=70000 y^(5/4)exp(-pi y/2) and E=70 y^(3/4)exp(-pi y/2). For fixed eta, a sufficiently large fixed multiple of log(1/kappa)+1 satisfies (3); hence R=O(loglog(1/kappa)+1). For unit v in Ran Q, u=(1-chi)v obeys B_c[u]<=||V|| ||u||^2<=41 because Acrit[u]<0 and the pole term is positive. Therefore ||u||_(B_c+I)<=sqrt(42)<9. The constant 41 is the original full-prime bounded-perturbation envelope from [REPORT.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/REPORT.md).

# Part III. Explicit original-form finite polynomial coverage

## 1. Original objects and precise input

Use the original even L2(dx) space, H=B-V, B=m b(D)m, ||m||infinity<=2, and the complete Gamma symbol

 b(t)=Re psi(1/4+it/2)-psi(1/4).

Fix 0<kappa<=1/2 and let Q be the actual spectral band of H with eigenvalues at most -kappa, with the known ground removed. This definition is legitimate even if Q=0. The sole additional input is an explicit bound

 ||v''||2<=K2(kappa)||v||2, v in Ran Q, K2(kappa)>=1.       (1)

Part I, Section 5, supplies (1) by a complete signed-prime double-commutator/Lyapunov proof, with K2(kappa)<=kappa^(-1-o(1)). No regularity is asserted for the whole critical kernel or for an arbitrary Gamma-energy ball.

Choose a radius R>=2 at which Part II's whole-negative-band localization gives, for ||v||=1 and u=C_R v,

 Acrit[u]<=-(1-eta0)kappa, eta0<=1/16,
 ||u||_A<9, A=B_c+I, Acrit=H+(1/2)|e0><e0|.              (2)

The complete Gamma reference B_c is the central Dirichlet restriction on [-R,R]. The sharp cutoff maps the actual original operator domain into itself. For a completely explicit choice take eta0=1/16, y=100(1+log(1/kappa)), and R=(1/2)log y. Then R>=2 and the reviewed tail formulas become D(R)=70000 y^(5/4) exp(-pi y/2) and E(R)=70 y^(3/4) exp(-pi y/2); these satisfy D(R)<=kappa sqrt(eta0 kappa)/4 and E(R)<=eta0 kappa^2/8 throughout 0<kappa<=1/2. For example, use pi>3, log(1+L)<=L for L=log(1/kappa), log(70000)<12 and log(100)<5 to bound the two expressions by the stated powers with ample strict margin. Thus R=O(loglog(1/kappa)+1), while the stronger exact identity exp(2R)=100(1+log(1/kappa)) also holds. No spectral vector is used to choose it.

The strip bound for the actual theta square root is

 |m(x+iy)|^2<=100 exp(4|x|-(3/2)e^(2|x|)), |y|<=1/2.

Since max_(u>=1) u^2 exp(-3u/2)=(16/9)e^-2<1/4, the modulus of m on this strip is less than 5. Cauchy on radius 1/4 then gives the uniform REAL derivative bound

                         ||m'||infinity<=20.            (3)

These are bounds for the original multiplier, not a replacement norm.

## 2. A finite even trial space and exact error

Partition [0,R] into n intervals of length h=R/n<=1, reflect the grid evenly, and let Z_(R,n) be the space of even continuous piecewise-linear functions on [-R,R], extended by zero outside. There is no imposed zero boundary value. Its dimension is n+1. All its vectors lie in the original central operator domain D(A): multiplying by m gives a compactly supported piecewise-smooth BV source; its Fourier transform is O(1/|t|), so the complete logarithmic b(D) applied to that source lies in L2. The associated-form criterion gives the claimed domain membership, including the actual endpoint jumps.

For v in Ran Q, let z=I_h v be its nodal interpolant on this grid, extended by zero. H2 regularity supplies continuous representatives and hence well-defined nodal values. Put e=u-z. On every grid interval the interpolation error is zero at both endpoints. Its sharp zero extension is therefore in H1, despite u and z separately being allowed nonzero boundary traces.

Two ordinary Dirichlet/zero-mean Poincare inequalities on each interval give

 ||e||2<=a0:=h^2 K2/pi^2,
 ||e'||2<=a1:=h K2/pi.                                  (4)

To check the second inequality, the derivative of the interpolation error has mean zero on each interval, and its derivative is v''. The first then follows from the vanishing endpoint traces. Summation includes both reflected halves, so there is no additional factor of two.

The full Gamma symbol obeys, on the whole real line,

                         b(t)<=6+(1/2)log(1+t^2).        (5)

Indeed Part I gives b(t)<=4+(1/2)log(1+4t^2)<=(4+log2)+(1/2)log(1+t^2)<6+(1/2)log(1+t^2).

For g=me, Plancherel and concavity of log imply

 b[g]<=6||g||2^2+(||g||2^2/2)
                         log(1+||g'||2^2/||g||2^2).

The expression x log(1+y/x) is increasing in each of x,y>=0. Thus (3)-(4), ||m||infinity<=2, and the convention at g=0 give the explicit ORIGINAL A-form estimate

 dist_A(u,Z_(R,n))^2
 <=a0^2 {25+2 log[1+(10+pi/h)^2]}.                       (6)

All prime effects are retained in the original negative-band input and in the later signed matrix. No prime contribution is being estimated by (6); this is a controlled approximation in the complete Gamma reference norm.

## 3. An explicit rank bound

Let 0<delta<=1 be the requested A-form error and put

 x=K2/delta>=1,
 L=100(1+log x),
 n=ceil[R sqrt(x L)], h=R/n.                             (7)

Then h<=1/sqrt(xL)<=1 and (6) is strictly less than delta^2. One direct verification uses the monotonicity of the right side of (6) as a function of h>0. For the continuous value h0=1/sqrt(xL), put t=1+log x>=1. Since pi<4,

 log[1+(10+pi/h0)^2]<=log(197/h0^2)<9+2t.

The square root bracket in (6) is therefore less than 7 sqrt(t), while a0=delta/(100 pi^2 t). Their product is less than delta. The integer rounding only decreases h, and hence decreases the bound. Monotonicity can also be checked directly from the product h^4[25+2log(1+(10+pi/h)^2)]: differentiating with respect to log h, the negative contribution from the logarithm has absolute value less than 4, whereas the positive contribution is at least 100.

Consequently

 dim Z_(R,n)<=2+10 R sqrt[(K2/delta)(1+log(K2/delta))].     (8)

For delta=kappa/4000, the Sobolev cost K2<=kappa^(-1-o(1)) and R=O(loglog(1/kappa)+1) yield the genuine asymptotic upper cost

                         dim Z_(R,n)<=kappa^(-1-o(1)). (9)

This covers only actual negative-band cores. It is consistent with the much larger rank needed to approximate the ENTIRE central reference resolvent, since those are different targets.

## 4. Exact compatibility condition for a complete signed positive block

Take the central restriction A_c of Acrit at this same R and the shift s=kappa/2. If an independently certified finite matrix establishes

                         (A_c+sI) restricted to Z_(R,n)>=0, (10)

with n as in (7) and delta=kappa/4000, then Ran Q is zero. For a hypothetical unit v in Ran Q, (2) gives

 (Acrit+sI)[u]<=-7kappa/16.

The original bounded-part form estimate |(Acrit+sI)(a,b)|<=42||a||_A||b||_A and (6) imply

 |(Acrit+sI)[u]-(Acrit+sI)[I_hv]|
 <=42 delta(18+delta)<kappa/5,

contradicting (10). The 42 constant follows from B>=0 and the actual bounded-part norm <=41+1/2+s<=41.75; it does not assert positivity of the signed V. The test is on an entire finite block, not on separate diagonal vectors.

One may instead use the stronger true signed Schur test. Part II defines

 t(R)=7exp(2R-(pi/2)e^(2R)),
 D(R)=10000t(R)e^(R/2), ||chi V chi||<=D(R).

The same choice of R in (2) has D(R)<s. Let A_e be the closed exterior restriction of Acrit. Its Gamma form and pole form are positive, so A_e+s>=s-D(R)>0, without any assumed critical exterior positivity. The off-diagonal Ccross is bounded by D(R)+E(R)+sqrt(g(R))/2, by the complete prime, Gamma and pole cross bounds of Part II. Thus the following inverse and cross form are well defined on the original central form domain. If

 S_s=A_c+s-Ccross*(A_e+s)^(-1)Ccross

is nonnegative on Z_(R,n), then (10) follows, since the omitted Schur loss is positive. Here Ccross retains the complete Gamma cross, every signed prime leg, and the exact pole cross. This is an optional stronger certificate; no new two-sided exterior estimate or fixed positive division-source block is a dependency of the rank theorem.

All entries of the raw central matrix (10) are computable original-domain quantities. In its prime terms both source factors are supported in [-R,R], so every shift with log n>2R has exactly zero overlap (and equality only changes a null boundary set). The complete prime contribution to this central block is therefore the finite sum n<=exp(2R), without a discarded tail. The full Gamma and pole terms are still retained. With the localization scale above, this prime index cutoff is O(log(1/kappa)).

If the optional Schur test is used, its exterior resolvent loss can be enclosed using actual original-L2 residuals and the positive denominator s-D(R). Endpoint jumps in all central trial sources must be paid by BV Fourier tails rather than silently assigning H2 regularity. No central matrix sign computation, much less a uniform-in-kappa sign theorem, is asserted here.

The new conclusion using the reviewed actual Sobolev input is the explicit rank and domain-safe approximation (6)-(9). It does not establish (10). A known fixed-dimensional eventually-positive theta-jet or odd-collar result cannot be substituted for (10); this even spline space has its stated growing dimension and uses the original signed operator and pole correction.


## 5. Fixed higher degree: an explicit smaller-rank version

The same construction has a fixed-order version, so it is not restricted to the linear interpolation rate. Fix an integer p>=2 and use the actual-band Sobolev bound

 ||v^(p)||2<=K_p(kappa)||v||2,
 K_p(kappa)>=1, K_p(kappa)<=kappa^(-p/2-o(1)).             (11)

Let the trial space consist of even continuous piecewise polynomials of degree at most p-1 on the same reflected grid, with no imposed boundary zero. Its dimension is n(p-1)+1. The space is again contained in D(A), by the same compact BV source argument.

Here is an explicit interpolant and all constants. On a cell [a,a+h], take the degree-(p-1) Taylor polynomial of v at a, and add the linear term that makes its value at a+h equal to v(a+h). H^p in one dimension makes every endpoint derivative used here well-defined. The result matches both endpoint values; adjacent cells are therefore continuous, and the error has zero endpoint values. Reflect the construction on [0,R] evenly. The reflected error is still H1 after zero extension, including at zero and at the two outer endpoints.

If r is the Taylor remainder, its integral formula and Young/Cauchy inequalities give on each cell

 ||r||2<=h^p/p! ||v^(p)||2,
 ||r'||2<=h^(p-1)/(p-1)! ||v^(p)||2,
 |r(a+h)|<=h^(p-1/2)/[(p-1)! sqrt(2p-1)] ||v^(p)||2.

The linear endpoint correction has L2 norm |r(a+h)|sqrt(h/3) and derivative norm |r(a+h)|/sqrt(h). Thus, after summing cells,

 ||e||2<=F_p K_p h^p,
 ||e'||2<=F_p K_p h^(p-1), F_p=2/(p-1)!.                (12)

The constants in (12) intentionally dominate the sharper Taylor constants. The same monotone Jensen calculation now gives

 dist_A(Cv,Z_(R,n,p))
 <=F_p K_p h^p sqrt{25+2log[1+(10+1/h)^2]}.              (13)

For delta<=1 put

 x=max(1,F_p K_p/delta), L=100(1+log x),
 n=ceil[R(xL)^(1/p)].                                   (14)

Then (13) is less than delta. Indeed for h0=(xL)^(-1/p), t=1+log x>=1 and p>=2, the logarithm in (13) is less than 8+2t, so the square-root factor is less than 7sqrt(t); the preceding factor is at most delta/(100t). Rounding n upward decreases (13), as direct differentiation shows. Consequently

 dim Z_(R,n,p)<=p+(p-1)R[xL]^(1/p).                      (15)

With delta=kappa/4000 and the same radius from Part II this is

 dim Z_(R,n,p)<=kappa^(-1/2-1/p-o(1))                    (16)

for each FIXED p. Equivalently, for every fixed epsilon>0 one may choose a fixed p>1/epsilon and obtain a sufficiently small-depth bound C_epsilon kappa^(-1/2-epsilon). Neither statement sets p to an unbounded function of kappa without paying its constants.

The raw central sufficient test (10), or its stronger signed Schur variant, applies verbatim to this ENTIRE finite polynomial block. Its sign is still not proved. Formula (16) is an explicit actual-negative-band coverage upper cost, not a positivity result and not an assertion that true theta jets can represent this block at the same dimension or with free conditioning.

# Appendix A. Actual negative-band counting and Schatten summability

## 1. An explicit count using fixed-error linear interpolation

Use the original even Hilbert space, H=B-V, H>=-1/2, the normalized known ground e0 with He0=-e0/2, and Acrit=H+(1/2)|e0><e0|. For 0<kappa<=1/2 let Q_kappa be the spectral projection 1_[-1/2,-kappa](H) with the known ground removed. All statements are valid if Q_kappa=0.

Let K2(kappa)>=1 be the explicit H2 bound from Part I's double-commutator recursion and interpolation, so ||v''||2<=K2(kappa)||v||2 for v in Ran Q_kappa and K2(kappa)<=kappa^(-1-o(1)). Put

    y=100(1+log(1/kappa)), R=(1/2)log y,
    x=4K2(kappa), L=100(1+log x),
    n=ceil[R sqrt(xL)].

Use the even continuous piecewise-linear nodal interpolant I_h on [-R,R], h=R/n, extended by zero. Its fixed trial space has dimension n+1. Part III's approximation estimate with delta=1/4 gives, for every v in Ran Q_kappa,

    ||C_R v-I_h v||2 <= ||C_R v-I_h v||_(B_c+I)
                      < (1/4)||v||2.                  (1)

Part II's whole-band localization bound with eta=1/16 is

    ||(1-C_R)Q_kappa||²<=5kappa/256.

Since C_R is an orthogonal projection,

    ||I_h v||2 >= [sqrt(1-5kappa/256)-1/4]||v||2.       (2)

The bracket is strictly positive throughout 0<kappa<=1/2. Nodal evaluation is a linear operation, well-defined by actual H2 regularity; thus I_h is a linear injective map from the ENTIRE Ran Q_kappa into this finite trial space. No eigenbasis, sign of a trial matrix, or theta-jet representation has been used. Consequently

    dim Ran Q_kappa <= n+1
       <= 2+20 R sqrt[K2(kappa)(1+log(4K2(kappa)))].     (3)

This is a fully explicit finite bound at every stated depth. The asymptotic cost is

    dim Ran Q_kappa <= kappa^(-1/2-o(1)).               (4)

Equivalently, for every epsilon>0 there is a finite C_epsilon with

    dim Ran Q_kappa <= C_epsilon kappa^(-1/2-epsilon),
                         0<kappa<=1/2.                (5)

For small kappa this follows from (3) and the reviewed H2 upper cost; extending to the compact interval of larger depths uses monotonicity of Q_kappa. Unlike exclusion by a signed finite matrix, dimension counting only needs a fixed error below the localization lower bound. There is therefore no need to choose delta proportional to kappa or to increase the polynomial degree.

## 2. The actual negative part is in every S_a with a>1/2

Let T=(-Acrit)_+ be the positive negative part of the actual pole-corrected operator, defined by spectral calculus on the original even space. It is bounded with ||T||<=1/2. Since the known ground is exactly removed and its orthogonal complement reduces H,

    1_[kappa,1/2](T)=Q_kappa.

Equation (3) makes each of these spectral projections finite rank. Moreover

    ||T-T Q_kappa||<=kappa.

Thus T is the operator-norm limit, as kappa decreases to zero, of finite-rank operators; in particular it is compact. Its positive eigenvalues, counted with multiplicity, can therefore accumulate only at zero.

For t>0 let N_T(t)=rank 1_(t,infinity)(T). Then N_T(t)<=dim Ran Q_t for 0<t<=1/2. Fix a>1/2, and choose epsilon with 0<epsilon<a-1/2. The positive layer-cake identity and (5) give

    Tr(T^a)=a integral_0^(1/2) t^(a-1) N_T(t) dt
       <=a C_epsilon integral_0^(1/2) t^(a-3/2-epsilon) dt
       <infinity.                                    (6)

Hence T belongs to the Schatten class S_a for every a>1/2 (with its usual quasi-norm interpretation when a<1). No endpoint S_(1/2) claim follows. Adding back the single known ground would only add a rank-one term, but T as defined already uses the original pole correction.

These estimates permit nonzero negative spectrum and do not establish any signed central positivity. In particular they do not change the previously certified gap or prove RH.

