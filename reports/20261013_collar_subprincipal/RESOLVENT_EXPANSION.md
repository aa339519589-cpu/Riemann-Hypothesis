# A controlled constant-order expansion of the actual new-collar inverse

This is a mathematical supplement to [SUBPRINCIPAL_FORM.md](SUBPRINCIPAL_FORM.md).
Its independent mathematical review is in [REFEREE_RESOLVENT.md](REFEREE_RESOLVENT.md). It concerns the new/new compression
of the explicit odd source form, with its exact polar coefficient two.
It does not estimate the inverse of the full old block.

Let B_cell be the positive self-adjoint operator associated to

    b_cell[g] = (1/4) integral_(0,1)^2 |g(u)-g(v)|^2/|u-v| du dv
                 -(1/2) integral_0^1 log(u(1-u))|g(u)|^2 du.

Since the regional term is nonnegative and u(1-u)<=1/4,
B_cell >= log(2) I. Set

    C = B_cell -(gamma+log(pi)) I,
    c_star = log(2)-gamma-log(pi),   L=log(k).

The subprincipal reconstruction asserts on the entire natural form
domain, equivalently as a bounded perturbation of associated operators,

    D_k = U_k^* D_new U_k = L I+C+R_k,
    R_k=R_k^*, ||R_k||=r_k=O(k^(-1/2)).                 (1)

In particular Dom(D_k)=Dom(C), and D_k is coercive when
L+c_star-r_k>0. No norm expansion of the unbounded C is asserted.

## An exact scalar resolvent identity and its remainder

Suppose L+c_star>0. For every g in Dom(C), the spectral theorem and

    1/(L+c) = 1/L-c/L^2+c^2/[L^2(L+c)]

give the exact quadratic identity

    <g,(L+C)^(-1)g>
       = ||g||^2/L-<g,Cg>/L^2
          +<Cg,(L+C)^(-1)Cg>/L^2.                     (2)

The final term is nonnegative and bounded above by

    ||Cg||^2/[L^2(L+c_star)].                          (3)

This needs only Dom(C), not Dom(C^2). From (4) onward assume also
L+c_star-r_k>0, so the perturbed inverse exists and is coercive. A
bounded perturbation resolvent identity then gives

    |<g,[D_k^(-1)-(L+C)^(-1)]g>|
        <= r_k ||g||^2/[(L+c_star-r_k)(L+c_star)].     (4)

Thus the constant-order inverse debit is already determined for each
fixed operator-domain profile:

    L^2 <g,D_k^(-1)g>
      = L||g||^2-<g,Cg>
         +O(||Cg||^2/L)+O(r_k||g||^2).               (5)

Constants in the O notation are universal once L>=2|c_star|+2 and
r_k<=1. The assertion remains uniform for families with bounded norms
of g and Cg. It is not a uniform inverse expansion on all L2 profiles.

## A full source row with a bounded leading-term remainder

Take b_k=-L g_k+e_k in unitary collar coordinates, with
g_k in Dom(C). Completion of the square gives exactly

    <b_k,D_k^(-1)b_k>
      =L^2<g_k,D_k^(-1)g_k>
         -2L Re<g_k,D_k^(-1)e_k>+<e_k,D_k^(-1)e_k>.

For the unperturbed inverse,

    ||L(L+C)^(-1)g_k-g_k||
       <= ||Cg_k||/(L+c_star).

The perturbation estimate in (4), now in operator norm, implies

    ||L D_k^(-1)g_k-g_k||
       <= ||Cg_k||/(L+c_star)
          +L r_k ||g_k||/[(L+c_star-r_k)(L+c_star)].

Consequently

    <b_k,D_k^(-1)b_k>
      =L||g_k||^2-<g_k,Cg_k>-2Re<g_k,e_k>+E_k,       (6)

where, writing z=L+c_star and z_r=z-r_k,

    |E_k| <= ||Cg_k||^2/z
          +L^2 r_k||g_k||^2/(z z_r)
          +2||e_k||[||Cg_k||/z+L r_k||g_k||/(z z_r)]
          +||e_k||^2/z_r.                            (7)

All factors, signs and terms in (7) follow from (2)-(4) and the preceding
norm estimate; no error depends on an unknown negative-band inverse.
If g_k, Cg_k, e_k stay bounded, E_k=O(1/log k)+O(k^(-1/2)).
Therefore an O(1) source-row error contributes at constant order through
-2 Re<g_k,e_k>; it cannot simply be discarded when testing a saturated
leading-order Schur difference.

## Operator-domain profiles and the limitation

Every complex C1([0,1]) profile g lies in Dom(B_cell). To verify this
without a formal singular-kernel differentiation, define

    (Jg)(u)=(1/2) integral_0^1 [g(u)-g(v)]/|u-v| dv,
    V(u)=-(1/2)log(u(1-u)).

The integral is absolutely bounded by ||g'||_infinity/2, and Vg is in L2
because log endpoint singularities are square-integrable. For every
h in the cell form domain the polarized regional form equals <h,Jg>:
the Lipschitz bound makes the expanded integrals absolutely integrable,
and symmetry produces the factor1/2. The potential term is <h,Vg> by
Cauchy-Schwarz. The form representation theorem therefore gives
B_cell g=Jg+Vg in L2, with

    ||Cg|| <= (1/2)||g'||_infinity
              +||V||_2||g||_infinity
              +|gamma+log pi| ||g||_2.

This includes the normalized exact polar profile and smooth rescaled
theta profiles in the new collar whenever their C1 norms stay bounded.
It does not identify those profiles as eigenvectors.

Equations (5)-(7) supply a usable constant-order expansion for the
new-collar inverse. The full old-space Schur form also requires its own
true Green correction, including changes of every finite pivot, mixed
row and new target. None of those corrections is supplied here, so no
full-window positivity or RH claim follows.
