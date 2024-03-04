//gcc -m32 -g sum_shell.c -o sum_shell -fno-stack-protector -no-pie -z execstack
//
#include<stdio.h>
#include<string.h>

/* shellcode  for sum of two numbers */
int main(int argc, char **argv)
{
    char shellcode[] = "\x55"
                   "\x89\xe5"
                   "\x83\xec\x04"
                   "\x8b\x45\x0c"
                   "\x8b\x55\x08"
                   "\x01\xd0"
                   "\x89\x45\xfc"
                   "\x8b\x45\xfc"
                   "\xc9"
                   "\xc3";


   int (*shell)(int, int) = (void *)&shellcode;
   return shell(1, 2);
}


