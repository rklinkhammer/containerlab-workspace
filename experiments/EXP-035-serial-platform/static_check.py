from pathlib import Path
import json,hashlib,ast
p=Path(__file__).resolve().parent;s=p/'sources';h=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
for row in json.loads((s/'MANIFEST.json').read_text()):assert h(s/row['path'].replace('/','__'))==row['sha256']
tree=ast.parse((s/'common__vrnetlab.py').read_text());vm=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='VM');init=next(n for n in vm.body if isinstance(n,ast.FunctionDef) and n.name=='__init__');defaults=dict(zip([x.arg for x in init.args.args][-len(init.args.defaults):],init.args.defaults));assert ast.literal_eval(defaults['arch'])=='x86_64'
x=json.loads((s/'base-image.json').read_text());assert h(s/'base-image-config.json')==x['config']['digest'].split(':')[1];assert json.loads((s/'base-image-config.json').read_text())['architecture']=='amd64'
assert h(s/'base-image.json')=='57f36ae1cf44a78a6b2cad35a6276565c56edfd28e8160ae9a772929db28fd6d'
assert '7df0201546f75b8bcc1044594c806c35749421ad3c9bc1be2a3ab806cfae39cc *ubuntu-24.04-server-cloudimg-arm64.img' in (s/'ubuntu-SHA256SUMS').read_text()
print('PASS: pinned sources, x86 default, immutable AMD64 base metadata and published ARM candidate checksum')
