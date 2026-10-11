## Round 129 — the Robin-criterion manuscript reverses its decisive implication

I audited Chua's manuscript *On the Riemann Hypothesis via Robin Criterion*,
[Zenodo record 18323203](https://zenodo.org/records/18323203), in particular
the “Main Proof” on its pages 8--9.  Robin's theorem itself is an
equivalence, so it would prove RH only after the Robin inequality had been
proved for every integer.  The manuscript's final argument does not establish
that universal inequality.

For a fixed odd \(n\), the manuscript attempts to propagate a verified
inequality from an exponent \(\alpha\) to a much larger exponent \(b\)
(the displayed threshold is \(b>e^{e^\alpha}\), subject to the manuscript's
typesetting).  In logical form the claimed propagation has the shape

\[
 P(\alpha)\Longrightarrow P(b)
\quad\text{for all sufficiently large }b,
\tag{129.1}
\]

where
\[
 P(k):\quad
 \frac{\sigma(2^k n)}{2^k n}
 <e^\gamma\log\log(2^k n).
\]

The manuscript then says, “By its contrapositive,” that a violation at some
\(\alpha\) yields a violation at an exponent
\(\beta<\log\log\alpha\).  That is not the contrapositive of (129.1).
The contrapositive of \(P(\alpha)\Rightarrow P(b)\) is

\[
 \neg P(b)\Longrightarrow\neg P(\alpha),
\tag{129.2}
\]

for the relevant pair \((\alpha,b)\).  It gives no implication
\(\neg P(\alpha)\Rightarrow\neg P(\beta)\) toward a smaller exponent.  The
“first violating \(\alpha\)” assumption therefore cannot produce the claimed
smaller violating \(\beta\), and the contradiction on page 9 does not follow.

There is a separate quantifier problem as well.  The Robin equivalence
concerns all integers \(m>5040\); a violation, if present, need not be
organized as the first violation in the exponent of \(2\) while the odd part
\(n\) is held fixed.  Even after fixing \(n\), the asserted propagation would
need to be proved for every missing exponent range and with its strict
inequalities and logarithmic domains checked.  The two endpoint estimates
for small and large \(\alpha\) do not supply that missing middle-range
argument.

Thus the manuscript proves neither \(P(k)\) for all \(k\) and all odd \(n\)
nor the Robin inequality for all integers.  Its own Section 19 correctly
states that proving Robin's inequality for every integer remains equivalent
to resolving RH; the page-9 reversal is exactly where the purported
resolution fails.

**Established:** Robin's criterion is a valid equivalence, and the elementary
large-exponent estimates may cover particular ranges when their hypotheses
hold.

**Failure:** the final contrapositive step is logically invalid; a violation
at \(\alpha\) does not imply a smaller violation, so the alleged
minimal-counterexample contradiction is unavailable.

**Remaining load-bearing statement:** prove the universal Robin inequality
with a valid argument for every odd part and every exponent, or supply a
different unconditional zero-exclusion proof.

**RH status:** no unconditional proof has been produced.
