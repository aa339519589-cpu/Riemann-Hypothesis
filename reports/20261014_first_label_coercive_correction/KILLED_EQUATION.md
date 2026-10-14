# Actual first-label regeneration and a killed positive potential

This is a continuation of the complete first-label energy theorem, not a
claim of accretivity in the original psi-squared metric. The killed kernel
is an actual first-refresh segment of the SAME full-band hidden process.
Its forcing keeps the complete prime-minus-continuous mismatch and the
centered true-refresh bias. No source eigen-equation is transported to an
arbitrary hidden label.

## 1. Exact same-source first-refresh equation

Use the actual plateau-zero ratio u, the full eta current field w, and
H_n=w_n-u, e=w_1-u from
[the current construction](../20261014_first_label_current_approximation/CURRENT_FIELD.md).
Let p=p(x), beta=K/psi, rho_n=p_n a_n/beta, and define

    S1=psi p_1=eta s, s=psi/Phi.

Starting at hidden label ONE, no divisor event is available before the
first refresh candidate. The spatial generator on this segment is exactly

    G1 f(x)=int_0^infinity kappa(h)S1(x+h)/S1(x)
                                           [f(x)-f(x+h)]dh.

The candidate refresh rate is beta(x), including self candidates, and the
newborn label law at its time is rho(x). This is not a separately guessed
Doob transform. It is a stopping segment of the already constructed full
hidden Markov process.

The source u has positive Holder regularity, so its complete continuous
and prime future drifts are well defined on each positive wing. Define

    D u=(G_psi-G1)u=G_prime,psi u-G_extra u,
    G_extra f=int kappa(h)psi(x+h)/psi(x)
                    [p_1(x+h)/p_1(x)-1][f(x)-f(x+h)]dh,
    R(x)=T[aH](x), f(x)=D u(x)+R(x).                  (1)

Both G_prime,psi and G_extra have nonnegative rates, but their DIFFERENCE
in (1) is retained. The exact hidden current drift at label one gives

    (G1+beta)e=f.                                    (2)

Equation (2) is initially an extended, stopped-martingale equation. It
need not be interpreted as a classical absolutely convergent drift for
w_1. The reset term is absolutely integrable against its true newborn
law by the proved logarithmic label bound and Gaussian refresh tails.

## 2. A direct stopped proof, without a formal adjoint substitution

Let Y have generator G1, and let tau be the first refresh candidate, with
survival exp[-int_0^t beta(Y_v)dv]. Stop also at a finite time and spatial
localizations. The closed hidden-current martingale and the ordinary
Dynkin formula for u give exactly

    e(x)=E_x[int_0^tau D u(Y_v)dv
                  +sum_n rho_n(Y_tau)H_n(Y_tau)]              (3)

at common finite cutoffs, with the surviving terminal e term retained
before the cutoff is removed. Replacing the terminal refresh expectation
by its hazard integral gives the positive killed-potential formulation

    e(x)=R1 f(x),
    R1 F(x)=E_x int_0^infinity
                 exp[-int_0^t beta(Y_v)dv]F(Y_t)dt.    (4)

Here are the actual domain facts that justify the limit. The ratio of the
G1 rate to the continuous G_psi rate is p_1(x+h)/p_1(x), bounded between1
and401/400. Therefore the existing physical-z first-moment bounds construct
a nonexplosive pure-continuous process for every x>0, and the same fixed
positive jump stream forces Y_t to infinity. Its physical-z first and
second jump moments tend to1/2, since p_1 tends to1 with Gaussian error.
The stopped-moment and dyadic-martingale argument of
[the original ray theorem](../20261014_positive_reflected_storage/FORWARD_RAYS.md) therefore gives
Z_t/t->1/2. Since beta=3/(2Z)+O(Z^(-2)), the integrated hazard diverges.
Thus tau is finite almost surely.

The actual label-one error is bounded and tends to zero; more strongly,
[the global label bound](GLOBAL_LABEL_CONTROL.md) and the
complete posterior tail give

    |e(x)|^2<=epsilon(x)V(x)
                 <=C_sigma||u||Hs^2 exp[-6pi exp(2x)].         (5)

One may remove the surviving terminal in (3) using this SAME-source bound,
not by postulating a generic original-metric resolvent norm.

There is also direct domination of the entire forcing in (4). The complete
prime and extra-continuous rows are bounded by constants times beta, and
|D u|<=C beta||u||infinity. The actual logarithmic label bound and the
uniform Gaussian newborn tails give |R|/beta=|E_rho H|<=C||u||Hs.
Consequently |f|<=C beta||u||Hs and

    R1|f|<=C||u||Hs R1 beta=C||u||Hs.                (6)

This proves absolute integrability of the GROUPED correction forcing in
(4), without separately integrating the unfiltered source equation or an
undamped Mobius prefix. The first-refresh current itself is treated via
its already closed martingale, not an assumed absolute infinite drift.

## 3. The honest operational origin and its competing hazards

Put theta1=exp(-x/2)S1. The continuous operational generator theta1 G1 has
at zero the finite exit measure kappa(y)S1(y)dy. The killed rate tends to

    theta1 beta -> p_1(0)K(0).

Thus its total origin holding rate is

    C1+p_1(0)K(0), C1=int_0^infinity kappa(y)S1(y)dy.

The actual first-label reset is a genuine competing hazard. It is not
removed by pretending that the source wall is absorbing. The continuous
exit measure, killing rate and normalized forcing f/beta have finite
limits from the already constructed hidden entrance and current field.
Hence (4) extends to zero using that operational entrance, not by dividing
by psi(0).

When the independently proved tail ordering a_n>a_1 for n>=2 is used,
a_1<=beta and the identity D0 S1=-a_1S1 gives C1<=p_1(0)K(0).
The first event at the operational origin is then a refresh with probability
at least1/2. This does not delete the spatial-exit branch or make its
terminal value neutral in the original source form.

## 4. A positive pointwise potential budget with the full signed forcing

The killing-location kernel K1=R1 beta is Markov. Jensen therefore yields

    |e(x)|^2<=R1[|D u+T(aH)|^2/beta](x).             (7)

The centered reset estimate is proved in
[the centered-reset note](RESET_FORCING.md).
Together with the complete Gamma and prime row estimates it gives

    |T(aH)|^2/beta <=(1/50)T(a|H|^2),
    |D u|^2/beta <=(3/80)[Gamma_prime[u]+Gamma_extra[u]],
    Gamma_extra[u]<=Gamma_cont[u]/400.              (8)

Here is a direct check of the second and third estimates. The prime row
is <(7/400)beta by the complete Mangoldt grouping in the centered-reset
proof. For the extra continuous row,

    p_1(y)/p_1(x)-1
       =[epsilon(x)-epsilon(y)]/[1+epsilon(y)]
       <=epsilon(x)-epsilon(y).

The proof of the Gamma posterior-debit bound in
[the Gamma error note](../20261014_first_label_current_approximation/GAMMA_ERROR.md)
therefore gives its entire row <=beta/50, with exactly the same physical-z
integral and no new cutoff. The sum of the two positive row masses is at
most(7/400+1/50)beta=(3/80)beta. Cauchy--Schwarz for that sum proves the
second estimate in (8), while retaining their opposite signs in D.
Finally p_1(y)/p_1(x)-1<=epsilon(x)<1/400 proves the third estimate. Combining their square roots, not
assigning a sign to either forcing, gives the valid coefficient budget

    |e|^2 <=(23/400) R1[Gamma_prime[u]
                            +Gamma_cont[u]/400+T(a|H|^2)].     (9)

All quantities refer to the SAME actual source and current. The earlier
complete forward-energy estimate13/400 and (9) are alternate controls;
the same reset channel cannot be spent twice as independent resources.

Crucially R1 is not asserted bounded in the ORIGINAL L2(psi^2) metric.
Its half-line adjoint has a signed incoming row; killing by beta does not
automatically dominate it. Integrating (9) against an original source
weight changes that weight to its exact killed adjoint potential. That
potential, all reflected edges, and the full pole form must remain in any
closing signed estimate. No favorable full source sign is claimed here.
