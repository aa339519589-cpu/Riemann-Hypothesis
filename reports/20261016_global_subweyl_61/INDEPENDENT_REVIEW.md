# Independent internal review

The complete proof, both arithmetic modules and exact parameter file were independently read. The global bound |zeta(1/2+it)| <= 61 |t|^(27/164), for |t| >= 3, passes this review.

Reviewed SHA-256 pins:

- `REPORT.md`: `ac7c835fedee860e462cacd6b63abeded81f3544173463f81a731be9248cfcf6`.
- `certify_global.py`: `f843148e8cf280d240952dde851c2a78cb3a1d311cb6db49f4df61e9c15002bd`.
- `unsplit_block.py`: `136a98c0b4156d50791bd03001829bb419c3a316094c18243465fabfdb813f4f`.
- `parameters.txt`: `665b95286320953962e637fabac8a83c8f1aff2e3dcdb58475231d5f703b2d04`.
- `global_subweyl_61.json`: `c23a24a7fa9eb3bc5be8f4b852993f1dd033fea51b7530adf7d778550a34c53d`.

The primary Patel–Yang Theorem 1.1 supplies the same exponent and height range with coefficient 66.7. The primary global Hiary–Patel–Yang bound .618 t^(1/6) log t pays all heights from 3 through exp(60), since its normalized expression increases there and is less than 41.890 at the upper endpoint. The separately reviewed finite unsplit-PY theorem pays the complete closed range exp(60) through exp(220). This review does not infer an exhaustive priority comparison from those two sources alone.

The shared finite-block module was compared with the accepted dependency: its mathematical functions are unchanged, with only the file-writing main routine omitted. An independent 192-bit Arb run from a separate directory passed all 54 closed intervals from log(t)=220 through 1300, with maximum rounded coefficient 60.89. The exact contiguous cover was checked separately. The generated scientific JSON was byte-identical to the supplied result.

The infinite tail is a separate uniform argument. The lower floor comparison, the upper bound on the number of blocks, and the constants q0 and p0 imply the integer conditions 1 <= q <= a for every actual block at every log(t) >= 1300. Their monotone dependence on height has the stated directions. The comparison between the two partition endpoints and the middle-block ratio also persists throughout this range.

The weighted raw-block powers were recomputed before summing: the first two rows combine into a^(5/82)t^(11/82), the secondary row is a^(-17/328)t^(61/328), and the remaining power rows are a^(87/164)t^(-15/82) and a^(-5/246)t^(5/41). The negative-power geometric sum retains the final-block floor factor. After normalization, the secondary row has exactly zero height exponent; the two decaying rows have exponents -27/328 and -427/8364. Thus no increasing term is silently discarded.

The complete logarithmic error is bounded using the exponent 188/697, then by D+Ex. Its block count is at most kx, so its whole normalized contribution is bounded by a constant times x^(3/2) exp(-27x/164), decreasing for x >= 1300. The initial sum, both middle-block series and both Riemann–Siegel remainder terms are retained. The independent directed enclosure of the complete tail coefficient is 59.7041270241269349496032461275537778596232155831693438, with radius below 2.54e-53, hence strictly below 60 and 61.

The four closed ranges overlap and cover every t >= 3; conjugation covers negative t. This is a global explicit function bound, not a zero-count percentage, zero-free theorem, or RH conclusion by itself. Its proof depends on the separately reviewed finite raw-block theorem and the stated published low-height input.
