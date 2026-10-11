import OAI.NumberTheory.DirichletL.Nonvanishing
import OAI.NumberTheory.DirichletL.Hecke.Nonvanishing

/-!
Acceptance probe for the pinned openai/math project
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb.
Check this file in that project's Lean environment after building the two
imported entry modules. It adds no axioms, incomplete proofs, or new hypotheses
to the imported theorems. The examples also check the public proposition types.
-/

example {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0 :=
  OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re hs

example {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0 :=
  OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re χ hs hpole

example (χ : OAI.SevenEighths.HeckeFamily.Character) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ.residue = 1 ∧ s = 1)) :
    OAI.SevenEighths.HeckeFamily.LFunction χ s ≠ 0 :=
  OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re χ hs hpole

#print axioms OAI.SevenEighths.CenteredMomentEnergyCertifiedExistence.terminal_certificate
#print axioms OAI.SevenEighths.ProbeFinalAssemblyUnconditional.detector_certified_bands
#print axioms OAI.SevenEighths.ProbeFinalAssemblyUnconditional.dirichlet_nonzero
#print axioms OAI.SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero
#print axioms OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.SevenEighths.HeckeRayFamily.LFunction_ne_zero_of_seven_eighths_lt_re
