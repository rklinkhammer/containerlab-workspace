# Per-input native profile comparison

**Observed:** each source is unchanged and hash-pinned in [input-manifest.json](input-manifest.json). Declaration availability is separate from resolved validity and deployment readiness. Messages are retained native errors; see [results.json](results.json) for diagnostic metadata.

## C088

Input: [C088.clab.yml](input/C088.clab.yml); SHA-256 `b2e1a58db41432e5d31cb610521498e72bc1b3b0431b404b0104820f346cc4b5`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
yaml: unmarshal errors:
  line 8: field publish not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: yaml: unmarshal errors:
  line 8: field publish not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

## C112

Input: [C112.clab.yml](input/C112.clab.yml); SHA-256 `e7580dffcab8ffe712dc9ceb04e740b4f6fed73b0ff10716355d2db1bc5aaaf1`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 0 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C113

Input: [C113.clab.yml](input/C113.clab.yml); SHA-256 `6d0055c6a9295a3ca6c9dd1e1fd67f96f475377f3fe85b5a64493a9c69e1140c`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C140

Input: [C140.clab.yml](input/C140.clab.yml); SHA-256 `efed48ecd47118d74ce776ae19d66119bf9c87adc42e2714576e6ba233b4795b`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C141

Input: [C141.clab.yml](input/C141.clab.yml); SHA-256 `36e30648396bc9324c4dabb039b7773cfa78d69ad1f1d0a66788c177a2ae7c32`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C150

Input: [C150.clab.yml](input/C150.clab.yml); SHA-256 `5d376d802fb5fb7eaecc14809bbc592bf6697d38f22e84374dc9b1afa255a894`.

**declarations:** `declarations_only`; 4 projected nodes, 0 declared links, 4 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C155

Input: [C155.clab.yml](input/C155.clab.yml); SHA-256 `d56e06e185bd75d5227d56420f8ae8f4183cba962158045918873377979b900d`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 0 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C159

Input: [C159.clab.yml](input/C159.clab.yml); SHA-256 `658655c1d554f393c62850fb35b30ae8a44dc27dc986e3aa7a9f996b1840e0d9`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 0 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C162

Input: [C162.clab.yml](input/C162.clab.yml); SHA-256 `f81e3fb790e26d223df251e10b8a36563af5f2eefbd85ffa2c142f2c4c3df59b`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C162.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C162.clab.yml:5: function "kind_code_name" not defined
```

## C163

Input: [C163.clab.yml](input/C163.clab.yml); SHA-256 `ec6a1d7cbd401ed13ab573d51c801ab2d1bf57ac09b777fceaad80f74abbf728`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C163.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C163.clab.yml:5: function "kind_code_name" not defined
```

## C164

Input: [C164.clab.yml](input/C164.clab.yml); SHA-256 `82e3bef60e00abadd82f300397495f9f01a0133786361487db18b5b5a52b8980`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C164.clab.yml:18: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C164.clab.yml:18: function "kind_code_name" not defined
```

## C166

Input: [C166.clab.yml](input/C166.clab.yml); SHA-256 `20142045a38c4c48465797c350291d5d0340d08da11154237670f3fbb1ca1825`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C166.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C166.clab.yml:5: function "kind_code_name" not defined
```

## C167

Input: [C167.clab.yml](input/C167.clab.yml); SHA-256 `bb54f84a3a8764f0019e7155cfcf80e6ba200626a4be918ca6d1eea5126903f5`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C167.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C167.clab.yml:5: function "kind_code_name" not defined
```

## C168

Input: [C168.clab.yml](input/C168.clab.yml); SHA-256 `b2a7978ba2e809ca8a516c31059bf1993d80e394e950c444370c4044f0c81f8a`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C168.clab.yml:6: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C168.clab.yml:6: function "kind_code_name" not defined
```

## C171

Input: [C171.clab.yml](input/C171.clab.yml); SHA-256 `6bf572cf6eb3b96dcb708b5188de1c71d98f463e47456a62636301a700e209ff`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C171.clab.yml:6: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C171.clab.yml:6: function "kind_code_name" not defined
```

## C172

Input: [C172.clab.yml](input/C172.clab.yml); SHA-256 `5c804d00fc8d16ad5c71ff139209bcb4524ef6cec656a2671c99f39412b544ee`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C172.clab.yml:8: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C172.clab.yml:8: function "kind_code_name" not defined
```

## C173

Input: [C173.clab.yml](input/C173.clab.yml); SHA-256 `f32a735e80ef104a6bc3e44d67b892323ded129eef8605f17d6fec6edf13d812`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C173.clab.yml:12: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C173.clab.yml:12: function "kind_code_name" not defined
```

## C174

Input: [C174.clab.yml](input/C174.clab.yml); SHA-256 `04821b7d1e09a924a34bf5d415a53e08d3054894abe761c6eabc078d23633f40`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C174.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C174.clab.yml:5: function "kind_code_name" not defined
```

## C175

Input: [C175.clab.yml](input/C175.clab.yml); SHA-256 `ec1f418ab25cf54c28fef4dd3d4c8167d80a1b6798f5c5adcca89f54a8b754c8`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C175.clab.yml:10: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C175.clab.yml:10: function "kind_code_name" not defined
```

## C176

Input: [C176.clab.yml](input/C176.clab.yml); SHA-256 `890ce0850fc82987742e6a9791b08444c39ae5dfc1522196e2b0aad0025938f6`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C176.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C176.clab.yml:5: function "kind_code_name" not defined
```

## C201

Input: [C201.clab.yml](input/C201.clab.yml); SHA-256 `6d005204938f1dcc81381e8258a8a1a8ba9e96e41ed6dc3a7b5f0839ba4c526b`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C201.clab.yml:8: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C201.clab.yml:8: function "kind_code_name" not defined
```

## C202

Input: [C202.clab.yml](input/C202.clab.yml); SHA-256 `ac189f02a4aad582465b6131c2bbcbcbae147d93268490c5bceb68c6e01a0e7c`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C202.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C202.clab.yml:5: function "kind_code_name" not defined
```

## C204

Input: [C204.clab.yml](input/C204.clab.yml); SHA-256 `f5b9368bcef9d217dbd79682caa37de9d4badd9de529ec7f6fb3637232342b0e`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C204.clab.yml:8: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C204.clab.yml:8: function "kind_code_name" not defined
```

## C205

Input: [C205.clab.yml](input/C205.clab.yml); SHA-256 `b08a47641bb783dc88f50094cc1f3a8aad3f30cb5f077793d9fd6e56a474d973`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C205.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C205.clab.yml:5: function "kind_code_name" not defined
```

## C206

Input: [C206.clab.yml](input/C206.clab.yml); SHA-256 `7d6b62e312385fef60d431c018539f25a106ce5d374afed9af6a2b5ec568c25e`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C206.clab.yml:9: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C206.clab.yml:9: function "kind_code_name" not defined
```

## C217

Input: [C217.clab.yml](input/C217.clab.yml); SHA-256 `47f7018bf1ac05ca12892273ae5e9095553fce7891dfb96dcb0f66d7282e18a8`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C217.clab.yml:7: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C217.clab.yml:7: function "kind_code_name" not defined
```

## C218

Input: [C218.clab.yml](input/C218.clab.yml); SHA-256 `dea8acafda19d9fcb7b4507e168efac65081004c9dfebce9209f6446e06f5165`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
yaml: unmarshal errors:
  line 9: field mgmt_ipv6 not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: yaml: unmarshal errors:
  line 9: field mgmt_ipv6 not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

## C221

Input: [C221.clab.yml](input/C221.clab.yml); SHA-256 `f261e65242945007d39e44f22c7fd0d60a025113903f960b8dde384ca88329e4`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C221.clab.yml:6: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C221.clab.yml:6: function "kind_code_name" not defined
```

## C226

Input: [C226.clab.yml](input/C226.clab.yml); SHA-256 `127c53050d76294118eacc79963da184bea5b2352af90b9c3b4915ae9a68e253`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C226.clab.yml:8: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C226.clab.yml:8: function "kind_code_name" not defined
```

## C227

Input: [C227.clab.yml](input/C227.clab.yml); SHA-256 `4e53641c85986bbd8293a026385679dedb4cf7d214e70594e2ea9e1b239c9b56`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C227.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C227.clab.yml:5: function "kind_code_name" not defined
```

## C228

Input: [C228.clab.yml](input/C228.clab.yml); SHA-256 `f5e5002f6605b8d189d1593ca9bfac52f986c7eea17df2de8d9b4acb6a3e1dd6`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C228.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C228.clab.yml:5: function "kind_code_name" not defined
```

## C248

Input: [C248.clab.yml](input/C248.clab.yml); SHA-256 `03ce2143bab2899077e7bac758721625e9ca69afe3bafc09afb32a059dfb18cc`.

**declarations:** `declarations_only`; 1 projected nodes, 0 declared links, 1 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to fetch http(s) resource: https://gist.com/<somehash>/staticroute.partial.cfg
```

## C252

Input: [C252.clab.yml](input/C252.clab.yml); SHA-256 `f6ad8b3d9e2693f88bfc632d41f631e513743e35199d84f3590eabc429db09f7`.

**declarations:** `declarations_only`; 3 projected nodes, 2 declared links, 7 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 3 projected nodes, 2 declared links, 7 unresolved dependency references.

## C258

Input: [C258.clab.yml](input/C258.clab.yml); SHA-256 `7fd19abf509cd7946743aa2ff5c643b9db1b8d6406073504ea75363415de441d`.

**declarations:** `declarations_only`; 1 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 1 projected nodes, 0 declared links, 2 unresolved dependency references.

## C276

Input: [C276.clab.yml](input/C276.clab.yml); SHA-256 `b892b1d538589398851ef276fdd2e201a813d606b945443a28549945b44c99bd`.

**declarations:** `declarations_only`; 1 projected nodes, 0 declared links, 1 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to fetch http(s) resource: https://gist.com/<somehash>/staticroute.partial.cfg
```

## C290

Input: [C290.clab.yml](input/C290.clab.yml); SHA-256 `227a4704fb8318e4198aea24c433048a7cd96b3904848ce6e622a8ba801a1631`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C290.clab.yml:8: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C290.clab.yml:8: function "kind_code_name" not defined
```

## C291

Input: [C291.clab.yml](input/C291.clab.yml); SHA-256 `dced2d748f0defb2da737d6a571cea2dd750b71ff073be30f4cfb28f53e9f71e`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C291.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C291.clab.yml:5: function "kind_code_name" not defined
```

## C292

Input: [C292.clab.yml](input/C292.clab.yml); SHA-256 `eaf0a3ab6bd6b52de8f32ac59d189e2d28a04e0c7f6e73c4e29e0cc15199f575`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C292.clab.yml:10: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C292.clab.yml:10: function "kind_code_name" not defined
```

## C293

Input: [C293.clab.yml](input/C293.clab.yml); SHA-256 `dfd31a25fe546ab89a47a5347ef365d5248204ada76115aa79b74e273d7544c6`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C293.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C293.clab.yml:5: function "kind_code_name" not defined
```

## C294

Input: [C294.clab.yml](input/C294.clab.yml); SHA-256 `38edd7091d48019109355c22afab01965e32486b408da677f55d885bee75120d`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C294.clab.yml:8: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C294.clab.yml:8: function "kind_code_name" not defined
```

## C295

Input: [C295.clab.yml](input/C295.clab.yml); SHA-256 `8e02c791d0d0303e000d134d7b0282e6a3e1dd1359858694208f660cdee9a3eb`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
template: C295.clab.yml:5: function "kind_code_name" not defined
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: template: C295.clab.yml:5: function "kind_code_name" not defined
```

## C310

Input: [C310.clab.yml](input/C310.clab.yml); SHA-256 `c31f40d96dc50686c48b7ab548a7c94d7d30c8734032f24f11d4942856c1ebdb`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 0 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "n1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C314

Input: [C314.clab.yml](input/C314.clab.yml); SHA-256 `2a2f207f179942f07fafb76a44bebe0be700b894cf123f4778015c36ac7ac091`.

**declarations:** `declarations_only`; 1 projected nodes, 1 declared links, 2 unresolved dependency references.

**skip-binds:** `link_resolution_failed`; 1 projected nodes, 1 declared links, 2 unresolved dependency references.

```text
Link not found
```

## C316

Input: [C316.clab.yml](input/C316.clab.yml); SHA-256 `affaa77e08168edef646e439b543957e41462c8ae975f51e96f8ae265ec967e4`.

**declarations:** `declarations_only`; 4 projected nodes, 5 declared links, 4 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C324

Input: [C324.clab.yml](input/C324.clab.yml); SHA-256 `083b0318d39b16195274449c9c6859afc3d0046fc5f8546aeb032dfd496f1577`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "n1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C325

Input: [C325.clab.yml](input/C325.clab.yml); SHA-256 `e43e5b86f058ac08f44327e706437ae952ca3005a6381804837fc9de48fbc237`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "n1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C326

Input: [C326.clab.yml](input/C326.clab.yml); SHA-256 `2634d4fea4e80714267ac1db5a0d116dc231b6d7540fc905d84eefa7ead93500`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "ansible": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C368

Input: [C368.clab.yml](input/C368.clab.yml); SHA-256 `3923bdba86b6e1287d55617e801829d40485556ede6775b7b516522b23a05ee1`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 4 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to fetch s3 resource: s3://my-bucket/configs/router1.cli: object not found or access denied: Head "https://my-bucket.s3.dualstack.us-east-1.amazonaws.com/configs/router1.cli": dial tcp: lookup my-bucket.s3.dualstack.us-east-1.amazonaws.com on 127.0.0.53:53: read udp 127.0.0.1:53460->127.0.0.53:53: read: connection refused
```

## C398

Input: [C398.clab.yml](input/C398.clab.yml); SHA-256 `4412cf610d4c2b1d57f258f53058d84ec2ac1aae6fc6856bda44e8c81cde4660`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "router1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C399

Input: [C399.clab.yml](input/C399.clab.yml); SHA-256 `fe983b657ebb13cbf2c96b875eee53b82779d6516d1a411d9c51306cf8e82477`.

**declarations:** `declarations_only`; 1 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C400

Input: [C400.clab.yml](input/C400.clab.yml); SHA-256 `1ac42b2cc8d66b18527caa02ca5f51b88b0d5e022509216b6ff7ce08b4ac078b`.

**declarations:** `declarations_only`; 1 projected nodes, 0 declared links, 0 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## C413

Input: [C413.clab.yml](input/C413.clab.yml); SHA-256 `2a2f207f179942f07fafb76a44bebe0be700b894cf123f4778015c36ac7ac091`.

**declarations:** `declarations_only`; 1 projected nodes, 1 declared links, 2 unresolved dependency references.

**skip-binds:** `link_resolution_failed`; 1 projected nodes, 1 declared links, 2 unresolved dependency references.

```text
Link not found
```

## C416

Input: [C416.clab.yml](input/C416.clab.yml); SHA-256 `f5cbc29c3ed78ebe20291f81615ba2e5476ff71c7a8b005226bcbb1894077198`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
yaml: unmarshal errors:
  line 6: cannot unmarshal !!str `nokia_s...` into types.NodeDefinitionWithDeprecatedFields
  line 7: cannot unmarshal !!str `ghcr.io...` into types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: yaml: unmarshal errors:
  line 6: cannot unmarshal !!str `nokia_s...` into types.NodeDefinitionWithDeprecatedFields
  line 7: cannot unmarshal !!str `ghcr.io...` into types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

## C423

Input: [C423.clab.yml](input/C423.clab.yml); SHA-256 `6d0055c6a9295a3ca6c9dd1e1fd67f96f475377f3fe85b5a64493a9c69e1140c`.

**declarations:** `declarations_only`; 2 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
constructing node "node1": kind "" is not supported. Supported kinds are "6wind_vsr, arista_ceos, arista_veos, arrcus_arcos, aruba_aoscx, bridge, c8000, ceos, checkpoint_cloudguard, ciena_saos, cisco_asav, cisco_c8000, cisco_c8000v, cisco_cat9kv, cisco_csr1000v, cisco_ftdv, cisco_iol, cisco_n9kv, cisco_sdwan, cisco_vios, cisco_xrd, cisco_xrd_vrouter, cisco_xrv, cisco_xrv9k, cjunosevolved, crpd, cumulus_cvx, cvx, dell_ftosv, dell_sonic, ext-container, f5_bigip-ve, fdio_vpp, fortinet_fortigate, freebsd, generic_vm, host, huawei_vrp, ipinfusion_ocnos, juniper_cjunosevolved, juniper_crpd, juniper_csrx, juniper_vjunosevolved, juniper_vjunosrouter, juniper_vjunosswitch, juniper_vmx, juniper_vqfx, juniper_vsrx, k8s-kind, keysight_ixia-c-one, linux, mikrotik_ros, nokia_srlinux, nokia_sros, nokia_srsim, nvidia_cumulusvx, openbsd, openwrt, ovs-bridge, paloalto_panos, plvision_sonic, rare, sonic-vm, sonic-vs, spirent_stc, srl, veesix_osvbng, vr-aoscx, vr-arista_veos, vr-aruba_aoscx, vr-ciena_saos, vr-cisco_csr1000v, vr-cisco_n9kv, vr-cisco_xrv, vr-cisco_xrv9k, vr-csr, vr-dell_ftosv, vr-ftosv, vr-juniper_vmx, vr-juniper_vqfx, vr-juniper_vsrx, vr-mikrotik_ros, vr-n9kv, vr-nokia_sros, vr-paloalto_panos, vr-pan, vr-ros, vr-sros, vr-veos, vr-vmx, vr-vqfx, vr-vsrx, vr-xrv, vr-xrv9k, vyosnetworks_vyos, xrd"
```

## CTX-C168

Input: [CTX-C168.clab.yml](input/CTX-C168.clab.yml); SHA-256 `2756437438c725cbfdfbf52dc3bee7d9717d662e488aa00cd6cba954f2424591`.

**declarations:** `declarations_only`; 2 projected nodes, 1 declared links, 4 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 2 projected nodes, 1 declared links, 4 unresolved dependency references.

## F1

Input: [F1.clab.yml](input/F1.clab.yml); SHA-256 `c66a474ca9a9a4cba7de16c29dcc995219854418dc48e1b0ef13841c5aa50911`.

**declarations:** `declarations_only`; 4 projected nodes, 3 declared links, 4 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 4 projected nodes, 3 declared links, 4 unresolved dependency references.

## F2

Input: [F2.clab.yml](input/F2.clab.yml); SHA-256 `0cc94c3bb55a72190b7b486b636d3d6d2688d9f324fc254316fe6719b06e5a01`.

**declarations:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
yaml: unmarshal errors:
  line 12: field x-unknown not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to read topology file: yaml: unmarshal errors:
  line 12: field x-unknown not found in type types.NodeDefinitionWithDeprecatedFields
Consult with release notes to see if any fields were changed/removed
```

## F3

Input: [F3.clab.yml](input/F3.clab.yml); SHA-256 `225e7850232935fafc7a7f2a42011d9de2c43cff8784deaa9c45f10d6d80fb95`.

**declarations:** `declarations_only`; 1 projected nodes, 0 declared links, 2 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 1 projected nodes, 0 declared links, 2 unresolved dependency references.

## F4

Input: [F4.clab.yml](input/F4.clab.yml); SHA-256 `60e8976995c6ea25921fe80a251a4ba98ad420912a976452c6797d7d4e301c13`.

**declarations:** `declarations_only`; 1 projected nodes, 2 declared links, 3 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 1 projected nodes, 2 declared links, 3 unresolved dependency references.

## F5

Input: [F5.clab.yml](input/F5.clab.yml); SHA-256 `41385331a06c6dd1e520c177f91cbafe81e727810fc52c65f9f63fae391dd16d`.

**declarations:** `declarations_only`; 2 projected nodes, 2 declared links, 2 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 2 projected nodes, 2 declared links, 2 unresolved dependency references.

## F7

Input: [F7.clab.yml](input/F7.clab.yml); SHA-256 `614c345a6bd15cca1d0fb8ce072254ee21257fdb0c316af6441fda83ffbf56ef`.

**declarations:** `declarations_only`; 1 projected nodes, 1 declared links, 1 unresolved dependency references.

**skip-binds:** `resolved_with_unchecked_dependencies`; 1 projected nodes, 1 declared links, 1 unresolved dependency references.

## D1

Input: [D1.clab.yml](input/D1.clab.yml); SHA-256 `ebf9373308571245c4f6df3f1e5d54fd541e2266ef3c236355f6e8305b789b23`.

**declarations:** `declarations_only`; 3 projected nodes, 3 declared links, 9 unresolved dependency references.

**skip-binds:** `rejected`; 0 projected nodes, 0 declared links, 0 unresolved dependency references.

```text
failed to fetch http(s) resource: https://example.invalid/startup.cfg
```

## D2

Input: [D2.clab.yml](input/D2.clab.yml); SHA-256 `c1ecbd16ddf95683a954d0c9a15bee8bc2b2ebacb79db759fb200af46cb92267`.

**declarations:** `declarations_only`; 1 projected nodes, 1 declared links, 1 unresolved dependency references.

**skip-binds:** `link_resolution_failed`; 1 projected nodes, 1 declared links, 1 unresolved dependency references.

```text
unable to find node absent
```
