# Restricted odd source Schur positivity and finite jet tail frames

For every fixed real even cutoff family satisfying the bounds in
[SOURCE_FORM.md](SOURCE_FORM.md), there is an integer \(K\) such that,
for all integers \(k\ge K\), the explicitly defined polar-inclusive
source form \(A_{k+1}\) is coercive on
\[
\operatorname{span}\{\chi_k(\Phi'''-\Phi'/4)\}
\oplus L^2_{\rm odd}\bigl((a_k,a_{k+1})\cup(-a_{k+1},-a_k)\bigr),
\qquad a_k=\tfrac12\log k,
\]
with its natural form domain. This includes the entire new collar,
not a finite discretization of it. Its scalar Schur remainder is at least
\((\delta\log k-C)\|r_k\|_2^2\), where \(r_k=(1-\chi_k)(\Phi'''-\Phi'/4)\)
and \(\delta>0\). The coercivity constant may depend on \(k\).

The proof keeps the complete Gamma multiplier, every prime power in the
source identities and row estimates, and the polar coefficient \(2\).
At these arithmetic endpoints the new/new prime block is exactly zero
by support geometry; the old/new prime coupling is retained. The key
inputs are the already proved narrow-tail energy, a strong Gamma
log-multiplier remainder, and a positive fraction of tail mass outside
the new window.

The [tracked-block proof](TRACKED_MODE_COLLAR.md) and its
[independent mathematical review](REFEREE_TRACKED_MODE.md) include the
complete pointwise prime series. The maximal sharp-window domain split
is supplied by [SHARP_WINDOW_DOMAIN.md](SHARP_WINDOW_DOMAIN.md), with
[review](REFEREE_DOMAIN.md). The generic
[Gamma remainder lemma](GAMMA_LOG_REMAINDER.md) also applies to complex
functions under its stated \(L^1\) and \(H^1\) hypotheses.

Separately, for every fixed finite \(d\), the first \(d\) odd theta jets
have a full-theta polynomial tail frame with
\[
\|1_{\{|x|\ge a_{k+1}\}}r\|_2^2\ge\delta_d\|r\|_2^2,
\quad \|r\|_1^2\le C_d k^{-1}\|r\|_2^2,
\quad \|r'\|_2\le C_d k\|r\|_2,
\]
uniformly over all complex coefficient vectors in that fixed jet span.
The [frame proof](FINITE_JET_TAIL_FRAME.md) and
[independent review](REFEREE_JET_FRAME.md) establish weighted convergence
on the whole tail, including the complete theta remainder. These
constants may deteriorate with \(d\); this report makes no claim for
growing or infinite jet families.

The remaining mathematical task is to control the simultaneous correction
to the old pivot, mixed row, and new target after the rest of the old
space is eliminated. Positivity of the displayed compression does not
supply that correction. The original complete-domain lower bound remains
\(511/1024\); no zeta zero is excluded and RH remains unproved.
