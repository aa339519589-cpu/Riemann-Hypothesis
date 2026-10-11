## Round 259 — A/B result: Part 4 yields an exact recovery-window theorem, but leaves the area inequality open

Source inspected: Rainer Andreas Mittermeier, *Recovery Witnesses in the
Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact
Quantifier Reduction for the Riemann-Hypothesis Tail -- Part 4*, Zenodo
record [22076079](https://zenodo.org/records/22076079), PDF SHA-256
903d84da9f1c66aca1159a97f8c568a0431f704615ac44f62e88c636c66accbf.
The source itself states that its remaining target is an
RH-independent proof of \(J_q\le C_q\) at every recovery witness.

### VERIFIED PROOF CHAIN addition

Let the prime-power events be
\(\ell_j<\ell_{j+1}\), with positive weights \(w_j\), and let
\[
W_j=\sum_{i\le j}w_i,\qquad
Y_j=W_j-A'(\ell_j),\qquad
\delta_j=A'(\ell_{j+1})-A'(\ell_j).
\]
On the open interval
\(I_j=(\ell_j,\ell_{j+1})\), no arithmetic jump occurs, so
\[
Y(t)=W_j-A'(t).
\]
Because \(A''(t)>0\), \(A'\) is strictly increasing and \(Y(t)\) is
strictly decreasing on \(I_j\). Therefore \(Y\) has a unique zero in
\(I_j\) if and only if
\[
A'(\ell_j)<W_j<A'(\ell_{j+1}),
\]
which is equivalent to
\[
0<Y_j<\delta_j.
\]
Since \(\Psi'=-Y\), this zero is exactly the unique strict interior
stationary minimum of \(\Psi\) on \(I_j\). If \(Y_j=\delta_j\), the zero
occurs at the right endpoint and is the corresponding boundary-contact
case; \(Y_j\le0\) or \(Y_j>\delta_j\) gives no such recovery contact after
the event.

The same condition has an exact weighted-Chebyshev form. With
\[
\Sigma_{1/2}(x)=\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n},
\qquad
E_{1/2}(x)=\Sigma_{1/2}(x)-2\sqrt x,
\]
the power-series expansion of the displayed service slope gives
\[
A'(\log x)=2\sqrt x-\alpha+R_A(x),
\qquad
R_A(x)=2\sum_{m\ge1}
\frac{x^{-(4m+1)/2}}{4m+1}.
\]
At an event \(q\), \(W_q=\Sigma_{1/2}(q)\), hence
\[
Y_q=E_{1/2}(q)+\alpha-R_A(q).
\]
Thus a strict recovery witness satisfies the exact level window
\[
-\alpha+R_A(q)
<E_{1/2}(q)
<-\alpha+R_A(q)+\delta_q.
\]
These are identities and inequalities derived from the event dynamics; no
zero-location hypothesis is used.

### Remaining RH load-bearing claim

The recovery-window condition constrains the endpoint level only. It does
not bound the intervening smoothed area
\[
J_q=\int_a^sP_0(a,t)\,dt
\]
against the exact capacity \(C_q\). The source's proposed completion
\[
J_q\le C_q
\quad\Longleftrightarrow\quad
V_q\ge0
\]
is still unproved at every recovery witness. The endpoint window therefore
does not close the RH criterion.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的恢复窗口及其加权 Chebyshev 形式，但没有产生新的无条件 RH 证明进展。
