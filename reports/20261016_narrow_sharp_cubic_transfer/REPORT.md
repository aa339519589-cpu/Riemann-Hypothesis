# Sharp cubic trace in the narrow density-paid range

16 October 2026. Derived proof-support result. No novelty claim, new
critical-line proportion, full-band fourth moment, or spectral absolute-third
moment is asserted.

## Statement

Let f be a fixed smooth, even, nonnegative probability density, compactly
supported in an interval [-lambda/2,lambda/2], where lambda<4/7. Put

    K(z) = integral f(u) exp(2 pi i u z) du,
    L = log T,
    z_rho = [gamma-i(beta-1/2)] L/(2 pi),  rho=beta+i gamma.

All zero labels include multiplicities. Fix 0<a<b. On L2 of the frequency
interval, form the finite Hermitian packet operator

    A_T(s,t) = sqrt(f(s)f(t))
                sum_(aT<gamma<=bT) exp(i L [gamma-i(beta-1/2)](s-t)).

The pairing rho with 1-conjugate(rho) makes this kernel Hermitian. Then,
unconditionally,

    tr A_T^3 / [T log T/(2 pi)] -> (b-a) D(f),                (1)

where

    D(f) = integral f^3
           +3 double-integral |s-t| f(s)^2 f(t) ds dt.        (2)

The logarithm in every packet is log T, not log gamma. The result concerns
the signed cubic trace, not the sum of absolute eigenvalue cubes. Its range
lambda<4/7 is insufficient for the near-unit probability window used in the
published competitive proportion certificate.

## Primary arithmetic inputs and the absolute majorant

Choose fixed theta<4/7, integer p>1 and kappa<1 so

    lambda<theta'=theta(1-1/p),  lambda/theta'<kappa<1.

The uniform near-line density bound is

    N(sigma,U) <<_theta U^(1+theta(1-2sigma)) log U,

uniformly sigma>=1/2. A primary statement and proof are in Baluyot's thesis,
Theorem 1.2.1 and Chapter 3:
https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320 .
The fixed-order microscopic count moments follow from Tsang's theorem as
restated in Theorem 2 of Simonic--Trudgian--Turnage-Butterbaugh:
https://arxiv.org/abs/2010.10675v1 .
No growing moment order is used.

Here are the exact consequences needed below. They hold for all zeros of
both ordinate signs in |gamma|<=U, with U>=T^kappa, and use the same L.
Let c_i count labels in bins of real normalized width one, and d_i^(j) count
those labels with j<=|(beta-1/2)L/(2pi)|<j+1. Writing R=log U/L,

    sum_i c_i^q <<_q U L(1+R)^q,
    sum_i d_i^(j) <<_theta U log U exp(-4 pi theta j R).      (3)

The first bound follows by preceding-bin injection into the fixed microscopic
increment moment with h=4pi/L, then dyadic summation in actual height. The
finitely many low zeros contribute a fixed constant. The second follows from
the uniform density bound and symmetry; a left limit handles a strict source
counting convention.

For w(m)=(1+|m|)^(-1), the discrete kernel

    k(m,n)=w(m)w(n)w(m-n)

has finite total mass K0. For d_i<=c_i, Holder and Jensen give

 sum_i d_i sum_(m,n) k(m,n)c_(i+m)c_(i+n)
   <= K0 (sum_i d_i)^(1-1/p)(sum_i c_i^(2p+1))^(1/p).        (4)

Indeed, after Jensen, shifted Holder with exponents 2p+1,
(2p+1)/p,(2p+1)/p bounds the sum of c_i c_(i+m)^p c_(i+n)^p.
Also sum_n w(n)w(n-m)<<log(2+|m|)/(1+|m|), proving K0<infinity.

The BV Fourier estimate is

    |K(x+iy)| <= C_f (1+|y|)exp(pi lambda|y|)/(1+|x|).

For a cubic cycle, the sum of the three imaginary differences is exactly
twice the range of its three imaginary coordinates. Assigning a cycle whose
largest |Im z| is in [j,j+1) to a maximal-band label therefore bounds it by

    C(1+j)^3 exp(4pi lambda(j+1)) k(m,n).

Apply (4) and (3). The resulting band contribution is at most

    C U L(1+R)^3 (1+j)^3 exp[-4pi(theta' R-lambda)j].

Since R>=kappa, the exponential gap is uniformly positive. Consequently

 sum_(|gamma_i|,|gamma_j|,|gamma_k|<=U)
   |K(z_i-z_j)K(z_j-z_k)K(z_k-z_i)|
      << U L(1+log U/L)^3.                                  (5)

For any fixed C>0 the same argument gives an exponentially decaying
max-imaginary tail on |gamma|<=CT. On a fixed bounded imaginary strip,
cycles touching a set E of M labels have absolute sum at most

    C_A M^(1-1/p)(T L)^(1/p).                               (6)

Combining the tail with (6), cycles meeting o(TL) labels are o(TL).
The constants are uniform for a fixed prefix C. In particular, boundary
intervals containing O(epsilon TL)+O(log T) labels contribute, after
normalization, a quantity tending to zero as epsilon tends to zero, with T
sent to infinity first. This conclusion does not assert spectral uniform
integrability.

The full derivations of (3)--(6) were independently written and checked in
[the comparable-height proof](DYADIC_ABSOLUTE_CUBIC_TAIL.md) and
[the same-normalization prefix proof](UNIFORM_PREFIX_CUBIC_MAJORANT.md); the proof
above records their complete inputs and the short discrete argument.

## Real-height sharp approximation

Choose a nonnegative Schwartz entire function k with integral one and smooth
compact Fourier support. For example, square a real Schwartz inverse Fourier
transform of a smooth compactly supported function, then normalize. Define

    k_eta(x)=eta^(-1) k(x/eta),
    h_eta=1_[a,b]*k_eta.

For each fixed eta>0, h_eta is an allowed Rudnick--Sarnak height function;
its Fourier preimage is smooth and compactly supported. On the real axis
0<=h_eta<=1. Away from fixed epsilon-neighborhoods of a,b,
h_eta converges uniformly to 1_[a,b] as eta tends to zero.

Fix C>b+2. On the prefix |gamma|<=CT, telescope the three height factors.
Terms for which a label belongs to an epsilon-boundary interval are paid by
(6) and the imaginary tail. All remaining terms are bounded by the uniform
height-factor error times (5), hence are at most TL times r(eta,epsilon),
where r tends to zero as eta tends to zero at fixed epsilon.
The Riemann--von Mangoldt formula gives O(epsilon TL)+O(log T) labels in
the two boundary intervals. Endpoint choices change only this same paid set.

Outside the prefix, the sharp product is zero. For max|gamma| in
[2^m CT,2^(m+1)CT], at least one smoothed height factor is at most

    C_M eta^(M-1)(1+2^m C)^(-M),   0<eta<=1.

The other two factors are at most one. Applying (5) at U=2^(m+1)CT and
summing m gives an O(eta^(M-1) TL) bound for any fixed M>2, uniformly in
large T. This includes both signs of the ordinate and all low-height labels
inside the original prefix; no separate changed-logarithm argument is used.

Thus, first taking T to infinity, then eta to zero at fixed epsilon, and
finally epsilon to zero, the real-height smoothed cubic and the sharp cubic
have the same normalized limit.

## Analytic-height replacement

The primary theorem uses h_eta([gamma-i(beta-1/2)]/T), not h_eta(gamma/T).
For each fixed eta and every fixed M,

 |h_eta([gamma-i(beta-1/2)]/T)-h_eta(gamma/T)|
   <= C_(eta,M) T^(-1)(1+|gamma|/T)^(-M).

This follows from the derivative bound on a fixed complex horizontal strip
and |beta-1/2|<=1/2. Telescope the three factors, using bounded rapidly
decreasing bounds for the remaining analytic and real factors. Bound (5)
and the dyadic maximum-height summation then give O_eta(log T), which is
o(T log T). No positive-real-diagonal replacement is assumed silently.

## Primary trace coefficient

Rudnick--Sarnak, Theorem 3.1, equations (3.2)--(3.9), printed pp.19--20:
https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/rudnick-sarnak.pdf .
The theorem sums unrestricted zero indices with multiplicity. For the cycle,

    xi=(u1-u3,u2-u1,u3-u2),
    sum |xi_j|=2(max u_j-min u_j)<=2lambda<2.

The common-translation fiber has unit Jacobian in plane coordinates. The
pushforward is smooth and compactly supported strictly inside the support
diamond; a smooth extension off the zero-sum plane is an ambient C^1 test.
Its zero value is integral f^3. Each of the three disjoint-pair lines gives

    integral |r| integral f(t)^2 f(t+r) dt dr
      = double-integral |s-t| f(s)^2 f(t) ds dt.

There is no extra coincidence correction: it is already included by the
unrestricted primary sum. Hence that theorem gives

 cubic_analytic(h_eta)/(TL/(2pi))
       -> D(f) integral h_eta(x)^3 dx.

Since integral h_eta^3 -> b-a, the two fully paid replacements prove (1).
The RH-only sharp Theorem 3.2 is not invoked.

## Scope

This closes sharp cubic transfer only in lambda<4/7 by the established
uniform near-line density input and fixed-order local count moments. It does
not establish the all-prefix fourth hypothesis from a conditional
wide-window transfer argument. Nor does it control the full operator's absolute spectral
third moment, prove a near-unit fourth bound, or improve the accepted
critical-line proportion. No claim of novelty over the literature is made.
