;to compile:
;nasm -f elf32 arith.asm

;to link:
;ld -m elf_i386 arith.o -o arith


section .text

global _start

_start:
    mov ECX, 4 ; ecx = x = 4
    mov EDX, 3 ; edx = y = 3
    mov EBP, 1 ; ebp = x = 1 (modified from slide)

    lea eax, [edx + edx * 2] ; eax = y*3
	sal eax, 4               ; eax *= 16 (t4)
    lea eax, [ecx + 4 + eax] ; eax = t4 +x+4 (t5)
    add edx, ecx             ; edx = x+y (t1)
    add edx, ebp             ; edx += z (t2) (modified from slide)
    imul eax, edx            ; t2 * t5 (rval)

