"""Check the exact scientific outputs required by the pinned verifier."""
import pathlib,hashlib
D=pathlib.Path(__file__).resolve().parent
expected={
 'candidate_am_kernel.u32le':'97c3b113c7c3be7030406984972794cceb1591e533ee26a541531c2acc9850e5',
 'candidate_am_jets.i64le':'4227017a8bd49a500fa5a420c360308e1b202a019d172451bdf218d1749efb31',
 'verified_expanded_partition_cells.txt':'c4ff4ded6568430b0ede46d6308f56b2e04a66f9a8c5f3c8ddc2b6acf1361425',
 'expanded_partition_coordinate_cover.txt':'41528c1a6198fd7e2e1003067618765e96aab73dc057b44c3d9f80e693058033',
 'expanded_partition_anchor_proposals.txt':'1032722f512045bba7cc4691f8d00cc178aa977ff0405033437850fa611e153c'}
for n,h in expected.items():assert hashlib.sha256((D/n).read_bytes()).hexdigest()==h,n
print('GENERATED_SCIENTIFIC_BYTES_PASS')
