# Per-topology native diagnostics — EXP-014

**Observed:** 57 rejected inputs with exact native errors, linked to unchanged staged YAML. These are errors returned by the pinned native library; interpretations and remedies are separate. [Machine-readable results](results.json), [input provenance](input-manifest.json), [summary and limits](RESULTS.md). F1 resolved and is excluded from this failure list.

## C088

Exact tested YAML: [C088.clab.yml](input/C088.clab.yml) — SHA-256 `b2e1a58db41432e5d31cb610521498e72bc1b3b0431b404b0104820f346cc4b5`.

**Observed:** rejected at `load`; result case `C088-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: yaml: unmarshal errors:
  line 8: field publish not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**Inferred disposition:** `native_schema_rejection`. Review against the pinned native schema and preserve the original. Record any correction as a new input. Unknown attributes must not be silently discarded.

## C112

Exact tested YAML: [C112.clab.yml](input/C112.clab.yml) — SHA-256 `e7580dffcab8ffe712dc9ceb04e740b4f6fed73b0ff10716355d2db1bc5aaaf1`.

**Observed:** rejected at `load`; result case `C112-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C113

Exact tested YAML: [C113.clab.yml](input/C113.clab.yml) — SHA-256 `6d0055c6a9295a3ca6c9dd1e1fd67f96f475377f3fe85b5a64493a9c69e1140c`.

**Observed:** rejected at `load`; result case `C113-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C140

Exact tested YAML: [C140.clab.yml](input/C140.clab.yml) — SHA-256 `efed48ecd47118d74ce776ae19d66119bf9c87adc42e2714576e6ba233b4795b`.

**Observed:** rejected at `load`; result case `C140-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C141

Exact tested YAML: [C141.clab.yml](input/C141.clab.yml) — SHA-256 `36e30648396bc9324c4dabb039b7773cfa78d69ad1f1d0a66788c177a2ae7c32`.

**Observed:** rejected at `load`; result case `C141-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C150

Exact tested YAML: [C150.clab.yml](input/C150.clab.yml) — SHA-256 `5d376d802fb5fb7eaecc14809bbc592bf6697d38f22e84374dc9b1afa255a894`.

**Observed:** rejected at `load`; result case `C150-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C155

Exact tested YAML: [C155.clab.yml](input/C155.clab.yml) — SHA-256 `d56e06e185bd75d5227d56420f8ae8f4183cba962158045918873377979b900d`.

**Observed:** rejected at `load`; result case `C155-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C159

Exact tested YAML: [C159.clab.yml](input/C159.clab.yml) — SHA-256 `658655c1d554f393c62850fb35b30ae8a44dc27dc986e3aa7a9f996b1840e0d9`.

**Observed:** rejected at `load`; result case `C159-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C162

Exact tested YAML: [C162.clab.yml](input/C162.clab.yml) — SHA-256 `f81e3fb790e26d223df251e10b8a36563af5f2eefbd85ffa2c142f2c4c3df59b`.

**Observed:** rejected at `load`; result case `C162-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C162.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C163

Exact tested YAML: [C163.clab.yml](input/C163.clab.yml) — SHA-256 `ec6a1d7cbd401ed13ab573d51c801ab2d1bf57ac09b777fceaad80f74abbf728`.

**Observed:** rejected at `load`; result case `C163-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C163.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C164

Exact tested YAML: [C164.clab.yml](input/C164.clab.yml) — SHA-256 `82e3bef60e00abadd82f300397495f9f01a0133786361487db18b5b5a52b8980`.

**Observed:** rejected at `load`; result case `C164-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C164.clab.yml:18: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C166

Exact tested YAML: [C166.clab.yml](input/C166.clab.yml) — SHA-256 `20142045a38c4c48465797c350291d5d0340d08da11154237670f3fbb1ca1825`.

**Observed:** rejected at `load`; result case `C166-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C166.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C167

Exact tested YAML: [C167.clab.yml](input/C167.clab.yml) — SHA-256 `bb54f84a3a8764f0019e7155cfcf80e6ba200626a4be918ca6d1eea5126903f5`.

**Observed:** rejected at `load`; result case `C167-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C167.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C168

Exact tested YAML: [C168.clab.yml](input/C168.clab.yml) — SHA-256 `b2a7978ba2e809ca8a516c31059bf1993d80e394e950c444370c4044f0c81f8a`.

**Observed:** rejected at `load`; result case `C168-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C168.clab.yml:6: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C171

Exact tested YAML: [C171.clab.yml](input/C171.clab.yml) — SHA-256 `6bf572cf6eb3b96dcb708b5188de1c71d98f463e47456a62636301a700e209ff`.

**Observed:** rejected at `load`; result case `C171-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C171.clab.yml:6: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C172

Exact tested YAML: [C172.clab.yml](input/C172.clab.yml) — SHA-256 `5c804d00fc8d16ad5c71ff139209bcb4524ef6cec656a2671c99f39412b544ee`.

**Observed:** rejected at `load`; result case `C172-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C172.clab.yml:8: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C173

Exact tested YAML: [C173.clab.yml](input/C173.clab.yml) — SHA-256 `f32a735e80ef104a6bc3e44d67b892323ded129eef8605f17d6fec6edf13d812`.

**Observed:** rejected at `load`; result case `C173-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C173.clab.yml:12: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C174

Exact tested YAML: [C174.clab.yml](input/C174.clab.yml) — SHA-256 `04821b7d1e09a924a34bf5d415a53e08d3054894abe761c6eabc078d23633f40`.

**Observed:** rejected at `load`; result case `C174-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C174.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C175

Exact tested YAML: [C175.clab.yml](input/C175.clab.yml) — SHA-256 `ec1f418ab25cf54c28fef4dd3d4c8167d80a1b6798f5c5adcca89f54a8b754c8`.

**Observed:** rejected at `load`; result case `C175-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C175.clab.yml:10: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C176

Exact tested YAML: [C176.clab.yml](input/C176.clab.yml) — SHA-256 `890ce0850fc82987742e6a9791b08444c39ae5dfc1522196e2b0aad0025938f6`.

**Observed:** rejected at `load`; result case `C176-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C176.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C201

Exact tested YAML: [C201.clab.yml](input/C201.clab.yml) — SHA-256 `6d005204938f1dcc81381e8258a8a1a8ba9e96e41ed6dc3a7b5f0839ba4c526b`.

**Observed:** rejected at `load`; result case `C201-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C201.clab.yml:8: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C202

Exact tested YAML: [C202.clab.yml](input/C202.clab.yml) — SHA-256 `ac189f02a4aad582465b6131c2bbcbcbae147d93268490c5bceb68c6e01a0e7c`.

**Observed:** rejected at `load`; result case `C202-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C202.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C204

Exact tested YAML: [C204.clab.yml](input/C204.clab.yml) — SHA-256 `f5b9368bcef9d217dbd79682caa37de9d4badd9de529ec7f6fb3637232342b0e`.

**Observed:** rejected at `load`; result case `C204-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C204.clab.yml:8: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C205

Exact tested YAML: [C205.clab.yml](input/C205.clab.yml) — SHA-256 `b08a47641bb783dc88f50094cc1f3a8aad3f30cb5f077793d9fd6e56a474d973`.

**Observed:** rejected at `load`; result case `C205-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C205.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C206

Exact tested YAML: [C206.clab.yml](input/C206.clab.yml) — SHA-256 `7d6b62e312385fef60d431c018539f25a106ce5d374afed9af6a2b5ec568c25e`.

**Observed:** rejected at `load`; result case `C206-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C206.clab.yml:9: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C217

Exact tested YAML: [C217.clab.yml](input/C217.clab.yml) — SHA-256 `47f7018bf1ac05ca12892273ae5e9095553fce7891dfb96dcb0f66d7282e18a8`.

**Observed:** rejected at `load`; result case `C217-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C217.clab.yml:7: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C218

Exact tested YAML: [C218.clab.yml](input/C218.clab.yml) — SHA-256 `dea8acafda19d9fcb7b4507e168efac65081004c9dfebce9209f6446e06f5165`.

**Observed:** rejected at `load`; result case `C218-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: yaml: unmarshal errors:
  line 9: field mgmt_ipv6 not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**Inferred disposition:** `native_schema_rejection`. Review against the pinned native schema and preserve the original. Record any correction as a new input. Unknown attributes must not be silently discarded.

## C221

Exact tested YAML: [C221.clab.yml](input/C221.clab.yml) — SHA-256 `f261e65242945007d39e44f22c7fd0d60a025113903f960b8dde384ca88329e4`.

**Observed:** rejected at `load`; result case `C221-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C221.clab.yml:6: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C226

Exact tested YAML: [C226.clab.yml](input/C226.clab.yml) — SHA-256 `127c53050d76294118eacc79963da184bea5b2352af90b9c3b4915ae9a68e253`.

**Observed:** rejected at `load`; result case `C226-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C226.clab.yml:8: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C227

Exact tested YAML: [C227.clab.yml](input/C227.clab.yml) — SHA-256 `4e53641c85986bbd8293a026385679dedb4cf7d214e70594e2ea9e1b239c9b56`.

**Observed:** rejected at `load`; result case `C227-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C227.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C228

Exact tested YAML: [C228.clab.yml](input/C228.clab.yml) — SHA-256 `f5e5002f6605b8d189d1593ca9bfac52f986c7eea17df2de8d9b4acb6a3e1dd6`.

**Observed:** rejected at `load`; result case `C228-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C228.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C248

Exact tested YAML: [C248.clab.yml](input/C248.clab.yml) — SHA-256 `03ce2143bab2899077e7bac758721625e9ca69afe3bafc09afb32a059dfb18cc`.

**Observed:** rejected at `load`; result case `C248-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to fetch http(s) resource: https://gist.com/<somehash>/staticroute.partial.cfg
```

**Inferred disposition:** `external_resource_context`. The isolated worker cannot fetch remote resources. Supply a reviewed, pinned offline dependency bundle where appropriate; placeholder URLs require actual documented assets.

**Unresolved:** this run does not establish remote object availability or credentials. Network denial is intentional; the error is not proof the remote object does not exist.

## C252

Exact tested YAML: [C252.clab.yml](input/C252.clab.yml) — SHA-256 `f6ad8b3d9e2693f88bfc632d41f631e513743e35199d84f3590eabc429db09f7`.

**Observed:** rejected at `load`; result case `C252-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to verify bind path: stat /input/corerouter1/daemons: no such file or directory
```

**Inferred disposition:** `missing_static_file`. Pin the actual referenced asset and stage its intended layout for dependency-complete resolution. Separately qualify a native display-only mode; do not fabricate files.

## C258

Exact tested YAML: [C258.clab.yml](input/C258.clab.yml) — SHA-256 `7fd19abf509cd7946743aa2ff5c643b9db1b8d6406073504ea75363415de441d`.

**Observed:** rejected at `load`; result case `C258-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to verify bind path: stat /path/to/vswitch.xml: no such file or directory
```

**Inferred disposition:** `missing_static_file`. Pin the actual referenced asset and stage its intended layout for dependency-complete resolution. Separately qualify a native display-only mode; do not fabricate files.

## C276

Exact tested YAML: [C276.clab.yml](input/C276.clab.yml) — SHA-256 `b892b1d538589398851ef276fdd2e201a813d606b945443a28549945b44c99bd`.

**Observed:** rejected at `load`; result case `C276-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to fetch http(s) resource: https://gist.com/<somehash>/staticroute.partial.cfg
```

**Inferred disposition:** `external_resource_context`. The isolated worker cannot fetch remote resources. Supply a reviewed, pinned offline dependency bundle where appropriate; placeholder URLs require actual documented assets.

**Unresolved:** this run does not establish remote object availability or credentials. Network denial is intentional; the error is not proof the remote object does not exist.

## C290

Exact tested YAML: [C290.clab.yml](input/C290.clab.yml) — SHA-256 `227a4704fb8318e4198aea24c433048a7cd96b3904848ce6e622a8ba801a1631`.

**Observed:** rejected at `load`; result case `C290-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C290.clab.yml:8: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C291

Exact tested YAML: [C291.clab.yml](input/C291.clab.yml) — SHA-256 `dced2d748f0defb2da737d6a571cea2dd750b71ff073be30f4cfb28f53e9f71e`.

**Observed:** rejected at `load`; result case `C291-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C291.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C292

Exact tested YAML: [C292.clab.yml](input/C292.clab.yml) — SHA-256 `eaf0a3ab6bd6b52de8f32ac59d189e2d28a04e0c7f6e73c4e29e0cc15199f575`.

**Observed:** rejected at `load`; result case `C292-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C292.clab.yml:10: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C293

Exact tested YAML: [C293.clab.yml](input/C293.clab.yml) — SHA-256 `dfd31a25fe546ab89a47a5347ef365d5248204ada76115aa79b74e273d7544c6`.

**Observed:** rejected at `load`; result case `C293-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C293.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C294

Exact tested YAML: [C294.clab.yml](input/C294.clab.yml) — SHA-256 `38edd7091d48019109355c22afab01965e32486b408da677f55d885bee75120d`.

**Observed:** rejected at `load`; result case `C294-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C294.clab.yml:8: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C295

Exact tested YAML: [C295.clab.yml](input/C295.clab.yml) — SHA-256 `8e02c791d0d0303e000d134d7b0282e6a3e1dd1359858694208f660cdee9a3eb`.

**Observed:** rejected at `load`; result case `C295-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: template: C295.clab.yml:5: function "kind_code_name" not defined
```

**Inferred disposition:** `documentation_macro_context`. Supply the pinned documentation frontmatter/context in a separately identified derivative. The original snippet remains unchanged.

## C310

Exact tested YAML: [C310.clab.yml](input/C310.clab.yml) — SHA-256 `c31f40d96dc50686c48b7ab548a7c94d7d30c8734032f24f11d4942856c1ebdb`.

**Observed:** rejected at `load`; result case `C310-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "n1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C314

Exact tested YAML: [C314.clab.yml](input/C314.clab.yml) — SHA-256 `2a2f207f179942f07fafb76a44bebe0be700b894cf123f4778015c36ac7ac091`.

**Observed:** rejected at `links`; result case `C314-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
Link not found
```

**Inferred disposition:** `host_interface_context`. Separate host-dependent link validation from static display. Do not borrow an existing host interface or invent a successfully resolved link.

**Documented:** the YAML names `macvlan:enp0s3`; pinned `links/link_macvlan.go:84` calls `netlink.LinkByName` during resolution. **Inferred:** the absent parent interface in the isolated namespace explains this generic native error. The native message itself does not name the interface.

## C316

Exact tested YAML: [C316.clab.yml](input/C316.clab.yml) — SHA-256 `affaa77e08168edef646e439b543957e41462c8ae975f51e96f8ae265ec967e4`.

**Observed:** rejected at `load`; result case `C316-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C324

Exact tested YAML: [C324.clab.yml](input/C324.clab.yml) — SHA-256 `083b0318d39b16195274449c9c6859afc3d0046fc5f8546aeb032dfd496f1577`.

**Observed:** rejected at `load`; result case `C324-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to verify bind path: stat /input/cfgs/n1/conf: no such file or directory
```

**Inferred disposition:** `missing_static_file`. Pin the actual referenced asset and stage its intended layout for dependency-complete resolution. Separately qualify a native display-only mode; do not fabricate files.

## C325

Exact tested YAML: [C325.clab.yml](input/C325.clab.yml) — SHA-256 `e43e5b86f058ac08f44327e706437ae952ca3005a6381804837fc9de48fbc237`.

**Observed:** rejected at `load`; result case `C325-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to verify bind path: stat /input/clab-mylab/n1/conf: no such file or directory
```

**Inferred disposition:** `missing_static_file`. Pin the actual referenced asset and stage its intended layout for dependency-complete resolution. Separately qualify a native display-only mode; do not fabricate files.

## C326

Exact tested YAML: [C326.clab.yml](input/C326.clab.yml) — SHA-256 `2634d4fea4e80714267ac1db5a0d116dc231b6d7540fc905d84eefa7ead93500`.

**Observed:** rejected at `load`; result case `C326-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "ansible": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C368

Exact tested YAML: [C368.clab.yml](input/C368.clab.yml) — SHA-256 `3923bdba86b6e1287d55617e801829d40485556ede6775b7b516522b23a05ee1`.

**Observed:** rejected at `load`; result case `C368-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to fetch s3 resource: s3://my-bucket/configs/router1.cli: object not found or access denied: Head "https://my-bucket.s3.dualstack.us-east-1.amazonaws.com/configs/router1.cli": dial tcp: lookup my-bucket.s3.dualstack.us-east-1.amazonaws.com on 127.0.0.53:53: read udp 127.0.0.1:48789->127.0.0.53:53: read: connection refused
```

**Inferred disposition:** `external_resource_context`. The isolated worker cannot fetch remote resources. Supply a reviewed, pinned offline dependency bundle where appropriate; placeholder URLs require actual documented assets.

**Unresolved:** this run does not establish remote object availability or credentials. Network denial is intentional; the error is not proof the remote object does not exist.

## C398

Exact tested YAML: [C398.clab.yml](input/C398.clab.yml) — SHA-256 `4412cf610d4c2b1d57f258f53058d84ec2ac1aae6fc6856bda44e8c81cde4660`.

**Observed:** rejected at `load`; result case `C398-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "router1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C399

Exact tested YAML: [C399.clab.yml](input/C399.clab.yml) — SHA-256 `fe983b657ebb13cbf2c96b875eee53b82779d6516d1a411d9c51306cf8e82477`.

**Observed:** rejected at `load`; result case `C399-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to verify bind path: stat /input/clab-mylab/shared-data.json: no such file or directory
```

**Inferred disposition:** `missing_static_file`. Pin the actual referenced asset and stage its intended layout for dependency-complete resolution. Separately qualify a native display-only mode; do not fabricate files.

## C400

Exact tested YAML: [C400.clab.yml](input/C400.clab.yml) — SHA-256 `1ac42b2cc8d66b18527caa02ca5f51b88b0d5e022509216b6ff7ce08b4ac078b`.

**Observed:** rejected at `load`; result case `C400-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## C413

Exact tested YAML: [C413.clab.yml](input/C413.clab.yml) — SHA-256 `2a2f207f179942f07fafb76a44bebe0be700b894cf123f4778015c36ac7ac091`.

**Observed:** rejected at `links`; result case `C413-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
Link not found
```

**Inferred disposition:** `host_interface_context`. Separate host-dependent link validation from static display. Do not borrow an existing host interface or invent a successfully resolved link.

**Documented:** the YAML names `macvlan:enp0s3`; pinned `links/link_macvlan.go:84` calls `netlink.LinkByName` during resolution. **Inferred:** the absent parent interface in the isolated namespace explains this generic native error. The native message itself does not name the interface.

## C416

Exact tested YAML: [C416.clab.yml](input/C416.clab.yml) — SHA-256 `f5cbc29c3ed78ebe20291f81615ba2e5476ff71c7a8b005226bcbb1894077198`.

**Observed:** rejected at `load`; result case `C416-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: yaml: unmarshal errors:
  line 6: cannot unmarshal !!str `nokia_s...` into types.NodeDefinitionWithDeprecatedFields
  line 7: cannot unmarshal !!str `ghcr.io...` into types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**Inferred disposition:** `native_schema_rejection`. Review against the pinned native schema and preserve the original. Record any correction as a new input. Unknown attributes must not be silently discarded.

## C423

Exact tested YAML: [C423.clab.yml](input/C423.clab.yml) — SHA-256 `6d0055c6a9295a3ca6c9dd1e1fd67f96f475377f3fe85b5a64493a9c69e1140c`.

**Observed:** rejected at `load`; result case `C423-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

**Inferred disposition:** `missing_kind_context`. Recover the documented native kind/default context. Do not guess Linux or silently add a kind.

## CTX-C168

Exact tested YAML: [CTX-C168.clab.yml](input/CTX-C168.clab.yml) — SHA-256 `2756437438c725cbfdfbf52dc3bee7d9717d662e488aa00cd6cba954f2424591`.

**Observed:** rejected at `load`; result case `CTX-C168-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to verify bind path: stat /input/mymapping.json: no such file or directory
```

**Inferred disposition:** `missing_static_file`. Pin the actual referenced asset and stage its intended layout for dependency-complete resolution. Separately qualify a native display-only mode; do not fabricate files.

## F2

Exact tested YAML: [F2.clab.yml](input/F2.clab.yml) — SHA-256 `0cc94c3bb55a72190b7b486b636d3d6d2688d9f324fc254316fe6719b06e5a01`.

**Observed:** rejected at `load`; result case `F2-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to read topology file: yaml: unmarshal errors:
  line 12: field x-unknown not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**Inferred disposition:** `native_schema_rejection`. Review against the pinned native schema and preserve the original. Record any correction as a new input. Unknown attributes must not be silently discarded.

## F3

Exact tested YAML: [F3.clab.yml](input/F3.clab.yml) — SHA-256 `225e7850232935fafc7a7f2a42011d9de2c43cff8784deaa9c45f10d6d80fb95`.

**Observed:** rejected at `load`; result case `F3-diagnostic`. Exact native message (no redaction or truncation was necessary for this reviewed public/synthetic error):

```text
failed to verify bind path: stat /input/missing-fixture-file: no such file or directory
```

**Inferred disposition:** `missing_static_file`. Pin the actual referenced asset and stage its intended layout for dependency-complete resolution. Separately qualify a native display-only mode; do not fabricate files.
