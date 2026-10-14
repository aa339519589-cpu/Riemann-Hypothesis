# Review of fixed-depth normalized-source regularity

Date: 2026-10-14.

Reviewed proof: [FIXED_DEPTH_REGULARITY.md](FIXED_DEPTH_REGULARITY.md).
Its SHA-256 is

    8c82cfda300edfb604a57e629ccc7c21157de4946ae92be022bf61b6544caa0f

The cited inputs were checked at repository snapshot
84edb736344e7aa1bd5e15942ca75beb24f7e3e5.

**Disposition: pass for the stated fixed-depth theorem.** A fresh
independent mathematical read-through and a separate derivation check
found no blocking gap. These are model-assisted mathematical reviews,
not proof-assistant verification or external human peer review.
The cited source theorems remain dependencies.

## Checks supporting the conclusion

1. The auxiliary equation has the actual positive-wing normalization
   \(H_\delta v=-2\delta v\). Its positive form is the full odd-line
   Gamma form, so the represented positive-wing operator is
   \(B_Nu=2\mu B_o(\mu u)\). All prime powers and the full pole
   operator remain present.

2. The identification of the composition-form domain uses the actual
   transformed ratio core. Spatial cutoffs, radial clipping, the
   logarithmic origin-cutoff estimate, and mollification across a
   remaining positive gap converge in both the weighted source norm
   and the kinetic form. The resulting \(f_j/\psi\) are valid smooth
   compact ratios. Thus the subsequent regularization is tested in
   the established auxiliary realization.

3. The complete coefficient estimates include forward and reverse
   shifts, reflections, and both odd-extension mirrors. Their
   zero-extended endpoint derivatives have integrable
   inverse-square-root singularities for \(1<p<2\). Theta decay
   gives summable \(W^{1,p}\) norms over all Mangoldt labels, hence
   the stated Fourier moments of every order below \(1/2\).
   The explicit affine-shift formulas before (11) keep the half-line
   boundaries inside these coefficients.

4. The regularizer symbol difference in (8) gives the uniform
   \(L^2\to H^\beta\) commutator estimate for \(s+\beta<1/2\).
   The logarithmic multiplier is absorbed by \(\beta>0\).
   The pole commutator is also bounded. The existing positive-order
   scalar source estimate supplies \(B_og\in L^2\).

5. Both endpoint rows of the complete bounded perturbation tend to
   zero uniformly in \(\delta\). Self-adjointness also controls the
   columns. On the remaining compact interval, the Gamma symbol
   absorbs the high-frequency part, retaining the bounded
   low-frequency map \(L_d\). This proves (15) on the whole actual
   form domain, without assuming regularity of an eigenbasis.

6. For each regularizer, (5)--(6) put \(G_\varepsilon v\) in
   \(D(B_N)\). The commutator identity (17) has the correct sign
   and factor two. The full pole term makes this argument valid
   even when \(G_\varepsilon v\) is not a centered original source.
   Equations (15)--(18) then bound its \(L^2\) norm uniformly in
   \(\varepsilon\); Fatou and the coefficient multiplier bound
   give the two \(H^s\) conclusions.

## Scope

The constant depends on the positive lower depth \(d\) and on \(s\).
There is no claim at \(s=1/2\), no uniform estimate as \(d\downarrow0\),
and no arbitrary mixed-eigenvalue packet bound obtained by summing
scalar estimates. Fixed-node translation domains, critical signed
positivity, and RH are not consequences of this result.
