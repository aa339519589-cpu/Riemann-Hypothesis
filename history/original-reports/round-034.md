## Round 34 — audit of the Robin-criterion proof claim

I audited the manuscript *On the Riemann Hypothesis via Robin Criterion*,
Zenodo record 18323203, against its own displayed inequalities. The verdict is
**不成立**.

### I. What is actually available

The manuscript correctly recalls Robin's equivalence: proving

\[
 \frac{\sigma(m)}m<e^\gamma\log\log m
 \qquad(m>5040)
\tag{34.1}
\]

for every integer \(m\) would prove RH. It also uses the elementary bound

\[
 \frac{\sigma(2^\alpha n)}{2^\alpha n}
 <\frac{2^\alpha n}{\varphi(2^\alpha n)}
 =\frac{2n}{\varphi(2n)}
\tag{34.2}
\]

for odd \(n\). Equation (34.2) is an upper bound independent of \(\alpha\);
it is not a recurrence relating the Robin ratios at two different exponents.

### II. The load-bearing implication is absent

The final argument assumes that if a first violation occurs at an exponent
\(\alpha\), then there is a violation at some
\(\beta<\log\log\alpha<\alpha\). No lemma proving this implication is given.
It does not follow from (34.2), nor from any preceding displayed inequality.

Set

\[
 a_\nu=\frac{\sigma(2^\nu n)}{2^\nu n},
 \qquad b_\nu=e^\gamma\log\log(2^\nu n).
\]

The assertion \(a_\alpha>b_\alpha\) contains no logical implication
\(a_\beta>b_\beta\) for \(\beta<\alpha\): both sequences vary with the
index, and (34.2) supplies only \(a_\nu<2n/\varphi(2n)\). An upper bound on
\(a_\beta\) cannot be converted into the required lower bound. Thus the
claimed contradiction with the minimality of \(\alpha\) is circular.

### III. An uncovered exponent range

The manuscript separately treats

\[
 \alpha<\log\log\log n
 \qquad\text{and}\qquad
 \alpha>\log n,
\tag{34.3}
\]

then states that all positive integers \(\alpha\) have been covered. The
interval

\[
 \log\log\log n\leq\alpha\leq\log n
\tag{34.4}
\]

is not treated. For the large \(n\) under consideration it contains many
integers, so the two endpoint estimates cannot establish (34.1).

There is also a quantifier gap: RH false implies the existence of infinitely
many counterexamples to Robin's inequality, but it does not by itself select a
fixed odd \(n\) for which the asserted exponent-descent relation holds. The
proof starts using such a fixed-\(n\) first exponent without establishing that
the required family of counterexamples has that structure.

### IV. Exact conclusion

The cited Robin equivalence remains valid, but the manuscript has not proved
Robin's inequality. Its central descent step and the intermediate range are
both missing. The document therefore supplies no unconditional RH proof.

**已确认事实:** (34.2) is a valid elementary upper bound; Robin's criterion is
an equivalence, not a proof of its inequality.

**失败 / 错误点:** unsupported violation descent, an uncovered range (34.4),
and an unproved fixed-\(n\) quantifier switch.

**下一步路线:** any Robin route must prove (34.1) uniformly over all integers;
endpoint estimates and a minimal-counterexample assertion are insufficient.

**RH status:** no unconditional proof has been produced.
