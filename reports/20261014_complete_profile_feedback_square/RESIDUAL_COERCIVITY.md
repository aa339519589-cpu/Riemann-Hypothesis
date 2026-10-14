# Complete forward coercivity of the SAME orthogonal Mobius residual

The actual arithmetic residual has a nonzero label1 coordinate. It cannot
be inserted into the earlier root-zero incidence formula unchanged. Here
that coordinate is paid in the SAME star edge norm, and its full reset
and Gamma/prime commutators remain in the exact identity. The result is a
single joint forward-energy/score comparison for the genuine residual.
The full original reflected/pole boundary is not asserted to be paid at
coefficient one.

## 1. One arithmetic residual and two different profiles

Use the centered Mobius projection and residual of
[the complete boundary Schur proof](../20261014_centered_mobius_profile/BOUNDARY_SCHUR.md).
Let a_ar(n)=1-mu_ar(n), or its genuine finite version N>=3. Let Z satisfy

    T Z=0, T(a_ar Z)=0,
    b(x)=Z_1(x), xi_n(x)=Z_n(x)-b(x).

Thus xi_1=0 but T xi=-b, not zero. Write a_n for the POSITIVE RESET score,
not a_ar, and set

    E_a=int psi^2 T[a|Z|^2], E_a,xi=int psi^2 sum_(n>=2)p_n a_n|xi_n|^2,
    F_Z=F_star[Z] (expected original energy), F_b=F[b],
    c_0=401/40000.

Every F has ONE original forward Gamma-plus-prime orientation. The actual
Z has the finite hidden and original star domains proved by the centered
profile theorem and subtraction from the full current field.

## 2. The label1 function is small in the SAME full edge norm

For x<y, let l_n=p_n(x)-p_n(y), t=p_2(y)/p_2(x), and
c_n=2-a_ar(n), n>=2. Then c_2=c_3=0 and 0<=c_n<=2. The exact constraints
give 2p_1 b=-sum_(n>=4)p_n c_n Z_n. Subtract at x,y and regroup:

 2p_1(x)[b(x)-b(y)]
  =-sum_(n>=4)p_n(y)c_n[Z_n(x)-Z_n(y)]
   -sum_(n>=4)l_n c_n[Z_n(x)-b(y)]
   +[m(x)-m(y)]b(y), m=T a_ar.                       (1)

The SAME star edge square is

 S_Z=sum_(n>=2)p_n(y)|Z_n(x)-Z_n(y)|^2
       +sum_(n>=2)l_n|Z_n(x)-b(y)|^2
       +p_1(x)|b(x)-b(y)|^2.                         (2)

Cauchy in the first two disjoint channels of (1) bounds their joint
absolute value by 2sqrt(P_4(x))sqrt(S_Z), P_4=sum_(n>=4)p_n.
The already proved complete bounds are

 P_4<1/10000, p_1>400/401, q/p_1<1/400,
 |b(y)|<=sqrt(P_4(y))sqrt(T_y|Z|^2)/p_1(y),
 m(x)-m(y)<=(5/2)m(x)(1-t), m<=2q,
 S_Z>=(1-sqrt(t))[T_x|Z|^2+T_y|Z|^2].                (3)

They hold for the genuine infinite profile and every N>=3. Since
(1+sqrt(t))sqrt(1-sqrt(t))<=2, (1)-(3) give

 |b(x)-b(y)|
  <=[401/40000+401/3200000]sqrt(S_Z)
   =(32481/3200000)sqrt(S_Z)<sqrt(S_Z)/90.             (4)

This proves a genuine energy bound, not a small-amplitude inference:

    F_Gamma[b]<=F_Gamma,Z/8100,
    F_prime[b]<=F_prime,Z/8100,
    F_b<=F_Z/8100.                                   (5)

The same all-edge estimate applies to each positive boundary component
if desired, but only (5) is spent below.

## 3. Exact root-zero reduction, including both omitted terms

Let A_sp be the genuine hidden spatial generator, G the observed future
generator, and F_n^0 the full mismatch row

 F_n^0(b)=sum_(d|n)lambda_d[b(x+log d)-b(x)]
                 -int(q_1-q_n)(x,dy)[b(y)-b(x)].

Define the exact scalar pairings

 R_b=int psi^2 conj(b) T[a Z],
 C_b=int psi^2 sum_(n>=2)p_n conj(Z_n) F_n^0(b),
 T_xi=sum_d int K_d(x)sum_(m>=2)p_m(y)conj(xi_m(y))
                                     [xi_(dm)(x)-xi_m(x)].

Then the COMPLETE energy identity is

    E_full[Z]=F_Z+2E_a-2 Re R_b-2 Re T_xi-2 Re C_b.    (6)

Here E_full includes the same hidden Gamma, every true divisor and the
complete refresh. In particular neither R_b nor C_b is zero by the
arithmetic orthogonality T(a_ar Z)=0: a_ar is not the reset score.

To verify (6), first use the general root-zero spatial formula and the
full refresh square, without imposing T xi=0:

 E_full[xi]-F_star[xi]
  =2int psi^2{T[a|xi|^2]-Re[(T xi)conj(T[a xi])]}-2 Re T_xi.

Since T xi=-b and T[a xi]=T[a Z]-beta b, its braces equal
T[a|Z|^2]-Re[conj(b)T(aZ)]. For the deterministic b, the full paired
intertwining T A=G T gives

 E_sp(xi,b)-F_star(xi,b)
      =int psi^2 T[conj(Z)(A_sp b-Gb)]=-C_b.

Indeed A_sp,n b-A_sp,1 b=-F_n^0(b), while T Z=0 removes the common
label1 row. Refresh has zero cross with deterministic b. Expanding
Z=xi+b now gives (6), retaining the true origin and all divisor branches.

## 4. Pay the reset, parent and mismatch terms only once

The root constraint actually gives the sharper rare-label bound

    |b|^2<=(P_4/p_1^2)sum_(n>=4)p_n|Z_n|^2.

Retain this restricted sum before using beta<a_n on n>=4. One must NOT
replace it by the full V_Z and then assert beta V_Z<=T(a|Z|^2), since
a_1 may be below beta. The restricted bound proves

    int psi^2 beta|b|^2<=c_0^2 E_a.                    (7)

Weighted Cauchy therefore gives |R_b|<=c_0 E_a.
The complete tail reset mean is T_tail a<beta/50. Thus Minkowski gives

    sqrt(E_a,xi)<=(1+c_0/sqrt(50))sqrt(E_a)
                      <=(1+c_0/7)sqrt(E_a).          (8)

Because T Z=0, the SAME star mean cross with deterministic b vanishes:

    F_prime,star[xi]=F_prime,Z+F_prime[b]
                         <=(8101/8100)F_prime,Z.      (9)

The complete parent-union and incoming cooling proof in
[the incidence theorem](COMPLETE_INCIDENCE.md)
does not require T xi=0 for its estimate of T_xi. Combining it with
(8)-(9) yields

 |T_xi|^2<=(5/3)(1+c_0/7)^2(8101/8100)E_a F_prime,Z
                       <=(169/100)E_a F_prime,Z.     (10)

For clarity the exact coefficient is
70770984800989/42336000000000, less than169/100 by
776855199011/42336000000000. All parent divisors are paid as one union.

The mismatch retains its complete signed union. Its positive row masses
obey M_n=int(q_1-q_n)=L_n-a_n+a_1<L_n and L_n<=4a_n/3. Cauchy first in
the signed Gamma-plus-divisor union and then in labels gives

 |C_b|^2<=(8/3)E_a [F_prime[b]+F_extraGamma[b]].         (11)

The exact posterior identity makes the extra-Gamma kernel q_1-q_observed,
which is at most the original Gamma kernel divided by400. In particular
(5),(11) imply

    |C_b|^2<=(8/24300)E_a F_Z<E_a F_Z/55^2.           (12)

Neither the positive reset score nor F_Z is independently respent for
individual prime or Gamma entries: (10)-(12) are inserted together into
ONE identity (6).

## 5. A single joint full-residual comparison

Equations (6)-(12) give

 E_full[Z]>=F_Z+(39599/20000)E_a
                         -(29/11)sqrt(E_a F_Z).      (13)

The positive coefficient is 2-2c_0; the cross coefficient is
2(13/10+1/55)=29/11. The exact rational comparison

 (9/10)[39599/20000-1/25]-(29/22)^2
                          =202111/24200000>0

then proves the joint bound

    E_full[Z]>=F_Z/10+E_a/25.                         (14)

This one allocation keeps part of the complete reset score as well as
part of the full original forward form. It may not be added to (13) or
to the old root-zero allocation as a second resource. Complex and
finite-family versions follow from the same norms and polarization.

## 6. Common domains and the remaining signed comparison

The actual mu projection and Z already have finite hidden and star forms.
Equation (4) directly pays the deterministic b's original forward domain;
its source is also explicitly b=e+mA, a sum of two already lawful original-P
sources. Equations (7)-(8) pay all shifted root-zero score norms. The
single complete incidence estimate proves T_xi absolutely convergent;
(11) proves the grouped mismatch pairing finite without introducing
separate infinite Gamma diagonals. One may verify (6) at common spatial,
label and small-jump cutoffs and then pass by these form bounds.
No ordinary-L2 claim is made for a backward prime row.

All terms in (14) belong to the SAME actual arithmetic residual. The
complete original B_delta[Z], the spatial mixed pairing with the centered
Mobius principal, and the source stationarity corrections remain. Since
(14) has coefficient1/10, it is not a proof that2E_full[Z]>=B_delta[Z].
The theorem closes a nontrivial full-forward residual comparison, not
an RH exclusion or a free second reset budget.
