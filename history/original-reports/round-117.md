## Round 117 — exact unweighted regularization criterion for the Section-11 critical block

The source-faithful Section-11 block admits one further exact reduction.  It
does not solve the RH alternative, but it separates a finite-section
comparison estimate from the unproved assertion that the selected exceptional
direction has that estimate.

Let (C_N) be the critical coordinates in a finite truncation, let

[
 S_{C,N}c(u)=sum_{gammain C_N}c_gamma e^{-igamma u},
 qquad h_N=S_{E,N}e_N,
]

and write (lambda_N=-
arepsilon_N<0).  In the pure unweighted Gram
coordinates of Section 11, the critical block equation is

[
 (S_{C,N}^{*}S_{C,N}+
arepsilon_N I)c_N
   =-S_{C,N}^{*}h_N .
	ag{117.1}
]

Consequently (c_N) is the unique minimizer of

[
 mathcal J_{N,
arepsilon_N}(c)
   =|S_{C,N}c+h_N|_{L^2(E)}^2
      +
arepsilon_N|c|_2^2 .
	ag{117.2}
]

This follows by taking the first variation of (117.2), so it uses no
limit or RH assumption.  For every comparison vector (a_N), (117.2) gives

[
 |c_N|_2
 leq |a_N|_2
      +
rac{|S_{C,N}a_N+h_N|_{L^2(E)}}{sqrt{
arepsilon_N}} .
	ag{117.3}
]

Thus an exact critical representation is useful for the finite branch only
with a rate: if (S_Ca=-h), (a_N) is a finite truncation of (a), and

[
 |S_{C,N}a_N+h_N|=o(sqrt{
arepsilon_N}),
	ag{117.4}
]

then (limsup|c_N|_2leq|a|_2).  The existence of a representation with
no estimate such as (117.4) does not control the selected eigenvector when
(
arepsilon_N) tends to zero faster than the truncation residual.

For a fixed bounded synthesis operator (S_B:ell^2(B)	o L^2(E)) supplied by
a Riesz-basis subsystem, the exact coefficient cost of a target (h) has the
dual form

[
 inf_{S_Ba=h}|a|_2
 =sup_{|S_B^*v|_2leq1}|langle h,v
angle_{L^2(E)}|,
	ag{117.5}
]

whenever (hinoperatorname{Ran}S_B).  The inequality from right to left is
immediate; the reverse equality follows by taking the minimum-norm solution,
which is orthogonal to (ker S_B), and approximating its direction by the
dense range of (S_B^*) on ((ker S_B)^perp).  Formula (117.5) identifies
the source-faithful unweighted separation target: to contradict the
Section-11 off-line mass cone, one would need a dual (v) with

[
 |S_B^*v|_2leq1,qquad
 |langle h_E,v
angle|>|e_E|_2,
	ag{117.6}
]

for the exceptional packet selected by the finite Schur equation.

The short-interval Kadec construction in Rounds 30 and 115 goes in the
opposite direction for an arbitrary fixed finite conjugate off-line packet:
for sufficiently small (E), it supplies a critical representation whose
coefficient norm is (o(|e_E|_2)).  Hence (117.6) cannot follow from local
completeness, zero counting, or the mass cone alone.  To make (117.6) a proof
route one would need an additional arithmetic property of the exact
Schur-selected packet, not merely an arbitrary local representation.

**Established:** (117.1)--(117.3) are the exact source-coordinate
regularization and comparison inequalities; (117.5) is the corresponding
unweighted quotient dual for a bounded Riesz subsystem.

**Failure / missing step:** exact range membership without the
(sqrt{
arepsilon_N})-scale residual does not control the finite eigenvector;
the local dual separation required by (117.6) is contradicted by the
conditional short-interval construction for general packets.

**Route decision:** the remaining source-faithful target is either a theorem
that supplies (117.4) for the *selected* branch together with a strict mass
inequality, or a different global arithmetic positivity theorem. Neither has
been proved here.

**RH status:** no unconditional proof has been produced.
