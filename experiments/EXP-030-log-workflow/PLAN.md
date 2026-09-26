# Phase3 independent expectations

Existing A23 node-logs/0.1 remains the fixed100-line/64KiB bounded backend; no transport changes needed. Frontend gaps: no local literal filter/tail view/clear, incomplete reason messages, identity errors leave runtime bound, abort could accept a late response.

- Local last25/50/100 line views followed by bounded case-insensitive literal filtering. Never regex, semantic telemetry parsing or extra backend options. Distinguish empty fetched output from zero matches. Preserve truncation warning.
- Clear cancels follow/read and removes output. Stop retains labeled last-fetched output; node/session/tab switches remove old output and view settings.
- Known unsupported/unqualified/expired/malformed states are explained; manual retry supports transient recovery. Identity conflict/session expiry invalidates runtime and selection, cancels output; reconnect requires matching enrollment.
- Aborted/late replies cannot repopulate cleared state. Hostile text remains text; filter contents are never commands and never persisted.
- Verify existing unit/native static checks plus browser filter/tail/clear/follow/unsupported/empty/replacement/cancellation/recovery. Separate mocked evidence from historical actual Linux A23 evidence. No new Q gate pass or VM access.
