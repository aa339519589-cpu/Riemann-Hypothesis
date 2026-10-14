# Actual arithmetic propagation: no eventually constant positive-depth ratio

Let g=psi r be a nonzero actual pole-centered top source at depth delta>0,
with its unchanged full scalar equation

    T g=-delta Wg,
    Wg=L r-F_r g,
    T=B_o-C0-F_+-F_b+F_r,
    Tpsi=sinh(x/2)/2, Wpsi=0.                        (1)

All notation and domains are those of the [actual source equation](../20261013_supercritical_source_tails/REPORT.md), [origin transmission](../20261014_actual_origin_transmission/REPORT.md) and [ratio plateau](../20261014_actual_ratio_multipliers/REPORT.md) reports.
Then r cannot be constant on any entire terminal ray [R,infinity).
The proof uses the exact Gamma kernel, the complete prime row and the
reflected coefficient 1-delta. It does not assume RH or a zero-free region.

## 1. The actual tail equation for a compact ratio deviation

Suppose r(x)=c for x>=R. Set e=g-c psi. It is a real integrable source
supported in [0,R], with the established actual Holder/odd-origin trace.
Choose A>R. Because Wpsi=0, equation (1) gives

    T e+delta We=-c sinh(x/2)/2.

For x>A, e=0, F_+e=0 and L(e/psi)=0. Hence exactly

    F_b e-(1-delta)F_r e
       =Gamma_o e+c sinh(x/2)/2,                    (2)

where the off-support odd Gamma row is

    Gamma_o e(x)=-integral_0^R
                   [kappa(x-y)-kappa(x+y)]e(y)dy.    (3)

The local constants in B_o-C0 vanish off the support. Formula (3) retains
both Gamma wings and their minus sign; no separate divergent exit rate is
used. The kernels are smooth at positive separation x-R.

Extend e by zero outside [0,R] for the arithmetic convolution. Define on
the entire real x-line

    P(x)=sum_d alpha_d{e(x-log d)-(1-delta)e(log d-x)}.

This agrees with the left side of (2) for x>A and vanishes for
x<log2-R. Define the entire compact-source transforms

    E_-(s)=integral_0^R exp[-(s-1/2)y]e(y)dy,
    E_+(s)=integral_0^R exp[ (s-1/2)y]e(y)dy,
    H_delta(s)=E_-(s)-(1-delta)E_+(s).                (4)

For Re s>1, absolute convergence and the exact Mangoldt Dirichlet series
justify termwise integration:

    integral_(-infinity)^infinity exp[-(s-1/2)x]P(x)dx
                    =-(zeta'/zeta)(s)H_delta(s).    (5)

This is a full prime-power identity, not a model zero sum. Its left compact
piece x<=A has an entire transform because its support is bounded.

## 2. Gamma residues and the trivial zeta zeros

The kernel expansion

    kappa(t)=sum_(j>=0)exp[-(2j+1/2)t], t>0,

gives for x>A

    Gamma_o e(x)=-sum_(j>=0)D_j exp[-(2j+1/2)x],
    D_j=E_-(-2j)-E_+(-2j).                           (6)

Since A>R, its transformed tail is the locally normally convergent
meromorphic series

    -sum_(j>=0)D_j exp[-(s+2j)A]/(s+2j).             (7)

Indeed |D_j|<=C exp[(2j+1/2)R], so every compact subset avoiding the
poles has a geometric tail exp[-2j(A-R)]. The remaining pole term in (2)
has transformed tail

    (c/4){exp[-(s-1)A]/(s-1)-exp[-sA]/s}.             (8)

It has poles only at s=0 and 1 and does not affect s=-2j for j>=1.
Equations (2),(5),(7),(8) therefore give a meromorphic identity on C.
At every trivial zero s=-2j, j>=1, zeta has a simple zero, so the residue
of -(zeta'/zeta)H_delta is -H_delta(-2j). The residue of (7) is -D_j.
Consequently

    E_-(-2j)-(1-delta)E_+(-2j)
       =E_-(-2j)-E_+(-2j),
    delta E_+(-2j)=0.                               (9)

The exact reflected coefficient is decisive. Since delta>0, (9) gives

    integral_0^R exp[-(2j+1/2)y]e(y)dy=0,
                                      every j>=1.   (10)

No nontrivial-zero location, multiplicity estimate or zero-density theorem
enters this argument. The simple trivial zeros follow directly from the
classical zeta functional equation and its Gamma factor.

## 3. Compact moment uniqueness

Put u=exp(-2y), so u lies in [exp(-2R),1]. Equation (10) says that the finite
signed measure

    dnu(u)=e(-(1/2)log u)u^(-3/4)du/2

annihilates u^j for every j>=1. Since the left endpoint is strictly positive,
the linear span of u,u^2,... is dense in the continuous functions on this
interval: approximate F(u)/u by ordinary polynomials and multiply by u.
Thus nu=0 and e=0 almost everywhere. The actual continuous representative
then vanishes pointwise. Therefore g=c psi.

Finally the original source is pole-centered while ell(psi)=1/8, so c=0.
Equivalently this is the zero vector in the original P/N quotient and cannot
be a normalized positive-depth top source. This contradiction proves the
stated rigidity.

## 4. Strict positivity of the new hidden component on an actual source

Assume the independently established hidden coercivity

    E_hidden(g):=G_tail-D_div>=kappa min_a integral_b^infinity
                          W xi |(Mg)/xi-a|^2,
    kappa>0, b=log2.

If E_hidden(g)=0, its safe latent quotient is constant on [b,infinity), using its
actual continuous representative. The honest future inverse C M g=g then
implies g=c psi on this same terminal ray: all translated arguments in C
remain there. The preceding theorem excludes this for a nonzero actual
positive-depth source. Hence

    E_hidden(g)>0 for every nonzero actual positive-depth top source.  (11)

This is an actual-source-specific propagation statement beyond the finite
wall and neutral moment constraints. It does NOT supply a quantitative
lower bound for the original remainder, and it does not prove h>=0 or RH.
The neutral first-jet counterexample to universal remainder positivity is
unaffected: such a neutral source is not a positive-depth solution of (1).

The compact-residue argument in Sections 1-3 also applies to a compact L2
source e satisfying the same weak off-support equation (2), with fixed
constants c and delta>0. Compact L2 is L1; the separated Gamma row is smooth;
the compact transforms are entire; and (10) gives e=0 almost everywhere.
The actual continuous representative is only needed for the pointwise
phrasing of the ratio theorem, not for the head-kernel application.
