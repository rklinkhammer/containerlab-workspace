#!/usr/bin/python3
"""Disposable fixed ARM boot fixture. No native topology or network semantics."""
import os,subprocess,shutil
os.makedirs('/run/appliance',exist_ok=True)
shutil.copyfile('/usr/share/AAVMF/AAVMF_VARS.fd','/run/appliance/vars.fd')
subprocess.run(['qemu-img','create','-f','qcow2','-F','qcow2','-b','/opt/guest.img','/run/appliance/disk.qcow2'],check=True,stdout=subprocess.DEVNULL)
os.execvp('qemu-system-aarch64',['qemu-system-aarch64','-accel','kvm','-cpu','host','-machine','virt','-smp','2','-m','768','-display','none','-nodefaults','-no-reboot','-drive','if=pflash,format=raw,readonly=on,file=/usr/share/AAVMF/AAVMF_CODE.fd','-drive','if=pflash,format=raw,file=/run/appliance/vars.fd','-drive','if=none,id=osdisk,file=/run/appliance/disk.qcow2,format=qcow2','-device','virtio-blk-pci,drive=osdisk','-drive','if=none,id=seed,file=/opt/seed.iso,format=raw,readonly=on','-device','virtio-blk-pci,drive=seed','-chardev','socket,id=serial0,path=/run/appliance/serial.sock,server=on,wait=off,logfile=/run/appliance/serial.log','-serial','chardev:serial0','-qmp','unix:/run/appliance/qmp.sock,server=on,wait=off'])
