//gcc -m32 -g rop1.c -o rop1  -no-pie -mpreferred-stack-boundary=2 -fno-pic -fno-stack-protector

#include <unistd.h>
#include <stdio.h>
 
void Test()
{
   char buff[12];
   gets(buff);
   puts(buff);
}
 
void gogoGadget()
{
    __asm__("pop %eax; ret");
    __asm__("pop %ebx; mov $100, %esi; ret");
    __asm__("pop %ecx; mov $0xffffffff, %ebx;  ret");
    __asm__("mov $0x0, %edx; inc %edx; ret");
    __asm__("dec %edx; ret");
    __asm__("int $0x80; nop; nop; ret");
}

int main(int argc, char *argv[ ])
{
   char * myString = "/bin/sh";
   printf(myString);
   printf(" is a great command, isn't it?\n");
   
   Test();
   return 0;
}

