# Independent internal review

16 October 2026, UTC. **Pass for the stated asymptotic proportion and exact
increment**, after full mathematical review and independent scalar replay.
This is an internal audit, not external peer review or formal-kernel checking.

## Frozen scientific inputs

- `REPORT.md`: `03de2e0a91cdbe16bbec7b88d236b9e87b5c0c8a09597fc4c57e9a69183deebd`.
- `FINITE_CLIPPING_INTERFACE.md`: `a04e8c178928b599b0c3e98b10808e015c44c70f84fbcef8d804c5438173ccd2`.
- Scalar verifier: `9e56ad8d5fda0936883cdd59970f879da83182842a66b48cefded0b1ead7629d`.
- Exact window data: `3aec299878696245945760411329dbcdfd3e49e78c01fbf6bd8b1430f01c78e9`.

## Mathematical checks

1. The continuous-kernel Cotlar identity gives the stated Schatten-4 causal
   norm bound, with the null diagonal and the finite-rank density passage
   retained. It does not substitute the strict finite-matrix triangle for
   the continuous causal projection without its diagonal correction.
2. The sharp causal-square normalization was checked against its complete
   product decomposition. The Gamma, double-prime and two mixed rows have
   the claimed deliberately coarse leading bounds. In particular the
   regularized Gamma multiplier has mean square tending to `1/3`; the
   weighted off-diagonals remain lower-order. Their triangle bound is
   `49 F^4`, so each fixed window of height at most two eventually admits
   `M=1024`. This is a fixed-window limsup statement, not a uniform starting
   height for all tapers.
3. The finite clipping argument combines its mixed trace before estimating
   it. No operator-norm bound for a triangular truncation is assumed.
   The budget is the actual zero count `N`, not an unjustified smaller rank.
   Positive-rank interlacing and the negative-part trace debit give
   `beta-K/2=2`. Convexity, the scalar clipping identity and minimization of
   the square-root defect give precisely (F5)/(Q10), with `k=204`.
4. The actual sharp zero operator has the stated decomposition, trace,
   rank and positive-index bounds, including off-critical conjugate pairs
   and multiplicities. Its second trace is calculated exactly from the
   same sharp linear reduction; its third trace uses the linked, fully
   reviewed direct sharp cubic theorem. No smoothed surrogate or unsigned
   fourth moment is substituted.
5. The literal simple-zero Gram proof uses greedy pairing only at distance
   at most `theta=17/20`, exactly the certified close-pair domain. The
   unpaired set is theta-separated. The unchanged Fourier-support majorant
   bounds that block's spectrum below two. The complete nine-frame
   telescope, close two-by-two blocks and convex pinching yield (Q14a),
   including the finite boundary debit and the actual sharp span.
6. The fixed square-smooth inward taper has the stated mass, height and
   L1 bounds. The old positive majorant and close-pair margins survive;
   the all-gap inequality transfers uniformly with reward loss at most
   `32 epsilon`. The second- and third-moment error bounds, and consequently
   the `48 epsilon` defect allowance, were independently checked.
   The taper is fixed before taking the height limit. Summing the eventual
   dyadic estimate gives the asserted global liminf.

## Reproduction and exact target

The full scalar source was read. Its finite exponential-frequency algebra,
symbolic recognition of zero frequencies, formula for the distance
potential, normalization, and directed final comparison were checked.
The earlier exhaustive all-gap certificate remains an explicit linked
dependency; this scalar replay is not represented as a new exhaustive
geometry run.

The staged `reproduce.sh` was independently run from a separate copy with
official python-flint 0.9.0 / FLINT 3.6.0. Its complete manifest check passed;
both the 256-bit and 384-bit runs exited successfully and matched the
corresponding shipped JSON files byte for byte:

- 256 bits: `3e7e1e4dd1408da1e638109a429d7d5b4ff9cd556ce0919421367bd665c8c919`.
- 384 bits: `f19328ee5c647329045f856966e5cbe0255fc2ba0471ce4aeac633dce4223017`.

The final lower ball exceeds the claimed rational target by more than
`5.1904346305e-11`. Exact rational subtraction verifies that the displayed
new target exceeds the previous published target by `28/10^10`.
All relative links in the two proofs and reproduction instructions resolve.

The accepted increment is **2.8e-9 in the asymptotic simple critical-line
proportion**. It is neither a percent-scale removal of zeros nor a finite
height verification, and this review makes no literature-priority claim.
