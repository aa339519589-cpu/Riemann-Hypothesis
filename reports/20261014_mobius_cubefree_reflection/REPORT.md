# Exact squarefree-part cancellation in the same future Möbius form

2026-10-14. This note continues the legal actual-source arithmetic test of [the original-metric anchored future theorem](../20261014_anchored_future_mobius/REPORT.md). It gives a genuine signed coefficient cancellation of the complete reflected-prime block. It is not a positivity theorem: the surviving squarefree-part signs and all Gamma/diagonal/anchor payments remain.

## Dependencies and reproducibility

All original P, N, Gamma, pole, source, and Fourier conventions are those of [the anchored future theorem](../20261014_anchored_future_mobius/REPORT.md), with [the complete prime reference](../20261013_full_prime_green_reference/REPORT.md). The distinction between the new simultaneous Möbius coefficient law and the existing one-prime grouping is explained in Section 5; the earlier factorization is [complete prime-power grouping](../20261014_signed_prime_block_tools/GROUPED_PRIME_POWER_FACTORIZATION.md). These relative paths were verified at commit f5966ade2f9b65c373655c73e58dd6a6fdefb650.

The proof in Section 3 is algebraic for every integer L and does not depend on a numerical cutoff. The accompanying [exact checker](check_cubefree_reflection.py) independently compares prime-log coefficient vectors on all open divisor cells through L=500. Run `python check_cubefree_reflection.py`; it writes [the small check result](cubefree_reflection_checks.json). All 2,690 cells pass. This certifies an algebraic implementation, not positivity or RH.

## 1. Actual test and complete source reflection

Fix the SAME actual source f=g used in the anchored future theorem. Define on x>=0

    M f(x)=sum_(n>=1)mu(n)n^(-1/2)f(x+log n),
    A=Mf, t=A(0), b=Phi/Phi(0), a=A-t b.

The centered representative a-8ell(a)psi is legal in the original P completion; P,N and Q_delta are unchanged by this final constant-ratio subtraction. All arithmetic coefficients below are the actual mu, not absolute values.

For any theta-decaying positive-half-line sources define the full reflected SOURCE pairing

    R(u,v)=sum_(k>=2)Lambda(k)k^(-1/2)
            integral_0^(log k) u(x)v(log k-x)dx.        (1)

This is not the whole N form; its full reflected diagonal V must still be retained. The pairing in (1) is symmetric. Unlike N, it is separately finite even for a nonzero trace, so R(A,A), R(A,b), and R(b,b) may be expanded individually.

## 2. Divisor-cut coefficient before cancellation

Directly expanding BOTH true future Möbius sums and setting L=kmn gives

 R(Mf,Mf)
   =sum_(L>=2)L^(-1/2) integral_0^(log L)
                   R_L^mu(y) f(y)f(log L-y)dy,          (2)

where, outside the finitely many divisor-log endpoints,

 R_L^mu(y)
   =sum_(m|e|L, m<exp(y)<e) mu(m)mu(L/e)Lambda(e/m).    (3)

Indeed set y=x+log m and e=km=L/n. The original interval 0<x<log k becomes log m<y<log e. Thus (3) retains the exact reflection cutoff for every prime power.

All expansions are absolutely justified on these future theta sources. The actual fixed-depth source bound gives |f(y)|<=C exp(Cy-c exp(2y)), y>=0, with fixed c>0. Consequently

 |f(y)f(log L-y)|
   <= C L^C exp[-c(exp(2y)+L^2 exp(-2y))]
   <= C L^C exp(-2cL).                                (4)

Elementary divisor and logarithmic bounds therefore sum the complete coefficient expansions in (2). This is a local future-source calculation, not a bilateral current Fubini assertion.

## 3. Full prime-power cancellation theorem

Write L=a b^2 if L is cube-free, with a,b squarefree and gcd(a,b)=1. Then

 R_L^mu(y)=0 if L is divisible by a prime cube,            (5)

and, in the cube-free case,

 R_(a b^2)^mu(y)
   =-mu(a) sum_(p|a)(log p)
        sum_(d|a/p) 1_(log(bd)<y<log(bpd)).               (6)

For a=1 the right side is zero. Thus the sign, where nonzero, is exactly -mu(a), depending only on the squarefree part a. The square factor b^2 produces a translation by log b, not a new sign.

Proof. Fix a prime p contributing through k=e/m=p^j in (3), and let v_p(L)=v. Since mu(m)mu(L/e) is nonzero only when both arguments are squarefree, every other prime exponent in L is at most two. Fix their allocation m0,n0, with p not dividing m0 n0 and m0 n0=L/p^v. Its common coefficient is mu(m0)mu(n0)log p.

The p-adic possibilities for m,n have exponents i,l in {0,1}, j=v-i-l>=1. Their interval contributions, with their exact Möbius signs, are

 sum_(i,l in {0,1}, i+l<=v-1) (-1)^(i+l)
    1_(log(p^i m0)<y<log(p^(v-l)m0)).                   (7)

If v>=3, all four terms occur and cancel pointwise off endpoints. If v=2, the three terms cancel off their common meeting point log(pm0). If v=1, only i=l=0 remains, giving the interval (log m0,log(pm0)). Thus an active p must occur exactly once. An exponent at least three at a different prime makes every allocation impossible, proving (5).

When L=a b^2 is cube-free and p|a, every prime in b occurs in both m0 and n0, while primes in a/p are divided between them. Hence m0=bd, n0=b(a/p)/d with d|a/p, and

    mu(m0)mu(n0)=mu(a/p)=-mu(a).

Summing the remaining intervals proves (6). No assumption about zero locations, prime independence, or Möbius cancellation beyond the exact divisor algebra has been used.

## 4. Exact cutoff remainder

For M_N replace (3) by

 R_(L,N)^mu(y)
   =sum_(m|e|L, m<=N, L/e<=N, m<exp(y)<e)
                    mu(m)mu(L/e)Lambda(e/m).           (8)

The complete omitted coefficient is exactly

 R_(L,N)^mu-R_L^mu
   =-sum_(m|e|L, [m>N or L/e>N], m<exp(y)<e)
                    mu(m)mu(L/e)Lambda(e/m).           (9)

Every boundary branch appears once through the union condition. For L<=N it is zero. A finite cutoff can therefore retain cube-divisible labels; it would be false to impose (5) before adding (9). Equation (4) bounds the full paired remainder by C N^C exp(-cN), after changing fixed constants. No signed coefficient is replaced inside (8) or (9); an absolute estimate is used only to pay the genuine future tail.

## 5. Equivalent prime-fiber reading, with its precise scope

Let d=log p, z=p^(-1/2), and remove p from the Möbius product:

    M^(p)f=sum_(p not dividing n)mu(n)n^(-1/2)f(x+log n).

Then M=(I-z E_d)M^(p), and the cancellation above is equivalently

 sum_(j>=1)(log p) z^j integral_0^(jd)
                 Mf(x)Mf(jd-x)dx
   =(log p)z integral_0^d
              M^(p)f(x)M^(p)f(d-x)dx.                 (10)

The elementary grouping of p-power reflection into a paired future-fiber mean is already known. The new all-integer version (5)-(9) tracks what its simultaneous true Möbius congruence does to every square factor and finite divisor boundary. The pairing on the right of (10) is still indefinite; its two source samples are not a modulus square.

## 6. Complete actual quadratic expression after the cancellation

Let F be the complete future prime source operator. The exact identity

    F M f=[X,M]f=-sum_n mu(n)(log n)n^(-1/2)E_(log n)f

gives the complete unanchored forward term

    -4<A,FA>
      =2 sum_(m,n>=1)mu(m)mu(n)log(mn)/sqrt(mn)
                       <E_(log m)f,E_(log n)f>.       (11)

Define the bilinear forward cross correction

    C_F(t)=4t{<A,Fb>+<b,FA>}-4t^2<b,Fb>.

Then the SAME anchored source has the exact complete form

 Q_delta[a]
   = q_b[a_o]-2C0||a||_2^2+2delta integral V a^2-8ell(a)^2
     +2 sum_(m,n>=1)mu(m)mu(n)log(mn)/sqrt(mn)
                       <E_(log m)f,E_(log n)f>
     +C_F(t)
     +2(1-delta){ R(Mf,Mf)-2t R(Mf,b)+t^2 R(b,b) },    (12)

where R(Mf,Mf) is exactly (2),(5),(6). The V term is grouped with a before integration; integral V A^2 and integral V b^2 must not be separated. The full Gamma term, scalar mass, pole square, forward repair, reflected repair, and actual delta are all retained.

For finite M_N, use (8)-(9) and the complete mu-Lambda divisor remainder in the anchored future theorem before replacing F M_N by [X,M_N]. Dropping that remainder would corrupt (11).

The actual largest-source inequality requires (12)>=0. No independent opposite sign is proved. In particular the positive gcd Gram identity

    sum_(m,n)c_m c_n log gcd(m,n)
       =sum_d Lambda(d)(sum_(d|n)c_n)^2 >=0

cannot by itself assign a sign to (11): its companion multiplicative-distance term and the reflection/repair terms remain. The arithmetic cancellation here produces the explicit signed squarefree cut (6), not an unweighted positive gcd substitute.

## 7. The exact Gamma congruence for this ACTUAL source

The Gaussian-seed matrix is a special case, not a substitute for the actual f=g. For arbitrary actual f in this note define the entire half-transform and finite prefix

    H_f(z)=integral_0^infinity f(x)exp(izx)dx,
    J_(f,n)(z)=integral_0^(log n)f(x)exp(izx)dx,
    H_(f,n)(z)=n^(-1/2-iz)[H_f(z)-J_(f,n)(z)],
    c_(f,n)=n^(-1/2)f(log n),
    H_b(z)=integral_0^infinity b(x)exp(izx)dx.

These identities come from substituting y=x+log n in the normalized future branch. Thus the Fourier transform of its anchored odd extension is exactly

    F_(f,n)(z)=H_(f,n)(z)-H_(f,n)(-z)
                 -c_(f,n)[H_b(z)-H_b(-z)].            (13)

In particular the actual finite anchored source a_N has transform

    hat a_N(z)=sum_(n<=N)mu(n)F_(f,n)(z).              (14)

Its complete Gamma/mass/pole contribution is the true finite Möbius congruence

    sum_(m,n<=N)mu(m)mu(n) K_(f;m,n),

    K_(f;m,n)=1/(2pi) integral_R a(xi)
              overline(F_(f,m)(xi))F_(f,n)(xi)dxi
                  -2 overline(l_(f,m))l_(f,n),
    l_(f,n)=F_(f,n)(-i/2).                            (15)

Here a(xi)=b_Gamma(xi)-C0; l_(f,n) is the FULL-LINE sinh moment of the odd branch, equal to twice its positive-half moment. The factor -2 in (15) is therefore exactly the -8ell(a_N)^2 in (12). No individual archimedean positivity is asserted.

The trace cancellation in (13), the actual H^s control, and the theta tails prove convergence of (15). Formula (14) passes to the complete repaired M source in the original P norm by the anchored future theorem. For a Gaussian-polynomial seed the H_(f,n) can equivalently be evaluated by upper incomplete Gamma functions, directly substituting exp(2x) in their defining half-integrals. The uncut full-line Gaussian scale kernel does NOT equal (15), and no Gaussian replacement of the actual source is made here.

Equations (8)-(9), (12)-(15) are consequently an actual-source finite signed matrix specification with no source substitution, missing Gaussian overlap, omitted reflection cutoff, or erased origin moment. Its favorable total sign, after adding the original complete diagonal and prime terms, is still open.
