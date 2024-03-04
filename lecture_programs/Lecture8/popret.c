// gcc -m32 popret.c -o popret -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -z execstack

#include <stdio.h>

#include <string.h>

void function(int x, char* str)
{
  char buffer[4];
  strcpy(buffer, str);
}

int main(int argc, char** argv)
{
   function(10, argv[1]);
   return 1;
}

