## Round 51 — what critical-line completeness does and does not prove

There is a separate, rigorous obstruction to a frequently attempted shortcut.
Let \(\Gamma_C\) be the ordinates of the zeros on the critical line, counted
with multiplicity. The unconditional positive-proportion theorem for critical
zeros gives

\[
 N_C(T)\gg T\log T.
\tag{51.1}
\]

For any bounded interval \(I\), the exponentials

\[
 \{e^{-i\gamma u}:\gamma\in\Gamma_C\}
\]

are consequently complete in \(L^2(I)\). Indeed, if \(f\in L^2(I)\) is
orthogonal to every one of them, its zero extension has Fourier transform

\[
 \widehat f(z)=\int_I f(u)e^{-izu}\,du,
\]

an entire function of finite exponential type. It vanishes at every point of
\(\Gamma_C\). A nonzero finite-exponential-type entire function has only
\(O(T)\) zeros in \(|z|\le T\), whereas (51.1) supplies \(\gg T\log T\)
zeros; hence \(\widehat f\equiv0\) and \(f=0\).

This does **not** exclude the Bombieri zero-collapse relation. That relation
is an exact weighted range statement,

\[
 \sum_{\gamma\in\Gamma_C}\frac{w_\gamma}{d_\gamma}e^{-i\gamma u}
 =h_E(u)\quad(u\in I),\qquad w\in\ell^2,
\tag{51.2}
\]

where \(h_E\) is the finite off-critical/boundary packet. Completeness gives
only \(h_E\) in the closure of the critical exponential span; it does not give
or deny membership in the range with the required weighted \(\ell^2\) cost.
The missing statement is therefore a quantitative, zeta-specific range
exclusion (or a bounded-cost interpolation theorem), not an ordinary
orthogonality argument.

The positive-proportion input is due to Selberg-type critical-line results; a
classical explicit form is Conrey's paper,
https://doi.org/10.1515/crll.1989.399.1.

**RH status:** the exact weighted range-exclusion statement remains the
load-bearing unresolved step; no unconditional proof has been produced.
