//gcc -m32 -g smallBuff.c -o smallBuff -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic

#include <stdio.h>
#include <string.h>
 
 
int main(int argc, char *argv[ ])
{
   char buffer[4];
   gets(buffer);
   return 0;
}

