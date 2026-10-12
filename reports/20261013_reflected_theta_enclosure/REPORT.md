# A reflected theta enclosure with linearly many ideal-norm coefficients

For the unchanged fixed principal F_q defined below, this theorem constructs a reflection-preserving finite denominator with M=O(R) ideal-norm coefficients and height window T=O(sqrt(R)). The error in the COMPLETE coherent square is O(exp(-eta R)) for every fixed eta>0, uniformly on successive unit R intervals. Its sum over those intervals is finite. This is an unconditional finite-enclosure theorem with an independently paid safe-line denominator bound.

The number M counts ideal-norm coefficients and T measures a contour window. The theorem does not bound total evaluation or quadrature complexity, does not supply a numerical unknown source q, and does not estimate the retained finite expression at the desired critical amplitude. No new original spectral gap or zeta-zero exclusion is claimed. The distinct-prime, mixed-height and complementary terms of the square have not been discarded.

An essential limitation is also proved: every FIXED finite theta cutoff has infinitely many artificial zeros off the critical line, despite exact reflection symmetry. The enclosure therefore uses a growing cutoff and only its certified finite height window. It does not justify a stable left-contour inverse by reflection alone.

## Original source, multiplier and public dependencies

Use the original even theta density Phi, with

    m(x)^2=Phi(x)/(2cosh(x/2)),
    e0(x)=2m(x)cosh(x/2), dnu(x)=e0(x)^2 dx,
    v=e0 q, f_q=Phi q=mv,
    B_q(s)=integral_R Phi(x)q(x)exp(-(s-1/2)x)dx.

Here q is a fixed complex even member of L2(nu); no positivity or computed negative-state assumption is imposed. The original theta envelopes make ||m exp(c x)||_2 finite for every fixed real c. Cauchy--Schwarz gives every fixed exponential L1 source moment, so B_q is entire and bounded on every fixed closed real strip. The [original closed-form realization](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/552de4a3f1ccaa50459b3f8b0afa4bd818f223df/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md) supplies this unchanged normalization and source norm; no positive-depth spectral estimate is an input.

Let K=Q(omega), let S be the original fixed finite set of deleted ideal primes, and write P=Np. Keep the original fixed unitary character kappa and the exact half-damped local multiplier

    d_p=P^(-s), r_p=kappa(p)P^(2-6s),
    H_(p,half)(s)=(1-P^(-2))/(1-r_p)
                         [1+(d_p-r_p)/(P(1-d_p))],
    H_(half,S)(s)=product_(p outside S) H_(p,half)(s).

Equivalently,

    H_(half,S)(s)=zeta_K^S(2)^(-1) L^S(6s-2,kappa)
                 product_(p outside S)[1+(d_p-r_p)/(P(1-d_p))].

This is the multiplier derived in [HALF_DAMPED_PROBE.md, Section 3](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/552de4a3f1ccaa50459b3f8b0afa4bd818f223df/reports/20261011_qrh_selection_bridge/HALF_DAMPED_PROBE.md). Its products converge normally on every buffered half-plane Re s>1/2; the local numerator is P-(P-1)d_p-r_p and is nonzero there because |(P-1)d_p+r_p|<P. In particular H and its reciprocal are uniformly bounded on each fixed line Re s=sigma>1. These elementary Euler-product facts introduce no Q or unproved prime-mean hypothesis.

The exact principal from [UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md, Part B](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/552de4a3f1ccaa50459b3f8b0afa4bd818f223df/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md), with fixed source activation, is

    F_q(R)=1/(2pi i) integral_(Re s=sigma>1)
       exp((s-1/2)R) exp((s-5/6)^2)
                H_(half,S)(s) B_q(s)/zeta_K^S(s) ds.

This is also a direct definition of the object enclosed here. The activation contributes precisely B_q(s) to the principal Mellin integrand: simultaneously scaling the physical X,T by exp(-x), with ambient slots and normalizer fixed, multiplies its principal prefactor by exp(-(s-1/2)x), then integration against Phi(x)q(x) gives B_q. All S factors and H remain present. No identification of a finite theta term with an individual physical Mobius tag is used.

The [two independent mathematical reviews](REFEREE.md) cover the full proof below, including all source tails, reciprocal-Gamma growth, true denominator lower bounds, complete quadratic error and fixed-cutoff zero limitation. No diagnostic numerical script is needed for these analytic statements.

## 1. Exact reflected theta identity and finite object

Put a=2*pi/sqrt(3), and let r(n) count ALL integral Eisenstein ideals of norm n. The scaled Eisenstein lattice has covolume one and its dual is a rotation of itself. Poisson summation therefore gives

 Theta(t)=sum_(z in Z[omega]) exp(-a t Nz),
 Theta(t)=t^(-1)Theta(1/t),
 Theta(t)-1=6 sum_(n>=1)r(n)exp(-a n t).                     (1)

For Re s>1, splitting its Mellin integral at t=1 gives

 Lambda(s):=a^(-s)Gamma(s)zeta_K(s)
   =1/[6s(s-1)]+sum_(n>=1)r(n) I_n(s),
 I_n(s):=integral_1^infinity exp(-a n u)
                         [u^(s-1)+u^(-s)]du.               (2)

Each I_n is entire and I_n(1-s)=I_n(s). The identity continues meromorphically and keeps both reflected legs, not merely the first incomplete-gamma term.

For the ORIGINAL finite ideal-prime deletion set S put

 D_S(s)=product_(p in S)(1-(Np)^(-s)),
 zeta_K^S(s)=D_S(s)zeta_K(s).

S need not be closed under conjugation. For an integer M>=1 define

 Lambda_M(s)=1/[6s(s-1)]+sum_(1<=n<=M)r(n)I_n(s),
 Z_M^S(s)=D_S(s) a^s Lambda_M(s)/Gamma(s).                    (3)

Thus Lambda_M(s)=Lambda_M(1-s) EXACTLY, before the original deleted factors are restored. The density poles at 0 and 1 have their correct coefficients. The source multiplier remains

 A_q(s)=exp((s-5/6)^2) H_half,S(s) B_q(s).

The original q is in L2(nu). Its fixed-strip evaluation bound follows from f_q=Phi q=mv and
integral |f_q(x)|exp(-c x)dx <= ||q||_(L2(nu))||m exp(-c x)||_(L2(dx)).
Consequently, on every fixed safe line sigma>1,

                       |A_q(sigma+it)|<=C_(q,S,sigma)exp(-t^2).              (4)

No numerical or explicit negative-state witness is presumed available.

## 2. Exponentially small theta tail, with inverse Gamma fully charged

Fix sigma>1. For n>=1 and all real t,

 |I_n(sigma+it)|
 <= integral_1^infinity exp(-a n u)[u^(sigma-1)+u^(-sigma)]du
 <= C_sigma exp(-a n)/n.                                   (5)

For example, bound u^(sigma-1) by C_sigma exp(a(u-1)/2) and integrate; the second term is at most exp(-a n)/(a n). Since r(n)<=d(n)<=n, (5) gives

 |Lambda(sigma+it)-Lambda_M(sigma+it)|
                            <=C_sigma exp(-a M),           (6)

uniformly in ALL t. This is a completed-function estimate, not yet a zeta estimate.

The [fixed-line Gamma bound](https://dlmf.nist.gov/5.11.E9) gives

 |Gamma(sigma+it)|^(-1)
 <=C_sigma (1+|t|)^(1/2-sigma)exp(pi|t|/2)
 <=C_sigma exp(pi|t|/2).

The fixed finite product D_S is bounded on this line. Therefore

 |zeta_K^S(sigma+it)-Z_M^S(sigma+it)|
               <=K_(S,sigma)exp(-a M+pi|t|/2).              (7)

The reciprocal Gamma growth in (7) is essential. We do NOT infer an all-height lower bound for Z_M^S from this estimate.

Independently, absolute Euler convergence gives

 |zeta_K^S(sigma+it)|>=m_sigma:=1/zeta_K^S(sigma)>0.

Thus on the FINITE height interval |t|<=T, if

             K_(S,sigma) exp(-a M+pi T/2)<=m_sigma/2,       (8)

then |Z_M^S(sigma+it)|>=m_sigma/2. This is an independently proved safe-line lower bound, not a target-amplitude assumption.

## 3. The finite coherent quadratic enclosure

Keep the original principal

 F_q(R)=1/(2pi) integral_(t real) exp((sigma-1/2+it)R)
                              A_q(sigma+it)/zeta_K^S(sigma+it)dt.

For M,T satisfying (8), T>=1, define

 F_(M,T)^theta(R)=1/(2pi) integral_(-T)^T
       exp((sigma-1/2+it)R) A_q(sigma+it)/Z_M^S(sigma+it)dt. (9)

This finite object uses the original source and only the finitely many ideal counts r(n), n<=M, together with explicitly displayed reflected integrals. It is not a sharp finite Mobius polynomial or a replacement for individual physical tags.

On |t|<=T apply (7), (8) to the exact reciprocal difference. The integral of exp(-t^2+pi|t|/2) is a fixed finite constant. Outside this interval, bound the ORIGINAL integrand using the absolute Euler lower bound and Gaussian. Hence, for R>=0,

 |F_q(R)-F_(M,T)^theta(R)|
 <= Delta_(M,T)(R)
 :=C_(q,S,sigma) exp((sigma-1/2)R)
                         [exp(-a M)+exp(-T^2)].             (10)

Both amplitudes separately are bounded by C exp((sigma-1/2)R), by (4) and the proved safe-line lower bounds. Therefore the ENTIRE quadratic discrepancy, including every cross term, satisfies

 ||F_q(R)|^2-|F_(M,T)^theta(R)|^2|
 <=C exp((2sigma-1)R)[exp(-a M)+exp(-T^2)].                  (11)

Equivalently the certified enclosure is

 (max(0,|F_(M,T)^theta|-Delta))^2 <= |F_q|^2
                                     <=(|F_(M,T)^theta|+Delta)^2.          (12)

The approximating square in (11)-(12) is the full coherent double integral over [-T,T]^2, with numerator A_q(s)overline(A_q(s')) and denominators Z_M^S(s)overline(Z_M^S(s')). Neither diagonalization nor deletion of signed cross-height terms is involved.

For any fixed eta>0, choose on R in [j,j+1]

 T_j=sqrt(max(1,(2sigma-1+eta)(j+1))),
 M_j=max(1,ceil(a^(-1) max((2sigma-1+eta)(j+1),
                              pi T_j/2+log(2K_(S,sigma)/m_sigma)))).       (13)

These explicit minimal choices give M_j=O_(S,sigma,eta)(j+1), T_j=O_(sigma,eta)(sqrt(j+1)), and (11) is O(exp(-eta j)), uniformly on that whole unit interval. Thus the complete quadratic errors are absolutely summable over the original observation scales. No critical bound for F_q has been used.

## 4. A simple explicit safe-line specialization

At sigma=2 put B=zeta_R(2)^2=pi^4/36. Then m_2>=1/B and |D_S(2+it)|<=B, independently of which finite S is deleted. Also

 integral_1^infinity exp(-a n u)(u+u^(-2))du
 <=exp(-a n)[2/(a n)+1/(a n)^2].

Using r(n)<=n gives the explicit constant

 K_Lambda=(2/a+1/a^2)exp(-a)/(1-exp(-a)),
 K_2=B a^2 K_Lambda,
 |zeta_K^S(2+it)-Z_M^S(2+it)|<=K_2 exp(-a M+pi|t|/2).       (14)

Here the exact identity
 |Gamma(2+it)|^2=(1+t^2)pi t/sinh(pi t)
(including its limiting value at t=0) yields |Gamma(2+it)|^(-1)<=exp(pi|t|/2).
Thus a M>=pi T/2+log(2 B K_2) certifies the finite-height denominator bound. The remaining constant in (10)-(11) depends on the genuine fixed q and H bound. Formula (14) does not provide a numerical low-state q that is not otherwise known.

## 5. Exact finite update, and what it fails to sign-control

The next theta coefficient adds exactly

 Z_(M+1)^S(s)-Z_M^S(s)
       =D_S(s)a^s r(M+1)I_(M+1)(s)/Gamma(s).                (15)

On a common certified safe height window,

 F_(M+1,T)^theta-F_(M,T)^theta
 =-1/(2pi) integral_(-T)^T exp((sigma-1/2+it)R) A_q(s)
       [Z_(M+1)^S(s)-Z_M^S(s)]/[Z_M^S(s) Z_(M+1)^S(s)]dt. (16)

This retains the original forcing, both complex denominators and all phases. Its magnitude is exponentially small in M at fixed R, which is the basis of the certified enclosure. It gives no definite sign for the quadratic update. In particular r(M+1)>=0 does not make the reciprocal update or its covariance with the previous amplitude positive or negative.

## 6. Reflection alone does not make the finite inverse stable

There is a structural limitation even for this faster finite object. Define

                         Xi_M(s)=s(s-1)Lambda_M(s).

It is entire, real on the real axis, symmetric under s->1-s, and of order at most one: the integral in (2) is bounded on |s|<=r by a constant times Gamma(r+2)a^(-r-2), so log max|Xi_M|=O(r log(r+2)).

Set g_n(x)=exp(-a n exp(x))exp(x/2), x>=0. On the critical line,

 I_n(1/2+it)=2 integral_0^infinity g_n(x)cos(tx)dx.

Repeated integration by parts, valid since every derivative decays rapidly, gives

 I_n(1/2+it)=-2g_n'(0)/t^2+O_n(t^(-4)).

Consequently, for each FIXED finite M,

 Xi_M(1/2+it) -> c_M:=1/6+2 sum_(n<=M)r(n)g_n'(0)
                   =sum_(n>M)r(n)(2an-1)exp(-an)>0.         (17)

For the last equality differentiate the exact theta reflection at t=1: 2Theta'(1)+Theta(1)=0. Every term in the omitted sum is positive since a>1/2. Thus Xi_M has only finitely many zeros on the critical line.

It has infinitely many zeros in total. Otherwise Hadamard factorization for an entire function of order at most one would give Xi_M(s)=exp(alpha s+beta)P(s) for a polynomial P. Reflection forces alpha=0 (the resulting polynomial ratio cannot be a nonconstant exponential), so Xi_M would be a polynomial. But on real s->+infinity the n=1 integral already gives growth comparable to s(s-1)Gamma(s)a^(-s), contradicting polynomial growth. Therefore infinitely many zeros lie OFF the critical line. Reflection pairs them across that line; in particular infinitely many lie in Re s>1/2. The factors D_S and 1/Gamma do not remove such zeros there.

These are artificial zeros of the finite approximant, not zeros of the original zeta function. They do not contradict (8), whose height interval is finite and whose M increases with the requested interval. Nor do they assert activation by a given q. They prove that retaining exact reflection and an exponentially small completed tail still does not automatically give an all-height left inverse. A quantitative bound on the finite expression (9) in the target range, or a source-specific cancellation mechanism, remains unproved.
