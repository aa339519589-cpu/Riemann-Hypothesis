# The original source Schur operator in the true safe-seed mass space

## Results and scope

This package retains the COMPLETE original Gamma/prime/reflection/pole form.
It does not replace that form by a positive future Markov metric. Its new
closed realization uses the honest arithmetic future seed and an explicit
change of topology, not ordinary odd-source L2.

Let b=log2, xi be the Gaussian cubic seed, W the complete positive safe
integer row, and m=Wxi. The true future source relation is

    f(x)=sum_(n>=1)n^(-1/2)xi(x+log n)a(x+log n), x>b.

The verified original head on (0,b) has gap 10^(-10). Its inverse is used
ONLY in the closed logarithmic SOURCE domain. The package proves:

1. The exact original head Schur form S0. For an actual top source g at
   positive depth delta,

       S0[g_T]=-delta N[g/psi]-delta^2 D_g,
       D_g=<n_g,A0^(-1)n_g>, n_g=2(Vg-F_r g).

   The head subtraction has a MINUS sign. No separate original P/N
   membership of A0^(-1)n_g is asserted.

2. A GENERIC signed lower bound

       S0[a]>=-C_* integral_b^infinity m|a-c|^2

   for every constant c on the stated source class. C_* is finite and
   independent of actual depth and amplitude. It uses an unconditional
   enlarged positive head; the width and numerical C_* are not certified.

3. A densely defined, closed, semibounded original Schur form in
   H_m=L2(m dx), hence a selfadjoint operator. The whole mass-closed span
   of genuine neutral seeds is in its operator kernel. Orthogonal mass
   projection off that span preserves the original Schur value. It does
   NOT preserve actual-source status, original P membership, or finite
   hidden Gamma energy without a separate proof.

4. An explicit finite certificate interface for the head elimination.
   Genuine theta-head Grams recover the head penalty monotonically. A
   different operator-core least-squares sequence has a complete L2
   residual tending to zero and gives convergent two-sided Schur bounds.
   The two sequences and the hidden-orthogonal projection are distinct.

5. An explicit Bessel/reciprocal-heat family of nonzero mass vectors
   orthogonal to EVERY neutral seed. Different onset parameters give
   infinitely many linearly independent vectors in the complementary
   space. Thus no false neutral-density shortcut is available.

The operator's sign on this genuine complement remains unresolved. These
results do not establish RH, a nonnegative original remainder, a finite
total negative index, or a zero negative spectral part.

## Proof map

- [SOURCE_SCHUR.md](SOURCE_SCHUR.md): exact original head elimination,
  actual negative value, and joint finite hidden/remainder projection.
- [MASS_LOWER_BOUND.md](MASS_LOWER_BOUND.md): unconditional positive-head
  persistence, full arithmetic row bounds and generic lower comparison.
- [CLOSED_OPERATOR.md](CLOSED_OPERATOR.md): closed true-seed graph,
  minimized form, selfadjoint realization and entire closed neutral span.
- [NEUTRAL_GRAM.md](NEUTRAL_GRAM.md): form/operator cores of genuine theta
  heads, exact monotone completion and convergent complete-residual bounds.
- [EXPLICIT_COMPLEMENT.md](EXPLICIT_COMPLEMENT.md): real Bessel construction,
  exact mass Jacobian, reciprocal evenness and source-form legality.
- [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md): independently pinned review.

## Verified dependencies

The full prior original-head certificate and its mathematical checkers are
linked rather than copied:

- [Unpenalized original head](../20261014_unrepaired_original_head/REPORT.md)
  and [complete mixed source rows](../20261014_unrepaired_original_head/MIXED_FORCING.md).
- [Exact safe-xi weights and forms](../20261014_safe_xi_hidden_comparison/SAFE_RAY_FORMS.md),
  [positive hidden comparison](../20261014_safe_xi_hidden_comparison/REPORT.md),
  and [full original signed interface](../20261014_safe_xi_hidden_comparison/ORIGINAL_INTERFACE.md).
- [Honest future Mobius inverse and repaired source domain](../20261014_anchored_future_mobius/REPORT.md).
- [Actual origin transmission](../20261014_actual_origin_transmission/REPORT.md)
  and [actual ratio regularity/plateau](../20261014_actual_ratio_multipliers/REPORT.md).
- [Retained hidden Gamma energy and logarithmic Hardy estimate](../20261014_shifted_source_hidden_observability/RETAINED_GAMMA.md)
  and [complete shifted source embedding](../20261014_shifted_source_hidden_observability/SHIFTED_TAIL.md).

The new package is analytic apart from that already certified head input.
Its Bessel series and large-real-argument estimates are cited directly to
NIST DLMF in the explicit-complement proof. No floating diagnostic or
research log serves as evidence for a theorem here.
