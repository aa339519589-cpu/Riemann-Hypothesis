# Exact reflection of the future arithmetic semigroup and its wall coefficient

This note keeps the theta functional equation, the full positive finite-time
arithmetic kernel, and the polynomial ladder together. The reflected kernel
is computed before any backward prime row is expanded. It is a source-domain
interface, not a sign theorem for the original odd Weil form.

Use [the future Markov semigroup](SEMIGROUP_AND_HIDDEN_LIFT.md).
Throughout z=pi exp(2x), t>0, a=t/2, and

    theta(z)=sum_n exp(-n^2z),
    J_t(k)=product_(p|k)(1-p^(-t)).

For a physical source h(x), write h(x)=exp(x/2)H(z), and set

    A_t H(z)=1/Gamma(a) sum_k J_t(k)
                 integral_0^infinity v^(a-1)H(k^2z+v)dv,
    S_t h(x)=exp(x/2)A_t H(z).

This is the source, rather than ratio, version of the positive future
semigroup. On the controlled core S_t=exp(-tD), where
D=L_+-F_+-X-C0/2 in the conventions of the future intertwining.

## 1. The exact reflected kernel

Physical reflection J h(x)=h(-x) acts on H by

    R H(z)=sqrt(pi/z) H(pi^2/z).                        (1)

A direct change of variable y=pi^2/(k^2 pi^2/z+v) gives

    R A_t R H(z)
      =pi^t z^((1-t)/2)/Gamma(t/2)
         sum_k J_t(k) integral_0^(z/k^2)
             (z-k^2y)^(t/2-1)y^(-(t+1)/2)H(y)dy.      (2)

Every factor in (2) is retained. For example, no free backward row or
uncompensated prime identity term has been extracted.

The formula is absolutely convergent for every fixed z>0 when H is
continuous and has the two-sided theta bounds

    |H(y)|<=C y^A exp(-c y) at infinity,
    |H(y)|<=C y^(-B)exp(-c/y) at zero.                  (3)

The endpoint y=z/k^2 is integrable because t/2>0, and the small-y bound
pays the complete sum over k. Actual bounded-ratio odd sources satisfy
(3): their positive wing is theta-decaying and their negative wing is its
odd reflection. Hence (2) is available on those sources without assuming
that a separate backward Markov row is bounded in the original metric.

## 2. The raw theta pole cannot be reflected through the positive kernel

The theta functional equation is exactly

    theta(z)=sqrt(pi/z)theta(pi^2/z)
                         +(sqrt(pi/z)-1)/2.

Thus for Theta(x)=exp(x/2)theta(z) and s(x)=sinh(x/2),

    J Theta=Theta+s.                                  (4)

In H coordinates R theta=theta+(1-sqrt(pi/z))/2, which tends to 1/2 as
z tends to infinity. Consequently A_t(R theta) diverges for EVERY t>0.
Equivalently, the reflected ratio operator R_Theta P_t R_Theta is not a
finite Markov operator on the constant function, where

    R_Theta f(z)=[Theta(-x)/Theta(x)] f(pi^2/z).

This is an exact domain fact, not a deletion of a pole. Applying the
polynomial theta ladder before reflection removes the offending raw tail;
(2) is then finite, as (3) shows.

## 3. The exact scalar coefficient of the future wall leakage

For every continuous H satisfying (3), define the entire Mellin moment

    M_h(t)=integral_0^infinity z^((t-1)/2)H(z)dz
          =2 pi^((t+1)/2) integral_R exp((t+1/2)x)h(x)dx.

For each fixed t>0,

    S_t h(x)=c_t(h)exp(-x/2)+o(exp(-x/2)), x->-infinity,
    c_t(h)=M_h(t)/[2 Gamma((t+1)/2) zeta(1+t)].         (5)

Only zeta at the real point 1+t>1 occurs. There is no inverse-zeta crossing
of the critical line in (5).

To prove (5), the elementary divisor representation of J_t gives

    sum_(k<=X)J_t(k)=X/zeta(1+t)+o(X).                  (6)

Indeed J_t=1*(mu(n)n^(-t)), the floor-function error is
O(sum_(d<=X)d^(-t))=o(X), and the absolutely convergent main coefficient
sum mu(d)d^(-1-t) equals 1/zeta(1+t). Also 0<=J_t<=1.

Put F(w)=Gamma(a)^(-1)integral_0^infinity v^(a-1)H(w+v)dv.
It is continuous, and F(u^2) is integrable with a Gaussian tail. Equation
(6), first on a compact u-window and then using 0<=J_t<=1 and this tail,
gives

    sqrt(z) A_t H(z)
       -> [1/zeta(1+t)] integral_0^infinity F(u^2)du.

The beta integral evaluates the last integral as

    sqrt(pi)/[2 Gamma(a+1/2)]
          integral_0^infinity y^(a-1/2)H(y)dy.

Since exp(x/2)/sqrt(z)=exp(-x/2)/sqrt(pi), (5) follows.
All signed exchanges are dominated by the same calculation with |H|.

For an odd pole-centered source, integral_R exp(x/2)h(x)dx=0, so M_h(0)=0.
The analytic scalar coefficient in (5) is consequently O(t^2), with the
precise expansion below (its quadratic coefficient may also vanish):

    c_t(h)=t^2 M_h'(0)/(2sqrt(pi))+O(t^3).              (7)

This cancellation does not make c_t identically zero for a nonzero source.
Indeed M_h is an entire transform of a two-sided theta-decaying source;
if it vanished on an interval of t, transform uniqueness would give h=0.
Thus centering removes the first infinitesimal wall coefficient but does
not by itself put the finite-time future evolution back in the original
two-sided theta source class.

## 4. Exact polynomial ladder and reflection checks

Let q(z)=4z^2-6z and c(z)=8z^3-30z^2+15z. The additive gamma semigroup
satisfies

    G_t q=q+4tz+t^2-t,
    G_t c=c+t(3q+1/2)+t^2(6z-3/2)+t^3.

Since Phi/Theta=Tq, psi/Theta=Tc, and
Theta'=Theta/2-2exp(x/2)sum_n n^2z exp(-n^2z), intertwining gives

    S_t Theta=Theta,
    S_t Theta'=Theta'-tTheta,
    S_t Phi=Phi-2tTheta'+t^2Theta,
    S_t psi=psi+t(3Phi+Theta/2)-3t^2Theta'+t^3Theta.      (8)

These equalities hold for fixed t>0 on the full log line; polynomial growth
in the latent variable is paid by the Gaussian and gamma moments.

The evenness of Phi and oddness of psi, together with (4), imply

    (S_t+J S_t J)Phi
       =2Phi+2t s'+2t^2Theta+t^2s,
    (S_t+J S_t J)psi
       =2psi-(t/2)s-6t^2Theta'-3t^2s'-t^3s.            (9)

The first derivatives at t=0 recover the complete source identities

    (D+JDJ)Phi=-cosh(x/2),
    (D+JDJ)psi=sinh(x/2)/2.

In particular the pole coefficients are not guessed from a positive future
kernel; they arise from the exact theta reflection before differentiation.
The higher-time Theta and Theta' terms in (9) remain and must not be treated
as if they were the same finite pole correction.

As independent normalization checks, the Mellin formula (5) gives exactly

    c_t(Phi)=t(t+1)/2,
    c_t(psi)=t(t+1)(2t+1)/4,

which also follow from (8) and the left-tail asymptotic
Theta(x)~exp(-x/2)/2, Theta'(x)~ -exp(-x/2)/4.

## 5. Remaining signed problem

The reflected formula (2) and the wall coefficient (5) are legal before
forming any backward prime expansion. They expose the precise boundary
that a finite-time positivity or original-metric comparison must retain.
The positive future semigroup alone neither controls the original adjoint
metric defect nor signs the resulting odd Gamma/prime/pole joint. Those
are the unresolved requirements; no positivity of the full form is asserted.
