#!/bin/bash
set -eu
umask 077
mkdir -p /tmp/exp015/source /tmp/exp015/bin
cd /tmp/exp015
curl --location --fail --silent --show-error --max-time 180 https://go.dev/dl/go1.27.1.linux-arm64.tar.gz -o go.tar.gz
printf '%s\n' '3450b45a3f9ee8568792736a5c5e70a1f2e9b36c35a8f74958c03e51d7d92bec  go.tar.gz' | sha256sum -c -
tar -xzf go.tar.gz
printf '%s\n' 'd7f0ce9cd64e7427777e1aba901f89d7207e25a04391dd14286da4b0b952a45e  native.tar' | sha256sum -c -
tar -xf native.tar -C source
mkdir -p source/exp015
cp main.go source/exp015/main.go
cd source
export PATH=/tmp/exp015/go/bin:$PATH
export GOTOOLCHAIN=local
go version
timeout -k 5 900 go build -mod=readonly -o /tmp/exp015/bin/probe ./exp015
sha256sum /tmp/exp015/bin/*
