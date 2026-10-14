# Depth-uniform Sobolev control of individual supercritical odd Green sources

For an actual pole-centered scalar eigen-source of the complete odd Green map, normalized by ||g/mu||_(L2(0,infinity))=1, this report proves ||g_odd||_(H^s)<=C_s for every s<1/16, with constants independent of its supercritical depth. The stronger high-frequency estimate (9.10) retains the depth factor in its leading term. The proof uses a legal compact-propagation Poisson test, the complete reflected operator, the original ratio-core closure, and every prime/Gamma term.

The result concerns each individual scalar eigen-source. It is not a whole-band estimate, a small covariance-defect theorem, a coefficient-one Green comparison, or an RH proof.

## Dependencies and normalization

The complete theta kernel, Fourier convention, Gamma multiplier and bounded physical prime perturbation are from [the original form foundation](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1ce3543ac2d9077573dbdf397b8007dc34bc5349/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). The actual P and N gradient completions and compact-core identity are from [the reflected-prime energy report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1ce3543ac2d9077573dbdf397b8007dc34bc5349/reports/20261013_reflected_prime_energy/REPORT.md). The scalar source equation, complete bounded normalized prime operators and the precise delta^-2 tail used below are from [the supercritical source-tail theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1ce3543ac2d9077573dbdf397b8007dc34bc5349/reports/20261013_supercritical_source_tails/REPORT.md). The parity-preserving physical closed form and coefficient-two pole are specified in [the odd operator-domain report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1ce3543ac2d9077573dbdf397b8007dc34bc5349/reports/20261013_odd_operator_domains/REPORT.md).

These dependencies supply the actual eigen-source and its tail, not the new smoothing or Sobolev conclusion. The complete new argument is below. All inner products are conjugate-linear in their first slot.

## 1. Fixed objects and the conclusion being checked

Use the complete odd Green realization from the linked source-tail theorem, with

    psi=-Phi' on (0,infinity),
    L(x)=sum_(log n>x) alpha_n psi(log n-x), alpha_n=Lambda(n)/sqrt(n),
    mu^2=psi/L, d_n=log n,
    (R v)(x)=sum_n alpha_n mu(x)mu(d_n-x)1_(0,d_n)(x)v(d_n-x),
    H=I-R >=0.

The bounded operator H here is ONLY on ordinary L2(0,infinity). The full
reflected energy, with the conventions of the linked reflected-prime report, is

    N[r]=2<v,Hv>, v=psi r/mu.                           (1.1)

In particular A_N[g]:=<g/mu,Hg/mu>=N[g/psi]/2. This notation
must not be confused with the full signed source form h=P-N.
All prime powers occur in R. The source form and Gamma form remain the
original complete forms.

Let r be an actual pole-centered supercritical Green eigen-source with
N(r,z)=lambda P(r,z), lambda>1, and delta=(lambda-1)/lambda. Set g=psi r
and normalize ||v||_2=1. Inputs from the original source-tail theorem are

    V(X):=int_X^infinity |v|^2 <= C delta^-2 exp(9X-pi exp(2X)),  (1.2)
    ||g||_2^2+q_b[g_odd] <= C,
    mu^2/m^2 <= C exp(3x), m^2=Phi/(2cosh(x/2)).             (1.3)

Here g_odd denotes odd extension and the Fourier convention is
hat f(xi)=integral f(x)exp(i xi x)dx. Explicitly,

    q_b[f]=(2pi)^-1 int b(xi)|hat f(xi)|^2 dxi,
    b(xi)=sum_(j>=0) (xi/2)^2 /
          [(j+1/4)((j+1/4)^2+(xi/2)^2)] >=0,
    C_0=EulerGamma+pi/2+3log(2)+log(pi),
    h[f]=q_b[f]-C_0||f||_2^2
         -2sum_(n>=2)alpha_n Re<f,tau_(d_n)f>
         -2|int sinh(x/2)f(x)dx|^2.

The full source expression is interpreted through the linked original closed
physical form, not as a globally bounded unweighted operator. The bounded
normalized prime terms, ||mu v||<=||mu||_infinity, and h[g]=-delta N[r]
give the uniform log-form budget in (1.3). Its last weight comparison follows
from mu^2/m^2=2cosh(x/2)psi/(Phi L), psi/Phi<=C exp(2x), and
L>=c exp(-x/2); near zero the quotient is O(x).

The supercritical equation on the ACTUAL P completion is

    h(g,k)=-delta N(g/psi,k/psi).                          (1.4)

Fix a smooth even cutoff chi, nonincreasing on [0,infinity), equal to one
on [-1,1], zero outside [-2,2]. Define the whole-line even convolution C by

    k_t^a(h)= t/[pi(t^2+h^2)] chi(h/a), 0<t<=a,
    (C g)_odd=k_t^a*g_odd.

On the positive half-line C has Dirichlet kernel

    K(x,y)=k_t^a(x-y)-k_t^a(x+y)>=0.                       (1.5)

Its propagation is at most 2a, its L2 norm is at most one, and its mass
is at most one. The claimed complete covariance and mixed bounds are

    A_N[Cg] <= A_N[g]+C(e_0+T_delta+T_delta^2),
    Re A_N(g,C^2g) <= A_N[g]+C(e_0+T_delta),               (1.6)

where every vector in these displays has its actual source interpretation,
C g/psi and C^2g/psi lie in the original ratio-core P closure, and

    e_0 = epsilon + sqrt(eta),
    epsilon = C exp(2aK_R)[t/a + K_R t log(1+a/t)],
    eta = C_beta[ sqrt(b)+t^beta
              +exp(2aK_R)(K_R+b^-1)t log(1+a/t)],          (1.7)
    T_delta(R,a) <= C delta^-1 exp(CR-c exp(2R)).

Here 0<beta<1/2, b<log(2)/4, 2a<b/2, aK_R<=1, a is below one
fixed sufficiently small constant, and R exceeds a fixed sufficiently
large constant. K_R<=C exp(2R). The constants do not depend on the source
or delta. The t^beta term uses the COMPLETE reflected coefficient Fourier moment proved in Section 4. T applies to propagation
4a as well as 2a after adjusting its fixed constants.

These are signed upper bounds. Their errors vanish under the compatible
limiting parameters specified below. They do not say A_N[Cg]<=A_N[g]
exactly, and the two upper bounds CANNOT be subtracted to bound the defect
A_N[Cg]-Re A_N(g,C^2g). That defect has not been proved small. No full source regularity claim follows just by
renaming the bounded normalized variable v as the source g.

## 2. Endpoint-compatible quasi-contraction

Put phi(x)=log(mu(x)/sqrt(x)). The complete theta and row estimates give

    phi locally Lipschitz, |phi'(x)|<=C exp(2x) a.e.,
    phi is decreasing beyond one fixed R0.                (2.1)

Indeed L is absolutely continuous, not necessarily C1 across log n.
Its lower bound is c exp(-x/2); the complete derivative sum has upper
bound C(1+x)exp(x/2). Hence |L'/L|<=C(1+x)exp(x), whereas
psi'/psi=-2pi exp(2x)+O(1) in the far wing. At zero psi has a simple
odd zero and L(0)>0, so phi has a finite Lipschitz extension.

Choose R>=R0 and define

    phi_R(x)=phi(min(x,R)), mu_R(x)=sqrt(x)exp(phi_R(x)).

This Lipschitz extension is enough; differentiability at R is not needed.
It satisfies mu_R=mu on [0,R], mu_R>=mu everywhere, and
||phi_R'||_infinity=K_R<=C exp(2R).

Let Z=mu_R^-1 C mu_R. First the untruncated Dirichlet Poisson operator
P_t^D is contractive on L2(dx/x). Its positive symmetric kernel has
P_t^D 1<=1, and its action on the positive weight is exactly

    P_t^D(1/x)=x/(x^2+t^2)<=1/x.

Cauchy--Schwarz against its kernel and then Fubini give contraction.
Thus ||x^-1/2 P_t^D x^1/2||<=1.

The discarded smooth tail has normalized norm at most C t/a. One proof
scales a to one, writes tau=t/a, and splits x,y into comparable and
separated regions. On x/2<=y<=2x the factors sqrt(y/x) are bounded and
ordinary L1 convolution gives O(tau). On y>2x, the tail vanishes unless
y is bounded away from zero, and its radial derivative is bounded by
C tau/(1+y)^3. Odd cancellation therefore bounds the normalized kernel
by C tau sqrt(xy)/(1+y)^3. Its square integrates to O(tau^2), since
int_0^(y/2) x dx=O(y^2). The opposite separated region gives
C tau y^(3/2)/(sqrt(x)(1+x)^3), also with square integral O(tau^2).
Consequently

    ||x^-1/2 C x^1/2|| <= 1+C t/a.                       (2.2)

For conjugation by exp(phi_R), the kernel difference has extra factor
bounded by exp(2aK_R) K_R |x-y|. In the comparable region its norm is
O(exp(2aK_R)K_R t log(1+a/t)). In y>2x the derivative estimate for the
FULL smooth kernel is

    K(x,y)<=C t x y/(t^2+y^2)^2.

After multiplying sqrt(y/x)|x-y|, the squared kernel integrates to

    C t^2 int_0^(4a) y^7/(t^2+y^2)^4 dy
      <= C t^2 log(1+a/t).

The x>2y region has the same estimate. This proves

    ||Z||<=1+epsilon,                                   (2.3)

with epsilon as in (1.7). Restrict parameters so epsilon<=1. No unbounded
conjugated fractional operator is invoked.

## 3. Complete reflected endpoint removal

For b<log(2)/4 define R_b by deleting from EACH actual reflected label the
part where x<b or d_n-x<b. It remains a bounded sum of reflected operators
and satisfies

    R_b=P_(x>=b) R_b P_(x>=b),
    ||R-R_b||<=C sqrt(b).                               (3.1)

For the second bound use mu(x)<=C sqrt(x) near zero and

    sum_n alpha_n sup_(d_n-b<=y<=d_n) mu(y)<infinity.

The complete theta decay makes this series finite, uniformly for small b;
no prime label is dropped from the final error estimate.

Write E_Z=Z-C. On either side of R_b its kernel is supported where x,y>=b/2,
because propagation is 2a<b/2. The reflected part k(x+y) vanishes there.
The ordinary logarithmic derivative of mu_R is bounded by K_R+C/b.
The first-moment Schur estimate therefore gives

    ||E_Z P_(x>=b)||+||P_(x>=b)E_Z||
       <=C exp(2aK_R)(K_R+b^-1)t log(1+a/t).              (3.2)

The constant absorbs exp(Ca/b), uniformly bounded by the parameter choice.
Globally ||E_Z||<=||Z||+||C||<=3. Hence the exact decomposition

    [Z,R]=[C,R]+[E_Z,R_b]+[E_Z,R-R_b]                    (3.3)

already controls both endpoints of every reflection, including the
half-line boundary pieces that would disappear in an invalid full-line
translation-only calculation.

## 4. Complete ordinary-convolution commutator

Extend v oddly, mu evenly, and the reflected coefficients with their
negative-wing mirror. The complete coefficient fact needed here is

    sum_n int <xi>^beta |hat r_n(xi)| dxi <infinity,
    r_n(x)=alpha_n mu(x)mu(d_n-x)1_(0,d_n)(x),
    0<beta<1/2.                                         (4.1)

It follows from W^(1,p), 1<p<2: mu'=O(x^-1/2) at zero; full theta
bounds and exp(2x)+exp(2(d_n-x))>=2n give a summable polynomial in n
times exp(-pi n) bound for every coefficient W^(1,p) norm. Choose p close
enough to two and beta+1/2<s<3/2-1/p, then W^(1,p)->H^s and Fourier
Cauchy--Schwarz. Thresholds log n in L' are allowed a.e.; they must not
be described as a C1 coefficient.

For the compact Poisson multiplier c_t^a,

    |c_t^a(xi)-c_t^a(eta)|
      <=C_beta t^beta |xi-eta|^beta,                     (4.2)

because int |h|^beta k_t^a(h)dh<=C_beta t^beta. Even convolution commutes
with the full-line reflections; only the coefficient commutators remain.
Young's inequality in Fourier variables and (4.1) give

    ||[C,R]||<=C_beta t^beta.                            (4.3)

Combining (3.1)--(3.3) proves ||[Z,R]||<=eta as in (1.7).
Equivalently ||[H,Z]||<=eta.

## 5. Bounded square-root gate, including the mixed test

For bounded positive H and bounded Z, the resolvent representation gives

    ||[H^1/2,Z]||<=C sqrt(||Z|| ||[H,Z]||).               (5.1)

For completeness write H^1/2=pi^-1 int_0^infinity
s^-1/2 H(H+s)^-1 ds. The commutator integrand has norm at most
min(2||Z||,||[H,Z]||/s); splitting at s=||[H,Z]||/||Z|| proves (5.1).
No strictly positive lower bound for H is required.

Let u=H^1/2 v. Then

    H^1/2 Zv=Z u+[H^1/2,Z]v,

and (2.3), (5.1) imply

    <Zv,HZv> <= <v,Hv>+C_H(epsilon+sqrt(eta)+eta)||v||^2. (5.2)

For the source-equation test, Z need not be self-adjoint:

    Re<v,HZ^2v>
      =Re<u,Z^2u>+Re<u,[H^1/2,Z^2]v>,
    ||[H^1/2,Z^2]||<=2||Z||||[H^1/2,Z]||.

It follows that

    Re<v,HZ^2v> <= <v,Hv>+C_H(epsilon+sqrt(eta))||v||^2. (5.3)

Absorb eta into sqrt(eta) when eta<=1. These estimates are purely bounded
Hilbert-space statements. The next steps are what make them legal actual
source estimates.

## 6. True theta weight and the actual supercritical tail

Write rho=mu/mu_R<=1 and v_R=rho v. If w=mu^-1 Cg, then

    Z v_R=rho w,
    w-Zv=(1-rho)w+Z(rho-1)v.                            (6.1)

The first term is supported in x>R. For x>R and |x-y|<=2a, the complete
row/theta log derivative bound gives

    mu(y)/mu(x)<=exp(Ca exp(2y)).

Far from zero the reflected Dirichlet kernel vanishes. Cauchy--Schwarz
with the nonnegative convolution kernel, whose mass is at most one,
and then Fubini yield

    ||1_(x>R)w||^2
      <=C int_(R-2a)^infinity exp(Ca exp(2y))|v(y)|^2dy.   (6.2)

This retains the essential exp(Ca exp(2y)) factor. Stieltjes integration
against (1.2), for a below one fixed constant, proves

    RHS <=C delta^-2 exp(CR-c exp(2R)).                  (6.3)

Therefore ||w-Zv||<=T_delta(R,a). For w_2=mu^-1 C^2g the exact identity
is instead Z^2v_R=rho w_2. The same proof uses propagation 4a and mass at
most one, giving ||w_2-Z^2v||<=T_delta(R,a) with adjusted fixed constants.
Since H is bounded, (5.2)--(5.3) now give both estimates (1.6). The
quadratic energy error has the additional T_delta^2 term; the mixed error
is linear even when T_delta is large. This distinction matters below.

## 7. Actual ratio-core and full Gamma/source domain

For fixed t,a>0, k=Cg or C^2g is a smooth odd whole-line function and is in
H^1, since the convolution kernels and their derivatives are integrable.
As psi is smooth odd with a simple zero, k/psi has a smooth even extension
at zero. Section 6 and compact-region boundedness give k/mu in L2.
The same tail proof with the additional factor exp(3x), combined with
(1.3), gives k/m in physical L2. Therefore k/m belongs to the original
full physical form domain, since k in H^1 implies q_b[k]<infinity.

Let chi_j be even smooth spatial cutoffs with bounded derivative, tending
to one, and set r_j=chi_j k/psi. These are exactly the original compact
ratio-core elements. Their N differences tend to zero by

    N[r_j-r_l]<=4||(chi_j-chi_l)k/mu||^2.

Their source H^1 differences and physical L2 differences tend to zero.
The original complete h form is continuous in the corresponding form norm:
its Gamma part is bounded by H^1, and its full physical potential is bounded,
including the rank-one pole term -2|<m sinh(x/2),u>|^2. The intermediate
cutoffs need not themselves be centered.
The exact compact-core identity P=N+h thus implies

    P[r_j-r_l] -> 0.

This proves membership in the ACTUAL P core completion. It does not
identify a formal maximal domain with that completion. It retains the
complete Gamma form and both prime wings through the original closed form.

Actual g has every fixed exponential L1 moment by (1.2)--(1.3). Even
compact convolution multiplies its sinh moment by the kernel's cosh
moment, so exact pole centering is preserved. Hence k=Cg and C^2g are
legitimate centered tests in (1.4).

With the normalization (1.1), the resulting exact identity is

    h[Cg]=-delta N(g/psi,C^2g/psi)
          =-2delta A_N(g,C^2g),                          (7.1)

and h[g]=-2delta A_N[g]. The factor two may disappear only if the author
has explicitly rescaled h and N together. No domain-free operator product
with the full unbounded source expression is being asserted.

## 8. Scope and the remaining sign comparison

The proof supplies the complete reflected smoothing-energy and mixed-source
regularization gates (1.6). It does not bound their covariance defect. The reflected endpoint term is controlled by
its actual square-root vanishing, the true far theta weight is paid, and
the ratio-core closure is checked. Section 9 now pays the complete prime contribution to turn (7.1) into
an actual source high-frequency estimate. Neither result supplies the
coefficient-one Green comparison.

A compatible limiting choice is b=t^(1/2), a=b/8 and
exp(2R)=M[log(e/delta)+log(e/t)], with M fixed sufficiently large.
For each fixed delta and sufficiently small t, aK_R<=1, epsilon, eta and
T_delta all tend to zero. This example demonstrates nonempty parameters;
it is not an optimized exponent or an RH exclusion.

## 9. Depth-uniform high-frequency control of the actual odd source

This step uses only the MIXED bound in (1.6), where the far-tail
error is linear. It does not use a nonexistent small covariance defect.
For each sufficiently large N set

    t=N^-1, b=N^-1/2, a=b/8, beta=1/3,
    exp(2R)=M_R log N.

M_R is a fixed constant chosen sufficiently large for any desired fixed
inverse-power tail error. Now K_R<=C M_R log N and aK_R<=1 for all
N beyond a fixed threshold, independent of delta. Equations (1.7) give

    epsilon+sqrt(eta)<=C N^-1/8.                         (9.1)

Crucially, (6.3) gives the depth-free WEIGHTED mixed error

    delta T_delta(R,a)<=C exp(CR-c exp(2R))<=C_B N^-B     (9.2)

for any fixed B after choosing M_R. T_delta itself need not be small.
The legal actual equation (7.1) and its unfiltered counterpart imply

    h[g]-h[Cg]
       <=C delta N^-1/8+C_B N^-B.                       (9.3)

Here and below h uses the odd whole-line source g_odd; the preceding
half-line notation for A_N and N fixes the factor two already in (7.1).

### 9.1 The full prime tail, without a physical spectral projection

Extend mu evenly to the whole line. Its fixed theta envelope implies,
uniformly for |s|<=4a and all n>=2,

    sup_x mu(|x|)mu(|x+log n+s|)<=C exp(-c n).            (9.4)

Indeed |x|+|x+D|>=|D| and
exp(2|x|)+exp(2|x+D|)>=2exp(|D|). Any fixed polynomial/exponential prefactor
in mu is absorbed in half the double-exponential decay; |D|>=log n-4a.
Since g_odd=mu v_odd and ||v_odd||^2=2, Cauchy--Schwarz gives

    |<g_odd,tau_(log n+s)g_odd>|<=C exp(-c n).            (9.5)

Moreover <Cg,tau_d Cg> is the double average of
<g,tau_(d+s)g> against the two nonnegative convolution kernels, with
|s|<=4a and total averaging mass at most one. Thus it obeys the same bound.
The ENTIRE prime tail therefore satisfies

    sum_(n>P) alpha_n (|<g,tau_(log n)g>|
                       +|<Cg,tau_(log n)Cg>|)
       <=C exp(-c'P).                                  (9.6)

This argument does not spend ||Cg/mu||, does not assume an ordinary-L2
bounded complete prime operator, and retains every prime label in the tail.

### 9.2 Complete Gamma loss and the finite-prime absorption

Take P=L_B log N, with fixed L_B sufficiently large that (9.6) is O(N^-B).
The exact finite-prime source symbol on centered odd sources is

    a_P(xi)=b(xi)-C_0-2 sum_(2<=n<=P) alpha_n cos(xi log n).

Here b is the COMPLETE Gamma symbol, b>=0 and b(xi)>=c log(2+|xi|)-C.
Elementary Lambda(n)<=log n gives

    M_P:=C_0+2 sum_(n<=P)alpha_n
       <=C_B sqrt(log N)log log(e^e N)=o(log N).         (9.7)

Let c_N be the real Fourier multiplier of C and d_N=1-c_N^2>=0.
Comparison with the untruncated Poisson multiplier gives

    |c_N(xi)-exp(-|xi|/N)|<=C t/a<=C N^-1/2.

In particular

    d_N(xi)<=C N^-1/2 on |xi|<=sqrt(N),
    d_N(xi)>=c_1>0 on |xi|>=N,                          (9.8)

uniformly for sufficiently large N. On |xi|>=sqrt(N), (9.7) and the full
Gamma lower bound give a_P(xi)>=c_2 log(2+|xi|). On its complement,
a_P>=-M_P. Since ||g_odd||_2<=C, Plancherel yields

    h_P[g]-h_P[Cg]
      =(2pi)^-1 int a_P(xi)d_N(xi)|hat g_odd(xi)|^2 dxi
      >= c int_(|xi|>=N) log(2+|xi|)|hat g_odd(xi)|^2 dxi
          -C_B N^-1/2 sqrt(log N)log log(e^e N).          (9.9)

The centered polar terms vanish exactly before and after C. Equations
(9.3), (9.6) and (9.9), with B>=1, prove

    int_(|xi|>=N) log(2+|xi|)|hat g_odd(xi)|^2 dxi
      <= C delta N^-1/8
         +C N^-1/2 sqrt(log N)log log(e^e N).            (9.10)

All constants and the minimum N are independent of the actual source and
delta in (0,1), after ||g/mu||_(half-line)=1. Standard dyadic summation
therefore gives

    ||g_odd||_(H^s)<=C_s, 0<=s<1/16.                    (9.11)

The exponent is deliberately unoptimized. The increment is the actual
source and complete-prime/Gamma domain theorem with depth-uniform constants,
not a rephrasing of regularity in v, and not an estimate with a negative
power of delta. The stronger mixed bound (9.10) retains its explicit delta
in the leading tail term. No whole supercritical-band operator estimate is
asserted: the actual scalar equation (1.4) was essential. No new coefficient-
one signed Green margin, individual-zero correspondence, or numerical
exclusion follows from this theorem alone.

## Verification scope

Two independent mathematical read-throughs checked the endpoint kernel estimates,
the complete reflected coefficient sum and commutator, the bounded square-root
inequality, the true-theta tail and actual ratio-core passage, and every sign and
normalization in the full prime/Gamma loss estimate. Those checks cover the
individual-source theorem stated here. They do not certify a whole-band or
coefficient-one sign claim, neither of which is asserted.
