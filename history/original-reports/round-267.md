## Round 267 — A-result: finite verified spectral data yields a valid pinned upper bound for \(J_q\)

Source checked: Mittermeier, Part 3, Theorem 5.6, together with Chirre and
Helfgott, *Optimal bounds for sums of non-negative arithmetic functions*,
[arXiv:2512.15709](https://arxiv.org/abs/2512.15709), Proposition 9.1.
The finite zero verification used by the construction is the published
Platt--Trudgian verification through
\[
H_*=3{,}000{,}175{,}332{,}800.
\]
For \(10^7\le T\le H_*\) and \(x>\max\{T,10^9\}\), the cited finite-height
theorem at \(\sigma=1/2\) gives the unconditional prefix bound
\[
\Sigma_{1/2}(u):=\sum_{n\le u}\frac{\Lambda(n)}{\sqrt n}
\le U_T(u):=(c_T+e_T)\sqrt u-\alpha+d_T
\qquad(u\ge x),
\]
where
\[
c_T=\frac{\pi}{T}\coth\!\left(\frac{\pi}{2T}\right),
\qquad
e_T=\frac{\pi}{T-1},
\qquad
d_T=\frac1{2\pi}\log^2\!\left(\frac{T}{2\pi}\right)
-\frac1{6\pi}\log\!\left(\frac{T}{2\pi}\right).
\]
The only imported hypothesis is a finite, rigorously verified statement about
zeros up to height \(T\); it is not RH at unbounded height.

Let \(a=\log x\) be a reference prime-power event, \(q=e^s\) a later
current active event, \(Y_a>0\) the exact workload at \(a\), and
\(W_x=\Sigma_{1/2}(x)\). The exact endpoint identity is
\[
W_x=A'(a)+Y_a,
\]
with
\[
A'(a)=4\sinh(a/2)-\alpha+
\operatorname{artanh}(e^{-a/2})+\arctan(e^{-a/2}).
\]
Define \(R_{T,a}(u)=U_T(u)-W_x\). Substitution cancels the common
\(-\alpha\) term and gives
\[
R_{T,a}(u)=(c_T+e_T)\sqrt u+d_T-4\sinh(a/2)
-\operatorname{artanh}(e^{-a/2})-\arctan(e^{-a/2})-Y_a.
\]
For \(x\le u<q\), the actual preterminal cumulative load satisfies both
\[
M_a(\log u)=\Sigma_{1/2}(u)-W_x\le R_{T,a}(u)
\]
and the exact terminal-state front-loading bound
\(M_a(\log u)\le P_q^-\), where \(P_q^-\) is the load strictly before the
current event. Since
\[
J_q=\int_x^q M_a(\log u)\,\frac{du}{u},
\]
pointwise integration gives the unconditional one-sided certificate
\[
J_q\le\widehat J_{T,\mathrm{pin}}
:=\int_x^q\min\{P_q^-,R_{T,a}(u)\}\,\frac{du}{u}.
\]
The loss is exactly
\[
\widehat J_{T,\mathrm{pin}}-J_q
=\int_x^q\bigl(\min\{P_q^-,R_{T,a}(u)\}-M_a(\log u)\bigr)\frac{du}{u}
\ge0.
\]
It is also never larger than either unclipped envelope:
\[
\widehat J_{T,\mathrm{pin}}
\le\min\!\left\{P_q^-\log\frac qx,
\int_x^qR_{T,a}(u)\frac{du}{u}\right\}.
\]
Thus this is a complete unconditional finite-range/sufficient-interface
theorem and is added to the VERIFIED PROOF CHAIN.

### Remaining RH load-bearing claim

The theorem only certifies an active event when the independently computed
upper bound also satisfies
\[
\widehat J_{T,\mathrm{pin}}\le C_q.
\]
No proof shows this for every recovery witness, and the admissible finite
height and entry-range conditions do not remove the universal tail
quantifier. Therefore this interface does not establish
\(V_q=C_q-J_q\ge0\) or RH.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的有限谱单向认证接口，但没有产生新的无条件 RH 证明进展。
