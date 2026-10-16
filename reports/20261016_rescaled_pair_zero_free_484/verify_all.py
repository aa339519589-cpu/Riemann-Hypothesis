"""Rebuild every finite certificate. Search/optimization is not invoked."""
from pathlib import Path
import subprocess,sys,json
base=Path(__file__).resolve().parent
for name in ['certify_rescaled_packet.py','certify_bty_analytic_constants.py','certify_rescaled_prime_packet.py','certify_rescaled_archimedean.py','certify_rescaled_zero_pairs.py','certify_bty_rescaled_unconditional.py','certify_bty_rescaled_margin.py']:
    print('RUN',name,flush=True)
    subprocess.run([sys.executable,str(base/name)],cwd=base,check=True)
    if name == 'certify_bty_rescaled_unconditional.py':
        assert json.loads((base/'bty_rescaled_unconditional_4.84.json').read_text())['status'] == 'PASS'
    if name == 'certify_bty_rescaled_margin.py':
        assert json.loads((base/'bty_rescaled_margin_4.795.json').read_text())['status'] == 'PASS'
print('ALL FINITE CERTIFICATES PASS. Analytic proof and external theorem inputs are separate requirements.',flush=True)
