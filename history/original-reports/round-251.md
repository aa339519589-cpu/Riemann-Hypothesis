## Round 251 — A/B result: Cadeddu's parametric-limit argument confuses big-O error bounds with asymptotic equivalence

Source audited: Enrico P. G. Cadeddu, *Proof of the Riemann Hypothesis through the limit of an approximated ξ function*, Zenodo version v25,
[record 21243275](https://zenodo.org/records/21243275), PDF dated 2026-07-01, SHA-256
`762133bd77412267ea27871aa7758fda0eec134286cfced827dec2419f77ad5f`.
The five-page manuscript defines finite Euler--Maclaurin-type approximants and
then uses a path (s(Q)=s_0+iQ^{-k}) approaching a presumed zero.

For (0<\sigma_0<1), the manuscript records error estimates of the form
\(
\xi_Q(s(Q))=\xi(s(Q))+O(Q^{-\sigma_0}),\qquad
\xi_Q(1-s(Q))=\xi(1-s(Q))+O(Q^{-1+\sigma_0}).
\)
It then chooses exponents so that the exact zero-approach is smaller than
the second error but larger than the first, and concludes that the quotient
of the two approximants tends to zero. That conclusion does not follow from
the displayed estimates. An (O(Q^{-1+\sigma_0})) statement is only an upper
bound; it does not imply a nonzero leading term or the lower bound
\(\xi_Q(1-s(Q))\asymp Q^{-1+\sigma_0}\). The error may cancel the leading
term, have a different order, or have a different phase. Consequently the
quotient limit in equation (6) is not derived.

The exact completed function has the functional equation
\(\xi(s)=\xi(1-s)\). Hence, whenever the denominator is nonzero, the exact
quotient \(\xi(s(Q))/\xi(1-s(Q))\) is identically (1), even while both
quantities tend to zero. The finite truncations do not inherit this identity
merely because their limits do: the two truncations use different arguments
and their remainder terms are not shown to be equal. The manuscript's
Section 3.1 assertion that two functions approaching the same zero have the
same 'form' and therefore quotient limit (1) is an unsupported premise
(and its definition of 'same form' effectively assumes equality on an
interval). Equality of limiting values at a common zero is insufficient; for
example, (Q^{-1}) and (Q^{-2}) both tend to zero but their quotient does
not tend to (1).

Thus neither the zero quotient in equation (6) nor the finite-approximation
version of the symmetry in equation (7) is proved. The asserted contradiction
and the conclusion that an off-critical zero cannot exist do not follow.
No numerical limit calculation changes this missing asymptotic lower bound or
the absent symmetry of the finite approximants.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
