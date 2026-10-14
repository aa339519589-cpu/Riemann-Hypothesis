#!/usr/bin/env python3
"""Exact constants for the full same-star Mobius boundary angle."""
from fractions import Fraction as F
import json
c1=F(401,160000)
c2=F(401,76800)
assert F(1024,20**15)<F(1,10000)
assert c1<c2<F(1,190)
assert F(1)-F(101,190)==F(89,190)>0
assert F(1)+F(101,190)==F(291,190)
print(json.dumps({'first_cross_constant':str(c1),'second_cross_constant':str(c2),
 'all_edge_bound':'1/190','complete_boundary_bound':'101/190',
 'boundary_Gram_lower_factor':'89/190','status':'all exact checks passed'},sort_keys=True,indent=2))
