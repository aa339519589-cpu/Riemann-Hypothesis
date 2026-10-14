# Complete same-source eta–Mobius ground identity

This note combines the genuine future Mobius seed with the complete even-Phi
ground expansion of the original odd source form. It retains the full prime
reflection, archimedean wall, pole, star-transfer cross term and Jensen defect.
There is no positivity claim for their sum, and no replacement of the original
psi metric by a Phi metric variational inequality.

## 1. Same actual source, conventions, and a useful domain bound

Let g=psi r be the actual real scalar source, with psi=-Phi', and use its proved
bounds r in L-infinity and r-c_infinity in H^s on the half-line for every s<1.
Take once and for all 1/2<s<1. The future inverse and direct maps are

    M f(x)=sum_(n>=1) mu(n)/sqrt(n) f(x+log n),
    C f(x)=sum_(n>=1) 1/sqrt(n) f(x+log n),       x>=0.

Set f=M g. These are honest absolutely convergent future sums on the actual
source, and C f=g by divisor collection. They are NOT bilateral inverses.
The seed and its shifted integer weights are

    eta(t)=exp(t/2)(4 pi^2 exp(4t)-6 pi exp(2t))exp(-pi exp(2t)),
    eta_n(x)=n^(-1/2)eta(x+log n),
    Phi(x)=sum_n eta_n(x),   p_n(x)=eta_n(x)/Phi(x).

Every eta_n is positive on x>=0. Define

    Z_n(x)=f(x+log n)/eta(x+log n),
    u(x)=g(x)/Phi(x)=E_(p(x)) Z_N(x),
    H_n(x)=Z_n(x)-u(x),      V_lat(x)=E_(p(x)) H_N(x)^2.       (1)

Here u is not the original ratio r=g/psi. The odd extension is used for g and
u, whereas the latent seed f is defined only on the positive half-line.
Most importantly, the actual common seed imposes

    Z_n(x+log d)=Z_(dn)(x).                                 (2)

It is not legitimate to optimize the label values independently of (2).

For z=pi exp(2x), the explicit theta polynomials and bounded r give

    |f(x)| <= C_r sum_k k^(-1/2)psi(x+log k)
            <= C_r(1+z)eta(x),
    |Z_n(x)| <= C_r(1+n^2 z).                              (3)

The last comparison first follows for z sufficiently large by extracting the
k=1 Gaussian and summing polynomially weighted exp(-(k^2-1)z); on the remaining
compact interval eta has a positive minimum and the same theta sum converges
uniformly. Thus no assertion that the derivative seed -eta' is positive at the
origin is needed. In particular all polynomial label moments in (1) converge
locally normally and V_lat(x)<=C_r(1+z^2).

For completeness, the same expansion yields, for every 0<alpha<s-1/2,

    |(f/eta)(t+h)-(f/eta)(t)|
          <= C_(r,s,alpha) exp(C_alpha t)|h|^alpha,
                      t>=0, 0<=h<=1.                      (4)

Indeed write f/eta as the sum of the smooth theta coefficients multiplying
r(t+log k). The coefficients and their first derivatives are bounded by a fixed
polynomial in exp(2t), times Gaussian-decaying polynomials in k. Apply the global
H^s Holder bound to r-c_infinity in the coefficient-free difference and the
mean-value bound to the coefficient difference. Uniform summability proves (4).
Equations (3)-(4) pay all the Gamma diagonal integrals below. They do not claim
that M is a bounded map on the entire original P completion.

## 2. The complete Phi-ground expansion, with all constants

Write alpha_d=Lambda(d)/sqrt(d), a_d=log d, kappa(t)=exp(-t/2)/(1-exp(-2t)),
K(x,y)=kappa(|x-y|)-kappa(x+y), and

    ell(g)=int_0^infinity sinh(x/2)g(x) dx,
    h[g]=<g_o,T g_o>_(L2(R))-8 ell(g)^2,
    T=a(D)-S,       T Phi=-cosh(x/2).

The full-line prime shift is Sg=sum_d alpha_d[g(x+a_d)+g(x-a_d)].
Use the following positive terms:

    G[u]=int_(x,y>0) Phi(x)Phi(y)K(x,y)|u(x)-u(y)|^2 dxdy,
    W_Gamma[u]=4 int_0^infinity Phi(x)u(x)^2
                           int_0^infinity kappa(x+y)Phi(y)dy dx,
    PF[u]=2 sum_d alpha_d int_0^infinity Phi(x)Phi(x+a_d)
                                     |u(x)-u(x+a_d)|^2 dx,
    PR[u]=sum_d alpha_d int_0^(a_d) Phi(x)Phi(a_d-x)
                                     |u(x)+u(a_d-x)|^2 dx,
    A[u]=2 int_0^infinity Phi(x)cosh(x/2)u(x)^2 dx.

Then the exact original source identity is

    h[g]=G[u]+W_Gamma[u]+PF[u]+PR[u]-A[u]-8 ell(g)^2.        (5)

To verify (5), apply the ordinary positive-ground identity with ground Phi to
the full-line source g. The Gamma part is one half the full double integral;
the prime part is sum_d alpha_d times the full-line shift square. The source
identity T Phi=-cosh leaves -int_R Phi cosh u^2. Split into the two positive
wings and the two crossing wings. Oddness changes the crossing differences to u(x)+u(y). The exact regrouping is

    kappa(|x-y|)(u(x)-u(y))^2+kappa(x+y)(u(x)+u(y))^2
     =K(x,y)(u(x)-u(y))^2+2kappa(x+y)(u(x)^2+u(y)^2).

Symmetry gives W_Gamma with coefficient 4. The prime crossing interval occurs
once for each positive shift, giving PR, while the two same-wing intervals
give PF with coefficient 2. This proves every factor in (5).

## 3. Star Gamma row and genuine divisor variance

For x<y use the coupling

    pi_xy(n,n)=p_n(y), n>=2; pi_xy(1,1)=p_1(x),
    pi_xy(n,1)=p_n(x)-p_n(y), n>=2.

All other entries are zero. Positivity follows from the proved strict decrease
of p_n, n>=2. Put W(x,y)=Phi(x)Phi(y)K(x,y) and define

    G_diag=2 int_(x<y) W sum_n p_n(y)|Z_n(x)-Z_n(y)|^2,
    M_xy=sum_n[p_n(x)-p_n(y)]H_n(x),
    Mix=4 int_(x<y) W[u(x)-Z_1(y)]M_xy,
    D_J=2 int_(x<y) W Var_(pi_xy)[Z_N(x)-Z_M(y)] >=0.

Let beta(w)=(4w-1)/(4w^2-6w) and, for x>0,

    R_w(t)=eta(x+t)/eta(x) when pi exp(2x)=w,
    T_n(x)=int_0^infinity kappa(2x+t)R_(n^2 pi exp(2x))(t)dt.

The covariance below always groups T_n before taking x down to zero; individual
T_n(0) are infinite. An equivalent harmless convention is to replace every T_n
by T_n-T_1, which leaves covariance unchanged.

The exact Gamma row calculation and star expansion yield

    G[u]-PF[u]
      =G_diag+2 int Phi^2 Cov_p(T_N-beta(N^2 z),H_N^2)
        +2 int Phi V_lat (F_-^+Phi-F_+Phi)+Mix-D_J.          (6)

Here

    F_+Phi(x)=sum_d alpha_d Phi(x+a_d),
    F_-^+Phi(x)=sum_(a_d<x) alpha_d Phi(x-a_d).

For reference the arithmetic step of (6), including the actual-source input,
is elementary and exact. If P_d=sum_(d|n)p_n, then

    P_d=d^(-1/2)Phi(x+a_d)/Phi(x),
    E(Z_N | d divides N)=u(x+a_d),
    Var(Z_N | d divides N)=V_lat(x+a_d),                  (7)

where the last equality uses (2). Therefore

    PF=2 int Phi^2 [E(log N H_N^2)
                         -sum_d Lambda(d)P_d V_lat(x+a_d)].

The Gamma row has coefficient exactly one on log n. Subtracting the displayed
prime density leaves sum_d Lambda(d)P_d[V_lat(x+a_d)-V_lat(x)] plus the covariance
in (6). Changing variables in the first part gives its F_-^+Phi-F_+Phi row.
The reflected primes a_d>x are not included in F_-^+.

The exact beta and T averages have theta representatives:

    Theta(x)=exp(x/2)sum_n exp(-pi n^2 exp(2x)),
    Phi E beta(N^2z)=-2Theta'(x),
    Phi E T_N=int_x^infinity kappa(x+y)Phi(y)dy,
    Theta(-x)=Theta(x)+sinh(x/2),     Theta'(0)=-1/4.       (8)

These identities do not identify the covariance with the pole term.

## 4. Complete reflected prime lift

Unlike the Gamma diagonal, the reflected prime term permits independent label
coupling without a singularity. Define the positive square

    PR_lift=sum_d alpha_d int_0^(a_d) Phi(x)Phi(a_d-x)
             E_(p(x) tensor p(a_d-x))
                      |Z_N(x)+Z_M(a_d-x)|^2 dx.           (9)

The two centered independent label errors have zero covariance. Thus

    PR=PR_lift-2 int_0^infinity Phi(x)V_lat(x) F_rPhi(x)dx,
    F_rPhi(x)=sum_(a_d>x) alpha_d Phi(a_d-x).              (10)

The factor 2 follows by interchanging x and a_d-x in one variance term. In
particular the row in (10) is the complete reflected row, not a finite-prime
substitute or an absolute bound replacing the signed identity.

## 5. Complete joint identity on the same actual source

Combining (5), (6), and (10) gives

    h[g] = G_diag + 2 PF[u] + PR_lift + W_Gamma[u] - A[u]
           -8 ell(g)^2 + Mix - D_J
           +2 int_0^infinity Phi V_lat
                              (F_-^+Phi-F_+Phi-F_rPhi)
           +2 int_0^infinity Phi^2
                       Cov_p(T_N-beta(N^2z),H_N^2).       (11)

Every term uses f=M g and g=C f, with the original Mobius coefficients. All
primes, the true eta polynomial, the odd Gamma wall, and the full pole rank-one
form are present. The same identity applies to g-c psi with f-c(-eta'), keeping
the changed pole moment. It is not legitimate to discard that moment when
using the constant-ratio null calibration.

For the actual centered supercritical source, the left side is -delta N[g]<0.
The exact comparison still needed is a nonnegative completion of the complete
right side, not positivity of its log-variance row alone. In particular Mix
has no proved sign and -D_J is nonpositive. The covariance and the complete
prime variance row are also signed. Equation (11) does not prove RH.

## 6. Convergence and cutoff order

The pointwise probability identities use the complete normally convergent label
sums. Prove the integrated identities with compact spatial cutoffs and a Gamma
separation cutoff, using (3) for absolute label convergence. Restore complete
prime sums and remove spatial/separation cutoffs using (3), (4), and the
Gaussian weights; finite numerical label truncations are not assigned the
unchanged complete marginal p or unchanged mean u.
Near x=y, the diagonal label square is O(|x-y|^(2 alpha)) times a summable
polynomial label moment. Star transfers have total mass O(|x-y|), again with
polynomial Gaussian moments, so both G_star and Mix are locally integrable
against kappa(|x-y|). The Jensen defect is finite because G_star and G are.
The grouped T covariance is controlled uniformly down to the origin by

    |T_n(x)-T_1(x)|<=log n+beta(z)-beta(n^2z),

because R_(n^2z)<=R_z and kappa(2x+t)<=kappa(t). The exact Frullani difference
therefore pays its complete centered label-square moments. At infinity the
factor Phi^2 pays all remaining polynomial moments.

For reflected prime rows, the elementary Chebyshev bound on logarithmic blocks
gives F_rPhi(x)<=C exp(x/2), and the analogous positive backward row has the
same bound. Equations (3) and theta decay then give absolute integrability of
(9)-(11). The forward row decays faster still. Thus Tonelli applies to their
nonnegative lifted squares and ordinary absolute Fubini to the displayed row
reductions. No undamped sum sum mu(n)r(log n) is separated anywhere.

Finally, the full source form in (5) is finite by the already established actual
H^s and theta weighted source bounds. Its derivation can be obtained by compact
source approximation; the estimates above justify the same limit in (11).
No moving source, altered Green eigenvalue inequality, or unproved infinite
quadratic delta-load pairing occurs.

## 7. Dependencies and reproducible checks

The source-domain inputs are the [anchored future inverse theorem](../20261014_anchored_future_mobius/REPORT.md) and the [actual ratio multiplier theorem](../20261014_actual_ratio_multipliers/REPORT.md). The complete Phi-ground realization is established in [Original form foundation, Sections 6–7](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md).

[ETA_TRANSPORT.md](ETA_TRANSPORT.md) contains the complete positive star-coupling proof, exact Frullani calculation, and centered star/divisor algebra. [DOMAIN.md](DOMAIN.md) independently proves the integrated actual-source Gamma domain, including the origin corner and the retained positive Jensen defect.

Run `python check_eta_gamma_transport.py` with Python and mpmath. The checker uses exact fractions for the centered star algebra and high-precision independent quadrature for both scalar Gamma integrals. The checked output is [check_result.json](check_result.json). These finite checks supplement, not replace, the algebraic proofs. No numerical check of RH or complete signed positivity is claimed.
