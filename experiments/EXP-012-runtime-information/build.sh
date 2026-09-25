#!/bin/bash
set -eu
umask 077
mkdir -p /tmp/exp012/source /tmp/exp012/bin
cd /tmp/exp012
curl --location --fail --silent --show-error --max-time 180 https://go.dev/dl/go1.27.1.linux-arm64.tar.gz -o go.tar.gz
printf '%s\n' '3450b45a3f9ee8568792736a5c5e70a1f2e9b36c35a8f74958c03e51d7d92bec  go.tar.gz' | sha256sum -c -
tar -xzf go.tar.gz
tar -xf native.tar -C source
mkdir -p source/exp012
cp main.go source/exp012/main.go
cd source
export PATH=/tmp/exp012/go/bin:$PATH
export GOTOOLCHAIN=local
go version
timeout -k 5 900 go build -mod=readonly -o /tmp/exp012/bin/probe ./exp012
timeout -k 5 900 go build -mod=readonly -o /tmp/exp012/bin/containerlab .
sha256sum /tmp/exp012/bin/*
