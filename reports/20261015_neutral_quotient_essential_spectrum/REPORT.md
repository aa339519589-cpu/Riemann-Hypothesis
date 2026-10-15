# The full Green operator has essential spectrum [0,1] after removing the known neutral space

Date: 2026-10-15.

## Statement and scope

Use the complete positive forms P and N, their gradient completions K_P
and K_N, and the bounded map

\[
 T:K_P\longrightarrow K_N,\qquad T\nabla_P r=\nabla_N r,
 \qquad C=TT^*.
\]

These are the unchanged objects of the
[full-prime Green construction](../20261013_full_prime_green_reference/REPORT.md).
In particular, every von Mangoldt prime power is retained. Let S_P and
S_N be the closed P- and N-gradient spans of the known theta-neutral ratios

\[
 r_j=\frac{\Phi^{(2j+3)}-\Phi^{(2j+1)}/4}{\psi},\qquad
 \psi=-\Phi',\qquad j\ge0.
\]

The exact neutral identities make these reducing eigenvalue-one spaces
for T* T and C, respectively. No identification with their entire
one-eigenspaces is assumed.

We use the standard complexifications of these real energy spaces for
the oscillatory packets below. This does not change the spectrum of the
original real selfadjoint operators.

**Theorem.** With essential spectrum defined by singular Weyl sequences,

\[
 \boxed{\sigma_{\rm ess}(C)
 =\sigma_{\rm ess}\bigl(C|_{K_N\ominus S_N}\bigr)=[0,1].}       \tag{1}
\]

Thus removing the entire known closed neutral space does not make the
Green operator compact or Schatten-class. This does not determine the
sign of C-I. The previously proved compactness of (C-I)_+ remains intact:
possible spectral points strictly above one are discrete eigenvalues,
and this theorem neither excludes nor produces any such eigenvalue.
There is no RH conclusion.

The proof reuses the complete-prime estimates and source compactness in
[Compactness of the positive excess](../20261013_compact_green_excess/REPORT.md),
and the complete reflected-row asymptotic in
[The reflected renewal law](../20261013_reflected_markov_essential_edges/REPORT.md).
It is not a transfer of the essential-spectrum statement for the reflected
Markov operator alone.

## 1. Exact centered-source forms

On x>0 put

\[
 s(x)=\sinh(x/2),\quad W_0(x)=s(x)/\psi(x),\quad
 L(x)=\sum_{\log n>x}\frac{\Lambda(n)}{\sqrt n}\psi(\log n-x),
 \quad V(x)=L(x)/\psi(x).
\]

For a compact smooth ratio r, choose the pole-centered source

\[
 g=\psi\left(r-8\int_0^\infty\psi(x)s(x)r(x)\,dx\right).
\]

Then int s g=0, and the full positive pole form is

\[
 E_{W_0}[g]=\int W_0|g|^2\le P[r].                         \tag{2}
\]

The centered source extends to K_P. Write g_o for its odd full-line
extension. In the Fourier convention of the cited source identity, let

\[
 b(t)=\Re\psi_{\rm digamma}(1/4+it/2)-\log\pi+C_0\ge0,
 \quad C_0=\gamma+\pi/2+3\log2+\log\pi,
 \quad q_b[g_o]=\langle g_o,b(D)g_o\rangle.
\]

Here b(t)=log|t|+O(1) at infinity and b'(t)=O(1/|t|) there.
For d_n=log n and alpha_n=Lambda(n)/sqrt n, set

\[
 J_n[g]=\int_0^\infty\overline{g(x)}g(x+d_n)\,dx,
 \qquad
 R_n[g]=\int_0^{d_n}\overline{g(x)}g(d_n-x)\,dx.
\]

Expansion of N and the exact polar-inclusive source identity give

\[
 \begin{split}
 N[g]&=2\int V|g|^2-2\sum_n\alpha_n\Re R_n[g],\\
 P[g]&=q_b[g_o]+2\int V|g|^2
          -2C_0\|g\|_2^2-4\sum_n\alpha_n\Re J_n[g].
 \end{split}                                                   \tag{3}
\]

Notation P[g] means the ratio form for the unique pole-centered source,
not an independently enlarged source domain. Equations (3) first hold on
the common core and extend by its actual P completion.

Define the comparison form on this same centered-source space by

\[
 H_0[g]=q_b[g_o]+2\int V|g|^2.                             \tag{4}
\]

It is equivalent to P. Indeed, the published weighted prime bounds and
(2) give H_0<=C P from (3). Conversely,

\[
 E_{W_0}[g]\le\sup_{x>0}\frac{s(x)}{L(x)}\int V|g|^2,
\]

and this supremum is finite: at zero L has a positive limit, and at
infinity the complete row satisfies

\[
 L(x)\sim J e^{x/2},\qquad
 J=\int_0^\infty e^{y/2}\psi(y)\,dy>0.                    \tag{5}
\]

The same prime bounds in (3) now give P<=C H_0. In particular these two
norms have the same weak topology on the completed centered-source
space. Also inf V>0, since V is positive and continuous, tends to infinity
at zero, and tends to infinity at infinity.

All lower-order terms in (3) are compact forms in this topology. For
completeness, set v_0=1/W_0 and

\[
 A_n=\sup_{x>0}\sqrt{v_0(x)v_0(x+d_n)},\qquad
 B_n=\sup_{0<x<d_n}\sqrt{v_0(x)v_0(d_n-x)}.
\]

The complete estimates are

\[
 |J_n[g]|\le A_n E_{W_0}[g],\quad |R_n[g]|\le B_n E_{W_0}[g],
 \quad \sum_n\alpha_n(A_n+B_n)<\infty.                    \tag{6}
\]

Their tails tend to zero in form-operator norm. For a fixed label, the
translation or reflection is bounded in ordinary L2, and the published
centered-source map K_P to L2 is compact. Thus every finite-label pullback
is compact; (6) passes to the full prime sum. The mass term is compact by
the same source map. Consequently

\[
 P-H_0\quad\hbox{and}\quad N-N_0\quad\hbox{are compact forms},
 \qquad N_0[g]=2\int V|g|^2.                              \tag{7}
\]

No separate ordinary-L2 domain for a past-prime operator is asserted.

## 2. Packets with a prescribed spectral ratio

Fix kappa>0 and put lambda=1/(1+kappa). Choose real x_j tending to infinity,
let h_j=exp(-3x_j), v_j=V(x_j), and t_j=exp(kappa v_j). Fix a smooth
compact function phi in (-1,1) with L2 norm one, and set

\[
 f_j(x)=h_j^{-1/2}\phi((x-x_j)/h_j)e^{it_jx}.               \tag{8}
\]

Every f_j/psi is a legal smooth compact ratio. Its source need not be
pole-centered, so replace it by

\[
 g_j=f_j-c_j\psi,\qquad c_j=8\int_0^\infty s(x)f_j(x)\,dx. \tag{9}
\]

This changes neither gradient nor P or N. In fact |c_j|<=C exp(-x_j),
by the width in (8); psi has finite H_0 energy. Thus the H_0 cost of this
centering correction tends to zero.

From (5) and the true theta asymptotic
psi(x)~8pi^3 exp(13x/2-pi exp(2x)),

\[
 V(x)\sim\frac{J}{8\pi^3}\exp(\pi e^{2x}-6x),\qquad
 \epsilon_j:=\sup_{|x-x_j|\le h_j}|V(x)/v_j-1|\longrightarrow0.
                                                               \tag{10}
\]

The uniform assertion follows directly from the asymptotic and
h_j exp(2x_j) tending to zero. It does not differentiate V across its
prime knots.

The odd modulated packet also satisfies the ordinary L2 estimate

\[
 \|b(D)(f_j)_o-\kappa v_j(f_j)_o\|_2=O(1).                \tag{11}
\]

Here is the operator, rather than just symbol, justification. The Fourier
transform is the sum of two reflected Schwartz packets centered at t_j
and -t_j, each of frequency width h_j^{-1}. On
|xi-t_j|<=t_j/2, the mean-value bound for b gives a residual bounded in L2
by C/(t_j h_j). On the complement, the Schwartz tail gives, for each
fixed sufficiently large M, a bound

\[
 C_M(1+\log t_j+|\log h_j|)(t_jh_j)^{-M}.
\]

The same estimate applies to the packet centered at -t_j, since b is even.
Both bounds tend to zero. Finally b(t_j)-kappa v_j=O(1), proving (11).
This also keeps the odd reflected packet in the calculation.

Since q_b is the full odd-line form, (10)-(11) give

\[
 H_0[g_j]=2(1+\kappa)v_j(1+o(1)).                         \tag{12}
\]

The factor two is the odd extension, not a second factor inside b.
Write u_j for the P-gradient represented by

\[
 \widetilde g_j=g_j/[2(1+\kappa)v_j]^{1/2}.                \tag{13}
\]

These vectors tend weakly to zero in the H_0, and hence P, topology. For
example, against the dense centered compact-ratio sources, the potential
pairing tends to zero by spatial escape and Cauchy--Schwarz in L2(V dx).
For the Fourier pairing, move b(D) onto the fixed smooth test, whose odd
source lies in its L2 operator domain, and use
||f_j||_2/sqrt(v_j) tending to zero. The vanishing gauge correction in
(9) causes no change. Density and the bounded H_0 norms complete the
weak-convergence argument.

## 3. The full dual residual

The comparison pencil N_0-lambda H_0 has residual tending to zero on (13)
in the H_0 dual norm. To verify the nontrivial potential part, for an H_0
unit test h use

\[
 \left|\int (V-v_j)f_j\overline h\right|
 \le\left(\int_{\operatorname{supp} f_j}
              \frac{|V-v_j|^2}{V}|f_j|^2\right)^{1/2}
       \left(\int V|h|^2\right)^{1/2}
 \le C\epsilon_j\sqrt{v_j}.                              \tag{14}
\]

After (13), this is O(epsilon_j), even though its ordinary L2 residual
need not be small. The Fourier part is O(v_j^{-1/2}) in ordinary L2 by
(11), hence also in H_0 dual since inf V>0. The scalar leading terms
cancel exactly because 1-lambda=lambda kappa. The gauge term is negligible
by (9). Thus

\[
 \|(N_0-\lambda H_0)u_j\|_{H_0^*}\longrightarrow0.        \tag{15}
\]

Equivalence of norms and (7), applied to the weakly zero sequence, now
retain every complete prime and mass term and give

\[
 \|(N-\lambda P)u_j\|_{P^*}\longrightarrow0,\qquad
 \|u_j\|_P\longrightarrow1.                              \tag{16}
\]

Indeed P-H_0 is compact, so (12)-(13) also give the second conclusion.
Normalizing once more makes these unit vectors without affecting (16).
If Lambda=T* T, (16) is exactly

\[
 \|(\Lambda-\lambda)u_j\|_P\longrightarrow0,
 \qquad u_j\rightharpoonup0.                              \tag{17}
\]

This is a singular Weyl sequence for the original complete operator.

## 4. Removing the neutral space and passing to reflected edges

Let Pi_P be the orthogonal projection onto S_P. Since Lambda=I there,

\[
 (1-\lambda)\|\Pi_Pu_j\|_P
 \le\|(\Lambda-\lambda)u_j\|_P\longrightarrow0.           \tag{18}
\]

Hence replacing u_j by its neutral-orthogonal projection preserves (17)
and its limiting unit norm. No estimate for a finite set of theta jets
is being substituted for the projection onto their entire closed span.

Set z_j=T u_j/sqrt(lambda). Then

\[
 \|z_j\|_N\longrightarrow1,\quad z_j\rightharpoonup0,
 \quad (C-\lambda)z_j
       =T(\Lambda-\lambda)u_j/\sqrt\lambda\longrightarrow0.
                                                               \tag{19}
\]

The exact neutral correspondence T S_P=S_N, with T an isometry on S_P,
shows that z_j belongs to S_N perpendicular after the projection in (18).
Thus every lambda in (0,1) belongs to the essential spectrum of that
compression. Essential spectrum is closed, so both endpoints do as well.

Finally C is positive, and the published compactness of (C-I)_+ excludes
essential spectrum above one. This proves (1), on the full space and on
the stated neutral complement.

## What remains unchanged

The relevant RH-bearing threshold is still C<=I, equivalently the full
P>=N comparison. The Weyl sequences here have spectral ratios at or below
one. They disprove a compact/Schatten shortcut after neutral removal, not
the threshold inequality. They do not constrain the possible discrete
excess spectrum above one and do not improve the actual fixed-main or
microscopic first-variation estimate.
