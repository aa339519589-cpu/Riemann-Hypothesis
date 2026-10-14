# A coherent current field with the same pointwise hidden variance

This note constructs a new coupling of the actual complete original-psi
currents. Its initial conditional field is exactly the full-band eta current
field w(x,n), not the different conditional field of a one-reference online
extension. Consequently its covariance diagonal is precisely the V in the
signed transport identity F = E_current + integral b V. The full signed
source correction and the initial spatial cooling term are retained. No
original coefficient-one sign theorem is asserted.

## 1. Inputs and one spatial initial-label process

Use [the current-adapted field](../20261014_first_label_current_approximation/CURRENT_FIELD.md),
[the full-band hidden lift](../20261014_first_label_current_approximation/HIDDEN_LIFT.md),
and [global label control](../20261014_first_label_coercive_correction/GLOBAL_LABEL_CONTROL.md).
The actual bounded plateau-zero ratio u belongs to H^s, 1/2<s<1. Write

    T w=u, V=T(w-u)^2, |w(x,n)|<=C(1+log n),
    E I_x=u(x), Var I_x=J(x), sup J<infinity.

The complete current includes the operational holding current at zero.
All probabilities p_n(x)=n^(-1/2)eta(x+log n)/Phi(x) are positive. The proved
[star-coupling theorem](../20261014_eta_mobius_transport/ETA_TRANSPORT.md)
gives p_n'<0 for every n>=2 and p_1'>0. Set

    mu_n(dt)=-p_n'(t)dt, n>=2;
    epsilon=sum_(n>=2)mu_n([0,infinity))=1-p_1(0)<1.             (1)

Choose an initial random pair (N,T) with measure mu_n(dt), and an additional
atom of mass p_1(0) at N=1. On the atom put N_x=1 for every x; otherwise put

    N_x=N if x<T, and N_x=1 if x>=T.                            (2)

Thus N_x has law p(x), and for x<=y its pair probabilities are exactly

    P(N_x=N_y=n)=p_n(y), n>=2;
    P(N_x=N_y=1)=p_1(x);
    P(N_x=n,N_y=1)=p_n(x)-p_n(y), n>=2.                         (3)

This is ONE measurable initial-label field, not separately chosen edge
couplings. The spatial index x in (2) is not the later operational time.

## 2. Attach the genuine hidden dynamics, without changing a marginal

Independently of (N,T), take common Poisson drivers for the full operational
eta-score process. A concrete realization uses three collections:

* Gamma marks (h,a), with intensity dt dh da, accepted at state (x,n) when
  a is below its true operational Gamma rate density;
* for every genuine prime power d, divisor marks a of intensity dt da,
  accepted only if d divides n and a is below the true operational divisor
  rate, sending (x,n) to (x+log d,n/d);
* for every m>=1, reset marks a of intensity dt da, accepted below
  r_m(x)=p_m(x)d_m(x), sending (x,n) to (x,m).

Self resets are allowed. At the wall use the proved operational rates,
not a singular physical time change. In particular the Gamma density and
nontrivial divisor rates can be written without dividing by s(x):

    lambda_n(x,h)=exp(-x/2)Phi(x) s(x+h) kappa(h)
                          eta(x+log n+h)/eta(x+log n),
    l_d(x,n)=1_(d|n) exp(-x/2)Phi(x) s(x+log d)Lambda(d).        (4)

Here s=psi/Phi. Formula (4) includes x=0 by continuity. Each ray starting
from (x,N_x) uses the SAME drivers. This is a new joint coupling. A finite
family of starts suffices for every finite-dimensional statement below.

For completeness this construction has a jointly measurable version in x.
First localize the observed coordinate and labels, restrict h>=a>0, and
truncate the reset labels. There are finitely many jumps on compact time
intervals; the accepted-mark recursion is a Borel function of initial state
and drivers. For fixed labels the integral of h times the Gamma density and
its local x derivative is finite, including at zero after (4). The usual
same-mark comparison therefore removes the small-jump cutoff by an L1
Gronwall bound. The sums of reset rates and their local derivatives have
Gaussian label tails. The previously proved hidden nonexplosion removes
spatial and label localization. A fast subsequence gives a measurable
limit for almost every initial x with respect to any prescribed finite
absolutely continuous measure; pathwise uniqueness identifies its marginal
for each fixed x. Separately adjoin x=0 on the same drivers. This is enough
for all source-coordinate integrals and the wall statements here; no claim
of simultaneous exceptional-set removal for every uncountable start is
needed.

Every marginal observed ray is the original operational psi process,
because its initial label has law p(x). Define its complete current I_x
on this new coupling. The scalar L2 and uniform J estimates depend only on
that marginal and therefore remain true. Future Poisson drivers are
independent of the entire initial label field, so

    E[I_x | sigma(N_y:y>=0)]=w(x,N_x)=:W(x),
    E W(x)=u(x), Var W(x)=V(x).                                 (5)

The equality in (5) is exact even though the new simultaneous observed flow
does NOT generally have posterior p at each ray after conditioning on all
other observed histories. No such filtering claim is used.

Likewise, conditional on the full hidden-driver history at operational time
t, the future mean in each coordinate is w at that coordinate's current
hidden state. Thus the full conditional current is a closed martingale.
Its joint reset increments are whatever the COMMON reset marks actually
produce. One may not replace their simultaneous square by a product of
one-ray posterior averages or import the one-reference coefficient-one
Hilbert refresh formula. Old observed-flow coalescence and polynomial
neutral-current results also do not automatically transfer to this new law.
Only the actual bounded current is used here.

## 3. Exact covariance as positive cutoff features minus one rank one

Put

    Delta_n(x)=w(x,n)-w(x,1), n>=2;
    e(x)=w(x,1)-u(x)=-sum_(n>=2)p_n(x)Delta_n(x);
    f_(n,t)(x)=Delta_n(x)1_(x<t).                               (6)

Then W=w_1+f_(N,T), with f=0 on the initial label-one atom. In particular

    integral f_(n,t)(x) mu_n(dt)=-e(x).

For x<=y, expansion of (3), or direct use of (2), gives

    Cov(W(x),W(y))
      =sum_(n>=2)p_n(y)Delta_n(x)Delta_n(y)-e(x)e(y).            (7)

Equivalently, on the whole square,

    C_W+e tensor e
       =sum_(n>=2) integral f_(n,t) tensor f_(n,t) mu_n(dt).     (8)

The measure in (8) is positive and has total mass epsilon. Equation (8)
identifies V(x) as the covariance diagonal, so it is the SAME V that enters
the integrated hidden-current energy, not a surrogate pair variance.
The negative rank one is the true mean correction e tensor e. It is not
the original polar functional and must not be identified with it.

## 4. Domain and the exact continuous forward correction

Let K_Gamma(x,y)=psi(x)psi(y)kappa(y-x) on x<y. The complete hidden Gamma
energy is

    E_Gamma=int_(x<y) K_Gamma sum_n p_n(y)
                                      |w_n(y)-w_n(x)|^2 dxdy. (9)

This follows directly from the genuine hidden conductances. It is finite
as a component of E_current. The first-label source psi w_1 is legal in the
original P completion by
[the first-label theorem](../20261014_first_label_current_approximation/DOMAIN.md).

For every fixed finite n and t, psi f_(n,t) is also in that completion.
On compact intervals p_n(y) has a positive lower bound, so (9) pays the
local logarithmic Gamma norm of w_n. Cutting at t adds a finite crossing
integral: boundedness on a compact interval pays
integral_(x<t<y) kappa(y-x)dxdy. The other original rows are finite by the
compact support, bounded ratio near zero, and the complete prime/physical/
pole bounds. The source trace vanishes because psi(0)=0. Cutoff and logarithmic-form smoothing give the
actual P-core approximation. This is not an assertion that every psi w_n
is a globally legal source.

These features are integrable in the full two-energy form as well. Their
Gamma sum is exactly

    sum_n int F_Gamma[f_(n,t)] mu_n(dt)
       =int_(x<y) K_Gamma {
          sum_(n>=2)p_n(y)|Delta_n(y)-Delta_n(x)|^2
          +sum_(n>=2)[p_n(x)-p_n(y)]|Delta_n(x)|^2}.             (10)

The first line is bounded by 2E_Gamma+2F_Gamma[w_1]. For the second, global
label control and the complete Gaussian derivative bound

    |p_n'(x)|<=C n^6(1+z)exp[-z(n^2-1)], z=pi exp(2x),

remove the Gamma diagonal. For h=y-x<=1 use the integrated derivative
bound; for h>1 use p_n(x). All source-coordinate integrals converge with
the theta weights. The remaining forward-prime and boundary forms follow
from their finite rows and E|W(x)|^2<=u(x)^2+J(x). In particular expectation
and all full signed form pairings below are legitimate. No finite-prime
truncation or divergent backward theta row is separated.

For an explicit comparison let d=w_1(y)-w_1(x),

    r_n=p_n(x)-p_n(y),
    C_cool(x,y)=sum_(n>=2)r_n|Delta_n(x)|^2,
    B_cool(x,y)=-sum_(n>=2)r_n Delta_n(x).

Then the exact initial-star squared difference is

    E|W(y)-W(x)|^2
       =sum_n p_n(y)|w_n(y)-w_n(x)|^2
                          +C_cool+2 Re(conj(d)B_cool).         (11)

The positive cooling square and its mixed term are both mandatory. The
actual hidden divisor energy has transitions (x,dm) -> (x+log d,m), whereas
(3) retains a label or absorbs it at one. These are DIFFERENT pair kernels;
(11) does not identify the star forward-prime energy with hidden divisor
energy. Nor does this construction assume divisibility-coherent Gamma
couplings of the stronger, previously obstructed kind.

## 5. The original boundary Hilbert norm and full signed accounting

Let B_delta=H_b+(1-delta)N_b-P_b, 0<=delta<=1/3, be the independently
proved positive boundary graph. Its three rows are dominated by the finite
measure rho=psi(Hpsi+L+sinh(x/2))dx. The uniform marginal current bound
therefore makes I and W Bochner L2 fields in its quotient Hilbert space,
modulo spatial constants. Conditional expectation (5) is legitimate there.
Write

    V_B=E B_delta[W-u],  J_B=E B_delta[I-u].

Then exactly

    V_B=sum_(n>=2)int B_delta[f_(n,t)]mu_n(dt)-B_delta[e],
    J_B=V_B+E B_delta[I-W],                                    (12)
    E B_delta[W]=B_delta[u]+V_B.

The total feature mass in (1) gives the genuine Hilbert inequality

    B_delta[e]<=epsilon sum_n int B_delta[f_(n,t)]mu_n(dt),
    V_B>=(1-epsilon)sum_n int B_delta[f_(n,t)]mu_n(dt).          (13)

It is a covariance bound in an already positive boundary component, not
positivity of the original source form. In particular it gives a LOWER
bound on covariance and is not the missing upper forward comparison.

For clarity retain the exact original identity

    Q_delta[psi u]=2F[u]-B_delta[u],
    F[u]=E_current+int b(x)V(x)dx,
    b=psi[sinh(x/2)/2+2K-2x psi-Hpsi-L].                       (14)

Here E_current is the INTEGRATED current-adapted hidden Gamma/divisor/reset
energy, not the safe-xi common-seed expression G_tail-D_div. Substituting
(12) into (14) gives

    Q_delta[psi u]
       =2E_current-E B_delta[W]+V_B+2int b V.                   (15)

All quantities in (15) now belong to a common field with the same pointwise
V. To make the covariance correction completely explicit, use the ordered
boundary integrals from their original conventions and set

    X_B(C)=2 int int kappa(x+y)psi(x)psi(y) C(x,y)dxdy
       +2(1-delta)sum_d alpha_d int_0^(log d)
                      psi(x)psi(log d-x)C(x,log d-x)dx
       -8 int int sinh(x/2)psi(x)sinh(y/2)psi(y)C(x,y)dxdy.

Then

    V_B=2int psi[Hpsi+(1-delta)L-sinh(x/2)/2]V-X_B(C_W),
    V_B+2int bV
       =2int psi[2K-2x psi-delta L]V-X_B(C_W).                 (16)

The original negative pole coefficient is included in X_B. Its rank-one
kernel is distinct from e tensor e in (8). Neither the signed storage in
(16), the mixed cooling term in (11), nor the true divisor/star discrepancy
has been dropped. Equations (8), (11), and (15)-(16) provide a common-field
slot for a future signed comparison, not that comparison itself.
