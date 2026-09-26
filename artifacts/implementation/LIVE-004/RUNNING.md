# Running installed application

Open **http://127.0.0.1:4173**. Full four-radio is deployed in the explicitly resumed user runtime `clab-app-3a2d71d640034b2d`. The package contains no topology bundles. Actual source remains `../containerlab-vrt/generated/four-radio.clab.yml` with seven explicitly included files; source is unchanged.

Select a node → Logs → Load logs / Follow. Select a link → filename, capture/display filters, optional reviewed Lua → Start capture → Save PCAP or Reanalyze same PCAP. Capture supports qualified Linux interfaces, not arbitrary native endpoints. Reviewed Lua is currently the synthetic CLAB probe profile; this is not a VITA-specific dissector. Serial is unavailable. The browser can close/reopen without redeployment.

The server is running from `/Users/rklinkhammer/workspace/containerlab-releases/0.3.0-preview.8/Containerlab GUI Live.app`, using bundled Node and `/tmp` working directory. `LIVE-004/server.json` records its exact PID/arguments; do not kill another process holding4173. No repository application code is imported at runtime.

After closing this server, the reproducible launch is:

```sh
APP="/Users/rklinkhammer/workspace/containerlab-releases/0.3.0-preview.8/Containerlab GUI Live.app/Contents/Resources"
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" /Users/rklinkhammer/workspace/containerlab-vrt/generated/four-radio.clab.yml \
  --include radio1.json --include radio2.json --include radio3.json --include radio4.json \
  --include processor.json --include detector.json --include srlinux.cli
```

To shut down: use **Stop lab** in the GUI, close this app server, then:

```sh
APP="/Users/rklinkhammer/workspace/containerlab-releases/0.3.0-preview.8/Containerlab GUI Live.app/Contents/Resources"
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime status
"$APP/runtime/node" "$APP/packaging/live-cli.mjs" runtime stop
```

App restart reconciliation is supported while the owned VM runs. VM resume and project retirement are not yet packaged; do not remove identity metadata to bypass errors or run `runtime create` to reuse a stopped VM. No unrelated VMs should be touched. Retain this runtime until intentionally retired; qualification VM is already stopped.

New-install instructions and dependencies are beside the release in README.md and inside the app in DEPENDENCIES.md. Local VRT image archive is a separate user resource: `/Users/rklinkhammer/workspace/containerlab-user-tests/live-002/vrt-image.tar`. Installed `runtime load-image` successfully imported it. GUI installation does not build or bundle project images.
