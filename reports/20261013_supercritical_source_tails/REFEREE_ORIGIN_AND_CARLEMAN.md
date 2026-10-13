# Independent checks of the origin domain and ordinary transform

Date: 2026-10-14. This record summarizes separate mathematical checks of
the actual publication files [ORIGIN_GRAPH_DOMAIN.md](ORIGIN_GRAPH_DOMAIN.md)
and [ORDINARY_CARLEMAN.md](ORDINARY_CARLEMAN.md). The checks covered the
abstract odd operator, the complete arithmetic-source application, and
the transform consequence. They are independent derivation checks by
research agents, not a proof-assistant certification or external human
peer review. The cited upstream theorems remain explicit dependencies.

## 1. Abstract odd domain separation

The odd folding gives exactly
\(B_o=T_D+M_k\), with
\(D(x,y)=\kappa(|x-y|)-\kappa(x+y)\) and
\(k(x)=2\int_0^\infty\kappa(x+y)dy\). This is the half-line
operator action corresponding to half the full odd quadratic form.
The cross identity in (6), including its factors \(1/4\) and \(1/2\),
checks by direct symmetrization for complex as well as real sources.

The combined ratio formula (7) has the correct signs on both sides of
\(y=x\). Monotonicity of \(t\kappa(t)\) for \(t\le1\) controls
the singular endpoint. For \(t\ge1\),
\((-F'(t))_+\le2t e^{-t/2}\). The outer logarithmic integral is at
most 8; its middle contribution is less than 144. Thus
\(B_ow_\eta\ge-304\) uniformly in \(\eta\), the cross pairing is
at least \(-152\|h\|^2\), and the norm expansion has exactly the
\(+304a\|h\|^2\) correction. The elementary uses of \(e^2>4\) and
\(\log6<2\) are justified in the text.

A preliminary argument had described the extension of an operator
pairing only as form approximation. The publication repairs this:
the inequality is first a closed-form pairing; the even extension of
\(w_\eta\) is a bounded Lipschitz form multiplier for each fixed
\(\eta\); form-core continuity then extends it. On \(D(B_o)\), the
representation theorem identifies the form pairing with the operator
inner product. No unproved singular-potential operator core is used.

Monotone convergence of the positive forms, the chosen resolvent
approximants, weak graph closure of \(B_o\), and local identification
of \(w_\eta h_\eta\) prove the forward domain inclusion and graph
estimate. The reverse inclusion follows from the represented form
functional \(B_oh+ah/x\). The exact domain equality (3) therefore passes.

## 2. Application to the actual complete source

The actual equation was rederived from
[SIGNED_ZERO_PAIRING.md, (4)--(5)](SIGNED_ZERO_PAIRING.md), together with
the auxiliary definition in [REPORT.md](REPORT.md), rather than inferred
from the proposed endpoint formula. Dividing the common half-line factor
two gives precisely
\[
B_og+\delta Vg=C_0g+F_+-(1-\delta)F_-.
\]
The positive coefficient is \(\delta\), the centered pole moment is
zero, and both complete translated sums include every prime power.

The complete Chebyshev multiplicity bound is
\(3e^{3\epsilon/2}e^{y/2}\); the unconditional PNT row lower bound
then gives exactly \(C_F=579e^{3\epsilon/2}(s_++s_-)/c_L\).
Applying the estimate to omitted labels proves convergence, not only a
bound on finite sums. The PNT invoked here is unconditional and concerns
the actual full row.

Normal convergence of the theta-row derivatives on the first prime
interval and the simple odd zero of \(\psi\) give
\(V=c/x+U\), with \(c>0\) and bounded \(U\). Localization is valid
because the Gamma commutator is L2 bounded. The source form core proof
now includes amplitude truncation, spatial truncation, and the two
separate terms of the origin-cutoff error. Only the product-cutoff term
is assigned the \(O(\eta\log(1/\eta))\) rate. An even mollifier
preserves oddness in the last step. This establishes the required
operator-domain membership from the weak equation.

The constants \(M,Q,C_r\) and the final \(C_1,C_2\) check directly.
In particular \(\|g\|_2^2\le3088P\), \(\|J\|_2\le M\sqrt P\),
and \(a=\delta c\). Hence the localized \(B_o h\) bound is uniform
in \(\delta\), whereas the squared ratio and divergence estimates
have the displayed \(\delta^{-2}\) loss. No uniform trace follows.

## 3. Ordinary transform

A separate review checked the actual companion file with the preceding
origin theorem as input. The sharper inherited \(e^{14R}\) source tail
and the theta derivative bound give the ratio weight \(B>3\).
The full translated sum satisfies (3) with \(O_C(P)\), not merely
\(O_C(\delta^{-2}P)\), because
\(\int\psi e^{y/2}|r|^2\le193P/c_L\). Its label tail converges in
the same weighted L2 norm by dominated convergence.

The diagonal term \(Lr\) requires \(C>4\). Combining that tail with
the new endpoint theorem gives the global weighted divergence bound,
absolute convergence for \(\operatorname{Im}z>2\), and the Hardy
estimate on each shifted half-plane \(\operatorname{Im}z>2+\eta\).
The constants do not assert a Hardy bound at the limiting height 2.

The two support representations of the theta convolution give an
entire numerator. Weighted Fubini supplies \(B=\Xi\mathcal C_+\)
in the initial half-plane with the stated Fourier sign. The old
finite-part numerator is \(B_\rho=B-c_\rho\Xi\).
At a zero of multiplicity \(m\), the quotient residue equals
\(mB^{(m-1)}/\Xi^{(m)}\); comparison with the inherited residue
\(-imG/\delta\) cancels \(m\). The publication's derivative formula
correctly contains no additional multiplicity.

## 4. Scope of the accepted result

These checks establish the new domain and ordinary-transform deductions
under the cited original source, complete-row, global-convolution and
residue inputs. They do not freshly certify every earlier theorem in
the repository. No finite-height zero computation is used in these new
deductions, and no additional zero is excluded. The Hardy estimate is
outside the zero strip; it does not force the signed residues to vanish.
The full critical comparison \(K\le I\) remains unproved.
