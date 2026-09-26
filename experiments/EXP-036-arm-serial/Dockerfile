FROM ubuntu@sha256:008173c23f95b170204355c12626cb5a965d779a7e1283b09e9cffbb1bf33ca3
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends qemu-system-arm=1:8.2.2+ds-0ubuntu1.18 qemu-utils=1:8.2.2+ds-0ubuntu1.18 qemu-efi-aarch64=2024.02-2ubuntu0.9 python3=3.12.3-0ubuntu2.1 && rm -rf /var/lib/apt/lists/*
COPY guest.img seed.iso /opt/
COPY launcher.py qmp_probe.py /opt/
ENTRYPOINT ["/usr/bin/python3", "/opt/launcher.py"]
