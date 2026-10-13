# Complete-prime source control and growing-rank positivity without a bandwidth restriction

2026-10-13. These estimates retain the original full Gamma symbol and every prime power. They prove positivity for arbitrary high-frequency families whose total rank grows at the stated rate, with no bound on their frequency diameter and no separation assumption. All cross terms within each such family are included. They do not prove positivity of an unlimited-rank zero-coupled form or the Riemann hypothesis.

## 1. Original setting and target

Use the complete theta source weight w=m^2=Phi/(2 cosh(x/2)) from the [original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). The full Gamma symbol and complete source prime sum are

 b(t)=sum_(j>=0) 2t^2/[a_j(a_j^2+t^2)],  a_j=2j+1/2,
 S F(x)=sum_(n>=2) Lambda(n)/sqrt(n) [F(x+log n)+F(x-log n)],
 C0=EulerGamma+pi/2+3log 2+log pi.

The prime sum below is evaluated in its absolutely convergent source quadratic pairing; no bounded unweighted L2 realization of S is assumed. For v=m r and F=mv=w r,

 H[v]=<F,b(D)F>-C0||F||^2-<F,SF>.

For every finite exponential polynomial considered below, F and all its derivatives have double-exponential real tails, so b(D)F belongs to L2, and the complete physical weighted prime operator is bounded. When the polynomial is even, v lies in the original even operator domain. The prime-pair estimate itself does not require parity; Section 4 explicitly evenizes its vectors. All forms retain every prime power.

For any infinite zero-mode expansion, finite truncations belong to the class below but their total rank grows with the truncation. Estimates with a rank price cannot be passed to the whole expansion without a separate argument, even if that expansion converges in the original graph norm.

## 2. Full prime sum relative to the source norm

Theorem 1. There is a fixed C depending only on w such that, for every nonzero exponential polynomial

 g(x)=sum_j sum_(k=0)^(r_j-1) a_jk x^k exp(i z_j x),
 r=sum_j r_j, |Im z_j|<=1/2,

and F=w g,

 |<F,SF>| <= C sqrt(r+1) [log(r+2)]^(3/2) ||F||_2^2.                 (P)

The real parts, node separations and coefficients are unrestricted. The constant does not depend on a carrier frequency.

External input is the classical measurable Turan--Nazarov inequality: for an exponential sum of r terms, a real interval I and measurable E subset I,

 sup_I |g| <= exp(|I| max|Im z_j|) (C_T |I|/|E|)^(r-1) esssup_E |g|.

The result is due to F. Nazarov, Algebra i Analiz 5(4), 1993, pp. 3–66; the stated form is reproduced as Theorem 1.1 in O. Friedland and Y. Yomdin, [An observation on the Turán–Nazarov inequality](https://www.impan.pl/shop/publication/transaction/download/product/89801), Studia Mathematica 218 (2013), 27–39, DOI 10.4064/sm218-1-2. For jets, replace x^k exp(lambda x) by exp(lambda x)[(exp(i epsilon x)-1)/(i epsilon)]^k. A multiplicity-j cluster uses the shared exponents lambda+i ell epsilon, 0<=ell<j. The total rank remains at most r, the real parts of lambda are unchanged, and compact-uniform convergence permits passage to the inequality. Because this is done only to establish the pointwise envelope (1), no weighted-norm convergence at infinity is presumed in this limiting step.

Choose E subset [-1,1] of measure at least 1 on which |g|<=||g||_L2[-1,1]. Since w has a strictly positive minimum there, this norm is <=C_w||F||. Applying the inequality on [-X,X], X=max(1,|x|), gives

 |g(x)| <= C exp(X)(C X)^r ||F||.                                (1)

The complete theta envelope w(x)<=C exp(4|x|-pi exp(2|x|)) implies

 |F(x)| <= C exp(5X-pi exp(2X)+r log(CX)) ||F||.                  (2)

Choose R_r>=1 by exp(2R_r)=K(r+1)log(r+2), with one fixed sufficiently large K. For all X>=R_r, the positive terms in (2) are at most (pi/2)exp(2X), including the fixed prefactor after enlarging K. This follows first at R_r and then by monotonicity of [5X+r log(CX)+C]/exp(2X). Therefore

 ||1_(|x|>=s)F||_2 <= C exp(-c exp(2s)) ||F||_2, s>=R_r.         (3)

For a shift d>=0 split the integration into |x|>=d/2 and its complement, on which |x+d|>=d/2. Cauchy--Schwarz gives

 |<F,tau_d F>| <= min(1, 2||1_(|x|>=d/2)F||/||F||) ||F||^2.     (4)

With d=log n, use the bound 1 up to n<=exp(2R_r) and (3) above that cutoff. Since alpha_n=Lambda(n)/sqrt n and Lambda(n)<=log n,

 |<F,SF>|/||F||^2
 <= 2 sum_(2<=n<=exp(2R_r)) log n/sqrt n
    +C sum_(n>exp(2R_r)) log n/sqrt n exp(-c n)
 <= C exp(R_r)(1+R_r).

This is (P). In particular there is no truncation error or omitted reflected shift; both signs of every shift contribute in the factor 2.

## 3. Complex translation with no maximum-frequency price

Assume now that every frequency in g satisfies Re z_j>=T, while |Im z_j|<=1/2 remains unchanged. The real parts may have arbitrary spread. On the r-dimensional exponential-polynomial space E, use the Hilbert norm

 ||g||_E=||wg||_2,        Z=-i partial_x.

The spectrum of Z consists of the z_j with their jet multiplicities. Its exact functional calculus gives

 exp(itZ)g(x)=g(x+t),       exp(-delta Z)g(x)=g(x+i delta).

These identities take place in the finite-dimensional exponential-polynomial space. They do not assert that complex translation is bounded on the original physical Hilbert space.

### 3.1. Real translations control the horizontal resolvents

From (1), 1+|x+t|<=(1+|x|)(1+|t|), and the complete theta moments,

 ||exp(itZ)||_(E->E)
 <= M_r exp(|t|)(1+|t|)^r,
 M_r <= exp(C r log(r+2)).                                      (5)

Indeed the additional factor is at most a constant to the rth power times

 (integral w(x)^2 exp(2|x|)(1+|x|)^(2r) dx)^(1/2),

which has the displayed bound by the double-exponential theta envelope. The bound is uniform over coefficients, multiplicities, separations, and every real frequency.

Fix a>1. The two one-sided group Laplace formulas, using (5) with opposite signs of t, give

 sup_(s real) ||(Z-(s+ia))^(-1)||
 +sup_(s real) ||(Z-(s-ia))^(-1)||
 <= 2M_r integral_0^infinity exp(-(a-1)t)(1+t)^r dt
 <= exp(C_a r log(r+2)).                                       (6)

For example, the integral is at most exp(a-1) r!/(a-1)^(r+1). No norm of Z, maximum real eigenvalue, or eigenvector condition number enters (6).

### 3.2. Remove all resolvent poles in the strip

Set c=pi/(2a). For |Im zeta|<a define the finite strip Blaschke product

 B_E(zeta)=product_j
   [(exp(c zeta)-exp(c z_j))
    /(exp(c zeta)+exp(c conjugate(z_j)))]^(r_j).                 (7)

The exponential maps this strip to the right half-plane. Each factor in (7) is holomorphic, has modulus at most 1 inside the strip and modulus 1 on its two horizontal boundary lines, and has its prescribed zero. The denominator has no zero in the strip.

The matrix function B_E(zeta)(Z-zeta)^(-1) has every resolvent pole removed, including its full Jordan order. On the horizontal boundary its norm is bounded by (6). As Re zeta tends to either infinity, the matrix tends to zero for each fixed Z: its resolvent tends to zero and |B_E|<=1. Apply the maximum principle on expanding rectangles to each scalar Hilbert-space matrix pairing. This proves the bound from (6) throughout the strip. The limiting argument is performed separately for each finite-dimensional Z; its resulting constant is the same uniform horizontal-boundary constant.

On the left line Re zeta=T-1 one has

 |exp(c zeta)|/|exp(c z_j)|<=exp(-c).

The triangle inequalities for numerator and denominator therefore give, for each individual factor,

 |(exp(c zeta)-exp(c z_j))
   /(exp(c zeta)+exp(c conjugate(z_j)))|
 >= (1-exp(-c))/(1+exp(-c))=tanh(c/2)=:b_a>0.

Consequently, on that whole vertical segment,

 ||(Z-zeta)^(-1)||<=exp(C_a r log(r+2)) b_a^(-r).                (8)

### 3.3. Dunford integration and the shifted theta weight

For fixed delta>0, integrate exp(-delta zeta)(zeta-Z)^(-1) around the rectangle with left side Re zeta=T-1, upper and lower sides Im zeta=+/-a, and right side beyond every eigenvalue. Let the right side tend to infinity. Its contribution vanishes. The two horizontal sides are bounded by (6) and the convergent integral of exp(-delta Re zeta); the left side has fixed length and is bounded by (8). Thus

 ||exp(-delta Z)||_(E->E)
 <= exp(-delta T+C_(a,delta) r log(r+2)).                        (9)

This is a one-sided spectral damping estimate and requires only the lower bound T for the real parts.

For 0<delta<pi/4, the analytic complete-theta envelope is

 |w(x+iy)|<=C_delta exp(C_delta|x|-c_delta exp(2|x|)),
 |y|<=delta.

The positive-real-half-line theta series proves this estimate there; analytic evenness gives the negative wing, and cosh(z/2) has no zero in this strip. Applying the real envelope (1) to any h in E and integrating this theta bound gives, for p=1,2,

 ||w(.+i delta)h(.)||_Lp
 <=exp(C_delta r log(r+2))||wh||_2.

Take h=exp(-delta Z)g and use (9). With, for example, a=2 fixed once and for all,

 ||w(.+i delta)g(.+i delta)||_Lp
 <=exp(-delta T+C_delta r log(r+2))||wg||_2, p=1,2.             (10)

Neither (9) nor (10) contains a bandwidth or highest-frequency constant.

## 4. Complete high-frequency form at growing total rank

Define the even polynomial and original physical vector

 q_even(x)=[g(x)+g(-x)]/2,       v=m q_even,       F=w q_even.

The total exponential-polynomial rank of q_even is at most 2r. Its frequencies occur on both real half-lines; their imaginary parts remain in [-1/2,1/2]. Its original even operator domain was paid in Section 1.

To control the norm without a frame assumption, put

 g^sharp(z)=conjugate(g(conjugate(z))).

The analytic function g^sharp(-z) again has all real frequencies at least T, and its real weighted norm equals ||wg||. Shift the contour upward in

 cross=integral w(x)^2 g(x)conjugate(g(-x)) dx.

The analytic integrand is w(z)^2 g(z)g^sharp(-z). Apply the p=2 case of (10) to the two factors and Cauchy--Schwarz on the shifted line. This gives

 |cross|<=exp(-2delta T+C_delta r log(r+2))||wg||^2,
 ||F||^2=(1/2+O(exp(-cT+C r log(r+2))))||wg||^2.                (11)

All contour end pieces vanish by the complete analytic theta tail. The constants are independent of the real-frequency spread.

Use the source Fourier convention Fhat(t)=integral F(x)exp(itx)dx. The p=1 estimate (10), with the contour shifted upward, gives

 |(wg)^hat(t)|<=exp(-delta(T+t)+C_delta r log(r+2))||wg||.

When |t|<T/2 this is at most exp(-delta T/2+C_delta r log(r+2))||wg||. The other reflected Fourier term is (wg)^hat(-t), so the same estimate holds for it. Provided the error in (11) is sufficiently small, the source Fourier mass on |t|<T/2 satisfies

 (1/(2pi))integral_(|t|<T/2)|Fhat(t)|^2 dt
 <=epsilon_(T,r)||F||^2,
 epsilon_(T,r)<=C T exp(-cT+C r log(r+2)).                       (12)

The original full Gamma symbol is nonnegative, and b(t)>=log T-C for |t|>=T/2 and large T. Therefore

 <F,b(D)F>>=(log T-C)(1-epsilon_(T,r))||F||^2.                  (13)

Applying Theorem 1 at total rank at most 2r, and retaining C0, yields the complete original-form estimate

 H[v]>={log T-C-C sqrt(r+1)[log(r+2)]^(3/2)
               -epsilon_(T,r)log T}||F||^2.                   (14)

Theorem 2. The full original H form is strictly positive on every nonzero vector in these families, for all sufficiently large T along every sequence with

 r[log(r+2)]^3=o((log T)^2),        T->infinity.

In particular r<=A log T, for any fixed A, is allowed for sufficiently large T. There is no bound on the maximum real frequency, no separation assumption, and no restriction to a single cluster. All mixed terms among the selected frequencies are included in (14). The exact source norm is used; no uniform physical ||v||^2 coercivity constant is asserted.

When the frequencies are genuine Xi zeros and the jets stay within their genuine multiplicities, the even vectors also have their original zero ground pairing. The estimate itself is valid without requiring the frequencies to be zeros.

## 5. The remaining total-rank boundary

Theorems 1 and 2 are finite-total-rank estimates with explicit rank prices. Equation (14) pays cross terms within every family satisfying its total-rank condition, even when the frequencies lie in widely separated windows. It does not pay a sum of arbitrarily many such families: positivity of individual blocks is insufficient for their full mixed form, and their combined rank must be counted.

An infinite source expansion is not covered merely because each fixed-width zero window has O(log T) members. Its finite truncations have growing total rank, and the rank condition must be checked against their minimum positive real frequency. Passing to a graph-norm limit is legitimate only after a uniform inequality for those same complete truncations is established. Small absolute coefficient tails alone do not provide that relative estimate for the actual negative-eigenstate expansion.

No positivity claim for unlimited rank or the whole zero family is made. The original coefficient-one comparison remains unproved.
