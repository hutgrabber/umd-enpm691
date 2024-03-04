//gcc deadcode64.c -o deadcode64 -fno-stack-protector -no-pie -mpreferred-stack-boundary=4 -fno-pic -g 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void deadCode()
{
   printf("I'm alive!");
   exit(0);
}

void getData()
{
        char buffer[8];
        gets(buffer);
        puts(buffer);
}

void main(int argc, char** argv)
{
    getData();
    return;
}

