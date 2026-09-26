# Live application candidate dependencies

Live link capture/reanalysis and installed end-to-end qualification are implemented.
Do not replace an existing installation implicitly; use a fresh extraction directory.

Bundled: official Node 26.8.1 darwin-arm64 (verified upstream archive hash),
production React/React Flow assets, Zod, Python helper sources, Containerlab 0.79.0
commit 5ae50094a3afd70e4e1674fe5385e64d8979da26 ARM64 binary, and the declaration worker
compiled against that same source. Binary hashes are in runtime/linux/SHA256.json.
No topology examples, fixture catalogs, recorded graphs or project sources ship.

External on macOS: Apple Silicon / Virtualization.framework, Lima (tested host
2.2.0; minimum configuration 2.0.0), Python3 for explicit runtime provisioning,
network access for the pinned Ubuntu image and Ubuntu packages. Node/npm/Go/C++
are not user runtime prerequisites. Linux runtime: 8 CPUs, 16GiB memory, 50GiB
sparse disk; no host filesystem mounts or agent forwarding or public port forwards.

Ubuntu image is checksum pinned. Direct Docker/Python/bubblewrap/libpcap/TShark package
versions are selected explicitly by runtime-create.py. Transitive Ubuntu packages
and iproute2 are repository-resolved: exact reproducible runtime dependency closure
is still unresolved, not claimed by this candidate. Package availability failures
must stop creation, never silently substitute versions. The configuration has no
experiment expiry timer. VM survives browser/application exit until explicitly stopped.

Project container images are separate user dependencies; image names in the user's
unmodified topology must be available on its Linux runtime. Local-only images use
`runtime load-image /absolute/path/image.tar` after an external image build/export. Installing the GUI
does not build a user's VRT image or turn a mutable tag into a pinned image.

Native TShark 4.2.2-1.1build3, capture helpers and a minimal isolated analysis root
with one checksum-verified reviewed Lua profile are provisioned. Arbitrary Lua scripts
are not accepted. Serial discovery/transport remains gated. Docker is pinned to
29.1.3-0ubuntu3~24.04.2, Python to 3.12.3-0ubuntu2.1, bubblewrap to
0.9.0-1ubuntu0.3 and libpcap to 1.10.4-4.1ubuntu3.1. Exact observed transitive
packages are recorded in LIVE-002/linux-packages.txt; that is an inventory, not a
repository snapshot guaranteeing future availability.

Build-only: npm lockfile dependencies, TypeScript/Vite, Go + Containerlab source for
worker compilation, Python3, macOS pkgbuild/otool. Licenses and npm dependency inventory
ship in licenses/. Package is unsigned/unnotarized; successful pkgbuild is not evidence
of an Apple Installer transaction or notarization.
