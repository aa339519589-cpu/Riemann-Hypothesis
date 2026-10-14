# A coercive full Gamma-wall/reflected-prime/pole graph

This note proves a signed NONLOCAL boundary comparison, not just positivity
of a diagonal row. It includes the complete reflected prime-power measure
and the original coefficient of the pole. It signs the entire bridge
variance correction in the coalescing-current identity. It does not prove
positivity of the full original Q_delta form.

## 1. Definitions and theorem

Use the original positive odd-theta source psi=-Phi' on x>0 and

    kappa(t)=exp(-t/2)/(1-exp(-2t)), s(x)=sinh(x/2),
    d_n=log n, alpha_n=Lambda(n)/sqrt(n), int_0^infinity s psi=1/8.

For real or complex ratios u define

    H[u]=int_(x,y>0) kappa(x+y)psi(x)psi(y)|u(x)-u(y)|^2 dxdy,
    N[u]=sum_(n>=2) alpha_n int_0^d_n psi(x)psi(d_n-x)
                                      |u(x)-u(d_n-x)|^2 dx,
    P[u]=int s psi |u|^2 -8|int s psi u|^2
        =4 int_(x,y>0) s(x)psi(x)s(y)psi(y)|u(x)-u(y)|^2 dxdy.

The last equality uses the EXACT total mass 1/8. In particular P is the
full original polar difference form, not an independently rescaled rank-one
term. Put R=7/10, C=(0,R), T=(R,infinity), and

    M_C=int_C psi,  c_C(u)=M_C^(-1)int_C psi u.

**Theorem.** For every 0<=delta<=1/3 and every ratio for which the displayed
forms are finite (in particular the actual bounded ratio and all finite
theta-jet repairs),

    B_delta[u]:=H[u]+(1-delta)N[u]-P[u]
             >=(9/50) int_0^infinity psi(x)|u(x)-c_C(u)|^2 dx. (1)

Thus this complete signed graph is positive semidefinite and its only
zero vectors are constant ratios. The same statement applies to measurable
random ratio fields whenever the three nonnegative edge forms have finite
expectation; it does NOT require original-P membership of the random field.

The theorem uses the unconditional Chebyshev bounds and complete theta
estimates already proved in
[the complete reflected-row tail proof](../20261014_positive_reflected_storage/ANALYTIC_TAIL.md)
and [the actual-depth extension](../20261014_positive_reflected_storage/ACTUAL_DEPTH_STORAGE.md),
together with [the directed-interval checker](certify_boundary_graph.py). No arithmetic cutoff replaces N.

## 2. Exact central/tail graph decomposition

Write beta=1-delta, so 2/3<=beta<=1, and v=u-c_C(u). All three graph forms
are invariant under this constant subtraction. Since kappa is decreasing,

    H[u]>=H_CC[u]
         >=kappa(2R) int_(C x C) psi(x)psi(y)|v(x)-v(y)|^2 dxdy
         =h_C int_C psi|v|^2,
    h_C=2kappa(2R)M_C.                                (2)

The last factor two is the symmetric central pair integral, and the mean
of v under psi on C is zero. On the other hand the exact polar formula gives

    P[u]=int s psi|v|^2-8|int s psi v|^2
         <=int s psi|v|^2.                            (3)

For x>R and y<R define the two complementary reflected rows

    L_C(x)=sum_(0<d_n-x<R) alpha_n psi(d_n-x),
    L_T(y)=sum_(d_n-y>R) alpha_n psi(d_n-y).

Endpoints have no effect in the form integrals. Both orientations of the
reflected edges occur in N, so its cross part is EXACTLY

    N_CT[u]=2 int_T psi(x) sum_(0<d_n-x<R) alpha_n psi(d_n-x)
                                      |v(x)-v(d_n-x)|^2 dx. (4)

Discarding N_CC and N_TT is favorable. For

    epsilon=1-1/(2beta),  1/4<=epsilon<=1/2,

use |a-b|^2 >= (1-epsilon)|a|^2-(epsilon^(-1)-1)|b|^2.
Changing variables y=d_n-x in the negative central contribution gives

    beta N_CT[u]
      >=int_T psi L_C |v|^2
          -[2beta/(2beta-1)]int_C psi L_T |v|^2
      >=int_T psi L_C |v|^2-4int_C psi L_T |v|^2.      (5)

Here 2beta(1-epsilon)=1, and 2beta/(2beta-1)<=4. This is the worst actual
endpoint delta=1/3; neither an orientation nor a beta factor is dropped.
Combining (2), (3), and (5) proves

    B_delta[u]>=int_C psi[h_C-s-4L_T]|v|^2
                      +int_T psi[L_C-s]|v|^2.         (6)

It remains to certify the two scalar brackets, with their complete tails.

## 3. The central bracket has a uniform strict margin

The checker rigorously encloses

    h_C>0.9401707510149349,
    s(R)<0.3571897294372720,
    sup_(0<=y<=R)L_T(y)<0.0994192011514519.             (7)

Consequently

    h_C-s(y)-4L_T(y)>0.1853042169718555>9/50,
                                                  0<=y<=R. (8)

Here is the entire tail majorant behind the last row bound; it is not a
finite sum asserted to be exact. Put c(z)=8z^3-30z^2+15z. Every derivative
theta term exp(x/2)c(m^2 pi exp(2x))exp(-m^2 pi exp(2x)) decreases once its
argument is >=12: its derivative polynomial is

    -16z^4+112z^3-165z^2+(75/2)z<0, z>=12.

Since pi exp(2(log4-R))>12, this gives

    L_T(y)<= [alpha_2+alpha_3]psi(R)
                 +sum_(n>=4)(log n)/sqrt(n) psi(log n-R). (9)

For n=2,3 use the restriction d_n-y>R and monotonicity on the tail; retaining
the n=2 majorant even when its restriction is empty is harmless. For n>=4
use d_n-y>=log n-R and Lambda(n)<=log n, which is only used for this UPPER
bound. The actual lower rows always retain true prime powers.

For z=pi exp(2x)>12 the complete theta upper enclosure is

    psi(x)<=exp(x/2)[c(z)exp(-z)+1024 z^3 exp(-4z)].    (10)

Indeed c(m^2z)<=8m^6z^3 and the ratio of consecutive m^6 exp(-m^2z) terms
for m>=2 is at most (3/2)^6 exp(-5z)<1/2. The inner omitted tail is thus
at most 8z^3*(2*64)exp(-4z). The checker sums (9) through n=16 with (10).
For n>=17 let a=pi exp(-2R). Since log n<=n, the complete summand is at most

    16 exp(-R/2)a^3 n^7 exp(-a n^2).

Its consecutive ratio is <=(18/17)^7 exp(-35a)<1/2, so the entire outer
remainder is at most 32exp(-R/2)a^3 17^7 exp(-289a). This pays every integer
and every theta label in (9).

For the first enclosure in (7), use Phi(0) greater than its positive first
theta term and the complete bound

    Phi(R)<=exp(R/2)[(4z^2-6z)exp(-z)+128z^2exp(-4z)],
    z=pi exp(2R).

This encloses M_C=Phi(0)-Phi(R) from below. All exponentials, pi, square
roots and logarithms in these enclosures use directed intervals.

## 4. Complete truncated reflected tail row

The remaining estimate is the genuinely truncated row inequality

    L_C(x)-s(x)>1/4, x>=R.                           (11)

### 4.1 Analytic all-prime tail

Set F(t)=exp(-t/2)psi(t), X=exp(x), and

    J_C=int_0^R exp(t/2)psi(t)dt,
    I_C,+=int_0^R exp(t)max(F'(t),0)dt.

The complete theta estimates from the cited reflected-storage proof give
J>507/500 and I_+<293/100. For t>=R, each Phi term has logarithmic derivative
at most 13/2-2z<-35/2, z=pi exp(2t)>12. Therefore

    int_R^infinity exp(t/2)psi(t)dt
      <=exp(R/2)Phi(R)*(35/34)<7/500.

This is integration by parts followed by
int_R^infinity exp(t/2)Phi(t)dt<=exp(R/2)Phi(R)/17.
Hence J_C>1, while I_C,+<=I_+<293/100. The actual certified J_C lower bound
is 1.0105185792183015.

For X>=349 the unconditional Rosser--Schoenfeld bounds give

    .91Y<Psi_C(Y)<1.04Y, Y>=349,
    Psi_C(Y)=sum_(n<=Y)Lambda(n).

Stieltjes integration with the complete moving window yields

    L_C(x)/sqrt(X)
       =F(R)Psi_C((X exp R)-)/X
               -int_0^R F'(t)Psi_C(X exp t)/X dt
       >=.91 J_C-.13 I_C,+
       >5291/10000.                                  (12)

The negative endpoint jump of F*1_[0,R] is INCLUDED in the first term.
At an upper prime threshold the left-limit bound follows by approaching
X exp R from below; this endpoint is strictly greater than349. The lower
endpoint contributes zero because F(0)=0. Thus no truncated-prime boundary
has been discarded with the wrong sign.

Since s(x)=(exp(x/2)-exp(-x/2))/2, (12) gives

    L_C(x)-s(x)>(291/10000)exp(x/2)+(1/2)exp(-x/2)>1/2,
                                               x>=log349,   (13)

using sqrt349>18 and 291*18>5000.

### 4.2 Rigorous compact certificate

On the 530 closed cells [j/100,(j+1)/100], 70<=j<600, the checker retains
only genuine prime powers n<=1024 whose ENTIRE interval d_n-X lies inside
(0,R). A term crossing either moving endpoint is omitted favorably, because
the complete psi is nonnegative. On each retained interval it uses the
first derivative-theta term only when its interval lower bound is positive;
all omitted theta labels m>=2 are positive. It subtracts the interval upper
bound for s(X).

The minimum certified L_C-s margin is greater than0.3601803038492796, attained
on the cell [1.06,1.07]. In particular every cell has margin>1/4. Since
log349<6, this overlaps (13) and proves (11) on the whole half-line tail.
No point sampling, unproved prime density, or finite-prime surrogate enters.

## 5. Conclusion and lawful bridge covariance consequence

Insert (8) and (11) into (6):

    B_delta[u]>=(9/50)int_C psi|v|^2+(1/4)int_T psi|v|^2
               >=(9/50)int_0^infinity psi|v|^2.

This proves (1), with the constant mode retained exactly. The argument
passes from bounded truncations to its finite-form domain by the displayed
positive estimates; alternatively every step applies directly when the
three edge forms are finite and a representative is locally square
integrable under psi.

For the [coherent polynomial-neutral bridge theorem](../20261014_coherent_prime_ray_bridges/POLYNOMIAL_NEUTRAL_CURRENT_BRIDGES.md), fix a reference start
and write Z_u(x) for its centered random bridge field. The cocycle identity
means Var B_u(x,y)=E|Z_u(x)-Z_u(y)|^2. The polynomial moment bounds proved
there pay all three edge expectations and the psi-weighted central mean.
Applying (1) samplewise and then Tonelli to its nonnegative constituents
therefore gives the ENTIRE signed variance comparison

    V_H+(1-delta)V_N-V_P
       >=(9/50) E int psi |Z_u-c_C(Z_u)|^2 >=0.        (14)

This uses only the finite wall, reflected-prime and pole graph energies.
It does not assume finite expected singular forward-Gamma energy or
samplewise original-P membership of Z_u. The exact finite neutral
projection and every mixed stochastic neutral covariance from the bridge
theorem remain; (14) can be polarized and compressed in any finite neutral
bridge family, without deleting its Gram cost.

Finally the full original form remains

    Q_delta[psi u]=2F_G[u]-B_delta[u]
       =P_B-H_B-(1-delta)N_B+2F_G[u]
                              +V_H+(1-delta)V_N-V_P.

The positive variance correction (14) is NOT an independent free surplus:
it is exactly the difference between the lifted boundary form and its
mean-field boundary form. Proving B_delta[u]<=2F_G[u] on the actual source
or obtaining a contradictory full compensated bound remains open.

The exact positive decomposition, including every retained square and the
common neutral quotient interpretation, is in
[POSITIVE_FACTORIZATION.md](POSITIVE_FACTORIZATION.md).

To reproduce the certificate, run `python certify_boundary_graph.py`.
Only Python and mpmath are needed; no prime table or network access is used.
The expected output is [boundary_graph_certificate.json](boundary_graph_certificate.json).
