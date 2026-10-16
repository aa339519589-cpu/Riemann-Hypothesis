# A further 8,192 certified zeros: cumulative finite extension of 49,152

## Exact interval and count

Let T0 = 3,000,175,332,800, and set

- T2 = 384,022,443,823,399 / 128 = 3,000,175,342,370.3046875;
- T3 = 3,072,179,552,547,071 / 1024 = 3,000,175,344,284.2490234375.

The certificate establishes exactly 8,192 nontrivial zeta zeros in
T2 < Im(s) <= T3, all simple and on Re(s)=1/2. Its independently recomputed
total-zero counts, including multiplicity, are

- N(T2) = 12,363,153,478,098;
- N(T3) = 12,363,153,486,290.

The new height increment is 1,959,879 / 1024 = 1,913.9443359375.
Together with the unchanged
[40,960-zero certificate](../20261016_certified_frontier_extension_40960/REPORT.md),
this gives exactly 49,152 simple critical-line zeros in T0 < Im(s) <= T3.
The cumulative height increment is 11,759,871 / 1024 = 11,484.2490234375.
Previous batches are included, not counted again.

Platt–Trudgian Theorem 1 supplies critical-line coverage through T0. Combining
that theorem with these explicit intervals therefore extends its finite coverage
through T3. This is not a world-record assertion, an asymptotic proportion, or
RH. No claim is made to exclude unpublished or unlocated computations.

## Certificate proof

The JSON stores 8,192 exact dyadic brackets, strictly ordered, pairwise disjoint,
and strictly within (T2,T3), together with the two exact total counts and nonzero
Hardy-Z signs at both outer endpoints.

The read-only verifier calls the official rigorous FLINT routine
`acb_dirichlet_platt_hardy_z_zeros` in two fresh blocks, starting at indices
12,363,153,478,099 and 12,363,153,482,195. Each call must return all 4,096 requested
consecutive Hardy-Z zero balls. Every fresh ball must be strictly contained in
its corresponding stored bracket. Mere overlap, a partial return, an unresolved
ball, or a failed ordering check rejects the entire certificate.

The documented routine contract gives a critical-line zero in each returned
ball. Its isolation and refinement implementation preserves sign-changing
enclosures rather than merely returning numerical guesses. Thus the disjoint
brackets give at least 8,192 distinct critical-line zeros.

Separately, `acb_dirichlet_zeta_nzeros` certifies N(T), the number of all nontrivial
zeros with multiplicity in 0 < Im(s) <= T, by Turing's method. The difference here
is exactly 8,192. The bracketed zeros therefore exhaust the total count, so each
has multiplicity one and no off-critical zero occurs in this half-open interval.

Nonzero Hardy-Z values directly exclude critical-line zeros at the outer
endpoints. Count exhaustion excludes an off-critical zero at T3, while the
previous coverage excludes one at T2. Hardy nonvanishing alone is not being used
to exclude an off-critical boundary zero.

## Reproduction and trust

Generation used official python-flint 0.9.0 with bundled FLINT 3.6.0, 192-bit
arithmetic and four native threads. All raw enclosures were checkpointed before
validation. The one 8,192-index generating call took about 192 seconds; it did not
improve on the earlier 4,096-block average. This measurement is not a scalability
claim and is not a separate mathematical result.

Run the full independent verification on Linux with the official package:

    python verify_native_block_certificate.py frontier_next8192_certificate.json --bits 256 --threads 4

The verifier requires precision strictly above the recorded generation precision.
It recomputes both all-zero counts, both outer Hardy signs, every bracket-order
condition, and every zero ball. The two adjacent index blocks cover each stored
bracket exactly once. The generating block size is not trusted for acceptance.
Only a final PASS after all checks is successful verification.

The compact JSON stores every mathematical field read by the verifier, not
unused decimal enclosure strings or capture logs. The wrapper uses official
opaque vector-allocation and entry-pointer functions, without copying C layouts.
For endpoint Hardy signs it uses Gamma divided by its absolute value for the
phase. No branch choice for an unwrapped log-Gamma is required.

The proof trusts the documented rigorous FLINT/Arb implementation, its official
binary dependencies, the compiler and ordinary hardware. It is not a Lean-kernel
proof or an integer-only Turing transcript. Higher requested precision does not
by itself guarantee a narrow ball; strict containment is always checked.

## Primary sources

- Platt and Trudgian, *The Riemann hypothesis is true up to 3 · 10^12*, Theorem 1:
  https://arxiv.org/abs/2004.09765
- Official FLINT documentation, “Riemann zeta function zeros” and “Riemann zeta
  function zeros (Platt's method)”, especially `acb_dirichlet_zeta_nzeros` and
  `acb_dirichlet_platt_hardy_z_zeros`:
  https://flintlib.org/doc/acb_dirichlet.html
- Version-pinned FLINT 3.6.0 documentation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/doc/source/acb_dirichlet.rst
- Consecutive-block implementation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/platt_hardy_z_zeros.c
- Isolation and enclosing-ball refinement:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/platt_local_hardy_z_zeros.c
- Total-count/Turing implementation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/isolate_hardy_z_zero.c

These count and existence contracts do not assume RH. No timeout, partial return,
or unresolved computation is accepted as a certificate.
