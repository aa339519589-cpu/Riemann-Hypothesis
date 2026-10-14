# The genuine prime 2 edge is paid by a central Gamma routing

The SINGLE original prime 2 energy admits a useful complete Gamma form
comparison. This is not a comparison of the entire prime form with Gamma:
the complete incoming prime row has a different far-wing scale, and must
remain in the higher-prime source forcing. The coefficient below is less
than3, which is the relevant threshold for the dominant4/3 source-energy
mismatch in the true Mobius conditional metric.

## 1. Original kernels and the theorem

Use the exact positive theta ground source

 psi(x)=exp(x/2)sum_(n>=1)c(n^2 z)exp(-n^2 z),
 c(q)=8q^3-30q^2+15q, z=pi exp(2x),
 kappa(t)=exp(-t/2)/(1-exp(-2t)).

The original Gamma energy has ONE orientation:

 F_Gamma[u]=int_(0<x<y)psi(x)psi(y)kappa(y-x)|u(x)-u(y)|^2 dxdy.

Set d=log2, alpha=log2/sqrt2 and

 F_2[u]=alpha int_0^infinity psi(x)psi(x+d)|u(x)-u(x+d)|^2 dx.

Then for every measurable complex or Hilbert-valued u with finite Gamma
energy,

    F_2[u] <=(11/4)F_Gamma[u].                       (1)

There is no change to the original prime 2 coefficient. The inequality is
constant-gauge invariant and needs neither a source eigenstate equation
nor individual prescribed point traces: it is an integrated form bound.
No reflected prime or polar term is identified with F_2.

## 2. A true intermediate-point probability

Put C=(0,1/2), R=1/2, and

 J=int_C psi(a)da=Phi(0)-Phi(R),
 I(y)=int_C psi(a)kappa(y-a)da, y>=d.

For each prime 2 edge y=x+d define the positive probability

    rho_y(da)=1_C(a)psi(a)kappa(y-a)da/I(y).

Two full-theta row estimates, certified below, are

    alpha psi(x)/I(x+d) <=3/2, x>=0,                 (2)

 alpha psi(x+d)kappa(x+d-a)
       /[I(x+d)kappa(|x-a|)] <=1/12,
                  x>=0, a in C, x!=a.              (3)

Their roles differ: (2) pays the lower-density terminal against the
Gamma edge from the hub, and (3) pays the return to the actual initial
point. The intermediate distribution depends on the terminal; no mean
or source values are replaced by an independent field.

## 3. Complete two-edge proof, with orientation counting

For every intermediate a, the exact two-piece decomposition and Young
inequality give

 |u(y)-u(x)|^2
    <=(3/2)|u(y)-u(a)|^2+3|u(a)-u(x)|^2.             (4)

Average (4) in rho_y and integrate the ORIGINAL prime 2 conductance.
By (2), the first term is at most

 (9/4)int_(y>=d,a in C)psi(a)psi(y)kappa(y-a)
                                  |u(y)-u(a)|^2 dady
    <=(9/4)F_Gamma[u].                              (5)

Here a<R<d<=y, so this is a genuine single-orientation subset.
By (3), the second term is at most

 (1/4)int_(x>=0,a in C)psi(x)psi(a)kappa(|x-a|)
                                  |u(x)-u(a)|^2 dadx
    <=(1/2)F_Gamma[u].                              (6)

The factor2 in (6) is retained: the C-by-C portion occurs in BOTH
orientations. Adding (5)-(6) proves (1). All measures are positive, so
Tonelli and form completion justify the same statement beyond smooth
core functions, without an unproved endpoint sampling bound.

## 4. Complete theta tails and the directed incoming certificate

Let P(q)=4q^2-6q. The standard exact theta identity psi=-Phi' gives J.
The following elementary full-tail enclosures are used:

 psi_lower(x)=exp(x/2)[c(z)exp(-z)+c(4z)exp(-4z)] <=psi(x),
 psi_upper(x)=exp(x/2)[c(z)exp(-z)+1024z^3exp(-4z)] >=psi(x),
 Phi_upper(x)=exp(x/2)[P(z)exp(-z)+128z^2exp(-4z)] >=Phi(x).

The omitted n>=3 terms in psi_lower are positive. For psi_upper, use
c(n^2z)<=8n^6z^3 and the complete consecutive tail ratio
(3/2)^6 exp(-5pi)<1/2. The Phi bound follows from the corresponding
n^4 ratio. Thus no theta truncation is declared exact. In particular

    J> P(pi)exp(-pi)-Phi_upper(1/2)>0.831.

The positive expansion kappa(t)=sum_(j>=0)exp[-(2j+1/2)t] gives

 I(y)>=sum_(j=0)^7 U_j exp[-(2j+1/2)y],
 U_j=int_0^(1/2)psi(a)exp[(2j+1/2)a]da.              (7)

The accompanying directed interval checker computes lower enclosures
for all eight U_j using10000 disjoint cells, the complete lower theta
bound, and psi>=0. It then verifies (2) on6000 closed cells covering
0<=x<=3/5, using the full psi_upper and (7). Its largest directed upper
ratio is below1.499573, strictly less than3/2. The unrounded endpoints,
not these printed decimals, are used in every assertion.

For x>=3/5, all q=n^2pi exp(2x)>10. Since

    4c(q)-q c'(q)=q(8q^2-60q+45)>0, q>=10,

and that quadratic is increasing there, each positive term of
exp(x/2)psi(x) has logarithmic derivative at most9-2q<0. Hence that
whole function decreases. Using I(y)>=J exp(-y/2),

 alpha psi(x)/I(x+d)
    <=[log2/J]exp(x/2)psi(x)
    <=[log2/J]exp(3/10)psi_upper(3/5)<0.268.          (8)

This proves the entire infinite wing of (2) analytically, not by stopping
the finite interval scan.

## 5. The return-path estimate includes all initial positions

For0<=x<=R and a in C,

 kappa(x+d-a)/kappa(|x-a|)<=kappa(d-R)/kappa(R).

For x>=R, monotonicity and the exact exponential ratio give the stronger
upper bound exp(-d/2)<1, so the displayed uniform bound still holds.
Also I(y)>=J kappa(y). On y>=d, the function psi(y)/kappa(y) decreases:
the positive theta terms of exp(y/2)psi(y) have log derivative<=9-2q,
q>=4pi>12, while the factor1-exp(-2y) adds at most2/3. Therefore

 alpha psi(y)kappa(y-a)/[I(y)kappa(|x-a|)]
   <=alpha psi_upper(d)kappa(d-R)/[J kappa(d)kappa(R)]
   <0.080361<1/12.                                  (9)

The same directed checker verifies the last strict comparison using the
complete tail upper bound and the certified lower J. Equations (8)-(9)
pay every large x and every hub endpoint. The diagonal x=a is a null set
and the kernel ratio has its natural zero limit there.

## 6. Reproducibility and exact use in the current problem

Run check_prime2_gamma_routing.py with Python and mpmath. It uses
55-digit directed interval arithmetic, explicit full-tail inequalities,
10000 moment cells and6000 source cells, and prints its certificate as
JSON. All source and tail assumptions used in the analytic completion
are asserted. The generated JSON is only a transcript of the reproducible
assertions, not a replacement for the inequalities above.

A useful algebraic consequence is

    (4/3)F_2 <=(44/45)(F_Gamma+F_2),                 (10)

because F_2<=11F_Gamma/4. This spends the SAME Gamma/prime 2 form once;
(10) is not an additional resource to add to (1). It identifies why the
coefficient below3 is useful for the genuine dominant source-gradient
mismatch. Before inserting (10) into the Mobius current equation, its
true conditional metric, the complete higher-prime forcing, the
Gamma/profile cross and original reflected/pole form must all remain.
No full-prime/Gamma comparison, actual-null invariance or RH sign is
asserted.
