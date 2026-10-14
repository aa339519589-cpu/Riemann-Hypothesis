# The original-metric future Möbius test and its complete boundary form

2026-10-14. This is an exact arithmetic test construction for the SAME actual largest supercritical Green source. It is not an accretivity theorem. Unlike an uncorrected long even translate, the complete future Möbius map is a legal original-P test after an explicit trace and pole repair. Its inverse modulo repair has an explicit correction of rank at most two. The complete signed quadratic form below retains the Gamma term, every prime reflection, and all repair terms.

## 0. Original definitions and verified dependencies

Write P[f]=P[f/psi] and similarly N[f] when using source rather than ratio notation. The norm ||f||_P is sqrt(P[f]). The positive half-line source is psi=-Phi', with Phi the original even theta kernel. Let

    kappa(t)=exp(-t/2)/(1-exp(-2t)),
    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    w(x)=psi(x)sinh(x/2), integral_0^infinity w=1/8,
    L(x)=sum_(d_n>x)alpha_n psi(d_n-x),
    nu(x)^2=psi(x)/L(x), V=nu^(-2),
    m(x)^2=Phi(x)/(2cosh(x/2)).

The weight nu is distinct from the arithmetic Möbius function mu(n). The complete original gradient forms are

    P_Gamma[r]=double integral psi(x)psi(y)
       [kappa(|x-y|)-kappa(x+y)]|r(x)-r(y)|^2 dx dy,
    P_pole[r]=4 double integral w(x)w(y)|r(x)-r(y)|^2 dx dy,
    P_F[r]=2 sum_n alpha_n integral_0^infinity
       psi(x)psi(x+d_n)|r(x)-r(x+d_n)|^2 dx,
    N[r]=sum_n alpha_n integral_0^(d_n)
       psi(x)psi(d_n-x)|r(x)-r(d_n-x)|^2 dx,
    P=P_Gamma+P_pole+P_F.

All double integrals are over positive half-lines. The full-line Gamma form is q_b[f]=integral b_Gamma(xi)|hat f(xi)|^2 dxi/(2pi), where

    b_Gamma(xi)=Re digamma(1/4+i xi/2)-digamma(1/4),
    C0=EulerGamma+pi/2+3log(2)+log(pi).

These conventions, the actual closures, and the complete source identity are fixed in the [original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), [reflected-prime energy](../20261013_reflected_prime_energy/REPORT.md), and [full-prime reference](../20261013_full_prime_green_reference/REPORT.md). The [odd operator-domain report](../20261013_odd_operator_domains/REPORT.md) fixes the coefficient-two pole normalization and exact null source psi. The regularity and cutoff inputs are [actual source tails](../20261013_supercritical_source_tails/REPORT.md), [source smoothing](../20261013_supercritical_source_tails/SOURCE_SMOOTHING.md), [fixed-depth regularity](../20261013_supercritical_source_tails/FIXED_DEPTH_REGULARITY.md), and [the second bootstrap and fixed translations](../20261013_supercritical_source_tails/BOOTSTRAP_AND_FIXED_TRANSLATIONS.md).

All eight dependency paths were verified at repository commit 9f9ca85d42120bcc7411c86e2ccb1e7a94738b8c. They are relative to this report's intended repository directory, reports/20261014_anchored_future_mobius/.

## 1. Source and two repairs

Let g=psi r be the actual real odd centered source, delta>=d>0, and v=g/nu. Use the original forms P,N, h=P-N, Q_delta=h+delta N. The newest fixed-depth bootstrap gives, for every fixed 1/2<s<1,

    ||v_o||_(H^s)+||g_o||_(H^s)<=C_(d,s) sqrt(P[g]),
    Q_delta>=0,  Q_delta(g,z)=0.                         (1)

The continuous representative has g(0)=0. Put

    ell(f)=integral_0^infinity sinh(x/2)f(x)dx,
    b(x)=Phi(x)/Phi(0),
    e=b-8ell(b)psi,
    Rf=f-f(0)e-8ell(f)psi.                              (2)

Thus e(0)=1, ell(e)=0, Rf(0)=ell(Rf)=0. Both repairs have theta tails, unlike an exponential origin repair. The two summands f and f(0)e need NOT be individually legal P vectors; their trace cancellation must precede the weighted origin integral.

Write E_a f(x)=f(x+a), x>0, and

    C=sum_(n>=1)n^(-1/2)E_(log n),
    M=sum_(n>=1)mu(n)n^(-1/2)E_(log n),
    F=sum_(n>=2)Lambda(n)n^(-1/2)E_(log n).             (3)

These are positive-half-line operators, not full-line odd convolutions. In particular no convolution covariance is imported.

## 2. Legality on the actual fixed-depth source class

The complete sources RMg and RCg belong to the ORIGINAL centered P completion. For finite cutoffs, including arbitrary large predetermined integers,

    ||R M_Ng||_P+||R C_Ng||_P<=C_(d,s) sqrt(P[g]),       (4)

uniformly in N; the finite sources converge in P to their complete counterparts. This is a bound on the actual fixed-depth source class. It is NOT a bounded-operator assertion on the entire P completion, whose norm need not control g(log n).

Here are sufficient estimates proving (4). Split off the identity term, and let K have coefficients bounded by n^A for some fixed A, supported on n>=2. This covers the tails of M,C,F and their finite polynomially weighted products. The published complete-row bounds give

    nu(y)<=C exp(Cy-pi exp(2y)/2),
    |nu'(y)|<=C exp(Cy-c exp(2y))  (y>=eta>0)            (5)

almost everywhere, with a positive fixed c. The possible prime-knot derivative jumps do not affect this a.e. bound or the W^(1,p) estimates. Since v_o belongs to H^s and hence L-infinity,

    |g(x+log n)|<=C_(d,s) sqrt(P[g])
                      exp(Cx)n^C exp(-pi n^2 exp(2x)/2).
                                                               (6)

A smooth cutoff to y>=log n-eta, with fixed small eta<log(2)/2, and (5) give summable H^s norms of the shifted g. More explicitly the H^s algebra estimate applied to (cutoff nu)v gives

    ||g( . +log n)||_(H^s(0,infinity))
       <=C_(d,s) n^C exp(-c' n^2) sqrt(P[g])            (7)

for a fixed c'>0. The finitely many small n are harmless. Thus Kg and its trace converge in H^s and uniformly, with summable arithmetic coefficients.

The anchored function h=Kg-(Kg)(0)b satisfies, for any 0<alpha<s-1/2,

    |h(x)|<=C_(d,s) sqrt(P[g]) x^alpha, 0<x<1.          (8)

Its odd extension belongs to H^s: this is the usual odd extension of an H^s half-line function with zero trace, with 1/2<s<1. Since V=1/nu^2 is O(1/x) at zero, (8) pays its normalized origin norm. The physical weight m^(-2) is bounded there. At infinity, (6), n>=2, and the theta tail of b pay both weighted norms. In detail the shifted part decays at least as exp(-2pi exp(2x)+Cx), while b decays as exp(-pi exp(2x)+Cx); both squared bounds dominate V and m^(-2), whose leading growth is exp(pi exp(2x)).

Subtracting 8ell(h)psi restores centering and preserves these bounds. Cut off and approximate these grouped odd sources by smooth ratio-core sources. The complete estimates

    N[f]<=C||f/nu||_2^2,
    |h[f]|<=q_b[f_o]+C||f_o/m||_2^2,
    P=N+h                                                 (9)

make the approximants P-Cauchy. The logarithmic Gamma form q_b is controlled by H^s. The same estimates, with the summable tails in (7), prove convergence and (4). The n=1 term is the already legal actual g, not an additional trace repair.

These arguments also pay every finite iteration of C,M followed by R on this fixed source: the new pieces are theta-decaying H^s corrections. No assertion that they remain eigen-sources is made.

## 3. Exact rank-two repaired inversion

On a half-source with the preceding theta tails, the complete positive-half-line sums C and M are honest inverse operators. Indeed

    CMf=MCf=f                                               (10)

follows by locally absolutely convergent divisor collection, sum_(d|k)mu(d)=1_(k=1). This statement has no hidden critical-line inverse-zeta range condition: it concerns future sums on x>=0, not a bilateral transform or an L2 boundary quotient.

For the actual centered zero-trace g, write A=RM and B=RC. Then

    ABg=g-(RMe)(Cg)(0)-8(RMpsi)ell(Cg),
    BAg=g-(RCe)(Mg)(0)-8(RCpsi)ell(Mg).                 (11)

Both are exact identities of legal centered P sources. The rank is at most two, not asserted exactly two. Every scalar trace and moment displayed is retained.

The first two repair vectors are explicit Gaussian-polynomial seeds. Let

    eta(x)=(4pi^2 exp(9x/2)-6pi exp(5x/2)) exp(-pi exp(2x)),
    eta_psi=-eta'.

The genuine theta identities Phi=C eta and psi=C eta_psi give

    Mpsi=eta_psi,
    Me=eta/Phi(0)-8ell(b)eta_psi.                       (12)

Thus (11) is not a formal inverse with unspecified null corrections.

## 4. The exact mu-Lambda law retains the repair commutator

Let X be multiplication by x. On the same future-tail class,

    MF=FM=[X,M],                                        (13)

because [X,E_(log n)]=-(log n)E_(log n) and
sum_(a|n)mu(a)Lambda(n/a)=-mu(n)log n.

For a finite Möbius cutoff M_N, the complete defect is

    M_N F=[X,M_N]+D_N,
    D_N=sum_(k>N) k^(-1/2)
          {sum_(a|k,a<=N)mu(a)Lambda(k/a)} E_(log k).    (14)

No omitted-divisor term has been discarded. The series converges on the future class. It tends to zero on these particular future tails, not in a claimed bilateral current pairing.

Let t(f)=f(0). The corrected maps satisfy the exact finite-rank commutator

 [RM,RF]g
   = -(RMe)t(Fg)-8(RMpsi)ell(Fg)
     +(RFe)t(Mg)+8(RFpsi)ell(Mg).                       (15)

This follows by expanding the two R factors and using MF=FM. For M_N the SAME identity holds, with M replaced by M_N, since a finite future shift polynomial still commutes with F. Formula (14), rather than a false exact finite log identity, is used whenever [X,M_N] replaces M_NF.

## 5. Full original quadratic form of the repaired arithmetic test

Define the legal but not necessarily centered anchor vectors

    u_1=g,
    u_n(x)=g(x+log n)-g(log n)b(x), n>=2,
    a_N=sum_(n<=N)mu(n)n^(-1/2)u_n.                    (16)

Then R M_Ng=a_N-8ell(a_N)psi. Constant ratios are exact null directions of BOTH gradient forms P and N. Consequently

    Q_delta[R M_Ng]=Q_delta[a_N].                      (17)

Equation (17) retains the coefficient-two pole term: it uses its exact constant-ratio invariance, not the centered source formula on an uncentered vector. In particular all centering cross terms vanish for this stated algebraic reason.

For any real zero-trace theta source a, the complete source formulas give

 Q_delta[a]
   = q_b[a_o]-2C0 integral a^2
     -4 sum_n alpha_n integral_0^infinity a(x)a(x+d_n)dx
     +2(1-delta) sum_n alpha_n integral_0^(d_n) a(x)a(d_n-x)dx
     +2delta integral_0^infinity V(x)a(x)^2dx
     -8 ell(a)^2.                                    (18)

Here alpha_n=Lambda(n)/sqrt(n), d_n=log n, and q_b is the FULL-LINE logarithmic Gamma form from the original odd-source convention. The last coefficient is fixed by the original coefficient-two polar term and ell(psi)=1/8. In (18) every prime power remains and V is the full reflected diagonal. This is an uncentered formula; only after subtracting 8ell(a)psi can the rank-one pole term be dropped.

Equivalently, without any dependence on expanded polar normalizations, the completely intrinsic formula is

    Q_delta[a_N]
      =sum_(m,n<=N) mu(m)mu(n)/sqrt(mn)
           {P(u_m/psi,u_n/psi)
                    -(1-delta)N(u_m/psi,u_n/psi)}.     (19)

All the prime, Gamma and pole bilinear forms in (19) are exactly the original gradient forms. The finite and complete identities are justified by the P convergence in Section 2. In particular no term involving Vb^2 is split out: that integral diverges at zero, while each grouped u_n is legal.

The actual variational statement is Q_delta[a_N]>=0, including neutral projection if desired. Neither (13) nor the rank-two inverse (11) determines the sign of the matrix in (19). The reflected and Gamma terms in (18) are not generated by the future mu-Lambda relation alone.

## 6. Why the formal adjoint cannot silently restore convolution covariance

For the finite anchored map in (16), acting on zero-trace functions,

    A_N=I+sum_(2<=n<=N)c_n(E_(d_n)-b t_(d_n)),
    c_n=mu(n)/sqrt(n),  t_d(f)=f(d).

Its formal half-line L2 adjoint is

    A_N^*a=a+sum_(2<=n<=N)c_n 1_(x>d_n)a(x-d_n)
                  -<b,a>sum_(2<=n<=N)c_n delta_(d_n). (20)

The point loads in (20) are real boundary terms. Thus A_N^*A_Ng is not automatically a P source. With (1), W_g is continuous on every compact interval in (0,infinity): g is continuous, psi is positive there, and the complete translated/reflected loads converge uniformly by (6). The actual source equation therefore permits a weak mixed pairing against each fixed delta_(d_n), by smooth approximation, with

    N(g,delta_d)=2W_g(d),
    h(g,delta_d)=-2delta W_g(d).                       (21)

These point terms cancel only in their COMPLETE Q_delta pairing. Neither separate sum over n to infinity nor a quadratic P norm of delta_d is asserted. This gives a valid finite mixed identity if an adjoint calculation is needed, but not a new positive covariance.

## 7. Current outcome and sign target

The future arithmetic map is now a uniformly legal same-source test, complete inversion has an explicit rank-two boundary, and (14), (15), (18)-(21) retain the finite divisor, origin, polar, reflected and Gamma corrections. The remaining question is an actual signed estimate on (19), or a completed mixed identity with a legal comparison vector, that contradicts its necessary nonnegativity. No such estimate has been obtained here. Boundedness on the whole P completion, an accretive number operator, and RH are not claimed.
