//gcc execve64.c -o execve64 -fno-stack-protector -no-pie -mpreferred-stack-boundary=4 -fno-pic

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

