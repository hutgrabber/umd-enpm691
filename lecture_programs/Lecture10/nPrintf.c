//gcc -m32 nPrintf.c -o nPrintf -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <stdio.h>

int main()
{
    int count = 0;
    printf("Hello World%n",&count);
    printf("\n");
    printf("Count=%d\n",count);

    return 0;
}


