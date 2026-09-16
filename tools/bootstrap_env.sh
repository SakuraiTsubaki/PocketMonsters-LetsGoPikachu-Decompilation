#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
export PROJECT_ROOT="$ROOT_DIR"
BOOTSTRAP_COMMIT="04a26bf4c5d233eefb678a266def3ba5bc2a92bd"
BOOTSTRAP_URL="https://raw.githubusercontent.com/SakuraiTsubaki/Sakurai/${BOOTSTRAP_COMMIT}/tools/bootstrap_env.sh"
TMP_FILE="$(mktemp)"
trap 'rm -f "$TMP_FILE"' EXIT
curl --fail --silent --show-error --location "$BOOTSTRAP_URL" --output "$TMP_FILE"
bash "$TMP_FILE"
