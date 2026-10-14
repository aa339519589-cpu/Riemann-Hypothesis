# A generic lower bound for the original Schur form by safe hidden mass

This is a SIGNED lower comparison for the complete original source form.
It uses the verified unpenalized head gap, not actual largest-eigenvalue
positivity. Its constant is finite and independent of actual depth and
source amplitude, but is not numerically certified. It is not a positivity
theorem: the retained negative constant is not zero.

Use b=log2 and the exact safe-ray weights xi,W,m=Wxi. Let q0 be the FULL
original odd source form, including Gamma, all prime powers, both prime
orientations, and the pole. For a source f let its honest future seed on
y>b be a=(Mf)/xi, so

    f(x)=sum_(n>=1)n^(-1/2)xi(x+log n)a(x+log n), x>b. (1)

Initially take theta-localized sources with finite odd Gamma form, including
actual sources and finite neutral jets; all formulas below extend whenever
the displayed source forms and future representation are defined by their
proved closures. The theorem is: there is ONE finite C_* such that

    q0[f] >= -C_* integral_b^infinity m|a-c|^2          (2)

for every constant c and every source in this class. The same bound holds
for the original-source Schur form S0 at b:

    S0[f_T]>=-C_* integral_b^infinity m|a-c|^2.         (3)

No bounded-amplitude hypothesis is used. The arbitrary constant in (2)-(3)
is an exact global psi gauge; it is not an independent source replacement.

## 1. The unconditional positive head extends a little beyond b

The independently verified
[complete original head theorem](../20261014_unrepaired_original_head/REPORT.md)
gives gamma=10^(-10) on H_b=(0,b), in its closed logarithmic source domain.
Fix B_max=b+1/100. For every B in [b,B_max], let D_B be the zero-supported
odd Gamma source domain and q0,B its complete restriction. These are nested
Dirichlet source spaces, not the separate original P/N weighted domains.

All q0,B are restrictions of one form on D_(B_max). In this larger compact
head, the internal forward prime term is n=2, and the internal reflected
terms are n=2,3,4; all other internal prime overlaps vanish geometrically.
The new forward n=2 and reflected n=4 terms are NOT discarded. They, the
constant Gamma shift, and the full pole are bounded L2 forms. Hence a fixed
finite C_max gives, uniformly in B,

    q0,B[v]>=q_b[v_o]-C_max||v||_2^2.                 (4)

The positive Gamma symbol tends to infinity. Thus bounded Gamma energy
with support in [-B_max,B_max] is compact in L2, by the Fourier translation
criterion. It follows that there exists B_* in (b,B_max] such that

    q0,B_*[v]>=(gamma/2)||v||_2^2.                   (5)

For completeness, suppose no such interval exists. Choose B_j decreasing
to b and normalized v_j in D_(B_j) with q0[v_j]<gamma/2. Equation (4)
bounds their Gamma energy. Pass to an L2-convergent subsequence with limit
v of norm one supported in [0,b]. Lower semicontinuity of q_b and continuity
of all bounded internal shift/reflection/pole terms give q0[v]<=gamma/2.
The limit belongs to D_b. One direct domain verification is odd amplitude
truncation, removal of origin and support-end collars with their bounded
O(epsilon log(1/epsilon)) Gamma cutoff costs, and smooth approximation;
these show that every such supported finite-Gamma limit is in the stated
closed sine-core source domain. The bound at b contradicts q0[v]<=gamma/2.
This proves (5).

This is an UNCONDITIONAL fixed-head stability argument. It does not use
an actual depth delta, the no-eventual-constant theorem, or an actual
head eigenvector. It gives no numerical width B_*-b. That limitation remains
in C_* below.

## 2. The complete shifted tail is controlled in weighted L2 by mass

Fix one B=B_* satisfying (5), and let a0=a-c,

    M=integral_b^infinity m|a0|^2,
    F_B(x)=1_(x>B)sum_n n^(-1/2)xi(x+log n)a0(x+log n),
    S=||F_B||_L2(exp(2x)dx),
    Q_B=sup_(y>=B) exp(2y)xi(y)/W(y)<infinity.

The last supremum is finite: W is strictly positive away from b and has
its complete integer-row exponential asymptotic, whereas xi has its Gaussian
tail. It is the SAME exact W as in the hidden comparison, not a finite-row
surrogate. Minkowski and y=x+log n give

    S<=sum_n n^(-3/2)
             [integral_(B+log n)^infinity exp(2y)xi(y)^2|a0(y)|^2dy]^(1/2)
      <=3 sqrt(Q_B M),
    S^2<=9 Q_B M.                                    (6)

Every integer label remains. Unlike the endpoint weak-L2 estimate, (6)
needs no source amplitude because the cut is strictly beyond b.

## 3. Every negative original tail row and complete mixed row are bounded

Write alpha_n=Lambda(n)/sqrt(n),
A=sum_(n>=2)Lambda(n)n^(-3/2)<5. The exact tail source form is

    q0[F_B]=q_b[(F_B)_o]-2C0||F_B||_2^2
       -4 sum_n alpha_n integral_B^infinity
                          conjugate(F_B(x))F_B(x+log n)dx
       +2 sum_n alpha_n integral_0^(log n)
                          conjugate(F_B(x))F_B(log n-x)dx
       -8|ell(F_B)|^2.                              (7)

All pairings are real after the usual polarization/real-part convention.
For complex sources take the real part of the forward term in (7).
The weighted Cauchy estimates are

    |sum forward overlaps|<=A exp(-2B) S^2,
    |sum reflected overlaps|<=A S^2,
    |ell(F_B)|^2<=J_B S^2,
    J_B=integral_B^infinity sinh(y/2)^2 exp(-2y)dy<infinity.

For the reflected row use x+y=log n, so exp(-x-y)=1/n exactly. Therefore

    q0[F_B]>=q_b[(F_B)_o]-C_T(B)S^2,
    C_T(B)=2|C0|exp(-2B)+20exp(-2B)+10+8J_B.          (8)

No unbounded backward arithmetic row is split off here.

The complete mixed head density, for 0<x<B, is

    (B0^B F_B)(x)
      =-2 integral_B^infinity [kappa(y-x)-kappa(y+x)]F_B(y)dy
       -2 sum_n alpha_n F_B(x+log n)
       +2 sum_n alpha_n F_B(log n-x)1_(log n-x>B)
       -8sinh(x/2)ell(F_B).                          (9)

It satisfies ||B0^B F_B||_2<=K_B S for a finite explicit expression K_B.
The Gamma row is bounded by its Carleman kernel plus an exponential rank-one
kernel, the complete forward arithmetic row by 2AS, and the reflected row
by 2 exp(B)AS. The pole contributes
8||sinh(x/2)||_L2(0,B) sqrt(J_B)S. For example the larger safe expression

    K_B=2(pi+2)+10+10exp(B)
                    +8sqrt[(sinh(B)-B)/2]sqrt(J_B)    (10)

suffices. The first term deliberately overestimates the Gamma norm. The
Carleman and arithmetic derivations are the same absolute operator estimates
as in the [complete mixed-source proof](../20261014_unrepaired_original_head/MIXED_FORCING.md),
with b replaced by fixed B. Thus all infinite rows converge in L2 and retain
both prime orientations and the full pole.

## 4. Minimize only the positive enlarged head

Put e=f-c psi, v=1_(0,B)e, so its tail is F_B. The psi change is an exact
q0-null gauge, including its changed pole; q0[e]=q0[f]. The cuts are legal
in the source Gamma domain. The logarithmic Hardy bound pays their sharp
boundary cost without a trace hypothesis; in particular one may first
argue on the smooth source core and then use source-form closure.

Using (5), (8), (9), and completing the head square gives

    q0[e]=q0[v]+q0[F_B]+2 Re<B0^B F_B,v>
      >=q_b[(F_B)_o]
                -[C_T(B)+2K_B^2/gamma]S^2
      >=-9Q_B[C_T(B)+2K_B^2/gamma]M.                 (11)

Hence (2) holds with

    C_*=9Q_B[C_T(B)+2K_B^2/gamma].                    (12)

For (3), take f=E0(f_T), the original-harmonic source extension at b. Its
safe field is unchanged, because its added source is supported in (0,b).
It is in the logarithmic SOURCE domain, which is precisely what (4)-(11)
use. No separate N/P norm of that inverse output is needed. Thus the same
constant gives (3). Alternatively minimize (11) over the original head.

## 5. A sharper actual-source signed constraint

For an actual top source, the independently verified
[original Schur identity](SOURCE_SCHUR.md) is

    S0[g_T]=-delta N[g/psi]-delta^2 D_g,
    D_g=<n_g,A0^(-1)n_g>, n_g=2(Vg-F_r g).

Use the SAME head-weighted hidden mean c_a and M=integral m|a-c_a|^2 in
(3). The result is the signed actual constraint

    delta N[g/psi]+delta^2 D_g <=C_* M.              (13)

In particular, because P[g/psi]=(1-delta)N[g/psi],

    P[g/psi] <=(1-delta)C_* M/delta.                 (14)

Unlike the endpoint amplitude argument, C_* in (13)-(14) is independent of
actual fixed-depth Sobolev or supremum constants. Its dependence is solely
on the unconditional fixed enlarged head and the complete theta/prime rows.
The width in (5) and thus a numerical C_* are not certified here. One may
then use M<=125000 E_hidden, spending the one hidden budget once.

Neither (2), (3), nor (13) asserts C_*=0 or excludes an actual negative
source. They do not sign the universal original remainder, remove neutral
jets, or claim a coefficient-one payment. They give a finite lower bound
for the GENERIC original reduced form by hidden MASS, with all unfavorable
head and arithmetic contributions retained.
