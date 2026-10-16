# Attribution and changes for imported mathematical hints

The fixed frame weights/pressures and the partition/anchor hints originate in
attempt-024, pinned at commit 9e6ca6615b9dbfec4a1d722995cff0ffe3abf9bb:
https://github.com/josusanmartin/riemann/blob/9e6ca6615b9dbfec4a1d722995cff0ffe3abf9bb/submissions/attempt-024/proof/Solution.lean

The inspected source SHA256 is
637d8197291a39ec2d9c7529642ac1df9731ceea706882a1c2e0b4391642d0ac.
The source attribution/change notice is retained verbatim below. Its historical
bounds and descriptions concern that upstream source, not our new certificate.

Changes made on 16 October 2026: mathematical partition bit data were decoded
into explicit closed binary-tree splits and leaf slope proposals, with all eight
checkpoint subtrees expanded. The data were compressed in a deterministic gzip
file. No upstream executable or acceptance decision is used. The new rational
window, table construction, geometric coverage replay, and exact inequality
verifier are independently supplied. Every imported leaf is unpaid until our
checker proves its new-window inequality. Original frame weights and pressures
are retained. Apache-2.0 text is supplied in LICENSE-APACHE-2.0.txt for the
upstream-derived material.

## Upstream notice

```text
/-
R. Arun Chandru
arun.chandru@gmail.com
https://github.com/arun-chandru
https://x.com/arunchandru
https://researchgate.net/profile/R_Chandru

Copyright (c) 2026 R. Arun Chandru, for the circle-enclosure refinement.
SPDX-License-Identifier: Apache-2.0

Critical-line proportion: 167031227639218487/247987190000000000.

-/
/-
R. Arun Chandru
arun.chandru@gmail.com
https://github.com/arun-chandru
https://x.com/arunchandru
https://researchgate.net/profile/R_Chandru
-/
/-
Copyright (c) 2026 R. Arun Chandru, for original contributions.
SPDX-License-Identifier: Apache-2.0
-/
/-
Copyright (c) 2026 Samuel Lavery (github: samlavery). Licensed under Apache-2.0. Built on the author's
riemannzeta.fun submissions attempt-012/013/014/015/016 and on R. Arun Chandru's "master-of-puppets"
and "master-of-puppets2".
NOTICE: reuse or adaptation of this file must retain this copyright and attribution notice
(Apache-2.0 §4(c)) and must state any changes made (§4(b)).
The internal modules are by Samuel Lavery's agent team (bridge-port, am-cert, mvt-engine, window-scope).
-/
/-
Changes (Apache-2.0 §4(b)), by Samuel Lavery's agent team, 2026-10-10. This file is derived from
R. Arun Chandru's riemannzeta.fun submission "master-of-puppets" (2026-10-09, κ = 66812491/99194876,
Apache-2.0; Solution.lean sha256 f7ef331e72e8c34804e196a4cc0c6fdd69bb1c6947a51dfbf60b88a6343aad9d).
* Dead declarations removed: every declaration outside the dependency closure of the three scored
  theorems, computed from the compiled olean (attributed lemmas kept). Non-notice comments removed.
  Every copyright, license and attribution notice is retained verbatim.
* Certificate replaced by a re-optimised 9-point certificate (2026-10-14: weights lp9, see the last bullet; earlier versions of
  this file used the t570 weights).
* Counting chain generalised to n-point certificates (OpethN, same proofs with band width n − 1:
  error 4(n − 1)δ per point, boundary (n − 1)c, δ ≤ c/(8(n − 1)), C = 4(n − 1) + 2 + c + B, and a
  parametrised copy of Kristian Muri Knausgard's card_near_le); Arun's eight-point instances replaced.
* Window bound taken from R. Arun Chandru's "master-of-puppets2" (2026-10-11, κ = 167031227639218487/247987190000000000,
  Apache-2.0; Solution.lean sha256 a99b3172fe7885abb4119b1b00d124545e2689e1f441d571b1470439d6c3b03c): its circle-enclosure
  `cos_theta0_le` / `sin_theta0_ge`, giving H_W ≥ 672168410556873948/10¹⁸; changes 2026-10-11.
* Window bound: the order-20 cos θ₀ enclosure from R. Arun Chandru's master-of-puppets3 and the terminal HW floor at
  denominator 10²⁴ from Yuhang Shi's shi-anchor-variance-refinement-2026, both taken via R. Arun Chandru's master-of-puppets4
  (2026-10-12, Apache-2.0, sha256 ba9bf43cce4421a7580b03bfb90453b9f34381296943b38f3dc1f4c2a89a9de0), whose block notice is kept
  verbatim: HW_ge 672168410564118872522651/10²⁴; changes 2026-10-13.
* Changes 2026-10-14/15, by Samuel Lavery's agent team:
  - 9-point weights lp9, the frame-optimum separation LP (window-scope), certified on a composite tree sized at δ = 1.65e-5
    (root 36 at δ = 1.8e-5): 48 roots (RCUT 1:51168,1:39936) and 8 walk cuts at 450 leaves, 10,750 leaves (am-cert,
    bridge-port); B = 437542/10⁸;
  - Y walk codes (ranked kind flags and an escape-coded 6-bit tangent-position table) and the DCOV decoder-elimination leaf proof
    (am-cert);
  - the range-end anchor: position code 34 reads the term range's end U (module PCellDKH, am-cert);
  - Yuhang Shi's anchor-variance term (shi-anchor-variance-refinement-2026) ported to the 9-point checker with a per-cell
    curvature table as module PCellVarW (am-cert), applied to 38 leaves; PCellVarW's notice is kept verbatim;
  - certificate thinning (am-cert): per leaf, minorant terms downgraded and multipliers dropped while the leaf still certifies
    the floor below;
  - exact floor closure: c = 72086209857930095324931/8388608000000000000000000, the largest floor every leaf certifies (scale
    2²³·10¹⁸; am-cert);
  - the H_W enclosure closed to 10⁻³² with an own bound π < 3141592653589793238462643383280/10³⁰ (the lead's block, placed before
    the master-of-puppets3/4 block notice, which is kept verbatim): HW_ge 67216841056411887477599838142972/10³².
  The matching/pinching chain is unchanged, so κ = (H_W⁻ − B)/(1 − c)
  = 34191001116882886388531117129201664/50760020691785094633026544189453125 = 0.67358130771.
-/
```
