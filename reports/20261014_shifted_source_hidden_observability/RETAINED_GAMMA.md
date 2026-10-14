# The hidden comparison retains half of its complete transformed Gamma energy

Use the [independently certified safe-xi comparison](../20261014_safe_xi_hidden_comparison/REPORT.md),
including its [exact cap](../20261014_safe_xi_hidden_comparison/CAPPED_COMPLETION.md), scalar potential bounds and [proper-divisor residual](../20261014_safe_xi_hidden_comparison/DIVISOR_STAR.md).
No new numerical input or stronger arithmetic hypothesis is introduced here.

Let b=log2, Y=b+31/100, m=Wxi, and let h be exactly the published positive
capped comparison function. Choose the SAME global constant c by

    integral_b^Y m(y)[a(y)-c]/h(y)dy=0,
    v=(a-c)/h.

Set

    E_h[a]=2 integral_(b<y<t)W(y)xi(t)kappa(t-y)
                              h(y)h(t)|v(y)-v(t)|^2 dydt.

This contains every transformed Gamma edge, including the mixed head/tail
edges. It is not only the energy restricted to the first head. Then

    B[a]=G_tail[a]-D_div[a]
       >=(1/2)E_h[a]+8*10^(-6) integral_b^infinity m|a-c|^2. (1)

The constant c in (1) is the published head-weighted mean, not an arbitrary
independently optimized constant in each term. The right side is ONE joint
lower bound for B; neither term is a second independent positive budget.

## Proof with the exact constants

The exact ground identity, the complete divisor-star domination and its
bounded residual give, before discarding any transformed positive edges,

    B[a]>=E_h[a]-(102/10^6) integral_b^Y m|a-c|^2
                     +(8/10^6) integral_Y^infinity m|a-c|^2. (2)

The certified restricted head gap and 1<=h<=1001/1000 give

    E_h[a]>=lambda integral_b^Y m|a-c|^2,
    lambda=3/[4000(1001/1000)^2].                    (3)

Retain half of E_h and use (3) only on its other half. The remaining head
coefficient is

    lambda/2-102/10^6 >8/10^6,

an immediate exact rational inequality. Substitution in (2) proves (1).
All proper divisor conditional means and the complete residual were already
included in (2). In particular this does not spend P_F again.

The proof uses precisely the existing actual/common-seed completion. The
absolute grouped-row domination and positive-kernel monotone limit from the
published proof apply unchanged. No new original-P status of the unbounded
auxiliary h is asserted.

## A directly available local source regularity consequence

For a compact interval I contained in (b,infinity), all of W,xi,h are
bounded above and below by positive constants, and xi h is Lipschitz there.
Let phi0=xi(a-c)=xi h v. Then (1), the product difference identity and
integrability of kappa(t-y)|t-y|^2 give

    ||phi0||_L2(I)^2
       +integral_(y<t in I)kappa(t-y)|phi0(y)-phi0(t)|^2 dydt
       <=C_I B[a].                                 (4)

This uses BOTH terms of the joint bound (1), not two copies of B. The
constant C_I is finite and expressible using the extrema of the positive
weights and the Lipschitz constant of xi h on I. It may deteriorate when
the interval approaches b, where W vanishes.

The same local energy pays a sharp source cutoff at any B>b. The elementary
logarithmic Hardy estimate on a finite interval is obtained from

    |v(s)|^2<=2|v(s)-v(t)|^2+2|v(t)|^2,   0<2s<t<L.

Multiplying by dt/t and then integrating ds gives

    integral_0^(L/2)|v(s)|^2 log[L/(2s)]ds
       <=2 integral_(0<2s<t<L)|v(s)-v(t)|^2/t dsdt
                    +integral_0^L |v(t)|^2dt.        (5)

Since kappa(t-s) is bounded below by a positive multiple of 1/t on this
fixed interval, (5) is controlled by the local Gamma energy and L2 norm.
The jump induced by zero extension across a fixed interior cut therefore
has the requisite finite logarithmic boundary cost. This is a quantitative
energy statement, not merely pointwise existence of a trace.

Equations (4)-(5) are local consequences. A full original-tail P or Q_delta
estimate after the future integer lift still needs its complete arithmetic,
weight and pole comparisons. The remaining signed original residual is not
claimed positive.
