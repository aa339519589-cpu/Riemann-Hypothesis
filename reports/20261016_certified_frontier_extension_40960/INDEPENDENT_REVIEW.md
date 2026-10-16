# Independent internal review

The complete report, the read-only verifier, the exact scientific input, and the documented official-library contracts were independently checked. Final package pins:

- `REPORT.md`: `9070728d24eb270cd9400f23712d1afa06d5bfc1ee52fc2e9baf801de5ce4bd7`.
- Compact certificate: `59cbceecc43b44a94adaa31b26ee0fadd6fe24a25e94c0acc473c651db84c104`.
- `verify_native_block_certificate.py`: `db9e2ff689b9d730e1b3dddd44809f2d803db6b8b6d106b2a19ca765c4c7a620`.

## Full independent replay

A fresh replay used 256-bit arithmetic, four native threads, python-flint 0.9.0 and FLINT 3.6.0. It independently recomputed both total-zero counts and both nonzero Hardy endpoint signs. All 32,768 exact dyadic brackets were strictly ordered and disjoint inside the claimed interval. Eight consecutive 4,096-index calls each returned the full requested number of rigorous zero balls, and every fresh ball was strictly contained in its corresponding bracket. The run terminated with PASS after 988.829 seconds.

The exact interval and total counts were

- `(1536089771373645/512, 384022443823399/128]`;
- `12363153445330` to `12363153478098`;
- difference `32768`.

The expensive fresh replay read the original certificate at SHA256 `4d251406be887dddbda99952e58c146ff44150d5ef1c418b6ba0f4b526c83d22`. Independently, every field read by the verifier was compared exactly with the compact certificate: both endpoints, counts, number of roots, first index, endpoint signs, generation precision and all 32,768 lower/upper bracket pairs agree. Only unused provenance and native strings were removed. Thus the replay certifies exactly the same mathematical input as the compact file; no approximate overlap or provenance assertion replaces a check.

## Proof and implementation checks

The official FLINT consecutive-zero contract supplies a Hardy-Z zero in every returned enclosure. Exact total-zero counts include all nontrivial zeros with multiplicity, not just the located critical-line zeros. Existence in disjoint brackets and exhaustion of the total count therefore imply completeness and simplicity. The report correctly distinguishes nonzero Hardy endpoint values from exclusion of an off-critical endpoint zero; count exhaustion and previous coverage supply the latter.

The wrapper requires full return and strict containment, rejects nonfinite balls, and requires replay precision above generation precision. It uses opaque FLINT allocations rather than guessed C structure layouts. Stored native-enclosure strings are never used as proof inputs. The earlier failed one-shot generation is not part of this accepted certificate. Requested precision is not assumed to imply a ball-width bound.

Combining this batch with the unchanged 8,192-zero certificate gives 40,960 additional simple critical-line zeros above the exact Platt--Trudgian endpoint, without double counting the initial 32. The total height increment and rational upper endpoint were checked.

No mathematical correction is requested. Acceptance relies on the stated rigorous FLINT/Arb implementation and ordinary compiler/binary/hardware trust. This is a finite certified extension, not an asymptotic percentage, a worldwide computational record claim, an integer-only Turing transcript, a Lean-kernel proof, or RH.
