# A globally positive reflected row and same-source current storage

## Verified result and exact scope

Let psi=-Phi' be the original odd theta source, positive on x>0. Use

    kappa(t)=exp(-t/2)/(1-exp(-2t)),
    Hpsi(x)=int_0^infinity kappa(x+y)psi(y)dy,
    L(x)=sum_(log n>x) Lambda(n)/sqrt(n) psi(log n-x).

The row L is REFLECTED ONLY. It is not enlarged by the backward row. Then

    R(x):=Hpsi(x)+L(x)-sinh(x/2)/2 >1/16,    x>=0.       (1)

For the SAME actual source g=psi r, take its proved plateau-zero null
representative u=r-c_infinity. Let J_u(x) be the finite positive variance
of the complete homogeneous Gamma-plus-prime ray current, defined below.
With K0=3Phi+Theta/2, the signed storage functional satisfies

    S[u]:=4 int_0^infinity psi(x)[K0(x)-x psi(x)]J_u(x)dx
       =2 int_0^infinity psi(x)^2 Gamma_psi[u](x)dx
          +2 int_0^infinity psi(x)R(x)J_u(x)dx
       >=2 int psi^2 Gamma_psi[u]+(1/8)int psi J_u>=0.  (2)

The coefficient K0-x psi is positive near zero and negative at infinity.
Thus (2) is a genuine signed, nonlocal storage statement on the actual
current field, not a pointwise replacement of that coefficient by its
absolute value.

This is NOT positivity of the full original form. Its remaining reflected
and coherent current-edge comparison is stated explicitly in Section 4.

## 1. Complete analytic tail

The [analytic tail proof](ANALYTIC_TAIL.md) proves, with every prime power
retained,

    L(x)>(127/500)exp(x/2),                exp(x)>=101. (3)

It uses the unconditional Rosser--Schoenfeld bounds
0.84X<sum_(n<=X)Lambda(n)<1.04X for X>=101, taken from Theorems 10 and 12
of their 1962 paper, printed page 71. The proof links the primary paper and
states the precise table entry and thresholds.

For F(t)=exp(-t/2)psi(t), Stieltjes integration by parts gives

    exp(-x/2)L(x)>=0.84 J-0.20 I_plus,
    J=int exp(t/2)psi(t)dt>1,
    I_plus=int exp(t)max(F'(t),0)dt<2.93.

The last two estimates are proved from explicit theta polynomials. The
[exact rational checker](check_reflected_row_tail.py) certifies their
constants; it does not replace the cited arithmetic theorem by finite data.
Equation (3) implies

    R(x)>exp(x/2)/250+exp(-x/2)/4
           >=1/(5 sqrt(10))>1/16.                   (4)

The last comparison is the exact rational inequality 256>250.

## 2. A rigorous compact certificate, not a finite-prime surrogate

The [interval checker](certify_reflected_storage_row.py) proves R(x)>1/16
on every one of the 500 closed cells [j/100,(j+1)/100], 0<=j<500.
Its [reproducible result](reflected_storage_row_certificate.json) gives
minimum certified margin greater than 0.61910821304956. Since log(101)<5,
this overlaps (4) and proves (1) for all x>=0.

Here is the complete enclosure argument. First,

    Hpsi(x)>=exp(-x/2)V_psi,
    V_psi=int exp(-y/2)psi(y)dy
       >=exp(-1/4)[Phi(0)-Phi(1/2)]>3/5.              (5)

For Phi(0), retain its first positive theta term. At y=1/2 let z=pi e>8.
The complete tail obeys

    Phi(1/2)<=exp(1/4){(4z^2-6z)exp(-z)
                                      +128z^2 exp(-4z)}.

Indeed the ratio of consecutive m^4 exp(-m^2 z) terms, m>=2, is at most
(3/2)^4 exp(-5z)<1/2. The interval checker encloses the lower bound in (5)
above 0.64724302186036, then uses the weaker exact constant 3/5.

Write c(w)=w(8w^2-30w+15). For y>=0,

    psi(y)>=max{0, exp(y/2)c(pi exp(2y))exp(-pi exp(2y))}. (6)

This follows from positivity of the complete psi and positivity of every
omitted derivative-theta term with integer label m>=2, since its argument
is at least 4pi>12. No signed first term near zero is silently declared
positive.

For each cell, retain only genuine prime powers n<=256 whose log n is
strictly above the whole cell. Bound their psi(log n-x) by the positive
interval lower bound from (6); if that interval bound is not positive,
omit the term. A term crossing the moving reflection boundary is also
omitted. Every omission is favorable because the full reflected row is a
sum of positive terms. This leaves 70 available genuine prime powers,
with Lambda(p^k)=log p exactly, not an all-integer replacement.

The checker combines this lower row with (3/5)exp(-x/2) and subtracts the
interval upper bound of sinh(x/2)/2. All cell endpoints are exact rational
intervals, and all pi, exponential, logarithm and square-root evaluations
use outward interval arithmetic at 60 decimal digits. The whole interval,
not merely its endpoints or a sample grid, is enclosed.

Run from this folder:

    python check_reflected_row_tail.py
    python certify_reflected_storage_row.py

Only Python's standard library and mpmath are required. No network access
or external prime table is needed to reproduce the certificates.

## 3. Same actual current and signed integration

The [forward-ray theorem](FORWARD_RAYS.md) constructs the genuine
homogeneous process with positive generator

    G_psi u(x)=int kappa(h)psi(x+h)/psi(x)[u(x)-u(x+h)]dh
       +sum_n Lambda(n)/sqrt(n) psi(x+log n)/psi(x)
                                      [u(x)-u(x+log n)].

Its process generator is -G_psi. It starts at x>0, is nonexplosive, and
escapes to infinity. It is not the normalized finite-time source filter.
For the actual u in H^s, 1/2<s<1, the complete signed current has an
ordinary almost-sure and L2 limit I_x with

    E I_x=u(x),  Var(I_x)=J_u(x)
       =E_x int_0^infinity Gamma_psi[u](X_t)dt
       <=C_s(1+1/x)||u||_(H^s)^2.

The proof uses physical z=pi exp(2x) unit-block occupation and the original
log-coordinate Sobolev norm, with their weights kept distinct.

The [complete current-form theorem](CURRENT_FORM.md) justifies the adjoint
pairing, including both origin and infinity cutoffs:

    int psi^2 Gamma_psi[u]=int b J_u,
    b=G_psi*(psi^2)
      =psi[sinh(x/2)/2+2K0-2x psi-Hpsi-L].            (7)

Combining (7) with the definition of S gives the equality in (2).
All its integrals are finite by the current estimate and theta tails.
Finally apply the proved full row inequality (1). This proves the signed
storage bound, with no independent or arbitrary replacement for J_u.

## 4. Full form and the exact budget that remains

Take two independent laws of the COMPLETE current I_x,I_y solely as an
exact reference coupling, and set

    E_ray(x,y)=E|I_x-I_y|^2
                    =[u(x)-u(y)]^2+J_u(x)+J_u(y).

Let H_ray integrate this kernel against kappa(x+y)psi(x)psi(y)dxdy.
Let N_ray integrate it against the exact reflected prime measure
sum_n alpha_n psi(x)psi(d_n-x)dx on 0<x<d_n.
Let P_ray integrate it against
4sinh(x/2)psi(x)sinh(y/2)psi(y)dxdy.
Every term is finite and nonnegative. The complete identity is

    h[g]=P_ray-H_ray-N_ray+S[u].                      (8)

For the actual top source, with Q_delta=h+delta N,

    0=Q_delta[g]
      =P_ray-H_ray-(1-delta)N_ray+S[u]
                               -2delta int psi L J_u. (9)

The now-positive storage is not a new free surplus to spend twice.
The added variance cost in P_ray-H_ray-N_ray is exactly

    -2 int psi R J_u.

It cancels the corresponding positive term in (2) when the edge lifts are
returned to the original unlifted forms. Therefore (1)--(2) establish a
verified signed component, while (8)--(9) still require a genuinely joint
edge-current comparison or a coherent covariance mechanism. No RH claim,
full-form positivity claim, or removal of the original pole is made.


## 5. Stronger storage through the entire actual comparison depth

The [actual-depth extension](ACTUAL_DEPTH_STORAGE.md) proves the stronger
row Hpsi+(1/2)L-sinh(x/2)/2>1/16 for all x>=0. It uses the same primary
paper's distinct .91/349 table entry and a separate rigorous certificate
on [0,6], with 198 genuine prime powers through 1024. Its minimum certified
compact margin exceeds 0.56369057955513. The original full-L proof and
checker remain independently reproducible.

Consequently the ENTIRE delta-adjusted storage in (9) satisfies

    S_delta:=S[u]-2delta int psi L J_u
       >=2int psi^2 Gamma_psi[u]+(1/8)int psi J_u>=0,
                                                   0<=delta<=1/2.

This includes the established actual three-halves Green depth, where
0<delta<=1/3. The complete comparison is still
P_ray-H_ray-(1-delta)N_ray+S_delta=0, and its added current-variance row
cancels the extra positive storage term exactly. The same no-double-spending
limitation therefore applies to this stronger actual-depth theorem.
