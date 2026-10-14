# Raw finite-translation covariance for an actual top Green source

2026-10-14 UTC. All objects below are the complete original forms. Inputs
are the [complete smooth-convolution variation](../20261013_full_prime_green_reference/ODD_VARIATION_PRIME_BOUNDARY.md),
[fractional origin theorem](../20261013_supercritical_source_tails/FRACTIONAL_ORIGIN_BOUNDARY.md),
[actual source-tail theorem](../20261013_supercritical_source_tails/REPORT.md),
[complete row asymptotic](../20261013_reflected_markov_essential_edges/REPORT.md),
and [original physical closed-form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md).
No prime label is removed.

The new point is that smooth convolution profiles can be replaced by raw
cosine translations for almost every sufficiently small translation
parameter. This is an actual form-domain statement, not an assertion of
point traces or differentiability. It gives finite signed translation
matrices and a uniform line-boundary formula. It does not settle their
required sign or exclude the hypothetical eigen-source.

## 1. Setup and statement

Let g be a real, odd, pole-centered source for the largest supercritical
Green eigenvalue lambda>1. On the positive wing, g=psi r, psi=-Phi'>0,

    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    L(x)=sum_(d_n>x) alpha_n psi(d_n-x),
    V=L/psi, mu^2=1/V, P0=P[r], delta=1-1/lambda.

Every prime power is retained. In source notation,

    N(f,h)=2 integral V f h
           -2 sum_n alpha_n integral_0^(d_n) f(x)h(d_n-x) dx,
    Q_delta=P-(1-delta)N >=0,
    h=P-N, h(g,z)=-delta N(g,z).                       (1)

The odd extension is denoted g_o. For a real parameter a, define

    (T_a g)_o(x)=(g_o(x+a)+g_o(x-a))/2.                 (2)

There is R>0, independent of the actual source and its depth, and a
symmetric conull measurable set E in (-R,R), containing zero, such that:

1. T_a g/psi belongs to the actual pole-centered P-completion for a in E.
   The map a -> T_a g/psi belongs to L2((-R,R);P).

2. For each finite m, for almost every tuple (a_1,...,a_m) in
   (-R/2,R/2)^m, the matrix

   K_ij=N(T_(a_i)g,T_(a_j)g)
        -1/2 N(g,[T_(a_i+a_j)+T_(a_i-a_j)]g)            (3)

   is positive semidefinite. Its exact normalization is

   delta K_ij=Q_delta(T_(a_i)g,T_(a_j)g).               (4)

   The entries with a_i=0 are zero whenever the other entries are legal.
   Predetermined arithmetic spacings are not licensed by this almost-
   everywhere assertion; fixed arithmetic masks must retain smoothing
   unless their pointwise domain is proved separately.

3. For almost every 0<a<R/2, put

   D_V(a)=integral V (T_a g)^2
          -1/2 integral V g(g+T_(2a)g),
   F(t)=sum_n alpha_n[g(d_n+t)+g(d_n-t)],              (5)

   with F extended evenly near zero. Then

   Q_delta[T_a g]=2 delta [D_V(a)-D_pr(a)] >=0,        (6)

   D_pr(a)=1/2 integral_0^a {
       T_a g(x) F(a-x)
       -1/2 [F(2a-x)+F(x)] g(x)} dx.                 (7)

   All V pairings in (5) are legal weighted pairings. For every fixed
   0<s<1/16, shrinking R if necessary,

   delta |D_pr(a)| <= C_s a^(1+2s) P0.                (8)

The constant in (8) is uniform in a, g, and delta. Unlike a passage to
concentrating smooth profiles in the previous theorem, it contains no
profile derivative or concentration constant.

## 2. Averaged control of the singular endpoint

The source theorem gives g_o in H^s(R) for every s<1/16. For any odd
f in H^s(R), 0<s<1, and a,x>0,

    T_a f(x)=[f(a+x)-f(a-x)]/2.

Consequently, for every fixed epsilon>0 and R>0,

    integral_0^R da integral_0^epsilon |T_a f(x)|^2 dx/x
    <= (1/4) integral_0^epsilon ||tau_x f-tau_(-x)f||_2^2 dx/x
    <= C_s epsilon^(2s) ||f||_(H^s)^2.                (9)

The first inequality extends the a integration to the full line. The
second uses |exp(i xi x)-exp(-i xi x)|<=C_s|xi x|^s
and then integrates x^(2s-1). Thus no point value of f or f' is used.
In particular (9) supplies the missing normalized origin norm for almost
every raw translation, since V(x) is comparable to 1/x there.

## 3. Uniform far-wing integrability of raw translations

The published actual-source estimate is

    integral_X^infinity |g/mu|^2
        <= C_delta P0 exp(9X-pi exp(2X)).                 (10)

The theta and row estimates give, in the far wing,

    log(mu(x)^2)=-pi exp(2x)+O(x),
    log(m(x)^2) =-pi exp(2x)+O(x).                    (11)

Hence, for |b|<=R and large y, either quotient

    mu(y)^2/mu(y-b)^2,  mu(y)^2/m(y-b)^2

is at most

    C_R exp(C_R y+pi[exp(2R)-1]exp(2y)).              (12)

Choose R with exp(2R)-1<1/2. Stieltjes integration of (10) against
(12), or integration by parts of its increasing envelope, proves

    sup_(|b|<=R) integral_X^infinity |g_o(x+b)|^2
                      [V(x)+m(x)^(-2)] dx
         <= C_(delta,R) P0 exp(C_R X-c_R exp(2X)),        (13)

for large X and some c_R>0. Changing X by a fixed R only changes the
constants. For the lower bound in (11) one uses positivity/continuity on
compact intervals and the complete PNT row asymptotic in the far wing;
no lower bound on an individual prime contribution is substituted.

Jensen's inequality makes (13) valid as well for averages of translated
g_o against any probability measure supported in [-R,R]. Thus it applies
uniformly to raw T_a g and to their smooth mollifications. The estimate
is used only for a fixed actual delta, to prove domain membership; no
uniform-in-depth claim about these full norms is made.

## 4. Closure in the actual P-completion

Take a nonnegative even smooth mass-one mollifier rho_epsilon and put

    f_(a,epsilon)=T_a(rho_epsilon*g_o), restricted to x>0.

Choose a in a smaller fixed interval and epsilon small enough that all
kernels involved stay within the original legal convolution radius and
within the radius of (13). Each f_(a,epsilon)/psi is already a legal
pole-centered P vector by the inherited smooth-convolution theorem.
The pole moment is multiplied by cosh(a/2) and by the mollifier's
cosh moment, so remains exactly zero.

Let epsilon and eta tend to zero. Equation (9), applied to
(rho_epsilon-rho_eta)*g_o, proves that f_(a,epsilon)-f_(a,eta) tends to
zero in averaged L2(V dx) at the origin. On compact intervals away from
zero the same assertion follows from ordinary L2 translation continuity.
The uniform tail estimate (13) handles the omitted far wing. The identical
argument, without the singular endpoint step, gives averaged convergence
in physical L2(dx/m^2).

Moreover T_a is a contraction for the full Gamma Fourier norm, so

    integral da q_b[(f_(a,epsilon)-f_(a,eta))_o]
      <= length(interval) q_b[(rho_epsilon-rho_eta)*g_o] ->0. (14)

On legal centered sources the complete reflected bound and physical prime
bound imply

    N[f] <= C ||f/mu||_2^2,
    |h[f]| <= q_b[f_o]+C ||f_o/m||_2^2,               (15)

with a harmless change of a fixed constant for half-line normalization.
The complete prime correlations in the second estimate are absolutely
summable; it is not a prime truncation. Since P=N+h on these vectors,
(9), (13)--(15) show that f_(a,epsilon)/psi is Cauchy in the Bochner
space L2(da;P).

Take the Bochner limit and an almost-everywhere convergent subsequence.
The centered P source map is injective and continuous: its pole square
controls integral [sinh(x/2)/psi(x)]|f(x)|^2 dx, whose coefficient has a
strictly positive global minimum. The ordinary source limit is T_a g.
Thus the Bochner limit has exactly that source, proving assertion 1.
Symmetrize the full-measure set and adjoin a=0, which was already legal.

## 5. All finite signed translation matrices

The elementary identity

    T_a T_b=[T_(a+b)+T_(a-b)]/2                       (16)

holds on odd full-line sources. For a finite tuple, all its a_i and
nonzero a_i+/-a_j belong to E for almost every choice of that tuple:
each bad set is the inverse image of a one-dimensional null set under a
nonconstant linear map. The identically zero differences are legal by
construction. Diagonal sums 2a_i are covered in the same way.

The Gamma multiplier, scalar mass, and each complete prime shift commute
with the real selfadjoint T_a. All resulting full prime sums are absolutely
convergent by the physical membership just proved. The centered pole term
vanishes. Thus

    h(T_a g,T_b g)=h(g,T_a T_b g).

Use (1) on the right and (16) to obtain (4). Positivity of Q_delta gives
(3), including every mixed entry. In particular every finite signed mask
sum_i c_i T_(a_i) is a legal test for almost every tuple of its nodes.
This statement is stronger than saying a smoothed profile can be made
arbitrarily narrow with uncontrolled profile-dependent constants.

## 6. The complete reflected line boundary

For one label d>4a let R_d f=1_(0,d)f(d-x). A direct calculation with odd
extensions gives

    [R_d,T_a]g(x)=1/2[g(d+a-x)+g(d-a+x)], 0<x<a,

and, on the opposite corner x=d+t, |t|<a,

    [R_d,T_a]g(d+t)=-1/2 g(a-|t|).

It vanishes elsewhere, apart from null endpoints. Pairing against T_a g
and changing variables t=+/- (a-x) in the two opposite-corner pieces gives

    <T_a g,[R_d,T_a]g>
     =1/2 integral_0^a {T_a g(x)[g(d+a-x)+g(d-a+x)]
          -[T_a g(d+a-x)+T_a g(d-a+x)]g(x)} dx.       (17)

The coefficient 1/2 comes from T_a; the two corners introduce no additional
factor. The complete local prime load converges absolutely in H^s and
hence in L2 by the fractional origin theorem. Its even extension satisfies

    F_(T_a g)(t)=[F(t+a)+F(t-a)]/2, 0<t<a.            (18)

Summing (17) over every actual prime-power label yields (7). This passage
can also be checked first at finite label sets and then in local L2.
The global reflected pairings converge absolutely by the diagonal
reference bound on the legal vectors. These are the same complete limits.

Finally ordinary L2 translation and odd/even reflection give

    ||T_a g||_(0,a) <= 2^(-1/2)||g||_(0,2a),
    ||F_(T_a g)||_(0,a) <= 2^(-1/2)||F||_(0,2a).

Therefore

    |D_pr(a)| <= 2^(-1/2) ||g||_(0,2a)||F||_(0,2a).   (19)

The established fractional estimates are

    ||g||_(0,2a)<=C_s delta^(-1) a^(1+s) sqrt(P0),
    ||F||_(0,2a)<=C_s a^s sqrt(P0).

Substitution proves (8), while the covariance identity proves (6).
No trace or Taylor expansion of the unsmoothed actual source has been
introduced.

## 7. Precise remaining issue

The result exposes the full nonlocal constraint as almost-everywhere
finite signed translation matrices, not merely smooth test profiles.
Nevertheless it only gives

    delta D_V(a) >= -C_s a^(1+2s)P0

for the single-node mask. The mixed matrices retain more information,
but a negative test for the actual source has not been constructed.
The full potential term and every reflected boundary term remain present.
