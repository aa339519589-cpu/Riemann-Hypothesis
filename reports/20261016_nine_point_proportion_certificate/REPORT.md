# A certified nine-point window improvement for simple critical-line zeros

**16 October 2026.** A computer-assisted parameter improvement, with a full
all-gap certificate, independent exhaustive replay, and a separate
signed-overflow/undefined-behavior sanitizer replay. This is not a Lean
certificate or a claim of acceptance by an external record service.

## 1. Statement and size of the result

Let N(T) count nontrivial zeta zeros with multiplicity, and let N₀ˢ(T) count
simple zeros on Re(s)=1/2. The conclusion is

\[
 \liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}\ge
 P_*:=\frac{16693751421060564439209480356677}
 {24783250000000000000000000000000}
 =0.6735900828608259384547821757306648\ldots . \tag{1}
\]

The new input is a completely checked finite inequality for an explicit
probability window. The zeta transfer uses the existing certificate principle
in Knausgård, [arXiv:2610.08965v1, Theorem 5.1 and §§2–3,5](https://arxiv.org/html/2610.08965v1).
No new twisted-moment theorem is asserted or required.

At the primary-site check on 16 October 2026, 10:51 UTC, the current recorded
bound was

\[
 P_{\rm old}=\frac{34191001116882886388531117129201664}
 {50760020691785094633026544189453125}
 =0.673581307708495341\ldots .
\]

See [attempt-024](https://www.riemannzeta.fun/submissions/attempt-024) and its
[pinned source](https://github.com/josusanmartin/riemann/blob/9e6ca6615b9dbfec4a1d722995cff0ffe3abf9bb/submissions/attempt-024/proof/Solution.lean).
That source first obtains its bound for simple critical-line zeros before
weakening the count. The exact difference P*−Pold is positive and is about
0.00000877515233, or **0.000877515233 percentage points**. This is a small
quantitative improvement, not a percent-scale zero exclusion and not RH.
The earlier source's recorded formal checks do not constitute formal checking
of our new data or program.

## 2. Explicit window and objective

Put I=[−1/2,1/2], m₀=√2 sin(1/√2), and define, on I,

\[
 f(u)=m_0^{-1}\left(\cos(\sqrt2u)+\sum_{j=1}^{12}c_j\cos(2\pi ju)\right),
 \qquad f(u)=0\quad(u\notin I), \tag{2}
\]
where 10⁹(c₁,…,c₁₂) is

```
13694670, -16312527, 4644034, 5307110, -911968, 4401646,
-5681831, 3684884, -5485934, 5860802, -2204107, 2806387.
```

The cosine perturbations have zero integral, so ∫f=1. Moreover
cos(1/√2)−Σ|cⱼ|>0.68924869, proving positivity on I. Write

\[
 K(t)=\int_I f(u)e^{-2\pi itu}\,du,\qquad w(t)=K(t)^2. \tag{3}
\]

K is real and even, |K⁽ʲ⁾|≤πʲ, and |w‴|≤8π³. The exact transform used
in the ball calculations is, with a=√2/(2π),

\[
 K(t)=\frac{\tfrac12(\operatorname{sinc}(t-a)+\operatorname{sinc}(t+a))
 +\tfrac12\sum_jc_j(\operatorname{sinc}(t-j)+\operatorname{sinc}(t+j))}{m_0},
 \quad\operatorname{sinc}(x)=\frac{\sin\pi x}{\pi x}. \tag{4}
\]

For g=(g₀,…,g₇)≥0, define dᵢⱼ=Σᵢ≤r<j gᵣ and

\[
 F(g)=10^{-8}\left(\sum_{r=0}^7P_rg_r+
                    \sum_{0\le i<j\le8}W_{ij}w(d_{ij})\right). \tag{5}
\]

The pressure numerators are

```
27009, 49712, 65952, 76098, 76098, 65952, 49712, 27009.
```

The W numerators, in lexicographic order of (i,j), are

```
11453652, 0, 9353385, 20180801, 39505410, 72664292, 100000000, 200000000,
22268377, 28293816, 39642409, 46976295, 60494589, 54671414, 100000000,
31270590, 39534992, 51004204, 65685806, 60494589, 72664292,
35007379, 64342382, 51004204, 46976295, 39505410,
35007379, 39534992, 39642409, 20180801,
31270590, 28293816, 9353385, 22268377, 0, 11453652.
```

All weights are nonnegative. P and W are reflection symmetric, and for each
s=1,…,8, ΣᵢWᵢ,ᵢ₊ₛ≤2·10⁸. Also ΣPᵣ=437542. The finite proposition is

\[
 F(g)\ge c:=867000/10^8=0.00867\quad\hbox{for every }g\ge0. \tag{6}
\]

Sections 5–7 give the independently authored certificate proof of (6).
No numerical minimizer is a premise of this proposition.

## 3. Energy and analytic side conditions

For C(f)=∫f²+∬|u−v|f(u)f(v), put H=2−C(f). The stationary
Montgomery–Taylor base and the zero means of the perturbations give exactly

\[
 H=\frac32-\frac{\cot(1/\sqrt2)}{\sqrt2}
 -m_0^{-2}\sum_{j=1}^{12}c_j^2
       \left(\frac12-\frac1{4\pi^2j^2}\right). \tag{7}
\]

For completeness, if h has zero integral, its |u−v| quadratic term equals
−2∫(∫₋₁/₂ᵘh)². The mixed term with the stationary base vanishes; ordinary
cosine and sine orthogonality then gives (7).

The outward ball calculation proves

\[
 H>H_-:=67212547684242257756837921426708/10^{32}. \tag{8}
\]

Set θ=17/20 and γ=13/20. The nonnegative majorant

\[
 G(u)=\gamma\left[\operatorname{sinc}(\theta(u-1/2))+
                     \operatorname{sinc}(\theta(u+1/2))\right]^2 \tag{9}
\]

has Fourier support in [−θ,θ] and mass
Λ=(2γ/θ)(1+sinc θ)<1.78943<2. On I it exceeds f by more than
0.06044. This is certified on 32,768 closed interval cells, using evenness.
The complete kernel table further proves

\[
 w(t)\ge\beta:=13669479/2^{28}>0.05092>c
 \quad (|t|\le\theta). \tag{10}
\]

All these bounds were independently regenerated at both 160 and 320 bits.
Their input coefficients are the exact integers in §2, not rounded displays.
The table builders use outward Arb ball operations; agreement between the two
precisions is an additional reproducibility check, not a substitute for
outward enclosures.

## 4. Transfer from nine-point frames to zeta zeros

Here we spell out the small change from the cited eight-point/uniform-pressure
formulation. Let y₁<…<yₘ be θ-separated, and let nonnegative symmetric
entries eᵢⱼ satisfy eᵢⱼ≥w(yᵢ−yⱼ)−ε. Sum (6) over the m−8 consecutive
nine-point frames when m≥9. A fixed pair at index separation s receives total
weight at most two, by the capacity constraint in §2. A fixed gap receives
total pressure at most

\[
 B=\sum_rb_r=437542/10^8. \tag{11}
\]

Since the sum of all pair weights in a frame is below16, we obtain

\[
 \sum_{i\ne j}e_{ij}\ge cm-B\operatorname{span}(Y)-8c-16\epsilon m. \tag{12}
\]

Only pairs of index distance at most8 are needed on the left. When m<9,
the right side is nonpositive, so the same bound is trivial. There are no
storage functions or omitted boundary charges in this argument.

For the normalized smoothed Gram matrix Uε from the cited certificate
principle, the majorant gives Uε,SS≤(Λ/mε)I on a θ-separated subset S.
Here mε→1, so Λ/mε<2 for sufficiently small ε. It is not necessary or
correct to replace this normalized bound by Λ for every ε.

Here the clipped-square function is φ₂(t)=t²−(t−2)₊² for t≥0.
Choose a maximal family of disjoint pairs at distance below θ. The unpaired
points are θ-separated. Pinching for the clipped-square function at level2
reduces the matrix to those pairs and the separated block. On the separated
block it is the ordinary square, and (12) applies. On a pair, the eigenvalues
are 1±u≤2 and its square trace is2+2u²; (10) gives at least2+2c−O(η),
where η is the uniform kernel perturbation. Thus the whole matrix satisfies

\[
 \operatorname{tr}\varphi_2(U_\varepsilon)-n
 \ge cn-B\operatorname{span}(Y)-8c-o_\varepsilon(1)n. \tag{13}
\]

This is precisely a critical-line certificate with parameters(c,B).
For clarity, the analytic input of that principle is the unconditional
trace-energy inequality

\[
 (C(f_\varepsilon)+o(1))N\ge
 2(N-n)+\operatorname{tr}\varphi_2(U_\varepsilon),
 \qquad n=N_0^s,\quad \operatorname{span}(Y)\le N+o(N).
\]

Combining it with (13), then taking height to infinity and ε to zero, gives
(1−c) liminf N₀ˢ/N≥2−C(f)−B. Equations (8),(11) yield (1).
The analytic input being used is the cited rank/energy certificate theorem,
not the cited paper's computer-search assertion. Our separate proof of(6)
replaces that numerical assertion for the new data.

## 5. Rigorous scalar enclosures

Let h=16384, S=2⁵⁰, and Δ=2²⁸. The scalar table has 2²⁰ entries,
covering every closed cell[k/h,(k+1)/h] in[0,64]. Its kth uint32 entry is a
lower bound for Δw on that whole cell. A second table stores four signed
integers per cell:

1. a lower bound aₖ≤S w(mₖ);
2. derivative bounds bₖ≤S w′(mₖ)≤cₖ;
3. a whole-cell curvature lower bound dₖ≤S w″;

where mₖ=(2k+1)/(2h). The global third-derivative bound after(3) supplies
the curvature enclosure. A separate all-cell certificate verifies that

\[
 d_k+\lceil249S/h\rceil+2 \tag{14}
\]

is a whole-cell curvature upper bound. This verification explicitly includes
the midpoint enclosure width; it is not inferred merely from dₖ being a
lower bound.

For any chosen integer slope s, Taylor's inequality implies the affine lower
bound for w(t)−st/S on the kth closed cell with intercept, after multiplying
by8h²S,

\[
 8h^2a_k-4hs(2k+1)-4h\max(c_k-s,s-b_k)+\min(0,d_k). \tag{15}
\]

A segment-tree lower hull computes the minimum of(15) on a requested union
of whole cells, exactly. Its two points per cell are the two linear branches
of the maximum in(15). Duplicate abscissae retain the smaller ordinate;
ordinary exact cross products construct the lower hull. Therefore a queried
support is valid for every real point of the entire requested range, not only
for grid points or for the suggested anchor.

## 6. Domain coverage and exact cell rules

### 6.1 Infinite domain and the fresh precover

Outside Pᵣgᵣ<867000 for every r, pressure alone proves(6). More generally,
Σgᵣ≥867000/minP implies(6). The search therefore retains the outward grid
span bound ceil(867000h/27009)=525934, well inside the scalar-table range.

Write Eᵣ(g)=Pᵣg+Wᵣ,ᵣ₊₁w(g). The program computes a rigorous lower bound
for each Eᵣ on its entire pressure-unpaid coordinate interval. Since
10⁸F≥ΣEᵣ, a coordinate cell is discarded only if its lower bound plus all
other coordinate minima already reaches867000. The remaining closed runs
are computed from the **new** kernel. Their Cartesian product is a full
precover of every still-unpaid point.

### 6.2 Reused geometry is untrusted input

A partition decoded from the public attempt-024 bit data is used solely as
geometric guidance. An independent Python verifier checks that its48 roots
are exactly the Cartesian product of the listed coordinate intervals. The
C++ verifier checks, with exact doubled-grid integer endpoints, that every
run in the freshly computed precover is contained in those coordinate unions.
No old COV=true assertion or old kernel bound is imported.

Every internal node splits a distance yⱼ−yᵢ into≤q and≥q. Both children
are retained. Their union covers the parent, including the common boundary.
Difference-bound closure only adds implications of existing inequalities.
The independently replayed tree has10,702 splits and10,750 leaves. All leaves,
including410 previously symmetry-labelled leaves, are treated as unpaid.
All eight former checkpoint subtrees are expanded; none is accepted by its
old proof label. Rounding each directed upper bound d to ceil(d/2) converts
source grid32768 to our grid16384 outwardly, for both signs.

### 6.3 Difference-bound cells and conservative contractions

A cell stores Dᵢⱼ with yⱼ−yᵢ≤Dᵢⱼ/h. Its closure is checked. Tightening
one edge a→b to v gives
D′ᵢⱼ=min(Dᵢⱼ,Dᵢₐ+v+Dᵦⱼ); a negative cycle certifies emptiness.
All gaps remain nonnegative. Reflection reduction is used only after verifying
reflection symmetry of the exact P and W arrays.

Pressure contractions discard only points already reaching the target.
For a pair-collar contraction, the program fixes the old total lower bound,
subtracts exactly that pair's old contribution, and searches the scalar RMQ
for the first and last cells that could still be unpaid. It keeps their
entire closed hull. After contractions the cell is requeued and all bounds
are recomputed. No omitted disconnected region is presumed favourable.

### 6.4 Affine and transportation acceptance

A sum of certified pair supports and pressure is an affine function of the
gaps. It can be minimized over their coordinate box, or over the tighter
closed difference-bound cell. For the latter, write its linear part b·y,
with Σbᵢ=0. Any nonnegative flow fᵢⱼ with outgoing-minus-incoming balance b
proves

\[
 b\cdot y=\sum f_{ij}(y_i-y_j)\ge-\sum f_{ij}D_{ij}/h. \tag{16}
\]

The program explicitly checks nonnegativity, every node balance, and the
recomputed cost of the proposed flow. Optimality is unnecessary.
Imported old anchor positions and convex weights only propose slopes s in
(15). Every actual intercept is recalculated over the full current interval
with the new table, and(16) is verified afresh. Old tangent-validity ranges,
old positive assertions and old numerical certificates are not premises.

### 6.5 Full-matrix convexity acceptance

For pair(i,j), let aᵢⱼ be its gap-incidence vector. A certified curvature
lower bound times Wᵢⱼaᵢⱼaᵢⱼᵀ contributes a Hessian lower bound. Flooring
each scalar coefficient is Loewner-safe, even for negative coefficients.
The program constructs their integer sum M for the numerator10⁸F.

At a feasible cell centre it obtains an objective lower bound and outward
componentwise gradient intervals from the midpoint jets and(14). An integer
matrix R is accepted only if exact row diagonal dominance proves
RᵀMR≥dI with d>0. This implies R invertible and M positive definite, and

\[
 \min F_{\rm numerator}\ge F_{\rm centre,lower}
       -\frac{\|R^T\nabla F_{\rm centre}\|^2}{2d}. \tag{17}
\]

The transformed gradient is bounded over its outward interval, and the debit
is rounded upward. The centre is the average of two feasible DBM potentials,
so it is feasible. Floating Cholesky only suggests R; it never authorizes
acceptance without the integer test. If a guard fails, this rule rejects and
the search continues.

### 6.6 Integer safety and termination

All accepted bounds are integer or rational comparisons. The fixed data have
ΣW=1599999984 and ΣP=437542; the slope proposals satisfy |s|≤8S. The total
transport demand is at most 8hS(ΣP+8ΣW)<1.890·10³⁰. Each checked directed
distance has absolute value≤525934, and there are at most 72 flow entries,
so the absolute cost bound is below 7.16·10³⁷<2¹²⁷.

The hull/Taylor arithmetic is below 2¹²⁴ under the table guards. In the
matrix test, |Mᵢⱼ|≤10¹², |Rᵢⱼ|<10⁸ and absolute gradient endpoints≤10⁹
keep transformed-gradient squares below 2¹²⁰ and Gram sums below 2¹⁰⁴.
These bounds concern the pinned data and checker; enlarging data or scales
requires a new analysis. The independent sanitizer replay additionally checks
the executed arithmetic but is not a replacement for these bounds.

An unpaid cell is split into two covering closed children. LIMIT and
UNRESOLVED are nonacceptance outcomes. A PASS is emitted only after the full
work stack and its deferred initial-sweep stack are empty.

## 7. Completed run and reproducibility

The frozen source is `check_am9_expanded_anchors.cpp`, SHA256
`19f8d5fa97135fed3564b282a1c1af121bcf711e5c258cccb9a108a00b39d297`.
It was compiled with g++ 14.2.0, using `-O3 -std=c++17`, and invoked as

```
./check_am9_expanded_anchors candidate_am_kernel.u32le candidate_am_jets.i64le 867000
```

The completed run returned exit 0 and

```
PASS reward=867000 denominator=100000000 nodes=5324457
pressure=780 basic=87078 affine=954828 convex=26942
symmetry=959 empty=42462 maxstack=10750 seconds=229.402
```

The full transcript SHA256 is
`ae604378de1b7d87b8f0d1c386c8534057cb162fb0efc5ab74b7a0f26c74a820`.
The portable [source/data manifest](code/PACKAGE_MANIFEST.json) identifies all
shipped mathematical inputs and code. The [verification record](verification/VERIFICATION_RECORD.json)
records the completed replays and generated scientific outputs. In particular:

- scalar table: `97c3b113c7c3be7030406984972794cceb1591e533ee26a541531c2acc9850e5`;
- jet table: `4227017a8bd49a500fa5a420c360308e1b202a019d172451bdf218d1749efb31`;
- expanded geometry: `b34f0477ea5c93941db1f488bb606385a91e9c402aceaf1ddedf0dab314aad70`;
- outward closed cells: `c4ff4ded6568430b0ede46d6308f56b2e04a66f9a8c5f3c8ddc2b6acf1361425`;
- proposed anchors: `1032722f512045bba7cc4691f8d00cc178aa977ff0405033437850fa611e153c`.

An independently compiled ordinary replay returned the identical PASS and
all acceptance counters (255.087 seconds). A separately compiled replay with
`-O2 -fsanitize=undefined,signed-integer-overflow -fno-sanitize-recover=all`
also returned the identical PASS (392.102 seconds), exit 0, with no sanitizer
diagnostic. The full [original](verification/original_replay.log),
[independent](verification/independent_replay.log), and
[sanitizer](verification/sanitizer_replay.log) transcripts are retained.

### Portable reproduction

The [code directory](code/README.md) contains a small source/data package, not
opaque binary tables. From that directory, with Python 3, official
`python-flint==0.9.0` and a C++17 compiler with signed `__int128`, run

```
PYTHON=python3 CXX=g++ bash reproduce.sh
```

The wrapper rejects Python optimization, so certificate assertions cannot be
disabled by `-O` or `PYTHONOPTIMIZE`. It regenerates the complete million-cell
scalar and jet tables, checks every upper-curvature entry, verifies the energy
floor, pair capacities, majorant and close-pair bound, independently replays
the geometric cover, and checks every generated scientific byte hash before
the unlimited exhaustive search. No author program is executed.

The clean input is `certified_window_data.json`, SHA256
`3aec299878696245945760411329dbcdfd3e49e78c01fbf6bd8b1430f01c78e9`.
Its seven scientific fields exactly equal the data used to generate the
independently replayed tables; stale proposal metadata was removed, as recorded
in [the input identity record](code/SCIENTIFIC_INPUT_IDENTITY.json).
The retained frame constants and mathematical hints are attributed to
attempt-024 in [the provenance notice](code/THIRD_PARTY_NOTICES.md); their
old inequality assertions are never trusted. The new rational window and
its complete acceptance are the new inputs here.

A clean invocation of that frozen wrapper regenerated all inputs and completed
with exit 0. Its exhaustive-search stage again visited 5,324,457 nodes, with
identical acceptance counters, in 254.637 seconds. The complete
[regeneration/replay transcript](verification/portable_reproduction.log) is
retained. The wrapper's optimized-Python rejection was separately tested.
The source/data manifest SHA256 is
`6fc112f2096192895e686737432afd5febbde4d7f4eea3385f42f4140ede5031`.

## 8. What is and is not claimed

The proposition(6) is an all-gap inequality, not a sampled or local-minimum
claim. The nine-point counting extension includes every pair capacity,
pressure debit, smoothing normalization and finite-frame boundary.
The resulting proportion is a small improvement of an existing theorem's
explicit parameters. It does not constitute a new moment theorem, a proof
of RH, a five-percent gain, or a Lean-kernel verification of this new package.
Previously published RH research files are not modified by this result.
