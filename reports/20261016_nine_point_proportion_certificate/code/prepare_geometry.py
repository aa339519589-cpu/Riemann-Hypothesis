"""Unpack untrusted binary-tree/anchor proposals; prove coverage separately."""
import gzip,hashlib,json,pathlib
D=pathlib.Path(__file__).resolve().parent
raw=gzip.decompress((D/'partition_hints.json.gz').read_bytes())
assert hashlib.sha256(raw).hexdigest()=='b34f0477ea5c93941db1f488bb606385a91e9c402aceaf1ddedf0dab314aad70'
(D/'attempt024_partition_expanded.trees.json').write_bytes(raw)
p=json.loads(raw);assert p['source_scale']==32768
pairs=p['anchor_term_pairs'];assert len(pairs)==34 and p['anchor_lambda_denominator']==1024
rows=[t[-1] if len(t)>4 else None for r in p['roots'] for t in r['tokens'] if t[0]=='L']
assert len(rows)==10750
with (D/'expanded_partition_anchor_proposals.txt').open('w') as f:
 f.write(str(len(rows))+' '+str(len(pairs))+'\n')
 f.write(' '.join(str(v) for pair in pairs for v in pair)+'\n')
 for row in rows:
  if row is None:f.write('0\n');continue
  assert len(row)==34 and all(len(a)==4 and all(isinstance(v,int) for v in a) for a in row)
  f.write('1 '+' '.join(str(v) for a in row for v in a)+'\n')
assert hashlib.sha256((D/'expanded_partition_anchor_proposals.txt').read_bytes()).hexdigest()=='1032722f512045bba7cc4691f8d00cc178aa977ff0405033437850fa611e153c'
print('UNTRUSTED_HINTS_UNPACKED; no local inequality accepted')
