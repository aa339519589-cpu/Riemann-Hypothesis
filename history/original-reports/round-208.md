## Round 208 — A/B result: Oukil v17 gives a conditional rigidity implication, not universal zero exclusion

**Source inspected:** W. Oukil, *Scalar rigidity, abstract prime systems, and
the Riemann zeta function*, Version 17, PDF pp. 3--6,
<https://www.cambridge.org/engage/coe/article-details/6a5a82ec4770e67d92083d91>.

The source's Theorem 1 states the implication
\[
L_\eta(s,\theta)\ne0\quad\text{for every }\theta\in[0,2\pi]
\quad\Longrightarrow\quad
(\mu_\eta(s),\mu_\eta(1-s))\ne(0,0),
\]
under its Rotation Number Hypothesis and the additional condition
\(\mu_\eta(1+i\tau)\ne0\).  Theorem 2 has the analogous antecedent
\[
0\notin[\inf_\theta F_h(s,\theta),\sup_\theta F_h(s,\theta)].
\]
Neither theorem proves that its antecedent holds for every off-critical-line
\(s\).  The paper reports only an exploratory numerical check for one sample
holomorphic weight; that cannot establish the required universal
nonvanishing or interval-exclusion statement.

The encoding of zeta by the scalar functional is not, by itself, the missing
step.  For \(\eta(u)=\{u\}\), Euler summation gives, for \(\Re w>1\),
\[
\int_1^\infty \{u\}u^{-1-w}\,du
=\frac1{w-1}-\frac{\zeta(w)}w,
\]
and therefore the definition
\[
\mu_\eta(w)=-1-(1-w)\int_1^\infty \{u\}u^{-1-w}\,du
\]
indeed yields
\[
\mu_{\{t\}}(w)=\frac{1-w}{w}\zeta(w).
\]
This identity only translates simultaneous vanishing into a zeta statement;
it does not prove the universal hypothesis needed by Theorem 1 or Theorem 2.
The abstract-prime-system expression on p. 5 is likewise a definition and
reformulation; no theorem there establishes the required condition for the
ordinary primes.

Thus this source supplies no complete unconditional zero-exclusion theorem
and no unconditional RH proof.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
