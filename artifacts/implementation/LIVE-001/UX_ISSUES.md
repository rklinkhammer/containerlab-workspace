# User-task issues

| Intended action | Actual behavior / issue | Change / retest |
|---|---|---|
| Launch own YAML, without example chooser | Old package ships examples | Separate production entry and fixture-free candidate; archive verified. Installed launch pending. |
| See selected-node logs / eventual serial | Revision 1 placed output ambiguously | Revision 2 approved; wide bottom output pane; mocked browser passes. |
| Capture selected link | Old UI requires endpoint selection | New form has no endpoint picker; backend resolver unit-tested. Live capture integration remains pending. |
| Stop after a failed lifecycle operation | Native generated files invalidated source inventory | Use native CLAB_LABDIR_BASE; repeated actual deployment/logs/restart/Stop pass. |
| Use requested local port | Existing preview occupies 4173 | Leave process untouched. Await free port for installed browser acceptance. |
| Install and operate continuously | Candidate core implemented; durable provisioning unqualified | Finish capture, provisioning/image acquisition and installed E2E before readiness claim. |
