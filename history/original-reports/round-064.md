## Round 64 — the August 2026 rank--trace result is a proportion theorem, not RH

I checked Alpöge--Furman's August 2026 preprint,
*More than two thirds of the zeta zeros are simple and on the critical line*:
https://arxiv.org/abs/2608.13637. Its Theorem A states

\[
 N_0^s(T,2T)\geq\left(\frac23-o(1)\right)N(T,2T),
 \qquad
 N_d(T,2T)\geq\left(\frac56-o(1)\right)N(T,2T).
\tag{64.1}
\]

The proof uses a finite compression of Weil's Hermitian form. The zero-side
matrix is split into positive rank-one contributions from simple on-line zeros
and signature-\((1,1)\) blocks from off-line pairs; a rank--trace inequality
then gives the lower bound. This is a legitimate strengthening of the
positive-density input in Round 63, in particular
\[
 \#\{\gamma\in\Gamma_C^*:|\gamma|\leq T\}\gg T\log T.
\tag{64.2}
\]

It does not close RH. The paper itself states that its theorems are lower
bounds only: the remaining third of the zeros is not shown to be off the line,
and the inputs are insensitive to \(o(N)\) off-line zeros. The finite
rank--trace certificate therefore controls an aggregate proportion, not the
sign of the full Weil form on every compactly supported test function and not
the exact Bombieri range relation (61.3). Its advertised ceiling for this
bandwidth-one class is also strictly below \(100\%\).

Thus (64.1) may replace the older \(0.4058\) constant when proving density of
critical exponentials, but it supplies no lower bound for the distance from
\(\operatorname{Ran}A_I\), no coercivity of the zero-collapse branch, and no
all-zero positivity theorem.

**Established:** the new result, as stated in its source, is an unconditional
positive-proportion theorem and explicitly does not claim RH; it strengthens
the density fact used in (63.2).

**Failure / error:** promoting (64.1) to “all zeros are on the line,” or
reading the finite rank--trace certificate as global Weil positivity, would
discard the off-line signature blocks and is not a valid inference.

**Unknown / next verification:** an exact weighted-range membership or
coercivity theorem beyond finite aggregate rank--trace information.

**RH status:** no unconditional proof has been produced.
