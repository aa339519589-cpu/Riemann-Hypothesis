# The actual Green source: physical L2 range and a signed mixed crossing

For the original positive-depth Green source, the complete causal load has
an ordinary physical L2, self-Fourier completion with its constant channel
retained. A trace- and mean-repaired selfdual test then gives a strictly
negative **mixed** crossing. This does not prove a negative crossing
quadratic, exclude the actual source, or establish RH. All statements
concern this same original source, not an eigenstate in a changed mass
space.

## 0. Source forms, arithmetic operators and dependencies

All fields below are real; the complex form is obtained by conjugate-first
polarization. Write d_n=log n, alpha_n=Lambda(n)/sqrt(n), retaining every
prime power. On the positive logarithmic half-line put

    B(x)=exp(x/2-pi exp(2x)),
    xi=-(partial_x^3-partial_x/4)B,
    (Cf)(x)=sum_(n>=1)n^(-1/2)f(x+log n), psi=C xi,
    F_+f(x)=sum_n alpha_n f(x+d_n),
    F_-f(x)=sum_(d_n<x)alpha_n f(x-d_n),
    F_rf(x)=sum_(d_n>x)alpha_n f(d_n-x),
    L=F_r psi, V=L/psi, ell(f)=int_0^infinity sinh(x/2)f(x)dx.

The theta source psi is positive on x>0 and has a simple zero at0. Its
extension to the full log line is odd. Let f_o denote the odd extension of
a half-line source f and use the log Fourier convention
fhat_o(t)=int_R f_o(x)exp(itx)dx. The complete original source form is

    q0[f]=(1/(2pi))int_R a(t)|fhat_o(t)|^2dt
       -2 sum_n alpha_n int_R f_o(x)f_o(x+d_n)dx
       -2|int_R sinh(x/2)f_o(x)dx|^2,
    a(t)=Re digamma(1/4+it/2)-log pi.

Thus its half-line pole is exactly -8 ell(f)^2. The accompanying original
reflection form, and the positive-depth form, are

    N[f]=2int_0^infinity V(x)f(x)^2dx
       -2sum_n alpha_n int_0^(d_n) f(x)f(d_n-x)dx,
    P[f]=q0[f]+N[f], Q_delta[f]=q0[f]+delta N[f].

Here P[f] is source shorthand for the original ratio energy P[f/psi],
and likewise for N. These forms use their original completion, not a
replacement unweighted source domain. If f=psi r, the signed density is
Wf=Lr-F_rf, with N(f,z)=2int Wf z whenever the full pairing is legal.
The positive-wing source operator is

    T=(a(D) acting on f_o)|_(x>0)-F_+-F_-+F_r,
    q0(f,z)=2int_0^infinity [Tf-4ell(f)sinh(x/2)]z(x)dx.

The exact form and theta identities are established in the
[original source form](../20261012_localized_odd_schur/SOURCE_FORM.md)
and its linked complete foundation. An actual source in this report
means a nonzero pole-centered scalar Green source g=psi r at fixed
0<delta<1, with Q_delta(g,z)=0 for all original-form tests z. In
particular ell(g)=0, Tg=-delta Wg, and
P[g]=(1-delta)N[g]. Its existence and domain are those of the
[published actual source realization](../20261013_supercritical_source_tails/REPORT.md),
not an additional existence assertion here. The fixed-depth source
regularity and complete load estimates used below are the
[origin transmission theorem](../20261014_actual_origin_transmission/REPORT.md)
and the [actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md).
No constant is claimed uniform as delta decreases to zero.

## 1. Exact old-state inputs and normalization

Let g=psi r be a real, pole-centered actual source of fixed depth delta>0,
with original source equation T g=-delta Wg, where

    Wg=L r-F_r g,
    L(x)=sum_(log n>x) Lambda(n)/sqrt(n) psi(log n-x).

The complete origin transmission and plateau arguments prove

    Wg(0)=0,
    w(x)=exp(-x/2)Wg(x) in H^s(0,infinity), every s<1,
    ||w||_(H^s)<=C_(delta,s)sqrt(P[g]).             (1)

See Sections 2–3 of the
[origin transmission theorem](../20261014_actual_origin_transmission/REPORT.md)
and Section 1 of the
[actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md).
Here (1) is the regularity of the WHOLE signed load, not of a separately
zero-extended nonzero-trace prime or Gamma term.

The original neutral identities imply

    integral_0^infinity Wg(x) psi^(2j)(x) dx=0,
                                      every integer j>=0.             (2)

Indeed the centered neutral jets are psi^(2j)-4^(-j)psi. The actual
stationarity equation gives their N-orthogonality, and N(g,psi)=0 since
psi is the constant-ratio null direction. The exact polarized identity
is N(g,z)=2 integral Wg z. All these integrals are absolutely theta-paid. For completeness, the exact
identity Tpsi=sinh(x/2)/2 and ell(psi)=1/8 imply the original neutral
identity for psi and for every psi^(2j)-4^(-j)psi: commute full-line
even derivatives through T and integrate the pole moment by parts. The
theta tails pay those operations. These jets belong to the original form
domain, so actual stationarity gives (2).

Put, with an even extension in the physical variable u,

    w_phys(u)=w(log|u|) for |u|>=1, and 0 for |u|<1,
    G(u)=sum_(n>=1) n^(-1) w_phys(u/n).                (3)

Every sum in (3) is locally finite. Equivalently, for u>=1,

    G(u)=u^(-1/2) sum_(n<=u)n^(-1/2)Wg(log u-log n).

Thus (3) is exactly the complete causal Euler adjoint of the SAME Wg.
For any s>1/2 in (1), Sobolev embedding gives bounded w and therefore
|G(u)|<=C(1+log(2+|u|)). In particular G is a genuine tempered function,
zero on (-1,1), not merely a formal critical-line inverse.

## 2. The physical homogeneous Sobolev estimate

For every 1/2<s<1,

    [w_phys]_(dot H^s(R))<=C_s||w||_(H^s(0,infinity)),
    [G]_(dot H^s(R))<=zeta(s+1/2)[w_phys]_(dot H^s(R)). (4)

Use the Gagliardo seminorm, defined modulo constants. For u=e^x and
v=e^y with x>=y>=0, its same-wing measure is exactly

    du dv/|u-v|^(1+2s)
      =exp((1-2s)y) exp(x-y)/(exp(x-y)-1)^(1+2s) dx dy.

The first factor is at most one. The remaining kernel is bounded by
C_s|x-y|^(-1-2s) for |x-y|<=1 and by C_s exp(-2s|x-y|) otherwise.
The same-wing contribution is consequently bounded by the H^s norm
of w. The opposite-wing kernel uses exp(x-y)+1 instead; it is bounded
near x=y and exponentially decaying at infinity, and is paid by ||w||_2.
The interaction with |u|<1 is bounded near the endpoint by

    C_s integral_0^1 |w(x)|^2 x^(-2s) dx.

This is finite with norm control by the zero-trace fractional Hardy
inequality for H^s(0,infinity), 1/2<s<1. Away from that endpoint the
factor exp((1-2s)x) is bounded, so ordinary log-variable L2 pays it.
This proves the first assertion of (4), including the actual wall.

For every n the exact dilation scaling is

    [n^(-1) w_phys(./n)]_(dot H^s)
                   =n^(-s-1/2)[w_phys]_(dot H^s).

Minkowski proves (4) for each finite partial sum. Local stabilization
of (3), followed by Fatou in the double integral, proves the complete
bound. No claim that the individual summands are in ordinary physical
L2 is used.

## 3. The complete Gaussian ladder retains exactly one pole constant

Let B(x)=exp(x/2)exp(-pi exp(2x)) and
xi=-(partial_x^3-partial_x/4)B, so psi=C xi. Absolute theta decay and
the log growth of G justify the complete adjoint pairing in (2), giving

    integral_1^infinity G(u) kappa_(xi^(2j))(u)du=0,

where kappa_f(u)=u^(-1/2)f(log u). Define

    H_B(t)=exp(t/2) integral_1^infinity
                         G(u)exp(-pi exp(2t)u^2)du.

This is holomorphic in |Im t|<pi/4. The last orthogonality says
H_B^(2j+3)(0)=H_B^(2j+1)(0)/4. Therefore

    H_B(t)-H_B(-t)=c sinh(t/2),
    c=4H_B'(0)
     =4 integral_1^infinity G(u)(1/2-2pi u^2)exp(-pi u^2)du. (5)

The identity continues along the real axis. Gaussian Fourier
transformation and uniqueness of even tempered distributions give,
with Fourier kernel exp(-2pi iuv),

    G-Fourier(G)=c(delta_0-1).                         (6)

The distributional uniqueness step is elementary here. If an even tempered
distribution annihilates all exp(-pi rho u^2), rho>0, differentiation in
rho shows that it annihilates every even monomial times a fixed Gaussian.
Its convolution with that Gaussian is entire, by the Schwartz-seminorm
bounds for complex Gaussian translates, and all derivatives at0 vanish.
The convolution is therefore zero. Fourier transformation and the
nonvanishing Gaussian multiplier force the distribution to be zero.
Apply this to the difference between the two sides of (6).

## 4. The actual zero trace upgrades (6) to ordinary physical L2

Set H=G+c as a tempered function. Then (6) gives Fourier(H)=H.
More strongly, for every 1/2<s<1,

    integral_R |u|^(2s)|H(u)|^2du
                         <=C_s [G]_(dot H^s)^2<infinity.              (7)

To avoid multiplying a Dirac mass by a nonsmooth fractional power,
prove (7) with ordinary translations. For almost every h, the finite
Gagliardo seminorm gives Delta_h G in L2. Its Fourier transform is

    (exp(2pi i h u)-1) Fourier(G)
       =(exp(2pi i h u)-1)(G+c),

because the multiplier annihilates delta_0. This distribution is thus
an L2 function and Plancherel applies. Integrate its squared norm against
|h|^(-1-2s)dh and use Tonelli. The inner integral is the positive finite
constant C_s' times |u|^(2s), proving (7).

On (-1,1), H is precisely the constant c. Combining that local fact
with (7) proves H in L2(R). Consequently the exact conclusion is

    H=Fourier(H) in L2(R),
    H(u)=c on |u|<1,
    |u|^s H in L2(R), every 1/2<s<1.                  (8)

In particular H also belongs to ordinary H^s(R), by Fourier symmetry.
The constant c is not zero by this argument. This is a constant-head
extended Sonine field, not a gap2 vector and not necessarily a gap1
zero-head vector. It is a transform of Wg, not of g or its future
Mobius seed. Equations (3), (6), and (8) preserve every pole term.

## 5. The same-source pairing that is licensed

For a smooth theta-tailed physical test v on u>=1, put
phi(x)=exp(x/2)v(exp x), x>=0, and Cphi(x)=sum n^(-1/2)phi(x+log n).
Absolute theta decay gives the exact identity

    integral_0^infinity Wg(x) Cphi(x)dx
                       =integral_1^infinity G(u)v(u)du
                       =integral_1^infinity H(u)v(u)du-c integral_1^infinity v(u)du. (9)

This is also valid under any other explicit absolute pairing bounds.
It does not assert that arbitrary physical L2 tests have original-P
Euler images. In particular (8) supplies a legitimate same-Wg Fourier
constraint for finite parity commutators, but not positivity of their
complete clipped Gamma/prime row or the original Phi-ground critical gap.

## 6. A direct same-load test with an exact positive pairing

There is a concrete lawful mixed test, but this is NOT a nonnegative
crossing estimate. Write gamma(u)=exp(-pi u^2) and

    h=H-c gamma.

It is self-Fourier, h(0)=integral_R h=0. Indeed (8), with s>1/2,
implies H in L1 as well as H^s, so Fourier continuity gives integral H=c.
Since H=c on (-1,1), integral_1^infinity H=-c/2. Hence the exact pairing

    I=integral_1^infinity G h
      =||H_tail||_2^2+c^2/2-c<H_tail,gamma_tail>
                                       +c^2 integral_1^infinity gamma
      =N_half/2+||h_tail||_2^2/2
                  +c^2 integral_1^infinity (gamma-gamma^2/2)
      >=N_half/2,                                    (10)

where N_half=integral_0^infinity H^2. This retains the full constant
channel. For nonzero actual g, H is nonzero: otherwise G is constant
and its unit gap makes c=G=0; the locally finite causal inverse gives
Wg=0, whence N[g]=0 and actual P[g]=(1-delta)N[g]=0. Pole centering
then excludes the remaining constant-ratio null source.

One need not assume an original-P norm for C U h to use (10). Take
H_t=exp(-t L_osc)H, L_osc=-partial_u^2+4pi^2 u^2, and set

    c_t=H_t(0), h_t=H_t-c_t gamma, E_t=C U h_t,
    U h_t(x)=exp(x/2)h_t(exp x).

The oscillator commutes with the unitary Fourier transform. Its heat
maps L2 into Schwartz and is strongly continuous in both H^s and
L2(<u>^(2s)du). For a direct justification of the simultaneous assertion,
its Mehler kernel factors exactly as

    exp(-t L_osc)=M_a exp(b partial_u^2) M_a,
    M_a F(u)=exp(-a u^2)F(u),
    a=pi tanh(2pi t), b=sinh(4pi t)/(4pi).

Gaussian multiplication and ordinary heat are uniformly bounded near
t=0 and strongly continuous in both displayed norms, by the fractional
product inequality, weighted convolution, and compact-smooth density.
Consequently c_t->c, h_t->h in L2 and L1. Every h_t is self-Fourier
Schwartz with trace and integral zero. Its complete Euler source E_t
is an even-null source, with the complete even pole included.

### Complete even-null identity and the boundary normalization

The even-null assertion used above has the following direct proof, valid
for every even self-Fourier Schwartz h with h(0)=int_R h=0. Put
E(x)=exp(x/2)sum_(n>=1)h(n exp x) on the whole logarithmic line. Poisson
summation gives E(-x)=E(x), and E decays faster than every exponential
at both log ends. With M_h(s)=int_0^infinity h(u)u^(s-1)du, one has

    Ehat(s)=int_R E(x)exp[(s-1/2)x]dx=zeta(s)M_h(s).

M_h is holomorphic for Re s>-2, since h(u)=O(u^2) at0, and rapidly
decreasing on every closed vertical strip in this half-plane. Ehat is
entire by the two log tails. In particular M_h(1)=0 cancels the zeta
pole, but Ehat(1)=M_h'(1) need not vanish. For 1<Re s<3/2, transform
the full future-prime row as -zeta'(s)M_h(s), then move its inverse
contour to Re s=1/2. The pole at1 contributes Ehat(1)exp(-x/2).
The product has no pole at nontrivial zeros, including multiple zeros.
Evenness gives the past row and the complementary exp(x/2) term.
The functional equation, in logarithmic-derivative form,

    -zeta'/zeta(s)-zeta'/zeta(1-s)
      =[digamma(s/2)+digamma((1-s)/2)]/2-log pi,

therefore yields, with U_E=int_0^infinity exp(x/2)E(x)dx and
V_E=int_0^infinity exp(-x/2)E(x)dx,

    T_even E=-2(U_E+V_E)cosh(x/2).

Polynomial zeta bounds and rapid M_h decay justify the horizontal
limits. This proves the full even-null identity, including its positive
cosh pole, without a physical gap hypothesis or a zero-location assumption.

Now define the pole-completed boundary operator on x>0 by

    H_>E(x)=int_0^infinity [kappa(x+y)-exp(-(x+y)/2)]E(y)dy,
    kappa(t)=exp(-t/2)/(1-exp(-2t)),
    B_cross E=H_>E+F_rE-exp(x/2)U_E.

Changing the full source parity from even to odd contributes
2(H_kappa+F_r)E to T, where H_kappa has kernel kappa(x+y).
The odd pole is -8 sinh(x/2)ell(E), with ell(E)=(U_E-V_E)/2.
Combining these exact rows gives

    q0(f,E)=4<f,(H_kappa+F_r)E>-4(U_f U_E+V_f V_E)
           =4<f,B_cross E>.

Only the lowest Gamma Hankel kernel cancels V_f V_E. The higher Gamma
modes, all reflected prime powers and the remaining U pole are retained.
Here q0(f,E) means the mixed half-line source form with both positive
wings oddized. This is a mixed-source identity, not positivity of B_cross.

### Passage in the actual first slot

Actual first-slot stationarity extends to each E_t by ordinary source
cutoffs. Near zero, E_t is smooth bounded and the sharp odd source has
finite logarithmic Gamma form; a collar cutoff costs O(epsilon
log(1/epsilon)). The actual bound g=O(x) also makes Vg bounded there.
At infinity, E_t has rapid log decay against all complete actual rows,
which are O(exp(x/2)); all first-slot integrals converge. This extension
does not assert finite quadratic N or P for E_t. It proves

    q0(g,E_t)=-2 delta integral Wg E_t
             =-2 delta integral_1^infinity G h_t
             =4<g,B_cross E_t>.                      (11)

Here B_cross is exactly the full Gamma/reflected-prime/pole boundary
operator just defined. The last equality follows from the displayed
even-null/odd-source identity, not from a positivity assertion. Taking the
limit in the density pairing, not in an unproved P norm, gives

    lim_(t->0) 4<g,B_cross E_t>=-2 delta I
                              <=-delta N_half<0.     (12)

Thus the old actual state itself supplies a genuinely physical L2
selfdual mixed test and a strictly negative complete crossing. The
unproved step is an independent nonnegative lower bound for this SAME
mixed crossing. Equation (12) is not a negative crossing quadratic,
not a bare conductor identity, and not an exclusion theorem.
