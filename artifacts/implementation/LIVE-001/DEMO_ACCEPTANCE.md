# Selected official-demo acceptance — before execution

Pinned source: Containerlab `5ae50094a3afd70e4e1674fe5385e64d8979da26`.
The historical 177-case denominator remains unchanged. These cases are external
qualification inputs; they are not application package contents.

| Input | Independent native declaration expectations | Coverage / deployment prerequisite |
|---|---|---|
| C042 `lab-examples/srl-quickstart/srl01.clab.yml` | `srl`: nokia_srlinux; zero links | Disconnected native NOS. Upstream environment defaults reference a mutable image; deployment needs an explicit reviewed image profile. |
| C043 `lab-examples/srl-quickstart/srl02.clab.yml` | `srl1`, `srl2`: nokia_srlinux; two distinct veth occurrences joining e1-1/e1-1 and e1-2/e1-2 | Parallel links/native aliases. Same image-profile prerequisite. |
| C023 `lab-examples/frr01/frr01.clab.yml` | router1/2/3 and PC1/2/3: linux; six exact links from source | Native group inheritance, six explicitly inventoried router companion files. Image architectures/acquisition require separate deployment qualification. |
| C002 `lab-examples/br01/br01.clab.yml` | srl1/2/3: nokia_srlinux, br-clab: bridge; three links to distinct bridge ports | External bridge prerequisite must remain explicit; never fabricate the bridge during loading. |

The separate user example is `../containerlab-vrt/generated/four-radio.clab.yml`:
8 nodes (radio1–4, processor, detector, recorder, switch1), seven veth links.
Its original bytes remain unchanged. Local VRT image acquisition and SR Linux
image acquisition are deployment prerequisites, not declaration failures.

For this continuation, first execute native loading and verify individual node
kinds and endpoint pairs. Record deployment, observation, logs, capture and
installed E2E independently. Loading alone passes none of those stages.
