# Live application — 0.3.0-preview.10

This Apple Silicon preview contains no topology bundles, recorded graphs or developer catalog. User topology files, companions and container images are separate inputs.

Extract the archive into a fresh directory. `install.command` installs the separately named app and refuses to overwrite an existing one. Do not overlay an app whose bundled Node is running. Finder prints help; topology selection is currently through the CLI.

```sh
APP="$HOME/Applications/Containerlab GUI Live.app/Contents/Resources"
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" doctor
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime create
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime load-image /absolute/path/image.tar
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" /absolute/path/topology.clab.yml --include relative/companion.cfg
```

Create is explicit and refuses an existing runtime pointer. Image import is optional for locally built images (Docker save format, regular .tar file up to 4 GiB); registry images are acquired by native deployment. Include every required local companion explicitly. Missing template context is rejected; arbitrary environment-variable context is not supported. No example or application-specific assumptions exist in the GUI.

Open http://127.0.0.1:4173. GO invokes Containerlab deployment. Node selection exposes actual logs; link selection exposes PCAP filename, bounded capture and display filters, and the installed reviewed Lua profile. Capture automatically selects a qualified Linux interface; unsupported kinds remain explicit. Download preserves captured bytes. Reanalysis uses the same in-memory artifact. Limits: one capture, 1 MiB, 1–10 seconds, first 100 packet rows, five-minute artifact retention; no file rotation or persistent capture storage. Serial transport remains unavailable.

Stop lab invokes native destruction. Closing the browser or server leaves the lab running. Restart the same CLI command to reconcile exact saved container identities; do not remove metadata or replace containers on mismatch. For an intentional runtime shutdown, stop the lab first, close the server, then:

```sh
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime status
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime stop
```

Runtime start/status and scoped recovery are implemented; project-removal remains unavailable. Runtime metadata lives privately under `~/Library/Application Support/Containerlab GUI`; the VM has an eight-project limit and 50 GiB disk. Fresh runtimes configure Docker local logs at 10 MiB × 3 files per container. Source snapshots persist until explicit runtime retirement; this is a trusted local test profile, not a private-source storage service. No experiment expiry timer is installed. Uninstalling the app does not remove VMs, labs, images or metadata.

Installed qualification covered a synthetic Linux pair, the full four-radio example and two pinned official SR Linux demos. Capability results are separate: the SR Linux-only demos have no qualified Linux capture point. This is not universal topology, deployment or serial support. The package is unsigned/unnotarized; archive installation is tested separately from the Apple Installer transaction. See DEPENDENCIES.md and the source workspace's LIVE-002 evidence for pins and limitations.


## Resume and recovery

New runtimes automatically record an offline resume identity after live owner verification.
For a runtime created by preview.8 or earlier, while it is running, use the new installed CLI:

```sh
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime prepare-resume
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime update-helper
```

Preparation checks live owner/native pins and the original creation record before saving
Lima config, VZ identifier and disk identity. It refuses to enroll an unknown stopped VM.
A changed saved identity is refused, not overwritten. Helper update replaces only the fixed
application helper under its operation lock after ownership and package-content hash checks;
it neither deploys nor destroys a lab. An in-progress operation can make it return busy.

```sh
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime status
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime start
```

Status can report Stopped without attempting a guest connection. Start boots only the
anchored instance, then verifies guest ownership/native pins; it does not deploy a lab.
A post-boot mismatch leaves operations refused and is not automatically rolled back.
Do not erase identity files to bypass refusal. A stopped older runtime without preparation
requires an operator to verify and resume that known VM first; it cannot be adopted automatically.

In the GUI, **Resume / reconnect** starts the anchored runtime if needed, then reconciles.
**Check recovery** inspects the current project without starting the VM. No native resources
means stale deployment intent can be cleared and GO retried. Exact saved running identities
reconnect. Partial resources remain explicit: use **Stop lab** before retrying GO. Unknown or
replacement identities refuse recovery. These controls never silently enroll replacements.

After an app restart, a previous incomplete operation may need Check recovery. Existing
project metadata and original input files must remain intact. Native timeout/collision/source
mismatch reason codes are retained; unrestricted stderr is never shown. General image-pull,
license and native CLI diagnostics remain coarse. Deployment cancellation is not added here.

For isolated explicitly authorized qualification only, `--state-dir /absolute/private/path`
precedes CLI arguments. Ordinary launch uses the normal private user state directory.
Do not point a test suite at a user's active deployment without explicit permission.

Native container IDs can survive VM shutdown while processes remain exited. Such a lab is partial after reconnect: use Stop lab, then GO. The GUI does not mistake a resumed VM for a running lab or start containers through a competing lifecycle engine.
