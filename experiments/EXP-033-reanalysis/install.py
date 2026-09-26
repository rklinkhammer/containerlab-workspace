from pathlib import Path
import subprocess,json,os
r=Path(__file__).resolve().parents[2];os.chdir(r)
d=Path((r/'experiments/EXP-033-reanalysis/session-path.txt').read_text().strip());s=json.loads((d/'observation-session.json').read_text());vm=s['vm']
def run(*args):subprocess.run(args,check=True)
def guest(*args):run('limactl','shell',vm,*args)
guest('sudo','env','DEBIAN_FRONTEND=noninteractive','apt-get','install','-y','tshark=4.2.2-1.1build3','wireshark-common=4.2.2-1.1build3')
run('limactl','copy','native/observer/capture.py',vm+':/tmp/clab-capture.py');guest('sudo','install','-m755','/tmp/clab-capture.py','/opt/clab-capture.py')
run('limactl','copy','-r','native/analysis',vm+':/tmp/exp033-analysis');guest('sudo','python3','/tmp/exp033-analysis/install.py','/tmp/exp033-analysis')
run('limactl','copy','native/analysis/reanalyze.py',vm+':/tmp/clab-reanalysis.py');guest('sudo','install','-m755','/tmp/clab-reanalysis.py','/opt/clab-reanalysis.py')
guest('dpkg-query','-W','-f=${Package} ${Version}\n','tshark','wireshark-common','systemd');guest('sha256sum','/opt/clab-capture.py','/opt/clab-reanalysis.py','/usr/bin/tshark','/opt/clab-analysis-manifest.json')
