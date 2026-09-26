# Build and use the installed GUI

Current milestone:0.2.0-preview.1, Apple Silicon macOS. Installed GUI and recorded examples work independently of the repository. Persistent runtime deployment is not implemented by this package. Do not mistake the recorded example for a running lab.

## Install and launch

The user-level archive includes `Containerlab GUI.app` and `install.command`. Extract to a temporary directory, run install.command, then discard the extracted directory. The installer refuses to overwrite an existing app. It installs under `~/Applications`, with no administrator access or startup hooks.

Launch from Finder, or use the bundled CLI in a terminal:

```sh
APP="$HOME/Applications/Containerlab GUI.app/Contents/Resources"
"$APP/runtime/node" "$APP/packaging/cli.mjs" doctor
"$APP/runtime/node" "$APP/packaging/cli.mjs" serve --open
```

The browser opens http://127.0.0.1:4173. Ctrl-C stops a terminal-launched GUI; no VM or lab is started/stopped. For this preview, a Finder-launched background server can be quit through Activity Monitor by its Node process; a convenient installed application stop/status workflow is tracked for the next increment. Do not kill unrelated Node processes. Prefer terminal launch during the preview review.

The alternative `.pkg` installs the app under `/Applications` and `/usr/local/bin/containerlab-gui`; use `containerlab-gui doctor` and `containerlab-gui serve --open`. The `.pkg` builds successfully but a macOS Installer transaction was not run. Both artifacts are unsigned local previews, not signed/notarized distribution releases. Do not disable Gatekeeper or SIP.

No npm/build/checkout is required on the target. No session manifests, captures, private state, test dependencies or experiment archives are shipped. The installed launcher deliberately excludes old experimental sessions. Missing runtime capabilities stay unavailable.

## Build prerequisites and commands (developers only)

Node26.8.1/npm, locked build dependencies, Python3, macOS pkgbuild/otool, curl/TLS and tar. Fetch the pinned official Node archive, verify its SHA256, and extract into the build cache; build.py verifies it again:

```sh
npm ci
npm run build
mkdir -p .runtime-release/node
curl --fail --location https://nodejs.org/dist/v26.8.1/node-v26.8.1-darwin-arm64.tar.gz -o .runtime-release/node.tar.gz
# Expected SHA256:6e577fd0d9db776db82306629e441a9dace416702622aebdd171c9dfaa41f4d2
shasum -a 256 .runtime-release/node.tar.gz
tar -xzf .runtime-release/node.tar.gz -C .runtime-release/node --strip-components=1
python3 packaging/build.py
```

Artifacts and SHA256SUMS appear under `.runtime-release/`. Build inputs are pinned but archive timestamps/package metadata mean byte-for-byte rebuild reproducibility is not claimed. Generated manifests identify each output. Runtime Node links only system libraries, verified with otool. DEPENDENCIES.md separates bundled, host, Linux runtime and example-image requirements. `packaging/smoke.py` tests an already installed user-level copy; it does not install or create VMs and requires4173 free. Its browser harness uses developer Playwright, which is not an application dependency.

Uninstall this user-level preview only after stopping its own server: remove the single installed `~/Applications/Containerlab GUI.app`. No VM/data directory exists from this milestone. Future durable lab state must have a separate explicit removal policy; upgrading or uninstalling a GUI must not destroy a running lab.
