//gcc printf64.c -o printf64 -fno-stack-protector -no-pie -mpreferred-stack-boundary=4 -fno-pic -g 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getData()
{
        char buffer[40];
        fgets(buffer, 40, stdin);
        printf(buffer);
}

void main(int argc, char** argv)
{
    getData();
    return;
}

