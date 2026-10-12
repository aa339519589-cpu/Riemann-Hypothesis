# Complete physical short-conductor pruning and the literal unit kernel

Work at eta=1. For each original compensation summand, write

    n=n0 r^2, n0 squarefree, g=(c,s), c1=c/g,
    Nc1 Nn0 Nr <= X' Z^(-delta),  delta>0 fixed.

The complete signed contribution of this literal selected family, with the entire m column summed first, is O_(A,delta)(Z^(-A)) for every fixed A>0. The theorem includes every physical s valuation, both original and half-damped n weights, original/core nonflat marks, every finite-compensation subset, every admissible primitive auxiliary character and all 0<T<=Z. No Q is used. The original normalization, positive auxiliary average and Gaussian-restoring operator preserve the assertion for the half-damped observation only.

The necessary primitive transformation is proved explicitly below. For squarefree physical s it also identifies the exact literal u=1 Poisson component: its true support forces n to be a square, and all normalized Gauss roots reduce to the genuine signed coefficient mu(g c1) kappa(r). The resulting long Mobius column is displayed with its full masks and joint Gaussian/Fourier weights. That long-column identity is not a decay estimate and is not asserted here for every non-squarefree s.

This is a signed subtraction before any positive class decomposition. The complementary long-conductor block, its Mobius correlation, and the cross-class term remain unestimated. No whole-low, all-epsilon spectral, or RH conclusion follows.

## Precise inherited observation and necessary dependencies

All primary/finite-ray conventions and the positive additive pairing are those of the [pinned original general-probe/Psi source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). The original and half-damped physical coefficient, including the indispensable chi_A(m), is written explicitly in [PHYSICAL_KUMMER_BLOCKS.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/33fef7a5b36b296fdf4363d949ba343e106d1ead/reports/20261011_qrh_selection_bridge/PHYSICAL_KUMMER_BLOCKS.md). Part I A-B there proves the two exact complete-column higher-s-valuation identities used in Part II below; their old slot labels, scalar normalizations and restoring-prime set remain unchanged.

The actual primitive-Poisson/Schwartz bound and original scale conventions also appear in [PHYSICAL_SQUARE_RESONANCE.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/dde3bf1526f28311f4cd6f527c1cc7c80bf6f4a6/reports/20261011_qrh_selection_bridge/PHYSICAL_SQUARE_RESONANCE.md). The bounded T-only operator is the published [Gaussian restorer](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261011_qrh_selection_bridge/RESTORED_AUXILIARY_COMPARISON.md). No new local observation, auxiliary re-selection, or fixed-conductor Mertens assumption is introduced. The [independent review](REFEREE_PHYSICAL_SHORT_CONDUCTOR.md) records the source-level normalization, support, full-root and whole-scale checks. Formula numbers are local to the two parts.

# Part I. Exact primitive transformation and squarefree-s unit kernel

## 1. Actual squarefree-s row and primitive conductor

Use eta=1 and the original physical probe, initially with squarefree s. Retain the genuine primitive auxiliary xi modulo b*, B=N(b*), its full Gauss root tau_xi, and every original zero extension. Write

 n=n0 r^2, n0 squarefree;
 g=(c,s), c=g c1, s=g s1, with g,c1,s1 pairwise coprime squarefree;
 A=c n0^3 r^6, S=Ns, M=B S X.

Let theta be the primitive good character inducing chi_A conjugate(chi_s) on its units. Its conductor ideal and the missing-unit hole are exactly

 f=rad(c1 s1 n0), F=Nf,
 D=rad(g r) with all primes of f removed.                  (1)

Indeed the local exponent of the good character is
 1_(p|c)+3*1_(p|n0)-1_(p|s) modulo six.
It is nonzero precisely at rad(c1 s1 n0); the remaining original A,s unit zeros are D. This includes every possible overlap with n0 and r. Thus

 chi_A(m)conjugate(chi_s(m))=theta(m)1_((m,D)=1),
 (D,b*f)=1, and F ND <= S Nc1 Nn0 Nr.                     (2)

Put tau_theta=F^(-1/2)g_theta(f,1), using the same positive additive character as the source. If f=1, set theta=1 and tau_theta=1. The product psi=xi theta is primitive modulo b*f, even in that case, because the original auxiliary character is primitive and nonprincipal.

## 2. Exact Poisson and cancellation of the auxiliary root

Expand the D-unit mask once. Primitive Poisson with the source self-dual measure gives

 M^(-1/2) sum_m xi(m)theta(m)1_((m,D)=1)W0(Nm/M)
 =sqrt(SX/F) tau_xi tau_theta xi(f)theta(b*)
     sum_(d|D) mu(d)xi(d)theta(d)/Nd
     sum_(h, (h,b*f)=1) conjugate(xi(h)theta(h))
                    Wtilde0(SX Nh/(F Nd)).                (3)

The h sum is over elements with the original lattice conventions. In particular h=0 is absent, for every row: this is the genuine primitive Fourier zero, not the separate good-core label u=1. The radial Fourier profile is exactly the source Wtilde0, so generator rotations introduce no new weight.

For squarefree s its original s Gauss factor is
 gamma_1(s)conjugate(chi_s(-1))conjugate(chi_s(m)).
The remaining original auxiliary multiplier is
 chi_s(b*)/[tau_xi xi(s)Xi(A)], with Xi(A)=xi(A)chi_A(b*).
Since theta(b*)=chi_A(b*)conjugate(chi_s(b*)), substituting (3) cancels every b* factor except

                    xi(f d/(s A h)).                    (4)

This notation is used only on the true b*-unit support. It may equivalently be written as conjugate(xi(H)), where

                         H=(sA/(f d))h.                 (5)

The quotient sA/(f d) is an integral ideal generator: f d divides rad(sA). Formula (5) is the original full-modulus Poisson frequency, not a newly selected frequency. Indeed X NH/NA=SX Nh/(F Nd), exactly the original Fourier argument.

Define the remaining true root

 Q(c,n,s)=gamma_2(c)conjugate(alpha(A))conjugate(G(A))
          R(A,s)gamma_1(s)conjugate(chi_s(-1))tau_theta.

The complete row after (3), including its original c,n coefficient, is therefore

 (1/Y) W1(S/Y) (Nc)^(-1/2)(Nn)^(-3/2) V_G(NA/T)
   *sqrt(SX/F) Q(c,n,s)
   *sum_(d|D) mu(d)theta(d)/Nd
    sum_(h,(h,b*f)=1) conjugate(theta(h))conjugate(xi(H))
                       Wtilde0(SX Nh/(F Nd)).            (6)

This is stated for the half-damped n weight. Replacing (Nn)^(-3/2) by (Nn)^(-1) gives the original weight. All marked tests and masks may be retained coefficientwise. Equations (3)--(6) are exact finite-mask/complete-column identities, not pointwise character estimates. The only frequency scale in (6) is F Nd/(SX), independent of the size of B.

## 3. Unconditional short-conductor pruning

For each fixed L>=0, primitive Poisson and the entire nonzero Schwartz tail, including the short-scale two-dimensional lattice estimate, yield

 |M^(-1/2) sum_m xi(m)theta(m)1_((m,D)=1)W0(Nm/M)|
 <<_(L,epsilon) sqrt(F/(SX)) (F ND)^epsilon
                                      [F ND/(SX)]^L.     (7)

One direct verification applies the primitive bound sqrt(BF)(BF/U)^L to U=M/Nd and divides by sqrt(M), before summing the exact d mask. This also proves (7) when its bracket exceeds one. No auxiliary norm remains.

Fix delta>0 and the original ambient Z. In each actual compensation summand, select the squarefree-s physical rows satisfying

                        F ND/(S X') <= Z^(-delta).       (8)

The complete m sum over this signed subfamily is smaller than every prescribed fixed power of Z, uniformly in every admissible auxiliary and every 0<T<=Z. A simple sufficient condition for (8), from (2), is

                        Nc1 Nn0 Nr <= X' Z^(-delta).     (9)

Here the exact criterion (8), rather than its sufficient enlargement, defines the selected rows.

To pay all physical sums, note F<=S Nc Nn0. After multiplying the square root in (7) by the half-damped coefficient, the absolute c,n weight is bounded by

                 (X')^(-1/2)(Nn0)^(-1)(Nr)^(-3).

The full Gaussian c sum is O(T_eff/((Nn0)^3(Nr)^6)), including effective scales below one with their original Gaussian tail. Thus the n0,r sums have exponents -4 and -9 and converge absolutely. The annular s sum cancels the original Y'^(-1). Consequently the selected subset is at most

      Z^epsilon Z^(-delta L) T_eff/(X')^(1/2).            (10)

The missing-unit small powers are paid by slightly increasing the fixed Gaussian moments, with no B cost. For the original n weight the corresponding convergent exponents are -7/2 and -8, so (10) remains valid.

At the actual scales X'=Z^(17/48-d), T_eff<=Z^(7/6-d), d in [0,1/6], one has T_eff/sqrt(X')<=Z^(95/96). The full original slot mass costs at most Z^(16/96). Hence the entire selected signed observation is

                   O(Z^(37/32-delta L+epsilon)).          (11)

Choose L fixed after the desired final power. The support criterion is independent of the Gaussian variable T, so the already reviewed half-damped restorer and original normalizations preserve this arbitrary-power bound. This subtraction must be done before a positive class decomposition, just like the powerful-s resonance subtraction. Nothing here bounds the complementary long-conductor rows.

## 4. Exact sixth-power frequency support forces n to be a square

Now retain in (6) only the literal original good-core frequency u=1, namely H=a^6 with the source's unique ideal/primary convention. At a prime p|n0 the primitive theta conductor contains p. Thus the zero mask requires v_p(h)=0, and p cannot divide d. Writing a=1_(p|c), b=1_(p|s), the exponent of sA/f at p is

                      a+b+2 modulo six,

which is one of 2,3,4. This is incompatible with H being a sixth power. Therefore this entire projected frequency component has

                              n0=1.                     (12)

This is an exact support statement, not cancellation after absolute values. It uses the same primitive zero mask retained in (3).

With n=r^2 one has f=c1s1 and D=rad(gr) outside f. Equations (5) and H=a^6 then force exactly

                         h=g^4 d z^6,
                         a=g r z,
                         (z,b*f)=1.                    (13)

The dual z may share primes with g and r; these are not additional holes. Conversely (13) produces every original u=1 frequency in this row. It retains the literal unit convention and does not group the other five units into u=1.

The Fourier argument becomes

           SX Nh/(F Nd)=X (Ng)^5 (Nz)^6/Nc1,             (14)

independent of d and r. The finite mask sum therefore simplifies exactly to

 sum_(d|D) mu(d)theta(d)conjugate(theta(g^4 d z^6))/Nd
       =conjugate(theta(g^4)) phi(D)/ND.                 (15)

The character factors are units on this support, so (15) is legitimate even when z shares D. The auxiliary factor in (4) is one because H is a literal sixth power.

## 5. All Gauss roots in this component cancel to the genuine Mobius sign

Put kappa(r)=conjugate(alpha(r))^6. The source Hasse--Gauss identities and reciprocity give

 Q(g c1,r^2,g s1)conjugate(theta(g^4))
                              =mu(g c1)kappa(r).         (16)

For an explicit check, use gamma_j(ab)=gamma_j(a)gamma_j(b)
 chi_a(b)^j chi_b(a)^j on coprime squarefree a,b and

 tau_theta=gamma_1(c1)gamma_5(s1)
                              chi_(c1)(s1)conjugate(chi_(s1)(c1)).

The gamma_1(s1)gamma_5(s1)=chi_(s1)(-1) product cancels the s1 part of conjugate(chi_s(-1)). The g and c1 products gamma_1 gamma_2 give mu(g)mu(c1)alpha(g c1)G(g)G(c1). The quadratic refinement G(g c1)=G(g)G(c1)R(g,c1), together with conjugate(theta(g^4)), reduces the remaining cross-prime factors to R(g,c1)R(g,s1)R(c1,s1)conjugate(chi_g(-1)). Multiplication by R(A,s) cancels them, since R(g,g)=chi_g(-1) and R takes values in {1,-1}. Finally G(r^6)=chi_(r^3)(4)=1, R(c,r^6)=1, and the remaining alpha factor is exactly kappa(r). This verifies (16) including the original additive convention and fixed ray factors.

Combining (6) and (12)--(16) yields the following exact squarefree-s unit component of the HALF-DAMPED physical probe:

 sqrt(X)/Y sum_(g,c1,s1 squarefree pairwise coprime; r)
   mu(g c1)kappa(r)/[Nc1 (Nr)^3]
   *W1(Ng Ns1/Y) V_G(Ng Nc1 (Nr)^6/T)
   *phi(D)/ND
   *sum_(z,(z,b*c1*s1)=1)
                       Wtilde0(X (Ng)^5 (Nz)^6/Nc1),     (17)

where D=rad(gr) outside c1s1. All original S holes, primary conventions and marked tests are retained in this formula. The original n weight changes (Nr)^(-3) to (Nr)^(-2). There is no unrecorded auxiliary Gauss phase or angular twist in the c1 Mobius column; kappa(r) remains the actual fixed nonzero angular character in the r column.

## 6. What the explicit unit kernel supplies and what it leaves

Since Nz>=1 and Wtilde0 is Schwartz, rows with Nc1/(Ng)^5 <= X Z^(-delta) have arbitrarily rapid frequency decay. This is a pointwise statement with the entire z tail retained; any sum over such rows must still pay its real c1,g,s1,r weights, as in Section 3. Formula (17) identifies the remaining long Nc1>=approximately X(Ng)^5 Mobius column with its true shared masks and joint Fourier/Gaussian weights. It does not replace that column by arbitrary coefficients or claim a square-root Mertens estimate.

The component in (17) is the actual original u=1 frequency projection. Deriving it does not justify estimating the complete observation by an already known high comparison. The unconditional new pruning in Section 3 and the exact constraints (12)--(16) are usable before any positive norm; the remaining signed long-column and cross-class correlations still need a genuine bound.

# Part II. The literal short block on the entire physical s support

## 1. A criterion expressed in the original physical variables

Use eta=1, either the original or half-damped physical n weight, and any admissible primitive auxiliary xi with its full original modulus. Write

 n=n0 r^2 with n0 squarefree, g=(c,s), c1=c/g.

For a fixed original compensation summand, retain its genuine X',Y',T_eff and fix delta>0. Select precisely the physical tuples satisfying

                    Nc1 Nn0 Nr <= X' Z^(-delta).          (1)

The criterion does not depend on m or the Gaussian scale T. All original unit masks, marked tests, primary conventions and outside coefficients are retained. For every prescribed A0>0, the contribution of this selected signed family, after the ENTIRE m sum, is O_(A0,delta)(Z^(-A0)), uniformly over all admissible auxiliary data and 0<T<=Z. This holds for the full original finite compensation with original/core nonflat marks.

For the actual polylogarithmic auxiliary ensemble, it remains true after the same half-damped restoring operator, c_Sb normalization, positive ensemble average and ambient slot normalization. The original-n version is a physical signed subtraction; no principal restoring formula for that weight is asserted.

## 2. Reduce higher s valuations without altering the selector

Write s=s1 t, with s1 squarefree, t powerful, and (s1,t)=1. On the true Gauss/chi_A(m) support, every prime of t is prime to A=cn^3. Hence (c,t)=1 and

                         (c,s)=(c,s1)=g.                 (2)

In particular the variables c1,n0,r appearing in (1) are unchanged by the reviewed higher-s reductions.

For p^k exactly dividing t with k mod6 nonzero, use the exact identity
 P^(-k) times the observation with xi_p=chi_p^(-k),
 auxiliary modulus enlarged by p, and Y replaced by Y/P^k.
For 6|k, use the exact two-complete-column identity

 P^(-k)[J_p(X,Y/P^k,T)-P^(-1/2)J_p^omega(PX,Y/P^k,T)],

with its genuine p-unit row restrictions and omega=bar xi(p)chi_s1(p)bar chi_A(p). Its multiplier is independent of m. Both identities preserve any extra selector depending only on c,n,s1,t, including (1). All current full CRT roots and phases are kept at each step.

Thus for a fixed t the selected family is an exact sum of squarefree-s1 columns. They have Y_t=Y'/Nt, unchanged T_eff, some X_t>=X', and a primitive auxiliary of potentially larger full norm. Their common outside coefficient is (Nt)^(-1); the total additional absolute coefficient is at most

             C(t)=product_(p|t,6|v_p(t))(1+P^(-1/2)).     (3)

No constant per new auxiliary prime occurs. The old slot labels, normalization and restoring prime set are not changed by this calculation. If a marked condition forces a prime of t into A, that branch is exactly zero.

## 3. Every resulting column lies in the reviewed short-conductor region

For a squarefree-s1 column write s1=g s2. The exact primitive good conductor and missing hole are

 f=rad(c1 s2 n0),
 D=rad(g r) with the primes of f removed.

Their norms satisfy

             Nf ND <= Ns1 Nc1 Nn0 Nr.

Consequently (1) and X_t>=X' imply

                 Nf ND/(Ns1 X_t) <= Z^(-delta).          (4)

The complete primitive m-Poisson estimate is uniform in the enlarged auxiliary norm. The reviewed proof, including the convergent n0,r Gaussian moments, therefore bounds this resulting selected column by

                  Z^epsilon Z^(-delta L)
                                         T_eff/sqrt(X_t) (5)

for every fixed L>=0, in either physical n weight. The extra modulus-one row factors from the principal two-column reduction do not change that proof: (5) is obtained by summing the absolute bounds AFTER each complete m column has been transformed.

The s1 window can be nonempty only when Y_t is bounded below by a positive constant depending on W1. The annular count used in (5) is uniform on that full range, including the fixed compact interval below one. All small powers in (5) concern good row variables and the fixed ambient geometry; there is no hidden power of the temporary auxiliary modulus.

## 4. The powerful-layer sum is absolutely convergent

For any fixed epsilon1 in (0,1/2), C(t)<<_(epsilon1)(Nt)^epsilon1. The ideal series

                 sum_(t powerful) C(t)/Nt               (6)

is absolutely convergent. This follows either from the O(V^(1/2)) powerful-ideal count, or from its Euler product: the local nonconstant contribution starts at P^(-2), and the extra C(t) factor only occurs from exponent six onward. This convergence is over ALL t, not merely a hard cutoff depending on Y'.

Multiply (5) by (Nt)^(-1), use X_t>=X', and sum all exact branches and all t via (3)--(6). The whole selected original s support is at most

                    Z^epsilon Z^(-delta L)
                                         T_eff/sqrt(X'). (7)

This proves that the higher s valuations incur no loss of a positive Y or auxiliary-conductor power. No positive class energy has been deleted; the original signed complete columns have only been rewritten exactly and then bounded.

At the actual compensation geometry,
 T_eff/sqrt(X')<=Z^(95/96), while the total slot tuple mass costs at most Z^(16/96). Thus the full selected family is

                        O(Z^(37/32-delta L+epsilon)).    (8)

Choose L fixed after the required A0. The support (1) is independent of T, so the reviewed half-damped restorer preserves it and has the same uniformly bounded product norm on sup_(0<T<=Z). The original ensemble normalizations then have their already reviewed O(1) or fixed-logarithmic prices. This proves the assertion of Section 1.
