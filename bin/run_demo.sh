#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PYTHONPATH=src python3 -m ai_test_factory \
  --input examples/cluster_time_loss/input.txt \
  --output outputs/cluster_time_loss
