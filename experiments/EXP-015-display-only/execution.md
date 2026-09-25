# Executed commands

Executed from the implementation workspace. All Lima commands target only the new experiment VM.

```sh
limactl start --name=clab-display-20260925-014338-exp015 --tty=false experiments/EXP-015-display-only/lima.yaml
limactl shell clab-display-20260925-014338-exp015 mkdir -p /tmp/exp015
limactl copy /tmp/clab-exp011-native.tar clab-display-20260925-014338-exp015:/tmp/exp015/native.tar
limactl copy experiments/EXP-015-display-only/build.sh experiments/EXP-015-display-only/main.go experiments/EXP-015-display-only/facade.py experiments/EXP-015-display-only/run.py experiments/EXP-015-display-only/input-manifest.json clab-display-20260925-014338-exp015:/tmp/exp015/
limactl copy -r experiments/EXP-015-display-only/input clab-display-20260925-014338-exp015:/tmp/exp015/
limactl shell clab-display-20260925-014338-exp015 bash /tmp/exp015/build.sh
limactl shell clab-display-20260925-014338-exp015 python3 /tmp/exp015/run.py
limactl copy clab-display-20260925-014338-exp015:/tmp/exp015/results.json experiments/EXP-015-display-only/results.json
python3 experiments/EXP-015-display-only/check.py
limactl shell clab-display-20260925-014338-exp015 bash -c 'sudo systemctl stop docker.service docker.socket containerd.service; sudo systemctl is-active docker.service docker.socket containerd.service; mountpoint /tmp/exp015/scratch; systemctl list-units --all --no-legend "exp014-job-*"'
limactl stop clab-display-20260925-014338-exp015
limactl list clab-display-20260925-014338-exp015 --json
```

Start/build/run/cleanup/stop outputs were redirected to their named evidence logs; final state to final-vm.json. The source tar was reused as an inert host file, hash-verified against the original pin; no prior VM was used. Do not rerun these commands against this now-pre-existing stopped VM: choose a fresh VM name for another trial.
