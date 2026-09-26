"""Fixed operations for one owned application runtime; native topology authority."""
from pathlib import Path
import os, sys, json, re, hashlib, base64, subprocess, tempfile, shutil, fcntl, time, signal
sys.path.insert(0, '/opt/clab-loader')
import runner
BASE = Path('/opt/clab-application')
PROJECTS = BASE / 'projects'
CODES = {'REQUEST_LIMIT','INVALID_REQUEST','RUNTIME_IDENTITY_MISMATCH','INVALID_PROJECT','BUSY','DEPLOYMENT_EXISTS','PROJECT_INVENTORY','PROJECT_LIMIT','SOURCE_HASH_MISMATCH','NATIVE_LAB_NAME_UNSUPPORTED','LAB_NAME_COLLISION','ASSOCIATION_CONFLICT','STOP_INCOMPLETE','INVALID_ACTION','NATIVE_TIMEOUT','OUTPUT_LIMIT','NATIVE_OPERATION_FAILED','CLEANUP_UNCONFIRMED','UNDECLARED_BUNDLE_FILE','WORKER_TIMEOUT','WORKER_EXIT','MALFORMED_OUTPUT','CANCELLED','CAPTURE_FAILED','CAPTURE_TIMEOUT','CAPTURE_UNSUPPORTED','MALFORMED_CAPTURE','MALFORMED_ANALYSIS','ARTIFACT_MISMATCH','LUA_INTEGRITY'}
def digest(b): return hashlib.sha256(b).hexdigest()
def fail(code): raise ValueError(code)
def write(path, value):
    tmp = path.with_suffix('.tmp')
    with open(tmp, 'w', opener=lambda p, f: os.open(p, f, 0o600)) as f:
        json.dump(value, f); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
def native(args, seconds=120):
    # Never disclose unrestricted native stderr. Bound disk output in the child.
    def limits():
        import resource
        resource.setrlimit(resource.RLIMIT_FSIZE, (2097152, 2097152))
    with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
        proc = subprocess.Popen(['/usr/local/bin/containerlab', *args], stdout=out, stderr=err, start_new_session=True, preexec_fn=limits, env={'PATH':'/usr/local/bin:/usr/bin:/bin','HOME':'/root','CLAB_LABDIR_BASE':str(BASE/'labs')})
        start = time.monotonic()
        try:
            while proc.poll() is None:
                if time.monotonic()-start > seconds: fail('NATIVE_TIMEOUT')
                if os.fstat(out.fileno()).st_size+os.fstat(err.fileno()).st_size > 2097152: fail('OUTPUT_LIMIT')
                time.sleep(.05)
            if os.fstat(out.fileno()).st_size+os.fstat(err.fileno()).st_size > 2097152: fail('OUTPUT_LIMIT')
            if proc.returncode: fail('NATIVE_OPERATION_FAILED')
            out.seek(0); return out.read(2097153)
        finally:
            if proc.poll() is None: os.killpg(proc.pid, signal.SIGKILL); proc.wait()
def inventory(name):
    result = json.loads(native(['inspect', '--all', '--details'], 20))
    if not isinstance(result, dict): fail('MALFORMED_OUTPUT')
    rows = result.get(name, [])
    if not isinstance(rows, list) or len(rows)>256: fail('MALFORMED_OUTPUT')
    return rows

def identities(rows, name, topology):
    # The native topology-file label proves attribution after a failed attempt.
    result = []
    for row in rows:
        labels = row.get('Labels', {})
        cid = row.get('ID')
        if not isinstance(cid, str) or not re.fullmatch('[a-f0-9]{64}', cid): fail('ASSOCIATION_CONFLICT')
        if labels.get('containerlab') != name or labels.get('clab-topo-file') != topology: fail('ASSOCIATION_CONFLICT')
        result.append(cid)
    if len(set(result)) != len(result): fail('ASSOCIATION_CONFLICT')
    return sorted(result)

def validate_files(record, encoded, project):
    if not isinstance(record, dict) or record.get('id') != project or not isinstance(encoded, dict): fail('INVALID_PROJECT')
    files = record.get('files')
    if not isinstance(files, list) or not 1<=len(files)<=32: fail('PROJECT_INVENTORY')
    entry = runner.safe_path(record.get('entry'))
    data = {}; total = 0
    for item in files:
        if not isinstance(item, dict) or set(item)!={'path','sha256'}: fail('PROJECT_INVENTORY')
        name = runner.safe_path(item['path'])
        if name in data or name not in encoded: fail('PROJECT_INVENTORY')
        value = base64.b64decode(encoded[name], validate=True); total += len(value)
        if len(value)>1048576 or total>4194304: fail('PROJECT_LIMIT')
        if digest(value) != item['sha256']: fail('SOURCE_HASH_MISMATCH')
        data[name] = value
    if set(encoded)!=set(data) or entry not in data: fail('PROJECT_INVENTORY')
    canonical = json.dumps({'entry':entry,'files':files}, sort_keys=True, separators=(',',':')).encode()
    if digest(canonical)!=record.get('bundleSha256'): fail('SOURCE_HASH_MISMATCH')
    return data

def operate(q):
    owner = json.loads((BASE/'owner.json').read_text())
    if not isinstance(q, dict) or q.get('owner')!=owner['id']: fail('RUNTIME_IDENTITY_MISMATCH')
    action = q.get('action')
    if action not in ['status','load','deploy','stop','inspect','logs','observe','capture','analyze']: fail('INVALID_ACTION')
    required = {'owner','action'} if action=='status' else {'owner','action','project'}
    if action=='load': required |= {'record','files','job'}
    if action=='logs': required |= {'containerId'}
    if action=='observe': required |= {'plan'}
    if action=='capture': required |= {'plan','input'}
    if action=='analyze': required |= {'input'}
    if set(q)!=required: fail('INVALID_REQUEST')
    if action=='status': return {'owner':owner['id'],'nativeSha256':digest(Path('/usr/local/bin/containerlab').read_bytes())}
    project = q['project']
    if not isinstance(project, str) or not re.fullmatch('project-[a-f0-9]{24}', project): fail('INVALID_PROJECT')
    PROJECTS.mkdir(mode=0o700, exist_ok=True); folder = PROJECTS/project
    if folder.is_symlink(): fail('INVALID_PROJECT')
    with open(BASE/'operation.lock','w') as lock:
        try: fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: fail('BUSY')
        if action=='load':
            job = q['job']
            if not isinstance(job,str) or not re.fullmatch('[a-f0-9]{32}',job): fail('INVALID_REQUEST')
            record = q['record']; data = validate_files(record,q['files'],project)
            if not folder.exists() and sum(p.is_dir() for p in PROJECTS.iterdir())>=8: fail('PROJECT_LIMIT')
            if folder.exists():
                if (folder/'deployment.json').exists(): fail('DEPLOYMENT_EXISTS')
                shutil.rmtree(folder)
            folder.mkdir(mode=0o700); inputs=folder/'input'; inputs.mkdir()
            for name,value in data.items():
                path=inputs/name; path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(value); path.chmod(0o444)
            try:
                runner.RUN.mkdir(mode=0o700,exist_ok=True)
                # tmpfs bounds worker scratch, including output written directly to /tmp.
                scratch=folder/'scratch'; scratch.mkdir()
                subprocess.run(['mount','-t','tmpfs','-o','size=16m,mode=0777,nosuid,nodev','clab-app-scratch',str(scratch)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                try: result=runner.execute(folder,record['entry'],job)
                finally: subprocess.run(['umount',str(scratch)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            finally:
                scratch=folder/'scratch'
                if scratch.exists() and not os.path.ismount(scratch): shutil.rmtree(scratch)
            write(folder/'record.json',record)
            if result.get('status')=='declarations_only':
                name=result.get('lab_name')
                if not isinstance(name,str) or not re.fullmatch('[A-Za-z0-9][A-Za-z0-9_.-]{0,127}',name): fail('NATIVE_LAB_NAME_UNSUPPORTED')
                (folder/'lab-name').write_text(name)
            return {'ok':True,'jobId':job,'bundleId':project,'bundleSha256':record['bundleSha256'],'summary':result,'workerSha256':digest(Path('/opt/clab-loader/worker').read_bytes()),'cleanup':'complete'}
        record=json.loads((folder/'record.json').read_text())
        runner.bundle_bytes(folder/'input',record) # Refuse mutated guest snapshots before any lifecycle action.
        name=(folder/'lab-name').read_text(); topology=str(folder/'input'/record['entry'])
        statefile=folder/'deployment.json'
        if action=='deploy':
            if statefile.exists(): fail('DEPLOYMENT_EXISTS')
            if inventory(name): fail('LAB_NAME_COLLISION')
            write(statefile,{'labName':name,'status':'deploying','ids':None})
            error=None
            try: native(['deploy','--topo',topology],300)
            except Exception as e: error=e
            # Preserve failed attempts and establish exact scoped recovery IDs.
            try:
                rows=inventory(name); ids=identities(rows,name,topology)
                write(statefile,{'labName':name,'status':'partial' if error else 'running','ids':ids})
            except Exception: fail('CLEANUP_UNCONFIRMED')
            if error: raise error
            return {'labName':name,'inventory':{name:rows}}
        state=json.loads(statefile.read_text()); rows=inventory(name)
        current=identities(rows,name,topology)
        if not isinstance(state.get('ids'),list) or any(cid not in state['ids'] for cid in current): fail('ASSOCIATION_CONFLICT')
        if action in ['observe','capture']:
            plan=q['plan'];deployment=plan.get('deployment',{})
            if deployment.get('labName')!=name or sorted(c.get('id','') for c in deployment.get('containers',[]))!=state['ids']: fail('ASSOCIATION_CONFLICT')
            if plan.get('bundleSha256')!=record['bundleSha256']: fail('ASSOCIATION_CONFLICT')
            write(Path('/opt/clab-observation-plan.json'),plan)
            sys.path.insert(0,'/opt/clab-observer')
            import importlib.util
            spec=importlib.util.spec_from_file_location('native_observer','/opt/clab-observer.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
            if action=='observe': return module.inspect()
            spec=importlib.util.spec_from_file_location('capture','/opt/clab-capture.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
            return module.collect(q['input'])
        if action=='analyze':
            sys.path.insert(0,'/opt/clab-observer')
            import importlib.util
            spec=importlib.util.spec_from_file_location('analysis','/opt/clab-reanalysis.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
            return module.analyze(q['input'])
        if action=='logs':
            cid=q['containerId']
            if cid not in current: fail('ASSOCIATION_CONFLICT')
            sys.path.insert(0,'/opt/clab-observer')
            from logs import tail
            from reader import Reader
            text,truncated=tail(cid,Reader())
            after=identities(inventory(name),name,topology)
            if after!=current: fail('ASSOCIATION_CONFLICT')
            return {'text':text,'truncated':truncated}
        if action=='inspect': return {'labName':name,'inventory':{name:rows},'status':state['status']}
        native(['destroy','--topo',topology,'--cleanup'],120)
        if inventory(name): fail('STOP_INCOMPLETE')
        statefile.unlink(); return {'stopped':True}

def main():
    raw=sys.stdin.buffer.read(6000001)
    if len(raw)>6000000: fail('REQUEST_LIMIT')
    return operate(json.loads(raw))
if __name__=='__main__':
    try: print(json.dumps({'ok':True,**main()},separators=(',',':')))
    except Exception as e: print(json.dumps({'ok':False,'code':str(e) if str(e) in CODES else 'RUNTIME_OPERATION_FAILED'}))
