# Independent internal review

The complete proof in `REPORT.md` and the full scalar verifier were independently read. The analytic transfer and the independent directed replay pass.

## Frozen files

- Report: `157290b0f2e2ba11cc0187f798956c978cb1ee6308f9d3d9acc39910315e5d72`.
- Verifier: `615bd2d883ed2ff2e2aa8d5624b204f89bd3a3a298ffde470123ce813d7c7c97`.
- Exact packet: `0cab19992748abf3d4c80789517b9220957f356a25847785e7f1fbbb618c0cef`.
- Exact detector: `5bce21a50b06a0eec005a6c58bd99a7e76f149d521a3588968afeaccce5e46e2`.
- Scientific result: `4fcaac88f0ac328b108e71e5b37e2620abeacc24372e583882def930fed49d83`.

## Proof checks

The source, detector, complete near/far paired-zero partition, all prime powers, Gamma terms and real-pole reserve are unchanged from the cited checked dependencies. The seed 4.8594 follows from the stronger unconditional 4.84 theorem; no unpublished improvement is needed.

For every used height x>=log H, the source stays in the original complete rectangle. The scalar cover below log H is numerical overcoverage only. At each fixed height the isolated pair is nonincreasing in the distance parameter because F''>=0 and its first argument is no greater than its second. Substituting the height-dependent endpoint therefore retains both roots with the correct inequality direction. It does not differentiate the source with respect to height or enlarge the rectangle.

The full scalar has the stated coefficients 1.775, 104, 6037 and 10^-6, with the exact detector and packet hashes checked. Its compact Laplace integrals and outward interval implementation agree with the earlier verified source formulas. The code's bisection covers both closed child intervals and cannot authorize success with an unresolved cell.

The low endpoint, positive denominator and strict endpoint comparison are explicitly checked. The established 4.79 theorem supplies the affine strip for all x>=63; equality of the two widths occurs exactly at x=188/3. Conjugation gives the negative-height statement. There is no dependency cycle.

## Independent replay

The frozen verifier and both input JSON files were copied to a separate directory and run with 160-bit Arb through python-flint 0.9.0 / FLINT 3.6.0. The run terminated with PASS: 350,201 accepted closed cells and 700,401 evaluations on [28,63], with no unresolved interval. Its smallest directed lower margin exceeds 4.26211388847e-9. The generated scientific JSON is byte-for-byte identical to the frozen result above. Floating conversion is used only to select a displayed smallest margin, not to accept a cell.

## Scope

This establishes the stated affine finite-height envelope for |t|>=3e12, combined with the existing classical region. It improves that region only below the stated crossover. It is not a smaller global classical denominator, a percentage of excluded zeros, a proof of RH, external peer review or a global-priority claim.
