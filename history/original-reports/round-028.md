## Round 28 — source-problem correction: Bombieri's Sections 8 and 11 are different

The preceding weighted-range rounds contain a source-identification issue that
must be corrected before they can carry an RH argument.

### I. Correctness decision

**条件成立 (the operator lemmas are valid, but their Bombieri attribution was
too broad).**

Bombieri's second eigenvalue problem in Section 11 uses the pure local Gram
matrix \(K_{E,N}(\gamma,\gamma')=\int_Ee^{i(\gamma-\gamma')u}\,du\) and the
equation \(K_{E,N}z_N=\lambda_Nz_N\). Its local waveform is
\(F_N(u)=\sum_{\gamma\in\Gamma_N}z_{\gamma,N}e^{-i\gamma u}\), and its mass
inequality is stated in the same unweighted \(z\)-coordinates.

Bombieri's Sections 8 and 10 concern a different, first variational problem.
There one introduces \(z_\gamma=X_\rho\),
\(w_\gamma=d_\gamma z_\gamma\), and
\(d_\gamma=\frac14+\gamma^2\). The finite matrix is built from the
boundary-corrected kernel \(K^*(x,y;t)\), not merely from the pure Gram kernel
above. The normalization in that problem is on \(w\), and its energy identity
contains \(d_\gamma^2|z_\gamma|^2=|w_\gamma|^2\).

Therefore the equations \(Gz_N=\lambda_NDz_N\) and
\(A_N=S_{C,N}D_{C,N}^{-1/2}\) studied in Rounds 20--27 are valid for the
explicit auxiliary generalized model. They are not, without an additional
derivation, the source-normalized Section-11 problem. In particular, the
identification of \(\|c_N\|\) in those rounds with Bombieri's Section-11
source mass is not established. The weighted operator results remain valid
conditional analytic lemmas, but their direct RH attribution is withdrawn.

### II. Correct Section-11 finite Schur system

For the actual pure-Gram problem, split \(z_N=(c_N,e_N)\) into critical and
exceptional coordinates and write \(G_N=K_{E,N}\). If
\(\lambda_N=-\varepsilon_N<0\), the exact equations are

\[
 (G_{CC,N}+\varepsilon_NI)c_N+G_{CE,N}e_N=0,
\tag{28.1}
\]

\[
 c_N=-(G_{CC,N}+\varepsilon_NI)^{-1}G_{CE,N}e_N,
\tag{28.2}
\]

and

\[
 \left[G_{EE,N}+\varepsilon_NI
 -G_{EC,N}(G_{CC,N}+\varepsilon_NI)^{-1}G_{CE,N}\right]e_N=0.
\tag{28.3}
\]

If \(S_{C,N}\) is the finite unweighted critical synthesis and
\(h_N=S_Ee_N\), then \(G_{CC,N}=S_{C,N}^*S_{C,N}\) and
\(G_{CE,N}e_N=S_{C,N}^*h_N\). Hence (28.2) is the unweighted regularized
least-squares equation

\[
 c_N=-S_{C,N}^*(S_{C,N}S_{C,N}^*+\varepsilon_NI)^{-1}h_N.
\tag{28.4}
\]

There is no \(D^{1/2}\) change of variables in (28.1)--(28.4). The correct
finite target is the source-normalized unweighted coefficient geometry,
together with the exceptional direction selected by (28.3).

### III. Hostile audit

The weighted range and tail results in Rounds 24--27 cannot be silently
substituted into (28.1). The Section-11 critical family is locally
overcomplete and its full unweighted synthesis is not a bounded operator on
all of \(\ell^2\); a Riesz-basis subsystem gives exact unweighted
representations but does not select the finite-section eigenvector or its
source norm.

Conversely, (28.1)--(28.4) do not exclude the finite-exception branch. The
limiting equation can still collapse to \(F=0\) on \(E\), and the unweighted
critical kernel/range obstruction recorded in Rounds 12--18 remains
applicable.

### IV. Ledger update

**已确认事实:** Section 11 uses the pure unweighted Gram problem; Sections 8
and 10 use a distinct boundary-corrected first problem with \(z\)-to-\(w\)
weights.

**成立点:** the auxiliary generalized Schur and weighted least-squares
identities in Rounds 20--27 are correct for their stated \(G,D\) model.

**失败 / 错误点:** treating those weighted identities as an already proved
source-faithful reduction of the Section-11 mass-normalized eigenvectors.

**仍属假设:** a theorem linking the weighted auxiliary model to the chosen
Bombieri variational problem.

**未知 / 待验证:** the Section-11 unweighted finite-eigenvector provenance
and any source-specific obstruction in (28.1)--(28.4).

**下一步路线:** continue on the correct unweighted Section-11 branch; keep
Rounds 20--27 as conditional auxiliary analysis only, and do not use them as
an unconditional RH implication.

**RH status:** no unconditional proof has been produced.
