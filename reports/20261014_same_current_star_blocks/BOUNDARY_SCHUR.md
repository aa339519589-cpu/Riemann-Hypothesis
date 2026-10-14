# A strict full-boundary Schur comparison for the SAME star current field

The dominant and genuinely higher-label parts of the actual star field
are not independent. Their triangular mixed kernel is retained here and
is quantitatively smaller than generic covariance Cauchy. The conclusion
is a global matrix comparison for the COMPLETE Gamma-wall/reflected-prime/
pole form. It uses all posterior labels and all original boundary edges,
not only pointwise variance or a rowwise sign. It does not exclude the
actual source or assign the missing sign to Q_delta.

## 1. The same star law and its two centered components

Use the actual current field w and the ONE initial-label star coupling in
[CURRENT_STAR_FIELD.md](CURRENT_STAR_FIELD.md).
Its exact pair law for x<y is

    Pr(N_x=N_y=n)=p_n(y), n>=2,
    Pr(N_x=n,N_y=1)=p_n(x)-p_n(y), n>=2,
    Pr(N_x=N_y=1)=p_1(x).

The full posterior is

    p_n(z)=P(n^2z)e^(-n^2z)/sum_(m>=1)P(m^2z)e^(-m^2z),
    P(t)=4t^2-6t, z=pi exp(2x).

Let u=T w, e=w_1-u, q=1-p_1, epsilon=q/p_1, and
w_tail=q^(-1)sum_(n>=2)p_n w_n. Define deterministic label fields

    D_1=e, D_n=-e/epsilon (n>=2),
    Z_1=0, Z_n=w_n-w_tail (n>=2).

Then the actual star conditional field is EXACTLY

    W(x)-u(x)=D(x,N_x)+Z(x,N_x),
    T D=T Z=0,
    T D^2=e^2/epsilon, T Z^2=R_high.

These two components are pointwise orthogonal, but are NOT orthogonal at
different positions. Write

    S_D(x,y)=E|D_x-D_y|^2,
    S_Z(x,y)=E|Z_x-Z_y|^2,
    M_DZ(x,y)=E[(D_x-D_y)conj(Z_x-Z_y)].

The theorem below applies to complex fields as well. Only the displayed
posterior law, the tail centering of Z, and finite boundary moments are
needed; no actual source equation is substituted at an individual edge.

## 2. Exact triangular mixed kernel and the two edge variances

For x<y the star law gives

    E[D_x conj(Z_y)]=0,
    E[D_y conj(Z_x)]=-e(y)/q(y) sum_(n>=2)p_n(y)conj(Z_n(x)).

Consequently the mixed EDGE covariance, with its sign retained, is

    M_DZ(x,y)=e(y) sum_(n>=2)pi_n(y)conj(Z_n(x)),
    pi_n(x)=p_n(x)/q(x), n>=2.                            (1)

This is the actual triangular term; setting it to zero would change the
joint field. Put omega=1/epsilon. The dominant edge variance is exactly

    S_D(x,y)=omega(x)|e(x)-e(y)|^2
                         +[omega(y)-omega(x)]|e(y)|^2.    (2)

The higher edge variance is exactly

    S_Z(x,y)=sum_(n>=2)p_n(y)|Z_n(x)-Z_n(y)|^2
                  +sum_(n>=2)[p_n(x)-p_n(y)]|Z_n(x)|^2.  (3)

Both the surviving-label square and the cooling-to-label1 square occur in
(3). Neither is a new independent budget.

For later use define

    t=p_2(y)/p_2(x), r=q(y)/q(x).

Every p_n/p_2, n>=3, decreases, while p_2 itself decreases. Thus
0<r<=t<1 and p_n(y)/p_n(x)<=t for all n>=2. Equation (3) implies

    S_Z(x,y)>=(1-t)R_high(x).                            (4)

The exact dominant kernel (2) implies

    S_D(x,y)>=[(1-r)/(q(x)r)]|e(y)|^2.                   (5)

## 3. Complete posterior rate comparison, with rational constants

Write R_n(z)=p_n(z)/p_2(z), n>=3, and
E_tail(z)=sum_(n>=3)R_n(z). The notation E_tail here is a posterior scalar,
NOT an energy. Differentiating the complete theta sums gives

    -d_z log R_n=(n^2-4)[1+6/((2n^2z-3)(8z-3))]
                    <=(21/20)(n^2-4), z>=pi>3.           (6)

The complete moment bound E_p N^2<17/16 follows without truncation:
p_n<=2n^4 exp[-3(n^2-1)] and hence

    E_p N^2<=1+2sum_(n>=2)n^6 exp[-3(n^2-1)]
       <1+[128/20^3]/(1-1/1000)<17/16.                  (7)

Here exp3>20 follows from its Taylor sum through degree8, and the
consecutive ratio in (7) is at most
(3/2)^6 exp(-15)<729/(64*20^5)<1/1000. All integer labels are included.

Using P(n^2z)'/P(n^2z)=1/z+2n^2/(2n^2z-3), one obtains

    d_z log p_2
       =-4+E_p N^2+8/(8z-3)
                              -E_p[2N^2/(2N^2z-3)].

The final expectation is greater than1/z. Therefore

    -d_z log p_2>4-17/16-1/21>14/5.                      (8)

Combining (6) and (8), with
lambda_n=(3/8)(n^2-4)>1, proves the finite-interval relation

    a_n:=R_n(y)/R_n(x)>=t^(lambda_n),
    0<=1-a_n<=lambda_n(1-t).                             (9)

Here a_n is only a ratio abbreviation inside this proof and must NOT be
confused with the hidden reset score a_n used elsewhere.

The full initial tail and its rate-square sum have the bounds

    E_tail(z)<1/1000,
    (1+E_tail(z))sum_(n>=3)R_n(z)lambda_n^2
           <1/384^2.                                   (10)

For an entirely rational verification, use

    R_n(z)<=n^4 exp[-3(n^2-4)]/14.

The n=3 term is retained exactly. For n>=4, bound
n^4(n^2-4)^2<=n^8; the consecutive n^8 Gaussian ratio is at most
(5/4)^8 exp(-27)<6/20^9<1/2. Hence the squared-rate expression in (10)
is at most

    (1001/1000)(9/896)[2025/20^5+131072/20^12]
       =203607432171/32000000000000000 <1/384^2.           (11)

The same tail, with n=3 numerator81 in place of2025, proves E_tail<1/1000.
The accompanying fractions-only checker reproduces every comparison.
No finite posterior truncation is declared exact.

## 4. An all-edge mixed correlation bound

Let chi^2=chi^2(pi(y)||pi(x)). Since pi(x) centers Z(x), (1) and weighted
Cauchy give

    |M_DZ(x,y)|^2
          <=|e(y)|^2 R_high(x) chi^2/q(x).                (12)

There is a useful exact tail formula. Set E_x=E_tail(x), E_y=E_tail(y),
v=E_x-E_y, and d2=sum_(n>=3)R_n(x)(1-a_n)^2. Then

    chi^2=[(1+E_x)d2-v^2]/(1+E_y)^2
       <=(1+E_x)sum_(n>=3)R_n(x)lambda_n^2(1-t)^2
       <(1/384^2)(1-t)^2.                               (13)

In particular the signed normalization subtraction -v^2 is not replaced
by an independent resource; it is retained in the equality and discarded
only for the stated upper estimate.

Combining (4),(5),(12),(13) yields

    |M_DZ(x,y)|^2/[S_D(x,y)S_Z(x,y)]
       <=chi^2 r/[(1-r)(1-t)] <=1/384^2,                 (14)

because r<=t. If a denominator vanishes, the same inequality follows
directly from (12); at x=y all edge increments vanish. Thus for ALL edges,

    |M_DZ(x,y)|<=(1/384)sqrt(S_D(x,y)S_Z(x,y)).            (15)

This is much stronger than generic covariance Cauchy. It is possible
because the actual conditional tail is overwhelmingly label2, and its
small higher-label reweighting is compared to BOTH positive cooling terms,
not just to the marginal variance at one endpoint.

## 5. The COMPLETE signed boundary Schur block

Use the exact original forms

    B_delta=H+(1-delta)N-P_pole, 0<=delta<=1/3,
    A_delta=H+(1-delta)N+P_pole=B_delta+2P_pole.

The definitions, factors of two and polar mass are those of the published
[complete boundary graph](../20261014_boundary_graph_coercivity/REPORT.md).
In particular

    P_pole[f]=int sigma psi |f-c|^2
                      -8|int sigma psi(f-c)|^2
             <=(1/2)int mu|f-c|^2,
    sigma=sinh(x/2), mu=psi exp(x/2).

The published
[strong-metric boundary corollary](../20261014_same_current_boundary_transfer/NORMALIZED_BOUNDARY_TRANSFER.md)
gives, with its SAME spatial mean c=c_(0,7/10)(f),

    B_delta[f]>=(1/100)int mu|f-c|^2.

Consequently the full positive edge envelope obeys

    A_delta[f]<=101 B_delta[f].                          (16)

This retains the negative polar rank-one term in its correct direction.
It is a consequence of ONE complete boundary form, not an independently
added use of its coercivity.

Define the random-field boundary diagonals and cross pairing by

    B_D=E B_delta[D], B_Z=E B_delta[Z],
    B_DZ=E B_delta(D,Z).

Apply (15) on every H, reflected-prime and pole edge. Taking the absolute
value of the signed sum only at this step, then Cauchy in the COMPLETE
positive edge measure A_delta, gives

    |B_DZ|<=(1/384)sqrt(A_D A_Z)
            <=(101/384)sqrt(B_D B_Z).                    (17)

Thus the full SAME-star boundary covariance has the two-sided comparison

    (283/384)(B_D+B_Z)
         <= E B_delta[D+Z]
         <=(485/384)(B_D+B_Z).                            (18)

Every true reflected prime power, both edge orientations, and the exact
pole have been included. Formula (17) is a nonlocal signed graph result,
not merely a bound on its diagonal rows.

The same argument works for arbitrary finite families of dominant fields
and tail-centered fields using the same star law. If G_D,G_Z are their
boundary Gram matrices and C their mixed matrix, then

    [[G_D,C],[C*,G_Z]] >=(283/384) diag(G_D,G_Z).            (19)

One obtains (19) by applying (17) to arbitrary linear combinations on each
side. No density or independence of the two families is assumed, and the
common constant null mode of B is left intact.

## 6. Domain and exact accounting

For the actual current, E|D(x)|^2=e^2/epsilon<=V<=J and
E|Z(x)|^2=R_high<=V<=J, where sup J is finite. The three complete boundary
edge measures have finite total mass by the original theta/all-prime
bounds. Therefore all H,N,P expectations above are finite, as are the
mu-centered norms used in (16). Tonelli and Cauchy justify the full sums.
No random original-P membership or forward-energy estimate is required.

This is the SAME star conditional field W, with W-u=D+Z. If I denotes the
complete current on that coupling, its additional future-driver noise has
zero conditional mean given the initial star labels. Its boundary covariance
is a separate nonnegative B-Hilbert term. Thus (18) can be inserted into the
existing full conditional covariance identity without changing a marginal
or inventing an independent label law.

The new comparison does not create a free Q gain: conditioning changes the
lifted boundary energy and its covariance subtraction together. Likewise
B_D is the exact dominant kernel in
[the dominant boundary completion](DOMINANT_COVARIANCE.md),
while the two-group spatial energy remains the same already-accounted
hidden block. The actual reflected/pole term, higher-label spatial terms,
complete source forcing and any neutral projection costs still have to be
matched in the full signed source comparison. No Q_delta exclusion or RH
claim is made.
