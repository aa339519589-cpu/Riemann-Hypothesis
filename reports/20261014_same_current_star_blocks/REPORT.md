# Same-current star covariance and complete nested-tail spatial blocks

This package gives a coherent original-space covariance decomposition of
the actual current-adapted arithmetic lift. It compares its dominant and
higher-label parts with the COMPLETE forward, Gamma-wall, reflected-prime
and pole forms. The continuous Gamma cooling cancels against genuine
divisor outgoing rows at coefficient one. The remaining arithmetic
cross-incidence is explicit and is not assigned an unproved sign.

**The full original coefficient-one comparison, K<=1, and RH remain
unproved.** Statements using Q_delta>=0 are conditional consequences of
the actual positive-depth setup, not independent proofs of that positivity.
No current/seed identification or iteration of an actual-only estimate is
made.

## 1. Conventions and previously proved inputs

Let psi=-Phi'>0 on x>0, eta=exp(x/2)(4z^2-6z)exp(-z), z=pi exp(2x),
and

    p_n(x)=n^(-1/2)eta(x+log n)/Phi(x), T h=sum_n p_n h_n,
    kappa(t)=exp(-t/2)/(1-exp(-2t)), alpha_n=Lambda(n)/sqrt(n).

The same actual plateau-zero ratio u has a complete current I_x, with
E I_x=u(x), bounded variance J(x), and its true full-band conditional field
w(x,n), T w=u. Every Gamma, true-divisor and refresh channel is retained.
The operational holding current at the origin is included.

These input theorems are available in the published
[current field and full hidden lift](../20261014_first_label_current_approximation/REPORT.md),
[global label control](../20261014_first_label_coercive_correction/GLOBAL_LABEL_CONTROL.md),
and [coherent original current construction](../20261014_coherent_prime_ray_bridges/COHERENT_OPERATIONAL_RAY_CURRENTS.md).
The genuine positive refresh scores a_n satisfy beta=T a=K/psi,
K=3Phi+Theta/2. Do not confuse these scores with an arithmetic mask.

The original forward form has ONE future orientation:

    F[f]=int_(x<y)psi(x)psi(y)kappa(y-x)|f(x)-f(y)|^2dxdy
       +sum_n alpha_n int psi(x)psi(x+log n)
                                 |f(x)-f(x+log n)|^2dx.

The full source form is Q_delta[psi f]=2F[f]-B_delta[f], where
B_delta=H+(1-delta)N-P_pole keeps both reflected orientations and the
original negative polar term. Its precise normalization and unconditional
boundary positivity are in the
[complete boundary graph](../20261014_boundary_graph_coercivity/REPORT.md).
For the stronger boundary metric used below see
[NORMALIZED_BOUNDARY_TRANSFER](../20261014_same_current_boundary_transfer/NORMALIZED_BOUNDARY_TRANSFER.md).
We use 0<delta<=1/3, fixed throughout.

## 2. One common field, not unrelated marginal couplings

[CURRENT_STAR_FIELD.md](CURRENT_STAR_FIELD.md) constructs one initial-label
field with, for x<=y, mass p_n(y) on (n,n), mass p_n(x)-p_n(y) on (n,1),
and mass p_1(x) on (1,1). Genuine future hidden drivers are independent of
that initial field. Consequently W(x)=w(x,N_x) is the conditional mean
of the SAME complete current. The variance is exactly V=T(w-u)^2.

Put

    e=w_1-u, q=1-p_1, epsilon=q/p_1,
    D_1=e, D_n=-e/epsilon for n>=2,
    Z_1=0, Z_n=w_n-q^(-1)sum_(m>=2)p_m w_m for n>=2.

Then W=u+D+Z and V=e^2/epsilon+R_high, R_high=T Z^2. The full joint
matrix, proved in [JOINT_STAR_MATRIX.md](JOINT_STAR_MATRIX.md), is for x<=y

    E[D_x D_y]=e(x)e(y)/epsilon(x),
    E[D_x Z_y]=0,
    E[Z_x D_y]=-e(y)/q(y) sum_(n>=2)p_n(y)Z_n(x),
    E[Z_x Z_y]=sum_(n>=2)p_n(y)Z_n(x)Z_n(y).

Thus the dominant Brownian/nested-cutoff kernel is exactly a component
of this same field. The nonzero triangular cross kernel is retained.
Every random-field source and integrated form used in the package has
its stated original-P or boundary-Hilbert domain; unweighted individual
higher-label legality is not assumed.

## 3. A strict full-boundary matrix, with the original pole intact

[BOUNDARY_SCHUR.md](BOUNDARY_SCHUR.md) proves on EVERY original edge

    |E[(D_x-D_y)(Z_x-Z_y)]|
      <=(1/384) sqrt(E|D_x-D_y|^2 E|Z_x-Z_y|^2).

It follows, with the same field, that

    |F_DZ|<=(1/384)sqrt(F_D F_Z),
    |B_DZ|<=(101/384)sqrt(B_D B_Z),
    (283/384)(B_D+B_Z)<=E B_delta[D+Z]
                         <=(485/384)(B_D+B_Z).

The first line uses the forward domains proved in JOINT_STAR_MATRIX.
The boundary estimate is a signed all-edge comparison, including every
reflected prime power and the negative pole. It extends to finite mixed
Gram matrices by polarization. It is NOT a uniform Schur angle for Q_delta
near its null directions.

The fractions-only checker is
[check_star_boundary_schur.py](check_star_boundary_schur.py). It proves
the complete analytic series bounds, not a finite-label numerical sample.
Run it with Python 3; no external package is needed.

## 4. Dominant spatial square and the paid head contribution

[CONTRAST_TRANSPORT.md](CONTRAST_TRANSPORT.md) and
[DOMINANT_COMPLETION.md](DOMINANT_COMPLETION.md) retain the actual signed
current/source transport, all reset terms and the weighted-domain passage.
[TWO_GROUP_SPATIAL.md](TWO_GROUP_SPATIAL.md) identifies the resulting
positive expression as ONE genuine hidden spatial square. With
Y_1=0, Y_n=e/q for n>=2 and omega=1/epsilon,

    E_sp[Y]=F[e]+F_D+G_D,
    F_D=F_(psi^2 omega)[e]+int C_omega e^2,
    G_D=int psi^2 omega(abar-a_1)e^2,
    abar=q^(-1)sum_(n>=2)p_n a_n.

Here C_omega is the full nonnegative incoming Gamma/prime commutator.
It has not been produced by a separate unsigned row bound.
[DOMINANT_COVARIANCE.md](DOMINANT_COVARIANCE.md) supplies the matching
complete original boundary and any fixed common-neutral leakage.

[HEAD_VARIANCE.md](HEAD_VARIANCE.md) inserts the
[unconditional original head gap](../20261014_unrepaired_original_head/REPORT.md)
without claiming e is an actual null source. For b=log2 it gives the
additional paid term

    10^(-10)int_0^b psi^2 e^2 omega(1-omega/omega(b)).

It is obtained by exactly completing the finite feature mean, before
using the head sign. The remaining mean, tail and delta-N terms stay
explicit. This strengthens the SAME spatial block; it is not an extra
copy of its energy.

## 5. Complete higher-label and nested-tail arithmetic incidence

The mixed and higher-label formulas in JOINT_STAR_MATRIX cancel the
continuous Gamma cooling against the complete divisor outgoing mass.
Their remaining terms have genuine label increments Z_(dm)(x)-Z_m(x),
with the shifted coordinate and all prime powers kept. The resulting
higher-label Schur equation remains signed.

[NESTED_INCIDENCE.md](NESTED_INCIDENCE.md) extends the spatial diagonal
to EVERY integer cut. For q_k=sum_(n>k)p_n and
V_k=sum_(n>k)p_n(a_n-beta),

    E_sp[A 1_(n>k)]=F_star[A 1_(n>k)]+int psi^2 V_k A^2,
    V_k>3log2 q_k.

For k<l the exact off-diagonal difference has the additional term

    -sum_d int alpha_d psi(x)psi(y)A_k(y)A_l(x)
                            sum_(k<m<=l<dm)p_m(y)dx,
    y=x+log d.

Thus the strict scalar diagonals are not silently summed into a positive
full matrix. For W_1=0 the complete incidence is

    E_sp[W]-F_star[W]
       =int psi^2 sum_(n>=2)p_n(a_n-beta)W_n^2-2T_W,
    T_W=sum_d int alpha_d psi(x)psi(y)
                sum_(m>=2)p_m(y)W_m(y)[W_(dm)(x)-W_m(x)]dx.

The exact matrix, not only its positive diagonal, is the retained target
for a coefficient-one all-prime comparison. Current covariance, canonical
Mobius seed energy and independently constructed semigroup metrics are
not interchanged in any of these identities.
