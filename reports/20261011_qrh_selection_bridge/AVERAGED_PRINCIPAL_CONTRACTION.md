# Averaged principal row for the unrestricted auxiliary ensemble

Date: 2026-10-12. Private derivation from `AVERAGED_NONPRINCIPAL_HIGH.md`, `POLYNOMIAL_AUXILIARY_ENSEMBLE.md` Part A, and `HALF_DAMPED_PROBE.md` §§3–4, 6, 9. This proves a principal-row statement for the actual finite ensemble. It does not close the whole high/low comparison and makes no RH claim.

## 1. The actual ensemble and its exact principal multiplier

Write $R$ for the auxiliary norm cap, $L=\log R$, and $\ell_R=\log\log R$,

\[
P_0=L^{64},\qquad k=\left\lfloor\frac{L}{65\ell_R}\right\rfloor,
\qquad w_p=W(Np/P_0),
\]

where the pool consists of all good prime ideals outside the fixed original bad set $S_0$, $W\geq0$ is the fixed smooth weight supported in $[1,2]$, and $N_0=\sum_p w_p\asymp P_0/\log P_0$. The ensemble is the unordered $k$-set law

\[
\Pr(J)=\frac{\prod_{p\in J}w_p}{e_k((w_p)_p)},\qquad
e_k((w_p)_p)=\sum_{|J|=k}\prod_{p\in J}w_p.
\tag{1}
\]

Thus primes are distinct and the normalizer is the elementary symmetric coefficient. The exact one-prime inclusion probability is

\[
\Pr(p\in J)=\frac{w_p\,e_{k-1}((w_q)_{q\ne p})}{e_k((w_q)_q)},
\tag{2}
\]

and, for a fixed finite set $A$,

\[
\Pr(A\subseteq J)=\frac{(\prod_{p\in A}w_p)\,e_{k-|A|}((w_q)_{q\notin A})}{e_k((w_q)_q)}.
\tag{3}
\]

These are the probabilities relevant to this ensemble. In particular, one must not insert a guessed probability such as $1/(P+1)$, or replace (1) by independent Bernoulli sampling.

For each sampled set, the auxiliary modulus satisfies $NB_J=\prod_{p\in J}Np\leq(2P_0)^k\leq R$ for all sufficiently large $R$, since $k\log(2P_0)=(64/65+o(1))\log R$.

For a sampled $J$, put $S_J=S_0\cup J$. For each $p\in J$, let $P=Np$, $d_p(s)=P^{-s}$, and $r_p(s)=\kappa(p)P^{2-6s}$, with $|\kappa(p)|=1$. The principal scalar residues and local corrections in `HALF_DAMPED_PROBE.md` give the exact identity

\[
\frac{c_{S_J}}{c_{S_0}}
\frac{H_{S_J,\mathrm{half}}(s)}{H_{S_0,\mathrm{half}}(s)}
\frac{\zeta_K^{S_0}(s)}{\zeta_K^{S_J}(s)}
=\prod_{p\in J}h_p(s),
\tag{4}
\]

where

\[
h_p(s)=\frac{(1-P^{-1})^2}{H_{p,\mathrm{half}}(s)(1-P^{-s})}.
\tag{5}
\]

Each of the three factors in (5) has a separate source: $(1-P^{-1})^2$ is the change in the two scalar zeta residues, $H_{p,\mathrm{half}}^{-1}$ deletes the local principal correction from the Euler product, and $(1-P^{-s})^{-1}$ is the inverse local factor from deleting $p$ in the target zeta denominator. Omitting any one of them gives the wrong principal normalizer.

Indeed, for $a(S)=\operatorname{Res}_{v=1}\zeta_K^S(v)$,

\[
a(S_J)=a(S_0)\prod_{p\in J}(1-P^{-1}),
\]

so the exact constant from the two residues is

\[
c_{S_J}=\widehat W_1(1)M(1/6)\frac{a(S_J)^2}{6}
=c_{S_0}\prod_{p\in J}(1-P^{-1})^2.
\tag{6}
\]

Also

\[
H_{S_J,\mathrm{half}}=H_{S_0,\mathrm{half}}\prod_{p\in J}H_{p,\mathrm{half}}^{-1},
\qquad
\zeta_K^{S_J}(s)=\zeta_K^{S_0}(s)\prod_{p\in J}(1-P^{-s}).
\tag{7}
\]

Equations (6)–(7) prove (4) by finite deletion, including the full local factors.

The exact averaged principal multiplier is therefore

\[
\mathcal M_R(s):=\mathbb E_J\prod_{p\in J}h_p(s)
=\frac{e_k((w_ph_p(s))_p)}{e_k((w_p)_p)}.
\tag{8}
\]

This is the fixed-size weighted average, not a product of one-prime expectations. Formulae (2)–(3) give its exact marginals if an expansion is desired.

## 2. Exact half-damped formula and uniform nonvanishing

At the principal scalar residues $w=1,z=1/6$, the local formula in `HALF_DAMPED_PROBE.md` is

\[
H_{p,\mathrm{half}}(s)=\frac{1-P^{-2}}{1-r_p}
\left(1+\frac{d_p-r_p}{P(1-d_p)}\right).
\tag{9}
\]

Writing $D_p=P-(P-1)d_p-r_p$, this becomes

\[
H_{p,\mathrm{half}}(s)=\frac{(1-P^{-2})D_p}{P(1-r_p)(1-d_p)}.
\]

Substitution into (5) gives the useful exact closed form

\[
\boxed{\displaystyle
h_p(s)=\frac{P(P-1)}{P+1}\,\frac{1-r_p(s)}{P-(P-1)d_p(s)-r_p(s)}.}
\tag{10}
\]

This algebra is also a check that the deleted zeta factor in (5) has been included: without $(1-P^{-s})^{-1}$, (10) does not result.

For $\sigma=\Re s>1/2$,

\[
|d_p|<P^{-1/2},\qquad |r_p|<P^{-1}.
\]

For every prime norm $P\geq7$,

\[
|D_p|\geq P-(P-1)P^{-1/2}-P^{-1}>0.6P,
\qquad |1-r_p|\geq1-P^{-1}>0.
\tag{11}
\]

For the displayed numerical margin, use $(P-1)P^{-1/2}+P^{-1}<\sqrt P+P^{-1}\leq(2/5)P$ for $P\geq7$; the last inequality holds at $7$ and its left-to-right gap increases thereafter.

Thus $h_p$ is holomorphic and nonzero on $\Re s>1/2$. If $A_P=P(P-1)/(P+1)$, then

\[
\begin{aligned}
|h_p-1|
&=\frac{|A_P(1-r_p)-D_p|}{|D_p|}\\
&\leq\frac{2/P+|d_p|+|r_p|}{0.6}
\leq 5P^{-1/2}.
\end{aligned}
\tag{12}
\]

Here $A_P-P=-2P/(P+1)$, and $|1-A_P|\leq P$ for $P\geq7$. On the buffered half-plane $\Re s\geq1/2+\delta$, for $0<\delta\leq1/2$, the same calculation gives

\[
|h_p(s)-1|\leq 9P^{-1/2-\delta}.
\tag{13}
\]

The pool has $P\in[P_0,2P_0]$, so (12) holds with $\eta_R=5P_0^{-1/2}$ for every sampled prime, uniformly in all imaginary parts and in the unit phase $\kappa(p)$. For every $J$ of size $k$,

\[
\left|\prod_{p\in J}h_p(s)-1\right|
\leq(1+\eta_R)^k-1\leq e^{k\eta_R}-1.
\tag{14}
\]

Since $k\leq L/(65\ell_R)$ and $P_0=L^{64}$,

\[
k\eta_R\leq\frac{1}{13}\frac{(\log R)^{-31}}{\log\log R}.
\tag{15}
\]

The ensemble weights in (1) are positive and sum to one. Averaging (14) therefore proves, without any assertion about an average of arbitrary nonzero complex functions,

\[
\boxed{\displaystyle
\mathcal M_R(s)=1+O\!\left(\frac{(\log R)^{-31}}{\log\log R}\right),}
\tag{16}
\]

uniformly for all $\Re s>1/2$ and all heights. In particular $\mathcal M_R(s)\ne0$ throughout that open half-plane for all sufficiently large $R$, with a single threshold. On a fixed buffered half-plane, (13) sharpens this to

\[
\mathcal M_R(s)=1+O_\delta\!\left(\frac{(\log R)^{-31-64\delta}}{\log\log R}\right)
\quad(\Re s\geq1/2+\delta).
\tag{17}
\]

The threshold for (17) can depend on δ. No angular zero-free input is needed: the source factorization is

\[
H_{S_0,\mathrm{half}}(s)=\zeta_K^{S_0}(2)^{-1}
L^{S_0}(6s-2,\kappa)E_{S_0,\mathrm{half}}(s),
\]

\[
E_{S_0,\mathrm{half}}(s)=\prod_{p\notin S_0}
\left(1+\frac{d_p-r_p}{P(1-d_p)}\right).
\tag{18}
\]

For $\Re s>1/2$, $\Re(6s-2)>1$, so (L^{S_0}(6s-2,\kappa)) has an absolutely convergent, nonvanishing Euler product. Each local numerator in (E) is (D_p), which is nonzero by the stronger bound

\[
|(P-1)d_p+r_p|<(P-1)P^{-1/2}+P^{-1}<P.
\]

The local defects of (E) are normally summable on compact subsets of this half-plane. Thus (H_{S_0,\mathrm{half}}) is holomorphic and nowhere zero there, with (H) and (1/H) uniformly bounded on each $\Re s\geq1/2+\delta$, uniformly in height. This uses absolute convergence of the angular (L)-factor only; no Q hypothesis or angular zero-free claim is used.

Any fixed small primes stay in (S_0) when already declared bad, and are not sampled. The (P\geq7) estimate is only applied to added ensemble primes; the baseline local proof (18) covers all primes outside (S_0), including any smaller ones, using the source's (P\geq2) inequality. No small-prime factor is silently replaced by the large-prime approximation.

## 3. Physical slot normalization and collisions

Let the original disjoint physical prime slots have (P_i=Z^{\ell_i}), $\ell_i>0$, and the original nonnegative slot weights (W_i). The fixed normalization is

\[
S_i(Z)=\sum_{p\in\mathcal P_i(Z)}W_i(Np/P_i)(Np)^{-5/6},
\qquad
A_T(Z)=(-1)^K Z^{-\ell/6}\prod_i S_i(Z),
\quad\ell=\sum_i\ell_i.
\tag{19}
\]

If there are no slots, take $A_T=1$. The original ray prime theorem gives $S_i(Z)>0$ for sufficiently large $Z$. With $R=Z^\lambda$, the auxiliary pool has norms at most $2P_0=2(\lambda\log Z)^{64}$, whereas every physical slot has norm at least $P_i=Z^{\ell_i}$. Consequently, for fixed $\lambda>0$ and all sufficiently large (Z),

\[
J\cap\bigcup_i\mathcal P_i(Z)=\varnothing.
\tag{20}
\]

This proves the needed absence of auxiliary/selected-tuple collisions; it is not an independence assumption. The ensemble itself has no repeated prime by (1), and the physical slot supports are already pairwise disjoint. For the principal row the sixth-power-free label is $u=1$, so $p\nmid u$ for every $p\in J$. In nonprincipal rows the exact source multiplier is zero when $p\mid u$; (5) is used only for the principal row here.

Equivalently, if $r=\prod_i p_i$ denotes a physical selected tuple, then every auxiliary prime $p\in J$ has $p\nmid r$ by (20). Thus no tuple-local factor is accidentally deleted before its original or core replacement is applied.

At $u=1$, the original and core finite compensations retain their exact source local replacements. On $\Re s\geq1/2+\delta$, each selected slot contributes $-S_i(Z)(1+\rho_{i,\star}(s))$, where $\star\in\{\mathrm{orig},\mathrm{core}\}$ and

\[
|\rho_{i,\star}(s)|\ll_\delta P_i^{-1/2-\delta}.
\]

This follows from the separate original and core principal formulas (8)–(9) of `HALF_DAMPED_PROBE.md`; the core formula must not be obtained by reusing the original simplified replacement. Define

\[
1+\mathcal R_{\star,Z}(s)=\prod_i(1+\rho_{i,\star}(s)).
\]

Then

\[
|\mathcal R_{\star,Z}(s)|\ll_\delta\sum_iP_i^{-1/2-\delta},
\qquad
Z^{\ell/6}A_T(Z)(1+\mathcal R_{\star,Z}(s))
\tag{21}
\]

is the exact selected-principal factor with its uniform approximation displayed. By (20), it is independent of (J). Thus averaging the auxiliary deletions does not alter (A_T), the ray conditions, the original/core marker choice, or any finite compensation term.

For all sufficiently large $Z$, the right side of the bound in (21) is below $1/2$. Hence the exact finite original or core slot factor $1+\mathcal R_{\star,Z}(s)$ is holomorphic and nonzero on each fixed buffered half-plane. After including every finite compensation term, the averaged numerator is exactly

\[
N_{R,Z,\star}(s)=c_{S_0}A_T(Z)H_{S_0,\mathrm{half}}(s)\mathcal M_R(s)
(1+\mathcal R_{\star,Z}(s)),
\tag{21a}
\]

up to the common scalar power $Z^{C(s)}$ and the unchanged Mellin windows. Thus the finite original/core observation preserves the nonvanishing numerator and all target poles on the buffered domain.

For the three retained contour pieces in the principal comparison, the residue factor $h_p(s)$ is only evaluated at $w=1,z=1/6$. Away from those residues, the exact deleted local factor is the source's

\[
Z_{p,\mathrm{half}}(1;x,w,z)=
\frac{(1-V)(1-P^{-w})}{(1-D)H_{p,\mathrm{half}}(x,w,z)}.
\tag{22}
\]

On the crossing box used in `HALF_DAMPED_PROBE.md` §9, choose a margin $0<\varepsilon<\min(\delta_x/8,1/200)$ and then take $d_w,\eta<\varepsilon$, where $\delta_x=(\sigma-1/2)/2$. The box lies in the half-damped critical window of `POLYNOMIAL_AUXILIARY_ENSEMBLE.md` Part A §7. The exact local multiplier then satisfies $Z_{p,\mathrm{half}}(1;x,w,z)=1+O_{\delta_x}(P^{-1/2})$ uniformly in all three heights. Hence its product over $J$ is $1+O_{\delta_x}(kP_0^{-1/2})$, so all retained contour terms remain uniformly bounded. This keeps the dynamic deleted primes distinct from the principal residue multiplier (5).

## 4. Averaged principal Mellin function and target poles

Define the varying principal meromorphic factor and its Mellin signal by

\[
F_R(s)=\frac{H_{S_0,\mathrm{half}}(s)\mathcal M_R(s)}{\zeta_K^{S_0}(s)},
\qquad
f_R(Z)=\frac1{2\pi i}\int_{(\sigma)}Z^{C(s)}e^{(s-5/6)^2}F_R(s)\,ds.
\tag{23}
\]

Here $C(s)=s+\ell_x/2-1+h/6$, $h=1-\ell_x+\ell>0$, and the integral uses the original Gaussian. Formulae (4), (8), and (20) show that $F_R$ is the exact ensemble average of the principal numerator/normalization after division by $c_{S_0}A_T$, with the finite slot factor omitted. The exact finite-slot averaged factor is $F_R(s)(1+\mathcal R_{\star,Z}(s))$; (21) shows its difference from $F_R$ has the additional power saving $Z^{-\kappa_P}$ on the buffered line.

For any zero $\rho$ of the ordinary Dedekind zeta $\zeta_K$ with $\Re\rho>1/2$, the finite deletion product relating $\zeta_K^{S_0}$ to $\zeta_K$ is nonzero, and both (H_{S_0,\mathrm{half}}(\rho)) and $\mathcal M_R(\rho)$ are nonzero. Therefore (F_R) has a pole at $\rho$ of exactly the multiplicity of that ordinary zeta zero. This conclusion holds for every fixed $\delta<\Re\rho-1/2$ and all sufficiently large (R); in fact (16) supplies one nonvanishing bound over the whole open half-plane. The factor $e^{(s-5/6)^2}$ and the scalar powers are entire and nonzero.

The changing reciprocal remains safe on any line where the fixed reciprocal is safe. If $1/\zeta_K^{S_0}(s)$ is holomorphic and polynomially bounded for $\Re s\geq\sigma>1/2$, then

\[
\prod_{p\in J}|1-P^{-s}|^{-1}
\leq\exp(CkP_0^{-\sigma})=1+o(1)
\tag{24}
\]

uniformly in (J), heights, and $\Re s\geq\sigma$. Thus the same polynomial-height bound holds for every (1/\zeta_K^{S_J}), uniformly over the ensemble. This is an explicit safe-line condition for the actual principal contour comparison; it is not inferred from half damping.

Under the hypotheses of `HALF_DAMPED_PROBE.md` §9 (in particular a fixed safe reciprocal line $1/2<\sigma<1$), the same contour sequence, with all three independent heights retained, applies uniformly in (J). Averaging yields

\[
\boxed{\displaystyle
\frac{\mathbb E_J P_{J,\star}(Z)}{c_{S_0}A_T(Z)}
=f_R(Z)+O\!\left(Z^{C(\sigma)-m}\right),}
\tag{25}
\]

for either $\star=\mathrm{orig}$ or $\mathrm{core}$, with any fixed

\[
0<m<\min\{\ell_y d_w,\,h\eta,\,\kappa_P\},
\qquad
0<\kappa_P<(1/2+\delta)\min_i\ell_i,
\quad\delta=(\sigma-1/2)/2.
\tag{26}
\]

Omit $\kappa_P$ if there are no selected slots. The (m)-saving is the existing principal comparison's power error from the retained (w,z) contours and exact finite slots; it is uniform over (J) because of (20), (22), and (24). Equation (25) concerns the actual principal row, not the full probe.

Finally, comparing the varying signal to the fixed half-damped signal (f_{\mathrm{half}}(Z)) from `HALF_DAMPED_PROBE.md` gives the separate logarithmic error

\[
f_R(Z)=f_{\mathrm{half}}(Z)
+O_\delta\!\left(
Z^{C(\sigma)}\frac{(\log R)^{-31-64\delta}}{\log\log R}
\right),
\tag{27}
\]

or the buffer-free exponent (31) from (16). This follows by inserting (17) in the absolutely convergent Gaussian Mellin integral, using the safe reciprocal height bound. For $R=Z^\lambda$, this is a log saving of at least $(\log Z)^{-31}/\log\log Z$, while the exact factor (F_R(s)) still has all target poles visible. The log error is not a power-saving high/low comparison.

## 6. Absolute Dirichlet series and the contraction transfer

Fix any $\sigma_*=1/2+\delta>1/2$. For $A(s)=\sum_{n\geq1}a(n)n^{-s}$, define

\[
\|A\|_{\sigma_*}=\sum_{n\geq1}|a(n)|n^{-\sigma_*}.
\tag{28}
\]

This coefficient norm is submultiplicative under Dirichlet convolution. Coefficients that land at equal integer indices (for example, from distinct prime ideals with equal norm) are combined after expansion and paid by the triangle inequality.

### Auxiliary factors

From (10), with the positive constant $c_p=(P-1)/(P+1)$,

\[
\frac{h_p(s)}{c_p}=\frac{1-r_p(s)}{1-\alpha_p(s)-\beta_p(s)},
\quad \alpha_p=(1-P^{-1})P^{-s},\quad
\beta_p=\kappa(p)P^{1-6s},\quad r_p=\kappa(p)P^{2-6s}.
\tag{29}
\]

At $\Re s=\sigma_*$, let $q_p=(1-P^{-1})P^{-\sigma_*}+P^{1-6\sigma_*}$. For $P\geq7$ and $\sigma_*>1/2$, $q_p\leq7^{-1/2}+7^{-2}<0.4$. Therefore

\[
(1-\alpha_p-\beta_p)^{-1}=\sum_{j\geq0}(\alpha_p+\beta_p)^j
\tag{30}
\]

converges absolutely in this norm, with norm at most $(1-q_p)^{-1}<5/3$. Its nonconstant indices are powers $P^m$, $m\geq1$. Also

\[
\frac{h_p}{c_p}-1=\frac{\alpha_p+\beta_p-r_p}{1-\alpha_p-\beta_p}.
\]

The numerator has indices $P$ and $P^6$, and

\[
\left\|\frac{h_p}{c_p}-1\right\|_{\sigma_*}
\leq\frac{(1-P^{-1})P^{-\sigma_*}+P^{1-6\sigma_*}+P^{2-6\sigma_*}}{1-q_p}
\leq CP^{-\sigma_*}.
\tag{31}
\]

Here $P^{1-6\sigma_*},P^{2-6\sigma_*}\leq P^{-\sigma_*}$ for $\sigma_*>1/2$. Thus $h_p=c_p+$ a series supported at indices $n\geq P$, with relative nonconstant norm $O(P^{-\sigma_*})$, uniformly for $P\geq7$ and every angular phase.

Write the exact weighted ensemble average as $\mathcal M_R(s)=\sum_{n\geq1}a_R(n)n^{-s}$. Its constant coefficient is

\[
a_{R,0}:=a_R(1)=\mathbb E_J\prod_{p\in J}c_p>0,
\qquad (1-2/P_0)^k\leq a_{R,0}\leq1,
\qquad a_{R,0}=1+O(k/P_0)\to1.
\tag{32}
\]

Factor $h_p=c_p(1+g_p)$, with $g_p$ constant-free and $\|g_p\|_{\sigma_*}\leq CP_0^{-\sigma_*}$. Applying (31) to each actual $k$-set and averaging its positive probability gives

\[
\boxed{\displaystyle
\sum_{n>1}|a_R(n)|n^{-\sigma_*}
\leq a_{R,0}\left[(1+CP_0^{-\sigma_*})^k-1\right].}
\tag{33}
\]

There is no nonconstant support in $1<n<P_0$. Since $P_0=(\log R)^{64}$ and $k\ll\log R/\log\log R$, the relative tail is

\[
O\!\left(\frac{(\log R)^{1-64\sigma_*}}{\log\log R}\right)=o(1).
\tag{34}
\]

This is a coefficient-norm bound for the actual fixed-size weighted average; it does not replace the ensemble by independent local choices.

### Exact original/core selected slot factor

Use the actual principal compensation formulas (8)–(9) in `HALF_DAMPED_PROBE.md`. Set

\[
\mathcal N_p(s)=1-(1-P^{-1})P^{-s}-\kappa(p)P^{1-6s}
=1-\alpha_p-\beta_p.
\]

For the original marker,

\[
B_{p,\mathrm{orig}}+1
=(1-P^{-1})\frac{r_p/d_p-r_p/P-(1-P^{-1})d_p}{\mathcal N_p(s)},
\tag{35}
\]

with the actual term $r_p/d_p=\kappa(p)P^2(P^5)^{-s}$. The numerator indices are $P^5,P^6,P$, with norm at most $P^{2-5\sigma_*}+P^{1-6\sigma_*}+P^{-\sigma_*}\leq3P^{-\sigma_*}$.

For the core marker the separate source formula is

\[
B_{p,\mathrm{core}}+1
=-(1-P^{-1})\frac{(1-P^{-1})d_p+r_p/P}{\mathcal N_p(s)}.
\tag{36}
\]

Its numerator indices are $P,P^6$, with norm at most $2P^{-\sigma_*}$. By (30), $\|\mathcal N_p^{-1}\|_{\sigma_*}<5/3$. Hence in both cases $U_{p,\star}:=-B_{p,\star}$ has constant coefficient $1$ and

\[
U_{p,\star}=1+u_{p,\star},\qquad
u_{p,\star}\text{ is constant-free},\qquad
\|u_{p,\star}\|_{\sigma_*}\leq CP^{-\sigma_*}.
\tag{37}
\]

The sign and full two-term compensation matter: the constant is $1$ for $-B_p$, with the source's $-P^{-1}$ term retained. The core identity comes from its own marked local sum, not from the original marker by domination.

For each physical slot, use its exact positive normalized weights

\[
\nu_{i,Z}(p)=\frac{W_i(Np/P_i)(Np)^{-5/6}}{S_i(Z)},
\qquad U_{i,\star,Z}(s)=\sum_{p\in\mathcal P_i(Z)}\nu_{i,Z}(p)U_{p,\star}(s).
\tag{38}
\]

They sum to one, so $U_{i,\star,Z}$ has constant $1$ and $\|U_{i,\star,Z}-1\|_{\sigma_*}\leq CP_i^{-\sigma_*}$. The exact source tuple sum factors slotwise because the tuple weights multiply and the supports are pairwise disjoint. Thus $V_{\star,Z}=\prod_iU_{i,\star,Z}=1+\mathcal R_{\star,Z}$ has constant $1$, with

\[
\|V_{\star,Z}-1\|_{\sigma_*}
\leq\prod_i(1+CP_i^{-\sigma_*})-1
=O\!\left(\sum_iP_i^{-\sigma_*}\right).
\tag{35a}
\]

No independence between an auxiliary prime and a selected tuple is assumed. By (20), for $R=Z^\lambda$ their supports are disjoint for large $Z$, so no auxiliary $p$ divides a selected tuple product $r=\prod_i p_i$. The exact full averaged principal factor, with either original or core finite slots, is therefore

\[
\mathcal A_{Z,\star}(s)=\mathcal M_{R(Z)}(s)V_{\star,Z}(s)
=\sum_{n\geq1}a_{Z,\star}(n)n^{-s},
\qquad a_{Z,\star}(1)=a_{R(Z),0}.
\tag{36a}
\]

Combining (33) and (35a),

\[
\boxed{\displaystyle
\sum_{n>1}|a_{Z,\star}(n)|n^{-\sigma_*}
\leq a_{R(Z),0}\left\{(1+CP_0^{-\sigma_*})^k
\prod_i(1+CP_i^{-\sigma_*})-1\right\}
=a_{R(Z),0}\theta_Z,}
\tag{37a}
\]

where $\theta_Z\ll kP_0^{-\sigma_*}+\sum_iP_i^{-\sigma_*}=o(1)$. Nonconstant support is at $n\geq P_0$ for large $Z$, since $P_i\gg P_0$. Thus $a_{Z,\star}(1)\geq a_*>0$, and a fixed $\theta<1$ works for all sufficiently large $Z$, including at jumps of $k$. Moreover, for every $\Re s\geq\sigma_*$,

\[
|\mathcal A_{Z,\star}(s)-a_{Z,\star}(1)|\leq a_{Z,\star}(1)\theta,
\]

so the full averaged auxiliary-plus-slot numerator is holomorphic and nowhere zero on that buffered half-plane. Multiplication by $H_{S_0,\mathrm{half}}(s)$ preserves nonvanishing. Its denominator $\zeta_K^{S_0}(s)$ therefore leaves all ordinary zeta zeros with real part at least $\sigma_*$ as poles of the exact varying principal factor.

### Exact convolution on the absolute line

The exponent in `HALF_DAMPED_PROBE.md` §9 is affine with slope one:

\[
C(s)=s+\ell_x/2-1+h/6=s-c_{\mathrm{exp}},
\qquad c_{\mathrm{exp}}=1-\ell_x/2-h/6.
\tag{38a}
\]

Put the fixed principal factors into $K(s)=e^{(s-5/6)^2}H_{S_0,\mathrm{half}}(s)/\zeta_K^{S_0}(s)$. On the original absolute line $\Re s=2$, define

\[
f(T)=\frac1{2\pi i}\int_{(2)}T^{s-c_{\mathrm{exp}}}K(s)\,ds,
\qquad
f_{R,Z,\star}(Z)=\frac1{2\pi i}\int_{(2)}Z^{s-c_{\mathrm{exp}}}
\mathcal A_{Z,\star}(s)K(s)\,ds.
\tag{39a}
\]

Here $f_{R,Z,\star}$ is the averaged principal double-residue Mellin signal, normalized by $c_{S_0}A_T(Z)$ and including the exact finite slot factor. The fixed kernel is integrable in height on line 2, and the same coefficient estimates applied at exponent $2$ give absolute convergence of the varying Dirichlet series there, also when the chosen $\sigma_*$ differs from $2$. Fubini gives the exact identity

\[
\boxed{\displaystyle
f_{R,Z,\star}(Z)=\sum_{n\geq1}a_{Z,\star}(n)n^{-c_{\mathrm{exp}}}f(Z/n).}
\tag{40a}
\]

Indeed, $Z^{s-c_{\mathrm{exp}}}n^{-s}=n^{-c_{\mathrm{exp}}}(Z/n)^{s-c_{\mathrm{exp}}}$. This holds pointwise for the actual $R(Z)=Z^\lambda$ ensemble, including every jump in $k$.

The literal principal row also has retained $w,z$ contour terms. For the transfer to that row, take $1/2<\sigma_*<1$ and assume the safe-line hypothesis in §4. `HALF_DAMPED_PROBE.md` §9 bounds those terms and the exact slot discrepancy by $O(Z^{\sigma_*-c_{\mathrm{exp}}-m})$ for some fixed $m>0$, uniformly over $J$. Thus (40a) is the exact double-residue signal and differs from the literal averaged principal row by the already proved power error.

### Contraction lemma

**Lemma.** Let $q=\sigma_*-c_{\mathrm{exp}}$. Suppose for every sufficiently large $Z$ the coefficients satisfy

\[
a_Z(1)\geq a_*>0,
\qquad \sum_{n>1}|a_Z(n)|n^{-\sigma_*}\leq\theta a_Z(1),
\qquad 0\leq\theta<1.
\tag{41a}
\]

Let $f$ be continuous on $(0,\infty)$ with $F(X)=\sup_{0<t\leq X}|f(t)|t^{-q}<\infty$ for every finite $X$. If

\[
f_Z(Z)=\sum_{n\geq1}a_Z(n)n^{-c_{\mathrm{exp}}}f(Z/n),
\qquad |f_Z(Z)|\leq K Z^q
\tag{42a}
\]

for every sufficiently large $Z$, then $|f(Z)|\ll Z^q$.

For $n>1$,

\[
n^{-c_{\mathrm{exp}}}|f(Z/n)|Z^{-q}
=n^{-\sigma_*}|f(Z/n)|(Z/n)^{-q}.
\]

Divide (42a) by $Z^q$, isolate the $n=1$ term, and apply (41a):

\[
\frac{|f(Z)|}{Z^q}
\leq\frac{K}{a_Z(1)}
+\frac{\sum_{n>1}|a_Z(n)|n^{-\sigma_*}}{a_Z(1)}F(Z)
\leq\frac{K}{a_*}+\theta F(Z).
\tag{43a}
\]

For the present fixed Mellin kernel, $F(X)$ is finite. Move the contour for $f$ from line 2 to any fixed $\Re s=\sigma'>\max\{2,\sigma_*\}$; $K(s)$ is holomorphic there and rapidly decreasing in height, so $f(t)=O_{\sigma'}(t^{\sigma'-c_{\mathrm{exp}}})$ as $t\downarrow0$. It follows that $|f(t)|t^{-q}=O(t^{\sigma'-\sigma_*})$ near zero, and continuity handles compact intervals. Taking the supremum of (43a) over $Z_0\leq Z\leq X$ gives

\[
F(X)\leq\max\left\{F(Z_0),\frac{K}{a_*}+\theta F(X)\right\},
\]

and hence $F(X)\leq\max\{F(Z_0),K/[a_*(1-\theta)]\}$ for $X\geq Z_0$. This proves the lemma. The proof is pointwise and needs no continuity or slow variation of the coefficient family or of $k$.

For (36a)–(37a), (41a) holds with $a_Z(1)=a_{R(Z),0}\to1$ and a fixed $\theta<1$ for large $Z$. A matching bound for the varying double-residue signal at exponent $O(Z^{\sigma_*-c_{\mathrm{exp}}})$ transfers to the fixed signal $f(Z)$ by the contraction lemma. For the literal averaged principal row, however, §9 supplies only an error $O(Z^{\sigma_{\mathrm{safe}}-c_{\mathrm{exp}}-m_0})$ from its double-residue signal. It supports a target exponent $\sigma_*-c_{\mathrm{exp}}$ only when $\sigma_{\mathrm{safe}}-m_0\leq\sigma_*$ (strict inequality gives room); the presently available safe line above $0.875$ does not by itself reach arbitrary $\sigma_*>1/2$. The abscissa-descent note records a conditional way to choose the safe line near the rightmost zeta-zero abscissa. This contraction avoids trying to upgrade the logarithmic comparison (27) to a power error. It does not itself prove a matching averaged whole-probe low theorem and makes no RH claim.

## 7. Scope

The derivation retains the exact positive elementary-symmetric ensemble, both varying scalar residues, the deleted target-zeta Euler factors, the principal half-damped Euler correction, and the original/core selected finite compensation. Its only analytic line condition is the same safe reciprocal-zeta hypothesis needed by the existing principal contour comparison. The angular (L)-factor is used only in its absolute convergence half-plane. No angular Q input, average-nonzero heuristic, ray-conditioned cancellation, or RH assertion is used. Nonprincipal high-row bounds and a matching whole-probe low estimate remain separate obligations.

The safe-line choice and its pole contradiction are proved in [PRINCIPAL_ABSCISSA_DESCENT.md](PRINCIPAL_ABSCISSA_DESCENT.md), conditional on the same averaged low bound. Independent verification is [REFEREE_AVERAGED_PRINCIPAL_CONTRACTION.md](REFEREE_AVERAGED_PRINCIPAL_CONTRACTION.md). The finite-order Q attribution is [FORMAL_INPUT_Q.md](FORMAL_INPUT_Q.md).
