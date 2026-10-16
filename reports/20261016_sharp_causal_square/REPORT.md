# A sharp causal-square bound for the zero operator

16 October 2026. Independently checked analytic result. This is a bound for
the square of a triangular part, not a bound for the fourth trace of the full
Hermitian operator. No sharp cubic asymptotic, improved zero proportion, or
claim of novelty over the literature is asserted.

## Target and notation

Fix 0<a0<b0 and a smooth nonnegative window f supported in
I_f=[-lambda/2,lambda/2], with lambda<1. Set L=log T, and

    S(d)=sum_(a0 T<gamma<=b0 T) exp[(rho-1/2)L d],
    A(s,t)=sqrt(f(s)f(t)) S(s-t),
    B(s,t)=1_(s>t) A(s,t).

Zero labels include multiplicity. Then

    ||B^2||_(HS)^2 = O_f,a0,b0(T L).                         (C1)

This is weaker than tr(A^4)=O(TL). A two-step nilpotent triangular operator
can have B^2=0 while B+B* has arbitrarily large fourth trace.

Choose lambda<mu<1 and set X=T^mu, sigma=1+1/L, alpha=sigma-1/2.
Let J=[A0,B0], with endpoints comparable to T, differing by at most one
from a0 T,b0 T, and chosen a distance at least c/log T from every zero
ordinate. The standard horizontal logarithmic-derivative bound is then
O(log^2 T), uniformly on the bounded real strip used by the rectangular
contour. A primary locator is Elkies' author notes, printed page 3, formula
(6), https://people.math.harvard.edu/~elkies/M229.22/zeta2.pdf :
zeta'/zeta(s)=sum_(|Im(s-rho)|<1) 1/(s-rho)+O(log|Im s|), uniformly
for -1<=Re s<=2, with O(log|Im s|) summands. Riemann--von Mangoldt bounds
the number of ordinates in the endpoint unit intervals by O(log T). Remove
intervals of radius c/log T about them, choosing c small enough that their
total length is less than the available endpoint interval. On the remaining
height, every displayed denominator is at least c/log T, proving the
O(log^2 T) bound. Moving the original endpoints to these endpoints adds O(log T)
zero labels. Their kernel on 0<=d<=lambda is bounded by
O(log T exp(Ld/2)), so it has the same error class used below.

Use the ordinary Fourier convention

    D_J(v)=integral_J exp(i t v) dt,
    Omega(t)=log(t/(2pi)).

## 1. Rectangular explicit formula on positive frequency differences

Residues of zeta'/zeta against exp[(s-1/2)Ld] in the rectangle with real
sides sigma and 1-sigma, followed by the functional equation on the left,
give, for 0<=d<=lambda,

    S(d)=G(d)-R(d)+E(d),                                    (C2)
    G(d)=exp(-alpha Ld)/(2pi) integral_J Omega(t)exp(i t Ld)dt,
    R(d)=exp(alpha Ld)/(2pi) sum_(n<=X) Lambda(n)n^(-sigma)
                                      D_J(Ld-log n),
    |E(d)| <= exp(alpha Ld) L^C.                            (C3)

Here C is a fixed finite exponent, which may change between estimates.
The negligible O(1/T) error in the logarithmic derivative of the Gamma
factor contributes O(1). The other Euler branch has argument Ld+log n,
so |D_J|<=2/(Ld+log n) and its whole contribution is in (C3).
The omitted right-Euler tail satisfies

 sum_(n>X) Lambda(n)n^(-sigma)/|log n-Ld| = O_(mu-lambda)(1)

uniformly d<=lambda. This follows by partial summation from Chebyshev, or
from comparison with integral_mu^infinity exp(-u)/(u-lambda) du. Horizontal
contours and the endpoint adjustment also obey (C3). No pole at s=1 is
inside a rectangle with positive heights comparable to T.

Two useful absolute estimates, with

    P(d)=sum_(n<=X) Lambda(n)n^(-sigma) D_J(Ld-log n),
    G0(d)=(2pi)^(-1) integral_J Omega(t)exp(i t Ld)dt,

are

    integral_(-C0)^(C0) |P(d)| dd = O(L^C),
    sup_(d<=0) |P(d)| = O(L^C),
    |G0(d)| <= C min(TL,1/|d|),
    integral_0^lambda exp(-2alpha Ld)|G0(d)| dd=O(L^C).       (C4)

The first uses integral over a bounded interval of |D_J(Ld-v)|=O(log T/L),
uniformly for log n/L in [0,mu], and sum Lambda(n)n^(-sigma)=O(L).
The second uses log n-Ld>=log n. The Gamma bound follows by integration
by parts; the constants depend only on the fixed height interval.

Consequently every causal product containing the E row in (C2) has
pointwise size at most exp(alpha L(s-t)) L^C. Its squared kernel integral
is O(T^lambda L^C)=o(TL). This also pays replacing endpoints by good heights.
The middle factor f(v) is bounded throughout.

## 2. Right-Euler times right-Euler

The product kernel, after removal of outer square-root factors, is

 exp(alpha Ld)/(2pi)^2 integral_t^s f(v) P(s-v)P(v-t) dv,
 d=s-t>0.

Extending v to the full real line changes this by at most
exp(alpha Ld)L^C: outside [t,s], one prime argument is nonpositive, and
(C4) pays the other over the fixed support of f.

For each m,n<=X, put v0=t+log n/L. Then

 integral_R f(v) D_J(L(s-v)-log m) D_J(L(v-t)-log n)dv
 = (2pi/L) f(v0) D_J(Ld-log(mn)) + O_f(log T/L^2).             (C5)

The constant is uniform in s,t in I_f and m,n<=X. The constant-function
identity is Plancherel / P_J^2=P_J. For the error, on a fixed interval
containing both translated centers, use

 |f(v)-f(v0)| |D_J(L(v-v0))| <= 2 ||f'||_infinity/L

and the L1 Dirichlet-kernel bound for the other factor. Outside that fixed
interval both kernels are O(1/(L|v|)), which is integrable after multiplication.
Summing the error in (C5) costs at most O(L^C), since the sum of the prime
coefficients is O(L).

Terms with mn>X have |log(mn)-Ld|>=(mu-lambda)L. Their entire contribution
is O(exp(alpha Ld)L^C), using the squared sum of prime coefficients. Thus
only q=mn<=X remains. Define

    b_q(t)=sum_(mn=q) Lambda(m)Lambda(n)f(t+log n/L).

The remaining kernel is

    exp(alpha Ld)/(2pi L) sum_(q<=X) b_q(t)q^(-sigma)
                                              D_J(Ld-log q).

Replace exp(alpha Ld)q^(-sigma) by q^(-1/2). The elementary inequality

 |exp(alpha v)-1| |D_J(v)| <= C max(1,exp(alpha v))

shows that the resulting error is O(T^(mu/2)L^C), uniformly on I_f^2.
Indeed sum_(q<=X)(Lambda*Lambda)(q)/sqrt(q)=O(sqrt(X)L^C), while
sum_(q<=X)(Lambda*Lambda)(q)q^(-sigma)=O(L^2). This error has squared
integral o(TL), since mu<1.

For the main kernel, extend d to the real line and apply Plancherel:

 integral_R |sum_(q<=X) b_q(t)/sqrt(q) D_J(Ld-log q)|^2 dd
 = (2pi/L) integral_J |sum_(q<=X) b_q(t)/sqrt(q) q^(-iu)|^2 du.

The elementary Dirichlet mean-value upper, uniformly in the interval J, is

 integral_J |sum_(q<=X) c_q q^(-iu)|^2 du
 <= [|J|+C X log(2X)] sum |c_q|^2.                           (C6)

It follows directly by expanding and using
|log(n/m)|>=|n-m|/X and the harmonic row-sum bound. Since X<T,
the bracket is O(T). Finally

 sum_(q<=X) (Lambda*Lambda)(q)^2/q = O(log^4 X).              (C7)

For two distinct prime bases this follows by the product of
sum_(p^k<=X) log^2(p)/p^k=O(log^2 X); the one-prime-base terms are bounded
by the convergent prime-power sum with k>=2. Thus, including the prefactor
1/L^2, the right-right squared Hilbert--Schmidt norm is O(TL).

## 3. Gamma times right-Euler, in either order

Keep the natural contour exponentials. After extracting exp(alpha Ld),
the causal Gamma leg becomes

    V(y)=1_(y>0) exp(-2alpha Ly) G0(y).

Its ordinary Fourier transform at frequency Lt is exactly

 H(t)=integral_R V(y)exp(-iLt y)dy
     =(2pi L)^(-1) integral_J Omega(u)/(2alpha-i(u-t)) du.     (C8)

For t in J and endpoints A0,B0 comparable to T,

 |H(t)| <= C [1+log(T/(1+dist(t,{A0,B0})))],
 sup_J |H| + integral_J |H'| = O(log T).                     (C9)

The logarithm can equivalently be replaced by its positive part; J has
length comparable to T. Integration by parts gives the exact derivative

 H'(t)=(2pi L)^(-1){Omega(A0)/(2alpha-i(A0-t))
                  -Omega(B0)/(2alpha-i(B0-t))
                  +integral_J du/[u(2alpha-i(u-t))]}.

The positive 2alpha>1 regularizes the endpoint singularities. No sharp
uncapped Hilbert-transform logarithm is silently bounded by a capped one.

For Gamma on the right of the prime leg, extend the V integration past s.
The added prime argument is nonpositive, hence (C4) pays it. Replace the
middle f(v) by f(s-log n/L). The same Lipschitz cancellation used in (C5)
bounds each prime's error by C ||V||_1/L=O(L^C). The remaining convolution
is exact and equals

 f(s-log n/L) integral_J H(u)exp[iu(Ld-log n)]du.

For the other product order the coefficient is f(t+log n/L), with the same
height multiplier H. The sum of prime coefficients is O(L), so all these
errors retain the exp(alpha Ld)L^C bound.

Set D_H(v)=integral_J H(u)exp(iuv)du. By (C9),
|D_H(v)|<=C log T/|v|. Consequently the exponential-conjugation replacement
can again be made, at squared-integrable error O(T^mu L^C)=o(TL). The main
mixed kernel is, up to fixed constants,

 sum_(n<=X) Lambda(n)/sqrt(n) f(s-log n/L) D_H(Ld-log n),

or its version with t+log n/L. Plancherel, fixing s in the first case and t
in the second, reduces its norm to a height integral over J with weight
|H(u)|^2 and the prime Dirichlet polynomial.

The weighted form of (C6) is

 integral_J |H(u)|^2 |sum_(n<=X)c_n n^(-iu)|^2 du
 <= C [T+X log(2X)log^3(2T)] sum |c_n|^2.                    (C10)

Split each endpoint into dyadic collars down to length one. On a collar of
length T/2^j the weight is O((j+1)^2), and use (C6). Sum j. The two innermost
unit collars have bounded weight O(log^2 T) and are paid by (C6) or by
|P|^2<=X sum|c_n|^2. Since mu<1, the bracket in (C10) is O(T).
Now sum_(n<=X)Lambda(n)^2/n=O(L^2), and Plancherel contributes 1/L.
Both mixed squared Hilbert--Schmidt norms are therefore O(TL).

## 4. Gamma times Gamma

On 0<=d<=lambda, replacing exp(-alpha Ld)G0(d) by G0(d) costs O(L),
by (C4). The resulting causal product errors are O(L^C), hence negligible.
The full, untriangular Gamma operator is a compactly localized Fourier
multiplier with multiplier Omega(u)/L on J, uniformly bounded since
u is comparable to T. Its squared Hilbert--Schmidt norm is O(TL).
Therefore its fourth Schatten norm to the fourth power is O(TL).

Triangular projection is bounded on S4, independently of the discretization
or interval. Here is the continuous-nest passage. Compress the full Gamma
operator to successively finer interval-step subspaces. These compressions
converge in Hilbert--Schmidt norm, hence also in S4. Their strictly triangular
matrices, viewed as step kernels, converge in Hilbert--Schmidt norm to the
causal kernel: away from the diagonal this is conditional-expectation
convergence, while the total integral of the squared kernel on the shrinking
diagonal blocks tends to zero. The finite-dimensional triangular S4 bound
is uniform and therefore passes to this limit. Thus the triangular Gamma
part also has fourth Schatten norm to the fourth power O(TL). Schatten Holder gives
||G_+^2||_HS^2<=||G_+||_4^4=O(TL).

A primary research-paper statement of this standard input is Jonathan
Arazy, On large subspaces of the Schatten p-classes, Compositio Mathematica
41(3), 1980, printed page 299 (the paragraph defining P_T),
https://www.numdam.org/article/CM_1980__41_3_297_0.pdf .
The full primary PDF was opened and this statement checked. Its reference
[6], page 121, is the original background source for the boundedness result.

## Leading-constant scope

The main-term bounds above depend only on a bound for ||f||_infinity, the
common frequency interval of length at most one, and the fixed comparable
height endpoints. Derivatives of f and the gap mu-lambda occur only in
errors that are o(TL) at each fixed f,lambda,mu. Consequently the
bound has a uniformly bounded leading limsup along bounded-height smooth
tapers with fixed widths tending to one:

    sup_f limsup_(T->infinity) ||B_T(f)^2||_HS^2/(TL) < infinity.

The supremum is outside the limsup. No uniform starting height, interchange
of these operations, or width lambda(T) tending to one is asserted.

## Conclusion and scope

The four product rows and the error class prove (C1). The standalone
[regularized Gamma calculation](REGULARIZED_GAMMA_MEAN_SQUARE.md) gives
the detailed scalar estimates used in (C8)--(C10). The following distinctions
are retained:

- The contour signs and both Euler branches in (C2) come from the exact
  zeta functional equation; the nonresonant branch is retained in the error.
- Every full-line extension above keeps the compact middle f and pays the
  causal collars. No arbitrary Schur multiplier estimate is assumed.
- Exponential conjugation is removed only after the causal product, not in
  the original prime branch before multiplying it.
- The mean-value integration is over J. The endpoint weight (C9) is not
  asserted to be globally integrable on the whole real line.
- Bound (C1) does not itself supply a sharp cubic asymptotic, a shrinking-height
  mixed-product estimate, or a critical-line proportion. A finite clipping
  interface and any count application require their separate hypotheses.
  No full fourth trace is claimed here.
