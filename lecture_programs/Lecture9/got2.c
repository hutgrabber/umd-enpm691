//gcc -m32 got2.c -o got2 -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -Wl,-z,norelro 


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
   char buffer[32];
   gets(buffer);
   printf("Your data is %d bytes.\n", strlen(buffer)); 
   puts(buffer);
   return 0;
}
