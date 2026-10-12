# Independent review: sharp-window Gamma form split

**Reviewed:** `SHARP_WINDOW_DOMAIN.md`.

## Verdict

The new domain-splitting proof is sound. It supplies the missing point that Carleman boundedness alone could not supply: truncate the positive Gamma difference form, use the exact disjoint-support identity at every truncation, bound the cross term uniformly, and then pass to the maximal finite-energy domain by monotone convergence. Thus the sharp old/collar projections preserve the natural localized Gamma form domain. The earlier domain caveat is resolved by this proof.

The full localized form is a bounded perturbation of the split Gamma diagonal form: the local constant, finitely many active prime-power translations, and the polar rank-one term are bounded on each fixed window. The cross block is bounded and the actual form domain is the old/new direct sum. The signed Schur identity is valid on that full form domain for an invertible old block; it is a minimization identity only when the old block is coercive positive. Nothing here proves positivity of the new Schur form.

## Kernel and truncation checks

The kernel estimate is correct. From `1-exp(-2u) >= 2u/(1+2u)`,
`u κ(u) <= (u+1/2) exp(-u/2)`. The latter has maximum `2 exp(-3/4) < 2` at `u=3/2`, so `κ(u) <= 2/u` globally.

Split the collar into positive and negative components. Across each shared endpoint, with distances `s,t > 0` from that endpoint, the kernel is bounded by `2/(s+t)`. The Carleman kernel `1/(s+t)` has L2 norm at most `π` by the stated weighted Schur test. Each component operator therefore has norm at most `2π`; combining the two collar components as an orthogonal direct sum gives `||K|| <= 2π sqrt(2)`, as claimed. Positivity of the kernel also yields the absolute bilinear cross bound for `|f0|, |f1|`.

For each fixed epsilon, `κ_epsilon = κ 1_{u>epsilon}` is integrable, so its difference form is bounded on L2. The coefficient and factor in (4) are right: the two ordered cross regions cancel `2 Re <f0,K_epsilon f1>` in the split. Since `0 <= K_epsilon <= K` at kernel level, the absolute cross pairing is uniformly bounded by (3) and converges by dominated convergence. If the full energy of `f0+f1` is finite, (4) bounds the sum of the two increasing nonnegative diagonal truncated energies; monotone convergence makes both component energies finite. Conversely, finite component energies plus the bounded cross pairing give finite energy of the sum and identity (5). This proves the maximal-domain equality, rather than assuming it. The form graph norms are equivalent after the usual L2 shift: the cross term is bounded by a constant times `||f0|| ||f1||`. Reflection invariance passes the decomposition to odd subspaces.

## Full localized blocks and Schur algebra

For the next source window, a prime-power shift with `n >= k+1` has length `log n >= 2 a_(k+1)` and zero overlap up to endpoints of measure zero. Thus the localized prime form is the finite exact sum over integer prime powers `n < k+1`; no prime term is discarded from this compressed form. Each restricted translation is bounded. This is distinct from a global IMS commutator, where the corresponding prime sum would not be truncated. The local `-C0 I` and any coefficient-2 polar rank-one form are bounded on the fixed window and preserve the Gamma domain.

The full form domain in (7) is therefore the product of the old and collar zero-extended Gamma domains, as established in Section 2. Its Gamma cross block is `-K`; the prime cross translations and, in the polar-inclusive version, the rank-one cross block are added once and are bounded. Adding this bounded off-diagonal self-adjoint operator to the diagonal associated operator gives the asserted operator domain `D(C_k) direct-sum D(D_k)` as well as the form-domain decomposition.

Let `B_k` map the new space to the old space, so the block is `[C_k, B_k; B_k*, D_k]`. If `C_k` is self-adjoint and zero lies in its resolvent set, `C_k^(-1)` is bounded and maps into `D(C_k)`. For `y` in the new form domain, `C_k^(-1) B_k y` lies in `D(C_k)`; the triangular transformation therefore preserves the product form domain. Expanding the form gives exactly

`q[x,y] = q_C[x + C^(-1) B y] + q_D[y] - <B y, C^(-1) B y>`.

The sign and conjugation agree with the stated convention (inner product linear in the second entry). This is valid signed algebra when `C_k` is invertible, with no PSD assumption. If `C_k >= c_k I > 0`, it is also the variational minimum over the old variable, attained at `x = -C_k^(-1) B_k y`. If `C_k` is invertible but indefinite, the identity still holds, but that old-variable infimum need not be finite. The note correctly leaves positivity of the resulting Schur form as an independent obligation.

## Scope

- **Accepted:** the sharp-window maximal-form domain splits; the factor `1/2`, the two-sided collar constant `2π sqrt(2)`, and the prime cutoff `n < k+1` check out.
- **Accepted conditionally as stated:** operator-domain and Schur formulas assume the old block is self-adjoint and invertible; minimization additionally assumes coercive positivity.
- **Not proved:** positivity of the new Schur form, any missing P2 baseline/source inequality, uniform old spectral gap, or RH.
