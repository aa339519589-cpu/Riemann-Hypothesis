# Explicit nonzero true-seed vectors orthogonal to every neutral jet

Let b=log2, z=pi exp(2x), m=Wxi, and

    B(x)=exp(x/2)exp(-z),
    xi=-(partial_x^3-partial_x/4)B,
    a_j=xi^(2j)/xi-4^(-j), j>=1.

The identity for xi is the exact polynomial ladder
xi=B(8z^3-30z^2+15z). The mass space is H_m=L2((b,infinity),m dx),
and K is the mass-closed span of 1,a_1,a_2,... from
[the closed original Schur construction](CLOSED_OPERATOR.md).

There are explicitly given, nonzero, linearly independent vectors in
K-perp. In particular K is NOT dense in H_m. This is not a sign assertion
for the original Schur operator on that complement.

## 1. A real Bessel density with a reciprocal heat transform

Fix any A>4pi. For s>0 define

    g_A(s)=(s/A)^(1/8) J_(1/4)(2sqrt(A s)),
    u_A(A+s)=g_A(s)-integral_0^s sin(s-v)g_A(v)dv,
    u_A(z)=0 for z<=A.                               (1)

All functions are real. The standard Bessel power series, also fixing its
normalization, is [DLMF 10.2.2](https://dlmf.nist.gov/10.2.E2). It gives

    g_A(s)=sum_(k>=0)(-A)^k s^(k+1/4)/[k!Gamma(k+5/4)],
    g_A(s)=s^(1/4)/Gamma(5/4)+O_A(s^(5/4)).           (2)

Termwise Laplace integration for rho>0 is justified absolutely: the sum of
the integrals of the absolute terms is rho^(-5/4)exp(A/rho)<infinity.
Thus

    integral_0^infinity exp(-rho s)g_A(s)ds
                       =rho^(-5/4)exp(-A/rho).

Using the sine convolution in (1) and the translation by A gives exactly

    L_A(rho):=integral_A^infinity exp(-rho z)u_A(z)dz
       =rho^(3/4)/(rho^2+1) exp[-A(rho+1/rho)]
       =rho^(-1/4) exp[-A(rho+1/rho)]/(rho+1/rho).    (3)

The fixed-order large-real-argument Bessel estimate from
[DLMF 10.17.3](https://dlmf.nist.gov/10.17.E3) gives g_A(s)=O_A(s^(-1/8))
for s>=1. Consequently u_A(A+s)=O_A((1+s)^(7/8)) by absolute integration
in (1). Near zero the sine convolution is O_A(s^(9/4)), so

    u_A(A+s)=s^(1/4)/Gamma(5/4)+O_A(s^(5/4)).         (4)

In particular u_A is nonzero immediately to the right of A. The polynomial
bound justifies all the Laplace and convolution integrals for rho>0.

## 2. The exact arithmetic mass vector

For x>b define

    f_A(x)=2 pi^(1/4) z^(3/4) u_A(z)/W(x).            (5)

The denominator is the COMPLETE positive integer row W, not an asymptotic
substitution. It is strictly positive on the support x>=x_A,
x_A=(1/2)log(A/pi)>b. The known W(x)~I0 exp(x/2) and its compact positivity
show that (5) has polynomial growth in z, while m has its Gaussian tail.
More explicitly, coordinate change gives

    ||f_A||_m^2
       =2 pi^(1/4) integral_A^infinity
          z^(3/4)c(z)exp(-z)|u_A(z)|^2/W(x(z)) dz<infinity,
    c(z)=8z^3-30z^2+15z.                             (6)

Its onset is the nonzero one-sided power (z-A)^(1/4), and it vanishes for
b<x<=x_A. Thus f_A is a genuine nonzero mass vector, not a distribution,
and no value at the signed xi first root is divided by.

## 3. Every neutral pairing vanishes exactly

Define its Gaussian pairing on real t by

    H_B(t)=integral_b^infinity f_A(x)W(x)B(x+t)dx.

The coordinate identity
f_A(x)W(x)exp(x/2)dx=u_A(z)dz and rho=exp(2t) give

    H_B(t)=rho^(1/4)L_A(rho)
          =exp[-A(rho+1/rho)]/(rho+1/rho).            (7)

This is EXACTLY even in t. The polynomial growth proved above makes the
Gaussian integral and all its t derivatives absolutely convergent on each
compact real t interval. The xi ladder therefore gives

    H_xi(t):=integral_b^infinity f_A W xi(x+t)dx
             =-(partial_t^3-partial_t/4)H_B(t),       (8)

which is odd. In particular all even derivatives at zero vanish. Hence

    <f_A,1>_m=H_xi(0)=0,
    <f_A,a_j>_m=H_xi^(2j)(0)-4^(-j)H_xi(0)=0,
                                                   j>=1. (9)

By mass continuity, f_A is orthogonal to the entire closed span K.
No zeta-zero hypothesis, inverse-zeta contour, or physical-source analytic
regularity is used in (9). All arithmetic dependence of this exact dual is
retained through W in (5) and in the mass m.

For any finite strictly increasing list A_1<...<A_r, their vectors are
linearly independent: on x_(A_1)<x<x_(A_2) only the first can be nonzero,
and (4) forces its coefficient to vanish; repeat. Thus K-perp is infinite
dimensional, not merely nontrivial.

## 4. Source-form legality and the remaining sign

These vectors also furnish concrete source-form tests, not only abstract
mass duals. Their genuine seed sources are

    phi_A(x)=xi(x)f_A(x)
        =2z c(z)exp(-z)u_A(z)/W(x).                  (10)

They are zero below x_A and have a one-sided quarter-power onset there.
On compact intervals away from b, W and its reciprocal are Lipschitz and
bounded, so (10) has local H^sigma regularity for every sigma<3/4. The
ordinary derivative grows at most polynomially in z away from the onset;
all far source norms are paid by exp(-z). Its complete future integer lift
C phi_A is locally H^sigma for such sigma: only finitely many translated
onsets meet a fixed compact interval, and every remaining label is paid
by the Gaussian derivative rows. It has the same Gaussian type at infinity.
Its zero-supported tail at b consequently has finite logarithmic Gamma
form. Thus f_A belongs to the original Schur form domain D_m.

No sign for s0[f_A], or for the full matrix s0(f_A,f_D), is assigned here.
The construction supplies explicit non-neutral test vectors in the exact
mass quotient, with no arbitrary-model zero insertion and no omitted
prime/reflection/pole term. Evaluating that original signed matrix still
requires its complete head Schur subtraction; the even transform (7) does
not by itself make the original form positive.
