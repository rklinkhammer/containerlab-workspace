# Containerlab GUI

The current focus is an installed application and persistent interactive lab workflow. Serial investigation is preserved at A32 and deferred.

The first **macOS ARM64 GUI preview** is packaged and installed independently of the checkout. It currently supports recorded examples; it does **not** yet provision or monitor a persistent lab. [Install/launch guide](packaging/README.md) · [Dependencies](packaging/DEPENDENCIES.md) · [Actual results](artifacts/implementation/INSTALL-001/RESULTS.md).

For the installed user-level copy:

```sh
APP="$HOME/Applications/Containerlab GUI.app/Contents/Resources"
"$APP/runtime/node" "$APP/packaging/cli.mjs" doctor
"$APP/runtime/node" "$APP/packaging/cli.mjs" serve --open
```

Use the browser at http://127.0.0.1:4173. Ctrl-C stops the foreground GUI. No repository/npm/build is required to run this installed copy. The package is an unsigned local preview; the user-level install was tested, the alternative `.pkg` Installer transaction was not.

The next acceptance target is the complete existing four-radio example running continuously in a newly created owned runtime, with live observation/logs and supported capture/reanalysis from the installed GUI. It has eight native nodes. Its topology/application details must stay out of generic GUI code. [Implementation sequence and acceptance](artifacts/design/INSTALLED_WORKFLOW.md).

## Development

```sh
npm ci
npm test
npm run build
npm run test:browser
npm run preview
```

Development checks do not create VMs. Reproduction of older experiments requires their explicit scoped workflows; stopped trial VMs must never be reused. Historical README/design sets are preserved under artifacts/design/history; current architectural state is in [the handoff](IMPLEMENTATION_HANDOFF.md) and [design index](artifacts/design/README.md).
