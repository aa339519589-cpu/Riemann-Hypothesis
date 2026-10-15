# A finite-frequency Gamma lower bound for a genuine filtered complement source

## Scope

This is a component of a complete original-source Schur test, not a sign
assertion for that Schur form. In particular the complete prime/pole debit
and the full positive-head inverse must still be subtracted. No FFT
high-frequency truncation is used as mathematical evidence.

Use the exact stable-filter family from
[the filtered reciprocal-heat construction](SOURCE_DEFINITION.md)
with A=16, k=3, nu=9/4, m=6. Put z=pi exp(2x), b=log2,

    phi(x)=2z c(z)exp(-z)u(z)/W(x), c(z)=8z^3-30z^2+15z,
    F(z)=c(z)exp(-z)u(z)/W(x(z)),
    t(x)=sum_(n>=1)n^(-1/2)phi(x+log n), x>b,
    c_b=t(b)/psi(b), T(x)=1_(x>b)[t(x)-c_b psi(x)].       (1)

Extend T oddly. The complete W row and complete future integer sum are
retained. The exact nonzero seed is specified in SOURCE_DEFINITION.md; no
complement-wide sign is used in this certificate. The subtraction in (1) is a lawful original neutral
TAIL gauge; it preserves S0, not the seed mass projection.

The claimed component, subject to the independently replayed certificate
below, is

    <T,a(D)T>_L2(R) > 3*10^(-9),
    a(w)=Re digamma(1/4+iw/2)-log pi.                  (2)

All integrals in this note use the unnormalized transform
G(w)=integral_R exp(-iwx)T(x)dx, hence Parseval measure dw/(2pi).

## 1. A lower comparison that never estimates an omitted positive tail

The exact digamma series shows a is even and increasing on w>=0. Thus,
for any R>0 and any odd source in the logarithmic Gamma domain,

    <T,a(D)T> >= a(R)||T||_2^2
       -(1/pi)integral_0^R [a(R)-a(w)]|G(w)|^2 dw
    >= a(R)||T||_2^2 -R[a(R)-a(0)] B_R^2/pi,          (3)

provided |G(w)|<=B_R on [-R,R]. Here

    a(0)=-EulerGamma-pi/2-3log2-log pi.

For the positive wing define mu_j=integral T(x)(x-9/10)^j dx and
A_J=integral |T(x)||x-9/10|^J dx. Taylor's formula for the unit-modulus
exponential gives the exact uniform bound

    B_R=2 sum_(j=0)^(J-1)|mu_j|R^j/j! +2R^J A_J/J!.   (4)

The phase exp(9iw/10) has modulus one. This estimates the complete odd
transform; it does not impose a zero moment on the source. We use R=24,
J=10. Every moment in (4) is enclosed, not replaced by zero.

## 2. Stable density jets and a sharp complex-disc bound

The exact convergent series is

    u(A+s)=s^nu sum_(n>=0)(-1)^n D_n s^n/Gamma(n+nu+1),
    D_0=1, D_1=A+m,
    (n+1)D_(n+1)=(n+A+m)D_n-A D_(n-1).               (5)

The positive D_n formula and decreasing complete-tail ratio are proved in
[the validated series interface](FILTERED_COMPLEMENT_VALIDATED_SERIES_INTERFACE.md).
The evaluator retains 601 terms, enclosing the whole remaining series
and its first two derivatives by that ratio. Subsequent Taylor jets use

    s u'''+(s+2-nu)u''+(m-nu+1+A)u'+Au=0.             (6)

This follows either coefficientwise from (5) or by inverting
rho^2(rho+1)L'=[-(nu+1)rho^2+(m-nu-1+A)rho+A]L.
It is an identity for s>0 and requires no unsupported derivative trace
at zero. If u(A+s+v)=sum c_j v^j, then

    c_(j+3)=-[(j+2)(j+1)(s+j+2-nu)c_(j+2)
             +(j+1)(j+m-nu+1+A)c_(j+1)+A c_j]
                         /[s(j+3)(j+2)(j+1)].        (7)

For |w-s|<=r<s, the Poisson integral for J_nu and the positive real branch
of sqrt imply

    |g(w)| <= (s+r)^nu/Gamma(nu+1)
                         *exp(sqrt(A)r/sqrt(s-r)).

Indeed 2|Im sqrt(w)|<=r/sqrt(s-r). Integrating the finite stable
convolution along v=t w, its j-th absolute exponential moment is at most
[(s+r)/(s-r)]^j. Consequently

    |u(A+w)| <= (s+r)^nu/Gamma(nu+1)
       *exp(sqrt(A)r/sqrt(s-r))*[1+(s+r)/(s-r)]^m.     (8)

The evaluator chooses r<=s/2. This avoids an uncontrolled absolute-series
majorant on long positive-real intervals.

## 3. Complete integer row and validated Taylor integration

Between its integer knots, write the COMPLETE row in z coordinates as

    W(x(z))=(z/pi)^(1/4)
       sum_(2<=n<=sqrt(z/pi)) (1/n)
       sum_(k>=1)c(k^2 z/n^2)exp(-k^2 z/n^2).         (9)

The integration interval [16.001,128] is split at every knot pi n^2.
The evaluator uses k<=12 and encloses every omitted Taylor coefficient
of orders 0,...,24 by 10^(-90). Here is a direct bound for that enclosure.
For center z in a fixed branch, 16<=z<=128, n<=6, and |w-z|<=3/4,
Re(w)/n^2>2 and |w|/n^2<33. Hence the absolute omitted row is bounded by

    2^22 sum_(k>=13) k^6 exp(-2k^2) <10^(-130).

Its successive-term ratio is below 1/2. Cauchy on radius 1/4 shows that
each omitted coefficient through order 24 is less than
4^24*10^(-130)<10^(-90). The corresponding differentiated row has the
same elementary bound with k^8 and a larger power of two, still below
10^(-90). Thus no theta row is silently truncated.

On each branch the code bounds |W(w)-W(z)| by r D_W, where D_W is the
complete absolute first-derivative row, and insists r D_W<W(z)/2.
Together with (8) this gives an explicit analytic majorant M_F for F on
the disc. For a real cell of half-width h<=r/4, the degree-24 Taylor
remainder is at most

    M_F (h/r)^25/[1-h/r].                            (10)

The same argument applies directly to F(z)(log(z/pi)/2-9/10)^j and to
4z F(z)^2. The latter is exactly the FULL-ODD source mass density:
2 integral phi(x)^2 dx=integral 4z F(z)^2 dz.
Even Taylor coefficients are integrated exactly. For the absolute tenth
moment, the sum of absolute scaled coefficients plus (10) is an upper
pointwise bound, integrated over the cell. All binary float exports are
rounded outward with nextafter; interval calculations use 90 decimal
places. Adaptive subdivision changes efficiency, not the validity of
any cell enclosure.

The same evaluator gives the complete future-prefix bounds. If E=t-phi,
then Cauchy with sum_(n>=2)n^(-2)<1 and complete prefix summation give

    ||E||_L1(b,infinity)
       <=sqrt2*pi^(-1/4) integral_(16pi)^infinity z^(1/4)|F(z)| dz,
    2||E||_L2(b,infinity)^2
       <=(1/pi) integral_(16pi)^infinity z^2 F(z)^2 dz. (11)

For z<=128, every shifted source argument in the prefix lies between b
and log(sqrt(128/pi)); hence |x-9/10|<1. The L1 bound also pays all prefix
moment corrections through order 10.

## 4. The three remaining absolute tails and the exact trace gauge

On 0<s<.001, the complete row satisfies W>=1. The absolute series bound
gives

    integral_16^16.001 |F(z)| dz <2*10^(-13),
    |x(z)-9/10|<1/10.                                (12)

Thus its j-th moment correction is at most 2*10^(-13-j).
Its contribution to the mass lower bound may simply be omitted.

For z>=128, choose n=floor(sqrt(z/(4pi)))>=3. Then
log2<=x(z)-log n<=log3. Since c(w)>=5w^3 for w>=12 and w^3 exp(-w)
is decreasing there,

    psi(v)>=5(9pi)^3 exp(-9pi)>10^(-8), log2<=v<=log3.

It follows from this ONE retained row that W>=10^(-8)z^(-1/4).
The real Poisson/stable-convolution bound |u(A+s)|<=64s^(9/4)/Gamma(13/4)
then yields |F(z)|<=10^11 z^(11/2)exp(-z). Elementary incomplete-gamma
bounds pay all moment and L1-prefix tails by 10^(-25), and the full-odd
L2-prefix tail by 10^(-58). The checker verifies the larger moment bound
using exponent 33/4. These constants deliberately exceed the actual
Gaussian tails by large margins.

The trace t(b) is evaluated with the exact n=2,3 terms. The n>=4 series
is bounded by twice its n=4 absolute envelope, using the same W bound;
its ratio is less than 1/2 and its total is below 10^(-60). The resulting
interval proves |c_b|<6*10^(-16). Finally, for 0<=j<=10,

    integral_b^infinity psi(x)|x-9/10|^j dx <10,
    ||psi_o 1_(|x|>b)||_2 <1.                        (13)

For example |x-9/10|<=z^(1/4). The COMPLETE theta row obeys
psi(x)<=16*pi^(-1/4)z^(13/4)exp(-z) for z>=4pi>12:
use c(k^2 z)<=8k^6 z^3 and sum_(k>=2)k^6 exp[-(k^2-1)z]<1.
This reduces (13) to the elementary incomplete-gamma bounds explicitly
checked in the final arithmetic script (moment bound below 8.18 and
full-odd mass bound below .0031). Thus all changed neutral-gauge moments,
source mass and pole are retained; no small coefficient is discarded.

## 4.1 The same certified lower bound for the UNCORRECTED source

The augmented Schur certificate uses t, not the optional trace-repaired T.
No comparison of two unbounded Gamma energies is needed to transfer the
lower bound. Let B_* and m_* denote exactly the Fourier-bound and square-root
mass quantities used by the checker:

    B_* = the right side of (4), with +10|c_b| in each moment bound,
    m_* = sqrt(main full-odd mass lower)-sqrt(prefix L2 upper)-|c_b|.

The checker proves m_*>0 and a(24)>0. The very same triangle estimates
without the gauge terms give, for the odd extension t_o of the uncorrected t,

    sup_(|w|<=24)|hat(t_o)(w)| <= B_*,
    ||t_o||_2 >= sqrt(main full-odd mass lower)-sqrt(prefix L2 upper)
                >= m_*.

Indeed every gauge term in B_* is an added nonnegative allowance, and the
-|c_b| in m_* is a conservative decrease. Applying (3) DIRECTLY to t_o,
with a(24)>0 and a(24)-a(0)>0, therefore gives

    <t_o,a(D)t_o> >= a(24)m_*^2
       -(24/pi)[a(24)-a(0)]B_*^2 > 3*10^(-9).

This is exactly the same outward interval expression used for T; it is not
a gauge-invariance assertion for the Gamma component. In particular the
uncorrected source in the mixed columns, prime/pole debit, and augmented
Schur matrix satisfies this bound with no representative change.

## 5. Reproduction and the still-unpaid terms

Run, in this directory:

    python certify_filtered_bessel_moments.py --stop 128 \
      --out filtered_bessel_main_moments.json
    python certify_filtered_bessel_moments.py --prefix-only --stop 128 \
      --out filtered_bessel_prefix_moments.json
    python check_filtered_bessel_gamma_floor.py

The JSON files are generated interval results, not substituted for the
proof or its fresh reproduction. The final script uses (3)-(13) and the
already certified digamma evaluator from the published original-head
kernel. It must finish with the asserted lower bound (2).

The current approximate enclosed lower value is 3.396*10^(-9). This is
not q0[T] and not S0[T]. In particular the original reflected/forward
arithmetic, full pole and complete head Schur penalty have not been
made favorable by (2). Their separate common-source enclosure remains
necessary before this becomes a signed quotient test.
