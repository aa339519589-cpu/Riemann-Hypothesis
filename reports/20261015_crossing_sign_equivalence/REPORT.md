# The complete crossing sign is equivalent to original positivity without a head inverse

Fix any finite c>0. Nonnegativity of the complete original odd source form
is equivalent to a crossing-sign assertion on an explicit finite class of
self-Fourier Euler sources which vanish on (0,c) and have both exponential
moments zero. No positive head certificate, head inverse, or quantitative
trace inequality is needed for this equivalence.

This is an existence transfer, not a proof of either sign. It does not
preserve an actual eigen-equation, bounded ground ratio, current, or
controlled hidden norm. Separate original P and N energies of the new
representatives need not be finite.

## 1. Complete source conventions and the precise statement

Use the [original source form](../20261012_localized_odd_schur/SOURCE_FORM.md)
and its linked original-form foundation. All fields in this report are real.
For a positive-half-line source f, let f_o be its odd extension, and use
hat f_o(t)=integral_R f_o(x)exp(itx)dx. Set

    kappa(x)=exp(-x/2)/(1-exp(-2x)), x>0,
    alpha_n=Lambda(n)/sqrt(n),
    a(t)=Re digamma(1/4+it/2)-log pi,
    C0=gamma+pi/2+3log2+log pi, b(t)=a(t)+C0>=0.

The complete half-line source form, written using its full odd extension,
is

    q0[f]=(1/(2pi)) integral_R a(t)|hat f_o(t)|^2dt
       -2 sum_(n>=2) alpha_n integral_R f_o(x)f_o(x+log n)dx
       -2 [integral_R sinh(x/2)f_o(x)dx]^2.                 (1)

Its polarized version is denoted q0(f,z). In particular its half-line
pole is -8 ell(f)ell(z), where ell(f)=integral_0^infinity sinh(x/2)f(x)dx.
Write T_odd for a(D) minus both complete prime shifts on odd extensions.
The half-line density convention is

    q0(f,z)=<f,Q0 z>, Q0 z=2T_odd z-8 sinh(x/2)ell(z).      (2)

There is no global unweighted self-adjoint realization of T asserted here.
A sufficient common source graph for this proof has norm

    ||f||_src^2=integral_R (1+b(t))|hat f_o(t)|^2dt
                                      +integral_0^infinity exp(2x)|f(x)|^2dx.

The form (1) is continuous on this graph. For example, each positive-wing
future correlation and each reflected correlation is bounded by
n^(-1)||exp(x)f||_2||exp(x)z||_2. Multiplication by alpha_n is summable
because sum Lambda(n)n^(-3/2)<infinity. The pole is bounded by the same
weighted norm. Smooth compact odd sources are dense in this graph, by
symmetric smooth cutoffs followed by mollification. The logarithmic Gamma
part is handled by its full Fourier multiplier; cutoff commutators have
bounded rows, while the weighted mass pays the tails. All sources actually
constructed below have either rapid logarithmic tails or theta tails and
at most a bounded jump at the fixed head endpoint. Thus they also admit
the explicit cutoff approximations described in Section 3.

Let F denote the physical Fourier transform with phase exp(-2pi iuv), and
put

    U h(x)=exp(x/2)h(exp x),
    C_phys h(u)=sum_(n>=1)h(nu),
    C_log f(x)=sum_(n>=1)n^(-1/2)f(x+log n).

Thus C_log U=U C_phys. Define, on positive logarithmic wings,

    U_f=integral_0^infinity exp(x/2)f(x)dx,
    V_f=integral_0^infinity exp(-x/2)f(x)dx,
    C_cross=H_kappa+F_r,
    H_kappa f(x)=integral_0^infinity kappa(x+y)f(y)dy,
    F_r f(x)=sum_(n>exp x)alpha_n f(log n-x),
    B_cross=C_cross-exp(x/2) tensor exp(x/2)
                         -exp(-x/2) tensor exp(-x/2).      (3)

Every prime power and every Gamma Hankel mode is included. The notation
C_cross means the raw crossing; B_cross includes both pole ranks.

**Theorem.** For each fixed c>0 the following are equivalent:

1. q0[f]>=0 for every smooth compact odd source f.
2. <E,C_cross E>>=0 for every source E=C_log U h with
   h=(d+F d)/2, where d is real even compact smooth, d(0)=integral_R d=0,
   and where E=0 on (0,c), U_E=V_E=0.

It suffices in item 2 to use the finite representatives explicitly
constructed in Sections 3-5. The theorem does not claim that C_cross is
positive on arbitrary fields with two vanishing moments. Its sign on
this constrained finite class remains unproved.

## 2. The selfdual and anti-selfdual source identities

For every even self-Fourier Schwartz h with h(0)=integral_R h=0, the
complete [even-null and odd-boundary identity](../20261015_old_actual_physical_range/REPORT.md)
(Section 6, “Complete even-null identity and the boundary normalization”)
gives

    Q0(C_log U h)=4B_cross(C_log U h).                      (4)

This identity does not require a physical gap. For completeness, its
anti-selfdual counterpart needed here follows by the same full contour,
with a different parity and pole coefficient, as follows.

Let w be even Schwartz, Fw=-w, and w(0)=integral_R w=0. Put
N(x)=exp(x/2)C_phys w(exp x) on the whole log line. Poisson summation gives
N(-x)=-N(x), and N decays faster than every exponential at both log ends.
For M_w(s)=integral_0^infinity w(u)u^(s-1)du,

    Nhat(s)=integral_R N(x)exp[(s-1/2)x]dx=zeta(s)M_w(s).

M_w is holomorphic on Re s>-2 and rapidly decreasing on closed vertical
strips there; Nhat is entire. M_w(1)=0 cancels the zeta pole. Initially on
1<Re s<3/2, the full future-prime transform is -zeta'(s)M_w(s). Moving
the inverse contour to Re s=1/2 contributes the residue
Nhat(1)exp(-x/2). Odd parity makes the past contribution have the
opposite exponential term. The zeta functional equation therefore gives

    T_odd N=2Nhat(1)sinh(x/2),
    Nhat(1)=U_N-V_N=2ell(N).

Polynomial zeta bounds and rapid M_w decay justify the horizontal limits;
the product -zeta'M_w has no poles at nontrivial zeros. In the convention
(2), both complete pole rows cancel exactly:

    Q0 N=0.                                                (5)

The identities first hold against compact source tests. Continuity in
the source graph extends them to all the pairings used below. In
particular (5) is genuine full-source neutrality, not cancellation of
only a finite arithmetic or archimedean row.

## 3. Move a negative direction entirely past any fixed head

Suppose item 1 of the theorem fails, and choose ONE smooth compact odd
source f with q0[f]<0. The centered theta jets

    s_j=(partial_x^2)^j(psi''-psi/4), j=0,1,2,...,

are genuine q0-neutral sources with theta tails. Their restrictions are
dense in the smooth odd functions on every fixed interval [-c,c]. The
[endpoint-inclusive density proof](../20261014_original_seed_schur/NEUTRAL_GRAM.md)
(Section 1) is independent of its displayed endpoint log 2: an odd compact
distribution supported in [-c,c] which annihilates these jets gives a
holomorphic even convolution with s_0 whose derivatives all vanish.
The Fourier transform of s_0 is nonzero on some open interval, while the
transform of the compact distribution is entire. Analytic uniqueness
then makes the distribution zero. This proves the same Frechet density
for arbitrary fixed c, without using any head-form positivity.

Choose finite neutral combinations N_j with

    ||f-N_j||_(C1([-c,c]))=epsilon_j ->0,
    h_j=1_(0,c)(f-N_j), t_j=f-N_j-h_j.

The odd extension of h_j has L2 norm and total variation O(epsilon_j),
including the jumps at the two endpoints. Hence

    |hat h_j(t)|<=C epsilon_j min(1,1/|t|).

Its complete logarithmic Gamma form tends to zero. Head prime labels
are finite at this fixed c, and the head pole is a bounded L2 form, so
q0[h_j]->0. Also q0(f,h_j)->0: use Gamma form Cauchy, the finite set of
prime shifts meeting the TWO fixed compact supports, and the head pole.
The first slot in this limit is the fixed f, never the growing N_j.
Exact neutrality consequently gives

    q0[t_j]=q0[f]-2q0(f,h_j)+q0[h_j] ->q0[f]<0.              (6)

Fix one sufficiently large j. The source t_j is smooth beyond c, with a
possible bounded jump at c and a theta tail. A collar cutoff of width
epsilon has logarithmic Gamma error O(epsilon |log epsilon|); its weighted
L2 error tends to zero. Far cutoffs are paid by the fixed theta tail, and
mollification stays within (c,infinity). Thus a single

    tau in C_c^infinity((c,infinity)), q0[tau]<0             (7)

can be chosen. No positive head gap, inverse, or resolvent entered this
argument. There is no uniform bound as c or the neutral approximation
varies.

## 4. A single finite Mobius mask gives an exact selfdual representative

Put p(u)=u^(-1/2)tau(log u), extended evenly. Its positive support is inside
(exp(c),R) for a finite R. Choose ONE integer M>=exp(c)R and one even smooth
anchor k, supported away from zero inside |u|<exp(-c), with integral_R k=1.
Set

    a(u)=sum_(n<=M)mu(n)p(nu), m=integral_R a,
    d=a-mk, h=(d+F d)/2, E=C_log U h.                       (8)

Here d is compact smooth, is zero near zero, and has mean zero. Therefore
h is self-Fourier Schwartz with trace and mean zero. No infinite Mobius
limit is used.

For every u>1 the complete finite divisor identity is

    C_phys a(u)=p(u).

Indeed all contributing products jn satisfy jn<R/u<R<=M, so each of their
divisors lies in the finite mask. On 1<u<exp(c) the reciprocal identity
also gives C_phys a(1/u)=p(1/u)=0, because every contributing product is
below uR<=exp(c)R<=M. The support of k makes both C_phys k(u) and
C_phys k(1/u) vanish on this interval. Poisson summation for d gives

    C_phys(Fd)(u)=u^(-1)C_phys d(1/u).

Thus E vanishes on (0,c) exactly. On the entire positive source wing,
C_log U d=tau, since C_phys k(u)=0 for u>1. With w=(d-Fd)/2, equation (5)
therefore proves

    Q0(E-tau)=0, q0[E]=q0[tau]<0.                          (9)

This is equality of complete source forms. It is not weighted convergence
of a family of representatives and not a change of an actual eigenstate.

## 5. An exact two-moment kernel normalization

Take any even compact smooth d_0, supported away from zero inside
|u|<exp(-c), with integral_R d_0=0. Define

    h_0=d_0+F d_0, w_0=Fd_0-d_0, N_0=C_log U h_0.

Because C_phys d_0(u)=0 for u>1, N_0=C_log U w_0 on the complete positive
wing. Equations (4)-(5) give Q0N_0=0 and B_cross N_0=0. Its head also
vanishes by reciprocal Poisson and the stated support.

The moments are ordinary convergent source integrals. Write
M_d0(s)=integral_0^infinity d_0(t)t^(s-1)dt. C_phys d_0(r) is zero for
large r and flat as r tends to zero, by Poisson, the zero mean/trace and
the Schwartz decay of Fd_0. Its entire Mellin transform is the continuation
of zeta(s)M_d0(s), initially obtained by absolute summation for Re s>1.
Consequently

    U_(N_0)=integral_0^1 C_phys d_0(r)dr/r=-M_d0(0)/2,
    V_(N_0)=integral_0^1 C_phys d_0(r)dr=M_d0'(1).           (10)

No interchange of divergent individual mean-zero integrals at s=0 or1
is used.

Choose a nonnegative even smooth k_0 supported away from zero in
|u|<exp(-c)/4, with integral_R k_0=1. For r=2,4 define
k_r(u)=r^(-1)k_0(u/r), d_r=k_r-k_0, and m0=M_k0(0)>0. Their moment columns
from (10) are

    (U_(N_d2),V_(N_d2))=(m0/4,log2/2),
    (U_(N_d4),V_(N_d4))=(3m0/8,log2),
    determinant=m0 log2/16>0.                              (11)

A finite linear combination subtracts both moments of E in (8). Call
the result E_sharp. It still vanishes on (0,c), is still the Euler lift
of a selfdual trace-zero Schwartz seed obtained from ONE compact smooth
seed as in the theorem, and satisfies

    U_(E_sharp)=V_(E_sharp)=0,
    B_cross E_sharp=B_cross E,
    q0[E_sharp]=q0[E]=q0[tau]<0.                            (12)

For the last equality, the corrections are genuine source-neutral;
equivalently use symmetry of the complete B_cross pairing. The resulting
compact seed is d minus twice the chosen linear combination of d_2,d_4.
All masks and corrections are finite.

## 6. Equivalence and retained scope

Apply (4) and (12). Since both moments are zero,

    4<E_sharp,C_cross E_sharp>=q0[E_sharp]=q0[tau]<0.        (13)

Thus any original negative compact direction violates item 2. Conversely,
if item 1 holds, approximate every constructed rapid-log source in the
source graph by compact smooth odd sources. Continuity of (1) gives
q0[E]>=0; equation (4) and its zero moments give item 2. This proves the
stated equivalence for every fixed finite c.

Every reflected prime power, every Gamma Hankel mode and the complete pole
were retained before exact neutral normalization. Positive entries of a
reflection kernel are not positive-semidefinite quadratic-form evidence.
Neither the universal crossing sign nor original positivity is proved
here. The construction supplies no original-P/hidden-square bound,
no actual-current stationarity for the changed source, and no uniform
representative norm. In particular no infinity-minus-infinity definition
of q0 as separate P-N energies is used.
