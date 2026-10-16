# Local compactness of normalized positive neutral sources

Date: 2026-10-16.

The complete weak-neutral positive cone, normalized by its pole moment, is
precompact in local L1 on the open positive half-line. Every subsequential
limit is again a nonnegative complete weak-neutral source, possibly zero,
with no increase of the pole moment. The proof retains the odd Gamma
operator, every prime power, both prime orientations, reflection, and the
full pole. It uses no local supremum bound on the sources.

The conclusion is local. An explicit normalized positive neutral family
escapes entirely to infinity. Neither a positive limiting ground, a full
quadratic ground identity, a minimizing ground, nor the original sharp
source sign follows.

## 1. Complete source and statement

Use the half-line conventions

    s(x)=sinh(x/2), ell(h)=integral_0^infinity s(x)h(x)dx,
    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    kappa(t)=exp(-t/2)/(1-exp(-2t)), t>0,
    a(xi)=Re digamma(1/4+i xi/2)-log pi.

All Mangoldt sums below include every prime power. For positive inputs,
these rows are initially interpreted by Tonelli, allowing infinity:

    F_+h(x)=sum_n alpha_n h(x+d_n),
    F_-h(x)=sum_(d_n<x) alpha_n h(x-d_n),
    Rh(x)=sum_(d_n>x) alpha_n h(d_n-x).                 (1)

For a smooth compact test phi in `(0,infinity)`, let phi_o be its odd
extension and put `G phi=(a(D)phi_o)|_(0,infinity)`, with Fourier convention
`hat f(xi)=integral_R f(x)exp(i xi x)dx`. The full source is

    Q0 phi/2=G phi-F_+phi-F_-phi+Rphi-4ell(phi)s.        (2)

A locally integrable function h on `(0,infinity)` is a complete weak
neutral source if every full pairing below is absolutely defined and

    integral_0^infinity h(x)Q0 phi(x)dx=0
                for every phi in C_c^infinity(0,infinity). (3)

This is the full weak equation, not merely vanishing of a scalar quadratic
form. The conventions and endpoint estimates are those of the published
[positive-neutral approximation report](../20261015_positive_neutral_approximation_cost/REPORT.md),
Sections 1 and 2. We repeat the estimates needed here.

**Theorem.** Let h_j be nonnegative complete weak neutral sources with
`ell(h_j)=1`. Then a subsequence converges in `L1(K)` for every compact
`K subset (0,infinity)` to a nonnegative complete weak neutral source h,
with `ell(h)<=1`. More precisely, after passing to a subsequence,

    s h_j dx -> s h dx + (1-ell(h)) delta_infinity       (4)

weakly on the compact interval `[0,infinity]`. There is no mass at any
finite point in this limit, including the wall zero.

Thus the set of normalized sources is relatively compact in
`L1_loc((0,infinity))`. The limit may be zero. No assertion is made about
unweighted L1 convergence at the wall, local uniform convergence, a
positive lower bound, or tightness at infinity.

## 2. Complete test endpoints and exclusion of finite atoms

For every fixed compact smooth phi, the function

    B_phi(x)=Q0 phi(x)/s(x)                            (5)

extends continuously to `[0,infinity]`, is bounded, and has value zero at
infinity. Near zero, the past row is zero and the full future/reflection
pair is the finite sum

    sum_n alpha_n[phi(d_n-x)-phi(d_n+x)]=O_phi(x).

The odd Gamma kernel, off the support of phi, is

    G phi(x)=-integral_0^infinity
       [kappa(|x-y|)-kappa(x+y)]phi(y)dy.               (6)

It is smooth and odd at the wall. The pole is also O(x). The same
expressions show that the quotient has a limit at zero.

At infinity, G phi is O(exp(-x/2)) and F_+phi vanishes. The ordinary prime
number theorem applied to smooth compact logarithmic weights gives

    F_-phi(x)=exp(x/2) integral exp(-y/2)phi(y)dy
                 +o(exp(x/2)),
    Rphi(x)=exp(x/2) integral exp(y/2)phi(y)dy
                 +o(exp(x/2)).                        (7)

Their difference has leading term `2ell(phi)exp(x/2)`, canceled exactly by
`-4ell(phi)s(x)`. This proves the assertion at infinity. Individual past,
reflection, and pole rows do not have that vanishing quotient.

Set `nu_j=s h_j dx`. These are probability measures on `[0,infinity]`.
Any weak subsequential limit nu satisfies

    integral B_phi dnu=0                              (8)

for every fixed test phi. We now exclude atoms using bounded families of
these exact complete tests. The passage first takes the weak limit in j,
and only then takes the small-scale limit in the test.

### 2.1. The wall

Put `d=log 2` and `alpha_2=log(2)/sqrt(2)`. Choose a smooth compact bump
vartheta supported in `(-1,1)` with `vartheta'(0)=1`, and set

    phi_epsilon(x)=epsilon vartheta((x-d)/epsilon).

Choose a fixed wall collar smaller than both `d/4` and
`(log 3-log 2)/4`. For small epsilon the only arithmetic label meeting
the bump from this collar is n=2. Its complete Q0 contribution is

    2 alpha_2[phi_epsilon(d-x)-phi_epsilon(d+x)].       (9)

The past row is zero. The uniform Lipschitz bound makes (9) O(x), while
(6) is O(x epsilon^2) and the pole is O(s(x)epsilon^2). In particular,

    B_(phi_epsilon)(0)=-8 alpha_2+O(epsilon^2).         (10)

For x outside that fixed collar, the Chebyshev estimate
`sum_(n<=X)Lambda(n)<=C X` and partial summation give the arithmetic bound
`C epsilon exp(x/2)`. The Gamma row has supremum at most
`C epsilon(1+log(1/epsilon))` on bounded intervals and its decaying
kernel tail off the bump. The pole quotient is O(epsilon^2).
Consequently B_(phi_epsilon) is uniformly bounded on the compactification
and tends to zero at every fixed positive x and at infinity. Dominated
convergence in (8), using (10), gives `nu({0})=0`.

### 2.2. Every interior point

Fix x0>0. This time choose vartheta even, supported in `(-1,1)`, with
`vartheta(0)=1`, and put

    phi_epsilon(x)=vartheta((x-x0)/epsilon),
    L_epsilon=log(1/epsilon).

The Gamma symbol has asymptotic `a(xi)=log|xi|-log(2pi)+O(|xi|^-2)`.
Fourier inversion for the single bump at its center therefore gives

    G phi_epsilon(x0)=L_epsilon+O(1).                 (11)

Indeed, after scaling frequency by epsilon, subtract L_epsilon under the
integral against the Schwartz function hat(vartheta); the remaining
logarithmic singularity at frequency zero is integrable, and the
frequency interval of size epsilon contributes O(epsilon L_epsilon).
The negative reflected bump of the odd extension contributes O(epsilon)
by its separation from x0. The same Fourier estimate bounds the Gamma
supremum by `C(1+L_epsilon)`. At each other fixed positive point, (6)
shows that its normalized value tends to zero.

There is no uncontrolled wall quotient in this argument. If x0 is a
prime-power label log n, evenness gives exact cancellation of its
future/reflection pair in a sufficiently small fixed wall collar. All
other labels are separated. If x0 is not a label, choose the collar
smaller than its distance to the finitely many nearby labels; then all
arithmetic rows there vanish for small epsilon. Formula (6) gives a
Gamma wall quotient O(epsilon), and the pole quotient is O(epsilon).
Outside the collar Chebyshev bounds each arithmetic quotient uniformly.
It follows that

    B_(phi_epsilon)/L_epsilon
       -> (2/s(x0)) 1_{x0}                            (12)

pointwise on `[0,infinity]`, with a uniform bound. The factor two comes
from (2). Applying dominated convergence to (8) proves `nu({x0})=0`.

These conclusions hold for every weak subsequential limit. In particular,
for every fixed finite set of interior points, their sufficiently small
neighborhoods carry uniformly small nu_j mass. Otherwise a subsequence
and shrinking neighborhoods would produce an atom in a weak limit. This
fact will patch the prime knots below; it is not an unweighted wall bound.

## 3. An exact integrable inverse for the logarithmic model

Write

    B0(xi)=log(1+xi^2)/2,
    a(xi)=B0(xi)-log(2pi)+r(xi).                       (13)

The digamma asymptotic, with differentiated remainders, gives
`r(xi)=O(|xi|^-2)` and `r''(xi)=O(|xi|^-4)` at infinity. The symbol is
smooth and even near zero, so `r,r'' in L1(R)`. These estimates follow
from the uniform sector expansion in
[DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2), or directly by differentiating
its analytic remainder on smaller sectors. Thus the inverse Fourier
kernel k_r is bounded near zero and O(x^-2) at infinity, by two
integrations by parts. In particular `k_r in L1(R)`.

The model inverse has the exact representation

    1/(1+B0(xi))
      =integral_0^infinity exp(-t)(1+xi^2)^(-t/2)dt.   (14)

For t>0,

    (1+xi^2)^(-t/2)
      =1/Gamma(t/2) integral_0^infinity
           v^(t/2-1)exp(-v)exp(-v xi^2)dv.            (15)

The inverse Fourier transform of the last factor is the Gaussian
`(4pi v)^(-1/2)exp(-x^2/(4v))`, of integral one. Tonelli applied to
(14)-(15) constructs an ordinary nonnegative integrable kernel K with

    integral_R K(x)dx=1,
    hat K(xi)=1/(1+B0(xi)).                            (16)

There is no point mass at zero: (15) is a mixture of densities for every
t>0, and t=0 has zero measure in (14). In particular

    ||K(.+z)-K||_1 -> 0 as z -> 0.                    (17)

Only this integrable model inverse is used. No positivity of the inverse
of the full signed source operator is being assumed.

## 4. Localization away from prime knots

Let `D={log n: Lambda(n)>0}`. Choose an even smooth compact cutoff chi
whose positive support K0 lies in `(0,infinity)` and has positive distance
from D. We may choose chi equal to one on any smaller compact set avoiding
D. Define the compactly supported odd source

    f_j=chi (h_j)_o.

This is an ordinary L1 function with uniformly bounded norm, because s is
bounded below on K0. The unrestricted odd extension need not be an
ordinary L1 function at the wall. It is instead the tempered distribution

    <(h_j)_o,phi>=integral_0^infinity
                       h_j(y)[phi(y)-phi(-y)]dy,      (18)

whose wall pairing is controlled by `y h_j(y)` and whose tail is controlled
by ell(h_j). We do not assume unweighted wall integrability.

### 4.1. Each localized prime row is a finite measure

Changing variables in (1), the three positive incoming columns for an
output set K0 are respectively

    sum_n alpha_n 1_(y-d_n in K0),
    sum_n alpha_n 1_(y+d_n in K0),
    sum_n alpha_n 1_(d_n-y in K0).                    (19)

They vanish for all sufficiently small y: for the last two this uses the
positive distance of K0 from D. On the remaining bounded y interval they
are bounded, and at infinity partial summation of Chebyshev gives the
bound `C exp(y/2)`. Therefore each column in (19) is at most `C_chi s(y)`
for all y>0. Tonelli gives uniform local L1 bounds for all three separate
prime rows. Every prime power remains in these estimates. At a prime
knot the same separate wall bound has not been asserted.

### 4.2. The whole odd Gamma commutator is integrable

The exact kernel of `[a(D),chi]` acting on the odd extension, on positive
variables, is

    (chi(x)-chi(y))[kappa(|x-y|)-kappa(x+y)].          (20)

Its x-L1 column satisfies

    integral_0^infinity |(20)| dx <= C_chi s(y).       (21)

Here are the three endpoint mechanisms. For sufficiently small y,
chi(y)=0 and x is in the fixed support of chi; the odd kernel difference
is O(y). Near x=y the Lipschitz difference of chi cancels the
`1/|x-y|` singularity. When y is large, only x in the fixed support can
contribute and the kernel decays as O(exp(-y/2)); when y is in a fixed
middle interval, the remaining x tails are exponentially integrable.
These observations prove (21), including the x=0 side. By (18), Tonelli,
and ell(h_j)=1, the entire commutator is uniformly L1 on the full line.
This is where the odd wall cancellation is retained rather than replaced
by an unweighted mass assumption.

### 4.3. A bounded measure right-hand side

Localize (2)-(3), odd-extend the localized equation, and use (13). In the
sense of full-line tempered distributions,

    (1+B0(D)) f_j = mu_j,
    mu_j=(1+log(2pi))f_j
         +chi(F_+h_j+F_-h_j-Rh_j+4s)_o
         +[a(D),chi](h_j)_o-r(D)f_j.                 (22)

Every displayed term is a finite signed measure, and

    sup_j ||mu_j||_TV < infinity.                    (23)

For the prime and Gamma terms this is Sections 4.1 and 4.2. The pole is
compactly cut and keeps its full coefficient. Finally, `r(D)f_j=k_r*f_j`
is uniformly L1 by Section 3. The distributional localization can
alternatively be obtained first by cutting (18) at the wall and infinity;
(19) and (21) justify passing those cuts. No separate uncut prime operator
domain is used.

Applying the exact model inverse to (22) gives `f_j=K*mu_j`. Indeed (16)
is the reciprocal of the nonvanishing smooth multiplier in (22), so this
is also uniqueness in tempered distributions. Equations (17) and (23)
give

    ||f_j(.+z)-f_j||_1
       <= ||mu_j||_TV ||K(.+z)-K||_1 -> 0             (24)

uniformly in j. Together with the fixed compact support of f_j and its
uniform L1 bound, the Kolmogorov-Riesz criterion proves L1 precompactness
of the localized sources. Thus h_j is locally L1 precompact away from D.

## 5. Patching the knots and retaining weak neutrality

First pass to a weakly convergent subsequence of the probabilities nu_j
on `[0,infinity]`. Then take a diagonal subsequence with local L1
convergence on the complement of D, using Section 4. Every fixed interior
compact contains only finitely many points of D. By Section 2 its weak
limit has no atom at these points. Choose small neighborhoods of them
with arbitrarily small limiting mass and with boundaries of zero limiting
mass. Weak convergence makes their nu_j masses small for all sufficiently
large j. Since s is bounded below on that compact, their h_j L1 masses
are also small. Convergence off these neighborhoods now proves the L1
Cauchy property on the entire compact. Exhausting the open half-line
gives the asserted local L1 limit h.

On the open half-line the weak measure limit is therefore `s h dx`.
Section 2 excludes a wall atom, leaving only an infinity atom. Positivity
and total mass one give `ell(h)<=1` and (4). For any fixed compact smooth
phi, (5) is continuous and bounded on the compactification and vanishes
at infinity. Hence

    0=lim_j integral B_phi dnu_j
      =integral_0^infinity h(x)Q0 phi(x)dx.            (25)

This pairing is absolute, bounded by `||B_phi||_infinity ell(h)`.
Thus h is a complete weak neutral source, even when h=0 or h has zeros.
This finishes the theorem. It does not assign a quadratic form domain
or positive-ground identity to the limit.

## 6. Explicit failure of tightness at infinity

The failure is realized inside the same positive weak-neutral cone, not
by an unrelated sequence of measures. Use the even theta source

    Phi(x)=sum_(n>=1)
       [4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2)]
                      exp(-pi n^2 exp(2x)).

It is positive, even, strictly decreasing for x>0, and has theta tails
with all derivatives. The complete translation-invariant source

    T=a(D)-sum_n alpha_n(E_(d_n)+E_(-d_n))

satisfies `T Phi=-cosh(x/2)`, and

    integral_R cosh(y/2)Phi(y)dy=1/2.                 (26)

These identities and their full-prime passages are proved in the
[original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md)
and the [odd operator-domain report](../20261013_odd_operator_domains/REPORT.md).
The strict monotonicity is the positivity of `psi=-Phi'` established in
the [reflected-prime energy report](../20261013_reflected_prime_energy/REPORT.md).

For z>0 define, using the even full-line Phi,

    n_z(x)=[Phi(x-z)-Phi(x+z)]/2,
    h_z(x)=4n_z(x)/sinh(z/2), x>0.                    (27)

Then n_z>0. Complete finite translation and (26) give exactly

    T n_z=sinh(z/2)s,
    ell(n_z)=sinh(z/2)/4,
    Q0 n_z/2=T n_z-4ell(n_z)s=0.                     (28)

Thus h_z is positive, complete weak neutral, and ell(h_z)=1. For each
fixed z all source pairings are justified by the theta tails; no original
quadratic P membership for arbitrarily large translations is inferred.

At x=z+y,

    s(z+y)h_z(z+y) -> 2exp(y/2)Phi(y)                 (29)

as z tends to infinity. The limiting density has integral one by (26).
For z>=1, on y>-z its left side is bounded by
`C exp(y/2)Phi(y)`: the difference of the two Phi terms is nonnegative
and at most Phi(y), and the hyperbolic factor has that bound. Dominated
convergence applies. Also h_z tends to zero uniformly on every fixed
interior compact. Consequently

    s h_z dx -> delta_infinity,
    h_z -> 0 in L1_loc((0,infinity)).                 (30)

The lost pole mass in (4) can therefore equal one.

## 7. Scope

The theorem gives local strong compactness and weak-source closure for
the normalized nonnegative complete-neutral cone. It requires neither a
bound on reflected comparison cost nor an assumed local supremum bound.
It preserves all source terms, especially the wall oddness and the full
past/reflection/pole cancellation at infinity.

It does not yield unweighted wall tightness, local uniform positivity,
a lower comparison with psi, or a full ground identity for a rough or
vanishing limit. In particular, local L1 convergence cannot silently
replace a positive locally uniform limit in stronger reflected-cost
escape-debit arguments. Nor does it license the legal ground variations
proved for more restrictive classes in the
[neutral-ground descent report](../20261016_neutral_ground_descent_pole_floor/REPORT.md)
and its [lower-comparable addendum](../20261016_neutral_ground_descent_pole_floor/LOWER_COMPARABLE_GROUND_ADDENDUM.md).

The result proves no existence of an optimizer, no contraction or sharp
comparison in the original metric, and no assertion about the location
or simplicity of zeta zeros.
