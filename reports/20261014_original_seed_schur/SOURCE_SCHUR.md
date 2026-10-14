# Original-source head elimination and the joint neutral quotient

The independently verified [unpenalized head theorem](../20261014_unrepaired_original_head/REPORT.md)
gives the COMPLETE original source form on H=(0,b), b=log2, the bound

    q0[v_H]>=gamma_H ||v_H||_2^2, gamma_H=10^(-10).       (1)

The head theorem retains Gamma, both compressed prime reflections, and the
full pole. Its closed domain D0 is the logarithmic odd Gamma SOURCE domain.
Write A0 for this strictly positive source operator. The following argument
uses that domain, NOT an unproved inverse into the separate original P/N
completion. In particular no assertion integral V|A0^(-1)F|^2<infinity is
made for a general L2 forcing F.

## 1. A complete original-source Schur form

Let t be a positive-wing tail supported in [b,infinity), with finite Gamma
source form and sufficient theta decay. This class includes the tail of an
actual fixed-depth source and every finite polynomial theta jet. The
complete mixed density B0 t on H is

    (B0 t)(x)=-2 integral_b^infinity
                   [kappa(y-x)-kappa(y+x)]t(y)dy
              -2 sum_n alpha_n t(x+log n)
              +2 sum_n alpha_n t(log n-x)1_(log n-x>b)
              -8 sinh(x/2) integral_b^infinity sinh(y/2)t(y)dy. (2)

Here alpha_n=Lambda(n)/sqrt(n), and each arithmetic row is COMPLETE. This
is an ordinary L2(H) function. The near-boundary Gamma kernel is controlled
by the Carleman operator, while its far part is exponentially bounded.
The arithmetic rows are bounded from L2(exp(2y)dy) by the complete sum
sum Lambda(n)n^(-3/2)<infinity, and the pole has its full weighted dual
norm. These are precisely the bounds in the
[complete mixed source estimate](../20261014_unrepaired_original_head/MIXED_FORCING.md).
They require no sign of t or of an individual mixed pairing.

Define the original-harmonic extension and reduced form by

    E0 t=t-A0^(-1)B0 t,
    S0(t,u)=q0(t,u)-<B0 t,A0^(-1)B0 u>.                (3)

The head correction is understood as a zero-supported SOURCE in D0.
Its global Gamma form is finite and its complete mixed source pairings
are legal by (2). Thus q0(E0 t,E0 u)=S0(t,u), and

    q0(E0 t,v_H)=0, v_H in D0.                        (4)

The ordinary q0 source expression is sufficient for (3)-(4); there is no
separate evaluation of N[E0 t] or P[E0 t]. All original arithmetic and pole
terms remain in q0. Formula (3) does not assert that S0 is nonnegative.

## 2. The exact signed value for an actual top source

Let g=psi r be an actual pole-centered source at positive depth delta,
0<delta<1, so Q_delta=q0+delta N is globally nonnegative on its original
P completion and Q_delta(g,z)=0. Set t=g_T. The head functional N(g,.) has
the explicit density

    n_g(x)=2[V(x)g(x)-F_r g(x)],
    F_r g(x)=sum_(log n>x)alpha_n g(log n-x), x in H.   (5)

The actual origin transmission L(0)r(0)=F_r g(0), and the established
weighted-load regularity, make n_g continuous at zero with n_g(0)=0.
On the rest of the compact head all complete translated loads are locally
H^s, s<1. In particular n_g belongs to L2(H). This conclusion uses the
actual source; it is not a boundedness assertion for N on all of D0.

Actual stationarity on smooth compact head tests therefore extends by the
SOURCE-form density to

    A0 g_H+B0 t=-delta n_g.                            (6)

Indeed all three terms define continuous functionals on D0, including the
L2 density on the right. Set

    v=A0^(-1)n_g,
    D_g=<n_g,A0^(-1)n_g>=q0[v]>=0.                     (7)

Then the original-harmonic extension is exactly

    E0 t=g+delta v.                                   (8)

The notation N(g,v)=<n_g,v> may be used as a paired extension of the actual
load (5), but it does NOT assert that N[v] is finite. Using (6), or directly
completing the source head square, gives

    S0[g_T]=q0[g]-delta^2 D_g
           =-delta N[g/psi]-delta^2 D_g.              (9)

Thus an actual nonzero source would give a strictly negative reduced
original-source direction, with the complete additional head subtraction
retained. The positive head gap has not changed (9) to a positive value.
Equation (9), not the zero Q_delta Schur relation, is the exact signed
target for a comparison with the safe hidden energy.

## 3. Neutral tails extend without a delta-dependent head repair

Let s_1,...,s_m be any finite independent family of centered polynomial
theta neutral jets. The original identity q0(s_i,z)=0 holds on the smooth
source core. For z supported in H its left side is continuous in the
D0 source norm: s_i,H has finite Gamma form and its full mixed density is
L2 by (2). Hence that identity extends to every z_H in D0, and uniqueness
in (4) gives

    E0(s_i,T)=s_i.                                    (10)

In particular, for every tail t in the above class,

    S0(s_i,T,t)=0.                                    (11)

For the actual tail, this follows also from its original neutral identity;
for arbitrary tails in the stated source class it follows by the same
source-form extension of q0(s_i,.). No original-P inclusion of E0 t is
needed to justify that extension. This differs from eliminating the
positive-depth Q_delta head: the latter requires the explicit correction
s_i-delta A_delta^(-1)N(s_i,head) and has a nonzero reduced neutral Gram.
Those two operations must not be mixed.

## 4. Project hidden energy and the ORIGINAL remainder together

Write E_hidden for the proved safe-xi form G_tail-D_div. It depends only
on source values at x>=b, through the honest future Mobius seed. Compact
source changes in H do not change this field. For the given finite jets let

    G_ij=E_hidden(s_i,s_j), k_i=E_hidden(g,s_i),
    c=G^(-1)k, s_c=sum_i c_i s_i, t_perp=g_T-s_c,T.

The finite Gram G is positive definite by hidden coercivity and the
nonconstant polynomial latent ratios. All these energies are finite for
actual sources and finite jets. Its orthogonal projection gives exactly

    E_hidden[t_perp]=E_hidden[g]-k^T G^(-1)k,
    E0 t_perp=g+delta v-s_c,
    S0[t_perp]=S0[g_T]=-delta N[g/psi]-delta^2 D_g.     (12)

Define only the GROUPED reduced remainder R0=S0-E_hidden. Then

    R0[t_perp]=R0[g_T]+k^T G^(-1)k.                   (13)

The gain on the right of (13) is exactly the hidden energy removed by the
same projection; it is not an independent positive budget. The universal
neutral counterexample is fully retained: for a nonzero jet tail,
S0=0 while E_hidden>0, so R0 is negative.

The projected harmonic source in (12) is not an actual top source. It lies
in the explicitly stated source space; its individual N/P membership,
prime-origin transmission, and actual amplitude bounds are not imported.
One may use (12)-(13) for a joint source-form comparison, but not as an
excuse to discard the inhomogeneous forcing or original pole. Neither a
sign for R0 nor a global original-form sign is proved here.
