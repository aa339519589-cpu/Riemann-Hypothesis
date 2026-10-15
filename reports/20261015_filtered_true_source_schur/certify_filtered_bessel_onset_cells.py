"""Validated extra onset cells for the complete mixed-head evaluator."""
import json,os
import certify_filtered_bessel_moments as c
lo=c.iv.mpf(1600001)/100000;hi=c.iv.mpf(16001)/1000
vals=c.integrate(lo,hi,2,[0])
out={'scope':'extra onset interval for complete mixed-head source representation','cells':c.CELL_DATA}
p=os.path.join(os.path.dirname(__file__),'filtered_bessel_onset_cells.json')
with open(p,'w') as f:json.dump(out,f)
print('SUCCESS onset cells',len(c.CELL_DATA),'full mass',vals[c.J])
