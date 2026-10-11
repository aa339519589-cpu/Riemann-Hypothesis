## Round 111 — zeta Fourier interpolation does not supply the fixed-interval weighted dual

I audited Bondarenko--Radchenko--Seip, *Fourier Interpolation with Zeros of
Zeta and \(L\)-Functions* ([published version](https://link.springer.com/article/10.1007/s00365-022-09599-w),
[arXiv version](https://arxiv.org/abs/2005.02996)).  It is a valid
interpolation theorem in its stated analytic class, but it cannot be
substituted for the Bombieri inequality (103.6).

Theorem 1.1 represents an even function \(F\) as
\[
F(z)=\sum_{n\ge1}\widehat F\!\left(\frac{\log n}{4\pi}\right)U_n(z)
+\lim_{k\to\infty}\sum_{0<\gamma\le T_k}
\sum_{j<m(\rho)}F^{(j)}\!\left(\frac{\rho-\frac12}{i}\right)V_{\rho,j}(z).
\tag{111.1}
\]
The second sum runs over the full multiset of nontrivial zeros, including
any off-line zeros, and the first sum contains the integer source samples.
The interpolatory identities explicitly assign an independent coordinate to
each zero and to each integer sample.  Removing the off-line coordinates or
discarding the integer term is therefore not a consequence of the theorem.

There is also a direct Paley--Wiener obstruction.  The dual inequality
(103.6) concerns \(G_g(z)=\int_Ig(u)e^{izu}\,du\), an entire function of
finite exponential type determined by the fixed interval \(I\).  If an
interpolation basis function \(V_{\rho,0}\) associated with a hypothetical
off-line zero were of this fixed Paley--Wiener type, its interpolation
properties would make it vanish at every other critical zero.  By the
unconditional positive-proportion count and Jensen's \(O(T)\) zero bound from
Round 109, that would force \(V_{\rho,0}\equiv0\), contradicting
\(V_{\rho,0}((\rho-\frac12)/i)=1\).  Hence these basis functions cannot
themselves be the fixed-interval dual test functions required by (103.6);
their rapid real-axis decay is not a substitute for an exponential-type
bound.

The corollary asserting uniqueness from integer samples additionally assumes
that \(F\) is divisible by \(\zeta(\tfrac12+iz)\), which imposes vanishing at
the entire zero divisor.  A finite off-line exponential packet, or an
arbitrary \(G_g\) from the Bombieri range problem, does not satisfy that
divisibility assumption.  No estimate in the interpolation theorem controls
an off-line evaluation by the weighted critical samples alone.

**Established:** the full-zero/integer interpolation formula and its exact
coordinate structure; the associated basis functions are not fixed-type
Paley--Wiener functions when an off-line zero is present.

**Failure / missing step:** no transfer from (111.1) to a fixed-interval
weighted sampling inequality, and no removal of the integer-source or
off-line coordinates.

**Route decision:** retain the theorem as structural evidence about the
arithmetic duality, but keep (103.6)/(25.2) as the load-bearing target.

**RH status:** no unconditional proof has been produced.
