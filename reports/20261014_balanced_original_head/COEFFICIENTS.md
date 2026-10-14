# Certified sine coefficients and high tails of the exact balanced head loads

Use the EXACT loads l_U and l_V from
[CALIBRATION.md](CALIBRATION.md), with
calibration defined by its matrix inverse, not rounded coefficient values.
The corresponding independent calibration data have SHA-256
89d93cde94b0aef5219edcf192f45cfbc3d459ebb9330fe2a3b7f2a81c13026b.
In particular l_V already includes the factor 5/787.

For b=log2 and e_k=sqrt(2/b)sin(k*pi*x/b), define

    u_k=integral_0^b l_U(x)e_k(x)dx,
    v_k=integral_0^b l_V(x)e_k(x)dx.

The interval checker proves:

    |l_U(0)|+integral_0^b |l_U'| <3.542886632,
    |l_V(0)|+integral_0^b |l_V'| <6.722937823.          (1)

The right endpoint contributions are EXACTLY zero by the calibration.
Consequently, for every k>=1,

    |u_k|<1.327808/k<2/k,
    |v_k|<2.519632/k<3/k,                             (2)
    sum_(k>48)|u_k|^2<=4/48,
    sum_(k>48)|v_k|^2<=9/48.                         (3)

Each of the first 48 coefficients is enclosed in
the generated balanced_head_coefficients.json, with
radius less than 10^(-6). Both vectors use the displayed orthonormal basis.
The complete calibration interval uncertainty is propagated, not suppressed.

The executable proof is
[certify_balanced_head_coefficients.py](certify_balanced_head_coefficients.py).
This certificate supplies only the two load vectors and their high tails.
It does not by itself assert positivity of a finite Schur matrix, the
original head form, the mixed head/tail remainder, or RH.

## 1. Complete derivatives, including the removable origin ratio

The polynomial ladder, exact divisor regrouping and Gaussian tail argument
are those in the calibration proof. Here the ordinary theta ladder is used
through order 28 and the mirrored row through order 10. The checker verifies
complete omitted-tail bounds 10^(-220) beyond ordinary label16 and10^(-260)
beyond mirrored label32, on the slightly enlarged interval [0,.7]. The
coefficient-l1 recurrence and geometric ratios are checked for every order.

For 0<=x<=1/50 use

    H_j=psi^(j)/x, j=0,2,4,6,
    H_j(x)=sum_(r even, 0<=r<=20)
                  psi^(j+r+1)(0)x^r/(r+1)!+remainder.

For the kth derivative, k<=4, the exact Taylor remainder is bounded by

    sup_(0<=y<=1/50)|psi^(j+22)(y)|/22
                          *x^(21-k)/(21-k)!.

This follows from H_j^(21)=integral_0^1 t^21 psi^(j+22)(tx)dt.
Thus the neutral ratios psi^(2j)/psi=H_(2j)/H_0 are evaluated without an
uncontrolled zero-over-zero operation. Outside this interval use the direct
positive theta denominator. The full load derivatives then use the exact
identity n_j=2[L psi^(2j)/psi-F_r psi^(2j)]. The 4^(-j) subtractions have
already canceled because Wpsi=0.

## 2. Whole-box variation bounds, improved only by the mean-value theorem

Split 1024 equal boxes of [0,b] once more at x=1/50. On every whole box,
the checker encloses both loads and their first four derivatives using the
interval ladder, quotient derivative recurrence and product rule. It also
encloses the first derivative at the exact interval midpoint. For either
load l, the box derivative upper bound is the smaller of the two VALID bounds

    sup_box |l'| <= direct interval bound,
    sup_box |l'| <= |l'(mid)|+(length/2)sup_box |l''|.  (4)

The midpoint is not substituted for the derivative supremum: its entire
mean-value remainder in (4) is retained. Multiply these upper bounds by the
exact interval box lengths and add the left endpoint enclosure. The exact
right endpoint zero gives (1). In particular the reported variation fields
are upper-bound enclosures, not enclosures of the exact variation itself.

All interval arithmetic uses mpmath.iv at 50 decimal digits. Converted float
endpoints or absolute upper bounds are expanded outwards by nextafter. The
calibration coefficients are read as intervals from the independently
validated JSON; its hash is recorded in the output. No midpoint-only
calibration enters any subsequent arithmetic.

## 3. The first 48 coefficients

Composite Simpson integration uses 2048 subintervals. Function and sine
values are intervals, and the exact angle k*pi*i/2048 is used. If M_j bounds
sup|l^(j)| on [0,b], the uniform error for all k<=48 is

    sqrt(2/b)*b/180*(b/2048)^4
           *sum_(j=0)^4 binom(4,j)M_j(48*pi/b)^(4-j).

Its upper endpoints are less than 5.074e-7 for l_U and9.054e-7 for l_V.
Adding these signed remainder intervals to the full interval Simpson sums
produces the output enclosures, all of radius less than10^(-6). Input
calibration uncertainty remains inside the sums.

Finally integration by parts gives

    |integral_0^b l e_k|
      <=sqrt(2b)/pi * [|l(0)|+|l(b)|+integral|l'|]/k.

Using (1), l(b)=0 and the outward interval normalization proves (2).
The integral comparison sum_(k>48)1/k^2<=1/48 proves (3), including the
whole infinite high tail.

## 4. Replay order

    python certify_balanced_head_loads.py
    python certify_balanced_head_coefficients.py

The first script regenerates the exact calibration enclosures; the second
records their SHA-256 and regenerates the sine/variation enclosures. The
proof rests on the complete analytic tails, whole-box derivative bounds and
quadrature remainder assertions, not on point sampling or an unexplained
finite cutoff.
