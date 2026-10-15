# Mathematical review and dependencies

Date: 2026-10-15.

The report proves an essential-spectrum statement for the original full
Green operator, not a positivity theorem. Two separate internal reviews
checked the complete manuscript and its mathematical dependencies, rather
than only the author's dependency list. Both covered the complete form
identities, the packet normalization, the dual residual, and the projection
onto the entire known neutral space. These are internal proof reviews,
not formal verification or external referee endorsements.

## Dependencies retained

1. [Full-prime Green construction](../20261013_full_prime_green_reference/REPORT.md):
   the actual positive forms, their gradient completions, bounded T,
   C=TT*, and the eigenvalue-one correspondence of the known theta spaces.
2. [Compact positive excess](../20261013_compact_green_excess/REPORT.md):
   the pole-centered source identity, compact source map to L2, complete
   prime tails in form-operator norm, and compactness of (C-I)_+.
3. [Complete reflected renewal row](../20261013_reflected_markov_essential_edges/REPORT.md):
   L(x)~J exp(x/2), proved with the unconditional PNT and the full theta
   tail. No assertion about total-variation convergence of return laws is
   used, and no Markov-only Weyl sequence is transferred to C.

## Checks

- The exact centered-source formulas retain all prime powers. The
  reflected correlation cancels in P, but remains in N as its complete
  compact lower-order form; it is not discarded from a finite model.
- The comparison norm H0 is equivalent to P, using the full pole weight
  and bounded s/L. Individual past-prime terms are never asserted to lie
  in ordinary L2 operator domain.
- The full odd Fourier form supplies 2 kappa V_j, whereas N supplies
  2 V_j. This gives lambda=1/(1+kappa) and normalization
  sqrt(2(1+kappa)V_j).
- The narrow packet sees V/V_j tending uniformly to one. This follows
  from the published asymptotic, without differentiating prime knots.
- The Gamma estimate is a modulated-Schwartz-packet operator estimate.
  Both Fourier packets from odd extension are retained.
- The potentially large multiplication residual is estimated in the
  V-inverse weighted dual norm. Only the Gamma residual is paid by an
  ordinary L2 bound. Pole centering is exact and has vanishing cost.
- Weak convergence precedes the use of compact lower-order forms.
  The complete prime tails therefore vanish in the actual dual residual,
  not merely in a numerical Rayleigh quotient.
- For lambda different from one, the whole neutral projection is bounded
  by the Weyl residual divided by 1-lambda. This does not replace the
  closed neutral span by finitely many modes or identify it with the
  entire one-eigenspace.
- Bounded T transfers the singular sequence to C. Positivity and compact
  positive excess give the matching essential-spectrum upper inclusion.

## Limit of the conclusion

The full operator and its known-neutral compression have essential
spectrum [0,1]. Their possible eigenvalues above one remain exactly the
unresolved discrete excess allowed by the earlier theorem. In particular,
this result gives no new upper estimate for the actual arithmetic load,
no C<=I statement, no negative original-form vector, and no RH conclusion.
