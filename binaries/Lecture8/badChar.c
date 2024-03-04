// gcc -m32 badChar.c -o badChar -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -z execstack

#include <string.h>
#include <stdio.h>

void copyData( char *arg)
{
    char buffer[150];
    strcpy(buffer, arg);
}

void jmpesp()
{
    __asm__("jmp *%esp");
}

int main()
{
   char inputBuffer[300];
   printf("Enter a string!");
   scanf("%s", &inputBuffer);
   copyData(inputBuffer);
   return 0;
}

