//gcc -m32 -g exit_shell.c -o exit_shell -fno-stack-protector -no-pie -z execstack
//
#include<stdio.h>
#include<string.h>

//shellcode for exit(2)
int main(int argc, char **argv)
{
    char shellcode[] = "\xb8\x01\x00\x00\x00"
                       "\xbb\x02\x00\x00\x00"
                       "\xcd\x80";
    
    int *ret;
    ret = (int *)&ret + 6;
    (*ret) = (int)shellcode;
}


