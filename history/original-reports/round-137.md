## Round 137 — the adelic fixed-point manuscript is an equivalence sketch, not a global proof

I audited Morato de Dalmases, *The Adelic Connes–Weil Fixed-Point
Formulation of the Riemann Hypothesis* ([manuscript record](https://zenodo.org/records/19825247)),
including Sections 2–11 and Theorems 6.1, 8.1, 10.1, and 13.1.  Its central
claim is that RH is equivalent to positivity of a cyclic pairing for a
crossed-product spectral triple.  No new unconditional positivity theorem is
actually proved.

There is a basic analytic problem already in the proposed Hilbert-space
model.  The manuscript puts
\[
 H=L^2(\mathbb A_\mathbb Q/\mathbb Q^\times,d\mu_{\rm inv}),\qquad
 d\mu_{\rm inv}(x)=|x|^{-1}d\mu_{\rm Tam}(x),
\]
and asserts that this is a scaling-invariant measure.  The quotient contains
the zero orbit, and near a nonzero finite-adele unit with real coordinate
\(x_\infty\to0\), the proposed density contains \(dx_\infty/|x_\infty|\).
The manuscript supplies no removal of this singular orbit, no
\(\sigma\)-finite measure construction on the actual quotient, and no
domain/essential-self-adjointness proof for the resulting generator.  The
formal Jacobian calculation in Proposition 2.4 is not a construction of the
claimed spectral triple.

The trace statements are also not defined at the level required by the
argument.  The operator is declared self-adjoint as
\[
 D=-i\,\frac{d}{dt}U_t,
\]
but Theorems 6.1 and 8.1 use \(\operatorname{Tr}_{\rm reg}(e^{-tD})\).
For a self-adjoint generator, \(e^{-tD}\) is generally an unbounded
semigroup rather than a heat operator; the unitary evolution is
\(e^{-itD}\).  A regularized trace could in principle be introduced, but the
manuscript gives no trace-class/meromorphic continuation definition, no
renormalization theorem, and no derivation of the displayed zero sum.  In
particular, the raw series \(\sum_\rho e^{-t\rho}\) is not convergent merely
from \(0<\Re\rho<1\).

The prime-power periodic-orbit correspondence in Proposition 7.2 is not
proved for the stated flow.  The flow is written as multiplication by the
real scalar \(e^{-t}\), while the proposed fixed-point calculation treats
\(p^{-k}\) as a diagonal rational idele acting at the finite \(p\)-adic
component.  Those are different actions.  The claimed normal-bundle
determinant is infinite-dimensional and no Fredholm determinant or
linearized Poincare map on a defined normal bundle is constructed.  Thus the
prime coefficient \(p^{-k/2}\) does not follow from the asserted Lefschetz
formula.

The critical positivity step in Theorem 10.1 is algebraically invalid.  The
Weil zero contribution before RH has the form
\[
 \sum_\rho \widehat g(\rho)\widehat g(1-\rho),
\]
not \(\sum_\rho|\widehat g(\rho-\tfrac12)|^2\).  Replacing the former by
absolute squares is valid only after the zeros have been shown to lie on the
critical line, which is the conclusion being sought.  Conversely, the
manuscript's proposed “unitary” with Fourier transform supported in an
arbitrary tiny interval around an off-line zero is neither constructed nor
shown to be a unitary of the crossed product.  The positivity of a cyclic
pairing on all such unproved test unitaries cannot exclude an off-line zero.

Finally, the later fixed-point statements follow by definition from the
asserted spectral identification:
\[
 \operatorname{Fix}_{\rm spec}(\varphi_t)
 =\{-i(\rho-\tfrac12):\zeta(\rho)=0\}.
\]
If that identification and the positivity criterion were established, RH
would indeed follow; but they are precisely the missing global trace and
spectral-correspondence theorems.  Calling the resulting equivalences
Theorems 10.1 and 13.1 does not prove their premises.

**Established:** the manuscript records familiar formal relationships among
the adeles, the scaling action, the explicit formula, and Weil positivity.

**Failure / missing lemmas:** construct the stated measure and spectral
triple, define and prove the regularized trace formula, establish the
prime-orbit determinant, and derive the zero pairing without replacing it by
the RH-only square form.

**Remaining load-bearing statement:** supply an independent global
arithmetic-to-spectral construction satisfying all analytic domain and trace
hypotheses, followed by a genuine positivity proof on the full Weil test
class.  The current manuscript is an equivalence sketch, not an unconditional
RH proof.

**RH status:** no unconditional proof has been produced.
