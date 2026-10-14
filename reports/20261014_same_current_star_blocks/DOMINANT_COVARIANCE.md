# A coherent full-boundary completion for the dominant current variance

This is an exact conditional block comparison for an actual positive-depth
source. It identifies a single original-space covariance whose diagonal is
the dominant conditional variance e^2/epsilon. It retains its entire Gamma
wall, reflected-prime and pole forms, as well as any common-neutral cost.
It does not turn the first-label error into an actual null source or infer
that a positive dominant block excludes the complete original state.

## 1. Same current and the positive spatial block

Use the actual complete current w, its first label v=w_1, and

    u=T w, e=v-u, q=1-p_1, epsilon=q/p_1,
    omega=1/epsilon, mu_0=psi^2, m=mu_0 omega,
    abar=q^(-1)sum_(n>=2)p_n a_n.

The complete theta posterior gives omega smooth, positive and increasing.
The verified actual tail has e=O(poly(z)exp(-3z)), where z=pi exp(2x),
while omega=O(poly(z)exp(3z)). At zero e is bounded and omega has a finite
positive value. All labels and true prime-power rates are retained.

In the independently verified
[two-group spatial factor](TWO_GROUP_SPATIAL.md),
put Y_1=0 and Y_n=e/q for n>=2. The exact spatial identity is

    E_sp[Y]=F[e]+F_m[e]+int C_omega e^2
                              +int m(abar-a_1)e^2.             (1)

Here F is the one-forward-orientation original Gamma/prime form,
F_m=integral m Gamma_G, and

    C_omega(x)=psi(x)int_0^x kappa(x-y)psi(y)
                                  [omega(x)-omega(y)]dy
       +psi(x)sum_(d_n<x)alpha_n psi(x-d_n)
                                  [omega(x)-omega(x-d_n)].     (2)

The weighted-form passage in
[the dominant same-current completion](DOMINANT_COMPLETION.md)
establishes finiteness of every term in (1), and the two-group factor
identifies its spatial energy. No derivative trace at a prime knot is assumed. The exact
spatial projection factor is also the two-group completion, not a second
independent energy budget. Its potential is positive because
abar>=a_2>a_1+3log2.

## 2. One genuine coherent covariance, not only its diagonal

Define the positive measure on [0,infinity)

    dnu(a)=omega(0)delta_0(da)+omega'(a)da,
    h_a(x)=e(x)1_(x>=a).

Then the direct-integral feature map has covariance

    K_D(x,y)=int h_a(x)h_a(y)dnu(a)
            =e(x)e(y)omega(min(x,y)).                         (3)

It is positive semidefinite for every finite set of positions. It can
also be realized as X(x)=e(x)B_(omega(x)) for a single real Brownian motion;
no stochastic realization is needed for any proof below. Its diagonal
is exactly K_D(x,x)=e(x)^2/epsilon(x), the dominant part of the SAME V.
It is not the full current covariance, and it does not prescribe a joint
law for the genuine higher-label remainder.

For 0<x<y its squared-increment kernel is exactly

    D_D(x,y)=omega(x)|e(x)-e(y)|^2
                          +[omega(y)-omega(x)]|e(y)|^2.       (4)

For reversed endpoints use the symmetric version. Complex sources use
conjugated covariance and the identical squared-modulus formula. Inserting
(4) into the original forward Gamma and EVERY prime edge gives

    F_D:=int F[h_a]dnu(a)
         =F_m[e]+int C_omega e^2.                            (5)

The upper-endpoint term in (4), including its full incoming arithmetic row,
is precisely (2). It is not discarded as a diagonal correction. Equations
(1) and (5) give

    E_sp[Y]=F[e]+F_D+G_D,
    G_D=int m(abar-a_1)e^2>=3log2 int m e^2.                 (6)

Thus the same dominant spatial block has an explicit original-space
covariance factor, rather than merely a positive scalar storage density.

## 3. The full boundary and the full pole

Use the original boundary graph conventions

    H[f]=int_(x,y>0)kappa(x+y)psi(x)psi(y)|f(x)-f(y)|^2dxdy,
    N[f]=sum_n alpha_n int_0^d_n psi(x)psi(d_n-x)
                                    |f(x)-f(d_n-x)|^2dx,
    P_pole[f]=4int sigma(x)psi(x)sigma(y)psi(y)
                                    |f(x)-f(y)|^2dxdy,
    sigma(x)=sinh(x/2), int sigma psi=1/8,
    B_delta=H+(1-delta)N-P_pole.

Define H_D,N_D,P_D by replacing each squared difference by the ONE
kernel D_D. Then exactly

    B_D:=H_D+(1-delta)N_D-P_D
         =int B_delta[h_a]dnu(a).                           (7)

Every reflected prime power and the polar coefficient 4 are retained.
In particular P_D is not replaced by a freely adjustable diagonal or a
new rank-one norm. Each of its terms is the original pole applied to a
lawful feature source. The separate positive edge integrals are finite:

    H_D <=4int psi(Hpsi) omega |e|^2,
    N_D <=4int psi L omega |e|^2,
    P_D <=int sigma psi omega |e|^2.                        (8)

The complete original rows on the right have at most exponential growth
before multiplication by psi. The actual squared theta margin of e,
with omega, makes all three tails integrable. At zero psi=O(x), omega and
e are bounded, and the already verified original boundary rows are locally
integrable. Consequently signed interchange in (7) is legitimate only
after these three positive integrals have each been paid.

The audited complete boundary graph theorem implies B_D>=0. More
importantly, (7) supplies the exact boundary object that matches (5), not
an unrelated scalar upper bound for dominant variance.

## 4. Legality of the feature sources and integrated Q

For every a>0 the source psi h_a is in the original P completion. It has
the unchanged actual theta tail and vanishes in an origin neighborhood.
The single jump at a is allowed by the logarithmic Gamma form. Explicitly,
cutting the already finite F[e] introduces only the cross-edge term with
bounded e. Near a its continuous cost is bounded by a constant times
int_0^eta int_0^eta (s+t)^(-1)dsdt, which is finite. The complete prime
cross-edges are finite by the actual theta rows. Smooth approximations
of the cutoff converge in F: their extra near-jump cost is
O(eta[1+|log eta|]), while the original F[e] part converges by dominated
convergence. The separate boundary and pole terms converge by (8) and
ordinary bounded theta envelopes. Original-P closure follows from its
exact expression 2F-H+P_pole. The a=0 source is the already lawful psi e.
No claim that these sources are actual top-kernel states is needed.

If the centered realization of P is used, subtract the appropriate
constant multiple of psi from each feature; all displayed ratio-difference
forms are unchanged. The full pole is retained before this recentering.
There is no assertion that the cut sources retain the original pole
centering on their own.

By (5) and (8), the feature family has finite integrated original P and N.
The actual PSD hypothesis Q_delta>=0 therefore gives the lawful identity
and inequality

    Q_D:=int Q_delta[psi h_a]dnu(a)=2F_D-B_D>=0.             (9)

The measure nu is infinite, but the displayed form integrals are finite;
no bounded total mass assumption on nu is used. One may equivalently
truncate nu first and pass by the paid positive component integrals.

## 5. Exact common-neutral compensation

Let S be a fixed lawful closed common P/N neutral span, and Pi_S its
common projection. Finite theta-jet spans suffice. Define the COMPLETE
feature leakage cost

    K_S,D=int N[Pi_S(psi h_a)]dnu(a).

It is finite and at most N_D. Common neutrality gives the exact splitting
Q_delta[z]=Q_delta[(I-Pi_S)z]+delta N[Pi_S z], hence

    Q_D-delta K_S,D
      =int Q_delta[(I-Pi_S)(psi h_a)]dnu(a)>=0.              (10)

Apply the same identity to psi e and combine (6),(9),(10). The full
neutral-compensated dominant block satisfies EXACTLY

    2E_sp[Y]-B_delta[e]-B_D
        -delta{N[Pi_S(psi e)]+K_S,D}
       =Q_delta[(I-Pi_S)(psi e)]
          +int Q_delta[(I-Pi_S)(psi h_a)]dnu(a)+2G_D
       >=6log2 int m e^2.                                 (11)

All mixed neutral coefficients are inside the common projections. The
same S is used in every feature; it is not chosen separately to remove
unpaid terms. Formula (11) is also valid with S=0.

## 6. Exact limitation for the higher-label comparison

The original current variance is V=e^2/epsilon+R_high, but (3) supplies
only a coherent realization of its dominant diagonal. It does NOT identify
the original complete current covariance, make its higher-label cross
covariance zero, or equate arbitrary pointwise posterior couplings.
Thus B_D is a specific complete boundary object that must be matched,
with the SAME higher-label and mixed terms retained, before (11) can be
used in a full source comparison.

In particular (11) uses the actual global PSD hypothesis on lawful test
sources. It is a conditional positive block with an explicit strictly
positive potential when e is nonzero, not an independent proof of global
Q positivity or a contradiction to the existence of the actual state.
The two-group spatial energy in (6) is the same energy as in the dominant
current identity and cannot be added a second time. No iteration of the
actual-input contraction or RH exclusion is asserted.
