# Independent referee: updated zero-free input and selection consequences

Date: 2026-10-13. Reviewed [REPORT.md](REPORT.md), the fixed correspondence declarations and their completed kernel replay, and [the original selection bridge](../20261011_qrh_selection_bridge/REPORT.md), especially Propositions 1–3.

## Verdict

I found no substantive mathematical error in the updated strip conversion or in Propositions 1–3 as conditional deductions from the stated selection identities and zero-free input. The new boundary arithmetic is exact, the multiplicities are accounted for once per distinct zero, and the activity-exponent and real-ray Mellin arguments have the stated scope.

The conclusion remains conditional on two separate inputs: the zero-free theorem credited to Baiying Liu, and the complete source-selection identities. Neither this update nor the Lean replay establishes RH. The updated input correctly leaves the strict growth-descent target, the fixed-probe correlation saving, and the high-end continuation extension unproved.

## Checks on the updated boundary

For
\[
 B=\frac{1507-2\sqrt{921}}{1653},
\]
direct subtraction gives
\[
 1-B=\frac{146+2\sqrt{921}}{1653}=\delta,\qquad
 B-\frac12=\frac{1361-4\sqrt{921}}{3306}=a,
 \qquad \delta=\frac12-a.
\]
These are consistent with the displayed decimals. Since the zero-free theorem is for the strict half-plane \(\Re s>B\), it gives \(\beta\le B\), with equality not excluded. Applying the functional equation to a nontrivial zeta zero gives \(\beta\ge1-B\). Under
\(w=\gamma+i(1/2-\beta)\), this is exactly the closed strip
\(|\Im w|\le B-1/2=a\). The use of the closed endpoint in Proposition 1 is therefore correct.

The external source is appropriately identified as [Baiying Liu’s preprint](https://arxiv.org/abs/2610.12234) and its pinned formalization. The stated \(B\) is the preprint’s \(B_{\rm new}\); the preprint also reports an intermediate rational boundary, but omitting that weaker value is harmless. The draft credits Liu and makes no “world record” claim. The theorem is an external zero-free input, not a result newly proved by this repository.

## Propositions 1–3

**Proposition 1 (all fixed derivative tails).** From
\(\sum_w n_w\langle\Re w\rangle^N|a_w|<\infty\) for every \(N\) and the uniform bound \(|\Im w|\le a\), one has
\(\sum_w n_w|a_w||w|^j<\infty\) for each fixed \(j\). Thus the full zero expansion and its fixed derivatives converge uniformly on compact \(x\)-sets and satisfy the claimed \(e^{a|x|}\) bound. The derivatives of \((2\cosh(x/2))^{-1}\) contribute \(e^{-|x|/2}\), and Leibniz gives the \(q^{(j)}\) bound with exponent \(1/2-a\). Including the closed strip endpoint is valid. The note properly makes constants state- and derivative-dependent and does not claim uniformity as \(\lambda\uparrow1/2\).

**Proposition 2 (exact activity exponent).** The distinct-zero convention for \(\mathcal Z\), with the multiplicity \(n_w\) in each sum, is internally consistent and does not double-count zeros. Conjugation symmetry gives
\(\sup\Im w=\sup|\Im w|\). If only real \(w\) were active, reality of \(f\) makes every active \(a_w\) real, so the zero-side Weil sum \(\sum n_w a_w^2\) would be nonnegative, contradicting the stated negative source identity. This establishes \(\alpha(q)>0\).

The Laplace series is normally convergent on compact sets away from its poles: for large \(|\Re w|\), its denominator is comparable to \(|\Re w|\), and the \(N=0\) coefficient sum is finite; only finitely many remaining zeros meet a fixed bounded region. At \(s=-iw\), the residue is \(-n_wa_w/\varepsilon\), which is nonzero for an active zero. Distinct zeros give distinct pole locations; multiplicity appears in the residue exactly once. A hypothetical bound \(g(x)=O(e^{bx})\) with \(b<\alpha(q)\) makes the Laplace integral holomorphic on \(\Re s>b\); choosing an active \(w\) with \(\Im w>b\) places its nonremovable pole inside that half-plane, contradicting uniqueness of continuation from \(\Re s>1/2\). No attainment of the supremum is used. Since on \(x\ge0\),
\[
 \tfrac12e^{-x/2}\le(2\cosh(x/2))^{-1}\le e^{-x/2},
\]
the shift \(\tau(q)=\tau(g)-1/2\) is exact.

**Proposition 3 (real-ray Mellin comparison).** For real \(\sigma>1+c\), the pointwise inequality
\(e^{-c|x|}\le e^{-cx}\), positivity of \(\Phi\), and
\(\mathcal M\Phi(s)=\xi(s)=G(s)\zeta(s)\) give precisely the displayed ratio. In this range \(\xi(\sigma-c)\) and \(G(\sigma)\) are positive, so division is legitimate. The Gamma quotient is asymptotic to \((\sigma/2)^{-c/2}\), the rational factor tends to one, and \(\zeta(\sigma-c)\to1\). Thus the real-ray rate \(O_{q,c}(\sigma^{-c/2})\) and the specialization \(c=1/2-\alpha(q)\) are correct. The draft accurately limits the conclusion to real \(\sigma\); it does not infer a right-half-plane bound or an absolute Dirichlet expansion for \(D_{\Phi q}\).

## Scope and remaining gaps

The fixed-probe bookkeeping retains the original \(3/8\) saving target and identifies it as unproved. The updated input also correctly distinguishes the original high-end hypothesis \(\beta_*>7/8\), hence \(2\beta_*-1>3/4\), from the new region where a contradictory \(\beta_*\) may lie in \((\sigma_0,B]\). The prior high-end estimate cannot be reused there without new principal-term, error, and uniform-margin bounds.

For the original fixed probe, the remaining (T), (R4), and extended high-end requirements must remain explicit. Later restored-observation comparison theorems retain their separate hypotheses, as stated in REPORT.md. The improved strip bound by itself only gives
\(0<\alpha(q)\le a\); it supplies no strict relative growth descent and cannot eliminate every low state. The new real-ray Mellin estimate likewise does not provide the missing arithmetic correlation estimate for the original fixed probe.

## Formal-verification wording

The replay note distinguishes the raw-checkout failure from the successful kernel replay after restoring the required closure and module layout. Its stated scope—22 declarations, kernel trust zero, only the standard Lean axioms in their dependency lists, and no claim that every line of the preprint was formalized—is appropriately narrow. The current input’s formal-verification paragraph is consistent with that report and should continue to say that the raw public checkout is not a one-command replay.

The focused alias check is now closed for the concrete targets at issue. The independently checked wrapper explicitly states the conclusions as _root_.riemannZeta and _root_.DirichletCharacter.LFunction, calls the corresponding CombinedPaper declarations directly, and completes with kernel trust zero. Its two axiom reports are exactly propext, Classical.choice, and Quot.sound. This confirms the global target types for these zeta and Dirichlet declarations; it does not broaden the main replay’s scope to every manuscript statement or to the full optimality claim.

I found no reason to alter the displayed \(B\), \(\delta\), \(a\), the \(3/8\) probe target, or the multiplicity convention.
