# The normalized actual Mobius current is an original-form test

This is a domain upgrade for the SAME actual current, not a sign for the
ordered arithmetic collar. It applies to the original full and finite
Mobius masks, not automatically to a sparse signed outer filter.

Use the published [true-variance metric](../20261014_coupled_source_profile_square/TRUE_VARIANCE_METRIC.md),
[finite arithmetic projection](../20261014_coupled_source_profile_square/FINITE_PROJECTION.md),
and [reset, amplitude and whole-forcing bounds](../20261014_coupled_source_profile_square/RESET_FACTS.md).
The projected off-site term has the **plus** attenuated-prime sign from
that finite arithmetic projection. No Liouville-character operator is
substituted. Every prime-power diagonal and source term, and the full
finite-mask boundary, remain in the equation below.

**Projection-convention correction.** An earlier normalization used the
auxiliary notation G_l and a negative Liouville-character term -K_l.
That operator is not the actual finite/full Mobius covariance projection.
Here it is replaced by the genuine plus K_theta term, and Section 5
recomputes the entire original-form remainder accordingly. The bounded
perturbation domain argument survives this correction; the old
character-based equation or remainder is not an alternative identity
for the same actual current.

## 1. Exact normalized conjugation

Use the notation and complete forcing of the linked actual projection.
The profile is a(n)=1-mu(n), or a_N(n)=1-mu(n)1_(n<=N), N>=2; in the
finite case a_N is ONE beyond N. Write T for the genuine posterior mean,
sigma^2=T(a^2)-(Ta)^2, and kappa=kappa_a for its reset coefficient.
The off-site attenuation satisfies 0<=theta_p<=1, with theta_p=0 for
p>N in the finite case. Set

    h=sigma^2 A_cur, R(z)=exp(3z)sigma(z)^2,
    0 < -R'(z)/R(z) < 1/2, z=pi exp(2x),
    P_a h=f=-S_a(u)+r+I_Z.

The actual amplitude A_cur is bounded. The forcing f is the WHOLE
source-gradient, reset residual and finite-divisor boundary forcing.
Its previously proved bounds are O(poly(z) exp(-3z)) on the wing and
O(1/x) at the origin. No canonical label forcing is being substituted.
Set B=exp(x/2-z), q_psi=psi/B and g_B=q_psi h. The exact earlier equation is

    (G_1+beta+kappa+K_theta)g_B=q_psi f,
    K_theta g_B=sum_(p prime)(log p) exp[-(p^2-1)z]
                             theta_p(p^2z)g_B(p^2z).

Define

    F1(z)=psi(x) A_cur(x)/sqrt(2z)=ell1(z)g_B(z),
    ell1(z)=1/(sqrt(2) pi^(1/4)) z^(-1/4) exp(2z)/R(z).

Thus ||F1||_L2(dz)=||psi A_cur||_L2(dx). Direct conjugation gives

    [G_3+beta+kappa+(log 3)/2-J1+K1]F1=S1,
    S1=ell1 q_psi f,                                      (1)

where

    G_3 F=(1/2)int_0^infinity exp(-3v)[F(z)-F(z+v)]dv/v,
    J1 F=(1/2)int exp(-3v)[A1(z,v)-1]F(z+v)dv/v,
    A1(z,v)=(1+v/z)^(1/4) R(z+v)/R(z),
    K1 F=sum_(p prime)(log p)sqrt(p)exp[-3(p^2-1)z]
                          R(p^2z)/R(z)theta_p(p^2z)F(p^2z).

The scalar in (1) is exactly (log 3)/2 by the grouped Frullani integral.
Every prime power remains in the original diagonal and source, and the
same complete finite-mask forcing remains. Only the exact projected
off-site covariance is restricted to primes. The positive sign in front
of K1 is not interpreted as a sign of its quadratic pairing.

## 2. Actual generator domain

The logarithmic R bounds give

    exp(-v/2) <= A1(z,v) <= (1+v/z)^(1/4) <= 1+v/(4z),
    |A1(z,v)-1| <= v/2.

Hence the absolute J1 kernel is at most exp(-3v)/4 and both Schur rows
are at most 1/12. The complete K1 is bounded on L2(dz), because theta_p and the R ratio
are at most one, dilation by p^2 has norm at most 1/p, and the complete
row is majorized by the convergent all-integer sum
Lambda(d)/sqrt(d) exp[-3pi(d^2-1)].

The SAME actual amplitude bound gives F1=O(poly(z)exp(-z)) and
F1=O(z-pi) at the origin. The complete score estimates give
beta+kappa=O(1+1/x), so (beta+kappa)F1 is L2. Also
R(z)>=R(pi)exp[-(z-pi)/2]; this is sufficient for S1 to have a
polynomial-Gaussian L2 tail. At the origin q_psi=O(x) pays the full
O(1/x) forcing. We have not assumed R is bounded below by a constant.

Equation (1), initially local weak, therefore gives G_3 F1 in L2 as a
distribution. Extend F1 by zero to z<pi. Its image on z=pi-r is

    -(1/2)int_0^infinity exp[-3(r+t)]F1(pi+t)/(r+t)dt,

which is L2 by the Carleman bound. The full logarithmic multiplier sends
L2 into every H^(-epsilon); a discrepancy supported at pi is impossible
for epsilon<1/2. Thus the full zero extension is in the logarithmic
Gamma generator domain. Restriction gives F1 in D(G_3) on (pi,infinity).
No boundary condition on the future Gamma semigroup was imposed.

## 3. Return to the ordinary original source form

This coordinate passage is needed: a conjugated generator domain alone
is not asserted to be the original source form. Write
j(x)=psi(x)A_cur(x)=sqrt(2z)F1(z). For |w-z|<1, the ordinary short-distance
logarithmic x-kernel, together with dx=dz/(2z), becomes comparable to

    dz dw/|w-z|

on F1 increments. The coefficient difference from sqrt(w/z) contributes
only a bounded L2 row, since z>=pi and that difference is O(|w-z|/z).
The G_3 form controls these local increments because exp(-3|w-z|) is
bounded below on this region.

For 1<|w-z| with bounded log-distance, use the endpoint square bound.
The row integral is at most O(log(2+z)); the Gaussian pointwise bound
on F1 pays this entire moment. At large log-distance the original
Gamma kernel is integrable and its endpoint rows are bounded. The
odd-wall/Hankel correction is paid near zero by j=O(x), or by the
already obtained zero-extension Gamma boundary term, and away from
zero by the same Gaussian mass. Consequently j has the complete
ordinary odd-Gamma source form.

Bounded A_cur pays all remaining original potential/reflected/prime/pole
terms by the complete theta majorants used for bounded-ratio source
tests. Smooth annular cutoffs converge: the Gamma part follows from its
closed form and the preceding origin/tail bounds, and every other row
by those same absolute theta majorants. More explicitly, the extra carre
row of an origin cutoff is bounded by C(1+|log x|), paid by j=O(x).
Choose far cutoffs with uniformly Lipschitz transition; their extra row
is uniformly bounded and converges pointwise to zero. Dominated
convergence removes both cutoffs, and mollification on the fixed
annulus gives the required smooth core approximation. Therefore

    L_cur=psi A_cur belongs to the original P domain.       (2)

This proof retains the whole finite-mask forcing at each finite cutoff.
It also applies to the full mask. It makes no separate domain claim for
individual canonical label fields, sparse B0 profiles or an infinite
past-adjoint source.

## 4. Exactly what is new in the same-source interface

The following is a conditional same-source interface, separate from the
proof of (2). If a canonical test L_can=H_can/sigma^2 is known to belong
to original P for the same mask and whole trace gauge, then

    L_can-L_cur=(H_can-psi h)/sigma^2 is in P.               (3)

Under the actual Q_delta>=0 assumption, the two-by-two Gram of L_can
and L_cur is positive semidefinite, including its full mixed form and
all W terms. Write g_act for the original actual source, distinct from g_B above.
The linear first-slot identity Q_delta(g_act,L_cur)=0 was
already supplied by bounded-ratio weak stationarity and is NOT a new
constraint. Neither (2) nor (3) supplies an independent sign for D_sigma,
the finite parity W/skew correction, or the critical negative-wing
ordered collar. The new Gram must be matched to that complete same-source
expression before any critical norm gain can be claimed.

## 5. The original density still has its full missing row

For clarity set omega=sigma^2, X_cur=L_cur, and

    P_theta=D0+F_theta+beta+kappa,
    F_theta j=sum_(p prime)alpha_p theta_p(x+log p)j(x+log p),
    alpha_p=(log p)/sqrt(p).

Here D0 is the prime-free one-sided source operator; D=D0-F with F
the untwisted complete future prime row. In this section C_cross=H_kappa+F_r
is the RAW crossing operator, not its pole-completed version;
s0=sinh(x/2), and X_mult is multiplication by x. The original source equation
is exactly

    omega^(-1)P_theta(omega X_cur)=psi f/omega.          (4)

The ordinary original operator has

    Q_delta/2=D0+D0^*+2X_mult-F-F^*+C_cross
                           +delta W-4s0 tensor s0.

Thus, on common form cutoffs and then in the now licensed scalar
source domain, its complete quadratic expression is

    Q_delta[X_cur]/2=<X_cur,psi f/omega>
                                  +<X_cur,R_theta X_cur>,     (5)

    R_theta=D0^*+2X_mult-F-F^*-F_theta+C_cross+delta W
          -beta-kappa-omega^(-1)[D0+F_theta,omega]
          -4s0 tensor s0.

All brackets in (5) are retained with their complete cutoff grouping;
this formula does not assert separately unneeded operator domains.
In particular the second row includes the whole backward, reflected,
pole and variance-commutator correction. The G3 principal is not the
original Q_delta quadratic form. Splitting L_can into X_cur and its
newly legal discrepancy only polarizes this same retained row and
does not by itself produce a negative Gram or an absorption.

The forcing pairing in (5) is integral psi^2 A_cur f/sigma^2,
whereas the older true-variance principal paired integral psi^2 A_cur f.
The earlier source and feedback contraction constants therefore do not
transfer to (5). This note proves no quantitative comparison in that
stronger source metric.
