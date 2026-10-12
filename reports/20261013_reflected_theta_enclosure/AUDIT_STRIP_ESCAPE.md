# Internal audit of unbounded-right spurious zeros in fixed reflected theta cutoffs

Date: 2026-10-13. Reviewed [STRIP_ESCAPE_OF_ARTIFICIAL_ZEROS.md](STRIP_ESCAPE_OF_ARTIFICIAL_ZEROS.md) against the original finite object in [REPORT.md](REPORT.md). This is a mathematical consistency audit done within the project, not an independent external referee or a formal verification. No RH conclusion is claimed.

## 1. Dependency isolation

The theorem needs only four unconditional and explicitly written facts: the Eisenstein theta reflection with \(a=2\pi/\sqrt3\), nonnegative ideal counts \(r(n)\) with \(r(1)=1\) and infinitely many positive coefficients, elementary repeated integration by parts, and standard Hadamard factorization for entire order <=1 functions with finitely many zeros. It uses **neither** any purported finite RH spectral gap nor a low physical bound, the Q hypothesis, off-line zeros or an inverse-zeta assumption.

The original finite approximant is exactly
\(Z_M^S(s)=D_S(s)a^s\Lambda_M(s)/\Gamma(s)\)
where \(\Lambda_M(s)=1/[6s(s-1)]+\sum_{n\le M}r(n)I_n(s)\) with BOTH reflected integrals. The old source, deletion factors and infinite original \(\zeta_K^S\) are not changed.

## 2. An independent sign and phase check of the strip endpoint

For \(s=\sigma+it\), the substitution \(u=e^x\) gives:
\[
I_n(s)=\int_0^\infty e^{-an e^x}
        \big(e^{\sigma x}e^{itx}+e^{(1-\sigma)x}e^{-itx}\big)\,dx.
\]
Call the two real positive amplitudes A and B. Their boundary values coincide: A(0)=B(0)=e^(-an). Their *derivative sum* is
\(A'(0)+B'(0)=e^{-an}(1-2an)\), independent of sigma. With the standard integration-by-parts convention,
\[
\int_0^\infty A(x)e^{itx}dx
=-A(0)/(it)+A'(0)/(it)^2+O(t^{-3}),
\]
\[
\int_0^\infty B(x)e^{-itx}dx
=+B(0)/(it)+B'(0)/(-it)^2+O(t^{-3}).
\]
The first-order contributions cancel; the \(1/(it)^2=-1/t^2\) sign gives
\(I_n(\sigma+it)=(2an-1)e^{-an}/t^2+O(t^{-3})\), **positive leading coefficient**. The remainder is uniform in |sigma|<=B because for each fixed B,n all 0th through 3rd x derivatives of A,B are exponentially bounded by a polynomial in exp(x) times exp(-an exp(x)+(B+1)x), an L1 function.

Multiplication by
\(s(s-1)=-t^2+it(2\sigma-1)+\sigma(\sigma-1)\)
therefore yields the *negative* coefficient \(-d_n\) in the limit. The theta reflection derivative is
\[
2\Theta'(1)+\Theta(1)=0
\Longrightarrow
1/6=\sum_{n\ge1}r(n)(2an-1)e^{-an}.
\]
Consequently the limiting constant is the positive **omitted tail**
\(c_M=\sum_{n>M}r(n)(2an-1)e^{-an}\). The positivity is strict for every finite M because \(r(m^2)>=1\) for every integer m≥1.

The manuscript's (10) sums absolute third derivatives and second-derivative endpoint values on a compact sigma interval. It is a finite, explicit nonnegative constant. The remainder inequality (11) follows from the third integration-by-parts step. With |t|>=B+1, the bound |s(s-1)|<=4t² is valid. Separating the coefficient \(s(s-1)/t²+1\) produces exactly
\(B(B+1)+2B+1\), so (12)-(13) imply a **genuine, computable finite-height** lower bound \(c_M/2\). No unlabeled uniformity in M is used.

## 3. Entire order, reflection and actual existence of infinitely many zeros

On the disk |s|<=R, R>=1, the integrand satisfies
\(|u^{s-1}+u^{-s}|\le2u^R\) for u>=1. Hence
\(|I_n(s)|\le2\Gamma(R+1)(an)^{-R-1}\).
For fixed finite M, \(\log\max_{|s|\le R}|X_M(s)|=O_M(R\log(R+2))\): the entire order is at most one.

The lower bound on the positive real axis is independently checked. For S>a and n=1,
\[
I_1(S)\ge\int_{S/a}^{S/a+1}e^{-au}u^{S-1}du
\ge e^{-S-a}(S/a)^{S-1}.
\]
Since \(X_M(S)\ge S(S-1)I_1(S)\), the function grows faster than every fixed polynomial.

If it had finitely many zeros, Hadamard factorization would be
\(X_M(s)=P(s)e^{\alpha s+\beta}\). Reflection gives
\(e^{\alpha(2s-1)}=P(1-s)/P(s)\). As s runs along the positive real axis to infinity, the rational right side tends to the finite nonzero number \((-1)^{\deg P}\). An exponential in s can have that finite nonzero limit only when alpha=0. Then X_M would be a polynomial, contradicted by its real-axis lower bound. Infinite zero set follows.

By the uniform *nonzero* high-imaginary limit \(c_M\) and analytic isolation, each bounded vertical strip contains finitely many zeros. Hence infinitely many zeros escape every sufficiently large strip. Reflection takes any zero with Re s<-B to a zero with Re s>1+B; zeros escaping to the right are already there. Thus the set of real parts of the zeros is unbounded above. There are in particular infinitely many with Re s>1. Gamma and the finite deleted Euler factors cannot cancel any of these since their zeros/poles lie outside Re s>1. The exact original Dedekind zeta Euler product has no zeros there. This completes the strengthened failure mechanism.

## 4. Separate diagnostic check, not an existence certificate

A 60-digit mpmath calculation was performed locally with the actual a. It gives \(c_1=0.00040393437941625741317\ldots\) and evaluates the **exact** incomplete-gamma formula for \(I_1\). The real parts of X_1 at t=100 for sigma=-2,1/2,2 were, respectively,
\(0.0004007759930301311\),
\(0.0004007701198320544\),
\(0.0004007722355724597\). They all tend towards the same positive c1. At sigma=1/2 the imaginary part was zero as required by exact reflection. These floating-point values check only the sign and vertical-strip asymptotic. They do not numerically certify any remote zero. The existence theorem is analytic.

## 5. Limits of the result and repository compatibility

The new claim is stronger than the last section of REPORT.md: that section already showed infinitely many zeros with Re s>1/2; it did **not** exclude the possibility that all such zeros stay in Re s<=1. The new bounded-strip asymptotic closes exactly that gap. In fact every right half-plane contains spurious fixed-M zeros.

This does not assert a zero on any particular safe vertical line, invalidate the existing *growing-M* finite-height enclosure, or produce a critical signal bound for the genuine original physical probe. The only correct mathematical conclusion is that fixed reflected truncation cannot yield a global zero-free reciprocal half-plane by theta reflection alone.

**Audit verdict: the stronger entire-function/spurious-zero statement is sound given the exact original theta identity; NO NEW UNCONDITIONAL RH THEOREM PROVED.**
