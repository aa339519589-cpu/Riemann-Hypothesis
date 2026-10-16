# Finite-jet neutral-ground descent and a fixed-coset pole floor

Two complementary facts hold for the complete original source form. A fixed
plateau-zero source has a strict reflected-cost descent at every admissible
nonnegative finite-theta-jet ground, including grounds with interior zeros.
On the other hand, the complete pole gives a positive, ground-independent
energy floor for each fixed nonneutral source coset. Within the admissible
ground-identity class below, this floor prevents the corresponding quotient
from tending to one. The descent does not prove RH.
Neither statement supplies the unresolved actual prime-correlation upper
bound. No compactness or existence of an optimizing ground is asserted.

## 1. Complete conventions and theta inputs

All sources and pairings are real and on `(0,infinity)`. Put

    s(x)=sinh(x/2), ell(f)=integral s(x)f(x)dx,
    U(f)=integral exp(x/2)f(x)dx,
    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    kappa(t)=exp(-t/2)/(1-exp(-2t)).

Every Mangoldt sum includes every prime power. Define

    F_+f(x)=sum_n alpha_n f(x+d_n),
    F_-f(x)=sum_(d_n<x) alpha_n f(x-d_n),
    Rf(x)=sum_(d_n>x) alpha_n f(d_n-x).

For a compact smooth half-line test phi, let phi_o be its odd extension,
and let G phi be the positive-half restriction of the Fourier multiplier
with symbol `Re digamma(1/4+it/2)-log pi` applied to phi_o. The complete
source operator is

    Q0 phi/2=G phi-F_+phi-F_-phi+Rphi-4ell(phi)s.       (1)

Thus the quadratic pole is exactly `-8ell(f)^2`. A complete weak neutral
source h satisfies the absolutely defined pairing

    integral h Q0 phi=0, every phi in C_c^infinity(0,infinity). (2)

The full Gamma term, both prime orientations, reflection and pole in (1)
are retained throughout.

Use the original theta source

    B(x)=exp(x/2-pi exp(2x)),
    xi=-(partial_x^3-partial_x/4)B,
    psi(x)=sum_(m>=1)m^(-1/2)xi(x+log m).

Its full-line continuation is odd and holomorphic in `|Im x|<pi/4`.
It is positive on the positive half-line, has a simple wall zero, and
`ell(psi)=1/8`. All finite even jets `psi^(2j)` are complete neutral
sources. Let

    E=span_R{psi^(2j): j>=0},                          (3)

where each member is a finite sum. The leading theta term shows that
`psi^(2j)/psi` has a positive leading polynomial term of degree `2j` in
`pi exp(2x)`. These facts follow from the complete theta identity and
commutation of even derivatives, including integration by parts in the
pole moment. They are recorded in the
[actual physical range report](../20261015_old_actual_physical_range/REPORT.md),
Sections 0-1. The source conventions and theta bounds are also in the
[small-shift report](../20261015_actual_small_shift_gram/REPORT.md), Section 1.
No large-shift original-P domain statement from that report is used here.

For a nonnegative, nonzero h and a fixed real f with
`integral |f| R|f|<infinity`, define the extended reflected cost by

    N_h[f]=2 integral (Rh) f^2/h -2<f,Rf>.             (4)

Zeros of h are treated by the extended integral; isolated zero points do
not affect it. Expansion at a common finite prime cutoff identifies (4)
with the nonnegative reflected-edge square

    sum_n alpha_n integral_0^(d_n) h(x)h(d_n-x)
       [f(x)/h(x)-f(d_n-x)/h(d_n-x)]^2 dx.             (5)

The extension follows by monotone convergence for the diagonal term and
absolute convergence of the fixed cross term. The cost is invariant under
positive rescaling of h. It is not invariant under adding an arbitrary
neutral source to f after h has changed.

## 2. A zero-preserving finite-jet variation

Fix a measurable real source e, nonzero modulo equality almost everywhere,
such that

    |e(x)|<=C psi(x),  e(x)/psi(x)->0 as x->infinity.   (6)

Let h0 be a nonzero nonnegative member of E and suppose `N_h0[e]<infinity`.
Its highest nonzero even jet has a positive leading theta-polynomial term,
because h0 is nonnegative. Hence h0 is eventually positive. Real analyticity
through the wall excludes finite accumulation of zeros. Thus there are
only finitely many interior zeros, each of finite even multiplicity, and
a finite odd wall order.

Let J collect derivative evaluations through multiplicity minus one at
all these zeros, including the wall. A tangent direction is an n in E
with `Jn=0`. The quotient n/h0 extends continuously across every zero,
and has at most polynomial growth in exp(2x) at infinity.

For every such n there is a b in E satisfying

    Jb=0,  b/h0 >= (n/h0)^2+1.                        (7)

To construct it, choose a fixed finite-jet interpolation basis for the
finite-dimensional image J(E). Take an even jet of sufficiently high
order and subtract its interpolation in this basis. The resulting b0
lies in ker J, and its positive leading degree, after division by h0,
strictly exceeds that needed to dominate `(n/h0)^2`. Both ratios extend
across all zeros. Adding a sufficiently large multiple of h0 then gives
(7). In particular b has the same zero orders as h0.

The neutral path

    h_t=h0+t n+t^2 b

obeys, away from the zeros and hence by continuation,

    h_t/h0 >= (t n/h0+1/2)^2+3/4+t^2.                (8)

It is nonnegative, preserves the same zeros, and has finite reflected
cost for small real t. It may be normalized to fixed ell(h_t) without
changing that cost.

Put `q=e^2/h0`. Positivity of Rh0 on every compact and the full PNT
asymptotic `Rh0(x)~U(h0)exp(x/2)` imply

    q is locally integrable, U(q)<infinity,
    integral q Rh0<infinity.                          (9)

The positivity is strict because h0 is eventually positive and the full
reflection sum has arbitrarily large prime-power labels. The theta tail
also pays all polynomial factors needed below. Differentiating (4) along
(8) gives

    L(n):=d/dt N_(h_t)[e] at t=0
        =2 integral q Rn-2 integral (n/h0)q Rh0.       (10)

This differentiation is dominated on zero collars by `q Rh0`, using
continuous quotients, and on the tail by theta decay times polynomials.
The zero-preserving condition on b is important: lifting a zero by a
positive `t^2 b` without it can introduce a nonsmooth first-order change
of the singular cost.

## 3. The repaired generating function

We show that (10) cannot vanish on every tangent direction. Use the HALF
symmetric translation

    S_z psi(x)=[psi(x+z)+psi_o(x-z)]/2.                (11)

Thus `S_0 psi=psi` and its Taylor coefficients are
`psi^(2j)/(2j)!`. This convention differs by a factor two from the full
translation sum in the linked small-shift report.

The finite-dimensional image J(E) is closed. All Taylor coefficients of
`J(S_z psi)` lie in that image. Analyticity and continuation in the
connected theta strip therefore put `J(S_z psi)` in J(E) for every z in
the strip. Fix a linear right inverse on this image, represented by
finite jets u_i, and define

    n_z=S_z psi-sum_i c_i(z)u_i,  Jn_z=0.              (12)

The coefficients are holomorphic; every Taylor coefficient of n_z at
zero is a tangent finite jet. The corrected translations n_z are only
**generating tests** for the following functional. They are not asserted
to be admissible large-shift positive-ground variations.

Define the complete expression

    L(n_z)=2 integral q Rn_z
           -2 integral (n_z/h0)q Rh0.                 (13)

It is holomorphic in `|Im z|<pi/4`. Here is the required domination at the
zeros, rather than a formal split into potentially divergent terms. If
x_i has multiplicity m_i, the first m_i x-jets of n_z vanish there.
Taylor's integral remainder divides the WHOLE n_z by `(x-x_i)^m_i`,
uniformly and holomorphically for z in each compact substrip.
Since `h0/(x-x_i)^m_i` is nonzero locally, n_z/h0 is uniformly bounded
there, and (9) dominates the second row. The same argument includes the
wall. At infinity, `(e/h0)^2 Rh0` is bounded by a polynomial times
exp(x/2), while complex translated theta functions and their derivatives
retain theta decay on compact substrips. The first row follows from
`U(q)<infinity` and the complete prime-bin bound

    |R n_z(x)|<=C_K exp(x/2),  z in a compact substrip K. (14)

This bound uses the Chebyshev estimate for the full Mangoldt sum and the
uniform theta envelopes. It does not assume a separate local domain for
`W_h0 q=(Rh0/h0)q-Rq`, which can be singular at the zeros.

If L vanished on all tangent finite jets, differentiation under these
bounds would make every Taylor coefficient of (13) zero. Holomorphy
would then make (13) identically zero throughout the strip.

## 4. Its full-prime asymptotic and strict descent

For real z tending to infinity, the full PNT on the smooth translated
theta seed gives

    exp(-z/2) R(S_z psi)(x) -> exp(x/2)/8              (15)

at each fixed x, with absolute majorant `C exp(x/2)`. For precision, the
shifted odd packet in (11) has limiting moment

    (1/2) integral_R exp(y/2)psi_o(y)dy
       =ell(psi)=1/8.

One first truncates its theta tails, applies PNT to the smooth compact
weight, and then removes the truncation using the Chebyshev prime-bin
majorant. The other packet in (11) is negligible. Thus (9) and dominated
convergence give

    exp(-z/2) 2 integral q R(S_z psi) -> U(q)/4.       (16)

No pointwise PNT statement for the possibly singular q is used.

All c_i(z) in (12), and all fixed x-derivatives of S_z psi on a compact
x-interval, tend to zero theta-fast. Their contribution to the first row
is negligible. On fixed zero collars, Taylor division therefore makes
n_z/h0 uniformly theta-small, so the second row is negligible by (9).
Away from those collars on a fixed compact it is negligible in the same
way. Finally, on the tail

    (e/h0)^2 Rh0=o(exp(x/2)),                          (17)

because (6) and the positive polynomial tail of h0/psi give e/h0->0.
The absolute translated-theta moment is O(exp(z/2)), so (17), followed
by an arbitrarily small tail bound, makes the remaining second row
o(exp(z/2)). All interpolation corrections have the same negligible
bound. Consequently

    L(n_z)~[U(q)/4]exp(z/2),  U(q)>0.                 (18)

This contradicts its proposed identical vanishing.

**Finite-jet descent theorem.** Under (6), every nonzero nonnegative
h0 in E with finite N_h0[e] admits a finite tangent n and a zero-preserving
neutral parabolic path (8) whose cost has a nonzero derivative. Choosing
one sign of sufficiently small t strictly lowers N_(h_t)[e]. Thus no
such finite-jet ground is stationary against all finite-jet variations,
even after normalizing its positive mass.

For the SAME actual source `g=psi r`, take
`e=g-r_infinity psi`. The established bounded ratio and plateau give
(6); see the [actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md),
Section 1, which also gives `r_infinity=U(g)/U(psi)`. For a nonconstant actual ratio, e is nonzero. This application does
not transfer the original actual-null equation to the changed ground.

## 5. The independent fixed-coset pole floor

This assertion uses a separate, explicit admissibility hypothesis, not
an automatic realization for every weak neutral source. Let h>0 satisfy
(2), `0<ell(h)<infinity`, and suppose a real f satisfies `integral s|f|<infinity` and has the
complete ground identity

    P_h[f]=q0[f]+N_h[f],                              (19)

where P_h is the sum of the nonnegative Gamma, forward-prime and pole
rows and contains its full nonnegative pole block

    E_p(h,f)=8{ell(h)ell(f^2/h)-ell(f)^2}.             (20)

All expressions are taken in their admissible complete form domain.
An infinite value of (20) makes the following lower bound immediate.
The original positive psi-ground and legitimate complete ground
transforms have precisely this pole normalization; (19) is not inferred
merely from weak neutrality for an arbitrary h.

For every compact smooth phi define

    C_phi=||Q0 phi/s||_infinity<infinity.              (21)

The endpoint estimates proving (21), with the complete pole included,
are

    Q0 phi(x)=O_phi(x) at zero,
    Q0 phi(x)=o_phi(exp(x/2)) at infinity.

They are proved in the
[positive neutral approximation report](../20261015_positive_neutral_approximation_cost/REPORT.md),
Section 2. The tail estimate uses cancellation of the leading full
reflected-minus-past prime row against the full pole. On the intervening
compact, the smooth test-source expression is bounded.

Set `c=ell(f)/ell(h)`. Neutrality and weighted Cauchy give

    |<f,Q0 phi>|=|<f-c h,Q0 phi>|
       <=C_phi integral s|f-c h|
       <=C_phi [ell(h) integral s(f-c h)^2/h]^(1/2)
       =C_phi [E_p(h,f)/8]^(1/2).                    (22)

Hence, whenever C_phi>0,

    P_h[f]>=E_p(h,f)>=8|<f,Q0 phi>|^2/C_phi^2.        (23)

The numerator, and q0[f], remain unchanged under legal additions of a
complete neutral source to f. Thus the lower bound depends only on the
fixed neutral coset, although P_h and N_h themselves need not be invariant
under those additions. No uniform constant over moving nonneutral
cosets is claimed.

If q0[f]<0 and phi is a compact witness with `<f,Q0 phi>!=0`, put
`A=-q0[f]>0` and `c_phi=8|<f,Q0 phi>|^2/C_phi^2>0`. Equations (19) and
(23) yield

    N_h[f]>=A+c_phi,
    A/N_h[f]<=A/(A+c_phi)<1.                          (24)

Such a witness exists for the actual nonneutral source because
`Q0 g=-2delta Wg!=0`; a legal neutral gauge does not remove it.
For the particular sign-changing e, the simpler Cauchy bound in (20)
also gives `P_h[e]>=32ell(e_+)ell(e_-)>0`. Its sign-changing property
follows from the actual plateau mean `U(e)=0` and e!=0.

## 6. What is and is not concluded

The descent changes the reference ground while keeping the source fixed.
The floor is an independent full-pole estimate for a fixed nonneutral
coset. On the admissible positive-ground class of Section 5, the floor excludes
the inference that repeated finite-jet descent must push the quotient to
one. The boundary descent theorem does not itself assign the ground
identity (19) to a singular boundary ground.

Even if a degree-bounded normalized slice has a minimizer, the theorem
only finds an improving direction that can have higher degree. A sequence
of such improvements has no proved compact positive-neutral limit or
attained optimum across all degrees. Limits with unbounded jet degree,
more complicated zero sets, or losses of the stated admissibility remain
unclassified. The existing local-uniform neutral approximation theorem
does not supply that missing compactness.

No independent upper bound for the complete actual damped prime
correlation, no threshold-one contraction, no exclusion of the actual
source, and no proof of the Riemann hypothesis follows.
