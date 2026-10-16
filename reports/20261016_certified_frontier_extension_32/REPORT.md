# A small certified interval above the Platt–Trudgian endpoint

## Exact finite statement

Let T0 = 3,000,175,332,800 and T1 = T0 + 31/4 = 3,000,175,332,807.75.
The supplied rational sign-change certificate and total-count replay certify exactly 32
nontrivial zeta zeros in T0 < Im(s) <= T1. Every one is simple and has real part 1/2.
This is a height increment of 7.75, not a positive proportion theorem or a proof of RH.

Platt–Trudgian Theorem 1 gives the prior endpoint T0 and count
12,363,153,437,138. The certificate gives N(T1) = 12,363,153,437,170.
The strongest primary contiguous-height result located in the current literature check
is that theorem; no assertion that no unpublished or unlocated larger computation exists
is needed for this finite statement. Combining the theorem and this certificate extends
that published finite-range conclusion through T1.

## Proof from the certificate

There are 32 pairwise disjoint open intervals with exact dyadic endpoints, all strictly
inside (T0,T1). For each, the Hardy function
Z(t) = exp(i theta(t)) zeta(1/2+it),
with theta(t) = Im log Gamma(1/4+it/2) - (t/2) log(pi),
has rigorously enclosed nonzero values of opposite signs. Hardy Z is continuous and real
on the real axis, so each interval contains at least one critical-line zero.

The independent total-count call computes all nontrivial zeros, with multiplicity,
in 0 < Im(s) <= T, not merely sampled line zeros. The exact difference is 32.
Consequently each bracket accounts for exactly one zero of multiplicity one, and there
are no other zeros in this height interval, including off-line zeros. Both outer
endpoints are independently certified nonzero, so there is no endpoint ambiguity.

## Arithmetic and reproducibility

The generating run uses python-flint 0.9.0, FLINT 3.6.0, 96-bit Arb balls, one thread.
It took 21.25 seconds after search suggestions had been found. Suggestions carry no
mathematical force: the certificate uses only the rational brackets and checked signs.
The ordinary high-precision root-search benchmark took 130 seconds for 32 roots and is
not the preferred scalable search method.

Read-only replay from this directory (official PyPI python-flint 0.9.0 required):

    python verify_frontier_certificate.py

The verifier defaults to 128 bits, repeats every sign evaluation and both exact total
counts, checks disjointness and outer endpoints, and rejects any indeterminate result.
The proof trusts the documented rigorous FLINT/Arb implementation and normal hardware;
it is not a Lean-kernel proof or an integer-only standalone Turing transcript.

## Primary dependencies

- Platt and Trudgian, Theorem 1: https://arxiv.org/abs/2004.09765
- Official FLINT zero-count and Turing contracts:
  https://flintlib.org/doc/acb_dirichlet.html
- Version-pinned contract: “Riemann zeta function zeros”, including the Turing-method bound and zeta_nzeros:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/doc/source/acb_dirichlet.rst
- Version-pinned count implementation:
  https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_dirichlet/isolate_hardy_z_zero.c

The documented count is multiplicity-counted in 0 < Im(s) <= T. The implementation
constructs certified good Gram blocks and separated sign lists using Turing's method.
It does not assume RH to return a successful count; an RH counterexample can prevent
this search from terminating. A timeout is not a certificate.
