#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/tools/use_toolcache.py"
printf 'Ready. Run: source .tools/env.sh\n'
