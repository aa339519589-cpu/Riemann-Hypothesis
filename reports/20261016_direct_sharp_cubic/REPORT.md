# Direct sharp cubic calculation through causal composition

16 October 2026. This proof uses the
[sharp causal-square theorem](../20261016_sharp_causal_square/REPORT.md),
not a full fourth Schatten bound and not an inference from a signed third
moment to spectral uniform integrability. It extends the previously recorded
[narrow-width sharp cubic calculation](../20261016_narrow_sharp_cubic_transfer/REPORT.md)
by a direct signed calculation. No literature-priority claim is made.

## Statement

For each fixed smooth even nonnegative probability f supported in
[-lambda/2,lambda/2], lambda<1, and fixed 0<a0<b0, let A_T be the SAME sharp
Hermitian zero operator defined in the causal-square theorem. Then the
unconditional asymptotic is

 tr(A_T^3)/(T log T/(2pi)) -> (b0-a0)
       [integral f^3 +3 double-integral |s-t|f(s)^2 f(t) ds dt]. (D1)

All zero labels retain multiplicity. This is the signed trace only. No new
proportion, numerical certificate, or novelty claim is made here.

## 1. Paid reductions and conventions

Use L, J=[A0,B0], X=T^mu, alpha, G0, R and H from the causal-square proof,
with lambda<mu<1. Write d=s-t. The causal kernel B=T(A) satisfies

    tr A^3=6 Re <B^2,B>_HS.                                  (D2)

The causal-square proof supplies all four quadratic rows and errors of
Hilbert--Schmidt norm o(sqrt(TL)). The linear slot can additionally be
replaced, in Hilbert--Schmidt norm at the same error scale, by

    C(s,t)=1_(d>0)sqrt(f(s)f(t))G0(d),
    P(s,t)=1_(d>0)sqrt(f(s)f(t))/(2pi)
             sum_(n<=X)Lambda(n)/sqrt(n) D_J(Ld-log n),
    B=C-P+o_HS(sqrt(TL)).                                    (D3)

For the prime replacement, use exactly the exponential-difference bound
from the square proof with a SINGLE prime coefficient sum. Its error is
O(T^(mu/2)L^C), so its squared integral is o(TL). The Gamma damping change
is O(L) pointwise. This linear replacement is made only after the quadratic
row has already been reduced; it is not used before forming the prime square.

Both B and C-P have HS norm O(sqrt(TL)): for P this follows from the same
single-prime Plancherel and mean-value argument, and for C it follows from
the full Gamma HS bound. Each retained quadratic main row has HS norm
O(sqrt(TL)). Thus every omitted error in (D2) contributes o(TL).

After removing the outer sqrt(f(s)f(t)), the quadratic main rows are:

 (i)  C^2, with its actual compact middle f;
 (ii) Q_RR=(2pi L)^(-1) sum_(q<=X)b_q(t)/sqrt(q) D_J(Ld-log q),
      b_q(t)=sum_(mn=q)Lambda(m)Lambda(n)f(t+log n/L);
 (iii) Q_mix=(2pi)^(-1)sum_(n<=X)Lambda(n)/sqrt(n)
           [f(s-log n/L)+f(t+log n/L)]D_H(Ld-log n),
      D_H(v)=integral_J H(u)exp(iuv)du.

The signed combination is B^2=C^2-Q_mix+Q_RR+o_HS(sqrt(TL)).
Changing the damped Gamma square to C^2 has pointwise error O(L^C), by the
causal L1 estimate already used in the square proof.

## 2. Elementary bilinear freezing rules

For any uniformly bounded Lipschitz coefficient F(d), translated Dirichlet
kernels whose centers lie in a fixed bounded interval obey

 integral_R F(d)D_J(Ld-log q)overline(D_J(Ld-log n))dd
  =(2pi/L)F(log q/L)D_J(log n-log q)+O_F(log T/L^2).            (D4)

This is the same proof as (C5): the Lipschitz increment cancels one Dirichlet
denominator on a fixed interval, and outside it both denominators decay.
The rule with the first kernel D_H instead of D_J has error
O_F(log^2 T/L^2), because sup|H|+Var_J(H)=O(log T). Its main term is

    (2pi/L)F(log q/L) integral_J H(u)exp[iu(log n-log q)]du.    (D5)

The coefficient F may be one of the products of shifted f factors below;
its boundedness and Lipschitz constant are uniform in all prime labels.

The original d>0 integral can be extended to the full line in these
prime/prime rows at cost O(X L^C)=o(TL). On d<=0 every prime center is
strictly positive, so each summed flat prime kernel is bounded by
O(sqrt(X)L^C); the same estimate applies to the semiprime sum after its
1/L prefactor. On the noncompact tails use the extra inverse-difference
factor from each kernel. The outer compact f coefficient is retained before
freezing; the full-line freezing error includes its exterior tail.

For any two coefficient vectors supported on n<=X, the off-diagonal
bilinear sum with denominator |log(n/m)| is at most

    C X log(2X) ||a||_2 ||b||_2.                             (D6)

This follows from the harmonic row-sum bound used in (C6). For D5 multiply
it by the O(log T) variation/endpoint bound for H. Every such error below
is O(X L^C)=o(TL), since mu<1.

## 3. Gamma scalar multipliers and one-prime terms

Let V0(d)=1_(d>0)G0(d), and let H0 be its Fourier transform at frequency Lu.
As a boundary value,

 H0(u)=Omega(u)1_J(u)/(2L)
       +(i/(2pi L)) PV integral_J Omega(v)/(v-u)dv.           (D7)

This is the c down to zero limit of the regularized H_c. On J its endpoint
singularities are logarithmic. For fixed nonnegative integers r,s with r+s<=2 and r+s>0,

 |integral_J H0(u)^r H_c(u)^s exp(i v u)du|
       <= C log^C(Tv)/v,       v>=log 2,                    (D8)

and the same estimate holds with conjugated factors. One proof removes
endpoint collars of length 1/v, bounds those integrals using the logarithmic
singularity, and integrates by parts on the complement. There the derivative
is bounded by a constant times the endpoint reciprocal distances times the
remaining logarithmic factors. The half real diagonal in (D7) is retained.

For clarity, the causal Gamma-square kernel can itself be reduced without
using any new operator domain. On 0<d<=lambda,

 integral_0^d f(t+y)G0(d-y)G0(y)dy
   = f(t)(V0*V0)(d)+O_f(L^C).                               (D9)

The increment f(t+y)-f(t) cancels the 1/y bound for G0(y); the other Gamma
factor has bounded-interval L1 norm O(L). Also

 |(V0*V0)(d)| <= C log(2+TLd)/(d+1/(TL)), d>0,

so its bounded-interval L1 norm is O(L^2), and its product with an exterior
Dirichlet denominator is absolutely integrable. Freezing the remaining outer
coefficient at a prime center is therefore legitimate, with O(L^C) error
per coefficient. More explicitly, on a fixed region the product
|F(d)-F(a)| |D_J(L(d-a))| is at most 2 Lip(F)/L, while the
bounded-region integral of |V0*V0| is O(L^2). Outside that region retain
the O(log(2+TLd)/d) convolution bound and the other O(1/(Ld))
denominator together. No global L1 norm of the causal Gamma kernel is used.

For the scalar Fourier license, V0 belongs to L2 and the explicit H0
belongs to L4: its endpoint singularities are logarithmic and its tails
are O(T/|u|). Hence H0^2 belongs to L2. The convolution identification
follows by scalar Abel regularization and convergence in L4 of the
explicit regularized multipliers, or equivalently by L2 Plancherel.
Thus the main height multiplier is H0^2; no product of unspecified
distributions or operator-valued continuity is assumed.

Apply (D8) to the resulting nonzero frequencies log n or log q. It follows
that all of the following pairings are o(TL):

    <C^2,P>,    <Q_mix,C>,    <Q_RR,C>.                      (D10)

For the first the multiplier is H0^2; for the second it is H_c overline(H0);
for the third it is overline(H0). The coefficient absolute sums are
O(sqrt(X)L^C), including the semiprime row and its 1/L prefactor. Thus the
bound O(sqrt(X)L^C) is already o(TL). No zero-frequency prime term occurs.

## 4. Three-prime row

Apply (D4) to <Q_RR,P>. The diagonal requires q=n with Lambda(q)>0, hence
q=p^k with k>=2. Its coefficient sum is bounded:

 sum_q (Lambda*Lambda)(q)Lambda(q)/q
  =sum_(p,k>=2) (k-1)log^3(p)/p^k < infinity.

With the two 1/L factors this contributes O(T/L^2). The off-diagonal and
freezing/collar errors are O(X L^C) by (D4)--(D6). Consequently

    <Q_RR,P>=o(TL).                                         (D11)

## 5. Two-prime/Gamma main row

Only <Q_mix,P> has a surviving prime diagonal. Set x_n=log n/L and

    J_f(x)=integral f(t)f(t+x)[f(t)+f(t+x)]dt.

Use (D5), freezing all outer/shifted f factors at d=x_n. Off-diagonal and
freezing errors are again O(XL^C). The exact surviving expression is

 <Q_mix,P>
  =(1/(2pi L)) [integral_J H(u)du]
                sum_(n<=X)Lambda(n)^2/n J_f(x_n)+o(TL).     (D12)

The real part of the multiplier average satisfies

    Re integral_J H(u)du=|J|/2+o(T).                        (D13)

Indeed Re H is the Cauchy/Poisson convolution of Omega/L with the interval
indicator, with factor 1/(2pi); Omega/L converges uniformly to one on J.
The Cauchy mass lost through the two endpoints has integrated size O(log T),
which is o(T). The imaginary average is irrelevant here.

The prime number theorem and partial summation give

 sum_(n<=X)Lambda(n)^2/n J_f(log n/L)
    =L^2 integral_0^lambda x J_f(x)dx+o(L^2).                (D14)

Proper powers contribute only O(1), and J_f vanishes for x>=lambda. Finally

 integral_0^lambda xJ_f(x)dx
     =double-integral |s-t|f(s)^2f(t)dsdt.                  (D15)

Combining (D12)--(D15) with the factor 6 in (D2) gives precisely the
coefficient 3 multiplying the double integral in (D1).

## 6. Pure Gamma main term

Let Gfull(s,t)=sqrt(f(s)f(t))G0(s-t), so C=T(Gfull). Then
6 Re<C^2,C>=tr Gfull^3 exactly. This trace can be evaluated directly.
In its three-kernel integral replace f(t)f(v) by f(s)^2. The resulting error
is O_f(L^2), since for k_h(x)=min(1/h,1/|x|), h=(TL)^(-1),

 integral_R^2 min(|x|,1)k_h(x)k_h(y)k_h(x+y)dxdy=O(log^2(1/h)).

To see this, use (k_h*k_h)(x)<=C log(2+|x|/h)/(|x|+h), then split
|x| at h and 1. The other Lipschitz increment is symmetric. The tail beyond
the compact frequency support is covered by the same integrable majorant.
The exact convolution at the origin then gives

 tr Gfull^3
  =(integral f^3)/(2pi L^2) integral_J Omega(u)^3du+O_f(L^2)
  =|J|L/(2pi) integral f^3+o(TL).                            (D16)

## 7. Assembly and scope

Insert (D10), (D11), (D12) and (D16) into (D2), with the signed rows from
Section 1. This proves (D1). The good-height endpoint adjustment is already included in the
causal-square error class; it is not paid by an assumed real-zero condition.

The detailed [causal Gamma Fourier-product proof](CAUSAL_GAMMA_FOURIER_PRODUCTS.md)
pays the unregularized multiplier and (D8). The
[right-Euler cubic subrow](RIGHT_EULER_CUBIC_SUBROW.md) supplies a standalone
verification of (D11). Every causal-to-full-line collar in (D4)--(D5) is
retained above.
Nothing here identifies the signed cubic with an absolute spectral moment,
and no general S2 continuity of cubic traces is assumed.
