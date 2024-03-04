//gcc -m32 execve.c -o execve -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <unistd.h>
#include <stdlib.h>

int main()
{
   char* args[2];

   args[0] = "/bin/bash";
   args[1] = NULL;

   execve(args[0], args, NULL);
   exit(0);
}

