# Live application — 0.3.0-preview.6

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

Restart/resume and project-removal commands are not implemented. Runtime metadata lives privately under `~/Library/Application Support/Containerlab GUI`; the VM has an eight-project limit and 50 GiB disk. Fresh runtimes configure Docker local logs at 10 MiB × 3 files per container. Source snapshots persist until explicit runtime retirement; this is a trusted local test profile, not a private-source storage service. No experiment expiry timer is installed. Uninstalling the app does not remove VMs, labs, images or metadata.

Installed qualification covered a synthetic Linux pair, the full four-radio example and two pinned official SR Linux demos. Capability results are separate: the SR Linux-only demos have no qualified Linux capture point. This is not universal topology, deployment or serial support. The package is unsigned/unnotarized; archive installation is tested separately from the Apple Installer transaction. See DEPENDENCIES.md and the source workspace's LIVE-002 evidence for pins and limitations.
