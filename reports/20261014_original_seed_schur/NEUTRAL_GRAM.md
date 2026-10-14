# Exact original-head elimination by increasing neutral-tail Gram matrices

Let b=log 2. Use the COMPLETE original source form q0, with its Gamma
multiplier, both prime orientations, and full pole. The un-repaired head
[theorem](../20261014_unrepaired_original_head/REPORT.md) gives

    q0[h] >= gamma_H ||h||_2^2, gamma_H=10^(-10),

on the closed restricted odd Gamma source domain D0 in H=(0,b). Let A0
be its positive selfadjoint realization. This is a SOURCE domain, not an
assertion that every member belongs to the separate original P/N domain.

This note replaces the complete infinite head inverse by an increasing
sequence of explicit genuine theta-neutral Gram penalties. It does not
prove a sign for the remaining tail form.

## 1. Centered theta jets are dense in the head FORM domain

Put psi=-Phi' and choose

    s_j=(partial_x^2)^j (psi''-psi/4), j=0,1,2,... .       (1)

These are the genuine centered theta jets, not arbitrary local repairs.
Every s_j has finite original P and N energies, zero pole moment, and
q0(s_j,z)=0 on the original core. The exact smooth source equation extends
this mixed null identity to the theta-decaying SOURCE class used below.
Each s_j is odd, holomorphic on |Im x|<pi/4, and has double-exponential
real tails. Its Fourier transform has the form

    hat s_0(t)=constant * it(t^2+1/4)Xi(t),               (2)

with a nonzero constant depending only on the Fourier convention. In
particular it is nonzero on some open real interval. No zero-location
assumption is used.

The restrictions of the s_j span a dense subspace of the Frechet space of
smooth odd functions on [-b,b]. To prove this including the endpoints,
let a continuous functional annihilate all restrictions. Extend it to the
space of smooth functions on [-b,b] and then to an odd compactly supported
distribution nu on R, supported in [-b,b]. Its restriction to odd tests is
the original functional. Define

    H(z)=<nu(x),s_0(x+z)>, |Im z|<pi/4.

Compact support and theta holomorphy make H holomorphic. Both nu and s_0
are odd, so H is even. Its even derivatives at zero vanish by the assumed
annihilation of (1); its odd derivatives vanish by parity. Therefore H=0.
On the real line Fourier transformation yields the product of hat s_0 and
the Fourier transform of the reflected compact distribution. The latter
is entire. Equation (2), the identity theorem, and distributional Fourier
uniqueness imply nu=0. Hahn--Banach proves the stated density. In
particular this argument does not require division by psi at the origin.

This smooth density implies density in D0, not just in L2. Indeed the
finite sine spans are a form core by definition. Approximate any such sine
combination on [-b,b] by a finite combination of (1) in C^1. If the C^1
error is epsilon, its zero-supported odd extension has L2 norm O(epsilon)
and total variation O(epsilon), including the two endpoint jumps. Its
Fourier transform is consequently bounded by

    C epsilon min(1,1/|t|).

Since the Gamma symbol grows only logarithmically, its Gamma form tends
to zero. The complete remaining head terms are bounded L2 forms. This
proves convergence in the positive q0 head norm and hence

    closure_span^{q0,H}{s_j,H:j>=0}=D0.                (3)

Every finite set of these restrictions is linearly independent: a vanishing
combination on H vanishes on the theta holomorphic strip; its Fourier
transform is a polynomial in t^2 times (2), so the polynomial is zero.
Thus each finite head Gram below is positive definite.

## 2. Exact neutral-tail Gram equality

Let T=(b,infinity). The admissible tail class consists of tails with finite
restricted odd Gamma source energy and sufficient theta decay for all
complete mixed rows and pole pairings. It includes actual fixed-depth
source tails and every finite theta-jet tail. Let B0 t in L2(H) be the
complete tail-to-head density from
[the original mixed source kernel](../20261014_unrepaired_original_head/MIXED_FORCING.md),
with delta=0. Explicitly it retains the Gamma difference kernel, every
forward and reflected prime crossing, and the full pole.

The positive source head gives

    u_t=-A0^(-1)B0 t,
    S0[t]=q0[t]-<B0 t,A0^(-1)B0 t>.                    (4)

Only this source-domain inverse is used. No separate P/N membership for
u_t is asserted. For m>=1 put

    G^(m)_ij=q0(s_i,H,s_j,H), 0<=i,j<m,
    p^(m)_i=q0(s_i,T,t).                              (5)

The full mixed neutral identities give exactly

    G^(m)_ij=q0(s_i,T,s_j,T),
    p^(m)_i=-<s_i,H,B0 t>=q0(s_i,H,u_t).               (6)

All q0 entries in (5)-(6) have their original signs. There is no replacement
by the hidden positive energy and no assumption about positivity of q0
on arbitrary tail sources.

Set

    c_m=(G^(m))^(-1)p^(m),
    s^(m)=sum_(j<m)(c_m)_j s_j,
    k_m=(p^(m))^* (G^(m))^(-1)p^(m).                  (7)

In the complex case the usual conjugate-linear first-slot conventions
are understood. By (6), s^(m)_H is precisely the q0-orthogonal projection
of u_t onto the first m neutral heads. Hence (3) proves

    k_m increases to <B0 t,A0^(-1)B0 t>,
    q0[u_t-s^(m)_H] decreases to 0.                    (8)

The complete, MONOTONE neutral-tail Schur completion is therefore

    q0[t-s^(m)_T]=q0[t]-k_m decreases to S0[t],
    q0[t-s^(m)_T]-S0[t]=q0[u_t-s^(m)_H]>=0,            (9)

and equivalently

    S0[t]=inf_{s finite centered neutral combination} q0[t-s_T]. (10)

Thus the genuine theta-tail Gram, without auxiliary load penalties,
recovers the entire original head subtraction. Each finite stage is a
finite exact variational problem, but a favorable finite stage is only an
UPPER bound for S0. A lower certificate must control the remaining positive
quantity in (9); it may not declare convergence from numerics alone.

## 3. A rigorous a posteriori enclosure

Every s^(m)_H lies in the head OPERATOR domain. Indeed its mixed neutral
identity gives A0 s_j,H=-B0 s_j,T in L2(H), first on the form core and then
by continuity. Define the complete residual

    r_m=-B0 t-A0 s^(m)_H=-B0(t-s^(m)_T).                (11)

It is an ordinary L2 head density, with every Gamma, prime, and pole term
retained. Since u_t-s^(m)_H=A0^(-1)r_m, (9) yields

    0<=q0[t-s^(m)_T]-S0[t]
       =<r_m,A0^(-1)r_m>
       <=10^(10)||r_m||_2^2.                          (12)

Consequently q0[t-s^(m)_T]-10^(10)||r_m||_2^2 is a certified lower
bound for S0[t], while q0[t-s^(m)_T] is the upper bound. Formula (8) does
NOT assert that ||r_m||_2 tends to zero: form-density alone does not imply
operator-graph convergence. A quantitative use of (12) must separately
certify its actual residual. The exact complete mixed-row formula makes
that residual observable; it is not an unknown projection error.

## 3b. An operator core gives a different, convergent two-sided scheme

There is a stronger density fact, but it does not turn the Ritz sequence
(7) into an operator-graph convergent sequence. Instead it permits a
separate least-squares construction with a guaranteed vanishing residual.

The finite sine spans are an OPERATOR core for A0. To see this from the
already proved exact head matrix, its archimedean part is the diagonal
2a(omega_j) minus a bounded matrix E: the bound

    |E_ij|<=1/(i+j)+4b/(pi^2 i j)

gives a bounded Hilbert-kernel operator plus a bounded rank-one operator.
Both compressed reflections and the pole are also bounded on L2. Hence
A0 is a logarithmic diagonal operator plus a bounded selfadjoint remainder.
Its operator domain is the corresponding weighted sequence space, and
finite sequences are a graph core.

The C1 approximation in Section1 also converges in this OPERATOR graph.
Indeed the same Fourier estimate now gives

    integral_R log^2(2+|t|)|hat w(t)|^2dt<=C epsilon^2.

The full odd archimedean multiplier applied to the zero extension is thus
L2-small. Restriction to H and the bounded reflection/pole terms show
||A0 w_H||_2<=C epsilon. These smooth restricted sources belong to the
operator domain, either by this direct multiplier argument or by their
L2 represented form functional. Approximating each finite sine vector
proves

    closure_span^{graph(A0)}{s_j,H:j>=0}=Dom(A0).       (16)

Because A0 is onto L2(H), (16) implies that the vectors A0 s_j,H span a
dense subspace of L2(H). Now define a SECOND finite Gram system

    K^(m)_ij=<B0 s_i,T,B0 s_j,T>,
    d^(m)_i=<B0 s_i,T,B0 t>,
    z_m=(K^(m))^(-1)d^(m),
    sigma^(m)=sum_(j<m)(z_m)_j s_j.                   (17)

Every K^(m) is positive definite, since A0 is injective and the neutral
heads are independent. These are the COMPLETE mixed densities, not merely
their Gamma parts or endpoint asymptotics. Formula (17) minimizes the L2
residual in (11). Therefore

    R_m=B0(t-sigma^(m)_T),
    ||R_m||_2^2=||B0 t||_2^2-(d^(m))* (K^(m))^(-1)d^(m)
                         decreases to zero.          (18)

Numerically the grouped residual square can be evaluated directly to avoid
cancellation; the exact identity (18) is not a license to round a small
negative result up to zero. Applying (12) to this new finite shift gives

    U_m=q0[t-sigma^(m)_T], epsilon_m=10^(10)||R_m||_2^2,
    U_m-epsilon_m <= S0[t] <= U_m,
    epsilon_m ->0, U_m -> S0[t].                     (19)

The upper bounds U_m in this second construction need not be monotone;
the monotone sequence is (9). If desired, cumulative maxima of the lower
bounds and cumulative minima of the upper bounds in (19) give nested
certified intervals with the same common limit. Thus the full source head
inverse can be enclosed to arbitrary accuracy using ONLY finite genuine
neutral-tail Grams and their complete residuals. There is no unknown
Galerkin tail assumption. The convergence is qualitative until the actual
finite residual has been bounded; (19) supplies the rigorous stopping
criterion for any such certified computation.

The coefficient vectors in (7) and (17) are generally different. Neither
is the hidden-energy orthogonal projection. No hidden norm or actual
stationary equation is transferred to their finite remainders for free.

## 4. Consequence for an actual source and the unspent hidden remainder

For an actual pole-centered top source g at depth delta>0, the exact
original-source head identity in
[the Schur neutral quotient](SOURCE_SCHUR.md)
gives, with t=g_T and n_g=2(Vg-F_r g) on H,

    S0[g_T]=-delta N[g/psi]
             -delta^2<n_g,A0^(-1)n_g>.                 (13)

For a nonzero actual source the right side is strictly negative. Thus some
FINITE m in (9) already gives a genuinely legal original-P tail source

    t_m=g_T-s^(m)_T, supported in [b,infinity),
    q0[t_m]<0.                                        (14)

Legality follows directly from its finite Gamma energy, theta tail, and
support away from the physical origin. It does not require u_t to be an
original-P vector. Each t_m is a lawful tail test, NOT an actual stationary
source, and no actual amplitude or transmission estimate is imported to it.

The safe common seed of t_m is exactly the original future Mobius seed
minus the same finite neutral seed on y>=b. If E_hidden denotes the proved
G_tail-D_div form, then its change is the complete identity

    E_hidden[t_m]=E_hidden[t]-2 Re E_hidden(t,s^(m)_T)
                                      +E_hidden[s^(m)_T].      (15)

No boundedness, monotonicity, or convergence of (15) follows from (8).
In particular this is not the hidden-orthogonal projection, and it must
not be combined with that different normalization for free. The original
remainder R0=S0-E_hidden changes by the exact opposite amount under the
same full neutral shift, because S0 is unchanged. Infinite neutral
cancellation and the full signed tail problem therefore remain.

The constructive gain is the exact increasing theta Gram realization of
the whole original head inverse, together with a convergent two-sided complete-residual
enclosure using the separate operator-core least-squares sequence. Neither (9), (12), nor (14) proves nonnegativity of the
full tail Schur form or excludes a supercritical source.
