# Independent internal review

The complete mathematical report, finite verifier and portable source/data package were independently reviewed. The final report delta was checked after the full draft read. Final SHA256 pins:

- `REPORT.md`: `d783b151b937ae8cbdb1932d40b3beed1735e082458798f26fa907d8c3654dd5`.
- Complete C++ verifier: `19f8d5fa97135fed3564b282a1c1af121bcf711e5c258cccb9a108a00b39d297`.
- `code/PACKAGE_MANIFEST.json`: `6fc112f2096192895e686737432afd5febbde4d7f4eea3385f42f4140ede5031`.
- `verification/VERIFICATION_RECORD.json`: `a5249b6de5ce8c1913c7c2aa9e62f9feaa7de2182578c2ed761cd946b46df24e`.

## Analytic and exact-input checks

The existing unconditional rank/energy certificate principle and its smoothing normalization were checked against the cited primary paper. The nine-point extension is a direct counting argument: each index-distance pair receives capacity at most two, each gap receives total pressure at most B, and the frame and kernel perturbations retain the stated finite boundary and vanishing-error debits. The separated-block majorant is Lambda divided by the smoothed mass, not an unnormalized Lambda. The close-pair estimate and the positive gap below the clipping threshold are separately paid. No numerical search assertion from the cited paper is used as a premise for the new all-gap inequality.

The window coefficients, zero mass of each cosine perturbation, positive density, exact Montgomery--Taylor quadratic formula, lower energy floor, pair capacities, pressure sum and final rational were checked. An independent 192-bit side-condition replay passed. The resulting exact rational is strictly larger than the explicitly identified attempt-024 comparator. This is a small improvement in an asymptotic simple-critical-line lower proportion, not a percent-scale exclusion or RH.

## Complete finite certificate

The scalar and derivative builders use outward ball enclosures, including a whole-cell third-derivative remainder. The upper-curvature certificate is a separate all-cell upper check, not an inference from a lower bound. Supporting 160/320-bit full-table replays agree byte-for-byte. The lower-hull argument was checked at source level: its exact endpoint lines encode the whole-cell Taylor support, and exact convex-hull queries take a valid minimum over every cell in the requested range. Sampled hull tests are only debugging and are not used as a proof.

The independently replayed tree covers all 48 roots through 10,702 splits and 10,750 unpaid leaves. Every former checkpoint is expanded. Outward grid conversion, the new-precover inclusion, DBM closure, pressure contractions, and paid-pair collar contractions preserve every unpaid point. Imported anchors propose slopes only. All actual supports are recomputed with the new tables.

Transportation acceptance checks every nonnegative edge flow, node balance and cost. Convex acceptance uses a certified integer Hessian lower bound and an exact positive congruence test; floating values merely propose a matrix or a split. Fixed-input signed-128-bit bounds and guards were checked. No LIMIT or unresolved cell counts as success.

## Independent exhaustive replay

A separately compiled copy of the frozen C++ verifier completed with exit zero and PASS:

- reward 867000 / 100000000;
- 5,324,457 visited nodes;
- pressure 780, basic 87,078, affine 954,828, convex 26,942;
- symmetry 959, empty 42,462, maximum stack 10,750.

Every terminal counter exactly matches the author's completed run. The independent run took 255.087 seconds. A separate full undefined-behavior/signed-overflow sanitizer replay also passed with the same counters and no diagnostic. These runtime checks supplement, rather than replace, the source-level coverage and integer bounds.

## Portable reproduction and final pin

Every shipped source/data manifest entry was checked against its byte length and SHA256. The cleaned scientific input was independently compared with all seven original mathematical fields; removed historical proposal fields are not proof inputs. The geometry unpacker and Python checks were read, and the final wrapper rejects optimized Python before any assertion-based verification. The final clean wrapper invocation regenerated all scalar/jet cells, certified all upper-curvature cells and side conditions, checked every generated scientific hash, and exited zero after the same exhaustive PASS. Its complete transcript was checked against the staged copy. The unsuccessful earlier invocation affected by a live wrapper edit is not counted as a successful reproduction.

The independently compiled run used g++ (Debian 14.2.0-19) 14.2.0 with `-O3 -std=c++17`. Its staged complete log is byte-identical to the independent original. The added final definitions of the clipped-square function and unconditional rank/energy inequality agree with the primary theorem and give the stated final objective algebra. No mathematical revision is requested.

## Trust and scope

The proof uses the identified analytic theorems, rigorous Arb arithmetic, the audited exact-integer program, ordinary compiler/hardware, and the explicit source/data package. It is not a Lean-kernel verification of the new theorem. The geometric hints carry no trusted acceptance flags. A publication comparison is only with the precisely identified checked baseline, not a claim to have excluded every unlocated result.
