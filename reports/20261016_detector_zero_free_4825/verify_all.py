"""Regenerate all changed-detector certificates; the base theorem is cited separately."""
from pathlib import Path
import json,subprocess,sys
base=Path(__file__).resolve().parent
for n in ['certify_detector_prime.py','certify_detector_gamma.py','certify_detector_scalar.py']:
    subprocess.run([sys.executable,str(base/n)],cwd=base,check=True)
assert json.loads((base/'detector_scalar_4.825.json').read_text())['status']=='PASS'
print('ALL CHANGED-DETECTOR CERTIFICATES PASS')
