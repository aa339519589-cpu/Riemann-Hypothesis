# Exact source for the one-source Schur certificate

This file extracts only the source definition and domain facts used by the
certificate. It does not assert positivity on a complement, exclude a negative
eigenstate, or prove RH. No critical inverse-zeta estimate is used.

Put b=log 2, A=16, k=3, nu=9/4, z=pi exp(2x), and

    c(z)=8z^3-30z^2+15z.

The stable density is zero below A. For s>=0 define

    g(s)=(s/16)^(9/8) J_(9/4)(2sqrt(16s)),
    mu=delta_0+exp(-v)[-6+15v-10v^2+(5/2)v^3-v^4/4+v^5/120]dv,
    u(16+s)=integral_[0,s] g(s-v) mu(dv).

Equivalently, and as used in the interval evaluator,

    u(16+s)=s^(9/4) sum_(n>=0) (-1)^n D_n s^n/Gamma(n+13/4),
    D_n=sum_(j=0)^n 16^j/j! binom(5+n-j,n-j).

The positive coefficient formula, complete tail bound, recurrence and complex
disc enclosures are proved in
[FILTERED_COMPLEMENT_VALIDATED_SERIES_INTERFACE.md](FILTERED_COMPLEMENT_VALIDATED_SERIES_INTERFACE.md).
For general notation in that proof, A=16 and 2k=6 here. The Bessel normalization
also follows directly by expanding its defining power series. For that Bessel
series, termwise Laplace integration is absolute for every positive rho.
Combining it with the finite exponentially decaying convolution measure gives

    integral_16^infinity exp(-rho z)u(z)dz
      =rho^(11/4)/(rho+1)^6 exp[-16(rho+rho^(-1))].

In particular u(16+s)=s^(9/4)/Gamma(13/4)+O(s^(13/4)), so this density
is nonzero. No large-argument Bessel asymptotic is needed for the certificate.
The complete real bound used in the infinite arithmetic tails,
|u(16+s)|<=s^(5/4)/4, is proved in
[FILTERED_K3_COMPLETE_PRIME_POLE_DEBIT.md](FILTERED_K3_COMPLETE_PRIME_POLE_DEBIT.md).

The complete original integer row, on each integer branch, is

    W(x(z))=(z/pi)^(1/4)
       sum_(2<=n<=sqrt(z/pi)) (1/n)
       sum_(j>=1)c(j^2 z/n^2)exp(-j^2 z/n^2).

It is the same original row used in every cell, endpoint and tail estimate.
Set

    phi(x)=2z c(z)exp(-z)u(z)/W(x),
    t(x)=1_(x>b) sum_(n>=1)n^(-1/2)phi(x+log n).

The main source has onset x_A=(1/2)log(16/pi)>b. It is C1 there and is
piecewise smooth at all integer knots of W. The complete positivity/lower
bounds and derivative bounds for W needed on the source support are retained
in the Gamma and variation proofs, including the far wing. They give Gaussian
source tails. Thus the main source and its complete future sum belong to the
original logarithmic Gamma source domain. The single sharp cut at b is legal
in that domain; no H1 boundary condition is imposed. The complete mixed force
of t on (0,b) is L2 by the mixed-column proof.

The operator and form conventions are those of the already published
[original source Schur form](../20261014_original_seed_schur/SOURCE_SCHUR.md)
and [unrepaired original head certificate](../20261014_unrepaired_original_head/REPORT.md).
In particular the sign theorem concerns the UNCORRECTED t above. An optional
neutral tail gauge appearing in the Gamma component note is not applied in
the mixed columns or augmented Schur assembly; the component proof explains
why its conservative lower bound also holds for this uncorrected source.

The completed result is exactly S0[t]>=10^(-9) for this one explicit t.
