import Init

set_option autoImplicit false

namespace RHToolchainSmoke

theorem naturalAddZero (n : Nat) : n + 0 = n := rfl

/-- A finite prefix alone cannot imply a universal predicate on natural numbers. -/
theorem finitePrefixInsufficient (cutoff : Nat) :
    ∃ P : Nat → Prop, (∀ n, n < cutoff → P n) ∧ ¬ (∀ n, P n) := by
  refine ⟨fun n => n < cutoff, ?_, ?_⟩
  · intro n hn
    exact hn
  · intro h
    exact (Nat.lt_irrefl cutoff) (h cutoff)

end RHToolchainSmoke

#print axioms RHToolchainSmoke.naturalAddZero
#print axioms RHToolchainSmoke.finitePrefixInsufficient
#eval "RH toolchain smoke only; no Riemann Hypothesis result."
