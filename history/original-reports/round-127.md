## Round 127 — fixed-window Weil positivity is a finite certificate, not a global closure

I audited the recent paper *Weil positivity in compact windows: certified
two-sided bounds and a Landau--Widom decay law*,
[arXiv:2608.24827](https://arxiv.org/abs/2608.24827).  Its object is the
compact-support Rayleigh quotient

\[
 \lambda^*(L)=\inf_{\substack{0\ne f\in L^2([-L,L])}}
 \frac{Q(f)}{\|f\|_2^2},
\tag{127.1}
\]

where \(Q\) is the Weil quadratic form.  The paper gives an unconditional
numerical certificate at the fixed window \(L=0.8\):

\[
 Q(f)\ge 8.9\times10^{-18}\|f\|_2^2
 \quad\text{for }\operatorname{supp}f\subset[-0.8,0.8],
\tag{127.2}
\]

and separately certifies positivity in the odd sector, together with a
simple even ground state.  This is a meaningful finite-window result, but
(127.2) is only one value of the function \(L\mapsto\lambda^*(L)\).  The
global Weil criterion requires positivity for every compact support, hence
for all \(L>0\); no implication from the single window \(L=0.8\) to
arbitrary \(L\) is proved.

The lower certificate reduces the geometric-side multiplier to

\[
 \Psi_L(t)=\Re\psi\!\left(\tfrac14+\tfrac{it}{2}\right)-\log\pi
 -\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n),
\tag{127.3}
\]

and combines a pointwise high-frequency envelope with a finite Legendre
matrix.  The high-frequency threshold is bounded by a quantity of the form

\[
 T_1(L)=2\pi e^{A_L},\qquad A_L\asymp 4e^L,
\tag{127.4}
\]

so the finite computation is an effective certificate for fixed \(L\), not a
uniform all-\(L\) estimate.  As \(L\) grows, both the prime support in
(127.3) and the required finite-dimensional budget grow; the argument does
not provide a common positive lower bound or a form-core theorem covering
the full Weil form.

The paper's Landau--Widom law is fitted to computed upper bounds.  Those
upper bounds, even if numerically extremely small at larger \(L\), cannot
replace a lower positivity estimate.  The conditional large-\(L\) estimate
under RH likewise cannot be used in an unconditional proof.  The paper also
explicitly leaves the separate Connes spectral step--proving the required
operator/form convergence and the resulting zero correspondence--untouched.

**Established:** an unconditional positive lower bound on one compact
window is a valid finite Weil certificate and can be independently checked;
it does not extend by itself to complete Weil positivity, to all compact
supports, or to the Section-11 selected-eigenvector branch.

**Remaining load-bearing statement:** obtain a uniform all-\(L\) lower bound
or an equivalent complete Weil-positivity theorem, and separately close the
spectral correspondence and finite/infinite Section-11 branches.

**RH status:** no unconditional proof has been produced.

## Ledger erratum — placement of Round 117

Round 117 was inserted after an earlier generic `RH status` anchor rather than
at the physical end of the append-only file.  Its text is unchanged and its
mathematical scope is unchanged.  For chronological reading, treat Round 117
as following Round 116; no earlier round is overwritten or reinterpreted by
this placement error.

## Ledger erratum — placement of Round 127

Round 127 was also inserted at the first matching section anchor rather than
at the physical end of this append-only file.  Its text is unchanged.  For
chronological reading, treat it as the continuation after Round 126; this
erratum is the authoritative end-of-file anchor for that round.
