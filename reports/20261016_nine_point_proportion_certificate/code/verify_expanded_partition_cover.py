#!/usr/bin/env python3
"""Independently replay untrusted binary split trees; no author inequalities."""
import json, itertools, hashlib, pathlib, sys
D=pathlib.Path(__file__).parent
src=D/'attempt024_partition_expanded.trees.json'
trees=json.loads(src.read_text())
assert trees['source_scale']==32768
roots=trees['roots']; assert len(roots)==48
rootboxes=[tuple(map(tuple,r['gap_bounds'])) for r in roots]
assert len(set(rootboxes))==len(roots)
intervals=[sorted(set(b[i] for b in rootboxes)) for i in range(8)]
assert set(rootboxes)==set(itertools.product(*intervals))
assert all(0<=a<b for ints in intervals for a,b in ints)
# All source-coordinate gaps are independently recorded for the new-kernel
# checker to compare against its own exact precover, not the old precover.
(D/'expanded_partition_coordinate_cover.txt').write_text('\n'.join(str(len(v))+' '+' '.join(f'{a} {b}' for a,b in v) for v in intervals)+'\n')
def close(d):
 for k in range(9):
  for i in range(9):
   for j in range(9):
    d[i][j]=min(d[i][j],d[i][k]+d[k][j])
 return d
out=[];splits=0;terminals=0;empty=0
for root in roots:
 d=[[0 if i==j else 10**9 for j in range(9)] for i in range(9)]
 for i,(a,b) in enumerate(root['gap_bounds']):d[i][i+1]=b;d[i+1][i]=-a
 close(d);tokens=root['tokens'];pos=0
 def visit(d,depth):
  global pos,splits,terminals,empty
  assert depth<200 and pos<len(tokens)
  token=tokens[pos];pos+=1
  if token[0]=='B':
   _,i,j,q,*_=token;assert 0<=i<j<=8 and isinstance(q,int)
   splits+=1
   left=[r.copy() for r in d];left[i][j]=min(left[i][j],q);close(left)
   right=[r.copy() for r in d];right[j][i]=min(right[j][i],-q);close(right)
   visit(left,depth+1);visit(right,depth+1)
  else:
   assert token[0]=='L';terminals+=1
   if any(d[i][i]<0 for i in range(9)):empty+=1;return
   # ceil(d/2) gives an outward upper for each directed difference.
   rounded=[[ -((-d[i][j])//2) for j in range(9)] for i in range(9)]
   close(rounded);assert all(rounded[i][i]==0 for i in range(9))
   out.append((root['root'],rounded))
 visit(d,0);assert pos==len(tokens)
p=D/'verified_expanded_partition_cells.txt'
with p.open('w') as f:
 f.write(str(len(out))+'\n')
 for rid,d in out:f.write(str(rid)+' '+' '.join(map(str,sum(d,[])))+'\n')
result={'status':'COMPLETE_BINARY_COVER_ONLY_NO_KERNEL_INEQUALITY','roots':len(roots),'splits':splits,'terminals':terminals,'empty':empty,'outward_cells':len(out),'tree_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'verifier_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'cells_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(D/'verified_expanded_partition_cover.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
