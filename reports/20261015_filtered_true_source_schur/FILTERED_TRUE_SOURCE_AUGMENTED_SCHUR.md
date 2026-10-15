# A complete augmented Schur test for one exact filtered source

**Status:** the complete outward replay and independent assembled review passed.
The exact uncorrected source below satisfies S0[t] >= 10^-9. This is one
nonneutral source, not a uniform complement inequality or a negative-state
exclusion. The development matrix was not used as mathematical evidence.

The exact source is the UNCORRECTED t=1_(x>b)C phi, A=16,k=3, of
[FILTERED_MIXED_COLUMNS_INTERVAL_CERTIFICATE.md](FILTERED_MIXED_COLUMNS_INTERVAL_CERTIFICATE.md).
The complete Gamma lower bound gives3*10^-9 for this same representative;
the complete all-prime/pole debit gives less than1.71*10^-10. Consequently

    q0[t] > 2.829*10^-9.                                         (1)

All positive-head elimination is still required. Let A0 be the original
restricted source-form head operator on(0,b), whose unconditional gap
10^-10 is proved in the published unrepaired-head theorem. We seek

    S0[t]=q0[t]-<f,A0^-1 f> >=10^-9,
    f_j=q0(e_j,t).                                                (2)

The source belongs its logarithmic Gamma domain, and f belongs L2 on the
head: main phi is separated from b, and its complete future remainder is
controlled by the mixed operator in the column certificate. Thus (2) uses
the genuine closed head inverse, not an informal finite inverse.

## 1. Complete high block and finite columns

Use N=64,M=4096, with the original sine matrix and complete diagonal
minorant d_j of the published head certificate. Its high block is bounded
below by diag(d_j), with d_65>2 and d_4097>10. All off-diagonal high
interactions, reflections and pole were paid in that minorant.

For65<=j<=4096 form the65-component column v_j=(q_1j,...,q_64j,f_j).
The finite debit is sum v_j v_j^*/d_j. Every coefficient is an outward
interval. The checker chooses exact dyadic centers C_ij/2^60 and radii
R_ij/2^60, and upward dyadic weights for1/d_j. The full operator uncertainty
is bounded by

    sum_j w_j[2||C_j||_1||R_j||_1+||R_j||_1^2]/2^180.             (3)

It is subtracted as a scalar diagonal bound. The entire finite central
Gram AND this uncertainty are further multiplied by1001/1000. This is a
conservative increase, using the independently verified head reserve;
it does not omit or discount any source coefficient.

## 2. Joint infinite endpoint feature

The original head high columns have the exact six-feature decomposition
from the grouped high-column theorem. Its full Loewner debit is T, which
includes all six feature squares and the complete head remainder.
Write v_0 for its first endpoint vector. The main-source force satisfies

    f_j^main =(-1)^j v_s/omega_j+R_j,
    v_s=-sqrt(2/b)F(b),
    |R_j|<=sqrt(2/b)*10/omega_j^2.                                (4)

Both F(b) and the variation bound refer to MAIN phi, with all main-source
Gamma, primes and pole included. The complete Cphi-phi force has L2 norm
less than5*10^-15. Its source-only infinite coefficient error is therefore
paid by Parseval, not by summing uniform finite-column errors.

Let

    I1=(b/pi)^2/(M d_*), d_*=d_4097,
    R_s=(2/b)*100*(b/pi)^4/(3 M^3 d_*).

A valid65x65 majorant for the complete j>M column Gram has blocks

    head:              2T,
    head/source:       (21/2) I1 v_0 v_s,
    source/source:     (21/2) I1 v_s^2+116 R_s
                                      +3(5*10^-15)^2/d_*.       (5)

Here is the exact allocation. Apply the seven-square inequality to the
six head features and their remainder, appending v_s only to the first
feature. Split the combined remainder by Young with head factor11/10 and
source factor11. Add the complete future-error column with Young
parameter1/2. The resulting head debit is at most(33/20)T<=2T; the endpoint
cross coefficient is(3/2)*7=21/2. The source remainder coefficient is
(3/2)*7*11=115.5<=116, and the future-error coefficient is3.
This retains the endpoint mixed feature. Replacing it by independent
absolute endpoint squares would be a different, weaker comparison.

## 3. Exact finite remainder and infinite-domain passage

Subtract the complete finite debit(3) and infinite debit(5) from the low
augmented block

    [[ q_ij-10^-10 delta_ij, f_i ],
     [ f_j, q0[t]-10^-9 ]].                                    (6)

Use the lower value(1) in its final diagonal entry. The script
`certify_filtered_true_source_schur.py` performs direct interval LDL on
this65x65 remainder, retaining all input errors and signed cross entries.
If every pivot has positive lower endpoint, (6) is positive for every
finite head sine combination and arbitrary real source coefficient.
The high diagonal completion then proves the same on the full head
operator core. Closure of the genuine logarithmic source form and the
bounded mixed forcing extend it to the complete head form domain.
Taking the infimum over the head proves(2).

The least eigenvalue of a sampled finite matrix is not used as evidence.
The proof requires all complete row majorants, the directed source cells,
the endpoint and variation estimates, the full infinite column allocation,
and the final exact/interval replay together.

## 4. Scope after successful replay

Even a verified(2) would establish positivity only for this specific,
explicit non-neutral reciprocal-heat seed. It does not prove positivity
on its whole complement, exclude an actual negative eigenstate, or settle
the remaining Riemann-hypothesis sign problem. The complete same-source
head penalty is essential; the positive Gamma component alone is not the
Schur value.

## Final directed replay

The independently regenerated 4,096-column artifact has SHA-256
`e33385916a9878b7f2b111c778412dc88c1361871713e7e968f9cbfd1ee61928`.
The complete 65-dimensional augmented interval LDL has final pivot lower
`8.346541945890685e-10 > 0`. Every analytic tail and cross allocation above
was independently checked. The same uncorrected t=C phi is used throughout.
