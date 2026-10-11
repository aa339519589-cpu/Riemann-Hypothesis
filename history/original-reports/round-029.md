## Round 29 — source mass-direction correction for Bombieri's Section 11

The original Section-11 formula fixes the direction of the mass cone and
corrects an earlier interpretation in this ledger.

### I. Correctness decision

**成立 (direct source-formula correction).**

For a negative finite eigenvalue in the pure Gram problem, Bombieri normalizes
\(\sum_{\gamma\in\Gamma_N}|z_{\gamma,N}|^2=1\). The inequality obtained from
the quadratic identity is

\[
 \sum_{\gamma\notin\mathbb R}|z_{\gamma,N}|^2
 \geq
 \sum_{\gamma\in\mathbb R}|z_{\gamma,N}|^2,
\tag{29.1}
\]

and hence

\[
 \sum_{\gamma\notin\mathbb R}|z_{\gamma,N}|^2\geq\frac12.
\tag{29.2}
\]

The same orientation survives the coordinatewise limit in Bombieri's
finite-exception theorem. Thus the source-selected limiting relation has
nonzero off-line mass; it is not a relation whose required mass is primarily
on the critical line.

Accordingly, the following earlier claims in this ledger are withdrawn:

1. the statement that Section 11 itself supplies only a critical-half-mass
   condition;
2. the statement that a pure-critical kernel automatically satisfies all
   source-level mass conditions;
3. the statement that Section 11 leaves open whether its selected limit has
   nonzero exceptional mass.

The pure-critical kernel remains a valid warning that the local equation
\(F|_E=0\) alone is nonselective, but it does not satisfy (29.2). The actual
finite-exception target is a relation with a nonzero off-line component and
with its source-normalized coefficient ratio in the cone (29.1).

### II. Correct unweighted Schur target

For Section 11, with \(G_N=K_{E,N}\), write \(z_N=(c_N,e_N)\) where \(e_N\)
contains the off-line coordinates. At
\(\lambda_N=-\varepsilon_N<0\),

\[
 (G_{CC,N}+\varepsilon_NI)c_N+G_{CE,N}e_N=0,
\]

so

\[
 c_N=-(G_{CC,N}+\varepsilon_NI)^{-1}G_{CE,N}e_N.
\tag{29.3}
\]

The finite mass cone is

\[
 \|e_N\|_2\geq\|c_N\|_2,
\tag{29.4}
\]

up to the exact multiplicity and symmetry quotient used by the source. The
exceptional Schur equation still selects \(e_N\):

\[
 \left[
 G_{EE,N}+\varepsilon_NI
 -G_{EC,N}(G_{CC,N}+\varepsilon_NI)^{-1}G_{CE,N}
 \right]e_N=0.
\tag{29.5}
\]

Therefore the surviving finite-exception question is an upper bound on the
minimum critical coefficient cost relative to the exceptional coefficient
cost, not a lower bound on critical mass. If an off-line waveform \(h_E\)
admits a critical representation \(S_Cc=-h_E\) with
\(\|c\|_2\leq\|e\|_2\), then its normalized relation lies in the source mass
cone. The existence of an arbitrary unweighted representation does not
establish this inequality.

### III. Hostile audit and ledger update

**已确认事实:** Section 11's negative-eigenvector mass is on the off-line
side, as in (29.1)--(29.2); its finite block equation is the unweighted
system (29.3)--(29.5).

**成立点:** local critical kernels still show that the null equation alone
cannot select a source representative.

**失败 / 错误点:** using a pure-critical kernel or a representation with
arbitrarily inflated critical norm as if it met the source off-line mass cone.

**仍属假设:** the precise quotient treatment for repeated zeros and the
finite-to-limit stability of the source coefficient ratio.

**未知 / 待验证:** whether the minimum unweighted critical cost of the
exceptional waveform can be bounded by its off-line coefficient cost, or
whether the source-selected Schur direction forces that inequality.

**下一步路线:** compute the source-faithful unweighted quotient norm and its
dual lower bounds for exceptional exponential packets; use (29.5) only after
the mass orientation and multiplicity quotient are fixed.

**RH status:** no unconditional proof has been produced.
