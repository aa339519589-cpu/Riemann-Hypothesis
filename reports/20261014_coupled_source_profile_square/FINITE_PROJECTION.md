# Exact finite Mobius projection: only prime off-site coefficients, with parent-6 residual

This is a same-current arithmetic identity at EVERY finite cutoff. All
higher prime powers remain in the true diagonal and in the actual source
forcing, but disappear exactly from the projected off-site coefficient and
orthogonal residual. After the two genuine orthogonality constraints are
used, the entire residual incidence starts at initial label 6, not 4.
No canonical-seed/current identification or favorable whole-form sign is
asserted.

Use the notation and exact finite reset completion of
[the finite reset facts](RESET_FACTS.md).
For N>=2 let a_N(n)=1-mu_ar(n)1_(n<=N), m=T a_N, sigma^2=Var_p(a_N),
H=w-u, h=T(a_N H)=sigma^2 A, and

    H_n=A[a_N(n)-m]+Z_n, T Z=T(a_N Z)=0,
    kappa=T[c(a_N-m)^2]/sigma^2,
    r=-T[c(a_N-m)Z], beta=T c.

All symbols below are for this SAME N and source. Every expectation at a
future point y uses its full posterior p_n(y).

## 1. Exact covariance coefficient and the complete finite union

For a true prime power d define

    gamma_(d,N)(y)=-Cov_y(a_N(dm),a_N(m)).

If d=p^k, k>=2, then a_N(dm)=1 for ALL m, even before the cutoff limit.
Consequently gamma_(d,N)=0. For a prime p put

 B_(p,N)=sum_(m<=N/p,p not dividing m)p_m mu_ar(m)^2,
 C_(p,N)=sum_(m<=N/p,p not dividing m)p_m mu_ar(m),
 A_mu,N=T mu_N=1-m, mu_N=mu_ar1_(n<=N).

The elementary identity
mu_N(pm)=-mu_ar(m)1_(m<=N/p,p not dividing m) gives exactly

    gamma_(p,N)=B_(p,N)-A_mu,N C_(p,N),
    0<=gamma_(p,N)<=sigma^2.                         (1)

Indeed 0<A_mu,N<1, and each summand
mu_ar(m)^2[1-A_mu,N mu_ar(m)] is nonnegative. The upper bound is not a
norm estimate: the exact missing part is

 sigma^2-gamma_(p,N)
   =sum_(m<=N, [p divides m OR m>N/p])
          p_m mu_ar(m)^2[1-A_mu,N mu_ar(m)].          (2)

The UNION is counted once. It includes both the square collision and the
finite child-cutoff boundary. In particular gamma_(p,N)=0 when p>N.
No omitted prime branch is assigned zero before (2) is combined.

## 2. Full projected current equation

Let G_cont be the original continuous positive generator, r_d its true
observed prime-power rates, lambda_prime=sum_d r_d, and A_sp the genuine
hidden continuous-plus-divisor generator. Define the complete source
mismatch

 S_N(u)=T[(a_N-m)A_sp Uu]
   =int q_Gamma(x,dy)[m(y)-m(x)][u(x)-u(y)]
       +sum_d r_d(x)[T_y a_N(dm)-m(x)][u(x)-u(y)],    (3)
    y=x+log d.

Every prime power, including d>N, occurs in (3). Its continuous and prime
channels have their original opposite signs. The actual source u has
not been replaced by a projected or neutral field.

The exact projected equation is

 (G_cont+lambda_prime+kappa)h(x)
       +sum_(p prime,p<=N)r_p(x)
               [gamma_(p,N)(y)/sigma(y)^2]h(y)
       =-S_N(u)(x)+r(x)+I_N(Z)(x), y=x+log p.       (4)

Thus the surviving prime off-site coefficient lies in [0,1], with a PLUS
sign. This is not a Markov difference; its sign remains explicit.
All higher prime powers still occur in lambda_prime and S_N(u).

To verify (4), start with the full masked-current product identity

 (G+kappa)h=Gamma_G(m,u)
      +sum_d r_d T_y[(a_N(dm)-a_N(m))(w_m(y)-u(x))]+r.

The part involving u(y)-u(x) combines with Gamma_G(m,u) into -S_N(u).
The projected part is

 T_y[(a_N(dm)-a_N(m))A(y)(a_N(m)-m(y))]
       =-h(y)-gamma_(d,N)(y)A(y).

Its -h(y) cancels the corresponding negative future term in G EXACTLY,
leaving lambda_prime on the diagonal. The remaining part is

    I_N(Z)=sum_d r_d T_y[a_N(dm)Z_m],                (5)

because T(a_N Z)=0. Higher powers have constant parent profile1, so their
part of (5) is0 by T Z=0. For p>N the parent profile is likewise1, so its
part is0. These are exact cancellations, not truncations of the source
operator.

Equivalently, before the next orthogonal cancellation, the prime residual is

 T_y[a_N(pm)Z_m]
   =-sum_(m<=N,[p divides m OR m>N/p])p_m(y)mu_ar(m)Z_m(y). (6)

For p>N the entire right side of (6) is0 by T(mu_N Z)=0. The complete
union must be combined before taking this zero or passing a prime limit.

## 3. The full orthogonal residual starts at initial label 6

Subtract the affine interpolant through child labels1,2:

 j_(p,N)(m)=a_N(pm)-a_N(p)
              -[a_N(2p)-a_N(p)]a_N(m)/2.           (7)

Both constraints on Z give exactly

    T_y[a_N(pm)Z_m]=T_y[j_(p,N)(m)Z_m].

For every prime p and every N>=2,

    j_(p,N)(1)=j_(p,N)(2)=0,
    |j_(p,N)(m)|<=1,
    j_(p,N)=0 if p>N.                              (8)

For the absolute bound, if p<=N<2p the interpolant is2-a_N/2, while
all parents pm with m>=2 lie past the cutoff and equal1. If 2p<=N and
p is odd the interpolant is2-a_N, and the exact fresh-prime/cutoff cases
give values in {-1,0,1}. For p=2 the interpolant is2-a_N/2 because
mu_N(4)=0; the squarefree and repeated-prime cases give values in
{-1,-1/2,0}. These cases include m>N. If p>N every profile value at p,2p,
pm is1, so (7) vanishes identically.

In the complete limit,

 j_p(m)=-mu_ar(pm)-mu_ar(m)
       =-mu_ar(m)1_(p divides m), p odd;
 j_2(m)=-mu_ar(2m)-[1+mu_ar(m)]/2 in {0,-1/2,-1}.   (9)

Thus p=2 first acts on child3, initial parent6. Odd primes first have a
nonzero square-collision child at least p, initial parent at least p^2>=9.
The disappearance of parent4 is due to the TWO actual orthogonality
constraints, not to an artificial deletion of the square-collision term.

The exact finite boundary is

 j_(p,N)-j_p
  =[a_N(pm)-a(pm)]-[a_N(p)-a(p)]
   -(1/2){[a_N(2p)-a_N(p)]a_N(m)-[a(2p)-a(p)]a(m)}. (10)

It has absolute value<=2 and support pm>N; both sides vanish for m=1,2.
For m>=3, pm<=N implies 2p,p,m<=N, proving the support claim. Thus the
finite affine boundary and prime transition have been retained together.

## 4. Operator and original-form scope

In the Gaussian variable the principal in (4) becomes exactly

 G_B+beta+kappa
   +sum_(p prime,p<=N)(log p)exp[-(p^2-1)z]
               [gamma_(p,N)/sigma^2](p^2z)E_(p^2).

The attenuation is in [0,1]. The companion [true-variance proof](TRUE_VARIANCE_METRIC.md)
pays this whole bounded prime perturbation in the precise conditional metric,
keeping its correct plus sign. Pointwise positive kernel entries alone
would not prove the required quadratic coercivity.

The main forcing -S_N(u) and the SAME score-orthogonal reset remainder r
remain in (4). Neither is assigned a favorable sign here. The complete original
Gamma-wall/reflected-prime/pole comparison still contains the centered
profile, residual and their genuine mixed cross. This theorem gives a
new exact arithmetic cancellation and the retained residual in that comparison,
not a full favorable sign or an RH proof.
