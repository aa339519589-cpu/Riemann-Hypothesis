# Finite-pivot obstruction for the actual odd theta source window

2026-10-13. Result type: rigorous finite-codimension consequence of the existing growing-jet construction, with a new existential constrained-old Schur consequence. The final research goal remains a complete unconditional proof of RH; **no RH proof or zero exclusion follows here**.

## 1. Precise input, with an explicit rate

Use the exact polar-inclusive odd source form in ../20261012_localized_odd_schur/SOURCE_FORM.md, defined on odd functions supported in (-a,a):
\[
\mathfrak A_a[z]=\frac1{2\pi}\int b(t)|\widehat z(t)|^2dt-C_0\|z\|^2
-2\sum_{2\le n<e^{2a}}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\!\int\overline{z(x)}z(x+\log n)dx
-2\left|\int\sinh(x/2)z(x)dx\right|^2 ,
\]
with its maximal compact-window Gamma form domain, b(t)=Re psi(1/4+it/2)-psi(1/4). This is the actual fully signed finite-window source form; it is distinct from the weighted even Hilbert operator H. On compact supports the finite prime sum includes every active prime power; the earlier full-source proof pays all other primes.

Let a_k=(log k)/2. For each fixed complex smooth profile W compactly supported in (0,pi), the *linear* Laguerre/growing-jet construction of ../20261013_growing_theta_trial/LAGUERRE_SCHUR_TRIAL.md, equations (9)-(10b) and (26)-(29), gives
\[
u_k(W)=v_k(W)+y_k(W)\in\operatorname{Dom}(\mathfrak A_{a_{k+1}})^{1/2},
\]
where v_k lies in the old window |x|<=a_k, y_k lies in the disjoint new collar a_k<|x|<a_(k+1), and
\[
\|y_k(W)\|^2\to2\int_0^\pi |W(s)|^2e^{-2s}ds.\tag{1}
\]
Here Dom(form) is intended by the displayed notation, not the operator domain. The synthesis is complex-linear: the Laguerre coefficients are linear under the explicitly chosen conjugate-linear-first inner product, the scaled Taylor inverse does not depend on W, and each other operation is linear.

The earlier note records the rate ingredients for every **fixed integer p>2**:
\[
m_k=\lfloor(\log k)^{1/4}\rfloor,\quad
\epsilon_{0,k}=O_W(m_k^{-p}+k^{-1+o(1)}),\quad
\epsilon_{1,k}=O_W(m_k^{1-p}+k^{-1+o(1)}),\quad
A_k=k^{o(1)}.\tag{2}
\]
Its equation (26), paying the full Gamma, signed prime series, and coefficient-two polar contribution, is the *absolute* quadratic bound
\[
|\mathfrak A_{a_{k+1}}[u_k(W)]|
\le C_W((1+\log k)\epsilon_{0,k}^2+\epsilon_{1,k}^2)
+C_W A_k^2(e^{-ck}+(\log k)/\sqrt k+k^{-1/2}).\tag{3}
\]
Therefore, for every fixed N>0 and W, choosing p>2N+4 gives
\[
\boxed{|\mathfrak A_{a_{k+1}}[u_k(W)]|
   \le C_{W,N}(\log k)^{-N}}\qquad(k\ge K_{W,N}).\tag{4}
\]
The constant depends on W, N and the fixed cutoff family. Nothing is uniform over an infinite-dimensional ball of profiles.

## 2. Uniform finite-dimensional flatness on actual compact windows

**Theorem 1.** For each fixed M>=1 and N>0, there are M-dimensional subspaces U_(k,M) of the *unchanged original* odd source-window form domain, for all sufficiently large integers k, satisfying
\[
\boxed{\sup_{z\in U_{k,M}\setminus\{0\}}
 \frac{|\mathfrak A_{a_{k+1}}[z]|}{\|z\|_2^2}
 \le C_{M,N}(\log k)^{-N}.}\tag{5}
\]
Moreover, restriction to the new collar is injective on U_(k,M), with lower L2 norm bounded independently of k for that fixed M.

**Proof.** Choose M smooth profiles W_1,...,W_M with pairwise disjoint compact supports in (0,pi) and weighted norms \(\int_0^\pi|W_j|^2e^{-2s}ds=1\). Form \(u_{j,k}=u_k(W_j)\), and write \(u_{j,k}=v_{j,k}+y_{j,k}\). The collar vectors have exactly disjoint physical supports, because the collar coordinate \(s=\pi e^{2|x|}-\pi k\) is injective on each positive wing and reflected oddly. By (1), for all sufficiently large k,
\[
\|\sum c_jy_{j,k}\|_2^2
=\sum|c_j|^2\|y_{j,k}\|^2\ge\sum|c_j|^2.\tag{6}
\]
Old and collar supports are disjoint, hence
\(\|\sum c_ju_{j,k}\|_2^2\ge\sum|c_j|^2\); the M vectors are linearly independent.

By complex linearity \(u_k(W_i\pm W_j)=u_{i,k}\pm u_{j,k}\), and similarly for \(W_i\pm iW_j\). Apply (4) to this *fixed finite list* of profiles. Hermitian polarization then bounds every entry of the actual M-by-M quadratic Gram \(\mathfrak A[u_{i,k},u_{j,k}]\) by \(C_{M,N}(\log k)^{-N}\). For every vector c,
\[
|\mathfrak A[\sum c_ju_{j,k}]|
\le C_{M,N}(\log k)^{-N}(\sum|c_j|)^2
\le M C_{M,N}(\log k)^{-N}\sum|c_j|^2.
\]
Use (6) to conclude (5). All gamma and prime cross terms are retained automatically in the Hermitian polarized *actual form*. QED.

## 3. Arbitrary fixed-rank constraints and constrained old Schur trials

**Theorem 2.** Given fixed d>=0,r>=1,N>0, and any k-dependent complex-linear map from the full source form domain into C^d, there is an r-dimensional subspace of its kernel satisfying the bound (5) with constant C_(d,r,N), independent of that map and its norm.

**Proof.** In Theorem 1 take M=d+r. Restrict the map to U_(k,M). Its rank is <=d, so its kernel there has dimension >=r. The estimate (5) applies to every vector in that kernel. QED.

Thus any k-dependent bounded selfadjoint perturbation R_k of rank <=d, even if ||R_k|| grows without bound, leaves r independent directions on which the perturbed source form has absolute Rayleigh <=C_(d,r,N)(log k)^(-N): choose the kernel of R_k. A fixed finite rank cannot yield a k-uniform strictly positive source-window gap. This is *not* a statement about the weighted original even H.

For the previously unclosed restricted-pivot interface, let \(\lambda_k:\mathcal D_{\rm old,k}\to\mathbb C^d\) be arbitrary complex-linear old-space constraints. For M=d+r, restrict \(\lambda_k\) to the span of the M old components v_(j,k). Its coefficient kernel has dimension >=r; its image in the span of M disjoint collar vectors is still injective. Each resulting nonzero collar y has an admissible old trial v satisfying \(\lambda_k(v)=0\) and \(|\mathfrak A[v+y]|\le C(\log k)^{-N}\|y\|^2\). **If** the old compression is coercive on ker(lambda_k), its exact constrained-old Schur variational form therefore obeys
\[
\boxed{\exists\,Y_{k,r}\subset\mathcal D_{\rm collar,k},\quad
\dim Y_{k,r}=r,\quad
\sup_{0\ne y\in Y_{k,r}}
\frac{\operatorname{Schur}^{\lambda}_k[y]}{\|y\|^2}
\le C_{d,r,N}(\log k)^{-N}.}\tag{7}
\]
The trial existence and absolute bound require no coercivity assumption; only the interpretation through a finite Schur infimum does. This statement is **existential in y**, and does not assert that every prescribed collar profile survives pivot projection. No negative Schur sign is established.

## 4. Slowly growing codimension by a rigorous diagonal choice

Choose a countably infinite list of smooth weighted-normalized profiles with pairwise disjoint supports in (0,pi). For each fixed M, Theorem 1 gives K_M such that the M-vector subspace has bound <=1/M for every k>=K_M. Make K_M strictly increasing. Define \(M(k)=\max\{M:K_M\le k\}\). Then \(M(k)\to\infty\), and the k-th source form has a space of dimension M(k) with absolute Rayleigh <=1/M(k). Against **any** constraints of rank at most floor(M(k)/2), rank-nullity leaves >=ceil(M(k)/2) such directions with that same bound. This is a valid existence result only; no explicit rate for M(k) is claimed because profiles have shrinking supports.

The same conclusion holds for finite-rank repairs and, conditionally on coercive restricted old blocks, the constrained-old Schur upper trial.

## 5. Countermodel and RH acceptance

A finite-dimensional example forbids mistaking isotropic form directions for near-zero *eigenvectors*: take A=diag(1,-1) on C^2 and u=(1,1). Then <u,Au>=0 but ||Au||=||u||>0 and spec(A)={-1,1}. Take r direct sums for any dimension r. Theorem 1 concerns quadratic-form Rayleigh values, never ||Au||, and by itself does not identify the sign of any eigenvalue.

The original full RH criterion still requires nonnegativity of the complete even weighted Weil form on the entire ground-orthogonal domain. The odd source-window form is a different realization. These theorems neither prove full-old coercivity nor a nonnegative Schur complement and exclude no off-critical zeta zero.

Internal audit: [REFEREE_FINITE_PIVOT.md](REFEREE_FINITE_PIVOT.md). Exact elementary algebra sanity: [check_finite_pivot.py](check_finite_pivot.py); it does not verify the inherited theta analysis.

**NO NEW UNCONDITIONAL RH THEOREM PROVED.**
