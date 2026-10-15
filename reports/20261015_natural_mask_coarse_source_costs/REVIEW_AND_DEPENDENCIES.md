# Mathematical review and dependency record

## Precise result

For the unchanged self-Fourier physical field H, the fixed finite mask
P_N=(I-5D4+4D16)M_N gives three fixed-shape compact logarithmic sources:
its microscopic right field, its complete future-prime row, and its
separated continuous far-exit row. Their H^sigma norms are O(sqrt N)
and their full original P/Q_delta costs are O(N).

The result concerns these same three fields, including both finite polar
cancellations and their surviving logarithmic remainders. It is neither
an estimate on an arbitrary output weight nor a subpower bound on the
signed main collar or critical head first variation.

## Checks in the complete proof

1. **Original form and source factor.** The source coordinate is x=log t,
   with physical argument u=t/(16N) and normalization sqrt(t/(16N)).
   The original Gamma, forward prime, reflected, V and pole forms are
   explicitly defined. A compact-source Sobolev estimate pays their
   complete costs and their original closure, not a replacement domain.
2. **The same finite mask.** The coefficients include all three outer
   branches, have support d<=16N and sum|a_d|<=10N. Both sum a_d and
   sum a_d/d vanish exactly. Every Lambda row retains all prime powers.
3. **Reciprocal right field.** Complete Poisson cancels its two polar
   terms before a norm is taken. Fixed compact inversion and interpolation
   give exponent -s-1/2+2sigma for each H(nq/t), so the complete Euler
   sum is absolutely convergent in the local Sobolev space.
4. **Logarithmic field domain.** For h=H-c gamma, the actual constant
   unit head gives h=c(1-gamma) near zero. At infinity, dyadic weighted
   L2 and H^s interpolation pay multiplication by log|u| after a fixed
   regularity loss. Poisson is then passed for this logarithmic field
   and its Fourier transform in their simultaneous weighted/Sobolev
   closure. No domain for an unrelated Wg future derivative is assumed.
5. **Full future-prime normalization.** Lambda*1=log produces
   sum Lambda(n)e_N(nu), without1/n. The exact Gaussian expansion has
   positive constant log(2pi)/2. The two mask moments leave, rather than
   erase, c b0'(1)m_N(1)/(2u), with b0'(1)=3log4/4. The elementary
   floor identity pays its coefficient. The remaining reciprocal and
   Gaussian rows are all included.
6. **Continuous far exit.** Subtract c/2 separately in every reciprocal
   branch before using sum a_d=0. The proof only needs branchwise ds/s
   integrability, not an unjustified pointwise Euler-tail limit. The
   retained logarithmic sum is -3log4 S_N, not zero. A fixed positive
   input/exit separation pays the complete differentiated remainder.
7. **Scope.** No estimate for an N-dependent Green weight, vanishing
   input/exit gap, local singular Gamma row, separate drift log term,
   or either ordered covariance is included. A finite Gram of these
   O(N) sources remains on the same coarse scale. The uncut right field
   is not promoted to the original form domain.

## Published dependencies

- [The actual physical range theorem](../20261015_old_actual_physical_range/REPORT.md)
  supplies the SAME field H=Dw+c, self-Fourier symmetry, constant unit
  head, full-line mean c, and H^s intersect X_s for 1/2<s<1. Its
  Section0 also supplies the theta-ground and N, P, Q_delta conventions
  explicitly repeated in this report.
  SHA-256:
  `02c17ec44d84c3f515b032555fedd07e115dab448b99709a2add9e41497f03a1`.
- [The original source form](../20261012_localized_odd_schur/SOURCE_FORM.md)
  supplies the original q0 formula and source completion. The compact
  localization estimate is proved directly in the present report using
  q0 and the complete N/P/Q_delta rows from range Section0.
  SHA-256:
  `6fccf89fbbf98d2746c739e4ec173ad3ea5086bd5125a63701f4e2d8d40a7c2d`.
- [The right-field replacement theorem](../20261015_natural_mask_right_error/REPORT.md)
  is a contextual link identifying the different subpower error result
  and the signed terms it leaves. Its high-pass theorem is NOT used in
  the proof of the coarse estimates here.
  SHA-256:
  `46d219748f65e2a0dd55c906e4f4ef76f9950f52310d4959753e943898e22f37`.

This report does not use the normalized-current projection, an auxiliary
Liouville operator, a large-shift original-form domain, or an unavailable
positive hidden second moment. It is an analytic proof and requires no
new numerical certificate or computational replay.

## Report pin

`REPORT.md` SHA-256:
`4b087ebdd95c227a4d4ae49aa758879cce853003845009fc9409b768a974c904`.
