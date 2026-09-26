"""Experimental fixed-image read-only serial classifier, not a public API.

Caller must collect before/after identity from the runtime, not user input.
An available result identifies backing only; it grants no transport capability.
"""
import json

def classify(expected, before, after, argv, inventory, checked_at, now, complete=True):
    if before != expected or after != expected:
        return {'status':'conflict','reason':'IDENTITY_CHANGED','consoles':[]}
    if not isinstance(now,(int,float)) or not isinstance(checked_at,(int,float)) or not 0 <= now-checked_at <= 15:
        return {'status':'stale','reason':'EVIDENCE_EXPIRED','consoles':[]}
    if not complete:
        return {'status':'unchecked','reason':'INCOMPLETE_INVENTORY','consoles':[]}
    if not isinstance(argv,list) or not all(isinstance(x,str) for x in argv) or len(json.dumps([argv,inventory]))>65536:
        return {'status':'unavailable','reason':'MALFORMED_OR_LIMIT','consoles':[]}
    if not isinstance(inventory,dict) or not isinstance(inventory.get('chardev'),list):
        return {'status':'unavailable','reason':'MALFORMED_INVENTORY','consoles':[]}
    if len(inventory['chardev'])>16 or not all(isinstance(x,dict) and isinstance(x.get('label'),str) and isinstance(x.get('filename'),str) for x in inventory['chardev']):
        return {'status':'unavailable','reason':'MALFORMED_INVENTORY','consoles':[]}
    if not argv or argv[0]!='qemu-system-aarch64':
        return {'status':'unsupported','reason':'PROCESS_PROFILE_UNSUPPORTED','consoles':[]}
    labels=[x['label'] for x in inventory['chardev']]
    if len(labels)!=len(set(labels)):
        return {'status':'unavailable','reason':'AMBIGUOUS_INVENTORY','consoles':[]}
    # Exact reviewed serial selector, not arbitrary listener/monitor detection.
    selectors=[argv[i+1] for i,x in enumerate(argv[:-1]) if x=='-serial']
    if selectors!=['chardev:serial0']:
        return {'status':'unsupported','reason':'SERIAL_MAPPING_UNQUALIFIED','consoles':[]}
    rows=[x for x in inventory['chardev'] if x['label']=='serial0']
    if len(rows)!=1 or '/run/appliance/serial.sock' not in rows[0]['filename'] or not rows[0]['filename'].startswith('unix:') or rows[0].get('frontend-open') is not True:
        return {'status':'unavailable','reason':'SERIAL_BACKING_UNCONFIRMED','consoles':[]}
    return {'status':'available','reason':'FIXED_IMAGE_SERIAL_BACKING','consoles':[{'label':'Guest serial 0'}]}
