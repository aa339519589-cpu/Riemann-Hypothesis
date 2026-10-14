# The reciprocal Gaussian identity of the full safe neutral complement

This note identifies a necessary analytic identity in the ACTUAL safe
mass orthogonal complement. It also proves the exact conditional Sonine
classification when an additional physical L2 norm is available. That
additional norm is not implied by the mass space or by actual plateau
regularity; it remains an arithmetic range condition.

Use b=log2, m=Wxi, and the genuine centered neutral fields

    a_j=partial^(2j)(partial^2-1/4)xi/xi, j>=0.

Let Z be the closure in L2(m dy) of their span together with the constant1.
For a real h in Z-perp define the physical function

    G(u)=W(log u)h(log u)/sqrt(u), u>2,
    G(u)=0, 0<u<2.                                     (1)

Complex h is handled by the same bilinear transform or conjugating h.
Its exact available norm is

    integral_2^infinity q(u)|G(u)|^2du=||h||_M^2,
    q(u)=xi(log u)/W(log u).                           (2)

This is generally MUCH weaker than ordinary L2(du), since q has a
Gaussian tail.

## 1. A genuine local transform and its unavoidable elementary defect

For Re rho>1/2 the integral

    F(rho)=integral_2^infinity G(u)exp(-pi rho u^2)du    (3)

converges absolutely and is holomorphic. To verify it, apply (2) and
Cauchy--Schwarz to q^(-1)exp(-2pi Re(rho)u^2). At infinity the complete W
row grows only exponentially in y=log u, whereas xi has the exact
polynomial-Gaussian decay exp(-pi u^2). Thus the remaining exponent is
-pi(2Re rho-1)u^2. At u=2, W vanishes linearly and xi is positive, so
q^(-1)=O(u-2). Fixed rho derivatives are paid by the same strict margin.

Define near t=0

    H_B(t)=exp(t/2)F(exp(2t)),
    H_xi(t)=-(partial_t^3-partial_t/4)H_B(t).           (4)

The latter equals the actual pairing of h with the translated xi seed:

    H_xi(t)=integral_b^infinity W(y)h(y)xi(y+t)dy.

All these are convergent integrals on their common holomorphic neighborhood,
not a formal transform of a non-tempered measure. Orthogonality to1 and
the a_j says

    H_xi(0)=0,
    H_xi^(2j+2)(0)-(1/4)H_xi^(2j)(0)=0.

Hence all even Taylor coefficients of H_xi vanish: H_xi is odd near zero.
The odd part of H_B therefore lies in the kernel of
partial_t(partial_t^2-1/4). It follows exactly that

    H_B(t)-H_B(-t)=c sinh(t/2),
    c=4H_B'(0).                                      (5)

The elementary right side cannot be discarded from neutral annihilation
alone. It is annihilated by the xi differential operator.

Putting rho=exp(2t) gives the complete reciprocal identity

    F(rho)-rho^(-1/2)F(1/rho)
                       =(c/2)(1-rho^(-1/2)).          (6)

Initially (6) is valid where BOTH original integrals converge,

    Re rho>1/2 and Re(1/rho)>1/2,                     (7)

using the holomorphic principal square root. This connected lens contains
rho=1, so the identity theorem extends the local proof to (7). For small
positive rho, (6) may define a reciprocal continuation; without extra
hypotheses it does NOT assert convergence of the original integral (3)
there. The defect c remains explicit.

## 2. Ordinary physical L2 removes the defect and gives exact Sonine parity

Assume additionally G in L2((0,infinity),du). Then (3) converges on the
whole half-plane Re rho>0, and (6) continues there. Cauchy--Schwarz gives

    |F(rho)|<=C||G||_2 rho^(-1/4), rho>0.

The same estimate at1/rho bounds rho^(-1/2)F(1/rho) by O(rho^(-1/4)).
As rho decreases to0, the right side of (6) would have a nonzero
rho^(-1/2) term unless c=0. Therefore

    F(rho)=rho^(-1/2)F(1/rho), rho>0.                  (8)

Let C be the unitary cosine transform with kernel2cos(2pi uv). Since
C[exp(-pi rho u^2)]=rho^(-1/2)exp(-pi u^2/rho), (8) says that C G-G
annihilates every Gaussian exp(-pi rho u^2). These Gaussians are total in
L2(0,infinity): after u^2=v, their pairings are Laplace transforms, and a
fixed positive exponential damping reduces uniqueness to the ordinary
Fourier uniqueness theorem for an L1 density. Consequently

    C G=G, and G=0 on(0,2).                           (9)

Conversely, if G in L2 has the gap(0,2), C G=G, and the weighted norm(2)
is finite, then h from(1) belongs to Z-perp. For completeness put D=u partial_u+1/2 and B(u)=exp(-pi u^2).
The cosine transform obeys C B=B and C D=-D C on Schwartz functions.
The physical xi seed is -D(D^2-1/4)B and hence is cosine-odd, as are
all of its even D derivatives and centered combinations. Their pairings
with the cosine-even G vanish by Plancherel. The exact change of variable
u=exp y turns those pairings into the stated mass-neutral pairings.

Thus the regular part of Z-perp is EXACTLY the cosine-even Sonine space
with gap2 and the additional endpoint weight(2). No statement that every
member of Z-perp lies in this regular part is made.

## 3. What a negative original Schur equation must additionally provide

Suppose the closed original reduced form S0 on the safe mass space is
available, and suppose h is a negative eigenvector, S0 h=-lambda h,
lambda>0. Let

    f_T(x)=sum_n n^(-1/2)xi(x+log n)h(x+log n), x>b,
    f=E0 f_T.

Here E0 is the complete original SOURCE head-harmonic extension, not a
positive-metric scattering inverse. If the source density Qf representing
q0(f,.) is an ordinary function on the tail, then its weak equation is

    C_b^*(Qf)(y)=-lambda W(y)h(y),
    C_b^*H(y)=sum_(n<=exp(y-b))n^(-1/2)H(y-log n).      (10)

More generally (10) is a distributional identity on every compact subset
of y>b, with the displayed finite shifted prefixes. It follows by testing
against a compact safe seed variation, applying the complete future C
identity, and cancelling the strictly positive xi. The density Qf in
(10) retains Gamma, both prime orientations, and the full pole.

For G in(1), change of variables gives

    ||G||_L2(du)^2=integral_b^infinity W(y)^2|h(y)|^2dy.

Therefore the ordinary Sonine conclusion(9) for this eigenvector requires
precisely

    C_b^*(Qf) in L2(dy),                              (11)

with ||G||_2=lambda^(-1)||C_b^*(Qf)||_2 when the density is defined.
The Gaussian M norm supplies no such estimate. Neither does an actual
ratio remainder merely belonging to H^s(dy), s<1: at infinity W(y)^2 has
size exp(y), so(11) asks for a genuinely stronger weighted tail norm.

Equations(6) and(10) are usable retained constraints on a future signed
comparison. They do not remove the complete prefix row, prove(11), or
license replacing the full original Schur form by a positive uncut
conductor energy. In particular the elementary defect in(6) and the
possible non-L2 range in(11) must not be silently set to zero.
