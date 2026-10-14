# One signed square for the source, projected profile, and full orthogonal feedback

This is a companion to the complete source/profile factor. It absorbs the
SAME orthogonal reset and square-collision feedback using ONE complete
residual allocation. The positive factor still does not sign the original
boundary remainder; that remainder is displayed exactly.

Inputs are [the passed source/profile square](../20261014_coupled_source_profile_square/COUPLED_SQUARE.md),
[the exact-metric parent-six and reset bound](PARENT_SIX.md),
and the [complete residual forward theorem](RESIDUAL_COERCIVITY.md).
The full finite masks have N>=3; the infinite Mobius mask is also allowed.
All objects refer to the SAME actual source and current decomposition.

## 1. Keep the raw one-budget residual allocation

Use w-u=D+Z, D=A(a-m), h=sigma^2 A, T Z=T(aZ)=0,
E_Z=E_full[Z], F_Z=F_star[Z], and
E_a=int psi^2 T[c|Z|^2]. The complete residual theorem proves

 E_Z >= F_Z+(39599/20000)E_a-(29/11)sqrt(E_a F_Z).

It follows from the exact determinant

 (49/50)(39599/20000-1/5)-(29/22)^2
                         =816471/121000000>0

that the SAME residual budget obeys

 E_Z >= F_Z/50+E_a/5.                              (1)

Set K_Z=E_Z-F_Z/50. Thus K_Z>=E_a/5>=0. This is an
alternative allocation of the original residual theorem, not a second
copy of its energy or its earlier F_Z/10+E_a/25 allocation.

## 2. The complete feedback in the same dual space

Let R_Z=r+I_Z, where r=-T[c(a-m)Z] and I_Z is the exact finite/full
orthogonal prime residual. Every finite cutoff union and true prime
power remains in its defining equation. The exact-metric residual bound is

 int psi^2 |R_Z|^2/(beta sigma^2) <= E_a/2750.

Since lambda_0=beta+kappa_a+23/200>=2beta, the dual norm used by the
source/profile square satisfies

 ||R_Z||_*^2 :=int psi^2 |R_Z|^2/(lambda_0 sigma^2)
                    <=E_a/5500<=K_Z/1100.           (2)

The source theorem gives ||S_a u||_*^2<=c F[u],
c=124633/125000. Combining the two vectors in the SAME dual space,
without assuming any favorable angle, gives

 ||S_a u-R_Z||_*
     <=sqrt(c F[u])+sqrt(K_Z/1100),
 ||S_a u-R_Z||_*^2 <= c_total(F[u]+K_Z),             (3)
 c_total=c+1/1100=1372213/1375000<1.

Thus the complete feedback is paid once together with the complete source
forcing, not by two separate Young allocations of E_a.

## 3. Exact coupled completion with the full residual

Use I[A]=int psi^2 A P_a(sigma^2 A),
D_lambda=int psi^2 lambda_0 sigma^2 A^2,
D_0=int psi^2 sigma^2 A^2, and
F_A(z)=psi(x)sigma(x)A(x)/sqrt(2z). Define

 C_full[u,A,Z]=F[u]+E_Z+I[A]
                         +2int psi^2 A[S_a(u)-R_Z].         (4)

The exact identity is

 C_full = F[u]+K_Z-||S_a u-R_Z||_*^2
          +[I[A]-D_lambda]+F_Z/50
          +int psi^2 lambda_0 sigma^2
                    |A+[S_a u-R_Z]/(lambda_0 sigma^2)|^2.   (5)

The principal factor already proves
I-D_lambda>=D_(3/2)[F_A]+(199/120000)D_0. Therefore

 C_full >= (2787/1375000)[F[u]+K_Z]+F_Z/50
          +D_(3/2)[F_A]+(199/120000)D_0
          +int psi^2 lambda_0 sigma^2
                    |A+[S_a u-R_Z]/(lambda_0 sigma^2)|^2.   (6)

Every term on this right side is nonnegative. The full signed adjoint
storage is still inside I, with

 2I[A]=E_full[D]+int b sigma^2 A^2.

Neither b nor the reset and collision feedback has been discarded. The
Gamma half-line E_1/4 boundary remains inside D_(3/2). The proof uses no
actual Q_delta positivity, although the current and residual inputs are
those already constructed for the actual source class. It is not a claim
that arbitrary unrelated fields Z have these same bounds.

## 4. Actual equation and the unchanged original obstacle

At this same actual source the full projected equation is
P_a h=-S_a u+R_Z. Consequently

 C_full=F[u]+E_Z-I[A].                              (7)

This is a quantitative original/current relation, not an iteration on a
new actual kernel. The full original form is still
Q_delta[psi u]=2F[u]-B_delta[u]. Thus exactly

 Q_delta[psi u]=2C_full-R_full,
 R_full=B_delta[u]+2E_Z+2I[A]
                           +4int psi^2 A[S_a u-R_Z].         (8)

At the actual equation this reduces to
R_full=B_delta[u]+2E_Z-2I[A]. No upper comparison of this remainder with
(6) has been established. In particular neither B_delta[u], B_D, the
residual boundary B_Z nor its mixed covariance can be inferred from the
positive coupled square. Equation (6) is a strict all-feedback signed
block, not a full original-form sign or an RH proof.

## 5. Domains

The complete residual theorem pays E_Z,F_Z,E_a on the SAME actual field.
The parent-six translation operator and grouped reset proof give (2)
without splitting a divergent incoming prime row. The source estimate
pays S_a u in the identical dual space. Therefore every cross and square
in (3)-(6) is finite. The actual amplitude has the separately proved
half-line Gamma generator domain; general amplitudes can instead use the
closed sectorial-form interpretation of I. Common finite label, divisor,
origin and Gamma cutoffs preserve the exact projected equation before
passing to these bounds. No unweighted higher-label original-P claim is
needed.
