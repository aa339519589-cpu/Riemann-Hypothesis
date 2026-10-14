# A coherent full Gamma-prime ray-current field

This note constructs shared-noise currents for the complete original-psi
forward process, not a Gamma-only divisibility coupling. Its covariance is
retained in the exact original signed form. No favorable sign of that
covariance combination is asserted.

## 1. Operational clock and an honest entrance state

Put z=pi exp(2x), x>=0, and

    c(z)=8z^3-30z^2+15z,
    theta_c(z)=sum_(n>=1)c(n^2z)exp(-n^2z),
    psi(x)=exp(x/2)theta_c(z).

The full theta function theta_c is positive for z>pi and vanishes simply
at z=pi. Individual c(n^2z) are not assigned positive probabilities.
For a ratio u(x), write v(z)=u((1/2)log(z/pi)). The physical forward
original-psi generator is

    Gv(z)=int_0^infinity theta_c(z+w)/[2w theta_c(z)]
                                      [v(z)-v(z+w)]dw
       +sum_(n>=2)Lambda(n)theta_c(n^2z)/theta_c(z)
                                      [v(z)-v(n^2z)].

Define the operational generator H=theta_c G. It extends to z=pi:

    Hv(z)=int_(y>z) theta_c(y)/[2(y-z)][v(z)-v(y)]dy
       +sum_(n>=2)Lambda(n)theta_c(n^2z)[v(z)-v(n^2z)]. (1)

At the boundary the continuous total rate is finite, because theta_c(y)
has a simple zero at pi. The prime rate is also finite. For z>pi the
continuous activity is infinite, but its first and second jump moments
are finite, uniformly on the whole state space. Theta polynomial bounds
also make the complete prime first and second moments uniformly finite.
Thus the increasing H process is nonexplosive.

If Y_s is this process, the physical clock is

    t(s)=int_0^s theta_c(Y_a)da.                       (2)

For a start z>pi, t(s) tends to infinity and the inverse clock gives the
original G process. One way to verify this is to use the already proved
nonexplosive physical process; alternatively, if the clock in (2) were
finite, the physical-scale first and second moment bounds would make
Y_s converge to a finite limit, contradicting its uniformly positive
exit channel on every compact band. In the interior,

    int Gv dt=int Hv ds,    int Gamma_G[v]dt=int Gamma_H[v]ds. (3)

At z=pi there is an exponential operational holding time. It collapses to
zero physical time because theta_c(pi)=0, but its CURRENT must be retained.
It is not legitimate to replace its nonzero operational current by zero.

## 2. Uniform current variance, including the origin

Use the actual plateau-subtracted ratio u=r-c_infinity in H^s, 1/2<s<1.
The proved interior ray-current theorem gives a finite L2 current I_x,
with E I_x=u(x), variance J(x), and

    J(x)<=C_s(1+1/x)||u||_(H^s)^2, x>0.

The operational clock improves this to

    sup_(x>=0) J(x)<=C_s'||u||_(H^s)^2.               (4)

Here the boundary current at zero is defined by the H process, including
its first holding interval. To prove (4), fix a finite band pi<=z<=b.
A local Holder exponent 0<alpha<s-1/2 gives a uniform bound on Gamma_H[v]
in this band: its small-jump integral is bounded by a constant times
`int_0^1 [theta_c(z)+Cw]w^(2alpha-1)dw`; its large-jump and prime parts
are bounded by theta tails. There is a state-independent positive jump
channel to the fixed destination interval [b+1,b+2]. Its rate is bounded
below uniformly on the band, so its mean exit time is bounded uniformly.
The pre-exit occupation energy is therefore bounded. After exit, the
already proved interior bound is uniform because x is bounded away from
zero. The strong Markov property proves (4).

At z=pi the exact total H rate is

    K=3Phi(0)+Theta(0)/2
     =int_0^infinity kappa(y)psi(y)dy
                       +sum_n alpha_n psi(log n).

Its destination law mu0, in x coordinates, is

    mu0(dy)=[kappa(y)psi(y)dy
                  +sum_n alpha_n psi(log n)delta_(log n)(dy)]/K.

Let C_g=K[u(0)-int u dmu0]. If tau has the Exp(K) law and Y has law mu0,
then the exact boundary current decomposition is

    I_0=C_g tau+I_Y,                                  (5)

where tau is independent of Y and of its future current. In particular

    K J(0)=int [ (u(y)-u(0))^2+J(y)] K mu0(dy),
    J(0)>=C_g^2/K^2.                                 (6)

The identity follows from the variance formula in (5):
`Var(C_g tau)=C_g^2/K^2`, while the other variance is
`E_mu0 J+Var_mu0 u`. Their sum is exactly (6). Thus even the C_g=0
harmonic boundary condition does not remove the entrance jump variance.

## 3. A single full Poisson field for all starts

For the continuous part take one Poisson random measure in operational time,
destination y>pi and mark a>0, with intensity

    ds theta_c(y)dy da/2.

A ray at state z jumps to y when y>z and a<1/(y-z). For each integer label
n>=2, use a common independent Poisson mark field with intensity
`Lambda(n) ds da`; a state z jumps to n^2z when a<theta_c(n^2z).
All prime powers are included. Equality of two rays is absorbing under
this common noise.

For clarity, this is a finite-variation jump construction, even though the
continuous activity is infinite in the interior. Truncate jumps smaller
than epsilon, construct the ordinary marked jump paths, and remove the
cutoff. The mean total discarded displacement on a bounded operational
interval is O(epsilon). The L1 difference of the continuous jump maps at
states z,w has the modulus

    C |z-w| [1+log_+(1/|z-w|)].

Indeed, destinations between z and w contribute O(|z-w|), and destinations
above both states contribute at most
`|z-w| int_(max(z,w))^infinity theta_c(y)/(y-min(z,w))dy`.
The complete prime maps add a locally Lipschitz modulus with Gaussian-
summable integer constants. The Osgood integral for the displayed modulus
diverges at zero. Applying the elementary integral inequality to two
truncations shows convergence in L1 uniformly on each bounded time interval;
the same inequality proves pathwise uniqueness. Choose a sufficiently fast deterministic cutoff subsequence using the locally
uniform Bihari bounds, and define its measurable limit wherever it exists.
The resulting field is jointly measurable; for each fixed starting point the
limit exists almost surely, and pathwise uniqueness identifies it with that
starting-point solution. Thus these are shared-noise rays, not merely
unrelated pairwise distributions. Simultaneous exceptional-set removal for
all uncountably many starts is not required for the integral identities.

For the continuous arrows alone the coupling is order preserving and
coalescing. If z<w and a destination y>w is accepted by the lower state,
then `1/(y-z)<1/(y-w)` makes the upper state accept the SAME destination.
A destination between the two states cannot cross their order. Prime events
can break their order, but once equal the rays stay equal. No assertion of
simultaneous-divisibility conditioning is made or needed.

The continuous operational drift is

    b_cont(z)=(1/2)int_z^infinity theta_c(y)dy,

which is strictly decreasing. This is a useful exact ordering property,
not a claim that the full prime jump kernel is stochastically monotone.
No pair-coalescence time estimate is used in the identities below.

## 4. Exact coherent current covariance

On the common noise define

    M_s^z=v(Y_s^z)-v(z)+int_0^s Hv(Y_a^z)da.

The current theorem and (3)-(4) give its L2 terminal value and

    I_z=v(z)+M_infinity^z,
    C(z,w)=Cov(I_z,I_w)=E[M_infinity^z M_infinity^w].

Thus C is a positive-semidefinite kernel, C(z,z)=J(z), and
`|C(z,w)|<=sqrt(J(z)J(w))`. Its entries need not be nonnegative.
The exact common-noise bracket is

    C(z,w)=E int_0^infinity [gamma_cont(Y_s^z,Y_s^w)
                              +gamma_prime(Y_s^z,Y_s^w)]ds,            (7)

where

    gamma_cont(z,w)
      =int_(y>max(z,w)) theta_c(y)/[2(y-min(z,w))]
                     [v(y)-v(z)][v(y)-v(w)]dy,

    gamma_prime(z,w)
      =sum_(n>=2)Lambda(n)min(theta_c(n^2z),theta_c(n^2w))
                     [v(n^2z)-v(z)][v(n^2w)-v(w)].     (8)

These are precisely the simultaneous accepted jumps. The complete signed
cross integrand is absolutely integrable in expected time: its absolute
value is bounded by one half the sum of the two marginal carre rates.
Equation (4) therefore justifies (7), not merely a formal martingale
covariance calculation. At the origin the holding contribution in (5)
is part of this same compensated-jump martingale.

## 5. Full signed current identity with covariance retained

Return to x coordinates for C and J. Use the finite current edge forms in
the complete forward-current representation, but replace the independent
pair-current kernel by the coherent kernel

    E_coh(x,y)=E|I_x-I_y|^2
                 =[u(x)-u(y)]^2+J(x)+J(y)-2C(x,y).

Denote the resulting nonnegative edge forms by P_coh,H_coh,N_coh, with
weights respectively `4s(x)psi(x)s(y)psi(y)`,
`kappa(x+y)psi(x)psi(y)`, and
`alpha_n psi(x)psi(log n-x)` on the prime-reflected lines.
All three are finite by (4) and the integrability of these edge measures.
In particular no singular kappa(|x-y|) current energy or pathwise original-P
membership is assumed.

Write

    C_P=int int s(x)psi(x)s(y)psi(y) C(x,y)dxdy,
    C_H=int int kappa(x+y)psi(x)psi(y) C(x,y)dxdy,
    C_N=sum_n alpha_n int_0^(log n) psi(x)psi(log n-x)
                                               C(x,log n-x)dx.

Then the complete original signed form is exactly

    h[g]=P_coh-H_coh-N_coh
          +4int psi[3Phi+Theta/2-xpsi]J
          +8C_P-2C_H-2C_N.                           (9)

Likewise its actual supercritical form is

    Q_delta[g]=P_coh-H_coh-(1-delta)N_coh
       +2int psi[2(3Phi+Theta/2)-2xpsi-delta L]J
       +8C_P-2C_H-2(1-delta)C_N.                     (10)

For the actual state the last quantity equals zero, by its exact original
stationarity. These formulas follow by expanding E_coh in each edge form
and using the independently proved complete product-current identity.
Every sign-changing storage term and every cross covariance is retained.

The PSD property of C implies C_P>=0 and C_H>=0: the former is a variance,
and the latter is the sum of variances associated with the Laplace-square
expansion of kappa(x+y). It gives no sign to the prime-reflected C_N.
Nor does it determine the sign of their combination in (9)-(10).
A coefficient-one conclusion still needs a new signed comparison for this
SPECIFIC coherent field; replacing it by an arbitrary PSD kernel or dropping
the storage term would change the problem.

Dependencies: the published [forward-ray occupation/current theorem](../20261014_positive_reflected_storage/FORWARD_RAYS.md),
[complete product-current form](../20261014_positive_reflected_storage/CURRENT_FORM.md),
and [actual Sobolev ratio and plateau gauge](../20261014_actual_ratio_multipliers/REPORT.md).
The original pole and reflected-prime normalization is displayed in this
package's [physical pair-kernel report](PHYSICAL_PAIR_KERNEL_AND_ADJOINT.md). The common-noise construction here uses the
full generator and is not the impossible Gamma-only divisibility-coherent
coupling considered separately.
