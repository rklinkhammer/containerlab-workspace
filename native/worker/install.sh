#!/bin/bash
set -eu
sudo install -d -m 755 /opt/clab-loader /opt/clab-loader/etc
sudo install -m 755 /tmp/exp016/bin/probe /opt/clab-loader/worker
sudo install -m 644 /tmp/exp016/runner.py /opt/clab-loader/runner.py
sudo cp -R /tmp/exp016/bundles /opt/clab-loader/bundles
sudo chown -R root:root /opt/clab-loader
sudo chmod -R go-w /opt/clab-loader
sudo install -m 600 /tmp/exp016/session.txt /opt/clab-loader/session.txt
printf 'nobody:x:65534:65534:nobody:/tmp:/usr/sbin/nologin\n' | sudo tee /opt/clab-loader/etc/passwd >/dev/null
printf 'nogroup:x:65534:\n' | sudo tee /opt/clab-loader/etc/group >/dev/null
printf '' | sudo tee /opt/clab-loader/etc/resolv.conf >/dev/null
