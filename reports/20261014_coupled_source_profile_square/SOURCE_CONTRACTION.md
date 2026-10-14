# A strict complete projected-source contraction in the TRUE variance dual norm

This is a source-operator comparison in the original forward Gamma/prime
metric. It retains the whole continuous/profile cross and EVERY prime
power of the exact projected Mobius source. A specific prime 2 routing,
not a false full-prime/Gamma domination, pays the leading mismatch. The
result does not identify this forward metric with the full original Q
form, and does not license iteration on transformed current sources.

Dependencies: [reset/profile facts](RESET_FACTS.md),
[the true-variance principal](TRUE_VARIANCE_METRIC.md), and the published
[complete two-group indicator balance](../20261014_same_current_star_blocks/TWO_GROUP_SPATIAL.md).

## 1. Exact profile, source and norm

Use the genuine complete arithmetic profile a(n)=1-mu_ar(n), or its
natural finite version a_N(n)=1-mu_ar(n)1_(n<=N), N>=3. Write

    m=T a, M=T a^2, sigma^2=M-m^2,
    kappa_a=T[c(a-m)^2]/sigma^2, beta=T c,
    lambda_0=beta+kappa_a+23/200.

Here c_n is the POSITIVE reset score; a is the arithmetic profile. The
same true conditional-variance principal is coercive with the pointwise
weight lambda_0, since its exact constant shift minus its two bounded
Gamma/prime defects is greater than 23/200. This retains kappa_a rather
than replacing the full score by a weaker constant.

For a source ratio u define its EXACT complete projected mismatch

 S_a u=-Gamma_cont(m,u)
       +sum_(d>=2)r_d(x)[A_d(y)-m(x)][u(x)-u(y)],
 y=x+log d, A_d(y)=T_y a(dm),
 r_d(x)=Lambda(d)d^(-1/2)psi(y)/psi(x).

Every sum over d contains every true prime power, including d>N at a
finite mask. Off-site cancellations of the projected principal do not
remove any of these source terms. Put

 ||f||_*^2=int_0^infinity psi(x)^2 |f(x)|^2
                                     /[lambda_0(x)sigma(x)^2] dx,
 F[u]=F_Gamma[u]+F_2[u]+F_high[u],
 F_high[u]=sum_(d>=3)int psi^2 r_d|u(x)-u(x+log d)|^2 dx.

All F energies have ONE original forward orientation. The theorem is

    ||S_a u||_*^2 <=(124633/125000)F[u].              (1)

The coefficient is strictly below one. At zero input energy both sides
are zero; no strict pointwise norm inequality at zero is asserted.
The bound is uniform in all the stated genuine masks and is a finite-
family operator/Gram inequality by polarization.

## 2. Keep the true second-label score in the denominator

The complete posterior bounds give p_1>400/401 and q/p_1<1/400,
q=1-p_1. Since a(1)=0, a(2)=2, 0<=a<=2,

 sigma^2>=4p_1p_2, m^2/sigma^2<=q/p_1<1/400.

All reset scores c_n for n>=2 are at least c_2. The fraction of the
profile variance at label 1 is p_1m^2/sigma^2<1/400. Consequently

 kappa_a>=(399/400)c_2,
 c_2>=L_2-log2, L_2=log2*s(x+log2)/s(x)>=4log2.       (2)

The last two inequalities follow from the COMPLETE positive reset score
and s(x+log2)/s(x)>=4; no Gamma component was subtracted with a negative
sign. The genuine posterior/divisor flux is exactly

    r_2(x)p_1(x+log2)=p_2(x)L_2(x).                 (3)

We claim

 lambda_0 >=(25/32)(401/400)^2 L_2
                   >=(25/32)L_2/[p_1(x)p_1(x+log2)]. (4)

Indeed its difference from the first right side is bounded below by

 [399/400-(25/32)(401/400)^2]L_2
                         -(399/400)log2+23/200
 >=[-1517/10240]log2+23/200
 >1157/102400>0,

using L_2>=4log2 and log2<7/10. Combining (3)-(4) with the variance floor
therefore proves

    r_2/(lambda_0 sigma^2)<=8/25.                   (5)

This is where replacing kappa_a by2 beta+21/10 too early would lose the
necessary origin scale. The denominator in (5) is the genuine conditional
variance metric of the projected principal.

## 3. The COMPLETE higher-prime row is small relative to prime 2

Write theta_c(z)=exp(-x/2)psi(x)=sum_(n>=1)c(n^2z)exp(-n^2z),
c(t)=8t^3-30t^2+15t. Let r_high=sum_(d>=3)r_d. For z>=pi>3,

 theta_c(4z)>=(11/2)(4z)^3 exp(-4z)=352z^3exp(-4z).

The numerator sum retains the full divisor identity before taking an
upper bound:

 sum_(d>=3)Lambda(d)theta_c(d^2z)
   <=8z^3 sum_(l>=3)l^6 exp(-l^2z)
                           sum_(d|l,d>=3)Lambda(d)
   <=8z^3 sum_(l>=3)l^6 log(l)exp(-l^2z).

Thus log(l)<=l and the COMPLETE consecutive Gaussian tail imply

 r_high/r_2
   <=[1/(44log2)]sum_(l>=3)l^7 exp[-(l^2-4)z]
   <[2*2187/(44*(69/100))]exp(-15)
   <729/16192000<1/20000.                            (6)

Here log2>69/100, exp3>20, and the tail ratio is at most
(4/3)^7 exp(-21)<1/2. Non-prime-power integers occur only in the safe
upper sum. No true prime power or finite-mask source boundary was omitted.

## 4. Exact continuous-profile source cost

Every tail posterior coordinate decreases. Therefore m decreases,
0<=m<=2q, and

 Gamma_cont(m)<=m G_cont m<=2m G_cont q<=4q r_prime.   (7)

The last step is the exact complete two-group indicator identity
 G_cont q=p_1[r_prime-q(abar-c_1)]<=r_prime;
its true divisor death into label 1 is retained. Cauchy in the original
continuous rate kernel, followed by (5)-(6), gives

 ||Gamma_cont(m,u)||_*^2
   <=sup_x [Gamma_cont(m)/(lambda_0 sigma^2)] F_Gamma[u]
   <=[4/401]*(8/25)*(20001/20000)F_Gamma[u]
   <=(2/625)F_Gamma[u].                             (8)

This is the complete Gamma/profile forcing, including its mixed source
increments. It is not bounded merely by the profile amplitude.

## 5. Prime2 and the remaining prime powers use disjoint source budgets

The exact coefficient satisfies |A_d(y)-m(x)|<=2. Hence (5) gives for
S_2=r_2[A_2-m]Delta_2u,

    ||S_2||_*^2 <=(32/25)F_2[u].                    (9)

Cauchy in the COMPLETE d>=3 row, then (5)-(6), similarly gives

 ||S_high||_*^2
    <=sup_x [4r_high/(lambda_0 sigma^2)] F_high[u]
    <=F_high[u]/15625.                              (10)

The smallness in (10) is applied to the genuine HIGHER source row,
not to all primes after its leading d=2 coordinate has been spent.
Every higher prime power remains in F_high and S_high.

The independently certified original graph routing is

    F_2[u]<=(11/4)F_Gamma[u].                        (11)

It is the [single-prime 2 theorem](PRIME_TWO_ROUTING.md),
with the full directed theta certificate and both return orientations.
No universal F_prime<=C F_Gamma assertion is made.

## 6. Joint continuous/prime 2 cross, then the whole source

Minkowski retains a possible worst sign of the continuous/prime 2 cross:

 ||-Gamma_cont(m,u)+S_2||_*
   <=sqrt((2/625)F_Gamma)+sqrt((32/25)F_2).

For t=F_2/F_Gamma in[0,11/4], the squared ratio to F_Gamma+F_2 is

    f(t)=[sqrt(2/625)+sqrt((32/25)t)]^2/(1+t).

It increases on this interval, since its unconstrained maximum is at
t=(32/25)/(2/625)=400. At t=11/4, direct rational squaring gives

    f(11/4)<997/1000.                               (12)

Precisely, after subtracting the two square terms from
(997/1000)(15/4), the positive remainder is4311/20000;
its square exceeds4*(32/25)*(2/625)*(11/4) by
562321/400000000. If F_Gamma=0, (11) makes F_2=0 and the same estimate
holds without division. Thus (12) pays BOTH channels with the single
budget F_Gamma+F_2.

Finally use Minkowski with S_high and the two-coordinate Cauchy inequality
in the disjoint energy budgets:

 ||S_a u||_*
  <=sqrt((997/1000)(F_Gamma+F_2))
                                      +sqrt(F_high/15625)
  <=sqrt((997/1000+1/15625)F[u]).                    (13)

Since 997/1000+1/15625=124633/125000, this is (1). The positive margin
is367/125000. The source-gradient cross has not been set to zero, and
no Gamma energy is used again for the complete higher-prime block.

## 7. Domain, actual use and the remaining original sign

For finite F, the source series and the continuous pairing exist almost
everywhere by the same row Cauchy estimates; the target dual norm is
finite by (1). Common compact/finite-prime limits converge in that norm.
The full inequalities therefore extend the exact projected mismatch
from the original form core, modulo its constant gauge. Complex and
Hilbert-valued inputs obey the same proofs. For the actual source this
is precisely the forcing in the projected current equation, not a
canonical Mobius seed and not an eigenstate-invariant transformation.

The true-variance principal retains its positive half-line Gamma term,
its exact conditional storage interpretation, and the same orthogonal
reset/collision forcing. Equation (1) must be inserted together with
those identities and the complete original Gamma-wall/reflected-prime/
pole boundary. It is a strict original-F-to-conditional-dual source
comparison, NOT positivity of the whole Q form or a proof of RH.
