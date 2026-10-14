# A complete signed Mobius-profile spatial factor on the same current

The genuine profile a(n)=1-mu(n) has a special divisor-incidence sign which
arbitrary nested-label combinations do not have. Its FULL spatial matrix,
including every prime power and every square collision, has a strict positive
comparison with the coherent star field. This concerns a rank-one arithmetic
profile, not the whole hidden field or the canonical inverse M g. The actual
conditional projection onto this profile is legal in the stated averaged
forms; its centering and residual cross terms are retained explicitly.

Dependencies are the [general incidence factor](../20261014_same_current_star_blocks/NESTED_INCIDENCE.md),
[the original current mask/domain theorem](BOUNDED_MASK_DOMAIN.md),
and [the complete second-label score comparison](../20261014_first_label_coercive_correction/SECOND_LABEL_COMPLETION.md).

## 1. Complete arithmetic coefficient and strict potential

Write mu_ar for Mobius, mu_0=psi^2 for the original measure, p_n for the
complete eta posterior, and a_score,n for the positive refresh score.
Let beta=T a_score and define the FIXED label profile and its moments

    a(n)=1-mu_ar(n) in {0,1,2}, a(1)=0,
    m_1=T a, m_2=T a^2, sigma_a^2=m_2-m_1^2,
    V_a=T[(a_score-beta)a^2].

The complete score estimate gives

    a_score,n-beta>3log2 for every n>=2,
    V_a>3log2 m_2.                                    (1)

Indeed a_score,2>3log2+(9/2)log2/s, whereas
beta/p_1<(48521/16000)/s and (9/2)log2>621/200. Their difference is
>3log2+1159/(16000s), and a_score,n>=a_score,2 for n>=2.
This uses the complete theta moments, not a first-label replacement.

For a true prime power d and child label m, the exact incidence is

 a(m)[a(dm)-a(m)]=a(m)[mu_ar(m)-mu_ar(dm)]
   =-4, if mu_ar(m)=-1, d is prime, and (d,m)=1;
   =-2, if mu_ar(m)=-1 and dm is not squarefree;
   = 0, otherwise.                                   (2)

If mu_ar(m)=1 the prefactor is zero. If mu_ar(m)=0 then both Mobius
values are zero. The remaining case is mu_ar(m)=-1: a new prime makes
mu_ar(dm)=1, while every repeated prime or higher prime power makes it0.
This proves (2) for ALL labels and ALL prime powers.

Put

    C_d(y)=-sum_m p_m(y)a(m)[a(dm)-a(m)].

Then C_d>=0 and, exactly rather than only in absolute value,

    C_d=4sum_(mu_ar(m)=-1, d prime, (d,m)=1)p_m
         +2sum_(mu_ar(m)=-1, dm not squarefree)p_m,
    0<=C_d<=4sum_(mu_ar(m)=-1)p_m<=m_2.              (3)

Thus square collisions are retained with coefficient2, not deleted.

## 2. Exact full spatial factor and its nonlocal sign

Let A(x) be a real scalar amplitude and Y_n(x)=A(x)a(n). Let E_sp be the
genuine hidden continuous-Gamma plus divisor energy, and F_star the
original forward energy of the SAME coherent star initial-label field.
The complete general incidence formula gives

 E_sp[Y]-F_star[Y]
   =int mu_0 V_a A^2
      +2sum_d alpha_d int_0^infinity
                  psi(x)psi(y) C_d(y) A(x)A(y)dx,
    y=x+log d, alpha_d=Lambda(d)/sqrt(d).             (4)

The cross term is not declared positive. In particular opposite signs of
A(x),A(y) are permitted. It is paid in its TRUE two-endpoint metric.

The complete posterior bounds are

    p_2(x)>16p_1(x)exp(-3z), p_1>=400/401,
    q_tail(x)=sum_(n>=2)p_n(x)<=28exp(-3z), z=pi exp(2x).

Since 4p_2<=m_2<=4q_tail, for EVERY d>=2,

    m_2(x+log d)/m_2(x)
      <(2807/1600)exp[-3(d^2-1)z]
      <2exp[-3(d^2-1)z].                            (5)

Set B(x)=psi(x)sqrt(m_2(x))A(x). From (3)-(5), the absolute value of the
second line of (4) is bounded by

 2sqrt(2)sum_(d>=2)alpha_d exp[-(3pi/2)(d^2-1)] ||B||_2^2
       <(1/60000)||B||_2^2.                         (6)

Here future translation is an L2(dx) contraction. To check the entire
constant without a cutoff, use Lambda(d)/sqrt(d)<=sqrt(d), pi>3 and
exp(3)>16. The first term after the prefactor is4exp(-27/2)<1/65536.
The ratio of successive majorant terms is at most
sqrt(3/2)exp(-45/2)<2^(-29). Therefore the complete series is less than
[1/65536]/[1-2^(-29)]<1/60000. Composite non-prime-powers are included
only in this upper bound; the exact signed expression remains (4).

Consequently the FULL comparison is

 E_sp[Y]>=F_star[Y]+(3log2-1/60000)int mu_0 m_2 A^2
          >=F_star[Y]+2int mu_0 m_2 A^2.             (7)

The coefficient 3log2-1/60000 is strictly greater than2; the last
energy inequality is strict when A is nonzero in L2(mu_0 m_2).
This is a positive arithmetic subspace of the full signed matrix, not
an assertion that the general off-diagonal matrix is positive. No prime
or Gamma budget from another identity is added to (7).

## 3. Common cutoffs and the SAME actual projected amplitude

For a smooth compact amplitude, (4) follows first with common spatial,
Gamma-diagonal and label cutoffs. The identity (2) is then applied only
after the full infinite label limit: a truncated profile a(n)1_(n<=N)
has the additional exact incidence

 a(m)1_(m<=N)[a(dm)1_(dm<=N)-a(m)1_(m<=N)]
      -a(m)[a(dm)-a(m)].                            (8)

It is supported at dm>N. Absolute value is at most8, so its paired
contribution is controlled by the complete initial-label tail
sum_(n>N)p_n L_n, with the SAME two endpoint values of A. This tends to
zero for bounded compact amplitudes by the full Gaussian posterior and
score bounds. No independent finite-cutoff multiplicativity is claimed.

For the SAME actual current w, let u=T w and H_n=w_n-u. Its natural
conditional orthogonal projection amplitude is

    A_*(x)=T(a H)/sigma_a^2=-T(mu_ar H)/sigma_a^2.     (9)

This does not identify w with the canonical Mobius seed. The exact
conditional decomposition is

    H_n=A_*[a(n)-m_1]+Z_n,
    T Z=0, T(a Z)=0,
    V=sigma_a^2 A_*^2+T Z^2.                        (10)

The scalar A_* is bounded on the whole positive wing. Here are domain
details rather than a division-by-small-posterior assumption. Put
q=q_tail, pi_n=p_n/q for n>=2, and h_n=w_n-w_1. Then

    D=m_2/q-q(T_pi a)^2,
    A_*=sum_(n>=2)pi_n[(a(n)-m_1)/D]h_n,
    D=sigma_a^2/q>=4p_1p_2/q>2.                     (11)

The last strict bound follows from q/p_2<2807/1600 and p_1>=400/401.
The complete actual estimate |h_n|<=C(1+log n) and
pi_n<=C n^4 exp[-(n^2-4)z] pay the boundedness in (11).

For the continuous domain, write b_n=pi_n(a(n)-m_1)/D. The normally
convergent explicit theta series gives

    |b_n|<=C pi_n,
    sum_(n>=2)(1+log n)|b_n'(x)|<=C z exp(-3z).       (12)

For clarity, derivatives of every pi_n with n>=3 are bounded by
C n^2 z pi_n, the pi_2 derivative is minus their sum, and m_1'=O(z exp(-3z)).
The same estimates give D'=O(z exp(-3z)). They prove (12) also on the
compact origin region by smooth convergence, with a larger finite C.

At x<y split Delta A_* using b_n(y)Delta h_n and
[b_n(x)-b_n(y)]h_n(x). Multiplying its square by m_2(y)<=4q(y), the first
term is paid by C sum_(n>=2)p_n(y)|Delta h_n|^2. The latter is paid by
the SAME hidden continuous energy and the already legal w_1 continuous
energy. The second term is paid by (12), the logarithmic label bound,
and the integrability of the full Gamma kernel with a squared local
increment. Thus the weighted continuous energy of Y=A_*a is finite.
All divisor energies are finite from bounded A_*, |a|<=2 and the complete
theta prime rows. The potential integral is finite because
T(a_score a^2)<=4beta and int psi^2 beta<infinity.
The star cooling term is finite by the smooth complete moment m_2 and
bounded A_*. This proves both positive energies in (4) are finite for (9).
Approximating A_* in the weighted local logarithmic form, then cutting
the original theta tails, gives (4)-(7) for this SAME actual amplitude.
No legality of the individual unweighted sources psi*w_n is used.


### Natural finite Mobius cutoffs retain the signed incidence

There is also a finite approximation better suited to the actual Mobius
mask: a_N(n)=1-mu_ar(n)1_(n<=N), N>=2. It equals1 beyond N, not0.
If dm<=N its incidence is (2). If m<=N<dm, its incidence is exactly-2
when mu_ar(m)=-1 and0 otherwise. If m>N it is0. Consequently

    a_N(m)[a_N(dm)-a_N(m)]<=0,
    -a_N(m)[a_N(dm)-a_N(m)]<=a_N(m)^2.

The entire cutoff branch is retained with coefficient2. Since a_N(1)=0,
a_N(2)=2 and0<=a_N<=2, all complete two-endpoint and score estimates
above apply uniformly, with m_1,m_2 replaced by their a_N moments.
Thus the complete uncentered factor (7) holds before every natural finite
Mobius limit. This is distinct from the auxiliary zero-label truncation
(8), whose explicit boundary is still used for the density proof.

## 4. Full original boundary covariance and the centering debit

The same star law gives the uncentered covariance

    E[Y(x)Y(y)]=A_*(x)A_*(y)m_2(max(x,y)).           (13)

All original Gamma-wall, reflected-prime and pole forms of this field
are evaluated with (13) and diagonal m_2 A_*^2, with their original
coefficients. The expected original-P norm is finite by Section3 and the
bounded ratios. Actual Q_delta>=0 therefore applies to each lawful cut
and its integrated limit, giving

    2F_star[Y]-B_delta,star[Y]>=0,
    2E_sp[Y]-B_delta,star[Y]
         >=2(3log2-1/60000)int mu_0 m_2 A_*^2.      (14)

The full pole covariance in (13), rather than the square of its mean,
is required in B_delta,star. No independent positive boundary budget is
added here.

The orthogonal component in (10) is CENTERED, whereas Y is not. Write
b(x)=m_1(x)A_*(x), so D_n=Y_n-b has mean zero. Its star covariance is
(13)-b(x)b(y). Centering has a genuine spatial defect. In the common weak
form domain its exact expression is

 E_sp[D]-F_star[D]
   =E_sp[Y]-F_star[Y]
       -2int mu_0 T{Y_n[(A_sp U b)_n-G b]},          (15)

where U b is the label-independent field and A_sp is the true continuous
plus divisor generator (reset kills U b). To verify it, use the complete
intertwining T A=G T in the polarized product rule:

 T Gamma_A(U b,Y)=Gamma_G(b,T Y)
                       +T{Y_n[(A_sp U b)_n-G b]}.

The scalar field U b has identical genuine and star energy. This proves
(15) and keeps its actual continuous/divisor correlation. Formula (7)
DOES NOT remove this centering debit or the cross with the residual Z
in (10). Those are the remaining SAME-current signed terms. In particular
(14) is neither full Q_delta positivity without its hypothesis nor an RH
proof, and it does not transfer stationarity to Y, D, Z or the canonical
seed.
