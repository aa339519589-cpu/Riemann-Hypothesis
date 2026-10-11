## Round 248 — A/B result: Chua's Robin-criterion manuscript assumes an unproved all-exponent propagation

**Source inspected:** Cheong Siong Chua, *On the Riemann Hypothesis via Robin
Criterion*, Zenodo record <https://zenodo.org/records/18323203>, PDF pp. 6--10.
Downloaded source SHA-256:
8b65cb45ee306a342aa9a26a4c83275a65040f5f8e1f4faec137e09c21a7b41f.

The manuscript correctly states Robin's equivalence, but its proposed proof of
the forward arithmetic inequality does not establish the missing universal
case. After treating only the ranges
\[
\alpha<\log\log\log n
\quad\text{and}\quad
\alpha>\log n,
\]
it asserts, without a derivation covering the omitted intermediate range,
that for all positive integers \(\alpha,b,\beta\), with
\(b>e^{e^\alpha}\), validity at exponent \(\alpha\) propagates to validity
at exponent \(b\). The displayed estimates before that assertion do not prove
this statement for arbitrary \(\alpha\); in particular, for
\(n\ge\log(10^{108})\) they leave the positive intermediate exponents
between the two stated ranges untreated.
 
The final minimal-counterexample step then invokes the “contrapositive” to
claim that a violation at exponent \(\alpha\) yields a violation at some
\(\beta<\log\log\alpha\). The actual contrapositive of a proved implication
\(P_\beta\Rightarrow P_b\) would be
\(\neg P_b\Rightarrow\neg P_\beta\), and it requires the precise
admissibility relation between \(b\) and \(\beta\), together with a valid
proof of \(P_\beta\Rightarrow P_b\) on the entire domain. Neither is supplied
for the claimed universal family. The argument also does not close the
small-exponent base cases for a fixed odd part \(n\).
 
Thus the contradiction is obtained only after assuming the load-bearing
all-exponent propagation that would have to exclude the Robin counterexample
in the first place. The manuscript itself later acknowledges that proving
Robin's inequality for all integers remains equivalent to resolving RH.
Consequently the stated Robin inequality and the RH conclusion are not
proved.
\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
