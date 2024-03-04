//gcc -m32 directPrintf.c -o directPrintf -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <stdio.h>

int main()
{
    int j = 4;
    int i = 2;
    printf("i=%2$d, j=%1$d",j,i);

    return 0;
}

