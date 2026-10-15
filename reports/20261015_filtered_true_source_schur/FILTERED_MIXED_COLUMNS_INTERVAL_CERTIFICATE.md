# Complete outward mixed columns for the filtered true source

## Scope and same source

Use A=16,k=3, b=log2 and the exact main phi of
[FILTERED_TRUE_SOURCE_GAMMA_LOWER_CERTIFICATE.md](FILTERED_TRUE_SOURCE_GAMMA_LOWER_CERTIFICATE.md).
This certificate uses the **uncorrected** tail t=1_(x>b) C phi throughout.
The optional neutral tail subtraction in the Gamma note is not performed
here. Its passed lower bound remains valid for t: removing that subtraction
only reduces each conservative absolute moment correction and increases
the conservative norm lower bound in its final arithmetic.

Let e_j(x)=sqrt(2/b)sin(omega_j x), omega_j=j*pi/b, on (0,b). The entries
certified here are the COMPLETE original mixed form

    f_j=q0(e_j,t).                                                 (1)

The original forward/reflected prime rows and full pole are retained.
The main phi contribution is evaluated directly. E=C phi-phi is paid by
a complete L2 force estimate, including its possible nonzero split trace.
No BV assertion for the complete t force is used.

## 1. Exact main-source formulas

Put lambda_r=2r+1/2, sigma_j=(-1)^j and

    A_r=integral phi(y)[exp(-lambda_r(y-b))-exp(-lambda_r(y+b))]dy.

Direct integration against e_j gives

    f_j^Gamma=2sqrt(2/b) sigma_j omega_j
                         sum_(r>=0) A_r/(lambda_r^2+omega_j^2),
    f_j^prime=-2sqrt(2/b) sum_(n>=2) alpha_n
        integral_(log n-b)^(log n+b) phi(y)sin(omega_j(y-log n))dy,
    f_j^pole=-8 ell(phi) ell_j,
    ell_j=-sqrt(2/b) sigma_j omega_j sinh(b/2)/(omega_j^2+1/4).      (2)

These signs follow from the original mixed kernel, not from an absolute
prime bound. The source is zero below x_A=log(16/pi)/2>b.
Only prime powers n<=12 meet the evaluated region z<=128. The omitted
prime powers are handled by the full far envelope below.

## 2. Outward analytic integration, not a floating-error allowance

The main and additional onset cells are precisely those of
[FILTERED_MAIN_FORCE_VARIATION.md](FILTERED_MAIN_FORCE_VARIATION.md).
On each cell, source coefficients and the complete analytic remainder
are already outward intervals. On a subcell write z=z_c+h v and
F_0(z)=sum_(r=0)^24 p_r v^r+error. The power-kernel integrals use

    V_k=sum_(r+k even) 2p_r/(r+k+1),
    integral F_0(z)(z/pi)^a dz
       =h(z_c/pi)^a sum_(k>=0) binomial(a,k)(h/z_c)^k V_k.          (3)

The polynomial is re-centered by interval Horner arithmetic. All integer
prime cuts are intersected with the source cell as outward intervals.
The finite sum uses K=64; kernel-only subdivision ensures

    |a| beta/(1-beta)<5, beta=h/z_c.

If c_K=binomial(a,K)beta^K, the complete coefficient tail is bounded by

    |c_K| (|a|+K)beta/(K+1) / (1-q),
    q=max(beta,(|a|+K+1)beta/(K+2))<1.                            (4)

Multiply this by2 sum|p_r| for the absolute integration tail. The original
source remainder is also integrated: its real-axis kernel multiplier is
bounded by1 for prime phases,256 times the center prefactor for Gamma,
and2 for the pole powers. The first uses unit modulus, the second exp(5)<256,
and the last |a|=1/4. Neither source nor kernel Taylor remainder is dropped.

`interval_array_kernel.py` uses binary64 endpoint intervals with every
arithmetic endpoint widened using nextafter. Product extrema use all four
endpoint products. Sine/cosine use verified pi/2 range reduction followed
by Taylor polynomials through degrees21/22 on |v|<.8; their full remainder
is bounded by10^-23. The exponential uses verified log2 range reduction
to -.01<v<.71 and its degree25 polynomial, with remainder10^-28, followed
by binary ldexp. The interval pi and log2 constants and scalar logarithms
are obtained from mpmath interval arithmetic. Thus no platform libm
trigonometric value or guessed floating-roundoff allowance is an enclosure.
Range-reduction indices may be chosen in floating arithmetic, because the
resulting reduced INTERVAL is then explicitly verified. Bounds used only
to choose subdivisions have the same status: (4) and the actual kernel
condition are verified afterward by outward arithmetic.

A tiny uncertain intersection can straddle an exact prime-window endpoint.
Only this unit-modulus prime-phase case uses the width times the uniform
source bound .01. The remainder checker explicitly verifies that bound on
EVERY doubled source cell: sum |p_j|(2h)^j+2^26 e<.01. The analytic-disc
ratio <=1/4 makes the doubled-cell remainder inflation valid. These
intersections have outward width below2*10^-12; their whole mass is kept.

The interval-array primitive and all positive compound bounds direct each
individual arithmetic operation. The numerical certificate assumes ordinary
IEEE754 binary64 elementary NumPy arithmetic, without flush-to-zero mode.
Subnormal endpoints are covered by nextafter as well.

## 3. Complete future-prefix force error

Use the weighted norm ||E||_(2,e)=||exp(x)E(x)||_(L2(b,infinity)).
The already validated prefix certificate gives a full-odd main squared
norm less than5.8*10^-35. Its source labels have z<=128, so the observed
variable also has exp(2x)<=128/pi. For the omitted far source, Cauchy with
sum_(n>=2)n^-2<1 and the exact prefix change of variable gives

    2||exp(x)E_far||_2^2
       <=2 integral exp(2y)phi_far(y)^2
                         sum_(2<=n<=exp(y-b))1/n dy
       <=(2/pi) integral_128^infinity z^3 F_0(z)^2 dz.             (5)

Here sum_(n=2)^N 1/n<=log N<=y and y<=z/2. The complete Gaussian envelope
|F_0(z)|<=C_F z^(11/2)exp(-z), C_F=8*64*10^8/Gamma(13/4),
therefore bounds (5) by10^-55. Triangle inequality yields

    ||E||_(2,e)<5*10^-17.                                        (6)

The full mixed-force map from such an E to L2(0,b) has norm less than100:

* The Gamma cross operator has norm at most pi+sqrt2. Indeed
  kappa(s)<=exp(-s/2)[1+1/(2s)], and the singular cross term is the
  Carleman operator; the regular cross term is rank one. The odd reflected
  subtraction only decreases the positive absolute kernel.
* The complete prime map has norm at most6A, A=sum Lambda(n)/n^(3/2)<5.
  The forward windows cost2A; reflected windows cost4A since exp(b)=2.
  These are complete weighted translation estimates, not truncated primes.
* The full pole is rank one and has norm less than10. In fact its tail
  weight integral is integral_b^infinity exp(-2y)sinh(y/2)^2dy=7/96.

Thus the entire E force has L2 norm less than5*10^-15. It is paid ONCE
in the infinite augmented-column estimate by its complete squared norm,
not by summing a per-column constant over infinitely many indices.

## 4. Other omitted terms in the finite columns

Below z=16.00001 the complete disc estimate gives
|F_0(16+s)|<=.004 s^(9/4), so its L1 mass is less than10^-19.
Its Gamma kernel stays separated by x_A-b>0, and the finite prime/pole
rows have bounded normalized sine tests. The total omitted onset
coefficient is less than10^-17, uniformly in j.

Above z=128, the complete prime window satisfies
2 sum_(n<=2exp(y))alpha_n<=z, as proved in the variation note. The
Gaussian envelope bounds ALL omitted arithmetic, Gamma and pole
coefficients together by100 integral_128^infinity z|F_0(z)|dz<10^-20.
The r>=200 Gamma series is bounded geometrically using

    |A_r|<=1.2*10^-5 exp[-lambda_r(x_A-b)],
    omega/(lambda_r^2+omega^2)<=1/(2lambda_r).

Its whole omitted coefficient is less than10^-20. These estimates are
uniform over every sine frequency, not just the finite4096 under test.

`check_filtered_mixed_absolute_remainders.py` verifies all numerical
inequalities in (5)-(6) and this section by directed interval arithmetic.
Their sum, including the complete future force error, is less than10^-14.
Accordingly `certify_filtered_mixed_columns.py` inflates EACH of its4096
finite intervals by10^-14 after summing the exact main Gamma, prime and
pole contributions. This finite coefficient inflation is distinct from
the complete L2 error used for the infinite column tail.

## 5. Reproduction and limitations

Regenerate the main and prefix moments/cells with the Gamma certificate,
then run

    python certify_filtered_bessel_onset_cells.py
    python check_filtered_mixed_absolute_remainders.py
    python certify_filtered_mixed_columns.py --N 4096

The generated JSON `filtered_mixed_columns_intervals.json` contains outward
intervals, not midpoint diagnostics. Its complete finite columns must still
be combined with the certified F(b), variation(2), and the original-head
structured infinite-column estimate. This note alone makes no signed
claim for S0 or for any larger family of sources.
