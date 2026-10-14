# Exact dominant-current variance completion with all reset forcing canceled

This note uses the SAME actual current field throughout. It combines its
conditional-tail Schur decomposition, the complete signed mismatch
covariance, and the actual first-label equation BEFORE any Cauchy estimate.
The entire centered tail-reset forcing cancels. The dominant mode produces
an explicit positive incoming Gamma/prime commutator and positive potential;
only the genuine higher-label remainder remains signed. This is not yet a
coefficient-one comparison for the full original Q_delta form.

## 1. Actual fields and notation

Use the verified full eta current field w, posterior p, u=T w, and

    v=w_1, e=v-u, q=1-p_1, epsilon=q/p_1,
    v_tail=q^(-1)sum_(n>=2)p_n w_n,
    Z_n=w_n-v_tail (n>=2), R_high=sum_(n>=2)p_n Z_n^2,
    abar=q^(-1)sum_(n>=2)p_n a_n, beta=T a,
    F_tail=sum_(n>=2)p_n a_n Z_n,
    mu=psi^2, m=mu/epsilon, omega=1/epsilon.

All fields are real; real polarization gives the corresponding Hermitian
identities. The same-field identities already proved are

    V=T(w-u)^2=e^2/epsilon+R_high,
    (G_1+abar)e=D u+F_tail,
    D=G_psi-G_1=G_prime-G_extra,
    abar>=a_2>a_1+3log2.                                  (1)

The complete prime-minus-continuous sign of D is retained. In particular
D is NOT replaced by a positive row. Let G=G_psi and define

    F[f]=int mu Gamma_G[f], F_m[f]=int m Gamma_G[f],
    b=G^*mu,
    Delta_n=w_n-v, E_Delta=int mu T Gamma_A[Delta].

Here A is the genuine full hidden score lift. Write E_Delta,sp for its
continuous PLUS true-divisor part, with only refresh removed. Every
component of E_Delta,sp is nonnegative; no divisor square is suppressed.

## 2. Center the mismatch in precisely the same tail

The finite complete mismatch kernel from
[CONTRAST_TRANSPORT.md](CONTRAST_TRANSPORT.md)
is

    F_n^0=sum_(d|n)lambda_d[v(x+log d)-v(x)]
                  -int(q_1-q_n)(x,dy)[v(y)-v(x)], F_1^0=0.

It equals (G_1-A_n)v on its lawful core. Since T A v=Gv, its exact mean is

    sum_n p_n F_n^0=-D v.                                  (2)

Define the higher-label covariance by the FINITE mismatch representation

    C_high=int mu sum_(n>=2)p_n Z_n F_n^0.                  (3)

One may subtract the tail mean of F_n^0 inside (3), because T_tail Z=0.
No separate classical A_n v drift is required. If H_n=w_n-u, then on the
tail H_n=Z_n-e/epsilon. Consequently the old full covariance is exactly

    C=-int mu sum_(n>=2)p_n H_n F_n^0
      =-int m e Dv-C_high.                                 (4)

The actual first-label equation also gives

    Dv=(G+abar)e-F_tail.                                   (5)

Equations (4)-(5) use the actual same-source equation, not a formal
stationarity substitution at a finite prime cutoff.

## 3. The positive full incoming commutator

The complete posterior tail decreases strictly, so omega=1/epsilon is
smooth and increasing. Define the grouped density

    C_omega(x)=G^*(mu omega)(x)-omega(x)G^*mu(x)
      =psi(x)int_0^x kappa(x-y)psi(y)[omega(x)-omega(y)]dy
       +psi(x)sum_(d_n<x)alpha_n psi(x-d_n)
                                [omega(x)-omega(x-d_n)].   (6)

Thus C_omega>=0, with the continuous part strictly positive for x>0.
The difference in (6) cancels the Gamma singularity at y=x. This is a
joint original incoming-Gamma/ALL-prime density, not a new auxiliary
posterior variance or an unsigned replacement for D.

Section 6 justifies the weighted product identity

    2int m eGe=F_m[e]+int [omega b+C_omega]e^2.              (7)

In particular F_m[e] is finite. Its finiteness is derived from the actual
weak equation and weighted cutoff passage, not from a pointwise tail
bound alone.

## 4. Complete cancellation of the centered reset forcing

The earlier exact contrast identity is

    E_Delta=F[e]-int bV-2C.

Insert (1),(4),(5),(7). This gives

    E_Delta=F[e]+F_m[e]+int C_omega e^2
          +2int m abar e^2-2int m eF_tail
          -int b R_high+2C_high.                           (8)

Now calculate the ACTUAL refresh contribution, rather than bounding it.
Its two standard parts are int mu T[a H^2]+int mu beta V. Since
H_1=e and H_n=Z_n-e/epsilon on the tail, direct expansion gives

    E_Delta,refresh
       =int m(a_1+abar)e^2-2int m eF_tail+R_high,a,
    R_high,a=int mu[sum_(n>=2)p_n a_n Z_n^2+beta R_high].    (9)

For transparency the coefficient in (9) uses
beta=p_1a_1+q abar and
q a_1+p_1 abar+beta=a_1+abar. All complete labels remain in R_high,a.
It is nonnegative and is part of the original refresh budget, not an
independently added resource.

Subtracting (9) from (8) cancels EVERY term involving F_tail, including
its mixed sign. The exact resulting signed completion is

    F[e]+F_m[e]+int C_omega e^2
                 +int m(abar-a_1)e^2
       =E_Delta,sp+int b R_high+R_high,a-2C_high.             (10)

Every term on the left is nonnegative, and its last potential is strictly
positive unless e vanishes. The signed right-hand remainder uses ONLY the
genuine higher-label variance and its centered mismatch, besides the
complete nonnegative spatial contrast energy. No claim is made that this
right side is bounded above by an unspent original positive budget.

This identity is stronger bookkeeping than bounding F_tail by a separate
small square: that forcing has canceled EXACTLY against its own refresh
cross term. Spending its old Cauchy bound as another gain after (10) would
be double counting. Likewise the positive commutator in (6) is not a
second copy of the incoming-prime hub budget.

## 5. Finiteness of the other terms and their unchanged meaning

The already proved E_Delta is finite, and its refresh part is nonnegative
and finite. The actual global current estimates give w_n=O(1+log n),
e=O(poly(z)exp(-3z)), R_high=O(poly(z)exp(-8z)), z=pi exp(2x), with bounded
origin traces. The exact posterior ratio obeys

    epsilon=(16+O(1/z))exp(-3z),
    omega=O(exp(3z)), (log omega)'=O(1+z).

Therefore m e^2, m abar e^2, and m eF_tail are integrable at infinity and
at zero. In particular m=O(x^2) at zero, whereas a_n,beta,abar have at most
1/x growth there, with complete Gaussian label moments paying their
coefficients. The higher-label reset terms in (9) are finite by the same
moments. The original full covariance C is finite by its previously proved
finite-kernel Cauchy estimate. The term int m eDv is finite because the
complete finite mismatch D has a Gaussian-small row at infinity and an
O(1/x) row at zero, while v is bounded. Hence (4) also proves absolute
integrability of the grouped C_high in (3), without assigning individual
drift domains to all w_n.

The source pole and reflected graph do not occur in the internal identity
(10). They have NOT been removed from Q_delta=2F-B_delta. Inserting (10)
into that full signed comparison still requires the exact reflected/pole
and any neutral forcing terms. In particular the canonical xi seed field
is not a substitute for Z or Delta.

## 6. Weighted form passage, including the exponentially growing m

Here are details needed for (7). They avoid an inference from amplitude
alone to Gamma form regularity.

First, e is already a legal original-P ratio and has finite F[e]. The
actual first-label killed equation is a weak form equation on every compact
positive wing. The difference D is a finite positive-channel UNION with
its original relative minus sign, so adding D e to that equation gives
(5) in the same weak sense. On a compact wing a smooth multiplier of e
is a legal form test; this follows from the local logarithmic Gamma form
product inequality and the bounded complete prime kernels. Thus one may
test (5) against m chi e for smooth chi supported away from zero and
infinity. Equivalently, use original-P core approximations after this
compact multiplier. The grouped weak current equation is kept intact;
no truncated source equation is set to zero.

The product identity with that test gives

    int m chi Gamma_G[e]
       =2int m chi eGe-int G^*(m chi)e^2.                   (11)

The fixed compact statement uses only the already finite original local
form and its polarization. Now take monotone spatial cutoffs chi tending
to1, with the usual O(1/epsilon) derivative at the lower cutoff and a
bounded derivative at the upper cutoff. The exact adjoint commutator is

    G^*(m chi)-chi G^*m
      =psi(x)int_0^x kappa(x-y)psi(y)omega(y)
                                      [chi(x)-chi(y)]dy
       +psi(x)sum_(d_n<x)alpha_n psi(x-d_n)omega(x-d_n)
                                      [chi(x)-chi(x-d_n)]. (12)

Near zero omega is smooth and bounded, psi(x)=O(x), and e is bounded.
The Gamma contribution paired with e^2 is O(epsilon^2[1+|log epsilon|]);
the prime contribution is O(epsilon^2), exactly as in the verified
original-current adjoint cutoff proof. Its large-x part is even more
convergent because the actual e has a Gaussian tail.

For the upper cutoff, write z_x=pi exp(2x). In each incoming term y<x,
the absolute source factor including e(x)^2 satisfies, up to fixed
polynomial factors,

    psi(x)psi(y)omega(y)e(x)^2
        <=poly(z_x,z_y)exp[-7z_x+2z_y]
        <=poly(z_x)exp(-5z_x).                            (13)

The factor chi(x)-chi(y)=O(min(1,|x-y|)) cancels the local Gamma singularity.
For nonlocal Gamma and prime incoming rows, complete Chebyshev shell bounds
supply at most an exponential in x, which is also paid by (13). Thus (12)
paired with e^2 tends to zero by an integrable bound. No separately growing
backward row is omitted.

The exact density G^*m=omega b+C_omega is absolutely integrable against
e^2. For the C_omega term, split the Gamma integral at h=1/(1+z_x). On the
short part use |omega(x)-omega(x-h)|<=C(1+z_x)omega(x)h; on the remainder
use the source theta bounds and the complete Chebyshev row. This gives
C_omega<=poly(z_x)exp(2z_x) on the tail, and C_omega=O(x^3) at zero.
The same tail majorant pays |omega b|. Multiplication by e^2 makes both
integrable. Finally Ge=Dv-abar e+F_tail has O(1/x) growth at zero and
O(poly(z)exp(-3z)) at infinity, from the finite mismatch and the actual
complete tail-score bounds. Therefore int m|eGe| is finite as well.

All right-hand terms of (11) now converge absolutely. The left side is a
nonnegative increasing cutoff integral. Monotone convergence proves its
finiteness and gives (7) exactly. This is the required form-level proof of
F_m[e]<infinity, including both the origin and exponentially growing
weight; it does not postulate higher regularity of w_1 or of its labels.
