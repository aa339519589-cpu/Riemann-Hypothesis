## Round 173 — the Robin-criterion manuscript assumes its decisive converse

I audited Chua's manuscript *On the Riemann Hypothesis via Robin Criterion*:

<https://zenodo.org/records/18323203>

The paper states as Theorem 2 the known equivalence

\[
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \frac{\sigma(n)}{n}<e^\gamma\log\log n
 \quad(n\ge5041).
\tag{173.1}
\]

Its Section 12 then simply asserts that failure of RH creates violations of
(173.1) through “oscillatory terms”; no explicit formula with a quantified
remainder is proved.  The claimed main proof does not repair this missing
converse.

More specifically, pages 8--9 prove estimates only in the two regimes

\[
 \alpha<\log\log\log n
 \qquad\text{and}\qquad
 \alpha>\log n.
\tag{173.2}
\]

The interval
\(\log\log\log n\le\alpha\le\log n\) is never treated.  Nevertheless the
manuscript next states, without a new argument, that the estimate holds for
all positive \(\alpha,b,\beta\) whenever \(b>e e^\alpha\).  That universal
statement is exactly what would be needed to propagate the inequality through
the omitted intermediate exponents, so it cannot be inferred from (173.2).

The final contradiction also begins with “assume RH is false, there exists a
first integer \(\alpha\)” at which Robin's inequality fails.  The existence of
such an integer is not a consequence of the preceding estimates; it is the
converse direction of Robin's theorem.  If it is imported from (173.1), then
the manuscript has used the desired RH implication as a premise.  If it is not
imported, the argument has no starting violating integer.  The subsequent
“smaller violating exponent” step therefore cannot create the missing
converse.

The computational checks of known colossally abundant numbers are finite
checks and do not establish (173.1) for every integer.  Thus this manuscript
neither proves Robin's criterion nor supplies an independent proof of RH; it
repackages the equivalence and leaves its decisive direction unproved (and
partly circular).

**Established:** the Robin manuscript's final conclusion depends on an
unproved universal propagation claim and on the existence of a violation
already equivalent to the missing RH converse.

**Remaining load-bearing statement:** prove Robin's inequality for every
\(n\ge5041\) with a complete treatment of the intermediate exponent range and
without assuming the failure-of-RH converse.  No such proof is present.

**RH status:** no unconditional proof has been produced.
