# Independent internal review

The complete proof in `REPORT.md` and both certificate programs were read and independently checked. The mathematical transfer and the directed computation pass this review.

## Frozen inputs

- Report: `aa12f188d060f734a924f9085cb7ea90375080e5ddda442d46f12c53c3ffda96`.
- Main verifier: `c688b0d7fcd76c83bee895731e7fb1419d8cee847978156fde8b250467ff95fa`.
- HPY parameter verifier: `aae9754e8223e007af5b6429c721155e5c83aa1e7e4f992a17eca14cad8512c4`.
- Scalar summary: `21af21cbc772d9f06b6de8548b276d3d68b835e8da712926db992dd3d185d9b3`.
- Closed-cell witnesses: `5412b19f62c331e16612ac3ad3f9fdb6a6ece12d90394d5f7f8b8e0e0c2b6dde`.

## Analytic checks

1. Yang's primary formula (4.65) and the adjacent complete logarithmic-integral formula were reopened. At eta=1/2 the integration ordinate is exactly jt+u/pi, with the factor 1/2 and the full cosh-squared kernel used in the report. The right-hand integral, zero pair, far-zero remainder, pole and negative count coefficient remain those of the previously checked complete argument.
2. Euler summation gives the asserted global bound at every real ordinate, including zero. The two entire tails beyond |u|=100 have the stated upper bound. Negative logarithmic values and logarithmic singularities are not discarded in an invalid direction.
3. The central windows lie above exp(60); their complete logarithmic displacement is less than 10^-22. The chosen table row is a common upper coefficient for every interval touched by all 46 harmonics and the whole closed certificate cell. The finite table is never extrapolated beyond exp(220).
4. The central upper bound is positive, so replacing the central kernel mass by one is lawful. The reserve pays both center displacement and both infinite tails. Since the table coefficient is common, the exact aggregate 3.377 debit is retained without a hidden harmonic-dependent constant. The optional HPY alternative follows from increasing concavity and the same complete tail bound.
5. The inherited global interpolation witnesses retain their all-half-line bounds. Each coefficient multiplying an upper detector constant is checked positive. Smoothing, the genuine global-minimum zero-free rectangle, R>=100 and the discarded count coefficient retain the earlier hypotheses. The 4.79 low-height seed and published VK high-height splice are noncircular and cover the complete stated domain.

## Independent computation

The frozen programs were copied to a separate directory and run with python-flint 0.9.0 / FLINT 3.6.0. The HPY checks passed at 192 bits; the main verifier then explicitly restored 160-bit precision and terminated with PASS: 887 accepted closed cells, 1,758 evaluations, and smallest directed lower margin greater than 1.19182596830e-7.

Both generated scientific JSON files are byte-for-byte identical to the frozen files. A separate rational check verified ordered, gap-free coverage from 64 to 1,000,000. The accepted witness counts are 515 direct finite-table cells, 116 inherited global sub-Weyl cells and 256 inherited discrete-k cells. No optional direct HPY cell is required. Floating proposals and reporting conversions do not authorize acceptance.

## Scope

The conclusion is the stated explicit Littlewood zero-free region with denominator 20.0. It is not a proportion of zeros, a proof of RH, a claim of global priority, or external peer review. In particular, the finite-height input is used only with its separately paid complete integration tails.
