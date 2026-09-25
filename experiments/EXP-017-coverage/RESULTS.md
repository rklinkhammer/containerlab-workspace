# EXP-017 — approved coverage expansion

**Observed:** 14 additional bundles qualified for outcomes (11 graphs, three native rejections), 23 total approved. See [A12 results](../../artifacts/implementation/A12/RESULTS.md) for scope, preserved failures and limitations. Historical Q gates and denominator 177 unchanged.

- [Plan](PLAN.md), [original oracle](expectations.json), [native dispositions](native-dispositions.json), [source ledger](source-ledger.json), [bundle origins](bundle-origins.json).
- [First attempt: 12/14](integration-attempt1.log), [second outcome attempt: 14/14](integration-attempt2.log), [per-case outcomes and hashes](case-results.json). Original malformed-brief graph expectation remains unmet, not silently changed.
- [Contracts](contracts-final.log), [build](build-final.log), [A11 regression](regression.log), [18 supervisor checks](worker-checks.json), [live browser](browser-live.log), [offline browser](browser-offline.log).
- [Runtime profile](runtime-profile.json), [pre-stop cleanup](cleanup-prestop.json), [stopped VM](final-vm.json). No existing VM or container operations.

To repeat supervisor checks only in a session just created for the trial:

```sh
python3 - <<'PYCODE'
import json, subprocess
vm=json.load(open('.runtime/native-session.json'))['vm']
subprocess.run(['limactl','copy','tests/integration/worker_qualification.py',vm+':/tmp/worker_qualification.py'],check=True)
subprocess.run(['limactl','shell',vm,'sudo','python3','/tmp/worker_qualification.py'],check=True)
PYCODE
python3 scripts/native-session.py stop
```

Setup uses the unchanged EXP-016 pinned image/build recipe and explicit fresh-session helper. Build networking is allowed; worker networking is denied. Utility apt packages are not fully hermetic. Ordinary checks never start a VM.
