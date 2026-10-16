# Independent internal review

## Final artifacts

The complete report, mathematical certificate and read-only verifier were independently read. The reviewed SHA-256 hashes are:

- `REPORT.md`: `e299cfe3e040670dccda474498c35ea95302893021ff197810a66ba3d754d206`.
- `frontier_next8192_certificate.json`: `4b78ce67f33f7aab86411d5d6bcd15674e570434ece4cf0befb549c502b1d3e4`.
- `verify_native_block_certificate.py`: `db9e2ff689b9d730e1b3dddd44809f2d803db6b8b6d106b2a19ca765c4c7a620`.

The report's pending-replay banner was removed after the successful replay below; no mathematical statement, certificate input or verifier changed.

## Proof and source checks

The acceptance uses the documented rigorous FLINT 3.6.0 consecutive-zero contract, previously checked against the official documentation and isolation/refinement implementation. A full returned block supplies a critical-line zero in every enclosing ball. This is not an assumption based on a numerical root search or on an approximate ordinate.

The verifier independently recomputes both all-zero counts, including multiplicity, and both nonzero outer Hardy-Z signs. It checks exact positive outer endpoints and strictly ordered, pairwise disjoint dyadic brackets. Its two fresh 4,096-index calls start at the exact successive indices. Every call must return its full requested count, and each new higher-precision ball must lie strictly inside the corresponding stored bracket. Overlap alone does not pass. The generating enclosures are not reused as existence evidence.

Consequently the 8,192 distinct bracketed critical-line zeros exhaust the exact total-count increment. Each is simple, and no additional off-critical zero is present in the stated half-open interval. The report correctly distinguishes critical-line endpoint nonvanishing from off-critical endpoint exclusion: the latter follows from exhaustion at the upper endpoint and the previous coverage at the lower endpoint.

The exact endpoint arithmetic was independently checked:

- Lower endpoint: `384022443823399/128`.
- Upper endpoint: `3072179552547071/1024`.
- New height increment: `1959879/1024`.
- Cumulative increment above the cited Platt–Trudgian endpoint: `11759871/1024`.

The unchanged preceding certificate contributes 40,960 zeros; the new interval adds 8,192, giving 49,152 without double-counting.

## Fresh independent replay

The complete read-only verifier was run independently at 256-bit precision with four native threads, using official python-flint 0.9.0 / FLINT 3.6.0. Generation had used 192 bits. Both fresh 4,096-index calls returned fully, and all 8,192 strict containment checks passed.

The replay terminated with exit status zero and `PASS` after approximately 228.890 seconds. The independently recomputed all-zero counts were exactly:

`12363153478098 -> 12363153486290`.

The replay output pins the certificate and verifier hashes listed above. The result is a terminal full replay, not an intermediate progress count or a partial return.

## Scope

The review supports the report's finite interval certificate and its cumulative extension of the explicitly cited Platt–Trudgian coverage. It does not assert a worldwide computational record, an asymptotic proportion, RH, or a proof-assistant verification. Its numerical trust base is the documented rigorous FLINT/Arb implementation, official binary dependencies, compiler and ordinary hardware. A larger requested precision alone never substitutes for the explicit containment and completeness checks.
