# Coarse original-form costs for the natural-mask right field and its complete future exits

The natural finite mask applied to the same physical field H produces
compact logarithmic source tests with original-form cost O(N). The same
bound holds for their complete future-prime row and their separated
continuous far-exit row. Both polar mask cancellations are used, but two
nonzero logarithmic remainders must be retained.

These are coarse bounds, not a subpower estimate or a signed comparison.
They do not control the critical first variation, an arbitrary
N-dependent Green weight, or the full uncut original-form energy. No
positivity assumption on the mixed collar is made or proved.

## 1. Definitions and theorem

Use the physical Fourier convention

    Fourier(f)(xi)=int_R f(u)exp(-2pi i u xi)du,
    X_s=L2(R,|u|^(2s)du).

All fields are real, and physical fields are even. Physical integrals without another measure
use du; the logarithmic source coordinate is x=log t. Let H satisfy

    Fourier(H)=H,   H(u)=c on |u|<1,
    H in H^s(R) intersect X_s for every 1/2<s<1,
    int_R H(u)du=c.                                  (1)

In the intended application H is the SAME actual-field completion
H=Dw+c from the
[physical range theorem](../20261015_old_actual_physical_range/REPORT.md).
Its actual origin, complete signed load, and constant channel are not
changed here. The estimates below only require the displayed properties
(1). In particular they are not another actual-source exclusion theorem.

Write mu for the Mobius function and Lambda for the von Mangoldt
function, with Lambda(1)=0. Define physical operators

    D_d f(u)=f(du),
    C f(u)=sum_(n>=1)f(nu),
    M_N=sum_(m<=N)mu(m)D_m,
    B0=I-5D4+4D16,
    P_N=B0 M_N=sum_d a_d D_d,
    F_N=P_N H,   e_N=C F_N,   L=16N,   q_d=L/d.

Here D_d is dilation, not differentiation. The finite coefficients obey

    a_d=mu(d)1_(d<=N)
         -5*1_(4|d)mu(d/4)1_(d/4<=N)
         +4*1_(16|d)mu(d/16)1_(d/16<=N),
    d<=L, q_d>=1, sum_d |a_d|<=10N,
    sum_d a_d=sum_d a_d/d=0.                         (2)

Every prime power remains in Lambda. The complete Euler operator C is
bounded on X_s for s>1/2, since its dilation norms sum to
zeta(s+1/2). The same is true of the complete future-prime operator
f -> sum Lambda(n)f(nu).

Fix a compact interval I contained in (1,infinity), a smooth multiplier
omega supported in its interior, and B>max I. These choices, including
the positive input/exit separation, are independent of N. The three
compact logarithmic sources are

    t_N(x)=omega(t)sqrt(t/L)e_N(t/L),
    p_N(x)=omega(t)sqrt(t/L)sum_(n>=2)Lambda(n)e_N(nt/L),
    g_N(x)=omega(t)sqrt(t/L)
              int_B^infinity s e_N(s/L)/(s^2-t^2)ds,
    t=exp x.                                        (3)

The source normalization is sqrt(t/L), not sqrt(t). The last integral
is exactly the physical future exit starting at B/L, after changing its
integration variable from y to s=Ly. There is no additional Jacobian.
The prime row in (3) has no factor 1/n.

**Theorem.** For any fixed 1/2<s'<s<1 and sufficiently small sigma>0,
for example 0<2sigma<s'-1/2, the sources in (3) belong to the original
form domain and satisfy

    ||t_N||_(H^sigma(dx))+||p_N||_(H^sigma(dx))
                          +||g_N||_(H^sigma(dx))<=C sqrt N,
    P[t_N]+P[p_N]+P[g_N]
      +|Q_delta[t_N]|+|Q_delta[p_N]|+|Q_delta[g_N]|<=C N.  (4)

Here 0<delta<1 is fixed, and the original forms are specified below.
The constant may depend on H, s, s', sigma, delta, I, omega and B, but
not N. No assertion with the same constant is made for a moving B,
a shrinking input/exit gap, or an arbitrary N-dependent omega.

### Original-form normalization

For clarity, the forms in (4) are the original half-line source forms,
not ordinary physical L2 substitutes. Put

    B_log(x)=exp(x/2-pi exp(2x)),
    xi(x)=-(partial_x^3-partial_x/4)B_log(x),
    psi(x)=sum_(n>=1)n^(-1/2)xi(x+log n),
    alpha_n=Lambda(n)/sqrt(n),
    F_r f(x)=sum_(log n>x)alpha_n f(log n-x),
    V(x)=(F_r psi)(x)/psi(x),
    ell(f)=int_0^infinity sinh(x/2)f(x)dx.

Let f_o be the odd extension of f to the full log line, with Fourier
transform fhat_o(t)=int_R f_o(x)exp(itx)dx. Then

    q0[f]=(1/(2pi))int_R
              [Re digamma(1/4+it/2)-log pi]|fhat_o(t)|^2dt
          -2sum_n alpha_n int_R f_o(x)f_o(x+log n)dx
          -8|ell(f)|^2,
    N[f]=2int_0^infinity V(x)|f(x)|^2dx
          -2sum_n alpha_n int_0^(log n) f(x)f(log n-x)dx,
    P[f]=q0[f]+N[f],   Q_delta[f]=q0[f]+delta N[f].   (5)

The q0 source formula and its completion are given in the
[original source form](../20261012_localized_odd_schur/SOURCE_FORM.md).
The theta ground and N, P, Q_delta conventions are those explicitly
stated in Section0 of the
[physical range theorem](../20261015_old_actual_physical_range/REPORT.md),
and are repeated in full above. P[f] is source notation for the
corresponding original ratio energy P[f/psi]. All pole, forward,
reflected and potential terms in (5) remain.

For a fixed compact log interval strictly above zero, H^sigma with any
sigma>0 controls the absolute Gamma form, whose Fourier multiplier grows
only logarithmically. The original V is bounded there. In the quadratic
forward and reflected pairings only finitely many prime-power labels
meet both compact supports, and each such row is L2 bounded. The pole
is a bounded rank-one form. Consequently

    P[f]+|Q_delta[f]|<=C ||f||_(H^sigma)^2           (6)

for sources on that fixed compact. Smooth approximation there converges
in the original form completion. Thus it remains to prove the Sobolev
bounds in (4), rather than replace the original form by another domain.

## 2. Complete Poisson and reciprocal Euler estimates

The assumptions (1) imply H in L1, and complete Poisson gives

    C H(y)=y^(-1)C H(1/y)+(c/2)(y^(-1)-1).           (7)

This is used in local Sobolev closure, not by assuming pointwise
convergence of every Euler series. The necessary closure can be seen
directly. If f is in H^s intersect X_s and lambda>=1, fixed compact
inversion t -> 1/t and localization give

    ||omega(t)f(lambda/t)||_2<=C lambda^(-s-1/2)||f||_(X_s),
    ||omega(t)f(lambda/t)||_(H^s)<=C lambda^(s-1/2)||f||_(H^s).

Interpolation therefore gives

    ||omega(t)f(lambda/t)||_(H^sigma)
                         <=C lambda^(-s-1/2+2sigma). (8)

The same bounds hold with the harmless additional smooth compact
multipliers 1/t and sqrt(t). For 0<2sigma<s-1/2, summing (8) at
lambda=nq yields

    ||omega(t)(q/t)C f(q/t)||_(H^sigma)
                         <=C q^(1/2-s+2sigma)<=C,
                         q>=1.                    (9)

The complete n sum converges absolutely in this local space. The same
argument holds with an extra log n because its exponent is below -1.

For general f and its Fourier transform in H^s intersect X_s, the
ordinary Schwartz Poisson formula passes to these local spaces by
simultaneous approximation in that intersection. Trace convergence
follows from s>1/2, and mean convergence follows from X_s and L2.
Fourier interchanges the weighted and Sobolev norms. This proves (7)
for H and will also justify its logarithmic version below.

Apply (7) at y=dt/L=t/q_d and sum the SAME finite coefficients a_d.
Both polar terms cancel jointly by (2), leaving exactly

    e_N(t/L)=sum_d a_d(q_d/t)C H(q_d/t).             (10)

Do not take a separate norm of either uncancelled polar term. Equations
(9)-(10), sum|a_d|<=10N and the factor L^(-1/2) show

    ||t_N||_(H^sigma(dx))<=C sqrt N.                 (11)

The smooth change between physical t and x=log t on the fixed compact
has uniform Sobolev composition bounds. Together with (6), this proves
the first source estimate in (4).

## 3. The complete future-prime row

### Logarithmic Poisson identity with its actual constant

Set gamma(u)=exp(-pi u^2), h=H-c gamma, and define

    f_log(u)=(log|u|)h(u),
    A h=f_log+Fourier(f_log),
    Z_h(v)=sum_(k>=1)(log k)h(kv).                  (12)

The even h is self-Fourier with zero trace and mean. For
1/2<s'<s<1, f_log belongs to H^(s') intersect X_(s'). Here is a direct
proof sufficient for the actual field. On |u|<1, h=c(1-gamma), so
f_log=O(u^2 log|u|) and its first derivative is square integrable.
On dyadic annuli of radius R>=1, localization gives an L2 bound
C R^(-s) from X_s and a uniform H^s bound from global H^s. Interpolation
gives an H^(s') bound C R^(-(s-s')). Multiplication by log|u| on that
annulus costs only C(1+log R), including its derivatives, and the
annular bounds sum. The X_(s') bound follows directly from
sup_(u>=1)u^(s'-s)log u<infinity. The compact transition is harmless.
Fourier thus places A h in the same intersection, with a continuous
value A h(0).

Apply the Poisson closure from Section2 to f_log. Its trace is zero,
and Fourier(f_log)=A h-f_log. Consequently

    Z_h(v)=v^(-1)[C(A h)(1/v)-Z_h(1/v)]+A h(0)/(2v). (13)

Indeed C f_log(v)=Z_h(v)+(log v)C h(v), and the log v terms cancel by
C h(v)=v^(-1)C h(1/v). This proves (13) without introducing an
unweighted infinite Euler inverse or an unproved source derivative.

Since Lambda*1=log and both complete operators converge absolutely on
X_(s') for s'>1/2, the original physical future-prime row is exactly

    sum_(n>=2)Lambda(n)e_N(nu)
      =sum_d a_d Z_H(du)
      =sum_d a_d {
          (du)^(-1)[C(A h)(1/(du))-Z_h(1/(du))]
          +A h(0)/(2du)+c Z_gamma(du)}.             (14)

In particular this is the unweighted sum Lambda(n)e_N(nu), not the
separate weighted sum Lambda(n)e_N(nu)/n.

### Gaussian subtraction and the nonzero logarithmic rank

For every prescribed finite derivative order and every fixed T,

    Z_gamma(v)=v^(-1)[A_gamma-(log v)/2]
                           +log(2pi)/2+R_gamma(v),
    A_gamma=int_0^infinity exp(-pi t^2)log t dt,     (15)

where R_gamma has bounded corresponding derivatives on [0,T]. To check
this normalization, use the Mellin integrand
-zeta'(s)M gamma(s), with M gamma(s)=pi^(-s/2)Gamma(s/2)/2.
The double pole at1 gives the v^(-1) row. The pole at0 gives the
positive constant log(2pi)/2. Moving the contour a finite distance
farther left and retaining the negative-even poles gives the finite
even polynomial and a differentiably bounded remainder required for
any specified order. No convergent infinite asymptotic series is used.

Define the finite Dirichlet polynomials

    b0(s)=1-5*4^(-s)+4*16^(-s),
    m_N(s)=sum_(m<=N)mu(m)m^(-s).

In (14), sum a_d/d=0 removes the A h(0) rank. Both moments remove the
Gaussian A_gamma, log u and constant pieces, but the log d piece
survives:

    -(c/(2u))sum_d a_d log d/d
       =c b0'(1)m_N(1)/(2u),
    b0'(1)=3log4/4.                                (16)

This term is NOT zero. For completeness, the elementary identity
1=sum_(m<=N)mu(m)floor(N/m) gives
N m_N(1)=1+sum_(m<=N)mu(m){N/m}. The m=1 fractional part is zero;
there are at most N-1 other terms of modulus less than one. Thus
|m_N(1)|<=1, also for N=1.

### Source estimate

Use (8) with exponent s' and f=A h or h. For j=0,1 and
0<2sigma<s'-1/2,

    ||omega(t)(q/t)sum_n(log n)^j f(nq/t)||_(H^sigma)
                           <=C q^(1/2-s'+2sigma)<=C. (17)

After u=t/L in (14), the reciprocal terms are bounded by (17). The
nonzero rank (16), multiplied by sqrt(t/L), is O(sqrt N) on the fixed
compact. The remainder c sum a_d R_gamma(dt/L) has the same source
bound: dt/L=t/q_d lies in a fixed bounded interval, and its fixed
Sobolev derivatives are uniformly bounded before summing |a_d|.
Hence

    ||p_N||_(H^sigma(dx))<=C sqrt N.                 (18)

This proves the second assertion of (4), including all original
prime-power, reflected, potential and pole costs through (6).

## 4. The separated continuous far exit

Let

    E_q(s)=(q/s)C H(q/s),
    G_far,N(t)=int_B^infinity s e_N(s/L)/(s^2-t^2)ds.

Equation (10) holds also with s in place of t, in the stated local
closure. Poisson isolates c/2 in each E_q. Subtract that constant from
EVERY branch before integrating, and only then use sum a_d=0. No
pointwise claim C H(v)->0 is needed.

Split s/(s^2-t^2)=1/s+t^2/[s(s^2-t^2)]. The first branch integral is

    J_q=int_B^infinity [E_q(s)-c/2]ds/s
       =int_0^(q/B)[v C H(v)-c/2]dv/v
       =-(c/2)log q+O_(H,B)(1), q>=1.              (19)

At zero, Poisson gives
v C H(v)-c/2=C H(1/v)-cv/2. Its integral against dv/v is absolute
because C H has an X_s positive tail, s>1/2. At infinity, C H is L1
by the same bound. These observations prove both the branchwise
integrability and the uniform remainder in (19).

The logarithmic sum is retained exactly. With S_N=sum_(m<=N)mu(m),

    sum_d a_d log q_d=-sum_d a_d log d
                                  =-3log4 S_N.     (20)

It is O(N), not zero. Thus a separate O(log q) cost on each branch
must not be replaced by a spurious O(N log N) total.

For the second branch, the fixed gap max I<B gives, for every fixed
nonnegative integer j,

    |partial_t^j int_B^infinity
           t^2[E_q(s)-c/2]/[s(s^2-t^2)]ds|
       <=C_(I,B,j) q^(-2)int_0^(q/B)
                               v |v C H(v)-c/2|dv
       <=C_(I,B,j,H)(1+q^(1/2-s))<=C.              (21)

Near zero use the same Poisson identity. For v>=1, Cauchy in X_s gives
int_1^Q v^2|C H(v)|dv<=C Q^(5/2-s); the c/2 part contributes O(Q^2).
All differentiated denominators are uniformly separated from zero.
Summing (19)-(21) with (2) proves

    ||G_far,N||_(C^j(I))<=C_j N.                    (22)

Multiplication by omega(t)sqrt(t/L), followed by (6), proves the final
bound in (4). This is the complete continuous far-exit kernel at
threshold B/L, not a claim about its local diagonal or a separate
log-u term in the full drift.

## 5. What the estimates do and do not control

Both nonzero logarithmic remainders (16) and (20) are part of the
proof. The complete constant channel c is retained throughout. If a
microscopic input/exit geometry has B<2 min I, every future-prime jump
from I crosses the exit threshold, so (18) is exactly that entire
prime-exit field. More general fixed geometries must explicitly retain
the finitely many nonexit dilations instead of assigning them a sign.

The costs in (4) all have the same N scale. Combining them into a
finite original-form Gram does not turn O(N) into O_eta(N^eta), nor
does polarization of nonnegative quadratics sign a mixed pairing.
In particular this report does not establish a uniform bound for an
N-dependent occupation weight, discard the full right overshoot in a
product identity, bound its two ordered covariances, or remove the
critical physical region u of order 1/N. The uncut fields are not
promoted to the original form domain.

The [right-field replacement theorem](../20261015_natural_mask_right_error/REPORT.md)
addresses a different error estimate and explicitly retains its signed
main and delta head first variation. The present coarse source costs do
not pay those remaining terms and are not an independent positive
reserve. They imply neither the universal crossing sign, K<=1, nor RH.
