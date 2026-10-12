# Independent review: physical-first multiband compression

This review accompanies [MULTIBAND_COMPRESSION.md](MULTIBAND_COMPRESSION.md) and the two actual interval programs and output certificates in [multiband_certificate](multiband_certificate).

Status: Approved for the full-norm approximation theorem and four actual interval parameter budgets. No new resolvent Gram or spectral sign is certified by these budgets.


## 1. Exact base and physical truncation

The frequency set E contains every point where C_N>(1-sigma)b. On E the new symbol d equals b; outside it d=b-C_N>=sigma b. Its difference from the original b is bounded, including its endpoint jumps. Thus the actual closed operator domain and operator core are unchanged, A>=e, and the full original comparison in (2) holds with the actual prime tail paid in e=epsilon-delta_N. No smooth-window approximation or finite-Gamma omission is hidden here.

The corrected statement explicitly retains 0<epsilon<=1/2 and delta_N<epsilon; this makes the displayed double-logarithmic source bound well-defined. For this bound, d>=sigma b gives A>=sigma B+e. The previously reviewed source estimate at e/sigma, enlarged to its monotone bound at e, justifies (3), alongside the elementary m-infinity bound. Physical multiplication P_R is applied directly to J=mA^-1/2. Therefore ||(1-P_R)J||<=m_tail(R)/sqrt(e), and expansion of the two-sided difference gives exactly 2cM tau_R. There is no assumed spatial localization of a sharp Fourier projection.

Compactness follows independently because h is integrable with compact frequency support, m belongs to L2, and A^-1/2 is bounded. The signed symbol h is never assumed nonnegative.

## 2. Even Fourier normalization and carrier expansion

For the full-line even L2 norm, the unitary positive-frequency transform has coefficient 1/sqrt(pi). This gives Q_R* sign(h) Q_R=P_R h(D) P_R. Its norm is at most sqrt(c). The real Taylor expansion in t about each band center retains the exact potentially large carrier. Its n-th derivative has modulus at most |x|^n on real arguments, so the remainder is (R w)^n/n! with no complex-strip exponential factor. Odd-k terms x^k cos(nu x+k pi/2) are also even. On the central band odd powers vanish, so remainder order 2r costs only rank r.

The Hilbert-Schmidt error is bounded by (2R/pi) sum integral_I |h| beta_i^2. The factor 2R is the full physical interval length and 1/pi is the squared transform normalization. Orthogonality is used only for the disjoint frequency-feature intervals. Combining ||Q_p||<=sqrt(c)+zeta with the physical tail gives exactly (10), including both the linear and quadratic zeta terms and the M^2 factor.

## 3. The actual new finite matrix

The compactly supported carrier-polynomial functions are resolvent input vectors, not vectors asserted to lie in D(B). With their factorials included in phi, the matrix entry is (1/pi) integral_I h(t)(t-nu)^(k+l)dt. This verifies the factorization (12). Only this frequency-feature matrix D is block diagonal. The actual Gram F*A^-1F retains every cross-band entry; no physical prime-shift interaction has been discarded.

The basis may be nonorthogonal or singular as a presentation. The previously reviewed signed one-sided Gram principle still applies after correct enclosures. Endpoint jumps of the new inputs are real and the manuscript explicitly disallows reusing the old analytic-strip input envelope. In particular the executed 373-dimensional Legendre Gram does not certify these new spaces.

## 4. Interval coverage and independent reproduction

The exact positive summand of b is decreasing as a function of j+1/4. Integrating its tail from 32+1/4 proves (13). It is increasing in t>=0. On every dyadic cell the interval cosine upper enclosure for C_N, minus .99 times b_low at the left endpoint, therefore bounds the full symbol on that entire cell. Only strictly negative cells are excluded; unresolved eighth-unit cells are included. This is a full interval cover, not a sampled sign inference. Beyond the initial endpoint, the strict b_low/c_N comparison and monotonicity exclude the entire infinite tail.

Both supplied programs were independently run in a separate independent replay directory. Program hashes are `aaae0276dbdb9b2b01bde9ed1d80b5ddcc64998a12b0e43b357a73069717bf71` for the cover and `4c325f40f6b894bda0857e73924d62c3fe8bfffe5a0da57c8f1b1d9d0717c35c` for the budgets. All assertions passed. The covers agree exactly after removing elapsed-time metadata, and the complete budget JSON is byte-for-byte identical.

The covers have respectively 7,10,60 positive intervals, lengths 110/8,134/8,456/8 and final endpoints 370/8,873/8,12402/8. The actual full-norm upper bounds reproduced are:

- epsilon=1/8: rank at most 58, error 0.0196478295841617 <1/32.
- epsilon=1/64: rank at most 77, error 0.00188179618045155 <1/256.
- epsilon=1/1024: rank at most 127, error 0.000116144798940999 <1/4096.
- epsilon=1/1048576: rank at most 853, error 0.000000107538795534060 <1/4194304.

The script chooses actual R and integer Taylor orders, computes the spatial and feature errors separately with outward intervals, and compares their sum to the exact rational eta. The norm upper constants and the complete-prime remainder remain in that computation.

## 5. General rank scope

For sufficiently small epsilon, the single-interval fallback uses the actual complete b and the same finite-prime norm bound. The stated choices N=O(log(1/epsilon)), T=exp(O(sqrt(log(1/epsilon))loglog(1/epsilon))) and R=O(loglog(1/epsilon)), followed by a Taylor order O(TR+log(1/eta)+log M), give rank epsilon^-o(1) when eta is a fixed power of epsilon. The four arithmetic covers improve actual parameter dimensions without any assumed general distribution of the frequency wells.

This is a new full-original-operator approximation with verified smaller finite spaces. It remains a parameter and norm-tail result: it supplies no new true Gram, interval inertia, deeper gap, all-depth spectral conclusion, or runtime estimate.
