# Executed commands

Executed from the implementation workspace. All Lima commands target only the new experiment VM.

```sh
limactl start --name=clab-errors-20260925-013725-exp014 --tty=false experiments/EXP-014-specific-errors/lima.yaml
limactl shell clab-errors-20260925-013725-exp014 mkdir -p /tmp/exp014
limactl copy /tmp/clab-exp011-native.tar clab-errors-20260925-013725-exp014:/tmp/exp014/native.tar
limactl copy experiments/EXP-014-specific-errors/build.sh experiments/EXP-014-specific-errors/main.go experiments/EXP-014-specific-errors/facade.py experiments/EXP-014-specific-errors/run.py experiments/EXP-014-specific-errors/input-manifest.json clab-errors-20260925-013725-exp014:/tmp/exp014/
limactl copy -r experiments/EXP-014-specific-errors/input clab-errors-20260925-013725-exp014:/tmp/exp014/
limactl shell clab-errors-20260925-013725-exp014 bash /tmp/exp014/build.sh
limactl shell clab-errors-20260925-013725-exp014 python3 /tmp/exp014/run.py
limactl copy clab-errors-20260925-013725-exp014:/tmp/exp014/results.json experiments/EXP-014-specific-errors/results.json
python3 experiments/EXP-014-specific-errors/check.py
limactl shell clab-errors-20260925-013725-exp014 bash -c 'sudo systemctl stop docker.service docker.socket containerd.service; sudo systemctl is-active docker.service docker.socket containerd.service; mountpoint /tmp/exp014/scratch; systemctl list-units --all --no-legend "exp014-job-*"'
limactl stop clab-errors-20260925-013725-exp014
limactl list clab-errors-20260925-013725-exp014 --json
```

Start/build/run/cleanup/stop outputs were redirected to their named evidence logs; final state to final-vm.json. The source tar was reused as an inert host file, hash-verified against the original pin; no prior VM was used. Do not rerun these commands against this now-pre-existing stopped VM: choose a fresh VM name for another trial.
