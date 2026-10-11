# Research Note 233 — The radial-current transform

## 0. Purpose

Note 232 reduced the all-zero problem to positivity of the polarized
horizontal-current kernel

\[
 \mathcal N_F(z,w)
 =\frac{F'(z)\overline{F(w)}
        +F(z)\overline{F'(w)}}{z+\bar w}.             \tag{0.1}
\]

For a positive bilateral source \(F(z)=\int e^{zt}\phi(t)\,dt\), formula
(0.1) still contains a quotient by the spectral variables and is not a
manifest Gram kernel.  This note removes that quotient before taking the
Laplace transform.

It introduces a nonlinear two-variable source transform

\[
                         \phi\longmapsto\mathfrak R[\phi],      \tag{0.2}
\]

called the **radial-current transform**.  Its defining equation is a
one-dimensional conservation law in the sum coordinate \(r=t+u\).  The
main identity is

\[
 \boxed{\mathcal N_F(z,w)
 =\iint_{\mathbb R^2}\mathfrak R[\phi](t,u)
          e^{zt+\bar w u}\,dt\,du.}                  \tag{0.3}
\]

Consequently, positive-semidefiniteness of the explicit source kernel
\(\mathfrak R[\phi]\) forces every zero of \(F\) onto \(i\mathbb R\),
including zeros of arbitrary multiplicity.  No zero list occurs in the
definition.

The transform has a nontrivial calculus:

* on a Gaussian density it is a positive rank-one kernel;
* on a uniform density it is a positive Dirichlet Green kernel;
* it obeys an exact convolution Leibniz rule, so its positive cone is
  closed under convolution;
* the cone is not closed under positive mixtures, which is consistent with
  the existence of positive even densities having off-axis Laplace zeros.

For the Riemann theta density, RH is therefore reduced to one concrete
source assertion:

\[
                       \boxed{\mathfrak R[\Phi]\succeq0.}       \tag{0.4}
\]

This assertion is not proved here.  The contribution is the new source
transform, its exact all-zero theorem, and its structural calculus.

No density, proportion, mollifier, numerical, or finite-height argument is
used.

## 1. Admissible bilateral sources

Let \(\phi:\mathbb R\to(0,\infty)\) be real, even, and continuously
differentiable.  Assume that for every \(A>0\),

\[
 \int_{\mathbb R}e^{A|t|}
       \bigl(\phi(t)+|\phi'(t)|\bigr)\,dt<\infty.      \tag{1.1}
\]

The bilateral Laplace transform

\[
 F(z)=\int_{\mathbb R}e^{zt}\phi(t)\,dt               \tag{1.2}
\]

is then entire, even, real on the real axis, and strictly positive there.
All differentiations and changes of variables below are justified by
(1.1).  Compactly supported bounded densities are also admitted by direct
use of the integral formulas; smoothness is only a convenient default
class.

For \(r,q\in\mathbb R\), define the product density in sum/difference
coordinates

\[
 \Psi_\phi(r,q)
 =\frac12\,
   \phi\!\left(\frac{r+q}{2}\right)
   \phi\!\left(\frac{r-q}{2}\right).                 \tag{1.3}
\]

Evenness of \(\phi\) gives

\[
 \Psi_\phi(-r,q)=\Psi_\phi(r,q),\qquad
 \Psi_\phi(r,-q)=\Psi_\phi(r,q).                     \tag{1.4}
\]

## 2. Definition by a radial conservation law

Define the tail current

\[
 M_\phi(r,q)
 =\int_{|r|}^{\infty}v\,\Psi_\phi(v,q)\,dv.          \tag{2.1}
\]

It is pointwise nonnegative and even in both variables.  Its decisive
property is

\[
                         -\partial_r M_\phi(r,q)
                         =r\Psi_\phi(r,q).            \tag{2.2}
\]

For \(r>0\), (2.2) is the fundamental theorem of calculus.  For \(r<0\),
differentiating the lower endpoint \(-r\) and using (1.4) gives the same
identity.  Both sides vanish continuously at \(r=0\).

### Definition 2.1 (radial-current transform)

\[
 \boxed{\mathfrak R[\phi](t,u)
 :=M_\phi(t+u,t-u).}                                 \tag{2.3}
\]

The kernel is real and symmetric:

\[
 \mathfrak R[\phi](t,u)=\mathfrak R[\phi](u,t).       \tag{2.4}
\]

Pointwise nonnegativity follows from (2.1), but the property needed below
is stronger.

### Definition 2.2 (radial-current positivity)

The density \(\phi\) is **RC-positive** when

\[
 \iint_{\mathbb R^2}\mathfrak R[\phi](t,u)
       f(t)\overline{f(u)}\,dt\,du\ge0               \tag{2.5}
\]

for every \(f\in C_c^\infty(\mathbb R)\).  Equivalently,
\(\mathfrak R[\phi]\) is a positive-semidefinite integral kernel.

Pointwise positivity and kernel positivity must not be confused.  The
former is automatic; the latter is a genuine global constraint coupling
all source points.

### Lemma 2.3 (arbitrary exponential moments of the current)

For every \(A>0\),

\[
 \iint_{\mathbb R^2}e^{A(|t|+|u|)}
       \mathfrak R[\phi](t,u)\,dt\,du<\infty.          \tag{2.6}
\]

#### Proof

In the coordinates \(r=t+u,\ q=t-u\), one has

\[
 |t|+|u|=\max(|r|,|q|),\qquad dt\,du=\frac12dr\,dq.   \tag{2.7}
\]

Tonelli's theorem and (2.1) therefore give an upper bound for the left
side of (2.6) by

\[
 \int_{\mathbb R}\int_0^\infty
       v^2 e^{A(v+|q|)}\Psi_\phi(v,q)\,dv\,dq.         \tag{2.8}
\]

Indeed, after interchanging the \(r\)- and \(v\)-integrals, the inner
range is \(-v\le r\le v\), whose contribution is at most
\(2v e^{A(v+|q|)}\).  Now put
\(x=(v+q)/2,\ y=(v-q)/2\).  On \(v\ge0\),

\[
 v^2\le2(x^2+y^2),\qquad
 v+|q|\le2(|x|+|y|),\qquad
 \Psi_\phi(v,q)=\frac12\phi(x)\phi(y).                \tag{2.9}
\]

Thus (2.8) is finite by (1.1), with a slightly larger exponential
weight absorbing the polynomial factor. \(\square\)

## 3. The double-Laplace current identity

### Theorem 3.1 (radial-current factorization)

For all \(z,w\in\mathbb C\), with the quotient interpreted by removable
continuation when \(z+\bar w=0\),

\[
 \boxed{
 \frac{F'(z)\overline{F(w)}
       +F(z)\overline{F'(w)}}{z+\bar w}
 =\iint_{\mathbb R^2}\mathfrak R[\phi](t,u)
       e^{zt+\bar w u}\,dt\,du.}                    \tag{3.1}
\]

Both sides are sesquientire on all of \(\mathbb C^2\).

#### Proof

The numerator on the left is

\[
 \iint_{\mathbb R^2}(t+u)
       \phi(t)\phi(u)e^{zt+\bar w u}\,dt\,du.         \tag{3.2}
\]

Set

\[
 r=t+u,\qquad q=t-u,\qquad
 \alpha=\frac{z+\bar w}{2},\qquad
 \beta=\frac{z-\bar w}{2}.                           \tag{3.3}
\]

Since \(dt\,du=\frac12dr\,dq\), the definition (1.3) turns (3.2) into

\[
 \iint_{\mathbb R^2}r\Psi_\phi(r,q)
        e^{\alpha r+\beta q}\,dr\,dq.                \tag{3.4}
\]

By (2.2) and the super-exponential decay, integration by parts in \(r\)
has no boundary term and gives

\[
 (3.4)
 =\alpha\iint_{\mathbb R^2}
      M_\phi(r,q)e^{\alpha r+\beta q}\,dr\,dq.        \tag{3.5}
\]

When \(\alpha\ne0\), dividing by \(z+\bar w=2\alpha\), and then returning to
\((t,u)=((r+q)/2,(r-q)/2)\), yields

\[
 \frac12\iint M_\phi(r,q)e^{\alpha r+\beta q}\,dr\,dq
 =\iint\mathfrak R[\phi](t,u)e^{zt+\bar w u}\,dt\,du,
\]

which is (3.1).  Lemma 2.3 makes the right side sesquientire.  On the
hyperplane \(\bar w=-z\), evenness gives

\[
 F'(z)F(-z)+F(z)F'(-z)=0,                              \tag{3.6}
\]

so the quotient on the left has a removable continuation.  Taking the
limit from \(\alpha\ne0\) completes the identity there as well.
\(\square\)

The conservation law (2.2) is precisely what removes the spectral
denominator.  It is not an asymptotic approximation.

## 4. The all-zero theorem

### Theorem 4.1 (RC positivity forces the reflection axis)

If \(\phi\) is RC-positive, then every zero of its bilateral Laplace
transform \(F\) lies on \(i\mathbb R\).

#### Proof

By Theorem 3.1, for any finite points \(z_j\in\Pi_+\) and coefficients
\(c_j\),

\[
\begin{aligned}
 \sum_{j,k}c_j\overline{c_k}\mathcal N_F(z_j,z_k)
 &=\iint\mathfrak R[\phi](t,u)
      G(t)\overline{G(u)}\,dt\,du,\\
 G(t)&=\sum_jc_je^{z_jt}.
                                                               \tag{4.1}
\end{aligned}
\]

Choose \(A>2\max_j|\Re z_j|\).  Lemma 2.3 permits smooth cutoff
approximation of \(G\) in (2.5), with dominated convergence for the
quadratic integral.  Hence the right side is nonnegative.  Thus
\(\mathcal N_F\) is a positive kernel on \(\Pi_+\).

Suppose \(F\) has a zero \(\rho\in\Pi_+\) of exact multiplicity \(m\).
Write

\[
 F(z)=(z-\rho)^m g(z),\qquad g(\rho)\ne0.             \tag{4.2}
\]

For \(z_\varepsilon=\rho-\varepsilon\), where
\(0<\varepsilon<\Re\rho\), one has

\[
 \frac{F'(z_\varepsilon)}{F(z_\varepsilon)}
 =-\frac{m}{\varepsilon}+O(1).                       \tag{4.3}
\]

On the diagonal,

\[
 \mathcal N_F(z,z)
 =\frac{|F(z)|^2}{\Re z}
    \Re\!\left(\frac{F'(z)}{F(z)}\right).             \tag{4.4}
\]

Equations (4.2)--(4.4) give

\[
 \mathcal N_F(z_\varepsilon,z_\varepsilon)
 =-\frac{m|g(\rho)|^2}{\Re\rho}\,
       \varepsilon^{2m-1}+O(\varepsilon^{2m})<0       \tag{4.5}
\]

for sufficiently small \(\varepsilon\).  This contradicts positivity.
Hence \(F\) has no zero in \(\Pi_+\).  Evenness sends every left-half-plane
zero to \(\Pi_+\), so every zero lies on the axis. \(\square\)

The proof is local at a hypothetical zero but the hypothesis is one global,
zero-independent source inequality.  Every multiplicity is covered by the
same sign reversal (4.5).

### Theorem 4.2 (order-one exactness)

Assume in addition that \(F\) has order at most one.  Then

\[
 \boxed{
 \mathfrak R[\phi]\succeq0
 \quad\Longleftrightarrow\quad
 \text{every zero of \(F\) lies on \(i\mathbb R\)}.}   \tag{4.6}
\]

#### Proof

The forward implication is Theorem 4.1.  Conversely, suppose every zero
lies on the axis.  Since \(F\) is even, \(F(0)>0\), and its order is at
most one, the paired Hadamard product is

\[
 F(z)=F(0)\prod_{\gamma>0}
       \left(1+\frac{z^2}{\gamma^2}\right)^{m_\gamma},
 \qquad \sum_{\gamma>0}\frac{m_\gamma}{\gamma^2}<\infty,       \tag{4.7}
\]

where \(m_\gamma\) is the multiplicity at \(i\gamma\).  There is no
nonconstant exponential factor: the order bound makes it at most linear,
and evenness makes the linear coefficient vanish.  Logarithmic
differentiation gives

\[
 \frac{F'(z)}{F(z)}
 =\sum_{\gamma>0}\frac{2m_\gamma z}{z^2+\gamma^2}.     \tag{4.8}
\]

Consequently the entire continuation of the current kernel has the Gram
expansion

\[
\begin{aligned}
 \mathcal N_F(z,w)
 &=2\sum_{\gamma>0}m_\gamma
   \left(A_\gamma(z)\overline{A_\gamma(w)}
        +B_\gamma(z)\overline{B_\gamma(w)}\right),    \tag{4.9}\\
 A_\gamma(z)&=\frac{zF(z)}{z^2+\gamma^2},
 &B_\gamma(z)&=\frac{\gamma F(z)}{z^2+\gamma^2}.
\end{aligned}
\]

The apparent singularities of \(A_\gamma,B_\gamma\) are removable, and
the series converges locally by the summability in (4.7).  Thus
\(\mathcal N_F\) is a positive kernel, in particular on the boundary
\(z=i\xi,\ w=i\eta\).

For \(f\in C_c^\infty(\mathbb R)\), Fourier inversion and Theorem 3.1 give

\[
\begin{aligned}
 &\iint\mathfrak R[\phi](t,u)f(t)\overline{f(u)}\,dt\,du\\
 &\quad=\frac1{(2\pi)^2}\iint
       \mathcal N_F(i\xi,i\eta)
       \widehat f(\xi)\overline{\widehat f(\eta)}\,d\xi\,d\eta
 \ge0.                                                \tag{4.10}
\end{aligned}
\]

Here \(\widehat f(\xi)=\int f(t)e^{-i\xi t}dt\).  The integrals are
justified by Lemma 2.3: it makes \(\mathcal N_F(i\xi,i\eta)\) bounded,
while \(\widehat f\in L^1\).  Equivalently, (4.10) is the unitary Fourier
congruence of the two kernels.  Hence
\(\mathfrak R[\phi]\succeq0\). \(\square\)

### Corollary 4.3 (exact theta-source RH compiler)

Let \(\Phi\) be the positive even Riemann theta density, and form
\(\mathfrak R[\Phi]\) from (1.3), (2.1), and (2.3).  Its bilateral
Laplace transform is a positive constant multiple of
\(F(z)=\xi(1/2+z)\), an even entire function of order one.  Positive
rescaling of \(\Phi\) does not change RC positivity.  Therefore

\[
 \boxed{\mathfrak R[\Phi]\succeq0\quad\Longleftrightarrow\quad\mathrm{RH}.}
                                                               \tag{4.11}
\]

This condition is stated entirely in the source variables \(t,u\).  It
does not use the zero set, a height cutoff, or a zero count.  The reverse
implication is included: (4.11) is an exact source-space equivalence, not
only a sufficient criterion.

## 5. Exact convolution calculus

For kernels on \(\mathbb R^2\), write

\[
 (K*_{2}L)(t,u)
 =\iint_{\mathbb R^2}K(t-r,u-s)L(r,s)\,dr\,ds.        \tag{5.1}
\]

For a one-variable function \(g\), put

\[
 P_g(t,u)=g(t)g(u).                                  \tag{5.2}
\]

This is a positive rank-one kernel.

### Theorem 5.1 (radial-current Leibniz rule)

If \(\phi=\phi_1*\phi_2\), then

\[
 \boxed{
 \mathfrak R[\phi_1*\phi_2]
 =\mathfrak R[\phi_1]*_{2}P_{\phi_2}
  +P_{\phi_1}*_{2}\mathfrak R[\phi_2].}              \tag{5.3}
\]

#### Proof

Let \(F_i\) be the bilateral Laplace transform of \(\phi_i\).  Then
\(F=F_1F_2\).  Direct differentiation of (0.1) gives

\[
 \mathcal N_{F_1F_2}(z,w)
 =F_2(z)\overline{F_2(w)}\,\mathcal N_{F_1}(z,w)
  +F_1(z)\overline{F_1(w)}\,\mathcal N_{F_2}(z,w).
                                                               \tag{5.4}
\]

The double bilateral Laplace transform of \(P_{\phi_i}\) is
\(F_i(z)\overline{F_i(w)}\), and two-variable convolution becomes
multiplication.  Applying Theorem 3.1 to (5.4) shows that the two sides of
(5.3) have identical double Fourier transforms on \(z=i\xi,w=i\eta\).
Uniqueness of the Fourier transform gives (5.3). \(\square\)

### Lemma 5.2 (positive congruence under two-variable convolution)

If \(K\in L^1(\mathbb R^2)\) is a positive kernel and
\(g\in L^1(\mathbb R)\) is real, then \(K*_{2}P_g\) is positive.

#### Proof

For a test function \(f\), Fubini and the changes \(x=t-r\), \(y=u-s\)
give

\[
\begin{aligned}
 &\iint (K*_{2}P_g)(t,u)f(t)\overline{f(u)}\,dt\,du\\
 &\qquad=\iint K(x,y)(A_gf)(x)\overline{(A_gf)(y)}\,dx\,dy,
                                                               \tag{5.5}\\
 &(A_gf)(x)=\int_{\mathbb R}g(r)f(x+r)\,dr.
\end{aligned}
\]

The function \(A_gf\) is bounded.  Cut it off smoothly and use dominated
convergence against \(|K|\in L^1\); the last expression is therefore
nonnegative by positivity of \(K\). \(\square\)

### Corollary 5.3 (the RC-positive cone is convolution closed)

If \(\phi_1\) and \(\phi_2\) are RC-positive, then
\(\phi_1*\phi_2\) is RC-positive.

#### Proof

Each term on the right side of (5.3) is positive by Lemma 5.2, and their
sum is positive. \(\square\)

This closure law is a genuine structural gain over a bare transform
criterion.  It permits positive source factorizations to be assembled
without returning to the zero set.

## 6. Two exact positive building blocks

### 6.1 Gaussian source: a rank-one current

Let

\[
 \phi_\beta(t)=\sqrt{\frac{\beta}{\pi}}\,e^{-\beta t^2},
 \qquad \beta>0.                                    \tag{6.1}
\]

Then

\[
 \Psi_{\phi_\beta}(r,q)
 =\frac{\beta}{2\pi}
   e^{-\beta(r^2+q^2)/2},                            \tag{6.2}
\]

and hence

\[
 M_{\phi_\beta}(r,q)
 =\frac1{2\pi}e^{-\beta(r^2+q^2)/2}.                 \tag{6.3}
\]

Since \(r^2+q^2=2(t^2+u^2)\),

\[
 \boxed{
 \mathfrak R[\phi_\beta](t,u)
 =\frac1{2\beta}\phi_\beta(t)\phi_\beta(u).}          \tag{6.4}
\]

Thus the Gaussian current is positive rank one.  Its Laplace transform
\(F_\beta(z)=e^{z^2/(4\beta)}\) is zero-free, consistently with Theorem
4.1.

### 6.2 Uniform source: a Dirichlet Green kernel

Let

\[
 \phi_\delta(t)=\frac1{2\delta}\mathbf1_{[-\delta,\delta]}(t),
 \qquad\delta>0.                                     \tag{6.5}
\]

Put \(c=(2\delta)^{-1}\).  Formula (1.3) gives
\(\Psi=c^2/2\) on the diamond \(|r|+|q|\le2\delta\), and zero outside.
Therefore

\[
 M_{\phi_\delta}(r,q)
 =\frac{c^2}{4}
   \bigl((2\delta-|q|)^2-r^2\bigr)_+.                \tag{6.6}
\]

Returning to \(t,u\), the support condition is
\(|t|,|u|\le\delta\), and elementary factorization gives

\[
 \boxed{
 \mathfrak R[\phi_\delta](t,u)
 =c^2\,
   (\delta+\min(t,u))(\delta-\max(t,u))
   \mathbf1_{\{|t|,|u|\le\delta\}}.}                 \tag{6.7}
\]

Define the factor in (6.7), divided by \(2\delta\), to be
\(G_\delta(t,u)\).  It is the Green kernel of \(-d^2/dt^2\) on
\([-\delta,\delta]\) with Dirichlet boundary conditions.  It is positive
because for \(f\in L^2[-\delta,\delta]\), if
\(-v''=f\) and \(v(\pm\delta)=0\), then

\[
 \iint G_\delta(t,u)f(t)\overline{f(u)}\,dt\,du
 =\int_{-\delta}^{\delta}|v'(t)|^2\,dt\ge0.          \tag{6.8}
\]

Hence the uniform density is RC-positive.  Its Laplace transform

\[
 F_\delta(z)=\frac{\sinh(\delta z)}{\delta z}         \tag{6.9}
\]

has only imaginary zeros.

By Corollary 5.3, every finite convolution of Gaussian and uniform
building blocks is RC-positive.  The transform therefore contains a
nontrivial source cone with a direct positive-kernel proof, not merely a
formal implication.

## 7. Mixture obstruction and the Riemann target

The cone is not convex under positive mixtures.  To prove this without
assuming a converse to Theorem 4.1 outside the order-one class, first let

\[
 b_A=\frac12(\delta_{-A}+\delta_A),\qquad
 C_A(z)=\cosh(Az).                                    \tag{7.1}
\]

In the distributional extension of Theorem 3.1, its current is

\[
 \mathfrak R[b_A](t,u)
 =\frac A2\mathbf1_{[-A,A]}(t)\,\delta_t(u),           \tag{7.2}
\]

because its double Laplace transform is

\[
 \frac A2\int_{-A}^A e^{(z+\bar w)t}\,dt
 =\frac{A\sinh(A(z+\bar w))}{z+\bar w}
 =\mathcal N_{C_A}(z,w).                              \tag{7.3}
\]

The distribution (7.2) is positive, since its quadratic form is
\((A/2)\int_{-A}^A|f(t)|^2dt\).  Let \(h=\phi_\beta\) be a Gaussian.
Applying (5.3) with finite measures gives

\[
 \mathfrak R[h*b_A]
 =\mathfrak R[h]*_2P_{b_A}+P_h*_2\mathfrak R[b_A].    \tag{7.4}
\]

Both terms are positive congruences and are ordinary kernels.  The
identity follows first at the level of double Laplace transforms and then
by Fourier uniqueness, exactly as in Theorem 5.1.  Hence both \(h\) and
\(h*b_A\) are smooth, strictly positive, even, and RC-positive.

For \(0<\varepsilon<1/2\), however, their positive mixture has transform

\[
 e^{z^2/(4\beta)}
 \frac{1+2\varepsilon\cosh(Az)}{1+2\varepsilon},      \tag{7.5}
\]

and the second factor has the explicit off-axis zeros

\[
 z=\frac{\pm\operatorname{arcosh}(1/(2\varepsilon))
              +(2k+1)\pi i}{A},\qquad k\in\mathbb Z.  \tag{7.6}
\]

Theorem 4.1 therefore forces the mixture's radial-current kernel to have a
negative direction.  Thus two RC-positive even densities can have a
positive mixture that is not RC-positive.  This also shows why pointwise
positivity in (2.1) cannot replace operator positivity in (2.5).

For the normalized Riemann density

\[
 \phi_\xi(t)=\frac{\Phi(t)}{\int_{\mathbb R}\Phi(u)\,du},       \tag{7.7}
\]

the remaining source problem is now exact:

\[
\begin{aligned}
 \Psi_\xi(r,q)
 &=\frac12\phi_\xi\!\left(\frac{r+q}{2}\right)
             \phi_\xi\!\left(\frac{r-q}{2}\right),\\
 M_\xi(r,q)
 &=\int_{|r|}^{\infty}v\Psi_\xi(v,q)\,dv,\\
 \mathfrak R_\xi(t,u)&=M_\xi(t+u,t-u).
                                                               \tag{7.8}
\end{aligned}
\]

A factorization

\[
 \mathfrak R_\xi(t,u)
 =\int_\Omega A(t,\omega)\overline{A(u,\omega)}\,d\nu(\omega)
                                                               \tag{7.9}
\]

with \(\nu\ge0\), or a Hilbert--Schmidt limit of convolution-positive
current kernels, would prove (0.4), and Theorem 4.1 would then prove RH for
all nontrivial zeros at once.  Positivity is closed under such kernel
limits because, for every \(f\in L^2\),

\[
 |\langle f,(K_n-K)f\rangle|
 \le \|K_n-K\|_{\mathrm{HS}}\|f\|_2^2.                \tag{7.10}
\]

## 8. Novelty and A/B audit

The ingredients used in the proofs--bilateral Laplace transforms,
integration by parts, positive integral kernels, Fourier uniqueness, and
Dirichlet Green functions--are standard.  The project-specific new object
is the nonlinear radial-current transform (2.1)--(2.3), together with:

1. the exact spectral-denominator removal (3.1);
2. the multiplicity-stable all-zero theorem (4.1) and the order-one exact
   equivalence (4.6);
3. the convolution Leibniz rule (5.3);
4. the rank-one and Green-kernel building blocks (6.4), (6.7).

These results create a zero-independent source-space mechanism capable in
principle of controlling the complete divisor.  What remains unproved is
the Riemann-specific membership statement
\(\mathfrak R[\Phi]\succeq0\).  The project has not independently
established literature priority for the transform, so a final success-B
claim is withheld pending novelty review and a second proof audit.  No
claim of a complete RH proof is made.