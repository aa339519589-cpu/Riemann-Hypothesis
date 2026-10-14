# Polynomial neutral current differences on the complete coalescing flow

This note puts the finite theta-jet neutral corrections into the SAME
coherent forward-current construction as the bounded actual ratio. Individual
polynomial currents and Abel terminals can diverge. Their pair differences
are instead stopped at the genuine coalescence time and are proved L2 here.
No assertion about moments of the absolute meeting state is substituted for
this proof, and no favorable sign of the original form is asserted.

Use the complete operational flow and its finite almost-sure coalescence
from `COHERENT_OPERATIONAL_RAY_CURRENTS.md` and
`FULL_PRIME_TAIL_CONTRACTION_AND_COALESCENCE.md`. In this note

    theta(z)=sum_(k>=1)c(k^2 z)exp(-k^2 z),
    c(z)=8z^3-30z^2+15z, z>=pi,

is the original positive source weight, not the Gaussian theta function.
The positive operational generator is

    Hv(z)=int_(y>z) theta(y)[v(z)-v(y)]/[2(y-z)]dy
         +sum_(n>=2)Lambda(n)theta(n^2 z)[v(z)-v(n^2 z)].  (1)

The Markov generator is -H. All prime powers and all shared-arrow cross
terms are included. Write (Z_s,W_s) for a coupled pair and tau for its first
meeting time. Equality is absorbing.

## 1. Polynomial weighted distances retain a negative full drift

For each integer p>=0 put

    F_p(z)=(1+z)^(p+1)/(p+1),
    D_p(z,w)=|F_p(z)-F_p(w)|,
    A_p(z,w)=int_(min(z,w))^(max(z,w)) theta(y)(1+y)^p dy.

There are a finite threshold R_p>pi and c_p>0 such that the COMPLETE pair
Markov generator satisfies

    L^(2)D_p(z,w)<=-c_p A_p(z,w),  z,w>=R_p.           (2)

Here and below constants may depend on the indicated fixed degree; there
is no uniform assertion as the number of neutral jets grows.

For the continuous arrows, order is preserved, so the exact drift for z<w
is b_p(w)-b_p(z), where

    b_p(z)=1/2 int_z^infinity theta(y)
                          [F_p(y)-F_p(z)]/(y-z)dy.

Writing the divided difference as the average of F_p' gives

    b_p'(z)=-theta(z)(1+z)^p/2
          +1/2 int_z^infinity theta(y) partial_z
                            {[F_p(y)-F_p(z)]/(y-z)}dy,
    0<=partial_z{...}<=p(1+y)^(p-1)/2                 (3)

(the last term is zero for p=0). The exact theta expansion implies, for
any fixed q>=0 and sufficiently large z,

    int_z^infinity theta(y)(1+y)^q dy
                         <=C_q theta(z)(1+z)^q.

Thus b_p'(z)<=-theta(z)(1+z)^p/4 beyond a finite threshold.

The prime acceptance rho_n(z)=theta(n^2 z) is decreasing there. A common
n jump has rate Lambda(n)rho_n(w) and increases D_p by at most
(n^(2p+2)-1)D_p. The extra lower-ray rate is
Lambda(n)[rho_n(z)-rho_n(w)]; its increase of D_p, even if it reverses the
order, is at most F_p(n^2 z)-F_p(z)<=C_p n^(2p+2)(1+z)^(p+1).
Consequently the full prime drift is at most

    int_z^w (1+y)^p B_p(y)dy,
    B_p(y)=C_p sum_(n>=2)Lambda(n)n^(2p+2)
                   [theta(n^2 y)+(1+y)n^2|theta'(n^2 y)|]. (4)

The complete normally convergent theta/prime series gives

    B_p(y)/theta(y)->0, y->infinity.                  (5)

For example, expand theta, bound Lambda(n) by n, group k=mn, and dominate
by a fixed polynomial in y times sum_(k>=2)k^C exp(-(k^2-1)y). Divide by
theta(y)>=c y^3 exp(-y) on the tail. This proves (5) for EACH fixed p with
no prime truncation. Combining (3)-(5) proves (2), for instance with c_p=1/8
after increasing R_p. This is a weighted version of the full-prime distance
contraction, not a bound obtained by omitting asynchronous prime jumps.

## 2. Entrance and uniform weighted-distance expectations

Every fixed positive polynomial F_q has a uniformly bounded nonnegative
one-state operational drift on z>=pi:

    0<=(-H)F_q(z)<=C_q.                              (6)

For the continuous term use its polynomial divided difference and the
integrable tail theta(y); for the prime term use the complete Gaussian
bound in (4). These bounds hold also at pi, with its actual finite holding
rate. They imply the crude global pair bound L^(2)D_p<=2C_p.

Let T_p be the first time both states exceed R_p. The common fixed arrow
set with destination in [R_p+1,R_p+2] and mark
0<a<1/(R_p+2-pi) sends every remaining state below R_p above it. Therefore
T_p is dominated by one exponential arrow time and E T_p<=C_p.
The larger state is not assumed bounded before this time; (6) pays all of
its polynomial jump moments honestly.

Apply Dynkin's formula first with bounded state, small-jump and prime
cutoffs. Before T_p use (6), and after T_p use (2). Localization and Fatou
give, for fixed starting states z,w and every S>=0,

    E D_p(Z_(S wedge tau),W_(S wedge tau))
       <=D_p(z,w)+C_p,
    E int_(T_p wedge tau)^tau A_p(Z_s,W_s)ds
       <=C_p[D_p(z,w)+1].                            (7)

The same proof with arbitrary finite S before the last limit proves the
occupation inequality; it does not require an unproved optional-stopping
identity at infinity. Gaussian jump tails justify the bounded cutoffs,
and the nonnegative quantities permit their removal.

## 3. Complete pair-carre bound for polynomial neutral ratios

Let v be C1 on [pi,infinity) and suppose, for a fixed integer m>=1,

    |v(z)|<=(C_v)(1+z)^m,
    |v'(z)|<=(C_v)(1+z)^(m-1).                        (8)

The full one-state operational carre Gamma_H[v] is uniformly bounded:

    sup_(z>=pi) Gamma_H[v](z)<=C_v'.                 (9)

For example its continuous integrand is bounded by
C theta(y)(y-z)(1+y)^(2m-2), and the prime sum has the same Gaussian
polynomial majorant. The pair carre for
F(z,w)=v(z)-v(w) is at most twice the sum of the marginal carres, so (9)
pays its expected integral before any fixed-degree entrance time.

More importantly, beyond a finite threshold,

    Gamma^(2)[F](z,w)<=C_v A_(2m-1)(z,w).             (10)

Here is a termwise proof retaining every shared event. Suppose z<w and
d=w-z. For the continuous lower-only arrows y in (z,w), the square increment
is [v(y)-v(z)]^2; the rate theta(y)/(2(y-z)) and (8) bound their integral by
C int_z^w theta(y)(1+y)^(2m-1)dy. For upper-only destinations y>w the rate is

    theta(y)/2 * [1/(y-w)-1/(y-z)].

Its square increment [v(y)-v(w)]^2 gives a bound
C d int_w^infinity theta(y)(1+y)^(2m-2)dy
<=C d theta(w)(1+w)^(2m-2). The common coalescing arrows contribute
lambda_coal(z,w)[v(z)-v(w)]^2, bounded by the SAME expression using
lambda_coal<=C theta(w)/d. For large states,
theta(y)(1+y)^(2m-1) is decreasing, so both are bounded by C A_(2m-1).

For a common prime n jump, the increment of F is the difference between
the values at z,w of v(n^2 y)-v(y). Its derivative is bounded by
C n^(2m)(1+y)^(m-1). Its squared contribution is therefore at most

    C Lambda(n)theta(n^2 w)n^(4m)d^2(1+w)^(2m-2).

Use d<=1+w and the complete Gaussian ratio to bound its sum by
C A_(2m-1). The extra lower-only prime contribution is at most

    C Lambda(n)n^(4m)(1+z)^(2m)
                            [theta(n^2 z)-theta(n^2 w)]
      <=C int_z^w Lambda(n)n^(4m+2)(1+y)^(2m)
                                             |theta'(n^2 y)|dy.

The full series is at most C A_(2m-1), by exactly the complete tail argument
in (5). A prime reversal causes no change in this square bound: it is a
single labelled-ray increment v(n^2 z)-v(z). This proves (10).
Combining (7), (9), and (10), at a common sufficiently large entrance,

    E int_0^tau Gamma^(2)[F](Z_s,W_s)ds
                           <=C_v[1+z^(2m)+w^(2m)].   (11)

## 4. The terminal difference really vanishes in L2

Almost-sure finite coalescence alone is not enough for this step. The elementary
polynomial bounds give, with M=max(z,w),

    |v(z)-v(w)|^2<=C_v D_(2m-1)(z,w),
    |v(z)-v(w)|^2<=C_v (1+M)^(-2)D_(2m+1)(z,w).      (12)

Indeed the divided difference in (8) gives C d^2(1+M)^(2m-2), and
D_p>=d(1+M)^p/(p+1). The estimates (7) for p=2m+1 therefore imply

    sup_S E[|F(Z_(S wedge tau),W_(S wedge tau))|^2;
                                  max(Z,W)>R]<=C_(z,w,v)/(1+R)^2.

On the complementary bounded state band, F is bounded and is exactly zero
once S>=tau. Dominated convergence and then R->infinity prove

    F(Z_(S wedge tau),W_(S wedge tau))->0 in L2.       (13)

No bound for E[max(Z_tau,W_tau)^k] was assumed or obtained. The weighted
difference moments (7) and (12) are precisely the moments needed here.

## 5. L2 polynomial current bridges and their exact mean

For finite S the stopped difference martingale is

    M_S=F(Z_(S wedge tau),W_(S wedge tau))-F(z,w)
          +int_0^(S wedge tau)[Hv(Z_s)-Hv(W_s)]ds.

Its bracket expectation is bounded by (11), so M_S converges in L2.
Combining this with (13) proves that the ordinary finite pre-meeting integral

    B_v(z,w)=int_0^tau[Hv(Z_s)-Hv(W_s)]ds             (14)

is L2, and

    E B_v(z,w)=v(z)-v(w),
    Var B_v(z,w)=E int_0^tau Gamma^(2)[F](Z_s,W_s)ds
                       <=C_v[1+z^(2m)+w^(2m)].      (15)

The integral is pathwise finite because tau is finite, the increasing paths
are nonexplosive, and Hv is locally bounded. It is NOT a difference of two
separately convergent polynomial infinite currents. All statements use the
same common noise, so bridges are linear in v and satisfy the finite-triple
cocycle identity. This follows by taking a common time beyond all three
pairwise coalescence times, before cancelling the identical future paths.

## 6. Exactly the neutral degrees required by the tangent repair

For s_j=(partial_x^2-1/4)^j psi, the ratio

    v_j(z)=s_j(x)/psi(x), x=log(z/pi)/2,

extends smoothly across z=pi. The theta polynomial expansion gives
v_j(z)=4^j z^(2j)+O(z^(2j-1)) and v_j'=O(z^(2j-1)) as z->infinity.
Thus (8) applies with m=2j. The bracket estimate uses p=4j-1 (primitive
degree 4j); terminal L2 control uses p=4j+1 (primitive degree 4j+2).
For s1 specifically these are p=3 and p=5. Adding a constant ratio changes
neither generator nor bridge.

The actual plateau ratio u=r-c_infinity already has its L2 bridge by the
bounded H^s current theorem. Write U(f)=int_0^infinity exp(x/2)f(x)dx and
J=U(psi)>0. Hence every finite neutral repair

    u#=u-sum_j beta_j[v_j-U(s_j)/J]

has an L2 bridge by linearity, without requiring its individual infinite
current or Abel terminal to converge. The constants shown only express a
possible U=0 representative and disappear from every bridge difference.

## 7. Lawful neutral projection of bridges, with covariance retained

Each bridge square is integrable against the original reflected-prime,
Gamma-wall, and pole edge measures. Equation (15) gives a polynomial in
z,w; their psi factors have theta tails. For the prime lines x+y=log n,
psi(x)psi(y) contributes exp[-pi(exp(2x)+exp(2y))]<=exp(-2pi n), paying every
fixed polynomial degree and every prime power. Near the origin the wall
measure is O(xy/(x+y))dxdy. No singular forward-Gamma path energy is inferred
from these estimates.

In particular the reflected-edge bridge gradients define random vectors in
the N edge Hilbert space with finite second moment. Their mean is the
original deterministic gradient. For a fixed finite common-neutral span S,
its N-orthogonal projection is continuous, so projection and expectation
commute. Let Z_v denote the centered random bridge gradient for v. If the
neutral ratios v_j belong to S, then exactly

    E ||(I-Pi_S) bridge(u-sum beta_j v_j)||_N^2
      =||(I-Pi_S)u||_N^2
         +E||(I-Pi_S)(Z_u-sum beta_j Z_(v_j))||_N^2.  (16)

Thus neutral subtraction is NOT free on each random current field: the
full quadratic and mixed covariance of its bridge noise remains in (16).
For the actual u, its deterministic component is N-orthogonal to S.
For a corrected source h#=g-alpha psi-sum_j beta_j s_j, let T denote
the uncentered odd source operator (T psi=sinh(x/2)/2 and T s_j=0),
and W=V_psi-F_r, with V_psi=L/psi. Starting from the original
pole-centered actual source (T+delta W)g=0, its equation is
(T+delta W)h#=-alpha sinh(x/2)/2-sum beta_j delta W s_j;
this stochastic representation does not turn it into a bare top source.

For completeness there is an all-finite signed identity avoiding the
individually divergent polynomial J and C fields. For a legal repaired ratio
v let P_B,H_B,N_B be the pole, Gamma-wall, and reflected-prime edge integrals
of E|B_v(x,y)|^2. Let V_P,V_H,V_N denote the same edge integrals of Var B_v.
Write F_G[v]=int psi^2 Gamma_psi[v]. Then the exact original ground formula
and (15) give

    Q_delta[psi v]
      =P_B-H_B-(1-delta)N_B+2F_G[v]
                         +V_H+(1-delta)V_N-V_P.       (17)

Every quantity in (17) is finite for the actual source plus finitely many
neutral jets. Its common neutral cost is still subtracted as
-delta N[Pi_S(psi v)]. Formula (17) retains the signed variance combination;
it does not give it a favorable sign, and does not assert that a random
bridge field belongs pathwise to original P. It is a lawful noncompact
comparison interface, not a closure of the remaining sign problem.
