# Candidate refresh qualification

**Observed:** overlay-extracting the updated candidate onto its previously executed app
caused bundled Node to exit with SIGKILL 9, although every manifest hash matched.
The failed candidate is preserved outside Git under `.runtime-live-release/overlay-candidate-app`.
Fresh extraction into a new app directory passed external-CWD doctor. Existing user
installation was untouched. `package-overlay-attempt.json` retains the failure.

**Unresolved:** macOS executable replacement/signature caching is a hypothesis, not a
confirmed root cause. In-place upgrades are not qualified. The shipped install script
refuses overwrite; do not bypass it by overlay extraction. The final archive and expanded
pkg payload match all 914 manifest entries. Installer transaction/signing/notarization
remain unrun; pkgbuild permission diagnostics remain unexplained.
