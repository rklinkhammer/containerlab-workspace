# Installed release dependency boundary

## First package: macOS ARM64 GUI

Bundled: checksum-verified upstream Node26.8.1 Darwin ARM64 executable/license; compiled React19.2.8/React DOM19.2.8/React Flow12.10.2 frontend and their locked transitive dependencies; Zod4.6.5 server dependency; application backend/contracts; approved public fixture catalog and recorded frontend assets. Full locked npm inventory and notices ship in Resources/licenses. No Homebrew dylib, npm, Git, compiler, repository, test runner or sibling path is needed to view the installed GUI.

OS/runtime: Apple Silicon macOS and browser; loopback port4173 (or explicit PREVIEW_PORT); system libraries listed in runtime-dylibs.txt. Qualification applies only to the tested macOS build, not every macOS release. Package is an unsigned local preview, not a signed/notarized distribution release. No privileged install hooks, VM creation or network downloads occur when launching.

## Persistent live runtime: separate milestone, not bundled or enabled yet

Mac: Lima (previous experiments2.2.0), its VZ/SSH support and the current macOS virtualization profile. Linux VM: checksum-pinned Ubuntu image, systemd, Python3, sudo, coreutils timeout, util-linux nsenter, iproute2, Docker daemon and Containerlab0.79.0; privileged lifecycle/inspection confined to the owned VM. Loader binary is built against the pinned native revision and must ship with a hash, runner and public bundle context. Observer/log/capture/analysis helpers and reviewed Lua catalog must be installed explicitly. TShark/dumpcap, shared libraries and minimal analysis root are needed for capture and reviewed Lua. Exact Linux transitive/package pins must be captured during the installed runtime build; current experimental versions are evidence, not an installed runtime bill of materials.

Example deployment: separate reviewed bundle of the full eight-node four-radio topology, all companion configuration files, pinned containerlab-vrt application image and pinned SR Linux switch image, image licenses and architecture support. No source checkout or image build should be required on the user's Mac. Configuration generation, CMake/C++ compiler, VRT framework/submodules and Docker BuildKit belong to the release build pipeline, not GUI startup. No containerlab-vrt source is silently copied from private .runtime directories.

Excluded from this milestone: QEMU/AAVMF/guest image and serial transport (not needed for the container-only example), arbitrary Lua, metrics database, authentication under TT-01, and automatic application-health inference. Persistent storage/log/capture quotas, runtime ownership, reconnect/restart and explicit shutdown need separate implementation and installed acceptance.
