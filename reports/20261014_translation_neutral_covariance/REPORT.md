# Raw translations and neutral-compensated Green covariance

For the actual largest-supercritical source of the original full-prime
Green operator, this package proves two test tools.

1. [Raw translation domain and finite matrices](RAW_TRANSLATION_DOMAIN.md).
   Almost every sufficiently small cosine translation T_a g belongs to
   the actual centered P-completion. Every generic finite tuple gives
   the exact positive matrix

       B_ik=N(T_(a_i)g,T_(a_k)g)
            -(1/2)N(g,[T_(a_i+a_k)+T_(a_i-a_k)]g).

   Its full reflected-prime defect is an explicit line integral, with
   the depth-uniform bound delta |D_pr(a)|<=C_s a^(1+2s)P0 for every
   fixed 0<s<1/16. No trace of the actual source is assumed. Arithmetic
   nodes specified in advance require smoothing or a separate pointwise
   domain argument; an almost-everywhere result does not license them.

2. [Exact neutral leakage compensation](NEUTRAL_LEAKAGE_COMPENSATION.md).
   If s_j are independent known neutral centered theta sources,
   M_jl=N(s_j,s_l) and L_ji=N(s_j,C_i g), then the necessary matrix
   inequality is the stronger

       B-L^T M^(-1)L >=0.

   The correction is the common P/N orthogonal projection cost. Every
   leakage entry has an exact bulk-plus-complete-prime commutator
   formula. Increasing finite neutral spans recover their full closed-
   span projection, without assuming this span is the whole kernel.

Both results retain every prime power, both reflected boundary corners,
and all mixed matrix entries. Their proofs and constants refer to the
original actual source and original closed forms, not a replacement
model. The linked independent review pins the exact proof-file hashes.

**Status.** No actual source or signed mask violating the compensated
matrix inequality has been constructed. The original coefficient-one
Green comparison and RH remain unproved. These are additional legal
tests and exact necessary inequalities, not a sign-exclusion theorem.
