;to compile:
;nasm -f elf32 logical.asm

;to link:
;ld -m elf_i386 logical.o -o logical


section .text

global _start

_start:
    mov eax, 0xffffeeee ; eax=0xffffeeee=y
    mov ebx, 3  ; ebx=3=x


	xor eax, ebx ; eax = x^y (t1)
	sar eax, 17  ; eax = t1>>17 (t2) 
    and eax, 8185; eax = t2 & mask (rval)


