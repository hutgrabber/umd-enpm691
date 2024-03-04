;to compile:
;nasm -f elf32 movlea.asm

;to link:
;ld -m elf_i386 movlea.o -o movlea


section .text

global _start

_start:
    PUSH 0xc0ffee
    PUSH 0xdecaff
    MOV EAX, [ESP + 4]
    LEA EBX, [ESP + 4]

    MOV ECX, 2
    MOV EDX, 3
    LEA ESI, [ECX*2 + EDX + 1]

