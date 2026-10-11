## Round 238 — A/B result: Sharma's S-decomposition drops the horizontal-path contribution that detects off-line zeros

**Source inspected:** S. S. Sharma, *Riemann Hypothesis: A Complete Proof via
the S-Decomposition and Backlund Substitution*, Zenodo record
<https://zenodo.org/records/19035487>, Version 5.12, DOCX pp. 2–5 and
summary tables.

The manuscript defines \(S(t)\) by continuously tracking the argument along
the standard path from \(2\) to \(2+it\) and then horizontally to
\(1/2+it\). It then replaces that path-defined argument by
\[
S(t)=-\frac{\theta(t)}{\pi}+\frac{\arg Z(t)}{\pi},
\qquad
Z(t)=e^{i\theta(t)}\zeta(1/2+it),
\]
and concludes \(\Delta S=s_c-n\). The pointwise identity for the endpoint
values is valid only modulo a branch choice. It is not an identity of the
continuous path lifts used to define \(S\) when a horizontal segment crosses
a zero of \(\zeta\). As \(t\) passes the ordinate of an off-line zero, that
horizontal segment acquires a winding jump; \(Z(t)\), which samples only the
critical line, does not see it.

This is exactly the missing term. The local logarithmic-derivative
calculation in the manuscript's Lemma 0 uses
\(\zeta'/\zeta(1/2+it)\), which differentiates the endpoint phase away from
singular heights. It does not differentiate the path-dependent horizontal
continuation through a zero. For a reflected off-line pair, the two
contributions to the endpoint phase may cancel, but the pair consists of two
zeros inside the Backlund rectangle, so their argument-principle
contributions to \(N(T_1,T_2)\) add with multiplicity. Symmetry does not make
two enclosed zeros disappear from the contour count.

The contradiction with the claimed identity can be stated without any
numerical input. Backlund's formula is
\[
N(T_1,T_2)=n+\Delta S.
\]
If the asserted identity \(\Delta S=s_c-n\) were an independent theorem,
then it would immediately give \(N=s_c\) on every interval. Since \(s_c\)
counts only sign changes of the critical-line Hardy function, this identity
already contains the desired exclusion of off-line zeros. The manuscript's
“Mirror Cancellation” is therefore not an independent derivation; it is the
RH-bearing assertion in another form, obtained by discarding the horizontal
path term.

The downstream good-block argument has a separate unsupported premise.
The bound \(|S(t)|=O(\log t/\log\log t)\) and the existence of positive and
negative values do not imply that \(S(P_k)=0\) at a prescribed sequence of
P-points, nor that a bounded integer walk has increments at most one. An
interval can contain several zeros, and a multiple zero can make the jump
larger than one. A sign change across a jump also need not pass through zero.
Thus Lemmas A and B do not prove the asserted good P-point density or the
existence of a good block containing every target height.

The elementary fact that a sign change of a real \(Z(t)\) counts an odd
critical-line zero is valid, and the numerical checks test only intervals
where the critical-line data are already known. They do not establish the
missing path-phase identity or the universal good-block theorem. Therefore
Theorem 3, Theorem 4, and Theorem 5 do not constitute an unconditional proof
of RH or of simplicity.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
