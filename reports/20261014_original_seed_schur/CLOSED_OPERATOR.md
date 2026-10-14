# A closed original Schur form in the true safe-seed mass space

This note uses the generic lower comparison in
[MASS_LOWER_BOUND.md](MASS_LOWER_BOUND.md).
It changes topology explicitly. It does NOT assert a closable nonnegative
original form on ordinary odd-source L2, or a positive original Schur form.
The source pole and complete arithmetic future lift remain part of the form.

Let b=log2, m=Wxi on (b,infinity), and H_m=L2((b,infinity),m(y)dy).
The exact future map is

    (C_xi a)(x)=sum_(n>=1)n^(-1/2)xi(x+log n)a(x+log n), x>b. (1)

It is locally bounded from H_m into L2 on every closed interval strictly
to the right of b, and bounded into L2(exp(2x)dx) on every ray x>B>b.
These statements follow from the complete Minkowski estimate (6) in the
cited lower-comparison proof, not from an inverse-zeta multiplier.
No such bound is asserted at the degenerate endpoint b.

## 1. A closed hybrid source graph

Use the Hilbert space

    X=L2(0,b) direct-sum H_m.

For (u,a) in X define J(u,a) by u on (0,b) and C_xi a on (b,infinity),
whenever this piecewise source is in L2 and its zero-supported odd extension
has finite complete positive Gamma form q_b. Let D be this graph domain.
Its graph norm is

    ||a||_m^2+||J(u,a)||_2^2+q_b[J(u,a)_o].           (2)

D is complete in (2). Indeed a graph-Cauchy sequence has a mass limit a
and a Gamma/L2 source limit f. Its head tends to u=f|_(0,b). By the local
boundedness of (1) on every x>b+epsilon, the tail limit satisfies
f=C_xi a almost everywhere. Hence (u,a) lies in D and is the graph limit.
This argument pays the endpoint through the CLOSED GRAPH; it does not
pretend (1) is a bounded map into the endpoint source norm.

D is dense in X. Compact smooth heads are dense in L2(0,b), and compact
smooth seeds supported away from b are dense in H_m. For such a seed (1)
is a locally finite smooth sum and is compactly supported on the positive
wing. Concatenation at b introduces only a bounded jump, which has finite
logarithmic Gamma form. Thus these pairs lie in D.

Multiplication by a sharp fixed interval cutoff is bounded on the Gamma
source norm. The direct proof uses the logarithmic Hardy estimate

    integral_0^(L/2)|v(s)|^2 log[L/(2s)]ds
      <=2 integral_(0<2s<t<L)|v(s)-v(t)|^2/t dsdt
                                      +integral_0^L|v(t)|^2dt.

The regional difference kernel is bounded by the full Gamma jump kernel
on fixed collars. Far cross-cut terms are L2 bounded. Thus cuts at b or at
the fixed B below are legal without a trace assumption. In particular
(2) is equivalent to the split-source Gamma norm plus the mass norm.

## 2. The ORIGINAL source form is closed and semibounded on this graph

Let B>b be the unconditional enlarged positive head provided by the cited
lower-comparison theorem, and lambda=gamma/2>0 its lower bound. Write
f=J(u,a), v=f1_(0,B), F=f1_(B,infinity). The complete source expression
q0[f] is well-defined on D. All negative tail rows are bounded by the
weighted L2 norm of F; its full mixed density is also L2 bounded, and
that weighted norm is bounded by ||a||_m. Only finitely many internal
prime shifts/reflections remain on the compact head, and all are retained.

The full row estimates give

    q0[f]>= (1/2)q0[v]+q_b[F_o]
                     -9Q_B[C_T(B)+2K_B^2/lambda]||a||_m^2. (3)

Here Q_B,C_T,K_B are the COMPLETE constants of that theorem. This time
half of the positive head form is retained: use
2K_B S||v||<=q0[v]/2+2K_B^2 S^2/lambda.
Since q0[v]>=lambda||v||^2 and q_b[v_o]<=q0[v]+C_max||v||^2,
(3) implies, for a sufficiently large fixed C_1,

    q0[J(u,a)]+C_1||a||_m^2
       >=c[||f||_2^2+q_b[f_o]+||a||_m^2], c>0.       (4)

Conversely all the same bounded source rows and the split Gamma inequality
give an upper bound by a finite constant times the right graph norm.
Therefore q0+C_1 mass is a closed positive form with norm equivalent to
(2), and q0 is a densely defined closed SEMIBOUNDED form on X. No positivity
of q0 itself is inferred. This explicit graph completion is different from
ordinary-source L2 and from the original P norm.

## 3. Closed minimization over the original head

Let D_m consist of seeds a for which the zero-supported odd tail
1_(x>b)C_xi a has finite L2/Gamma source norm. The cutoff statement above
shows that this is exactly the set of mass components occurring in D.
It is dense in H_m. For each a in D_m put t=1_(x>b)C_xi a. Its weighted
L2 tail norm is finite: compact collars use its source L2 norm, and the
far wing uses (1). Hence its COMPLETE mixed density B0 t belongs to L2(0,b).

The verified head A0 has gap gamma>0 on its source domain D0. Its unique
original-harmonic extension is

    E0 a=t-A0^(-1)B0 t,
    s0[a]=q0[E0 a]=q0[t]-<B0 t,A0^(-1)B0 t>.          (5)

Thus s0 is precisely the original Schur form expressed in the TRUE seed
variable, not an auxiliary Markov metric. It is lower bounded by

    s0[a]>=-C_*||a||_m^2.                            (6)

The form is CLOSED. To see this directly, let a_j be Cauchy for
s0+C_1 mass. The corresponding harmonic graph vectors E0 a_j are Cauchy
for q0+C_1 mass because (5) is an exact quadratic identity, including
polarization. By (4) they converge in the closed graph D. Harmonicity
against every head source persists by form continuity. The limit is
therefore the unique extension E0 a of its seed limit, proving that a
belongs to D_m and establishing form convergence.

Consequently s0 defines a selfadjoint operator S on H_m bounded below by
-C_*. Its negative spectral part is a bounded operator, of norm at most
C_*. Neither discreteness of that negative part nor its vanishing is
claimed.

## 4. The entire closed neutral span is an honest zero-mode space

The constant seed 1 corresponds to psi. For each centered neutral jet
s_j=psi^(2j)-4^(-j)psi, its genuine safe seed is

    a_j=xi^(2j)/xi-4^(-j), j>=1.

These seeds belong to H_m and D_m by their polynomial growth and the full
Gaussian weights. Their global original sources are q0-neutral. The
neutral identities first extend in the AMBIENT source class consisting of
finite Gamma norm and finite far exponentially weighted L2 norm: ordinary
source cutoffs and mollifiers converge there, and the complete theta mixed
rows make the pairing with each fixed jet continuous. Restrict that identity
to graph sources afterward. No claim is made that arbitrary compact source
approximants themselves lie in the C_xi seed graph, and no inverse-C density
is used. Equivalently one can use the original-source Schur neutral extension
already proved.
It follows that

    s0(a_j,a)=0 for every a in D_m, and s0(1,a)=0.

Hence every a_j and 1 is in the OPERATOR kernel of S, not merely a formal
quadratic null direction. Put

    K=closure_(H_m) span{1,a_1,a_2,...}.

Since the kernel of a closed selfadjoint operator is closed,

    K subset ker S.                                 (7)

For any a in D_m, the orthogonal mass projection Pi_K a lies in ker S,
thus in the operator/form domain. Therefore

    a_perp=a-Pi_K a belongs to D_m,
    s0[a_perp]=s0[a], ||a_perp||_m<=||a-c||_m          (8)

for every constant c. This is a genuine infinite neutral projection in a
specified Hilbert space. It is NOT a claim that the neutral seeds are dense
in H_m, and it is not the finite E_hidden-orthogonal projection. The
projected seed is not asserted to retain finite hidden Gamma energy,
original P membership, actual boundedness, or actual wall transmission.
Those properties are unnecessary for the closed Schur statement (8).

## 5. Exact actual negative direction survives the whole neutral projection

For an actual source g at positive depth delta, its true safe seed belongs
to D_m. The independently proved actual Schur identity is

    s0[a]=-delta N[g/psi]-delta^2 D_g,
    D_g=<n_g,A0^(-1)n_g>, n_g=2(Vg-F_r g).

Thus (8) gives the SAME strictly negative value on its mass-orthogonal
neutral complement, and (6) yields

    delta N[g/psi]+delta^2 D_g <=C_*||a_perp||_m^2
                                     <=C_* integral m|a-c_a|^2. (9)

This uses one and the same original source and the true complete future
seed. It does not reclassify the projected vector as an actual eigen-source.
A proof of nonnegativity of S on K-perp is still absent. Establishing the
closed operator and its exact infinite null quotient does not establish
that missing sign or RH.
