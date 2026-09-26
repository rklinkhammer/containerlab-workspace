# LIVE-002 — installed live interaction

**Observed:** an application extracted outside the repository loads a supplied YAML and explicit companions through pinned native APIs. GO/Stop, identity-bound observations and real node logs work. Selected-link capture automatically chooses one qualified Linux interface; there is no endpoint picker. PCAP filenames, capture/display filters, reviewed Lua, unchanged-byte download and same-artifact reanalysis work in actual installed browser trials. Approved revision-2 layout is retained; serial is explicitly unavailable.

## Verification and scope

| Evidence | Actual result |
|---|---|
| final-unit.log | 20 TypeScript tests + 9 Python checks pass |
| regression.log | 85 prior unit/contract tests pass |
| final-build.log | Typecheck and fixture-free frontend build pass |
| final-browser.log | Six mocked browser checks pass; not runtime evidence |
| installed-browser-results.json | Installed synthetic Linux pair: load, GO, real logs, capture, reviewed Lua, download, reanalysis, reconnect, Stop pass |
| installed-faults.json | Invalid filename refused, cancellation and artifact refusal after cancellation, Stop pass |
| four-radio-browser-results.json | Unchanged eight-node/seven-link project: all installed workflow stages pass after actual processor receive activity |
| official-installed-results.json | C042 and C043: native load, deployment, observation, logs and cleanup pass; capture explicitly unsupported for these SR Linux-only cases |
| package-verification.json | External archive payload hashes and absence of fixtures verified |

**Observed limits:** four-radio capture reached the size cap: 1,003,378 bytes, 100 displayed rows. Reanalysis returned two filtered rows, and download SHA256 matched the original. Synthetic ICMP capture was 252 bytes. Application-specific traffic counters are test preconditions only; production GUI contains no four-radio node/role/count assumptions and never infers application health from running containers.

**Observed fixes:** serialize bounded runtime calls to prevent observation/capture helper lock races; validate PCAP header/record bounds before publishing; preserve cancellation/identity/TTL; configure fresh Docker log rotation; expose identity-checked installed image import and runtime status/stop. Project snapshots capped at eight. Lima's ignore rule needs explicit wildcard guestIP, guestIPMustBeZero false, proto any and full range; earlier incomplete-rule logs remain preserved.

## Failed attempts and remaining gaps

First synthetic capture hit BUSY because polling shared the helper lock; fixed and rerun. First four-radio capture occurred before traffic and contained only a PCAP header; preserved as failed, then tested against a bounded actual receive-counter precondition. Startup and graph-render assertion races are preserved separately; readiness waits do not alter expected semantics. See attempt1-*, launch-race-* and render-race-* evidence.

**Unresolved/NOT_RUN:** serial transport; arbitrary Lua; all native-kind/link capture support; persistent/rotating captures; full corpus deployment; long-duration soak; app/runtime upgrade, resume and project removal; Apple Installer transaction, signing/notarization. pkgbuild still emits permission diagnostics while producing the package; archive extraction and per-file hashes are the tested install route. C023/C002 retain earlier native-only checks, not deployment claims. Runtime APT transitive versions are inventoried, not snapshot-pinned for future reproducibility. Source snapshots persist until explicit runtime retirement. No security certification or application-health claim.

**Observed cleanup:** qualification VM clab-app-c581a60705899c2f has no remaining lab containers and is stopped; qualification-stop.log and qualification-remaining-containers.txt record this. Its exact newly created runtime pointer was archived then removed. A separate new durable user runtime is documented in USER_RUNTIME.md; it is intentionally distinct from qualification cleanup.

TT-01, historical Q-gate results and the 177-case denominator remain unchanged. S-01/S-02/S-03/S-05/S-07 receive scoped boundary/identity/rendering/cancellation evidence only. B1/B2 native authority/version alignment and B4–B7 installed lifecycle, observation, logs/capture integration advance for these specific profiles.

## Reproduce

Developer checks: `npm run test:live`, `npm test`, `npm run build:live`, `node tests/live/browser.mjs`. These do not create VMs. Package: verified bundled Node and pinned native binaries, then `python3 packaging/build-live.py`. User commands and dependency closure are in packaging/README-LIVE.md and packaging/LIVE_DEPENDENCIES.md. Installed runtime tests require explicit `CLAB_INSTALLED_QUALIFY=LIVE-002` and an already provisioned, newly created qualification runtime; never point them at the user's continuous lab.

**Next:** use the installed GUI against the continuously running user lab and collect presentation feedback. Qualify restart/resume, retention/project retirement and long-duration resource behavior before claiming durable operation. Serial remains separately gated behind authoritative endpoint/native lifecycle qualification.

**Observed final installed candidate:** preview.6 user-runtime smoke passed native load, deployment, real logs, traffic precondition, capture, reanalysis, unchanged download and browser reconnect. The one-MiB capture cap was reached (1,003,556 bytes). Stop was intentionally NOT_RUN on the user runtime; qualification Stop passed separately. See user-browser-results.json. The inspected screenshot preserves approved layout; no new visual approval is required.
