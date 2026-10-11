## Round 55 — the eta-function nonvanishing claim is circular

I also checked the four-page paper by Xinjun Wang and Senlin Wang,
“A Complete and Rigorous Proof of the Riemann Hypothesis”
(\url{https://ssrn.com/abstract=6435838}). Its advertised core is the identity

\[
 \eta(s)=\bigl(1-2^{\,1-s}\bigr)\zeta(s),
\tag{55.1}
\]

followed by a claim that a computation of \(\lvert\eta(s)\rvert^2\) is
strictly positive in the critical strip.

The denominator factor is indeed nonzero in the open strip. If
\(1-2^{1-s}=0\), then taking absolute values gives
\(2^{1-\operatorname{Re}s}=1\), hence \(\operatorname{Re}s=1\), which is
outside \(0<\operatorname{Re}s<1\). Therefore (55.1) implies, throughout
the open strip,

\[
 \eta(s)=0
 \quad\Longleftrightarrow\quad
 \zeta(s)=0.
\tag{55.2}
\]

Consequently, the literal assertion
\(\lvert\eta(s)\rvert^2>0\) for every \(0<\operatorname{Re}s<1\) is false,
because the strip contains the known nontrivial zeros of \(\zeta\). If the
intended assertion is instead restricted to
\(\operatorname{Re}s\ne\tfrac12\), then by (55.2) it is exactly the
Riemann Hypothesis in different notation. The eta representation supplies
no positivity mechanism that proves it.

Thus the denominator nonvanishing is a valid elementary fact, but the
load-bearing eta nonvanishing is either directly contradicted by the
existing critical-line zeros (under the literal wording) or is a restatement
of RH (under the only interpretation relevant to the claimed conclusion).
No unconditional proof follows.

**Established:** the factor \(1-2^{1-s}\) has no zeros in the open critical
strip, and (55.2) holds there.

**Failure / error:** positivity of \(\lvert\eta(s)\rvert^2\) is asserted
without an independent proof and would itself settle the zero problem.

**RH status:** this candidate is not an unconditional proof.
