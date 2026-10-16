# Prescribed moments obstruct a stationary completion in the critical square measure

Date: 2026-10-16.

Consider a positive rank-one completion of the full past-prime row
required to match the theta ground and three specified source moments.
Those conditions do **not** permit a family of such completions to be
stationary, or contractive, in the critical damped-square measure as the
output cutoff is removed. The theorem below excludes the entire
specified family, even when its past multiplier and anchor vary with the
cutoff. It does not exclude arbitrary stationary kernels, establish an
estimate for the original signed form, or prove RH.

## 1. Full arithmetic rows and hypotheses

On x > 0, use the original positive theta source psi, with its simple
zero at the origin and its complete theta tail. In particular,

    psi(x) > 0,
    psi(x) = O(x)                                  as x -> 0,
    psi(x) = O(exp(13x/2) exp(-pi exp(2x)))         as x -> infinity.

These are the unchanged normalizations of the
[original source forms](../20261015_old_actual_physical_range/REPORT.md#0-source-forms-arithmetic-operators-and-dependencies).
Write Lambda for the von Mangoldt function and set

    d_n = log n,                   alpha_n = Lambda(n)/sqrt(n),

    (F_- f)(x) = sum_{d_n < x} alpha_n f(x-d_n),
    (F_r f)(x) = sum_{d_n > x} alpha_n f(d_n-x),

    U = F_- psi,                   L = F_r psi,
    J_+(f) = integral_0^infinity exp(x/2) f(x) dx,
    J_-(f) = integral_0^infinity exp(-x/2) f(x) dx.            (1)

Every nonzero von Mangoldt label is included, so all prime powers are
retained. The notation F_- denotes the past row, also written F* in
source-adjoint notation. All unspecified integrals below are over
(0, infinity) with respect to dx.

The complete sums are locally bounded, L > 0, and the ordinary prime
number theorem gives

    L(x) / exp(x/2) -> J_+(psi),
    U(x) / exp(x/2) -> J_-(psi).                             (2)

For each nonzero nonnegative continuous phi with compact support
strictly inside (0, infinity), it also gives

    (F_- phi)(x) / exp(x/2) -> J_-(phi) > 0.                  (3)

A direct verification, including the infinite reflected tail, is given
in Section 2. No prime-number-theorem error term is required.

Let r be a real bounded Borel function with a finite plateau:

    r(x) -> c as x -> infinity,
    g = psi r,                    q2 = psi r^2.             (4)

Fix m > 0 and 0 < epsilon <= 1. For cutoff parameters R -> infinity,
let A_R be nonnegative measurable functions satisfying

    0 <= A_R(x) <= exp(-epsilon x),
    A_R(x) -> exp(-epsilon x) for every fixed x > 0,         (5)

with compact support for each R. Define the finite measures and their
masses by

    d mu_R(x) = A_R(x) L(x)^2 dx,
    Z_R = integral A_R L^2.                                 (6)

For each R, allow arbitrary nonnegative measurable a_R and t_R, with
a_R finite, such that

    b_R = L - a_R U >= 0,

    integral t_R psi = 1,
    integral t_R g   = 0,
    integral t_R q2  = m.                                   (7)

All three integrals are finite. Neither a fixed anchor shape nor compact
support of t_R is assumed. There is no upper bound a_R <= 1; only
a_R >= 0 and a_R U <= L are required.

The corresponding positive source row and its normalized Markov map are

    K_R f = a_R F_- f + b_R integral t_R(y) f(y) dy,
    P_R h = K_R(psi h) / L.                                 (8)

They are well defined on |f| <= C psi and on bounded Borel h,
respectively. Equation (7) gives K_R psi = L, so P_R 1 = 1.

**Theorem.** There is no family satisfying (4)--(8) for which P_R is
mu_R-stationary for every sufficiently large cutoff R. The same
exclusion holds along any sequence R -> infinity for which (5) holds.
Here stationarity means

    integral P_R h d mu_R = integral h d mu_R.               (9)

It is enough to assume (9) initially for compactly supported continuous
tests. In particular, this family cannot consist of positive row-Markov
contractions on L2(mu_R).

For the original pole-centered actual source, the published
[ratio plateau theorem](../20261014_actual_ratio_multipliers/REPORT.md#1-sobolev-and-pointwise-plateau)
supplies (4). The prescribed second moment used in the matched-ground
construction is

    m = ell(q2) / ell(psi),
    ell(f) = integral sinh(x/2) f(x) dx,
    ell(psi) = 1/8.                                         (10)

For nonzero real g in that source class, m is finite and strictly
positive because r is bounded and the pole measure
psi(x) sinh(x/2) dx has full positive support. The theorem uses these
properties, not an additional claim about the original source equation
or its domain.

## 2. Arithmetic estimates and the retained past mass

For completeness, write X = exp(x) and
Psi(X) = sum_{n <= X} Lambda(n). The ordinary prime number theorem is
Psi(X)/X -> 1, and the Chebyshev upper bound is Psi(X) <= C X.
For a function f with the indicated compact support, or for psi,

    exp(-x/2) (F_- f)(x)
      = (1/X) sum_{n < X} Lambda(n)
                      (n/X)^(-1/2) f(-log(n/X)).            (11)

The rescaled positive measures X^(-1) d Psi(Xs) converge on compact
positive s-intervals to ds. For psi, the test in (11) extends
continuously to s = 0 with value zero by the complete theta tail; it
vanishes at s = 1 by the origin zero. The Chebyshev bound controls the
remaining interval near s = 0. Thus (11) tends to

    integral_0^1 s^(-1/2) f(-log s) ds = J_-(f).

The compactly supported case follows by the same argument. This proves
(3) and the assertion for U in (2).

For the reflected row,

    exp(-x/2) L(x)
      = (1/X) sum_{n > X} Lambda(n)
                      (n/X)^(-1/2) psi(log(n/X)).            (12)

On each finite s-interval the same convergence applies. The upper
bound on Psi, followed by dyadic shells [2^j, 2^(j+1)), uniformly bounds
the omitted tail by a constant times

    sum_{j >= j0} 2^j
       sup_{2^j <= s <= 2^(j+1)} s^(-1/2) psi(log s).

This tends to zero as j0 -> infinity by the theta tail. The limit of
(12) is therefore

    integral_1^infinity s^(-1/2) psi(log s) ds = J_+(psi).

This proves the remaining part of (2) with the complete prime-power row.

Assume now that stationarity holds. Fix a nonzero phi >= 0, continuous
and compactly supported away from the wall. Applying (9) to
h = phi/psi and dropping the nonnegative anchor contribution yields

    integral A_R L a_R F_- phi
      <= integral A_R L^2 phi/psi
      <= C_phi,                                            (13)

where C_phi is independent of R, by (5) and compact support.
By (2)--(3), U <= C F_- phi outside a fixed bounded interval.
On that interval, a_R U <= L. Consequently

    B0(R) := integral A_R L a_R U = O(1).                    (14)

Indeed, the contribution from the fixed interval is at most
the integral there of exp(-epsilon x) L^2, and the tail is bounded
by (13). This estimate is the essential full-row input: stationarity
permits only a bounded total contribution from the retained past row
in the critical measure. It does not require pointwise convergence of
a_R, and does not omit a changing tail or any prime powers.

## 3. The two stationary moments contradict the plateau

First justify using bounded, possibly noncompact tests in (9). For
each fixed R, mu_R is finite and P_R is a positive Markov kernel.
The measure

    nu_R(E) = integral P_R(1_E) d mu_R

is therefore finite, with total mass Z_R. Equality against all compact
continuous tests identifies nu_R = mu_R. Thus (9) holds for all bounded
Borel tests, including r and r^2. This is a measure-theoretic extension
of stationarity; it asserts no new original quadratic-form domain.

For j = 1, 2, put

    Bj(R) = integral A_R L a_R F_-(psi r^j).

Positivity of F_- and boundedness of r give

    |Bj(R)| <= ||r||_infinity^j B0(R) = O(1).                (15)

Also

    integral A_R L b_R = Z_R - B0(R).                        (16)

Using the exact anchor moments (7), stationarity of r and r^2 now reads

    integral r d mu_R   = B1(R),
    integral r^2 d mu_R = B2(R) + m [Z_R - B0(R)].            (17)

By (2), the integral of exp(-epsilon x) L(x)^2 over (0, infinity)
is infinite for 0 < epsilon <= 1. Fatou's lemma and (5) imply
Z_R -> infinity. Every fixed bounded interval has uniformly bounded
mu_R-mass. Therefore the probability measures mu_R/Z_R escape to
infinity. Since r is bounded and tends to c, splitting the integrals
at a fixed sufficiently large point gives

    (1/Z_R) integral r d mu_R   -> c,
    (1/Z_R) integral r^2 d mu_R -> c^2.                      (18)

But (14)--(17) make these same limits 0 and m, respectively.
Thus c = 0 and c^2 = m > 0, a contradiction. This proves the theorem.

To obtain the stated contraction consequence, suppose a positive
row-Markov P_R were contractive on L2(mu_R). The constant 1 lies in
that space, since mu_R is finite. For bounded real h, expand

    ||P_R(1 + t h)||_L2(mu_R)^2 <= ||1 + t h||_L2(mu_R)^2

for both signs of real t. Since P_R 1 = 1, equality of the linear
terms is forced:

    integral P_R h d mu_R = integral h d mu_R.

Thus P_R would be stationary, which the theorem excludes for this family.

## 4. Exact scope and the necessary escape for changed moments

The result excludes the positive past-plus-rank-one family (8) with the
three exact moments (7) in the critical square measure. It does not
exclude arbitrary stationary kernels, signed completions, changed
limiting measures, or estimates using the full compensated generators.
In particular it gives no sign to the original mixed quantity

    <Wg, A_R (F_- - F_r) g>,
    where Wg = (L/psi) g - F_r g.

Its complete archimedean, prime and pole partners remain unchanged and
are not estimated by this theorem.

There is a precise necessary condition for an anchor with different
moments. Retain all other hypotheses, including integral t_R psi = 1,
but replace the last two moment conditions in (7) by the definitions

    m1(R) = integral t_R psi r,
    m2(R) = integral t_R psi r^2.

The same proof gives

    integral r^j d mu_R = Bj(R) + [Z_R - B0(R)] mj(R),  j = 1, 2.

Consequently stationarity requires

    m1(R) -> c,
    m2(R) -> c^2,
    m2(R) - m1(R)^2 -> 0.                                  (19)

Thus such an anchor must concentrate in ratio value at the plateau.
This is only a necessary condition, not an estimate for the original
signed form. Replacing the prescribed moments (0, m) by (19) changes
the actions on both g and q2; the resulting full forcing and pole
corrections cannot be discarded.

An explicit changed-moment example confirms this scope. For Z_R > 0,
take

    a_R = 0,
    b_R = L,
    t_R(x) = A_R(x) L(x)^2 / [Z_R psi(x)].

Then integral t_R psi = 1 and P_R h is the constant
(1/Z_R) integral h d mu_R. It is the stationary, L2-contractive mean
projection. Its first two anchor moments are the normalized mu_R
moments of r and r^2, which tend to c and c^2 rather than the prescribed
pair (0, m) with m > 0. Only psi-weighted integrability of t_R is used;
ordinary unweighted integrability at the wall is not required.
