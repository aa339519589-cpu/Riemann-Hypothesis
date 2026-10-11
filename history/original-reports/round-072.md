## Round 72 — the updated semilocal Weil-positivity manuscript assumes its Hilbert norm

I audited version 5 of Simon Vélez's [*A proof of the Riemann
Hypothesis*](https://zenodo.org/records/21184595), including the [uploaded
PDF](https://zenodo.org/records/21184595/files/paper.pdf?download=1). The
support calculation in Section 5 is valid but does not establish the
positivity claim in Section 6.

### I. Support exhaustion is only an identity of forms

For \(F,G\) with \(\operatorname{supp}C_{F,G}\subset[-R,R]\), the elementary
observation
\[
 k\log p>R\quad\Longrightarrow\quad C_{F,G}(k\log p)=0
\tag{72.1}
\]
does imply that the prime-power part has stabilized once \(X>e^R\). Hence
\[
 q_X(F,G)=\langle L_{\mathrm{arith}},C_{F,G}\rangle
\tag{72.2}
\]
is a correct bookkeeping identity, assuming the displayed definitions of the
archimedean distribution. Equation (72.2) says nothing about the sign of
the form.

### II. The asserted Gram representation is not proved

The load-bearing Proposition 6.1 introduces
\[
 H_X=L^2(C_X,d^\times u)\ominus H_X^{0,1},
\qquad
 \Phi_X(F)=U_X(g_F)\eta_X,
\tag{72.3}
\]
where \(\eta_X\) is described as a “cutoff-renormalized completed vacuum
vector” obtained from a local basic vector by infrared/ultraviolet cutoff
and pole projection. The manuscript gives no explicit formula for
\(\eta_X\), no proof that the renormalized limit exists in \(H_X\), no norm
or domain statement, and no calculation showing that its pole projection
has the asserted global archimedean normalization.

The proposition then simply states
\[
 \langle\Phi_X(F),\Phi_X(G)\rangle_{H_X}
 =
 P_{\mathrm{pole}}(h_{F,G})-W_\infty(h_{F,G})
 -2\sum_{pk\le X}\log p\,p^{-k/2}C_{F,G}(k\log p)
 =q_X(F,G).
\tag{72.4}
\]
But (72.4) is exactly the missing positive Gram representation. A trace
formula supplies an equality for a regularized trace or distribution; it
does not by itself produce a vector \(\eta_X\) whose ordinary Hilbert-space
inner product equals the trace after subtracting pole and archimedean
terms. The conversion from the semilocal trace identity to (72.4) is
asserted in prose and in Appendix D, not derived.

In particular, the paper must prove all of the following before (72.4) is
available:

\[
 \eta_X\in H_X,\qquad
 F\longmapsto U_X(g_F)\eta_X\ \text{is defined on the full test class},
\qquad
 \text{the pole projection and cutoff limits preserve the stated pairing}.
\tag{72.5}
\]

None of these statements follows from the support condition (72.1).

### III. The alleged conclusion is the Weil positivity theorem itself

Combining (72.2) with (72.4) gives
\[
 Q_{\mathrm{arith}}(F)
 =\lVert\Phi_X(F)\rVert_{H_X}^2\ge0
\tag{72.6}
\]
for every compactly supported test function. By the Weil criterion, (72.6)
is already equivalent to RH. Thus the unproved step from the semilocal trace
formula to the ordinary Hilbert norm is not an auxiliary technical detail;
it is the complete RH-bearing assertion.

The appendix's quoted trace expansion does not close this gap. It does not
construct the completed vacuum vector, prove the sesquilinear equality for
all \(F,G\), or show that the regularized archimedean/pole subtraction is a
positive coefficient-space pairing. “Exact stabilization” of prime samples
cannot turn an indefinite or merely distributional expression into a norm.

**Established:** the finite-support condition makes the prime-power sum
stable under a sufficiently large cutoff.

**Failure / error:** the paper assumes, rather than derives, the Hilbert
space Gram identity (72.4); the undefined \(\eta_X\) and its
renormalization are exactly where positivity is being inserted.

**Remaining load-bearing statement:** construct \(\eta_X\) as an actual
element of a specified Hilbert space and prove (72.4) from the semilocal
trace formula with all pole, archimedean, and cutoff limits controlled.
Without that theorem, the Weil quadratic form has not been shown
non-negative.

**RH status:** no unconditional proof has been produced.
