;to compile:
;nasm -f elf32 jmpCMOV.asm

;to link:
;ld -m elf_i386 jmpCMOV.o -o jmpCMOV


section .text

global _start


_jmpSection:
    dec ecx
    cmp ecx, 0x5     ; SF flag will be set
    push 0xc0ffee
    push 0xd3caff
    cmovl ebx, [esp+4] ; second arg is r/m 
    cmovg eax, [esp]
    jmp _end
    
_start:
    mov eax, 0x0
    mov ecx, 0x5
    test eax, eax ; this will set ZF
    je _jmpSection

    inc ecx
    nop
    nop

_end:
    push ebx
    nop




