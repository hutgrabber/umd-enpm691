// gcc -m32 offby1.c -o offby1 -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -z execstack


#include<stdio.h>
#include<string.h>

void save(char* str)
{
   char buff[256];
   strncpy(buff, str, strlen(str)+1);
}

void function(char* str)
{
   save(str);
}

int main(int argc, char* argv[])
{
    if(strlen(argv[1]) > 256)
      printf("Input out of size.");
   else
      function(argv[1]);
}

