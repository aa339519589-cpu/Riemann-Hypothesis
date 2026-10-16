# Fourier products of causal Gamma multipliers

Scalar proof-support lemma, 16 October 2026. No continuity of an operator-valued
limit is asserted. Use L=log T, J=[A,B] with positive endpoints and length
comparable to T, Omega(u)=log(u/(2pi)), and

 H_c(t)=(2pi L)^(-1) integral_A^B Omega(u)/(c-i(u-t)) du,

where c>0 is bounded above independently of T. The regularized application
has c bounded above and below. The following unregularized limit is only
used as an explicit scalar locally integrable function.

## Half-diagonal and signs

On the interior of J the distributional boundary limit is

 H_0(t)=Omega(t)/(2L)
          +(i/(2pi L)) PV integral_A^B Omega(u)/(u-t) du.      (1)

This follows from (c-i x)^(-1) -> pi delta_0(x)+i PV(1/x).
In particular Re H_0=Omega/(2L), not identically1/2. The latter is the
asymptotic value because Omega(t)/L=1+O(1/L) uniformly on J.

Writing d_A=t-A, d_B=B-t, d=min(d_A,d_B), both H_0 and H_c satisfy,
away from the endpoints,

 |H_j(t)| <= C[1+log(C T/d)],
 |H_j'(t)| <= C[d_A^(-1)+d_B^(-1)+T^(-1)],  j in {0,c}.      (2)

Constants can be chosen uniform for 0<c<=c_max. For H_c this follows
from the exact derivative formula in the
[regularized Gamma proof](../20261016_sharp_causal_square/REGULARIZED_GAMMA_MEAN_SQUARE.md).
For H_0, freeze Omega at t in (1); the constant-numerator integral is
log((B-t)/(t-A)). Differentiating, or taking the explicit boundary limit
of the derivative formula, gives endpoint reciprocal terms plus

 (1/(2pi L t))[log((B-t)/(t-A))-log(B/A)]

in the imaginary part and 1/(2Lt) in the real part. The logarithm term
is absorbed by the right side of (2), using x log(1/x)<=1/e.

## Oscillatory products

Let F(t) be a product of k<=2 factors chosen from H_0,H_c and their
complex conjugates; k=0 is allowed. For every |v|>=log2,

 |integral_J F(t) exp(itv)dt|
       <= C_k [1+log(C T |v|)]^k/|v|.                       (3)

For k=0 this is the elementary interval Fourier bound. Otherwise delete
both endpoint collars of width delta=1/|v|. For sufficiently large T they
are disjoint. By (2), each collar has integral at most

 C integral_0^delta [1+log(C T/x)]^k dx
     <= C_k delta[1+log(C T/delta)]^k.

On the remaining closed interval integrate by parts. Its boundary terms
are at most C_k[1+log(C T |v|)]^k/|v|. The derivative has modulus at most

 C_k[1+log(C T/d)]^(k-1)
       [d_A^(-1)+d_B^(-1)+T^(-1)],

whose integral over d>=delta is O_k([1+log(C T |v|)]^k).
This proves (3), with every actual endpoint logarithm retained.

## Averaging the regularized diagonal

For c in a fixed positive bounded range,

 integral_J Re H_c(t)dt = |J|/2+O(T/L+log T).                 (4)

Indeed Re H_c is the Poisson integral

 (2pi L)^(-1) integral_J Omega(u)c/[c^2+(u-t)^2]du.

Integrating t first gives arctan((B-u)/c)+arctan((u-A)/c).
The normalized Omega/L differs from1 by O(1/L); the integrated loss from
the limiting angle pi is O(c log(1+T/c)). This proves (4).

The imaginary average is O(T/L) as well: symmetrize the double integral
against u,t and use |Omega(u)-Omega(t)|<=C|u-t|/T. Thus the complex average
also differs from |J|/2 by O(T/L+log T), although (4) alone suffices when
the operator row takes its real part.

These are scalar estimates. Identifying the complete cubic operator rows,
their frequency arguments, and all freezing errors remains separate.
