## Round 139 — an exact weighted-mass identity on the ideal lattice, and the transfer theorem it demands

The source-faithful first variational problem has a sharper model calculation
than the unweighted local synthesis.  It does not prove RH, but it isolates a
concrete quantitative target for the actual critical ordinates.

Fix \(I_t=(-t,t)\) and use the ideal lattice
\(\Lambda_t=(\pi/t)\mathbb Z\), with
\(d_\lambda=\tfrac14+\lambda^2\).  Suppose a boundary-corrected relation has
the Section-10 form

\[
 \sum_{\lambda\in\Lambda_t}\frac{c_\lambda}{d_\lambda}e^{-i\lambda u}
 +\sum_{j=1}^m\frac{w_j}{d_{\eta_j}}e^{-i\eta_j u}
 =Ae^{u/2}+Be^{-u/2},
 \qquad u\in I_t,
\tag{139.1}
\]

where the \(\eta_j\) are a finite off-real packet and
\(c\in\ell^2(\Lambda_t)\).  Set

\[
 h(u)=Ae^{u/2}+Be^{-u/2}-
       \sum_{j=1}^m\frac{w_j}{d_{\eta_j}}e^{-i\eta_j u}.
\]

Because the lattice series has coefficients \(c_\lambda/d_\lambda\), it is
the periodic \(H^2\) Fourier expansion of \(h\); in particular its value and
first derivative have matching traces at \(-t\) and \(t\).  Apply the periodic
operator \(L=\tfrac14-\partial_u^2\).  It annihilates the two boundary modes,
and multiplies each exponential by its corresponding \(d\).  Therefore

\[
 \sum_{\lambda\in\Lambda_t}c_\lambda e^{-i\lambda u}
 =-\sum_{j=1}^m w_j e^{-i\eta_j u}
 \quad\text{in }L^2(I_t).
\tag{139.2}
\]

The lattice Parseval identity gives the exact equality

\[
 \boxed{
 \sum_{\lambda\in\Lambda_t}|c_\lambda|^2
 =\frac1{2t}\int_{-t}^{t}
   \left|\sum_{j=1}^m w_j e^{-i\eta_j u}\right|^2du .}
\tag{139.3}
\]

For one off-real exponential \(\eta=a+ib\), this becomes

\[
 \sum|c_\lambda|^2
 =|w|^2\frac{\sinh(2bt)}{2bt}>|w|^2
 \quad (b\ne0),
\tag{139.4}
\]

so a single packet already violates Bombieri's Section-10 negative-eigenvector
mass orientation (sum_{\mathrm{off}}|w_j|^2\ge\sum_{\mathrm{crit}}|c_\lambda|^2).
For symmetric packets the cross terms matter.  For example, the odd pair
(w(e^{-i(a+ib)u}-e^{-i(a-ib)u})) has critical/off-critical ratio

\[
 \frac{\sinh(2bt)}{2bt}-1,
\tag{139.5}
\]

which is below \(1\) for small \(t\) but grows without bound with \(t\).  More
generally, for every fixed nonzero finite off-real exponential polynomial, the
right side of (139.3) eventually exceeds the finite coefficient norm as
\(t\to\infty\): the term with largest positive imaginary part produces an
exponentially growing weighted \(L^2\) average after any exact leading-group
cancellation is removed.

Thus the ideal lattice model says that, under the finite-off-line hypothesis,
one can choose a sufficiently large interval and contradict the source mass
cone—provided the actual critical synthesis has the same weighted Parseval
control.

### Exact transfer gap for the real zero ordinates

Littlewood's eventual-mesh theorem plus Kadec can give an \(L^2(I_t)\) Riesz
subsequence after selecting suitably separated critical ordinates near
\(\pi n/t\).  This only controls that selected subsequence; it does not
control arbitrary coefficients on the full critical-zero set, whose gaps
eventually become arbitrarily small.  It only controls

\[
 \left\|\sum b_ne^{-i\lambda_nu}\right\|_{L^2(I_t)}^2
 \asymp \sum|b_n|^2.
\]

Bombieri's norm instead controls

\[
 \sum\left|\left(\tfrac14+\lambda_n^2\right)b_n\right|^2,
\tag{139.6}
\]

which is a weighted \(H^2\)-type coefficient norm.  An arbitrary bounded
Kadec perturbation does not, by the \(L^2\) theorem alone, identify this
weighted coefficient operator with \(\tfrac14-\partial_u^2\), nor does it
preserve the periodic trace calculation (139.2).  Finite replacements of the
Kadec tail create an additional finite-dimensional boundary correction.

The missing source-bearing theorem can therefore be stated explicitly:
construct a critical-zero selection and prove a weighted Sobolev/Riesz estimate
strong enough to transfer (139.3), or at least prove for every finite off-line
packet and some \(t\) that

\[
 \inf\left\{
 \sum_{\lambda\in\Gamma_C}|c_\lambda|^2:
 \sum_{\lambda\in\Gamma_C}\frac{c_\lambda}{d_\lambda}e^{-i\lambda u}
 =h(u)\text{ on }I_t
 \right\}
 >\sum_{j=1}^m|w_j|^2.
\tag{139.7}
\]

The ordinary Kadec theorem, dense range, and unweighted exact synthesis do
not imply (139.7).  This is the precise remaining quantitative/provenance
problem for the Bombieri route; it is not closed by the ideal-lattice identity.

**Established:** (139.3) is an exact source-normalized identity in the ideal
lattice model, and it gives a mass-cone obstruction for sufficiently long
intervals for any fixed finite off-real packet.

**Failure / missing transfer:** no theorem has been proved that transports the
weighted Parseval/Sobolev identity from the ideal lattice to the actual critical
zero ordinates selected by Bombieri, nor that the selected finite eigenvectors
use the minimum-cost representation in (139.7).

**Remaining load-bearing statements:** prove the actual weighted transfer and
finite-section provenance estimate; separately handle infinitely many off-line
zeros; only then infer RH from the global positivity/eigenvalue argument.

**RH status:** no unconditional proof has been produced.
