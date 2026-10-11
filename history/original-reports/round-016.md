## Round 16 — a fixed compact window cannot close the all-scale criterion

The newest compact-window calculation gives an unconditional lower bound and a
simple-even ground state at one scale (support length \(1.6\)). That is a real
finite theorem, but it cannot be promoted to RH by monotonicity alone.

For the semilocal form define

\[
\mu_\lambda:=\inf_{0\ne f,\;\operatorname{supp}f\subset[\lambda^{-1},\lambda]}
 \frac{QW_\lambda(f,f)}{\|f\|_2^2}.
\]

If \(\lambda_2>\lambda_1\), the admissible space for \(\lambda_1\) embeds into
that for \(\lambda_2\), so

\[
\mu_{\lambda_2}\leq\mu_{\lambda_1}.
\]

Thus a positive certificate at one finite \(\lambda_0\) only gives
\(\mu_\lambda\leq\mu_{\lambda_0}\) for larger windows; it gives no lower bound
there. The global Weil criterion requires nonnegativity for every compact
window. In the semilocal formulation, the exact sufficient endpoint is the
separate statement

\[
\lim_{\lambda\to\infty}\mu_\lambda=0,
\]

because monotonicity would then force every \(\mu_\lambda\geq0\). No finite
collection of positive values establishes that limit: a decreasing function can
agree with all those values and later cross below zero.

The compact-window paper itself states that its second missing spectral step—the
cross-scale convergence of approximate ground states to the zeta zeros—is
untouched. Its large-scale decay theorem is explicitly conditional on RH, and
its proposed asymptotic identification of the profile is stated as a conjecture.
Therefore the fixed-scale simple-even result does not supply the missing
all-scale branch theorem or the global positivity required by Weil's criterion.

### Round 16 status

**Established:** the fixed-window certificate is logically local; the exact
monotonicity relation shows what additional all-scale limit theorem is required.

**Not established:** \(\mu_\lambda\geq0\) for every scale, the limit condition,
cross-scale ground-state convergence, or an unconditional RH proof.
