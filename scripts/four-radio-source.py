#!/usr/bin/env python3
"""Recreate the qualified private build snapshot from hash-matching sibling sources."""
import pathlib,json,hashlib,shutil
r=pathlib.Path(__file__).resolve().parents[1];source=r.parent/'containerlab-vrt';dest=r/'.runtime/exp026-source'
p=json.loads((r/'experiments/EXP-026-four-radio/source-provenance.json').read_text())
# Verify everything before changing the snapshot; this is not source admission.
for f in p['files']:
 s=source/f['path']
 if s.is_symlink() or not s.is_file() or hashlib.sha256(s.read_bytes()).hexdigest()!=f['sha256']:raise SystemExit('Source differs from qualified snapshot: '+f['path'])
for f in p['files']:
 s=source/f['path'];d=dest/f['path'];d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(s,d);d.chmod(s.stat().st_mode)
print('Qualified exact-byte private source snapshot ready')
