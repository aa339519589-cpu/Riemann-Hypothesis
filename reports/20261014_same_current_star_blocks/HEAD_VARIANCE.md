# An original-head Schur contribution to the actual dominant covariance

This note puts the independently proved UNPENALIZED original head gap
inside the dominant current covariance. The features are cutoffs of the
actual current ERROR e, not cutoffs of the actual source u. No stationary
source equation is asserted for e. The full feature mean and every mixed
term are completed exactly before the head theorem is applied.

## 1. Paid inputs and the covariance to be tested

Use the lawful dominant feature family from
[DOMINANT_COVARIANCE.md](DOMINANT_COVARIANCE.md):

    omega=1/epsilon increasing,
    dnu(a)=omega(0)delta_0(da)+omega'(a)da,
    h_a(x)=e(x)1_(x>=a), f_a=psi h_a,
    Q_D=int Q_delta[f_a]dnu(a),
    K_S,D=int N[Pi_S f_a]dnu(a).

Every f_a is in the original P completion and the integrated original P,N
forms are finite. The full pole and all prime powers are retained. Here S
is a single fixed lawful common P/N neutral span, possibly S=0, and Pi_S
is its common projection. Write

    Q_S[f]=Q_delta[(I-Pi_S)f]
          =q0[f]+delta N[(I-Pi_S)f]>=0.                     (1)

The final nonnegativity is the actual positive-depth PSD hypothesis.
The identity uses neutrality of S, not support preservation of Pi_S.

The new unconditional input is the published
[complete original-head theorem](../20261014_unrepaired_original_head/REPORT.md):
with b=log2 and gamma=10^(-10),

    q0[f]>=gamma int_0^b |f(x)|^2dx                       (2)

for the original logarithmic Gamma-domain sources supported in (0,b).
No U or neutral load is added to (2). All Gamma, internal reflected2/3,
and the full original pole are in that theorem. Its source normalization
is exactly the positive-wing source L2 norm in (2).

## 2. Exact mean completion, before using a sign

Restrict nu to [0,b], whose total mass is

    M=nu([0,b])=omega(b).

Let k_a=e1_(0,a), so h_a=e-k_a, and set

    kbar(x)=M^(-1)int_[0,b]k_a(x)dnu(a)
           =e(x)[1-omega(x)/M]1_(0,b)(x),
    hbar=e-kbar,
    j_a=k_a-kbar.

All j_a are supported in (0,b), and int_[0,b]j_a dnu=0. Consequently the
COMPLETE quadratic polarization identity is

    int_[0,b] Q_S[psi h_a]dnu(a)
        =M Q_S[psi hbar]+int_[0,b]Q_S[psi j_a]dnu(a).       (3)

No mixed term has been deleted: it vanishes because the feature fluctuation
has exactly zero mean. The same identity is valid for every bilinear pair
in a finite family of errors e_i, using the same omega and measure nu.

The projected fluctuations (I-Pi_S)(psi j_a) need not remain head-supported.
That is harmless but must not be confused with an input to (2): neutrality
makes their q0 form equal to q0[psi j_a], to which the head theorem DOES
apply. Thus exactly

    Q_S[psi j_a]=q0[psi j_a]
                        +delta N[(I-Pi_S)(psi j_a)].       (4)

Both terms on the right are retained.

## 3. The explicit positive head variance

The finite-measure variance identity is pointwise:

    int_[0,b]|j_a(x)|^2dnu(a)
       =|e(x)|^2 omega(x)[1-omega(x)/omega(b)]1_(0,b)(x).
                                                               (5)

Indeed k_a(x) is e(x) times the indicator a>x, whose nu mass is
M-omega(x). Its unnormalized variance is
(M-omega(x))-(M-omega(x))^2/M. The atom omega(0)delta_0 is essential for
M=omega(b) and for (5); it is not silently omitted.

Combining (1)-(5) and keeping the remaining a>b features gives the exact
paid decomposition

    Q_D-delta K_S,D
      =M Q_S[psi hbar]
       +int_(b,infinity)Q_S[psi h_a]dnu(a)
       +int_[0,b]q0[psi j_a]dnu(a)
       +delta int_[0,b]N[(I-Pi_S)(psi j_a)]dnu(a).          (6)

The first two terms are nonnegative by actual PSD, the third has the
UNCONDITIONAL original-head sign, and the fourth is the exact remaining
positive neutral-residual N variance. In particular

    Q_D-delta K_S,D
       >=gamma int_0^b psi(x)^2|e(x)|^2 omega(x)
                                    [1-omega(x)/omega(b)]dx.   (7)

One may retain the first, second, and fourth terms of (6) for a later
comparison; they are not independently available a second time.

For any finite family of actual errors e_i this is the Hermitian matrix
inequality

    [Q_D,ij-delta K_S,D,ij]
       >=gamma [int_0^b psi^2 e_i conj(e_j) omega
                                    (1-omega/omega(b))].      (8)

It is obtained by applying (7) to an arbitrary common linear combination,
not by independently choosing a favorable center for each matrix entry.

## 4. Head domain and full signed accounting

The feature cutoff proof already makes every psi k_a legal in the original
Gamma domain. It has the actual bounded origin ratio multiplied by psi,
so the source trace vanishes at zero. Its single interior jump is permitted
by the logarithmic form. Smooth cutoff approximations at a and b have the
same O(eta[1+|log eta|]) continuous cost and complete finite prime rows as
in the dominant-feature proof. The finite measure nu([0,b]) and the local
weighted form bounds pay the integrated passage. Thus psi j_a lies in the
head theorem's honest logarithmic domain, not a falsely strengthened
all-derivatives source class. Formula (4) does not assert that Pi_S j_a
has compact support.

Let G_D=int psi^2 omega(abar-a_1)|e|^2, and retain the exact two-group
spatial identity E_sp[Y]=F[e]+F_D+G_D. Then the earlier complete dominant
boundary comparison is now strengthened, on the SAME budget, to

    2E_sp[Y]-B_delta[e]-B_D
          -delta{N[Pi_S(psi e)]+K_S,D}
      >=2G_D+gamma int_0^b psi^2|e|^2 omega(1-omega/omega(b)).  (9)

The undisplayed nonnegative terms in (9) are explicitly those in (6)
and Q_S[psi e]. In particular the head variance is supplied by the Q_D
term already present in the exact dominant completion; it is not added
to a previously exhausted spatial budget.

This does NOT identify e with an actual null source, supply an unpenalized
sign for arbitrary future cuts, or remove the higher-label spatial and
boundary cross terms. The strict SAME-star boundary Schur comparison
[BOUNDARY_SCHUR.md](BOUNDARY_SCHUR.md)
controls one such global cross block, but the entire original Q comparison
still has to match its remaining signed terms. No exclusion or RH claim
is made.
