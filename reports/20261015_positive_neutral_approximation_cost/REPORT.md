# Positive neutral approximation and divergent reflected-prime cost

A positive sequence of complete weak neutral sources cannot converge locally
uniformly to a nonneutral positive source while keeping its reflected-prime
comparison cost bounded. The proof uses positivity of the approximating
sources, the prime number theorem, and the exact cancellation of the full
pole against the leading past/reflected prime row. It is not a sign theorem
for the original source form or an exclusion of general ground optimization.

## 1. Complete source and reflection conventions

All functions and pairings in this report are real and on `(0,infinity)`
unless a full-line extension is explicitly indicated. Set

    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    s(x)=sinh(x/2), ell(phi)=integral_0^infinity s(x)phi(x)dx,
    kappa(t)=exp(-t/2)/(1-exp(-2t)), t>0,
    a(t)=Re digamma(1/4+it/2)-log pi.

Every Mangoldt sum includes all prime powers. Define

    F_+h(x)=sum_(n>=2) alpha_n h(x+d_n),
    F_-h(x)=sum_(d_n<x) alpha_n h(x-d_n),
    Rh(x)=sum_(d_n>x) alpha_n h(d_n-x).                 (1)

For a smooth compact source phi in `(0,infinity)`, let phi_o be its odd
extension and let G phi be the positive-half-line restriction of
`a(D)phi_o`, with Fourier transform `hat f(t)=integral f(x)exp(itx)dx`.
The complete original source operator on such tests is

    Q0 phi/2=G phi-F_+phi-F_-phi+Rphi-4ell(phi)s.        (2)

Thus its half-line quadratic pole is `-8ell(phi)^2`. In particular (2)
retains both prime orientations, the reflected prime row, the odd Gamma
compression, and the full pole.

Outside the support of phi, the Gamma row has the explicit kernel

    G phi(x)=-integral_0^infinity
       [kappa(|x-y|)-kappa(x+y)]phi(y)dy.               (3)

This follows from
`a(t)=a(0)+2integral_0^infinity kappa(v)(1-cos(tv))dv`.
No diagonal convention in that integral affects the off-support formula.

A locally integrable source h is a **complete weak neutral source** here
if, for every `phi in C_c^infinity(0,infinity)`, the full pairing is
absolutely defined and

    integral_0^infinity h(x)Q0 phi(x)dx=0.             (4)

This is the weak source equation `Q0 h=0`, not the weaker scalar assertion
`q0[h]=0`. Equation (4) can also be obtained from a common-cutoff source
identity once its limit equals the displayed full pairing.

For a strictly positive continuous h and a strictly positive continuous f
with `C_f=integral f Rf<infinity`, define the nonnegative extended comparison
cost directly by its reflected-edge squares:

    N_h[f]=sum_(n>=2) alpha_n integral_0^(d_n)
       h(x)h(d_n-x)
       [f(x)/h(x)-f(d_n-x)/h(d_n-x)]^2 dx.             (5)

The value +infinity is allowed. Expanding first at a common finite prime
cutoff, reflecting `x -> d_n-x`, and then using Tonelli for the nonnegative
terms, together with the fixed finite C_f, gives the exact extended identity

    N_h[f]=2integral_0^infinity f(x)^2 Rh(x)/h(x)dx
           -2 C_f.                                   (6)

Here Rh itself may initially be an extended nonnegative function; no
pointwise generator domain for h is assumed.

These definitions agree with the full original source and reflection
normalization in the published
[actual-source small-shift report](../20261015_actual_small_shift_gram/REPORT.md),
Section 1. The argument below does not use its shift inequalities.

## 2. The full test-source endpoint estimates

For every `phi in C_c^infinity(0,infinity)`,

    Q0 phi(x)=O_phi(x)                  as x -> 0,
    Q0 phi(x)=o_phi(exp(x/2))           as x -> infinity. (7)

To prove the first assertion, take x smaller than both the lower endpoint
of the support of phi and log 2. Then `F_-phi=0`. The difference

    Rphi(x)-F_+phi(x)
      =sum_n alpha_n[phi(d_n-x)-phi(d_n+x)]

has only finitely many relevant labels and is O(x). Formula (3) is also
O(x), because its kernel is smooth and odd in x away from the support.
The pole in (2) is O(x).

For the second assertion, (3) gives `G phi(x)=O(exp(-x/2))`, and
`F_+phi(x)=0` once x exceeds the support. The prime number theorem
`sum_(n<=X)Lambda(n)=X+o(X)`, applied to the two smooth compact test
weights after a logarithmic change of variables, gives

    F_-phi(x)=exp(x/2) integral_0^infinity
                           exp(-y/2)phi(y)dy+o(exp(x/2)),
    Rphi(x)=exp(x/2) integral_0^infinity
                           exp(y/2)phi(y)dy+o(exp(x/2)). (8)

Consequently the leading term of `Rphi-F_-phi` is
`2ell(phi)exp(x/2)`. The complete pole satisfies

    -4ell(phi)s(x)
       =-2ell(phi)exp(x/2)+2ell(phi)exp(-x/2),          (9)

so that this entire leading term cancels. This proves (7). No rate of
prime-number-theorem error, and no zero-location assertion, is used.
The pole cannot be omitted from this argument.

## 3. A positive-mass bound from one reflection window

Fix an interval `I=(a,b)` with `0<a<log 2<b`. For every positive h,
Tonelli's theorem and `y=d_n-x` give

    integral_I Rh(x)dx=integral_0^infinity h(y)K_I(y)dy,
    K_I(y)=sum_n alpha_n 1_(log n-y in I).             (10)

For sufficiently small positive y, the n=2 term gives
`K_I(y)>=alpha_2`. At infinity the prime number theorem, now applied to
`sum_(exp(y+a)<n<exp(y+b))Lambda(n)/sqrt(n)`, gives

    K_I(y)~2(exp(b/2)-exp(a/2))exp(y/2).               (11)

In particular, there are fixed `epsilon_0>0`, `Y>1`, and positive
constants such that a bound on (10) bounds both

    integral_0^(epsilon_0) h(y)dy,
    integral_Y^infinity exp(y/2)h(y)dy.                (12)

The remaining compact interval is handled separately; no positivity of
the full signed operator Q0 is asserted.

## 4. Closure with bounded comparison cost

**Theorem.** Let f be a strictly positive continuous function on
`(0,infinity)` with `C_f<infinity`. Suppose that h_j are strictly positive
continuous complete weak neutral sources and that

    h_j -> f uniformly on every compact subset of (0,infinity). (13)

If `sup_j N_(h_j)[f]<infinity`, then f is itself a complete weak neutral
source.

**Proof.** On the fixed interval I in Section 3, positivity of f and (13)
give `f^2/h_j>=c_I>0` for all sufficiently large j. The upper bound in
(6), together with the fixed finite C_f, therefore bounds
`integral_I Rh_j`. Equations (10)-(12) bound the wall and tail masses of
h_j. Local uniform convergence bounds their mass on the middle compact.
Thus, after discarding finitely many terms,

    sup_j [integral_0^1 h_j(y)dy
             +integral_1^infinity exp(y/2)h_j(y)dy]<infinity. (14)

The same bounds hold for f by Fatou's lemma.

Fix a compact smooth test phi. By (7) and (14), the contributions to
`integral h_j Q0 phi` from `(0,epsilon)` tend uniformly to zero as
epsilon decreases to zero. Indeed their absolute values are at most a
constant times epsilon times the first mass in (14). The contributions
from `(Y,infinity)` likewise tend uniformly to zero as Y increases,
since `sup_(y>=Y)|Q0 phi(y)|exp(-y/2)` tends to zero. These estimates
also apply to f. On `[epsilon,Y]`, local uniform convergence passes the
pairing to f. The full pairing is absolutely defined by (7) and (14),
and (4) therefore passes to the limit. This proves `Q0 f=0`.

**Corollary.** Under (13), if f is not a complete weak neutral source,
then

    N_(h_j)[f] -> infinity.                            (15)

Otherwise a bounded-cost subsequence would contradict the theorem. This
is a statement about every sequence with the stated hypotheses; it does
not assert that such a sequence exists.

## 5. Application to the same actual source

Use the original positive theta source psi and the actual-source
hypotheses recorded in Section 1 of the linked small-shift report. For
completeness, psi can be specified by

    B(x)=exp(x/2-pi exp(2x)),
    xi_0(x)=-(partial_x^3-partial_x/4)B(x),
    psi(x)=sum_(m>=1)m^(-1/2)xi_0(x+log m).

It is odd, strictly positive on the positive half-line, has a simple
zero at the wall, and has a theta tail. Write

    V=Rpsi/psi, W=V-R,
    Q_delta=Q0+2delta W, 0<delta<1.

Let `g=psi r` be the same actual source, with bounded continuous r,
`Q_delta g=0`, `Q0 psi=0`, and `Wg!=0`. These equations are understood
in the complete weak source sense inherited from the original form.
Choose any real `c>||r||_infinity` and set `f=g+c psi`. Then f is strictly
positive and comparable to psi. Moreover `C_f<infinity`, since
`C_f<=C<psi,Rpsi>` and `<psi,Rpsi><infinity` by the theta tail, while

    Q0 f=-2delta Wg!=0.                                (16)

The corollary applies: every locally uniform approximation of this f by
positive complete weak neutral sources has comparison cost
`N_(h_j)[f]` tending to infinity.

This does not change the actual source, remove any prime powers, or
replace the full pole. It distinguishes local neutral approximation
from approximation with controlled global reflected-prime ratios. It
neither excludes arbitrary ground optimization nor proves a reverse
bound for the actual damped prime correlation, and it does not prove
the Riemann hypothesis.
