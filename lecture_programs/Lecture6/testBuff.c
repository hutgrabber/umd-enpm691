//gcc -m32 -g testBuff.c -o testBuff -fno-stack-protector -z execstack -no-pie -mpreferred-stack-boundary=2

#include <unistd.h>
#include<stdio.h>
 
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

