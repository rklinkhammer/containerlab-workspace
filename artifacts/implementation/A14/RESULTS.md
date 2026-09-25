# A14 — controlled native interface observation

**Observed:** the GUI now shows left/right eth1 observations alongside declared node/link inspectors. The native CLI supplies operational state, MAC and namespace-local index. Full container IDs, source/deployment identity and enrolled namespace/index/MAC attributes guard association. Admin state, carrier, peer, continuous interface identity and link health stay unknown. This is integration risk reduction for one Linux-veth lab, not a network correctness or 177-case fidelity result.

## Verification by stage

| Stage | Actual evidence and outcome |
|---|---|
| Native transitions and projection | One real integration test passed: initial up, admin down/up with native oper-state change, veth removal, same-name recreation, node stop/start, cancellation, lab removal and full-ID replacement rejection; per-step DTOs preserved in EXP-019 attempt directory |
| Contracts | 39 tests passed; attribute changes, duplicate/foreign IDs, absence versus unavailable, partial outcomes and strict allowlists |
| Build | TypeScript and production build passed; existing use-client and >500kB bundle warnings retained, no dependencies added |
| Guest subprocess safeguards | Four injected subprocess cases passed: malformed JSON, output limit, nonzero exit, six-second timeout; child processes reaped. These are fault seams, not native-runtime failures |
| Guest association faults | Six mock cases passed: partial failure, namespace race, container race, ambiguous eth1, >64 interfaces, omitted node group; right endpoint remains visible and canary excluded |
| Live Chromium | Targeted interface test passed. Full suite:23 passed/1 offline-only skip; actual native down/up and node stop/start, selection retention and narrow layout included |
| Offline Chromium | 20 passed/5 runtime-dependent skips (25 cases); includes new endpoint-absence/replacement/staleness transport mock. This extra mock was added after the 24-case live run |

**Observed preserved failures:** the initial short-name native filter yielded no interface group and correctly produced unavailable. Pinned WithListNodeName inspection identified the required native long name; implementation corrected and explicit enrollment now requires actual endpoints. `initial.json` preserves the first result. The first full browser run was22 passed/1 failed/1 skipped because the next test hit the intentional one-second backend rate limit. Added test spacing; no safeguard weakened. `browser-live.log` and `browser-initial-failure.md` preserve it; `browser-live-final.log` records correction. The default session-create refusal is also preserved: an existing session was left untouched and a separate task session directory used.

**Observed cleanup:** only task VM `clab-load-20260925-100311-exp016` was used. Native lab destroy completed, observer returned an empty successful inventory, Docker container list was empty, then the VM was stopped. Task session manifests removed. Pre-existing default session manifest hash is unchanged; its VM was not accessed. See EXP-019 cleanup.json, lab-cleanup.json and stop.log.

**Unresolved / NOT_RUN:** universal corpus and non-Linux/alias/stitch/guest associations; exact-attribute interface reuse; real concurrent namespace race/partial daemon fault (mock only); admin/carrier/peer export; packet forwarding, routing and capture; shared/durable deployment, Firefox/WebKit and manual assistive-technology audit. No Q-gate promotion. Sequential before/after guards do not prove atomicity. No new npm audit was run: dependencies and lockfile unchanged.

## Reproduction

See root README for fresh-session commands. `npm ci`, `npm run test`, `npm run build`, `npm run test:browser` require no VM. Explicit `CLAB_SESSION_DIR=.runtime/exp019 python3 scripts/observation-session.py create` creates a **new** VM and only the approved synthetic lab. Use both task session environment paths with preview on4173. Stop preview before Playwright binds the port. Use separate freshly created trials for live browser checks and destructive `npm run test:interfaces`; both mutate test state and the latter intentionally leaves old enrollment invalid. Run scoped stop after each; never reuse a stopped trial or auto-adopt replacement IDs. Operator re-enrollment during this qualification was explicit and recorded, solely to run regressions after destructive trials.

## Next gated step

**Inferred:** qualify the smallest native-supported administrative/carrier/peer and continuity evidence needed for reliable endpoint correlation, starting with the same controlled lab and a written capability contract. Keep unavailable fields unknown if the pin cannot supply them; do not build a traffic framework to manufacture link health. Broader kinds and any capture/action targeting require independent association qualification. This slice does not authorize those later operations.
