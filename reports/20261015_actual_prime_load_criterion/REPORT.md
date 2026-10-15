# A direct actual-source exclusion criterion, reduced to genuine primes

For the same original actual Green source, an all-positive-damping L2
bound on its complete reflected load would exclude that source. The
proper-prime-power part already satisfies this condition unconditionally;
the remaining sufficient condition concerns genuine primes. The genuine-
prime bound is **not proved here**, so this is not an exclusion theorem
without an additional hypothesis and does not prove RH.

## 1. Original source and the precise sufficient condition

Use the real, pole-centered actual source g=psi r at fixed 0<delta<1,
with all operators and original forms normalized as in the
[physical range theorem](../20261015_old_actual_physical_range/REPORT.md),
Section 0. In particular

    Wg=Lr-F_r g, L=F_r psi,
    T g=-delta Wg,
    q0[g]=-delta N[g]<0.

The last strict inequality is the nontrivial actual negative-state
hypothesis, not a conclusion for an arbitrary source or the null ground
psi. Write alpha_n=Lambda(n)/sqrt(n), d_n=log n, and retain every prime
power in F_+, F_-, F_r and L. The full source pole is -8 ell(g)^2,
ell(g)=int_0^infinity sinh(x/2)g(x)dx; the stated centering is ell(g)=0.

The published actual ratio and origin theorems, linked in the range
report, supply a bounded ratio r, a globally Holder-continuous ratio
remainder of some positive order, and the complete theta tail for g.
The same range report defines the physical load

    w(t)=t^(-1/2)(Wg)(log t), t>=1,
    w(t)=0 on |t|<1,

with even extension on the physical line. It also proves the retained-
constant completion H=Dw+c, Fourier(H)=H, H=c on the unit head. The
criterion below concerns Wg itself; it does not assume that the critical
causal inverse is bounded on physical L2.

**Conditional exclusion criterion.** If

    int_0^infinity exp(-epsilon x)|(Wg)(x)|^2 dx < infinity
                                      for EVERY epsilon>0,       (1)

then the nontrivial actual negative state cannot exist. Equivalently,

    int_1^infinity t^(-epsilon)|w(t)|^2 dt < infinity
                                      for EVERY epsilon>0.       (2)

The equivalence is the exact change of variable t=exp x. Ordinary
unweighted L2 for Wg, or equivalently ordinary physical L2 for w, is a
stronger sufficient hypothesis, not a necessary part of this statement.
One fixed positive epsilon only removes a corresponding smaller region
of off-critical zeros and is insufficient for the conclusion below.

## 2. Complete transform proof of the criterion

Put

    E_+(z)=int_0^infinity exp((z-1/2)x)g(x)dx,
    E_-(z)=int_0^infinity exp(-(z-1/2)x)g(x)dx,
    Delta E(z)=E_-(z)-E_+(z).

Both transforms are entire by the complete theta tail. Let

    M_T(z)=int_0^infinity exp(-(z-1/2)x)(Tg)(x)dx.

Initially Re z>1, the complete arithmetic rows are absolutely summable.
The past and reflected rows have exactly the transforms

    M_(F_-g)(z)=-(zeta'/zeta)(z) E_-(z),
    M_(F_rg)(z)=-(zeta'/zeta)(z) E_+(z)-J_g(z),
    J_g(z)=sum_(n>=2)Lambda(n)n^(-z)
                    int_(d_n)^infinity exp((z-1/2)y)g(y)dy.       (3)

The theta tail makes J_g entire, with locally uniform absolute
convergence. The future row F_+g has a theta tail uniformly after its
complete Mangoldt sum, so its one-sided transform is entire too.

For completeness, no infinite Gamma moment series is needed to continue
the archimedean row into the required half-plane. If g_o is the odd
extension and kappa(t)=exp(-t/2)/(1-exp(-2t)), its operator is

    A_Gamma g(x)=-C0 g(x)
       +int_0^infinity kappa(t)
          [2g(x)-g_o(x+t)-g_o(x-t)]dt,
    C0=log pi-digamma(1/4).                           (4)

This is the multiplier a(t)=Re digamma(1/4+it/2)-log pi used in the
range report. On a fixed compact x interval, the actual positive Holder
regularity pays the t=0 singularity. For x large, split t<1 from t>=1.
On the first part the Holder bound for r and the theta bounds for psi and
its derivative give a superexponentially small bound times t^alpha,
alpha>0. On the second part kappa(t)<=C exp(-t/2); the two translated
terms are bounded by

    C exp(-x/2) int_R exp(y/2)|g_o(y)|dy

and a superexponentially small future term. The unshifted contribution
is also theta-small. Consequently

    |A_Gamma g(x)|<=C exp(-x/2), x>=2,               (5)

and its one-sided transform is holomorphic for Re z>0. All local
integrals in (4) are genuine convergent integrals for this actual source;
no derivative of order one or physical operator-domain upgrade is used.

Since T=A_Gamma-F_+-F_-+F_r, equations (3)-(5) prove the complete
meromorphic identity

    M_T(z)=(zeta'/zeta)(z) Delta E(z)+R_g(z),
    R_g holomorphic on Re z>0.                      (6)

Every prime-power term is included. At z=1, Delta E(1)=-2ell(g)=0
removes the prime pole in the specified centered gauge. Without that
centering, the full source-pole transform would be
-2ell(g)[1/(z-1)-1/z], and its z=1 residue cancels the prime residue;
it may not simply be omitted in an uncentered formula.

Under (1), the actual equation M_T=-delta M_(Wg) has a holomorphic
right side throughout Re z>1/2. Indeed for a compact subset of this
half-plane choose epsilon>0 smaller than twice its distance from the
boundary; Cauchy--Schwarz with exp(-epsilon x)|Wg|^2 pays the transform
and all its complex derivatives locally uniformly. At a nontrivial zero
rho with Re rho>1/2 and multiplicity m_rho, equation (6) therefore gives

    0=Res_(z=rho) M_T(z)=m_rho Delta E(rho).          (7)

The odd-source transform E_+-E_- changes sign under z->1-z. Thus it
vanishes on the entire reflected left off-critical orbit as well.

The decisive last step uses the complete, absolutely convergent
[signed zero identity](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md),
equations (14)-(16), on exactly this actual source domain. In its
notation F(z)=int_R g_o(x)exp(izx)dx and z_rho=-i(rho-1/2),

    q0[g]=sum_rho m_rho F(z_rho) conjugate(F(conjugate(z_rho))).   (8)

All off-critical summands vanish by (7) and reflection. On the critical
line z_rho is real, so the remaining terms are m_rho|F(z_rho)|^2>=0.
Absolute convergence is part of the cited actual-source theorem and
licenses this restriction of the full sum, with multiplicities retained.
It contradicts q0[g]=-delta N[g]<0 and proves the conditional criterion.

This argument does not claim that neutral annihilation or the physical
self-Fourier completion alone supplies (1). The actual source equation
and the signed zero identity are indispensable to the implication.

## 3. The complete proper-prime-power load is already paid

Define, in physical variables,

    p(t)=t^(-1/2)psi(log t), R(t)=r(log t), t>=1.

Here p is the physical theta ground, while R is the same bounded actual
ratio. Explicitly, with z=pi t^2,

    kappa_xi(t)=(8z^3-30z^2+15z)exp(-z),
    p(t)=sum_(n>=1)kappa_xi(nt).

The complete normally convergent theta sum gives

    |p(t)|<=C t^6 exp(-pi t^2), t>=1.                (9)

No theta label is truncated. To avoid overloading p, write the prime
variable as ell. The proper-prime-power part of w is exactly

    w_high(t)=t^(-1)sum_(ell prime, k>=2, ell^k>t)
       (log ell) p(ell^k/t)[R(t)-R(ell^k/t)].        (10)

Both square-root factors in Lr-F_rg cancel to the displayed 1/t;
there is no additional label factor 1/ell^k in (10).

Only the unconditional Chebyshev bound theta(X)<=C X is needed.
It gives, for X>=2,

    A_high(X)=sum_(ell^k<=X, k>=2)log ell <=C sqrt(X),
    A_(>=3)(X)=sum_(ell^k<=X, k>=3)log ell <=C X^(1/3).          (11)

For the first bound isolate k=2, while all k>=3 contribute at most
C X^(1/3)log(2X)=O(sqrt X). For the second isolate k=3, while k>=4
contribute at most C X^(1/4)log(2X)=O(X^(1/3)). The finite small-X range
is absorbed into the constants. No prime-number-theorem error estimate
or square-root cancellation for genuine primes is being assumed.

Split (10) into the complete dyadic shells ell^k/t in [2^j,2^(j+1)),
j>=0. Bounded R, (9), and (11) give

    |w_high(t)|
       <=C t^(-1/2)sum_(j>=0)2^((13/2)j)exp(-pi 4^j)
       <=C' t^(-1/2), t>=1.                         (12)

The finite superexponential shell sum includes the finite t collar and
the entire infinite arithmetic tail. Applying the second bound in (11)
in the same way gives

    |w_(>=3)(t)|<=C t^(-2/3).                       (13)

Hence for every epsilon>0,

    int_1^infinity t^(-epsilon)|w_high(t)|^2dt<infinity.        (14)

Equivalently, W_high g(x)=exp(x/2)w_high(exp x) is O(1), and the
k>=3 source part is already in ordinary unweighted L2(dx). The square
scale is borderline only for that unnecessarily stronger norm.

Let w_prime be the k=1 term, retaining the same full ground and actual
ratio:

    w_prime(t)=t^(-1)sum_(ell prime, ell>t)
       (log ell) p(ell/t)[R(t)-R(ell/t)].            (15)

Since w=w_prime+w_high, the triangle inequality and (14) show that
(1)-(2) are equivalent to the single remaining direct condition

    int_1^infinity t^(-epsilon)|w_prime(t)|^2dt<infinity
                                      for EVERY epsilon>0.       (16)

Thus (16), if proved for this same actual source, would suffice for
exclusion. It is the unproved genuine-prime condition, not an established
bound or an independent positivity assertion.

## 4. Scope: the direct criterion is not a finite-mask norm estimate

The reduction removes proper prime powers only from the DIRECT
all-positive-damping condition (1). It does not split H into separately
self-Fourier prime and prime-power fields. The completion H=Dw+c, every
selfdual finite-mask test, and every complete source Gamma/prime/pole
identity must continue to use the whole w.

In particular (14) does not bound a proper-power load paired with a
finite-mask reflected collar, does not bound an escaping causal-adjoint
tail, and does not prove a subpower head norm for a natural Mobius mask.
Such full-mask estimates are not asserted necessary for the direct
criterion, and no converse from (1) to those estimates is used. The
present result isolates a sufficient actual-source endpoint and pays
its full proper-power component; the remaining genuine-prime estimate
and the complete signed comparison are still open.
