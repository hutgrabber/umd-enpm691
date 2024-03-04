//gcc -m32 -g testBuffC.c -o testBuffC -z execstack -no-pie -mpreferred-stack-boundary=2 -fno-pic -fstack-protector

#include <unistd.h>
#include <stdio.h>
 
void Test()
{
   char buff[4];
   gets(buff);
   puts(buff);
}
 
int main(int argc, char *argv[ ])
{
   Test();
   return 0;
}

