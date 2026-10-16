# Independent internal review

The complete proof and scalar verifier were independently read. The Littlewood denominator 19.875 theorem passes this review, using the separately established finite unsplit-PY table and the retained complete local inequality from the finite-strip 19.95 proof.

Reviewed SHA-256 pins:

- `REPORT.md`: `9bf1fa3fea9b2ca10d0092d7eabb137cb0bb8577cc0c6e360599358ffeacfe1c`.
- `certify_transfer.py`: `c0155ecbca106409e79f68dbfcef6ae7a0482ed98a46e6c33a1176f2dddf8770`.
- `transfer_19.875.json`: `a6845a2fa30b2c494066cb8acff553570a5d7d412868f8bc08169980c7df3135`.
- `transfer_witnesses_19.875.json`: `a980a1929d3e8d2735c0002f43d7f2b4a3910f0da0842d2d75b2675892075fe9`.

The inherited Yang detector inequality retains all zero, reflected-zero, pole, right-integral and zero-count contributions. Only the paid critical-line input changes. All 32 exact coefficients in the script agree with the independently reviewed finite table. Their monotonicity allows one common coefficient for every interval reached by all 46 harmonic rectangles in a closed height cell. The upper table endpoint and every transition are checked explicitly; no coefficient is extended beyond its stated height range.

The finite-strip argument remains valid after lowering the initial log height to 63. Every lower vertical endpoint exceeds exp(60), the logarithmic shift is below 1e-22, and the complete central integral lies within the barrier's paid region. The horizontal Euler bound and positive harmonic barrier cover the full rectangle. The complete two-sided infinite integral tails are bounded by 2 exp(-200) times 323.5. The three debits fit below 1e-20. The concave increasing critical and right-boundary functions have derivatives below one, and using the same critical coefficient for every harmonic justifies the source's 3.377 weighted logarithmic saving and Jensen's log(V) term.

Outside the finite range only the previously checked full-half-line integer-k witnesses are used. The program checks both multiplied bracket signs, every rectangle parameter condition, R >= 100, and strict positivity of the complete margin. Floating arithmetic selects a proposed witness; all acceptance inequalities use outward Arb intervals. The fixed detector enclosure is not replaced by a new unverified detector.

The minimizing-zero argument is not circular. The classical 4.79 theorem supplies the low-height splice and the possible t-1 sliver; the published Vinogradov–Korobov 55.241 theorem supplies the entire high tail. A violating positive infimum is attained in the remaining compact range. Its global minimality supplies the required rectangle, with all scalar replacements made in the inherited monotonic directions. The checker verifies both splices.

An independent run from a separate copy using 160-bit Arb arithmetic completed with PASS: 996 closed cells, 1,976 evaluations, 731 direct-table witnesses and 265 inherited integer-k witnesses. The minimum directed margin exceeds 5.6144572076530e-7. Both scientific JSON files were byte-identical to the supplied outputs. The exact rational endpoints were separately checked to form a gap-free cover of [63,1000000].

The conclusion is the stated zero-free region for every |t| >= 3, with conjugation covering negative heights. It does not use the separate global coefficient 61, assert a critical-line proportion, or quantify a percentage of zeros removed. This is an independent internal mathematical and computational review, not external peer review.
