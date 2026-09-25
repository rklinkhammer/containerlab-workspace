# EXP-016 — on-demand qualification results

**Observed:** nine approved bundles execute through the new native declaration worker; 18 supervisor checks and independent fixture comparisons pass. The new dedicated VM is stopped. No pre-existing VM or deployed lab was used.

See [complete A11 report](../../artifacts/implementation/A11/RESULTS.md), [live results](live-results.json), [native integration](integration.log), [worker checks](worker-checks.json), [live verification](verify-live.log), [offline verification](verify-offline.log), [cleanup](cleanup-prestop.txt) and [final VM state](final-vm.json).

No Q-gate status changes. Only approved public/synthetic bundles are qualified. Current image/native/toolchain pins are in lima.yaml and build.sh; source projection uses the unchanged native APIs qualified in EXP-015.
