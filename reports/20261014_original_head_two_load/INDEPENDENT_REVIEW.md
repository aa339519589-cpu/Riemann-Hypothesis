# Independent mathematical review

## Verified theorem

The report and companions pinned below establish

\[
 q_0[f]+2|U(f)|^2+2\left|\frac5{787}N(f,s_1)\right|^2
 \ge \frac1{100}\|f\|_{L^2(0,\log2)}^2.
\]

The domain is the closure of finite sine spans in the restricted Gamma
form norm. All original internal reflected-prime terms and the full pole
are included. The neutral load uses the complete global prime row, not a
prime truncation or a truncated neutral vector. This is an original-source
head estimate with two explicit loads, not a positivity theorem for the
uncorrected head or the full original head/tail form.

## Proof checks

1. The Gamma matrix is the exact half-line odd multiplier matrix. Its
   boundary Gram has coefficient `4/b`, `b=log 2`, and the complete sequence
   `lambda_r=2r+1/2`. The alternating sine signs do not affect positivity
   of this Gram. The Hilbert-kernel estimate controls infinitely many high
   modes, with both reflected-prime norms and the polar rank-one norm
   retained in the high diagonal.

2. The arithmetic neutral load is exactly regrouped using
   `sum_(d|k)Lambda(d)=log k` before any numerical enclosure. The removable
   origin quotient is evaluated through the odd theta Taylor expansion.
   The identity for its twenty-first derivative gives the stated factor
   `1/22` in the remainder. The complete ordinary and mirrored theta tails,
   one-sided endpoint derivatives, endpoint terms in integration by parts,
   and the Simpson `b*h^4/180` error factor were checked. The coefficient
   estimate `|v_j|<3/j` includes both endpoint values of the load.

3. The digamma enclosure follows from the exact
   [Binet integral, DLMF 5.9.15](https://dlmf.nist.gov/5.9.E15),
   not an unbounded asymptotic expansion. The remaining Bose integral is
   `1/480`; bounding `|t^2+w^2|` below by `2 Re(w) Im(w)` gives precisely
   the displayed remainder. The positive rational diagonal tail and the
   complete exponentially weighted Gamma correction were independently
   checked. Both reflection matrices and the pole coefficients have the
   stated half-line normalization.

4. The two high-load tails are paid once, by `20/N`, using
   `2|x+y|^2 >= |x|^2-2|y|^2`. After this step the remaining mixed block
   is the original `q0` block; no load cross term is silently discarded.
   The analytic bound beyond column `M=4096` includes the entire Gamma,
   n=3 reflection and pole contributions. The n=2 reflection is diagonal.

5. The finite Schur sum uses exact integer products with upward-rounded
   weights. The dyadic radius bound dominates every column's rank-one
   perturbation in operator norm. Interval LDL accounts for the complete
   neutral-load uncertainty and all matrix-entry uncertainty. Positive
   pivots are used only to certify positivity, not as estimates of the
   smallest eigenvalue.

6. The passage to the stated form closure is valid: the Gamma form is
   closed and semibounded, while compact reflection operators, the pole,
   and the two loads are bounded in `L2`. Actual head restrictions have
   stronger zero-extension `H^sigma` regularity for some `0<sigma<1/2`.
   A direct signed half-source with nonzero trace is not thereby assigned
   separate original `P` and `N` membership.

## Independent reproduction

The complete-load and complete-kernel files were regenerated independently
from the exact pinned programs, then supplied to the exact-dyadic Schur
checker. The publication copy of the Schur checker was also rerun on these
fresh enclosures. All assertions passed:

* complete endpoint-plus-variation upper bound below `1190.922099`;
* first high-diagonal lower endpoint `1.0800209029378012`;
* full omitted Schur upper endpoint `0.004070923468141872`;
* finite cross-interval scalar error below `2.530462074e-10`;
* all 48 interval LDL pivots positive, with minimum lower endpoint
  `0.3795637688920742`.

The generated neutral-load JSON has SHA-256
`663bb3ba48d9abee63e25fe5390570bd741163eb06782a28a205045f211c0623`;
the generated complete-kernel JSON has SHA-256
`39b2caafadc33ec5bd802e3b390b9fa0f5b0155d112c57dabc94389fba7b7ee0`.
The analytic enclosures and infinite-tail estimates are essential to this
conclusion; a finite numerical eigenvalue calculation would not suffice.

## Actual-source consequence and limitation

The additional actual-source assertion (17) is valid. In the plateau gauge,
`U(f)=0` and actual stationarity against the neutral jet gives `N(f,s1)=0`.
Both head and tail pieces are legal original-form vectors, and stationarity
gives `Q_delta[f_H]=Q_delta[f_T]`. Hence the two head loads equal the
negative genuine tail loads, yielding the stated head control with those
tail debits. They do not vanish separately. The changed pole, the full
mixed form and actual stationarity are retained.

This estimate cannot be added to a hidden comparison as an independent
positive budget. No sign of the remaining original mixed residual or RH
conclusion is certified.

## Pinned artifacts

| Artifact | SHA-256 |
|---|---|
| `REPORT.md` | `20b2966771bf31a678d39186682b213339d6bea43d4dff1723364ddb85ec2b5b` |
| `GAMMA_SINE_GRAM.md` | `8f6ea24097d3035c68be4ef7ad24d7084ff1c528cd615c7629787da707d0d30a` |
| `NEUTRAL_LOAD.md` | `4a0a1f1119ba953404a8b9490c009148edbf906858c01276937ac134d856d3e9` |
| `certify_head_neutral_load.py` | `92d2a648d143baf245bca4870caec26e274041cf90846963796bd19aabfcc4dd` |
| `certify_original_head_kernel.py` | `e525264c1fbeceb81a24d2550567a5cab1c553f938c0f04fe034424d61a4702f` |
| `certify_original_head_schur.py` | `85a5e91e8de67d1d9e908a487ebe4afcb67d1affe8b65de3038b65231680c6af` |
| `SHA256SUMS` | `dffaeb7b440d5b598f444740c51bb91587756b8f4a00fc8f5908659be7abe9d4` |
