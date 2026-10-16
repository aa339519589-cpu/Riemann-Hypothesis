# Independent internal review

## Reviewed artifacts

The complete report `REPORT.md` was read and checked against its primary inputs. Its SHA-256 is:

`5d567919d25448943964fc7770ae57009b77261a43e2e2aeed7652bc8da66356`.

The two complete verifiers were independently read and replayed in a separate working directory:

- `certify_hpy_constants.py`: `aae9754e8223e007af5b6429c721155e5c83aa1e7e4f992a17eca14cad8512c4`.
- `certify_optimized.py`: `c8ed73d04d4679c6effd198eb76766b8201842b5af48f94892ddff011ad934ab`.

The review found no correction required in the stated theorem or its certificate.

## Mathematical checks

1. **HPY parameter substitution.** The complete argument in §3.4 of [Hiary–Patel–Yang, version 1](https://arxiv.org/abs/2207.02366v1) was checked, not merely its final numerical example. The choice (T=e^{50}), block index 6, derivative-test parameter (4/3), and lower cutoff 1000 satisfies the block and floor constraints. The uniform bounds for the derivative-test coefficients, the harmonic-sum endpoint term and the small-block remainder have the correct directions. In particular, the upper bound for κ multiplies the entire positive bracket (log t/6+\omega); the negative term involving ω is not rounded separately as though it were positive. The estimate (I\leq-2) follows directly from the decreasing-sum integral bound.

2. **Standalone critical-line estimate.** The independent 192-bit replay verifies the reported bounds (b_1<.4467), (b_2<4.940), and (b_3<0), including positivity of that entire bracket at (e^{50}). Consequently the stated estimate ((.4467\log t+4.940)t^{1/6}) holds throughout (t\geq e^{50}), rather than only at the parameter-selection height.

3. **Finite-table and infinite-tail separation.** All 32 constants and their consecutive intervals were compared with Table 1 of [Patel–Yang, version 1](https://arxiv.org/abs/2302.13444v1). Section 3.1 explicitly asserts the bound throughout each listed interval. The exact rational maximum used by the verifier retains the global Theorem 1.1 constant 66.7 for every height above (e^{220}). Neither a finite row nor a sampled value is extrapolated to infinity.

4. **Global shifted boundaries.** Both critical-line boundary choices were checked at every height: the three lower-height ranges, the Euler bound on the compact segment, conjugation, all finite table intervals and the infinite tail. The logarithmic debit in the rational maximum is sufficient even when the shift Q exceeds the height. The other vertical boundary retains Yang's published (5/7)-line estimate.

5. **Interpolation and harmonic integrals.** The exponents and correction factor in the fixed-cell Phragmén–Lindelöf step match [Yang, version 2](https://arxiv.org/abs/2301.03165v2). The resulting power-log estimate holds on the entire half-line beyond the cell's fixed (t_0), so it pays the tails used in the proof of Yang's logarithmic-integral lemma. All 46 harmonics use the same cell-fixed boundary data. No finite-height estimate is silently substituted into an unbounded integral.

6. **Complete local inequality and minimization.** The isolated-zero term, degree-46 detector normalization, right-shift integral, pole and zero-count remainder remain the previously checked complete inequality. The local-count coefficient has the required nonpositive sign. The global infimum argument uses the existing classical 4.82 theorem and published Vinogradov–Korobov bound to establish a genuine zero-free rectangle and an attained violating minimum. It does not assume the proposed 20.1 conclusion. Both low- and high-height splice inequalities are explicitly certified.

7. **Directed acceptance.** Floating calculations select candidate witnesses only. Each accepted interval uses directed Arb inequalities on its full closed extent, including the shift conditions, positive coefficient brackets and remainder cutoff. The independent check also verified that the recorded intervals form an exact contiguous cover of ([64,10^6]). The program restores 160-bit precision after importing the separate 192-bit constant calculation and exits unsuccessfully if a cell remains unresolved.

## Independent replay result

The independent replay completed with exit status zero and reproduced the three scientific output files byte-for-byte:

- HPY constants: `700f3fcc452c299261022666c49abc0fa9bb4898b8fd40f0b4a157190627af76`.
- Continuum summary: `f3795de015bfdac73d622b10d69be3f2da1c036c01c11ef3c6e9581011b5bf83`.
- Full witnesses: `ed0aeb6a51570f040fde2c97e7679cee08d8b3e3d7d0e0d4f4013db2b850fbbf`.

The continuum run accepted 718 cells in 1,420 evaluations, with no unresolved interval. Its smallest directed lower margin exceeds (1.7187136541271\times10^{-6}).

## Scope

This is an independent internal mathematical and computational review, not external peer review or formal proof-assistant verification. It supports the report's explicit zero-free region and its standalone critical-line estimate. It does not prove RH, count a percentage of zeros, assert global priority, or use the unpublished 19.62 input. The already proved classical 4.82 region is the low-height dependency; later classical feedback bounds are not assumed.
