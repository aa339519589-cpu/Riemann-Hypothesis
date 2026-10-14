# Actual arithmetic origin trace and cancellation of the quadratic prime collar

For every actual scalar supercritical Green source at fixed positive depth, this note proves an exact arithmetic origin condition, a genuine first derivative at the origin, and cancellation of the quadratic-scale complete prime collar. It does not determine the full covariance sign, exclude the source, or prove RH. The input checkout is `675b83e872ce91ec31f9deab7f98516208faf78b`.

The actual realization and theta tail are from [the source-tail theorem](../20261013_supercritical_source_tails/REPORT.md). The new regularity and every-fixed-translation input is [the second source bootstrap](../20261013_supercritical_source_tails/BOOTSTRAP_AND_FIXED_TRANSLATIONS.md). The unchanged local source equation is recorded in [fractional origin control](../20261013_supercritical_source_tails/FRACTIONAL_ORIGIN_BOUNDARY.md). The complete smooth collar formula is from [odd Green variation](../20261013_full_prime_green_reference/ODD_VARIATION_PRIME_BOUNDARY.md), and the raw line formula and its normalization are from [raw translations](../20261014_translation_neutral_covariance/RAW_TRANSLATION_DOMAIN.md).

## 1. Actual inputs and conventions

Let g=psi r be a pole-centered source with N(r,z)=lambda P(r,z), lambda>1, delta=1-1/lambda>0. Let g_o denote its odd extension, and put

p=psi'(0)>0, d_n=log n, alpha_n=Lambda(n)/sqrt(n),
L(x)=sum_(d_n>x)alpha_n psi(d_n-x),
B_o g=(b(D)g_o)|_(x>0).

Every Mangoldt label is retained. The new fixed-depth theorem proves, for every s<1,

||g_o||_(H^s)+||v_o||_(H^s)<=C_(delta,s) sqrt(P[r]),
int_X^infinity |v|^2<=C_delta P[r] exp(9X-pi exp(2X)),
g=mu v, mu^2<=C exp(7x-pi exp(2x)).                    (1)

Fix 0<epsilon<log(2)/4. On (0,epsilon), define the complete loads

F_+(x)=sum_n alpha_n g(d_n+x),
F_-(x)=sum_n alpha_n g(d_n-x).

The exact actual source equation is

B_o g+delta L r=C_0 g+F_+-(1-delta)F_-.                 (2)

No Gamma term, prime direction, or source pole coefficient is altered. Pole centering has already killed the rank-one moment in (2).

## 2. Weighted source regularity and complete load traces

For every A>0 and every s<1,

exp(A|x|)g_o in H^s(R),
||exp(A|x|)g_o||_(H^s)<=C_(delta,A,s) sqrt(P[r]).         (3)

One self-contained proof is to choose s<q<1 and partition into fixed-width smooth spatial shells. Each shell has a uniform H^q bound from (1), while its L2 norm has a double-exponential bound from the mu envelope and the cumulative v tail. Interpolation gives an H^s norm with a strictly positive remaining double-exponential exponent. Multiplication on each shell by exp(A|x|), followed by summation, is therefore finite. The finitely many central shells are harmless; the weight is Lipschitz there and s<1. This proof makes no claim of a depth-uniform constant.

Choose a fixed cutoff chi supported in (-2epsilon,2epsilon), equal to one on (-epsilon,epsilon). For A=1 and w=exp(|x|)g_o, d_n-2epsilon>0 gives

chi(t)g(d_n+t)=n^(-1)chi(t)exp(-t)w(d_n+t).

Thus

||chi(.)g(d_n+.)||_(H^s)<=C_(delta,s) n^(-1) sqrt(P[r]).

The same holds after reflecting t. Since sum_n alpha_n/n<infinity, both complete load series converge absolutely in H^s(-epsilon,epsilon), for every s<1. For s>1/2 the Sobolev embedding also gives absolute convergence in a Holder norm of any order alpha<s-1/2. In particular the actual continuous representatives obey

F_+(0)=F_-(0)=F_0,
F_0=sum_n alpha_n g(d_n),                              (4)

with an absolutely convergent series. These are now genuine point evaluations, not merely local averages.

Choose s<q<1. The logarithmic symbol bound gives b(D)g_o in H^s from g_o in H^q. It remains odd, and for s>1/2 it is continuous with value zero at the origin. The same is true of g_o itself.

## 3. The exact arithmetic origin condition

All fixed derivative series for L converge normally on (-epsilon,epsilon); L is smooth and strictly positive there. Dividing (2) by delta L proves

r in H^s(0,epsilon), for every s<1.                     (5)

In particular r has a continuous origin trace. Taking x down to zero in (2), using oddness of g_o and b(D)g_o and (4), gives

boxed: L(0) r(0)=sum_n alpha_n g(d_n).                  (6)

The factor delta cancels exactly. Since L(0)=sum_n alpha_n psi(d_n), equation (6) is equivalently the complete positive arithmetic average

r(0)=sum_n q_n r(d_n),
q_n=alpha_n psi(d_n)/L(0), q_n>=0, sum_n q_n=1.          (7)

All r(d_n)=g(d_n)/psi(d_n) are defined by the continuous positive-wing source. The series in (7) converges absolutely because (4) does. No bound on unweighted point values of r at infinity is needed.

For every 0<alpha<1/2, choose s with alpha+1/2<s<1. The trace estimate in (5) yields

r(x)=r(0)+O_(delta,alpha)(sqrt(P[r]) x^alpha),
g_o(x)=a x+O_(delta,alpha)(sqrt(P[r]) |x|^(1+alpha)),
a=p r(0)=(p/L(0))sum_n alpha_n g(d_n).                 (8)

Here the odd expansion applies on both sides of zero. Thus g_o is genuinely differentiable at zero and g_o'(0)=a. This is one origin derivative, not a claim of C1 regularity at every prime knot. The complete reflected divergence W=Lr-F_- has trace W(0)=0.

## 4. The complete prime collar is o(t^2)

Let k be any fixed real even smooth kernel supported in (-1,1), with mass one, and C_t convolution by k_t=t^(-1)k(./t). Signed kernels are permitted. For t sufficiently small the inherited exact all-prime collar is

D_pr(t)=int_(x,y>0,x+y<t) k_t(x+y)
 { (C_tg)(x) F(y) -(k_t*F)(y)g(x) } dxdy,
F(y)=sum_n alpha_n[g(d_n+y)+g(d_n-y)].                  (9)

Use real sources for notation; complex sources use the corresponding real polarized expression. The complete load is even, with

F(y)=2F_0+O_(delta,alpha)(sqrt(P[r]) |y|^alpha).

Write g_o(x)=a x+h(x), h(x)=O(|x|^(1+alpha)), and F(y)=2F_0+E(y), E(y)=O(|y|^alpha). Since k is even and mass one,

C_t(a x)=a x,
C_tg(x)=a x+O_(delta,alpha,k)(sqrt(P[r]) t^(1+alpha))

for 0<x<t, and k_t*F=2F_0+O(sqrt(P[r])t^alpha) on the needed interval. The coefficient a x*2F_0 cancels EXACTLY in the braces of (9). Every remaining term is bounded by C_(delta,alpha,k) P[r] t^(1+alpha). The triangular area is O(t^2), and ||k_t||_infinity=O(t^(-1)). Hence

boxed: |D_pr(t)|<=C_(delta,alpha,k) P[r] t^(2+alpha),
       every fixed 0<alpha<1/2.                       (10)

In particular D_pr(t)/t^2 tends to zero. There is no omitted prime and no dependence on a pointwise approximation of the prime measure. The conclusion follows from the actual origin expansion and the complete continuous load, not from a generic compact-core source substituted for an eigen-source.

The arithmetic value relation (6) identifies a in the origin expansion. The cancellation of the purely constant-times-linear collar itself follows from even mass-one convolution; it should not be described as a separate sign theorem.

## 5. Every small raw translation has the same cancellation

For T_a g_o(x)=[g_o(x+a)+g_o(x-a)]/2, every sufficiently small fixed a is legal and the source map is continuous in the actual P norm by the second bootstrap. The exact complete raw prime collar is

D_pr,raw(a)=(1/2) int_0^a
 { (T_a g)(x)F(a-x)-[(F(2a-x)+F(x))/2]g(x) } dx.        (11)

The factor 1/2 follows from the two origin/prime corners of the reflected commutator. The inherited formula was first established almost everywhere; the new P-norm continuity, together with the continuous representatives g and F, extends it to every sufficiently small fixed a.

Equation (8) gives T_a g(x)=a_origin x+O(sqrt(P[r])a^(1+alpha)), where a_origin=p r(0). Both load factors in (11) equal 2F_0+O(sqrt(P[r])a^alpha). Their common leading product a_origin x*2F_0 cancels, exactly as in Section 4. Therefore

|D_pr,raw(a)|<=C_(delta,alpha)P[r]a^(2+alpha),
every fixed 0<alpha<1/2.                               (12)

The estimate is at fixed depth; it is not uniform as delta tends to zero.

## 6. Remaining signed question

The full covariance is 2(D_V-D_pr). Equation (10) shows that a putative negative contribution at quadratic scale must come from the complete potential term D_V, not a surviving leading prime collar. It does not assert that such a contribution exists. With the currently proved regularity, taking fourth-order differential limits still requires the correct boundary terms and separate justification.

The origin identity (6) is available to the independent quartet boundary calculation without an assumed prime derivative trace. The rest of the complete Gamma/pole/prime comparison remains unresolved.
