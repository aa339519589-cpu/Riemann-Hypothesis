# Mathematical review: fractional origin and complete boundary estimate

Reviewed text: [Fractional origin control and a sharper complete prime-boundary bound](FRACTIONAL_ORIGIN_BOUNDARY.md).

Disposition: pass, conditional on the cited source-smoothing, weighted
Sobolev, origin-equation, and exact odd-variation inputs. A separate
model-assisted read-through found no error in the normalization, complete
prime-power convergence, local equation signs, or boundary exponent. This
is not proof-assistant verification or an external human review of the
upstream theorems.

The source mass is \(M=\|g/\mu\|_2^2\le193P_0\), so the quoted
source and fixed exponential-weight Sobolev bounds scale as
\(C\sqrt{P_0}\), without a depth loss. Since
\(d_n-2\epsilon>0\), the cutoff identity in the proof is exact.
It gives an \(n^{-1}\) factor, and
\(\sum\alpha_n n^{-1}\le\sum(\log n)n^{-3/2}<\infty\).
Both complete loads therefore converge in the stated Sobolev norm and
agree with their existing local \(L^2\) definitions. No prime-point
sample is assumed.

The strict choice \(s<s_0<1/16\) correctly pays the logarithmic
multiplier. The source equation divides by the smooth positive row
\(L\), using \(Vg=Lr\); it does not divide Sobolev estimates through
an erroneously bounded \(V\sim c/x\). The multiplier \(\psi/x\)
extends smoothly at zero. The identity
\(\delta W=C_0g+F_+-F_--B_og\) and its signs are correct.
Thus the ratio, \(g/x\), and divergence incur precisely the displayed
\(\delta^{-1}\) factor.

On the fixed interval, \(H^s\) embeds into
\(L^{2/(1-2s)}\). Restriction to an interval of length \(t\)
therefore supplies \(t^s\) in the \(L^2\) norm. Applied to both
factors of the complete triangle estimate, this gives
\(\delta|D_{\rm pr}|\le C a^{1+2s}P_0\), retaining both corners
and every prime-power label. The fixed-profile constant is permitted
to depend on the kernel; no uniformity over varying profiles is claimed.

The absolute estimate holds for each actual scalar supercritical source.
Only the final inference from \(Q_\delta\succeq0\) requires the largest
eigenvalue. The text correctly claims no endpoint exponent, source trace,
signed covariance comparison, or RH conclusion.
