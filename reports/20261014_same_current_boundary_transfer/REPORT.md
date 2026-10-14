# A closed same-current transfer in the full signed-transport boundary weight

This package keeps the original eta posterior and the conditional mean of
one SAME actual complete current. It proves a nonlocal all-prime operator
comparison, not just a pointwise small-posterior estimate. The result reaches
the weight mu=psi exp(x/2), which is the tail scale of the negative variance
transport. It does not establish the final coefficient-one signed source
comparison or exclude a supercritical state.

## Main statements

1. [Exact triangular current transport](TRIANGULAR_CURRENT_CONTRAST.md).
   The continuous deficit has mass M_n=L_n-a_n+a_1, so its completion with
   the mandatory stay atom is a probability P_n. Subtracting actual hidden
   current equations gives

       (G_n+beta+L_n)(w_n-w_1)
          =sum_(d|n)lambda_d w_(n/d)(x+log d)-L_n P_n w_1.

   Its true killed terminal is paid. Every divisor remains, and
   |w_n-w_1|<=Omega(n)osc_future(w_1).

2. [Exact SAME-variance Schur completion](SAME_VARIANCE_TAIL_SCHUR.md).
   With e=w_1-u, epsilon=(1-p_1)/p_1 and the true conditional-tail mean,

       V=|e|^2/epsilon+R_high,
       (G_1+a_tail)e=D u+F_tail,
       |F_tail|^2<=S_a R_high.

   Thus only the genuinely higher-label variance forces the dominant mode.
   The [critical positive inverse](CRITICAL_DOMINANT_INVERSE.md) retains
   the full Gamma, half-line boundary, forcing and reset terms; the aligned
   feedback spends at most 1/40000 of int psi^2 beta R_high. This does not
   by itself pay R_high or the larger signed transport density.

3. [Closed normalized strong-weight transfer](NORMALIZED_BOUNDARY_TRANSFER.md).
   In X=direct_sum_(n>=2)L2(mu p_n), the genuine normalized potentials obey

       ||(G_n+beta+L_n)^(-1)L_n||<=4/3.

   The normalized complete child map has norm<1/2, since its exact shifted
   measure is bounded by d^(-3), not Lambda(d)/d. Their feedback therefore
   contracts with norm<2/3. The full true-divisor and continuous-probability
   source inputs are paid in L2(mu), giving

       ||(w_n-w_1)_(n>=2)||_X <=(23/10)||w_1-c||_(L2(mu)),
       ||w_1-u||_(L2(mu)) <=(23/200)||w_1-c||_(L2(mu)),
       ||w_1-c||_(L2(mu)) <=(200/177)||u-c||_(L2(mu)).

   These statements concern the same actual field and any constant c.
   They do not assert a bounded transformation on the whole original-P
   source completion. The complete boundary graph factorization gives
   B_delta[u]>=(1/100)int mu|u-c_C|^2, so this is also a finite transfer to
   an already signed original boundary norm.

4. [All-integer homogeneous child transport](INTEGER_CHILD_EULER_BOUND.md).
   The normalized inverse and exact divisor geometry yield a multiplicative
   majorant with total Euler product below7/5. The first-reset-killed
   homogeneous tail therefore has squared norm below2/5 of its first-label
   input. This is only that positive component: the actual common
   (G_1+beta)w_1 forcing and reference correction remain separate.

## Inputs and reproducibility

The proofs use the published
[first-label current construction and original-domain package](../20261014_first_label_current_approximation/REPORT.md),
[complete correction/coercive inverse package](../20261014_first_label_coercive_correction/REPORT.md),
and [full boundary graph factorization](../20261014_boundary_graph_coercivity/POSITIVE_FACTORIZATION.md).
Those inputs retain every prime power, the honest origin holding current,
and the full original pole form. No RH, prime truncation, canonical-seed
replacement or arbitrary-label source-domain assumption is added here.

`check_integer_child_euler_bound.py` verifies the complete arithmetic Euler
majorant. `check_transfer_coefficients.py` verifies the finite rational arithmetic used
in the comparisons. It is not a numerical sign test for the original source
form, and does not replace the analytic complete-tail arguments.

## Remaining signed comparison

The original identities are still

    Q_delta[psi u]=2F[u]-B_delta[u],
    F[u]=E_current+int b(x)V(x)dx,
    b=psi[sinh(x/2)/2+2K-2x psi-Hpsi-L].

The transfer above bounds the correct larger weighted field but its stated
constants do not close the final signed coefficient. The two pieces of V,
the source-input mixed terms, all normalized Gamma/Jensen squares, and every
neutral projection/source-forcing term must be retained jointly. No extra
positive energy may be counted a second time. This package proves the
closed operator transfer, not positivity of Q_delta on all sources or RH.
