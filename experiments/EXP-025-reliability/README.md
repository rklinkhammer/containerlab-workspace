# Explicit finite reliability trial

Read PLAN.md and expectations.json before execution. Run from the workspace root on the pinned macOS/Lima profile. Build first with the README commands. Ordinary tests never create a VM.

```sh
export CLAB_SESSION_DIR="$PWD/.runtime/exp025-new-unique-name"
export CLAB_OBSERVATION_PROFILE=CAPACITY-MAX
python3 scripts/observation-session.py create
bash experiments/EXP-025-reliability/execute.sh
python3 experiments/EXP-025-reliability/summarize.py
```

Never point the script at a prior VM/session, including a stopped one. The `create` workflow requires a new directory. Creation must finish before execute. Execute requires at least35 minutes remaining in the existing session lease and refuses an occupied4173; it does not extend leases or terminate an unrelated listener. The full browser window is1800 seconds, plus baseline/native samples and bounded fault phases.

`execute.sh` installs an EXIT/INT/TERM cleanup trap, using the existing EXP-024 exact-lab cleanup. It preserves the runtime command's exit status and treats cleanup failure as failure. Setup has its own failure cleanup. If interrupted outside the shell's catchable signals, inspect the exact task manifest and execute scoped cleanup:

```sh
export CLAB_CAPACITY_EVIDENCE_DIR="$PWD/experiments/EXP-025-reliability"
python3 experiments/EXP-024-consolidation/cleanup.py
```

The qualification harness temporarily replaces only the new VM's native executable with the existing EXP-024 fault shim, restores it and verifies its pinned hash. No application fault route or modified native binary ships in the application. The backend/browser use current source and `dist`; do not rebuild or edit application code during the healthy window.

Raw per-request snapshots, errors, resource samples, warmup and process-fault evidence are retained in timestamped attempt directories. Independent topology expectations come unchanged from EXP-024. Each attempt writes its own local evidence. The wrapper's create/cleanup console redirection filenames should be unique on subsequent reproductions; preserve existing evidence before repeating, rather than overwriting previous logs.

A real browser offline/reconnect and SIGTERM/restart phase is distinct from test-file expiry/format sentinels and injected native subprocess delays. This finite single-profile trial does not establish long-term availability, arbitrary shapes, packet forwarding or continuous identity.
