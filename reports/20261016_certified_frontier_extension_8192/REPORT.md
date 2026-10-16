# A certified 8,192-zero extension above the Platt–Trudgian endpoint

## Exact finite statement

Set

- T0 = 3,000,175,332,800;
- T1 = 1,536,089,771,373,645 / 512 = 3,000,175,334,714.150390625.

There are exactly 8,192 nontrivial zeta zeros with T0 < Im(s) <= T1.
Every one is simple and has real part 1/2. The exact height increment is
980,045 / 512 = 1,914.150390625.

The multiplicity-counted endpoint values certified here are
N(T0) = 12,363,153,437,138 and N(T1) = 12,363,153,445,330.
This larger interval includes the [previous 32-zero certificate](../20261016_certified_frontier_extension_32/REPORT.md).
It therefore adds 8,160 zeros beyond that certificate, not 8,192 additional zeros.
The earlier package remains unchanged.

Platt–Trudgian Theorem 1 proves critical-line coverage through T0. Combining that
published theorem with this finite certificate extends its conclusion through T1.
The strongest primary contiguous-height theorem located in the literature check was
that result. No claim to have excluded unpublished or unlocated larger computations
is required. This is a finite height extension, not a positive-proportion theorem,
a world-record claim, or a proof of RH.

## Proof from the certificate

The JSON supplies 8,193 strictly increasing exact rational samples
T0 = t0 < t1 < ... < t8192 = T1. Every Hardy value

    Z(t) = exp(i theta(t)) zeta(1/2 + i t)
    theta(t) = Im log Gamma(1/4 + i t/2) - (t/2) log(pi)

is rigorously enclosed with a nonzero sign, and successive signs are opposite.
The Hardy function is continuous and real for real t. Consequently each open
interval (tj, tj+1) contains at least one critical-line zero. These intervals
are pairwise disjoint, although their nonzero endpoints are shared.

The separate total-count computation counts every nontrivial zero with multiplicity
in 0 < Im(s) <= T, not just zeros located on the line. Its exact difference is
8,192. Thus the 8,192 disjoint sign changes exhaust the entire multiplicity count.
Each interval contains exactly one zero, that zero has multiplicity one, and no
other zero, including an off-line zero, occurs in the stated height interval.
Both outer endpoints are nonzero, so the half-open convention is unambiguous.

## Rigorous arithmetic and replay

The generating computation used python-flint 0.9.0 with FLINT 3.6.0, ordinary
96-bit Arb sign evaluations, and 128-bit exact endpoint counts. The search first
used FLINT's Platt batch routine to suggest separating sample positions. The
certificate does not trust those suggestions: its signs and total counts were
recomputed separately. On the cloud machine, the batch search took about 166
seconds and the complete sign/count generation about 439 seconds, using four
workers. These are measured timings, not scalability guarantees.

The mathematical data are the exact rational samples and signs. The recorded
real-ball triples are outward decimal enclosures of the form
(midpoint +/- radius) * 10^exponent; they are not silently interpreted as exact
function values. The read-only verifier recomputes every value rather than trusting
the stored enclosures or signs. The generator hash is provenance metadata and is
not a proof premise.

Replay using the official PyPI package python-flint 0.9.0:

    python verify_block_certificate.py --bits 160 --workers 4

The verifier uses the phase Gamma(1/4+i t/2) / abs(Gamma(1/4+i t/2)), rather than
the generating implementation's log-Gamma phase. It validates ordering, every
nonzero sign and sign alternation, the two exact endpoint counts, and their
agreement with the number of sign intervals. It rejects indeterminate enclosures.
A successful replay verifies the whole interval, not just selected samples or a
subset of its zeros.

The proof trusts the documented rigorous FLINT/Arb implementation and ordinary
hardware. It is not a Lean-kernel proof or an integer-only standalone transcript
of Turing's method.

## Primary dependencies and endpoint convention

- Platt and Trudgian, Theorem 1: https://arxiv.org/abs/2004.09765
- Official FLINT zero-count and Turing contracts:
  https://flintlib.org/doc/acb_dirichlet.html
- Version-pinned contract, section “Riemann zeta function zeros”, including the
  Turing-method bound and `acb_dirichlet_zeta_nzeros`:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/doc/source/acb_dirichlet.rst
- Version-pinned count implementation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/isolate_hardy_z_zero.c

The documented count is multiplicity-counted in 0 < Im(s) <= T. The implementation
uses certified good Gram blocks and separated sign lists with Turing's method.
A successful count does not assume RH; an RH counterexample can instead prevent
the search from terminating. A timeout or partial search is not a certificate.
