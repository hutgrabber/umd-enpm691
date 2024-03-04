//gcc -m32 basicPrintf.c -o basicPrintf -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic 

#include <stdio.h>

int main()
{
    int i = -1;
    printf("%u\n",i);
    printf("%x\n",i);
    printf("%d\n",i);
    printf("%c\n",i);

    return 0;
}

