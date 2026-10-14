# Finite-profile reset facts and the same-current domain

This note records only the reset and domain facts needed by the projected
principal. No different arithmetic-character operator is substituted.
The positive hidden lift, including the operational origin hold, is the
published [full-band lift](../20261014_first_label_current_approximation/HIDDEN_LIFT.md)
and [current field](../20261014_first_label_current_approximation/CURRENT_FIELD.md).
Its global logarithmic label bound is proved in
[GLOBAL_LABEL_CONTROL](../20261014_first_label_coercive_correction/GLOBAL_LABEL_CONTROL.md).
The actual projection and averaged domains are in the
[uncentered profile](../20261014_centered_mobius_profile/UNCENTERED_PROFILE.md)
and [centered profile](../20261014_centered_mobius_profile/CENTERED_PROFILE.md).

## 1. Genuine scores, full divisor rates and finite arithmetic masks

Use z=pi exp(2x), eta=exp(x/2)(4z^2-6z)exp(-z), Phi=C eta,
psi=-Phi', s=psi/Phi, p_n=n^(-1/2)eta(x+log n)/Phi(x), and T v=sum p_n v_n.
To distinguish the arithmetic mask from the refresh score, call the
positive refresh score c_n. Explicitly,

 c_n=beta_n+int_0^infinity kappa(t)eta(x+log n+t)/eta(x+log n)
                             [s(x+t)/s(x)-1]dt
               +sum_(d|n)Lambda(d)[s(x+log d)/s(x)-1],
 beta_n=(4n^2z-1)/(4n^4z^2-6n^2z),
 beta=T c=(3Phi+Theta/2)/psi,
 L_n=sum_(d|n)Lambda(d)s(x+log d)/s(x).

The complete score theorems give

 p_1>400/401, q=1-p_1<=28exp(-3z), q/p_1<1/400,
 c_n>=c_2>=c_1 for n>=2,
 c_n-beta>3log2 for n>=2,
 L_n<=(4/3)c_n,
 c_2>=L_2-log2, L_2=log2*s(x+log2)/s(x)>=4log2.

The score ordering and full theta bounds are proved in
[SECOND_LABEL_COMPLETION](../20261014_first_label_coercive_correction/SECOND_LABEL_COMPLETION.md),
[THETA_SCORE](../20261014_first_label_current_approximation/THETA_SCORE.md),
and [DIVISOR_RESET](../20261014_first_label_current_approximation/DIVISOR_RESET.md).
For clarity, the stronger tail separation follows from the same exact
constants: c_2>3log2+(9/2)log2/s, whereas
beta/p_1<48521/(16000s). Since (9/2)log2>621/200,

 c_n-beta >=c_2-beta/p_1
             >3log2+1159/(16000s)>3log2.

Thus no omitted divisor or separately estimated prime branch is used.

Let a(n)=1-mu_ar(n), or a_N(n)=1-mu_ar(n)1_(n<=N), N>=2.
The finite mask equals ONE beyond N, not zero. In both cases

 a(1)=0, a(2)=2, 0<=a<=2,
 m=T a, M=T a^2, sigma^2=M-m^2,
 sigma^2>=4p_1p_2, m<=2q<1/200,
 m^2/sigma^2<=q/p_1<1/400.

The variance floor is the label 1/label 2 term of
Var(a)=sum_(i<j)p_i p_j(a_i-a_j)^2. The final bound follows by
m^2<=q M and sigma^2>=p_1 M.

## 2. Exact orthogonal reset completion

For the SAME actual current w, T w=u. Set H=w-u and

 h=T(aH), A=h/sigma^2,
 D_n=A(a(n)-m), Z=H-D,
 T Z=T(aZ)=0,
 V=T H^2=sigma^2 A^2+T Z^2,
 kappa_a=T[c(a-m)^2]/sigma^2.

The reset projection is exactly

 m T(cH)-T(caH)=-kappa_a h+r,
 r=-T[c(a-m)Z].

No moving-mean contribution or independent replacement of Z is allowed.
Moreover

 kappa_a>beta+(399/400)3log2>beta+2,
 kappa_a>=(399/400)c_2.                            (1)

For the first inequality, use T(c-beta)=0 to obtain

 (kappa_a-beta)sigma^2
   =sum_(n>=2)p_n(c_n-beta)a_n(a_n-2m)
   >3log2(M-2m^2).

Each coefficient is nonnegative because every nonzero a_n is1 or2 and
m<1/200. Division by sigma^2 and m^2/sigma^2<1/400 proves the result.
For the second inequality, the root-label fraction of the variance is
p_1 m^2/sigma^2<1/400; all other scores are at least c_2.
These arguments hold before any finite-mask limit.

## 3. Actual amplitude and grouped forcing domain

The published profile-domain theorem proves that A is bounded uniformly
in these masks, and that D has the required averaged hidden and original
star form energies. It does not assert original-P membership of every
unweighted label field. The logarithmic current estimate is

 |w(x,n)|<=C(1+log n),
 T(w-u)^2<=C exp(-3z),
 |A(x)|<=C,

where C is allowed to depend on the fixed actual source. The source u is
bounded and has its already proved positive Hölder exponent. The score
and divisor envelopes are polynomial in n,z, with at most the paid 1/x
origin singularity. Complete posterior tails satisfy
p_n<=2n^4 exp[-(n^2-1)z].

These facts give the following grouped estimate for the exact projected
forcing f=-S_a(u)+r+I_Z in FINITE_PROJECTION:

 |f(x)| <= C beta(x) P(z)exp(-3z) on x>=1,
 |f(x)| <= C/x on 0<x<=1,                          (2)

for a fixed polynomial P, uniformly in the masks. To see the source part,
monotonicity of every tail posterior gives G_cont m<=2G_cont q<=2r_prime.
Hence its continuous increment against bounded u and its complete prime
row are bounded by C r_prime; the complete theta row has the first bound
in (2). For r, subtract its affine interpolant through labels1,2 before
using T Z=T(aZ)=0. The resulting coefficient is zero at both labels and
bounded by 2c_n for n>=3. For I_Z, use the finite arithmetic affine
subtraction in FINITE_PROJECTION: both child 1 and child 2 vanish, all
remaining coefficients have absolute value at most 1, and the full parent
rate sum is Gaussian-summable. The logarithmic bound on Z and these exact
subtractions pay the entire source, reset and divisor forcing. At the
origin the operational score bounds pay the common1/x order. No sharp
quantitative residual estimate is needed or spent here.

The variance-metric proof uses (2) only after multiplying by its exact
factor ell q_psi. That factor grows at most a polynomial times exp(z/2)
at infinity and vanishes linearly at the origin. The resulting complete
forcing is L2(dz). The separate Carleman argument in TRUE_VARIANCE_METRIC
then proves the actual Gamma generator domain; neither bounded amplitude
nor pointwise Gaussian decay alone is used to infer it.
