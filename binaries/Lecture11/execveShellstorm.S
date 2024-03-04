//https://shell-storm.org/shellcode/files/shellcode-827.html 
// execve('/bin/sh') in 23 bytes

//as --32 execveShellstorm.S -o execveShellstorm.o
//ld -m elf_i386 execveShellstorm.o -o execveShellstorm

.section .data

.section .text
.globl _start
_start:

xor %eax,%eax
push %eax 
push $0x68732f2f 
push $0x6e69622f 
mov %esp,%ebx 
push %eax 
push %ebx 
mov %esp,%ecx 
mov $0xb,%al 
int $0x80



