# Independent internal review

The complete report `REPORT.md` was independently read, together with the full verifier and the primary analytic inputs. Reviewed SHA256 pins:

- Report: `cd20a4bba017507a333505a03a62e676725a956e4afe2b4d3bee72b49927df35`.
- Verifier: `b950b47af2ac8457cbd40079886fccdd853dfb2d06b1f2edd0ed2c1a050f0ce6`.

## Checks

1. Hiary--Patel--Yang, arXiv:2207.02366v1, Theorem 1.1 and the final display of Section 3.4, give the two cited Weyl bounds with their stated height ranges. Patel--Yang, arXiv:2302.13444v1, Theorem 1.1, gives the bound with coefficient 66.7 and exponent 27/164 for every t >= 3. The increased positive HPY coefficients are conservative.
2. The shifted boundary estimates for `(s-1) zeta(s)` hold globally on both vertical boundaries. The separate low-height estimates pay the interval omitted by the sharper HPY formula. Yang's Phragmen--Lindelof lemma then gives the stated fixed-cell interpolation, with the full power and logarithm corrections in E. The same Q, X and Y apply to every harmonic and every ordinate of the required half-line.
3. This whole-half-line estimate pays the proof-level requirement in Yang's logarithmic-integral lemma, including integration beyond the selected harmonic. The detector, isolated-zero, pole and complete zero-count remainder are unchanged. The discarded local zero-count coefficient is nonpositive in the entire stated eta range.
4. The global minimizing-zero argument is valid: the published Vinogradov--Korobov bound reduces a hypothetical violating infimum to a finite set, and the previously proved classical denominator 4.82 pays both low heights and the lower rectangle sliver. The actual ratio `(1-beta)/lambda` is retained. No zero-free rectangle is assumed circularly.
5. The verifier accepts only directed Arb inequalities on closed rational cells. Floating values propose witnesses but do not certify them. Both positive bracket checks justify insertion of the rounded detector upper bounds. The lambda, eta and R hypotheses, height splices, fixed-detector theta enclosure and c(R) bound are explicitly checked.

## Independent replay

A separately copied, unchanged verifier was run with 160-bit Arb arithmetic in the stated python-flint environment. It terminated with PASS on all 1,602 cells after 3,188 evaluations, with no unresolved interval. The smallest certified margin was greater than

`4.1949176584803466021017954971109184059923138789e-7`.

The result is accepted as an explicit Littlewood zero-free-region refinement with denominator 20.15, conditional only on the identified published analytic theorems and the already checked classical 4.82 theorem. It is not a percentage of excluded zeros, a proof of RH, or a formal-kernel verification. No unpublished 19.62 estimate is used.
