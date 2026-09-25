#!/usr/bin/env bash
set -euo pipefail
: "${CLAB_SESSION_DIR:?Set the newly created task session directory}"
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
export CLAB_CAPACITY_EVIDENCE_DIR="$PWD/experiments/EXP-025-reliability"
cleanup() {
  local original=$?
  trap - EXIT INT TERM
  python3 experiments/EXP-024-consolidation/cleanup.py > "$CLAB_CAPACITY_EVIDENCE_DIR/cleanup.log" 2>&1 || { printf 'Cleanup failed: see cleanup.log\n' >&2; exit 1; }
  exit "$original"
}
trap cleanup EXIT INT TERM
node experiments/EXP-025-reliability/run.mjs
