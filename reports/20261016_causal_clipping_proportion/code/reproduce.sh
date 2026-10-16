#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
python - <<'PY'
if not __debug__:
    raise RuntimeError('Run Python without -O or PYTHONOPTIMIZE')
import hashlib,json,pathlib
manifest=json.loads(pathlib.Path('PACKAGE_MANIFEST.json').read_text())
for rel,expected in manifest['files'].items():
    p=pathlib.Path('..')/rel
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got!=expected: raise RuntimeError(f'Hash mismatch: {rel}')
PY
python certify_cubic_window_gain.py --input certified_window_data.json --bits 256 --output scalar_reproduced_256.json
python certify_cubic_window_gain.py --input certified_window_data.json --bits 384 --output scalar_reproduced_384.json
