;to compile:
;nasm -f elf32 arithmetic1.asm

;to link:
;ld -m elf_i386 arithmetic1.o -o arithmetic1


section .text

global _start

_start:
    MOV EAX, 0x5555
    MOV ECX, 0x2

    PUSH EAX
    PUSH ECX

    MOV ECX, 0x42

    INC EAX
    INC EAX

    ADD EAX, ECX
    ADD EAX, DWORD [ESP]

    SUB EAX, 0x4444
    MUL ECX

    NOP
    NOP
    NOP
