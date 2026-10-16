# Independent internal review

The complete proof in `REPORT.md` was read and independently checked. Its SHA-256 is

`cca52bd0bfe4a9bab37b46e4f98ae8327bd10800a3647bf3e786d2a8276afaa6`.

The following points were verified.

1. **Fixed-order arithmetic input.** Theorem 2 in [Simonic, Trudgian, and Turnage-Butterbaugh](https://arxiv.org/html/2010.10675), explicitly attributed there to Tsang's Theorem 4, allows any fixed positive integer k, T^a < H <= T with a > 1/2, and 0 < h < 1. Taking k=3, H=T, and h=4 pi/log T gives the required sixth moment O(T). The same theorem on [T/2,T] pays the lower endpoint extension. The Riemann--von Mangoldt main increment is bounded on these intervals. This is a fixed-order use, not a uniform assertion for an increasing moment order.
2. **Occupancy discretization.** Each preceding bin of length delta is contained in the integration range, and its two-delta increment contains the following bin for almost every base point. Disjoint preceding bins give the sixth occupancy moment, including all multiplicities and close ordinates. Integer occupancies then give the fifth moment.
3. **Complex Gaussian comparison.** The majorant of f, the complex Gaussian integral, and its bound exp(4 pi A^2) exp(-pi (x_k-x_l)^2) have the stated signs and factors. Real-part separation gives the Schur row bound. The two parity classes correctly convert a per-unit-bin occupancy bound into an operator norm bound.
4. **Fourth Schatten estimate.** On occupancy level r, the operator norm costs O_A(2^r), the trace costs the number of packets, and the fifth occupancy moment leaves a factor 2^(-r). The fourth-root geometric series converges. Schatten Holder gives ||F J F*||_4 <= ||F F*||_4 without assuming the paired operator is positive.
5. **Exact scope.** Conjugate pairing preserves the fixed normalized strip. Hermiticity identifies the fourth trace with the fourth Schatten power; the spectral cubic-tail bound follows by division by R. The constants depend on the fixed A, f, and lambda. Neither uniformity as A grows nor a small fourth-norm remainder outside the strip is proved.

No mathematical correction is requested. This is a bounded-strip fourth-moment and cubic uniform-integrability lemma, including the critical-line suboperator. It is not a full-operator fourth-moment theorem, a sharp cubic trace transfer, or a new zero proportion or exclusion result.
