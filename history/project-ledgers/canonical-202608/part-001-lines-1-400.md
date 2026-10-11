# RH Research Ledger — Canonical Project Record

**Project:** Riemann Hypothesis research campaign  
**Canonical ledger status:** Persistent, append-only research ledger  
**Current phase:** Round 8 launched  
**Core rule:** Every returned model report is only **REPORT CLAIM** until independently re-derived and audited from the project definitions.

---

## 0. Non-negotiable audit protocol

For **every single returned report**, including multiple reports pasted in one user message, create **one independent audit entry per report**. Never merge multiple reports into one audit.

Each audit must return and record exactly three layers:

### I. Validity verdict
Allowed top-level verdicts:

- **成立**
- **不成立**
- **条件成立**
- **证据不足 / 暂不可判定**

The audit must explicitly separate:

- **事实**
- **推论**
- **假设**
- **未知**

For a verdict of **成立**, the record must include the full auditable logic chain:

1. premises;
2. established facts;
3. evidence;
4. key derivations;
5. hypotheses;
6. necessary conditions;
7. sufficient conditions;
8. counterexample / hostile audit;
9. conclusion;
10. why the chain closes.

For **不成立**, record every load-bearing failure, why it is a failure, which implication it breaks, what conditions would be needed for validity, and which conditions are actually available.

For **条件成立**, state exactly what is proved, what remains missing, and whether the missing condition is merely technical or carries the final conclusion.

For **证据不足 / 暂不可判定**, distinguish lack of factual information from inability to infer the conclusion. Never equate “not yet proved” with “false”.

### II. Route decision
For each independently audited report:

- choose route **X** and explain why;
- identify a genuinely competitive route **Y**, if one exists;
- compare X and Y on:
  - validity conditions;
  - potential payoff;
  - mathematical cost;
  - risk;
  - constraints/no-gos;
  - current evidence;
- explain strictly why X is selected over Y.

If no credible Y exists, classify why as exactly one of:

- **信息不足**
- **可行域唯一**
- **客观约束排除其他路线**

### III. Ledger update
Every entry must explicitly distinguish:

- **已确认事实**
- **成立点**
- **失败 / 错误点**
- **仍属假设**
- **未知 / 待验证**
- **下一步路线**

No model verdict, inference, working hypothesis, or temporary preference may be silently promoted to an established fact.

---

## 1. Epistemic / proof standard

The project uses only:

- **correct**;
- **incorrect**;
- **unfinished**.

There is no “almost proved”.

Additional project rules:

1. Builder/Killer conflicts are settled by verifiable mathematics, not model identity.
2. One unproved load-bearing lemma means no proof.
3. “No counterexample found” is not proof.
4. Until a concrete impossibility theorem excludes a path, the path remains logically open; this does **not** imply it will succeed.
5. Full target:

   \[
   \xi(\rho)=0\Longrightarrow \Re\rho=\frac12
   \]

   unconditionally, noncircularly, and with arbitrary multiplicity.
6. User controls goals/resources/question pressure; technical route selection is the assistant's engineering responsibility.
7. Progress is measured in **research rounds**, not hours/days/weeks.

---

## 2. Model / resource discipline

Current resource policy:

- **SOL Extra High:** normal research main force.
- **SOL Pro:** only true load-bearing single-node deep reasoning, candidate closure, major conflicts, or final audits.
- **Luna / Terra:** structural exploration, long searches, classification, countermodel work according to task fit.
- **SOL Max / Ultra:** candidate closure and independent high-grade audit.
- **Codex Max / Ultra:** large search trees, parallel contexts, formalization, terminal/computation; advantage is orchestration, not assumed stronger base reasoning.

Never rank Terra Ultra and SOL Pro on one scalar “strength” axis.

---

# PART A — PRE-ROUND HISTORY AND EARLY ROUTE ARCHAEOLOGY

## A0. Earliest recoverable route-generation phase

### Historical status
The earliest recoverable project stage predates Round 1. The campaign explored and stress-tested a large family of nonstandard RH mechanisms, including:

- Chebyshev / polynomial orbit constructions;
- dyadic resolvent / band-pass observables;
- Lee–Yang / tensor formulations;
- heat-flow / collision invariants;
- exponential tilts and reflection / Lévy-type formulations;
- operator positivity and canonical-system ideas;
- quantum-channel / cocycle / nonautonomous transport ideas;
- Loewner/Pick mechanisms;
- Brown-measure / free-probability ideas;
- stochastic localization;
- matrix scaling / Sinkhorn;
- Hilbert projective contraction;
- optimal transport;
- Hermite–Biehler / de Branges style endings;
- positive-kernel and Herglotz/Weyl reformulations.

### Retrospective classification
**已确认事实:** A broad route-search phase occurred and produced a systematic anti-circularity methodology.

**成立点:** The project learned to reject candidate endings that merely rewrite RH as positivity, monotonicity, bounded transport, or zero-exclusion in another language.

**失败 / 错误点:** Many attractive mechanisms had no independent arithmetic rigidity and collapsed to known RH-equivalent criteria or generic geometric facts.

**仍属假设:** No surviving early mechanism is presently promoted as an RH route.

**未知 / 待验证:** Individual archived route files may contain local theorems that require future independent re-audit if reused.

**下一步路线:** Historical archive only; do not reopen catalog search unless current surviving categories collapse and a genuinely new datum appears.

---

## A1. Old quantitative lower-bound campaign

### Strongest promoted project bound

\[
X_{\rm BA}=0.6725423273723657732332425686296255\ldots
\]

Historical project records state this was promoted after countermodel, algebraic, analytic/source, clean-room, exact rational/Arb/Lean finite-core, and final integration audits.

### Information-class ceilings

Reduced local three-point information class:

\[
0.6725423488634452180\ldots<0.68.
\]

Full fixed-kernel two-point information class:

\[
0.6766804570526070818\ldots<0.68.
\]

Order-14 abstract zero-side gates exceeded 0.90, but actual prime-side order-14 moment transport remained open.

### Active old arithmetic source problem

`COMMON-FOUR-ENTRY-CENTRAL-SOURCE` inside `JOINT-UNITARY-AFFINE-RATIONAL-SAMPLING`.

Structural lesson carried into the RH project:

\[
\boxed{\text{complete unsplit arithmetic source must interfere before character/frequency/v/orientation diagonalization or absolute values}}
\]

and positivity / small norm should be imposed only after global recombination.

### Retrospective ledger

**已确认事实:** The quantitative campaign contains a more mature formal/certificate audit culture than the later structural RH campaign. The above numbers are frozen project records, not current RH targets.

**成立点:** It established the project-wide “interference first, positivity later” operation-order principle.

**失败 / 错误点:** Lower-bound improvement is not the present research target; a 68% target is not to be reopened merely because of this archive.

**仍属假设:** Order-14 actual prime-side transport remains unproved in the archived campaign.

**未知 / 待验证:** If any old arithmetic-source theorem is imported into RH work, its exact source typing and theorem domain must be independently rechecked.

**下一步路线:** Preserve only transferable structural lessons; do not create a dedicated lower-bound branch.

---

## A2. Notes 233–241 — stationary positivity archaeology

### Note 233 — radial-current transform
Reported identity:

\[
\iint \mathfrak R[\phi]e^{zt+\bar wu}
=
\frac{F'(z)\overline{F(w)}+F(z)\overline{F'(w)}}{z+\bar w}.
\]

For the Riemann kernel, positivity of the radial current is RH-equivalent.

### Note 235 — positive defect / compensated current
Algebraic defect identities survive, but the decisive positivity condition is again RH-equivalent.

### Note 236 — positive square-mode atoms
Positive atoms, cusp cancellation, and equal-weight rigidity were developed; the full polarized cross-current was unresolved.

### Note 238 — fixed bounded control
Fixed bounded-control realization was reported impossible because saturation forces a stationary tail-renewal equation incompatible with the theta tail.

### Notes 240–241 — stationary scalar gluing
Stationary exact reconstruction reduces to a Cauchy/Weyl transform of the form

\[
X/X'=\operatorname{spv}\int \frac{d\mu(\lambda)}{\lambda-z},
\]

with positive measure iff RH.

### Retrospective ledger

**已确认事实:** The project identified stationary scalar positivity as a detector/reformulation, not an activation mechanism.

**成立点:** These notes generated the durable principle

\[
\boxed{\text{interference first, positivity later}}.
\]

**失败 / 错误点:** Stationary positive-kernel/Weyl/Herglotz endings cannot be counted as independent RH progress merely because they are exact.

**仍属假设:** Any detailed analytic identity reused later must be re-audited at point of use.

**未知 / 待验证:** Publication-level novelty of these formulations was never established.

**下一步路线:** Nonstationary / non-scalar / pre-positivity mechanisms only.

---

# PART B — ROUNDS 1–3: CATEGORY NO-GOS

## Rounds 1–3 — closed historical category compression

The following categories were recorded as killed or structurally insufficient:

1. stationary scalar spectral / renewal route;
2. fixed bounded-control feedback;
3. fixed zero eigenstate + assumed bounded/power-bounded Hilbert/Banach transport, unless an independent ambient theorem supplies the bound;
4. cancellation-only RG admissibility;
5. full-channel pre-Gramization;
6. generic positive-even Fourier/self-dual source;
7. ordinary Herglotz/Pick “no swallowing”;
8. generic positive-state to connected/cumulant positivity;
9. local cusp cancellation as a substitute for global current positivity;
10. reflected copies that add no independent information;
11. wrong invariants such as rank/codimension, curvature gauge, whitening, or integer indices that erase or miss the continuous radial defect.

### Retrospective ledger

**已确认事实:** These categories form the historical no-go ledger used to prevent route recycling.

**成立点:** The campaign learned that generic conservation, positivity, reflection, and boundedness do not by themselves distinguish Riemann zeros from generic reciprocal-hyperbolic countermodels.

**失败 / 错误点:** Do not reopen any category by renaming the same assumption.

**仍属假设:** Some no-go proofs have not yet been re-audited under the new mandatory independent-validation protocol.

**未知 / 待验证:** Exact category boundaries may need refinement if a future construction lies outside the original hypotheses.

**下一步路线:** Only mechanisms carrying genuinely additional arithmetic information beyond these generic categories.

---

# PART C — ROUND 4

## R4-1. Zero cancellation -> nonzero state

### Modular-defect construction
Reported:

\[
\mathfrak m_z'(0)=2(F(z)-1/2),
\]

so at a zero of F:

\[
\boxed{\mathfrak m_z\neq0,\qquad \mathfrak m_z'(0)=-1.}
\]

### Theta boundary system

\[
H=L^2((0,\infty),du;\mathbb C^2),
\qquad
D=\sigma_3\left(\frac d{du}-a(u)\right),
\]

\[
j_w(u)=\sqrt{\Phi(u)}(e^{wu},e^{-wu})^T,
\qquad
Dj_w=wj_w,
\]

\[
B(j_w)=F(w)=\xi(1/2+w).
\]

At an order-m zero, the jets

\[
j_w,j'_w,\dots,j_w^{(m-1)}
\]

form an independent root chain.

### Current audit status
**状态:** **高可信 / 尚未按新协议完成全量独立审计。** Core algebraic pieces are straightforward to rederive; detailed domain/analytic parts remain to be audited if they become load-bearing.

---

## R4-2. Natural quadratic conservation classification

Reported classification in the stated C1 Hermitian Hilbert-Schmidt class:

\[
K=cK_0,\qquad c\in\mathbb R.
\]

Selected value:

\[
h_0(j_w,j_w)=\frac{\Im F(w)}{\Re w}
\]

for \(\Re w\ne0\). Thus at an off-axis F-zero the selected diagonal is zero.

### Current audit status
**状态:** **强一审支持 / 未完成新协议的完整独立复核。** The characteristic-PDE derivation and boundary classification are concrete and internally coherent.

### Consequence
Natural degree-2 indefinite conservation does not supply RH rigidity in this category.

---

## R4-3. Nonstationary symplectic transport

Reported conserved defect:

\[
\Omega(\Psi_z^0,\Psi_{-\bar z}^0)
=-2\Re z\,\|\mathfrak m_z\|^2.
\]

Generic pseudo-unitary/symplectic countermodels allow reciprocal hyperbolic exponents \(\pm\delta\), so conservation alone is insufficient.

### Current audit status
**状态:** Core symplectic algebra is direct; endpoint arithmetic rigidity remained absent.

---

## R4-4. Pontryagin / negative-square detector

Reported exact identity:

\[
\boxed{\sup_{0<h\le1/2}\kappa(h)=2M},
\]

where \(M\) is total multiplicity of off-critical quartets, possibly infinite.

