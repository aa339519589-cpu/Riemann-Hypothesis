# Positive second-label damping in the same actual signed reset equation

This is an EXACT signed completion, not an absolute-value estimate of the
whole reset forcing. The dominant label2 contribution is moved to positive
killing. Every remaining label, true divisor, Gamma row, and original
source restriction is retained. The resulting positive killing does not
by itself cure the original theta-weighted inverse problem.

## 1. Same current and coefficient conventions

Use the full-band eta current field and original-domain first-label test
of [the first-label theorem](../20261014_first_label_current_approximation/REPORT.md).
Let

    p_n=n^(-1/2)eta(x+log n)/Phi(x), s=psi/Phi,
    beta=K/psi, K=3Phi+Theta/2,
    a_n=beta_n-(A_eta s)_n/s>0, T a=beta,
    T w=u, H_n=w_n-u, e=H_1=w_1-u.

All equations below concern THIS actual current-adapted field. They do not
assert that the individual label fields are canonical Mobius seeds or that
all psi w_n are original-P sources. Only psi w_1 has that proved status.
Write G1 for the continuous source generator with S1=psi p_1=eta s.
The independently justified actual first-refresh equation is

    (G1+beta)e=D u+T(aH), D=G_psi-G1.                 (1)

Here D=G_prime,psi-G_extra has its original opposite channel signs.
Its stopped and killed-potential meaning, including the genuine operational
origin, is established in
[KILLED_EQUATION.md](KILLED_EQUATION.md).

## 2. Coefficient ordering: label2 is the smallest true tail reset score

Set s_d=s(x+log d). Split the exact reset score as

    s a_n=C_n+D_n,
    C_n=s beta_n+int_0^infinity kappa(h)
                  eta(x+log n+h)/eta(x+log n)[s(x+h)-s(x)]dh,
    D_n=sum_(d|n)Lambda(d)(s_d-s).                    (2)

Every C_n is positive. It decreases with n. To check this, beta_n decreases,
and for a fixed h>0 put r=exp(2h), P(w)=4w^2-6w. The eta future ratio is
exp(h/2)P(rw)exp[-w(r-1)]/P(w); its logarithmic w derivative is

    -(r-1){1+(3/2)/[(rw-3/2)(w-3/2)]}<0.

Thus 0<C_n<=C_1=s a_1. Since T a=beta and p_1>=400/401,

    C_1<=K/(Phi p_1)<C0:= (121/40)(401/400)
                           =48521/16000.            (3)

For (3), the complete theta sum gives Theta/Phi<=1/P(z)<1/20,
z=pi exp(2x)>=pi>157/50. No first-label truncation replaces Phi.

The exact score estimate s'-2s>3, proved in
[THETA_SCORE.md](../20261014_first_label_current_approximation/THETA_SCORE.md),
implies for every h>0

    s(x+h)>exp(2h)s(x)+(3/2)[exp(2h)-1].             (4)

In particular s_2>4s+9/2. From (2)-(3),

    s(a_2-a_1)>3(log2)s+(9/2)log2-C0,
    a_2-a_1>3log2.                                  (5)

The constant discarded in the second line is STRICTLY positive:
(9/2)log2>(9/2)(69/100)=621/200>C0. The elementary logarithm bound follows,
for example, from log2=2sum_(j>=0)(1/3)^(2j+1)/(2j+1)>56/81>69/100.

For EVERY n>=3, one also has a_n>a_2. Here is the full divisor argument,
including composites.

* If n is odd, it has a prime divisor p>=3. Consequently
  D_n-D_2>=log2(s_3-s_2). Applying (4) between x+log2 and x+log3, and then
  using s_2>9/2, gives s_3-s_2>15/2. Thus
  D_n-D_2>(15/2)log2>C0.
* If 4 divides n, the true divisors2 and4 both occur. Their Mangoldt weights
  are both log2, so D_n-D_2>=log2(s_4-s)>(45/2)log2>C0.
* If n is even but not divisible by4 and n>=3, it has an odd prime divisor
  p>=3 in addition to2. Hence D_n-D_2>=log3(s_3-s)>12log3>C0.

In each case C_n-C_2>=-C0, so (2) proves the asserted strict ordering.
No false monotonicity of a_n in EVERY integer n is needed or claimed.

Define

    kappa_2(x)=p_1(x)[a_2(x)-a_1(x)].

Equations (3)-(5) prove the uniform positive bound

    kappa_2>(400/401)3log2>828/401>2.                 (6)

## 3. The exact signed cancellation and its complete residual

Because T H=0 and H_1=e, simple centering gives exactly

    T(aH)=-kappa_2 e+R_3,
    R_3=sum_(n>=3)p_n(a_n-a_2)H_n.                  (7)

Thus the actual equation (1) is

    (G1+beta+kappa_2)e=D u+R_3.                     (8)

The n2 term has become POSITIVE killing. No sign of e, H_n, u or the
remaining forcing is assumed. In particular no monotone-current order
or positivity cone for the actual eigen-source is used.

The ordering in Section2 implies

    |R_3|^2 <= T_(n>=3)a_n * T(a_n |H_n|^2).         (9)

Indeed (a_n-a_2)^2/a_n<=a_n on n>=3, and weighted Cauchy--Schwarz proves
(9). This is the SAME weighted reset-square channel as before, not a new
independent budget.

## 4. The entire label>=3 reset mass is less than beta/200000

Put epsilon_3=sum_(n>=3)p_n/p_1. The scalar beta_n and the eta Gamma future
ratios decrease in n, and every tail posterior coordinate decreases with x.
Exactly as in the complete refresh-row calculation, the scalar-plus-Gamma
part of T_(n>=3)a is at most epsilon_3 beta. The divisor part is bounded by
its full positive rate, with its label2 contribution removed EXACTLY:

    T_(n>=3)L_n =lambda_p-p_2(log2)s_2/s,
    L_n=sum_(d|n)Lambda(d)s_d/s,
    lambda_p=F_+psi/psi.

The exact posterior identity gives

    T_(n>=3)L_n/beta
       =[sum_(d>=3)alpha_d psi(x+log d)
           +alpha_2 psi(x+log2)(1-p_1(x+log2))]/K.   (10)

Thus all divisor multiplicities and the moving cutoff label2 are retained.
Using the complete theta bounds and the divisor identity
sum_(d|l)Lambda(d)=log l, as in the all-prime reset estimate,

    sum_(d>=3)alpha_d psi(x+log d)/K
       <=(4/3)z sum_(l>=3)l^6 log(l)exp[-z(l^2-1)]
       <17496/16^8.                                (11)

For detail, z exp[-z(l^2-1)] decreases for z>=3, log l<=l, and the
resulting series is bounded by twice its first term:
4sum_(l>=3)l^7 exp[-3(l^2-1)]<8*3^7 exp(-24)<17496/16^8.
The consecutive ratio is at most (4/3)^7 exp(-21)<1/2.
Similarly the COMPLETE posterior tail obeys

    epsilon_3<=2sum_(n>=3)n^4 exp[-z(n^2-1)]
                 <324/16^8.                        (12)

The consecutive ratio is at most (4/3)^4 exp(-21)<1/2. Finally the second
term in (10) is at most

    [F_+psi/K]epsilon(x+log2)<7/(400*2^42).          (13)

Here the full all-prime bound F_+psi/K<7/400 and the complete shifted
posterior bound epsilon(x+log2)<2^(-42) are already proved, not assumed
finite cutoffs. Combining (10)-(13),

    T_(n>=3)a/beta
       <17820/16^8+7/(400*2^42)<1/200000.            (14)

Consequently the remaining SIGNED forcing in (8) has the precise estimate

    |R_3|^2/beta <=(1/200000)T(a|H|^2).             (15)

## 5. The retained Gaussian factor and actual forcing restriction

The complete proof above gives a useful nonuniform estimate BEFORE any
numerical supremum is taken. Keeping z in all exponential tails,

    T_(n>=3)a/beta <=B_3(z),
    B_3(z)=(324+5832z)exp(-8z)+1680z exp(-15z).       (16)

Indeed (12) gives324 exp(-8z), the complete series in (11) is at most
(8/3)z*3^7 exp(-8z)=5832z exp(-8z), and the shifted label2 remainder is
at most[60z exp(-3z)][28exp(-12z)]. Thus

    |R_3|^2/beta <=B_3(z)T(a|H|^2).                 (17)

The uniform1/200000 bound and (16) are BOTH valid; neither replaces the
other when a changed metric is involved.

The actual logarithmic label control yields an even stronger absolute
forcing envelope. The complete posterior has E n^2<17/16, directly from
2sum_(n>=2)n^4(n^2-1)exp[-z(n^2-1)]<1/16. Thus s(x+log d)<(17/8)d^2z.
From (2)-(3) and beta s=K/Phi>=3,

    a_n/beta <=401/400+(17/24)z n^2 log n.

Since |H_n|<=C_sigma||u||Hs(1+log n), the positive tail in (7) and the
complete Gaussian label series prove

    |R_3(x)|<=C_sigma'||u||Hs beta(x)(1+z)exp(-8z).   (18)

The constant is independent of x and comes from a convergent complete
label series after factoring exp(-8z); no actual forcing pulse is varied
independently of u.

The two opposite-sign rows in D have the separately proved envelopes

    lambda_prime/beta <=60z exp(-3z),
    lambda_extra/beta <=(336/5)z exp(-3z).

Consequently their GROUPED actual forcing satisfies

    |D u|<=(1272/5)||u||infinity beta z exp(-3z).      (19)

It is the remaining leading far-tail term; R_3 has the stronger exponent8.
These actual Gaussian envelopes justify the larger metric used in
[COERCIVE_INVERSE.md](COERCIVE_INVERSE.md), but alone do not give a full
signed original-form comparison. The dependence on the same
u, the exact mismatch signs and the same reset square in (17) must remain.

## 6. The exact asymptotic killing

The complete theta expansion gives p_1->1 and
s(x+log2)/s(x)->4. Equations (2)-(3) give C_1/s,C_2/s->0. Therefore

    a_1->0, a_2->3log2,
    kappa_2->3log2, beta->0.                         (20)

This is a positive constant asymptotic killing, unlike beta alone.
The honest first-refresh representation can be localized with the extra
positive factor exp[-int kappa_2] to give a positive killed potential for
(8). The actual e and forcing retain their already proved Gaussian-small
relation to the SAME u; no generic forcing class is substituted.

