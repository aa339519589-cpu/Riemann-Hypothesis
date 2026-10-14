# Exact bounded tail loads in the common-seed hidden metric

This note identifies which complete original-source tail loads are continuous
in the established hidden variance norm. It does not replace the full source
Schur complement by that variance or assert a sign for its original remainder.

## 1. Exact pullback of a complete tail load

Put b=log2, xi(y)=exp(y/2)c(pi exp(2y))exp[-pi exp(2y)],
c(z)=8z^3-30z^2+15z, and

    W(y)=sum_(2<=n<=exp y)n^(-1/2)psi(y-log n),
    m(y)=W(y)xi(y),                       y>b.

The positive safe seed is a(y)=phi(y)/xi(y), where phi=Mf is the honest
future Mobius inverse of the SAME source. Future inversion gives, for x>b,

    f(x)=sum_(n>=1)n^(-1/2)xi(x+log n)a(x+log n).       (1)

Let l be a real locally Lipschitz load on [b,infinity), of at most exponential
polynomial growth. Define

    A_l(y)=sum_(1<=n<=exp(y-b))n^(-1/2)l(y-log n),
    C_l^2=integral_b^infinity xi(y)|A_l(y)|^2/W(y)dy.   (2)

Whenever the integrals are absolutely convergent, the exact adjoint identity is

    integral_b^infinity l(x)f(x)dx
         =integral_b^infinity xi(y)A_l(y)a(y)dy.       (3)

For a finite common label/source cutoff this is simply y=x+log n. Absolute
convergence then removes the common cutoff. In particular there are no
independently reset label marginals and no deletion of arithmetic branches.
The same formula applied to the constant seed a=1 gives

    integral_b^infinity xi A_l=integral_b^infinity l psi. (4)

## 2. The two exact balance conditions

For the complete neutral loads used below, the functional in (3) is bounded
on L2(m dy) if and only if

    l(b)=0.                                         (5)

To see the endpoint explicitly, write y=b+s and p=psi'(0)>0. For s<log(3/2),

    W(b+s)=psi(s)/sqrt2=(p/sqrt2)s+O(s^3),
    A_l(b+s)=l(b+s),
    xi(b+s)=xi(b)+O(s).

Thus if l(b) differs from zero, the integrand in (2) has the asymptotic

    [sqrt2 xi(b)l(b)^2/p]/s+O(1),                    (6)

and its integral diverges logarithmically. If l(b)=0, local Lipschitz
regularity makes that integrand O(s), which is integrable. This is a genuine
bounded-functional criterion by the L2 Riesz theorem. It is not repaired by
assuming merely that an individual source has a finite value of the load.

Continuity on the constant quotient additionally requires exactly

    integral_b^infinity l(x)psi(x)dx=0.              (7)

Indeed a constant seed is a null vector of the variance seminorm. Equations
(4) and (7) say that k_l=A_l/W is orthogonal to constants in L2(m). When
(5) and (7) both hold, the sharp scalar bound is

    |integral_b^infinity l f|^2
       <=C_l^2 inf_c integral_b^infinity m(y)|a(y)-c|^2dy. (8)

This is ordinary Hilbert-space Cauchy--Schwarz after subtracting c; equality
in the unconstrained hidden Hilbert space occurs when a-c is proportional
to k_l. No claim is made that this extremizer is an actual stationary source.
Conversely, failure of (7) makes (8) impossible even for constant seeds.
Failure of (5) gives smooth compactly supported hidden test sequences with
unbounded functional-to-mass ratio; those sequences need not be actual sources.

## 3. Full far-tail convergence for the lawful jet loads

The original neutral loads have the form

    n_j(x)=2[(L(x)/psi(x))t_j(x)-(F_r t_j)(x)],
    L(x)=sum_(log d>x)alpha_d psi(log d-x),
    (F_r t_j)(x)=sum_(log d>x)alpha_d t_j(log d-x),    (9)

where t_j is a fixed centered even-derivative theta jet, for example
psi^(2j)-4^(-j)psi. All prime powers are retained. The vanishing of psi and
t_j at zero makes (9) continuous through every threshold log d and locally
Lipschitz; its one-sided derivatives may jump there. Since psi is positive
on x>0, its denominator is harmless on every closed subinterval of (0,infinity).

The theta polynomial ladder gives

    |t_j(x)/psi(x)|<=C_j exp(4j x),                  x>=b.

No prime number theorem is needed to bound the reflected rows. Use only
Lambda(d)<=log d, divide log d-x into unit intervals, and use the rapidly
decreasing suprema of |psi| or |t_j| on those intervals. The number of d in
the kth interval is at most exp(x+k+1); its d^(-1/2) weight is at most
exp[-(x+k)/2]. Hence, with an absolutely summable theta majorant,

    |L(x)|+|(F_r t_j)(x)| <=C_j(1+x)exp(x/2),
    |n_j(x)|<=C_j(1+x)exp[(4j+1/2)x].               (10)

Consequently a finite combination of exp(x/2),n_1,...,n_J has
|A_l(y)|<=C(1+y)^2 exp[(4J+1/2)y]. This follows directly from its complete
sum (2); the exp(x/2) term only contributes a harmonic sum.

For y>=2b put z=pi exp(2y). The positive n=2 term of W yields
W(y)>=psi(y-b)/sqrt2>=xi(y-b)/sqrt2. Factor
c(z)=8z(z-r_+)(z-r_-), r_++r_-=15/4. Since z/4>=4pi>12,

    c(z)/c(z/4)<=128,
    xi(y)/W(y)<=256 exp(-3z/4).                    (11)

The first bound follows by bounding the numerator factors above by 1 and
the denominator product below by 1-(15/4)/(z/4)>1/2. Thus (10)-(11) give
an explicit superexponentially integrable far majorant for (2). Together
with the endpoint computation this proves (5), without a formal transform
of an exponentially growing arithmetic log measure.

The identities (3)-(4) first hold for compact seeds. When C_l is finite,
Cauchy--Schwarz extends (3) continuously to the hidden weighted completion.
For the actual theta-localized source class, the direct integral has the
same value by absolute Fubini. In particular this extension does not assert
new original P membership for every abstract hidden vector.

## 4. Two balanced loads and exact matrix-valued payment

For balanced loads l_1,...,l_r, define their finite Gram matrix

    G_ij=integral_b^infinity xi(y)A_(l_i)(y)A_(l_j)(y)/W(y)dy.

Let h_i=integral_b^infinity l_i f. If G is invertible, the exact joint bound is

    h^* G^(-1)h <=inf_c integral_b^infinity m|a-c|^2. (12)

For a singular G the statement uses its pseudoinverse on its range. This
follows by orthogonal projection onto the span of the Riesz vectors k_(l_i),
not by spending the same hidden variance independently r times.

The published complete hidden comparison B[a]=G_tail[a]-D_div[a] gives

    h^*G^(-1)h <=125000 B[a].                        (13)

This spends at most the one previously established hidden variance budget.
The constant 125000 is exactly the reciprocal of 8*10^(-6).

For the actual plateau representative f=g-c_infinity psi, the total U load
and every lawful neutral N(f,t_j) vanish. Therefore every balanced linear
combination l of their densities has zero GLOBAL load, and

    integral_0^b l(x)f(x)dx=-integral_b^infinity l(x)f(x)dx. (14)

Equations (12)-(14) are genuine same-source restrictions on the head. A
single endpoint-cancelled combination of U and n_1 need not satisfy the
constant balance (7). Both conditions must be imposed, for example using
additional actual neutral loads, not new unsupported wall moments.

Neither (12) nor (14) bounds the full tail Q_delta form or its mixed head
forcing. A head coercivity theorem with these particular balanced loads
also requires a separate proof; their abstract linear independence is not
a replacement for it. No new positivity of the original residual follows
merely from this exact dual construction.
