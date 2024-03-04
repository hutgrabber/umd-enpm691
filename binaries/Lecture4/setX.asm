;to compile:
;nasm -f elf32 setX.asm

;to link:
;ld -m elf_i386 setX.o -o setX 


section .text

global _start

_start:
    mov eax, 0x0
    mov ebx, 0xffffffff
    test eax, eax ; this will set ZF

    sete bl ; setting bl, lower 8 bytes to 0x1
    movzx ebx, bl



