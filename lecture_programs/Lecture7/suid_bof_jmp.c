//gcc -m32 -g suid_bof_jmp.c -o suid_bof_jmp -fno-stack-protector -z execstack -no-pie -mpreferred-stack-boundary=2

#include <string.h>


void jmpesp()
{
    __asm__("jmp *%esp");
}

void copyData( char *arg)
{
    char buffer[80];
    strcpy(buffer, arg);
}

int main(int argc, char *argv[ ])
{
   copyData( argv[1] );
   return 0;
}

