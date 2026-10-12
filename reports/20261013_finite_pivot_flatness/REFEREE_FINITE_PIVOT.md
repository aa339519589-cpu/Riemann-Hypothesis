# Internal audit of the finite-pivot odd-source theorem

2026-10-13. Audit target: FINITE_PIVOT_FLATNESS.md. This is a mathematical self-check of a new consequence of the cited prior growing-jet result; it is not an independent outside referee, a proof-assistant formalization, or an RH verification.

## 1. Dependency and domain checks

The only hard analysis imported from the current main is the fixed-profile result of ../20261013_growing_theta_trial/LAGUERRE_SCHUR_TRIAL.md, using ../20261013_growing_theta_trial/GROWING_JET_FRAME.md and the window domain split in ../20261012_localized_odd_schur/SHARP_WINDOW_DOMAIN.md. It constructs an actual complex-linear map W -> u_k(W)=v_k(W)+y_k(W) into the maximal compact-window odd Gamma source form domain. The *same* original signed prime term and coefficient-two polar form occur at every step. The original weighted even H is a separate operator, and this audit draws no inference from odd-window positivity to H.

No term of the unbounded Gamma operator is evaluated on a vector outside the form domain: every u_k(W), including finite combinations, is an actual compact supported smooth trial. The full source form of the noncompact tail is used only in the inherited exact theta cancellation and is justified by its separate finite-energy and complete-prime absolute summability. There is no finite-rank replacement of the actual source form.

## 2. Rate from previously published inequalities

For each fixed smooth W, the Laguerre expansion has arbitrary fixed Sobolev exponent p. The earlier explicit residual estimate for the exact full source form reads
\[
|q[u_k(W)]|\le C_W\bigl[(1+\log k)\epsilon_0(k)^2+\epsilon_1(k)^2
+A_k^2(e^{-ck}+k^{-1/2}(1+\log k))\bigr].
\]
The actual quoted errors are \(\epsilon_0=O_W((\log k)^{-p/4}+k^{-1+o(1)})\), \(\epsilon_1=O_W((\log k)^{(1-p)/4}+k^{-1+o(1)})\) and \(A_k=k^{o(1)}\). Squaring proves the leading exponents \(1-p/2\) and \((1-p)/2\); the true theta/prime remainder is \(k^{-1/2+o(1)}(1+\log k)\). Thus any prescribed logarithmic power N follows after picking a **fixed** p>2N+4. This calculation is not uniform in W or in an expanding number of profiles, and the new theorem never asserts such uniformity.

## 3. Hermitian polarization and injection

The existing construction is complex-linear in W. With the conjugate-linear-first convention, the cross matrix \(B(u_i,u_j)\) is recovered from \(q(u_i\pm u_j)\) and \(q(u_i\pm i u_j)\). There are only \(O(M^2)\) profiles for each **fixed** M; all have the same arbitrary inverse-log power estimate with a finite maximum of constants and thresholds. Therefore \(|B(u_i,u_j)|\le C_{M,N}(\log k)^{-N}\), irrespective of cancellations among the signed prime components.

The disjoint profile supports on (0,pi) imply exactly disjoint supports of the new collar vectors, on both reflected wings. Each normalized collar has squared norm tending to 2. Since the old and collar portions have disjoint physical supports,
\(\|\sum c_i(v_i+y_i)\|^2\ge\sum|c_i|^2\) for k large. This is sufficient to control the absolute Rayleigh form on the whole M-dimensional trial span. No unproved Riesz estimate on an infinite theta family is inserted.

## 4. Rank and exact constrained-old interpretation

An arbitrary linear map from an M-dimensional space to C^d has kernel dimension >=M-d, with no assumption on its operator norm. This also holds for k-dependent maps, since the previously constructed M-dimensional subspace and its form bound are independent of the map. For a finite-rank R_k the restriction R_k|U has rank<=d and vanishes on the selected kernel. The source-window claim is an obstruction to uniform strictly positive **lower bounds**, not a spectral characterization.

For constraints acting only on old components v_i, rank-nullity applies to their coefficient synthesis even if the old v_i have dependencies. The resulting coefficient kernel is injected into the new collar span (since its y_i are independent), so the final collar subspace has the asserted dimension. Its old trial is admissible by construction. The formula with constrained Schur infimum additionally assumes the **entire constrained old block** is coercive; this premise is not discharged, and the conclusion is only an upper bound for some collar subspace, never a nonnegative or negative Schur sign.

The diagonal selection fixes the infinite list of smooth bumps beforehand. It chooses thresholds one M at a time; M(k) then increases arbitrarily slowly. Thus there is no unsupported uniformity in growing dimension or explicit growth rate.

## 5. Spectral countercheck and execution scope

The exact rational model A=diag(1,-1) in each 2x2 block has q(e1+e2)=0 and norm(A(e1+e2))>0. Direct sums give arbitrary-dimensional q-null spans with no zero eigenvalues. This invalidates any promotion of small absolute **quadratic forms** to small eigenvector residuals or zero eigenvalue existence. The minimal script check_finite_pivot.py was executed separately under Python with Fraction arithmetic and passed finite samples of rank-nullity and this countermodel; it provides **no theta source verification**, whose proof is inherited from the cited reports.

**Audit conclusion:** The finite-pivot source-window near-null statement, its conditional existential constrained-old Schur upper trial, and its nonquantitative growing-codimension corollary follow from the stated fixed-profile growing-jet theorem. The missing original H sign and complete RH proof remain untouched. **NO NEW UNCONDITIONAL RH THEOREM PROVED.**
