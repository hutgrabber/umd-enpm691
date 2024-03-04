//gcc -m32 basicPrintf3.c -o basicPrintf3 -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <stdio.h>

int main()
{
    int i = 2;
    printf("%d\n",i);

    return 0;
}

