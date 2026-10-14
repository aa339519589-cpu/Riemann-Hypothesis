# The complete original source tail is bounded by the same hidden energy

This theorem pays the logarithmic source boundary channel at every fixed cut
B>log 2 using the retained nonlocal hidden Gamma energy. It retains the full
prime, reflected-prime, potential and pole terms in the original source
metric. It is a bounded embedding, not a favorable sign for the original
remainder. In particular it is compatible with the nonconstant neutral
examples for which the original form vanishes.

## 1. Statement and the one available budget

Put b=log 2, z(x)=pi exp(2x),

    xi(x)=exp(x/2-z(x))c(z(x)),
    c(z)=8z^3-30z^2+15z,
    W(x)=sum_(2<=n<=exp x)n^(-1/2)psi(x-log n),
    m=W xi,  q=xi/W,  kappa(t)=exp(-t/2)/(1-exp(-2t)).

Thus xi,W are positive on (b,infinity). To distinguish the original
reflected row from an integer log row, throughout this report write

    L_ref(x)=sum_(log n>x)alpha_n psi(log n-x),
    alpha_n=Lambda(n)/sqrt(n),  V=L_ref/psi.

Let h be the SAME capped comparison function as in the certified hidden
comparison. Explicitly, with Y=b+31/100 and epsilon=10^(-6),

    h=1+epsilon min(m^(-1/2),1000) on (b,Y),
    h=1+epsilon m^(-1/2) on [Y,infinity).

Choose c_a by the published head mean, not by a new independent projection:

    integral_b^Y m(a-c_a)/h=0,
    v=(a-c_a)/h,  M=integral_b^infinity m|a-c_a|^2,
    E_h=2 integral_(b<x<y) kappa(y-x)W(x)xi(y)h(x)h(y)
                                                  |v(x)-v(y)|^2 dxdy.

The independently verified retained-energy theorem gives the SINGLE bound

    E_hidden[a]=G_tail[a]-D_div[a] >= E_h/2+8*10^(-6)M.       (1)

See [the retained-half theorem](RETAINED_GAMMA.md)
and its cited complete hidden comparison. Every divisor conditional mean
and every mixed hidden Gamma edge is retained in (1).

Fix B>b. Define the source tail by the honest future integer lift

    f_B(x)=1_(x>B) sum_(n>=1)n^(-1/2)
                    xi(x+log n)[a(x+log n)-c_a].             (2)

For the actual/common-seed class, the series is the usual C lift. More
generally it converges in the source norms below whenever E_h+M is finite.
There is a finite constant C_B, depending only on B and the fixed theta
weights and cap, such that

    q_b[(f_B)_o]+integral_B^infinity V|f_B|^2
                  <= C_B(E_h+M) <= 125000 C_B E_hidden[a].  (3)

Here q_b is the original full-line odd logarithmic Gamma form, with the
normalization in Section 5 below. The proof gives constants from explicit
weight suprema, convergent Gaussian series and elementary kernel bounds;
it uses no unknown head eigenvalue or inverse. A numerical value of C_B is
not certified here. Constants may diverge as B decreases to b.

The source f_B is a genuine vector of the original P completion. In
particular, for every 0<=delta<=1,

    |Q_delta[f_B]|+N[f_B/psi]+P[f_B/psi]
                                        <= C'_B E_hidden[a], (4)

with all original terms present. The estimate for P follows from P=N+q,
not from an assertion that each signed source term is positive.

For an actual g, let a=(Mg)/xi on the safe ray. Then (2) is exactly

    f_B=1_(x>B)(g-c_a psi).                               (5)

The constant c_a is not generally the plateau value or the origin ratio.
The pole moment in (4) is therefore NOT set to zero.

## 2. Uniform weight facts away from the hidden endpoint

Set F=xi h and mu_h=m h^2. Then F^2/mu_h=q. On [B,infinity),

    0<c_B<=mu_h<=C_B<infinity,
    |(log mu_h)'|<=C_B almost everywhere,
    |(log q)'|+|(log F)'|<=C_B(1+z),
    F(y)<=C_B F(x) whenever y>=x>=B.                      (6)

These bounds include the integer knots of W and the cap boundaries in the
almost-everywhere/Lipschitz sense; no analytic regularity at a knot is used.
Here is a direct verification. The complete integer Riemann-sum estimates
in [the safe bulk proof](../20261014_safe_xi_hidden_comparison/BULK_TAIL.md) give

    W(x) asymptotic to I0 exp(x/2),
    |W'/W-1/2|<=20/23 for x>=3,
    |W/(I0 exp(x/2))-1|<=16 exp(-2x),

with I0>0. On the remaining compact interval away from b, W is positive
and locally Lipschitz. Consequently W/exp(x/2) is bounded above and below
and W'/W is bounded on [B,infinity). The cubic formula gives
|(log xi)'|<=C_B(1+z); xi is decreasing on this safe ray. Outside the cap,

    mu_h=(sqrt(m)+epsilon)^2,
    (log mu_h)'=[sqrt(m)/(sqrt(m)+epsilon)](log m)'.

The Gaussian decay of sqrt(m) pays the possible factor z in the last
expression. On the compact cap portion the assertion is immediate. The
bounds on log F and log q follow. Finally F=xi+epsilon sqrt(q) outside the
cap, while W(y)/W(x) is bounded below by c_B exp((y-x)/2), and xi decreases.
This proves the last bound of (6), including the compact capped portion.

For later label summation define

    R(A)=sup_(x>=A) q(x)[1+log(1+z(x))],  A>=B.             (7)

It is finite and tends to zero superexponentially. For example the n=2
term of W and the exact cubic give, for x>=2b,

    q(x)<=256 exp[-3 z(x)/4].                            (8)

Indeed W(x)>=psi(x-b)/sqrt2>=xi(x-b)/sqrt2, and
c(z)/c(z/4)<=128 once z/4>=4pi. The factors exp(x/2) supply the other
factor 2 in xi(x)/xi(x-b) after multiplication by sqrt2, giving the
displayed 256. The loose cubic bound 128 follows from c(z)<=8z^3 and
c(z/4)>=4(z/4)^3 in this range.
Thus R(A)<=C_B(1+A)exp[-c_B exp(2A)] for A sufficiently large.

A separate original-prime row estimate needed below is

    L_ref(x)<=C exp(x/2),
    sup_(x>=B) L_ref(x)/W(x)<infinity.                   (9)

No RH input is needed. Use the elementary Chebyshev bound
sum_(n<=X)Lambda(n)<=C_Lambda X. Split n>exp x into
2^j exp x<n<=2^(j+1)exp x. The contribution to exp(-x/2)L_ref(x) is at most

    2 C_Lambda 2^(j/2)
                    sup_(jb<=t<=(j+1)b)psi(t).

This is summable by the theta Gaussian envelope. The second part of (9)
follows from the W bounds above. This keeps all prime powers, rather than
replacing L_ref by a single row or by the rougher O((1+x)exp(x/2)) bound.

## 3. A weighted logarithmic Hardy estimate with a moving window

For A>=B put l_A=1/[2(1+z(A))]. The estimates (6) imply, with constants
independent of A, that on I_A=[A,A+l_A] the functions mu_h and q are
comparable to their values at A. Also kappa(t-s)>=c/(t-s) there. Therefore

    E_h >= c_B mu_h(A) integral_(A<s<t<A+l_A)
                                  |v(s)-v(t)|^2/(t-s) dsdt.       (10)

Indeed W(s)xi(t)h(s)h(t)=sqrt(mu_h(s)mu_h(t))sqrt(q(t)/q(s)).
The scale l_A makes all these ratios uniformly bounded.

For any L>0 and any measurable v of finite right side, Tonelli and
|v(s)|^2<=2|v(s)-v(t)|^2+2|v(t)|^2 give

    integral_0^(L/2)|v(s)|^2 log[L/(2s)]ds
       <=2 integral_(0<2s<t<L)|v(s)-v(t)|^2/t dsdt
                    +integral_0^L |v(t)|^2dt.                    (11)

Apply this after translation by A with L=l_A. On the rest of (A,infinity),
log_+(1/(x-A)) is at most log(2/l_A). Combining (10)-(11),
F^2=mu_h q, and the local comparisons proves

    integral_A^infinity F(x)^2|v(x)|^2
                    [1+log_+(1/(x-A))]dx
                              <= C_B R(A)(E_h+M).                (12)

For the near window, the extra log(2/l_A) is at most C[1+log(1+z(A))].
For the rest, monotonicity of z, not of q, gives
[1+log(1+z(A))]sup_(x>=A)q(x)<=R(A). Thus the same logarithm is
absorbed. For explicit bookkeeping one may enlarge R(A) everywhere to

    R_*(A)=[1+log(1+z(A))] sup_(x>=A)q(x)
                         +sup_(x>=A)q(x)[1+log(1+z(x))].         (13)

This explicit harmless enlargement avoids requiring q to be monotone.
Below use R_* in all estimates; it has the same Gaussian label summability.
There is no assumption of a source trace or a derivative at A.

## 4. The source product costs only a Gaussian-weighted hidden energy

For A<=u<w, expand

    F(w)v(w)-F(u)v(u)
        =F(w)[v(w)-v(u)]+[F(w)-F(u)]v(u).             (14)

The first square is bounded by the hidden kernel because

    F(w)^2/[W(u)xi(w)h(u)h(w)]
          =F(w)/[W(u)h(u)] <= C_B q(u)
                                  <= C_B sup_(x>=A)q(x).        (15)

For the second square, define the grouped finite row

    J_F(u)=integral_0^infinity kappa(t)|F(u+t)-F(u)|^2 dt.

The bounds (6) give

    J_F(u)<=C_B F(u)^2[1+log(1+z(u))].                         (16)

To check (16), split at t0=1/(1+z(u)). For t<t0, the log derivative bound,
z(u+t)<=exp(2)z(u), and F(u+t)<=C_BF(u) give
|F(u+t)-F(u)|<=C_B F(u)(1+z(u))t. Its square against kappa(t)<=C/t is
integrable with a uniform bound C_BF(u)^2. For t>=t0 use
|F(u+t)-F(u)|<=C_BF(u) and
integral_(t0)^infinity kappa(t)dt<=C[1+log(1+z(u))].
All differences remain grouped at t=0.

Equations (14)-(16) imply

    integral_(A<u<w)kappa(w-u)
                           |F(w)v(w)-F(u)v(u)|^2 dudw
                                      <=C_B R_*(A)(E_h+M).       (17)

This step uses the complete hidden edge energy, not only its diagonal or
its restriction to a compact head.

## 5. Every shifted label, its sharp cutoff, and the entire C lift

For d>=0 let A=B+d and define on the positive wing

    e_d(x)=1_(x>B)F(x+d)v(x+d).

The original odd Gamma normalization is exactly

    q_b[(e_d)_o]
      =2 integral_(0<x<y)kappa(y-x)|e_d(x)-e_d(y)|^2 dxdy
       +integral_(x,y>0)kappa(x+y)|e_d(x)+e_d(y)|^2 dxdy.          (18)

The internal same-wing term is bounded by (17). Its zero-extension cost
at B is bounded by (12), since

    integral_0^B kappa(y-x)dx
                        <= C_B[1+log_+(1/(y-B))], y>B.

The opposite-wing term in (18) is bounded by C_B||e_d||_2^2: whenever
e_d(x) is nonzero, x>B and integral_0^infinity kappa(x+y)dy<=C_B.
Thus

    q_b[(e_d)_o]+||e_d||_2^2
                                  <=C_B R_*(B+d)(E_h+M).        (19)

For the n-th term in (2), d=log n and the amplitude is n^(-1/2).
Minkowski in the Hilbert norm q_b+L2 therefore gives convergence and

    q_b[(f_B)_o]+||f_B||_2^2
       <= C_B [sum_(n>=1)n^(-1/2)sqrt(R_*(B+log n))]^2(E_h+M).  (20)

The series is finite by (8),(13). It is the complete all-integer sum;
there is no truncation of the common seed or separation across a zeta zero.

## 6. The complete original inverse-theta potential

Let r_+=(15+sqrt(105))/8 and r_-=(15-sqrt(105))/8, and set

    gamma_B=(1-r_+/z(B))(1-r_-/z(B))>0.

The exact cubic and the integer-row injection give, for x>=B and n>=1,

    xi(x+log n)/xi(x)
       <=gamma_B^(-1)n^(13/2)exp[-z(B)(n^2-1)],
    W(x+log n)>=n^(-1/2)W(x).                         (21)

For the second inequality, inject each label k>=2 of W(x) into the label
nk of W(x+log n). It remains valid across every threshold. Since
psi(x)>=xi(x)>0 on this ray, (9),(21) imply

    sup_(x>=B) n^(-1)V(x)q(x+log n)
                  <=C_B n^6 exp[-z(B)(n^2-1)].                  (22)

In detail, the left expression is
n^(-1)(L_ref(x)/psi(x))xi(x+log n)/W(x+log n), at most
n^(-1/2)(L_ref(x)/W(x))xi(x+log n)/xi(x).
This is where the complete reflected potential, rather than a physical
L2 surrogate, is paid. The n=1 bound is finite by (9).

Because |Fv|^2=mu_h q |v|^2, (22) and Minkowski in L2(V dx) yield

    integral V|f_B|^2
       <= C_B [sum_(n>=1)n^3 exp[-z(B)(n^2-1)/2]]^2 M.          (23)

Equations (20),(23) prove the first inequality (3). Combining their
constants and using (1) proves the second, without spending two separate
copies of the hidden energy.

## 7. Original P completion, all reflected terms, and the pole

The complete normalized prime operators are bounded in the variable
sqrt(V)f. Explicitly, write mu=V^(-1/2). Their norms are bounded by
sup_x mu(x)mu(x+log n) and sup_(0<x<log n)mu(x)mu(log n-x).
The complete alpha-weighted sums of these bounds converge by the theta
envelope, as proved in the
[source-tail foundation](../20261013_supercritical_source_tails/REPORT.md).
Also mu is bounded and sinh(x/2)mu(x) belongs to L2. Consequently all
ordinary mass, prime and pole terms below are bounded by C integral V|f|^2.

On the source core the exact unchanged formula is

    Q_delta[f]
      =q_b[f_o]-2C0 integral|f|^2+2delta integral V|f|^2
       -4 sum_n alpha_n Re integral_0^infinity conjugate(f(x))f(x+log n)dx
       +2(1-delta)sum_n alpha_n Re integral_0^(log n)
                                      conjugate(f(x))f(log n-x)dx
       -8|integral_0^infinity sinh(x/2)f(x)dx|^2.                (24)

Thus |Q_delta[f]|<=q_b[f_o]+C integral V|f|^2 uniformly for 0<=delta<=1.
Moreover N[f/psi]<=4 integral V|f|^2, and P=N+Q_0.

For completeness these are genuine completion identities for (2), not
merely formulas on a maximal source space. For any source supported in
[B,infinity) with finite q_b+L2(V), first use odd amplitude truncation.
Its residual converges by the normal-contraction jump-form argument and
weighted dominated convergence. A bounded source can then be cut off at
infinity and in an increasingly small collar of B; the additional boundary
cost is paid by its already finite logarithmic jump form, or by (11) on a
fixed interior collar. For a bounded source the shrinking collar cost is
O(eta log(1/eta)) plus its removed energy. Smooth approximation on compact
subintervals of (0,infinity) then converges in q_b+L2(V), since V is bounded
on those compact sets. All ratios of these smooth compact sources by psi
are in the original ratio core. The bounded complete prime and pole terms
and N<=4 integral V|f|^2 make their P differences tend to zero through
P=N+Q_0. The source is therefore an original P vector, and (24) passes
unchanged. This proves (4).

The construction is linear in the centered latent a-c_a, but the choice
c_a is the single projection already present in (1). For an actual source
(5), a different constant gauge must be inserted explicitly before using
pole centering or the actual two origin moments. No such change has been
made here. The positive bound (1) has not been added to another independent
copy, no reflected wall term has been omitted, and no sign is assigned to
Q_0 or to the dynamic remainder E_hidden leaves behind.
