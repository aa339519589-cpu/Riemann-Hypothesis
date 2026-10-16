# An original-reference comparison at a selected neutral-ground minimum

Date: 2026-10-16.

For the same actual negative source and an attained neutral-ground
minimum, we prove

    integral q V_psi v <=(2/delta-1) integral q Rv,
    q=e^2/h,                                        (1)

for the positive neutral seeds specified below. In particular the
normalized positive shifted-Phi seeds give

    sup_(z>=z_0) integral_(z-1)^(z+1) q/psi<infinity

for some fixed z_0>1. This is a moving-window L1 bound only on the far
tail; it does not include a window touching the wall. The comparison uses the original actual
equation, the complete positive edge forms, and one-sided minimizing
inequalities. It does not replace the old reflected metric by the new
one, assign positivity to an arbitrary cross form, or assume a signed
feasible ground variation.

The conclusion concerns the optimized reciprocal source q. It does not
bound the original current W_psi g, give a reverse signed IMS estimate,
or control e/h near zeros of e/psi. The original upper bound and RH
remain unproved.

## 1. Complete objects and selected-pair hypotheses

All unqualified integrals are on (0,infinity). Use

    s(x)=sinh(x/2), ell(f)=integral s f,
    U(f)=integral exp(x/2)f,
    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    kappa(d)=exp(-d/2)/(1-exp(-2d)),
    J_o(x,y)=kappa(|x-y|)-kappa(x+y)>0.

Every sum includes every prime power. Set

    F_+f(x)=sum_n alpha_n f(x+d_n),
    F_-f(x)=sum_(d_n<x) alpha_n f(x-d_n),
    Rf(x)=sum_(d_n>x) alpha_n f(d_n-x),
    Q0 f/2=Gf-F_+f-F_-f+Rf-4ell(f)s,                (2)

where G is the positive-half restriction of the full Gamma multiplier
on the odd extension. Thus q0 has the full pole -8ell(f)^2.
Let psi=-Phi' be the positive odd theta source, with ell(psi)=1/8,
and write

    L=Rpsi, V_psi=L/psi, W_psi=V_psi-R.

The complete smooth-seed estimates give L<=C exp(x/2) and
L(x)/exp(x/2)->U(psi)>0.

Fix the SAME actual real source g from the
[actual-ratio report](../20261014_actual_ratio_multipliers/REPORT.md),
and any finite gauge e=g-c psi used by the selected minimum. We use

    e=psi a, a bounded and globally Holder,
    Q0 e=-2delta W_psi e, 0<delta<1.                 (3)

Its odd extension is bounded Holder. All prime and pole terms in (3)
are retained; (3) is not asserted in a changed metric.

A nonnegative complete weak-neutral ground h satisfies the absolutely
defined equation integral h Q0 phi=0 for compact smooth positive-half
tests. The published wall closure also gives U(h)<infinity and the
through-wall odd extension of this equation. Suppose ell(h)=1,
e=0 a.e. on {h=0}, and

    q=e^2/h on {h>0}, q=0 on {h=e=0},
    D_h[e]=integral q Rh<infinity,
    N_h[e]=2D_h[e]-2<e,Re>.                         (4)

The complete positive ground form is

    P_h[e]=double integral J_o E_h[e]
       +2 sum_n alpha_n integral E_h[e](x,x+d_n)dx
       +4 double integral s_x s_y E_h[e],           (5)

where E_h[e]=h_x h_y(e_x/h_x-e_y/h_y)^2 at positive endpoints
and is zero when a ground endpoint is zero. Its pole block is exactly
8[ell(h)ell(q)-ell(e)^2]. The
[full ground-identity addendum](../20261016_neutral_wall_heat_picone/GROUND_IDENTITY_ADDENDUM.md)
and the finite-gauge extension in the
[joint report](../20261016_joint_gauge_minimizing_compactness/REPORT.md)
give

    P_h[e]-N_h[e]=q0[e].                            (6)

Assume h is a lawful minimum for this fixed e over the normalized
nonnegative weak-neutral finite-diagonal class. The jointly attained
pair in the joint report has this property at its selected gauge.
Only the positive mixtures h+t v will be used. Positive rescaling of
a ground changes neither energy, so their normalization is harmless.

The already proved
[reciprocal budget](../20261016_joint_gauge_minimizing_compactness/RECIPROCAL_INTEGRABILITY_ADDENDUM.md)
supplies

    integral s psi (e/h)^2<infinity,
    integral exp(beta x)q<infinity
       for every fixed real beta.                  (7)

No strict positivity or pointwise lower comparison for h is assumed.
All ratios involving e/h are set to zero on the common-zero set.

## 2. Admissible fixed positive seeds

The theorem applies to each fixed v satisfying all of the following:

* v is a strictly positive complete weak-neutral source, smooth and odd
  through the wall, with bounded globally Holder odd extension;
* v is bounded, 0<ell(v)<infinity, U(v)<infinity, and integral v/s<infinity;
* b=e/v is bounded and globally Holder of some positive exponent;
* the fixed integrals

      M_0=integral e^2/(s v),
      M_1=integral exp(x)e^2/(s v),
      M_p=integral s e^2/v,
      M_v=integral exp(x)v/s                         (8)

  are finite;
* the complete seed rows obey

      F_+v+F_-v+Rv <=C_v exp(x/2).                  (9)

Constants here may depend on v. The comparison factor in (1) will not.
The normalized shifted-Phi seeds in Section 6 satisfy these hypotheses
for every fixed shift. No uniform Holder or reciprocal constant over
that family is needed.

For fixed t>0, h+t v is a lawful competitor. Indeed q_t=e^2/(h+t v)
obeys q_t<=q, so

    integral q_t R(h+t v)
       <=D_h[e]+t integral q Rv<infinity.            (10)

The full ground identity applies, all common zeros are preserved as
source zeros, and minimum therefore gives

    P_(h+t v)[e]-P_h[e]
       =N_(h+t v)[e]-N_h[e]>=0.                     (11)

## 3. Fixed-v reciprocal budget, with the full pole

Put H=h/v, b=e/v, p=e/h, and

    q_t=v b^2/(H+t), A_t=H+t/2,
    J_t^v=integral s v b^2/[H(H+t)].                 (12)

At a common zero every quotient is zero. Finite ell(q) makes
J_t^v<=ell(q)/t finite for fixed t before any uniform estimate.
On each edge, the exact quotient of E_(h+t v)-E_h, divided by t,
is v_x v_y D_t, where

    D_t=(H_x-H_y)
        [b_x^2/(H_x(H_x+t))-b_y^2/(H_y(H_y+t))].     (13)

At H_x=b_x=0 this is b_y^2/(H_y+t), not zero. Completing a square gives

    D_t=I_t-S_t,
    I_t=(b_x-b_y)^2/(H_x+H_y+t),
    S_t=[sqrt(H_y(H_y+t)/(H_x(H_x+t)))b_x
          -sqrt(H_x(H_x+t)/(H_y(H_y+t)))b_y]^2
                      /(H_x+H_y+t)>=0.              (14)

At a zero endpoint S_t is defined as zero; (14) then holds directly.
Also, when H_x>=H_y, (D_t)_+<=b_x^2/(H_x+t), and symmetrically
for the other ordering.

The exact pole quotient, using ell(h)=1, is

    8ell(v)ell(q_t)-8J_t^v.                         (15)

In particular its negative coefficient is not discarded.
For completeness, the global Gamma absorption works as follows.
Bounded v and J_o<=kappa(|x-y|) imply, for 0<l<=l_0<1,

    integral_(|x-y|>=l) J_o(x,y)v_y dy
       <=C_v(1+log(1/l)),
    integral_(|x-y|<l) J_o(x,y)v_y |x-y|^(2alpha)dy
       <=C_(v,alpha) l^(2alpha).                    (16)

Choose l_x=l_0 exp[-c s(x)/A_t(x)]. Split the pairs into the UNION
of |x-y|<l_x and |x-y|<l_y, and its complement, where BOTH far
cutoffs hold. Holder continuity of b bounds the near integral of
v_xv_y I_t by

    C integral v_x l_x^(2alpha)/A_t(x) dx
       <=C_c integral v/s.                         (17)

Here exp(-2alpha c s/A)/A<=1/(2alpha e c s).
On the far set, symmetry and (16) give

    C integral v b^2/A_t
       +C c integral s v b^2/A_t^2
       <=C sqrt(M_0 J_t^v)+C c J_t^v.              (18)

The inequality H(H+t)<=A_t^2 has the indicated direction.
The complete forward-prime positive quotient is bounded by

    2 integral q_t(F_+v+F_-v)
       <=C_v integral exp(x/2)q_t
       <=C_v sqrt(M_1 J_t^v).                      (19)

Every proper power is included. Similarly ell(q_t)<=sqrt(M_p J_t^v).
Choosing c sufficiently small, (11) and the exact pole (15) yield

    0<=[P_(h+t v)[e]-P_h[e]]/t
       <=C_v+C_v sqrt(J_t^v)-4J_t^v,
    sup_(0<t<=1) J_t^v<infinity.                    (20)

Monotone convergence proves the additional fixed-seed budget

    J_v=integral s v p^2<infinity.                  (21)

No derivative at zero or signed feasible variation was used to obtain it.

## 4. Full derivative and cross closure

Use the positive edge measure consisting of
J_o v_xv_y dxdy, the forward measures
2alpha_n v_xv_(x+d_n)dx, and the pole measure
4s_xs_y v_xv_y dxdy. Denote their sum by mu_v.
The complete integral of I_0 is finite. For Gamma this follows from
(17)-(18) at t=0 and (21). For forward and pole use

    I_0<=2b_x^2/H_x+2b_y^2/H_y

with the common-zero convention, (8)-(9), and (7).
Since I_t<=I_0, (11) and (14) imply
integral S_t dmu_v<=integral I_t dmu_v. Fatou therefore pays the
complete integral of S_0, where at positive endpoints

    I_0=(H_x p_x-H_y p_y)^2/(H_x+H_y),
    S_0=(H_y p_x-H_x p_y)^2/(H_x+H_y).              (22)

The zero-endpoint formulas agree with the limits.

Here is an integrable domination for the actual derivative, rather than
an interchange assumed from finite energy. If H_x>=H_y>0, then

    D_t=H_y/(H_y+t) D_0
       +(H_x-H_y)p_x^2
          [H_x/(H_x+t)-H_y/(H_y+t)],                (23)

and the second term is nonnegative. The reversed ordering is symmetric.
Thus (D_t)_-<=(D_0)_-<=S_0 and (D_t)_+<=I_t<=I_0.
The common-zero formulas satisfy the same bounds directly. DCT in
ALL the positive edge measures gives

    dP:=lim_(t down to0)[P_(h+t v)[e]-P_h[e]]/t
       =integral D_0 dmu_v.                        (24)

Define the absolutely finite positive row

    A=integral q Rv.

The exact reflected difference quotient has the combined form

    [N_(h+t v)[e]-N_h[e]]/(2t)
       =integral [q Rv-v p^2 Rh]/(1+t v/h).         (25)

On common zeros the integrand is zero. The first row is dominated by
q Rv. The second increases monotonically as t decreases. Minimum in
(11) therefore gives

    B=integral v p^2 Rh<=A<infinity,
    dN=2(A-B)>=0.                                  (26)

The full identity (6) now implies dP=dN. This passage uses only positive
mixtures, not an unbounded weak test or a negative signed direction.

Define P_cross,v and N_cross,v by replacing E_h in the positive and
reflected edge measures by

    C_v(x,y)=(h_x v_y+v_x h_y)(p_x-p_y)^2.           (27)

The positive cross energy is finite because

    I_0+S_0=(H_x+H_y)(p_x-p_y)^2/2
       +(H_x-H_y)^2(p_x+p_y)^2/[2(H_x+H_y)].         (28)

Thus C_v/(v_xv_y)<=2(I_0+S_0). Reflection cross is bounded by
4(A+B). The cross pole is exactly

    8[ell(h)ell(v p^2)+ell(v)ell(q)
                      -2ell(e)ell(vp)],            (29)

which is finite by (7), (21), and Cauchy. At a common zero (27) may
be nonzero: it is the derivative cross contribution, not the original
zero-endpoint E_h. That contribution has been retained in (13)-(28).

Put t_v=vp. It has the weighted integrability needed by the OLD actual
first slot:

    integral exp(x/2)|t_v|
       <=sqrt(J_v M_v)<infinity,
    integral |t_v|<=sqrt(J_v integral v/s)<infinity. (30)

The bounded Holder odd extension of e gives an absolute full Gamma
mixed jump against t_v: it is bounded by a constant times

    ||t_v||_1 integral_R kappa(|z|)
                   min(C|z|^alpha,2||e||_infinity)dz,

which is finite. Complete prime rows are absolute because
F_+|e|+F_-|e|+R|e|<=C exp(x/2); the pole is paid by (30).
Consequently ordinary absolute pairing of the actual equation gives

    q0(e,t_v)=-delta N_psi(e,t_v).                  (31)

This does not claim t_v is in the original quadratic P domain.

For clarity, the ground-v mixed identity is also absolute here.
The positive mixed edge is one half of the sum of (27) and D_0 v_xv_y,
and the reflected mixed edge is paid by A+B. The smooth neutral v can
be paired with q: its Gamma mixed jump is absolute by bounded Holder
v and q in L1; all prime and pole partners are paid by (7) and (9).
Thus the ordinary ground algebra, first on common finite cuts and then
by these absolute bounds, gives q0(e,t_v)=P_v(e,t_v)-N_v(e,t_v).
The elementary edge polarization

    2(H_x p_x-H_y p_y)(p_x-p_y)
       =(H_x+H_y)(p_x-p_y)^2
          +(H_x-H_y)(p_x^2-p_y^2)                  (32)

then yields

    2P_v(e,t_v)=P_cross,v+dP,
    2N_v(e,t_v)=N_cross,v+dN,
    2q0(e,t_v)=P_cross,v-N_cross,v.                 (33)

The last equality uses the complete dP=dN passage, not a substitution
of N_v for the original N_psi in (31).

## 5. The original-reference comparison

In addition to A and B, put

    C=integral e R(vp),
    D=integral q V_psi v.                          (34)

C is absolutely defined either by (30) and R|e|<=C exp(x/2), or by
Cauchy in the reflected measure alpha_n h_x v_y dx, y=d_n-x:

    |C|<=sqrt(A B).                                (35)

D is nonnegative and separately finite. Writing a=e/psi,

    D=integral L a v p,
    D^2<=J_v integral L^2 a^2 v/s
          <=C||a||_infinity^2 J_v M_v<infinity.     (36)

Reflection symmetry and the ORIGINAL metric give exactly

    N_cross,v=2(A+B)-4C,
    N_psi(e,t_v)=2(D-C).                           (37)

Combining (31), (33), and (37), retaining every row, gives

    P_cross,v=2(A+B)-4(1-delta)C-4delta D>=0.        (38)

Its left side is nonnegative because it is the complete positive cross
energy (27), not because a signed cross form has been assigned PSD.
By (26) and (35),

    4delta D
       <=2(A+B)+4(1-delta)sqrt(A B)
       <=4(2-delta)A.

We have proved (1). The coefficient uses 0<delta<1. No sign is imposed
on C, and no prime-diagonal, prime-off-diagonal or pole term is removed.

## 6. Uniform moving windows from positive shifted-Phi seeds

The explicit neutral seeds are

    v_z(x)=2[Phi(x-z)-Phi(x+z)]/sinh(z/2), z>0.     (39)

The theta Phi is even, positive and strictly decreasing on x>0.
The complete translation identity and normalization, proved in
[the compactness report, Section 6](../20261016_positive_neutral_local_compactness/REPORT.md),
give v_z>0, full weak neutrality and ell(v_z)=1. Each fixed v_z is
smooth odd, has a positive linear wall, and is bounded below by a
positive constant times psi. Its shifted theta tails and the actual
Holder ratio show that all conditions in Section 2 hold for each fixed
z, including the Holder bound for e/v_z. These constants need not be
uniform in z.

Only two estimates used after (1) must be uniform for large z. First,
complete Chebyshev bin bounds give

    Rv_z(x)<=C exp(x/2), z>=1, x>0.                (40)

Indeed positivity allows the negative shifted-Phi summand in (39) to
be discarded. For the remaining sum, each unit bin of d_n has alpha
mass at most C exp(d/2). Therefore

    sum_(d_n>x) alpha_n Phi(d_n-x-z)
       <=C exp((x+z)/2)
             sum_(j in Z) exp(j/2) sup_[j,j+1] Phi.

The last sum is finite by the two theta tails, and division by
sinh(z/2) proves (40). This estimate includes every proper power.

Second, for all sufficiently large z,

    L(x)v_z(x)>=c_0>0 on |x-z|<=1.                 (41)

On that window Phi(x-z) has a fixed positive minimum, whereas
Phi(x+z) tends uniformly to zero. Hence v_z(x)>=c exp(-z/2).
The complete smooth-seed PNT asymptotic
L(x)~U(psi)exp(x/2) then proves (41).
Using (1), (40), and (41),

    c_0 integral_(z-1)^(z+1) q/psi
       <=integral q V_psi v_z
       <=(2/delta-1) integral q Rv_z
       <=C(2/delta-1)U(q).                         (42)

Choose a sufficiently large fixed z_0>1 so that (41) holds. Then (42)
is uniform for z>=z_0. No claim is made for windows reaching the
physical wall, or for the ordinary wall integral of q/psi.

## 7. Exact scope

The result is an actual selected-pair comparison: it uses the SAME old
source equation, an attained one-sided minimum, and the full positive
and reflected forms. The fixed-v reciprocal and derivative passages are
proved above; neither signed feasibility nor a formal differentiation
of an unbounded reciprocal is assumed.

Since q/psi=(e/psi)(e/h), (42) cannot be divided by e/psi near its
zeros. It does not control e/h there, give a pointwise lower bound for
h, estimate W_psi g, or sign a reverse IMS remainder. No geometric-mean
quadratic-domain assertion is needed anywhere in this proof. The
original RH comparison remains open.
