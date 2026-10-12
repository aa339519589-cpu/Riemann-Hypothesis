# Common boxes and pooled tails for the sharp mode-local detector

This is a proof supplement for Part XXXI B–C of
[QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), frozen at
`d74308ed56639ddf0505f1e50007f79337d367da`. It addresses the box and tail
qualification in the independent mode-window review. It does not replace the
local reciprocal-L lemma, shifted-height density theorem, or original
detector identity. Its application is conditional on those separately
stated analytic inputs, with their original seminorm and conductor
quantifiers. In particular an arithmetic checker does not establish them.

## 1. One common height box for every retained mode

Fix the real Fourier spacing omega and a positive constant C0 once.
Let eta=7/500, tau0=1/500 and choose one zeta in (0,1/100000]. Put

    H_F=ceil(M^eta(1+T)), L=M^zeta(1+T), 0<=T<=M^tau0.

The original selected heights obey |gamma_i|<=T and every retained
Fejer frequency is nu_j=omega j, |j|<=H_F. Any additional fixed finite
collection of Mellin variables restricted to |u_r|<=L has total absolute
size <=K L, where K is fixed by the kernel separation, independently of
j, row, M, T, and b. Choose C0 larger than this K plus the fixed contour
height margins; increasing C0 does not change any power below.

For M>=2, 1+T<=2M^tau0 and H_F<=3M^(eta+tau0). Thus the maximum height
of every center, box, and retained additional Mellin shift is at most

    2+T+|omega|H_F+(C0+K)L <= C(omega,C0,K) M^(2/125),

since eta+tau0=2/125 and zeta+tau0<=201/100000<2/125.
The strict difference

    1/50-2/125=1/250

absorbs the fixed constant for all sufficiently large M. The remaining
bounded M are absorbed into the implied constant. This proves inclusion
of the entire mode range, not a grid of sampled frequencies. All constants
are common on the compact real-part interval used in Part XXXI C.

On a sufficiently small closed interval around alpha0=47/300 the local
height exponent p2(alpha) belongs to [p_min,p_max] contained in (0,1),
because p2(alpha0)=611/4429 and its rational denominator is nonzero
there. The actual bad-mode intervals are contained in the single interval
centered at -nu_j of radius T+C0 L. Covering it by fixed-width intervals
costs O(M^zeta(1+T)); every covered height satisfies

    1+|t0| <= C(1+|j|) M^zeta(1+T).

The local row-count bound therefore gives the common estimate

    |B_j| <= C_epsilon M^(D2(alpha)+2zeta+epsilon)
                      (1+T)^C (1+|j|)^(p2(alpha)+epsilon).

For any a in a fixed compact subset of (0,infinity),
sum_(j<=H) (1+j)^(a-1) <= C_a H^a, with C_a bounded uniformly on that
compact subset. Taking a=3p2(alpha)/8 (and reserving the small epsilon
loss) gives the actual weighted mode cost H_F^(3p2(alpha)/8+epsilon).
The exponent 2zeta becomes 3zeta/4 in Holder's 3/8 row factor. This is
the full mode sum used in Part XXXI B (10).

## 2. High Mellin tails before a reciprocal contour shift

Here is the elementary tail estimate that is available independently
of a zero-free assumption. Let W be a compact smooth norm test, with
support in a fixed annulus, and let beta range in a fixed compact interval
[b_min,b_max] contained in (1/2,1). Choose a fixed delta_abs>0, put
c_beta=1+delta_abs-beta, and suppose D>=1. Mellin inversion for the
smooth Mobius dyad, with the genuine presentation holes S, is

    F_(chi,j,u)(D)=sum_(d,(d,S)=1) mu_K(d)chi(d)(Nd)^(-rho+i nu_j+i u)W(Nd/D)
      = (1/(2pi i)) integral_(c_beta)
          What(s) D^s / L^S(rho-i nu_j-i u+s,chi) ds.

On this ORIGINAL line, the argument of L^S has real part 1+delta_abs.
The absolutely convergent inverse Euler series yields

    |1/L^S(1+delta_abs+it,chi)| <= zeta_K(1+delta_abs),

Here (d,S)=1 means that d avoids every prime deleted in L^S; the
character also retains its own original zero extension. The sum and
the incomplete Euler product therefore have exactly the same masks.
The bound is uniform in the character, height, and deleted prime set. No estimate
of reciprocal L near a zero is used. For every fixed integer N>=2,
integration by parts in log x gives, uniformly in beta,

    |What(c_beta+i v)| <= C_N (1+|v|)^(-N),

where C_N is controlled by finitely many common compact norm seminorms.
The portion |v|>L of the original integral consequently obeys

    |F_tail| <= C_N D^(1+delta_abs-b_min) L^(1-N).

The frequencies nu_j and u are shifts of the L argument, not derivatives
of W. There is no (1+|j|)^N cost in this inequality. If the already
separated common weight seminorms cost (1+T)^(B_N), retain that factor.
With D<=M^x_max, where x_max is fixed before N, this is at most

    C_N M^[x_max(1+delta_abs-b_min)-zeta(N-1)](1+T)^(B_N).

For any prescribed A and any previously fixed polynomial M-cost B of
restoring the original finite columns, one can choose the finite N so
that zeta(N-1)>A+B+x_max(1+delta_abs-b_min). The tail then remains
M^(-A-B)(1+T)^(B_N). N is selected after zeta, and its possible effect
on B_N is retained. In particular we do not substitute T<=M^tau0 to
infer pointwise smallness from this final polynomial T factor.

## 3. Horizontal joins on good rows

For clarity, a truncated contour move is not an equality obtained by
dropping its horizontal joins. For a good row, the original local
zero-free box has no zeros with Re>=b+h and imaginary part within C0 L
of gamma_i-nu_j. Suppose that every retained extra u has |u|<=K L and
that C0>K+3. Move the rectangle from Re s=c_beta to

    Re s=b+2h-beta,

at heights Im s=+L and -L. Its L arguments stay in the original box
and have real part at least b+2h. There are no reciprocal-L poles in
the rectangle; a principal L pole produces a reciprocal zero. The
buffered local reciprocal-L input of Part XXXI B supplies its
conductor-height small-power bound on these two joins as well as on
the new vertical segment. The width is bounded uniformly on the
compact beta interval. Repeated integration by parts bounds the
horizontal integrands by C_N L^(-N), while D^Re s is bounded by
M^[x_max(1+delta_abs-b_min)]. Thus the joins have the same arbitrarily
small M-power tail, with their original small conductor-height power
and polynomial T dependence retained. If the quoted reciprocal-L
input were proved only on the central vertical segment, this
horizontal-bound application would be an additional required input;
it is not implied by the exponent ledger.

This argument leaves the high original-line tails unshifted. It makes
no contour move outside the prescribed zero-free box and pays no
unaccounted zero residue. On bad rows no such contour move is used:
their exact original central representation is retained.

## 4. Pooling and restoration to the original detector

The finite Fejer coefficients satisfy

    sum_(|j|<=H_F)|c_j| <= C log(2H_F).

Consequently any uniform per-mode tail bound E_j<=M^(-A)(1+T)^(C_A)
implies

    |sum_j c_j E_j| <= C M^(-A)(1+T)^(C_A) log(2H_F).

For every fixed epsilon_tail>0, log(2H_F), the finite number of separated
columns, and O((log M)^C) dyadic pieces cost at most
M^epsilon_tail(1+T)^epsilon_tail. For a positive
row moment r>=1, Minkowski gives the corresponding pooled bound

    sum_(i in original rows)|sum_j c_j E_(i,j)|^r
        <= C M^(1-rA+epsilon_tail)(1+T)^(r C_A+epsilon_tail),

using the actual O(M^(1+epsilon)) family size. Row masks depending on
j can only reduce each positive r-norm; they are not absorbed into
a common column coefficient. Markov at a fixed threshold leaves a
negative M power after A is chosen large enough, with the same full
polynomial T dependence. Increase the final theorem's height degree
only after the finite N,A have been fixed.

This pooling step applies to the full detector after restoring its
original separated columns. That restoration must use the inherited
common Mellin/Schwartz bounds, before tuple ratios or dyad labels are
pooled. No arbitrary row-dependent weights are admitted here. On the
compact beta interval the original central L integral has polynomial
conductor-height growth and its Gamma factor has exponential relative
height decay. The finite inverse column has length <=X=M^x_max with
coefficients of modulus at most one. Thus their absolute restoration
has a fixed polynomial M bound B and finite seminorm-dependent T
degree, independent of j. Equivalently on the exact reflected kernel,
the second column's tail m^(beta-1) min(1,K0/m) is absolutely summable
because beta<=b_max<1; its original gamma is used and is independent
of nu_j. These are the previously stated detector inputs that justify
choosing the larger A+B in Section2. An angular or j-dependent weight
class would require a new proof and is outside this lemma.

The order is: freeze the compact beta interval and common weight class;
fix omega, eta, tau0, zeta and structural box constants; prove the
original-line and horizontal-join tail bounds with finite derivative
orders; restore the actual columns and pool the L1 mode sum; apply
Markov on the original row family; select the final polynomial T
degree and small losses last. The original polynomial kernel tail and
sharp cutoff error remain separate paid terms of Part XXXI B.

## Scope

This closes the elementary all-mode box and pooled-tail accounting
provided the cited local reciprocal rectangle and common-weight
detector inputs have their stated uniform scope. It makes no new
numerical physical gain claim, no all-row reciprocal-L bound, and no
RH conclusion. The analytic companion and full detector still require
independent review.

The original analytic and physical statements are Part XXXI A--C and Part XXX C of [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md). An independent audit of this supplement is [REFEREE_MODE_LOCAL_BOX_TAIL.md](REFEREE_MODE_LOCAL_BOX_TAIL.md). The elementary all-mode slack and center height exponent are checked by [check_mode_local_boxes.py](check_mode_local_boxes.py); this script does not verify the analytic inputs.
