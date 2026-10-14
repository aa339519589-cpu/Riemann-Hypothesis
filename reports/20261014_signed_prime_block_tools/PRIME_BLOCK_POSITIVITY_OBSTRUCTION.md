# A positive Gamma payment cannot be split into summable prime blocks

This proves a structural obstruction to a prime-by-prime Gamma payment,
including blocks with all powers of each individual prime and the full
Gamma form. It does not prove or disprove the coefficient-one comparison.

## 1. Allowed blocks and the claimed impossibility

Use the exact forms and theta jets in the companion notes. Write
`P_F,n` and `N_n` for the actual individual prime-power forms, with
`alpha_n=Lambda(n)/sqrt(n)`. Consider a finite or countable collection

\[
 B_b=c_bP_\Gamma+d_bP_{\rm pole}
       +\sum_{n\ge2}\lambda_{b,n}(P_{F,n}-N_n),
\tag{1}
\]

with nonnegative coefficients satisfying

\[
 \sum_bc_b=\sum_bd_b=1,\qquad
 \sum_b\lambda_{b,n}=1\quad(\Lambda(n)>0).
\tag{2}
\]

Assume each block has summable arithmetic strength,

\[
 \sum_{n\ge2}\lambda_{b,n}\alpha_n<\infty.
\tag{3}
\]

Finite sets of primes, each retaining all its powers, satisfy (3).
The decomposition (1)--(2) is exact on the core, with all separated
positive energies summable, since their total is `P+N`.

**Theorem.** It is impossible that every `B_b` is nonnegative on the
whole actual compact ratio core.

Thus one cannot allocate fixed nonnegative portions of Gamma and pole
energy to individual primes (or summable arithmetic blocks), prove each
block nonnegative, and then sum the inequalities to obtain `P>=N`.
A genuinely nonlocal positive mechanism must retain nonsummable complete
arithmetic interaction inside any nonzero block of this specified type,
or use additional cross-block terms outside (1).

## 2. Neutrality would force every block to annihilate all theta jets

Suppose all blocks are nonnegative. For each neutral ratio
`r_j=f_j/psi`, the two-energy cutoffs converge and

\[
 0\le B_b[\chi_Rr_j]\le A[\chi_Rr_j]\longrightarrow0.
\]

The form `B_b` is continuous for `E=P+N`, because all its coefficients
are at most one. Its limiting value is therefore `B_b[r_j]=0`.
Cauchy--Schwarz for the nonnegative form, first on cutoff cores and then
by E-continuity, gives

\[
 B_b(r_j,r)=0
\tag{4}
\]

for every compact ratio `r`. This step needs the actual simultaneous
neutral identities and does not replace them by independent
per-prime null identities.

## 3. A summable block has an L2 source row, apart from its fixed pole

Put `g=psi r` and use full-line odd source functions. For every compact
smooth odd source `h`, expansion of (1) has the form

\[
 B_b[g/\psi,h/\psi]
   =\langle g,L_bh\rangle_{L^2(\mathbb R)}
      -2d_b\,\overline{\ell(g)}\ell(h),
 \qquad \ell(g)=\int_{\mathbb R}\sinh(x/2)g(x)\,dx,
\tag{5}
\]

where

\[
 L_bh=c_b\,b(D)h
 -\sum_{n\ge2}\lambda_{b,n}\alpha_n
       [h(\cdot+\log n)+h(\cdot-\log n)]
 +V_bh.
\tag{6}
\]

Here `V_b` is the local diagonal produced by the source ground transform.
For normalization transparency, on `x>0` it is exactly

\[
 V_b(x)=-c_b\frac{b(D)\psi(x)}{\psi(x)}
 +\sum_{n\ge2}\lambda_{b,n}\alpha_n
       \frac{\psi(x+\log n)+\psi(x-\log n)}{\psi(x)}
 +d_b\frac{\sinh(x/2)}{2\psi(x)},
\]

with the odd full-line `psi` used in the translated numerator and the
result evenly extended. In particular it is locally bounded and real. To verify this assertion directly, the Gamma square
expands into the original full odd Gamma source form plus the local
multiplier `-b(D)psi/psi`; the signed prime square pair expands into its
two actual source translations plus its local ground-state diagonal;
and the pole square is exactly its local multiplier minus
`2|ell(g)|^2`. Every numerator in the local diagonals is odd and smooth
at zero, and `psi` has a simple zero, so these quotients extend smoothly
there. For the arithmetic sum, (3) and the uniform bounds on each fixed
theta derivative imply local uniform convergence, including at zero.

For compact smooth `h`, the first term of (6) belongs to L2 because the
Gamma symbol has logarithmic growth. The translation sum is bounded in
L2 by `2 sum_n lambda_(b,n) alpha_n`, by (3). Finally `V_bh` is L2 by
compact support and local boundedness. Thus

\[
                         L_bh\in L^2_{\rm odd}(\mathbb R).
\tag{7}
\]

Formula (5) extends from compact `g` to a fixed theta jet by its
L2 convergence and pole-moment convergence under cutoffs. Equivalently,
one may first pair (6) with the theta jet, whose complete theta tails
justify each term. No unbounded full-prime source operator is inserted:
(7) holds specifically because the block satisfies (3).

## 4. Ordinary L2 density forces every proposed positive block to vanish

The neutral source jets have `ell(f_j)=0` and span a dense subspace of
ordinary odd L2. Here is the needed completeness proof, independent of
any RH hypothesis. Write `f_j=f_0^(2j)`, with
`f_0=Phi'''-Phi'/4`. If an odd L2 function `h` annihilates every
`f_j`, then

\[
 H(z)=\int_{\mathbb R}\overline{h(x)}f_0(x+z)\,dx
\]

is holomorphic on `|Im z|<pi/4`, by the uniform theta L2 bounds on
smaller strips. Oddness of both functions makes `H` even. Its even
Taylor coefficients at zero vanish by the assumed annihilation, so
`H=0` throughout the strip. On the real axis, Fourier transformation
then gives the product of the reflected-conjugate Fourier transform of
`h` with

\[
 \widehat f_0(t)=it(t^2+1/4)\Xi(t)
\]

as zero almost everywhere. This multiplier is nonzero almost everywhere,
since Xi is a nonzero entire function. Plancherel therefore gives `h=0`.
The theta holomorphy and two-sided uniform tail bounds used here are in
`../20261013_reflected_prime_energy/REPORT.md`, Section 6. Combining
(4)--(7), for every compact odd `h` one gets

\[
 \langle f_j,L_bh\rangle=0\quad(j\ge0),\qquad L_bh=0.
\]

Therefore the supposedly nonnegative block satisfies on the entire core

\[
 B_b[g/\psi]=-2d_b|\ell(g)|^2.
\tag{8}
\]

Since `d_b>=0` and compact odd sources with nonzero `ell(g)` exist,
nonnegativity forces `d_b=0`; then `B_b=0`. Applying this to every block
contradicts `sum_b d_b=1` already, and also contradicts the nonzero full
form `A=sum_b B_b`.

The argument does not rely on compactly supported square functionals:
each proposed block was allowed to contain the full nonlocal Gamma form
and infinitely many prime powers. The missing ingredient is simultaneous
nonsummable arithmetic strength, or a comparably global cross-block
construction, not just retaining every power of one prime.
