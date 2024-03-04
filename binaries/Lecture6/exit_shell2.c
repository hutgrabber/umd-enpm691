//gcc -m32 -g exit_shell2.c -o exit_shell2 -fno-stack-protector -no-pie -z execstack
//
#include<stdio.h>
#include<string.h>

/* shellcode  for sum of two numbers */
int main(int argc, char **argv)
{
    char shellcode[] = "\xb8\x01\x00\x00\x00"
                       "\xbb\x02\x00\x00\x00"
                       "\xcd\x80";

   int (*shell)(void) = (void *)&shellcode;
   return shell();
}


