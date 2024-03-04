//gcc -g testBuffC64.c -o testBuffC64 -z execstack -no-pie -mpreferred-stack-boundary=4 -fno-pic -fstack-protector-all

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

