# Addendum: descent at lower-comparable weak neutral grounds

This addendum strengthens the ground class in the
[descent report](REPORT.md). It does not change that report's finite-jet
boundary theorem or its admissibility qualifications for the pole floor.
The new argument uses only estimates on smooth theta seeds, not pointwise
regularity or a prime-number asymptotic for the variable ground.

## 1. Statement and complete conventions

Use the complete operators, including every prime power, from Section 1
of the report. In particular,

    Rf(x)=sum_(log n>x) Lambda(n)/sqrt(n) f(log n-x),
    U(f)=integral_0^infinity exp(x/2) f(x)dx,
    N_h[e]=2 integral (Rh)e^2/h -2<e,Re>.

Weak neutrality means the absolutely defined full equation

    integral h Q0 phi=0, every phi in C_c^infinity(0,infinity),

where Q0 retains Gamma, both prime orientations, reflection and the pole.
Let E be the finite real span of the even derivatives of the original
positive theta source psi. Every member of E is completely neutral.

**Theorem.** Let e be a measurable real source, nonzero modulo equality
almost everywhere, with

    |e|<=C psi,             e/psi ->0 at infinity.       (A1)

Let h be a measurable complete weak neutral source such that, almost
everywhere,

    h>=c psi for some c>0,        U(h)<infinity.         (A2)

Then N_h[e] is finite. There are finite neutral jets n,b in E, with b
positive, for which

    h_t=h+t n+t^2 b >=3h/4                            (A3)

for every real t, and

    d N_(h_t)[e]/dt at t=0 <0.                        (A4)

Consequently N_(h_t)[e]<N_h[e] for sufficiently small positive t.
Every h_t is a positive complete weak neutral source with finite U(h_t)
and finite reflected cost. No smoothness of h or Rh is required.

The tail limits may equivalently be interpreted essentially; changing
representatives on null sets changes none of the conclusions.

## 2. Full-prime domination and finite cost

The elementary complete Chebyshev bound, applied in unit logarithmic
bins, implies the following useful estimate. If a nonnegative seed a is
bounded on compacts and

    sum_(j>=0) exp(j/2) sup_(j<=x<=j+1) a(x)<infinity,

then

    Ra(x)<=C_a exp(x/2).                              (A5)

Indeed the sum of Lambda(n)/sqrt(n) over a bin
exp(x+j)<n<=exp(x+j+1) is at most C exp((x+j)/2).
This includes all prime powers and requires no prime truncation in the
conclusion. It applies to absolute finite theta jets, to compact interval
indicators, and to the compact-strip theta envelopes used below.

Reflection symmetry and Tonelli give

    integral a Rh=integral h Ra.                      (A6)

Thus Rh is locally integrable, including at the wall, by taking a to be
a compact interval indicator. Put

    r_h=e/h,                 q=e^2/h.

The ratio r_h is bounded and tends to zero. Also q<=C_1 psi, so U(q) is
finite and strictly positive. Equations (A5)-(A6) give

    integral q Rh=integral h Rq<=C_2 U(h)<infinity.    (A7)

The fixed cross term is absolutely finite because |e|<=C psi and
Rpsi<=C_3 exp(x/2). This proves finite N_h[e]. It also justifies the
nonnegative reflected-edge representation by the same common-cut and
monotone-convergence argument as in the report.

For every finite jet v, both rows of the linear functional

    L(v)=2 integral q Rv-2 integral r_h^2 Rh v         (A8)

are absolutely finite. The first follows from U(q)<infinity and (A5).
For the second, boundedness of r_h and (A6) give

    integral r_h^2 Rh |v|<=||r_h||_infinity^2
                              integral h R|v|<infinity.  (A9)

## 3. A generating function without a variable-ground asymptotic

Use the HALF-average translations of the full odd theta source,

    S_z psi(x)=[psi(x+z)+psi_o(x-z)]/2.

They are only analytic generating tests here, not asserted to be
admissible large-shift variations in the original energy space.
For each compact subset K of |Im z|<pi/4, its envelope

    E_K(x)=sup_(z in K)|S_z psi(x)|

satisfies (A5). Uniform theta decay proves the bin condition. Hence

    integral q R E_K<infinity,
    integral r_h^2 Rh E_K<=C_K U(h)<infinity.          (A10)

These are complete-row analytic majorants. Dominated holomorphic
integration makes L(S_z psi) holomorphic throughout the strip, and its
Taylor coefficients at zero are L(psi^(2j))/(2j)!. No separate domain or
regularity for Rh has been used.

For real z tending to positive infinity, the smooth-seed complete PNT
calculation in Section 4 of the report gives

    exp(-z/2)R(S_z psi)(x)->exp(x/2)/8,
    exp(-z/2)R|S_z psi|(x)<=C_4 exp(x/2),             (A11)

with the second bound uniform in z>=1. Its factor 1/8 is ell(psi), and
uses the half-average convention. The bound also follows from shifted
unit-bin estimates. PNT is applied only to the smooth translated theta
seed, never to h or q. Dominated convergence yields

    exp(-z/2) 2 integral q R(S_z psi)->U(q)/4.        (A12)

The other row is smaller. Fix eta>0 and choose M so that |r_h|<=eta for
x>M. Symmetry and positivity, followed by (A11), imply

    integral_(x>M) r_h^2 Rh |S_z psi|
      <=eta^2 integral Rh |S_z psi|
      =eta^2 integral h R|S_z psi|
      <=C_4 eta^2 exp(z/2) U(h).                     (A13)

On 0<x<=M, Rh is integrable and the translated theta seed is uniformly
theta-small as z tends to infinity. Boundedness of r_h therefore makes
this compact contribution o(exp(z/2)). Letting eta decrease to zero gives

    integral r_h^2 Rh S_z psi=o(exp(z/2)).            (A14)

Together (A12)-(A14) show

    L(S_z psi)~[U(q)/4] exp(z/2),                    (A15)

with a strictly positive coefficient. Thus not all finite-jet Taylor
coefficients can vanish. Choose n in E with L(n)<0, reversing its sign
if necessary.

## 4. Positive completion and actual differentiation

The finite-jet theta asymptotics recalled in the report allow a positive
finite neutral jet b satisfying

    b>=n^2/(c psi).                                  (A16)

To construct it, choose an even jet whose positive leading polynomial
degree exceeds that of (n/psi)^2, multiply it by a positive constant to
pay the tail, and add a sufficiently large multiple of psi to pay the
remaining compact interval. All jet ratios extend continuously at the
wall. One may add another positive multiple of psi to make b positive.

Writing A=n/h and B=b/h, (A2) and (A16) give B>=A^2. Therefore

    1+tA+t^2B >=1+tA+t^2A^2 >=3/4,

which proves (A3). The weak-neutral equation and U integrability are
preserved by the finite sum. Section 2 applies to h_t as well.

For clarity, the derivative is a dominated integral, not merely formal.
The difference quotient of the diagonal cost divided by 2 is

    q [Rn+t Rb-(A+tB)Rh]/[1+tA+t^2B].                (A17)

For |t|<=t_0 its absolute value is bounded by a fixed multiple of

    q(R|n|+t_0 Rb)+r_h^2 Rh(|n|+t_0 b).

This is integrable by (A5), U(q)<infinity and (A9). The fixed reflected
cross term does not change. Dominated convergence in (A17) gives (A8),
and the chosen sign of n gives (A4).

## 5. Scope

The conclusion excludes stationarity under these legal finite-jet
variations at every lower-comparable ground (A2), not only at finite-jet
grounds. It does not cover general boundary grounds lacking a global
positive lower comparison with psi. It supplies neither compactness nor
attainment across all grounds, and it does not transfer the original
actual-state equation or the original numerical threshold to a changed
ground. The separate pole floor remains conditional on its stated full
ground identity. No original prime-correlation upper bound or RH proof
follows from this addendum.
