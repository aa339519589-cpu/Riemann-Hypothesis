# The right-Euler cubic subrow after the causal product reduction

Proof-support note, 16 October 2026. This is only one subrow of a
sharp cubic expansion. It assumes the explicitly stated, independently
checked right-right kernel reduction and its Hilbert--Schmidt errors; it does
not infer a full sharp cubic asymptotic or a fourth bound.

Use the notation of the [sharp causal-square theorem](../20261016_sharp_causal_square/REPORT.md): L=log T,
X=T^mu with fixed mu<1, D(v)=integral_J exp(iuv)du, and smooth bounded
nonnegative compactly supported f. Write d=s-t. The flat right-prime kernel
and the reduced right-right product are

 R0(s,t)=1_(d>0) sqrt(f(s)f(t))/(2pi)
          sum_(k<=X) Lambda(k)/sqrt(k) D(Ld-log k),

 Q(s,t)=1_(d>0) sqrt(f(s)f(t))/(2pi L)
          sum_(q<=X) b_q(t)/sqrt(q) D(Ld-log q),

 b_q(t)=sum_(mn=q) Lambda(m)Lambda(n) f(t+log n/L).

The checked product reduction gives

 ||R^2-Q||HS=o(sqrt(TL)), ||R-R0||HS=o(sqrt(TL)),
 ||R||HS+||R0||HS+||Q||HS=O(sqrt(TL)).                        (1)

The R/R0 norm bound follows directly from the same elementary mean square,
plus the pointwise conjugation error O(sqrt(X) log^C T). Thus (1) shows

    <R^2,R>HS=<Q,R0>HS+o(TL).                               (2)

It remains to prove the reduced inner product is o(TL).

## Causal-domain extension

For d<=0, every right resonance log n is positive, and
|D(Ld-log n)|<=2/log n. The flat prime sum and reduced semiprime sum
are therefore bounded respectively by O(sqrt(X) log^C T) and the same
bound times 1/L, using partial summation and the elementary convolution
bound. Extending the d-integral from d>0 to all d changes <Q,R0> by
O_f(X log^C T)=o(TL). The outer product f(t)f(t+d) keeps this error
integral on a fixed compact set. No exact causal/full-line identity is used.

## The bilinear freezing identity

Uniformly for q,k<=X and t in the support of f,

 integral_R f(t+d)D(Ld-log q)overline(D(Ld-log k)) dd
   =(2pi/L) f(t+log k/L)D(log k-log q)
      +O_f(log T/L^2).                                     (3)

For the constant part this is the exact Fourier projection identity. On a
fixed compact interval containing both centers, the Lipschitz difference
|f(t+d)-f(t+log k/L)| cancels the denominator of the k-kernel, leaving
O(1/L) times the L1 norm O(log T/L) of the q-kernel. Outside that interval
both kernels have integrable O(1/(L^2 d^2)) product. This proves the uniform
error in (3), including centers outside the support of f.

Summing the error in (3), with the 1/(4pi^2 L) outer prefactor, is
O_f(X log^C T)=o(TL), since

 sum_(q<=X) (Lambda*Lambda)(q)/sqrt(q) << sqrt(X)log^C X,
 sum_(k<=X) Lambda(k)/sqrt(k) << sqrt(X)log^C X.

## Diagonal and off-diagonal

The remaining main term is

 (1/(2pi L^2)) integral f(t)
   sum_(q,k<=X) [b_q(t)/sqrt(q)]
       [Lambda(k)f(t+log k/L)/sqrt(k)] D(log k-log q) dt.       (4)

On q=k, Lambda(q) is zero unless q=p^a. Nonzero convolution requires
a>=2, and (Lambda*Lambda)(p^a)=(a-1)log^2 p. Consequently

 sum_q (Lambda*Lambda)(q)Lambda(q)/q
   =sum_p sum_(a>=2) (a-1)log^3(p)/p^a < infinity.            (5)

The diagonal of (4) is therefore O_f(T/L^2), not order TL.

For the off-diagonal,

 |D(log k-log q)|<=2X/|k-q|.

The absolute harmonic matrix has l2 operator norm O(X log(2X)) by its row
sums. For each fixed t, the two coefficient l2 norms are at most

 C_f (sum_(q<=X) (Lambda*Lambda)(q)^2/q)^(1/2)=O_f(log^2 X),
 C_f (sum_(k<=X) Lambda(k)^2/k)^(1/2)=O_f(log X).

The first estimate retains both distinct-prime-base terms and all powers of
a single prime; it is exactly the arithmetic estimate in the checked
right-right reduction. Thus the off-diagonal in (4) is
O_f(X log^4 X/L^2)=o(TL). Together with (2)--(5),

                     <R^2,R>HS=o(TL).                       (6)

Only this all-right-Euler cubic row has been evaluated. The Gamma-containing
cubic rows and their main coefficients remain separate obligations.
