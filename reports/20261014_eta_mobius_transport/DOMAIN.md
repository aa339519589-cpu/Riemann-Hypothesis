# Complete Gamma domain for the actual eta star coupling

This note justifies the infinite-label Gamma coupling on the actual fixed-depth source. It retains both the same-half-line difference kernel and the odd reflected sum kernel. The Jensen defect has an explicit sign and is subtracted from the lifted energy; it is not a free lower bound for the original form.

## 1. Actual inverse seed and a sufficient weighted Sobolev estimate

Use the probabilities and coherent coupling gamma_(x,y) proved in the [companion eta transport theorem](ETA_TRANSPORT.md); for y<x transpose that coupling. Let the actual source be g=psi r, with

    r=c_infinity+h,    h in H^s_even(R),  1/2<s<1.

Set, only on x>=0,

    f=Mg=sum_(k>=1)mu(k)k^(-1/2)g(x+log k),
    v=f/eta,    F_n(x)=v(x+log n).

The unanchored f is used as a latent seed, not asserted to belong to the original P domain. Absolute future divisor collection gives C f=g and consequently

    m(x):=sum_n p_n(x)F_n(x)=g(x)/Phi(x).               (1)

One useful sufficient bound, valid for this actual seed, is

    w(x)=exp(-4x)v(x) belongs to H^s(0,infinity).        (2)

Here is a direct verification. Write

    exp(-4x)v(x)=sum_k a_k(x)r(x+log k),
    a_k(x)=exp(-4x)mu(k)k^(-1/2)psi(x+log k)/eta(x).

For k=1, eta is strictly positive on x>=0, psi/eta is smooth, and psi/eta=O(exp(2x)) with the same bound for its first derivative. Thus a_1 belongs to H^1 and W^(1,infinity). For k>=2 the explicit theta series gives

    ||a_k||_(H^1)+||a_k||_(W^(1,infinity))
       <=C k^C exp(-c k^2),                            (3)

for fixed positive constants C,c. This follows by dividing the shifted theta tail by eta(x): the exponent has the strictly favorable difference -pi(k^2-1)exp(2x), and every derivative or polynomial factor is absorbed by that difference. The translated h have uniformly bounded half-line H^s norms; the constant part of r is paid by the H^1 norm of a_k. Multiplication by these W^(1,infinity) coefficients is bounded on H^s for 0<s<1. Summing (3) proves (2).

In particular v is continuous and |v(x)|<=C exp(4x). Every p-weighted second moment

    M_2(x)=sum_n p_n(x)|F_n(x)|^2                       (4)

is finite and continuous, with uniform convergence on compact x intervals; moreover M_2(x)<=C exp(8x), since all fixed moments of n under p(x) are uniformly bounded for x>=0. Formula (1) preserves the exact actual-source constraints

    m(0)=0,       integral_0^infinity sinh(x/2)Phi(x)m(x)dx=0.

These are mean constraints, not zero conditions on individual F_n(0).

## 2. Full positive-half-line Gamma lift

Let kappa(t)=exp(-t/2)/(1-exp(-2t)). Define

    J_-(x,y)=sum_(n,j)gamma_(x,y)(n,j)|F_n(x)-F_j(y)|^2,
    J_+(x,y)=sum_(n,j)gamma_(x,y)(n,j)|F_n(x)+F_j(y)|^2.

Use the source-form Gamma convention: one half of the full-line double jump integral. Its complete coupled energy is

    G_Gamma^star=integral_(x,y>0) Phi(x)Phi(y)
       { kappa(|x-y|) J_-(x,y)+kappa(x+y) J_+(x,y) } dxdy.
                                                               (5)

Both terms are finite on the actual source class.

For the same-index part of J_-, order x<=y and put t=y-x. Its exact weights are p_1(x) for label 1 and p_n(y) for n>=2. On 0<t<1, write v(u)=exp(4u)w(u). The inequality

    |v(u+t)-v(u)|^2
      <=C exp(8(u+t))
          { |w(u+t)-w(u)|^2+t^2|w(u)|^2 }

reduces the singular kernel to the H^s difference seminorm of w. For n>=2 the coefficient Phi(x)n^(-1/2)eta(y+log n), after the displayed exponential factor is inserted, is bounded by C n^C exp(-c n^2). These bounds are summable. The n=1 coefficient is bounded separately. For t>=1, the squared-value bound and theta tails suffice.

For the genuine n-to-1 transfer part, the exact score and E_p[n^2]<4 give

    0<=-p_n'(u)<=C n^6 exp(2u)
                     exp[-pi(n^2-1)exp(2u)], n>=2.

The right side is decreasing in u>=0 up to a harmless fixed factor. Hence, for 0<t<1,

    0<=p_n(x)-p_n(x+t)
       <=C t n^6 exp(2x)exp[-pi(n^2-1)exp(2x)].        (6)

The factor t pays kappa(t) at the diagonal, even though the transfer compares different labels. The pointwise exponential bound on v and the Gaussian n tail make its full integral finite. For t>=1 use p_n(x)-p_n(x+t)<=p_n(x) and the same theta bounds. No independent-index diagonal term is introduced.

Finally, regardless of the coupling,

    J_+(x,y)<=2M_2(x)+2M_2(y).

The reflected row integral integral_0^infinity Phi(y)kappa(x+y)dy is O(1+|log x|) at x=0 and decays at infinity. Compact continuity of (4) and the complete theta bounds therefore pay the entire reflected sum term. This proves finiteness of (5), including its origin corner.

All label expansions above are sums of nonnegative terms, so Tonelli applies. Finite label partial sums and compact x,y cutoffs converge to their full energies. The displayed domination independently gives convergence of the means and permits their Jensen limits. There is no cancellation between separately infinite quantities.

## 3. Exact signed identity and the retained origin variance

Put

    D_-(x,y)=J_-(x,y)-|m(x)-m(y)|^2,
    D_+(x,y)=J_+(x,y)-|m(x)+m(y)|^2.

These are the variances of F_N(x)-F_J(y) and F_N(x)+F_J(y) under the stated joint coupling. In particular both are nonnegative. The even-Phi Gamma source-form ground energy of the odd source g (not the original psi-gauge summand P_Gamma) is exactly

    G_Gamma[g]=G_Gamma^star
       -integral_(x,y>0)Phi(x)Phi(y)
         {kappa(|x-y|)D_-(x,y)+kappa(x+y)D_+(x,y)}dxdy.
                                                               (7)

Every quantity in (7) is finite by Section 2. This convention is one half of the full-line double difference energy: after splitting into two same-sign and two opposite-sign quadrants, each displayed positive-quadrant term has coefficient one. Thus G_Gamma is exactly G+W_Gamma in the complete source identity, not twice that quantity.

At equal arguments the coupling is diagonal. Therefore

    D_-(x,x)=0,
    D_+(x,x)=4{M_2(x)-|m(x)|^2}.                       (8)

In particular the actual origin mean m(0)=0 leaves the boundary variance D_+(0,0)=4M_2(0), not zero in general. Its reflected kernel is integrable, but the term must be retained. Neither trace centering nor scalar optimality of the logarithmic transport cost removes it.

Equation (7) supplies a rigorous domain-complete Gamma lift. To obtain a coefficient-one signed comparison, the complete arithmetic and polar terms must compensate the actual conditional-variance defect in (7), with the actual label fields. Positivity of the coupling or its optimal scalar transport cost alone does not prove that compensation.
