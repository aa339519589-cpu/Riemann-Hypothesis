## Round 89 — the Gaussian--Perron local profile does not give an unconditional zero exclusion

Moriya's 2026 paper [*A Gaussian--Perron Prime-Side Defect and Local Profiles Near Critical-Line Zeros of the Riemann Zeta Function*](https://arxiv.org/abs/2607.04316) gives an exact contour-shift identity for a smoothed prime-side force. For a selected zero \(\rho_0\), it separates
\[
\Delta_{X,\alpha}
=\mathcal L_{\rho_0,X,\alpha}
+\mathcal E_{\rho_0,X,\alpha},
\tag{89.1}
\]
where \(\mathcal L_{\rho_0,X,\alpha}\) is the selected residue and \(\mathcal E_{\rho_0,X,\alpha}\) contains all other crossed zeros, the pole, trivial zeros, and the shifted contour integral. The selected residue can be computed exactly and has a different leading local scale for a hypothetical off-line zero than for a critical-line zero.

That calculation does not imply that an off-line zero is impossible. The full theorem controlling \(\mathcal E_{\rho_0,X,\alpha}\) requires explicit damping inequalities for every non-selected zero and a shifted-contour regularity hypothesis. The paper's full local-profile theorem then assumes RH, because under RH each non-trivial zero has zero horizontal displacement and the Gaussian exponent supplies the required vertical damping. The source states this scope in its abstract and in the theorem discussion: the unconditional content is the exact formula and selected-zero profile; the full critical-line localization is RH-conditional.

The obstruction is visible directly in the Gaussian factor. If
\[
\rho'=\tfrac12+x'+i(\gamma'),\qquad
\rho_0=\tfrac12+x_0+i\gamma_0,
\]
then, after scaling \(s\) near \(\rho_0\), the real part of the exponent contains an anisotropic term of the form
\[
Q_\alpha(\rho';\rho_0)
=\alpha^2\bigl((x'-x_0)^2-(\gamma'-\gamma_0)^2\bigr)
\tag{89.2}
\]
(up to the paper's fixed scaling convention). For a critical-line configuration \(x'=x_0=0\), every non-selected term is vertically damped. With hypothetical off-line zeros, a nearby horizontal displacement can instead make \(Q_\alpha>0\), amplifying rather than suppressing the remainder. A zero-free region alone does not establish the required uniform inequality for all zero pairs.

Hence a selected-zero “spike” cannot be converted into a contradiction unless one first proves the missing global remainder estimate. A remainder of the same leading order can cancel or alter the selected profile; the exact residue formula does not prevent that. This is the same structural issue as the Bombieri null-cone alternative, now expressed in a smoothed logarithmic-derivative coordinate.

**Established:** an exact Gaussian--Perron prime/zero formula and a rigorously derived selected-residue profile; conditional localization under stated damping and contour hypotheses.

**Failure / missing step:** no unconditional estimate makes the nonlocal remainder uniformly negligible around a hypothetical off-line zero. The complete profile theorem assumes RH and therefore cannot supply the conclusion needed to prove RH.

**Route decision:** retain the kernel as a diagnostic and as a possible source of test functions for the Weil form, but do not use the selected-zero asymptotic as a zero-exclusion proof. The needed new input is an unconditional anisotropic damping theorem for the entire non-selected zero set, together with contour control.

**RH status:** no unconditional proof has been produced.
