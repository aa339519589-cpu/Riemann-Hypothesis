## Round 95 — the Nicolas-criterion descent has the wrong error logic

I checked the newer two-page preprint [*Nicolas Criterion and Riemann Hypothesis*](https://zenodo.org/records/20790544), whose displayed criterion is

\[
 R(n):=\frac n{\varphi(n)}
 <e^\gamma\log\log n+\frac{e^\gamma(2+\beta)}{\sqrt{\log n}}.
\tag{95.1}
\]

The proposed proof tries to descend a violation at \(N_k\) to \(N_m\), \(m=\lfloor k/2\rfloor\), using
\[
 R(N_m)=R(N_k)\prod_{m<i\le k}\left(1-\frac1{P_i}\right).
\tag{95.2}
\]
After factoring out the main term, the relevant normalized correction is
\[
 a_j=\frac{2+\beta}{\sqrt{\log N_j}\,\log\log N_j}.
\tag{95.3}
\]
The manuscript's Lemma 4 asserts
\[
 (1+a_k)\bigl(1+O(e^{-c\sqrt{\log P_k}})\bigr)>1+a_m.
\tag{95.4}
\]
This does not follow. The prime-number theorem gives \(\log N_j\sim P_j\) and \(P_m/P_k\to\tfrac12\), hence
\[
 \frac{a_m}{a_k}\longrightarrow\sqrt2>1.
\tag{95.5}
\]
Thus the unperturbed left side is smaller than the required right side. Moreover,
\[
 a_m-a_k\asymp \frac1{\sqrt{P_k}\log P_k},
 \qquad
 \frac{e^{-c\sqrt{\log P_k}}}{a_m-a_k}\longrightarrow\infty.
\tag{95.6}
\]
The displayed \(O\)-term is therefore too coarse and, crucially, has no sign. An estimate \(E_k=O(e^{-c\sqrt{\log P_k}})\) permits both positive and negative \(E_k\); it cannot be used to deduce the positive lower bound required by (95.4). The manuscript's sentence that the error scale is “asymptotically more” than the gap reverses the logical requirement: an upper bound on an unsigned error is not a positive correction. Consequently the descent \(R(N_k)>\text{threshold}\Rightarrow R(N_m)>\text{threshold}\) is unproved, so the final induction contradiction does not exist.

This is a direct failure in the proposed proof, not a resolution of the underlying Nicolas equivalence. The preprint supplies no independent estimate that fixes the sign or gives a sufficiently sharp lower bound for the Mertens-product error. Therefore it does not close the arithmetic route to RH.

**Established:** the proposed descent step is invalid at the scale and sign of its own error term.

**Route decision:** discard this candidate as an RH proof; retain the Bombieri weighted-range problem as the active route.

**RH status:** no unconditional proof has been produced.
