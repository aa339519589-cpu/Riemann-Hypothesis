# Global label control for the actual full-band current field

This result concerns the current-adapted field of the FULL eta-score hidden
lift, not the different minimal-xi lift and not the singular canonical
quotient phi/(eta s). It retains every refresh and every true divisor death.
It proves a global logarithmic label bound and Gaussian conditional variance
for the SAME complete original-psi current.

## 1. Inputs and notation

Use the full-band rates in
[FULL_BAND_ETA_SCORE_HIDDEN_LIFT.md](../20261014_first_label_current_approximation/HIDDEN_LIFT.md)
and their honest operational entrance in
[OPERATIONAL_ETA_ENTRANCE_AND_WALL_RESOLVENT.md](../20261014_first_label_current_approximation/ENTRANCE.md).
Write

    p_n=n^(-1/2)eta(x+log n)/Phi(x), s=psi/Phi,
    beta_psi=K/psi, K=3Phi+Theta/2,
    a_n=beta_n-(A_eta s)_n/s>0, E_p a=beta_psi.

A physical-time refresh has total candidate rate beta_psi and newborn law

    rho_n(x)=p_n(x)a_n(x)/beta_psi(x).                 (1)

Self refreshes are retained as candidates with zero change. Divisor d|n
has rate Lambda(d)s(x+log d)/s(x). The operational clock multiplies all
rates by theta=exp(-x/2)psi(x); it leaves complete current integrals unchanged.
At x=0, (1) means rho_n(0)=p_n^0 b_n/B0, as in the entrance theorem.

For the actual plateau-zero u in H^sigma, 1/2<sigma<1, let I_x be its complete
original-psi current, including the real operational holding current at zero.
Let

    w(x,n)=E_(x,n) I_x,  T w=u,
    V_w=T(w^2)-u^2.

The closed-martingale construction in
[../20261014_first_label_current_approximation/CURRENT_FIELD.md](../20261014_first_label_current_approximation/CURRENT_FIELD.md)
gives T w^2<=u^2+J and finite original current bracket. The global bound
sup J<=C_sigma||u||_(H^sigma)^2 is proved in
[COHERENT_OPERATIONAL_RAY_CURRENTS.md](../20261014_coherent_prime_ray_bridges/COHERENT_OPERATIONAL_RAY_CURRENTS.md).

## 2. Uniform control of the TRUE refresh law

There are constants epsilon>0 and R<infinity, independent of x>=0, such that

    rho_1(x)>=epsilon,
    sum_n rho_n(x)log n<=R.                          (2)

Here is a direct justification that includes both endpoints. On every
compact positive x interval, all rates are continuous and positive. At zero,
rho_1 tends to p_1^0 b_1/B0>0. The Gamma integral in b_1 is strictly positive
since s(h)>0 for h>0.

For uniform label tails, use p_n<=2n^4 exp[-z(n^2-1)], z=pi exp(2x).
On a compact x band, cancel the singular s denominator BEFORE estimating:

    |q_n|/beta_psi=Phi |(A_eta s)_n|/K.

The Gamma integral has a uniform polynomial label envelope, since the eta
future ratio is polynomial-Gaussian and the increment of s is O(h) at the
Gamma diagonal. The divisor part is bounded by C(1+n^2 log n), using
s(x+log d)<=C d^2 and sum_(d|n)Lambda(d)=log n. The beta_n term is bounded
as well. Thus a_n/beta_psi has a uniform polynomial label envelope through
x=0, and (1) has uniformly Gaussian tails there.

On x>=a>0, s(x+log d)/s(x)<=C_a d^2 and the analogous continuous ratio bound
give a_n<=C_a(1+n^2 log n). Also beta_psi^(-1)<=C_a(1+z). Hence, for n>=2,

    rho_n(x)<=C_a(1+z)n^4(1+n^2 log n)exp[-z(n^2-1)].

This supplies a uniform summable log moment and shows sum_(n>=2)rho_n(x)
tends to zero as x tends to infinity. Therefore rho_1 tends to one. Compact
continuity, the positive wall limit and this positive infinity limit prove
the first assertion of (2); the Gaussian estimates prove the second.
There is no deletion of refresh re-births in (2).

## 3. A renewal lemma that pays all re-births

Consider any time interval on which every true divisor rate dominates
c Lambda(d), d|n, for a fixed c>0. Stop at the first label 1, or at any
additional spatial exit. Between refreshes, the log-label drift obeys

    A log N>=c(log 2)log N.

Equivalently, one may couple the divisor channels to independent baseline
prime-level shocks, each of rate c log p, which replace a prime exponent v
by min(v,j) for every level j<v. These baseline shocks have exactly the
rates c Lambda(d); extra divisor events only decrease the exponent further.
Thus, from initial label n, the time until baseline absorption has mean
at most

    log n/[c(log 2)^2].                             (3)

The first refresh or spatial exit only shortens this first cycle.
After any refresh, the probability that the newborn label is 1 is at least
epsilon, uniformly in the past. Consequently the expected number of refresh
candidates before stopping is at most 1/epsilon. The expected sum of the
logarithms of their newborn labels is at most R/epsilon, by conditional
expectation and (2). Applying (3) in each cycle therefore yields

    E tau<=C_c[log n+R/epsilon],
    E log N_tau<=log n+R/epsilon,                    (4)

where the second assertion is needed only when stopping at a spatial exit.
The pathwise bound for it is log N_tau<=log n+sum_refresh log N_new.
These arguments do not assume independent refresh times or a stationary
newborn law. A label-dependent spatial motion is allowed throughout.

## 4. Two clocks, one global current bound

Fix a>0. On x>=a, s is increasing, so every divisor rate is at least
Lambda(d). The physical reset rate is bounded, and the preceding renewal
lemma with c=1 gives

    E_(x,n) tau_1<=C_a(1+log n), x>=a.               (5)

The source forcing G_psi u is bounded on this wing by C_(a,sigma)||u||Hs,
using the actual Holder estimate and the grouped future theta kernel.

On the compact band 0<=x<=a use OPERATIONAL time. The divisor multiplier is

    theta(x)s(x+log d)/s(x)
       =exp(-x/2)Phi(x)s(x+log d)
       >=exp(-a/2)Phi(a)s(log 2)=:c_a>0, d>=2.       (6)

Equation (6) includes its finite value at x=0. The operational refresh rate
exp(-x/2)K(x) is bounded on the band. Apply (4) until the first label 1 or
exit into x>=a. Both the expected stopping time and the expected log label
at a band exit are bounded by C_a(1+log n). The operational source forcing
H u=theta G_psi u is bounded on the band by C_sigma||u||Hs, including its
proved origin value. Its Gamma diagonal is paid by the actual positive
Holder exponent; all prime rows are normally theta summable.

Finally the first-label field is already globally bounded. Indeed the eta
posterior has p_1>=c>0 on the whole half-line, and

    |w(x,1)|^2<=T w^2/p_1<=(u(x)^2+J(x))/p_1
                                  <=C_sigma||u||Hs^2.           (7)

Stop the CLOSED current martingale at the times above. Its pre-stop integral
is paid by the bounded forcing and (4)-(6). A terminal label 1 is paid by
(7); a band exit is paid first by the interior estimate and the second bound
in (4). Optional stopping is legitimate for this closed L2 martingale,
with the displayed L1 dominations for its finite-variation part. This proves

    |w(x,n)|<=C_sigma||u||_(H^sigma)(1+log n),
                     every x>=0 and n>=1.            (8)

The change of clock in the compact band has not changed the current or its
conditional mean. It only provides the correct finite entrance-time estimate.

## 5. Gaussian-small SAME conditional variance

Since the variance minimizes squared distance to constants, (8) gives

    V_w(x)<=sum_(n>=2)p_n(x)|w(x,n)-w(x,1)|^2
           <=C_sigma||u||Hs^2
                         sum_(n>=2)p_n(x)(1+log n)^2
           <=C_sigma'||u||Hs^2 exp[-3pi exp(2x)].     (9)

For the last inequality factor exp(-3z) from
2 sum_(n>=2)n^4(1+log n)^2 exp[-z(n^2-1)] and bound the remaining series
by its value at z=pi. This is a complete all-label bound, not a finite-tail
cutoff or a change of posterior.

Equation (9) strengthens V_w<=J for the SAME full-band current field and
allows its complete reset/divisor variance terms to be passed through theta
weights without introducing a new unbounded label norm. It does not identify
w with the canonical Mobius quotient, whose wall singularity remains real.
For a canonical numerator v=phi_shift/eta_shift, the exact repair
k=v-s w has T k=0, but k/s retains the canonical wall debt unless separately
renormalized. Nor does (9) sign the remaining Gamma/reflected/pole edge
combination or create an extra current-storage budget.
