## Round 62 — the matching \(\zeta'\) negative-moment results do not supply an unconditional closure

I checked the results most directly matched to the remaining weighted
range/derivative estimate. Heap--Li--Zhao define

\[
 J_{-k}(T)=\sum_{0\leq\gamma\leq T}
 \frac{1}{|\zeta'(\rho)|^{2k}},
\tag{62.1}
\]

but their main theorem explicitly assumes RH and simplicity of all zeros. Their
unconditional propositions concern auxiliary twisted moment sums; the passage
from those propositions to (62.1) uses RH to identify the relevant conjugate
factors. See the paper's theorem and hypotheses:
https://arxiv.org/abs/2003.09368.

The later Bui--Florea--Milinovich paper states at the outset that its negative
discrete-moment bounds are conditional. Its first main theorem assumes RH and
averages only over a separated subfamily of zeros; its full-family discussion
requires the Weak Mertens Conjecture, which itself implies RH and simplicity.
The paper also records that no upper bounds were known there for the full
negative moments \(J_{-k}(T)\) with \(k>0\):
https://arxiv.org/abs/2310.03949.

This matters in two independent ways. First, a theorem conditional on RH
cannot be used to establish RH. Second, even an unconditional bound on a
subfamily of critical-line zeros would not by itself exclude Bombieri's
critical-only local range relation (61.3), because that relation includes a
finite off-critical packet and requires a lower bound on the distance to the
entire weighted synthesis range, not merely control of individual
\(\zeta'(\rho)^{-1}\) values.

**Established:** the located \(\zeta'\) negative-moment literature provides
useful conditional or restricted-family estimates, while the auxiliary
twisted moments in Heap--Li--Zhao are unconditional.

**Failure / error:** substituting those results for Bombieri's range-distance
estimate either imports RH/simplicity or drops the exceptional and boundary
components of the actual null relation.

**Unknown / next verification:** a source-specific unconditional coercivity or
range-distance theorem for the selected Bombieri branch; this remains the
load-bearing target.

**RH status:** no unconditional proof has been produced.
