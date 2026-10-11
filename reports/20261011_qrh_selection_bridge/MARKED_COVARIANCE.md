# LCM covariance and the full marked resonance block

This note strengthens the expanding-row results in [MARKED_SEXTIC_MEAN_SQUARE.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/abad06c04fa9672e2c0338f6ecf334cb7c77eff5/reports/20261011_qrh_selection_bridge/MARKED_SEXTIC_MEAN_SQUARE.md) (fixed commit `abad06c04fa9672e2c0338f6ecf334cb7c77eff5`). It concerns the exact corrected row B_D, with all original characters and zero extensions. The conclusion applies to the complete zero-Poisson-frequency Gram matrix of a fixed slot family, including different markings which share the same physical sextic core. It does not estimate the remaining nonzero Poisson frequencies in the short physical window.

## 1. Uniform two-mark covariance

Use the definitions and means of that note. Fix an allowed s, two squarefree good markings D,D', and arbitrary U,V>0. Write L=lcm(D,D') and G=gcd(D,D'). Then
\[
 \boxed{\left|\mathsf M\left(B_D(U;m,s)
             \overline{B_{D'}(V;m,s)}\right)\right|
 \le\frac C{q_L}\prod_{p\mid L/G}
       (1+q_p^{-1}-2q_p^{-2}).}                         \tag{1}
\]
The constant C is independent of both scales, both markings, and s. The same bound holds for the covariance with the additional original weight |g_s(m)|^2/q_s. No comparison between U and V is assumed. All means first fix these parameters.

**Proof.** Write n=v k^2 and n'=v'k'^2. The exact sextic-core orthogonality proves that only (c,v)=(c',v') contributes, even with the external normalized Gauss square. In every surviving product, the original unit masks have average at most phi(L)/q_L.

Partition the primes of L uniquely into E,F,H: E contains those dividing c, F those dividing v but not c, and H those dividing neither. Put H_D=gcd(H,D), H_{D'}=gcd(H,D'). Then
\[
 c=E c_0,\quad v=Fv_0,\quad k=H_Dk_0,\quad k'=H_{D'}k'_0.
\]
After taking absolute values and dropping only positive restrictions, this part of the covariance has prefactor
\[
 q_E^{-1}q_F^{-2}q_{H_D}^{-2}q_{H_{D'}}^{-2}.            \tag{2}
\]
Its remaining double sum is the Hilbert inner product of the two vectors whose squared norms are the main note's S-functions at
\[
 U/(q_Eq_F^3q_{H_D}^6),\qquad
 V/(q_Eq_F^3q_{H_{D'}}^6).
\]
Cauchy--Schwarz and the uniform bound on S show that this inner product is at most C, simultaneously for all two scales.

For p|G, assigning p to E,F,H in (2) gives the three local factors P^{-1},P^{-2},P^{-4}. For p|L/G they are P^{-1},P^{-2},P^{-2}, since only one of k,k' is required to contain p. Multiplying the original unit density and summing all partitions therefore gives
\[
 \begin{split}
 |\mathsf M(B_D\overline{B_{D'}})|
 &\le C\frac{\phi(L)}{q_L}
  \prod_{p\mid G}(P^{-1}+P^{-2}+P^{-4})
  \prod_{p\mid L/G}(P^{-1}+2P^{-2})\\
 &\le \frac C{q_L}
  \prod_{p\mid L/G}(1+P^{-1}-2P^{-2}).
 \end{split}
\]
The omitted common-prime factor is (1-P^{-1})(1+P^{-1}+P^{-3})<=1. This proves (1). Uniform absolute convergence gives the existence of these mixed means; alternatively polarize the finite truncated periodic rows before passing to the limit. The weighted case uses exactly (G2) of the previously proved Gauss corollary. No new treatment of high-power Gauss sums is needed.

For every P>=2, 1+P^{-1}-2P^{-2}<=3/2. Thus if D and D' each have at most K prime factors,
\[
 |\mathsf M(B_D\overline{B_{D'}})|\le C_K/q_L,          \tag{3}
\]
with C_K independent of the moving prime norms. We do not assert that the product in (1) may be discarded with a constant uniform over unrestricted K.

## 2. The entire fixed-slot resonance matrix

Fix K disjoint prime sets P_1,...,P_K. For each i, assume
\[
 a_i P_i\le q_p\le b_iP_i\quad(p\in\mathcal P_i),
\]
where a_i,b_i>0 are fixed, and P_i>=1 may move. Empty slots give an empty family and need no estimate. Form all markings D=product_i p_i with p_i in P_i. Give each D an arbitrary positive scale U_D, and put
\[
 V_D(m)=q_D^{1/2}B_D(U_D;m,s).
\]
Let K_{D,D'}=M(V_D conjugate V_D') be the complete expanding-row Gram matrix, optionally with the same normalized Gauss square weight for every entry. It is positive semidefinite, and (3) gives
\[
 |K_{D,D'}|\le C_K\frac{\sqrt{q_Dq_{D'}}}{q_{\operatorname{lcm}(D,D')}}.
                                                               \tag{4}
\]
Disjointness of the prime sets makes the kernel on the right a product of slot kernels. For a fixed D its exact row sum is
\[
 \sum_{D'}\frac{\sqrt{q_Dq_{D'}}}{q_{\operatorname{lcm}(D,D')}}
 =\prod_{i=1}^K\left[
 1+\sum_{\substack{p'_i\in\mathcal P_i\\p'_i\ne p_i}}
       (q_{p_i}q_{p'_i})^{-1/2}\right].                 \tag{5}
\]
Ideal counting gives #P_i<=C b_i P_i, while each summand is at most (a_iP_i)^{-1}. Hence (5) is bounded by a constant depending only on the fixed slot system, uniformly in all moving prime sets and scales U_D. The matrix is Hermitian, so the same bound applies to its column sums. The elementary Schur inequality now yields
\[
 \boxed{\mathsf M\left|\sum_D z_D B_D(U_D;m,s)\right|^2
 \le C_{\rm slots}\sum_D\frac{|z_D|^2}{q_D}.}           \tag{6}
\]
This holds for every complex coefficient family z_D, without a factor equal to the number of markings. Equation (6) also holds with |g_s|^2/q_s inside the mean.

For bounded product-form slot weights z_D=product_i w_i(p_i), one consequently has
\[
 \mathsf M\left|\sum_D z_D B_D(U_D;m,s)\right|^2
 \le C_{\rm slots}\prod_i\sum_{p\in\mathcal P_i}
                         \frac{|w_i(p)|^2}{q_p}=O_{\rm slots}(1).
                                                               \tag{7}
\]
Only fixed ring ideal counting is used here; no prime number theorem or prime-window lower bound is required. The marked scales can in particular be U_D=Zq_D, exactly as in the original compensation formula.

## 3. What remains at the actual physical row scale

The full zero mode includes different physical (E,F,c_0,n_0) decompositions with the same ordered sextic core (c,v). Those are not discarded as off-diagonal: (1)-(7) control all of them jointly.

These conclusions control the complete residue average, equivalently the zero Poisson frequency of finite truncations and its convergent completed limit. At a fixed short row disk one must still estimate the nonzero dual frequencies. The Schur bound does not move the mean inside a changing short window, and no such exchange is claimed.

Independent verification: [REFEREE_MARKED_COVARIANCE.md](REFEREE_MARKED_COVARIANCE.md). The original corrected row, zero masks and all-scale positive majorant remain the user’s inherited contributions at commit `e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8`; this covariance proof uses no 7/8 zero-free input.
