;to compile:
;nasm -f elf32 endian.asm

;to link:
;ld -m elf_i386 endian.o -o endian

section .text

global _start

_start:
    PUSH 0x11223344
    PUSH 0x55667788
    PUSH 0x99aabbcc
    PUSH 0xddeeff00
    NOP

; in GDB
; break _start    
; run
; step
;x/bx $esp
;x/bx $esp+1
;x/bx $esp+2
;x/bx $esp+3
