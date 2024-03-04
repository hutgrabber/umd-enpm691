//gcc -m32 basicPrintf4.c -o basicPrintf4 -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <stdio.h>

int main()
{
    int j = 4;
    int i = 2;
    printf("%d%d");

    return 0;
}

