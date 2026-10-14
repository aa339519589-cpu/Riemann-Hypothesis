# A strict COMPLETE boundary Schur angle for the genuine Mobius projection

The centered arithmetic profile and its orthogonal residual have two
nonzero triangular cross covariances under the SAME star law. Both are
retained here. The result is a strict full Gamma-wall/reflected-prime/pole
matrix comparison for the genuine Mobius projection, not a replacement
by the earlier label1-versus-tail field and not a coefficient-one Q sign.

## 1. The genuine arithmetic projection

Let p_n(x) be the complete eta posterior, z=pi exp(2x), and

    a(n)=1-mu_ar(n), m(x)=T_x a, M(x)=T_x a^2,
    sigma(x)^2=M(x)-m(x)^2, q(x)=1-p_1(x).

Here a is the fixed arithmetic profile in {0,1,2}, NOT a hidden reset
score. In particular a(1)=0 and a(2)=a(3)=2. For the actual current H=w-u,
its orthogonal projection and residual are

    A(x)=T_x[aH]/sigma(x)^2,
    D_n(x)=A(x)[a(n)-m(x)], Z_n(x)=H_n(x)-D_n(x).

Exactly T D=T Z=T(aZ)=0. The argument below applies to arbitrary complex
amplitudes A and complex Z satisfying these two residual constraints and
the stated finite boundary domains. It also applies to the genuine finite
profiles a_N=1-mu_ar*1_(n<=N), N>=3: they have the same first three labels,
are in [0,2], and all estimates below retain the complete posterior.

Use ONE star initial-label field. For x<y its joint law is

    Pr(N_x=N_y=n)=p_n(y), n>=2;
    Pr(N_x=n,N_y=1)=p_n(x)-p_n(y), n>=2;
    Pr(N_x=N_y=1)=p_1(x).

Write D_x=D_(N_x)(x), Z_x=Z_(N_x)(x), and

    S_D=E|D_x-D_y|^2, S_Z=E|Z_x-Z_y|^2,
    M_DZ=E[(D_x-D_y)conj(Z_x-Z_y)], V_Z(x)=T_x|Z|^2.

## 2. Both exact triangular cross covariances

The pointwise orthogonality E[D_x conj(Z_x)]=0 does NOT remove the two
cross-position terms. Direct summation of the star law gives

 E[D_x conj(Z_y)]=A(x)[m(x)-m(y)]conj(Z_1(y)),
 E[D_y conj(Z_x)]=A(y)sum_(n>=2)p_n(y)a(n)conj(Z_n(x)).     (1)

Consequently M_DZ is minus the sum of the right sides of (1). The first
line is generally nonzero, unlike the old first-label/tail decomposition.

The two exact residual constraints also give

    2p_1(y)Z_1(y)
       =-sum_(n>=4)p_n(y)[2-a(n)]Z_n(y).                  (2)

The labels2 and3 vanish from (2) because a(2)=a(3)=2. Thus

 |Z_1(y)|<=[sqrt(P_4(y))/p_1(y)]sqrt(V_Z(y)),
 P_4(y)=sum_(n>=4)p_n(y).                               (3)

This is a genuine higher-label bound for the omitted-in-the-old-split
component Z_1, not a declaration that it vanishes.

## 3. A common all-edge variance lower bound

Put t=p_2(y)/p_2(x), so 0<t<1. The complete posterior ratios p_n/p_2,
n>=3, decrease, hence every tail survival probability
 t_n=p_n(y)/p_n(x) is at most t.
The transition kernel of the star label therefore admits the exact mixture

    P_(x,y)=(1-t)J_1+t Q_(x,y),                         (4)

where J_1 sends every label to1 and Q is a Markov kernel: label n>=2
survives with probability t_n/t and otherwise goes to1; label1 stays1.
The auxiliary mixture in (4) is only a proof of a two-position variance
inequality, not a replacement of the genuine hidden dynamics.

For any function f of N_y, Jensen and total variance in the Bernoulli
mixture give

 Var_(p_x)(P_(x,y)f)<=t^2 Var_(p_x Q)(f)
                         <=t Var_(p_y)(f).              (5)

Thus any centered h(N_x), k(N_y) obey
 |E[h conj(k)]|<=sqrt(t) sqrt(E|h|^2 E|k|^2).
Applying this separately to D and Z yields

 S_D>=(1-sqrt(t))[sigma(x)^2|A(x)|^2+sigma(y)^2|A(y)|^2],
 S_Z>=(1-sqrt(t))[V_Z(x)+V_Z(y)].                       (6)

Both endpoint variances are retained. This will pay both terms in (1)
with one two-coordinate Cauchy estimate.

## 4. Complete posterior inputs and the first cross term

The already verified full theta bounds, proved in
[the earlier Schur theorem](../20261014_same_current_star_blocks/BOUNDARY_SCHUR.md)
and [the centered profile factor](CENTERED_PROFILE.md), are

    p_1>400/401, q/p_1<1/400,
    -d_z log p_2>14/5,
    0<-d_z log m<7.                                   (7)

For completeness the last bound holds for every a_N as well: m>=2p_2,
a_N<=2, and the full profile-weighted second label moment is below5.
The exact logarithmic derivative is a difference of these complete label
moments plus a rational correction of absolute value at most1/3;
E_p N^2<17/16 then gives absolute derivative below7.

Since m^2<=qM,

    m/sigma<=sqrt(q/p_1)<1/20.                         (8)

Integrating the two hazards in (7) gives

    m(y)/m(x)>=t^(5/2),
    m(x)-m(y)<=(5/2)m(x)(1-t).                        (9)

The complete label>=4 posterior is also small without truncation:
 p_n<=2n^4 exp[-(n^2-1)z], and the n>=4 consecutive ratio is below1/2.
Therefore, using z>3 and exp(3)>20,

    P_4<=1024 exp(-15z)<1024/20^15<1/10000.            (10)

Combining (3),(8)-(10), and 1-t=(1-sqrt(t))(1+sqrt(t)), gives

 |A(x)[m(x)-m(y)]Z_1(y)|
  <=c_1(1-sqrt(t)) sigma(x)|A(x)|sqrt(V_Z(y)),
    c_1=401/160000<1/190.                             (11)

Every integer label beyond3 is included in (10); a square collision is
not omitted merely because the leading two tail labels agree.

## 5. The second cross term and the complete rate-square sum

Set R_n(z)=p_n(z)/p_2(z), lambda_n=(3/8)(n^2-4), n>=3.
The complete hazard comparison and rational Gaussian tail proof in the
previous Schur theorem establish

    1-R_n(y)/R_n(x)<=lambda_n(1-t),
    sum_(n>=3)R_n(x)lambda_n^2<1/384^2.               (12)

Use T_x(aZ)=0 to subtract t from the second cross sum in (1):

 B(x,y):=sum_(n>=2)p_n(y)a(n)conj(Z_n(x))
       =sum_(n>=3)p_n(x)a(n)[t_n-t]conj(Z_n(x)).       (13)

The label2 term is exactly zero, not estimated independently. Since
0<=a<=2, Cauchy and (12) give

 |B(x,y)|<=2sqrt(p_2(x))t(1-t)sqrt(V_Z(x))/384.        (14)

The variance pair formed by labels1 and2 gives the exact lower bound

    sigma(y)^2>=4p_1(y)p_2(y)=4p_1(y)t p_2(x).        (15)

Consequently

 |A(y)B(x,y)|
  <=c_2(1-sqrt(t)) sigma(y)|A(y)|sqrt(V_Z(x)),
    c_2=401/76800<1/190.                              (16)

Indeed sqrt(t)(1+sqrt(t))<=2 and 1/sqrt(p_1(y))<401/400.
Neither the residual at label3 nor the higher arithmetic tail is lost.

## 6. A strict all-edge and full signed-boundary matrix angle

Combine (11),(16) by the two-coordinate Cauchy inequality. Its constant
is max(c_1,c_2), NOT their sum. Using (6),

    |M_DZ(x,y)|<=(1/190)sqrt(S_D(x,y)S_Z(x,y)).        (17)

The result follows by continuity when an edge variance vanishes; at x=y
all edge increments are zero. It is valid for every pair x,y and hence
for every actual Gamma, prime, reflected-prime or polar edge.

Keep the ORIGINAL signed boundary form

    B_delta=H+(1-delta)N-P_pole, 0<=delta<=1/3.

Its full positive edge envelope satisfies

    A_delta=H+(1-delta)N+P_pole<=101 B_delta,           (18)

using the SAME central spatial mean, the exact negative pole rank-one
term, and the published strong-row boundary coercivity, exactly as in
Section5 of the prior Schur theorem. Applying (17) to every edge and
then Cauchy in this complete positive edge measure yields

 |B_DZ|<=(101/190)sqrt(B_D B_Z),
 (89/190)(B_D+B_Z)<=E B_delta[D+Z]
                         <=(291/190)(B_D+B_Z).       (19)

All Gamma-wall, reflected prime-power and pole terms retain their original
coefficients. The profile's moving mean m(x), the first nonzero residual
at label1, and both triangular kernels in (1) are included.

For any finite families of amplitudes and residuals with the same profile
and posterior, their Gram matrices obey

    [[G_D,C],[C*,G_Z]] >=(89/190)diag(G_D,G_Z).         (20)

If their forward domains are finite, the same all-edge estimate also gives
 |F_DZ|<=(1/190)sqrt(F_D F_Z), with no factor101 because F is a positive
edge form. This is not a uniform Schur angle in Q_delta near its kernel.

## 7. Actual domain and signed scope

The actual current projection D has finite genuine spatial and original
star-forward energy by the centered profile theorem. Its residual is
Z=W-u-D, so the already paid actual star-current domains give finite
expected original P energy for Z as well. Alternatively the boundary
conclusion (19) only needs finite positive component expectations; these
follow from the conditional variance bounds T|D|^2,T|Z|^2<=V<=J and the
bounded actual J together with the complete theta boundary rows.
No random original-P membership is inferred solely from a marginal bound.

The proof is homogeneous and works with finite linear combinations;
common cutoff limits follow by the finite positive boundary measures and
Cauchy. Every finite Mobius cutoff N>=3 obeys the same estimates and keeps
its genuine omitted-divisor boundary in its separate spatial equation.

Together with the independently proved positive spatial factor for D,
(19) supplies a genuine complete mixed-boundary block for the arithmetic
projection. It does not delete the original boundary of Z, the signed
true-divisor incidence of the residual, or the moving-profile spatial
cross term. No full coefficient-one comparison or RH exclusion follows
from this block alone.
