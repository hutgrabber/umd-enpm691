;to compile:
;nasm -f elf32 exit2.asm

;to link:
;ld -m elf_i386 exit2.o -o exit2

section .text

global _start

_start:
    mov eax, 1
    mov ebx, 2
    int 0x80
