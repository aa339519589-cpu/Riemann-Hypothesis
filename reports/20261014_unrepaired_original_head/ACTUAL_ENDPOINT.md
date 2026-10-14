# Actual endpoint observability from an unpenalized original-head gap

This is an exact implication of a verified unpenalized original-head bound.
The proof keeps its input gamma_H>0 explicit. The independently verified
[complete unpenalized original-head certificate](REPORT.md)
supplies gamma_H=10^(-10).
No load-penalized or finite Galerkin bound is being substituted for that
infinite-dimensional input.

Let b=log2. Assume the COMPLETE original source head form satisfies

    q_0[f_H]>=gamma_H ||f_H||_2^2,                       (H)

on its closed logarithmic Gamma domain, including the full n=2,n=3
reflections and pole. Let g=psi r be an actual pole-centered top source at
positive depth 0<delta<1. Thus Q_delta=q_0+delta N is globally nonnegative
and Q_delta(g,z)=0 in the original P completion.

Use the TRUE common seed a=(Mg)/xi on the safe ray. Choose the SAME
head-weighted constant c_a as in the retained hidden-energy theorem, and put

    a0=a-c_a, A=||a0||_infinity,
    M=integral_b^infinity W xi |a0|^2,
    e=g-c_a psi, e_H=1_(0,b)e, e_T=1_(b,infinity)e.

The global constant-ratio gauge preserves P,N and actual stationarity;
its changed pole moment is retained in every source expression below.
The actual fixed-depth regularity makes both sharp pieces original-P legal.

Let C_V denote the fixed complete theta/prime constant in
[the endpoint potential theorem](POTENTIAL_TAIL.md):

    integral_b^infinity V|e_T|^2<=C_V A sqrt(M),
    N[e_T/psi]<=4C_V A sqrt(M).                         (1)

The independently established
[full mixed weak-L2 bound](MIXED_FORCING.md)
is

    ||B_delta e_T||_L2(0,b)^2<=4000 A sqrt(M),           (2)

where B_delta retains all Gamma, prime, reflected-prime and pole cross
terms. Its statement is valid for any ONE constant c, so it applies to c_a
without changing the hidden gauge or imposing U(e)=0.

## 1. The signed original head pays its own reflected norm

By (H) and N>=0,

    Q_delta[e_H]>=gamma_H||e_H||_2^2+delta N[e_H/psi].    (3)

Actual stationarity gives

    Q_delta[e_H]=-Q_delta(e_T,e_H)
                         =-Re<B_delta e_T,e_H>.

Using (3), Cauchy--Schwarz, and the zero case separately yields

    Q_delta[e_H]<=||B_delta e_T||_2^2/gamma_H,
    N[e_H/psi]<=4000 A sqrt(M)/(delta gamma_H).         (4)

No repaired U load, neutral-load penalty, or unknown head eigenvalue is
used. The entire original head has the favorable sign (H), which is why
the earlier unpaired scalar U(e) cannot obstruct this step.

## 2. Global N and actual P with the same hidden mass

N is a genuine positive gradient-square form. Hence its triangle inequality
and (1),(4) imply

    N[e/psi]<=2N[e_H/psi]+2N[e_T/psi]
       <=[8000/(delta gamma_H)+8C_V] A sqrt(M).         (5)

Since psi is its null direction, N[e/psi]=N[g/psi]. Actual stationarity
paired with g gives P[g/psi]=(1-delta)N[g/psi]. Therefore, writing P0=P[r],

    P0 <= C_0(delta,gamma_H) A sqrt(M),
    C_0(delta,gamma_H)
       =(1-delta)[8000/(delta gamma_H)+8C_V].          (6)

The actual ratio/seed estimate in the endpoint theorem supplies

    A<=C_amp(delta) sqrt(P0).                          (7)

Here C_amp(delta) is the established fixed-depth regularity constant,
including the explicit Gaussian divisor-count majorant for the TRUE
Mobius seed. It is not a free assumption about a generic hidden field.
For P0>0, divide (6) by sqrt(P0) and square. The zero case is immediate:

    P0 <= [C_0(delta,gamma_H) C_amp(delta)]^2 M.         (8)

The [single retained hidden budget](../20261014_safe_xi_hidden_comparison/REPORT.md)
M<=125000 E_hidden gives

    P0 <=125000 [C_0(delta,gamma_H) C_amp(delta)]^2 E_hidden. (9)

This conclusion replaces a non-effective head eigenvalue by the explicit
unpenalized gap gamma_H. Constants C_V and C_amp retain their previously
proved analytical definitions; no numerical value for their product is
certified here. There is no claim of uniformity as delta decreases to zero.

## 3. What the implication does and does not establish

Equations (8)-(9) are an ACTUAL-source norm comparison at the degenerate
endpoint b. They use the genuine source equation, the full original head
sign, the actual bounded seed, all primes, and the true changed pole.
They do not assert a bounded linear generic mass-to-head operator at b.

They also do not give a favorable lower bound for the complete original
hidden remainder, show that an actual source cannot exist, or prove RH.
The U scalar obstruction to using only a load-penalized head theorem is
not ignored; it is bypassed only by the stronger unpenalized input (H).
