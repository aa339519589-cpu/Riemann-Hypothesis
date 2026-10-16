# Reciprocal integrability at a selected neutral-ground minimum

Date: 2026-10-16.

At a lawful one-sided minimizing ground for the same bounded Holder theta
source, the complete finite-mixture inequality controls the reciprocal
square `integral s psi (f/h)^2`. Consequently `f^2/h` belongs to L2 with
every fixed exponential weight, and its complete `Rpsi` pairing is
finite. The proof uses the exact negative pole variation to absorb the
Gamma and full forward-prime costs. No derivative at zero, pointwise
reflected lower bound, or signed feasible variation is assumed. This
strengthens the selected-minimum conclusions of the [joint report](REPORT.md);
it is not an original-metric upper bound or an RH proof.

## 1. Hypotheses and exact objects

Use the complete objects and normalization of the
[joint report](REPORT.md), Sections 1-2. In particular
`s(x)=sinh(x/2)`, `ell(f)=integral s f`, and psi is its positive odd
theta source, with `ell(psi)=1/8`.
Let h be a nonnegative full weak-neutral ground with ell(h)=1. Let
f=psi a, where a is real, bounded and globally Holder of some exponent
alpha>0. Assume f=0 a.e. on {h=0}, finite reflected diagonal, and the
already proved full ground identity at h and h+t psi. Write

    H=h/psi, q=f^2/h, q_t=f^2/(h+t psi),
    A_t=H+t/2,
    J_t=integral s psi a^2/[H(H+t)].                     (1)

At H=a=0, every quotient in (1) is zero. Require only the lawful
one-sided minimality

    P_(h+t psi)[f] >= P_h[f], 0<t<=1.                  (2)

This follows for the fixed-source or jointly gauged attained minimum,
since positive normalization of h+t psi does not change either energy.
It is not assumed for an arbitrary actual pair in the original metric.
The complete positive form is

    P_h[f]=double integral J_o E_h[f]
       +2 sum_n alpha_n integral E_h[f](x,x+log n)dx
       +8[ell(h)ell(f^2/h)-ell(f)^2],                  (3)

with every prime power, J_o=kappa(|x-y|)-kappa(x+y)>0,
kappa(d)=exp(-d/2)/(1-exp(-2d)), and ell(psi)=1/8.
Finite P_h implies ell(q)<infinity, so J_t<=ell(q)/t is finite for
fixed t>0. The full ground identity and add-psi cost estimates make
P_(h+t psi)[f] finite. No derivative at t=0 is taken below.

## 2. Exact edge and pole variations

For an edge with ground ratios H_x,H_y and source ratios a_x,a_y,
put

    D_t(x,y)=(H_x-H_y)
       [a_x^2/(H_x(H_x+t))-a_y^2/(H_y(H_y+t))].        (4)

Then (E_(h+t psi)-E_h)/t=psi_x psi_y D_t. The common-zero
convention extends this identity: if H_x=a_x=0, its value is
psi_x psi_y a_y^2/(H_y+t). At positive endpoints, completing a
square gives

    D_t <= (a_x-a_y)^2/(H_x+H_y+t).                  (5)

The subtracted square has numerator

    [sqrt(H_y(H_y+t)/(H_x(H_x+t))) a_x
       -sqrt(H_x(H_x+t)/(H_y(H_y+t))) a_y]^2,

and denominator H_x+H_y+t. Formula (5) also holds at common zeros.
A different elementary bound, used for the finite-rate forward rows,
is

    (D_t)_+ <= a_x^2/(H_x+t), if H_x>=H_y,
    (D_t)_+ <= a_y^2/(H_y+t), if H_y>H_x.             (6)

The complete pole has the exact variation

    [P_pole,h+t psi[f]-P_pole,h[f]]/t
       =ell(q_t)-8 J_t.                              (7)

This follows by expanding
8[(1+t/8)ell(q_t)-ell(f)^2] and using
(q_t-q)/t=-psi a^2/[H(H+t)]. The coefficient 8 is retained.

## 3. Gamma absorption with a variable distance cutoff

Boundedness of psi and J_o<=kappa(|x-y|) imply, uniformly in x>0
and 0<l<=l_0<1,

    integral_(|x-y|>=l) J_o(x,y)psi(y)dy
       <=C[1+log(1/l)],
    integral_(|x-y|<l) J_o(x,y)psi(y)|x-y|^(2alpha)dy
       <=C_alpha l^(2alpha).                         (8)

For the first bound, split `l<|x-y|<1` and `|x-y|>=1` and use
`kappa(d)<=C/d` and `kappa(d)<=C exp(-d/2)`, respectively. For the second,
integrate `C d^(2alpha-1)` on `(0,l)`. These estimates require only
bounded psi and retain the complete odd kernel. For c>0 to be chosen, set

    l_x=l_0 exp[-c s(x)/A_t(x)].                      (9)

By (5), the Gamma variation is at most

    I_t=double integral J_o psi_x psi_y
                    (a_x-a_y)^2/(A_t(x)+A_t(y)).     (10)

Split the pairs into the union-near set
{|x-y|<l_x} union {|x-y|<l_y} and its complement. The union may be
overcounted. Assign each of its two parts to its defining endpoint,
use the denominator >=A_t(x), and use the Holder bound for a. Then

    I_near <=C integral psi_x l_x^(2alpha)/A_t(x) dx
       <=C_c integral psi/s <infinity.               (11)

Indeed exp(-2alpha c s/A)/A<=1/(2alpha e c s). The last integral
is finite because psi/s extends boundedly through 0 and has theta
decay at infinity. This bound is uniform in t.

On the complementary far set BOTH cutoffs hold. Use
(a_x-a_y)^2<=2a_x^2+2a_y^2 and symmetry, followed by (8):

    I_far <=C integral psi a^2/A_t
             +C c integral s psi a^2/A_t^2
          <=C M_0^(1/2) J_t^(1/2)+C c J_t,           (12)

where M_0=integral psi a^2/s<infinity. The last step uses
H(H+t)<=A_t^2 and Cauchy--Schwarz. Thus, for any prescribed eta>0,
choose c small enough and then apply Young to obtain

    [P_Gamma,h+t psi[f]-P_Gamma,h[f]]/t
       <=eta J_t+C_eta.                              (13)

The near constant may increase when c decreases, but it remains finite
and independent of t. All estimates use the full odd Gamma kernel;
there is no derivative of h, no division by a, and no assumption on
zero orders of a or h.

## 4. Every forward prime power and the pole

By (6), the complete forward variation is at most

    2 integral q_t(F_+psi+F_-psi)
       <=C integral exp(x/2)q_t.                     (14)

The last full-prime bound F_+psi+F_-psi<=C exp(x/2) is the fixed smooth
seed Chebyshev estimate. It includes all proper powers. Cauchy--Schwarz
with (1) gives

    integral exp(x/2)q_t <=J_t^(1/2) M_1^(1/2),
    M_1=integral exp(x)psi a^2/s<infinity.            (15)

Similarly ell(q_t)<=J_t^(1/2) M_p^(1/2), with
M_p=integral s psi a^2<infinity. Therefore (7), (13), (14) and (15),
with eta chosen below the retained pole coefficient, yield

    0 <= [P_(h+t psi)[f]-P_h[f]]/t
       <=C+C J_t^(1/2)-4 J_t, 0<t<=1.               (16)

Changing the harmless constants in (16) absorbs every positive row.
It follows that sup_(0<t<=1)J_t<infinity.

## 5. Consequences and exact limits

Monotone convergence in (1) gives

    integral s psi (f/h)^2<infinity.                 (17)

In particular q=f^2/h belongs to L2 with every fixed exponential
weight. For each real beta,

    exp(2beta x)q^2
       <=||a||_infinity^2 sup_x[exp(2beta x)psi(x)/s(x)]
                             s psi (f/h)^2.         (18)

The supremum is finite at the wall and on the theta tail.

For every fixed real beta,

    integral exp(beta x)q(x)dx
       <=[integral s psi (f/h)^2]^(1/2)
          [integral exp(2beta x)psi a^2/s]^(1/2)
       <infinity.                                   (19)

This pays the previously missing ordinary reciprocal-wall part of
integral q Rpsi, and also the positive row integral q Rv for each
fixed smooth theta-neutral seed with |Rv|<=C_v exp(x/2).
A separate finite-t minimality argument may then pass the one-sided
KKT inequality for a positive admissible neutral v.

Nothing here gives two-sided signed ground variations, h>=c psi,
strict positivity everywhere, a representation of the positive neutral
cone, an original-P realization of h, or the original actual B_A upper.
The estimate is an additional budget at a lawful one-sided minimizing
ground, not a transfer of the actual source equation to that ground.

## 6. Published dependencies and scope

The [joint report](REPORT.md), Sections 1-2 and 6, supplies the actual
ratio hypotheses, the finite-gauge full identity, and the lawful
selected minimum. The complete rough ground identity is proved in the
[ground-identity addendum](../20261016_neutral_wall_heat_picone/GROUND_IDENTITY_ADDENDUM.md).
The complete fixed-seed prime bounds are used in those reports and in
the [lower-comparable addendum](../20261016_neutral_ground_descent_pole_floor/LOWER_COMPARABLE_GROUND_ADDENDUM.md).
The present proof adds the finite-mixture estimate (16)-(17); it does
not assume any new property of the rough minimizer from these references.

The conclusion is conditional on the one-sided minimizing property (2),
not a uniform coercivity assertion for every positive neutral ground.
Constants may depend on the selected source and its ground. There is
no claimed uniformity over a moving negative band or over hypothetical
actual states. All common-zero conventions agree with the full ground
identity, and no new pointwise representative is assigned to h.
