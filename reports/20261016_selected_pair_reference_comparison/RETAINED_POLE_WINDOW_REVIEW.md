# Independent internal review of the retained-pole addendum

Date: 2026-10-16.

The complete `RETAINED_POLE_WINDOW_ADDENDUM.md` was read and checked.
The reviewed SHA256 is

    0baac45b04d75accce68915ae77b620c4364d4355fc85906e9ca6702298fbf12

1. With both grounds normalized, the retained cross pole has exactly
   the coefficient 8 and the three terms displayed in (3). The complete
   cross upper bound uses D_v>=0, B_v<=A_v, reflection Cauchy and
   0<delta<1. It does not impose a sign on C_v.

2. The two weighted Cauchy inequalities use their respective normalized
   grounds. Completing the scalar square gives (6), and ell(q)>=ell(e)^2
   gives the simpler bound (7). The absence of an explicit delta^(-1)
   factor is correct; uniformity over source-dependent quantities is
   not claimed.

3. The shifted-Phi seed normalization and uniform full-prime bound are
   those of the report. On sufficiently far unit windows, s v_z has a
   fixed positive lower bound. This proves the ratio L2 estimate without
   dividing by a=e/psi or assuming its plateau is nonzero. All windows
   touching the wall are expressly excluded.

4. The exact difference C_z-D_z is an absolutely defined old-current
   pairing. Translation-bounded L1 of p follows from the new tail L2
   estimate plus the fixed interior reciprocal budget. The envelope
   exp(t/2)Phi(t) has summable unit-bin suprema, which pays the entire
   moving tail against the existing normalized little-o of W_psi g.

5. The compact and physical-wall pieces of this limit were checked
   separately. The proof uses integral x|p|<infinity and uniform
   v_z(x)/x->0, not ordinary wall L1 or L2 of p. No decay rate for the
   original current is obtained from this passage.

6. The full PNT normalization in (18) is correct: the bilateral
   exp(t/2)Phi(t) integral is 1/2 and the prefactor is asymptotic to
   4exp(-z/2). The second shifted branch vanishes. Uniform Chebyshev
   domination and U(q)<infinity then give A_z->2U(q), including every
   proper prime power.

7. The complete cross identity gives limsup D_z<=2U(q) with its full
   remainder retained. In the zero-plateau case, the additional factor
   a makes D_z->0; the wall part is paid by q L(v_z/psi), and C_z->0
   follows from the already proved difference limit. These are linear
   pairing limits, not square bounds for the old current.

No mathematical correction is requested. The frozen original report
and its review are not altered by this separately labeled addendum.
This is an independent internal mathematical review, not an external
referee report or institutional endorsement. The original RH comparison,
ordinary wall L2 of e/h, pointwise ground lower bounds, signed feasible
variations and reverse IMS signs remain outside the proved scope.
