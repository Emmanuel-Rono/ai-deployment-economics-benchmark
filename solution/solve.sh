#!/usr/bin/env bash
set -euo pipefail
python3 "$(dirname "$0")/solve.py" --data /workspace/data --output /workspace/output
