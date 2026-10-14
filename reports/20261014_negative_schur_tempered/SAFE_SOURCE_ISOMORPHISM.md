# The honest future inverse on the exact safe weighted source space

This note proves a complete weighted shift estimate on the whole open
safe ray. It supplies an actual inverse and source-cutoff core,
not an inverse-zeta multiplier on a Hardy line. It asserts no original
Schur sign and no ordinary physical L2 range.

Use the complete weights in [the safe-xi theorem](../20261014_safe_xi_hidden_comparison/REPORT.md):

    b=log2, z=pi exp(2x), c(z)=8z^3-30z^2+15z,
    xi(x)=exp(x/2-z)c(z), psi=C xi,
    W(x)=sum_(2<=n<=exp x)n^(-1/2)psi(x-log n), m=W xi.

Put

    H_m=L2((b,infinity),m dx),
    Y=L2((b,infinity),nu dx), nu=W/xi.

Multiplication by xi is an isometry H_m to Y. Near b, nu vanishes linearly;
at infinity it grows at the inverse-Gaussian rate. It is not equivalent
to ordinary source L2.

## 1. Both complete future operators are norm-close to identity in Y

For n>=1 define U_n f(x)=n^(-1/2)f(x+log n), x>b. Changing variables gives

    ||U_n||_(Y to Y)^2
      <=n^(-1) sup_(x>b) [W(x)/W(x+log n)]
                                      [xi(x+log n)/xi(x)].      (1)

The complete integer-row injection and exact cubic imply

    W(x+log n)>=n^(-1/2)W(x),
    xi(x+log n)/xi(x)
        <=gamma_b^(-1)n^(13/2)exp[-4pi(n^2-1)],
    gamma_b=1-15/(16pi)+15/(128pi^2)>11/16.

These estimates hold for every x>b. There is no endpoint inverse of W:
its vanishing at b only decreases the ratio in (1). Consequently

    ||U_n||<=gamma_b^(-1/2)n^3exp[-2pi(n^2-1)],
    epsilon:=sum_(n>=2)||U_n||
       <67108864/91461181640625<10^(-6).              (2)

For an explicit all-label check, gamma_b^(-1/2)<4/3. Replace pi by3
and use exp(1)>5/2. The consecutive ratio in
sum_(n>=2)n^3 exp[-6(n^2-1)] is at most(27/8)exp(-30)<1/1000,
while its first term is8 exp(-18). Therefore the whole bound is less than

    (32/3)(1000/999)(2/5)^18=67108864/91461181640625.

The W inequality follows by injecting the integer label k into nk in
the complete positive W row; the cubic inequality follows from
c(z)>=8z^3 gamma_b for z>=4pi and c(n^2z)<=8n^6z^3.

It follows that both series

    C=I+sum_(n>=2)U_n,
    M=I+sum_(n>=2)mu(n)U_n                            (3)

converge absolutely in operator norm on Y, with
||C-I||<epsilon and ||M-I||<epsilon. Moreover U_d U_n=U_(dn).
The double product series is absolutely convergent, so grouping its finite
divisors and using sum_(d|n)mu(d)=1_(n=1) proves

    C M=M C=I on Y.                                  (4)

Thus (3) is the honest complete future Möbius inverse in this explicitly
weighted topology. It is not obtained by extending 1/zeta through zeros.
In particular C xi maps H_m ONTO Y, with inverse f->M f/xi, and

    (1-epsilon)||f||_Y<=||M f||_Y<=(1+epsilon)||f||_Y. (5)

The near-identity norm concerns the safe weighted SOURCE map. It does not
make the full original signed form a small perturbation of a positive
form or control the source-only head inverse.

## 2. The closed source graph has a direct weighted-source description

Let D_m be the form domain in
[CLOSED_ORIGINAL_SCHUR_IN_TRUE_SEED_MASS.md](../20261014_original_seed_schur/CLOSED_OPERATOR.md).
For a in H_m, write t=1_(x>b)C(xi a) and extend t oddly. By (4), its exact
range condition is simply t|_(b,infinity) in Y. Therefore

    D_m corresponds bijectively to
    {t in Y: t_o has finite ordinary L2 and complete log-Gamma form}. (6)

The mass in the original Schur form is exactly

    ||a||_m^2=||M t||_Y^2,                            (7)

not ||t||_Y^2. Equations (5) compare these two positive norms, but all
M cross terms remain in an eigenvalue equation or a signed pairing.
The head-harmonic extension E0 and every prime/pole row in s0 are unchanged.

For example a negative eigenvector S a=-lambda a has, in source variables,
the weak equation on the tail

    Qf+lambda M_b^*[nu M t]=0, f=E0 t,               (8)

with the genuine finite causal adjoint prefix M_b^*. This is the same
complete equation as the finite-inverse density note, not an equation with
the Möbius terms omitted because of their small norm.

## 3. Compact source approximants and a true compact seed form core

There is now a justified cutoff argument, beyond the ambient neutral
pairing argument used in the original closure proof. Smooth compact source
tails t_j in C_c^infinity(b,infinity) approximate every t in (6) jointly in
Y and the ordinary L2/log-Gamma source norm. To see this, first cut off at
large x and in a shrinking collar of b. Weighted Y convergence follows
by dominated convergence. The characteristic half-line multipliers are
uniformly bounded on the logarithmic source norm by the proved logarithmic
Hardy inequality; convergence follows first on smooth bounded sources
and then by that uniform bound. Finally mollify on each remaining compact
interval, where nu is bounded above and below by positive constants.

Set a_j=M t_j/xi. Equation (4) proves C(xi a_j)=t_j, and (5) gives
convergence in the TRUE mass norm. The source/head norms also converge:
the full mixed density B0 is continuous under source log-Gamma plus far
weighted L2 convergence, and the latter follows from Y away from b and
source L2 on a fixed collar. Hence E0 t_j tends to E0 t in the closed graph
and a_j tends to a in the original Schur form norm.

Each M t_j is a finite future sum on x>b, is smooth, and vanishes above
a finite upper endpoint. It may be nonzero at b. Remove a small seed collar
(b,b+eta), with eta<b. For any difference supported in that collar, every
future label n>=2 vanishes on x>b, because x+log n>=2b>b+eta. Therefore
C of that collar difference is just its n=1 source term. Its mass and
log-Gamma source norms tend to zero as eta decreases to zero, by the same
bounded collar cutoff argument. This proves

    C_c^infinity(b,infinity) is a form core for the seed form s0. (9)

The proof uses the actual bounded inverse (4); it does not infer (9) merely
from mass density or from arbitrary compact-source approximants. Original
P membership, actual stationarity, and the physical norm integral W^2|a|^2
are not consequences of (9).
