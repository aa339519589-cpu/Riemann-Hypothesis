# The natural Euler error: its exact constant Fourier defect and a repaired dual bound

This theorem controls a specific error pairing, not the fixed-limit main
arithmetic collar. It retains the same original actual field and fixed
outer mask; no new negative state is introduced. Its source input is the
[physical range theorem](../20261015_old_actual_physical_range/REPORT.md),
including that theorem's retained constant channel and original source
normalization.

## 1. Fixed normalization and genuine weighted convergence

Use the real even old actual field H=Fourier(H), with H=c on (-1,1),
H in H^s(R) and |u|^s H in L2 for every 1/2<s<1. In particular
integral_R H=c. Write

 D_d f(u)=f(du), D_d^*f(u)=f(u/d)/d,
 B0=I-5D_4+4D_16,
 M_N=sum_(n<=N)mu(n)D_n, P_N=B0 M_N,
 F_N=P_N H, Fhat_N=P_N^*H,
 e_N=C F_N, ehat_N=C Fhat_N, C=sum_(n>=1)D_n.

The sums defining C are genuine bounded operators on
X_s=L2(R,|u|^(2s)du), because ||D_n||_(X_s)=n^(-s-1/2).
The complete Mobius inverse converges absolutely in the same operator norm,
so CM=MC=I there. Thus, with

 epsilon_N=e_N-B0 H,

one has the WHOLE-line bound

 ||epsilon_N||_(X_s)<=C_s N^(1/2-s)||H||_(X_s).       (1)

The finite coefficients of P_N have both polar sums zero:
sum a_d=sum a_d/d=0. Hence F_N has trace and full integral zero,
Fhat_N vanishes on (-1,1), and complete Poisson reciprocity gives

 e_N(u)=ehat_N(1/u)/|u|, u!=0.                       (2)

For clarity, this reciprocity does not assert an ordinary unweighted
Euler-sum limit. Since Fourier F_N=Fhat_N and both polar terms vanish,
Poisson summation gives it first on simultaneous Schwartz oscillator
approximants of H, with the finite mask kept fixed. On either physical
wing away from0, C is bounded on X_s and reciprocal pullback sends the
positive tail to the corresponding X_-s head. Passing in these weighted
spaces proves (2). Equivalently, one may prove the same equality with
common smooth Euler cutoffs and then the absolutely convergent weighted
operator limits. The positive physical moment and Sobolev bounds of H
supply the required fixed-N approximations; no bound for a critical-line
Euler multiplier is being assumed.

For each FIXED N, both e_N and ehat_N belong to X_s. Equation (2) also
puts e_N in X_-s. Consequently e_N is a genuine L1 and L2 function.
The latter assertions need not have uniform-in-N norms.

## 2. The Euler mean is not zero

Use half-line physical Mellin transforms M_f(z)=integral_0^infinity
f(u)u^(z-1)du. The X_s and X_-s bounds give absolute convergence of M_e
in a strip containing z=1. In the initial overlap Re z>1,

 M_e(z)=zeta(z) M_F(z),
 M_F(z)=B0(z)m_N(z)MH(z),
 B0(z)=1-5*4^(-z)+4*16^(-z),
 m_N(z)=sum_(n<=N)mu(n)n^(-z).

Since B0(1)=0 and MH(1)=c/2, continuation within the actual integral
strip gives the genuine full Euler mean

 k_N=integral_R e_N=2M_F'(1)
     =c B0'(1)m_N(1), B0'(1)=3log(4)/4.              (3)

This is not obtained by interchanging the complete Euler sum and the
integral. Every FINITE Euler sum C_K F_N instead has integral zero.
Its tempered-distribution limit is

 C_K F_N -> e_N-k_N delta_0.                        (4)

For precision, F_N has mean zero and a positive fractional L1 moment.
Thus for a Schwartz test phi with phi(0)=0,

 sum_n n^(-1) integral |F_N(v) phi(v/n)|dv < infinity,

by |phi(v/n)|<=C_alpha |v/n|^alpha and
sum n^(-1-alpha)<infinity. The limit therefore agrees with the ordinary
e_N pairing on every such test, so their difference is exactly a multiple
of delta_0, with no derivative atom. Fourier transforming the finite sums
gives sum_(n<=K)Fhat_N(u/n)/n. For fixed N, Fhat_N is bounded by
the H^s regularity of H and has a unit gap. These causal partial sums
therefore have a uniform O_N(log(2+|u|)) majorant, stabilize locally, and
converge in tempered distributions. They vanish on the unit gap. Since
e_N is L1, its Fourier value at zero is k_N, determining the coefficient
in (4).

Write Dv(u)=sum_n v(u/n)/n for this locally finite causal sum. Then

 Fourier(e_N)=D Fhat_N+k_N.                         (5)

On |u|<=N, finite causal Mobius cancellation gives
D Fhat_N=B0^*H. Therefore

 Fourier(epsilon_N)=k_N on |u|<N.                  (6)

The error has a CONSTANT low-frequency defect, not a spectral gap.
Applying physical B0 would kill it and give a true gap, but is unnecessary
for the trace-zero dual estimate below. In particular no X_s norm is
assigned to epsilon_N-k_N delta_0.

## 3. Weighted smooth high-pass duality with the constant retained

Lemma. Let 1/2<s<1, 0<q<1, N>=1. Suppose epsilon is a real even L2
function in X_s whose Fourier transform equals the constant k on |xi|<N.
Let phi be an even H^q function supported in

             {u: a<=|u|<=b}, 0<a<=1<=b.

Then

 |integral_R epsilon phi|
 <=C_(s,q) (1+b)^(1/2) a^(-5) N^(-q)
                         ||epsilon||_(X_s)||phi||_(H^q).   (7)

The same statement for a positive-wing test follows by even extension
and the harmless factor two. No point evaluation of phi at an interior
jump is used; its vanishing in a whole origin neighborhood is essential.

Proof. Choose one smooth even low-pass chi, equal to1 on |xi|<=1/4 and
supported in |xi|<1/2, and let L_N have symbol chi(xi/N). Choose a real even
Schwartz v with v(0)=1 and Fourier support in |xi|<1/4, and set v_N(u)=v(Nu).
The WHOLE repaired test is

 eta_N=(I-L_N)phi+[L_N phi](0)v_N.                  (8)

It has eta_N(0)=0. Both Fourier supports used in the subtraction/correction
lie strictly inside the interval in (6). Since phi vanishes near zero,

 integral epsilon L_N phi=k[L_N phi](0),
 integral epsilon v_N=k,

and hence integral epsilon phi=integral epsilon eta_N EXACTLY. The constant
Euler defect cancels between these two terms; it is not discarded.

It remains to prove

 ||eta_N||_(X_-s)<=C_(s,q)(1+b)^(1/2)a^(-5)
                                      N^(-q)||phi||_(H^q).            (9)

On |u|>=a/2, the weight is bounded by (2/a)^(2s). The standard smooth
high-pass L2 estimate is N^(-q)||phi||_(H^q). If K is the Schwartz kernel
of L_1, its off-support decay gives, for j=0,1 and any integer M,

 sup_(|u|<=a/2) |partial_u^j L_N phi(u)|
 <=C_(j,M)(1+b)^(1/2) a^(-M) N^(j+1-M)||phi||_2.    (10)

Also ||v_N||_2=N^(-1/2)||v||_2. These bounds pay the correction on
|u|>=a/2. On |u|<a/2, the WHOLE eta_N vanishes at zero, and (10) together
with ||v_N'||_infinity=O(N) gives

 |eta_N(u)|<=C_M(1+b)^(1/2)a^(-M)N^(2-M)||phi||_2 |u|.

Integrating |u|^(2-2s) is legitimate. Taking M=4, using N>=1, q<1,
s<1 and a<=1 proves (9), including the displayed polynomial dependence
on the distance a from the origin. The individual pieces in (8) need NOT
separately belong to X_-s; only their full trace-repaired combination does.
Weighted Cauchy now proves (7). QED.

Applying (7) and (1) yields the SAME original-mask ERROR estimate

 |integral epsilon_N phi|
 <=C_(H,s,q)(1+b)^(1/2)a^(-5)
                    N^(1/2-s-q)||phi||_(H^q).        (11)

## 4. Exact scope for the arithmetic comparison

The lemma by itself treats compact dual tests away from zero. Applying it
to the full comparable-label triangle, past and delta rows still requires
uniform bounds for their actual H^q test functions, all endpoint cuts and
both physical tails. In particular the cut at1 permits only q<1/2 without
an additional trace cancellation. Polynomial dependence on a^(-1) in (11)
allows a logarithmically shrinking origin collar if the omitted theta-flat
part is separately and completely paid.

Even after such an application, (11) pays only the difference e_N-B0H.
The fixed main field B0H, its reciprocal field, every prime power and the
complete actual delta/polar collar remain. No critical-head upper bound,
scalar contraction, replacement of the actual source, or RH sign follows
from the error estimate alone.
