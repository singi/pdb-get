#!/usr/bin/python3

import os
import sys
import subprocess

SYMCHK = r"C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\symchk.exe"
SYMPATH = r"SRV*C:\symbols*https://msdl.microsoft.com/download/symbols;SRV*C:\symbols*https://chromium-browser-symsrv.commondatastorage.googleapis.com"

def get_pdb(path):
    cmd = "{0} {1} /s {2}".format(SYMCHK, path, SYMPATH)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.poll()

    res = ""
    for l in p.stdout.readlines():
        res += l.decode("utf-8")
    print(res)

if __name__ == '__main__':
    if os.path.isfile(SYMCHK) != True:
        print("symchk not found.")
        sys.exit(0)

    if len(sys.argv) != 2:
        print("need dll path for get pdb file.")
        sys.exit(0)

    get_pdb(sys.argv[1])

    print("[+] Done.")

