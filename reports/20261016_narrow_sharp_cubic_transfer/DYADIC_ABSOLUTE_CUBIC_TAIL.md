# Absolute cubic-cycle tails in a fixed narrow window

16 October 2026. Derived proof-support lemma. No novelty claim, full-width
estimate, spectral absolute-third-moment estimate, or proportion improvement
is asserted.

## Statement and conventions

Fix 0<lambda<theta<4/7. Let f be a fixed compactly supported BV function,
with support in [-lambda/2,lambda/2], and put

    K(z) = integral f(u) exp(-2 pi i u z) du.

List all nontrivial zeta zeros rho=beta+i gamma with T<gamma<=2T, including
multiplicity. Write L=log T, delta=2 pi/L,

    x_rho = (gamma-T)/delta,     a_rho = (beta-1/2)/delta,
    z_rho = x_rho+i a_rho,      Nscale = T log T.

The Hermitian conjugate-packet operator uses the permutation pairing rho with
1-conjugate(rho). Its cubic trace, when this realization is used, is the sum
of K(z_j-z_i) K(z_k-z_j) K(z_i-z_k). The lemma below bounds the absolute
values of these summands, and does not identify them with the absolute cubes
of the operator's eigenvalues.

There are constants C,c>0 depending on f,lambda,theta such that, uniformly for
all sufficiently large T and every A>=1,

    sum_{i,j,k: max(|a_i|,|a_j|,|a_k|)>=A}
        |K(z_j-z_i) K(z_k-z_j) K(z_i-z_k)|
      <= C Nscale exp(-c A).                                      (1)

The unrestricted absolute sum is O(Nscale). Moreover, if E_T is any sublist
of o(Nscale) labels, the absolute sum of all cycles meeting E_T is o(Nscale).
All claims are restricted to this single comparable-height range with the
same normalization L=log T.

## Arithmetic inputs

Two established uniform statements are used.

1. For every fixed integer q>=1, if c_i counts all labels in the real unit bin
   [i,i+1), then

       sum_i c_i^q <<_q Nscale.                                   (2)

   This follows from the fixed microscopic increment moments in Theorem 2 of
   Simonic--Trudgian--Turnage-Butterbaugh,
   https://arxiv.org/abs/2010.10675v1, which restates Tsang's moment theorem.
   Choose a fixed even moment at least q, H=T and h=4 pi/log T. For a label
   bin, the immediately preceding bin's interval [t,t+2 delta] contains that
   entire label bin. Integrating over that preceding bin gives (2), using
   the Riemann--von Mangoldt formula and the bounded main-term increment.
   The lower end is covered by the same theorem on [T/2,T]. The threshold
   may depend on the fixed q; no uniform-in-q assertion is needed.

2. Let d_i^(j) count the labels in bin i with j<=|a|<j+1. Then

       sum_i d_i^(j) <<_theta Nscale exp(-4 pi theta j).             (3)

   This is the uniform near-line density theorem, for any fixed theta<4/7,
   as stated and proved in Baluyot's thesis, Theorem 1.2.1, printed page 16:
   N(sigma,U) <<_theta U^(1+theta(1-2 sigma)) log U, uniformly sigma>=1/2.
   Apply it at U=2T and sigma=1/2+2 pi j/log T, and use symmetry about the
   critical line. At j=0 use the ordinary total count. For j beyond the
   available imaginary range the left side is zero. Multiplicity is included.
   Primary thesis:
   https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320

## A discrete cycle estimate

Set w(m)=1/(1+|m|) and

    k(m,n)=w(m)w(n)w(m-n),       K0=sum_{m,n in Z} k(m,n)<infinity.

Indeed, sum_n w(n)w(n-m) is O(log(2+|m|)/(1+|m|)), by splitting at distances
|m|/2 from 0 and m and then summing the remaining tail. Multiplication by
w(m) and summation over m proves finiteness.

For any finite nonnegative integer sequence c_i, any 0<=d_i<=c_i, and any
fixed integer p>1, put

    S_i=sum_{m,n} k(m,n)c_(i+m)c_(i+n).

Then

    sum_i d_i S_i
      <= K0 (sum_i d_i)^(1-1/p) (sum_i c_i^(2p+1))^(1/p).          (4)

First apply Holder with measure d_i. Jensen for k/K0 gives

    S_i^p <= K0^(p-1) sum_{m,n} k(m,n)c_(i+m)^p c_(i+n)^p.

Since d_i<=c_i, shifted Holder with exponents 2p+1, (2p+1)/p and
(2p+1)/p bounds every sum_i c_i c_(i+m)^p c_(i+n)^p by sum_i c_i^(2p+1).
This proves (4), with no bound on the largest individual occupancy.

## Fourier growth and the tail sum

The zero extension of f has finite variation. The elementary L1 bound and
integration by parts against its distributional derivative imply

    |K(x+i y)| <= C_f (1+|y|) exp(pi lambda |y|)/(1+|x|).           (5)

The exponent in a three-cycle is not the product of three separate strip
maxima. Exactly,

    |a_i-a_j|+|a_j-a_k|+|a_k-a_i|
      = 2(max(a_i,a_j,a_k)-min(a_i,a_j,a_k)).

Consequently, when max|a| lies in [j,j+1), the product in (1) is at most

    C_f (1+j)^3 exp(4 pi lambda(j+1))
       w(bin(i)-bin(j))w(bin(j)-bin(k))w(bin(k)-bin(i)).             (6)

Replacing real differences by bin differences costs a fixed constant only.
Assign each such triple to one of its at most three maximal-band labels.
For that anchor, use d_i=d_i^(j) in (4). Other labels may then be enlarged to
all c_i, because the sum is positive; the strip growth factor in (6) was
applied before this enlargement. By (2)--(3), the contribution is bounded by

    C Nscale (1+j)^3
       exp(-4 pi [theta(1-1/p)-lambda] j).                         (7)

Choose p once so theta(1-1/p)>lambda. Summing (7) over j>=floor(A) gives
(1), with any smaller positive exponential decay constant. Summing from j=0
also proves the unrestricted O(Nscale) claim.

## Vanishing-count deletions and scope

For fixed A, cycles confined to |a|<=A and meeting a set E of M labels have
absolute sum at most

    C_A M^(1-1/p) Nscale^(1/p),                                  (8)

by (4) with d_i the number of E labels in bin i, and by assigning one of the
three possible E anchors. Thus M=o(Nscale) makes (8) negligible. The remaining
cycles are controlled by (1). Taking T to infinity first and A to infinity
second proves the deletion claim.

In particular a shrinking real-height boundary of o(Nscale) labels is harmless
inside a fixed comparable-height region. This does not yet prove a global
analytic smoothing passage over all real heights, does not provide a fourth
Schatten bound, and does not extend to lambda near one. The positivity used
above is that of the absolute cycle majorant, not positivity of the signed
zero operator. No assumption that all zeros are critical is made.
