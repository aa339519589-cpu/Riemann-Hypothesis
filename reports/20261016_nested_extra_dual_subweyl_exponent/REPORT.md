# A fully explicit nested-dual bound with exponent 229/1392

Status: complete proof and directed certificate, with completed independent internal review and reproducible replay.

## 1. Statement, dependencies and scope

The theorem is
\[
 |\zeta(1/2+it)|\le110|t|^{229/1392}\qquad(|t|\ge3).       \tag{1}
\]
The useful envelope keeps the minimum with the already established bounds
49|t|^(27/164) and 90|t|^(77/468). The exponent229/1392 is classical and is
explicitly identified in Patel–Yang's conclusion. We do not claim a new
unrestricted asymptotic exponent, exhaustive explicit-bound priority, or a
consequence for a proportion of zeros. The work here supplies the uniform
constants and all complementary ranges for this particular explicit bound.

We use [the complete extra-B theorem](../20261016_extra_dual_subweyl_exponent/REPORT.md)
for its first logarithmic Poisson reduction, Stieltjes representation and
established coefficient90. We use the same primary explicit A-process,
weighted power-sum inequality, complete Poisson formula and fourth-derivative
test as that theorem. All new nested processes and their errors are proved
below. No unpublished coefficient51 or formal exponent-pair assertion is an
input.

Write e(x)=exp(2 pi i x), and write S_f for a sum of e(f(n)) over a specified
half-open interval. We use the following two primary bounds:
\[
 |S_f|\le A_4(\eta,H)H^{1/4}n\lambda^{1/14}
                  +B_4(\eta)n^{3/4}\lambda^{-1/14},       \tag{2}
\]
when the fourth derivative has constant sign, is monotone, and lies in
absolute value between lambda and H lambda. The interval in(2) has integer
endpoints and length n. The Poisson error for decreasing f' is
\[
 4.686\lambda_2^{-1/2}+6+\frac5\pi\log(M+2)
 +\frac{2\,3^{2/3}}{\pi^{2/3}}H_2H_3^{1/3}L\lambda_3^{1/3}. \tag{3}
\]
Here L and M are the primal and dual interval lengths. Before an
integer-endpoint estimate is applied to any dual partial sum, remove its
first integer. This costs one maximum weight, and leaves integer length at
most M. Thus all occurrences of4.686 below are increased to5.686. The
half-open Poisson convention is otherwise unchanged. The positive weights
are monotone, so partial summation costs one maximum weight, not two.

For -1<s<=1, let b_s=2/((1+s)(2+s)). The weighted power sum used throughout is
\[
 \frac2Q\sum_{1\le j<Q}(1-j/Q)j^s\le b_sQ^s.            \tag{4}
\]
The A-process is valid for every integer Q>=1, without assuming Q is less
than the sum length: zero extension makes empty correlations zero. Its
weighted correlation measure has total mass at most one. These facts
justify the Jensen and subadditivity steps below.

## 2. First dual phase and strengthened local derivative bounds

In a large logarithmic block a<n<=b<=ha and a correlation1<=r<a, both x and
x+r remain in[a,b]. Put
\[
 C=\sqrt{tr/(2\pi)},\quad N=tr/(2\pi h^2a^2),\quad H=h^2,
 \quad \epsilon=\pi r/(2t).
\]
The exact first dual phase satisfies
\[
 \phi'(\nu)=r/2-C\sqrt{1/\nu+\epsilon},
 \qquad N\le\nu\le HN.                                  \tag{5}
\]
The containing interval follows from the exact endpoints
tr/(2 pi b(b-r)) and tr/(2 pi a(a+r)). The Stieltjes representation from the
dependency is
\[
 \sqrt{1/\nu+\epsilon}=\sqrt\epsilon+
 \frac1\pi\int_0^{1/\epsilon}
       \frac{\sqrt{1/s-\epsilon}}{\nu+s}\,ds.
\]
Differentiating gives the relative loss bound
\[
 1-\frac{\epsilon\nu}{2m-1}
 \le\frac{(-1)^m(\sqrt{1/\nu+\epsilon})^{(m)}}
              {(1/2)_m\nu^{-m-1/2}}\le1\qquad(m\ge1).    \tag{6}
\]
It follows either by comparing the density with s^(-1/2), whose loss is at
most epsilon*s, or by the corresponding beta-integral ratio1/(2m-1).

Set s0=10^(-12), q1=1-10^(-10), p=5/2. For
\[
 f=-\Delta_i\Delta_j\Delta_k\phi,\qquad D=3Cijk/4,
\]
if all shifts have total at most s0*N and epsilon times every argument is
at most s0, then, for1<=m<=7,
\[
 q_1D(p)_m\nu^{-p-m}\le(-1)^mf^{(m)}(\nu)
                      \le D(p)_m\nu^{-p-m}.               \tag{7}
\]
Indeed the lower ratio is at least
(1+s0)^(-p-m)(1-s0/(2m+3)), which the certificate proves exceeds q1 for all
seven m. All differences are taken only where their arguments lie in the
original dual interval. Section7 proves both guards for every retained
triple, not just for typical shifts.

## 3. Uniform inverse derivatives of the second dual phase

Apply(3) to -f, whose derivative decreases. If y=-f'(nu), its dual phase is
G(y)=-f(nu)-y nu. Set
\[
 a_*=5/7,\quad e_0=(7/2)(5/2)^{-5/7},\quad
 y_0=q_1(5/2)H^{-7/2},\quad H_Y=H^{7/2}/q_1,
\]
\[
 E=e_0D^{2/7},\qquad Y=y_0DN^{-7/2}.                       \tag{8}
\]
The actual second dual interval is contained in[Y,H_Y Y]. The model phase
is -E y^(5/7). We need its derivative comparison, not an identity of phases.

For completeness, the entire directed algebra is specified here. For the
ordinary Legendre phase Psi=f-nu f', put P2=-1 and
\[
 P_{m+1}=f_2\sum_{j=2}^m\frac{\partial P_m}{\partial f_j}f_{j+1}
                         -(2m-3)f_3P_m.                 \tag{9}
\]
Then Psi^(m)=P_m/f2^(2m-3). Each term has the same scaling
D^(1-m) nu^((m-1)p+m). Evaluate this rational expression with
f_j/((-1)^j(p)_jD nu^(-p-j)) in[q1,1]. Divide by its exact model value,
and multiply by the interval[q1^(m-5/7),1]. The latter accounts for
nu/(pD/y)^(2/7) in[q1^(2/7),1].

The checker constructs the integer/rational polynomials(9), evaluates every
term with outward Arb arithmetic, and proves for2<=m<=7
\[
 1-\varepsilon_G\le
 \frac{G^{(m)}(y)}{(-E y^{5/7})^{(m)}}
 \le1+\varepsilon_G,\qquad \varepsilon_G=10^{-5}.          \tag{10}
\]
The largest computed relative interval radius is less than1.46e-8, well
inside this bound. Negating f and changing the dual variable multiplies
both actual and model derivatives by the same signs. No absolute-value
sign is inferred from an uncertified numerical sample.

The maximum second-Poisson weight and its dual-length majorant are
\[
 W D^{-1/2}N^{9/4},\qquad d_MDN^{-7/2},
\]
where
\[
 W=q_1^{-1/2}(35/4)^{-1/2}H^{9/4},\quad d_M=(H-1)(35/4).   \tag{11}
\]
The weight decreases in the increasing dual variable. Its endpoint debit
is5.686 W D^(-1/2)N^(9/4). The derivative error is T_D D^(1/3)N^(-5/6), with
\[
 T_D=\frac{2\,3^{2/3}}{\pi^{2/3}}
 \frac{H^{9/2}}{q_1}\left(\frac{H^{11/2}}{q_1}\right)^{1/3}
 (H-1)\big(q_1(315/8)H^{-11/2}\big)^{1/3}.                \tag{12}
\]
The remaining error is the full6+(5/pi)log(2+d_M D N^(-7/2)).

## 4. Two A-processes and the third Poisson formula

Put
\[
 \kappa_2=Y^{53/140}E^{-1/10}
         =k_0D^{7/20}N^{-53/40},\quad
 k_0=y_0^{53/140}e_0^{-1/10}.                              \tag{13}
\]
First suppose kappa2>=2 and (3/2)kappa2^2<=s2Y, where s2=1/1000.
Choose K2=floor(kappa2), and use the two A lengths K2,K2^2. Their total
shift is at most(3/2)kappa2^2. By(10), a double difference of G has the
model form D2*y^(-p2), with
\[
 p_2=9/7,\quad D_2=c_DEij,\quad c_D=(1+\varepsilon_G)10/49.
\]
For1<=m<=5, its signed derivatives lie between q2 and1 times the model,
where q2=99/100. This follows from
\[
 \frac{1-\varepsilon_G}{1+\varepsilon_G}
       (1+s_2)^{-p_2-m}>q_2,                              \tag{14}
\]
checked for all five m. The phase is positive, decreasing and convex;
its third derivative is negative. Apply(3) to its negative, again matching
the primary decreasing-derivative convention.

Here are all constants for this third B-process. Put c_j=(p2)_j and
\[
 m_4=3q_2^2c_3^2-c_4c_2,\quad M_4=3c_3^2-q_2^2c_4c_2,
 \quad \lambda_*=m_4/c_2^5,
\]
\[
 H_4=(M_4/m_4)q_2^{-5}H_Y^{3p_2+4},\quad
 w_*=q_2^{-1/2}c_2^{-1/2}H_Y^{(p_2+2)/2},\quad d_*=(H_Y-1)c_2.
\]
The fourth Legendre numerator has fixed sign because m4>0. Its fifth
numerator is negative because
\[
 -q_2^3c_5c_2^2+10c_3c_4c_2-15q_2^3c_3^3<0.              \tag{15}
\]
Both inequalities are certified. Thus the transformed fourth derivative is
monotone and its absolute range is the required one. Define
\[
 T_1=w_*A_4(6/5,H_4)H_4^{1/4}d_*\lambda_*^{1/14},
 \quad T_2=w_*B_4(6/5)d_*^{3/4}\lambda_*^{-1/14},
\]
\[
 T_3=5.686w_*,\quad
 T_4=\frac{2\,3^{2/3}}{\pi^{2/3}}
 \frac{H_Y^{p_2+2}}{q_2}
 \left(\frac{H_Y^{p_2+3}}{q_2}\right)^{1/3}
 (H_Y-1)(q_2c_3H_Y^{-p_2-3})^{1/3}.
\]
For every partial double-difference sum the resulting bound has the four
rows T_j D2^d Y^n with
\[
 (d,n)=(2/7,-4/49),\ (13/28,-31/49),\ (-1/2,23/14),\ (1/3,-3/7), \tag{16}
\]
and the entire logarithmic error6+(5/pi)log(2+d_*D2Y^(-16/7)). The first
removed dual integer is covered by T3, including when the dual interval is
shorter than one. All interval endpoints remain inside the phase domain.

Write ell2=H_Y-1 and J2=ell2+s2. Iterating the A-process twice gives the
sum of two diagonal terms
\[
 Y\big((J_2\ell_2)^{1/2}+J_2^{3/4}\ell_2^{1/4}\big)K_2^{-1/2}
\]
and a correlation term (J2Y)^(3/4) times the fourth root of the weighted
average of the double-difference sum. The weighted measures have mass at
most one. By(4), a row T D2^dY^n contributes
\[
 V(T,d)E^{7d/40}Y^{3/4+n/4+159d/560},
\]
\[
 V(T,d)=J_2^{3/4}(T c_D^d b_d^2)^{1/4}
                         2^{\max(0,-3d/4)}.             \tag{17}
\]
The power of2 retains the lower floor bound K2>=kappa2/2 when d<0.
Add sqrt(2)[(J2ell2)^(1/2)+J2^(3/4)ell2^(1/4)] to the coefficient of the
first row. Both diagonal terms then have exactly its E,Y powers.

The full third-Poisson logarithm also remains. Since i*j<=kappa2^3,
\[
 M_3\le d_*c_DE^{7/10}Y^{-23/20}
       =L_3D^{-19/20}N^{161/40},\quad
 L_3=d_*c_De_0^{7/10}y_0^{-23/20}.
\]
In the range under consideration D>=1 and1<N<t^(3/2), so
M3<=L3 t^(483/80). Therefore set
\[
 d_3=6+(5/\pi)\log(2+L_3),\qquad e_3=2415/(80\pi).
\]
The logarithmic row after the two A-processes is
J2^(3/4)(d3+e3 log t)^(1/4)Y^(3/4). No logarithm is replaced by a constant
independent of height without its compensating decreasing exponential.

## 5. Both complementary inner ranges

The small-length failure kappa2<2 implies
\[
 D<L_1N^{53/14},\qquad L_1=(2/k_0)^{20/7}.                 \tag{18}
\]
Failure of the shift guard implies
\[
 D<L_2N^{17/6},\qquad L_2=((3/2)k_0^2/(s_2y_0))^{10/3}.  \tag{19}
\]
We do not discard either range and do not apply the new derivative lemma
there. Remove the first integer as already paid by the second-Poisson
endpoint debit. The rest of the dual sum has length at most d_M D N^(-7/2),
so its returned weighted contribution is at most
\[
 Wd_MD^{1/2}N^{-5/4}.
\]
On each failure set multiply this majorant by (Dcrit/D)^(1/4)>=1. The two
complete complementary rows are therefore
\[
 Wd_ML_1^{1/4}D^{1/4}N^{-17/56},\qquad
 Wd_ML_2^{1/4}D^{1/4}N^{-13/24}.                          \tag{20}
\]
The union is bounded by their sum. An overlap merely overestimates the
bound. All positive rows from the good region may also be extended to all
triples. The endpoint, derivative and logarithmic terms(11)–(12) remain
on every range.

To return a good row V E^kY^l to the triple-difference sum, multiply by the
weight(11) and use(8). Its coefficient and powers are
\[
 WVe_0^ky_0^l\,D^{2k/7+l-1/2}N^{9/4-7l/2}.              \tag{21}
\]
The complete list of D,N powers is as follows, in the order used by the
certificate:

| Origin | D power | N power |
|---|---:|---:|
| third B main, including the two diagonals | 13/40 | -47/80 |
| third B secondary | 79/320 | -181/640 |
| third B endpoint | 79/160 | -421/320 |
| third B derivative error | 61/240 | -53/160 |
| third B logarithm | 1/4 | -3/8 |
| small second K complement | 1/4 | -17/56 |
| excessive second shift complement | 1/4 | -13/24 |
| second B endpoint | -1/2 | 9/4 |
| second B derivative error | 1/3 | -5/6 |
| second B logarithm | 0 | 0 |

The third logarithm's coefficient contains(d3+e3 log t)^(1/4).
For the second logarithm, Section6 gives the majorant d2+e2 log t.
Every coefficient is given by(11)–(21), and all are recorded in the JSON.

## 6. The three outer-inner A-processes and first B return

Choose
\[
 \kappa=N^{127/502}C^{-13/251},\qquad K=\lfloor\kappa\rfloor,
\]
and first suppose kappa>=2. Use the three lengths K,K^2,K^4. Their sum is
at most(11/8)kappa^4. Put ell=H-1 and J=ell+s0. The diagonal contribution is
\[
 N\big((J\ell)^{1/2}+J^{3/4}\ell^{1/4}
                    +J^{7/8}\ell^{1/8}\big)K^{-1/2}.
\]
A triple-difference row T D^dN^n, with D=3Cijk/4, gives
\[
 U(T,d)C^kN^l,
\quad U(T,d)=J^{7/8}(T(3/4)^db_d^3)^{1/8}
                                 2^{\max(0,-7d/8)},
\]
\[
 k=20d/251,\qquad l=7/8+n/8+889d/4016.                   \tag{22}
\]
Add sqrt(2) times the displayed three diagonal coefficients to the main
row. Its powers are C^(13/502)N^(877/1004).

On this good range N>1. Also D<=3Ckappa^7/4, so
\[
 d_MDN^{-7/2}\le(3d_M/4)C^{160/251}\le(3d_M/4)t^{1/2}.
\]
Here C<t^(3/4). Thus the full second logarithm is bounded by
\[
 d_2+e_2\log t,\quad
 d_2=6+(5/\pi)\log(2+3d_M/4),\quad e_2=5/(2\pi).         \tag{23}
\]
Its contribution in(22) has coefficient(d2+e2 log t)^(1/8).

The first-Poisson weight is sqrt(pi)h^(3/2)a^(3/2)(tr)^(-1/2).
A row U C^kN^l consequently becomes V a^alpha(tr)^beta with
\[
 V=U\sqrt\pi h^{3/2}(2\pi)^{-k/2-l}h^{-2l},\quad
 \alpha=3/2-2l,\quad\beta=k/2+l-1/2.                    \tag{24}
\]
The main pair is(alpha,beta)=(-62/251,97/251). All ten rows are retained.
The original first-Poisson errors, on every range, are
\[
 E_4a^{3/2}(tr)^{-1/2}+E_5a^{-1/3}(tr)^{1/3}
 +6+(5/\pi)\log(2+(h-1)tr/(\pi a^2)),                   \tag{25}
\]
where E4=5.686sqrt(pi)h^(3/2) and E5=6h^3(h-1)/pi.

If kappa<2, then
\[
 r<R_0=d_Ra^{127/57}/t,\quad
 d_R=2\pi h^{127/57}2^{251/57}.                          \tag{26}
\]
Use the full trivial first-dual length, with the first integer already
paid by E4. Its bound is d_T a^(-1/2)(tr)^(1/2),
where d_T=(h-1)h^(3/2)/sqrt(pi). Averaging over r<min(q,R0) gives at most
\[
 d_S\{d_R^{3/2}a^{54/19}t^{-1}/q+a^{-1/2}t^{1/2}/q\},
 \quad d_S=(4\sqrt2/3)d_T.                              \tag{27}
\]
Indeed the weighted sum is bounded by2/q times the ordinary sum, and
sum(r^(1/2))<= (2sqrt(2)/3)(R0^(3/2)+1). This is the full complementary
range; no lower estimate on its proportion is used.

## 7. Uniform outer parameters, guards and infinite geometric sums

Set
\[
 x_0=10000,\quad h_1=51/50,\quad h_2=103/100,
 \quad\theta_2=1,\quad\theta_3=10^{-5},\quad\vartheta=229/1392.
\]
Use large blocks down to theta2*t^(3/7), with floor correction
\[
 c=1-(h_1/\theta_2)e^{-3x_0/7},\quad h=h_1/c,
 \quad B_0=\theta_2/h_1-e^{-3x_0/7}.
\]
Thus each large block's lower endpoint is at least B0*t^(3/7).
Let beta1=97/251 and V1 be the main coefficient in(24). Choose
\[
 \theta=\left(\frac{h-1}{\beta_1b_{\beta_1}V_1}\right)^{1/(1+\beta_1)},
 \qquad q_a=\lfloor\theta a^{313/348}t^{-97/348}\rfloor. \tag{28}
\]
Writing qa=313/348 and qt=-97/348 only in the next formulas, put
\[
 q_0=\theta B_0^{q_a}e^{((3/7)q_a+q_t)x_0},\quad Z=1-1/q_0,
 \quad p_0=\theta B_0^{q_a-1}e^{((3/7)(q_a-1)+q_t)x_0},
 \quad A=h-1+p_0.
\]
The checker proves q0>2, p0<.01, and p0^2/4<s0. These show the outer
integer length is lawful and q_a/a<=p0, hence the epsilon-argument guard
in(7). The triple-shift guard follows from
\[
 \kappa^4/N=(N^3/C^{52})^{1/251},\quad
 C^{52}/N^3=(tr/(2\pi))^{23}h^6a^6\ge(t/(2\pi))^{23},
\]
and the certified inequality exp(23(x0-log(2pi)))>((11/8)/s0)^251.
Thus(11/8)kappa^4<=s0N, uniformly above x0. The inner shift failures have
already been handled by(19)–(20), so no further unproved shift guard is
needed.

After the outer A-process and weight a^(-1/2), a row(V,alpha,beta) has
coefficient and exponents
\[
 D=\sqrt{A b_\beta V\theta^\beta Z^{\min(\beta,0)}},\quad
 u=(\alpha+(313/348)\beta)/2,\quad v=(251/348)\beta/2.     \tag{29}
\]
The main diagonal combines with its main correlation into
\[
 D_1=\sqrt{A((h-1)/(\theta Z)+b_{97/251}V_1\theta^{97/251})},
 \quad(u_1,v_1)=(35/696,97/696).                          \tag{30}
\]
For a positive block exponent u the entire geometric sum divided by
t^vartheta is bounded by
\[
 \frac{D(2\pi)^{-u/2}}{h_1^u-1}
                   e^{(u/2+v-\vartheta)x_0}.           \tag{31}
\]
For u<0 it is bounded by
\[
 \frac{Dc^u(h_1/\theta_2)^{-u}}{1-h_1^u}
                   e^{((3/7)u+v-\vartheta)x_0}.          \tag{32}
\]
In particular the second-Poisson endpoint has u=-659/11136 and normalized
height exponent-1/3248. It is not estimated at the top endpoint.

The new principal correction exponents from(31) are respectively
-1/22272, -1/1536, -17/66816, and-5/5568 for the third-B secondary,
endpoint, derivative and logarithmic rows. The two inner complementary
rows have exponents-1/7424 and-179/66816. The second-B derivative and
logarithm have exponents-19/8352 and-83/11136. All original first-B and
bad-kappa rows also have negative exponents, checked exactly by the script.
The main exponent is exactly zero. The growing third logarithm has final
power1/64, and the second logarithm power1/16. Their derivative is at most
that power divided by x; the checker proves each complete exponential
product decreases for x>=x0.

For(25)'s first logarithm use r<=a, a>=B0*t^(3/7), and the full majorant
\[
 d_1+e_1x,\quad d_1=6+(5/\pi)\log(2+(h-1)/(\pi B_0)),
 \quad e_1=20/(7\pi).
\]
The number of large blocks is at most x/(14log h1)+1. Thus its entire
normalized contribution is bounded by
\[
 \sqrt A\left(\frac1{14\log h_1}+\frac1{x_0}\right)
 \sqrt{d_1/x_0+e_1}\ x_0^{3/2}e^{-\vartheta x_0}.         \tag{33}
\]
The complete product decreases. Finally(27), after(28), gives two rows
with coefficients sqrt(A dS dR^(3/2)/(theta Z)) and sqrt(A dS/(theta Z)),
and exponent pairs
\[
 (u,v)=(12845/13224,-251/696),\quad(-487/696,271/696).
\]
Their full geometric sums use(31) and(32), respectively.

## 8. Remaining Riemann–Siegel blocks and complete splice

The initial and middle sums are treated as in the dependency but with the
new theta. The middle cutoff is theta3*t^(2vartheta), the upper cutoff
theta2*t^(3/7). Set
\[
 h_3=h_2/(1-(h_2/\theta_3)e^{-2\vartheta x_0}),
\]
\[
 D'_1=(3/\pi)^{1/14}A_4(1,h_3^4)h_3^{5/7}(h_3-1),
 \quad D'_2=(\pi/3)^{1/14}B_4(1)h_3^{2/7}(h_3-1)^{3/4}.
\]
Retaining also the shortened top middle block, its entire normalized bound is
\[
 U_2=\frac{D'_1\theta_2^{3/14}}{h_2^{3/14}-1}e^{(8/49-\vartheta)x_0}
    +\frac{D'_2\theta_2^{15/28}}{h_2^{15/28}-1}e^{(31/196-\vartheta)x_0}.
\]
Both height exponents are negative. The initial normalized sum is at most
U1=2sqrt(theta3+exp(-2vartheta*x0)/2). Let U3 be the sum of every complete
large-block contribution above. Including both Riemann–Siegel halves and
both remainder terms gives
\[
 |\zeta(1/2+it)|/t^\vartheta\le2(U_1+U_2+U_3)
 +1.48e^{(-1/4-\vartheta)x_0}+.127e^{(-3/4-\vartheta)x_0}. \tag{34}
\]
All partition-order and floor conditions are explicitly checked. At192-bit
Arb precision, the complete right side is strictly less than
103.140912578044659, uniformly for every log t>=10000.

On3<=t<=exp10000 the already established coefficient90 gives
\[
 |\zeta(1/2+it)|/t^\vartheta
 \le90\exp(10000/54288)<108.203362294481255<110.            \tag{35}
\]
Conjugation handles negative t. Equations(34)–(35) establish the theorem. No finite
sample of heights replaces an infinite-height bound.

Run `python certify_nested_exponent.py` with python-flint0.9.0/FLINT3.6.0.
The standalone script implements the source derivative recurrence, the
exact inverse polynomials, all new coefficients, signed exponent sums,
complementary rows, uniform guards and the entire tail/splice. Its scientific
JSON records the exact parameters, rational powers, directed intervals and
script hash. It contains no machine paths, runtime logs or unproved transfer.

## Primary sources

1. D. Patel and A. Yang, *An explicit sub-Weyl bound for zeta(1/2+it)*,
Journal of Number Theory262(2024),301–334,
https://doi.org/10.1016/j.jnt.2024.03.011 ; primary readable preprint
https://arxiv.org/html/2302.13444v1 . Sections1.2–2 supply the complete
processes; Section4 explicitly records the classical229/1392 exponent.
2. G. A. Hiary, D. Patel and A. Yang, *An improved explicit estimate for
zeta(1/2+it)*, https://arxiv.org/html/2207.02366v1 , for the unchanged
Riemann–Siegel normalization and complete remainder.
3. The checked extra-B dependency linked in Section1, with its fully written
first-lattice-point repair and global coefficient90.

The formal word A B A^3 B A^2 B A^2 B explains the power choices, but is
not substituted for the actual inverse-derivative calculations, error
terms or complementary ranges in this proof.
