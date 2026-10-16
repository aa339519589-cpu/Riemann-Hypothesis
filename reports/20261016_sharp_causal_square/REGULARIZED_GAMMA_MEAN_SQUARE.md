# Regularized causal Gamma multiplier: scalar payments

Research proof-support note, 16 October 2026. This note proves only scalar
multiplier and Dirichlet-polynomial estimates. It does not identify a complete
operator product, establish a fourth Schatten bound, or prove a sharp trace
transfer.

Let L=log T, I=[A,B], where 0<a0 T<=A<B<=b0 T and B-A is comparable to T.
Let c lie in a fixed compact subinterval of (0,infinity). Define

    G(y)=(1/(2 pi)) integral_I log(u/(2 pi)) exp(iuLy) du,
    G_c(y)=1_(y>0) exp(-cLy) G(y).

With convolution Fourier convention integral g(y)exp(-iLt y)dy, its multiplier
is exactly

    H(t)=(1/(2 pi L)) integral_A^B log(u/(2 pi))/(c-i(u-t)) du.       (1)

The positive real part c licenses the ordinary y-integral. Fubini is
absolute since I is finite. There is no sign/factor ambiguity in (1).

## Endpoint and variation estimates

For t in I, freeze log(u/(2 pi)) at u=t. Its difference is at most
C|u-t|/T. The resulting remainder in (1) is O(1/L). The constant-numerator
integral is i times the endpoint difference of log(c-i(u-t)). Hence, writing
d(t)=min(t-A,B-t),

    |H(t)| <= C[1+log(C T/(1+d(t)))].                            (2)

Take the fixed C large enough that the logarithm is nonnegative. In
particular integral_I |H|^2 <= C T. The cap 1+d is legitimate because c is
bounded below; it would not be legitimate for an unregularized sharp
triangular projection.

Differentiation and one integration by parts give the exact formula

 H'(t)=(1/(2 pi L)){
   log(A/(2 pi))/(c-i(A-t))-log(B/(2 pi))/(c-i(B-t))
   + integral_A^B du/[u(c-i(u-t))]}.                            (3)

Since integral_A^B |c-i(u-t)|^(-1)du=O(log T), (3) yields

 |H'(t)| <= C[(1+|t-A|)^(-1)+(1+|t-B|)^(-1)+T^(-1)].           (4)

Thus total variation on I is O(log T). On |t|>=C T the original formula
also gives |H(t)|<=C T/|t|. The square-integrable tail must be retained if
one integrates outside the height projection I.

## Elementary interval mean square

Let P(t)=sum_(1<=n<=N) a_n n^(it), with arbitrary complex coefficients, and
S=sum |a_n|^2. Direct expansion on any interval J of length h gives

    integral_J |P(t)|^2 dt <= [h+C N log(2N)] S.               (5)

Indeed off-diagonal integrals have modulus at most 2/|log(n/m)|,
|log(n/m)|>=|n-m|/N, and 2|a_n a_m|<=|a_n|^2+|a_m|^2.
The resulting harmonic row sum is O(log(2N)). No unproved mean-value
hypothesis or optimized Hilbert inequality is needed.

Divide I into the endpoint-distance collars d<=1 and
2^j<d<=2^(j+1), until 2^j is comparable to T. Equivalently index them
from the largest scale, with h_j comparable to T 2^(-j); each level is
a union of at most two intervals. On it the square of (2) is O((j+1)^2).
Using (5) and summing gives

 integral_I |H(t)P(t)|^2 dt
    <= C[T+N log(2N) log^3(2T)] S.                           (6)

The smallest bounded-length collars satisfy the same bound. In particular,
if N<=T^nu for a fixed nu<1, (6) is O_nu(T S).

For the unregularized endpoint logarithm, not needed in (1), the true
weight log^2(T/d) on d<1 is still payable: |P|^2<=N S and
integral_0^1 log^2(T/x)dx=log^2 T+2log T+2. Thus its extra contribution
is O(N log^2 T)S; silently capping an unregularized logarithm would instead
be an incorrect pointwise step.

For a global version retain the actual far multiplier bound T/|t| and
sum dyadic outside shells. Equation (5) then pays the outside part by
O(T+N log(2N))S. The same proof covers any fixed O(T)-sized enlargement
of I. It does not assert integrability of a globally extended constant-plus-
logarithmic upper bound.

These estimates are input to, not a substitute for, the exact operator
composition and its projection/conjugation identities.
