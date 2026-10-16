# Addendum: the prescribed-moment operator norms diverge

Date: 2026-10-16.

This addendum strengthens the conclusion for exactly the positive
past-row plus rank-one family in the
[stationary-completion report](REPORT.md). It does not change that
report or assume stationarity. In this family, even a uniform bound
on the critical-measure operator norms is impossible.

## 1. Hypotheses and extended norm

Retain all definitions and hypotheses (1)--(8) of the report. In
particular, r is a real bounded Borel function with r(x) -> c, m > 0,
and 0 < epsilon <= 1. The complete arithmetic rows give

    U = F_- psi,                       L = F_r psi,
    d mu_R = A_R L^2 dx,                Z_R = integral A_R L^2,

    K_R f = a_R F_- f + b_R integral t_R f,
    b_R = L - a_R U >= 0,               a_R >= 0,
    P_R h = K_R(psi h)/L.

The three exact anchor moments are

    integral t_R psi = 1,
    integral t_R psi r = 0,
    integral t_R psi r^2 = m.

Thus P_R is positive and P_R 1 = 1. As in the report, A_R has compact
support, 0 <= A_R <= exp(-epsilon x), and A_R converges pointwise to
exp(-epsilon x). No fixed shape or support is imposed on t_R, and
a_R need not be at most one.

Define M_R as the least constant in the inequality

    ||P_R h||_L2(mu_R) <= M_R ||h||_L2(mu_R)                 (A1)

for every bounded Borel h. Set M_R = infinity if no finite constant
exists. This convention also covers a row that does not respect
mu_R-null equivalence classes: if some h has zero input norm and
positive output norm, then M_R is already infinite. When M_R is
finite, (A1) gives the ordinary bounded L2 extension.

## 2. Quantitative theorem

**Theorem.** There are finite constants C0 >= 0 and C1 > 0, independent
of R, such that every finite M_R satisfies

    M_R [||(r-c)^2||_L2(mu_R) + d C1]
        >= d [sqrt(Z_R) - C0],                            (A2)

where

    d = m + c^2 > 0.

Consequently M_R -> infinity as R -> infinity. The same statement
holds along every cutoff sequence with the required pointwise limit.
Neither stationarity nor an additional actual-source equation is
assumed.

**Proof.** Put

    q_R = a_R U/L.

The row-positivity hypothesis gives 0 <= q_R <= 1. Choose one fixed
nonzero nonnegative continuous phi with compact support strictly
inside (0, infinity), and let h0 = phi/psi. This is a bounded
continuous compact test. Its input norm is uniformly bounded:

    ||h0||_L2(mu_R)^2
      <= integral exp(-epsilon x) L(x)^2 [phi(x)/psi(x)]^2 dx
      =: H0^2 < infinity.                                (A3)

The report proves, with all prime powers retained,

    (F_- phi)(x)/exp(x/2) -> J_-(phi) > 0,
    U(x)/exp(x/2)         -> J_-(psi) > 0.

Therefore there are fixed x0 and kappa > 0 such that
F_- phi >= kappa U on x >= x0. Positivity of the anchor term yields

    P_R h0 >= a_R F_- phi/L >= kappa q_R
                                                 on x >= x0.   (A4)

Using (A1), (A3) and (A4), the tail norm of q_R is at most
kappa^(-1) H0 M_R. On 0 < x < x0, use q_R <= 1 and the common bound
on A_R. Hence, with constants independent of R,

    ||q_R||_L2(mu_R) <= C0 + C1 M_R,                       (A5)

where one may take

    C0 = [integral_0^x0 exp(-epsilon x) L(x)^2 dx]^(1/2),
    C1 = kappa^(-1) H0.

Next use the single nonnegative bounded test

    f = (r-c)^2.

Its anchor expectation is exactly

    integral t_R psi f = m - 2c * 0 + c^2 * 1 = d.

The complete retained past row is positive. Thus

    P_R f >= (b_R/L) d = d(1-q_R).                         (A6)

The triangle inequality and (A5)--(A6) imply

    M_R ||f||_L2(mu_R)
      >= ||P_R f||_L2(mu_R)
      >= d ||1-q_R||_L2(mu_R)
      >= d [sqrt(Z_R) - C0 - C1 M_R].

Rearranging proves (A2).

The report's mass-escape argument uses only the complete L asymptotic
and the cutoff hypotheses, not stationarity. It therefore applies here:
Z_R -> infinity, and mu_R/Z_R gives vanishing mass to every fixed
bounded interval. Since r is bounded and tends to c,

    ||(r-c)^2||_L2(mu_R)^2 / Z_R
      = (1/Z_R) integral |r-c|^4 d mu_R
      -> 0.                                               (A7)

Divide (A2) by sqrt(Z_R). Its right side tends to d > 0, while the
factor multiplying M_R tends to zero. Equivalently, for all sufficiently
large R with finite M_R,

    M_R >= d [sqrt(Z_R)-C0]
               / [||(r-c)^2||_L2(mu_R) + d C1]
         -> infinity.                                     (A8)

The convention M_R = infinity covers all remaining cutoffs. This proves
the theorem. The varying L2 spaces cause no passage-of-operator issue:
every estimate is at a fixed R, and only the explicit scalar bounds
are then compared. QED.

## 3. Two immediate refinements

For the actual ratio in the report's application, the published plateau
theorem also gives r-c in L2(dx), and r-c is bounded. At epsilon = 1,
the complete tail and local boundedness make exp(-x)L(x)^2 bounded.
Consequently ||(r-c)^2||_L2(mu_R) is uniformly bounded. Formula (A2)
then strengthens to

    M_R >= c0 sqrt(Z_R) - c1

for fixed positive c0 and finite c1. This statement asserts no rate
in R for an unspecified cutoff family.

If the two anchor moments are instead allowed to vary, retain
integral t_R psi = 1 and write

    d_R = integral t_R psi (r-c)^2 >= 0.

For a family with uniformly bounded M_R, the proof of (A5) still gives
||q_R|| = O(1), while (A6) holds with d_R in place of d. Thus (A7)
forces d_R -> 0. Cauchy-Schwarz under the probability measure
t_R psi dx then gives

    integral t_R psi r   -> c,
    integral t_R psi r^2 -> c^2.

So the changed-moment escape condition in the report is necessary
even for uniform boundedness, without assuming stationarity.

## 4. Exact scope

This is a stronger obstruction to the same prescribed-moment positive
rank-one implementation, not a bound for the original signed prime
expression. It supplies no sign to the complete compensated-generator
comparison, and asserts no new original quadratic-form domain.
It does not prove RH.

The changed-moment mean projection at the end of the report still has
operator norm one. It is not a counterexample to this addendum: its
anchor expectation of (r-c)^2 tends to zero, rather than being the
fixed positive number m+c^2. The three exact prescribed moments and
positivity of both source branches are essential to (A6).
