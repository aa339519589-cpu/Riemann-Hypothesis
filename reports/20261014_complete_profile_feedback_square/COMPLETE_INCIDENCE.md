# Complete divisor incidence paid by the same root-zero star square

This is the incidence estimate needed by the orthogonal-residual proof.
Let Z be any field in its stated averaged domains with Z_1=0; no T Z=0
hypothesis is needed for the estimate below. Write c_n for the positive
reset score (denoted a_n in the copied calculation),

 E_a=int psi^2 sum_(n>=2)p_n c_n |Z_n|^2,
 F_prime,Z=sum_d int K_d E_star|Z(x)-Z(y)|^2,
 T_Z=sum_d int K_d sum_(m>=2)p_m(y)conj(Z_m(y))
                                      [Z_(dm)(x)-Z_m(x)],
 K_d=Lambda(d)d^(-1/2)psi(x)psi(y), y=x+log d.

The SAME star law and the genuine full divisor conductance are the
published [joint matrix](../20261014_same_current_star_blocks/JOINT_STAR_MATRIX.md).
The conclusion is |T_Z|^2<=(5/3)E_a F_prime,Z. Every parent divisor is
paid as one union; there is no separate branch allocation. The argument
below uses only Z_1=0, which allows its application to xi=Z-Z_1 in the
residual theorem even though T xi is not zero.

## 1. Every true prime edge has strong posterior cooling

Put z=pi exp(2x), z_y=d^2 z, P(z)=4z^2-6z, and

    epsilon(z)=sum_(n>=2)P(n^2z)e^(-n^2z)/(P(z)e^(-z)).

The complete previously proved bound is epsilon<1/400. Moreover
P(4z)/P(z)=16+18/(z-3/2) decreases. Consequently

 t:=p_2(y)/p_2(x)
   <=(1+epsilon(z))exp[-3(d^2-1)z]
   <(401/400)exp(-27)<1/1000.                              (2)

The last strict inequality follows from exp(3)>20. Every ratio p_n/p_2,
n>=3, decreases, so p_n(y)/p_n(x)<=t for every n>=2. This is a complete
posterior estimate; no label or prime cutoff is declared exact.

For this SAME star law its higher edge square is

 S_Z(x,y)=sum_(m>=2){p_m(x)|Z_m(x)|^2+p_m(y)|Z_m(y)|^2
                       -2p_m(y)Re[Z_m(x)conj(Z_m(y))]}.

Complete the upstream square separately at each label. This gives

 S_Z(x,y)>=sum_(m>=2)p_m(y)[1-p_m(y)/p_m(x)]|Z_m(y)|^2
          >=(999/1000)sum_(m>=2)p_m(y)|Z_m(y)|^2.          (3)

Unlike a generic incoming mass estimate, (3) uses the cooling-to-label1
term of the SAME star prime square. Therefore the entire incoming row is
paid at once:

 I:=sum_d int K_d sum_(m>=2)p_m(y)|Z_m(y)|^2
                          <=(1000/999)F_prime,Z.          (4)

There is no source head debit, no mu=psi exp(x/2) coercivity substitution,
and no missing d=2 branch in (4).

## 2. The complete parent union, not a single-branch allocation

Define the complete incidence difference square

 J=sum_d int K_d sum_(m>=2)p_m(y)|Z_(dm)(x)-Z_m(x)|^2.

The genuine posterior/divisor conductance identity is

 K_d(x)p_m(y)=psi(x)^2 p_(dm)(x)lambda_d(x),
 lambda_d=Lambda(d)s(x+log d)/s(x).

The full divisor score bound L_n=sum_(d|n)lambda_d<=4a_n/3, proved in
[DIVISOR_RESET](../20261014_first_label_current_approximation/DIVISOR_RESET.md),
therefore pays the ENTIRE parent branch:

 J_parent=sum_d int K_d sum_(m>=2)p_m(y)|Z_(dm)(x)|^2
          <=int psi^2 sum_(n>=2)p_n L_n|Z_n|^2
          <=(4/3)E_a.                                    (5)

No one divisor's lambda_d/a_n is reused to pay the whole union.
For the same-label branch, p_m(y)<=p_m(x), and the exact complete prime
row obeys lambda_prime=F_+psi/psi<(7/400)beta by
[RESET_FORCING](../20261014_first_label_coercive_correction/RESET_FORCING.md).
That note also proves a_m>beta/p_1>beta for every m>=2. Hence

 J_same=sum_d int K_d sum_(m>=2)p_m(y)|Z_m(x)|^2
        <=int psi^2 lambda_prime sum_(m>=2)p_m|Z_m|^2
        <=(7/400)E_a.                                    (6)

Minkowski in the SINGLE full d,x,m measure gives

 sqrt(J)<=[sqrt(4/3)+sqrt(7/400)]sqrt(E_a).                (7)

All source domains here are inherited from E_a<infinity; these estimates
also prove J_parent,J_same,J finite before the polarized limit.

## 3. The single complete-incidence bound

Cauchy in that same complete edge measure, using (4) and (7), proves

 |T_Z|^2<=C E_a F_prime,Z,
 C=(1000/999)[sqrt(4/3)+sqrt(7/400)]^2<5/3.               (8)

The strict scalar comparison is rational: after subtracting 1621/1200
from (5/3)(999/1000), the remaining positive number is 377/1200, whose
square exceeds 7/75. This is exactly the squared cross radical in (8).


## 4. Complete limit

The positive incoming and parent/same-label measures in (4)-(7) have
finite bounds from E_a and F_prime,Z before any polarized limit.
Cauchy therefore proves absolute convergence of the full T_Z. Common
finite prime and label cutoffs converge by these bounds. This proof does
not introduce an independent backward prime row or a second reset budget.
Its only expenditure here is the estimate (8), used once in
[RESIDUAL_COERCIVITY.md](RESIDUAL_COERCIVITY.md).
