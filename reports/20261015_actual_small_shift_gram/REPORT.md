# Actual-source small-shift positivity and the complete odd/even crossing Gram

An actual positive-depth null source satisfies a finite positive-semidefinite
translation constraint in the original form domain. The admissible parameters
are individually smaller than log(2)/2. A separate null gauge at each parameter
also makes the odd/even crossing Gram legal, with its full Gamma, prime, and
pole terms retained. A compact two-bump calculation at the prime-2 knot shows
that the first constraint is not a universal convexity property of the
reflection energy.

These are finite actual-source constraints, not a critical-load upper bound
or an exclusion theorem. No extension to large arithmetic shifts is asserted.

## 1. Complete forms and the actual-source hypotheses

All fields are real. Inner products without another indication are on the
positive logarithmic half-line, with measure dx. Complex statements follow by
Hermitian polarization. Write

    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    kappa(t)=exp(-t/2)/(1-exp(-2t)), t>0,
    a(t)=Re digamma(1/4+it/2)-log pi,
    s(x)=sinh(x/2), c(x)=cosh(x/2),
    ell(f)=int_0^infinity s(x)f(x)dx.

Every Mangoldt sum below includes all prime powers. For a half-line source f,
let f_o be its odd extension and use
hat f_o(t)=int_R f_o(x)exp(itx)dx. The complete original source form is

    q0[f]=(1/(2pi))int_R a(t)|hat f_o(t)|^2dt
       -2sum_(n>=2)alpha_n int_R f_o(x)f_o(x+d_n)dx
       -2[int_R s(x)f_o(x)dx]^2.                         (1)

In particular the half-line pole in (1) is -8 ell(f)^2. Define the theta
source and the three half-line prime operators by

    B(x)=exp(x/2-pi exp(2x)),
    xi=-(partial_x^3-partial_x/4)B,
    psi(x)=sum_(m>=1)m^(-1/2)xi(x+log m),
    F_+f(x)=sum_n alpha_n f(x+d_n),
    F_-f(x)=sum_(d_n<x)alpha_n f(x-d_n),
    F_rf(x)=sum_(d_n>x)alpha_n f(d_n-x).

The source psi is odd, positive on x>0, and has a simple zero at zero.
Put L=F_r psi, V=L/psi and

    N[f]=2int_0^infinity V f^2-2<f,F_r f>,
    P[f]=q0[f]+N[f], Q_delta[f]=q0[f]+delta N[f],
    Wf=Vf-F_rf.                                          (2)

Here P[f] means the original ratio completion evaluated at f/psi, not an
alternative unweighted completion. The bilinear density convention is
N(f,z)=2<Wf,z> when the complete pairing is legal.

Fix 0<delta<1 and a SAME actual source g=psi r in that original domain, with

    Q_delta >= 0 on the original P domain,
    Q_delta(g,z)=0 for every original-P test z.            (3)

The source can initially be pole-centered. Subtracting any real multiple
of psi preserves (3), because

    Q_delta psi=0, Wpsi=0.                               (4)

We use the already established actual-source regularity: r is bounded and
continuous, g_o belongs to H^sigma(R) for every sigma<1, and the source has
the theta tail |g(x)|<=C psi(x). In particular g(0)=0. These facts are proved
in the [actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md)
and its [fixed-depth source bootstrap](../20261013_supercritical_source_tails/BOOTSTRAP_AND_FIXED_TRANSLATIONS.md).
The complete form, theta identities, and original completion are fixed in
the [source-form foundation](../20261012_localized_odd_schur/SOURCE_FORM.md)
and the [actual source realization](../20261013_supercritical_source_tails/REPORT.md).
The definitions and same-source conventions are also collected in the
[physical range theorem](../20261015_old_actual_physical_range/REPORT.md).
No existence assertion beyond these actual-source hypotheses is made here.

For the estimates below, these inputs give the following useful bounds.
Near zero V(x)<=C/x. At infinity L(x)<=C exp(x/2), while the leading theta
term of psi is a positive polynomial in exp(x), times exp(-pi exp(2x)).
Consequently V(x)<=C exp(Cx+pi exp(2x)) for x>=1. These upper bounds suffice;
their constants, and all constants below, may depend on the fixed source
and on delta.

## 2. The exact parity operators, including both pole ranks

For h>0 define

    E_h f(x)=f(x+h),
    E_h^*f(x)=1_(x>h)f(x-h),
    R_h f(x)=1_(x<h)f(h-x),
    S_h=E_h+E_h^*-R_h, J_h=E_h-E_h^*+R_h.                (5)

Thus S_h is the symmetric translation sum on the odd extension, whereas
J_h is the odd-to-even translation difference. In particular

    S_h S_k=S_(h+k)+S_|h-k|, S_0=2I, J_0=0.              (6)

Let T_odd and T_even be the odd and even half-line compressions of the
complete full-line expression a(D)-sum_n alpha_n(E_(d_n)+E_(-d_n)).
They include the reflected Gamma and prime terms with the respective
parities. Set

    Q0=2T_odd-8s tensor s,
    Q_even=2T_even+8c tensor c,
    H_kappa f(x)=int_0^infinity kappa(x+y)f(y)dy,
    B_cross=H_kappa+F_r
             -exp(x/2) tensor exp(x/2)
             -exp(-x/2) tensor exp(-x/2).                (7)

For a tensor u tensor v, its action is u<v,f>. The full identities are

    Q0 S_h=S_h Q0,
    Q_even J_h=J_h Q0,
    Q0-Q_even=4B_cross.                                (8)

These are source/form-dual identities on a common cutoff core and its
admissible limits, not an assertion of a global unweighted operator domain.
To verify them, the full-line convolution commutes with translations.
Its odd/even compression difference is twice H_kappa+F_r. The pole
identities follow from

    S_h s=2cosh(h/2)s, J_h s=2sinh(h/2)c,
    ell(S_h f)=2cosh(h/2)ell(f),
    <c,J_h f>=-2sinh(h/2)ell(f).

In the difference Q0-Q_even, use
s tensor s+c tensor c=(exp(x/2) tensor exp(x/2)
+exp(-x/2) tensor exp(-x/2))/2. This gives exactly (7)-(8).
The common small-jump subtraction in the Gamma multiplier commutes and
cancels before its cutoff is removed. All prime powers remain present.

## 3. The original-domain window and the actual first-slot product

**Domain lemma.** If 0<h<log(2)/2, then S_hg belongs to the original P
domain. For any two such parameters h,k, the product S_hS_kg is an
admissible actual first-slot test:

    Q_delta(g,S_hS_kg)=0.                               (9)

The assertion (9) does not claim that S_hS_kg itself belongs to P.

**Proof.** The whole trace of S_hg is zero by oddness. Its H^sigma
regularity, with any fixed 1/2<sigma<1, gives a positive Holder exponent
at the wall. The endpoint x=h is continuously glued because g(0)=0.
Hence int_0^1 V|S_hg|^2 is finite. At infinity the slowest past translate
has a squared Gaussian factor exp(-2pi exp(-2h)exp(2x)). The strict
inequality 2exp(-2h)>1 pays the adverse exp(pi exp(2x)) in V. Therefore

    int_0^infinity V|S_hg|^2 < infinity.                 (10)

The ordinary Gamma form is controlled by H^sigma. The theta tails pay
both prime orientations and the pole in q0. The full reflection term is
bounded by its V diagonal: positivity of the reflected coefficients and
2|ab|<=a^2+b^2, applied after division by psi, give
|<f,F_rf>|<=int V f^2. Smooth annular cutoffs and then core approximation
converge in these bounds. This proves original-P membership, without
assigning it to the separate sharp pieces of (5).

Now let z=S_hS_kg. Formula (6) shows that its whole trace is zero and that
it has H^sigma regularity and a fixed slower Gaussian tail. Its ordinary
source Gamma, prime, and pole pairings are finite. In the mixed reflection
term use boundedness of the SAME actual ratio:

    |Vg|+|F_rg|<=C L,
    |N(g,z)|<=C int_0^infinity L|z| < infinity.         (11)

Each smooth annular cutoff of z is an original-P test. The cutoff sequence
converges in the ordinary source form and in (11), so (3) passes to (9).
This only uses the actual first slot g; it does not replace (11) by a
quadratic V estimate for z. This proves the lemma.

## 4. A finite positive-semidefinite translation kernel

**Theorem.** For 0<h,k<log(2)/2 put

    K_g(h,k)=N(S_hg,S_kg)-N(g,S_hS_kg).                  (12)

Then

    delta K_g(h,k)=Q_delta(S_hg,S_kg),                  (13)

and every finite matrix (K_g(h_i,h_j)) is positive semidefinite.

Indeed (8), symmetry of S_h, and the common source-form passage give
q0(S_hg,S_kg)=q0(g,S_hS_kg). Substitute (9) and then (2) to obtain
(13). Finite positive semidefiniteness follows from (3) applied to the
original-P source sum_i c_i S_(h_i)g.

The parameter square is not restricted by h+k: only the individual shifted
sources require the quadratic P domain. The product appears solely in
the first-slot statement (9). This distinction does not authorize repeated
quadratic translations, arbitrary arithmetic shifts, or analytic continuation
of the parameter window.

## 5. The full finite S/J Gram with individual null gauges

For each 0<h<log(2)/2 define separately

    f_h=g-r(h)psi, u_h=S_h f_h, v_h=J_h f_h.             (14)

Both u_h and v_h are original-P sources. For u_h use the preceding domain
proof. For v_h the whole wall trace is 2f_h(h)=0; the internal gluing uses
f_h(0)=0. Piecewise H^sigma regularity and matching traces give whole
H^sigma regularity. The strict Gaussian threshold and the V estimate are
unchanged. This proof uses a separate gauge at every h, not division by an
aggregate sum of values psi(h).

Equations (4) and (8) now give the complete form-dual equations

    Q_delta u_h=2delta(Wu_h-S_h Wg),
    Q_delta v_h=4B_cross v_h+2delta(Wv_h-J_h Wg).         (15)

In particular the B_cross in (15) contains both pole ranks, not only
H_kappa+F_r. P membership does not assert separate ordinary L2 membership
of Wu_h, Wv_h, or the displayed forces; the complete grouped pairings are
the ones asserted.

For finite real coefficient families c_h,d_h set

    U=sum_h c_h u_h, Z=sum_h d_h v_h,
    F_S=sum_h c_h S_h Wg, F_J=sum_h d_h J_h Wg.

Then the complete two-by-two Gram is

    A=Q_delta[U]=2delta<U,WU-F_S>,
    C=Q_delta(Z,U)=2delta<Z,WU-F_S>
                 =4<U,B_cross Z>+2delta<U,WZ-F_J>,
    B=Q_delta[Z]=4<Z,B_cross Z>+2delta<Z,WZ-F_J>,
    A>=0, B>=0, AB>=C^2.                               (16)

The Hermitian version has |C|^2. The equality of the two cross entries also
gives, for every h,k in this window,

    4<u_h,B_cross v_k>
       =2delta[<u_h,J_k Wg>-<v_k,S_h Wg>].              (17)

This follows by pairing the two equations (15), using symmetry of W, and
cancelling the same W cross term. No crossing or force term is removed
from (16). With identical coefficients, U+Z=2sum_h c_h E_h f_h is a
trace-repaired future P source. This is a domain statement, not a uniform
upper bound for its energy. If zero is included by a trace limit, the
conventions remain S_0=2I and J_0=0.

## 6. A complete prime-2 cusp calibration

The kernel in (12) is not positive semidefinite for arbitrary compact
sources in place of the actual null g. The following explicit calibration
retains the complete reflection operator and potential.

Put b=log 2 and j=alpha_2 psi'(0)/psi(b)>0. Near b the true potential has

    V(x)=j(b-x)_+ + V_reg(x),                           (18)

where V_reg has uniformly O(h^2) second differences. Indeed the n=2 term
is alpha_2 psi(b-x)/psi(x) on x<b and zero on x>b. Subtracting its linear
part leaves a C^(1,1) function. The other prime rows are smooth in a fixed
neighborhood of b, and their derivatives converge normally by the theta
tail. Thus, with A_h(x)=V(x+h)+V(x-h)-2V(x),

    A_h(b)=jh+O(h^2),
    A_h(b+-h+e)=O(h^2+|e|).                            (19)

For compact f whose relevant shifts stay away from the wall, expanding
the two symmetric shifts gives the exact multiplication identity

    <S_hf,V S_hf>-<f,V S_h^2f>
      =int A_h(x)f(x)^2dx
         -int A_h(x+h)f(x)f(x+2h)dx.                  (20)

Fix a nonnegative smooth bump phi supported in (-1,1) with ||phi||_2=1,
and let

    phi_h(x)=h^(-3/2)phi(x/h^3),
    f_h^test(x)=phi_h(x-(b-h))+phi_h(x-(b+h)).           (21)

For sufficiently small 0<h<b/4 these supports are disjoint, and f_h^test
and all its shifts in (20) remain away from zero. The first integral in
(20) is O(h^2). The only overlap in its second integral is between the two
identical bumps, whose product integral is one; (19) therefore gives

    <S_h f_h^test,V S_h f_h^test>
       -<f_h^test,V S_h^2 f_h^test>=-jh+O(h^2).         (22)

The COMPLETE reflected-prime contribution to this difference is zero.
To see this, extend f_h^test by zero to the full line. On all the shifted
supports under consideration, the half-line symmetric translations agree
with the full-line ones. Every full-line reflection f(x)->f(d_n-x)
commutes with the symmetric translation sum. Its two quadratic pairings
therefore agree; their restrictions are exactly the half-line pairings
with R_(d_n). Only finitely many labels can meet these compact supports,
so summing all the reflected rows preserves equality. Consequently

    K_(f_h^test)(h,h)=-2jh+O(h^2)<0.                   (23)

All sources in this calibration are compact original-P sources. They are
not asserted to be actual-null sources. Thus (23) is compatible with (13)
and demonstrates why the actual equation, not universal W convexity,
is essential to the constraint.

## 7. Scope

Equations (13) and (16) are genuine finite original-form inequalities on
the SAME actual source. Their proofs retain all prime powers, the reflected
Gamma row, the full pole, and every trace repair. They provide no upper
bound for either energy in (16), no original-P domain at large arithmetic
translations, and no independent reverse sign for the critical two-field
prime correlation. In particular this report does not prove the required
all-epsilon genuine-prime load bound or the Riemann hypothesis.
