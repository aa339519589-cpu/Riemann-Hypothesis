# A further 32,768 certified zeros, extending the finite coverage to 40,960 zeros

## Exact statement and relationship to the earlier certificates

Let

- T0 = 3,000,175,332,800;
- T1 = 1,536,089,771,373,645 / 512 = 3,000,175,334,714.150390625;
- T2 = 384,022,443,823,399 / 128 = 3,000,175,342,370.3046875.

There are exactly 32,768 nontrivial zeros of the Riemann zeta function in
T1 < Im(s) <= T2. All are simple and have real part 1/2. The new height increment
is 3,919,951 / 512 = 7,656.154296875.

The independent total-zero counts, including multiplicity, are

- N(T1) = 12,363,153,445,330;
- N(T2) = 12,363,153,478,098.

Combining this certificate with the unchanged
[8,192-zero certificate](../20261016_certified_frontier_extension_8192/REPORT.md)
gives exactly 40,960 simple critical-line zeros in T0 < Im(s) <= T2.
The total height increment above T0 is 1,224,999 / 128 = 9,570.3046875.
The earlier 8,192 already included the original 32; neither is counted twice.

Platt–Trudgian Theorem 1 establishes critical-line coverage through T0.
Consequently that published theorem and these certificates together give
critical-line coverage through T2. The literature search located that theorem
as its primary contiguous-height baseline. We do not claim to exclude all
unpublished or unlocated computations. This is an explicit finite extension,
not a world-record claim, an asymptotic proportion, or a proof of RH.

## Certificate and proof

The accompanying JSON contains 32,768 ordered exact dyadic brackets. Every bracket
is strictly inside (T1,T2), and successive closed brackets are strictly disjoint.
It also records the two exact total-zero counts and rigorously nonzero Hardy-Z
values at the outer endpoints.

For each of eight adjacent blocks, the verifier calls the official FLINT function
`acb_dirichlet_platt_hardy_z_zeros`. The starting indices are exactly

    12,363,153,445,331 + 4096 k,  k = 0, ..., 7.

Every call must return the full requested 4,096 consecutive Hardy-Z zero balls.
Each freshly returned rigorous ball must be strictly contained in its corresponding
stored exact bracket. A partial return, a nonfinite ball, a failed containment or
an overlapping bracket rejects the entire certificate. Mere overlap between a
fresh ball and a bracket is not accepted.

The documented function contract supplies existence of a Hardy-Z zero in every
returned ball. The isolation and refinement implementation retains sign-changing
enclosures; it is not a list of unvalidated floating-point root approximations.
Thus each of the 32,768 strictly disjoint brackets contains a critical-line zero.

Separately, `acb_dirichlet_zeta_nzeros` certifies the total number of nontrivial
zeros with multiplicity in 0 < Im(s) <= T. Its difference here is exactly 32,768.
The bracketed critical-line zeros therefore exhaust that count. Every bracket
contains exactly one zero of multiplicity one, and there is no other zero,
including any off-critical zero, in T1 < Im(s) <= T2.

The nonzero outer Hardy values directly rule out critical-line zeros at T1 and T2.
The total-count exhaustion also rules out an off-critical zero at T2; the previous
coverage rules out one at T1. Thus the half-open endpoint convention introduces no
unaccounted boundary zero. Nonzero Hardy values alone are not being used to rule
out off-critical zeros at an endpoint.

## Reproducible verification and trust boundary

The generating computation used python-flint 0.9.0 with its bundled FLINT 3.6.0,
192-bit arithmetic and four native threads. Eight fresh 4,096-index blocks took
about 718 seconds altogether on the cloud machine. Exact outer counts, signs,
bracket ordering and ball containment were checked separately when the certificate
was assembled. Timings are measurements for this batch, not scalability promises.

Replay with the official python-flint 0.9.0 package on Linux:

    python verify_native_block_certificate.py frontier_next32768_certificate.json --bits 256 --threads 4

The read-only verifier requires higher precision than the recorded generation
precision. It recomputes both global counts and both nonzero Hardy signs, validates
all exact brackets, and then recomputes every consecutive zero ball in fresh
adjacent blocks. All index blocks are covered exactly once, without a gap or an
overlap. A final `PASS` is printed only after every check has succeeded.

The wrapper locates the official bundled FLINT library and uses its opaque vector
allocation and entry-pointer functions. It does not reproduce C structure layouts.
The Hardy endpoint evaluation uses Gamma divided by its absolute value for the
phase, rather than a numerical choice of an unwrapped log-Gamma argument.

The compact JSON retains every exact bracket, both endpoints, the total counts,
outer signs, starting index, number of zeros and generation precision. Unused
native-enclosure strings and capture provenance are omitted. Its parsed mathematical
input is exactly identical to the generating certificate for every field read by
the verifier, including all 32,768 bracket pairs. This identity is independently
checked; the fresh replay therefore verifies the compact certificate without
trusting omitted provenance or stored approximate root values.

The mathematical proof relies on the documented rigorous FLINT/Arb implementation,
its official binary dependencies, and ordinary hardware. This is not a Lean-kernel
proof or an integer-only transcript of Turing's method. Requested arithmetic
precision is not itself a guarantee of ball width; strict bracket containment is
tested explicitly.

## Primary sources

- Platt and Trudgian, *The Riemann hypothesis is true up to 3 · 10^12*, Theorem 1:
  https://arxiv.org/abs/2004.09765
- Official FLINT documentation, sections “Riemann zeta function zeros” and
  “Riemann zeta function zeros (Platt's method)”, especially
  `acb_dirichlet_zeta_nzeros` and `acb_dirichlet_platt_hardy_z_zeros`:
  https://flintlib.org/doc/acb_dirichlet.html
- Version-pinned FLINT 3.6.0 documentation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/doc/source/acb_dirichlet.rst
- Version-pinned consecutive-block implementation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/platt_hardy_z_zeros.c
- Version-pinned isolation and enclosing-ball refinement:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/platt_local_hardy_z_zeros.c
- Version-pinned Turing/count isolation implementation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/isolate_hardy_z_zero.c

The total-count contract counts all zeros with multiplicity, not only located
critical-line zeros. Successful certified return does not assume RH. A timeout,
partial result, or unresolved enclosure does not count as a certificate.
