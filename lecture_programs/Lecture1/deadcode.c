#include <stdio.h>
#include <string.h>

void main(int argc, char** argv)
{
    getData();
    return;
}

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

