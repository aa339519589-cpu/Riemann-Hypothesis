# A constant-projected Gamma–divisor inequality on the safe xi ray

## Theorem and scope

Let

    b=log 2, z(x)=pi exp(2x),
    c(z)=8z^3-30z^2+15z,
    xi(x)=exp(x/2-z(x))c(z(x)),
    psi(x)=sum_(n>=1)n^(-1/2)xi(x+log n), x>=0,
    kappa(h)=exp(-h/2)/(1-exp(-2h)).

For completeness, put Theta(x)=exp(x/2)sum_(n>=1)exp[-pi n^2 exp(2x)].
Gaussian Poisson summation gives Theta(-x)=Theta(x)+sinh(x/2), so
Phi=(partial_x^2-1/4)Theta is even and psi=-Phi' is odd. Differentiating
its absolutely convergent theta series gives exactly the xi sum above;
in particular psi(0)=0. The certified head concavity and positive endpoint
give psi(x)>0 up to x=.31, and thereafter every xi summand is positive.
Thus psi(x)>0 for x>0; xi is positive on x>=b. Define the complete integer and prime-power rows

    W(y)=sum_(2<=n<=exp y)n^(-1/2)psi(y-log n),
    L(y)=sum_(2<=n<=exp y)(log n)n^(-1/2)psi(y-log n),
    W_Lambda(y)=sum_(2<=d<=exp y)Lambda(d)d^(-1/2)psi(y-log d),
    m(y)=W(y)xi(y).

For a real latent field a on (b,infinity), let

    q_n(y)=n^(-1/2)xi(y+log n)/psi(y),
    R(y)=sum_(n>=1)q_n(y)a(y+log n),

    G_tail[a]=2 integral_(b<y<t)W(y)xi(t)kappa(t-y)
                                              [a(y)-a(t)]^2dydt,
    D_div[a]=2 integral_b^infinity W_Lambda(y)psi(y)
                                    Var_(q(y))[a(y+log n)]dy.

Then

    G_tail[a]-D_div[a]
       >=8*10^(-6) inf_(c in R) integral_b^infinity m(y)|a(y)-c|^2dy. (1)

The theorem holds first for smooth compactly supported latent fields plus
constants, and then for the established common-seed completion by the cutoff
argument below. This includes the actual source field a=(Mf)/xi on y>=b and
its finite polynomial theta-jet modifications. Constants are the only zero
directions in this completed weighted class.

All integer labels, all prime powers, and the conditional mean in D_div
are retained. The theorem concerns this hidden component, not the full
reflected Weil form. The remaining original transport, wall and pole terms
are identified in Section 6; no RH conclusion is drawn.

## 1. Retain the conditional mean before collecting the diagonal

Introduce the centered star form

    D_star[a]=2 integral_b^infinity W_Lambda(y)
       sum_(n>=2)n^(-1/2)xi(y+log n)[a(y)-a(y+log n)]^2dy.

The exact variance identity is

    D_star-D_div=2 integral W_Lambda psi [R-a]^2>=0.     (2)

In H=sqrt(m)a variables, collecting the proper factorizations d*n=k,
d>=2,n>=2, gives an incoming diagonal 2(L-W_Lambda)/W. The omitted label
n=1 is exactly why Lambda(k) is subtracted. In particular this diagonal
is identically zero on b<y<log 4.

The exact dilation W(y+log n)>=n^(-1/2)W(y), the complete Gaussian tail,
and a two-sided Schur row bound prove

    |D_star[a]-2 integral [(L-W_Lambda)/W]H^2|
                                         <2*10^(-6)||H||_2^2.    (3)

Specifically the forward, incoming and outgoing-diagonal row bounds are
24/20^6, 36/20^6 and 256/20^12; their sum is less than 10^(-6).
The full proof, including all normalization factors, is in
[DIVISOR_STAR.md](DIVISOR_STAR.md). No conditional mean is replaced by
an uncentered diagonal in (2).

## 2. Positive Gamma ground transform

The reversible positive Gamma generator in L2(m) is

    L_Gamma a(y)=2 integral_(t>y) kappa(t-y)xi(t)/xi(y)[a(y)-a(t)]dt
               +2 integral_(b<t<y)kappa(y-t)W(t)/W(y)[a(y)-a(t)]dt.

Let V_Gamma be its exact scalar ground row,

    L_Gamma(m^(-1/2))=V_Gamma m^(-1/2),
    V_1=V_Gamma-2(L-W_Lambda)/W.

The complete grouped integral formula, its finite-row justification and
the exact rational Gamma primitive are given in
[SAFE_RAY_FORMS.md](SAFE_RAY_FORMS.md). The auxiliary function m^(-1/2)
is used algebraically; it is not asserted to belong to the original
source-energy domain.

Set Y=b+31/100, epsilon=10^(-6), K=1000, and

    k(y)=min(m(y)^(-1/2),K), b<y<=Y;
    k(y)=m(y)^(-1/2),       y>=Y;
    h=1+epsilon k,          rho=epsilon/(sqrt(m)+epsilon).

The cap is confined to b<y<b+10^(-4), contains b<y<=b+5*10^(-7),
and h<=1001/1000 on the entire head. Outside the cap, lowering the left
values of the comparison function improves its positive-generator row:

    L_Gamma h/h>=rho V_Gamma.                          (4)

On the cap, the complete outgoing row directly gives L_Gamma h/h>-10^(-6).
The endpoint inequalities and tail estimates proving these facts are in
[CAPPED_COMPLETION.md](CAPPED_COMPLETION.md), Section 1–2, and its
separate outward endpoint checker.

## 3. The head gap and uniform scalar inequalities

The exact first-head Gamma energy has the certified constant-projected gap

    G_head[v]>=(3/4000) integral_b^Y m|v-v_bar|^2.      (5)

[HEAD_GAP.md](HEAD_GAP.md) proves (5) using bounded Gamma kernels,
a nonnegative gradient jump operator, and monotone removal of the kernel
cutoff. Its theta concavity and score inputs are verified over entire
intervals, not sampled points.

The remaining scalar bounds are

    V_Gamma>=-100sqrt(m)                 on the head outside the cap,
    rho V_Gamma>=10^(-5)                on Y<=y<=log4,
    V_1-(1-rho)V_Gamma>=10^(-5)         on y>=log4.      (6)

[HEAD_SCALAR.md](HEAD_SCALAR.md) and its complete 66-leaf interval
certificate prove the first bound on the finite interval outside the
already controlled cap. The minimum certified lower bound for
V_Gamma+100sqrt(m) exceeds 0.124.

[BULK_COMPACT.md](BULK_COMPACT.md) proves the other two bounds through
y=3 with 999 complete interval boxes; its minimum certified lower bound
exceeds 0.0002318. The exact analytic tail proof
[BULK_TAIL.md](BULK_TAIL.md), followed by
[BULK_RHO.md](BULK_RHO.md), gives the stronger bound 1/10 for y>=3.
Every quadrature omission has an explicit grouped near-diagonal or complete
Gaussian tail bound.

Thus the scalar ground potential after the proper-divisor subtraction obeys

    L_Gamma h/h-2(L-W_Lambda)/W
       >=-10^(-4) on (b,Y),
       >=10^(-5)  on [Y,infinity).                    (7)

## 4. One global constant pays the complete mixed block

Choose the unique constant c for which

    integral_b^Y m(y)[a(y)-c]/h(y)dy=0,

and put a_0=a-c, v=a_0/h. Both G_tail and D_star are invariant under this
single global constant subtraction. Their mixed head/tail block is not
removed. The exact positive ground identity is

    G_tail[a_0]=2 integral_(y<t)W(y)xi(t)kappa(t-y)h(y)h(t)
                                                   [v(y)-v(t)]^2dydt
                       +integral (L_Gamma h/h)m a_0^2. (8)

Retain its head edges and discard only nonnegative remaining edges. Since
h>=1 and v has zero head mean, (5) gives a lower bound

    [3/(4000*(1001/1000)^2)] integral_b^Y m a_0^2

for the first term. Combining (2), (3), (7) and (8) proves the stronger form

    G_tail[a]-D_div[a]
       >=[3/(4000*(1001/1000)^2)-102/10^6]
                                        integral_b^Y m|a-c|^2
                              +(8/10^6) integral_Y^infinity m|a-c|^2. (9)

The head coefficient is greater than 8*10^(-6). Taking the infimum over
constants on the right proves (1). This is the exact constant-projected
completion; no favorable finite Galerkin matrix is used as a sign proof.

## 5. Domain and reproduction

The ground identity can be justified directly on each finite-Gamma field
with integral(1+y)m|a-c|^2<infinity. The auxiliary h is capped and bounded
at the left endpoint, locally Lipschitz at cap boundaries and integer knots,
and its future growth is paid by sqrt(xi/W). More precisely, the ABSOLUTE
grouped row

    integral rate(y,t)|1-h(t)/h(y)|dt

is bounded near the capped origin, locally bounded at the remaining knots,
and O(1+y) at infinity. Splitting |t-y| at 1/z(y) proves the last bound;
the large-separation logarithm is log z=O(y), while the left-cap correction
outside the head is exponentially smaller than the uncapped row.
This uniformly dominates every common separation-cutoff potential.
Dominated convergence for its m|a-c|^2 pairing and monotone convergence
for the nonnegative transformed kernel prove (8) without an
infinity-minus-infinity subtraction. No source-cutoff density assertion
is needed for that passage.

The complete star residual is bounded in L2(m), its multiplication row
is at most y, and its nonnegative squares satisfy Tonelli. The established
actual common-seed fields, and explicit finite polynomial theta jets,
have finite Gamma energy and the required weighted moment. Thus (9)
applies to them directly. The auxiliary h is never placed in the original
P completion.

The five mathematical checkers require Python, mpmath and numpy:

    python certify_xi_head_theta.py
    python certify_xi_lyapunov_cap.py
    python certify_xi_bulk_constants.py
    python certify_xi_compact_bulk.py
    python certify_xi_lyapunov_head.py

The default compact checker rebuilds the outward W cache; the head checker
uses the same certified complete-row routines. Generated caches and output
logs are not mathematical premises. The proofs state every analytic tail
and omitted-singularity estimate separately from the finite computations.

## 6. Exact original-source consequence and limitation

For the same origin-anchored source f=g-r_0 psi, true future inverse
phi=Mf, and R=f/psi, the division-free source identity is

    P_Gamma^future[R]+P_F[R]=G_tail-D_div+T_E,
    q[f]=G_tail-D_div+T_E-H_Gamma^diff[R]+P_pole[R]-N[R]. (10)

The full coefficient-one identity, its genuine source time derivative and
all domain qualifications are retained in
[SOURCE_IDENTITY.md](SOURCE_IDENTITY.md). In particular P_F is canceled
exactly once and cannot be spent again independently.

The remaining transport/wall/pole/reflection expression is not separately
nonnegative. On the anchored neutral theta jet
f=(partial_x^2-1/4)psi-r_0 psi, one has q[f]=0, while its true safe latent
field is nonconstant. Equation (1) is therefore strictly positive and the
remaining expression in (10) is strictly negative. See
[ORIGINAL_INTERFACE.md](ORIGINAL_INTERFACE.md). Further progress must
retain that neutral cancellation and the actual source equation; (1) by
itself is not a proof of the full original inequality or of RH.
